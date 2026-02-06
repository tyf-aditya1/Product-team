# 🎙️ KT Meeting: Zendesk Identity Migration (NFIN-22562)

## 📋 Executive Brief for Engineer
"We are facing a critical production issue where **Yahoo and AOL users are not receiving support emails from Zendesk**. 

**The Root Cause**: Our system currently sends user emails in the format `user+ID@yahoo.com` to ensure uniqueness in Zendesk. While Gmail supports this, Yahoo/AOL treat these as 'User Not Found' and bounce them with a 552 error.

**The Solution**: We need to move away from using the `email` field as our Primary Key. Instead, we want to:
1.  Use the clean email (`user@yahoo.com`) for communication.
2.  Use the Zendesk **`external_id`** field to store our unique identifier.

**Goal of this KT**: I need to understand the current code flow from ticket creation to delivery so I can draft the requirements for a logic change and a clean data migration of existing users."

---

## 🏗️ Phase 1: Origination & Code Flow (The "As-Is")
*Asking 'How does it work today?' to verify our assumptions.*

1.  **The Entry Point**:
    *   "Can you show me the exact code/service that triggers the ticket creation in Zendesk?"
    *   *Follow-up*: "Is this a direct REST API call (`POST /api/v2/tickets`) or are we constructing an email and sending it via SMTP?"
2.  **The Identifier Logic**:
    *   "Where do we construct the `user+ID@domain.com` string?"
    *   **CRITICAL**: "Is the `ID` part the **Raw User ID** from our database, or is it a Hash/Encoded value?" (We need to know this to reverse it).
3.  **The Trigger**:
    *   "Does this flow happen *only* when a user submits a form in Digital Banking, or does it also happen for emails sent to `support@`?"

## 🛠️ Part 2: Validate the "To-Be" Solution
*Asking 'Will this break anything?'*

4.  **External ID Feasibility**:
    *   "Does our current integration logic support sending the `external_id` field in the JSON payload?"
    *   "If we start sending `external_id`, do we need to make any changes to how the Digital Banking app *reads* tickets back?" (e.g., does the app look up tickets by email or by ID?)
5.  **Clean Email**:
    *   "If we strip the `+ID` and send just `user@yahoo.com` in the email field, is there any downstream system (Reporting, Data Warehouse) that relies on that `+ID` format?"

## 🔄 Part 3: The Migration Path (The Hard User)
*Asking 'How do we fix 10,000 existing users without downtime?'*

6.  **Data Cleanup**:
    *   "Do we have a script or job that can iterate through all Zendesk users?"
    *   "How should we handle **Duplicates**? (e.g., if `user+123@yahoo.com` exists AND `user@yahoo.com` (clean) already exists as a separate user – do we merge them?)"
7.  **Environment**:
    *   "Do we have a **Sandbox/Staging** Zendesk instance where we can dry-run the migration script first?"

## 📝 Request for Access/Resources
*   "Can I get a link to the Repo/File where the Ticket Creation logic lives?"
*   "Can we get API Access to the Sandbox environment?"

---

## 🧠 Context for You (The PM) to Keep in Mind
*   **Origination**: The exact moment the user hits "Submit" in the app.
*   **Delivery**: The moment Zendesk sends the "Request Received" email back.
*   **The Gap**: Currently, Origination adds `+ID`, causing Delivery to fail for Yahoo.
