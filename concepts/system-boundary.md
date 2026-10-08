---
id: "ti:c:system-boundary"
type: "concept"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_concepts: ["ti:c:assumptions-and-boundary-conditions"]
references: ["ti:r:nasa-7009b-2024-models-and-simulations", "ti:r:nasa-undated-decision-analysis"]
---

# System boundary

## Key takeaway

A boundary determines what is treated as internal, external, observed and controllable.

## Summary

A boundary is an analytical choice, not necessarily a product outline or organizational chart. It sets the entities and time scales of interest, relevant flows across the boundary and the level at which an outcome is evaluated.

## Definition and distinctions

Map inputs, outputs, stored quantities, feedback and external actors. Include the measurement path when interpreting data. Separate the observation boundary from the intervention boundary: you may observe a supplier interface without authority to change the supplier.

## Worked distinction

A build artifact’s boundary includes intended publication files, not the surrounding Git database. A cooling study may need ambient conditions outside the enclosure included as inputs. Moving a boundary can turn an apparent violation into an unaccounted flow.

## Limits

Boundary choice can conceal failure paths or costs. No boundary proves independence. A diagram of containment alone does not describe timing, information flow or causation.

## Evidence and authorship

The definition is operational vocabulary for this package. [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md) [NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md) supplies the cited technical or methodological basis; the examples and wording are authored synthesis.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Assumptions and boundary conditions](assumptions-and-boundary-conditions.md)

- [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md)
- [NASA decision analysis guidance](../references/nasa-undated-decision-analysis.md)

[Package home](../README.md)
