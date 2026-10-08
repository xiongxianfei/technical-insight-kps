---
id: "ti:me:build-an-explanatory-model"
type: "method"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_models: ["ti:mo:model-validity-envelope"]
uses_principles: ["ti:p:fit-does-not-establish-model-validity"]
references: ["ti:r:nasa-7009b-2024-models-and-simulations", "ti:r:nist-undated-model-fit-and-residuals", "ti:r:nist-undated-measurement-uncertainty"]
---

# Build an explanatory model

## Key takeaway

Represent the smallest set of relationships needed to explain or predict the decision-relevant behavior.

## Summary

Use an equation, event sequence, state diagram, causal sketch or constraint map. The model should define its elements and assumptions, produce an inspectable consequence and expose what it omits.

## Inputs and prerequisites

A question, candidate mechanisms, relevant source knowledge, units/events and intended use. Domain expertise is required when the physical, statistical or computational relationships are not known.

## Rationale

A picture or equation can make assumptions visible, but its scientific appearance does not establish validity. Implementation checks and empirical comparisons address different uncertainties.

## Procedure

1. Define intended use and the outcome the model must represent. Choose a boundary and time scale appropriate to that use.
2. Name variables/entities, units, states, inputs and outputs. Separate observed quantities, adjustable parameters and latent quantities.
3. Write the relationships, constraints or event order. Attribute scientific relationships; label approximations and design conventions.
4. Derive a qualitative or quantitative prediction and a limiting case. Check signs, units, conservation where applicable and consistency with the stated assumptions.
5. Distinguish calibration data from data used to evaluate predictions. Record what the parameter fitting can and cannot identify.
6. Compare rival structures and note where their predictions differ. Use residuals or error patterns when numerical observations exist.
7. Write a validity envelope with known checks, gaps and excluded use. Link the model to the Methods it informs, without claiming one Method is uniquely deduced.

## Expected effect

A representation that another engineer can reconstruct, inspect and challenge. The thermal example distinguishes energy storage from transfer before selecting a design.

## Validation and counterevidence

A unit error, failed limit or structured residual is reason to revisit the model. A correct analytic calculation verifies an implementation step, not the relevance of the model to actual equipment.

## Limits

A detailed model can add uncertain parameters without improving useful prediction. Do not use precision to hide structural uncertainty. Formal safety-critical assurance is outside this method alone.

## Evidence and authorship

[NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md) [NIST model fit and residual analysis](../references/nist-undated-model-fit-and-residuals.md) [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md) provides the cited concepts or guidance. This particular procedure is authored synthesis, not an experimentally validated programme.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Model validity envelope](../models/model-validity-envelope.md)
- [Fit does not establish model validity](../principles/fit-does-not-establish-model-validity.md)

- [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md)
- [NIST model fit and residual analysis](../references/nist-undated-model-fit-and-residuals.md)
- [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md)

[Package home](../README.md)
