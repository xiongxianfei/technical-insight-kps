---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:hypothesis-driven-analysis"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:bain-undated-case-interview-preparation", "ti:r:nasa-undated-decision-analysis"]
method_origin: "established"
technique_kind: "analytical technique"
---

# Hypothesis driven analysis

## Key takeaway

Organize a decision into testable questions and prioritize evidence that could change the conclusion.

## Summary

Organize a decision into testable questions and prioritize evidence that could change the conclusion. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Hypothesis driven analysis. **Role:** analytical technique. The named technique is reused from [Case Interview Preparation](../references/bain-undated-case-interview-preparation.md); [Source record](../references/nasa-undated-decision-analysis.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

A decision question, boundary, available facts and time or resource constraint. The technique is a reasoning family, not a certification or a proprietary Bain algorithm.

## Rationale

An issue decomposition reduces ambiguity, while explicit rival hypotheses prevent the first attractive answer from quietly becoming the objective.

## Procedure

1. State the decision and a neutral question tree. Use distinguishable branches; note overlaps and interactions rather than forcing false independence.
2. For each consequential branch state a working hypothesis, a rival and a possible observation-process artifact.
3. Specify a prediction and a contrary signal for each. A question tree organizes reasoning; it is not evidence.
4. Prioritize by consequence, uncertainty, discriminating value, cost and safety. Explain the priority instead of inventing precise probabilities.
5. Gather the relevant evidence, revise or reject hypotheses and stop branches that no longer affect the decision.

## Worked example

**Synthetic example, not a measured investigation.** A low-power detector could reduce transmissions, increase computation, or merely use a different test set. Separate communication, computation and detection claims, then compare candidate predictions on the same traces. The highest-impact unknown is not necessarily the easiest fact to collect.

## Working template

| Question | Working hypothesis | Rival | Distinguishing evidence | Decision impact | Next check |
|---|---|---|---|---|---|
| Bounded uncertainty | Testable statement | Alternative explanation | Prediction and counter-signal | Why resolving it matters | Authorized action |

## Output and validation

Deliver an evidence queue and updated hypothesis table. Reject priorities that cannot change the decision or require unsafe interventions.

## Limits and optional tools

Bain public case-interview guidance supports structured reasoning, not this exact engineering worksheet. MECE is a decomposition aspiration; interacting mechanisms need explicit cross-links. Do not call the selected hypothesis proven merely because other branches were not investigated.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[Case Interview Preparation](../references/bain-undated-case-interview-preparation.md); [Source record](../references/nasa-undated-decision-analysis.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
