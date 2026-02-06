
# 🎫 PROD-257: Phase 3 | Velera (Credit & Debit) Card Management | API

**Status**: `4. Requirements Definition` | **Priority**: `Medium` | **Assignee**: `Aditya Raj` | **Due Date**: `None`
**Jira Link**: https://tyfone.atlassian.net//browse/PROD-257

---

## 📄 Jira Description
OUCU Post Go Live November 15, 2025
Diamond
 
Post Go Live November 30, 2025
These are new features to be implemented as post-go-live items for OUCU, Diamond & Self-Reliance.
We need to carry forward the vendor-agnostic approach from UX2.0 to UX2.xx for all the new customers. Self-Reliance items tagged as in platform in the tracker below are delivery items. 
Order New Card & VISA Digital issuance:
Order New Card
Order Replacement Card
Track Plastic Card
Set Reset PIN + Notification
VISA | SDK | Digital Issuance
Authorized Users | Add Users
Mobile Wallet | In-App Push Provisioning | VISA
Payments
Balance Transfer to FI Card (Balance Consolidation) + Notification
Cash Advance Request
Credit Limit Increase Request (Link to Application)
Card Controls
     Decline Certain Merchant Types
     Decline Certain Transaction Types
Alerts
     Balance Consolidation is Submitted
     New Email Address is Created
     New User Account is Created
     Specific Merchant Type is Detected
     Specific Transaction Type is Detected
     User Credentials are Reset
     Installment Loan Payments ( add-on by Velera - Self reliance has signed up for it)
Out of Scope:
Update Cards on File
Recordings of PSCU UI:
 
 
 

## 📎 Attachments
_No attachments_

## 💬 Comments History
**KrishnaDeepthi K** (2025-07-02T09:15:35.038+0530):
> ,​​ Please fix a version for Velera phase 3 deliverables 

**KrishnaDeepthi K** (2025-07-10T11:12:21.591+0530):
>  
 
 ,  
please review the post-go-live commitments and confirm if there are no changes to the current ask
. If there’s anything we should be aware of from recent conversations with the CU, kindly share it here before we proceed. This is the scope as previously discussed with Diamond and OUCU.
cc: 
 
 
 
 
 

**Jamie Hancock** (2025-07-17T00:38:22.459+0530):
>  I have reviewed the scope and everything that is expected, is accounted for.

**Jennifer Harrison** (2025-07-26T00:17:48.971+0530):
>  
 
 are we truly tracking these items for November for OUCU?
Some of these items are contractual obligations which I believe will preclude us from billing OUCU at 100% until we deliver.
CC: 
 
 
 
 

**KrishnaDeepthi K** (2025-08-21T11:54:44.699+0530):
>  please add the fix version 
cc: 
 
 

**KrishnaDeepthi K** (2025-08-21T12:15:20.692+0530):
>  
 could you confirm the “need by date” for the feature by OUCU and Diamond? 

**KrishnaDeepthi K** (2025-08-21T12:31:06.535+0530):
>  , from your sheet attached below, I see this is tracked as post go-live for Diamond and OUCU correlation migration release, hence assigned the 10.48
 
cc: 
 Please confirm the if SOW is signed by Self reliance and does it include and specific date?

**Automation for Jira** (2025-08-21T12:31:29.204+0530):
> Engineering Lead Assigned:  
 ,  
 

**KrishnaDeepthi K** (2025-08-29T12:37:31.436+0530):
>  
 
  , please take a look at my 21st August comment and confirm if there is any risk associated with the 10.48 release date.
cc: 
 
 
 

**Aditya M** (2025-09-02T03:07:21.984+0530):
>  
 
 
Based on the initial analysis we have re-categorized the requirements. Please confirm this is accurate. 
Apart from the above, we also had few OUCU feedback items that needs to be supported: 
For each of the above i cannot see detailed requirement documents. Can you please provide the same? 
cc: 
 
 

**KrishnaDeepthi K** (2025-09-18T12:39:48.711+0530):
> ,  I have set up a call today with Jamie to review the items and clarify the scope. So that we can get started on these. As far as Digital issuance is concerned, from the sheets shared with me, I have only seen VISA as a vendor. When you mention the Velera API, I’m assuming it’s not a direct VISA integration, but rather a Velera API that internally calls VISA?
Also, I needed a confirmation from you if we have all the necessary API & SDK documentation to proceed with below features, or should we reach out to Velera or CU?
cc: 
 
 
  

**KrishnaDeepthi K** (2025-10-06T15:12:49.078+0530):
>  
  
  , 
please confirm the scope of the requirements discussed in the email [ 
's response] with the respective CUs. 
Once you’ve gathered the necessary clarifications, kindly schedule a follow-up session with the Velera team to review these features in detail and to ensure the engineering team addresses any technical questions. 
Please add Aditya, Pradeep, Dinesh, Ranjan and me to the call with Velera.
To stay on track for 10.48 Release, I plan to finalise the requirements by mid-next week, so it would be great to have the scope confirmation completed before then.
Appreciate your support in driving this forward.
cc: 
 
 
 
 
 

**Ashish Behera** (2025-10-06T21:44:26.955+0530):
> Hi
 ,
For Selfreliance there is
 no digital issuance and push provisioning. 
There important use case for Selfreliance FCU is Loan Installments. 
This is a copy of the SOW sent for their signing, 
  
Deliverables for the credit card API for your review is here. 

**Jennifer Harrison** (2025-10-15T07:07:26.258+0530):
>  I have copied you on an email to OUCU with some questions. I will also copy and paste below those items which I have listed as features we’re building for OUCU’s Credit Cards and Debit Cards:
Credit Cards:
Debit Cards:

**KrishnaDeepthi K** (2025-10-15T13:52:02.728+0530):
>  
, could you please review the existing Velera documents and analyze what’s missing from the scope listed above? Kindly share a list of open questions and any additional details needed to complete the analysis. I’ve also requested the DM to set up a call with the Velera team where we can get the open questions addressed. Please share the list by Friday EOD.

**KrishnaDeepthi K** (2025-10-15T13:56:50.522+0530):
> ,  as mentioned in the email, once you’ve received confirmation on the scope from all three CUs, please set up a call with the Velera team to clarify the open questions. You may use this thread to track the list of documents and follow-up questions for both Velera and the CUs.
attn: 
 
 
 
 
 

**KrishnaDeepthi K** (2025-10-23T12:42:42.721+0530):
>  
 Any update here?

**KrishnaDeepthi K** (2025-10-30T16:14:43.256+0530):
> OUCU scope is finalised in yesterday's (OCT 29th) call, they are not going for VISA integration all the features listed in the scoping document below are contracted with Velera. 
NOTE: Phase 3 shall be implemented on correlation core as confirmed by OUCU.
  (edited) 
 as discussed please followup on below action items from yesterday’s call with OUCU 
MOM from yesterday’s (29th OCT) call with OUCU
 
 
 
 
 

**Ashish Behera** (2025-11-12T03:43:49.094+0530):
> Hi 
 ,
Here is the confirmed list of use cases for Selfreliance which is part of the SOW they are signing, 
  
Please note Installment Loans is the most important ask for Selfreliance as part of the Phase 3 development. 
It would be helpful if you can confirm the delivery line items in this sheet for the DM to track- 
  
 we will need to plan the delivery line items once marked by 
 

**Automation for Jira** (2025-11-17T09:02:52.592+0530):
> 🔔 
Action Required: Update Missing Critical Fields
One or more critical fields need to be updated for this ticket.
Details:
Missing Fields:
• Engineering Lead: ❌ Not set
• T-shirt Size: ❌ Not set
• Customer Name: ❌ Not set
• Product: ❌ Not set
• Platform: ❌ Not set
• Product Area: ❌ Not set
• Category: ❌ Not set
• Source: ❌ Not set
• SOW | Project: ❌ Not set
Please update these fields to ensure proper tracking and planning.

**KrishnaDeepthi K** (2025-11-20T15:30:07.132+0530):
>  
 , once you have marked the items in platform, please notify here for 
 to pick them up and plan it accordingly. attn: 
 
 
 

**KrishnaDeepthi K** (2025-11-20T15:33:36.857+0530):
>  could you please follow up on the open items from the OUCU team? 
attn: 
 
 
 
  

**Marcus Abhilash Surendran** (2025-11-20T18:48:41.935+0530):
>  This is updated. Please note 
 
cc 
 
 

**KrishnaDeepthi K** (2025-11-20T19:49:54.784+0530):
>  
 Could you please confirm the scope from Diamond, too, as we did with OUCU 
  Post which we can setup a call with Velera team to clarify technical questions our dev team have.
attn: 
 
 
 
 

**KrishnaDeepthi K** (2025-11-20T19:55:14.568+0530):
>   , Please share the 
UX plan
 for these features, specifically detailing any proposed 
UX upgrades
 rooted in a 
vendor-agnostic design
 for card controls. As part of the recent CuofCo release, we successfully implemented this platform change for lower product versions within the UX 2.0 framework. Our next step should be to 
roll out this change to all higher product versions running UX 2.xx
.
attn: 
 
 
 
 
 

**KrishnaDeepthi K** (2025-11-20T19:59:10.665+0530):
>  please notify here once you have the list of missing tech specs to follow up with Velera.
attn: 
 


---

## 🛠️ Resolution Workspace
*Fill out the sections below to resolve the ticket.*

---

## 1. 📝 Problem Statement
*Describe the issue clearly. What is the expected behavior vs. the actual behavior?*

- **Description**:
- **Impact**:
- **Steps to Reproduce**:
    1.
    2.
    3.

## 2. 🔍 Root Cause Analysis (RCA)
*Why is this happening? Dig deep.*

- **Initial Observation**:
- **The 5 Whys**:
    1. Why?
    2. Why?
    3. Why?
    4. Why?
    5. Why?
- **Conclusion**:

## 3. 💡 Proposed Solution
*How do we fix it correctly and permanently?*

- **Approach**:
- **Risks/Side Effects**:
- **Alternatives Considered**:

## 4. 🛠️ Implementation Plan
*Checklist of tasks to execute the solution.*

- [ ] Step 1:
- [ ] Step 2:
- [ ] Step 3:

## 5. ✅ Verification & Testing
*Proof of perfection.*

- **Test Case 1**:
    - Input:
    - Expected Output:
    - Actual Output:
- **Test Case 2**:
    - ...

## 6. 🏁 Closure Notes
*Final thoughts for the record.*

- **Resolution Summary**:
- **Lessons Learned**:
