---
id: "ti:mo:readiness-evidence-model"
type: "model"
version: "1.1.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-08"
basis_kind: "authored evidence representation"
uses_concepts: ["ti:c:technology-readiness"]
uses_principles: ["ti:p:readiness-evidence-is-context-dependent"]
references: ["ti:r:nasa-2023-technology-readiness-levels"]
---

# Readiness evidence model

## Key takeaway

Map each maturity claim to its criterion, demonstrated configuration and evidence gap before assigning a label.

## Summary

This model makes readiness assessable without confusing a supplier declaration with an independently observed demonstration. It can use a named TRL framework or a project-specific demonstration checklist. It does not define a new certification standard.

## Representation

| Field | Meaning |
|---|---|
| Assessment object | Particular technology and configuration, not a company name |
| Intended use | Capability, boundary and relevant operating environment |
| Framework | Named issuer, revision, criterion and interpretation |
| Demonstration | What was built, tested, simulated or observed, and by whom |
| Evidence | Source, date, locator, configuration and access extent |
| Gap | Material differences, missing criteria or untested integration |
| Judgment | Supported, unsupported or not assessed, with uncertainty |
| Next check | Evidence that would change the judgment |

Claim -> criterion -> demonstration -> evidence -> scope comparison -> qualified judgment. A vendor's asserted level and the assessor's evidence-backed conclusion occupy different fields.

## NASA scale as an example

The inspected NASA overview moves from principles and formulated applications (1-2), through proof of concept (3), laboratory/relevant-environment validation (4-5), prototype/model demonstration (6-7), to qualification and successful mission use (8-9). Later descriptions are aerospace-specific. Consult the selected framework's actual criteria rather than treating these bands as sufficient for assigning a number.

## Use and interpretation

Assess relevant criteria individually. Report the highest level whose required criteria are supported only when the chosen framework permits that conclusion. Otherwise report an evidence profile and withhold the number. Do not calculate an average TRL for components or infer system readiness from a component's level.

## Limits

The model captures a reasoned assessment, not independent certification. It does not combine desirability, manufacturing readiness, commercial viability or hazard acceptance into a single maturity claim.

## Deeper knowledge

[Technology readiness](../concepts/technology-readiness.md), [context-dependent evidence](../principles/readiness-evidence-is-context-dependent.md), and [NASA overview](../references/nasa-2023-technology-readiness-levels.md).
