---
package_version: "1.1.0"
language: "KPS 9.x"
reviewed: "2026-10-08"
---

# Method selection map

## Key takeaway

Start with the question and evidence gap then select the smallest useful investigation operation.

## Summary

Technical investigation explains behavior; technology intelligence identifies and evaluates possible technologies. This map joins them without making every framework mandatory. It links to locally usable Methods and distinguishes analytical techniques from optional software. The comprehensive expansion is being introduced in reviewable increments.

## Choose the next operation

| Question | Start with | Result and main limitation |
|---|---|---|
| What decision are we making | [Frame an insight question](methods/frame-an-insight-question.md) | Bounded outcome and comparator; not a chosen solution |
| Where should the analysis focus | [Structure and prioritize hypotheses](methods/structure-and-prioritize-hypotheses.md) | Evidence-based queue; not a proof from an issue tree |
| Is the observation trustworthy | [Audit an observation](methods/audit-an-observation.md) | Measurement and provenance limits; not a cause |
| What may be emerging | [Scan technology signals](methods/scan-technology-signals.md) | Dated leads and uncertainty; not a forecast |
| How mature is the candidate here | [Assess technology readiness](methods/assess-technology-readiness.md) | Criterion-to-evidence gaps; not a general attractiveness score |
| What approaches may solve the need | [Map a technical landscape](methods/map-a-technical-landscape.md) | Scoped candidate set; not exhaustive coverage |
| What does the literature actually support | [Synthesize claim-relevant sources](methods/synthesize-claim-relevant-sources.md) | Premises, disagreement and inference; not citation counting |
| Why might the system behave this way | [Generate competing explanations](methods/generate-competing-explanations.md) and [build an explanatory model](methods/build-an-explanatory-model.md) | Explicit mechanisms and assumptions; not established causation |
| Which explanation survives a useful check | [Design a discriminating test](methods/design-a-discriminating-test.md) then [execute a bounded test](methods/execute-a-bounded-test.md) | Located observations; only in the tested conditions |
| Could the result be an artifact | [Evaluate results and uncertainty](methods/evaluate-results-and-uncertainty.md) and [challenge an explanation](methods/challenge-and-replicate-an-explanation.md) | Qualified assessment; repeatability alone does not prove correctness |
| Is this research opportunity worth a bounded next step | [Evaluate a research opportunity](methods/evaluate-a-research-opportunity.md) | Heilmeier-inspired evidence brief; not feasibility proof |
| Can a conflict suggest other designs | [Explore technical contradictions](methods/explore-technical-contradictions.md) | TRIZ-inspired candidates; not guaranteed solutions |
| How might capabilities develop under uncertainty | [Build a conditional technology roadmap](methods/build-a-conditional-technology-roadmap.md) | Dependencies and scenario-tested gates; not a prediction |
| Which candidate should we try | [Compare technical alternatives](methods/compare-technical-alternatives.md) | Conditional decision; rankings depend on criteria and uncertainty |
| Will the insight work elsewhere | [Assess transfer](methods/assess-transfer-to-a-new-context.md) | Target-context gaps; not automatic extrapolation |
| How do we retain useful learning | [Write an insight record](methods/write-an-insight-record.md) and [review knowledge](methods/review-and-revise-knowledge.md) | Traceable current account; no invented execution |

## Two connected routes

For an unexpected behavior: bound the question -> audit the observation -> compare hypotheses -> model -> test -> qualify -> apply.

For an opportunity: establish the need -> search candidate mechanisms -> compare evidence and demonstrations -> identify a decisive uncertainty -> investigate -> choose a bounded next action.

Cross between routes whenever needed. A search finds leads; an experiment can expose an omitted alternative. Neither is a replacement for the other.

## Techniques and tools are different

Issue trees and Five Whys can prompt questions, but a linear causal story is not evidence and several interacting causes may remain. A causal diagram represents assumptions. Experiments and simulation interrogate predictions under explicit validity limits. These supporting techniques fit the linked Methods; they are not extra KPS types.

Markdown and ordinary tables are the default. A spreadsheet, Python or a notebook is optional when calculations need reproducibility. An AI assistant can draft search terms, alternatives or summaries, but never supplies verified citations or measured results merely by generating text. Instruments and specialist simulators require applicable calibration, authority and domain expertise; no generic software list makes them interchangeable.

## Expansion boundary

The method library now covers structured hypotheses, scanning, landscapes, readiness, DARPA-inspired opportunity evaluation, TRIZ-inspired contradictions and conditional roadmapping. The next integration increment connects these operations into complete staged Practices and a worked route. There is no new software platform or mandatory tool subscription.

## Deeper knowledge

[Routing model](models/investigation-and-intelligence-routing-model.md) explains the selection logic. [Discover and validate an insight](practices/discover-and-validate-a-technical-insight.md) and [investigate an opportunity](practices/investigate-a-technical-opportunity.md) apply the existing workflow. [Boundaries](BOUNDARIES.md) retains authority, safety and confidentiality limits.
