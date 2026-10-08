---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:pugh-matrix"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:asq-undated-decision-matrix", "ti:r:nasa-undated-decision-analysis"]
method_origin: "established"
technique_kind: "analytical technique"
---

# Pugh matrix

## Key takeaway

Compare candidate concepts against a named datum using criterion-specific relative judgments.

## Summary

Compare candidate concepts against a named datum using criterion-specific relative judgments. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Pugh matrix. **Role:** analytical technique. The named technique is reused from [Decision Matrix](../references/asq-undated-decision-matrix.md); [Source record](../references/nasa-undated-decision-analysis.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

Credible candidates, a datum, agreed criteria, hard constraints and evidence sufficient for each relative judgment.

## Rationale

A shared reference exposes strengths and weaknesses without pretending early concept estimates are precise absolute utilities.

## Procedure

1. Screen hard constraints separately, then name the datum and define each criterion direction.
2. For each candidate mark better, comparable, worse or unknown relative to that datum. Support the judgment with evidence or an explicit assumption.
3. Inspect the pattern of tradeoffs. Any counts or optional weights summarize judgments; they do not erase a violated requirement.
4. Try a credible alternate datum and inspect uncertain cells. Combine useful concept features only when they remain technically compatible.
5. Select a next investigation or concept with reasons and record what evidence could change the decision.

## Worked example

**Synthetic example, not a measured investigation.** Compared with an incumbent, candidate A is better in energy, comparable in accuracy and worse in integration effort; candidate B has unknown accuracy. A net plus count cannot make B acceptable without the missing performance evidence.

## Working template

| Criterion and direction | Datum | Candidate A | Candidate B | Evidence and uncertainty |
|---|---|---|---|---|
| Defined property | 0 | + / 0 / - / ? | + / 0 / - / ? | Located reason |

## Output and validation

Deliver a relative comparison and unresolved evidence needs. Explain any ranking instability and whether it changes the next action.

## Limits and optional tools

Pugh comparison is not the same as an absolute weighted utility matrix. Relative symbols do not encode equal physical differences. Unknown is not zero or comparable.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[Decision Matrix](../references/asq-undated-decision-matrix.md); [Source record](../references/nasa-undated-decision-analysis.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
