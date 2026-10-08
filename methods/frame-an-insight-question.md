---
id: "ti:me:frame-an-insight-question"
type: "method"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_models: ["ti:mo:question-and-system-boundary-model"]
uses_concepts: ["ti:c:technical-insight"]
references: ["ti:r:nasa-undated-decision-analysis", "ti:r:nist-undated-measurement-uncertainty"]
---

# Frame an insight question

## Key takeaway

Turn a broad technical concern into a scoped uncertainty that matters to a decision.

## Summary

Use this before collecting a large bibliography or committing to a favoured mechanism. The output is a bounded question, outcome, comparison, context and authority limit. It accommodates faults, surprising results and opportunities for a new capability.

## Inputs and prerequisites

An initial concern, a decision owner or intended reader, available observations and known constraints. No permission to change a physical system or production service is inferred from permission to investigate it.

## Rationale

The boundary and objective determine what evidence would be useful. A topic such as “better cooling” is under-specified: a short transient and continuous operation can reward different properties.

## Procedure

1. Write the purpose in ordinary language: what decision or understanding should change when the uncertainty is reduced.
2. Describe what is known without adding a cause. Separate the report, the measurement conditions and the proposed interpretation.
3. Name the outcome and comparator, with units or observable events. Distinguish response time, reliability, cost and other competing outcomes.
4. Draw the smallest useful boundary: inputs, outputs, storage, actors, interfaces and measurement route. Mark unknowns explicitly.
5. List hard constraints, experiment authority, harm/stop conditions and the owner of the next decision.
6. Write one question in the form “Under context C, does X alter Y relative to Z, and what would distinguish mechanisms A and B?” Do not invent a causal contrast when only descriptive work is possible.
7. Define a sufficient stopping state: a decision justified, a bounded uncertainty accepted, or a need for specialist work identified.

## Expected effect

A question that another engineer can interpret with the same scope and outcome. In a thermal example, “lower at 100 seconds” and “lower eventual rise” become separate claims.

## Validation and counterevidence

Check that plausible different answers would affect the decision. If every answer leads to the same action, reframe the question or stop. If the measurement or permitted test cannot answer it, narrow the claim.

## Limits

A written boundary can be wrong. Revisit it after unexplained observations. This method does not replace hazard assessment, legal authorization or discipline-specific requirements.

## Evidence and authorship

[NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md) [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md) provides the cited concepts or guidance. This particular procedure is authored synthesis, not an experimentally validated programme.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Question and system boundary model](../models/question-and-system-boundary-model.md)
- [Technical insight](../concepts/technical-insight.md)

- [NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md)
- [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md)

[Package home](../README.md)
