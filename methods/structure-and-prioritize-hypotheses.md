---
id: "ti:me:structure-and-prioritize-hypotheses"
type: "method"
version: "1.1.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-08"
basis_kind: "Bain-inspired authored engineering adaptation"
uses_models: ["ti:mo:hypothesis-prediction-matrix", "ti:mo:investigation-and-intelligence-routing-model"]
references: ["ti:r:bain-undated-case-interview-preparation", "ti:r:nasa-undated-decision-analysis"]
---

# Structure and prioritize hypotheses

## Key takeaway

Decompose the question, keep rival explanations visible and investigate the uncertainty most likely to change the decision.

## Summary

This Bain-inspired engineering adaptation uses objective clarification and structured reasoning to create a short investigation queue. It adds explicit predictions and counterevidence from the existing KPS investigation methods. It is not an official Bain procedure or evidence that a plausible business case establishes technical truth.

## Inputs and prerequisites

A decision, bounded outcome, existing observations and safe access to information. Identify non-negotiable safety or compliance limits before prioritizing tests. Obtain permission before querying confidential systems, altering equipment or collecting restricted data.

## Rationale

A decomposition can expose overlooked questions; it can also hide interactions if its branches are treated as independent. A hypothesis is useful when it predicts something different from its rivals. Investigation priority reflects the consequences of uncertainty and the feasibility of obtaining discriminating evidence, not confidence in a preferred answer.

## Procedure

1. Write the decision, current baseline and an observable target. Separate a proposed implementation from the need it serves.
2. Decompose the question into a few investigable branches. Mark overlaps and dependencies; do not force a neat issue tree onto coupled mechanisms.
3. For each important branch, write at least one plausible explanation and a meaningful rival, or state that alternatives are not yet known. Include measurement or selection error when relevant.
4. Create a table with hypothesis, current support, distinguishing prediction, possible contrary result, missing evidence and proposed check. A restatement of the symptom is not an explanation.
5. Prioritize qualitatively: would resolving this uncertainty alter the choice; can the check distinguish rivals; what are its cost, delay, authority and risk? Keep the reasons visible. Numerical scores without defensible scales add false precision.
6. Select one next check and record a stopping rule. Keep other material unknowns in the queue, not erased because only one task is active.
7. After the check, distinguish what ran, what was observed and how confidence changed. Reopen a branch when the evidence contradicts its premise.

## Worked example

A checksum check passes locally but fails in CI. Candidate explanations are inconsistent file inclusion, changed bytes and path handling. Comparing the two file sets is a focused first check if the error concerns coverage, because it distinguishes inclusion mismatch before costly environmental speculation. This is an illustrative choice, not a new claim about any current repository.

## Expected effect and validation

The output is a reasoned queue and one discriminating action. Ask whether a different result could change the conclusion. If all branches merely justify the favored solution, rebuild the alternatives. If the chosen observation cannot distinguish them, narrow the claim or choose another test.

## Optional tools

A Markdown table or paper is sufficient. An AI assistant may propose missing branches, but the engineer verifies claims, source passages and test safety. A spreadsheet is useful only when the comparison genuinely needs calculation.

## Limits and evidence

Bain's public case-interview guidance supports framing, structure and adaptation, not the exact algorithm above. NASA's decision-analysis guidance supports objectives, alternatives and decision-relevant uncertainty. The hypothesis queue and counterevidence checks are our synthesis. They neither guarantee completeness nor prove causality.

## Deeper knowledge

[Bain guidance](../references/bain-undated-case-interview-preparation.md), [NASA decision analysis](../references/nasa-undated-decision-analysis.md), [hypothesis prediction matrix](../models/hypothesis-prediction-matrix.md), and [design a discriminating test](design-a-discriminating-test.md).
