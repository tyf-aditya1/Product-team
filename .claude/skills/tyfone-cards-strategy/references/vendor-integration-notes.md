# Vendor Integration Notes — Buy-Leg Reference

Use when populating the BUY block of each Build/Buy/Partner recommendation.
Each section covers API style, key integration touchpoints, and known
Tyfone-relevant caveats.

---

## Galileo (SoFi Technologies)

- **Strength**: Deepest virtual-card + issuer-processing stack in the
  market; powers many neobanks.
- **API style**: REST; well-documented sandbox; event-driven webhooks.
- **Cards coverage**: Full card lifecycle — issuance, provisioning,
  tokenization, spend controls, real-time transaction data.
- **Push provisioning**: Native support; handles Apple Pay / Google Pay
  provisioning flows end-to-end.
- **Business cards**: Commercial virtual-card programs supported;
  configurable limits + merchant controls.
- **Tyfone integration notes**: REST-to-REST integration is
  straightforward; auth via API-key + mTLS option. Sandbox
  environment available for CU demo flows. Pricing is per-card +
  per-transaction; negotiate volume tiers.
- **Watch**: Contract lock-in; SoFi owns Galileo — monitor for
  competitive tension if Tyfone serves SoFi competitors.

## Marqeta

- **Strength**: Best-in-class open card-issuing platform; real-time
  decisioning.
- **API style**: REST; comprehensive docs; webhook-driven event model.
- **Cards coverage**: Virtual + physical issuance; instant provisioning;
  granular spend controls (MCC, amount, geo, time).
- **Push provisioning**: Fully supported; wallet provisioning APIs.
- **Business cards**: Strong commercial-card story; AP automation
  use-cases well-supported; expense-card programs.
- **Tyfone integration notes**: Modern API design maps well to
  Tyfone's existing SSO/API layer. Sandbox + simulated transaction
  replay available. Per-card + interchange-share pricing model.
- **Watch**: Minimum volume commitments on enterprise tiers; review
  SLAs for card-art approval pipeline.

## Stripe Issuing

- **Strength**: Developer-experience leader; fastest time-to-first-card
  among card-issuing APIs.
- **API style**: REST; excellent docs + SDKs (JS, Python, Go, etc.).
- **Cards coverage**: Virtual + physical; instant provisioning;
  spend controls; 3DS support.
- **Push provisioning**: Supported via Stripe's wallet provisioning
  flow (limited to Stripe-supported regions — confirm USA CU
  eligibility).
- **Business cards**: Virtual expense cards; per-card spend limits;
  basic category controls.
- **Tyfone integration notes**: Easiest sandbox onboarding of any
  vendor. Auth is API-key-based. However, Stripe Issuing is
  primarily designed for fintech / neobank issuers — confirm that
  credit-union-issued cards are in scope before committing.
- **Watch**: Regulatory path for CU-issued cards through Stripe may
  require a BIN sponsor arrangement; confirm with compliance.

## Synctera

- **Strength**: Compliance-first; purpose-built for banks + CUs;
  Banking-as-a-Service middleware.
- **API style**: REST; good docs; compliance guardrails baked into
  API responses.
- **Cards coverage**: Virtual card issuance; spend controls;
  tokenization delegation to network.
- **Push provisioning**: Supported but less battle-tested than
  Galileo / Marqeta at scale.
- **Business cards**: Early-stage; fewer public case studies for
  commercial cards vs. Galileo / Marqeta.
- **Tyfone integration notes**: Best fit for Tyfone when the CU
  client needs compliance automation layered on top of card
  issuance. Avoid choosing Synctera solely for cards — the value
  is the compliance + identity layer.
- **Watch**: Smaller scale; monitor financial stability + roadmap
  continuity.
