---
id: "ti:me:map-a-technical-landscape"
type: "method"
version: "1.1.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-08"
basis_kind: "authored cross-source landscape synthesis"
uses_concepts: ["ti:c:technology-intelligence"]
uses_models: ["ti:mo:readiness-evidence-model"]
references: ["ti:r:epo-undated-patent-families", "ti:r:wipo-2015-patent-landscape-guidelines", "ti:r:li-2019-collecting-data-cochrane"]
---

# Map a technical landscape

## Key takeaway

Compare mechanisms and evidence under a recorded search scope rather than ranking technology names by attention.

## Summary

A landscape is a dated map of approaches relevant to a functional need. This Method combines literature discovery, patent-family awareness and comparable technical benchmarks. It produces an inspectable shortlist and evidence gaps, not a universal ranking, patent legal opinion or proof that the search was exhaustive.

## Inputs and prerequisites

A need, baseline, comparison criteria, time horizon and permissible sources. Identify hard constraints and the target operating environment. Distinguish an open technical question from a legal question that requires a qualified professional.

## Rationale

A technology label can conceal different mechanisms; publication volume can conceal repeated reports. Comparing results without their workload, scale or measurement method can reward incompatible demonstrations. The useful unit is an approach plus its evidence and applicability, not merely its citation or patent count.

## Procedure

1. Define inclusion and exclusion criteria before shortlisting: required function, target conditions, date range, languages and minimum evidence to assess a claim. Record unresolved criteria rather than adjusting them to favor a candidate.
2. Search scholarly sources with synonyms and functional terms. Follow relevant cited and citing work, including negative or limiting findings. Log service, exact query, filters, date and screening reason. Inspect the original study to the extent available.
3. Search patent sources separately when they may reveal mechanisms, applicants or development directions. Record document identifier, priority information, publication date, applicant as listed and source. Group families using a stated definition; do not silently mix DOCDB simple and INPADOC extended families.
4. Deduplicate records and identify shared experiments, datasets, patents or announcements. Author-network and activity maps show the recorded corpus, not automatically independent expertise or capability.
5. Create one row per candidate mechanism: function, physical/technical basis, measured claim, comparator, configuration, environment, uncertainty, maturity evidence, integration dependencies and missing information.
6. Normalize only genuinely comparable metrics. State units, load, scale, test boundary and whether a value is measured, simulated, asserted or estimated. Mark incompatible results as not directly comparable instead of forcing a score.
7. Compare the shortlist against the baseline and a plausible alternative. Search for a finding that would undermine each leading choice. State omissions and conflicting results.
8. Choose the next investigation: source clarification, demonstration evidence, mechanism test, partner conversation with permission, or deferral. Preserve why a candidate was excluded.

## Output and validation

A reproducible search log, source-family table and qualified candidate map. Check a sample of included and excluded records against the criteria. If deduplication, a changed family definition or a reasonable criterion changes the leading option, report that sensitivity. Counts are descriptive only unless their measurement and inference are justified.

## Example

Passive heat storage, improved heat rejection and active cooling may all reduce a temperature at some time. The landscape separates transient measurements from sustained operation, includes the extra mass or power boundary and identifies which target-condition demonstration is missing. This is illustrative, not an observed market survey.

## Optional tools

A browser and table are enough. OpenAlex or Crossref may help discover publication records; Espacenet or PATENTSCOPE may help locate patents. Their records are leads to inspect, not independent confirmation. Specialized analysis is optional; no APIs or integrations are required here.

## Limits and evidence

Patent publication and indexing gaps, undisclosed experiments, language and query choices constrain the map. No result here establishes patent validity, ownership, patentability or freedom to operate. Refer such decisions for professional legal assessment.

[EPO family guidance](../references/epo-undated-patent-families.md) establishes that family definitions differ. [WIPO's publication description](../references/wipo-2015-patent-landscape-guidelines.md) identifies objectives and analysis frameworks; its full report was not inspected. [Cochrane data collection](../references/li-2019-collecting-data-cochrane.md) supports separating reports from underlying studies. The integrated landscape procedure is authored synthesis, not a complete official WIPO or Cochrane review method.

## Deeper knowledge

[Scan technology signals](scan-technology-signals.md), [readiness evidence model](../models/readiness-evidence-model.md), and [compare technical alternatives](compare-technical-alternatives.md).
