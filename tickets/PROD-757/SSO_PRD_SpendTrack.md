# SSO Product Requirements Document (PRD)
## Fiserv SpendTrack (CardHub) Integration for Partners 1st FCU

**Document Version:** 1.0
**Date:** February 3, 2026
**Customer:** Partners 1st Federal Credit Union
**Integration Partner:** Fiserv
**Product:** Harmoney Business
**Product Area:** Card Management
**Release Target:** 10.51 | 02/2026

---

## 1. PROJECT BRIEF

### 1.1 Executive Summary
This document defines the requirements for implementing seamless Single Sign-On (SSO) integration between Tyfone's Harmoney Business digital banking platform and Fiserv SpendTrack (CardHub), enabling Partners 1st FCU business and commercial credit card users to access digital card management features without re-authentication.

### 1.2 Business Objective
Provide Partners 1st FCU commercial and small business customers with frictionless access to Fiserv SpendTrack card management capabilities directly from their Harmoney Business online banking and mobile applications, improving user experience and card program adoption.

### 1.3 Scope
- **User Segment:** Business Banking (Commercial & Small Business)
- **Card Type:** Credit Cards Only
- **Channels:**
  - Online Banking (Desktop/Responsive Web)
  - Mobile iOS
  - Mobile Android
- **Integration Type:** SAML-based SSO with JWT Token Exchange

### 1.4 Key Features
SpendTrack provides business cardholders and program administrators with:
- Real-time card transaction history and details
- Card controls and security settings
- Payment management and history
- Account statements
- Role-based access (Cardholder vs. Program Administrator)
- Self-service card activation
- Integration with uChoose Rewards (accessed within SpendTrack)

---

## 2. TYFONE CLASSIFICATION

### 2.1 Enrollment Type
**E3 - Automatic/Just-in-Time (JIT) Provisioning**

- No pre-enrollment required
- User provisioning occurs automatically upon first SSO invocation
- SpendTrack automatically assigns default "User" (Cardholder) role on first discovery
- Users can self-promote to Program Administrator role via workflow (subject to approval)

### 2.2 Feature Integration Type
**F2A - Iframe Integration (User-Triggered)**

- SpendTrack will be embedded within Harmoney Business using an iframe
- User explicitly clicks menu item, quick link, or Penni search result to launch
- Iframe displays SpendTrack application with full functionality
- Session maintained within iframe; logout redirects to specified returnURL

**Alternative Display Option (Pending FI Decision):**
**F1B - New Tab with External Link Warning**
- If iframe is not feasible due to technical constraints, SpendTrack can open in new browser tab
- External link warning popup must be displayed per Tyfone standards
- Warning includes: "You are leaving [FI Name] Digital Banking. Continue to external site?" with "Continue" and "Cancel" options

### 2.3 Reporting Type
**R2 - Vendor-Provided API/Export**

- SpendTrack usage analytics available through Fiserv reporting platform
- Tyfone Harmoney Admin logs SSO invocations, enrollment events, and error states
- Admin interface provides access to SSO request payload for troubleshooting

---

## 3. SOLUTION DESIGN

### 3.1 Authentication Flow

#### High-Level SSO Workflow
1. **User Authentication:** User logs into Harmoney Business (Online/Mobile)
2. **SpendTrack Access Initiated:** User selects SpendTrack from:
   - Main navigation menu (Business Card Management)
   - Quick Links widget
   - Penni AI search results
3. **SAML Assertion Generation:** Tyfone backend constructs SAML assertion with required attributes
4. **POST to Fiserv IDV Service:** Browser auto-submits SAML assertion to Fiserv Identity Verification (IDV) endpoint
5. **Certificate & Signature Validation:** Fiserv IDV validates certificate, signature, and required SAML attributes
6. **JWT Token Issuance:** Upon successful validation, Fiserv IDV returns HTTP redirect with JWT token
7. **SpendTrack Access:** Browser sends SSO request to SpendTrack with JWT token and user attributes
8. **User Validation & Dashboard Rendering:** SpendTrack validates External UserID and Company ID, then renders appropriate dashboard:
   - **Cardholder View:** For users with "User" role
   - **Program Administrator View:** For users with "Program Administrator" or "Reporting Administrator" roles
9. **Session Management:** User interacts with SpendTrack within iframe/tab; logout returns user to Harmoney Business

#### Technical Authentication Method
- **Protocol:** SAML 2.0 with JWT Token Exchange
- **Authentication Type:** Federated SSO via Fiserv eCS SSO Proxy
- **Token Lifetime:** 15 minutes (session timeout enforced by Fiserv)
- **Keep-Alive:** Optional keep-alive ping to maintain parent session while user is in SpendTrack

### 3.2 User Provisioning

#### New User Flow (First-Time Access)
1. User clicks SpendTrack link in Harmoney Business
2. Tyfone constructs SAML assertion with:
   - External User ID (Harmoney Business User ID)
   - Account ID (Credit card number or account number from core system)
   - Company ID (Fiserv Company ID associated with card)
   - Email address
3. Fiserv SpendTrack receives request and performs account/card lookup
4. If account/card exists in Fiserv system but no SpendTrack role assigned:
   - SpendTrack automatically creates user profile
   - Assigns default "User" (Cardholder) role
   - User must accept Terms & Conditions on first access
5. User lands on Cardholder dashboard

#### Existing User Flow (Subsequent Access)
1. User clicks SpendTrack link
2. Tyfone constructs SAML assertion (same attributes)
3. SpendTrack validates user and loads existing profile
4. User lands on dashboard based on assigned role:
   - **User Role:** Cardholder dashboard (single card/account view)
   - **Program Administrator Role:** Company-wide dashboard (all accounts and cards)
   - **Reporting Administrator Role:** View-only company dashboard

#### Role Management
- **Default Role:** All users automatically assigned "User" (Cardholder) role on first access
- **Self-Promotion to Program Administrator:**
  - Users can request promotion via SpendTrack self-registration workflow
  - Promotion requires approval (approval mechanism managed by Fiserv/FI)
  - Once approved, same External User ID will render Program Administrator dashboard
- **Role Assignment Outside SSO:** FI or Fiserv can manually assign Program Administrator or Reporting Administrator roles via backend configuration

### 3.3 SAML Assertion Attributes

Tyfone must include the following attributes in SAML assertion POST to Fiserv IDV endpoint:

| Attribute | Description | Required | Sample Value | Source |
|-----------|-------------|----------|--------------|--------|
| `cid` | Client Identifier (unique per FI) | Y | `AAAA6450001` | Provided by Fiserv (Partners 1st: `AAAA6450001`) |
| `appId` | Application Identifier (unique per FI) | Y | `partners-1st-fcu` | Provided by Fiserv (Partners 1st: `partners-1st-fcu`) |
| `externalUserID` | Harmoney Business User ID | Y | `user123456` | Tyfone User ID from session |
| `accountId` | Credit card number or account number | Y | `4017034000000309` | Retrieved from core system based on user's selected card/account |
| `companyID` | Fiserv Company ID | Y | `COMP123456` | Retrieved from core system or mapped from FI business account data |
| `emailAddress` | User's email address | Y | `jdoe@example.com` | Tyfone user profile |
| `returnURL` | URL to return user to Harmoney Business | Y | `https://[fi-domain]/banking/business/cards` | Tyfone-defined return URL |
| `logoutURL` | URL to redirect on SpendTrack logout | Y | `https://[fi-domain]/banking/logout` | Tyfone logout endpoint |
| `startURL` | Fiserv SSO Proxy endpoint | Y | See Environment URLs below | Environment-specific |

**Environment-Specific URLs:**

| Environment | `startURL` (SAML POST Endpoint) |
|-------------|--------------------------------|
| **CAT (Test/Stage)** | `https://cat1.fsdsapps.com/ecs-sso-proxy/sso/proxy/jwtproxy` |
| **Production** | `https://www.fsdsapps.com/ecs-sso-proxy/sso/proxy/jwtproxy` |

**Partners 1st Test Account Numbers (M Cycle):**
- `4017034000000309`
- `4017034000101024`
- `4017034000101032`

### 3.4 Security Requirements

#### IP Whitelisting
- **Tyfone Server IPs:** Must be whitelisted by Fiserv to POST SAML assertions to IDV endpoint
- **Action Required:** Tyfone to provide production and UAT server IP addresses to Fiserv during implementation

#### Certificate Management
- **SAML Signing Certificate:** Tyfone must provide X.509 certificate to Fiserv for SAML assertion signature validation
- **Certificate Rotation:** Tyfone must notify Fiserv 30 days prior to certificate expiration/rotation
- **Validation:** Fiserv IDV validates certificate validity and signature integrity on every SSO request

#### Data Transmission Security
- **Protocol:** HTTPS/TLS 1.2+ required for all communications
- **SAML Assertion:** Signed with Tyfone private key, validated by Fiserv using Tyfone public certificate
- **JWT Token:** Issued by Fiserv, short-lived (15-minute session timeout)

#### Session Management
- **Timeout:** 15 minutes of inactivity (enforced by Fiserv SpendTrack)
- **Timeout Behavior:**
  - **"Still Working" Option:** Keeps user on same page (session extended)
  - **"End Session" Option:** Redirects user to `logoutURL` defined in SAML assertion
- **Keep-Alive (Optional):** Tyfone may implement keep-alive ping to parent Harmoney session to prevent timeout while user is active in SpendTrack iframe

#### Error Handling
- **Invalid SAML Assertion:** Fiserv IDV returns error; user shown generic error message with support contact option
- **Missing Required Attributes:** SSO fails; Harmoney logs error details in Admin for troubleshooting
- **Account/Card Not Found:** SpendTrack displays error; user directed to contact FI support
- **Certificate Validation Failure:** SSO fails; Harmoney Admin logs payload and error state for debugging

---

## 4. ACCEPTANCE CRITERIA

### 4.1 User Experience Requirements

#### Navigation & Accessibility
- **Menu Integration:**
  - SpendTrack must appear under "Business Banking" > "Card Management" menu
  - Menu label: "SpendTrack Card Management" (or FI-approved branding)
  - Available to all business banking users with eligible credit card accounts

- **Penni Search Integration:**
  - Penni AI must return SpendTrack as result for queries such as:
    - "card management"
    - "spendtrack"
    - "credit card transactions"
    - "manage business card"
  - Search result displays: "SpendTrack - Manage your business credit card"

- **Quick Links Widget:**
  - FI can optionally add SpendTrack to Quick Links for one-click access
  - Widget displays: Icon + "SpendTrack" label

#### Multi-Channel Consistency
- **Online Banking:** SpendTrack accessible via menu, Penni, and Quick Links
- **Mobile iOS:** SpendTrack accessible via menu and search (iframe or in-app browser)
- **Mobile Android:** SpendTrack accessible via menu and search (iframe or in-app browser)
- **Responsive Design:** SpendTrack interface must render correctly on all screen sizes (mobile, tablet, desktop)

#### Display & Branding
- **Iframe Implementation (F2A):**
  - SpendTrack loads within Harmoney Business iframe
  - Harmoney navigation header remains visible (optional: can be hidden for full-screen experience)
  - Harmoney footer remains accessible
  - No scrolling issues; iframe resizes dynamically to content

- **New Tab Implementation (F1B - if iframe not feasible):**
  - External link warning popup displays before opening SpendTrack
  - Warning text: "You are leaving [FI Name] Digital Banking. You will be directed to SpendTrack, a service provided by Fiserv. Continue?"
  - Buttons: "Continue" (opens SpendTrack in new tab) | "Cancel" (returns to Harmoney)
  - SpendTrack opens in new browser tab; user must close tab to return to Harmoney

#### First-Time User Experience
- **Terms & Conditions Acceptance:**
  - On first SSO access, user must accept Fiserv SpendTrack Terms & Conditions
  - User cannot proceed to dashboard without acceptance
  - Subsequent logins skip T&C screen

- **Role Assignment:**
  - User automatically assigned "Cardholder" role
  - User lands on Cardholder dashboard showing selected card/account

#### Role-Based Dashboard Rendering
- **Cardholder View:**
  - Displays single card/account details
  - Access to: transactions, payments, statements, card controls, activation

- **Program Administrator View:**
  - Displays all cards/accounts associated with company
  - Access to: all cardholder functions + admin controls (user management, spending limits, reporting)
  - Self-promotion workflow available if user wants to request PA role

- **Reporting Administrator View:**
  - View-only access to company cards/accounts
  - No transaction or payment capabilities

#### Logout & Return Behavior
- **Logout from SpendTrack:**
  - User clicks "Logout" in SpendTrack interface
  - User redirected to `logoutURL` defined in SAML assertion
  - Harmoney session remains active (user returned to Harmoney Business home)

- **Return to Harmoney:**
  - If SpendTrack provides "Return to Digital Banking" link, user redirected to `returnURL`
  - User returned to Business Card Management section (or defined landing page)

### 4.2 Admin & Harmoney Requirements

#### SSO Invocation Logging
- **Harmoney Admin Logs:**
  - Log every SSO request with timestamp, user ID, account ID, success/failure status
  - Retain logs for minimum 90 days for auditing and troubleshooting

- **Admin Dashboard Visibility:**
  - Admin users can view SSO activity report:
    - Total SSO invocations (daily, weekly, monthly)
    - Unique users accessing SpendTrack
    - Failed SSO attempts with error codes

#### Enrollment Tracking
- **First-Time Enrollment Event:**
  - Log when user first accesses SpendTrack (JIT enrollment)
  - Capture: User ID, Account ID, Company ID, enrollment timestamp

- **Role Change Event:**
  - Log when user role changes (e.g., User → Program Administrator)
  - Capture: User ID, old role, new role, change timestamp

#### Payload & Error Debugging
- **SAML Assertion Payload Logging:**
  - Admin interface must allow authorized users to view SAML assertion payload for failed SSO attempts
  - Payload displayed in readable JSON/XML format with all attributes
  - Sensitive data (e.g., full card numbers) masked in display

- **Error State Logging:**
  - Capture and log all SSO errors:
    - Certificate validation failures
    - Missing required attributes
    - Fiserv IDV service errors (HTTP 4xx, 5xx)
    - SpendTrack validation errors
  - Admin can export error logs for Fiserv support escalation

#### Configuration Management
- **Environment Toggle:**
  - Admin can switch between CAT (test) and Production endpoints via configuration setting
  - No code deployment required to change environments

- **Certificate Management:**
  - Admin interface displays current SAML signing certificate details (issuer, expiration date)
  - Admin receives notification 30 days before certificate expiration
  - Certificate upload/update capability for authorized admins

### 4.3 Error Handling & User Support

#### User-Facing Error Messages
- **Generic SSO Failure:**
  - Message: "We're unable to connect to SpendTrack at this time. Please try again later or contact support."
  - Display Zendesk widget or support contact button

- **Account Not Found:**
  - Message: "We couldn't find a SpendTrack account associated with this card. Please contact [FI Name] support for assistance."
  - Provide phone number and Zendesk chat option

- **Session Timeout:**
  - Message: "Your SpendTrack session has expired due to inactivity. Click here to return to Digital Banking."
  - Button redirects to `returnURL`

#### Support Channel Integration
- **Zendesk Integration (if available):**
  - Users can report SpendTrack access issues directly via embedded Zendesk widget
  - Support ticket automatically includes: User ID, timestamp, error code, browser/device info

- **Phone Support:**
  - Error messages display FI support phone number for immediate assistance

- **Admin Support Tools:**
  - Admin can view user's last SSO attempt details to assist with troubleshooting
  - Admin can manually test SSO for specific user/account combination

### 4.4 Logic Gate: External Link Warning (F1B Only)

**IF Feature Integration Type = F1B (New Tab with Warning):**

#### Warning Popup Logic
- **Trigger:** User clicks SpendTrack menu item, Quick Link, or Penni result
- **Display:** Modal popup overlays Harmoney interface
- **Content:**
  - **Headline:** "You are leaving [FI Name] Digital Banking"
  - **Body Text:** "You will be directed to SpendTrack, a card management service provided by Fiserv. [FI Name] is not responsible for the content or availability of external sites."
  - **Checkbox (optional):** "Don't show this message again for SpendTrack" (stores preference in user session/profile)
  - **Buttons:**
    - **"Continue" (Primary):** Opens SpendTrack in new browser tab
    - **"Cancel" (Secondary):** Closes popup, returns to Harmoney Business

- **Behavior:**
  - Popup must display on every SpendTrack access (unless "Don't show again" selected)
  - "Continue" opens SpendTrack in new tab, original Harmoney tab remains open
  - "Cancel" closes popup without navigating away

**IF Feature Integration Type = F2A (Iframe):**
- **No external link warning required**
- SpendTrack loads directly within Harmoney iframe upon user click

---

## 5. PRE-LAUNCH CHECKLIST

### 5.1 Sitemap & Navigation Updates (Required)

- [ ] **Add SpendTrack to Business Banking Menu**
  - Menu item: "Card Management > SpendTrack"
  - Icon: Credit card or Fiserv-approved icon
  - Visibility rule: Display only for users with eligible business credit card accounts

- [ ] **Configure Penni Search Keywords**
  - Add SpendTrack to Penni search index with keywords:
    - "spendtrack", "card management", "credit card", "business card", "manage card", "card transactions"
  - Search result title: "SpendTrack Card Management"
  - Search result description: "Manage your business credit card, view transactions, and make payments"

- [ ] **Create Quick Link Widget (Optional)**
  - Widget name: "SpendTrack"
  - Widget icon: Credit card icon
  - Widget target: SpendTrack SSO URL
  - Admin can enable/disable for specific user groups

- [ ] **Mobile App Navigation (iOS & Android)**
  - Add SpendTrack to Business Banking section in mobile apps
  - Test iframe rendering or in-app browser behavior
  - Ensure responsive display on various device sizes

### 5.2 IP Whitelisting (Required)

- [ ] **Tyfone Provides Server IPs to Fiserv**
  - Production environment IPs
  - UAT/Staging environment IPs
  - IP addresses for all servers that will POST SAML assertions

- [ ] **Fiserv Whitelists IPs in eCS SSO Proxy**
  - CAT environment whitelisting complete
  - Production environment whitelisting complete
  - Confirmation received from Fiserv

- [ ] **Firewall Rules Updated**
  - Tyfone firewall allows outbound HTTPS to Fiserv endpoints:
    - `cat1.fsdsapps.com` (CAT)
    - `www.fsdsapps.com` (Production)

### 5.3 Certificate & Security Configuration (Required)

- [ ] **SAML Signing Certificate Generated**
  - X.509 certificate created by Tyfone
  - Private key securely stored in Tyfone certificate vault
  - Public certificate provided to Fiserv

- [ ] **Fiserv Configures Certificate in IDV Service**
  - Certificate uploaded to CAT environment
  - Certificate uploaded to Production environment
  - Certificate validation tested

- [ ] **Database Configuration in Fiserv eCS SSO Proxy**
  - `ECS_SSO_CLIENT_MAPPING` entry created with:
    - `appId`: `partners-1st-fcu`
    - `x500Id`: (Provided by Fiserv)
    - `cid`: `AAAA6450001`
    - `ocsShellId`: (Provided by Fiserv)
    - `logoutURL`: Tyfone logout URL
  - `ECS_SSO_SPEND_TRACK_SPA` entry created with SpendTrack sys/prin/agent details

### 5.4 Analytics & Reporting Configuration (Required)

- [ ] **Harmoney Admin Logging Enabled**
  - SSO invocation logging active
  - Enrollment event tracking configured
  - Error logging and payload capture enabled

- [ ] **Analytics Engine Data Push Configured**
  - SpendTrack access events pushed to Tyfone analytics platform
  - Metrics tracked:
    - Total SSO invocations
    - Unique users
    - Success/failure rate
    - Average session duration (if available)

- [ ] **Admin Dashboard Widgets Created**
  - SSO activity summary widget
  - Error log viewer
  - Payload inspector for troubleshooting

- [ ] **Fiserv Reporting Access (R2)**
  - FI granted access to Fiserv SpendTrack reporting portal
  - Reporting API credentials provided (if applicable)
  - Report export schedule configured (if needed)

### 5.5 Testing & Validation (Required)

- [ ] **UAT Testing in CAT Environment**
  - SSO flow tested with all required SAML attributes
  - First-time user enrollment tested (JIT provisioning)
  - Cardholder role dashboard rendering validated
  - Program Administrator role dashboard rendering validated (if applicable)
  - Logout and return URL behavior validated
  - Session timeout behavior tested
  - Error handling scenarios tested:
    - Missing SAML attributes
    - Invalid certificate
    - Account not found
    - Session timeout

- [ ] **Multi-Channel Testing**
  - Online Banking (desktop, tablet, mobile browsers)
  - Mobile iOS app
  - Mobile Android app
  - Iframe rendering and responsiveness validated

- [ ] **Load & Performance Testing**
  - SAML assertion generation performance tested under load
  - SSO response time validated (< 3 seconds for full redirect cycle)
  - Concurrent user testing (simulate expected peak usage)

- [ ] **Security Testing**
  - SAML signature validation tested
  - Certificate expiration handling tested
  - HTTPS/TLS enforcement validated
  - Session hijacking prevention tested

- [ ] **Accessibility Testing (if required by FI)**
  - WCAG 2.1 AA compliance validated for external link warning (if F1B)
  - Keyboard navigation tested
  - Screen reader compatibility tested

### 5.6 Communication & Training (Required)

- [ ] **FI Stakeholder Communication**
  - Release notes prepared with SpendTrack launch details
  - FI business owners notified of go-live date
  - Marketing materials prepared (if FI plans to promote feature)

- [ ] **End-User Communication**
  - In-app notification prepared: "New Feature: Manage your business credit cards with SpendTrack!"
  - Help center article created: "How to Access SpendTrack Card Management"
  - Email campaign prepared (if FI requests)

- [ ] **FI Support Team Training**
  - Support scripts created for common SpendTrack access issues
  - Admin troubleshooting guide provided (how to view SSO logs, payloads, errors)
  - Escalation path to Tyfone and Fiserv support documented

- [ ] **Admin Training**
  - Admin users trained on SSO activity monitoring
  - Admin users trained on certificate management and rotation
  - Admin users trained on error log analysis and Fiserv escalation procedures

### 5.7 Go-Live Readiness (Required)

- [ ] **Production Configuration Validated**
  - Production `startURL` configured: `https://www.fsdsapps.com/ecs-sso-proxy/sso/proxy/jwtproxy`
  - Production `cid`, `appId`, `returnURL`, `logoutURL` validated
  - Production certificate installed and validated

- [ ] **Runbook & Rollback Plan Documented**
  - Go-live runbook with step-by-step deployment checklist
  - Rollback plan documented (how to disable SpendTrack menu item if issues arise)
  - Incident response plan documented (Tyfone, Fiserv, FI contact tree)

- [ ] **Monitoring & Alerting Configured**
  - Real-time monitoring of SSO success/failure rates
  - Alerts configured for:
    - SSO failure rate > 5%
    - Fiserv endpoint downtime
    - Certificate expiration within 30 days

- [ ] **Post-Launch Review Scheduled**
  - 24-hour post-launch check-in scheduled
  - 7-day usage review scheduled
  - 30-day retrospective scheduled (review analytics, user feedback, error rates)

---

## 6. REQUIRED CLARIFICATIONS

The following items are **not specified** in the provided Jira context and must be confirmed before finalizing implementation:

### 6.1 Universal Requirements (Missing from Jira)

- [ ] **FI Decision: Iframe (F2A) vs. New Tab (F1B)?**
  - Does Partners 1st prefer iframe integration or new tab with warning?
  - If iframe, are there any content security policy (CSP) restrictions to consider?

- [ ] **Account/Card Selection Logic:**
  - If a business user has multiple credit cards, how is the `accountId` determined for SSO?
    - Option 1: User selects card from dropdown before launching SpendTrack
    - Option 2: Default to primary card; user can switch cards within SpendTrack
    - Option 3: Launch SpendTrack without specific `accountId`; SpendTrack displays all cards for user

- [ ] **Company ID Mapping:**
  - How is the `companyID` attribute populated?
    - Is it stored in Tyfone user profile?
    - Retrieved from core system based on business account data?
    - Provided by Fiserv during implementation?

- [ ] **Branding & Labeling:**
  - What menu label should be used? "SpendTrack", "Card Management", or FI-specific branding?
  - Does FI have custom icon/branding requirements?

- [ ] **uChoose Rewards Integration:**
  - Jira mentions uChoose Rewards integration within SpendTrack. Is this in scope for Tyfone?
    - If yes, requires separate SSO configuration (uChoose has different endpoints per Fiserv documentation)
  - Or is uChoose accessed entirely within SpendTrack (no separate Tyfone integration needed)?

### 6.2 Feature-Specific Requirements (Missing from Jira)

- [ ] **Deep Linking Support:**
  - Does FI want ability to deep link to specific SpendTrack pages?
    - Example: Link directly to "Make a Payment" or "View Transactions"
    - Requires `targetPage` and `targetId` attributes in SAML assertion (see Excel template)

- [ ] **Keep-Alive Implementation:**
  - Should Tyfone implement keep-alive ping to maintain Harmoney session while user is in SpendTrack?
    - If yes, what is the Harmoney session timeout (to determine ping frequency)?

- [ ] **Self-Promotion Workflow:**
  - Who approves Program Administrator promotion requests?
    - Fiserv handles approval automatically?
    - FI manual approval required?
    - Does Tyfone need to provide admin interface for approval workflow?

- [ ] **Test Environment Timeline:**
  - When will Partners 1st M Cycle test environment be available for UAT?
  - Are test user credentials already created, or does Tyfone need to request?

- [ ] **Production Cutover Plan:**
  - Will SpendTrack launch to all business users immediately, or phased rollout?
  - Is there a soft launch period with limited user group?

---

## 7. DEPENDENCIES & ASSUMPTIONS

### 7.1 Dependencies

- **Fiserv:**
  - Partnership agreement between Tyfone and Fiserv executed
  - CAT environment access provided (M Cycle test accounts)
  - Production configuration created (`cid`, `appId`, database entries)
  - 120-day implementation timeline from Fiserv (per Comment 3)

- **Partners 1st FCU:**
  - Service Request signed for SpendTrack solutions (completed per Comment 9)
  - Business credit card accounts provisioned in Fiserv system
  - Test user accounts linked to M Cycle card numbers

- **Tyfone:**
  - SAML SSO framework available in Harmoney Business platform
  - Certificate generation and management capability
  - Admin logging and payload inspection tools available

### 7.2 Assumptions

- SpendTrack is only available for **business/commercial credit cards** (not consumer credit cards or debit cards)
- Tyfone has access to card account numbers and company IDs from core system or user profile
- FI has communicated SpendTrack availability to business banking customers
- Fiserv handles all SpendTrack user interface, features, and backend logic (Tyfone only responsible for SSO initiation)
- Session timeout of 15 minutes is acceptable to FI (non-negotiable per Fiserv)

---

## 8. SUCCESS METRICS

### 8.1 Launch Success Criteria (First 30 Days)

- **Adoption:**
  - Minimum 20% of eligible business credit cardholders access SpendTrack within 30 days
  - Minimum 50% of Program Administrators access SpendTrack within 30 days

- **Technical Performance:**
  - SSO success rate ≥ 95%
  - Average SSO response time ≤ 3 seconds (from user click to SpendTrack dashboard load)
  - Zero critical security incidents (certificate failures, unauthorized access)

- **User Satisfaction:**
  - Support ticket volume related to SpendTrack access < 5% of total users
  - No escalations related to SSO failures beyond first 48 hours post-launch

### 8.2 Ongoing Monitoring Metrics

- **Usage:**
  - Monthly active users (MAU) accessing SpendTrack
  - Average sessions per user per month
  - Top accessed features within SpendTrack (if Fiserv provides data)

- **Reliability:**
  - Monthly SSO success rate
  - MTTR (Mean Time to Resolution) for SSO failures
  - Certificate expiration alerts and rotation success

- **Engagement:**
  - Percentage of users returning to SpendTrack within 7 days of first access
  - Program Administrator self-promotion requests and approval rates

---

## 9. RISK MITIGATION

### 9.1 Identified Risks

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| Fiserv 120-day implementation timeline delays project | Medium | High | Begin Fiserv partnership and configuration discussions immediately; track milestones weekly |
| Company ID mapping unavailable in Tyfone/core system | Medium | High | Confirm data source early in discovery; request sample data from Fiserv for validation |
| Certificate expiration causes SSO outage | Low | High | Implement 30-day expiration alert; document and test certificate rotation procedure |
| Iframe rendering issues (CSP violations, browser compatibility) | Medium | Medium | Test iframe in all supported browsers early; prepare fallback F1B implementation |
| Users have multiple cards, unclear which `accountId` to send | High | Medium | Clarify with FI and Fiserv during requirements phase; test multi-card user scenarios in UAT |
| Session timeout too short for user workflows | Low | Low | Educate users on timeout behavior; implement keep-alive if FI requests |

### 9.2 Contingency Plans

- **If Iframe Fails Technical Validation:**
  - Implement F1B (new tab with external link warning) as fallback
  - Communicate change to FI stakeholders

- **If Company ID Mapping Unavailable:**
  - Work with Fiserv to determine alternative identifier
  - Potentially defer Program Administrator functionality until data mapping complete

- **If UAT Timeline Slips:**
  - Prioritize critical path testing (SSO flow, cardholder dashboard)
  - Defer nice-to-have testing (deep linking, keep-alive) to post-launch iteration

---

## 10. APPENDIX

### 10.1 Reference Documentation

- **SpendTrack SSO Guide (PDF):** `/attachments/SpendTrack-SSO.pdf`
- **eCS SSO Proxy Guide (DOCX):** `/attachments/eCS_SSO_Proxy_Guide 1.docx`
- **SSO Attributes Template (XLSX):** `/attachments/SSO Attributes - Credit Migration Template v10.xlsx`
- **Jira Ticket:** [PROD-757](https://tyfone.atlassian.net/browse/PROD-757)
- **Related Project:** [PROD-1035 - Partners 1st DNA Implementation](https://tyfone.atlassian.net/browse/PROD-1035)

### 10.2 Environment Details

| Environment | SSO Endpoint (startURL) | CID | AppID | Test Accounts |
|-------------|------------------------|-----|-------|---------------|
| **CAT (M Cycle)** | `https://cat1.fsdsapps.com/ecs-sso-proxy/sso/proxy/jwtproxy` | `AAAA6450001` | `partners-1st-fcu` | `4017034000000309`<br>`4017034000101024`<br>`4017034000101032` |
| **Production (B Cycle)** | `https://www.fsdsapps.com/ecs-sso-proxy/sso/proxy/jwtproxy` | `AAAA6450001` | `partners-1st-fcu` | (Live card numbers) |

### 10.3 Fiserv Contact Information

- **Implementation Lead Time:** 120 days for SpendTrack SSO certification (per Fiserv email in Comment 3)
- **Partnership Agreement:** Required between Tyfone and Fiserv (completed per Comment 9)
- **Test Environment Access:** Requires Service Request from Partners 1st (completed per Comment 9)

### 10.4 Open Questions Log

| # | Question | Owner | Status | Resolution |
|---|----------|-------|--------|------------|
| 1 | Iframe (F2A) vs. New Tab (F1B) - which integration type? | FI/Tyfone | Open | Pending FI technical review |
| 2 | How is `companyID` populated in SAML assertion? | Tyfone Eng | Open | Needs core system data mapping analysis |
| 3 | Multi-card user: how to select `accountId` for SSO? | FI/Fiserv | Open | Pending requirements clarification |
| 4 | uChoose Rewards - separate Tyfone integration needed? | Fiserv | Open | Fiserv to confirm if in scope |
| 5 | Deep linking support - does FI want `targetPage`/`targetId`? | FI | Open | Pending FI feature prioritization |
| 6 | Keep-alive implementation - required? | FI | Open | Pending FI decision |
| 7 | Program Admin promotion approval - workflow ownership? | Fiserv/FI | Open | Fiserv to confirm approval mechanism |
| 8 | CAT environment UAT start date? | Fiserv | Open | Pending Fiserv implementation timeline |

---

## DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Product Manager** | | | |
| **Engineering Lead** | Aditya M / Dinesh Shilpi | | |
| **UX Lead** | TBD | | |
| **FI Stakeholder** | Partners 1st FCU | | |
| **Fiserv Partner Manager** | | | |

---

**Next Steps:**
1. Review and approve this PRD with FI stakeholders
2. Resolve all items in "Required Clarifications" (Section 6)
3. Initiate Fiserv partnership agreement and technical kickoff
4. Schedule UAT in CAT environment (120-day timeline from Fiserv)
5. Begin Tyfone SAML integration development based on approved design

**Document Control:**
- **Created:** February 3, 2026
- **Last Updated:** February 3, 2026
- **Version:** 1.0 (Initial Draft)
- **Next Review:** Upon FI approval and requirements clarification
