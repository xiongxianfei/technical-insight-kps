---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:fishbone-analysis"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:asq-undated-fishbone"]
method_origin: "established"
technique_kind: "analytical technique"
---

# Fishbone analysis

## Key takeaway

Organize possible causes of one effect without treating the diagram as a diagnosis.

## Summary

Organize possible causes of one effect without treating the diagram as a diagnosis. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** Fishbone analysis. **Role:** analytical technique. The named technique is reused from [Fishbone Diagram](../references/asq-undated-fishbone.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

One specified effect, a boundary and participants or evidence representing different parts of the process.

## Rationale

Categories broaden the search and make gaps visible when brainstorming otherwise follows the first familiar story.

## Procedure

1. Place the effect at the head of the diagram, using an observed event rather than a preferred cause.
2. Choose context-relevant categories. People, process, equipment, material, measurement and environment are prompts, not mandatory bins.
3. Add candidate causes and subcauses; retain interactions across branches and mark uncertain items.
4. Label each candidate with supporting evidence, contrary evidence or a missing observation.
5. Select a small number of discriminating checks based on consequence and evidence gaps, not the visual size of a branch.

## Worked example

**Synthetic example, not a measured investigation.** For intermittent sensor alarms, branches include actual vibration, sensor mounting, timing, filtering, environment and measurement logging. A large measurement branch may reflect who attended the session rather than its probability of being causal.

## Working template

| Effect | Category | Candidate cause | Evidence status | Discriminating check |
|---|---|---|---|---|
| One observed effect | Relevant branch | Specific mechanism | Supported / disputed / unknown | Measurement or review |

## Output and validation

Deliver a categorized hypothesis set and investigation priorities. Check whether a neglected subsystem or measurement route would change the candidate set.

## Limits and optional tools

Fishbone does not estimate likelihood, prove root cause or represent all feedback and timing. A Markdown table can carry the same reasoning when a drawing is unnecessary.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[Fishbone Diagram](../references/asq-undated-fishbone.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
