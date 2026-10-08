---
id: "ti:c:comparison-and-control"
type: "concept"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_concepts: ["ti:c:hypothesis", "ti:c:measurement-uncertainty"]
references: ["ti:r:nist-undated-experimental-design-handbook"]
---

# Comparison and control

## Key takeaway

A comparison is informative only about differences it can separate from competing influences.

## Summary

A comparator is the alternative condition against which a result is interpreted. Controls address specific rival explanations or nuisance influences. A baseline is not automatically a valid causal control.

## Definition and distinctions

Specify the experimental unit, intervention, outcome, allocation, timing and nuisance factors. Repeating a reading on one unit differs from independently assigning several units. Blocking, randomization, matched comparisons and factorial variation solve different design problems.

## Worked distinction

Changing both fan and enclosure geometry before one repeat confounds their separate contributions. A two-factor design can inspect combinations and interaction, if the chosen runs are safe and an adequate uncertainty plan accompanies the comparison.

## Limits

One-factor comparisons can help focused debugging but can miss interaction. Randomization does not erase carryover or repair a poorly measured treatment. Real work must respect safety, confidentiality and approval before any comparison.

## Evidence and authorship

The definition is operational vocabulary for this package. [NIST experimental design guidance](../references/nist-undated-experimental-design-handbook.md) supplies the cited technical or methodological basis; the examples and wording are authored synthesis.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Hypothesis](hypothesis.md)
- [Measurement uncertainty](measurement-uncertainty.md)

- [NIST experimental design guidance](../references/nist-undated-experimental-design-handbook.md)

[Package home](../README.md)
