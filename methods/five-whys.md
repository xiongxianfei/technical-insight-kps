---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:five-whys"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:asq-undated-five-whys", "ti:r:pearl-2009-causal-inference-in-statistics"]
method_origin: "established"
technique_kind: "analytical technique"
---

# Five Whys

## Key takeaway

Develop candidate causal chains by repeatedly questioning the explanation of an observed problem.

## Summary

Develop candidate causal chains by repeatedly questioning the explanation of an observed problem. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Five Whys. **Role:** analytical technique. The named technique is reused from [Five Whys and Five Hows](../references/asq-undated-five-whys.md); [Source record](../references/pearl-2009-causal-inference-in-statistics.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

A factual problem statement and people or records familiar with the process. Use after clarifying the event, not to invent facts about an unexplained report.

## Rationale

Symptoms and intermediate conditions can be mistaken for the underlying issue. Asking what accounts for each link exposes both candidate mechanisms and unsupported leaps.

## Procedure

1. Write one observable problem, with context and a comparison to expected behavior.
2. Ask why it happened and write an answer as a candidate explanation with a source or an explicit unknown.
3. Ask why that condition existed. Branch where multiple interacting explanations are plausible.
4. Stop when evidence or authority runs out; fewer or more than five questions may be appropriate.
5. Convert consequential links into tests or evidence requests. Separate an immediate containment action from a supported causal conclusion.

## Worked example

**Synthetic example, not a measured investigation.** Manifest fails -> path sets differ -> one includes checkout metadata -> generator and verifier use different filters. Each arrow needs a file listing or code observation. An additional branch asks whether path normalization differs. The chain is not established merely by writing it.

## Working template

| Observed effect | Candidate because | Supporting observation | Rival or unknown | Check |
|---|---|---|---|---|
| Event in context | Mechanism statement | Locator | Alternative | Safe discriminating step |

## Output and validation

Deliver a branching explanation with evidence status for every important link. A verified fix may be useful without identifying the only cause.

## Limits and optional tools

Avoid blame labels such as carelessness. Repetition is not causal proof. Do not require a fifth answer when evidence stops at the third, or collapse several causes into one linear story.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[Five Whys and Five Hows](../references/asq-undated-five-whys.md); [Source record](../references/pearl-2009-causal-inference-in-statistics.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
