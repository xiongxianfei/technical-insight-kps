---
package_version: "1.0.0"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Publication checks

## Key takeaway

Structural integrity and checked example arithmetic are not evidence of field effectiveness.

## Summary

Technical Insight KPS 1.0.0 was checked locally on 7 October 2026. The core validator and 31 regression tests are copied byte-for-byte from KPS Core commit 60972c57199ae8bc21d4b7a00ac55552b4105277. Nine additional tests check synthetic examples. The initial release was checked locally before GitHub publication. GitHub pull-request CI must run independently and is reported by GitHub rather than claimed by this record.

## Completed local checks

| Check | Result |
|---|---:|
| Core knowledge objects | 51 |
| Reference records | 11 |
| Markdown documents | 79 |
| Local links and fragments | 586 |
| Typed relationships | 236 |
| Practice stages | 27 |
| Rendered heading identifiers | 713 |
| Core regression tests | 31 of 31 passed |
| Synthetic example tests | 9 of 9 passed |
| Payload files with checksums | 88 |

The regression suite includes deliberate broken destinations, invented fragments, duplicate identities, imperative Principle titles, missing rationale, link-only stages, circular composition and changed dependency hashes. Manifest tests include altered or unlisted content and Git/cache exclusions.

The suite also passed after copying the package to a fresh local Git checkout. This reproduces the relevant presence of Git metadata without changing a remote repository. The synthetic tests verify the manifest set counterexample, thermal values/limits/energy balance and process-interaction arithmetic. They are not physical experiments.

## Rendering and extraction

All Markdown files were rendered locally with Pandoc using the GFM reader plus YAML metadata support. Every heading identifier was compared with the selected profile. MarkdownIt independently extracted link destinations. No actual GitHub website, MkDocs deployment or desktop editor was used for a click test.

The ZIP was extracted into a fresh directory, its payload checksums verified, and publication validation and both test suites rerun. Archive integrity is distinct from factual validity. The outer SHA256 file identifies the delivered archive.

## Content review

The authored review checked the separation of observation, source finding, inference, test plan, synthetic calculation and decision. Each Principle states an explanatory relationship. Methods contain prerequisites, local rationale, procedure and counterevidence. Each Practice stage contains operational content and a fallback without requiring every linked document.

This was not an independent expert review or a reader-comprehension trial. The framework is populated and structurally tested; its practical effectiveness remains unmeasured. Selected source sections are recorded accurately in Reference files rather than presented as exhaustive literature coverage.

## Tooling provenance

Git blob identities verified against the connected KPS Core commit:

- AUTHORING.md: d5890f789418d4ecf21917add2a9a8915be28d06, inspected externally and not duplicated as a competing domain specification.
- validate.py: b9f853f0b6c62d1c9b50839dc45324badc885f73.
- test_validate.py: de1cd80c477fc71cd69c1863378fd2767ec687f8.
- LICENSE: f2069d6cff77823390bd06ee0513c324db216050.

Local example code is authored for this package. The included GitHub workflow uses a pinned checkout action and read-only permissions; it has not executed remotely for this domain.

## Limits

No test here certifies scientific truth, professional competence, experimental safety, novelty, legal authority, model applicability to a real product or standards conformance. A successful self-contained-file check cannot establish that a reader will correctly apply the knowledge. Blank records do not document actual investigations.

## Reproduce the checks

```bash
python3 validate.py .
python3 test_validate.py
python3 test_examples.py
python3 validate.py . --manifest
```

After deliberate edits, the released manifest may no longer match. Review the changes and update dependencies and the publication manifest through the documented publication process; do not disable checksum coverage or blindly refresh reviewed summaries to silence failures.
