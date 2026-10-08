---
id: "ti:pr:investigate-a-technical-opportunity"
type: "practice"
version: "2.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-08"
basis_kind: "authored Practice integrating established techniques; not an independently validated programme"
confidence: "provisional for application"
stage_titles: ["Stage1 Define the useful change", "Stage2 Map mechanisms and competing approaches", "Stage3 Explain the proposed opportunity", "Stage4 Reduce the decisive uncertainty", "Stage5 Recommend a bounded next action"]
practice_format: "staged-inline-local-v1"
uses_methods: ["ti:me:5w2h", "ti:me:horizon-scanning", "ti:me:structured-literature-review", "ti:me:patent-landscaping", "ti:me:technology-readiness-assessment", "ti:me:triz-contradiction-analysis", "ti:me:morphological-analysis", "ti:me:heilmeier-catechism", "ti:me:design-of-experiments", "ti:me:pugh-matrix", "ti:me:weighted-decision-matrix", "ti:me:radar-chart", "ti:me:technology-roadmapping"]
uses_principles: ["ti:p:novelty-and-support-are-different-properties"]
uses_models: ["ti:mo:decision-and-transfer-model"]
references: ["ti:r:ahrq-undated-5w2h", "ti:r:asq-undated-decision-matrix", "ti:r:darpa-undated-heilmeier-catechism", "ti:r:epo-undated-patent-families", "ti:r:government-office-for-science-2024-futures-toolkit", "ti:r:ifm-engage-undated-technology-roadmapping", "ti:r:li-2019-collecting-data-cochrane", "ti:r:matplotlib-undated-radar-chart", "ti:r:matriz-undated-contradictions", "ti:r:nasa-2023-technology-readiness-levels", "ti:r:nasa-7009b-2024-models-and-simulations", "ti:r:nasa-undated-decision-analysis", "ti:r:nist-undated-experimental-design-handbook", "ti:r:oxford-creativity-undated-triz-glossary", "ti:r:ritchey-2013-general-morphological-analysis", "ti:r:w3c-2013-prov-overview", "ti:r:wipo-2015-patent-landscape-guidelines"]
---

# Investigate a technical opportunity

## Key takeaway

Discover useful possibilities by connecting a capability gap to mechanisms, alternatives and decisive evidence.

## Summary

This Practice begins with an opportunity rather than a failure. It builds a technical landscape, identifies a potentially useful distinction and selects the cheapest credible way to reduce decision-relevant uncertainty. New-to-project understanding is useful even when it is not new science.


## Established techniques used

[5W2H](../methods/5w2h.md), [Horizon scanning](../methods/horizon-scanning.md), [Structured literature review](../methods/structured-literature-review.md), [Patent landscaping](../methods/patent-landscaping.md), [Technology readiness assessment](../methods/technology-readiness-assessment.md), [TRIZ contradiction analysis](../methods/triz-contradiction-analysis.md), [Morphological analysis](../methods/morphological-analysis.md), [Heilmeier Catechism](../methods/heilmeier-catechism.md), [Design of experiments](../methods/design-of-experiments.md), [Pugh matrix](../methods/pugh-matrix.md), [Weighted decision matrix](../methods/weighted-decision-matrix.md), [Radar chart](../methods/radar-chart.md), [Technology roadmapping](../methods/technology-roadmapping.md). These supply repeatable techniques; the stage order, handoffs and decisions below are our authored Practice, not an official combined method.


## Goal and prerequisites

Bring an unmet capability or costly constraint and a decision owner. Initial work may be source review or simulation; no live-system changes are implied.

Stage numbers show recommended reading and learning order. Actual prerequisites, safety conditions and authorization govern entry. Revisit any stage when evidence requires it; this is not a one-way proof pipeline.

## Stage map

1. [Stage1 Define the useful change](#stage1-define-the-useful-change)
2. [Stage2 Map mechanisms and competing approaches](#stage2-map-mechanisms-and-competing-approaches)
3. [Stage3 Explain the proposed opportunity](#stage3-explain-the-proposed-opportunity)
4. [Stage4 Reduce the decisive uncertainty](#stage4-reduce-the-decisive-uncertainty)
5. [Stage5 Recommend a bounded next action](#stage5-recommend-a-bounded-next-action)

## Stage1 Define the useful change

**Goal:** State the capability and conditions worth improving.

**Why:** A technology name conceals the goal needed to evaluate it.

**What to do:** Separate purpose, current limitation, hard constraints and desired outcomes.

**What to observe:** Whether the goal changes for transient, steady, peak or typical use.

**Success signal:** A comparison can be evaluated without assuming one solution.

**Next:** Map alternatives.

**Understanding:** A cooler short burst, lower continuous temperature, less mass and lower power are different objectives. The useful insight may be that the problem contains multiple regimes rather than that one component is superior.

**Procedure**

1. Write the decision and the current baseline.
2. Define relevant users, environment, time horizon and measurable or observable outcomes.
3. Record hard constraints and who may authorize further evaluation.
4. Ask which uncertainty most limits progress and what answer would change action.

**Fallback and stopping:** If no decision depends on the answer, treat it as open study or narrow the purpose rather than manufacturing urgency.

**Established techniques in this stage: 5W2H and Horizon Scanning.** Define who benefits, what capability matters, when and where it is needed, why the incumbent is inadequate, how outcomes are measured and how much change is useful. Before scanning set the horizon and source coverage. For each signal record date, original source, evidence family, possible implication, counter-signal and next check. Group repeated publicity rather than counting it as independent progress. End the scan when more leads cannot materially change the bounded next decision.

## Stage2 Map mechanisms and competing approaches

**Goal:** Identify genuinely different routes to the goal.

**Why:** A landscape can reveal an untested assumption or omitted option before investment in a favoured design.

**What to do:** Compare existing, simpler, no-change and novel candidate approaches.

**What to observe:** Evidence type, mechanism, applicability and common upstream claims.

**Success signal:** Alternatives have meaningful distinctions and explicit gaps.

**Next:** Construct an explanatory opportunity hypothesis.

**Understanding:** Do not compare marketing labels as though they were mechanisms. For each approach identify what physical, computational or organizational relationship produces the intended effect and what limits it.

**Procedure**

1. Search claim-relevant official and primary sources; record what was inspected.
2. Build a small table of approach, mechanism, benefit, cost, applicability and unresolved assumptions.
3. Trace repeated citations to evidence families and inspect contrary evidence or failure contexts.
4. Record bounded search coverage and distinguish established ideas from speculation.

**Fallback and stopping:** A missing search hit is not proof of originality or absence. A vendor benchmark alone does not establish general performance.

**Established techniques in this stage: structured literature review, Patent Landscaping and TRL assessment.** Log keywords, classifications, databases, dates and exclusions; separate patent priority, filing and publication. Declare the family definition before counting related records. Compare candidate mechanisms under common benchmarks with raw units and context, not marketing labels. For readiness, identify the artifact, framework, environment, inspected demonstrations and missing integration evidence. Do not average component levels or assume a filing establishes feasibility, ownership or freedom to operate. The output is a landscape plus criterion-level gaps, not a universal ranking.

## Stage3 Explain the proposed opportunity

**Goal:** Turn an attractive option into a claim that can be tested.

**Why:** A solution can only be evaluated against an expected mechanism, context and competing explanation.

**What to do:** Build a scoped model and predicted advantage over alternatives.

**What to observe:** Assumptions that could reverse the ranking or create harm.

**Success signal:** The claimed advantage has an observable consequence and counter-signal.

**Next:** Select a decisive check.

**Understanding:** The insight may be a regime distinction, interaction or constraint. For example, additional heat storage and improved heat removal affect different parts of a transient response. That distinction can generate multiple designs.

**Procedure**

1. State the proposed relationship and why it matters for the target duty or context.
2. Define variables, units and limiting cases; distinguish supporting science from chosen approximations.
3. Compare rival explanations of the claimed benefit and identify missing measurements.
4. Write what evidence would reject the opportunity rather than merely refine its marketing story.

**Fallback and stopping:** If all explanations predict the same claimed gain, the current evidence may select a useful action without identifying its mechanism.

**Established techniques in this stage: TRIZ contradiction analysis and Morphological Analysis.** Write what improves and what worsens, distinguishing a property tradeoff from opposing requirements for one property. Explore separation in time, space, condition or system level and the use of existing resources. A morphological field lists alternatives for meaningful functional dimensions; cross-consistency eliminates incompatible combinations but cannot guarantee whole-system feasibility. For every retained candidate state a mechanism, an adverse effect and a falsifying comparison. These are generated possibilities, not demonstrated advances.

## Stage4 Reduce the decisive uncertainty

**Goal:** Learn enough to decide whether further investment is justified.

**Why:** Analysis effort has a cost and can be misdirected toward uncertainties that cannot change the decision.

**What to do:** Choose safe analysis, a fixture, simulation or approved pilot with defined predictions.

**What to observe:** Expected versus actual manipulation, response and adverse outcomes.

**Success signal:** The result changes or bounds the decision-relevant uncertainty.

**Next:** Choose a next investment or stop.

**Understanding:** A small experiment is not automatically representative. Select the design based on the uncertainty: a limiting calculation, interaction study and usability observation address different questions.

**Procedure**

1. List the uncertain premises and the decisions each could change.
2. Choose a permitted check with comparator, uncertainty plan and stop criteria; obtain the required expertise.
3. Record exact conditions and outcomes, including deviations and inconclusive results.
4. Evaluate both benefit and harms without reclassifying exploratory work as confirmatory.

**Fallback and stopping:** Use a surrogate or specialist review when the informative intervention is unsafe. Do not keep testing merely because the first result was unfavourable.

**Established techniques in this stage: Heilmeier Catechism and DOE.** Answer in ordinary language: objective, current approach and limitation, what is new, basis for success, beneficiary and outcome, risks, resource/time assumptions and intermediate/final checks. Identify a milestone that can fail. Use the appropriate design to test the decisive technical premise on representative units and conditions, preserving uncertainty and authorization. A well-framed research case can justify a small study; it does not prove feasibility or qualify a proposal for funding.

## Stage5 Recommend a bounded next action

**Goal:** Separate a supported insight from the funding or implementation choice.

**Why:** Preferences and constraints complete the bridge from evidence to action.

**What to do:** Compare alternatives, record rationale and define an application or research boundary.

**What to observe:** Sensitivity to context, uncertainty and decision priorities.

**Success signal:** The owner can accept, reject or defer with a clear reason.

**Next:** Transfer cautiously or preserve the unresolved question.

**Understanding:** An option can be technically promising without being the best next action. A null result or evidence of limited applicability can prevent wasted work and is legitimate insight.

**Procedure**

1. Summarize the claim, evidence and scope in language usable by the decision owner.
2. Compare no change and lower-complexity alternatives under the same objectives.
3. State what is recommended, by whom, and which further evidence or monitoring is required.
4. Write the insight separately from the selected design; publish only permitted source-linked knowledge.

**Fallback and stopping:** Do not imply that a desk study proves manufacturability, safety, economics or field-wide novelty.

**Established techniques in this stage: Pugh matrix, weighted decision matrix, Radar Chart and Technology Roadmapping.** Screen hard constraints first. For Pugh, compare candidates to a named datum with +, 0, -, or unknown and evidence per criterion. Use weighted scoring only with declared scales, preferences and sensitivity checks. Radar is optional display: keep raw values, common bounds, consistent desirable direction and missing values; do not rank polygon area. Build a roadmap connecting need -> capability -> technology/resources -> demonstration gates. Each gate needs an owner, timing basis and continue/redesign/stop condition. Record the selected action separately from the technical insight.

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

[NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md) [Cochrane collecting data guidance](../references/li-2019-collecting-data-cochrane.md) [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md) informs the underlying distinctions. The stage selection, operational synthesis and examples are authored here. This Practice is not independently validated, a professional certification or authorization for hazardous experiments. It does not guarantee original discovery, causality or successful application.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Map a technical landscape in the Practice](../practices/investigate-a-technical-opportunity.md#stage2-map-mechanisms-and-competing-approaches)
- [Compare technical alternatives in the Practice](../practices/investigate-a-technical-opportunity.md#stage5-recommend-a-bounded-next-action)
- [Build an explanatory model in the Practice](../practices/discover-and-validate-a-technical-insight.md#stage4-build-rival-explanations-and-a-model)
- [Design a discriminating test in the Practice](../practices/discover-and-validate-a-technical-insight.md#stage5-design-a-discriminating-comparison)
- [Novelty and evidential support are different properties](../principles/novelty-and-support-are-different-properties.md)
- [Decision and transfer model](../models/decision-and-transfer-model.md)

- [NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md)
- [Cochrane collecting data guidance](../references/li-2019-collecting-data-cochrane.md)
- [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md)

[Package home](../README.md)
