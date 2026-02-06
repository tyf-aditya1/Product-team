# Feature Requirement

| Date | December  04, 2025 | Product Manager | Aditya Raj |
| :---- | :---- | :---- | :---- |
| **Customer** | —-- | **Target Go Live Date** |  |
| **Product** | nFinia | **Feature Area** | Transfers |
| **Project** | Internationalization  | Beginning with Spanish | **Case \#** |  |
| **Jira PM \#** | [Prod-348](https://tyfone.atlassian.net/jira/polaris/projects/PROD/ideas/view/3921480?selectedIssue=PROD-348) (Internationalization) | **Jira ENG/SUP \#** |  |
| **Feature Type** | New Feature/Product | **Banking Type** | Retail |
| **Source** | Customer Request | **Channels** | Online Banking Mobile Banking (iOS) Mobile Banking (Android) Tablet Banking Harmoney |
| **SOW Required** | Yes No TBD |  |  |
| **Core(s)** | —---- |  |  |
| **Eng Team Lead** |  | **T-Shirt Size** | Select One |
| **Target Release** |  | **Actual Release** |  |

Revision History

| Date | Remarks |  | Version |
| :---- | :---- | ----- | :---- |
| 09/15/2025 | Initial Draft |  | 1.0 |

## **Contents** {#contents}

[Contents	3](#contents)

[1\. Introduction	5](#1.-introduction)

[1.1 Purpose	5](#1.1-purpose)

[1.2 Background	5](#1.2-background)

[1.3 Credit Union Overview	5](#1.3-credit-union-overview)

[2\. Objectives & Goals	6](#2.-objectives-&-goals)

[2.1 Business Objectives	6](#2.1-business-objectives)

[2.2 Success Metrics	6](#2.2-success-metrics)

[3\. Scope	6](#3.-scope)

[3.1 In Scope \- Feature Matrix by Credit Union	6](#3.1-in-scope---feature-matrix-by-credit-union)

[3.2 Out of Scope	9](#3.2-out-of-scope)

[3.3 Product Applicability	9](#3.3-product-applicability)

[4\. Functional Requirements	9](#4.-functional-requirements)

[FR-0: Credit Card Overview & Display	9](#fr-0:-credit-card-overview-&-display)

[FR-0.1: Credit Card Tile Display	9](#fr-0.1:-credit-card-tile-display)

[FR-1: Card Issuance & Lifecycle Management	13](#fr-1:-card-issuance-&-lifecycle-management)

[FR-1.1: Order New Card (Physical & Digital)	13](#fr-1.1:-order-new-card-\(physical-&-digital\))

[FR-1.2: Order Replacement Card	16](#fr-1.2:-order-replacement-card)

[FR-1.3: Track Card Delivery Status	18](#fr-1.3:-track-card-delivery-status)

[FR-1.4: Digital Issuance (Virtual Card)	20](#fr-1.4:-digital-issuance-\(virtual-card\))

[FR-1.5: Mobile Wallet Push Provisioning	21](#fr-1.5:-mobile-wallet-push-provisioning)

[FR-2: PIN Management	22](#fr-2:-pin-management)

[FR-2.1: Set/Reset PIN \+ Notification	22](#fr-2.1:-set/reset-pin-+-notification)

[FR-3: User Management	24](#fr-3:-user-management)

[FR-3.1: Authorized Users \- Add/Manage	24](#fr-3.1:-authorized-users---add/manage)

[FR-4: Card Controls	27](#fr-4:-card-controls)

[FR-4.1: Decline Certain Merchant Types	27](#fr-4.1:-decline-certain-merchant-types)

[FR-4.2: Decline Certain Transaction Types	29](#fr-4.2:-decline-certain-transaction-types)

[FR-4.3: Update Cards on File	30](#fr-4.3:-update-cards-on-file)

[FR-5: Payments & Billing	32](#fr-5:-payments-&-billing)

[FR-5.1: Balance Consolidation \+ Notification	32](#fr-5.1:-balance-consolidation-+-notification)

[FR-5.2: Cash Advance Request	34](#fr-5.2:-cash-advance-request)

[FR-5.3: Credit Limit Increase Request	35](#fr-5.3:-credit-limit-increase-request)

[FR-5.3: Credit Limit Increase Request	36](#fr-5.3:-credit-limit-increase-request-1)

[FR-5.4: Installment Loan Payment	37](#fr-5.4:-installment-loan-payment)

[FR-8.2: New User Account Created	38](#fr-8.2:-new-user-account-created)

[FR-8.3: Merchant Type Detected	38](#fr-8.3:-merchant-type-detected)

[FR-8.4: Transaction Type Detected	39](#fr-8.4:-transaction-type-detected)

[FR-8.5: User Credentials Reset	39](#fr-8.5:-user-credentials-reset)

[5\. Non-Functional Requirements	40](#5.-non-functional-requirements)

[5.1 Performance	40](#5.1-performance)

[5.2 Security	40](#5.2-security)

[5.3 Availability	40](#5.3-availability)

[5.4 Accessibility	40](#5.4-accessibility)

[6\. UX/UI Considerations	41](#6.-ux/ui-considerations)

[6.1 Credit Card Tile CTAs	41](#6.1-credit-card-tile-ctas)

[6.2 Visual Indicators	41](#6.2-visual-indicators)

[6.3 Quick Actions Menu (3-dot)	41](#heading=h.5gkg5b0urj)

[7\. Dependencies & Open Items	42](#7.-dependencies-&-open-items)

[7.1 Diamond TBD Items \- Clarification Needed	42](#7.1-diamond-tbd-items---clarification-needed)

[7.2 Velera Enrollments Required	42](#7.2-velera-enrollments-required)

[7.3 Velera API Function Reference	42](#7.3-velera-api-function-reference)

## 1\. Introduction {#1.-introduction}

### 1.1 Purpose {#1.1-purpose}

This PRD defines the functional and technical requirements for integrating Velera Phase 3 credit card management capabilities into the digital banking platform (Mobile Banking and Online Banking) for three Credit Unions:

- **OUCU** (OU Credit Union)  
- **SFCU** (Selfreliance Federal Credit Union)  
- **Diamond** (Diamond Credit Union)

The integration leverages Velera (formerly PSCU) APIs to enable members to manage their credit cards through self-service digital channels.

### 1.2 Background {#1.2-background}

Velera is the card processing vendor providing credit card management APIs. This Phase 3 integration builds upon existing platform capabilities to deliver advanced card management features including:

- Card issuance and replacement  
- Balance consolidation (balance transfer)  
- Installment payment plans  
- PIN management  
- Card controls  
- Authorized user management

### 1.3 Credit Union Overview {#1.3-credit-union-overview}

| Credit Union | Product Type | Core System | Phase Status |
| :---- | :---- | :---- | :---- |
| **OUCU** | Debit \+ Credit | Core (Correlation) | Phase 3 \- New Development |
| **SFCU** | Credit Only | TBD | Phase 3 \- New Development |
| **Diamond** | Debit \+ Credit | Keystone | Phase 3 \- New Development (Scope TBD on some items) |

- Auto-hide functionality after timeout

## 2\. Objectives & Goals {#2.-objectives-&-goals}

### 2.1 Business Objectives {#2.1-business-objectives}

- **Self-Service Enablement**: Reduce call center volume by enabling members to manage card functions digitally  
- **Member Experience**: Provide seamless, intuitive card management across mobile and online banking  
- **Fraud Prevention**: Enable real-time card controls and alerts to reduce unauthorized transactions  
- **Revenue Optimization**: Enable balance consolidation and installment plans to increase card utilization  
- **Operational Efficiency**: Automate card lifecycle processes currently handled manually

### 2.2 Success Metrics {#2.2-success-metrics}

| Metric | Target |
| :---- | :---- |
| Call center volume reduction (card-related) | 20-30% |
| Digital adoption for card replacement | 50%+ within 6 months |
| Balance consolidation submissions | Track baseline and growth |
| Installment plan enrollment (SFCU) | Track baseline and growth |

## 3\. Scope {#3.-scope}

### 3.1 In Scope \- Feature Matrix by Credit Union {#3.1-in-scope---feature-matrix-by-credit-union}

**Legend:**

- **YES** \= Confirmed in scope  
- **NO** \= Explicitly out of scope  
- **TBD** \= Pending confirmation (see Section 8 for clarification questions)

| Category | Feature | OUCU | SFCU | Diamond | Product | Notes |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **Card Issuance** | Order New Card (Physical) | YES | NO | TBD | Both | Diamond: Confirm with Velera |
| **Card Issuance** | Order Replacement Card | YES | YES | YES | Both | All CUs confirmed |
| **Card Issuance** | Track Plastic Card | YES | NO | YES | Both |  |
| **Card Issuance** | Digital Issuance (Virtual Card) | YES | NO | YES | Both | Diamond: Confirm with Velera |
| **Card Issuance** | Mobile Wallet Push Provisioning | YES | NO | YES | Both |  |
| **PIN Management** | Set/Reset PIN \+ Notification | YES | YES | YES | Both | All CUs confirmed |
| **User Management** | Authorized Users \- Add/Manage | YES (Both) | YES | YES (Credit) | Credit | Diamond: Credit only, No privileges |
| **Card Controls** | Decline Merchant Types | YES | YES | TBD | Both | Diamond: Not confirmed |
| **Card Controls** | Decline Transaction Types | YES | YES | TBD | Both | Diamond: Not confirmed |
| **Card Controls** | Update Cards on File  | YES | NO | YES | Both | Diamond: Check with Velera |
| **Payments** | Balance Consolidation \+ Notification | YES | YES | YES | Credit | Diamond: Check with Velera |
| **Payments** | Cash Advance Request | YES | NO | YES | Credit |  |
| **Payments** | Credit Limit Increase | YES | NO | TBD | Credit | Diamond: Explore Meridian Link option |
| **Payments** | Installment Loan Payment | NO | YES | NO | Credit | SFCU only \- requires Velera enrollment |
| **Payments** | Scheduled Payments | NO | YES | NO | Credit | SFCU only |
| **Payments** | Recurring Payments Enroll/Unenroll | NO | YES | NO | Credit | SFCU only |
| **Payments** | Posted Payments | NO | YES | NO | Credit | SFCU only |
| **Disputes** | Dispute Management \+ Report Lost/Stolen | YES | YES | YES | Both | All CUs confirmed |
| **Statements** | Next Statement Date | NO | YES | NO | Credit | SFCU only |
| **Alerts** | Balance Consolidation Submitted | YES | YES | TBD | Credit | Diamond: Not confirmed |
| **Alerts** | New User Account Created | YES | NO | TBD | Credit | Diamond: Not confirmed |
| **Alerts** | Merchant Type Detected | YES | NO | TBD | Both | Diamond: Not confirmed |
| **Alerts** | Transaction Type Detected | YES | NO | TBD | Both | Diamond: Not confirmed |
| **Alerts** | User Credentials Reset | YES | NO | TBD | Credit | Diamond: Not confirmed |

### 

### 3.2 Out of Scope {#3.2-out-of-scope}

- **Update Cardholder Information**: Handled by Core systems (Correlation for OUCU, Keystone for Diamond)  
- **In-branch card issuance**: Physical branch operations not included  
- **Debit card features for SFCU**: SFCU scope is Credit Card only  
- **SFCU Phase 2 features**: Already developed, requires configuration only (not covered in this PRD)

### 3.3 Product Applicability {#3.3-product-applicability}

| Product | Description | Applicable CUs |
| :---- | :---- | :---- |
| **Credit Card** | Velera-processed credit cards | OUCU, SFCU, Diamond |
| **Debit Card** | Velera-processed debit cards | OUCU, Diamond |

**Note**: Features marked "Both" apply to both debit and credit cards. Features marked "Credit" apply only to credit cards.

## 4\. Functional Requirements {#4.-functional-requirements}

---

### FR-0: Credit Card Overview & Display {#fr-0:-credit-card-overview-&-display}

#### FR-0.1: Credit Card Tile Display {#fr-0.1:-credit-card-tile-display}

**Applicable To**: OUCU, SFCU, Diamond

**Description** Display credit card information in a card tile format on the Cards Overview screen, consistent with debit card display but with credit-specific data fields.

**Credit Card Tile \- Required Display Fields**

| Field | Display Label | Description | Source |
| :---- | :---- | :---- | :---- |
| **Card Image** | \- | Visual representation of the card (branded) | Velera/FI Config |
| **Card Number (Masked)** | \- | xxxx-xxxx-xxxx-1234 | Velera API |
| **Cardholder Name** | \- | Primary or Authorized User name | Velera API |
| **Card Type Badge** | "Visa Credit" / "Visa Signature" / "Mastercard" | Card product type | Velera API |
| **Card Status** | "Status: Unlocked/Locked" | Toggle control for card lock/unlock | Velera API |
| **Current Balance** | "Current Balance" | Total amount owed on the card | Velera API |
| **Available Credit** | "Available Credit" | Credit Limit minus Current Balance | Velera API |
| **Payment Due Date** | "Due Date" | Date by which payment must be made | Velera API |
| **Authorized User Label** | "(Authorized User)" | Badge for non-primary cardholders | Velera API |

**Quick Action Buttons (Bottom of Tile)**

| Button | Card Type | Action | Notes |
| :---- | :---- | :---- | :---- |
| **Manage Card** | Credit | Navigate to card management/settings screen | Primary CTA for card controls, PIN, limits |
| **Make Payment** | Credit | Navigate to payment screen | Direct access to pay credit card bill |
| **View Activity** | Credit | Navigate to transaction history | See recent charges, pending transactions |
| **View Account** | Debit | Navigate to linked checking/savings account | Debit only \- links to deposit account |

**Debit Card Tile CTAs**: Follow existing implementation 

**Credit Card Tile CTAs**: `[Manage Card]` `[Make Payment]` `[Vie`

**Related Links Panel (Right Side) \- Credit Card Specific**

| Link | Description | CU Availability |
| :---- | :---- | :---- |
| Activate Card | Activate new/replacement card | All |
| Make a Payment | Quick link to payment | All |
| Balance Transfer | Initiate balance consolidation | All |
| Dispute a Transaction | Report issues with transactions | All |
| Installment Plans | View/enroll in installment plans | SFCU only |
| Manage Authorized Users | Add/remove authorized users | All |
| Travel Notification | Set travel dates | All |
| Card Controls | Manage merchant/transaction controls | All |
| eStatements | View/download statements | All |

**Requirements**

- Display credit card tile below debit card tiles on Cards Overview  
- All balance fields must refresh in real-time from Velera  
- Payment due date should highlight/change color if within 7 days or past due  
- Minimum payment should highlight if past due  
- Authorized users must be clearly labeled  
- Lock/Unlock toggle must update Velera in real-time  
- Support multiple credit cards per member

**Visual Indicators**

| Condition | Visual Treatment |
| :---- | :---- |
| Payment due within 7 days | Due date in **orange/warning** color |
| Payment past due | Due date and minimum payment in **red/error** color |
| Card locked | Status shows "Locked" with **red** indicator |
| Card unlocked | Status shows "Unlocked" with **green** indicator |
| Authorized User | Badge/label "(Authorized User)" next to name |

**Edge Cases**

- No credit cards on account → Do not display Credit Cards section  
- Credit card pending activation → Show "Activate Card" CTA prominently  
- $0 balance → Display "$0.00" for Current Balance  
- No minimum payment due → Display "No Payment Due" or "$0.00"

**Acceptance Criteria**

- AC1: Credit card tile displays all required fields accurately  
- AC2: Balances refresh within seconds of page load  
- AC3: Lock/Unlock toggle updates within seconds  
- AC4: Past due visual indicators display correctly  
- AC5: Authorized users clearly distinguished from primary cardholder  
- AC6: Quick actions navigate to correct screens

### FR-1: Card Issuance & Lifecycle Management {#fr-1:-card-issuance-&-lifecycle-management}

#### FR-1.1: Order New Card (Physical & Digital) {#fr-1.1:-order-new-card-(physical-&-digital)}

**Applicable To**: OUCU, Diamond (TBD)

**Velera API Reference**

- **Function ID**: 1440 (New Cardholder Account)  
- **Request Type (RQID)**: ACCTXML  
- **Mandatory Requirements**: Full cardholder address, SSN, acceptance of account terms (ACCTERMS=Y)

**Fulfillment Parameters**

| Parameter | Description | Values |
| :---- | :---- | :---- |
| PLSTCT | Number of plastics to be issued | Integer |
| PLSTTYPE | Material or image type | standard, photo |
| RUSHPLST | Expedited shipping carrier | BF (FedEx), AU (UPS Next Day), BA (DHL) |

**Description** Enable members to request a new physical or digital (virtual) credit/debit card through digital banking channels. This unified flow supports both card types with the option to issue a digital card instantly while a physical card ships.

**Use Cases**

1. Member requests a new card for a newly opened account  
2. Member requests an additional card for an existing account  
3. Member requests a card for an authorized user  
4. Member requests instant digital card for immediate use  
5. Member requests both physical and digital card simultaneously

**Entry Point**

- Cards Overview Screen → "+ Activate a new card" button (top right of Quick Links panel)

[Figma –](https://www.figma.com/proto/JQpeEGOXu39KrXB4YYwCAq/Digital-Issuance-2.0-Prototype-CFCU?page-id=9%3A29&node-id=34-945&viewport=279%2C-347%2C0.07&t=5UhZia8HCzxCWM1s-1&scaling=scale-down-width&content-scaling=fixed&starting-point-node-id=34%3A945&show-proto-sidebar=1) 

UX Flow \-

![][image1]

**Requirements**

- Member must be authenticated via MFA before card request  
- System validates member eligibility for new card issuance  
- Support account selection from dropdown (Checking, Savings, Credit accounts)  
- Support card type selection (Debit or Credit based on account type)  
- Display card design carousel with available designs  
- Physical vs Digital card option with clear messaging:  
  - Digital card available immediately regardless of physical card choice  
  - Physical card ships within 8-10 business days if selected  
- Member confirms shipping address if physical card requested  
- PIN setup required during card creation flow  
- System submits card order to Velera  
- Confirmation modal shows summary before final submission  
- Success screen displays new card details and next actions  
- Notification sent (push/email/SMS) upon successful submission


**Digital Card Immediate Availability (Debit vs Credit)**

| Card Type | Digital Card Availability | Notes |
| :---- | :---- | :---- |
| Debit | **Immediate** \- Available within 60 seconds | Card appears in Cards Overview instantly after creation |
| Credit | **Processing Required** \- Available within 24-48 hours | Requires credit approval/processing by Velera before activation |

**Post-Creation Actions**

- **View Card Details**: Navigate to full card management screen  
- **Add to Wallet**: Initiate push provisioning to Apple Pay/Google Pay/Samsung Pay  
- **Done**: Return to Cards Overview (new card will be visible)

**Acceptance Criteria**

- AC1: New card request submitted successfully to Velera within 5 seconds  
- AC2: Member receives confirmation with order reference number  
- AC3: Digital debit card available immediately after creation  
- AC4: Digital credit card available within 24-48 hours (processing status shown)  
- AC5: Card status trackable post-submission (see FR-1.3)  
- AC6: PIN successfully set during card creation flow  
- AC7: Physical card delivery estimated as 8-10 business days

**FI Configuration**

- Enable/disable new card ordering per CU  
- Configure maximum cards per member  
- Configure eligible card types (Debit, Credit, or both)  
- Configure available card designs per card type  
- Configure PIN requirements (length, restrictions)  
- Configure digital-only vs physical+digital options

#### FR-1.2: Order Replacement Card {#fr-1.2:-order-replacement-card}

**Applicable To**: OUCU, SFCU, Diamond

**Description** Enable members to request a replacement card when their existing card is lost or stolen. The current card will be blocked immediately, and a new digital version of the replacement card will be made available for immediate use while the physical card is shipped.

**Velera API Reference**

- **Function ID**: 1409 (Order Damage Replacement Card)  
- **Business Logic**: Reissues a card for an existing account due to damage without changing the account number  
- **CARDACTIVATION=Y**: Ensures new plastic requires verification before use  
- **REPLACEMENTFEE=Y**: Triggers replacement fee set in FI's Product Control File (PCF)

**Entry Point**

- Card Management Screen → "Replace Card" link (bottom right of card details section)

UX Flow –  Use Current Implementation

**Replacement Reason Options**

| Reason | Card Action | Notes |
| :---- | :---- | :---- |
| **Lost** | Blocked immediately | Card reported as lost, all transactions declined |
| **Stolen** | Blocked immediately | Card reported as stolen, fraud monitoring triggered |

**Key Messaging**

- Warning banner: "By replacing your card, your current card will be blocked. A new digital version of the replacement card will be made available to you for immediate use."  
- This clearly communicates:  
  1. Current card will be blocked (irreversible)  
  2. Digital replacement available immediately  
  3. Physical card will be shipped

**PIN Requirements for Replacement Card**

- PIN must be set during replacement flow   
- Same PIN validation rules as new card issuance

**Requirements**

- Display warning banner explaining card block and digital availability  
- Provide dropdown for replacement reason (Lost/Stolen)  
- Require PIN setup for replacement card  
- Display shipping address with option to change  
- Block current card immediately upon submission  
- Generate new digital card instantly (for Debit)  
- Process new digital card within 24-48 hours (for Credit)  
- Ship physical replacement card within 8-10 business days  
- Send confirmation notification (push/email/SMS)  
- Provide tracking capability on success screen

**Edge Cases**

- Member cancels → no action taken, card remains active  
- Address marked as undeliverable → prompt to change address or contact support  
- PIN validation fails → display inline error with requirements  
- Multiple replacement requests in short period → flag for fraud review  
- Credit card processing delay → show "Processing" status with expected timeframe

**Acceptance Criteria**

- AC1: Replacement request processed within 5 seconds  
- AC2: Previous card blocked immediately upon submission  
- AC3: Digital debit card available immediately after submission  
- AC4: Digital credit card shows "Processing" status, activates within 24-48 hours  
- AC5: Success screen displays all card status information  
- AC6: "Track Card" button navigates to tracking screen (FR-1.3)  
- AC7: Confirmation notification sent via member's preferred channel

#### FR-1.3: Track Card Delivery Status {#fr-1.3:-track-card-delivery-status}

**Applicable To**: OUCU, Diamond

**Velera API Reference**

- **Function ID**: 1480 (Cardholder Plastics)

**Fulfillment Status Codes (SHIPSTAT)**

| Code | Status | Description |
| :---- | :---- | :---- |
| O | Ordered | Request received by the production unit |
| D | In Production | Card is currently being manufactured |
| F | Formatting | Data is being prepared for embossing machines |
| I | Inserting | Card is being placed in the mailer |
| S | Shipped | Plastic has left the facility |

**Tracking Elements**

- **TRACKINGNMBR**: Carrier-specific tracking number  
- **SHIPDATE**: Exact ship date

**Description** Enable members to track the status of newly ordered cards, including both digital card activation status and physical card delivery status.

**Use Cases**

1. Member views status of digital card (immediate for Debit, processing for Credit)  
2. Member views delivery status of physical card shipment  
3. Member checks estimated delivery date for physical card  
4. Member sees shipping carrier and tracking info (if available)

**Card Status Tracking Matrix**

| Card Type | Digital Card Status | Physical Card Status |
| :---- | :---- | :---- |
| **Debit** | **Active** \- Immediate (within 60 seconds) | Ordered → In Production → Formatting → Inserting → Shipped |
| **Credit** | **Processing** → **Active** (24-48 hours) | Ordered → In Production → Formatting → Inserting → Shipped |

**User Flow**

1. Member navigates to Card Status/Tracking screen  
2. System displays card image and details  
3. **Digital Card Status Section**: Shows current status (Active/Processing)  
4. **Physical Card Delivery Section**: Shows progress timeline with current status  
5. If shipped: Display carrier, tracking number, estimated delivery  
6. Member can tap "Track with Carrier" to open carrier website

**Requirements**

- Display separate status sections for Digital and Physical card  
- Digital card status shows immediately after card creation  
- Physical card tracking shows delivery progress timeline  
- Link to carrier tracking website (opens in external browser)  
- Auto-refresh status every 5 minutes when screen is active  
- Push notification sent when status changes (Shipped, Delivered)

**Edge Cases**

- Digital card only (no physical) → Hide Physical Card Delivery section  
- Tracking number not yet available → Display "Tracking will be available once shipped"  
- Delivery delayed → Display "Delivery delayed. Expected by \[new date\]"  
- Card not delivered after 14 days → Display "Contact us" prompt with support link

**Acceptance Criteria**

- AC1: Card status retrieved from Velera and displayed within 3 seconds  
- AC2: Status updates reflected within 24 hours of Velera update  
- AC3: Digital debit card shows "Active" status immediately after creation  
- AC4: Digital credit card shows "Processing" status until Velera confirms activation  
- AC5: Physical card delivery timeline displays accurate progress  
- AC6: Carrier tracking link opens correctly in external browser  
- AC7: Push notifications sent for status changes

#### FR-1.4: Digital Issuance (Virtual Card) {#fr-1.4:-digital-issuance-(virtual-card)}

**Applicable To**: OUCU, Diamond (TBD)

**Velera API Reference**

- **Function ID**: 1346 (CVV Inquiry)  
- **Digital Presentation**: Retrieves CVV and CVVEXPDATE (MM/YY) for display in mobile app  
- **CVVTYPE=V**: Use for virtual card credentials  
- **Note**: Virtual credentials typically only available if physical card has not been activated

**Description** Enable instant issuance of virtual cards that can be used immediately for online purchases and digital wallet provisioning.

**Key Behavior by Card Type**

| Card Type | Digital Card Availability | Notes |
| :---- | :---- | :---- |
| Debit | Immediate \- within 60 seconds | Ready for online purchases and wallet provisioning |
| Credit | 24-48 hours processing | Requires Velera credit processing before activation |

**User Flow**

1. Member completes new card order (FR-1.1)  
2. For Debit: Digital card created and available immediately  
3. For Credit: Digital card shows "Processing" status  
4. Member can view full card number, expiry, CVV in app (after MFA)  
5. Member can add card to mobile wallet

**Requirements**

- Virtual card credentials displayed only after MFA verification  
- Show/hide toggle for card number and CVV  
- Auto-hide sensitive data after 60 seconds  
- Support copy-to-clipboard for card number  
- Enable "Add to Wallet" action from virtual card display

**Acceptance Criteria**

- AC1: Virtual card credentials retrieved via Function 1346  
- AC2: CVV displayed only for CVVTYPE=V  
- AC3: Credentials hidden by default, revealed on user action  
- AC4: Auto-hide after 60 seconds of display  
- AC5: Add to Wallet initiates push provisioning flow

#### FR-1.5: Mobile Wallet Push Provisioning {#fr-1.5:-mobile-wallet-push-provisioning}

**Applicable To**: OUCU, Diamond

**Velera API Reference** Uses specialized Authorization Type Codes (Appendix N) for tokenization:

| Code | Description |
| :---- | :---- |
| AC | Activation code for token provisioning via step-up authentication |
| TN | Confirms token is granted and linked to cardholder account |
| TM | Handles ongoing token maintenance (activation, suspension, deactivation) |

**Supported Wallets**

- Apple Pay  
- Google Pay  
- Samsung Pay

**Description** Enable members to add their card directly to mobile wallet (Apple Pay, Google Pay, Samsung Pay) from within the banking app using push provisioning.

**User Flow**

1. Member taps "Add to Wallet" on card details or success screen  
2. System detects available wallets on device  
3. Member selects target wallet (Apple Pay, Google Pay, Samsung Pay)  
4. System initiates push provisioning with step-up authentication (AC code)  
5. Member completes authentication (Face ID, fingerprint, or passcode)  
6. Token granted (TN code) and linked to account  
7. Card appears in selected mobile wallet  
8. Confirmation displayed in banking app

**Requirements**

- Detect available mobile wallets on device  
- Support Apple Pay, Google Pay, Samsung Pay  
- Implement step-up authentication per wallet requirements  
- Handle token lifecycle (activation, suspension, deactivation)  
- Display confirmation when card successfully added

**Acceptance Criteria**

- AC1: Available wallets detected and displayed  
- AC2: Push provisioning completes within 30 seconds  
- AC3: Step-up authentication required and validated  
- AC4: Token successfully created and linked  
- AC5: Card visible in mobile wallet after provisioning  
- AC6: Confirmation displayed in banking app

### FR-2: PIN Management {#fr-2:-pin-management}

#### FR-2.1: Set/Reset PIN \+ Notification {#fr-2.1:-set/reset-pin-+-notification}

**Applicable To**: OUCU, SFCU, Diamond

**Velera API Reference**

- **Function ID 1444**: Set PIN Offset  
- **Function ID 1445**: PIN Verification Number  
- **Function ID 1491**: Omaha PIN Resets \- Use with COUNTER=P to reset excessive PIN attempt counter if user is blocked

**Description** Enable members to set a new PIN or reset a forgotten PIN for their credit/debit card.

**Entry Point**

- Card Management Screen → "Set/Reset PIN" link  
- Quick Actions Menu → "Set/Reset PIN"

**User Flow**

1. Member navigates to Set/Reset PIN  
2. System verifies member identity (MFA if required)  
3. Member enters new 4-digit PIN  
4. Member confirms PIN (re-enter)  
5. System validates PIN against requirements  
6. System submits to Velera Function 1444/1445  
7. Success confirmation displayed  
8. Notification sent to member (push/email/SMS)

**PIN Requirements**

- Must be exactly 4 digits  
- Cannot be sequential (1234, 4321, 2345, etc.)  
- Cannot be repeated digits (1111, 0000, 2222, etc.)  
- Cannot match last 4 digits of card number  
- Cannot match last 4 digits of SSN (if configured)

**Validation Rules**

| Rule | Error Message |
| :---- | :---- |
| PIN not 4 digits | "PIN must be exactly 4 digits" |
| Sequential digits | "PIN cannot be sequential numbers (e.g., 1234)" |
| Repeated digits | "PIN cannot be repeated numbers (e.g., 1111)" |
| Matches card number | "PIN cannot match the last 4 digits of your card" |
| PINs don't match | "PINs do not match. Please try again." |

**Edge Cases**

- User locked out due to excessive attempts → Use Function 1491 with COUNTER=P to reset  
- PIN change fails → Display error with retry option  
- Session timeout during PIN entry → Require re-authentication

**Acceptance Criteria**

- AC1: PIN validated against all requirements before submission  
- AC2: PIN successfully set via Velera Function 1444  
- AC3: Excessive attempt counter reset via Function 1491 when needed  
- AC4: Confirmation notification sent upon success  
- AC5: PIN masked during entry (show/hide toggle available)

**FI Configuration**

- Configure PIN length (4 or 5 digits)  
- Configure which validation rules to enforce  
- Configure notification channels (push, email, SMS)

### FR-3: User Management {#fr-3:-user-management}

#### FR-3.1: Authorized Users \- Add/Manage {#fr-3.1:-authorized-users---add/manage}

**Applicable To**: OUCU (Both), SFCU, Diamond (Credit only)

**Velera API Reference**

- **Function ID 1404**: Update Cardholder Information  
  - **Add Process**: Set AUTHMBRSEQ=NEW and provide AUTHNAME  
  - **Remove Process**: Set AUTHNAME=%20 (space) and provide specific AUTHEXTRID for user to be deleted  
- **Function ID 1423**: Extended Cardholder Information  
  - **Data Returned**: Full list of secondary users including AUTHNAME, AUTHMBRSEQ, AUTHEXTRID, AUTHDATEOFBIRTH

**Description** Enable primary cardholders to add, view, and remove authorized users on their credit card account. Authorized users receive their own card but have no access to account management features.

**Critical Policy Constraints**

| Constraint | Policy | Rationale |
| :---- | :---- | :---- |
| **Who Can Add** | Primary Cardholder ONLY | Joint owners, authorized users, and other account holders cannot add authorized users |
| **Product Type** | Personal Credit Cards ONLY | Business credit cards are explicitly excluded from this feature |
| **Authorized User Privileges** | Transaction-only access | Authorized users receive a card for purchases ONLY \-no account access, no feature access, no card controls |
| **Card Delivery** | Primary cardholder's address only | Security requirement- cards are never mailed directly to the authorized user |

**Entry Points & Positioning**

| Entry Point | Location | Priority | Rationale |
| :---- | :---- | :---- | :---- |
| **Credit Card Tile** | 3-dot menu → "Manage Authorized Users" | Primary | Direct card-level management |
| **Related Links Panel** | Card Management → "Authorized Users" | Primary | Standard card management feature |
| **Account Settings** | Account Settings → "Manage Users" | Secondary | Account-level management path |
| **More Options Menu** | More → "Authorized Users" | Tertiary | Discoverable for users exploring features |

**Important Limitations (Display to User)**

- Authorized users are NOT joint account holders  
- Authorized users have NO access to:  
  - Online or mobile banking for this card  
  - Account management or settings  
  - Card controls or alerts  
  - Statement access  
- Primary cardholder is responsible for ALL charges made by authorized users  
- Authorized user's card will be mailed to primary cardholder's address

**Entry Point**

- Card Management → "Authorized Users" link  
- Credit Card Tile → 3-dot menu → "Manage Authorized Users"

**User Flow \- Add Authorized User**

1. Primary cardholder navigates to Authorized Users  
2. Taps "Add Authorized User"  
3. System displays disclaimer about authorized user limitations  
4. Primary enters required information:  
   - Full Legal Name (First, Middle optional, Last)  
   - Date of Birth  
   - Social Security Number  
   - Relationship to primary  
5. Primary reviews all information  
6. Primary accepts terms and conditions  
7. System submits to Velera Function 1404 (AUTHMBRSEQ=NEW)  
8. Success confirmation with card delivery timeline (8-10 business days)  
9. Confirmation notification sent

**User Flow \- View Authorized Users**

1. Primary cardholder navigates to Authorized Users  
2. System retrieves list via Function 1423  
3. For each authorized user, display:  
   - Name  
   - Card last 4 digits  
   - Relationship  
   - Date added  
   - Card status (Active/Inactive)  
4. Primary can tap any user to view details or remove

**User Flow \- Remove Authorized User**

1. Primary taps authorized user → "Remove"  
2. System displays confirmation modal with warnings:  
   - Card will be deactivated immediately  
   - Action cannot be undone  
   - To re-add, must submit new request  
3. Primary confirms removal  
4. System submits to Velera Function 1404 (AUTHNAME=%20, AUTHEXTRID)  
5. Authorized user's card deactivated immediately  
6. Confirmation displayed and notification sent

**Required Fields**

| Field | Required | Validation | Notes |
| :---- | :---- | :---- | :---- |
| First Name | Yes | 1-50 characters, letters only | As it will appear on card |
| Middle Name | No | 0-50 characters | Optional |
| Last Name | Yes | 1-50 characters, letters only | As it will appear on card |
| Date of Birth | Yes | Valid date, minimum age 15 | Required for identity verification |
| SSN | Yes | 9 digits, valid format | Required for credit bureau reporting |
| Relationship | Yes | Select from list | Required by Velera API |

**Relationship Options**

| Code | Display Label |
| :---- | :---- |
| SP | Spouse |
| DP | Domestic Partner |
| CH | Child |
| PA | Parent |
| SB | Sibling |
| FM | Other Family Member |
| OT | Other |

**Edge Cases**

- Maximum authorized users reached → Display limit message  
- SSN already exists on account → Display duplicate error  
- Authorized user under minimum age → Display age requirement error  
- Primary tries to add themselves → Display error  
- Business card selected → Feature hidden/disabled

**Acceptance Criteria**

- AC1: Only primary cardholder can access Authorized Users management  
- AC2: Business cards do not show Authorized Users option  
- AC3: Disclaimer about limitations displayed before form  
- AC4: All required fields validated before submission  
- AC5: SSN validation prevents duplicates on same account  
- AC6: Age validation enforces minimum age of 15  
- AC7: Terms acceptance required before submission  
- AC8: Authorized user added via Function 1404 within 10 seconds  
- AC9: Removal immediately deactivates card  
- AC10: Confirmation notifications sent for add/remove

**FI Configuration**

- Maximum authorized users per account (default: 5\)  
- Minimum age for authorized users (13/15/18)  
- Allow joint owner to manage (Yes/No)  
- SSN requirement (Required/Optional)

### FR-4: Card Controls {#fr-4:-card-controls}

#### FR-4.1: Decline Certain Merchant Types {#fr-4.1:-decline-certain-merchant-types}

**Applicable To**: OUCU, SFCU, Diamond (TBD)

**Velera API Reference**

- **Function ID**: 1762 (Set Card Policy)  
- **Control ID**: C04 (Merchant)  
- **Merchant Categories**:  
  - A04T01: Entertainment  
  - A04T07: Travel  
  - (Additional categories per Velera spec)

**Description** Enable members to block transactions at specific merchant category types with optional spending limits.

**Merchant Categories Available**

| Category | Description | Toggle Action |
| :---- | :---- | :---- |
| Entertainment | Theaters, concerts, streaming | Block all entertainment purchases |
| Travel | Airlines, hotels, car rentals | Block all travel purchases |
| Restaurants | Dining, fast food, cafes | Block all restaurant charges |
| Gas Stations | Fuel purchases | Block all gas station transactions |
| Grocery | Supermarkets, food stores | Block all grocery purchases |
| Retail | Department stores, shops | Block all retail purchases |
| Online Shopping | E-commerce merchants | Block all online purchases |
| Gaming/Gambling | Casinos, lottery, betting | Block all gambling transactions |
| Adult Entertainment | Age-restricted content | Block all adult purchases |

**User Flow**

1. Member navigates to Card Controls → Merchant Categories  
2. System displays list of categories with ON/OFF toggles  
3. Member toggles category OFF to block transactions  
4. Optionally, member sets spending limits per category:  
   - Single Transaction Limit (max per transaction)  
   - Cumulative Limit (daily/weekly/monthly total)  
5. Member saves changes  
6. System submits to Velera Function 1762 (Control ID: C04)  
7. Changes take effect within 2 minutes

**Control Elements per Category**

| Element | Description |
| :---- | :---- |
| Category Toggle | ON/OFF switch to enable/disable category |
| Single Transaction Limit | Maximum amount per individual transaction |
| Cumulative Transaction Limit | Maximum total over period (daily/weekly/monthly) |

**Acceptance Criteria**

- AC1: Toggle state change applied within 2 minutes  
- AC2: Single transaction limit enforced correctly  
- AC3: Cumulative limit tracked accurately across period  
- AC4: Decline alert triggered when transaction blocked  
- AC5: Changes persisted across sessions

**FI Configuration**

- Configure which merchant categories are visible  
- Configure default ON/OFF states  
- Configure minimum/maximum limit values  
- Configure available frequency options (daily/weekly/monthly)

#### FR-4.2: Decline Certain Transaction Types {#fr-4.2:-decline-certain-transaction-types}

**Applicable To**: OUCU, SFCU, Diamond (TBD)

**Velera API Reference**

- **Function ID**: 1762 (Set Card Policy)  
- **Control ID**: C03 (Transaction Type)  
- **Transaction Types**:  
  - C03T01: eCommerce  
  - C03T02: Mail/Phone Order  
  - C03T05: ATM

**Description** Enable members to block specific transaction types/channels with optional spending limits.

**Transaction Types Available**

| Type | Description | Toggle Action |
| :---- | :---- | :---- |
| ATM Withdrawal | Cash withdrawals at ATMs | Block all ATM cash withdrawals |
| Autopay/Recurring | Automatic recurring payments | Block all automatic recurring payments |
| In-Store Purchases | Point-of-sale transactions | Block all POS purchases |
| International | Cross-border transactions | Block all international transactions |
| Online Transactions | E-commerce/card-not-present | Block all online purchases |
| Mail/Phone Order | MOTO transactions | Block all mail/phone orders |

**User Flow**

1. Member navigates to Card Controls → Transaction Types  
2. System displays list of transaction types with ON/OFF toggles  
3. Member toggles type OFF to block those transactions  
4. Optionally, member sets limits:  
   - Single Transaction Limit  
   - Cumulative Transaction Limit (daily/weekly/monthly)  
5. Member saves changes  
6. System submits to Velera Function 1762 (Control ID: C03)  
7. Changes take effect within 2 minutes

**Acceptance Criteria**

- AC1: Toggle state change applied within 2 minutes  
- AC2: Limits enforced correctly per transaction type  
- AC3: Decline notification sent when transaction blocked  
- AC4: International toggle clearly labeled with implications

#### FR-4.3: Update Cards on File {#fr-4.3:-update-cards-on-file}

**Applicable To**: OUCU, Diamond

**Velera API Reference**

Card on File (COF) is a specialized solution requiring enrollment at the card program level through PSCU. It allows cardholders to manage their card credentials across various eCommerce merchant sites.

**Function ID 1622 \- Merchant List Retrieval**

| Parameter | Description |
| :---- | :---- |
| **Request** | CLIENTID, CARDNUMBER |
| **Response \- Merchant Metadata** | MERCHANTNAME, MERCHANTID, MERCHANTSITE (URL) |
| **Response \- Requirements** | REQFIELDS tag identifies required data (email, phone, CVV, billing address) to link card |
| **Response \- Link Status** | PRIMARY (if primary link), STORABLE (if can be saved) |

**Function ID 1623 \- Card Upsert (Add/Update Credentials)**

| Parameter Type | Fields |
| :---- | :---- |
| **Card Details** | CARDNUMBER, CVV, EXPDATE (YYYY-MM) |
| **User Identity** | NAME (as on card), EMAIL, PHONE |
| **Address Details** | ADDR1, CITY, STATE, ZIP, COUNTRY |
| **Response** | Result (TRUE/FALSE), GRANT (unique ID), CREATEDON, LASTUPDON |

**Implementation Requirements**

- Card on File must be explicitly configured in eMessenger platform for the card program  
- Non-participating institutions receive exception: "FI does not participate in Card on File"  
- Works in conjunction with Function 1346 (CVV Inquiry) to provide virtual credentials for upsert before physical card arrives

**Description** Enable members to view all merchants where their card is saved on file and manage those card credentials.

**User Flow**

1. Member navigates to Card Controls → Cards on File  
2. System retrieves merchant list via Function 1622  
3. Display list of merchants where card is stored:  
   - Merchant name  
   - Merchant website  
   - Last updated date  
   - Status  
4. Member can take actions per merchant:  
   - **Update**: Update card credentials at merchant  
   - **Remove**: Request card removal from merchant's records  
5. System processes via Function 1623  
6. Confirmation displayed

**Display Fields per Merchant**

| Field | Source |
| :---- | :---- |
| Merchant Name | MERCHANTNAME |
| Merchant Website | MERCHANTSITE |
| Primary Link | PRIMARY flag |
| Last Updated | LASTUPDON |
| Status | Active/Pending |

**Actions**

| Action | Description | API |
| :---- | :---- | :---- |
| Update Credentials | Update card info at merchant | Function 1623 (Upsert) |
| Remove Card | Remove card from merchant | Function 1623 with removal flag |

**Acceptance Criteria**

- AC1: Merchant list retrieved via Function 1622  
- AC2: Card credentials updated via Function 1623  
- AC3: GRANT ID returned and stored for management  
- AC4: Status updates reflected within 24 hours  
- AC5: Error handling for non-participating FIs

**FI Configuration**

- Enrollment in Card on File program required  
- Configure in eMessenger platform

### FR-5: Payments & Billing {#fr-5:-payments-&-billing}

#### FR-5.1: Balance Consolidation \+ Notification {#fr-5.1:-balance-consolidation-+-notification}

**Applicable To**: OUCU, SFCU, Diamond

**Velera API Reference**

- **Function ID**: 1439  
- **Modes**:  
  - I (Inquiry): Check available credit for transfer  
  - R (Release): Authorize the payoff check

**Description** Enable members to transfer balances from other credit cards to their CU credit card (balance transfer).

**User Flow**

1. Member navigates to Balance Transfer  
2. System checks available credit via Function 1439 (Mode: I)  
3. System displays:  
   - Available credit for transfer  
   - Transfer fee percentage  
   - Promotional APR (if applicable)  
   - Terms and conditions  
4. Member enters transfer details:  
   - Creditor name (bank/card issuer)  
   - Account number to pay off  
   - Transfer amount  
5. Member reviews and accepts terms  
6. System submits via Function 1439 (Mode: R)  
7. Confirmation displayed with:  
   - Transfer amount  
   - Fee charged  
   - Expected processing time (7-14 business days)  
8. Notification sent to member

**Requirements**

- Display available credit before transfer  
- Validate transfer amount does not exceed available credit  
- Clearly display fees and APR  
- Require terms acceptance  
- Send confirmation notification

**Edge Cases**

- Insufficient available credit → Display error with available amount  
- Account newly opened → May not be eligible, display message  
- Transfer to same FI card → Block and display error

**Acceptance Criteria**

- AC1: Available credit retrieved via Inquiry mode  
- AC2: Transfer submitted via Release mode  
- AC3: Confirmation includes transfer details and timeline  
- AC4: Balance Consolidation Submitted alert sent (FR-8.1)  
- AC5: Transfer reflected on account within stated timeframe

#### FR-5.2: Cash Advance Request {#fr-5.2:-cash-advance-request}

**Applicable To**: OUCU, Diamond

**Velera API Reference**

- **Function ID 1485**: Authorization  
- **Function ID 1486**: Post Transaction  
- **TRANCODE**: 254

**Description** Enable members to request a cash advance against their credit card limit.

**User Flow**

1. Member navigates to Cash Advance  
2. System displays:  
   - Available cash advance limit  
   - Cash advance APR (typically higher than purchase APR)  
   - Cash advance fee ($ or %)  
3. Member enters:  
   - Cash advance amount  
   - Destination account (checking/savings at CU)  
4. System calculates and displays fee  
5. Member reviews total (amount \+ fee) and confirms  
6. System authorizes via Function 1485  
7. System posts transaction via Function 1486 with TRANCODE=254  
8. Confirmation displayed  
9. Funds deposited to destination account

**Requirements**

- Display available cash advance limit (may differ from credit limit)  
- Clearly show APR and fees before confirmation  
- Validate amount against available limit  
- Require destination account selection  
- Process authorization and posting

**Acceptance Criteria**

- AC1: Available cash advance limit displayed accurately  
- AC2: Fees and APR clearly disclosed  
- AC3: Authorization processed via Function 1485  
- AC4: Transaction posted via Function 1486  
- AC5: Funds available in destination account per CU policy

#### FR-5.3: Credit Limit Increase Request {#fr-5.3:-credit-limit-increase-request}

**Applicable To**: OUCU, Diamond (TBD \- explore Meridian Link)

**Velera API Reference**

- **Function ID**: 1424 (Credit Limit Adjustment)  
- **CLAPASSED=TRUE**: Confirms limit was adjusted immediately on Omaha platform

**Description** Enable members to request an increase to their credit limit.

**User Flow**

1. Member navigates to Credit Limit Increase  
2. System displays current credit limit and account status  
3. Member enters requested new limit  
4. System may request additional information:  
   - Annual income  
   - Employment status  
   - Housing payment  
5. Member submits request  
6. System submits to Velera Function 1424  
7. **If CLAPASSED=TRUE**: Immediate approval displayed with new limit  
8. **If pending**: "Request submitted for review" message with expected timeline

**Requirements**

- Display current limit and available credit  
- Allow member to specify requested limit  
- Collect required income/employment info if needed  
- Handle immediate approval (CLAPASSED=TRUE)  
- Handle pending review scenario

**Acceptance Criteria**

- AC1: Current limit and status displayed  
- AC2: Request submitted to Function 1424  
- AC3: Immediate approval handled when CLAPASSED=TRUE  
- AC4: Pending status displayed with timeline when not immediately approved  
- AC5: Notification sent upon final decision

#### FR-5.3: Credit Limit Increase Request {#fr-5.3:-credit-limit-increase-request-1}

**Applicable To**: OUCU, Diamond (TBD \- explore Meridian Link)

**Velera API Reference**

- **Function ID**: 1424 (Credit Limit Adjustment)  
- **CLAPASSED=TRUE**: Confirms limit was adjusted immediately on Omaha platform

**Description** Enable members to request an increase to their credit limit.

**User Flow**

1. Member navigates to Credit Limit Increase  
2. System displays current credit limit and account status  
3. Member enters requested new limit  
4. System may request additional information:  
   - Annual income  
   - Employment status  
   - Housing payment  
5. Member submits request  
6. System submits to Velera Function 1424  
7. **If CLAPASSED=TRUE**: Immediate approval displayed with new limit  
8. **If pending**: "Request submitted for review" message with expected timeline

**Requirements**

- Display current limit and available credit  
- Allow member to specify requested limit  
- Collect required income/employment info if needed  
- Handle immediate approval (CLAPASSED=TRUE)  
- Handle pending review scenario

**Acceptance Criteria**

- AC1: Current limit and status displayed  
- AC2: Request submitted to Function 1424  
- AC3: Immediate approval handled when CLAPASSED=TRUE  
- AC4: Pending status displayed with timeline when not immediately approved  
- AC5: Notification sent upon final decision

#### FR-5.4: Installment Loan Payment {#fr-5.4:-installment-loan-payment}

**Applicable To**: SFCU only

**Velera API Reference**

- **Function ID 1465**: Retrieve available installment offers  
- **Function ID 1466**: Decline offer  
- **Function ID 1467**: Accept offer  
- **Eligibility**: Returns available offers for settled transactions

**Note**: Requires Velera enrollment at FI level. Contact PSCU Account Executive for enrollment.

**Description** Enable members to convert eligible purchases into fixed installment payment plans.

**User Flow**

1. Member views eligible transaction (or navigates to Installment Plans)  
2. System retrieves available offers via Function 1465  
3. For each eligible transaction, display:  
   - Original purchase amount  
   - Available plan options (3, 6, 12 months, etc.)  
4. Member selects transaction and plan  
5. System displays plan details:  
   - Monthly payment amount  
   - Number of payments  
   - Total interest/fees  
   - APR  
6. Member reviews and accepts  
7. System submits acceptance via Function 1467  
8. Confirmation with payment schedule displayed

**Requirements**

- Only show for settled (posted) transactions  
- Display multiple plan options when available  
- Clearly show total cost including interest/fees  
- Require acceptance of terms  
- Display payment schedule after enrollment

**Acceptance Criteria**

- AC1: Eligible offers retrieved via Function 1465  
- AC2: Plan details clearly displayed with total cost  
- AC3: Acceptance processed via Function 1467  
- AC4: Decline processed via Function 1466 if member cancels  
- AC5: Payment schedule displayed after enrollment
- AC5: Payment schedule displayed after enrollment

#### FR-5.5: Scheduled Payments (One-Time External) {#fr-5.5:-scheduled-payments}

**Applicable To**: SFCU Only

**Critical Branching Logic (Internal vs. External)**
To avoid late fees and interest charges, the system MUST route payment requests based on the funding source:
1. **Internal (SFCU Account)**: Process via Core Transfer / RTP.
2. **External (Non-SFCU Account)**: Process via **Velera API Function 1459**.

**Velera API Reference**
- **Function ID 1459**: Submit One-Time Future Dated Payment
- **Function ID 1460**: List/Inquiry of Scheduled Payments
- **Post-Date Logic**: As confirmed by Velera, payments submitted via Function 1459 will be recorded with the **Scheduled Date** as the **Effective/Post Date** on the member's statement, even if ACH settlement occurs 1-2 days later. This satisfies the "On-Time" requirement.

**Use Cases**
1. Member schedules a single payment for a future date (e.g., the Due Date).
2. Member views existing scheduled external payments.
3. Member cancels a scheduled external payment before the cutoff time.

**Requirements**
- **Date Selection**: Member can select any date up to the current Due Date (and beyond, subject to interest).
- **Acknowledgment**: System must display a message: "Payments from external accounts are credited as of your selected date, regardless of background settlement time."
- **Cutoff Management**: Enforce 5:00 PM ET (or as configured) cutoff for same-day scheduling.
- **View/Cancel**: Provide a "Scheduled Payments" list view using Function 1460 where members can delete pending requests.

**Acceptance Criteria**
- AC1: System correctly branches to Function 1459 for external sources.
- AC2: Member can select a future date for payment.
- AC3: Confirmation clearly shows the "Effective Payment Date."
- AC4: Scheduled payment appears in the "Pending/Scheduled" list view.
- AC5: Late fees are suppressed if the scheduled date matches the due date.

#### FR-5.6: Recurring Payments (AutoPay External) {#fr-5.6:-recurring-payments}

**Applicable To**: SFCU Only

**Description** Enable members to set up an automatic, recurring monthly pull from an external bank account to pay their credit card.

**Velera API Reference**
- **Function ID 1455**: AutoPay Management (Add/Update/Delete)

**Payment Options**
- **Minimum Payment Due**: Automatically pulls the minimum amount each month.
- **Statement Balance**: Automatically pulls the full balance from the last statement.
- **Fixed Amount**: Automatically pulls a user-defined dollar amount.

**Constraints**
- **Single Schedule**: Members are limited to **one** active recurring payment schedule at a time (similar to a travel notification).
- **External Only**: This requirement specifically covers the use of the Velera ACH engine for external accounts.

**Acceptance Criteria**
- AC1: Member can enroll in recurring payments using Function 1455.
- AC2: Member can choose between Minimum, Statement Balance, or Fixed.
- AC3: Enrollment success triggers a confirmation notification.
- AC4: Member can view and cancel the active schedule from the "Manage Card" screen.

#### FR-5.7: Posted Payments (History) {#fr-5.7:-posted-payments}

**Applicable To**: SFCU Only

**Description** Provide a dedicated view of payment-only history (separate from general transaction activity) to help members track their debt reduction.

**Velera API Reference**
- **Function ID 1414**: Payment History Inquiry

**Display Fields**
- Posting Date
- Payment Amount
- Payment Source (Channel/Method)
- Status (Posted/Reversed)

**Acceptance Criteria**
- AC1: Payment history retrieved via Function 1414.
- AC2: Chronological display of payments for the last 12-24 months.
- AC3: Clearly distinguishes between external ACH and internal transfers.

### FR-6: Dispute Management {#fr-6:-dispute-management}

#### FR-6.1: Dispute a Transaction {#fr-6.1:-dispute-transaction}

**Applicable To**: OUCU, SFCU, Diamond

**Velera API Reference**
- **Function ID 1458**: Submit Dispute Request

**Description** Allow members to report fraudulent or incorrect transactions directly from their transaction history.

**Requirements**
- Selection of transaction from history.
- Dropdown for dispute reason (Fraud, Incorrect Amount, Duplicate, Item Not Received).
- Text area for additional details.
- Warning that the card may be blocked/reissued if "Fraud" is selected.

### FR-7: Statement Management {#fr-7:-statement-management}

#### FR-7.1: Next Statement Date & eStatements {#fr-7.1:-next-statement-date}

**Applicable To**: SFCU only (Statement Date), All (eStatements)

**Velera API Reference**
- **Function ID 1402**: Card Summary (Retrieves NEXTSTMTDATE)

**Description** Keep members informed of their billing cycles and provide access to digital statements.

**Requirements**
- Display "Next Statement Date" on the main card tile or management screen.
- Provide a deep link to the eStatement portal.


#### FR-8.2: New User Account Created {#fr-8.2:-new-user-account-created}

**Applicable To**: OUCU, Diamond (TBD)

**Description** Send notification when a new authorized user is added to the account.

**Trigger**: Authorized user added via FR-3.1

**Notification Content**

- Authorized user name  
- Date added  
- Card delivery timeline

#### FR-8.3: Merchant Type Detected {#fr-8.3:-merchant-type-detected}

**Applicable To**: OUCU, Diamond (TBD)

**Velera API Reference**

- **Function ID**: 1762 (Set Card Policy)  
- **Alert Code**: Confirm with Velera

**Description** Send notification when a transaction occurs at a specific merchant category.

**Trigger**: Transaction at configured merchant category

**Configuration**

- Member selects which merchant categories trigger alerts  
- Alert threshold (optional \- only above certain amount)

#### FR-8.4: Transaction Type Detected {#fr-8.4:-transaction-type-detected}

**Applicable To**: OUCU, Diamond (TBD)

**Velera API Reference**

- **Function ID**: 1762 (Set Card Policy)

**Description** Send notification when a specific transaction type occurs.

**Trigger**: Transaction of configured type (ATM, International, Online, etc.)

**Configuration**

- Member selects which transaction types trigger alerts  
- Alert threshold (optional)

#### FR-8.5: User Credentials Reset {#fr-8.5:-user-credentials-reset}

**Applicable To**: OUCU, Diamond 

**Description** Send notification when PIN or other credentials are changed.

**Trigger**: PIN set/reset via FR-2.1

**Notification Content**

- Type of credential changed  
- Date/time of change  
- Device/channel used

## 5\. Non-Functional Requirements {#5.-non-functional-requirements}

### 5.1 Performance {#5.1-performance}

| Metric | Requirement |
| :---- | :---- |
| API Response Time | \< 3 seconds for all Velera API calls |
| Card Controls Update | \< 2 minutes to take effect |
| Page Load Time | \< 2 seconds |
| Card Status Refresh | \< 5 seconds |

### 5.2 Security {#5.2-security}

- MFA required for sensitive operations:  
  - PIN set/reset  
  - Card issuance  
  - Authorized user management  
  - Balance transfer  
- PIN encrypted via HSM before transmission to Velera  
- Session timeout after 15 minutes of inactivity  
- All API calls over TLS 1.2+  
- PCI DSS compliance for card data handling  
- Sensitive data (CVV, full card number) auto-hidden after 60 seconds

### 5.3 Availability {#5.3-availability}

- 99.9% uptime for card management features  
- Graceful degradation when Velera unavailable  
- Offline capability for viewing cached card data  
- Error messaging when services unavailable

### 5.4 Accessibility {#5.4-accessibility}

- WCAG 2.1 AA compliance  
- Screen reader support for all card information  
- Adequate color contrast for status indicators  
- Keyboard navigation support

## 6\. UX/UI Considerations {#6.-ux/ui-considerations}

### 6.1 Credit Card Tile CTAs {#6.1-credit-card-tile-ctas}

**Credit Card**: `[Manage Card]` `[Make Payment]` `[View Activity]`

**Debit Card**: `[View Account]` `[Manage Card]` `[View Activity]`

**Rationale**: "View Account" removed for credit cards because:

- Credit cards are standalone accounts, not linked to deposit accounts  
- "Manage Card" and "View Activity" are clearer CTAs for credit cards  
- "Make Payment" is the most critical action for credit card users

### 6.2 Visual Indicators {#6.2-visual-indicators}

| Condition | Treatment |
| :---- | :---- |
| Payment due within 7 days | Orange/warning color |
| Payment past due | Red/error color |
| Card locked | Red indicator |
| Card unlocked | Green indicator |
| Authorized user | Badge label |
| Processing status | Yellow/pending indicator |

## 7\. Dependencies & Open Items {#7.-dependencies-&-open-items}

### 7.1 Diamond TBD Items \- Clarification Needed {#7.1-diamond-tbd-items---clarification-needed}

| Feature | Current Status | Action Required |
| :---- | :---- | :---- |
| FR-1.1 Order New Card | TBD | Confirm with Velera if supported |
| FR-1.4 Digital Issuance | TBD | Confirm with Velera if supported |
| FR-4.1 Decline Merchant Types | Not confirmed | Confirm if Ondot integration available |
| FR-4.2 Decline Transaction Types | Not confirmed | Confirm if Ondot integration available |
| FR-4.3 Update Cards on File | TBD | Check with Velera how this is done |
| FR-5.3 Credit Limit Increase | TBD | Explore Meridian Link option instead of Velera |
| FR-8.x Alerts | Not confirmed | Confirm which alerts are supported |

### 7.2 Velera Enrollments Required {#7.2-velera-enrollments-required}

| Feature | Enrollment Required |
| :---- | :---- |
| Balance Consolidation | Contact PSCU Account Executive for eBalCon enrollment |
| Installment Payments | Requires Velera enrollment at FI level |
| Cards on File | Must be configured in eMessenger platform |

### 7.3 Velera API Function Reference {#7.3-velera-api-function-reference}

| Function ID | Name | Used By |
| :---- | :---- | :---- |
| 1346 | CVV Inquiry | FR-1.4 Digital Issuance |
| 1402 | Card Summary | FR-7.1 Next Statement Date |
| 1404 | Update Cardholder Information | FR-3.1 Authorized Users |
| 1409 | Order Damage Replacement Card | FR-1.2 Replacement Card |
| 1414 | Payment History | FR-5.7 Posted Payments |
| 1423 | Extended Cardholder Information | FR-3.1 View Authorized Users |
| 1424 | Credit Limit Adjustment | FR-5.3 Credit Limit Increase |
| 1439 | Balance Consolidation | FR-5.1 Balance Transfer |
| 1440 | New Cardholder Account | FR-1.1 Order New Card |
| 1444 | Set PIN Offset | FR-2.1 Set/Reset PIN |
| 1445 | PIN Verification Number | FR-2.1 Set/Reset PIN |
| 1455 | AutoPay Management | FR-5.6 Recurring Payments |
| 1458 | Submit Dispute | FR-6.1 Dispute Management |
| 1459 | Submit One-Time Payment | FR-5.5 Scheduled Payments |
| 1460 | List Scheduled Payments | FR-5.5 Scheduled Payments |
| 1465 | Retrieve Installment Offers | FR-5.4 Installment Plans |
| 1466 | Decline Installment Offer | FR-5.4 Installment Plans |
| 1467 | Accept Installment Offer | FR-5.4 Installment Plans |
| 1480 | Cardholder Plastics | FR-1.3 Track Card |
| 1481 | EMV PIN Change | FR-2.1 PIN Change |
| 1485 | Cash Advance Authorization | FR-5.2 Cash Advance |
| 1486 | Cash Advance Post Transaction | FR-5.2 Cash Advance |
| 1491 | Omaha PIN Resets | FR-2.1 Reset PIN Counter |
| 1622 | Merchant List Retrieval | FR-4.3 Cards on File |
| 1623 | Card Upsert | FR-4.3 Cards on File |
| 1762 | Set Card Policy (Ondot) | FR-4.1, FR-4.2, FR-8.x Alerts |

#### 

#### 

[image1]: <data:image/png;base64,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>