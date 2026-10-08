---
id: "ti:me:assess-technology-readiness"
type: "method"
version: "1.1.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-08"
basis_kind: "NASA-informed authored assessment method"
uses_concepts: ["ti:c:technology-readiness"]
uses_models: ["ti:mo:readiness-evidence-model"]
uses_principles: ["ti:p:readiness-evidence-is-context-dependent"]
references: ["ti:r:nasa-2023-technology-readiness-levels"]
---

# Assess technology readiness

## Key takeaway

Assess demonstrated capability against a named framework and target context before repeating a readiness label.

## Summary

Use this when a candidate is described as mature or ready but the relevant demonstrations are unclear. The output is a criterion-to-evidence assessment and a testable gap list. It can withhold a TRL number when the scale or evidence is inadequate.

## Inputs and prerequisites

The exact technology/configuration, target use and environment, selected readiness framework and revision, available demonstration records, and an authorized assessor. Do not assume a vendor label uses the same criteria as the receiving organization.

## Rationale

Evidence can be strong for one configuration yet leave another use unassessed. A progression from concept to laboratory validation to representative and operational demonstration reflects changing evidence demands. Readiness is not automatically cost-effectiveness, integration readiness, safety acceptance or adoption.

## Procedure

1. Name the object: component, process, subsystem or system. Record the configuration and claimed capability, not only a technology family name.
2. Select a suitable published framework and its actual criteria. NASA's nine-level aerospace overview is a reference example, not universal wording. If no suitable scale is established, use an explicit demonstration checklist and do not invent a certified TRL.
3. Define the relevant target environment: scale, loads, interfaces, users, duration and failure conditions that matter. Mark similarities and differences from the demonstrations.
4. For each criterion, record source, locator, evidence type, date, observed result and configuration. Separate supplier assertion, simulation, inspected test record and independent replication.
5. Mark criteria supported, not supported or not assessed. Explain scope limitations; missing access does not establish that a test failed.
6. Assign a qualified level only where the chosen framework and evidence permit it. Do not average component levels or promote a system solely because its parts are mature.
7. List the few missing demonstrations that could change the decision, with success/failure criteria, authority, resources and a safe next step. Keep manufacturing, economics, regulation and integration gaps in separate columns.
8. Record reviewer, assessment date and revision trigger. A changed configuration or intended use can require reassessment.

## Output and validation

Another reader can connect the judgment to the chosen criteria and specific evidence. A claim that cannot be traced is marked unassessed. Check whether the conclusion survives removal of promotional assertions and whether the next test addresses the largest material gap.

## Example and limits

A bench thermal prototype does not establish field performance under contamination and duty cycling. A bounded pilot might address those gaps; it does not retroactively validate untested conditions. This procedure is an assessment aid, not official certification, legal advice or permission for hazardous trials.

## Optional tools and deeper knowledge

Use a criterion-evidence table; software is optional. [NASA TRL overview](../references/nasa-2023-technology-readiness-levels.md), [readiness model](../models/readiness-evidence-model.md), and [transfer assessment](assess-transfer-to-a-new-context.md) support the reasoning. The procedure itself is our domain-independent adaptation.
