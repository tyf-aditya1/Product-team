# 📄 Requirement: Zendesk Identity Migration (Email to External ID)

**Project**: NFIN-22562 Resolution
**Goal**: Transition from using Sub-addressing (`user+ID@domain.com`) to Zendesk Native `external_id` for user identification. This resolves delivery failures to Yahoo/AOL.

---

## 1. Problem Statement
*   **Current State**: 
    *   Users are identified by `external_id` (Format: `TenantID-UniqueID`).
    *   **However**, the `email` field *also* appends this ID (`user+UniqueID@domain.com`) to ensure uniqueness/binding.
*   **Impact**: Yahoo and AOL reject these `+` addressed emails as "User Not Found".
*   **Target State**: 
    *   Continue using `external_id` (`TenantID-UniqueID`) as the Primary Key.
    *   **CRITICAL CHANGE**: Store the **Clean Email** (`user@yahoo.com`) in the `email` field. DO NOT append `+UniqueID`.

---

## 2. Technical Requirements

### A. API Logic Update (The "Create/Update User" Flow)
The Ticket Creation service (likely in `CreateUser` or `CreateTicket` method) must be updated:

*   **Existing Payload (Inferred)**:
    ```json
    { 
      "user": { 
        "email": "user+12345@yahoo.com", 
        "external_id": "BankName-12345", 
        "name": "John Doe" 
      } 
    }
    ```
*   **New Payload**:
    ```json
    { 
      "user": { 
        "email": "user@yahoo.com",  // <--- CHANGED: Clean Email
        "external_id": "BankName-12345", // <--- UNCHANGED: ID remains the primary link
        "name": "John Doe" 
      } 
    }
    ```
*   **Conflict Logic**:
    *   If `user@yahoo.com` already exists (as a different user without `external_id`), the API must **Merge** the new identity into the existing clean-email user, OR update the existing user to add the `external_id`.

### B. Migration Strategy (Data Cleanup)
Since `external_id` already exists, we only need to "Clean" the emails.

**Migration Logic (Script)**:
Fetch all users where `email` contains `+`.
1.  **Parse**: `user+12345@yahoo.com` -> `user@yahoo.com`.
2.  **Validate**: Ensure the `external_id` is present (`BankName-12345`).
3.  **Update**:
    *   Set `email` = `user@yahoo.com`.
    *   *Note: This might trigger a 'Email already taken' error if the clean email exists elsewhere. The script must handle this by identifying the duplicate and merging.*

---

## 3. Rollout Plan

### Phase 1: Validation (Staging)
1.  Create users with `+ID` in Staging Zendesk.
2.  Run Migration Script.
3.  Verify users now have `external_id` populated and Clean Email.
4.  Test Ticket Creation with New Logic (ensure it maps to the migrated user, not a new one).

### Phase 2: Production Migration
1.  **Stop Sync**: Pause Ticket Creation service (maintenance window).
2.  **Run Migration**: Execute script to clean up existing users.
3.  **Deploy Code**: Push API Logic Update.
4.  **Resume Sync**.

---

## 4. Risks & Mitigation
*   **Duplicate Users**: If `user@yahoo.com` exists separately from `user+123@yahoo.com`.
    *   *Mitigation*: The migration script must check for e-mail collisions. If collision, Merge the users.
*   **ID Mismatch**: If `+ID` isn't the exact DB ID.
    *   *Mitigation*: Verify ID format with Dev team before writing script.
