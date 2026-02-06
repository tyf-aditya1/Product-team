# 🚨 Technical Incident Report: Zendesk → Yahoo Delivery Failure
**Ticket**: NFIN-22562 | **Date**: 2025-11-30 | **Author**: Aditya Raj

---

## 📌 Executive Summary
**Issue**: Support emails sent from Zendesk are failing to reach customers with Yahoo email addresses.
**Impact**: High severity. Affects RelyOnCU, Oregonians, and UBI.
**Root Cause**: Missing **SPF/DKIM authentication** records for the Credit Union's custom domain. Yahoo's 2024 policy update mandates these records; without them, emails are rejected as unauthorized.

---

## 🔍 Root Cause Analysis (RCA)

### **The Critical Variable: Sending Domain**
The ticket description states emails are sent from `support@relyoncu.zendesk.com`. This creates two distinct scenarios:

#### **Scenario A: They are using the default `support@relyoncu.zendesk.com`**
*   **Auth Responsibility**: **Zendesk**.
*   **Why it fails**:
    *   **Shared IP Reputation**: Zendesk's sending IP might be blacklisted by Yahoo.
    *   **DMARC Misalignment**: If the CU has a strict DMARC policy on `relyoncu.com` but the email comes from `zendesk.com` (unlikely to trigger unless "From" header is spoofed).
*   **Fix**: We cannot edit SPF for `zendesk.com`. We must contact Zendesk to rotate the IP.

#### **Scenario B: They are using a Custom Domain (`support@relyoncu.com`)**
*   *Note*: Users often say "Zendesk email" even if it's white-labeled.
*   **Auth Responsibility**: **The Credit Union**.
*   **Why it fails**: Missing SPF/DKIM records for `relyoncu.com`.
*   **Fix**: Add `include:mail.zendesk.com` to SPF and enable DKIM.

**Assessment**: Given the CU asked "Is there an SPF record we need to add?", it is highly probable they **intended** to use a custom domain or are in a hybrid state where headers are confusing Yahoo. **We must verify the actual "From" address configured in Zendesk Admin.**

### **1. The Core Failure: Authentication Mismatch**
*   **Observation**: Emails sent to `@yahoo.com` addresses are silently dropped or bounced.
*   **Trigger Event**: Yahoo and Gmail enforced stricter email authentication requirements in **February 2024**.
*   **Technical Gap**:
    *   When Zendesk sends an email as `support@relyoncu.com`, it uses Zendesk's IP addresses.
    *   Yahoo checks the **SPF Record** of `relyoncu.com` to see if Zendesk's IPs are authorized.
    *   **Current State**: The SPF record likely lacks `include:mail.zendesk.com`.
    *   **Result**: Yahoo sees an unauthorized IP sending email for the domain → **BLOCK**.

### **2. Contributing Factor: Header Modification (The "Intermediary")**
*   **Context**: Zendesk Support noted (in 2023) that incoming emails had modified "From" addresses (e.g., `user+longstring@yahoo.com`).
*   **Analysis**: This indicates an **auto-forwarding** setup (e.g., User → Exchange → Zendesk).
*   **Impact**: Forwarding often breaks SPF checks because the "sender" IP changes.
*   **Conclusion**: While forwarding complicates things, **DKIM (DomainKeys Identified Mail)** is designed to survive forwarding. If we enable DKIM, the digital signature remains valid even if the email is forwarded. **Thus, enabling DKIM is the primary fix for both issues.**

---

## 🛠️ Technical Solution & Implementation Plan

To permanently resolve this, we must implement the following DNS changes.

### **Phase 1: SPF Configuration (The "Allow List")**
We must authorize Zendesk to send emails on behalf of the domain.

*   **Action**: Update the domain's TXT record.
*   **Current (Hypothetical)**: `v=spf1 include:spf.protection.outlook.com ~all`
*   **Required Change**: Add `include:mail.zendesk.com`
*   **New Record**: `v=spf1 include:spf.protection.outlook.com include:mail.zendesk.com ~all`

### **Phase 2: DKIM Configuration (The "Digital Signature")**
We must digitally sign emails so Yahoo trusts them, even if they are forwarded.

*   **Action 1 (Zendesk)**: Generate DKIM keys in **Admin Center > Channels > Email > Domains**.
*   **Action 2 (DNS)**: Add the 2 CNAME records provided by Zendesk to the domain's DNS.
    *   *Example*: `zendesk1._domainkey.relyoncu.com` -> `zendesk1.zendesk.com`
*   **Action 3 (Zendesk)**: Click "Enable" after DNS propagation.

### **Phase 3: DMARC Alignment (The "Policy")**
Ensure DMARC does not block valid emails.

*   **Action**: Verify `_dmarc` record exists.
*   **Recommendation**: Set policy to `p=none` (monitor) or `p=quarantine` initially, moving to `p=reject` only after SPF/DKIM are confirmed working.

---

## 🧪 Verification & Testing Strategy

Once DNS changes are made, we will validate using the following method:

1.  **Send Test Email**: Reply to a ticket from a test Yahoo account (`tyfonetesting@yahoo.com`).
2.  **Analyze Headers**: In the received email at Yahoo, view "Raw Message".
3.  **Success Criteria**:
    *   `Authentication-Results: yahoo.com; spf=pass ... dkim=pass`
    *   Email lands in **Inbox** (not Spam).

---

## 📚 References
*   [Zendesk: Google & Yahoo's Updated Sending Requirements](https://support.zendesk.com/hc/en-us/articles/6665707939482)
*   [Zendesk: Troubleshooting Email Deliverability](https://support.zendesk.com/hc/en-us/articles/4408834888730-Troubleshooting-email-deliverability)
