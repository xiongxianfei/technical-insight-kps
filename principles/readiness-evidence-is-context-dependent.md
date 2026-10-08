---
id: "ti:p:readiness-evidence-is-context-dependent"
type: "principle"
version: "1.1.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-08"
basis_kind: "scoped engineering inference"
uses_principles: ["ti:p:validation-has-a-domain-of-applicability"]
references: ["ti:r:nasa-2023-technology-readiness-levels"]
---

# Readiness evidence is context dependent

## Key takeaway

A demonstration supports the conditions actually represented; changes of environment or integration can leave new capability claims unsupported.

## Summary

A technology can have substantial evidence in one use and limited evidence in another. Readiness therefore depends on the evaluated configuration, relevant operating conditions and assessment criteria. This explanatory relationship does not prescribe one universal maturity scale.

## Statement

Evidence that a technology works in configuration C and environment E does not, without a justified transfer argument, establish its readiness in a materially different configuration or environment.

## Explanation and derivation

An experiment exposes a particular system to selected conditions and measurements. Altering load, scale, interfaces or failure recovery changes what must be demonstrated. NASA's TRL overview explicitly distinguishes laboratory, representative and operational evidence. The existing model-applicability principle similarly limits extrapolation beyond tested conditions. From these premises we infer that a readiness record needs its object and context, not just an ordinal label.

## Example and application

A sensor demonstrated on a bench may still need evidence about installation, interference and calibration drift in service. A Method can assess the missing demonstrations; a roadmap can schedule an integration trial. Neither application requires declaring all earlier evidence invalid.

## Limits and counterevidence

Not every context change is material. A justified similarity argument or accepted equivalence assessment may support transfer. The assessor must expose that argument rather than assuming either automatic transfer or automatic failure. This Principle does not establish any specific TRL threshold or certify a system.

## Evidence summary and deeper knowledge

[NASA readiness guidance](../references/nasa-2023-technology-readiness-levels.md) supplies environment distinctions. [Validation applicability](validation-has-a-domain-of-applicability.md) explains the broader reasoning. The cross-domain inference is authored here, not a separately validated NASA policy.
