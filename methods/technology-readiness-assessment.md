---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:technology-readiness-assessment"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:nasa-2023-technology-readiness-levels"]
method_origin: "established"
technique_kind: "analytical technique"
uses_models: ["ti:mo:readiness-evidence-model"]
---

# Technology readiness assessment

## Key takeaway

Assess demonstrated technology maturity against a named framework and intended use.

## Summary

Assess demonstrated technology maturity against a named framework and intended use. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Technology readiness assessment. **Role:** analytical technique. The named technique is reused from [Technology Readiness Levels](../references/nasa-2023-technology-readiness-levels.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

A named technology/configuration, intended environment, chosen TRL framework and located demonstration evidence. Uninspected vendor labels remain claims.

## Rationale

Readiness labels compress evidence. Reopening the item, environment and demonstration behind a label exposes application and integration gaps.

## Procedure

1. Define the assessed item and application before discussing a numeric level.
2. Read the relevant level criteria from the chosen framework; distinguish laboratory, relevant-environment and operational demonstrations.
3. Map each criterion to inspected evidence, date, configuration and limits.
4. State the justified level or range only where criteria are met; record uncertainty and missing evidence instead of guessing.
5. Describe the next representative demonstration and its acceptance criteria. Keep adoption, cost, safety and manufacturing judgments separate.

## Worked example

**Synthetic example, not a measured investigation.** A signal detector evaluated on saved traces has not automatically demonstrated a field-deployed sensor. Component evidence is useful, but power, mounting and communication integration may remain untested. No TRL is assigned without an actual evidence review.

## Working template

| Framework and item | Criterion | Evidence and configuration | Environment | Met or unresolved | Missing demonstration |
|---|---|---|---|---|---|
| Named assessment | Located criterion | Inspected record | Represented context | Justified status | Proposed check |

## Output and validation

Deliver a criterion-level evidence account and contextual assessment. Confirm that the assessed subject has not silently changed from component to system.

## Limits and optional tools

Do not average component TRLs into a system rating. A higher level does not automatically mean preferable, safe, affordable or suitable in a new context. This is not NASA certification.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[Technology Readiness Levels](../references/nasa-2023-technology-readiness-levels.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
