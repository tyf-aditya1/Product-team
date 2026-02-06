# PROD-761: Propay | SSO

**Jira Link:** https://tyfone.atlassian.net/browse/PROD-761
**Downloaded:** 2026-02-02 01:57:26

## Key Information

- **Status:** GTM Prep
- **Priority:** Medium
- **Assignee:** Aditya Raj
- **Reporter:** Jamie Hancock
- **Created:** 2025-03-18T23:17:04.943+0530
- **Updated:** 2025-12-13T03:58:01.542+0530
- **Due date:** None
- **Resolution:** None
- **Issue Type:** Idea
- **Project:** Product
- **Labels:** None
- **Components:** None

## Description

Vendor contact: 
Brayden Adams
 <
Brayden.Adams@lenderpayments.com
>
The SSO will be done through our API, specifically through the createAccountPerson call. You will make this call with the required data, and a URL to gain access to the payer portal for that account will be returned which should be used to redirect the payer to LenderPay for SSO access.
 
The documentation for this call can be found here: 
https://docs.epay.cm/#/docs/api/method/createAccountPerson/
 
Our Sandbox URL for API access is 
https://sandbox.aptx.cm
TyFone’s Sandbox API Token: SMD3M6PS90263D00
UBI’s Target ID in Sanbox: 1332
Sandbox creds - 
Username:- 
integrations@tyfone.com
Password:- Testing@420
The data passed in these calls (specificaly the integrationId and groupIntegrationId need to match the way we use them in our system or it could lead to a user not being able to log in, or duplicate and/or orphaned payer records being generated. That is due to the nature of this call, if an existing payer exists it will be utilized, otherwise a new one will be created.
 
All of the data required for the integrationId and groupIntegrationId is taken directly from Symitar and leading zeroes shouldn’t be modified.
 
The integrationID is a combination of three fields from the SymXchange call, each separated by an underscore:
MemberNumber
AccountNumber
ID (suffix) of sub account (this is often referred to as the LoanId or AccountId). Usually something like 01, 02, 50, etc. as returned from SymXchange in the getLoanList or getAccountsList calls.
The three fields combined should be arranged like so: {MemberNumber}_{AccountNumber}_{ID}
The groupIntegrationId is the MemberNumber field. It is used to group multiple accounts for the same member together.

## All Fields

- **Creator:** Jamie Hancock
- **Rank:** 0|i1c1jz:
- **Category:** Integration
- **Product:** nFinia Retail
- **Source:** Go-live Commitment
- **Impact Multiple:** High
- **Release:** Released | 10.46 | 09/2025
- **Customer Name:** UBI FCU
- **Engineering Lead:** Dinesh Shilpi
- **Requirement:** https://docs.google.com/document/d/1IedERL56W0XtyWAUWIkKwTic7QqQ6XLrEzlIKM_zndI/edit?usp=sharing
- **Risk:** Low
- **Last Comment Date:** {"start":"2025-11-26","end":"2025-11-26"}
- **Linked Issues:** {"id": "384254", "self": "https://tyfone.atlassian.net/rest/api/3/issueLink/384254", "type": {"id": "10405", "name": "Polaris work item link", "inward": "is implemented by", "outward": "implements", "self": "https://tyfone.atlassian.net/rest/api/3/issueLinkType/10405"}, "inwardIssue": {"id": "359820", "key": "NFIN-41491", "self": "https://tyfone.atlassian.net/rest/api/3/issue/359820", "fields": {"summary": "Propay | SSO", "status": {"self": "https://tyfone.atlassian.net/rest/api/3/status/10850", "description": "", "iconUrl": "https://tyfone.atlassian.net/", "name": "Done", "id": "10850", "statusCategory": {"self": "https://tyfone.atlassian.net/rest/api/3/statuscategory/3", "id": 3, "key": "done", "colorName": "green", "name": "Done"}}, "priority": {"self": "https://tyfone.atlassian.net/rest/api/3/priority/3", "iconUrl": "https://tyfone.atlassian.net/images/icons/priorities/medium_new.svg", "name": "Medium", "id": "3"}, "issuetype": {"self": "https://tyfone.atlassian.net/rest/api/3/issuetype/10000", "id": "10000", "description": "A big user story that needs to be broken down. Created by JIRA Software - do not edit or delete.", "iconUrl": "https://tyfone.atlassian.net/images/icons/issuetypes/epic.svg", "name": "Epic", "subtask": false, "hierarchyLevel": 1}}}}
- **Last Viewed:** 2026-02-02T01:12:43.803+0530
- **Status Category:** In Progress
- **Status Category Changed:** 2025-09-03T11:41:58.081+0530
- **Summary:** Propay | SSO

## Attachments

- [image-20250902-184834.png](attachments/image-20250902-184834.png) (32.3 KB) - by Dinesh Shilpi

## Links

- [Brayden.Adams@lenderpayments.com](mailto:Brayden.Adams@lenderpayments.com) *(from description)*
- [https://docs.epay.cm/#/docs/api/method/createAccountPerson/](https://docs.epay.cm/#/docs/api/method/createAccountPerson/) *(from description)*
- [https://sandbox.aptx.cm](https://sandbox.aptx.cm/) *(from description)*
- [integrations@tyfone.com](mailto:integrations@tyfone.com) *(from description)*
- [https://docs.google.com/document/d/1IedERL56W0XtyWAUWIkKwTic7QqQ6XLrEzlIKM_zndI/edit?usp=sharing](https://docs.google.com/document/d/1IedERL56W0XtyWAUWIkKwTic7QqQ6XLrEzlIKM_zndI/edit?usp=sharing) *(from comment Requirement)*
- [https://sandbox.aptx.cm/endpoint/service/api-v1/createAccountPerson](https://sandbox.aptx.cm/endpoint/service/api-v1/createAccountPerson) *(from comment 12)*

## Comments

### Comment 1 - Automation for Jira (2025-07-22 14:10:43)

Engineering Lead Assigned:  
 

### Comment 2 - Prashant Karpe (2025-07-22 14:11:14)

Assigned to 10.46 release after working with 
 

### Comment 3 - Rithesh Swamy (2025-08-03 21:47:24)

Hey 
 - you brought this up during the Friday meeting. 
The sandbox details are available for us to get started. 
Is there anything else you need from the customer or the vendor?

### Comment 4 - Dinesh Shilpi (2025-09-03 00:20:25)

 
 Could you provide the login credentials for accessing the sandbox environment? I am being prompted for credentials when trying to access 
https://sandbox.aptx.cm
 
CC: 

### Comment 5 - Rithesh Swamy (2025-09-03 10:02:04)

 - I dont have access to this portal. 
 - please check if you have it.

### Comment 6 - Dinesh Shilpi (2025-09-08 09:01:33)

  Could you confirm whether you have access to the portal? If not, could you assist in obtaining the necessary details and also share the vendor contact information so we can reach out to them?
CC: 
 
 

### Comment 7 - Dinesh Shilpi (2025-10-08 12:36:28)

 
 
 We are implementing this feature directly in the UBI 10.43 branch. Once UBI goes live, we will merge it into the latest product branch. Please let me know if you have any concerns with this plan.
Attn: 
 
 

### Comment 8 - Rithesh Swamy (2025-10-08 15:13:56)

 - I dont have any concerns. 

### Comment 9 - sreelekshmi.vh (2025-10-08 19:35:34)

Thank you 
 Here is the update from Jonathan for loans with Primary and Joint Association.
For all intents and purposes, test and prod are the same, just different dates on the database, no need to specify where you need the data for. Here's some accounts with joints:
564040
589690
662110
696804

### Comment 10 - Dinesh Shilpi (2025-10-08 19:52:58)

Thank you, 
 we will test and get back to you if we are not seeing the data we are looking for.

### Comment 11 - Dinesh Shilpi (2025-10-09 13:14:04)

 We were unable to retrieve the loans and shares linked to these members because they are not enrolled in nFinia, and we do not have their SSN and DOB to complete the enrollment and verification process.
Additionally, please confirm whether these members are joint on any loans owned by other members. If they are not, kindly provide the details of the members who are listed as joint.
CC: 
 
  
 

### Comment 12 - Dinesh Shilpi (2025-10-24 13:59:55)

 Could you please get the following details for PROD from vendor?
ProPay PROD Details:
API URL
API_TOKEN
API_TARGET_ID
For your quick reference here are the details we received for Sandbox:
API URL: 
https://sandbox.aptx.cm/endpoint/service/api-v1/createAccountPerson
API_TOKEN : SMD3M6PS90263D00
API_TARGET_ID : 1322
CC: 
 
 
 
 

### Comment 13 - Dinesh Shilpi (2025-11-26 09:14:31)

 Since the customer is now live, proceed with merging this feature into the product for both OLB and MB ASAP.


## Subtasks

_No subtasks_