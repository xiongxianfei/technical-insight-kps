---
id: "ti:me:evaluate-results-and-uncertainty"
type: "method"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_principles: ["ti:p:a-useful-intervention-need-not-identify-its-mechanism"]
uses_models: ["ti:mo:claim-evidence-inference-model"]
references: ["ti:r:nist-undated-model-fit-and-residuals", "ti:r:nist-undated-experimental-design-handbook", "ti:r:pearl-2009-causal-inference-in-statistics"]
---

# Evaluate results and uncertainty

## Key takeaway

Judge the claim against what actually happened, its uncertainty and competing explanations.

## Summary

Use this after a valid test or source extraction. The output is a qualified claim assessment, not a binary pass label divorced from scope.

## Inputs and prerequisites

Original observations, analysis plan, configuration/fidelity record, expected and contrary predictions, uncertainty information and competing explanations.

## Rationale

A favourable metric can coexist with a wrong mechanism, an unmeasured harm or a confounded comparison. Evaluation must distinguish execution, outcome, inference and decision.

## Procedure

1. Check execution fidelity and measurement validity before interpreting the outcome. Label invalid or incomplete comparisons.
2. Compare the planned response, uncertainty and tolerances with observations. Record effect magnitude and practical significance, not only a significance label.
3. For numerical models inspect residuals, variation across conditions and sensitivity. Separate calibration fit from independent evaluation.
4. Evaluate the predictions of rival accounts. Identify which are weakened, remain compatible or were not tested.
5. Inspect adverse outcomes and changed conditions. Keep exploratory analyses identifiable; do not retrospectively present selected results as a preregistered confirmation.
6. Write separate conclusions for effect evidence, mechanism evidence, scope and adoption. Use supported-within-context, weakened, contradicted or unresolved with reasons.
7. Choose a next discriminating check, a bounded application or stopping. Record what new evidence would reverse the conclusion.

## Expected effect

An assessment that states both the supported conclusion and the remaining uncertainty. “A helps under B0 but not B1” can replace an overgeneral “A helps.”

## Validation and counterevidence

A reviewer can trace the verdict to raw evidence and assumptions. If the verdict ignores a failed manipulation or competing prediction, revise it. A small sample does not become conclusive by adding decimal places.

## Limits

Formal statistical inference needs an appropriate sampling model. The package supplies no automatic p-values or confidence levels. Lack of detected difference is not proof of equivalence.

## Evidence and authorship

[NIST model fit and residual analysis](../references/nist-undated-model-fit-and-residuals.md) [NIST experimental design guidance](../references/nist-undated-experimental-design-handbook.md) [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md) provides the cited concepts or guidance. This particular procedure is authored synthesis, not an experimentally validated programme.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [A useful intervention need not identify its mechanism](../principles/a-useful-intervention-need-not-identify-its-mechanism.md)
- [Claim evidence and inference model](../models/claim-evidence-inference-model.md)

- [NIST model fit and residual analysis](../references/nist-undated-model-fit-and-residuals.md)
- [NIST experimental design guidance](../references/nist-undated-experimental-design-handbook.md)
- [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md)

[Package home](../README.md)
