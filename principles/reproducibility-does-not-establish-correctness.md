---
id: "ti:p:reproducibility-does-not-establish-correctness"
type: "principle"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "explanatory synthesis with source premises and inference separated"
confidence: "scope dependent; application requires evaluation"
level: "domain"
uses_methods: ["ti:me:challenge-and-replicate-an-explanation", "ti:me:write-an-insight-record"]
references: ["ti:r:sandve-2013-reproducible-computational-research", "ti:r:w3c-2013-prov-overview"]
---

# Reproducibility does not establish correctness

## Key takeaway

The same inputs and procedure can reproduce the same error.

## Summary

Reproducibility permits inspection of the chain from inputs to outputs. It does not establish that inputs measure the intended quantity, assumptions are justified or the conclusion follows.

## Statement

The same inputs and procedure can reproduce the same error.

## Explanation and derivation

Sandve provides guidance for traceable computational work and W3C describes provenance. The distinction between repeatable production and correct interpretation is an explicit logical inference: both can be present or absent independently.

## Application example

A deterministic unit conversion bug can produce identical results on every run. Repeating the run tests stability, while an independent unit check tests correctness. Re-running the same model is not a new physical experiment.

## Scope and counterevidence

Reproducibility remains useful; this is not a reason to omit it. Independent replication can also share assumptions or instruments, so name what changed and what stayed common.

## Evidence summary

[Reproducible computational research](../references/sandve-2013-reproducible-computational-research.md) [W3C provenance overview](../references/w3c-2013-prov-overview.md) The stated connection to Technical Insight KPS is authored reasoning. These sources do not evaluate the effectiveness of this complete framework.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Challenge and replicate an explanation](../methods/challenge-and-replicate-an-explanation.md)
- [Write an insight record](../methods/write-an-insight-record.md)

- [Reproducible computational research](../references/sandve-2013-reproducible-computational-research.md)
- [W3C provenance overview](../references/w3c-2013-prov-overview.md)

[Package home](../README.md)
