---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:patent-landscaping"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:wipo-2015-patent-landscape-guidelines", "ti:r:epo-undated-patent-families"]
method_origin: "established"
technique_kind: "analytical technique"
---

# Patent landscaping

## Key takeaway

Map patent information within an explicit technical and search scope without confusing filing activity with technical success.

## Summary

Map patent information within an explicit technical and search scope without confusing filing activity with technical success. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Patent landscaping. **Role:** analytical technique. The named technique is reused from [Guidelines for Preparing Patent Landscape Reports](../references/wipo-2015-patent-landscape-guidelines.md); [Patent families](../references/epo-undated-patent-families.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

A technical question, scope, date cutoff, selected databases, classification and keyword strategy, and the expertise to interpret the results. Legal decisions require qualified patent counsel.

## Rationale

Patent records can reveal disclosed approaches and actors, but related filings, geographic coverage and publication lag distort unqualified counts.

## Procedure

1. Define the technical boundary, countries, dates, document types and purpose; record excluded scope.
2. Search using keywords, classifications and known exemplars, iteratively inspecting false positives and missed concepts.
3. Record the query, database and search date. Distinguish priority, filing, publication and grant dates.
4. Normalize names cautiously and choose a declared family definition before counting. Retain traceability to individual records.
5. Compare disclosed mechanisms with nonpatent literature and actual performance evidence; document missing coverage, recent-publication gaps and uncertain status.

## Worked example

**Synthetic example, not a measured investigation.** Ten synthetic documents may represent two families rather than ten inventions. A listed applicant is not automatically the current rights holder. A large filing cluster can motivate source review but does not establish that its devices work.

## Working template

| Record or family | Family definition | Priority and publication | Classification or mechanism | Applicant normalization | Relevance | Legal and technical limits |
|---|---|---|---|---|---|---|
| Identifier | Database rule | Separate dates | Located disclosure | Explained mapping | Inclusion reason | Unverified questions |

## Output and validation

Deliver a reproducible search account and mechanism landscape. Spot-check family grouping, dates and relevance, and show how alternative grouping changes counts.

## Limits and optional tools

A landscape is not freedom-to-operate, infringement, patent validity, ownership or exhaustive novelty advice. Patent disclosures are claims to investigate, not certified feasibility results.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[Guidelines for Preparing Patent Landscape Reports](../references/wipo-2015-patent-landscape-guidelines.md); [Patent families](../references/epo-undated-patent-families.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
