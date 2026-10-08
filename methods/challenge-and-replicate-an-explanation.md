---
id: "ti:me:challenge-and-replicate-an-explanation"
type: "method"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_principles: ["ti:p:reproducibility-does-not-establish-correctness"]
uses_models: ["ti:mo:model-validity-envelope"]
references: ["ti:r:sandve-2013-reproducible-computational-research", "ti:r:nasa-7009b-2024-models-and-simulations", "ti:r:nist-undated-model-fit-and-residuals"]
---

# Challenge and replicate an explanation

## Key takeaway

Choose a challenge that changes an evidential dependency instead of merely rerunning the same calculation.

## Summary

Use this when an insight will support consequential or repeated action. The goal is to reveal sensitivity, hidden assumptions, alternate causes or failures outside the original conditions.

## Inputs and prerequisites

A scoped claim, model/evidence version, current limits and a safe authorized way to inspect or test it. Replication may need independent instruments, people, data or conditions rather than identical repeated processing.

## Rationale

Reproducible output is valuable but can preserve a shared error. Distinguishing reproducibility, independent replication, robustness and transfer helps select the challenge that matters.

## Procedure

1. List the dependencies that could make the conclusion wrong: inputs, calibration, code, model structure, selection, context and evaluator judgment.
2. Select a meaningful challenge: reproduce the analysis, independently check units/implementation, replicate with new units/data, test a boundary case or evaluate an alternative model.
3. State what remains shared. Do not call a reanalysis of the same experiment an independent replication.
4. Use an authorized safe design with predicted contrary outcomes; separate new calibration from testing.
5. Compare the result and investigate disagreement before pooling. Different context can be a boundary condition rather than misconduct or simple error.
6. Update the claim’s scope and confidence narrative, then identify affected Models, Methods and Practices.

## Expected effect

A stronger or narrower insight with explicit remaining dependencies. A refuted claim is a useful outcome.

## Validation and counterevidence

Check that the challenge could genuinely reduce confidence. If every possible result is explained away by changing the story, sharpen the claim. Passing one boundary test does not validate all untested conditions.

## Limits

Independent expertise may be necessary. A replication cannot safely reproduce a dangerous failure in production just to remove uncertainty.

## Evidence and authorship

[Reproducible computational research](../references/sandve-2013-reproducible-computational-research.md) [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md) [NIST model fit and residual analysis](../references/nist-undated-model-fit-and-residuals.md) provides the cited concepts or guidance. This particular procedure is authored synthesis, not an experimentally validated programme.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Reproducibility does not establish correctness](../principles/reproducibility-does-not-establish-correctness.md)
- [Model validity envelope](../models/model-validity-envelope.md)

- [Reproducible computational research](../references/sandve-2013-reproducible-computational-research.md)
- [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md)
- [NIST model fit and residual analysis](../references/nist-undated-model-fit-and-residuals.md)

[Package home](../README.md)
