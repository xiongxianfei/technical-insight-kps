---
language: "KPS 9.x"
reviewed: "2026-10-08"
package_version: "2.0.0"
---

# Method selection map

## Key takeaway

Select a named technique by the output you need, then use a Practice to combine it with evidence and decisions.

## Summary

This library contains 22 established techniques, not 22 newly invented engineering workflows. The scope still covers both technical investigation and technology intelligence. A questioning tool, visualization, experiment and decision framework produce different kinds of outputs.

## Select the next technique

| Task | Established technique | Useful output and boundary |
|---|---|---|
| Frame and structure | [5W2H](methods/5w2h.md) | Clarify a situation through seven concrete questions before choosing an explanation or solution. |
| Frame and structure | [SIPOC](methods/sipoc.md) | Expose the boundary and handoffs of a process before investigating detailed mechanisms. |
| Frame and structure | [Hypothesis driven analysis](methods/hypothesis-driven-analysis.md) | Organize a decision into testable questions and prioritize evidence that could change the conclusion. |
| Explore causes and risks | [Five Whys](methods/five-whys.md) | Develop candidate causal chains by repeatedly questioning the explanation of an observed problem. |
| Explore causes and risks | [Fishbone analysis](methods/fishbone-analysis.md) | Organize possible causes of one effect without treating the diagram as a diagnosis. |
| Explore causes and risks | [Failure mode and effects analysis](methods/fmea.md) | Anticipate how an item or process can fail and connect consequences to prevention and detection actions. |
| Explore causes and risks | [Pareto analysis](methods/pareto-analysis.md) | Locate the largest contributors to one defined aggregate measure. |
| Compare and communicate | [Pugh matrix](methods/pugh-matrix.md) | Compare candidate concepts against a named datum using criterion-specific relative judgments. |
| Compare and communicate | [Weighted decision matrix](methods/weighted-decision-matrix.md) | Make preference tradeoffs explicit while keeping technical evidence and uncertainty separate. |
| Compare and communicate | [Radar chart](methods/radar-chart.md) | Display a small set of comparable multiattribute profiles without interpreting polygon area as an overall score. |
| Test and quantify uncertainty | [Design of experiments](methods/design-of-experiments.md) | Plan controlled comparisons that can estimate effects and interactions at an appropriate experimental unit. |
| Test and quantify uncertainty | [Statistical hypothesis testing](methods/statistical-hypothesis-testing.md) | Evaluate a statistical contrast under explicit sampling and model assumptions. |
| Test and quantify uncertainty | [Measurement uncertainty budget](methods/measurement-uncertainty-budget.md) | Identify and combine the uncertainty contributions relevant to a reported measurement. |
| Test and quantify uncertainty | [Sensitivity analysis](methods/sensitivity-analysis.md) | Determine which uncertain inputs or preferences can change a model result or decision. |
| Find and assess technologies | [Structured literature review](methods/structured-literature-review.md) | Build a traceable evidence table around a defined question rather than collect supportive citations. |
| Find and assess technologies | [Horizon scanning](methods/horizon-scanning.md) | Collect and interpret dated signals of possible change relevant to a defined decision horizon. |
| Find and assess technologies | [Patent landscaping](methods/patent-landscaping.md) | Map patent information within an explicit technical and search scope without confusing filing activity with technical success. |
| Find and assess technologies | [Technology readiness assessment](methods/technology-readiness-assessment.md) | Assess demonstrated technology maturity against a named framework and intended use. |
| Create and plan opportunities | [Heilmeier Catechism](methods/heilmeier-catechism.md) | Challenge a research proposal through its objective, novelty, benefit, risk, resources and demonstrable milestones. |
| Create and plan opportunities | [TRIZ contradiction analysis](methods/triz-contradiction-analysis.md) | Use explicitly stated contradictions to generate candidate design directions before engineering validation. |
| Create and plan opportunities | [Morphological analysis](methods/morphological-analysis.md) | Explore combinations of functionally distinct options and eliminate inconsistent configurations. |
| Create and plan opportunities | [Technology roadmapping](methods/technology-roadmapping.md) | Connect needs, capabilities and technological resources over time through conditional milestones. |

## Start with a small route

For an unclear fault: **5W2H -> Fishbone or Five Whys -> a suitable experiment -> uncertainty-aware conclusion**. Use SIPOC when boundaries matter and FMEA when failure consequences matter. Do not add every technique to every investigation.

For an emerging opportunity: **Horizon Scanning -> literature and patent evidence -> contextual readiness -> Heilmeier review -> conditional roadmap**. Use TRIZ or Morphological Analysis only when alternative concepts are needed. Use Pugh or weighted scoring for a decision; a radar chart is optional communication, never proof by area.

## What remains our own work

The choice of technique, sequence, handoff, stopping decision, model construction and insight record are combined in [Investigation](practices/discover-and-validate-a-technical-insight.md), [Technology opportunities](practices/investigate-a-technical-opportunity.md), [Claim review](practices/assess-a-technical-claim.md), [Transfer](practices/apply-and-transfer-an-insight.md) and [Knowledge maintenance](practices/maintain-technical-insight-knowledge.md).

## Inputs before tools

Before selecting software, identify the question, required evidence, output and limits. Paper or Markdown is the default. Calculation packages and instruments are optional means with their own competence and calibration requirements. No dedicated KPS software is required.

## Limits and provenance

Named and well-known does not mean universally valid. Some entries are families with a bounded introductory variant, such as DOE and statistical testing; public guidance is not a complete specialist standard. Every Method identifies its inspected basis and where our worksheet or example adds application detail. [Migration](MIGRATION.md) records the complete replacement of the 20 generic operations. [Worked example](INTEGRATED-EXAMPLE.md) shows the distinction in use.
