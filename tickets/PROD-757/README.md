# PROD-757: Fiserv | Spendtrack (CardHub) | SSO

**Jira Link:** https://tyfone.atlassian.net/browse/PROD-757
**Downloaded:** 2026-02-02 02:36:56

## Key Information

- **Status:** 6. Ready for Dev/Design
- **Priority:** Medium
- **Assignee:** Aditya Raj
- **Reporter:** Jamie Hancock
- **Created:** 2025-03-18T23:04:51.638+0530
- **Updated:** 2026-01-28T02:19:37.008+0530
- **Due date:** None
- **Resolution:** None
- **Issue Type:** Idea
- **Project:** Product
- **Labels:** None
- **Components:** None

## Description

_No description_

## All Fields

- **Creator:** Jamie Hancock
- **Rank:** 0|i1c1jf:
- **Category:** Integration
- **Product:** Harmoney Business
- **Product Area:** Card Management
- **Source:** Go-live Commitment
- **Impact Multiple:** High
- **Release:** 10.51 | 02/2026
- **Customer Name:** Partners 1st
- **Engineering Lead:** Aditya M, Dinesh Shilpi
- **UX-Required:** TBD
- **Blocked?:** 1.0
- **Blocked Reason:** Awaiting API/SSO Specs
- **Last Comment Date:** {"start":"2026-01-27","end":"2026-01-27"}
- **Linked Issues:** {"id": "384917", "self": "https://tyfone.atlassian.net/rest/api/3/issueLink/384917", "type": {"id": "10409", "name": "Discovery - Connected", "inward": "is connected to", "outward": "connects to", "self": "https://tyfone.atlassian.net/rest/api/3/issueLinkType/10409"}, "inwardIssue": {"id": "356493", "key": "PROD-1035", "self": "https://tyfone.atlassian.net/rest/api/3/issue/356493", "fields": {"summary": "2026 06/23 | Partners 1st | DNA | Consumers, Business & NAO", "status": {"self": "https://tyfone.atlassian.net/rest/api/3/status/11140", "description": "", "iconUrl": "https://tyfone.atlassian.net/", "name": "Not Started", "id": "11140", "statusCategory": {"self": "https://tyfone.atlassian.net/rest/api/3/statuscategory/2", "id": 2, "key": "new", "colorName": "blue-gray", "name": "To Do"}}, "priority": {"self": "https://tyfone.atlassian.net/rest/api/3/priority/3", "iconUrl": "https://tyfone.atlassian.net/images/icons/priorities/medium_new.svg", "name": "Medium", "id": "3"}, "issuetype": {"self": "https://tyfone.atlassian.net/rest/api/3/issuetype/10693", "id": "10693", "description": "", "iconUrl": "https://tyfone.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/14148?size=medium", "name": "Project", "subtask": false, "avatarId": 14148, "entityId": "b66780fd-15a4-443b-ad1d-081584c7d8ec", "hierarchyLevel": 0}}}}
- **Last Viewed:** 2026-02-02T02:36:25.367+0530
- **Status Category:** In Progress
- **Status Category Changed:** 2025-07-21T22:25:53.120+0530
- **Summary:** Fiserv | Spendtrack (CardHub) | SSO

## Attachments

- [eCS_SSO_Proxy_Guide 1.docx](attachments/eCS_SSO_Proxy_Guide 1.docx) (25.3 KB) - by John Bonenberger
- [SpendTrack-SSO.pdf](attachments/SpendTrack-SSO.pdf) (100.1 KB) - by John Bonenberger
- [SSO Attributes - Credit Migration Template v10.xlsx](attachments/SSO Attributes - Credit Migration Template v10.xlsx) (27.5 KB) - by John Bonenberger

## Links

- [https://cat1.fsdsapps.com/ecs-sso-proxy/sso/proxy](https://cat1.fsdsapps.com/ecs-sso-proxy/sso/proxy) *(from comment 3)*
- [https://www.fsdsapps.com/ecs-sso-proxy/sso/proxy](https://www.fsdsapps.com/ecs-sso-proxy/sso/proxy) *(from comment 3)*
- [uChoose Rewards® Overview - CardDeveloper | Developer Studio](https://developer.fiserv.com/product/CardDeveloper/docs/?path=docs/release-notes/reward/reward_overview.md&branch=main) *(from comment 3)*
- [CardDeveloper | Developer Studio](https://developer.fiserv.com/product/CardDeveloper?branch=main) *(from comment 4)*
- [https://tyfone.atlassian.net/browse/PROD-757#icft=PROD-757](https://tyfone.atlassian.net/browse/PROD-757#icft=PROD-757) *(from comment 7)*
- [ https://www.fsdsapps.com/ecs-sso-proxy/sso/proxy/jwtproxy](https://www.fsdsapps.com/ecs-sso-proxy/sso/proxy/jwtproxy) *(from comment 10)*
- [ https://cat1.fsdsapps.com/ecs-sso-proxy/sso/proxy/jwtproxy](https://cat1.fsdsapps.com/ecs-sso-proxy/sso/proxy/jwtproxy) *(from comment 10)*

## Comments

### Comment 1 - John Bonenberger (2025-07-21 22:58:56)

 - spend track documentation does not live in the card studio. They are going to send me separate documentation but would like to provide a demo for the solution and how it ties into uChoose rewards for both you and krishna. 
spendtrack is only a credit solution and it’s for corporate commercial users. 
this would be tested in ‘M cycle’ environment. 
CC: 
 

### Comment 2 - KrishnaDeepthi K (2025-08-19 12:19:05)

 Please follow up on the SSO documentation and test environment details 

### Comment 3 - John Bonenberger (2025-08-21 07:03:38)

 - I received the specs from Fiserv today. 
See below with the comments from Fiserv as well as the attached documents.
 
 
 
As discussed, please find attached SpendTrack SSO documentation.
 
For SSO to SpendTrack, the endpoint must be
 
CAT- 
https://cat1.fsdsapps.com/ecs-sso-proxy/sso/proxy
/jwtproxy
Prod- 
https://www.fsdsapps.com/ecs-sso-proxy/sso/proxy
/jwtproxy
 
The lead time for implementation/ certification of SSO to Spend Track is 120 days.
Fiserv will need to discuss a potential partner agreement with Tyfone for these solutions.
 
SSO to uChoose ( not within CardHub)
uChoose Rewards® Overview - CardDeveloper | Developer Studio
You can find the endpoints and tech info using the link above.
The lead time is 45 days for set up in the sandbox and move to production.
The lead time may be longer if the client will use our Client Test Environment.
 
Fiserv will also need to discuss a potential partner agreement with Tyfone for these solutions.
 
Let me know if we need to meet once you have had a chance to review these materials.

### Comment 4 - John Bonenberger (2025-09-13 00:48:36)

 - i received this update today from fiserv
For SSO to uChoose, you can access the Sandbox through 
CardDeveloper | Developer Studio
 under Rewards. You need to set up a user id and can access the sandbox and tech specs.
For SpendTrack, you will need access to our test environment. To get this, Partners will need to sign a Service Request for these solutions, and Tyfone will need to sign a partnership agreement with Fiserv.
An SSO to uChoose is already build within the SpendTrack application.

### Comment 5 - Automation for Jira (2025-09-15 16:50:32)

Engineering Lead Assigned:  
 ,  
 

### Comment 6 - KrishnaDeepthi K (2025-09-15 16:51:13)

 
 Please review the SSO documentation and share your analysis on the same.

### Comment 7 - Automation for Jira (2025-11-17 09:01:35)

🔔 
Action Required: Update Missing Critical Fields
One or more critical fields need to be updated for this ticket.
Details:
Ticket:
 
 - Fiserv | Spendtrack (CardHub) | SSO
Current Status:
 6. Ready for Dev/Design
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

### Comment 8 - KrishnaDeepthi K (2025-12-08 11:39:04)

 Start following up on the ticket with DM and gather all the details and share with engineering to start analysis

### Comment 9 - John Bonenberger (2025-12-12 20:44:14)

 
 - Fiserv and Partners finally executed the SOW, so i’ve received these spendtrack SSO specs from Fiserv. 

### Comment 10 - John Bonenberger (2026-01-28 02:19:32)

 - I’ve received the details for partners 1st Spendtrack
Hi John,
Below is the information you will need for the SSO set up for eCS and Spendtrack:
Start url prod - 
 https://www.fsdsapps.com/ecs-sso-proxy/sso/proxy/jwtproxy
Start url stage test – 
 https://cat1.fsdsapps.com/ecs-sso-proxy/sso/proxy/jwtproxy
CID - AAAA6450001
APPID – partners-1st-fcu
Please see below for a few M cycle test accounts that can be linked to existing Online Banking user id’s that you have set up in order to test the connectivity to a Fiserv M cycle account. Let me know if you need any additional information.
4017034000000309
4017034000101024
4017034000101032


## Subtasks

_No subtasks_