---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:p:readiness-evidence-is-context-dependent"
type: "principle"
version: "2.0.0"
status: "active"
references: ["ti:r:nasa-2023-technology-readiness-levels"]
---

# Readiness evidence is context dependent

## Key takeaway

A demonstration supports readiness only for the technology and conditions it actually represents.

## Summary

Changes to configuration, integration or environment can introduce evidence gaps even when a component has previously worked. A numeric readiness label does not carry all those conditions by itself.

## Statement

Readiness evidence depends on the assessed technology, its configuration, integration and use environment; demonstration in one context does not establish readiness in every other context.

## Explanation

A component test omits some interfaces and operating conditions present in an integrated system. Changing a duty cycle, measurement route or deployment environment can expose a different limitation. This explains why readiness claims need a named subject and evidence boundary rather than a context-free score.

## Example and implications

A laboratory detector may recognize curated signals while an integrated device must also tolerate drift, power limits and missing communication. The old evidence remains useful, but some target questions remain unanswered. A new test is required only when the missing condition matters to the intended decision.

## Evidence and limits

[NASA TRL guidance](../references/nasa-2023-technology-readiness-levels.md) ties levels to demonstrations and environments. The cross-context reasoning here is an engineering inference, not a proof that all transfers fail. This Principle does not prescribe a universal readiness gate or exact record schema.
