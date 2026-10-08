---
id: "ti:mo:model-validity-envelope"
type: "model"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_principles: ["ti:p:fit-does-not-establish-model-validity", "ti:p:validation-has-a-domain-of-applicability"]
uses_methods: ["ti:me:challenge-and-replicate-an-explanation"]
references: ["ti:r:nasa-7009b-2024-models-and-simulations", "ti:r:nist-undated-model-fit-and-residuals"]
---

# Model validity envelope

## Key takeaway

Record where a model was checked and what decision those checks can support.

## Summary

The envelope joins intended use, assumptions, implementation verification, calibration, validation comparisons and uncertainty. It prevents a fitted model from becoming an unqualified explanation of every case.

## Representation

| Dimension | Record |
|---|---|
| Intended use | Decision, output and consequence of error |
| Structure | Equations, processes or relationships represented |
| Assumptions | Approximations and excluded mechanisms |
| Verification | Checks that implementation matches the specification |
| Calibration | Data and method used to select parameters |
| Validation | Relevant referent and conditions not hidden by calibration |
| Uncertainty | Input, parameter, structural and measurement limits |
| Envelope | Tested conditions, extrapolations and prohibited uses |

```text
Proposed use -> assumption check -> implementation check
     -> evidence comparison -> bounded credibility judgment
```

## Relationships and use

A model can pass unit tests and still represent the wrong system. Calibration and validation have different roles; using the same observations for both without qualification overstates independent support. Residual patterns can expose missing structure.

## Assumptions

The referent is credible enough for the use and its uncertainty is not ignored. Validation is tied to a model version and configuration. Analytic limiting cases check implementation, not empirical applicability.

## Limits and counterchecks

A compact envelope is not NASA conformance. An untested region is not automatically invalid, but confidence there needs an explicit basis. High-stakes applications require the relevant assurance process, not this template alone.

## Evidence summary

[NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md) [NIST model fit and residual analysis](../references/nist-undated-model-fit-and-residuals.md) supports the cited distinctions. The representation, examples and selection of fields here are authored models, not externally validated software or mandatory schemas.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Fit does not establish model validity](../principles/fit-does-not-establish-model-validity.md)
- [Validation has a domain of applicability](../principles/validation-has-a-domain-of-applicability.md)
- [Challenge and replicate an explanation](../methods/challenge-and-replicate-an-explanation.md)

- [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md)
- [NIST model fit and residual analysis](../references/nist-undated-model-fit-and-residuals.md)

[Package home](../README.md)
