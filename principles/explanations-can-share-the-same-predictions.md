---
id: "ti:p:explanations-can-share-the-same-predictions"
type: "principle"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "explanatory synthesis with source premises and inference separated"
confidence: "scope dependent; application requires evaluation"
level: "domain"
uses_models: ["ti:mo:hypothesis-prediction-matrix"]
uses_methods: ["ti:me:design-a-discriminating-test"]
references: ["ti:r:pearl-2009-causal-inference-in-statistics", "ti:r:nasa-7009b-2024-models-and-simulations"]
---

# Explanations can share the same predictions

## Key takeaway

Evidence separates explanations only where their predicted consequences differ sufficiently.

## Summary

Several models can account for the same trace or successful intervention. Agreement with a prediction is informative, but not a unique identification when alternatives make that prediction too.

## Statement

Evidence separates explanations only where their predicted consequences differ sufficiently.

## Explanation and derivation

The causal-source distinction between observationally compatible accounts and additional causal assumptions supports this limitation. Logically, observing an outcome predicted by two hypotheses cannot by itself choose between them.

## Application example

A lower early temperature is compatible with less power, more heat storage, greater heat removal and a slower sensor. A later plateau, an independent power measurement or sensor-response check may discriminate particular pairs.

## Scope and counterevidence

Tests can still be useful without uniquely identifying a cause, for example by bounding unsafe outcomes. Some accounts remain indistinguishable under available ethical or practical interventions; report that rather than inventing certainty.

## Evidence summary

[Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md) [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md) The stated connection to Technical Insight KPS is authored reasoning. These sources do not evaluate the effectiveness of this complete framework.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Hypothesis prediction matrix](../models/hypothesis-prediction-matrix.md)
- [Design a discriminating test](../methods/design-a-discriminating-test.md)

- [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md)
- [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md)

[Package home](../README.md)
