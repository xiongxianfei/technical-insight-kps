---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:pareto-analysis"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:asq-undated-pareto"]
method_origin: "established"
technique_kind: "analytical technique"
---

# Pareto analysis

## Key takeaway

Locate the largest contributors to one defined aggregate measure.

## Summary

Locate the largest contributors to one defined aggregate measure. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Pareto analysis. **Role:** analytical technique. The named technique is reused from [Pareto Chart](../references/asq-undated-pareto.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

A bounded dataset, mutually interpretable categories, a consistent measure such as count or downtime, and the reporting interval.

## Rationale

A ranked category view can focus investigation, provided categories, exposure and the quantity being summed are comparable.

## Procedure

1. Define the measure and population. Separate event count, duration, cost and severity rather than adding different units.
2. Clean duplicate events and record unclassified cases. Check changes in exposure or reporting coverage.
3. Sum the chosen measure by category and order largest to smallest.
4. Compute each share and cumulative share; display ordered bars with a cumulative line or a table.
5. Investigate the leading actionable categories, while separately screening rare severe hazards.

## Worked example

**Synthetic example, not a measured investigation.** Synthetic downtime totals are network 40, sensor 25, firmware 20 and other 15 minutes. Cumulative shares are 40%, 65%, 85% and 100%. The top two contribute 65%, not an assumed 80%. They are contributors to recorded downtime, not automatically underlying causes.

## Working template

| Category | Measure and units | Share | Cumulative share | Coverage caveat |
|---|---|---|---|---|
| Defined event class | Comparable total | Fraction of total | Running fraction | Missing or unequal exposure |

## Output and validation

Deliver a checked ranked table. Recompute the total and ensure percentages sum to 100 within rounding. Reassess priorities when the chosen measure changes.

## Limits and optional tools

A frequent minor fault need not outrank a rare catastrophic hazard. The 80/20 phrase is not a required result. Classification and reporting bias can alter the ranking.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[Pareto Chart](../references/asq-undated-pareto.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
