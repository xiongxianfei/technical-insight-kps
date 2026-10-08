---
id: "ti:me:generate-competing-explanations"
type: "method"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_principles: ["ti:p:explanations-can-share-the-same-predictions"]
uses_models: ["ti:mo:hypothesis-prediction-matrix"]
references: ["ti:r:pearl-2009-causal-inference-in-statistics", "ti:r:nasa-7009b-2024-models-and-simulations"]
---

# Generate competing explanations

## Key takeaway

Construct a small set of plausible accounts that differ in what they predict.

## Summary

Use this after bounding the question and auditing the observation. Include measurement, context, implementation and system mechanisms when relevant. The output is a hypothesis set, not a claim that every conceivable cause was enumerated.

## Inputs and prerequisites

A scoped observation/question, known mechanisms, constraints and source evidence. A hypothesis may be uncertain; it must not be presented as an established fact.

## Rationale

One familiar explanation can fit an observation without being unique. Rival accounts expose the missing information needed to justify a mechanism or choose a robust intervention.

## Procedure

1. State the observed pattern and the scope in which it occurs. Do not put the proposed cause inside the observation.
2. Generate explanations at different relevant locations: actual system change, environment/input change, measurement/processing change and interaction or feedback.
3. For each account write the intermediate mechanism and assumptions. Include a mixed-cause account where multiple changes can coexist.
4. Predict one result if the account is materially important and one result that would challenge it.
5. Reject only accounts inconsistent with reliable evidence or known constraints; mark missing evidence instead of assigning unsupported probabilities.
6. Build a hypothesis-prediction matrix and identify a safe observable difference between the leading accounts.

## Expected effect

The preferred explanation is exposed to a meaningful competitor. For a cooling trace, storage, transfer, input and sensor accounts lead to different checks.

## Validation and counterevidence

Ask a reviewer to propose an alternative consistent with the data. If two rows predict exactly the same available results, do not claim the planned test identifies one of them.

## Limits

An exhaustive “five whys” chain does not guarantee a unique root cause. Brainstorming is not evidence. Stop for missing expertise or unsafe discrimination rather than inventing an executable experiment.

## Evidence and authorship

[Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md) [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md) provides the cited concepts or guidance. This particular procedure is authored synthesis, not an experimentally validated programme.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Explanations can share the same predictions](../principles/explanations-can-share-the-same-predictions.md)
- [Hypothesis prediction matrix](../models/hypothesis-prediction-matrix.md)

- [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md)
- [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md)

[Package home](../README.md)
