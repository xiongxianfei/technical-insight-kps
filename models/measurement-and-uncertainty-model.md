---
id: "ti:mo:measurement-and-uncertainty-model"
type: "model"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_principles: ["ti:p:measurements-include-the-observation-process"]
uses_methods: ["ti:me:audit-an-observation"]
references: ["ti:r:nist-undated-measurement-uncertainty"]
---

# Measurement and uncertainty model

## Key takeaway

Model the route from the target quantity to the reported value before interpreting a small difference.

## Summary

This is a map of the measurement chain and its uncertainties, not a ready-made numerical uncertainty budget. It helps identify calibration, response, timing, sampling and transformation effects that can alter the inference.

## Representation

```text
Target quantity at place and time
       -> sensor or observation channel
       -> calibration and acquisition
       -> filtering and transformations
       -> reported value and uncertainty
```

A general measurement equation is `y = f(x1, ..., xn)`.
An illustrative additive approximation is `reading = target + offset + variable error`.
The latter is a model assumption; lag, saturation and nonlinear conversion require other terms.

| Check | Consequence of omission |
|---|---|
| Units and reference frame | Numerically plausible but wrong comparisons |
| Calibration and shared offsets | Repetition mistaken for accuracy |
| Response time and time alignment | A transient mistaken for system dynamics |
| Missingness and filtering | Important excursions or cases removed |

## Relationships and use

Explain each term, its source and why it matters for the decision. Distinguish uncertainty in a measured input from uncertainty in the structural model. Track correlated errors when deriving differences; they can cancel or reinforce rather than behaving independently.

## Assumptions

The measurand and evaluation conditions are defined. A statistical model of repeated readings does not describe every instrument error. Sampling assumptions must fit the physical or software measurement process.

## Limits and counterchecks

No numerical error bounds are supplied by this diagram. A full budget and acceptance decision need appropriate metrology expertise. Precision of display is not uncertainty, and normal residuals do not eliminate systematic errors.

## Evidence summary

[NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md) supports the cited distinctions. The representation, examples and selection of fields here are authored models, not externally validated software or mandatory schemas.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Measurements include the observation process](../principles/measurements-include-the-observation-process.md)
- [Audit an observation](../methods/audit-an-observation.md)

- [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md)

[Package home](../README.md)
