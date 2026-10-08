---
id: "ti:c:measurement-uncertainty"
type: "concept"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_concepts: ["ti:c:observation-and-interpretation"]
references: ["ti:r:nist-undated-measurement-uncertainty"]
---

# Measurement uncertainty

## Key takeaway

A reported value needs its measurement process and uncertainty context to support a technical decision.

## Summary

Measurement uncertainty describes the dispersion of values reasonably attributed to a measurand under the adopted evaluation. The measurand is the quantity intended to be measured. Resolution, repeatability, calibration and bias are different considerations.

## Definition and distinctions

Model the reading as a function of inputs and corrections: y=f(x1,...,xn). Include units, time/location, calibration status, sampling and processing. Type A and Type B describe statistical and other evaluation routes; they do not simply mean random versus systematic error.

## Worked distinction

Many readings from one thermometer can be tightly grouped while a calibration offset remains. Repetition can characterize variation without removing a shared offset. A fast sample interval does not guarantee a fast sensor response.

## Limits

This concept does not supply a full uncertainty budget. Correlations, nonlinear propagation, distributions and acceptance margins require domain-specific evaluation. Do not invent error bars or treat displayed decimal places as accuracy.

## Evidence and authorship

The definition is operational vocabulary for this package. [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md) supplies the cited technical or methodological basis; the examples and wording are authored synthesis.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Observation and interpretation](observation-and-interpretation.md)

- [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md)

[Package home](../README.md)
