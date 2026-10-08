---
id: "ti:p:a-useful-intervention-need-not-identify-its-mechanism"
type: "principle"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "explanatory synthesis with source premises and inference separated"
confidence: "scope dependent; application requires evaluation"
level: "domain"
uses_methods: ["ti:me:statistical-hypothesis-testing", "ti:me:measurement-uncertainty-budget", "ti:me:sensitivity-analysis"]
uses_practices: ["ti:pr:apply-and-transfer-an-insight"]
references: ["ti:r:pearl-2009-causal-inference-in-statistics", "ti:r:nasa-undated-decision-analysis"]
---

# A useful intervention need not identify its mechanism

## Key takeaway

Evidence that a change helps and evidence explaining why it helps are different claims.

## Summary

An intervention can meet a goal while the causal mechanism remains uncertain. Conversely a plausible mechanism can be understood without knowing an effective or safe implementation.

## Statement

Evidence that a change helps and evidence explaining why it helps are different claims.

## Explanation and derivation

The causal distinction between intervention effects and causal structure, together with intended-use evaluation, supports separating effect evidence from mechanism evidence. The package treats this as a scoped explanatory inference, not a universal guarantee of interventions.

## Application example

Reducing input load may remove an observed failure. That need not establish whether the failure arose from thermal limits, scheduling, supply limits or a measurement artifact. Adoption can be provisional while diagnosis continues.

## Scope and counterevidence

A coincident before/after improvement is not by itself evidence of intervention efficacy. Safety and adverse effects still need assessment. Do not keep an intervention that violates a hard constraint merely because one metric improves.

## Evidence summary

[Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md) [NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md) The stated connection to Technical Insight KPS is authored reasoning. These sources do not evaluate the effectiveness of this complete framework.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Evaluate results and uncertainty in the Practice](../practices/discover-and-validate-a-technical-insight.md#stage7-evaluate-the-explanation-and-its-limits)
- [Apply and transfer an insight](../practices/apply-and-transfer-an-insight.md)

- [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md)
- [NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md)

[Package home](../README.md)
