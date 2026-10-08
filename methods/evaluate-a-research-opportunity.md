---
id: "ti:me:evaluate-a-research-opportunity"
type: "method"
version: "1.1.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-08"
basis_kind: "Heilmeier-inspired authored opportunity assessment"
uses_models: ["ti:mo:decision-and-transfer-model", "ti:mo:readiness-evidence-model"]
references: ["ti:r:darpa-undated-heilmeier-catechism", "ti:r:nasa-undated-decision-analysis"]
---

# Evaluate a research opportunity

## Key takeaway

Use a Heilmeier-inspired brief to expose the feasibility and value assumptions behind a research proposal.

## Summary

This Method turns an attractive idea into a reviewable opportunity with baseline, novelty, beneficiaries, risks, resources and observable milestones. It helps decide what to investigate or fund next. A coherent brief remains a proposal until its technical claims receive evidence.

## Inputs and prerequisites

A need, candidate mechanism, baseline alternatives, relevant evidence and a decision owner. Identify safety, confidentiality and authority constraints. Treat unavailable cost, duration or performance information as uncertain, not zero.

## Rationale

A technology can be new but irrelevant, useful but infeasible, or feasible but inappropriate for adoption. The DARPA questions make several of these distinctions visible. Adding located evidence and rejection conditions makes the resulting proposal assessable rather than merely persuasive.

## Procedure

1. Write eight short sections: plain-language aim; current approach and limits; what differs and why plausible; beneficiary and material difference; risks; resource needs; duration; intermediate and final demonstrations. Avoid jargon that hides the outcome.
2. For every consequential assertion, mark observed evidence, external claim, calculation, assumption or unknown. Link to the exact contribution; novelty is not established by not having seen an idea before.
3. Compare the proposal with the current baseline, a credible alternative and deferral. Separate a mechanism advantage from integration effort and lifecycle cost.
4. Identify a critical premise whose failure would change the recommendation. State its plausible rival and a safe check, not only a demonstration designed to look successful.
5. Define one intermediate milestone: configuration, conditions, measurement, acceptance boundary, failure boundary, resource cap and decision owner. A milestone is an evidence-producing event, not a date or presentation.
6. Evaluate plausible unfavorable conditions, including weaker performance, unavailable components or higher integration cost. Do not average away a mandatory constraint.
7. Recommend investigate, bounded pilot, revise, monitor, defer or reject, with explicit assumptions and revisit triggers. Do not mark unexecuted milestones as passed.

## Example

For an illustrative cooling opportunity, the aim is to limit temperature under a specified duty cycle and mass cap. Novelty might concern the heat-transfer path; evidence about early temperature alone leaves sustained operation unresolved. A useful next milestone compares both transient and sustained behavior under a representative load. These are planned checks, not measured results.

## Expected effect and validation

A reviewer can identify the intended benefit, evidence gaps and the event that would alter the recommendation. Ask whether a negative milestone result could actually stop or redirect the work. If not, the gate is ceremonial. A strong narrative with inaccessible evidence remains a provisional proposal.

## Optional tools

A one-page Markdown brief and evidence table are sufficient. AI can challenge wording or missing assumptions, but cannot supply measured feasibility, estimates or source authority by assertion.

## Limits and deeper knowledge

[DARPA's Catechism](../references/darpa-undated-heilmeier-catechism.md) supplies the questions, not the full procedure above. [NASA decision analysis](../references/nasa-undated-decision-analysis.md) supports objectives, alternatives and uncertainty. [Assess readiness](assess-technology-readiness.md) and [design a discriminating test](design-a-discriminating-test.md) supply separate technical checks. This adaptation neither claims endorsement nor replaces funding, regulatory or professional approval.
