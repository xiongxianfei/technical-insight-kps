---
id: "ti:p:validation-has-a-domain-of-applicability"
type: "principle"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "explanatory synthesis with source premises and inference separated"
confidence: "scope dependent; application requires evaluation"
level: "domain"
uses_models: ["ti:mo:model-validity-envelope"]
uses_methods: ["ti:me:assess-transfer-to-a-new-context"]
references: ["ti:r:nasa-7009b-2024-models-and-simulations"]
---

# Validation has a domain of applicability

## Key takeaway

Evidence supports a model or method for specified contexts and uses, not for every future application.

## Summary

Validation is relational: a particular model or method is assessed against evidence for an intended use within a domain. Changes to material, scale, environment, operator or consequence can require new assessment.

## Statement

Evidence supports a model or method for specified contexts and uses, not for every future application.

## Explanation and derivation

NASA model guidance explicitly includes intended use and domain of validation. Applying that distinction beyond simulation is an authored generalization: preserve the source conditions whenever reusing a conclusion.

## Application example

A controlled lab response at modest input cannot certify operation at a higher load or in a different environment. A software test on one input class need not cover concurrency or resource limits absent from that test.

## Scope and counterevidence

The principle is not a demand to repeat all evidence for every tiny change. Compare which assumptions the change affects. If none material changed, justify reuse; otherwise identify the smallest credible additional assessment.

## Evidence summary

[NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md) The stated connection to Technical Insight KPS is authored reasoning. These sources do not evaluate the effectiveness of this complete framework.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Model validity envelope](../models/model-validity-envelope.md)
- [Assess transfer to a new context](../methods/assess-transfer-to-a-new-context.md)

- [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md)

[Package home](../README.md)
