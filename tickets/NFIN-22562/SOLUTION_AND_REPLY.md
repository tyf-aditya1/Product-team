# ✅ Final Solution: NFIN-22562 (Zendesk/Yahoo Delivery)

## 🎯 The Diagnosis
The issue is **not** with Zendesk's outbound delivery configuration (SPF/DKIM), but with the **Inbound Forwarding** setup at the Credit Union.

### **Evidence**
The bounce screenshot shows Zendesk attempting to reply to:
`tootskahrm+zw1iaetzblvowed2wwtvujbcdmfjut09@aol.com`

### **Root Cause**
1.  **Forwarding Rewriting**: When the Credit Union's mail server forwards emails to `support@ubifcu.zendesk.com`, it is **rewriting the "Reply-To" address** to include a tracking string (SRS or similar).
2.  **Rejection**: AOL and Yahoo reject emails sent to these modified `+long_string` addresses as they look like spam/bots. Gmail accepts them, which is why Gmail users are unaffected.

---

## 📨 The Reply to Send (Copy & Paste)

**To**: Jonathan Zulkeski (UBIFCU), Sreelekshmi VH, Donald Montenegro

**Subject**: RE: Yahoo/AOL Delivery Failure - Root Cause Identified

Hi Team,

Thank you for the screenshots. They have confirmed the exact root cause.

**The Issue**:
The bounce message shows that Zendesk is trying to reply to a modified email address:
`tootskahrm+zw1iaetzblvowed2wwtvujbcdmfjut09@aol.com`

This `+long_string` is **not** being added by Zendesk. It is being passed to Zendesk by the **system creating the ticket** (likely the Digital Banking platform or the forwarding mail server).

**Why it fails**:
While Gmail supports these `+` tags, AOL and Yahoo often reject them (especially long, random ones) as invalid addresses or spam. This explains why only Yahoo/AOL users are affected.

**The Solution (Action for IT / Digital Banking Team)**:
We need to ensure that when a ticket is created, the **Requester Email** is passed as the clean address (`user@aol.com`) without the tracking string.

1.  **If via Email Forwarding**: Check the forwarding rule to ensure it doesn't rewrite the sender address.
2.  **If via Digital Banking API**: Check the API call creating the ticket. Ensure the `requester` field uses the user's standard email address. If the `+string` is needed for tracking, please store it in a **Custom Field** or the **Ticket Description**, not in the email address itself.

**Verification**:
Once this change is made, send a test email from a Yahoo account. It should arrive in Zendesk showing the clean email address (`user@yahoo.com`) without the `+` string. Replies will then work correctly.

Best,
Aditya
