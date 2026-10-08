---
id: "ti:p:fit-does-not-establish-model-validity"
type: "principle"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "explanatory synthesis with source premises and inference separated"
confidence: "scope dependent; application requires evaluation"
level: "domain"
uses_models: ["ti:mo:model-validity-envelope"]
uses_methods: ["ti:me:evaluate-results-and-uncertainty"]
references: ["ti:r:nist-undated-model-fit-and-residuals", "ti:r:nasa-7009b-2024-models-and-simulations"]
---

# Fit does not establish model validity

## Key takeaway

Matching data is one check of a model, not proof of correct implementation, mechanism or future applicability.

## Summary

A model can fit calibration data closely through flexible parameters, compensating errors or omitted variables. Adequacy depends on intended use, assumptions, implementation checks and relevant independent comparisons.

## Statement

Matching data is one check of a model, not proof of correct implementation, mechanism or future applicability.

## Explanation and derivation

NIST recommends examining residual structure rather than relying only on a fit statistic. NASA separates calibration, verification and validation. Together they support a layered credibility argument, not an automatic validity score.

## Application example

A thermal curve can be matched by altering an effective time constant without identifying whether resistance or capacitance changed. The fitted curve must be checked against power, limiting behavior and data not used for fitting.

## Scope and counterevidence

A predictive black box can be adequate for a bounded use without revealing the true mechanism. Clean residuals are not proof of causality. Extrapolation, new loads or changed sensors can invalidate the application even when old fit remains excellent.

## Evidence summary

[NIST model fit and residual analysis](../references/nist-undated-model-fit-and-residuals.md) [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md) The stated connection to Technical Insight KPS is authored reasoning. These sources do not evaluate the effectiveness of this complete framework.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Model validity envelope](../models/model-validity-envelope.md)
- [Evaluate results and uncertainty](../methods/evaluate-results-and-uncertainty.md)

- [NIST model fit and residual analysis](../references/nist-undated-model-fit-and-residuals.md)
- [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md)

[Package home](../README.md)
