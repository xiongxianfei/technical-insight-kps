---
language: "KPS 9.x"
reviewed: "2026-10-08"
package_version: "2.0.0"
---

# Apply and publish the refactor

## Key takeaway

Apply the complete transition to the inspected baseline without overwriting unrelated work.

## Summary

This source package was validated against an inspected GitHub baseline. Publication uses one pull request directly against `main` and the maintainer-authorized automatic merge after GitHub checks pass. The actual merge and CI results must be verified on GitHub; this document does not assert them in advance.

## Repository baseline

Repository: `xiongxianfei/technical-insight-kps`. Inspected main commit: `85a92fdd39453a0de670cbfeadea85f237acc749`. The complete refactor retires the 20 exact Method filenames in [MIGRATION](MIGRATION.md) and writes the supplied 2.0.0 files. It does not delete private records or external directories.

## Guarded application

The separately supplied `apply_technical_insight_refactor.py` previews changes by default. With its explicit apply option, it requires a clean main checkout at the inspected commit, creates a new local branch and applies the explicit payload and removals. It checks archive checksums, rejects path traversal and symlink members, preserves the existing MIT license, and runs the package checks. It does not fetch credentials, push, merge or bypass protections.

Do not overlay the ZIP onto a different base without reviewing the changes. Old external links need the mapping in MIGRATION; Git history retains their former definitions.

## Validation

Run `python3 validate.py . --manifest`, `python3 test_validate.py`, `python3 test_examples.py` and `python3 test_transition.py` from the package root. A dependency refresh means relevant summaries were reviewed, not that evidence became true.

## Publication policy

For user-authorized knowledge changes, use one PR directly to main. Merge after required checks without an extra approval ceremony, while respecting actual repository permissions and protections. Do not create official release tags unless requested. Report only observed remote actions and results. GitHub records the work; it is not an additional knowledge type or validation of scientific truth.
