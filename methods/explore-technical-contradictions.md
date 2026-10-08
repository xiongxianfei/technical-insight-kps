---
id: "ti:me:explore-technical-contradictions"
type: "method"
version: "1.1.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-08"
basis_kind: "TRIZ-inspired authored ideation method"
uses_concepts: ["ti:c:tradeoff", "ti:c:mechanism"]
uses_models: ["ti:mo:causal-path-and-intervention-model"]
references: ["ti:r:matriz-undated-contradictions", "ti:r:oxford-creativity-undated-triz-glossary"]
---

# Explore technical contradictions

## Key takeaway

Treat a conflict as a model to challenge and a source of candidate designs rather than a reason to assume only compromise is possible.

## Summary

This TRIZ-inspired Method distinguishes a two-parameter trade-off from opposing demands on one property, then explores separation and alternative mechanisms. Its output is a candidate set with testable assumptions. It does not guarantee that a contradiction is resolvable or reproduce the full TRIZ matrix or ARIZ.

## Inputs and prerequisites

An observed or predicted trade-off, required function, operating boundary and measurable desirable/undesirable outcomes. Establish that the conflict is real in this context rather than caused by inconsistent requirements or incomparable tests. Keep safety and physical constraints explicit.

## Rationale

A particular design can couple two outcomes without establishing that every design couples them in the same way. Reframing the conflict by time, location, operating condition or system scale can reveal alternatives. A suggestive analogy remains a hypothesis until its mechanism and consequences are checked.

## Procedure

1. Write a conditional description: changing feature X improves outcome A but worsens outcome B under conditions C. Include units or visible events and distinguish evidence from an assumed relationship.
2. Ask whether this is an engineering contradiction between two parameters or opposing requirements on one property. Both requirements need a stated reason; inconsistent wording alone is not a physical contradiction.
3. Check the system boundary and available resources. Is a neglected interface, stored energy, timing difference or neighboring subsystem relevant? Avoid silently moving the harm outside the measured boundary.
4. Generate alternatives using separation in time, space, condition and component/system scale when meaningful. Also consider a different mechanism or removing an unnecessary requirement. Do not force every prompt to produce an answer.
5. Use a small morphological table when alternatives combine several functions: list options for each function, inspect feasible combinations and rule out incompatible combinations explicitly. This table is an optional organizing aid, not proof of novelty.
6. For each candidate, record the changed mechanism, retained benefits, new costs/risks, assumptions and a contrary prediction. A clever phrase or matrix cell is not evidence.
7. Compare with the baseline and a simple compromise. Select a bounded discriminating check and return to ordinary engineering validation. Reject candidates that violate hard constraints before experimentation.

## Worked example

A cooling path might need insulation during one operating mode but heat rejection in another. A mode-dependent path is a candidate from separation in condition; it introduces actuation, reliability and control questions. This hypothetical example does not establish a viable switch or permission to build one.

## Output and validation

Produce a trace from conflict to candidate mechanism to proposed check. Look for hidden constraint changes, unexplained effects and harm shifted elsewhere. If the same result can be produced by a simpler baseline, document that rather than favoring inventive complexity.

## Optional tools

Paper, Markdown or a table is enough. An external TRIZ matrix or effects database may suggest ideas, subject to its own access terms. Verify the underlying physics and sources. No copied matrix, paid subscription or software implementation is required.

## Limits and deeper knowledge

[MATRIZ](../references/matriz-undated-contradictions.md) supplies the contradiction distinctions; [Oxford Creativity](../references/oxford-creativity-undated-triz-glossary.md) describes separation prompts. Their shared conceptual tradition is not independent efficacy evidence. TRIZ inventive principles are solution-generation heuristics and remain in this Method, not in KPS principles/. [Discriminating tests](design-a-discriminating-test.md) and [alternative comparison](compare-technical-alternatives.md) assess candidates.
