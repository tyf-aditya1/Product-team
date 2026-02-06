---
name: tyfone-cards-strategy
description: >-
  Tyfone-internal cards strategy research and Build/Buy/Partner analysis for USA
  retail and business digital banking cards. Covers digital issuance, push
  provisioning, tokenization, virtual cards, commercial card programs, Visa
  DCAS/VTC/MLC, and vendor evaluation (Galileo, Marqeta, Stripe Issuing,
  Synctera). Tracks direct competitors: Alkami, Q2, Narmi, BankJoy, Lumin
  Digital. Use whenever someone at Tyfone asks about cards features, vendor
  comparisons, competitor moves, build-vs-buy trade-offs, or any USA cards
  strategy topic (retail or business).
---

# Tyfone Cards Strategy

## Overview

Research and analyze USA digital-banking cards features, vendors, and
competitors to produce actionable Build/Buy/Partner recommendations for the
Tyfone product team.  Every output includes a mandatory Competitor Matrix and
structured Buy/Build/Partner blocks per feature gap.

## Bundled References

Load these **only** when the research topic requires them — do not load all
three by default:

| File | Load when… |
|------|------------|
| `references/competitor-profiles.md` | Populating the Competitor Matrix or comparing any named competitor |
| `references/vendor-integration-notes.md` | Filling the BUY block — Galileo / Marqeta / Stripe Issuing / Synctera details |
| `references/visa-specs.md` | Topic touches DCAS, VTC, MLC, or Visa wallet provisioning |

---

## Workflow

### 1. Clarify scope

Before searching, confirm:

- **Topic** — e.g., "Visa DCAS 2026", "business virtual cards", "push provisioning"
- **Segment** — Retail, business, or both?
- **Competitor focus** — specific competitor, or full matrix?

Example prompt to the user:
> Tyfone cards research: [topic]. Retail, business, or both? Specific competitor?

### 2. Search aggressively (2025-2026 priority)

Run **all** of the following query patterns — do not stop after the first
result set.  No source-domain limits.

```
"USA digital banking cards 2026 Alkami OR Q2 OR Narmi OR BankJoy OR Lumin Digital"
"[competitor] cards features 2025 OR 2026"
"[competitor] cards features vs Tyfone"
"[feature] build vs buy banking 2026"
"Visa DCAS integration partners 2025 OR 2026"
"[feature] credit union digital cards 2026"
```

**High-value source domains** (prioritize, but do not limit to):
AmericanBanker, PYMNTS, Finextra, vendor blogs (galileo.com, marqeta.com,
stripe.com/issuing), competitor sites, GitHub repos, fintech conference
proceedings, earnings-call transcripts, job postings (signals capability
investment).

Scrape key URLs with curl or wget when the search snippet is insufficient.

### 3. Build the Competitor Matrix (MANDATORY)

Read `references/competitor-profiles.md` for the baseline.  Overlay anything
new from Step 2.  Output this table in every response — even if some cells are
"Not confirmed":

| Feature | Tyfone | Alkami | Q2 | Narmi | BankJoy | Lumin | Build/Buy/Partner Rec |
|---|---|---|---|---|---|---|---|
| Digital issuance | | | | | | | |
| Push provisioning | | | | | | | |
| Tokenization | | | | | | | |
| Virtual cards (retail) | | | | | | | |
| Virtual cards (business) | | | | | | | |
| Visa DCAS | | | | | | | |
| Spend controls | | | | | | | |
| AP automation | | | | | | | |
| Expense reporting | | | | | | | |

Add rows as the research surfaces new feature dimensions.

### 4. Build/Buy/Partner analysis — per feature gap

For every gap identified in Step 3, produce three blocks.  Read
`references/vendor-integration-notes.md` for the BUY details.

```
Feature: [name]

BUILD
  Effort:   [Low / Medium / High]  — key engineering tasks
  Cost:     [estimate or range]
  Timeline: [rough phases, not calendar dates]

BUY
  Top vendors: [1st choice + why] / [2nd choice + why]
  Integration: [key touchpoints with Tyfone's existing API/SSO layer]
  Pricing model: [per-card, per-txn, volume tiers — from vendor-integration-notes.md]

PARTNER
  Tyfone ecosystem fit: [which existing Tyfone integrations / CU partners help?]
  Complexity: [Low / Medium / High]
  Risk: [dependency, lock-in, competitive tension]
```

### 5. Assemble the final deliverable

Use this exact section order.  Do not skip sections.

```
1. Executive Summary
   - 3-5 bullet points: biggest competitor moves + top strategic recommendations

2. Cards Feature Matrix vs Competitors
   - The table from Step 3

3. Build/Buy/Partner Recommendations
   - One BUILD / BUY / PARTNER block per feature gap (from Step 4)

4. Business Banking Cards
   - Sub-sections: Virtual cards, AP automation, Expense controls
   - Competitor-by-competitor comparison within each sub-section

5. Recent Competitor Moves (last 90 days)
   - One bullet-list per competitor; cite source URL

6. Sources
   - 10+ URLs minimum; every URL used or consulted in this research
```

---

## Guardrails

- **USA-only scope** — do not include EU / APAC card-program details unless
  explicitly asked.
- **2025-2026 priority** — flag any data older than 2024 as potentially stale.
- **Tyfone perspective** — frame every recommendation in terms of impact on
  Tyfone's CU clients and Tyfone's platform roadmap.
- **Do not fabricate** competitor capabilities.  Mark unknown cells as
  "Not confirmed" and note what source would confirm them.
