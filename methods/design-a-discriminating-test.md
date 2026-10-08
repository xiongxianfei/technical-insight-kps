---
id: "ti:me:design-a-discriminating-test"
type: "method"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_models: ["ti:mo:hypothesis-prediction-matrix", "ti:mo:measurement-and-uncertainty-model"]
uses_principles: ["ti:p:factor-effects-can-depend-on-other-factors"]
references: ["ti:r:nist-undated-experimental-design-handbook", "ti:r:pearl-2009-causal-inference-in-statistics", "ti:r:nist-undated-measurement-uncertainty"]
---

# Design a discriminating test

## Key takeaway

Select a permitted comparison where rival accounts differ beyond relevant uncertainty.

## Summary

Use this to move from a plausible explanation to an assessment plan. A test can be an analytic counterexample, software fixture, simulation, reanalysis or approved experiment. The output is a plan, not a result.

## Inputs and prerequisites

Rival hypotheses and predictions, measurement capability, domain expertise, experimental units, constraints and an authorized safe test setting. Live-system and physical interventions need applicable safety and change approval.

## Rationale

A repeated test that all hypotheses pass adds little discrimination. Assignment, nuisance control, interaction and measurement determine what conclusion a comparison can support.

## Procedure

1. Choose the claim and competing account to distinguish. Define expected outcomes and a contrary signal before collecting confirmatory data.
2. Choose the least risky credible test: existing evidence or calculation may be enough; a physical or production test is not the default.
3. Specify the experimental unit, factor levels, response, conditions and measurement uncertainty. Distinguish independent replicates from repeated readings.
4. Choose controls for the actual alternatives. Block known nuisance factors; randomize order when feasible and justified. Address carryover and drift. Use joint/factorial variation when interactions are material rather than imposing one-factor-at-a-time universally.
5. Plan replication and sample size against effect size, variability and decision consequences with statistical help when needed. Do not impose an arbitrary small number as proof.
6. Define execution-fidelity checks, data exclusions, analysis, tolerances and stopping rules in advance. Preserve exploratory departures separately.
7. Obtain permission, safeguards and rollback/abort responsibility. If a control is harmful, use a safe substitute or change the question.
8. Record what each possible result will and will not establish, including inconclusive or failed-execution outcomes.

## Expected effect

An inspectable test plan that can discriminate a meaningful alternative or clearly bounds uncertainty.

## Validation and counterevidence

Review whether the factor actually changes the proposed mechanism and whether a nuisance change can explain the same outcome. A test is inadequate if its predictions overlap within measurement uncertainty or if the comparator is unsafe.

## Limits

This general method is not a protocol for hazardous equipment, medical/human research or offensive security testing. Some questions cannot be resolved with permitted tests; record that limitation.

## Evidence and authorship

[NIST experimental design guidance](../references/nist-undated-experimental-design-handbook.md) [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md) [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md) provides the cited concepts or guidance. This particular procedure is authored synthesis, not an experimentally validated programme.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Hypothesis prediction matrix](../models/hypothesis-prediction-matrix.md)
- [Measurement and uncertainty model](../models/measurement-and-uncertainty-model.md)
- [Factor effects can depend on other factors](../principles/factor-effects-can-depend-on-other-factors.md)

- [NIST experimental design guidance](../references/nist-undated-experimental-design-handbook.md)
- [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md)
- [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md)

[Package home](../README.md)
