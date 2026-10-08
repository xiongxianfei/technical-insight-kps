---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:structured-literature-review"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:li-2019-collecting-data-cochrane", "ti:r:w3c-2013-prov-overview"]
method_origin: "established"
technique_kind: "analytical technique"
---

# Structured literature review

## Key takeaway

Build a traceable evidence table around a defined question rather than collect supportive citations.

## Summary

Build a traceable evidence table around a defined question rather than collect supportive citations. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Structured literature review. **Role:** analytical technique. The named technique is reused from [Source record](../references/li-2019-collecting-data-cochrane.md); [Source record](../references/w3c-2013-prov-overview.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

A bounded question, inclusion/exclusion criteria, accessible search sources and a plan for locating claims. A full systematic review requires further design and domain-specific standards.

## Rationale

Publication identity and evidence identity differ. A structured extraction distinguishes what a source establishes from our inference and from repeated reports of the same work.

## Procedure

1. Define question, scope, search sources, terms and selection criteria before choosing favorable papers.
2. Record searches, dates and coverage limits, then retain inclusion/exclusion reasons for relevant candidates.
3. Identify underlying studies or evidence families; several reports of one experiment are not independent confirmation.
4. Extract the exact claim, method, context, evidence, uncertainty and contrary findings with a locator and access extent.
5. Synthesize agreement and disagreement by claim. Separate quoted or paraphrased premises from your inference and unresolved gaps.

## Worked example

**Synthetic example, not a measured investigation.** Three articles repeat one prototype demonstration while a fourth reports a different environmental test. The evidence table has two families, not four independent demonstrations. An abstract-only report cannot support details absent from its abstract.

## Working template

| Question or claim | Source and locator | Underlying study | Design and context | Finding | Limits or challenge | Our inference |
|---|---|---|---|---|---|---|
| Exact statement | Publication | Evidence family | Inspected method | Supported contribution | Boundary | Clearly labeled |

## Output and validation

Deliver a source-search log and claim-evidence matrix. Another reader should be able to distinguish missing evidence from negative evidence and source findings from interpretation.

## Limits and optional tools

This is a bounded structured review, not automatically a systematic review, meta-analysis or exhaustive novelty search. Cochrane guidance supplies study/report and extraction distinctions; medical evidence hierarchies are not blindly imposed on every engineering question.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[Source record](../references/li-2019-collecting-data-cochrane.md); [Source record](../references/w3c-2013-prov-overview.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
