# 📧 Email Delivery Journey & Failure Analysis
**Ticket**: NFIN-22562 | **Issue**: Zendesk → Yahoo Delivery Failure

This document maps the complete technical journey of an email from Zendesk to a Yahoo inbox, identifying critical failure points to guide the resolution team.

---

## 🗺️ The Complete Journey: Zendesk → Yahoo Inbox

### **Phase 1: Creation & Processing (Internal)**
1.  **Stage 1: Composition & Trigger**
    -   **Action**: User/Agent triggers an email (e.g., ticket response).
    -   **Zendesk**: Generates email from template.
    -   **Headers Set**: `From: support@relyoncu.zendesk.com` (or custom domain), `Reply-To`.
2.  **Stage 2: Processing**
    -   **Zendesk Server**: Adds tracking pixels/links.
    -   **Queueing**: Message placed in outbound mail queue.
3.  **Stage 3: Handoff to MTA**
    -   **Action**: Message moves to Zendesk's Mail Transfer Agent (MTA).
    -   **Signing**: Zendesk signs with DKIM (using their keys).
    -   **Routing**: Assigned to a shared sending IP.

### **Phase 2: Transmission (The Internet)**
4.  **Stage 4: DNS Lookup**
    -   **Zendesk MTA**: Queries DNS for Yahoo's MX records.
    -   **Result**: Resolves to `mta5.am0.yahoodns.net` (etc.).
5.  **Stage 5: Connection**
    -   **Action**: Zendesk initiates SMTP connection (Port 25) to Yahoo.
    -   **Handshake**: TLS negotiation (STARTTLS).
    -   **Yahoo Check**: Is this IP blacklisted/greylisted?
6.  **Stage 6: SMTP Transaction**
    -   **Zendesk**: `MAIL FROM:<bounces@relyoncu.zendesk.com>`
    -   **Zendesk**: `RCPT TO:<user@yahoo.com>`
    -   **Yahoo**: Validates recipient exists.
    -   **Zendesk**: `DATA` (sends body).

### **Phase 3: Reception & Filtering (Yahoo's Gate)**
7.  **Stage 7: Reception Gateway**
    -   **Action**: Yahoo receives the full message.
    -   **Check**: Initial reputation check on sending IP.
8.  **Stage 8: Authentication Checks (🔴 CRITICAL FAILURE POINT)**
    -   **SPF Check**: Yahoo queries DNS for `relyoncu.zendesk.com` (or custom domain).
        -   *Question*: Is Zendesk's IP authorized to send for this domain?
    -   **DKIM Check**: Validates cryptographic signature.
        -   *Question*: Does the signature match the public key in DNS?
    -   **DMARC Check**: Queries `_dmarc.relyoncu.zendesk.com`.
        -   *Question*: Do SPF/DKIM align? What is the policy (`p=reject`)?
9.  **Stage 9: Content Filtering**
    -   **Action**: Spam score calculation (Bayesian filters).
    -   **Checks**: Link analysis (blocklists), attachment scanning.

### **Phase 4: Decision & Delivery**
10. **Stage 10: Reputation Analysis (🟡 HIGH RISK)**
    -   **Domain Reputation**: Is `relyoncu.zendesk.com` trusted?
    -   **IP Reputation**: Is the shared Zendesk IP spammy?
    -   **Engagement**: Do users usually delete these emails?
11. **Stage 11: Final Disposition**
    -   **Decision**: Inbox / Spam / Reject / Drop.
    -   **Outcome**:
        -   *Reject*: 5xx error sent back to Zendesk.
        -   *Accept*: Queued for delivery.
12. **Stage 12: Mailbox Delivery**
    -   **Action**: Placed in user's folder (Inbox vs Spam).
13. **Stage 13: User Access**
    -   **Action**: User sees (or doesn't see) the email.

---

## 🔍 Failure Point Analysis for NFIN-22562

### **🔴 Stage 8: Authentication Checks (Most Likely)**
This is the primary suspect given Yahoo's strict 2024 requirements.
-   **SPF Failure**:
    -   *Scenario*: Your SPF record is missing `include:mail.zendesk.com`.
    -   *Result*: Yahoo sees an unauthorized IP → **SPF FAIL** → Rejects/Junks.
-   **DMARC Enforcement**:
    -   *Scenario*: You have `p=reject` policy, and SPF/DKIM fail.
    -   *Result*: Yahoo **must** reject the email per your policy.

### **🟡 Stage 10: Reputation Analysis (Very Likely)**
-   **Shared IP Issues**:
    -   *Scenario*: Other Zendesk customers spammed from the same shared IP.
    -   *Result*: Yahoo silently drops the email or sends to Spam based on IP reputation.
-   **Header Modification**:
    -   *Scenario*: As noted in the ticket, the "From" address is modified (`+longstring`).
    -   *Result*: Yahoo's heuristic filters flag this as suspicious/spoofed.

### **🟠 Stage 7: Reception Gateway (Possible)**
-   **IP Blocking**:
    -   *Scenario*: Yahoo throttles Zendesk's IP range due to volume.
    -   *Result*: Connection rejected (4xx/5xx error) before auth checks.

---

## 🛠️ Diagnostic Steps for the Team

To pinpoint the exact failure stage, perform these checks:

### **1. Check Zendesk Delivery Logs**
Look for the specific SMTP error code in Zendesk:
-   **550 5.7.1 SPF unauthorized**: Confirms **Stage 8 (SPF)** failure.
-   **554 5.7.1 DMARC policy**: Confirms **Stage 8 (DMARC)** failure.
-   **421 4.7.0 Try again later**: Confirms **Stage 7 (Throttling)**.
-   **No Error (Delivered)**: Confirms **Stage 10/11 (Reputation/Spam Folder)**.

### **2. Send Test Email & Analyze Headers**
Send a ticket response to a controlled Yahoo account and view raw headers:
-   Look for `Authentication-Results: yahoo.com;`
    -   `spf=fail`? → Fix SPF record.
    -   `dkim=fail`? → Fix DKIM keys.
    -   `dmarc=fail`? → Fix alignment.

### **3. External Validation**
-   Use **mail-tester.com** to check the "Spam Score" of Zendesk emails.
-   Use **mxtoolbox.com** to check the reputation of the sending domain/IP.
