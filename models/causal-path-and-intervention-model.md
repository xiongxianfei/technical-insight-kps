---
id: "ti:mo:causal-path-and-intervention-model"
type: "model"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_principles: ["ti:p:associations-do-not-determine-interventions", "ti:p:a-useful-intervention-need-not-identify-its-mechanism"]
uses_methods: ["ti:me:build-an-explanatory-model"]
references: ["ti:r:pearl-2009-causal-inference-in-statistics", "ti:r:nist-undated-experimental-design-handbook"]
---

# Causal path and intervention model

## Key takeaway

An intervention changes a system relation; a correlation only describes observed co-variation.

## Summary

A causal sketch exposes the proposed influences and confounders behind an action. It is a set of assumptions to scrutinize, not a result produced merely by drawing arrows.

## Representation

```text
Demand -> Heat generation -> Temperature -> Measured temperature
                                 |
                                 v
                            Controller -> Fan speed
                                           |
                                           v
                                      Heat removal
                                           |
                                           +----> Temperature
```

The feedback loop is a time-evolving system. For a static acyclic causal analysis, index the relevant variables by time rather than treating a cyclic sketch as a DAG. The sign and strength of each effect need evidence.

## Relationships and use

A high fan speed may be observed together with a high temperature because of controller response. A safe intervention question asks what happens when fan operation changes under controlled demand and context. Measure whether the intended intervention actually occurred and whether other paths changed.

## Assumptions

All material confounders are not guaranteed visible. Delays and feedback matter. The sketch is valid only at its declared level and time scale; a structural causal analysis needs a more precise formalization.

## Limits and counterchecks

No fan experiment is authorized by this file. Observation can constrain the sketch but need not identify it uniquely. A useful effect estimate and a correct complete mechanism are different goals.

## Evidence summary

[Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md) [NIST experimental design guidance](../references/nist-undated-experimental-design-handbook.md) supports the cited distinctions. The representation, examples and selection of fields here are authored models, not externally validated software or mandatory schemas.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Associations do not determine intervention effects](../principles/associations-do-not-determine-interventions.md)
- [A useful intervention need not identify its mechanism](../principles/a-useful-intervention-need-not-identify-its-mechanism.md)
- [Build an explanatory model](../methods/build-an-explanatory-model.md)

- [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md)
- [NIST experimental design guidance](../references/nist-undated-experimental-design-handbook.md)

[Package home](../README.md)
