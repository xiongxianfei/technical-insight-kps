---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:morphological-analysis"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:ritchey-2013-general-morphological-analysis"]
method_origin: "established"
technique_kind: "analytical technique"
---

# Morphological analysis

## Key takeaway

Explore combinations of functionally distinct options and eliminate inconsistent configurations.

## Summary

Explore combinations of functionally distinct options and eliminate inconsistent configurations. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Morphological analysis. **Role:** analytical technique. The named technique is reused from [General Morphological Analysis](../references/ritchey-2013-general-morphological-analysis.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

A bounded design question, meaningful dimensions, candidate states and people able to assess compatibility. Avoid enumerating unrelated attributes merely to fill a grid.

## Rationale

Looking at dimensions separately helps reveal alternatives that a list of complete favored solutions omits. Consistency checks prevent arbitrary combinations from becoming presumed designs.

## Procedure

1. Define the problem and choose dimensions that describe genuine design choices.
2. List plausible alternatives for each dimension, including a simpler or no-change state where meaningful.
3. Construct the morphological field and inspect cross-consistency of option pairs with recorded reasons.
4. Assemble promising configurations and assess whole-system interactions beyond pairwise compatibility.
5. Prioritize a few candidates for technical evaluation, retaining excluded combinations and uncertainty.

## Worked example

**Synthetic example, not a measured investigation.** A synthetic monitor field includes sensing mode (continuous/event-triggered), computation (local/remote), and communication (immediate/batched). Event-triggered/local/batched is one candidate. Pairwise compatibility does not establish acceptable detection latency or system power.

## Working template

| Dimension | Option 1 | Option 2 | Consistency question |
|---|---|---|---|
| Functional choice | Plausible state | Alternative | Why combinations may conflict |

## Output and validation

Deliver a documented field, exclusions and candidate configurations. Check whether the selected dimensions excluded a fundamentally different mechanism.

## Limits and optional tools

Combinatorial coverage is bounded by the chosen dimensions. Pairwise consistency is not global feasibility, optimum performance or likelihood of adoption. No new algorithm or exhaustive-search guarantee is implied.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[General Morphological Analysis](../references/ritchey-2013-general-morphological-analysis.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
