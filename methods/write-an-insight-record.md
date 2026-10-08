---
id: "ti:me:write-an-insight-record"
type: "method"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_concepts: ["ti:c:technical-insight"]
uses_principles: ["ti:p:novelty-and-support-are-different-properties"]
uses_models: ["ti:mo:claim-evidence-inference-model"]
references: ["ti:r:sandve-2013-reproducible-computational-research", "ti:r:w3c-2013-prov-overview", "ti:r:kps-undated-authoring-contract-9x"]
---

# Write an insight record

## Key takeaway

Record the explanation, evidence, limits and consequences without turning a proposal into an observed result.

## Summary

Use this to make technical understanding reusable and reviewable. The record is a supporting synthesis artifact; promote independently reusable knowledge into the five KPS types where appropriate.

## Inputs and prerequisites

Question, sources, observations, hypotheses, model, test plan/results, uncertainty, decision context and publication permissions. Unknown fields may remain explicitly unknown.

## Rationale

A short conclusion can omit the conditions that made it credible. A structured narrative preserves the path from observation to interpretation and application without copying all raw evidence.

## Procedure

1. Write a one-sentence insight: in context C, relationship X/Y holds or is proposed because of evidence E and reasoning M.
2. State why it changes prediction, diagnosis or design. Identify novelty relative to the project, not an unsupported field-wide claim.
3. Separate source findings, actual observations, synthetic calculations, hypotheses and decisions. Label each test planned, executed or illustrative.
4. Include the model/derivation, rival explanations, uncertainty and counterevidence. Name the applicability envelope and prohibited extrapolations.
5. Provide a compact example and nonexample, full provenance locators and inspected extent.
6. Map reusable definitions to Concepts, explanatory relationships to Principles, representations to Models, operations to Methods and orchestration to Practices. Do not create a sixth insights folder as a compulsory core type.
7. Review for confidentiality and self-containment. Preserve one canonical record and update linked local summaries deliberately.

## Expected effect

A locally understandable record that another engineer can challenge and use within scope.

## Validation and counterevidence

Hide links: can the reader understand the explanation and its limits? Restore links: do they support the actual claim? Remove unsupported causal language or success claims. The blank template is not an evidence record.

## Limits

Documentation is not validation. A polished narrative can faithfully describe an unresolved claim; it must not imply it has been experimentally confirmed.

## Evidence and authorship

[Reproducible computational research](../references/sandve-2013-reproducible-computational-research.md) [W3C provenance overview](../references/w3c-2013-prov-overview.md) [KPS authoring contract](../references/kps-undated-authoring-contract-9x.md) provides the cited concepts or guidance. This particular procedure is authored synthesis, not an experimentally validated programme.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Technical insight](../concepts/technical-insight.md)
- [Novelty and evidential support are different properties](../principles/novelty-and-support-are-different-properties.md)
- [Claim evidence and inference model](../models/claim-evidence-inference-model.md)

- [Reproducible computational research](../references/sandve-2013-reproducible-computational-research.md)
- [W3C provenance overview](../references/w3c-2013-prov-overview.md)
- [KPS authoring contract](../references/kps-undated-authoring-contract-9x.md)

[Package home](../README.md)
