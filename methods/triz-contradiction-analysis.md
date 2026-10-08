---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:triz-contradiction-analysis"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:matriz-undated-contradictions", "ti:r:oxford-creativity-undated-triz-glossary"]
method_origin: "established"
technique_kind: "analytical technique"
---

# TRIZ contradiction analysis

## Key takeaway

Use explicitly stated contradictions to generate candidate design directions before engineering validation.

## Summary

Use explicitly stated contradictions to generate candidate design directions before engineering validation. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** TRIZ contradiction analysis. **Role:** analytical technique. The named technique is reused from [TRIZ glossary](../references/matriz-undated-contradictions.md); [Oxford Creativity TRIZ glossary](../references/oxford-creativity-undated-triz-glossary.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

An identified function, the property to improve, the property worsened and a factual description of the conflict. This file covers an introductory TRIZ subset, not the full methodology.

## Rationale

A tradeoff framed only as a compromise can conceal alternative arrangements. Reformulating the conflict can expose changes in sequence, location, condition or available resources.

## Procedure

1. Write what improves and what worsens under the present solution. Check that the conflict is observed or clearly hypothetical.
2. Distinguish a technical contradiction between properties from opposing requirements for the same property under particular conditions.
3. Explore separation in time, space, condition or system level where applicable, and examine existing resources before adding components.
4. Translate prompts into concrete candidate mechanisms, recording new disadvantages and feasibility assumptions.
5. Compare candidates against the original need and define a discriminating calculation or authorized test.

## Worked example

**Synthetic example, not a measured investigation.** A sensor appears to need frequent sampling for detection but infrequent activity for low energy. A candidate uses a low-power trigger before higher-power analysis. This may miss events or add false triggers; it is an idea to test, not a guaranteed resolution.

## Working template

| Required function | Improving property | Worsening property | Contradiction type | Separation or resource prompt | Candidate | New failure and test |
|---|---|---|---|---|---|---|
| Goal | Desired change | Cost of change | Technical / physical / unclear | Relevant prompt | Mechanism | Counterevidence |

## Output and validation

Deliver a small set of candidate mechanisms with assumptions and validation plans. Discard prompts that violate physical limits or the actual requirement.

## Limits and optional tools

TRIZ inventive principles are heuristics, not KPS explanatory Principles. No proprietary contradiction matrix or ARIZ manual is reproduced. A conflict formulation does not establish that every problem has a feasible breakthrough.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[TRIZ glossary](../references/matriz-undated-contradictions.md); [Oxford Creativity TRIZ glossary](../references/oxford-creativity-undated-triz-glossary.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
