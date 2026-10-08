---
id: "ti:p:associations-do-not-determine-interventions"
type: "principle"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "explanatory synthesis with source premises and inference separated"
confidence: "scope dependent; application requires evaluation"
level: "domain"
uses_models: ["ti:mo:causal-path-and-intervention-model"]
uses_methods: ["ti:me:generate-competing-explanations"]
references: ["ti:r:pearl-2009-causal-inference-in-statistics"]
---

# Associations do not determine intervention effects

## Key takeaway

A relationship in observed data alone does not identify what changing one factor will cause.

## Summary

Shared causes, selection and reverse influence can produce an association. An intervention question requires assumptions about how the system responds when an input is changed, not only how variables co-vary.

## Statement

A relationship in observed data alone does not identify what changing one factor will cause.

## Explanation and derivation

Pearl distinguishes observational distributions from intervention statements. The package uses that distinction to require an explicit bridge between a correlation, a mechanism account and a proposed action.

## Application example

High temperature and high fan speed can occur together because a controller raises fan speed when temperature rises. That association does not imply increasing the fan causes heating. Inspect the control loop and the conditions of a safe intervention.

## Scope and counterevidence

Experiments also require valid assignment, implementation and measurement. A randomized test of an outcome does not automatically identify every mediating mechanism. This principle does not prohibit observational reasoning; it limits unsupported causal conclusions.

## Evidence summary

[Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md) The stated connection to Technical Insight KPS is authored reasoning. These sources do not evaluate the effectiveness of this complete framework.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Causal path and intervention model](../models/causal-path-and-intervention-model.md)
- [Generate competing explanations](../methods/generate-competing-explanations.md)

- [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md)

[Package home](../README.md)
