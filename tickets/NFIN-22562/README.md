
# 🎫 NFIN-22562: CU Reported | PM - Zendesk messages not being delivered to Yahoo domain Emails

**Status**: `Open` | **Priority**: `Medium` | **Assignee**: `Aditya Raj` | **Due Date**: `None`
**Jira Link**: https://tyfone.atlassian.net//browse/NFIN-22562

---

## 📄 Jira Description
Good morning,
In our testing we discovered messages direct from Zendesk (
support@relyoncu.zendesk.com
) are not making it to Yahoo mailboxes.  Its possible others are blocking as well.
Is there an SPF record we need to add or a setting that can be made to improve deliverability of messages from Zendesk?

## 📎 Attachments
_No attachments_

## 💬 Comments History
**Chandhar Singh** (2023-09-19T12:50:00.123+0530):
> We had raised a ticket with the Zendesk support team and CU had shared a few examples of Yahoo Email ID’d with them and update from the Zendesk team.
Hi there,
My name is Nara and I'll be helping resolve this from here on out. To start, thank you for sending over all of the example tickets. I took a look through our outbound logs and corroborated what Earle San Jose found regarding the bounce messages. However, I also checked the inbound messages, and it looks like at the time of ticket creation, the email that reaches out servers for all of these examples is sending over the
 long email name you are seeing in the Support UI
Essentially, Yahoo, or any intermittent email server between the end user address and Zendesk, is sending over those long email names verbatim. Zendesk itself is not changing the email; the system is accurately reflecting the data received as the sender's address.
Typically when this happens it is due to an intermediary/3rd party mail service. To resolve this, I would recommend working with your email/IT admins to identify any intermediary mail processing being done on these emails, or reaching out to the end users in the errored emails to ensure they are sending directly from their own email client, and not through another, separate service.
--
Tyfone Note:  
(This is related to Email ID we are sending with the unique identifier)
Example: Actual Email ID is 
tyfonetesting@yahoo.com
 and one in the Zendesk shows up as 
tyfonetesting+amv4k3puulbaauwznfppl3jvdxr0qt09@yahoo.com

**Chandhar Singh** (2023-09-20T14:22:21.463+0530):
>  
Please review this issue.
Oregonians CU has also reported a similar issue (the PS ticket is linked here)
 
 
 
 We may have this issue for other CU’s as well.
 
 
 
 
 

**Aniket Dutta** (2023-09-20T14:55:39.178+0530):
>  - this is regarding Zendesk. 

**Ranjini H.K** (2023-09-20T23:57:28.045+0530):
>  
 Request you to expedite this, Oregonians is asking for an update & expects to get this fixed asap
Have updated 
 with the latest details. Please review.

**Aniket Dutta** (2023-09-22T00:03:36.468+0530):
> , I have limited context on Zendesk and hence would request you to take over.  

**Ranjini H.K** (2023-09-26T23:31:47.834+0530):
>  
 Any update?

**Ashish Behera** (2023-10-10T17:34:16.758+0530):
>  
 Please do help with an update on this.
Attn: 
 

**Ranjini H.K** (2023-11-21T20:27:08.727+0530):
>  
 Please review this and guide us on next steps.

**sreelekshmi.vh** (2025-11-28T07:19:18.517+0530):
>  
 Just checking if we got any resolution for this issue yet. UBI has reported the same issue, so please let me know what our response was to the Oregonians team. Thanks!
cc: 
 
 

**Prashant Karpe** (2025-11-28T10:43:45.106+0530):
>  Please assist the team with performing these checks:
cc: 
 
 
 

**Aditya Raj** (2025-11-28T11:08:48.483+0530):
> Sure 
 !!

**Aditya Raj** (2025-11-30T12:39:24.530+0530):
>  
 
 
I'm investigating this Yahoo email delivery issue. Before implementing any fixes, I need to confirm our current Zendesk configuration 
i need the following information--
Based on the configuration, there could be two completely different root causes: -
If using system address (@zendesk.com): Issue is Zendesk's shared IP reputation with Yahoo → We need to contact Zendesk Support 
If using custom domain: Issue is missing DNS authentication records (SPF/DKIM/DMARC) --> We need to update DNS


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
