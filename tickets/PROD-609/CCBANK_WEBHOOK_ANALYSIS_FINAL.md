# CCBank Card Suite Webhook Events - Implementation Analysis
**Project**: PROD-609 | **Date**: December 28, 2025 | **Prepared By**: Aditya Raj

---

## Executive Summary

**CRITICAL FINDING**: CCBank is implementing:
- **Mobile**: Experience SDK Pro (full feature set)
- **Web**: Card Suite Pro **APIs** (NOT Web SDK Lite)

**SCOPE CLARIFICATION**:
- **Primary Channels**: **In-App & Push Notifications** are the core focus for the January release.
- **Secondary Channel**: **Email** will be used for audit trail/security confirmations.
- **Optional Channel**: **SMS** is currently categorized as *Optional/TBD* as there is no record of an SMS gateway contract in PROD-609 history.

This means we have FULL ACCESS to all 28 webhook events via APIs on both platforms. The question is not what's supported, but **what creates the best user experience**.

---

## 1. Platform Architecture Understanding

### What CCBank Actually Has:

**Mobile App**:
- Experience SDK Pro 2.9.1+
- Full UI provided by FIS
- All 28 events supported
- ✅ Card activation, disputes, wallet integration, PIN changes, etc.

**Web/Online Banking**:
- Card Suite Pro APIs (confirmed Oct 29, 2025 per comment history)
- We build the UI
- All 28 events supported via webhook APIs
- ✅ No SDK limitations - full API access

### What This Means:
🎯 **We're not limited by SDK compatibility** - All events are available via APIs for both platforms.

---

## 2. User Experience-Driven Event Classification

### Category A: MUST-HAVE - Critical Security & Fraud (Real-time Push Notifications)

These events prevent fraud and require IMMEDIATE customer notification:

| Event | User Experience Reason | Push | SMS (Opt) | Email |
|-------|------------------------|------|-----------|-------|
| **CARD_REPORTED** | Card lost/stolen - block immediately | ✅ | ❓ TBD | ✅ |
| **CARD_PIN_CHANGED** | Unauthorized PIN change indicator | ✅ | ❓ TBD | ✅ |
| **DECLINED_ON_POLICY** | Why transaction failed (Controls) | ✅ | ❌ | ❌ |
| **CARD_FROZEN** | Confirm freeze action | ✅ | ❌ | ❌ |
| **CARD_ACTIVATED** | New card ready to use | ✅ | ❌ | ✅ |

**Note on SMS**: SMS implementation is technically feasible but requires CCBank to confirm their SMS gateway provider and per-message budget.


---

### Category B: HIGH-VALUE - Transaction Awareness (Configurable Push)

Let customers CHOOSE if they want these (notification fatigue risk):

| Event | User Experience Reason | Default Setting | Configurable |
|-------|------------------------|-----------------|--------------|
| **APPROVED** | Every purchase confirmation | ❌ OFF (fatigue) | ✅ User can enable for high amounts |
| **TRANSACTIONS_APPROVED (Alert)** | Custom alert for specific conditions | ✅ ON for >$500 | ✅ User sets threshold |
| **TRANSACTION_DECLINED_ON_POLICY (Alert)** | Custom decline alerts | ✅ ON | ✅ User can disable |

**Best Practice**:
- Default: Only notify for transactions **>$500** (customer configurable)
- Let users set their own threshold ($100, $250, $500, $1000, or ALL)
- Reduce notification fatigue while maintaining security

**Example User Settings**:
```
Notify me for transactions:
○ Over $100
○ Over $500 (recommended)
● Over $1000
○ All transactions
○ Never
```

---

### Category C: CUSTOMER EMPOWERMENT - Control Confirmations (In-App + Email)

User takes action, gets confirmation:

| Event | User Experience | Channel |
|-------|-----------------|---------|
| **SPEND_LIMIT_UPDATED** | "Your daily limit is now $500" | In-App + Email |
| **CATEGORY_UPDATED** | "Gas stations are now blocked" | In-App |
| **LOCATION_UPDATED** | "Card will only work in USA" | In-App + Email |
| **INTERNATIONAL_CONTROL_TOGGLE** | "International purchases enabled" | In-App + Email |
| **ONE_TIME_OVERRIDE_UPDATED** | "Netflix payment allowed for 24 hours" | In-App |
| **CARD_ARCHIVED** | "Card moved to archive" | In-App |
| **CARD_DELETED** | "Card removed permanently" | In-App + Email |

**Why in-app works**:
- User just performed the action in the app
- Confirmation appears immediately
- Email for reference/audit trail

---

### Category D: CARD LIFECYCLE - System Events (Email + In-App)

Bank-initiated events customer needs to track:

| Event | User Experience | Why Email is Better |
|-------|-----------------|---------------------|
| **NEW_CARD_ISSUED** | "New card issued, arriving in 7-10 days" | Customer may not check app daily |
| **REPLACEMENT_CARD_ISSUED** | "Replacement card on the way" | Important for card tracking |
| **CARD_REISSUANCE_REQUESTED** | "Your reissue request is being processed" | Confirmation of request |

**Experience SDK Pro Feature**: These are version 2.9.1+ events - CCBank has access on mobile.

---

### Category E: DIGITAL WALLET - Modern Banking (Push + In-App)

Apple Pay/Google Pay integration:

| Event | User Experience | Channel |
|-------|-----------------|---------|
| **CARD_ADDED_TO_WALLET** | "Card ready for Apple Pay" | Push + In-App |

**Why this matters**:
- Confirms successful wallet provisioning
- Security confirmation (if customer didn't add it, they know to check)
- Drives wallet adoption

---

### Category F: CREDIT CARD PAYMENTS - Payment Tracking (Email)

For credit card holders:

| Event | User Experience | Channel |
|-------|-----------------|---------|
| **CREDIT_CARD_PAYMENT_INITIATED** | Payment scheduled confirmation | Email + In-App |
| **CREDIT_CARD_PAYMENT_CANCELED** | Payment cancellation notice | Email + Push |

**Experience SDK Pro 2.9.1+ Feature** - CCBank has access.

---

### Category G: DISPUTES - Fraud Protection (Email + In-App)

| Event | User Experience | Channel |
|-------|-----------------|---------|
| **DISPUTE_RAISED** | "Dispute submitted, confirmation #12345" | Email + In-App |
| **DISPUTE_STATUS_UPDATED** | "Your dispute is under review/approved/denied" | Email + Push (if approved/denied) |

**Experience SDK Pro Feature** - Mobile only (not on Web SDK Lite, but CCBank uses APIs for web, so supported).

---

### Category H: ADVANCED CONTROLS - Power User Features (In-App Only)

| Event | User Experience | Notification Strategy |
|-------|-----------------|----------------------|
| **CARD_SHARING_UPDATED** | Shared user added/removed | In-App (low priority) |
| **CARD_ADDED** | Manual card addition confirmed | In-App (immediate) |
| **HOME_COUNTRY_UPDATED** | Home country changed | In-App |
| **RECURRING_MERCHANT_UPDATED** | Recurring merchant blocked/unblocked | In-App |
| **LOCATION_STALED** | "Update your location for Location Shield" | In-App (can become annoying) |

**LOCATION_STALED Warning**: This can fire frequently if user doesn't open app regularly. Consider:
- Only notify after 7 days of staleness
- Don't spam users who rarely travel

---

## 3. REAL User Experience Recommendations

### Phase 1: Go-Live (January 2026) - 15 Events

**Security-Critical (5 events)**:
1. CARD_REPORTED ⚠️ CRITICAL
2. CARD_PIN_CHANGED ⚠️ CRITICAL
3. CARD_FROZEN ⚠️ CRITICAL
4. CARD_ACTIVATED ⚠️ CRITICAL
5. DECLINED_ON_POLICY ⚠️ CRITICAL

**Transaction Awareness (2 events)**:
6. TRANSACTIONS_APPROVED (Alert) - configurable threshold
7. TRANSACTION_DECLINED_ON_POLICY (Alert)

**Control Confirmations (5 events)**:
8. SPEND_LIMIT_UPDATED
9. LOCATION_UPDATED
10. INTERNATIONAL_CONTROL_TOGGLE
11. CATEGORY_UPDATED
12. CARD_DELETED

**Card Lifecycle (2 events)**:
13. NEW_CARD_ISSUED
14. REPLACEMENT_CARD_ISSUED

**Digital Wallet (1 event)**:
15. CARD_ADDED_TO_WALLET

**Rationale**: These 15 events cover:
- ✅ All security/fraud scenarios
- ✅ Transaction monitoring with user control
- ✅ Key card lifecycle events
- ✅ Modern digital wallet integration
- ✅ Control change confirmations

---

### Phase 2: Post Go-Live (30-60 days) - 8 Events

**Credit Card Features (2 events)**:
16. CREDIT_CARD_PAYMENT_INITIATED
17. CREDIT_CARD_PAYMENT_CANCELED

**Disputes (2 events)**:
18. DISPUTE_RAISED
19. DISPUTE_STATUS_UPDATED

**Advanced Controls (3 events)**:
20. ONE_TIME_OVERRIDE_UPDATED
21. CARD_REISSUANCE_REQUESTED
22. CARD_ARCHIVED

**Transaction Approval (1 event)**:
23. APPROVED (OFF by default, user configurable)

---

### Phase 3: Power Users (90+ days) - 5 Events

24. CARD_SHARING_UPDATED
25. CARD_ADDED
26. HOME_COUNTRY_UPDATED
27. RECURRING_MERCHANT_UPDATED
28. LOCATION_STALED (with 7-day throttling)

---

## 4. Critical Implementation Decisions

### Decision 1: APPROVED vs TRANSACTIONS_APPROVED (Alert)

**Problem**: These are similar but different:
- **APPROVED**: Every single transaction (100+ per month for active users)
- **TRANSACTIONS_APPROVED (Alert)**: Custom alert with configurable conditions

**Recommendation**:
- ❌ DON'T enable APPROVED by default (notification fatigue)
- ✅ Use TRANSACTIONS_APPROVED (Alert) with threshold logic
- ✅ Let users opt-in to APPROVED if they want every transaction

**Implementation**:
```javascript
// Backend logic
if (transaction.amount > user.notification_threshold) {
  sendNotification(TRANSACTIONS_APPROVED_ALERT);
}
```

---

### Decision 2: Location Shield Staleness

**Problem**: LOCATION_STALED can fire constantly for users who:
- Don't travel frequently
- Don't open app regularly
- Have Location Shield enabled but inactive lifestyle

**Recommendation**:
- Only notify after 7+ days of staleness
- Include helpful action: "Open app to update location"
- Don't repeat notification for 30 days

---

### Decision 3: Multi-Channel Strategy

| Priority | Push | SMS (Optional) | Email | In-App |
|----------|------|----------------|-------|--------|
| **Security Events** | ✅ Always | ❓ TBD | ✅ Always | ✅ Always |
| **Transaction Alerts** | ✅ Configured | ❌ No | ❌ No | ✅ Always |
| **Control Changes** | ❌ No | ❌ No | ✅ Important | ✅ Always |
| **Card Lifecycle** | ❌ No | ❌ No | ✅ Always | ✅ Always |

**SMS Cost & Scope Consideration**:
- **Status**: Currently classified as "Secondary/Optional" for Jan Go-Live.
- **Requirement**: Needs CCBank to confirm an active SOW for SMS gateway integration.


---

## 5. Notification Templates - User-Centric Language

### Security Events (Urgent, Action-Oriented)

**CARD_REPORTED (CRITICAL)**
```
🔒 SECURITY ALERT: Your card ending in <%=data.pan.last4%> has been reported <%=data.attributes.reported_reason%> and is now blocked for your protection. A replacement card will arrive in 7-10 business days.

Didn't report this? Call us immediately: 1-800-XXX-XXXX
```

**CARD_PIN_CHANGED (CRITICAL)**
```
🔒 SECURITY ALERT: Your card PIN was changed on <%=new Date(data.event_timestamp).toLocaleString()%>.

Didn't make this change? Call us immediately: 1-800-XXX-XXXX or freeze your card in the app.
```

**DECLINED_ON_POLICY**
```
❌ Transaction declined

Your <%=data.attributes.merchant_name%> purchase of <%=data.attributes.currency%><%=data.attributes.amount%> was declined due to: <%=data.attributes.reason%>

Tap to adjust your card controls
```

**CARD_FROZEN**
```
🧊 Card Frozen

Your card ending in <%=data.pan.last4%> is frozen. You can still use it for autopay/subscriptions.

Tap to unfreeze
```

**CARD_ACTIVATED**
```
✅ Card Activated

Your card ending in <%=data.pan.last4%> is ready to use! Start shopping securely.
```

---

### Transaction Alerts (Informative, Brief)

**TRANSACTIONS_APPROVED (Alert) - Over Threshold**
```
💳 Transaction Alert

<%=data.attributes.merchant_name%>
<%=data.attributes.currency%><%=data.attributes.amount%>
<%=new Date(data.attributes.transaction_time_epoch).toLocaleString()%>
<%=data.attributes.location_city%>, <%=data.attributes.location_state%>

Not you? Report fraud →
```

**TRANSACTION_DECLINED_ON_POLICY (Alert)**
```
🛑 Transaction Blocked

We blocked a <%=data.attributes.merchant_name%> transaction (<%=data.attributes.currency%><%=data.attributes.amount%>) based on your card controls.

Need to allow it? Tap to adjust controls
```

---

### Control Confirmations (Clear, Reassuring)

**SPEND_LIMIT_UPDATED**
```
✅ Spend Limit Updated

Your new limits:
• Daily: <%=data.attributes.daily_limit > 0 ? data.attributes.currency + data.attributes.daily_limit : 'No limit'%>
• Monthly: <%=data.attributes.monthly_limit > 0 ? data.attributes.currency + data.attributes.monthly_limit : 'No limit'%>
• Per Transaction: <%=data.attributes.per_transaction_limit > 0 ? data.attributes.currency + data.attributes.per_transaction_limit : 'No limit'%>
```

**CATEGORY_UPDATED**
```
<%=data.attributes.status === 'ALLOWED' ? '✅' : '🚫'%> Category Control Updated

<%=data.attributes.merchant_category%> transactions are now <%=data.attributes.status === 'ALLOWED' ? 'allowed' : 'blocked'%> on your card.
```

**LOCATION_UPDATED**
```
📍 Location Control Updated

<%=data.attributes.region_name%> has been <%=data.attributes.region_name_status%> for card transactions.

<%=data.attributes.date_range_start_date ? 'Active: ' + data.attributes.date_range_start_date + ' to ' + data.attributes.date_range_end_date : ''%>
```

**INTERNATIONAL_CONTROL_TOGGLE**
```
🌍 International Purchases <%=data.attributes.international_control_status === 'ENABLED' ? 'Enabled' : 'Disabled'%>

Your card can <%=data.attributes.international_control_status === 'ENABLED' ? 'now' : 'no longer'%> be used for international transactions.
```

---

### Card Lifecycle (Informative, Tracking)

**NEW_CARD_ISSUED**
```
📬 New Card Issued

Your new Capital Community Bank card has been issued and will arrive within 7-10 business days.

Track your card → [link]
```

**REPLACEMENT_CARD_ISSUED**
```
📬 Replacement Card Issued

Your replacement card for the card ending in <%=data.attributes.previous_pan_plain_text ? data.attributes.previous_pan_plain_text.slice(-4) : 'XXXX'%> has been issued.

Expected arrival: 7-10 business days
Your old card will stop working when you activate the new one.
```

**CARD_REISSUANCE_REQUESTED**
```
✅ Reissue Request Received

We're processing your card reissue request. Your new card will arrive within 7-10 business days.

Questions? Contact support
```

---

### Digital Wallet (Modern, Exciting)

**CARD_ADDED_TO_WALLET**
```
🎉 Card Added to <%=data.attributes.wallet === 'APPLE_PAY' ? 'Apple Pay' : 'Google Pay'%>

Your card ending in <%=data.pan.last4%> is ready for tap-to-pay!

Start using it at millions of stores worldwide.
```

---

### Credit Card Payments (Clear, Confirmatory)

**CREDIT_CARD_PAYMENT_INITIATED**
```
💰 Payment Scheduled

Amount: <%=data.attributes.currency%><%=data.attributes.payment_amount%>
From: Account ending in <%=data.attributes.payment_account_last4%>
Scheduled: <%=data.attributes.payment_date%>
Payment ID: <%=data.attributes.payment_id%>

Cancel payment →
```

**CREDIT_CARD_PAYMENT_CANCELED**
```
❌ Payment Canceled

Your payment of <%=data.attributes.currency%><%=data.attributes.payment_amount%> scheduled for <%=data.attributes.payment_date%> has been canceled.

Payment ID: <%=data.attributes.payment_id%>
```

---

### Disputes (Professional, Tracking)

**DISPUTE_RAISED**
```
✅ Dispute Submitted

Transaction: <%=data.attributes.merchant_name%>
Amount: <%=data.attributes.currency%><%=data.attributes.amount%>
Status: <%=data.attributes.dispute_status%>
Confirmation: <%=data.attributes.confirmation_id%>

We'll review your dispute and respond within 10 business days.

Track dispute →
```

**DISPUTE_STATUS_UPDATED**
```
📋 Dispute Status Update

Confirmation: <%=data.attributes.confirmation_id%>
New Status: <%=data.attributes.dispute_status%>

Transaction: <%=data.attributes.merchant_name%> (<%=data.attributes.currency%><%=data.attributes.amount%>)

View details →
```

---

### Advanced Controls (Brief, Informative)

**ONE_TIME_OVERRIDE_UPDATED**
```
⏰ One-Time Override Active

<%=data.attributes.merchant_name%> (<%=data.attributes.currency%><%=data.attributes.amount%>) is temporarily allowed.

Expires: <%=new Date(data.attributes.override_end_time).toLocaleString()%>
```

**CARD_ARCHIVED**
```
📦 Card Archived

Your card ending in <%=data.pan.last4%> has been moved to archived cards.

Restore card →
```

**CARD_DELETED**
```
🗑️ Card Removed

Your card ending in <%=data.pan.last4%> has been permanently removed from your account.
```

**CARD_SHARING_UPDATED**
```
👥 Shared User <%=data.attributes.shared_card_action === 'ADDED' ? 'Added' : 'Removed'%>

A shared user has been <%=data.attributes.shared_card_action%> to your card account.

Manage shared users →
```

**CARD_ADDED**
```
✅ Card Added

Your card ending in <%=data.pan.last4%> has been successfully added to Card Suite.
```

**HOME_COUNTRY_UPDATED**
```
🏠 Home Country Updated

Your home country has been changed from <%=data.attributes.current_home_country_code%> to <%=data.attributes.new_home_country_code%>.
```

**RECURRING_MERCHANT_UPDATED**
```
🔄 Recurring Merchant <%=data.attributes.status === 'BLOCKED' ? 'Blocked' : 'Unblocked'%>

Recurring transactions for <%=data.attributes.merchant_name%> are now <%=data.attributes.status%>.
```

**LOCATION_STALED**
```
📍 Location Update Needed

Your Location Shield hasn't been updated in <%=Math.floor((Date.now() - data.attributes.lastLocationUpdatedAt) / (1000 * 60 * 60 * 24))%> days.

Open the app to refresh your location for Location Shield to work properly.

Update now →
```

---

## 6. What You Need to Tell Stakeholders (Pradeep, CCBank, FIS)

### For Pradeep & Engineering Team:

**Recommendation**: Implement 15 events for go-live (Phase 1)

**Key Points**:
1. ✅ All 28 events are supported via Card Suite Pro APIs (no SDK limitations)
2. ✅ Experience SDK Pro 2.9.1+ gives mobile access to all features
3. ⚠️ APPROVED transaction event should be OFF by default (notification fatigue)
4. ✅ Use TRANSACTIONS_APPROVED (Alert) with configurable threshold instead
5. ⚠️ SMS should be reserved for critical security events only (cost consideration)

**Technical Requirements**:
- Webhook endpoint with HTTPS + authentication
- AES-256 GCM decryption for PAN data
- Multi-channel delivery: Push, SMS, Email, In-App
- User notification preferences system
- Threshold configuration for transaction alerts

---

### For CCBank:

**Questions for Bank Approval**:

1. **Transaction Notifications**:
   - Should we notify for ALL transactions or only above a threshold?
   - Recommended: Default to $500+, let users configure

2. **SMS Strategy Confirmation**:
   - SMS is currently proposed as an *Optional* channel for Phase 1.
   - Does CCBank wish to proceed with SMS for critical fraud alerts (`CARD_REPORTED`, `CARD_PIN_CHANGED`)?
   - If yes, please provide details for the SMS gateway/provider.

3. **Dispute Features**:
   - Do you want customers to dispute transactions via mobile app?
   - This requires DISPUTE_RAISED and DISPUTE_STATUS_UPDATED webhooks

4. **Digital Wallet Priority**:
   - Is Apple Pay/Google Pay a go-live requirement?
   - Requires CARD_ADDED_TO_WALLET webhook

5. **Credit Card Payments**:
   - Do you issue credit cards or only debit?
   - If debit only, we can skip CREDIT_CARD_PAYMENT events

---

### For FIS Vendor:

**Technical Questions**:

1. **Auto-Enrollment Issue** (from Pradeep's Dec 16 query):
   - Auto enrollment creates users but doesn't enroll cards
   - Need confirmation: Does auto-enrollment work in sandbox?
   - Request: Updated sandbox test credentials

2. **SDK Authentication Issue**:
   - Test user: Dexter Spencer (card ending ***1028)
   - Getting "unauthorized access error" when launching Experience SDK
   - Request: Verify sandbox authentication token generation

3. **Webhook Delivery SLA**:
   - What's the expected latency for webhook delivery?
   - What's the retry policy for failed webhooks?
   - Are there rate limits on webhook events?

4. **Event Customization**:
   - Can we customize the Alert category threshold logic on FIS side?
   - Or do we need to implement threshold filtering on our webhook endpoint?

---

## 7. Implementation Roadmap

### Week 1-2: Planning & Approvals
- [ ] Get CCBank approval on 15 go-live events
- [ ] Get template approval from CCBank marketing/compliance
- [ ] Resolve FIS sandbox issues (auto-enrollment, SDK auth)
- [ ] Finalize notification channel strategy (Push/SMS/Email)

### Week 3-4: Development
- [ ] Build webhook endpoint (HTTPS + auth + AES-256 decryption)
- [ ] Integrate multi-channel delivery (Push, SMS via Twilio, Email)
- [ ] Build user notification preferences UI
- [ ] Implement transaction threshold logic
- [ ] Create in-app notification center

### Week 5-6: Testing
- [ ] Sandbox testing for all 15 Phase 1 events
- [ ] Test template rendering with real data
- [ ] Test multi-channel delivery
- [ ] Load testing (webhook rate limits)
- [ ] UAT with CCBank stakeholders

### Week 7: Production Deployment
- [ ] Production webhook configuration
- [ ] Monitor event delivery
- [ ] Monitor notification delivery rates
- [ ] Collect customer feedback

### Post Go-Live (30-60 days):
- [ ] Analyze notification engagement rates
- [ ] Identify notification fatigue patterns
- [ ] Implement Phase 2 events (8 events)
- [ ] Optimize based on customer feedback

---

## 8. Success Metrics

### Customer Engagement:
- Push notification open rate > 40%
- Email open rate > 25%
- In-app notification engagement > 60%

### Security Effectiveness:
- Time to customer awareness for CARD_REPORTED < 5 minutes
- Fraud detection improvement via DECLINED_ON_POLICY insights

### Notification Quality:
- Unsubscribe rate < 5%
- Customer complaints about spam < 2%

---

## 9. Risk Mitigation

### Risk 1: Notification Fatigue
**Mitigation**:
- Default APPROVED to OFF
- Use thresholds for transaction alerts
- Let users customize notification preferences

### Risk 2: SMS Costs
**Mitigation**:
- Limit SMS to critical security events only
- Set monthly SMS budget caps
- Monitor per-user SMS usage

### Risk 3: Webhook Failures
**Mitigation**:
- Implement retry logic with exponential backoff
- Dead letter queue for failed webhooks
- Monitor webhook delivery SLA
- Alert on webhook endpoint downtime

### Risk 4: PAN Data Security
**Mitigation**:
- Encrypt PAN data in transit and at rest
- Never log unencrypted PAN data
- Implement PCI-DSS compliant storage
- Regular security audits

---

## 10. Final Recommendation Summary

### Phase 1 - Go-Live (15 Events):

**Security (5)**: CARD_REPORTED, CARD_PIN_CHANGED, CARD_FROZEN, CARD_ACTIVATED, DECLINED_ON_POLICY

**Transaction Monitoring (2)**: TRANSACTIONS_APPROVED (Alert), TRANSACTION_DECLINED_ON_POLICY (Alert)

**Control Confirmations (5)**: SPEND_LIMIT_UPDATED, LOCATION_UPDATED, INTERNATIONAL_CONTROL_TOGGLE, CATEGORY_UPDATED, CARD_DELETED

**Card Lifecycle (2)**: NEW_CARD_ISSUED, REPLACEMENT_CARD_ISSUED

**Digital Wallet (1)**: CARD_ADDED_TO_WALLET

### Notification Strategy:
- **Push**: Security events + configurable transaction alerts
- **SMS**: CARD_REPORTED, CARD_PIN_CHANGED only
- **Email**: All events for audit trail
- **In-App**: All events

### User Control:
- Let users set transaction notification threshold
- Let users enable/disable non-security events
- Provide granular notification channel preferences

---

**Next Action**: Review this with Pradeep, get CCBank approval, and resolve FIS sandbox issues before development kickoff.

---

**Document Version**: 2.0 (Final)
**Last Updated**: December 28, 2025
