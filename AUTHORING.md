---
package_version: "1.0.0"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Authoring authority

## Key takeaway

The pinned KPS Core contract is authoritative; this domain applies it without redefining it.

## Summary

Technical Insight KPS follows KPS 9.x and the practical Markdown profile. This file is a local implementation guide, not a competing standard. The full contract remains in KPS Core; reading and ordinary use of this package do not require its files to be installed.

## Canonical contract

[KPS Authoring Contract](https://github.com/xiongxianfei/knowledge-practice-system/blob/60972c57199ae8bc21d4b7a00ac55552b4105277/AUTHORING.md), commit `60972c57199ae8bc21d4b7a00ac55552b4105277`, package version 9.0.1. This record pins what was inspected instead of silently following a changing branch.

## Local conventions

Core folders are `concepts/`, `principles/`, `models/`, `methods/`, `practices/`. References identify external publications in `references/`. Use semantic lowercase kebab-case filenames, stable IDs in metadata and readable titles. Principles describe relationships; prescribed choices belong downstream.

Each substantive Markdown file includes a Key takeaway, Summary, necessary local definitions/reasoning, representation or procedure, limits and deeper links. A link is not a substitute for the local explanation.

Practice headings use `## Stage1 Meaningful stage name`, consecutively in recommended order. Prerequisites define actual dependencies. Each stage supplies Goal, Why, What to do, What to observe, Success signal and Next with an inline procedure. Repeated labels are bold prose rather than duplicate headings.

## Navigation example

```markdown
[Stage1 Bound the question](#stage1-bound-the-question)

## Stage1 Bound the question
```

The whole real heading determines the fragment. Metadata IDs and opaque prefixes do not create anchors. Headings use simple ASCII words for the selected parser profile. Relative file links stay inside the package. No wikilinks, custom HTML anchors or separate application editions are required.

## Review

Run the checks documented in README. Hide links and try the intended reading task, then inspect sources to check faithful compression. Structural checks cannot evaluate engineering truth or replace human review. Only refresh `summary-dependencies.json` after examining changed source meaning.
