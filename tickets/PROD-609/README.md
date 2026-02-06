
# 🎫 PROD-609: FIS Payments One (FIS Card Suite) | Debit Card Alerts and Controls

**Status**: `3. Release Planning (Roadmap)` | **Priority**: `Medium` | **Assignee**: `Aditya Raj` | **Due Date**: `None`
**Jira Link**: https://tyfone.atlassian.net//browse/PROD-609

---

## 📄 Jira Description
Scope:
 features in Shared Card Suite Pro SDK app spec 

## 📎 Attachments
- [auto_enrollment_rq_rs.txt](attachments/auto_enrollment_rq_rs.txt)
- [Capital Communityl Bank - Card Suite Pro Kick-Off_Deck 10.06.2025.pdf](attachments/Capital Communityl Bank - Card Suite Pro Kick-Off_Deck 10.06.2025.pdf)
- [Card_Suite_API_vs_SDK.xlsx](attachments/Card_Suite_API_vs_SDK.xlsx)
- [Card Suite Lite FAQ.pdf](attachments/Card Suite Lite FAQ.pdf)
- [Card Suite Lite FAQ (f467a13a-97bc-45b3-9c58-011f0e2369c0).pdf](attachments/Card Suite Lite FAQ (f467a13a-97bc-45b3-9c58-011f0e2369c0).pdf)
- [CC_HZN_xChange_API Mapping Worksheet_V7.xlsx](attachments/CC_HZN_xChange_API Mapping Worksheet_V7.xlsx)
- [CCBank - Code Connect - TYFONE - Production Keys and Tokens.docx](attachments/CCBank - Code Connect - TYFONE - Production Keys and Tokens.docx)
- [CS Lite App User Guide 202411.pdf](attachments/CS Lite App User Guide 202411.pdf)
- [CS Lite App User Guide 202411 (4cb42e11-e41b-4495-8cb6-d546883c50f4).pdf](attachments/CS Lite App User Guide 202411 (4cb42e11-e41b-4495-8cb6-d546883c50f4).pdf)
- [experience_sdk_rq_rs.txt](attachments/experience_sdk_rq_rs.txt)
- [Image-2025-07-11 14_09_46.png](attachments/Image-2025-07-11 14_09_46.png)

## 💬 Comments History
**KrishnaDeepthi K** (2025-04-01T23:09:36.290+0530):
>  Below is the list of card features available in the platform. Could you please get the clear scope defined by the Bank for debit cards? Also, please get the API & SDK documentation references for the FIS card suite pro.

**John Bonenberger** (2025-04-22T20:22:42.307+0530):
>  
API specs are located here. 
 
Prashant is working on getting access for a global login ID - it requires OTP verification and is linked to 
integrations@tyfone.com

**KrishnaDeepthi K** (2025-04-23T17:31:09.164+0530):
>  still I would need the scope to defined by the bank for debit cards? can we get the list of existing features the bank offers currently

**John Bonenberger** (2025-04-30T01:06:23.077+0530):
>   - these are the key features the client wants implemented today. I’m going to have a follow-up dicsussion with them tomorrow to see if there is anything else we need to add to the scope. 
API guide for Card Suite Lite is here
Key features

**John Bonenberger** (2025-05-01T19:48:20.549+0530):
>  - CCBank confirmed the scope of Card Suite Lite is small and all the features and functions in the specs are used today. 
They’ve also provided the user guide for reference. 

**John Bonenberger** (2025-05-13T21:18:19.431+0530):
>  - please confirm if this is still blocked

**KrishnaDeepthi K** (2025-05-13T22:42:26.519+0530):
> , We are unblocked for now. I shall review the scope and get back to you on any further questions.

**KrishnaDeepthi K** (2025-06-02T16:23:52.112+0530):
> ,​ We need access to the FIS card suite Lite API documentation. Also, the user guide is for the FIS companion app. I'm assuming those specs were shared just for reference purposes. The scope is still an API integration.
cc: 
 

**Automation for Jira** (2025-06-02T16:42:44.026+0530):
> Engineering Lead Assigned:  
 

**KrishnaDeepthi K** (2025-06-02T16:44:12.060+0530):
>  , could you please align a fix version to this item?
cc: 
 
 

**John Bonenberger** (2025-06-02T21:32:08.958+0530):
>   - 
 - here is API guide for card suite lite. You’ll need to use the global credentials for FIS API catalog that Prashant has created. 

**Aditya M** (2025-06-04T00:29:53.778+0530):
>  - the Card Suite Lite referred here is their existing App. I donot see any API references in both the PDFs provided.  Looks like there is a separate API specification URL provided, but i need a login for the same. Please advise. 
 
 

**KrishnaDeepthi K** (2025-06-10T16:55:33.258+0530):
>  seems like those credentials to access the API documentation have expired. Could you help us get 
integrations@tyfone.com
 registered on the portal and share with us the credentials?
cc: 
 
 
 

**John Bonenberger** (2025-06-25T20:52:35.480+0530):
>  - I received this URL from FIS as well. I’ve forwarded you the email too

**KrishnaDeepthi K** (2025-07-01T11:44:02.724+0530):
> ,   Any update on the bank’s decision on which product they are going ahead with, as per our last call, we were asked to wait until the bank confirms this. Please note scope and estimates will change based on their confirmation. It's already late for the go-live commitment.
cc: 
 
 
 
 
 

**Kati Mendelson** (2025-07-04T00:53:30.068+0530):
>  the Bank is inquiring if it’s possible to go with the Card Suite Lite option and add a wallet provisioning capability only from the PRO suite (possibly as a phase 2, not at go live).  Could we do this?  They are checking with FIS to determine if they will also permit this, and hope to have this finalized by early next week.
 
 
 
 
 

**Kati Mendelson** (2025-07-08T22:23:48.512+0530):
>  CCBank wants to move forward with the Card Suite PRO SDK
cc: 
 
 
 
 
 

**Prashant Karpe** (2025-07-10T08:21:21.467+0530):
>  Let's get moving with engineering on this soon. CCBank go-live is not too far. 

**Prashant Karpe** (2025-07-10T08:21:34.048+0530):
> Also, are we still blocked on this? If not, please remove the flag. 

**KrishnaDeepthi K** (2025-07-10T09:41:24.439+0530):
>  please use the cards suit pro SDK integration documentation from the portal , and confirm if we are good align a fix version for this.

**KrishnaDeepthi K** (2025-07-10T09:50:57.102+0530):
>  
 Meanwhile, as 
 estimates the efforts and timelines for the overall scope listed, could you please check if the bank has shared a list of priority features required for go-live? Since the confirmation is already delayed, it would be helpful to understand the priorities so we can plan phased deliveries accordingly.
Cc: 
 
 

**John Bonenberger** (2025-07-14T21:36:54.567+0530):
>   
 - i received these feautures and function requirements from CCBank for Card Suite pro. They have also prioritized which features are required for day 1 and the features they are ok with as a post go-live launch, if we’re unable to deliver these items on day 1. 
CC: 
 

**KrishnaDeepthi K** (2025-07-16T17:06:08.642+0530):
> ,​​ could you please review the documentation for Card Suite Pro and add a fix version to this.  I shall DM you the creds to FIS code connect , you may have to ask the authentication code to 
  to login 

**John Bonenberger** (2025-07-24T21:11:20.674+0530):
>  
additional docs shared for FIS cards 

**KrishnaDeepthi K** (2025-07-24T22:13:05.286+0530):
>  Let’s review the recommendation API vs SDK from FIS [ refer to attached XLSX] , found this on the Axon site shared by the FIS team. Let's evaluate and ensure we have enough details to proceed.

**Aditya M** (2025-07-25T21:49:29.229+0530):
>  as discussed today CU licensed for ‘Card Suite Pro’ and wants to use vendor SDK for both OLB and Mobile. CU prefers this approach as these SDKs come with their built-in user experience and makes development faster. 
 I reviewed their micro site provided and to be sure we need to confirm with the vendor if these are SDKs we should be looking and the our understanding on the SDK UI is correct or if the vendor has any other recommendation, they should share it with us:
For Mobile, Experience SDK Pro: 
  (SDK has UI)
For Desktop browser/tablets: Web SDK Lite: 
 (SDK has UI)
Note i reviewed Mobile SDK: 
 and it provides SDK APIs/events and nFinia should build the UI.
Below are the features in Experience SDK Pro (Mobile) Web SDK Lite(desktop). Items marked with * are available only in Experience SDK Pro:
Aggregate View*
Cards View
Transaction Details
Transaction Controls
Location Controls
Location Shield*
Region Shield
International Transactions
Merchant Controls
One Time Override
Change Card PIN*
Report Lost/Stolen Card*
Archive Card
Wallet Integration*
Credit Card Payment*
Rewards & Offers*
Dispute Transaction*
Digital Card Issuance*
cc: 
 
 

**John Bonenberger** (2025-07-26T00:40:07.259+0530):
>  
 
Are you following up with the vendor directly, or do you need me to raise those questions?
FIS Resources would be 
Austin.Rennich@fisglobal.com
 and 
jordan.schmidt@fisglobal.com
 

**KrishnaDeepthi K** (2025-07-28T12:08:49.828+0530):
> ,​​ I have replied on the same thread.
 

**John Bonenberger** (2025-07-29T07:18:56.480+0530):
>  
 - here is a recording of their current Card Suite digital banking integration. 
 

**John Bonenberger** (2025-07-31T07:12:24.552+0530):
>  - FIS communicated that they will not have a resource for cards for another 8 weeks from today. Project kickoff and execution will not be complete for another 8-12 weeks from that point. 

**KrishnaDeepthi K** (2025-08-04T20:25:41.642+0530):
> Latest reply from the FIS team:
Thank you for your patience here as I tracked down the appropriate answers for you. With respect to which SDK to focus on, this will be up to Capital Community to determine.  Here is a summary of the differences:
Experience SDK Pro
:  The Card Suite Experience SDK (CSE SDK) is a ready-to-use experience that enables financial institutions to add Card Suite capabilities to their mobile apps. It provides a unified user interface that can be customised to match a financial institution’s branding guidelines. As a result, the financial institutions can easily create fully integrated and customizable user experiences for their existing iOS and Android mobile apps.
Mobile SDK
: Also called “functional SDK” is all the functions without any experience or theme. Truly full customization for the FI to choose how they want the look and feel.
Web SDK Lite:
 SDK for web experience. Only covers the Card Suite Lite functionality. Does not include pro functions. Card Suite experience and not full customization
Additionally, once we get resources assigned to CCB’s implementation, we will walk through the mapping of the requested features below.
Please let us know if you have any questions in the meantime.
 
cc: 
 
 
 
 

**KrishnaDeepthi K** (2025-08-04T20:28:49.366+0530):
> , could you please follow up with the bank to confirm which product they have signed up for the mobile and web? Additionally, please note that Web SDK Lite is an SDK for a web experience. Only covers the 
Card Suite Lite functionality. Does not include pro functions. Card Suite experience and not full customisation
. How should we proceed with the Online banking SDK or API?

**John Bonenberger** (2025-08-05T01:40:55.099+0530):
>  - I spoke with Emily at CCBank about this today. Currently, they have a very limited web integration and it is not very complex for card controls. 
Emily said they have a preference for the fastest go-to-market experience. If we can roll out the web lite, that would be fine so they don’t lose functionality on day one, but they would like the full pro experience to be built out in a future state. Does this answer your question?
CC: 
 

**John Bonenberger** (2025-08-14T01:51:10.414+0530):
>  
CCBank is going to go with the Experience SDK Pro for mobile. It looks like the SDK file is within this website. 
 Can you confirm we have everything we need from the mobile SDK standpoint? is there anything else needed from FIS?
For the desktop/web experience, can you confirm there are 2 options? Web SDK SSO and Web SDK API? If so, which one have you called out below?
 
 
 
 

**Rithesh Swamy** (2025-08-14T08:58:47.755+0530):
>  - please the update from 
.

**KrishnaDeepthi K** (2025-08-19T14:44:01.292+0530):
>  
 ,  we will proceed with the Experience PRO SDK solution for mobile cards integration. 
 , please initiate the SDK analysis and flag any gaps or clarifications required without delay. 
,​​ I am not certain what you mean by Web SDK API or SSO. Nevertheless, we will proceed with the analysis for the Web SDK Lite. 
Could you also confirm whether the bank has acknowledged the gap between the Lite and Pro versions
?
FYI: Even with the above clarification, please note that FIS communicated that they will not have a resource for cards for another 8 weeks from today. Project kickoff and execution will not be complete for another 8-12 weeks from that point. [
as communicated on Jul 31st]
.
 
,​​ 
Please note, if the scenario below applies, I assume the post–go-live PRO experience will be handled as a separate SOW activity.
“
Emily said they have a preference for the fastest go-to-market experience. If we can roll out the web lite, that would be fine so they don’t lose functionality on day one, but they would like the full pro experience to be built out in a future state. Does this answer your question?
”
cc: 
 
 
 

**John Bonenberger** (2025-08-21T06:32:39.018+0530):
>  - I got clarity on my questions after speaking with Prabu. The bank has acknowledged there is a gap in functionality between web and mobile, but so long as the entire card suite lite functionality available is included with the web experience they are comfortable with this approach. 
We got confirmation from FIS tht they will not be able to provide a resource sooner than the date initially identified, as a result, we will not have an environment until we have resource assignment, but the bank is speaking with them frequently to see if the timetable for resource assignment changes. 

**KrishnaDeepthi K** (2025-08-21T11:21:15.012+0530):
>  
 , we need to assign a fix version to this item, with the delay from FIS counted in.
 FYI

**Rithesh Swamy** (2025-09-04T14:13:36.433+0530):
>   - this should get unblocked when FIS assigns the implementation manager, right?

**Prashant Karpe** (2025-09-19T14:21:46.829+0530):
> Confirmed that this is post go-live after discussing with the 
 
. 

**Rithesh Swamy** (2025-09-19T14:22:09.472+0530):
>  - this will be a post go-live activity. 

**John Bonenberger** (2025-10-02T22:10:55.509+0530):
>  
 - we have a call with FIS card team on Monday 10/05 at 11 AM EST. It was the only available time slot to meet with them before TFL, so we need to make sure we’re on that call. 
here is the updated API mapping matrix provided by FIS as well for your reference. 
 
CC: 
 
 

**John Bonenberger** (2025-10-06T18:27:29.889+0530):
>  
 - why is this moved to PGL? this is a critical integration for CCBank, 

**KrishnaDeepthi K** (2025-10-08T15:20:26.793+0530):
> ,​​ As per your confirmation on Slack, moving the release date to 10.48 Nov release to target the Jan go-live ​​@Aditya M​​ , please review the scope Experience SDK for the mobile app and raise the risks if we can’t meet 10.48 
,​​ please confirm on the web SDK lite if its in scope.

**Rithesh Swamy** (2025-10-08T15:33:45.688+0530):
>  - please remove PGL from the title.

**Aditya M** (2025-10-08T19:43:23.166+0530):
>  
 please see below update from 
 

**KrishnaDeepthi K** (2025-10-29T12:53:01.563+0530):
> do we have any confirmation from the bank regarding the web implementation? Are they still insisting on using the SDK for mobile and the API for web?
cc: 
 
 
 
 

**KrishnaDeepthi K** (2025-10-29T12:58:48.303+0530):
>  
 
 
FYI:
 The FIS and CC Bank project kickoff took place two weeks ago, and we’ve been having weekly syncs with both FIS and the bank since then.
During last week’s call, FIS and the bank agreed that the Web SDK Lite cannot be implemented, as it’s not included in the bank’s current contract. However, there appears to be some ongoing confusion; the bank is now requesting that we proceed with the SDK for mobile and the API for web.

**John Bonenberger** (2025-11-03T21:44:40.944+0530):
> Per CCBank
Currently only Card Suite Pro APIs are subscribed. 
I will be subscribing to the same APIs as UAT as well.
Please let me know if you have any questions.
 

**Automation for Jira** (2025-11-17T09:01:52.039+0530):
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

**PRADEEP S** (2025-12-10T22:37:55.622+0530):
> Hi 
 
Need a confirmation from vendor on the following for Manual enrollment:
cc: 
 

**PRADEEP S** (2025-12-16T23:14:04.523+0530):
> Hi 
 
We are facing few errors during the auto enrollment and SDK integration processes. Please share the following details with the vendor and provide us with their feedback.
Card Suite API: 
Manual enrollment successfully creates users and enrolls cards. However, in the auto enrollment, users were created, but no corresponding cards were enrolled. The request and response for the enrollment are attached. 
 
We need to confirm if the auto enrollment process works within the sandbox environment?
Experience SDK:
We enrolled the sandbox test user(Dexter Spencer), whose card ends in ***1028, and successfully generated an authentication token. However, when attempting to launch this user via the experience SDK, we encountered an unauthorized access error. The request and response for for the same is attached. 
 
cc: 
 
 
 
 

**Dinesh Shilpi** (2025-12-17T18:56:48.806+0530):
>  Could you please follow up with the vendor on this: 
https://tyfone.atlassian.net/jira/polaris/projects/PROD/ideas/view/4945263?selectedIssue=PROD-609&focusedCommentId=899928
? Please include me, 
  and 
  on the email thread.

**PRADEEP S** (2025-12-23T22:50:05.151+0530):
> Hi 
 We require your inputs regarding the card suite alerts and notifications.
The Card suite initiates real-time updates concerning card related alerts and notifications through a webhook mechanism. These updates fall into the following categories, each comprising multiple distinct events:
Kindly review the webhook events 
documentation 
and specify which of these events require support. Furthermore, please provide the corresponding notification templates for the selected events. 
A comprehensive list of all events, their supported fields, and sample templates are listed in the google sheet.
Webhook documentation: 
 
Sheet: 
 
cc: 
 
 
 
 

**Aditya Raj** (2026-01-06T14:58:50.140+0530):
> Hi 
 
Can you specify in the sheet what alerts we currently have or implemented for any customers. And which  channels will are planning to use for notifications?
CC: 
, 
 

**PRADEEP S** (2026-01-06T16:42:44.615+0530):
>  
The implementation of these card suite alerts is new, and they were not included in the previous card management implementations.
cc: 
 
 
 
 
 


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
