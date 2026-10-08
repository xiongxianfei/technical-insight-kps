---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:statistical-hypothesis-testing"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:nist-undated-hypothesis-tests", "ti:r:nist-undated-model-fit-and-residuals"]
method_origin: "established"
technique_kind: "statistical inference family"
---

# Statistical hypothesis testing

## Key takeaway

Evaluate a statistical contrast under explicit sampling and model assumptions.

## Summary

Evaluate a statistical contrast under explicit sampling and model assumptions. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Statistical hypothesis testing. **Role:** statistical inference family. The named technique is reused from [What are statistical tests](../references/nist-undated-hypothesis-tests.md); [Source record](../references/nist-undated-model-fit-and-residuals.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

A population or process, independent-unit definition, question, effect-size threshold, sampling design and assumptions for a selected test. Use qualified analysis for complex dependence or multiple outcomes.

## Rationale

Observed differences fluctuate. A defined statistic and reference distribution make one aspect of that uncertainty explicit, while engineering importance still needs a separate criterion.

## Procedure

1. Specify the null, alternative and direction of the contrast before testing. Define the practical effect threshold separately.
2. Select a test appropriate to the data and design, identifying distributional and independence assumptions.
3. Predefine an error-control plan, relevant comparisons and sample-size rationale. Do not keep looking until a convenient result appears.
4. Estimate the effect and uncertainty, compute the test result using a checked implementation, and inspect data quality and assumptions.
5. Report effect magnitude, uncertainty, test assumptions and all relevant comparisons; state what remains inconclusive.

## Worked example

**Synthetic example, not a measured investigation.** Suppose a synthetic analysis reports a difference of 2 units with an interval from -1 to 5. The estimate alone does not establish improvement. Failure to reject zero is not evidence of equivalence; equivalence needs a predeclared acceptable margin and a suitable design.

## Working template

| Population and unit | Null and alternative | Practical margin | Test and assumptions | Effect and interval | Error-control plan | Conclusion |
|---|---|---|---|---|---|---|
| Defined context | Stated contrast | Engineering threshold | Chosen before analysis | Estimate and uncertainty | Declared comparisons | Qualified |

## Output and validation

Deliver an auditable statistical result with effect size and applicability. Verify the implemented test on a known reference case and identify any post-hoc choices.

## Limits and optional tools

A p-value is not the probability that the null is true. Statistical significance does not establish causality, importance or safety. This overview does not select a test automatically or replace expert review.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[What are statistical tests](../references/nist-undated-hypothesis-tests.md); [Source record](../references/nist-undated-model-fit-and-residuals.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
