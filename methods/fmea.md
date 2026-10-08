---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:fmea"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:asq-undated-fmea"]
method_origin: "established"
technique_kind: "analytical technique"
---

# Failure mode and effects analysis

## Key takeaway

Anticipate how an item or process can fail and connect consequences to prevention and detection actions.

## Summary

Anticipate how an item or process can fail and connect consequences to prevention and detection actions. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Failure mode and effects analysis. **Role:** analytical technique. The named technique is reused from [Failure Mode and Effects Analysis](../references/asq-undated-fmea.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

Defined functions and boundary, multidisciplinary expertise, current controls, and the applicable project rating convention. Safety-critical work needs its required specialist review.

## Rationale

Examining failure modes before choosing a design exposes consequences that an average performance comparison can miss.

## Procedure

1. Define each function and how failure to perform it would appear.
2. Record the failure mode, local and downstream effects, possible causes and existing preventive or detecting controls.
3. Assess severity, occurrence and detection using declared definitions and evidence; retain unknowns. Use the required sector method where applicable.
4. Prioritize actions, assigning owner, due condition and an observable effectiveness check. Do not let a composite number override severe consequences.
5. Reassess residual risk only after the action has been implemented and evidence inspected.

## Worked example

**Synthetic example, not a measured investigation.** A monitor can miss an event, falsely alarm or transmit stale data. A missing event may be severe even if occurrence is uncertain. Proposed mitigation is a logged replay test and a detection-health indicator; no residual score is lowered until those controls are tested.

## Working template

| Function | Failure mode | Effect | Cause | Current control | Rating basis | Action and owner | Evidence after action |
|---|---|---|---|---|---|---|---|
| Required behavior | Failure form | Consequence | Candidate | Existing control | Defined scale and uncertainty | Proposed mitigation | Not executed |

## Output and validation

Deliver a reviewable risk-action table, not just a risk number. Check whether controls address the stated cause or merely make the symptom less visible.

## Limits and optional tools

Public ASQ guidance is not a sector-specific compliance standard. Ordinal rating products are not physical risk ratios. Interactions and common causes may require additional analysis; this introductory FMEA does not authorize hazardous testing.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[Failure Mode and Effects Analysis](../references/asq-undated-fmea.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
