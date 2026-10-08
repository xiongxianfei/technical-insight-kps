---
id: "ti:p:measurements-include-the-observation-process"
type: "principle"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "explanatory synthesis with source premises and inference separated"
confidence: "scope dependent; application requires evaluation"
level: "domain"
uses_models: ["ti:mo:measurement-and-uncertainty-model"]
uses_methods: ["ti:me:sipoc", "ti:me:measurement-uncertainty-budget"]
references: ["ti:r:nist-undated-measurement-uncertainty"]
---

# Measurements include the observation process

## Key takeaway

A reading depends on the target and on the instrument, sampling and processing used to observe it.

## Summary

A measurement is not a transparent window onto a system. Instrument response, calibration, placement, clock alignment, filtering and selection can create or hide patterns. Measurement hypotheses therefore compete with system hypotheses.

## Statement

A reading depends on the target and on the instrument, sampling and processing used to observe it.

## Explanation and derivation

NIST describes a measurement equation that includes significant input quantities and corrections. From this we infer that a surprising trace needs an audit of the acquisition path before attributing the pattern solely to the target system.

## Application example

A slower temperature trace can arise from sensor response as well as from a different object. Comparing a calibrated reference or acquisition settings can help distinguish the possibilities; it does not require dismissing the original sensor.

## Scope and counterevidence

This is not a claim that all measurements are unreliable or that every discrepancy is an instrument fault. The required audit depth depends on the effect size and consequences. Relevant changes to calibration or sampling can weaken a prior result.

## Evidence summary

[NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md) The stated connection to Technical Insight KPS is authored reasoning. These sources do not evaluate the effectiveness of this complete framework.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Measurement and uncertainty model](../models/measurement-and-uncertainty-model.md)
- [Audit an observation in the Practice](../practices/discover-and-validate-a-technical-insight.md#stage2-audit-the-evidence-before-the-story)

- [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md)

[Package home](../README.md)
