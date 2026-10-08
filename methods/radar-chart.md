---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:radar-chart"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:matplotlib-undated-radar-chart", "ti:r:asq-undated-decision-matrix"]
method_origin: "established"
technique_kind: "visualization technique"
---

# Radar chart

## Key takeaway

Display a small set of comparable multiattribute profiles without interpreting polygon area as an overall score.

## Summary

Display a small set of comparable multiattribute profiles without interpreting polygon area as an overall score. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Radar chart. **Role:** visualization technique. The named technique is reused from [Radar chart example](../references/matplotlib-undated-radar-chart.md); [Decision Matrix](../references/asq-undated-decision-matrix.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

A raw-data table, common context, meaningful dimensions, explicit transformations and a missing-data policy. Use a table or dot plot when precise comparisons are the task.

## Rationale

Radial axes make profiles visible, but the apparent shape also depends on axis order and scale. Interpretation therefore belongs to the underlying values, not the silhouette.

## Procedure

1. Choose a small, interpretable set of dimensions; state units, uncertainty and source for each raw value.
2. Define fixed bounds shared by all alternatives. For benefit dimensions use (x-L)/(U-L); for cost dimensions use (U-x)/(U-L) only when linear preference is justified.
3. Retain raw data and explain out-of-range values; do not silently clip. Leave missing values missing rather than replacing them with zero.
4. Plot the same axes, range and direction for every candidate. Keep axis order fixed when comparing versions. Label each dimension and transformation.
5. Read dimension by dimension, then check conclusions against the raw table. Test a changed axis order to expose area-based stories.

## Worked example

**Synthetic example, not a measured investigation.** Synthetic energy use in mJ per event: A=20 and B=35 with bounds 10 to 50, lower desirable, gives 0.75 and 0.375. Accuracy: A=0.92 and B=0.96 with bounds 0.80 to 1.00 gives 0.60 and 0.80. Mass in grams: A=120 and B=100 with bounds 80 to 180, lower desirable, gives 0.60 and 0.80. A saves energy; B scores better on the other declared dimensions. No overall winner follows from area.

## Working template

| Dimension | Units | L | U | Desirable direction | Raw A | Raw B | Mapped A | Mapped B |
|---|---|---|---|---|---|---|---|---|
| Measured outcome | Declared unit | Fixed bound | Fixed bound | Higher / lower | Value or missing | Value or missing | Value | Value |

## Output and validation

Deliver raw and transformed tables alongside the chart. Verify one transformation by hand and check that missing and uncertainty information survives. Our geometry example shows why polygon area is not invariant to axis order.

## Limits and optional tools

This is visualization, not a causal test, maturity framework or multicriteria decision rule. Matplotlib documents construction, not superiority or perception benefits. No charting software is mandatory; an annotated table can be the complete output.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[Radar chart example](../references/matplotlib-undated-radar-chart.md); [Decision Matrix](../references/asq-undated-decision-matrix.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
