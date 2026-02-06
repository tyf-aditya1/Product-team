#!/usr/bin/env python3
"""
Jira Ticket Downloader
Downloads complete ticket information including description, fields, comments, attachments, and subtasks.
"""

import os
import sys
import json
import base64
import re
import requests
from datetime import datetime


def load_env():
    """Load configuration from .env file."""
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if not os.path.exists(env_path):
        print(f"Error: .env file not found at {env_path}")
        sys.exit(1)

    config = {}
    with open(env_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip()
    return config


def get_auth_headers(config):
    """Create authentication headers for Jira API."""
    auth_str = f"{config['JIRA_EMAIL']}:{config['JIRA_API_TOKEN']}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()
    return {
        "Authorization": f"Basic {b64_auth}",
        "Accept": "application/json"
    }


def clean_filename(filename):
    """Remove invalid characters from filename."""
    return re.sub(r'[\\/*?:"<>|]', "_", filename)


def extract_adf_text(adf_content):
    """Extract plain text from Atlassian Document Format (ADF)."""
    if adf_content is None:
        return ""
    if isinstance(adf_content, str):
        return adf_content

    texts = []

    def extract_from_node(node):
        if isinstance(node, dict):
            if 'text' in node:
                texts.append(node['text'])
            if 'content' in node:
                for child in node['content']:
                    extract_from_node(child)
        elif isinstance(node, list):
            for item in node:
                extract_from_node(item)

    extract_from_node(adf_content)
    return '\n'.join(texts)


def extract_media_from_adf(adf_content):
    """Extract media references (attachments) from ADF content."""
    media_refs = []

    if adf_content is None or isinstance(adf_content, str):
        return media_refs

    def extract_from_node(node):
        if isinstance(node, dict):
            # Check for media nodes (inline attachments)
            if node.get('type') == 'media':
                attrs = node.get('attrs', {})
                media_refs.append({
                    'type': 'media',
                    'id': attrs.get('id'),
                    'alt': attrs.get('alt'),
                    'media_type': attrs.get('type')
                })
            # Check for inlineCard (links to Jira issues, Confluence, etc.)
            if node.get('type') == 'inlineCard':
                attrs = node.get('attrs', {})
                if 'url' in attrs:
                    media_refs.append({
                        'type': 'link',
                        'url': attrs.get('url')
                    })
            # Check for links in text marks
            if 'marks' in node:
                for mark in node.get('marks', []):
                    if mark.get('type') == 'link':
                        href = mark.get('attrs', {}).get('href')
                        if href:
                            media_refs.append({
                                'type': 'link',
                                'url': href,
                                'text': node.get('text', '')
                            })
            if 'content' in node:
                for child in node['content']:
                    extract_from_node(child)
        elif isinstance(node, list):
            for item in node:
                extract_from_node(item)

    extract_from_node(adf_content)
    return media_refs


def extract_links_from_comments(comments):
    """Extract all links and media references from comments."""
    all_links = []
    for i, comment in enumerate(comments):
        body = comment.get('body')
        media_refs = extract_media_from_adf(body)
        for ref in media_refs:
            ref['comment_index'] = i + 1
            ref['comment_author'] = comment.get('author', {}).get('displayName', 'Unknown')
            ref['source'] = 'comment'
            all_links.append(ref)
    return all_links


def extract_links_from_description(description):
    """Extract all links from the description field."""
    all_links = []
    media_refs = extract_media_from_adf(description)
    for ref in media_refs:
        ref['source'] = 'description'
        ref['comment_index'] = 'desc'
        all_links.append(ref)
    return all_links


def extract_links_from_fields(fields, names):
    """Extract URL links from all field values."""
    import re
    all_links = []
    url_pattern = re.compile(r'https?://[^\s<>"\']+')

    skip_fields = {'self', 'id', 'key', 'description', 'comment', 'attachment'}

    for field_id, field_value in fields.items():
        if field_id in skip_fields:
            continue

        # Convert field value to string for URL extraction
        if field_value is None:
            continue

        field_str = ""
        if isinstance(field_value, str):
            field_str = field_value
        elif isinstance(field_value, dict):
            field_str = json.dumps(field_value)
        elif isinstance(field_value, list):
            field_str = json.dumps(field_value)

        # Find URLs in the field value
        urls = url_pattern.findall(field_str)
        for url in urls:
            # Skip Jira API URLs
            if '/rest/api/' in url or 'atlassian.net/rest/' in url:
                continue
            # Skip image URLs from Jira
            if '/images/icons/' in url:
                continue
            # Skip avatar URLs
            if 'avatar' in url.lower() or 'atl-paas.net' in url:
                continue
            # Skip Jira internal URLs
            if 'atlassian.net' in url and ('browse' not in url and 'wiki' not in url):
                continue

            field_name = names.get(field_id, field_id)
            all_links.append({
                'type': 'link',
                'url': url.rstrip('.,;:)'),
                'text': url.rstrip('.,;:)'),
                'source': 'field',
                'field_name': field_name,
                'comment_index': field_name
            })

    return all_links


def fetch_issue(jira_domain, ticket_id, headers):
    """Fetch issue data from Jira API with all fields and changelog."""
    url = f"{jira_domain}/rest/api/3/issue/{ticket_id}"
    params = {
        "expand": "changelog,renderedFields,names,schema"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error fetching {ticket_id}: {response.status_code}")
        print(response.text)
        return None

    return response.json()


def fetch_comments(jira_domain, ticket_id, headers):
    """Fetch all comments for a ticket (handles pagination)."""
    comments = []
    start_at = 0
    max_results = 100

    while True:
        url = f"{jira_domain}/rest/api/3/issue/{ticket_id}/comment"
        params = {"startAt": start_at, "maxResults": max_results, "orderBy": "created"}

        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Error fetching comments: {response.status_code}")
            break

        data = response.json()
        comments.extend(data.get('comments', []))

        if start_at + max_results >= data.get('total', 0):
            break
        start_at += max_results

    return comments


def download_attachments(attachments, ticket_dir, headers):
    """Download all attachments to the ticket directory."""
    attachments_dir = os.path.join(ticket_dir, 'attachments')
    os.makedirs(attachments_dir, exist_ok=True)

    downloaded = []
    for attachment in attachments:
        filename = clean_filename(attachment['filename'])
        content_url = attachment['content']
        file_path = os.path.join(attachments_dir, filename)

        print(f"  Downloading: {filename}")
        try:
            response = requests.get(content_url, headers=headers, stream=True)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                downloaded.append({
                    'filename': filename,
                    'size': attachment.get('size', 0),
                    'author': attachment.get('author', {}).get('displayName', 'Unknown'),
                    'created': attachment.get('created', ''),
                    'id': attachment.get('id', '')
                })
            else:
                print(f"    Failed: {response.status_code}")
        except Exception as e:
            print(f"    Error: {str(e)}")

    return downloaded


def get_google_doc_export_url(url):
    """Convert Google Docs/Sheets/Slides URL to PDF export URL."""
    import re

    # Google Docs
    match = re.search(r'docs\.google\.com/document/d/([a-zA-Z0-9_-]+)', url)
    if match:
        doc_id = match.group(1)
        return f"https://docs.google.com/document/d/{doc_id}/export?format=pdf", f"google_doc_{doc_id[:8]}.pdf"

    # Google Sheets
    match = re.search(r'docs\.google\.com/spreadsheets/d/([a-zA-Z0-9_-]+)', url)
    if match:
        doc_id = match.group(1)
        return f"https://docs.google.com/spreadsheets/d/{doc_id}/export?format=pdf", f"google_sheet_{doc_id[:8]}.pdf"

    # Google Slides
    match = re.search(r'docs\.google\.com/presentation/d/([a-zA-Z0-9_-]+)', url)
    if match:
        doc_id = match.group(1)
        return f"https://docs.google.com/presentation/d/{doc_id}/export/pdf", f"google_slides_{doc_id[:8]}.pdf"

    return None, None


def download_linked_files(links, ticket_dir, headers, jira_domain):
    """Download files from links found in comments and description."""
    attachments_dir = os.path.join(ticket_dir, 'attachments')
    os.makedirs(attachments_dir, exist_ok=True)

    downloaded = []
    failed_downloads = []
    seen_urls = set()

    for link in links:
        if link.get('type') != 'link':
            continue

        url = link.get('url', '')
        if not url or url in seen_urls:
            continue
        seen_urls.add(url)

        # Check for Google Docs/Sheets/Slides - try to export as PDF
        if 'docs.google.com' in url:
            export_url, filename = get_google_doc_export_url(url)
            if export_url:
                file_path = os.path.join(attachments_dir, filename)
                if os.path.exists(file_path):
                    continue

                source = link.get('source', 'comment')
                source_idx = link.get('comment_index', '?')
                print(f"  Downloading Google Doc: {filename} (from {source} {source_idx})")
                try:
                    response = requests.get(export_url, stream=True, allow_redirects=True, timeout=30)
                    if response.status_code == 200:
                        with open(file_path, 'wb') as f:
                            for chunk in response.iter_content(chunk_size=8192):
                                f.write(chunk)
                        downloaded.append({
                            'filename': filename,
                            'url': url,
                            'comment_index': link.get('comment_index'),
                            'comment_author': link.get('comment_author', 'Unknown'),
                            'source': source
                        })
                    else:
                        print(f"    Failed (may require auth): {response.status_code}")
                        failed_downloads.append({'url': url, 'reason': 'Auth required'})
                except Exception as e:
                    print(f"    Error: {str(e)}")
                    failed_downloads.append({'url': url, 'reason': str(e)})
            continue

        # Check if it's a Jira attachment URL
        if '/attachment/' in url or '/secure/attachment/' in url:
            try:
                # Try to extract filename from URL or use a generic name
                url_parts = url.split('/')
                filename = url_parts[-1] if url_parts else 'attachment'
                filename = clean_filename(filename)

                # Remove query params from filename
                if '?' in filename:
                    filename = filename.split('?')[0]

                file_path = os.path.join(attachments_dir, filename)

                # Skip if already downloaded
                if os.path.exists(file_path):
                    continue

                print(f"  Downloading linked: {filename} (from comment {link.get('comment_index', '?')})")
                response = requests.get(url, headers=headers, stream=True, allow_redirects=True)
                if response.status_code == 200:
                    with open(file_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    downloaded.append({
                        'filename': filename,
                        'url': url,
                        'comment_index': link.get('comment_index'),
                        'comment_author': link.get('comment_author')
                    })
                else:
                    print(f"    Failed: {response.status_code}")
            except Exception as e:
                print(f"    Error downloading {url}: {str(e)}")

        # Check for downloadable file extensions in other URLs
        elif any(ext in url.lower() for ext in ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.png', '.jpg', '.jpeg', '.gif', '.zip', '.csv']):
            try:
                url_parts = url.split('/')
                filename = url_parts[-1] if url_parts else 'file'
                filename = clean_filename(filename)
                if '?' in filename:
                    filename = filename.split('?')[0]

                file_path = os.path.join(attachments_dir, filename)

                if os.path.exists(file_path):
                    continue

                print(f"  Downloading external: {filename} (from comment {link.get('comment_index', '?')})")
                # For external URLs, don't use Jira auth headers
                response = requests.get(url, stream=True, allow_redirects=True, timeout=30)
                if response.status_code == 200:
                    with open(file_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    downloaded.append({
                        'filename': filename,
                        'url': url,
                        'comment_index': link.get('comment_index'),
                        'comment_author': link.get('comment_author'),
                        'external': True
                    })
            except Exception as e:
                print(f"    Error downloading {url}: {str(e)}")

    return downloaded


def fetch_subtasks(jira_domain, subtasks, headers):
    """Fetch full details for all subtasks."""
    subtask_details = []
    for subtask in subtasks:
        subtask_key = subtask['key']
        print(f"  Fetching subtask: {subtask_key}")
        data = fetch_issue(jira_domain, subtask_key, headers)
        if data:
            subtask_details.append(data)
    return subtask_details


def format_field_value(field_name, field_value, field_schema=None):
    """Format a field value for display."""
    if field_value is None:
        return "None"

    if isinstance(field_value, dict):
        # Handle common field types
        if 'displayName' in field_value:
            return field_value['displayName']
        if 'name' in field_value:
            return field_value['name']
        if 'value' in field_value:
            return field_value['value']
        if 'content' in field_value:
            return extract_adf_text(field_value)
        return json.dumps(field_value, indent=2)

    if isinstance(field_value, list):
        items = []
        for item in field_value:
            if isinstance(item, dict):
                if 'displayName' in item:
                    items.append(item['displayName'])
                elif 'name' in item:
                    items.append(item['name'])
                elif 'value' in item:
                    items.append(item['value'])
                else:
                    items.append(json.dumps(item))
            else:
                items.append(str(item))
        return ', '.join(items) if items else "None"

    return str(field_value)


def create_ticket_output(data, comments, downloaded_attachments, subtask_details, jira_domain, ticket_dir, comment_links=None):
    """Create output files for the ticket."""
    fields = data.get('fields', {})
    names = data.get('names', {})
    comment_links = comment_links or []

    # Save raw JSON
    with open(os.path.join(ticket_dir, 'raw_data.json'), 'w', encoding='utf-8') as f:
        json.dump({
            'issue': data,
            'comments': comments,
            'subtasks': subtask_details
        }, f, indent=2)

    # Create readable summary
    ticket_id = data.get('key', 'UNKNOWN')
    summary = fields.get('summary', 'No Summary')

    output_lines = []
    output_lines.append(f"# {ticket_id}: {summary}")
    output_lines.append("")
    output_lines.append(f"**Jira Link:** {jira_domain}/browse/{ticket_id}")
    output_lines.append(f"**Downloaded:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output_lines.append("")

    # Key Fields Section
    output_lines.append("## Key Information")
    output_lines.append("")

    key_fields = ['status', 'priority', 'assignee', 'reporter', 'created', 'updated',
                  'duedate', 'resolution', 'issuetype', 'project', 'labels', 'components']

    for field_id in key_fields:
        if field_id in fields:
            field_name = names.get(field_id, field_id)
            value = format_field_value(field_id, fields[field_id])
            output_lines.append(f"- **{field_name}:** {value}")

    output_lines.append("")

    # Description Section
    output_lines.append("## Description")
    output_lines.append("")
    description = extract_adf_text(fields.get('description'))
    output_lines.append(description if description else "_No description_")
    output_lines.append("")

    # All Fields Section
    output_lines.append("## All Fields")
    output_lines.append("")

    # Skip internal/system fields and already displayed key fields
    skip_fields = {'self', 'id', 'key', 'description', 'comment', 'attachment', 'subtasks',
                   'worklog', 'watches', 'votes', 'aggregateprogress', 'progress', 'timetracking',
                   'workratio', 'issuerestriction', 'parent'}
    skip_fields.update(key_fields)

    for field_id, field_value in sorted(fields.items()):
        if field_id in skip_fields or field_value is None:
            continue
        if field_id.startswith('customfield_') and field_value is None:
            continue

        field_name = names.get(field_id, field_id)
        value = format_field_value(field_id, field_value)
        if value and value != "None" and value != "[]" and value != "{}":
            output_lines.append(f"- **{field_name}:** {value}")

    output_lines.append("")

    # Attachments Section
    output_lines.append("## Attachments")
    output_lines.append("")
    if downloaded_attachments:
        for att in downloaded_attachments:
            size_kb = att.get('size', 0) / 1024
            source = ""
            if att.get('from_comment'):
                source = f" *(from comment)*"
            output_lines.append(f"- [{att['filename']}](attachments/{att['filename']}) ({size_kb:.1f} KB) - by {att['author']}{source}")
    else:
        output_lines.append("_No attachments_")
    output_lines.append("")

    # Links Found Section
    if comment_links:
        output_lines.append("## Links")
        output_lines.append("")
        seen_urls = set()
        for link in comment_links:
            if link.get('type') == 'link':
                url = link.get('url', '')
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    text = link.get('text', '') or url
                    source = link.get('source', 'comment')
                    source_idx = link.get('comment_index', '?')
                    if source == 'description':
                        source_text = "description"
                    else:
                        source_text = f"comment {source_idx}"
                    output_lines.append(f"- [{text}]({url}) *(from {source_text})*")
        output_lines.append("")

    # Comments Section
    output_lines.append("## Comments")
    output_lines.append("")
    if comments:
        for i, comment in enumerate(comments, 1):
            author = comment.get('author', {}).get('displayName', 'Unknown')
            created = comment.get('created', '')[:19].replace('T', ' ')
            body = extract_adf_text(comment.get('body'))

            output_lines.append(f"### Comment {i} - {author} ({created})")
            output_lines.append("")
            output_lines.append(body)
            output_lines.append("")
    else:
        output_lines.append("_No comments_")
    output_lines.append("")

    # Subtasks Section
    output_lines.append("## Subtasks")
    output_lines.append("")
    if subtask_details:
        for subtask in subtask_details:
            st_key = subtask.get('key')
            st_fields = subtask.get('fields', {})
            st_summary = st_fields.get('summary', 'No Summary')
            st_status = st_fields.get('status', {}).get('name', 'Unknown')
            st_assignee = st_fields.get('assignee', {})
            st_assignee_name = st_assignee.get('displayName', 'Unassigned') if st_assignee else 'Unassigned'

            output_lines.append(f"### {st_key}: {st_summary}")
            output_lines.append(f"- **Status:** {st_status}")
            output_lines.append(f"- **Assignee:** {st_assignee_name}")

            st_description = extract_adf_text(st_fields.get('description'))
            if st_description:
                output_lines.append(f"- **Description:** {st_description[:200]}...")
            output_lines.append("")
    else:
        output_lines.append("_No subtasks_")

    # Write README.md
    with open(os.path.join(ticket_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))


def main():
    if len(sys.argv) < 2:
        print("Usage: python download_ticket.py <TICKET_ID>")
        print("Example: python download_ticket.py PROD-542")
        sys.exit(1)

    ticket_id = sys.argv[1].upper()

    config = load_env()
    jira_domain = config.get('JIRA_DOMAIN', '').rstrip('/')
    headers = get_auth_headers(config)

    print(f"\n{'='*50}")
    print(f"Downloading: {ticket_id}")
    print(f"{'='*50}")

    # Create ticket directory and subdirectories
    ticket_dir = os.path.join(os.path.dirname(__file__), 'tickets', ticket_id)
    os.makedirs(ticket_dir, exist_ok=True)
    os.makedirs(os.path.join(ticket_dir, 'attachments'), exist_ok=True)
    os.makedirs(os.path.join(ticket_dir, 'transcript'), exist_ok=True)
    os.makedirs(os.path.join(ticket_dir, 'notes'), exist_ok=True)

    # Create notes.md if it doesn't exist
    notes_file = os.path.join(ticket_dir, 'notes', 'notes.md')
    if not os.path.exists(notes_file):
        with open(notes_file, 'w') as f:
            f.write(f"# Notes for {ticket_id}\n\n")
            f.write("## Investigation Notes\n\n")
            f.write("_Add your notes here..._\n\n")
            f.write("## Action Items\n\n")
            f.write("- [ ] \n\n")
            f.write("## Resolution\n\n")
            f.write("_Document the resolution here..._\n")

    # Fetch main issue
    print("\n[1/5] Fetching issue details...")
    data = fetch_issue(jira_domain, ticket_id, headers)
    if not data:
        sys.exit(1)

    fields = data.get('fields', {})

    # Fetch all comments
    print("\n[2/5] Fetching comments...")
    comments = fetch_comments(jira_domain, ticket_id, headers)
    print(f"  Found {len(comments)} comments")

    # Download attachments
    print("\n[3/5] Downloading attachments...")
    attachments = fields.get('attachment', [])
    downloaded_attachments = []
    if attachments:
        downloaded_attachments = download_attachments(attachments, ticket_dir, headers)
        print(f"  Downloaded {len(downloaded_attachments)} attachments")
    else:
        print("  No attachments found")

    # Extract and download linked files from description, fields, and comments
    print("\n[4/5] Checking for linked files...")

    # Get links from description
    description_links = extract_links_from_description(fields.get('description'))
    if description_links:
        print(f"  Found {len(description_links)} links in description")

    # Get links from custom fields
    names = data.get('names', {})
    field_links = extract_links_from_fields(fields, names)
    if field_links:
        print(f"  Found {len(field_links)} links in fields")

    # Get links from comments
    comment_links = extract_links_from_comments(comments)
    if comment_links:
        print(f"  Found {len(comment_links)} links in comments")

    # Merge all links
    all_links = description_links + field_links + comment_links
    linked_downloads = []
    if all_links:
        linked_downloads = download_linked_files(all_links, ticket_dir, headers, jira_domain)
        if linked_downloads:
            print(f"  Downloaded {len(linked_downloads)} files from links")
    else:
        print("  No linked files found")

    # Keep all_links for README output
    comment_links = all_links

    # Merge linked downloads into attachments list
    for ld in linked_downloads:
        if not any(a['filename'] == ld['filename'] for a in downloaded_attachments):
            downloaded_attachments.append({
                'filename': ld['filename'],
                'size': 0,
                'author': ld.get('comment_author', 'Unknown'),
                'created': f"From comment {ld.get('comment_index', '?')}",
                'from_comment': True
            })

    # Fetch subtasks
    print("\n[5/5] Fetching subtasks...")
    subtasks = fields.get('subtasks', [])
    subtask_details = []
    if subtasks:
        subtask_details = fetch_subtasks(jira_domain, subtasks, headers)
        print(f"  Found {len(subtask_details)} subtasks")
    else:
        print("  No subtasks found")

    # Create output files
    print("\nCreating output files...")
    create_ticket_output(data, comments, downloaded_attachments, subtask_details, jira_domain, ticket_dir, comment_links)

    print(f"\n{'='*50}")
    print(f"SUCCESS! Ticket saved to: tickets/{ticket_id}/")
    print(f"{'='*50}")
    print(f"  - README.md       (Human-readable summary)")
    print(f"  - raw_data.json   (Complete JSON data)")
    print(f"  - attachments/    (Downloaded files)")
    print(f"  - transcript/     (Paste conversation transcripts here)")
    print(f"  - notes/          (Your investigation notes)")
    print("")


if __name__ == "__main__":
    main()
