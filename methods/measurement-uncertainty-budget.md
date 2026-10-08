---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:measurement-uncertainty-budget"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:nist-undated-measurement-uncertainty"]
method_origin: "established"
technique_kind: "analytical technique"
---

# Measurement uncertainty budget

## Key takeaway

Identify and combine the uncertainty contributions relevant to a reported measurement.

## Summary

Identify and combine the uncertainty contributions relevant to a reported measurement. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Measurement uncertainty budget. **Role:** analytical technique. The named technique is reused from [Source record](../references/nist-undated-measurement-uncertainty.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

A defined measurand, measurement model, input estimates, instruments and calibration information, repeat data where available and the reporting purpose.

## Rationale

A result includes the measurement chain. Repeat readings may miss calibration, resolution or environmental contributions, and correlated contributions cannot simply be treated as independent.

## Procedure

1. Define the quantity, units, conditions and measurement equation. List contributions such as repeatability, resolution, calibration and environment.
2. Evaluate each input uncertainty from data or other justified information, recording its distribution or bound assumptions.
3. Convert contributions to standard uncertainties and propagate through the model with sensitivity coefficients. Include covariance when dependence matters.
4. State combined and, where justified, expanded uncertainty, coverage factor and assumptions; do not infer coverage from a factor alone.
5. Review the dominant contributors and whether the uncertainty permits the intended decision.

## Worked example

**Synthetic example, not a measured investigation.** Two synthetic independent contributions of 0.3 and 0.4 units combine by root sum of squares to 0.5 units. Positive correlation would change that value. Doubling the number of display digits does not reduce the uncertainty.

## Working template

| Measurand or input | Estimate | Unit | Uncertainty source | Evaluation basis | Standard uncertainty | Sensitivity | Correlation |
|---|---|---|---|---|---|---|---|
| Defined quantity | Value | Unit | Identified contribution | Data or justified information | Value | Coefficient | Known or assessed |

## Output and validation

Deliver a measurement result and uncertainty budget whose units and assumptions are inspectable. Recompute a contribution and test whether alternative plausible correlation changes the decision.

## Limits and optional tools

Type A and Type B describe evaluation routes, not synonyms for random and systematic error. Linear propagation may be inadequate for strong nonlinearity; use a justified alternative or specialist analysis. A budget cannot correct an unidentified bias.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[Source record](../references/nist-undated-measurement-uncertainty.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
