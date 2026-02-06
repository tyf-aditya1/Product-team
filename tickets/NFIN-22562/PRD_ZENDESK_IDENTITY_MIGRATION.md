# 📄 PRD: Zendesk Email Identity Migration (Yahoo/AOL Delivery Fix)

**Document Status**: Draft
**Jira Ticket**: NFIN-22562
**Owner**: Product Team (Aditya Raj)
**Technical Stakeholders**: Backend Engineering, DevOps

---

## 1. Executive Summary
**The Problem**: Support emails sent to Yahoo and AOL users are bouncing with `Error 552: Inbox Full / User Not Found`.
**The Root Cause**: Our integration currently appends a unique identifier to the user's email address (e.g., `user+12345@yahoo.com`) to enforce uniqueness in Zendesk. While Gmail supports this "plus-addressing", Yahoo and AOL often reject these specific aliases as invalid users.
**The Solution**: We will transition our Zendesk integration to use the native **`external_id`** field as the Primary Key for user identity, allowing us to store the **clean** email address (`user@yahoo.com`) in the email field.
**Success Metric**: 100% Delivery rate to Yahoo/AOL recipients; 0% `552` Bounce errors.

---

## 2. Current Architecture (The "As-Is")
Based on codebase analysis (KT Transcript), the current flow is:
1.  **Identity Construction**: The backend constructs a Zendesk User record.
    *   `email`: `user+UniqueID@domain.com` (e.g., `john+88291@yahoo.com`)
    *   `external_id`: `TenantID-UniqueID` (e.g., `UBIFCU-88291`)
2.  **Logic**: The system forces the `+UniqueID` into the email field to ensure that if a user changes their email, the `external_id` remains the stable link.
3.  **Failure Point**: When Zendesk replies to the ticket, it sends the email to `john+88291@yahoo.com`. Yahoo servers reject this address because the mailbox `john` exists, but the alias `john+88291` is not recognized.

---

## 3. Product Requirements (The "To-Be")

### Requirement 1: Update API Logic (Create/Update User)
The Backend Service responsible for syncing users with Zendesk (likely `CreateTicket` or `CreateUser` workflow) must be updated.

| Field | Current Logic (OLD) | New Logic (REQUIRED) |
| :--- | :--- | :--- |
| **`email`** | `user+UniqueID@domain.com` | **`user@domain.com`** (Clean Email) |
| **`external_id`** | `TenantID-UniqueID` | **UNCHANGED** (`TenantID-UniqueID`) |
| **`name`** | User Full Name | UNCHANGED |

**Behavior Change**:
*   The system must **STOP** appending `+UniqueID` to the email string.
*   The system must rely **solely** on `external_id` to identify the user record in Zendesk.

### Requirement 2: Handle Email Updates
If a user changes their email address in the Core Banking app:
*   **Current Flow**: System detects mismatch, deletes old identity, creates new identity.
*   **New Flow**: 
    1.  The system should lookup the user by `external_id` (`UBIFCU-88291`).
    2.  Update the `email` field of that *existing* user record to the new address.
    *   *Benefit*: This preserves ticket history (which is linked to the User ID, not just the email).

---

## 4. Migration Strategy (Data Cleanup)
We have thousands of existing users stored with "Bad" emails (`user+ID@...`). We cannot leave them broken.

### Migration Script Logic
**Scope**: All Zendesk Users where `email` matches regex `.*\+.*@.*` (contains `+`).

**Process for each user**:
1.  **Extract Data**:
    *   Bad Email: `john+88291@yahoo.com`
    *   Clean Email (Target): `john@yahoo.com`
    *   Current ID: `UBIFCU-88291`
2.  **Check for Conflict**:
    *   Does a *separate* user already exist with email `john@yahoo.com`?
    *   **Scenario A (No Conflict)**: 
        *   Update the current user: Set `email` = `john@yahoo.com`.
    *   **Scenario B (Conflict Exists)**:
        *   We have two records for the same person.
        *   **Action**: Merge the "Bad Email User" (which has the ticket history) into the "Clean Email User", OR (simpler) Update the "Bad Email User" and archive the other if it has no history.
        *   *Engineer Decision*: If merging is too complex via API, log these conflicts for manual review.

---

## 5. Rollout Plan
1.  **Dev/Staging**:
    *   Deploy Logic Change.
    *   Create a test user `test@yahoo.com`. Verify it allows creation without `+` string.
    *   Send a test ticket. Verify bounce does NOT occur.
2.  **Migration Dry-Run**:
    *   Run the Migration Script in "Report Mode" (Read Only) to see how many users will be updated and how many conflicts exist.
3.  **Production**:
    *   Deploy Logic Change (Stop creating new bad emails).
    *   Run Migration Script (Fix old bad emails).

---

## 6. FAQ
*   **Q: Will this break Gmail users?**
    *   A: No. Gmail ignores the `+` tag anyway, so moving to the clean email has no impact on delivery. It just makes the data cleaner.
*   **Q: What if the user doesn't have an External ID?**
    *   A: All users originated from our Digital Banking platform have a Unique ID. If a user was created manually by an agent, they might look different. The migration script should strictly target users matching the `TenantID-UniqueID` pattern.
