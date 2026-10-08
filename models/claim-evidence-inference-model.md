---
id: "ti:mo:claim-evidence-inference-model"
type: "model"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_principles: ["ti:p:repeated-reports-can-share-one-evidence-base", "ti:p:reproducibility-does-not-establish-correctness"]
uses_methods: ["ti:me:synthesize-claim-relevant-sources"]
references: ["ti:r:li-2019-collecting-data-cochrane", "ti:r:w3c-2013-prov-overview"]
---

# Claim evidence and inference model

## Key takeaway

An evidence link is meaningful only with the inference and scope that connect it to a claim.

## Summary

The model keeps source material, extraction, inference and resulting knowledge distinguishable. It accommodates support, challenge, inconsistency and uncertainty rather than treating every reference as confirmation.

## Representation

```text
Source identity -> located passage or observed result
                         |
               extraction and access limits
                         |
Candidate claim <- inference plus assumptions -> rival account
      |                        |
      +------ scoped conclusion ------> possible application
```

| Record part | What it states |
|---|---|
| Claim | Exact statement, context and intended use |
| Contribution | What this source or test actually establishes |
| Family | Shared experiment, data or upstream reasoning |
| Inference | Why the contribution bears on the claim |
| Status | Supported within scope, weakened, unresolved or contradicted |
| Application | A separate decision that may depend on the claim |

## Relationships and use

Several records can contribute to one claim; a source can contribute to several claims. Contradictions can be about definitions, populations, measurement or mechanism. Separate these before synthesizing. Do not count a review and its included experiment as two replications.

## Assumptions

The extracted material is accurately located and the independence description is justified. Status words are a documentation convention, not probabilities. An inaccessible source has an access limitation even when its citation is precise.

## Limits and counterchecks

This model preserves an argument; it does not validate it automatically. A graph cycle between two knowledge objects is not independent support. Important uncertain premises remain visible in downstream Methods.

## Evidence summary

[Cochrane collecting data guidance](../references/li-2019-collecting-data-cochrane.md) [W3C provenance overview](../references/w3c-2013-prov-overview.md) supports the cited distinctions. The representation, examples and selection of fields here are authored models, not externally validated software or mandatory schemas.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Repeated reports can share one evidence base](../principles/repeated-reports-can-share-one-evidence-base.md)
- [Reproducibility does not establish correctness](../principles/reproducibility-does-not-establish-correctness.md)
- [Synthesize claim relevant sources](../methods/synthesize-claim-relevant-sources.md)

- [Cochrane collecting data guidance](../references/li-2019-collecting-data-cochrane.md)
- [W3C provenance overview](../references/w3c-2013-prov-overview.md)

[Package home](../README.md)
