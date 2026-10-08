---
package_version: "1.0.0"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Publishing this domain

## Key takeaway

Publish this domain as an independently versioned public repository through ready-for-review pull requests. Preserve existing repository files and run the included checks on the proposed branch.

## Summary

The repository is [technical-insight-kps](https://github.com/xiongxianfei/technical-insight-kps). The separate daily security-insight project has a different scope and remains untouched. The initial proposed version is 1.0.0, compatible with KPS 9.x; merging and an official GitHub Release are maintainer decisions.

## Review and publication workflow

Inspect the repository and default branch first. Preserve the existing license and unrelated files. Prepare a scoped publication branch, run local validation, and open a ready-for-review PR with results and limitations. Merge, tag and create an official release only with maintainer approval. For a domain without an accessible repository, distribute a verified ZIP instead. Do not include private investigation records or raw third-party publications.

## Continuous integration

The included workflow checks publication structure and runs core regression and synthetic-example tests. It uses read-only repository permissions and pins actions/checkout v6.0.3 to commit `df4cb1c069e1874edd31b4311f1884172cec0e10`, resolved from the official action tag on 2026-10-07. The workflow is configured to run on pull requests and main-branch updates; GitHub reports the actual CI result.

A checked-in archive manifest describes that exact release. It should be regenerated for a new publication after review, not used as an immutable expectation across arbitrary repository edits. The regression suite exercises manifest protection in temporary fixtures.

## Licensing and attribution

The included MIT notice is retained for reused KPS tooling. Linked publications remain third-party works and are not relicensed by this package. Review [Third party notices](THIRD-PARTY-NOTICES.md) before publication. No source PDFs or large excerpts are bundled.
