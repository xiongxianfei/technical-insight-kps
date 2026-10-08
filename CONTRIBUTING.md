---
package_version: "2.0.0"
language: "KPS 9.x"
reviewed: "2026-10-08"
---

# Contributing

## Key takeaway

Contribute a specific correction with evidence and reasoning rather than an unqualified technical tip.

## Summary

This publication is prepared for a future public repository. Contributions should preserve the five KPS roles, source attribution, safety boundaries and locally complete explanations. No corresponding repository has been created by this task.

## A useful contribution

State the exact claim or operation affected, the new evidence, inspected source locations, applicability and remaining uncertainty. Distinguish source findings from your inference. A personal success story can motivate a hypothesis but does not automatically establish a general Principle.

## Authoring and review

Follow [Authoring authority](AUTHORING.md). Keep Principles declarative, Methods executable and Practice stages self-contained. Use actual semantic headings and update incoming fragments when stages change. Run the structural tests and inspect changed summaries before refreshing dependencies.

## Code and checks

Run `python3 validate.py .`, `python3 test_validate.py` and `python3 test_examples.py`. Tests do not certify scientific accuracy. Include a failing test for a checker defect when possible and retain protection against changed or unexpected payload files.

## Evidence safety and privacy

Do not upload restricted source documents, personal data, secrets or confidential customer/project records. Synthetic examples must be labelled. Hazardous or unauthorized experiments are not acceptable contribution instructions.

## Publication workflow

When a corresponding repository exists, propose changes on a branch and open a ready-for-review PR. Preserve existing license and unrelated content. Merge authority follows the owner's explicit instructions; the owner may authorize automatic merging after required checks for a requested knowledge update. Tags and official releases require an explicit request. No protection bypass is permitted. In the absence of a repository, deliver a validated ZIP with honest checks and limits.

## New Method admission

A Method contribution names an established technique and an inspected source, supplies a concrete procedure and example, and explains the output and limitations. An original end-to-end workflow belongs in a Practice by default for this domain. Do not claim that a famous name validates a local adaptation. Keep older generic Method files retired; consult [MIGRATION](MIGRATION.md) before introducing an overlapping wrapper.
