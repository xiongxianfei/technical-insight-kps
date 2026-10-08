---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:design-of-experiments"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:nist-undated-experimental-design-handbook"]
method_origin: "established"
technique_kind: "experimental design family"
---

# Design of experiments

## Key takeaway

Plan controlled comparisons that can estimate effects and interactions at an appropriate experimental unit.

## Summary

Plan controlled comparisons that can estimate effects and interactions at an appropriate experimental unit. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Design of experiments. **Role:** experimental design family. The named technique is reused from [Source record](../references/nist-undated-experimental-design-handbook.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

A testable question, outcome and units, candidate factors and levels, experimental units, measurement capability, feasible sample-size reasoning and explicit authorization. Specialist design is required when risk or complexity warrants it.

## Rationale

Changing inputs systematically can distinguish effects that an uncontrolled comparison confounds. Randomization, replication and blocking address different sources of uncertainty.

## Procedure

1. State the response, practically important effect, candidate factors and safe levels before observing outcomes.
2. Identify the experimental unit. Repeated readings from one unit are not automatically independent replicates.
3. Choose a design matching the question. A factorial design can examine interactions; blocking groups known nuisance conditions; randomization addresses allocation/order bias.
4. Plan replication, measurement uncertainty, analysis and stop criteria. Keep exploratory and confirmatory work distinct.
5. Record the run order, actual factor settings and deviations. Analyze the planned contrasts and inspect residuals and applicability before generalizing.

## Worked example

**Synthetic example, not a measured investigation.** A synthetic 2 by 2 response table is (low A,low B)=10; (high A,low B)=14; (low A,high B)=15; (high A,high B)=13. Raising A changes the response by +4 at low B and -2 at high B. The difference of effects is -6. With one observation per cell, these numbers illustrate interaction but do not estimate repeatability or significance.

## Working template

| Run | Randomized order | Block | Independent unit | Factor levels | Actual response | Deviation |
|---|---|---|---|---|---|---|
| Planned ID | Recorded order | Nuisance group | Defined unit | Intended and actual | Value and units | Reason |

## Output and validation

Deliver a design and traceable results, effect estimates and uncertainty appropriate to the sampling. A failed manipulation is an execution finding, not evidence against the intended mechanism.

## Limits and optional tools

A simple A/B comparison cannot identify every interaction or mechanism. A simulator tests its model, not automatically the real system. Do not obtain causal certainty from uncontrolled assignment, pseudo-replication or a convenient fixed sample count.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[Source record](../references/nist-undated-experimental-design-handbook.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
