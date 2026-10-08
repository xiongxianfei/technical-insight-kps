---
language: "KPS 9.x"
reviewed: "2026-10-08"
package_version: "2.0.0"
---

# Technical Insight KPS

## Key takeaway

Use established techniques and evidence to develop technical understanding and qualified technology decisions.

## Summary

Technical Insight KPS 2.0.0 is a Markdown knowledge system for technical investigation and technology intelligence. Established Methods provide concrete techniques; our Practices combine them into end-to-end work. This breaking refactor replaces the complete generic Method layer instead of retaining parallel libraries.

## Start here

Open [METHOD MAP](METHOD-MAP.md) to choose a familiar technique. Start with [5W2H](methods/5w2h.md) for a vague question or [Radar chart](methods/radar-chart.md) for a carefully bounded profile visualization. For end-to-end execution use [Investigation](practices/discover-and-validate-a-technical-insight.md) or [Technology opportunity](practices/investigate-a-technical-opportunity.md).

## What changed

All 20 former generic Method paths are retired. Their framing, evidence handling, modeling, testing, documentation and revision responsibilities now have explicit homes in the five Practices. The Method library contains 22 established techniques with procedures, worksheets, synthetic examples, output checks and limits. [MIGRATION](MIGRATION.md) maps every former operation; Git history remains the historical source, not active compatibility stubs.

## Knowledge structure

| Type | Count | Purpose |
|---|---|---|
| Concepts | 15 | Define useful distinctions |
| Principles | 12 | Explain scoped relationships rather than prescribe commands |
| Models | 10 | Represent mechanisms, evidence, boundaries and decisions |
| Methods | 22 | Reuse established analytical techniques and visualizations |
| Practices | 5 | Combine knowledge for real work |
| Reference records | 30 | Preserve external contribution and access limits |

References are supporting infrastructure. The 64 core objects remain self-contained at their own level. [INDEX](INDEX.md) provides all files and [WHY MAP](WHY-MAP.md) connects operations to reasoning.

## Compatibility and use

Compatible with KPS 9.x and the practical Markdown profile; inspected core release 9.0.1. Numbered Stage1 headings indicate recommended order, not permission to skip prerequisites. The core authoring contract remains authoritative. See [AUTHORING](AUTHORING.md) and [COMPATIBILITY](COMPATIBILITY.md).

## Safety and evidence

No real investigation, field result, personal experience or independent effectiveness trial is invented. Source recommendations, proposed tests, actual results and design choices remain separate. Read [BOUNDARIES](BOUNDARIES.md) before acting on a live or hazardous system. Public patent information is not legal clearance. Third-party publications keep their own rights.

## Checks and publication status

Use `python3 validate.py . --manifest`, `python3 test_validate.py`, `python3 test_examples.py` and `python3 test_transition.py`. These check structure, migration and synthetic calculations, not truth or safety. See [CHECKS](CHECKS.md).

This locally prepared release has not been pushed or merged in GitHub during this session. The current connector offers read operations only. Its [application guide](PUBLISHING.md) explains the guarded repository change; no branch protection or credentials are bypassed.
