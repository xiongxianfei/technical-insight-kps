---
id: "ti:mo:investigation-and-intelligence-routing-model"
type: "model"
version: "1.1.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-08"
basis_kind: "authored decision routing model"
uses_concepts: ["ti:c:technology-intelligence"]
uses_models: ["ti:mo:hypothesis-prediction-matrix", "ti:mo:decision-and-transfer-model"]
---

# Investigation and intelligence routing model

## Key takeaway

Choose the next operation from the uncertainty blocking a decision rather than from a preferred framework.

## Summary

This model connects a question, its evidence gap, the operation that could reduce that gap and the resulting decision. It distinguishes discovery, explanation, comparison, demonstration and adoption. Moving between them is expected; the diagram is not a compulsory pipeline.

## Representation

| Uncertainty | Operation | Output that can change the next decision |
|---|---|---|
| The objective is vague | Bound outcome, comparator and constraints | A question whose possible answers matter |
| Relevant approaches are unknown | Scan and map available evidence | A qualified candidate set with omissions |
| A reported result lacks an explanation | Generate alternatives and discriminating predictions | A testable mechanism question |
| A claimed capability is not demonstrated here | Audit configuration, environment and measurement | A demonstration gap, not a guessed readiness score |
| Several candidates remain plausible | Compare criteria and uncertainty | A reversible next action or a reason to defer |
| The preferred direction may fail in another future | Stress-test assumptions and dependencies | Conditional milestones and review triggers |

The central record is: **question -> uncertainty -> operation -> evidence -> qualified conclusion -> next decision**. A new observation can send the work back to framing. A promising technology may require an experiment; a failed experiment may require a broader search.

## Reading the model

An opportunity brief organizes a proposed research direction; it does not validate the technology. A causal diagram represents assumed relationships; it is not observed causation. A readiness label summarizes a particular demonstration basis, not commercial desirability. The object of evaluation and the meaning of the evidence must remain explicit.

## Example and counterexample

For an overheating device, comparing publication counts does not distinguish heat storage from heat rejection. A scoped landscape is useful for finding candidate mechanisms, but a time-dependent temperature observation is needed for that mechanism question. Conversely, running experiments on only the familiar candidate does not show that the landscape is complete.

## Assumptions and limits

The model assumes an identifiable decision and some access to appropriate evidence. Restricted data, unsafe tests or unknown requirements may justify a stop or referral. The routes are authored design choices, not a validated optimal investigation algorithm.

## Deeper knowledge

[Technology intelligence](../concepts/technology-intelligence.md), [hypothesis prediction matrix](hypothesis-prediction-matrix.md), [decision and transfer model](decision-and-transfer-model.md), and [method map](../METHOD-MAP.md).
