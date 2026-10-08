---
id: "ti:pr:assess-a-technical-claim"
type: "practice"
version: "2.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-08"
basis_kind: "authored Practice integrating established techniques; not an independently validated programme"
confidence: "provisional for application"
stage_titles: ["Stage1 Extract the exact claim", "Stage2 Inspect sources and independence", "Stage3 Reconstruct the argument", "Stage4 Challenge the consequential uncertainty", "Stage5 Publish the judgment with boundaries"]
practice_format: "staged-inline-local-v1"
uses_methods: ["ti:me:5w2h", "ti:me:structured-literature-review", "ti:me:hypothesis-driven-analysis", "ti:me:measurement-uncertainty-budget", "ti:me:sensitivity-analysis", "ti:me:statistical-hypothesis-testing", "ti:me:design-of-experiments"]
uses_models: ["ti:mo:claim-evidence-inference-model"]
references: ["ti:r:ahrq-undated-5w2h", "ti:r:bain-undated-case-interview-preparation", "ti:r:li-2019-collecting-data-cochrane", "ti:r:nasa-7009b-2024-models-and-simulations", "ti:r:nasa-undated-decision-analysis", "ti:r:nist-undated-experimental-design-handbook", "ti:r:nist-undated-hypothesis-tests", "ti:r:nist-undated-measurement-uncertainty", "ti:r:nist-undated-model-fit-and-residuals", "ti:r:pearl-2009-causal-inference-in-statistics", "ti:r:sandve-2013-reproducible-computational-research", "ti:r:w3c-2013-prov-overview"]
---

# Assess a technical claim

## Key takeaway

Evaluate the exact claim and its supporting chain before adopting the conclusion.

## Summary

Use this for a paper, product claim, AI explanation, internal analysis or existing knowledge object. It distinguishes source quality, evidence independence, inference quality and relevance to the intended use. An honest result may be a narrowed or unresolved claim.


## Established techniques used

[5W2H](../methods/5w2h.md), [Structured literature review](../methods/structured-literature-review.md), [Hypothesis driven analysis](../methods/hypothesis-driven-analysis.md), [Measurement uncertainty budget](../methods/measurement-uncertainty-budget.md), [Sensitivity analysis](../methods/sensitivity-analysis.md), [Statistical hypothesis testing](../methods/statistical-hypothesis-testing.md), [Design of experiments](../methods/design-of-experiments.md). These supply repeatable techniques; the stage order, handoffs and decisions below are our authored Practice, not an official combined method.


## Goal and prerequisites

Bring the claim and the use it would support. Obtain the source material where permitted and preserve its context. A public claim does not authorize investigation of private systems.

Stage numbers show recommended reading and learning order. Actual prerequisites, safety conditions and authorization govern entry. Revisit any stage when evidence requires it; this is not a one-way proof pipeline.

## Stage map

1. [Stage1 Extract the exact claim](#stage1-extract-the-exact-claim)
2. [Stage2 Inspect sources and independence](#stage2-inspect-sources-and-independence)
3. [Stage3 Reconstruct the argument](#stage3-reconstruct-the-argument)
4. [Stage4 Challenge the consequential uncertainty](#stage4-challenge-the-consequential-uncertainty)
5. [Stage5 Publish the judgment with boundaries](#stage5-publish-the-judgment-with-boundaries)

## Stage1 Extract the exact claim

**Goal:** Identify what is asserted and what decision it would influence.

**Why:** A vague claim can shift meaning when challenged.

**What to do:** Separate definition, association, mechanism, efficacy and recommendation.

**What to observe:** Qualifiers, outcome definitions, comparator and context.

**Success signal:** The claim is precise enough to be supported or challenged.

**Next:** Trace source contributions.

**Understanding:** “Improves performance” may mean latency, throughput, energy or user success. A precise claim distinguishes average, tail, transient and steady outcomes. A source’s recommendation may depend on a preference not shared by the target use.

**Procedure**

1. Preserve the original wording and its surrounding qualifications.
2. Restate the narrowest faithful claim in your own words with scope and comparator.
3. Separate distinct claims rather than requiring one citation to support all of them.
4. Record why accepting the claim would matter.

**Fallback and stopping:** Do not silently strengthen or repair the source. Mark an ambiguous claim as ambiguous until clarified.

**5W2H application.** Extract the exact statement, claimant, intended population/system, timing, environment, outcome measure and claimed magnitude. Why may mean the claim's relevance or its asserted cause; distinguish them. Record unspecified comparisons rather than quietly supplying an easier claim to test.

## Stage2 Inspect sources and independence

**Goal:** Find what evidence was actually supplied.

**Why:** Repeated assertions and prestigious attribution are not equivalent to independent testing.

**What to do:** Locate source passages, study/data families and inspection limits.

**What to observe:** Directness, measured conditions, missing methods and shared data.

**Success signal:** Each cited contribution has a role and identifiable limits.

**Next:** Examine the reasoning bridge.

**Understanding:** A review and its included experiment are two publications but one underlying experiment. A specification can be authoritative about its own requirements without proving their universal efficacy.

**Procedure**

1. Register publication identity, reliable date and exact inspected extent.
2. Extract relevant observations, derivations or guidance and what they do not establish.
3. Map common evidence families and distinguish uninspected upstream citations.
4. Seek a materially independent challenge or boundary case when the claim warrants it.

**Fallback and stopping:** Use abstract-level support only for what the abstract says. Do not pretend inaccessible evidence resolves a disputed detail.

**Structured review application.** Trace summaries to original work. Record search boundary, selection reasons, study/report families, actual access extent and evidence limitations. A reference confirms the origin of a statement, not its truth. A negative result and an unsearched area are different entries.

## Stage3 Reconstruct the argument

**Goal:** Expose the assumptions between evidence and conclusion.

**Why:** A valid observation can support an invalid inference.

**What to do:** Represent premises, model, predictions and alternatives in plain language.

**What to observe:** Scope jumps, causal leaps, missing uncertainty and unexamined goals.

**Success signal:** A reviewer can identify the exact uncertain inference.

**Next:** Run a relevant challenge if permitted.

**Understanding:** Good fit is not a mechanism proof; reproduced computation is not independent empirical validation. A threshold can be a chosen requirement rather than a discovered physical limit.

**Procedure**

1. List source-supported premises separately from author assumptions.
2. Reconstruct the minimum model needed for the conclusion, including units and intended use.
3. Ask whether rival accounts can explain the same evidence.
4. Compare source and intended-use contexts and identify where extrapolation occurs.

**Fallback and stopping:** If the argument cannot be reconstructed, do not fill it with a more sophisticated story and attribute that story to the source.

**Hypothesis-driven analysis application.** Write premises, modeling assumptions and inference as distinct statements. Compare the proposed explanation with a rival mechanism and an observation artifact. Check units, boundary conditions and a limiting case. Retain an incomplete argument as incomplete rather than repairing it and attributing the repair to the source.

## Stage4 Challenge the consequential uncertainty

**Goal:** Check the part most likely to change the verdict.

**Why:** Repeating an easy calculation may leave the material assumption untouched.

**What to do:** Select a unit check, alternative analysis, reproducibility check or independent test.

**What to observe:** Whether the challenge could really weaken the claim.

**Success signal:** The outcome informs a bounded judgment and its uncertainty.

**Next:** Report a qualified verdict.

**Understanding:** A deterministic example can disprove an overbroad logical claim without validating a physical model. New measurements can broaden evidence but may retain shared calibration or selection effects.

**Procedure**

1. Choose a challenge and state its expected and contrary outcomes.
2. Verify authority and safety before using data or changing systems.
3. Record exact inputs, execution and observations; retain failed checks.
4. Assess whether a discrepancy concerns implementation, measurement, scope or the claimed mechanism.

**Fallback and stopping:** If testing is unavailable, report an evidence gap rather than simulate a favourable real result.

**DOE, uncertainty and sensitivity application.** Select a check that can distinguish the important alternatives, not simply reproduce a convenient number. Preserve independent-unit and measurement assumptions. Report effect sizes and intervals when supported; statistical significance is not practical importance or causality. If safe intervention is unavailable, document that limitation rather than inventing a result.

## Stage5 Publish the judgment with boundaries

**Goal:** Communicate what is supported and what is not.

**Why:** A binary verdict can hide partially valid or scope-dependent findings.

**What to do:** Separate effect support, mechanism support, applicability and recommendation.

**What to observe:** Whether caveats survive the short summary.

**Success signal:** The reader can make a bounded decision and know when to revisit it.

**Next:** Revise affected knowledge or request further evidence.

**Understanding:** Supported within context is not universal truth. Contradicted under one condition can narrow a claim rather than erase every useful part. Unresolved does not mean false.

**Procedure**

1. State the conclusion alongside the specific evidence and material limitations.
2. List the inference steps supplied by this review rather than by the source.
3. Give an actionable next decision: bounded use, more evidence, no adoption or specialist assessment.
4. Update downstream summaries and reference records without disguising the review as a full systematic review.

**Fallback and stopping:** Do not create a numerical confidence score without an explicit justified model. Keep judgment and approval distinct.

**Judgment record.** State supported, contradicted or unresolved components separately. Distinguish a statistical finding, a causal account, source access, applicability and a recommended action. Record what changed relative to the prior assessment and the evidence needed to revise the conclusion. This combination of Methods and documentation is our Practice.

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

[Cochrane collecting data guidance](../references/li-2019-collecting-data-cochrane.md) [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md) [NIST model fit and residual analysis](../references/nist-undated-model-fit-and-residuals.md) [Reproducible computational research](../references/sandve-2013-reproducible-computational-research.md) informs the underlying distinctions. The stage selection, operational synthesis and examples are authored here. This Practice is not independently validated, a professional certification or authorization for hazardous experiments. It does not guarantee original discovery, causality or successful application.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Synthesize claim relevant sources in the Practice](../practices/discover-and-validate-a-technical-insight.md#stage3-find-the-knowledge-the-question-needs)
- [Audit an observation in the Practice](../practices/discover-and-validate-a-technical-insight.md#stage2-audit-the-evidence-before-the-story)
- [Challenge and replicate an explanation in the Practice](../practices/discover-and-validate-a-technical-insight.md#stage7-evaluate-the-explanation-and-its-limits)
- [Evaluate results and uncertainty in the Practice](../practices/discover-and-validate-a-technical-insight.md#stage7-evaluate-the-explanation-and-its-limits)
- [Claim evidence and inference model](../models/claim-evidence-inference-model.md)

- [Cochrane collecting data guidance](../references/li-2019-collecting-data-cochrane.md)
- [Causal inference in statistics An overview](../references/pearl-2009-causal-inference-in-statistics.md)
- [NIST model fit and residual analysis](../references/nist-undated-model-fit-and-residuals.md)
- [Reproducible computational research](../references/sandve-2013-reproducible-computational-research.md)

[Package home](../README.md)
