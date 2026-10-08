---
id: "ti:me:build-a-conditional-technology-roadmap"
type: "method"
version: "1.1.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-08"
basis_kind: "IfM and Futures Toolkit inspired planning adaptation"
uses_models: ["ti:mo:readiness-evidence-model", "ti:mo:decision-and-transfer-model"]
references: ["ti:r:ifm-engage-undated-technology-roadmapping", "ti:r:government-office-for-science-2024-futures-toolkit"]
---

# Build a conditional technology roadmap

## Key takeaway

Link needs, capabilities, technologies and demonstrations through dependencies and decision gates rather than presenting dates as predictions.

## Summary

A roadmap connects a possible future outcome to the technical work and evidence needed to pursue it. This compact adaptation uses the IfM needs/capabilities/technology linkage and the Futures Toolkit roadmap and scenario reasoning. It supports an individual or small team without requiring formal workshop software.

## Inputs and prerequisites

A scoped objective, baseline, candidate technologies, readiness gaps, resource constraints, decision owners and planning horizon. Separate committed activity from proposed or speculative work. Use discipline-specific governance for safety-critical milestones.

## Rationale

A technology can depend on an enabling capability that has not been demonstrated. A date-only plan can hide that dependency. Contrasting future conditions reveals which actions remain useful, which should wait and what evidence could change the route. A scenario is not a probability forecast unless a separate defensible model provides probabilities.

## Procedure

1. Describe the target need and a few bounded outcomes over near, middle and longer horizons. Prefer event-based gates where dates are uncertain.
2. Create four linked layers: needs/drivers; required capabilities; candidate technologies; enabling resources and demonstrations. State why each link exists.
3. For each proposed milestone, specify configuration, relevant conditions, measurement, acceptable and contrary results, owner and dependency. Mark planned, executed or assessed status accurately.
4. Identify the critical dependencies and options. Separate a prerequisite from a convenient sequence. Add a fallback when an enabling demonstration fails or a source disappears.
5. Construct at least two genuinely contrasting plausible contexts where useful, such as plentiful versus restricted power or stable versus changing requirements. Do not assign invented probabilities or call them predictions.
6. Test the proposed route under those contexts. Identify robust actions, contingent bets and assumptions that dominate the decision. Prefer a reversible information-gathering step where uncertainty would materially change commitment.
7. Attach resource estimates as ranges with their basis. Record unresolved assumptions, update triggers and review ownership. Keep cost, capability and maturity distinct.
8. Publish the qualified roadmap with the next decision and evidence gap. Revise after meaningful new evidence; do not silently move dates to conceal failed assumptions.

## Example and output

An illustrative cooling roadmap links a temperature need to sustained heat rejection, a candidate architecture, and a representative-load demonstration. If a power budget may shrink, the roadmap includes a passive alternative and an early comparison gate. No execution or market forecast is asserted.

The output can be a Markdown table: need | capability | candidate | dependency | demonstration | decision rule | horizon | owner | status. It is usable without an image or specialized tool.

## Validation and counterevidence

Every committed step has a reason, owner and testable gate; speculative steps are labeled. Walk backward from the outcome to the missing evidence and forward from a failed gate to a feasible response. A roadmap that succeeds in every scenario only because assumptions change has not been stress-tested.

## Limits and deeper knowledge

[IfM T-Plan description](../references/ifm-engage-undated-technology-roadmapping.md) links market/product/technology perspectives. [Futures Toolkit](../references/government-office-for-science-2024-futures-toolkit.md) treats scenarios and roadmaps as foresight aids. The lightweight procedure above is not full T-Plan, a validated forecasting model or a guarantee of adoption. [Readiness assessment](assess-technology-readiness.md) and [opportunity evaluation](evaluate-a-research-opportunity.md) supply supporting decisions. Spreadsheet or diagram tools are optional.
