---
id: "ti:mo:decision-and-transfer-model"
type: "model"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_principles: ["ti:p:decision-preference-depends-on-objectives-and-uncertainty"]
uses_concepts: ["ti:c:transfer"]
uses_methods: ["ti:me:technology-readiness-assessment", "ti:me:sensitivity-analysis"]
references: ["ti:r:nasa-undated-decision-analysis", "ti:r:nasa-7009b-2024-models-and-simulations"]
---

# Decision and transfer model

## Key takeaway

Apply an insight by joining scoped evidence to a new context and a real decision.

## Summary

This model separates what is understood, what the target context changes and what stakeholders prefer. It supports provisional pilots and robust choices when a mechanism remains partially unresolved.

## Representation

```text
Source insight + source evidence envelope
                  |
             compare contexts
                  |
Target purpose + constraints + uncertainty
                  |
     alternatives and expected consequences
                  |
 authorized decision -> bounded use -> monitoring -> revision
```

For each alternative, record expected benefit, adverse effects, hard constraints, reversibility, evidence gaps and what observation would trigger reconsideration. A numeric score is optional, not evidence.

## Relationships and use

An insight can generate several interventions. Reject options that fail mandatory conditions before comparing preferences. Use sensitivity checks to identify which uncertain premises could reverse the choice. Further information is worthwhile when it can change a material decision enough to justify its cost.

## Assumptions

The decision owner and authority are known. Source and target have been compared on relevant mechanisms and conditions, not just labels. Monitoring can detect relevant harms before they become unacceptable.

## Limits and counterchecks

The model does not make all tradeoffs commensurable or permit dangerous field tests. If learning itself creates unacceptable risk, use analysis, a surrogate or specialist review instead. A decision can be useful without certifying a universal mechanism.

## Evidence summary

[NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md) [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md) supports the cited distinctions. The representation, examples and selection of fields here are authored models, not externally validated software or mandatory schemas.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Decision preference depends on objectives and uncertainty](../principles/decision-preference-depends-on-objectives-and-uncertainty.md)
- [Transfer](../concepts/transfer.md)
- [Assess transfer to a new context in the Practice](../practices/apply-and-transfer-an-insight.md#stage2-map-preserved-changed-and-unknown-assumptions)

- [NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md)
- [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md)

[Package home](../README.md)
