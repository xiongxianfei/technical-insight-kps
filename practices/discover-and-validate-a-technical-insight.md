---
id: "ti:pr:discover-and-validate-a-technical-insight"
type: "practice"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored operational synthesis; no field effectiveness study"
confidence: "provisional for application"
stage_titles: ["Stage1 Bound the question and authority", "Stage2 Audit the evidence before the story", "Stage3 Find the knowledge the question needs", "Stage4 Build rival explanations and a model", "Stage5 Design a discriminating comparison", "Stage6 Execute and preserve what happened", "Stage7 Evaluate the explanation and its limits", "Stage8 Document apply and keep the question revisable"]
practice_format: "staged-inline-local-v1"
uses_methods: ["ti:me:frame-an-insight-question","ti:me:audit-an-observation","ti:me:synthesize-claim-relevant-sources","ti:me:generate-competing-explanations","ti:me:build-an-explanatory-model","ti:me:design-a-discriminating-test","ti:me:execute-a-bounded-test","ti:me:evaluate-results-and-uncertainty","ti:me:write-an-insight-record","ti:me:structure-and-prioritize-hypotheses"]
uses_models: ["ti:mo:insight-learning-cycle","ti:mo:investigation-and-intelligence-routing-model"]
references: ["ti:r:pearl-2009-causal-inference-in-statistics","ti:r:nist-undated-measurement-uncertainty","ti:r:nist-undated-experimental-design-handbook","ti:r:nasa-7009b-2024-models-and-simulations","ti:r:nasa-undated-decision-analysis","ti:r:w3c-2013-prov-overview","ti:r:bain-undated-case-interview-preparation"]
---

# Discover and validate a technical insight

## Key takeaway

Build a scoped explanation by connecting a consequential question to evidence that can challenge competing accounts.

## Summary

This is the primary Practice for turning a surprise or knowledge gap into a reusable technical insight. It combines observation auditing, source synthesis, explanatory modeling, permitted tests and honest reporting. A supported result, a narrowed claim and a well-justified unresolved question are all legitimate outcomes.

## Investigation method selection

Use a Bain-inspired issue tree as an aid for breaking the engineering decision into observable questions, then write rival hypotheses for the parts whose outcome would change the decision. Decomposition and prioritization organize attention; they do not establish causality. Select a discriminating observation and check it against measurement and model uncertainty. If the uncertainty concerns which technologies exist or whether a research opportunity is worth pursuing, pass the bounded need and existing evidence to [the technology opportunity Practice](investigate-a-technical-opportunity.md). Do not upgrade a source report to a demonstrated capability.

## Goal and prerequisites

Use for a technical uncertainty whose resolution could change a prediction, design or investigation. Bring a concrete question and access to relevant evidence. Perform only operations you are competent and authorized to perform; hazardous equipment, production systems, personal data and human studies need their applicable approvals.

Stage numbers show recommended reading and learning order. Actual prerequisites, safety conditions and authorization govern entry. Revisit any stage when evidence requires it; this is not a one-way proof pipeline.

## Stage map

1. [Stage1 Bound the question and authority](#stage1-bound-the-question-and-authority)
2. [Stage2 Audit the evidence before the story](#stage2-audit-the-evidence-before-the-story)
3. [Stage3 Find the knowledge the question needs](#stage3-find-the-knowledge-the-question-needs)
4. [Stage4 Build rival explanations and a model](#stage4-build-rival-explanations-and-a-model)
5. [Stage5 Design a discriminating comparison](#stage5-design-a-discriminating-comparison)
6. [Stage6 Execute and preserve what happened](#stage6-execute-and-preserve-what-happened)
7. [Stage7 Evaluate the explanation and its limits](#stage7-evaluate-the-explanation-and-its-limits)
8. [Stage8 Document apply and keep the question revisable](#stage8-document-apply-and-keep-the-question-revisable)

## Stage1 Bound the question and authority

**Goal:** Name the uncertainty and the decision it affects.

**Why:** Without an objective and boundary, a technically interesting answer can be irrelevant or unsafe to obtain.

**What to do:** Write the outcome, context, comparator, scope and permitted operations.

**What to observe:** Whether different answers change the decision and whether the needed observations are accessible.

**Success signal:** A reader can restate the question and know what is outside scope.

**Next:** Audit existing observations, or reframe an unanswerable question.

**Understanding:** Separate a capability goal from a suggested solution. “Use a new material” is a candidate intervention; “reduce temperature during a 100-second burst” is an assessable purpose. The latter still needs input conditions, a comparison and uncertainty.

**Procedure**

1. Write one purpose sentence and identify the person who can act on the answer.
2. Describe the system, environment, interfaces, time scale and measurement path. Define the outcome with units or events.
3. List available evidence, uncertain inputs and hard constraints. Record what can be observed versus changed.
4. Choose a stopping point: a bounded decision, a permitted pilot or an explicit specialist handoff.

**Fallback and stopping:** Do not begin a test when competence, authority or safe stopping is unclear. Desk study can continue without intervention.

**Integrated framing check:** Write a decision owner, current baseline, named measurement and safe authorization boundary. Split the issue into observation quality, technical mechanism and use-context questions. These branches are organizational prompts, not proof that physical causes are mutually exclusive; mechanisms may interact. Select the first question by whether its answer would change the decision, not by how confidently it was proposed.

## Stage2 Audit the evidence before the story

**Goal:** Establish what actually happened and how it became observable.

**Why:** A displayed anomaly may arise from instrument, sampling, configuration or analysis effects.

**What to do:** Preserve the observation and inspect its acquisition chain.

**What to observe:** Units, time alignment, calibration, missingness, transformations and configuration differences.

**Success signal:** The report distinguishes original evidence from interpretation and unresolved quality issues.

**Next:** Search for relevant explanations and source support.

**Understanding:** A repeated number is not automatically accurate. Several measurements can share one offset; a log can omit events; preprocessing can remove excursions. Identify which uncertainty is material to the question rather than auditing every possible detail equally.

**Procedure**

1. Save a versioned evidence reference with time, source and conditions; keep private data outside public knowledge.
2. Define the quantity/event and reconstruct the route from input to displayed result.
3. Check units, clocks, sampling, filtering and an appropriate independent reference where available.
4. Write an observation sentence without a causal claim, followed by a separate interpretation and confidence limitation.

**Fallback and stopping:** If the original is unavailable, label the account second-hand. If quality is inadequate, reacquire safely or limit the claim.

## Stage3 Find the knowledge the question needs

**Goal:** Build an evidence base for specific claims, not a pile of related articles.

**Why:** Sources contribute different kinds of support and may repeat one underlying result.

**What to do:** Decompose the claims and synthesize located source contributions.

**What to observe:** Definitions, populations, setups, outcomes, independence and disagreements.

**Success signal:** Each consequential premise has a source, derivation or explicit uncertainty label.

**Next:** Generate competing explanations rather than adopting the first source as authority.

**Understanding:** A primary experiment can support a measured relation; a handbook can explain a method; a standard can establish a requirement within its authority. They do not all prove the same kind of claim. Source quantity is not independent replication.

**Procedure**

1. Separate what is being defined, observed, explained, predicted and recommended.
2. Search for direct technical sources and meaningful alternatives or negative results. Record exactly which sections or abstracts were inspected.
3. For each source note its contribution, context, evidence family and what it does not establish.
4. Write agreement, disagreement and your own inference separately; stop when the remaining gap is clear enough to guide the next test.

**Fallback and stopping:** Do not reconstruct inaccessible text from memory or use a prestigious citation to fill an unsupported step. Record unresolved source disagreement.

## Stage4 Build rival explanations and a model

**Goal:** Expose why the observation might occur and how the accounts differ.

**Why:** A compatible explanation is not uniquely established when rivals predict the same result.

**What to do:** Create a hypothesis-prediction matrix and a small explanatory representation.

**What to observe:** Distinctive predictions, model assumptions, units and omitted feedback or context.

**Success signal:** At least the material alternatives and their discriminating consequences are explicit.

**Next:** Plan the least risky useful check.

**Understanding:** Include measurement and context accounts as well as system mechanisms. A causal sketch is an assumption set. A numerical model also needs a validity envelope: intended use, parameter sources, calibration, independent checks and limits.

**Procedure**

1. Write candidate accounts with intermediate mechanisms, not merely renamed symptoms.
2. Draw events/relationships or equations, defining variables and units. Mark source-supported relations versus assumptions.
3. Derive qualitative or quantitative consequences and limiting cases; verify arithmetic and signs.
4. Compare the predictions across rivals and identify one difference large enough to inspect with available measurement.

**Fallback and stopping:** If no available test separates the accounts, keep them unresolved and consider an action robust to both. Do not invent a unique root cause.

**Hypothesis structuring and priority:** Apply [Structure and prioritize hypotheses](../methods/structure-and-prioritize-hypotheses.md) to the issue tree. Include measurement-process and context explanations alongside the favored mechanism. For each account, write a distinguishing prediction, a counter-signal and an assumption. A list of possible causes is not yet a causal model; if two explanations predict the same observation, preserve both until an authorized comparison can separate them.

## Stage5 Design a discriminating comparison

**Goal:** Choose an authorized test that can challenge the consequential explanation.

**Why:** Uncontrolled changes, interactions and measurement limits can make a favourable result ambiguous.

**What to do:** Specify comparator, units of replication, manipulation check, analysis and stopping plan.

**What to observe:** Whether the intended factor differs without an unaccounted nuisance difference.

**Success signal:** The test can produce an informative adverse or inconclusive outcome without unacceptable risk.

**Next:** Execute only after prerequisites are confirmed.

**Understanding:** One-factor comparisons are not a universal rule. When one factor’s effect depends on another, joint combinations may be needed. Blocking and randomization address different nuisance problems; carryover needs its own treatment. Repeated readings from one unit do not automatically provide independent replication.

**Procedure**

1. Choose analytic, software, simulation or approved physical testing according to the claim and risk.
2. Define outcome, conditions, expected difference, uncertainty and contrary signal before examining confirmatory results.
3. Select relevant controls and an appropriate design; justify sample size or plan further statistical design rather than inventing a universal number.
4. Specify execution fidelity, excluded data, stop criteria and rollback responsibility. Obtain necessary review.

**Fallback and stopping:** If a comparator is harmful or operationally prohibited, use a safe surrogate or change the question. A completed plan is not an executed test.

**Selection check:** Order candidate comparisons by decision impact, predicted discrimination, source quality, reversibility and authorization. Preserve a proposed test that failed feasibility review as a rejected option, not as a completed experiment. A desk source inspection, fixture or documented simulation can be chosen instead, but its inferential scope must be stated before the result.

## Stage6 Execute and preserve what happened

**Goal:** Obtain an interpretable result without hiding deviations.

**Why:** A planned intervention and actual intervention can differ, invalidating the planned inference.

**What to do:** Record setup, verify manipulation, retain raw outputs and stop on boundary violations.

**What to observe:** Configuration fidelity, unexpected events, missing data and safeguard conditions.

**Success signal:** The record states what ran, what changed, what was observed and what did not run.

**Next:** Evaluate the claim and competing accounts.

**Understanding:** Observations, processing and interpretations are separate artifacts. A failed run can be evidence about setup or reliability even when it cannot answer the intended mechanism question. Do not silently discard it.

**Procedure**

1. Confirm permissions, safety/rollback and measurement readiness immediately before execution.
2. Record exact input, code/equipment configuration and planned order.
3. Run only the permitted procedure and verify the intended manipulation occurred. Preserve raw results and deviations.
4. Label execution complete, partial, invalid or not executed; identify analysis inputs without publicly exposing restricted data.

**Fallback and stopping:** Stop for hazards, unexpected adverse effects or invalid measurement. Do not reproduce damage as a control; seek domain-qualified help.

## Stage7 Evaluate the explanation and its limits

**Goal:** State what the result supports without overgeneralizing.

**Why:** A helpful change, a correct mechanism and a valid model outside the test context are different claims.

**What to do:** Compare predictions, uncertainty, alternatives and application consequences.

**What to observe:** Residual structure, effect size, harms, failed manipulation and untested conditions.

**Success signal:** The verdict distinguishes effect, mechanism, scope and decision confidence.

**Next:** Document the insight or return to the unresolved assumption.

**Understanding:** A model fitted to the same evidence cannot claim independent validation from that fit. Look at data structure, not a single favourable number. An absence of detected difference does not establish equivalence. A test may narrow uncertainty without uniquely identifying a cause.

**Procedure**

1. Check test fidelity before interpreting outcome. Compare planned predictions and contrary signals.
2. Inspect variation and residuals where relevant; keep exploratory analyses distinguishable.
3. Update each rival account: supported within scope, weakened, contradicted or still compatible, with reasons.
4. Record whether the result justifies an application, another check or stopping with bounded uncertainty.

**Fallback and stopping:** If results change under reasonable analysis choices, report that sensitivity. Do not erase a contradictory result to create a tidy story.

## Stage8 Document apply and keep the question revisable

**Goal:** Convert the supported understanding into reusable knowledge and an explicit next decision.

**Why:** A result loses context when its assumptions and evidence disappear from the published conclusion.

**What to do:** Write the scoped insight and identify appropriate KPS objects and applications.

**What to observe:** Whether local summaries preserve caveats and whether target use changes assumptions.

**Success signal:** The reader can understand the claim, basis, limits and next action without opening every link.

**Next:** Apply through a bounded decision or publish a reviewable knowledge change.

**Understanding:** A technical insight is not a sixth mandatory object type. Its explanatory relationship may become a Principle, its representation a Model, its operation a Method and its integrated use a Practice. An actual investigation record remains supporting evidence.

**Procedure**

1. Write context, claim, mechanism/relationship, evidence, rivals, limitations and decision consequences.
2. Separate novelty to this project from unsupported claims of scientific originality.
3. For a new application compare source and target assumptions; define monitoring and a revision trigger.
4. Review confidentiality, references, self-containment and navigation; publish via a ready-for-review PR or validated ZIP without merging or releasing automatically.

**Fallback and stopping:** If the claim is unvalidated, preserve that status. Publication completeness cannot replace missing evidence or an authorized adoption decision.

**Handoff and tool discipline:** Record the qualifying context, contrary evidence, permission boundaries and any unresolved mechanism. The [integrated Practice routes](../INTEGRATED-PRACTICES.md) explain when to hand a capability gap to technology intelligence. Spreadsheets, calculations, Python or an AI assistant can support comparisons but do not independently validate premises or grant safety authorization.

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

[Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md) [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md) [NIST experimental design guidance](../references/nist-undated-experimental-design-handbook.md) [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md) [NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md) [W3C provenance overview](../references/w3c-2013-prov-overview.md) informs the underlying distinctions. The stage selection, operational synthesis and examples are authored here. This Practice is not independently validated, a professional certification or authorization for hazardous experiments. It does not guarantee original discovery, causality or successful application.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Frame an insight question](../methods/frame-an-insight-question.md)
- [Audit an observation](../methods/audit-an-observation.md)
- [Synthesize claim relevant sources](../methods/synthesize-claim-relevant-sources.md)
- [Generate competing explanations](../methods/generate-competing-explanations.md)
- [Build an explanatory model](../methods/build-an-explanatory-model.md)
- [Design a discriminating test](../methods/design-a-discriminating-test.md)
- [Execute a bounded test](../methods/execute-a-bounded-test.md)
- [Evaluate results and uncertainty](../methods/evaluate-results-and-uncertainty.md)
- [Write an insight record](../methods/write-an-insight-record.md)
- [Insight learning cycle](../models/insight-learning-cycle.md)

- [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md)
- [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md)
- [NIST experimental design guidance](../references/nist-undated-experimental-design-handbook.md)
- [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md)
- [NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md)
- [W3C provenance overview](../references/w3c-2013-prov-overview.md)

[Package home](../README.md)
