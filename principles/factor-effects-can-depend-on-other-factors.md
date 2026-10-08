---
id: "ti:p:factor-effects-can-depend-on-other-factors"
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
references: ["ti:r:nist-undated-experimental-design-handbook"]
---

# Factor effects can depend on other factors

## Key takeaway

An adjustment can help under one setting and hinder under another.

## Summary

Interaction means that the effect of changing one factor depends on the level of another. A marginal average can hide the conditions under which a method is useful.

## Statement

An adjustment can help under one setting and hinder under another.

## Explanation and derivation

NIST factorial design guidance makes joint factor combinations explicit. The inference for insight work is that a one-factor result needs a stated operating context; interaction questions may require a joint design rather than another isolated comparison.

## Application example

In the synthetic four-cell example, A changes the response by +4 units when B is low and by -2 when B is high. Neither “A always helps” nor the average effect captures both contexts.

## Scope and counterevidence

Every possible interaction need not be tested. Select those material to the mechanism or decision. One result per cell can show a numerical pattern in a constructed example but cannot estimate experimental variability or justify significance.

## Evidence summary

[NIST experimental design guidance](../references/nist-undated-experimental-design-handbook.md) The stated connection to Technical Insight KPS is authored reasoning. These sources do not evaluate the effectiveness of this complete framework.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Hypothesis prediction matrix](../models/hypothesis-prediction-matrix.md)
- [Design a discriminating test](../methods/design-a-discriminating-test.md)

- [NIST experimental design guidance](../references/nist-undated-experimental-design-handbook.md)

[Package home](../README.md)
