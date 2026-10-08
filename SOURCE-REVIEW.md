---
package_version: "1.0.0"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Source review

## Key takeaway

Source access and evidence independence are recorded explicitly rather than inferred from a citation.

## Summary

Review date: 7 October 2026. The sources below were selected for specific engineering-method claims. This is a claim-driven desk review, not a systematic or exhaustive survey of engineering science. Where only selected sections were read, the record says so.

## Inspected sources

| Record | Evidence role | Inspected extent |
|---|---|---|
| [Causal inference in statistics An overview](references/pearl-2009-causal-inference-in-statistics.md) | Theory of causal reasoning | Selected full-text PDF sections: abstract, Sections 2.1 through 2.4 and 3.1 through 3.2; page 99 visually inspected. Not a full review of all 51 pages. |
| [NIST experimental design guidance](references/nist-undated-experimental-design-handbook.md) | Experimental design guidance | Selected official HTML sections inspected: design selection, randomized block designs, two-level full factorial designs and DOE glossary. |
| [NIST essentials of measurement uncertainty](references/nist-undated-measurement-uncertainty.md) | Measurement concepts and evaluation basis | Basic definitions page inspected in full: measurement equation, input quantities, uncertainty components and Type A/Type B evaluation. |
| [NIST model fit and residual analysis](references/nist-undated-model-fit-and-residuals.md) | Model evaluation guidance | Selected HTML prose inspected: R squared limitations, residual definition and interpretation. The example dataset was not reused. |
| [NASA standard for models and simulations](references/nasa-7009b-2024-models-and-simulations.md) | Model credibility and scope guidance | Selected PDF sections inspected: definitions, 4.1.1, 4.2.1 and 4.2.3 through 4.2.7; PDF page 29 visually inspected. No claim of full clause-level conformance. |
| [NASA decision analysis guidance](references/nasa-undated-decision-analysis.md) | Decision reasoning and stopping guidance | Selected official HTML text inspected: 6.8.1, inputs, defining criteria, alternatives and discussion of reducing decision-relevant uncertainty. |
| [Reproducible computational research](references/sandve-2013-reproducible-computational-research.md) | Reproducible analysis and reporting guidance | Publisher HTML inspected, especially Rules 1–3 and 9–10, introduction and publication metadata. |
| [W3C provenance overview](references/w3c-2013-prov-overview.md) | Provenance vocabulary | Dated overview inspected: abstract, document status, introduction and document roadmap. |
| [Cochrane collecting data guidance](references/li-2019-collecting-data-cochrane.md) | Source synthesis and scope guidance | Chapter citation, key points, 5.2.1, 5.3.3 and 5.3.4.1 inspected; no comprehensive review of all chapters. |
| [OpenStax heat capacity and heat transfer](references/openstax-2016-university-physics-heat-transfer.md) | Physical basis for the illustrative thermal example | Selected HTML prose and equations inspected: heat capacity, temperature change and mechanisms of heat transfer. No textbook tables copied. |
| [KPS authoring contract](references/kps-undated-authoring-contract-9x.md) | Authoring compatibility authority | Full AUTHORING.md read through connected GitHub; matching local bytes verified by Git blob hash. Validator and regression tests inspected at the same commit. |

## Source selection and limits

Pearl supplies causal-inference theory; NIST supplies metrology and experimental/model-assessment guidance; NASA supplies model-credibility and decision-analysis guidance. Sandve and W3C contribute reproducibility/provenance distinctions; Cochrane contributes source-family and extraction concepts adapted from healthcare reviews. OpenStax supports the physics premises of a synthetic example.

The two NIST handbook records share one evidence family. Several pages or NASA sections are not independent field replications. KPS Core is authoring authority, not evidence of effectiveness. No source directly evaluates this complete package.

## Access fidelity

Selected primary PDFs were inspected as text and selected pages visually checked. Only Markdown bibliographic/contribution records are distributed. No full publications, external diagrams or original datasets are reproduced.

The local examples and workflow steps are authored and labelled as such. Source support does not automatically validate an implementation, quantify a probability or establish applicability to a hazardous target.
