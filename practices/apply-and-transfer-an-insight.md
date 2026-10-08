---
id: "ti:pr:apply-and-transfer-an-insight"
type: "practice"
version: "2.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-08"
basis_kind: "authored Practice integrating established techniques; not an independently validated programme"
confidence: "provisional for application"
stage_titles: ["Stage1 Define target use and source scope", "Stage2 Map preserved changed and unknown assumptions", "Stage3 Select an authorized implementation", "Stage4 Evaluate target behavior and adverse outcomes", "Stage5 Adopt with revision triggers"]
practice_format: "staged-inline-local-v1"
uses_methods: ["ti:me:5w2h", "ti:me:sipoc", "ti:me:technology-readiness-assessment", "ti:me:sensitivity-analysis", "ti:me:fmea", "ti:me:pugh-matrix", "ti:me:design-of-experiments"]
uses_models: ["ti:mo:decision-and-transfer-model"]
references: ["ti:r:ahrq-undated-5w2h", "ti:r:asq-undated-decision-matrix", "ti:r:asq-undated-fmea", "ti:r:asq-undated-sipoc", "ti:r:nasa-2023-technology-readiness-levels", "ti:r:nasa-7009b-2024-models-and-simulations", "ti:r:nasa-undated-decision-analysis", "ti:r:nist-undated-experimental-design-handbook", "ti:r:pearl-2009-causal-inference-in-statistics"]
---

# Apply and transfer an insight

## Key takeaway

Use an insight through a bounded decision and a target-context check rather than copying its original prescription.

## Summary

This Practice connects understanding to a safe design or process change. It retains alternative solutions, tests applicability and monitors consequences. Successful adoption does not automatically prove the complete mechanism.


## Established techniques used

[5W2H](../methods/5w2h.md), [SIPOC](../methods/sipoc.md), [Technology readiness assessment](../methods/technology-readiness-assessment.md), [Sensitivity analysis](../methods/sensitivity-analysis.md), [Failure mode and effects analysis](../methods/fmea.md), [Pugh matrix](../methods/pugh-matrix.md), [Design of experiments](../methods/design-of-experiments.md). These supply repeatable techniques; the stage order, handoffs and decisions below are our authored Practice, not an official combined method.


## Goal and prerequisites

Bring a source insight with evidence and scope, a target purpose and a decision owner. Required project, safety, privacy and operating controls remain authoritative.

Stage numbers show recommended reading and learning order. Actual prerequisites, safety conditions and authorization govern entry. Revisit any stage when evidence requires it; this is not a one-way proof pipeline.

## Stage map

1. [Stage1 Define target use and source scope](#stage1-define-target-use-and-source-scope)
2. [Stage2 Map preserved changed and unknown assumptions](#stage2-map-preserved-changed-and-unknown-assumptions)
3. [Stage3 Select an authorized implementation](#stage3-select-an-authorized-implementation)
4. [Stage4 Evaluate target behavior and adverse outcomes](#stage4-evaluate-target-behavior-and-adverse-outcomes)
5. [Stage5 Adopt with revision triggers](#stage5-adopt-with-revision-triggers)

## Stage1 Define target use and source scope

**Goal:** Identify what should transfer and what is being asked of it.

**Why:** An insight can be valid in its source conditions yet irrelevant to a new use.

**What to do:** Record the source explanation and the target goal separately.

**What to observe:** Different duty cycles, scale, interfaces, people and consequence of error.

**Success signal:** Both source and target conditions are explicit.

**Next:** Map assumptions.

**Understanding:** Transfer concerns relationships, not merely similar labels. A manifest policy illustrates separation of payload from tool state; its exact excluded names are implementation choices. A thermal time constant is not a universal material property.

**Procedure**

1. Write the source claim with evidence status and limitations.
2. State the target decision and outcome with units or events.
3. Identify hard constraints, authority and required expertise.
4. List the differences most likely to change the predicted result.

**Fallback and stopping:** If the original scope is unavailable, mark the source incomplete and avoid asserting ready transfer.

**5W2H and SIPOC application.** Specify the target user, process boundary, outcome, duty cycle and constraints. Identify inputs and outputs that differ from the original application. Keep the source result and the intended target benefit in separate columns.

## Stage2 Map preserved changed and unknown assumptions

**Goal:** Identify the applicability gaps that matter.

**Why:** A reused confidence label can conceal a new mechanism or operating regime.

**What to do:** Compare assumptions and model validity envelopes.

**What to observe:** Which changes affect the relationship versus only its implementation.

**Success signal:** Each material gap has a justification, check or prohibition.

**Next:** Compare possible implementations.

**Understanding:** A dimension may be unchanged in name but changed in behavior: same interface with new timing, same material with new geometry, same dataset with different selection. Include measurement and user context.

**Procedure**

1. Create a source-target table of mechanism, configuration, environment, timescale, interfaces and measurement.
2. Mark assumptions preserved, changed or unknown and state evidence for each classification.
3. Derive expected target consequences without importing exact source thresholds blindly.
4. Prioritize gaps by effect on the intended decision and harm potential.

**Fallback and stopping:** Do not use surface analogy as validation. A critical unknown may require expert review rather than a small pilot.

**Readiness and sensitivity application.** Compare configuration, interfaces, environmental conditions, scale, measurement and required outcome. Mark assumptions preserved, changed or unknown. Inspect whether plausible differences change model predictions or the proposed decision; do not transfer a numeric TRL without its evidence context.

## Stage3 Select an authorized implementation

**Goal:** Choose among ways of using the insight.

**Why:** Evidence about a relationship does not prescribe one unique design.

**What to do:** Compare alternatives against goals, constraints and uncertainty.

**What to observe:** Benefits, adverse effects, reversibility and monitoring ability.

**Success signal:** A decision owner approves a bounded option or a reason to defer.

**Next:** Plan and run the permitted assessment.

**Understanding:** A general explanatory relationship can support several Methods. Prefer a design whose necessary assumptions are supported and whose consequences can be observed; do not equate simplicity with guaranteed safety.

**Procedure**

1. List no change, a simpler approach and the proposed approach when credible.
2. Separate mandatory constraints from preference criteria.
3. Compare expected consequences and sensitivity to uncertain premises.
4. Record selection, authority, scope, stop criteria and rollback plan.

**Fallback and stopping:** Do not authorize deployment merely because a knowledge file says active or a structural validator passes.

**FMEA and Pugh application.** Screen unacceptable failure consequences before preference comparison. Include no change and a simpler alternative. A Pugh table compares each candidate to a datum with evidence or unknown cells. The selected implementation is a decision under constraints, not a newly discovered universal Principle.

## Stage4 Evaluate target behavior and adverse outcomes

**Goal:** Determine whether the chosen implementation meets the target need.

**Why:** A successful local metric can hide harm or loss of the original task.

**What to do:** Execute only the approved pilot or assessment and compare predicted consequences.

**What to observe:** Fidelity, expected benefit, side effects, changed context and residual uncertainty.

**Success signal:** The actual target evidence supports a bounded adoption decision or rejection.

**Next:** Adopt monitor or revise.

**Understanding:** A pilot has its own applicability limits. It may establish useful performance without identifying the mechanism, and it may miss rare events. Evidence depth should match consequence rather than a fixed repetition count.

**Procedure**

1. Confirm safe setup and measurement before execution.
2. Record configuration, observations, deviations and whether the intervention occurred.
3. Compare benefit, harms and competing explanations using the planned analysis.
4. State which source assumptions survived and which did not.

**Fallback and stopping:** Stop on safeguard violations. If the pilot is too narrow for the consequence, keep the deployment decision deferred.

**DOE application.** Plan a representative authorized pilot or surrogate with comparator, meaningful outcomes, independent units, measurement uncertainty and stop conditions. Keep actual implementation and observed effects separate. Check adverse outcomes as well as the hoped-for benefit; a laboratory success is not an automatic operational success.

## Stage5 Adopt with revision triggers

**Goal:** Keep implementation status separate from knowledge certainty.

**Why:** Changing conditions can invalidate a previously justified application.

**What to do:** Record the decision, operating envelope and monitoring/review responsibility.

**What to observe:** Signals that the assumptions or outcomes no longer hold.

**Success signal:** Owners know what is adopted, why, and when to stop or reconsider.

**Next:** Feed actual results into knowledge review.

**Understanding:** An adopted Method can remain provisional. Monitoring is not a promise of zero harm; it is a bounded detection and response plan. Preserve the prior evidence so later interpretation changes do not rewrite history.

**Procedure**

1. Record accept, reject or defer with scope and authority.
2. Specify relevant monitoring variables, escalation/stop conditions and responsible roles.
3. Write the target-specific insight and retain source conditions separately.
4. Update related Principles, Models or Methods only where the target evidence supports generalization.

**Fallback and stopping:** Do not promote a single successful target run to a universal law. A changed operating regime triggers a new applicability review.

**Working Practice update.** Record what was adopted, under which conditions, by whose authority and with what monitoring. Keep an exit or rollback condition appropriate to the use. A positive local outcome is personal or project evidence until broader support is established; do not publish confidential context while generalizing it.

## Troubleshooting

If the question keeps changing, return to its purpose and decision boundary. If rivals predict the same outcome, redesign the discriminating check or leave the mechanism unresolved. If the intervention was not executed as planned, assess execution rather than claiming the explanation failed. If a test introduces unacceptable risk, stop; use analysis, a surrogate or qualified review instead. If every result supports the favourite story, state a contrary prediction before proceeding.

## Current working summary

No real investigation results are supplied in this publication. Fill this section only from an actual permitted application, or copy the blank template into a private record.

| Item | Current record |
|---|---|
| Question and decision | Not recorded |
| Leading and rival explanations | Not recorded |
| Evidence and limitations | Not recorded |
| Model and applicability | Not recorded |
| Test and execution status | Not recorded |
| Decision and authority | Not recorded |
| Next check and review trigger | Not recorded |

## Evidence and limits

[NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md) [NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md) [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md) informs the underlying distinctions. The stage selection, operational synthesis and examples are authored here. This Practice is not independently validated, a professional certification or authorization for hazardous experiments. It does not guarantee original discovery, causality or successful application.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Assess transfer to a new context in the Practice](../practices/apply-and-transfer-an-insight.md#stage2-map-preserved-changed-and-unknown-assumptions)
- [Compare technical alternatives in the Practice](../practices/investigate-a-technical-opportunity.md#stage5-recommend-a-bounded-next-action)
- [Execute a bounded test in the Practice](../practices/discover-and-validate-a-technical-insight.md#stage6-execute-and-preserve-what-happened)
- [Evaluate results and uncertainty in the Practice](../practices/discover-and-validate-a-technical-insight.md#stage7-evaluate-the-explanation-and-its-limits)
- [Decision and transfer model](../models/decision-and-transfer-model.md)

- [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md)
- [NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md)
- [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md)

[Package home](../README.md)
