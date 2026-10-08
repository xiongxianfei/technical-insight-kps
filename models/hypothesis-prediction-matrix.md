---
id: "ti:mo:hypothesis-prediction-matrix"
type: "model"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_principles: ["ti:p:explanations-can-share-the-same-predictions", "ti:p:factor-effects-can-depend-on-other-factors"]
uses_methods: ["ti:me:design-of-experiments", "ti:me:measurement-uncertainty-budget"]
references: ["ti:r:pearl-2009-causal-inference-in-statistics", "ti:r:nist-undated-experimental-design-handbook", "ti:r:openstax-2016-university-physics-heat-transfer"]
---

# Hypothesis prediction matrix

## Key takeaway

Choose observations where credible rival explanations predict meaningfully different outcomes.

## Summary

A matrix converts a list of hypotheses into discriminating questions. Rows are candidate explanations; columns are observable consequences under specified checks. A shared prediction is useful context but weak discrimination.

## Representation

| Candidate account | Early temperature lower | Long-run temperature lower | Input power lower |
|---|---|---|---|
| Increased heat capacity with fixed resistance and power | Predicted | Not predicted | Not predicted |
| Reduced thermal resistance with fixed capacity and power | Usually predicted in the chosen model | Predicted | Not predicted |
| Reduced input power | Predicted | Predicted | Predicted |
| Slower measurement response | Possible displayed effect | Not necessarily | Not predicted |

This is an illustrative matrix under explicit thermal and measurement assumptions, not real equipment evidence.

## Relationships and use

Specify how each cell follows, what range or event is expected and which uncertainty could hide a difference. Select a safe check that distinguishes the consequential alternatives. If hypotheses overlap, refine them or record joint possibilities rather than forcing exclusive labels.

## Assumptions

Predictions depend on model adequacy, intervention fidelity and measurement resolution. The candidate set is not guaranteed exhaustive. Observing one predicted cell does not establish the whole row.

## Limits and counterchecks

The matrix cannot recommend a harmful control or replace specialist experiment design. A vague prediction such as “may change” does not discriminate. If no available check separates rivals, keep multiple accounts and consider a robust action.

## Evidence summary

[Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md) [NIST experimental design guidance](../references/nist-undated-experimental-design-handbook.md) [OpenStax heat capacity and heat transfer](../references/openstax-2016-university-physics-heat-transfer.md) supports the cited distinctions. The representation, examples and selection of fields here are authored models, not externally validated software or mandatory schemas.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Explanations can share the same predictions](../principles/explanations-can-share-the-same-predictions.md)
- [Factor effects can depend on other factors](../principles/factor-effects-can-depend-on-other-factors.md)
- [Design a discriminating test in the Practice](../practices/discover-and-validate-a-technical-insight.md#stage5-design-a-discriminating-comparison)

- [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md)
- [NIST experimental design guidance](../references/nist-undated-experimental-design-handbook.md)
- [OpenStax heat capacity and heat transfer](../references/openstax-2016-university-physics-heat-transfer.md)

[Package home](../README.md)
