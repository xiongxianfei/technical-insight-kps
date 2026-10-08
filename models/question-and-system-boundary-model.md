---
id: "ti:mo:question-and-system-boundary-model"
type: "model"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_concepts: ["ti:c:system-boundary", "ti:c:observation-and-interpretation"]
uses_methods: ["ti:me:frame-an-insight-question"]
references: ["ti:r:nasa-undated-decision-analysis", "ti:r:nist-undated-measurement-uncertainty", "ti:r:nasa-7009b-2024-models-and-simulations"]
---

# Question and system boundary model

## Key takeaway

A useful investigation connects a decision to an observable question inside an explicit boundary.

## Summary

This model frames technical work before selecting an explanation. It represents an outcome, context, entities, inputs and outputs, an observation path and the permitted intervention boundary. It is a reusable analytical form, not a domain physics model.

## Representation

```text
Stakeholder purpose -> decision to inform -> technical question
                            |
Context -> [ system and interfaces ] -> relevant outcome
                       |                     |
             permitted interventions   measurement process
                                             |
                                       reported evidence
```

| Element | Local meaning | Example |
|---|---|---|
| Purpose | Outcome worth improving | Remain within a thermal limit during a short burst |
| Question | Uncertainty blocking the decision | Is lower early temperature storage or heat removal |
| Boundary | What is inside the analysis | Object, power input and heat-transfer path |
| Observation | What can be read | Sensor trace, input power, ambient temperature |
| Intervention | What may be changed with approval | Candidate model parameter in simulation |

## Relationships and use

A question should name the relevant outcome, operating context and comparison. The measurement process is a separate element because a displayed effect can originate there. External conditions remain explicit inputs rather than disappearing outside the drawing.

## Assumptions

The selected boundary includes the mechanisms material to the decision. Observations are adequate to detect the proposed effect. Authority to observe does not imply authority to intervene. Unknown elements should be labelled rather than guessed.

## Limits and counterchecks

The model can reveal an omitted input or unanswerable question but cannot establish which mechanism is true. Expand the boundary when unexplained effects or new evidence make a previously external condition material.

## Evidence summary

[NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md) [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md) [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md) supports the cited distinctions. The representation, examples and selection of fields here are authored models, not externally validated software or mandatory schemas.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [System boundary](../concepts/system-boundary.md)
- [Observation and interpretation](../concepts/observation-and-interpretation.md)
- [Frame an insight question](../methods/frame-an-insight-question.md)

- [NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md)
- [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md)
- [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md)

[Package home](../README.md)
