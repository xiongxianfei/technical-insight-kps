---
package_version: "2.0.0"
language: "KPS 9.x"
reviewed: "2026-10-08"
---

# Publication checks

## Key takeaway

Structural validation and synthetic examples passed locally; no remote publication or field effectiveness is claimed.

## Summary

The complete transition was checked for KPS structure, links, typed references, migration coverage and deterministic arithmetic. The package contains 64 core objects and 30 Reference records, including 22 established Methods and five integrated Practices. These checks do not establish that a Method is appropriate in every context.

## Commands and results

| Check | Result |
|---|---|
| Shared validator regression suite | 31 of 31 passed |
| Retained synthetic example suite | 9 of 9 passed |
| Complete transition and technique examples | 16 of 16 passed |
| Local Markdown structure and typed relationships | Passed |
| Local Pandoc GFM heading comparison | Passed for all checked documents |
| Archive extraction and payload checksums | Passed in a fresh directory |

Run `python3 validate.py . --manifest`, `python3 test_validate.py`, `python3 test_examples.py` and `python3 test_transition.py`. The shared validator and its manifest exclusion behavior were retained, not weakened.

## What the transition tests cover

The tests check all 20 retired Method paths are absent, their receiving Practice stages exist, all 22 replacement techniques have named-source and local-procedure fields, old Method identities are absent from active metadata and all new Methods are used by a Practice. They check radar normalization, missing data, unclipped out-of-range values, changing area under axis reorder, weighted preference reversal, a factorial difference of effects, uncertainty arithmetic and the retained intelligence scope. Checking fields is not an assessment of the sources' scientific adequacy.

## Review of content and dependencies

The Method distinction, source roles, synthetic examples, constraints and receiving stages were reviewed before the dependency snapshot was regenerated. Original knowledge explanations were retained where relevant and links were migrated to actual techniques or meaningful Practice stages. The filename responsibility map is in MIGRATION.md. This is authored review, not independent peer or user validation.

## Important limits

No real engineering experiment, medical or legal clearance, professional certification or independent effectiveness trial occurred. The checks above are local results; the actual GitHub Actions conclusion must be inspected on the corresponding publication PR before merging. A local simulation is not a test of all Markdown renderers. Previously inspected References retain their access limits; not every historical source was newly reviewed in full.
