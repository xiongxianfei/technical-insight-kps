---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:weighted-decision-matrix"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:asq-undated-decision-matrix", "ti:r:nasa-undated-decision-analysis"]
method_origin: "established"
technique_kind: "analytical technique"
---

# Weighted decision matrix

## Key takeaway

Make preference tradeoffs explicit while keeping technical evidence and uncertainty separate.

## Summary

Make preference tradeoffs explicit while keeping technical evidence and uncertainty separate. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Weighted decision matrix. **Role:** analytical technique. The named technique is reused from [Decision Matrix](../references/asq-undated-decision-matrix.md); [Source record](../references/nasa-undated-decision-analysis.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

Feasible alternatives, defined criterion scales, stakeholder preferences and evidence for ratings. Do not aggregate incomparable units directly.

## Rationale

A decision mixes consequences and values. Separating scores, weights and hard constraints exposes why the preferred alternative can change.

## Procedure

1. Screen mandatory constraints and record exclusions before scoring.
2. Define criterion-specific scales with a consistent desirable direction; preserve raw measurements beside ratings.
3. Assign and justify weights. Check duplicated criteria and dependencies before using an additive sum.
4. Calculate the declared sum and vary uncertain scores and weights. Record plausible preference reversals.
5. Choose, defer or reject with authority and rationale; the calculation is a discussion aid, not a command.

## Worked example

**Synthetic example, not a measured investigation.** For synthetic comparable scores, A=(0.8,0.4) and B=(0.5,0.8). Weights (0.6,0.4) give A=0.64 and B=0.62. Weights (0.4,0.6) give A=0.56 and B=0.68. The reversal reveals a preference dependency, not a calculation defect.

## Working template

| Criterion | Raw evidence | Rating rule | Weight | A rating | B rating | Uncertainty |
|---|---|---|---|---|---|---|
| Relevant outcome | Units and source | Fixed rule | Justified preference | Value | Value | Range or unknown |

## Output and validation

Deliver scores plus sensitivity and constraint status. Independently recompute a row and the totals. Use an unresolved decision if the evidence does not separate alternatives.

## Limits and optional tools

Weights are not empirical probabilities. A scalar result can hide noncompensable harms. Additive scoring is inappropriate when its tradeoff assumptions are unacceptable.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[Decision Matrix](../references/asq-undated-decision-matrix.md); [Source record](../references/nasa-undated-decision-analysis.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
