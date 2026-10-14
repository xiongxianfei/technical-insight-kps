---
package_version: "2.0.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
---

# Agent guidance

## Key takeaway

Apply the shared Core Engineering Principles together with this repository's authoring, evidence and contribution boundaries.

## Summary

These repository-wide instructions apply to knowledge, code, tools and workflows. The nine Core Engineering Principles are maintained verbatim across the six knowledge repositories; propose shared revisions together and keep domain-specific instructions below. Each repository carries its own copy for independent use. These are working agreements, not scientific KPS Principle objects or a replacement for the authoring contract.

## Project purpose

Help readers investigate technical questions, understand mechanisms and apply established techniques to bounded engineering decisions. Use the [starting guide](guides/START-HERE.md), [knowledge index](docs/INDEX.md) and [Method map](guides/METHOD-MAP.md) to locate relevant explanations and Practices.

## Core Engineering Principles

1. **Self-contained knowledge.** Make each substantive document understandable on its own: explain the problem, essential terms, prerequisites, mechanisms, examples, and boundaries. Link to deeper material without requiring readers to follow links to understand the core argument. Keep canonical definitions in one place; avoid needless duplication.

2. **Reader-centered quality.** Evaluate whether a reader can explain *what happens, how, why, and when*; apply the knowledge to a realistic problem; predict likely outcomes and failure modes; and recognize opportunities to improve results. Correctness and clear reasoning matter more than polished prose.

3. **Goal-oriented work.** Identify the intended reader outcome before substantial work. Choose the smallest sufficient change; prioritize important knowledge gaps and useful results. Avoid speculative infrastructure, redundant research, unnecessary documentation, and rituals that do not advance the goal. Do not skip essential verification to save effort.

4. **Reuse before invention.** Look for established theory, standards, sources, methods, libraries, and tools before building alternatives. Prefer suitable, proven approaches; weigh fitness, reliability, cost, maintenance, and lock-in. Create custom solutions only when a material requirement justifies them.

5. **Mechanisms before memorization.** Explain causal relationships, relevant variables, assumptions, boundary conditions, and trade-offs. Show how the mechanism informs decisions and practical action. Surface possible improvements and testable hypotheses, clearly separating proposed innovations from demonstrated results.

6. **Delete obsolete internal compatibility.** When replacing internal code, paths, workflows, or knowledge structures, migrate affected uses and remove superseded implementations. Do not add internal legacy shims, deprecated aliases, dual-write logic, or competing canonical documents. Assess *external* contracts separately and honor actual obligations. Preserve unique evidence, provenance, and historically useful knowledge; remove obsolete representations, not valuable facts.

7. **Fix the problem class.** For defects or inconsistencies, identify the underlying cause and check for related instances. Make the smallest coherent change that addresses the confirmed class; add proportionate checks or regression coverage where useful. Do not turn isolated issues into speculative redesigns.

8. **Think before acting.** Before substantive work, clarify the intended outcome, inspect relevant context, challenge important assumptions, and consider dependencies, risks, and the simplest sound approach. Scale planning to the task: small, reversible changes need no formal plan; consequential or hard-to-reverse changes deserve more analysis. Avoid analysis that does not improve the decision.

9. **Test the core first; validate by risk.** First verify the main outcome: for software, the changed behavior; for knowledge, whether a reader can use it to reason through a representative problem. Expand to affected dependencies, contracts, edge cases, or regressions when the likelihood and impact of failure justify it. Prefer focused checks over redundant tests or unrelated full suites; never omit essential verification merely to save time.

## Project guidance

- Follow [Authoring](docs/AUTHORING.md) and its pinned Core contract. Technical insight is a domain and a kind of synthesis, not a sixth KPS role. Principles explain relationships rather than prescribing designs.
- Keep substantive documents locally sufficient, with a meaningful takeaway, summary, explanation or procedure, and limits. Preserve this domain's `StageN` format, inline procedures, observations and fallbacks; links cannot replace essential safety or rationale.
- Admit independently documented Methods only for established techniques with inspected source support. Keep original selection, sequencing, evidence handling, model-building and publication workflows in Practices. Consult [Method migration](docs/METHOD-MIGRATION.md) before reintroducing an overlapping wrapper.
- Preserve source identity, passage locators, access extent, independence and disagreement. Label inferences and synthetic examples. Do not invent experiments, measured outcomes, permissions, checks or source access. Visualization and questioning do not establish superiority or causation.
- Keep confidential investigations, personal data, secrets and restricted source documents outside this public repository. Retain the limits in [Boundaries](guides/BOUNDARIES.md). Update links and dependencies when refactoring, accounting for the retired responsibility.

## Verification

Run from the repository root as described in [Maintenance](docs/MAINTENANCE.md):

```bash
python3 validate.py .
python3 -m unittest discover -s tests -v
```

These cover package structure, the pinned checker, Method declarations and synthetic examples. Preserve manifest-payload exclusions and archive integrity checks; use them when packaging an archive. Review changed source meaning and receiving summaries before accepting new fingerprints. Report actual checks and limits; structural and arithmetic checks are not scientific validation.

## Contribution workflow

Follow [Contributing](.github/CONTRIBUTING.md) and [Publishing](docs/PUBLISHING.md). Read the actual repository and use one branch and one PR to `main` for a coherent change. Honor the owner's existing authorization for requested knowledge publications after required checks, without adding a second approval ceremony; do not extend it to unrelated work, tags or official releases. Report a merge only after observing it. Preserve unrelated work, protections and LF text under `.gitattributes`; never disable checks to publish. If remote writing is unavailable, deliver the checked work and state the limit; do not claim a remote change or repurpose an unrelated repository.
