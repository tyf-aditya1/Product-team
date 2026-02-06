# ❓ Questions for Chandhar Singh (Delivery Manager)

Hi Chandhar,

I'm investigating the Zendesk/Yahoo delivery issue (NFIN-22562). To finalize the fix, I need clarification on a few infrastructure details:

1.  **Exact "From" Address**:
    *   When a user receives an email, does it say it came from `support@relyoncu.zendesk.com` OR `support@relyoncu.com`?
    *   *Why*: If it's the first one, this is a Zendesk IP issue. If it's the second (custom domain), we MUST add SPF/DKIM records to `relyoncu.com`.

2.  **Email Forwarding Setup**:
    *   Are emails forwarded to Zendesk from an Exchange/O365 server (e.g., User -> `help@relyoncu.com` -> Forward -> Zendesk)?
    *   *Why*: Forwarding often breaks SPF. If this is the case, we rely heavily on DKIM to fix the issue.

3.  **DNS Access**:
    *   Who manages the DNS records for this domain? Is it Tyfone IT or the Credit Union's IT team?
    *   *Why*: We will need to add TXT and CNAME records to resolve this.

Thanks,
Aditya
