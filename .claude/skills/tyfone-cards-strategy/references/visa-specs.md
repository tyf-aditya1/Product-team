# Visa Card Programs — DCAS / VTC / MLC Cheat Sheet

Quick reference for Visa-specific programs that surface in cards-strategy
conversations. Load this file whenever the research topic touches Visa
provisioning, tokenization, or credential management.

---

## DCAS — Digital Card Art Service

- **What it is**: Visa-hosted service that allows issuers to deliver
  branded, dynamic card art to digital wallets and mobile apps without
  the issuer building its own card-art pipeline.
- **How it works**: Issuer uploads approved card-art assets to Visa's
  platform; Visa serves them to end-user apps via a secure API. Card art
  can be personalized (e.g., photo cards) or static brand art.
- **Why it matters for Tyfone**: If a Tyfone CU client wants branded
  digital card art without building or buying a custom card-art engine,
  DCAS is the fastest path. Integration is on the issuer/processor side —
  confirm whether the CU's card processor already supports DCAS.
- **Current status (as of late 2024)**: Visa has been expanding DCAS
  enrollment; several large processors now support it. Participation
  list is not fully public.
- **Integration owner**: Card processor / issuing bank — Tyfone's role
  is surfacing the capability in the digital banking app UI and
  coordinating with the processor.

## VTC — Visa Token Clearinghouse

- **What it is**: Visa's network-level tokenization service. Replaces
  the real PAN with a unique token for use in digital wallets and
  card-on-file transactions.
- **How it works**: When a cardholder adds a card to Apple Pay /
  Google Pay / a merchant, Visa issues a token bound to that
  specific environment. The token is used for authorization;
  Visa de-tokenizes for settlement.
- **Why it matters for Tyfone**: VTC is the backbone of push
  provisioning. Tyfone doesn't operate VTC directly, but the
  issuance / provisioning vendor (Galileo, Marqeta, etc.) must
  support VTC enrollment for the CU's BIN.
- **Tyfone action**: Confirm VTC support with the chosen card
  vendor during vendor evaluation; include in integration
  checklist.

## MLC — Mastercard Lifecycle Management (included for completeness)

- **What it is**: Mastercard's equivalent lifecycle-management
  framework covering tokenization, provisioning, and credential
  updates.
- **Why it matters**: Some Tyfone CU clients issue Mastercard
  products. When the research scope includes Mastercard, apply the
  same DCAS / VTC logic above but reference Mastercard's MDES
  (Mastercard Digital Enablement Service) instead.

---

### Quick Decision Guide

| Question | Answer |
|----------|--------|
| CU wants branded card art in-app? | Evaluate DCAS first |
| CU wants Apple Pay / Google Pay? | VTC (or MDES) required — confirm vendor supports it |
| Tyfone builds provisioning flow? | No — delegate to card vendor; Tyfone orchestrates UX |
| Competitor already on DCAS? | Check competitor-profiles.md for latest |
