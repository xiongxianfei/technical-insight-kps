---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:sensitivity-analysis"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:nasa-undated-decision-analysis", "ti:r:nasa-7009b-2024-models-and-simulations"]
method_origin: "established"
technique_kind: "analytical technique"
---

# Sensitivity analysis

## Key takeaway

Determine which uncertain inputs or preferences can change a model result or decision.

## Summary

Determine which uncertain inputs or preferences can change a model result or decision. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Sensitivity analysis. **Role:** analytical technique. The named technique is reused from [Source record](../references/nasa-undated-decision-analysis.md); [Source record](../references/nasa-7009b-2024-models-and-simulations.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

An explicit model or decision rule, baseline inputs, plausible ranges, dependencies and the outcome that matters.

## Rationale

A result can look precise while depending strongly on a poorly known parameter. Exploring variations separates robust conclusions from choices that require more evidence.

## Procedure

1. Name the output and decision boundary, keeping parameter uncertainty separate from preference uncertainty.
2. Choose physically and contextually plausible ranges; preserve known correlations and constraints.
3. Vary inputs individually for initial screening and jointly when interactions or dependencies could matter. Record the sampling strategy.
4. Identify outcome ranges, threshold crossings and changes in preferred alternatives. Do not assign probabilities unless the input distributions are justified.
5. Prioritize measurement or redesign around consequential uncertain influences and report the tested envelope.

## Worked example

**Synthetic example, not a measured investigation.** A synthetic thermal estimate uses rise = heat rate / conductance. With 10 W and conductance from 0.5 to 1 W/K, the steady rise ranges from 20 to 10 K. Heat capacity affects transient response but not this assumed steady-state equation. Whether the actual device follows the equation remains a separate validation task.

## Working template

| Input or weight | Baseline | Plausible range | Dependence | Output effect | Decision reversal |
|---|---|---|---|---|---|
| Named parameter | Value | Justified bounds | Constraint or correlation | Computed range | Threshold |

## Output and validation

Deliver a sensitivity result tied to the model and assumptions. Check limiting cases and whether missed interactions could reverse the conclusion.

## Limits and optional tools

One-at-a-time analysis does not expose every interaction. A sensitivity analysis does not validate its underlying model or establish a forecast distribution. This file is an introductory use of the established analysis family, not a new optimization algorithm.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[Source record](../references/nasa-undated-decision-analysis.md); [Source record](../references/nasa-7009b-2024-models-and-simulations.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
