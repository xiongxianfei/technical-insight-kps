---
language: "KPS 9.x"
reviewed: "2026-10-08"
package_version: "2.0.0"
---

# Complete Method transition

## Key takeaway

All 20 generic Method operations have named receiving Practice stages and established supporting techniques.

## Summary

This is a breaking 2.0.0 domain refactor, not a KPS language change. It replaces the active generic Method layer and preserves the responsibilities below in Practices. Old files remain available through prior Git history, not live stubs or duplicate Method documentation.

## Scope and source baseline

The inspected repository baseline is `85a92fdd39453a0de670cbfeadea85f237acc749` on main, after the merged 1.1.0 integrated Practices. Original 1.0 knowledge bytes from the prior publication and current repository content supplied the starting material. The later intelligence concepts, models, reference contributions and integrated workflow responsibilities are included and reworked in this snapshot; it is not an overlay that silently drops them.

## Responsibility map

| Retired Method filename | Receiving Practice stage | Responsibility retained | Established supporting techniques |
|---|---|---|---|
| `frame-an-insight-question.md` | [Stage1 Bound the question and authority](practices/discover-and-validate-a-technical-insight.md#stage1-bound-the-question-and-authority) | Purpose, boundary, authority, measures and a decision-relevant question | [5W2H](methods/5w2h.md), [SIPOC](methods/sipoc.md) |
| `audit-an-observation.md` | [Stage2 Audit the evidence before the story](practices/discover-and-validate-a-technical-insight.md#stage2-audit-the-evidence-before-the-story) | Observation versus interpretation, calibration, provenance and artifacts | [SIPOC](methods/sipoc.md), [Measurement uncertainty budget](methods/measurement-uncertainty-budget.md) |
| `synthesize-claim-relevant-sources.md` | [Stage3 Find the knowledge the question needs](practices/discover-and-validate-a-technical-insight.md#stage3-find-the-knowledge-the-question-needs) | Claim-oriented extraction, evidence families, contradictions and access limits | [Structured literature review](methods/structured-literature-review.md) |
| `generate-competing-explanations.md` | [Stage4 Build rival explanations and a model](practices/discover-and-validate-a-technical-insight.md#stage4-build-rival-explanations-and-a-model) | Rival mechanisms, observation artifacts and contrary predictions | [Hypothesis driven analysis](methods/hypothesis-driven-analysis.md), [Fishbone analysis](methods/fishbone-analysis.md), [Five Whys](methods/five-whys.md) |
| `build-an-explanatory-model.md` | [Stage4 Build rival explanations and a model](practices/discover-and-validate-a-technical-insight.md#stage4-build-rival-explanations-and-a-model) | Variables, units, relationships, limiting cases and applicability | [Hypothesis driven analysis](methods/hypothesis-driven-analysis.md), [Sensitivity analysis](methods/sensitivity-analysis.md) |
| `design-a-discriminating-test.md` | [Stage5 Design a discriminating comparison](practices/discover-and-validate-a-technical-insight.md#stage5-design-a-discriminating-comparison) | Comparators, manipulation, controls, independent units and safe stopping | [Design of experiments](methods/design-of-experiments.md), [Measurement uncertainty budget](methods/measurement-uncertainty-budget.md) |
| `execute-a-bounded-test.md` | [Stage6 Execute and preserve what happened](practices/discover-and-validate-a-technical-insight.md#stage6-execute-and-preserve-what-happened) | Actual execution, configurations, deviations, raw results and authority | [Design of experiments](methods/design-of-experiments.md) |
| `evaluate-results-and-uncertainty.md` | [Stage7 Evaluate the explanation and its limits](practices/discover-and-validate-a-technical-insight.md#stage7-evaluate-the-explanation-and-its-limits) | Effect, uncertainty, execution validity and inconclusive conclusions | [Statistical hypothesis testing](methods/statistical-hypothesis-testing.md), [Measurement uncertainty budget](methods/measurement-uncertainty-budget.md), [Sensitivity analysis](methods/sensitivity-analysis.md) |
| `challenge-and-replicate-an-explanation.md` | [Stage7 Evaluate the explanation and its limits](practices/discover-and-validate-a-technical-insight.md#stage7-evaluate-the-explanation-and-its-limits) | Independent challenge, reproducibility limits and alternative explanations | [Design of experiments](methods/design-of-experiments.md), [Sensitivity analysis](methods/sensitivity-analysis.md) |
| `compare-technical-alternatives.md` | [Stage5 Recommend a bounded next action](practices/investigate-a-technical-opportunity.md#stage5-recommend-a-bounded-next-action) | Constraints before preferences, raw evidence, uncertainty and reversibility | [Pugh matrix](methods/pugh-matrix.md), [Weighted decision matrix](methods/weighted-decision-matrix.md) |
| `assess-transfer-to-a-new-context.md` | [Stage2 Map preserved changed and unknown assumptions](practices/apply-and-transfer-an-insight.md#stage2-map-preserved-changed-and-unknown-assumptions) | Preserved, changed and unknown assumptions in the target context | [Technology readiness assessment](methods/technology-readiness-assessment.md), [Sensitivity analysis](methods/sensitivity-analysis.md) |
| `write-an-insight-record.md` | [Stage1 Identify the knowledge change](practices/maintain-technical-insight-knowledge.md#stage1-identify-the-knowledge-change) | Separate observations, interpretation, evidence, applicability and decisions | Record and publication orchestration remains in the Practice |
| `review-and-revise-knowledge.md` | [Stage2 Review evidence and downstream consequences](practices/maintain-technical-insight-knowledge.md#stage2-review-evidence-and-downstream-consequences) | New evidence, correction history and dependent-summary review | [Structured literature review](methods/structured-literature-review.md) |
| `map-a-technical-landscape.md` | [Stage2 Map mechanisms and competing approaches](practices/investigate-a-technical-opportunity.md#stage2-map-mechanisms-and-competing-approaches) | Comparable mechanisms, scope, family-aware counting and legal limits | [Structured literature review](methods/structured-literature-review.md), [Patent landscaping](methods/patent-landscaping.md) |
| `structure-and-prioritize-hypotheses.md` | [Stage4 Build rival explanations and a model](practices/discover-and-validate-a-technical-insight.md#stage4-build-rival-explanations-and-a-model) | Issue structure, rivals, discrimination value and consequential priorities | [Hypothesis driven analysis](methods/hypothesis-driven-analysis.md) |
| `scan-technology-signals.md` | [Stage1 Define the useful change](practices/investigate-a-technical-opportunity.md#stage1-define-the-useful-change) | Dated original signals, counter-signals, coverage and a search stopping rule | [Horizon scanning](methods/horizon-scanning.md) |
| `assess-technology-readiness.md` | [Stage2 Map mechanisms and competing approaches](practices/investigate-a-technical-opportunity.md#stage2-map-mechanisms-and-competing-approaches) | Technology and environment-specific criterion-to-evidence gaps | [Technology readiness assessment](methods/technology-readiness-assessment.md) |
| `evaluate-a-research-opportunity.md` | [Stage4 Reduce the decisive uncertainty](practices/investigate-a-technical-opportunity.md#stage4-reduce-the-decisive-uncertainty) | Need, incumbent, novelty, basis, beneficiaries, risks and falsifiable milestones | [Heilmeier Catechism](methods/heilmeier-catechism.md) |
| `explore-technical-contradictions.md` | [Stage3 Explain the proposed opportunity](practices/investigate-a-technical-opportunity.md#stage3-explain-the-proposed-opportunity) | Candidate mechanisms, resources, opposing properties and downside tests | [TRIZ contradiction analysis](methods/triz-contradiction-analysis.md), [Morphological analysis](methods/morphological-analysis.md) |
| `build-a-conditional-technology-roadmap.md` | [Stage5 Recommend a bounded next action](practices/investigate-a-technical-opportunity.md#stage5-recommend-a-bounded-next-action) | Needs, capabilities, dependencies, owners, evidence gates and fallback paths | [Technology roadmapping](methods/technology-roadmapping.md) |

## What is decisive about this change

The package contains no active generic Method files under their former names. Reusable formal techniques have explicit identities and source bases. Our engineering synthesis and record-keeping remain Practice work. Authorship alone is not a universal KPS type test; this domain deliberately adopts an established-Methods policy at this stage.

Former links and typed references are migrated to real named techniques or meaningful Practice stages. The application utility removes only the listed obsolete Method files and writes the explicit payload. It refuses an unexpected baseline or dirty working tree. Do not blindly copy the ZIP over a different branch.

## Limits of the map

A named replacement is a supporting technique, not a claim of equivalence to the whole original operation. For example, 5W2H clarifies a question but does not replace authority checking; a Pugh matrix compares alternatives but does not perform the entire decision process. Those extra responsibilities stay in the receiving Practice.

## Evidence and verification

[Source review](SOURCE-REVIEW.md) distinguishes source guidance from our application. [Checks](CHECKS.md) reports the tests actually run. No new engineering effectiveness study or GitHub merge is claimed.
