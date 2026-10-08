---
id: "ti:me:audit-an-observation"
type: "method"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_principles: ["ti:p:measurements-include-the-observation-process"]
uses_models: ["ti:mo:measurement-and-uncertainty-model"]
references: ["ti:r:nist-undated-measurement-uncertainty", "ti:r:sandve-2013-reproducible-computational-research", "ti:r:w3c-2013-prov-overview"]
---

# Audit an observation

## Key takeaway

Check what was actually measured before explaining why the system behaved that way.

## Summary

Use this when a surprising result could originate in measurement, preprocessing, configuration or reporting. The output is an observation record with a traceable acquisition chain and unresolved quality issues.

## Inputs and prerequisites

The original observation or immutable copy, acquisition details, configuration/time and permission to inspect the relevant artifacts. Preserve confidentiality and do not overwrite raw evidence.

## Rationale

A reading includes target behavior and the observation process. Repeating an analysis can reproduce a shared error. Independent checks of units, timing and processing constrain those explanations.

## Procedure

1. Save or identify the original evidence and its version; record who/what produced it, when and under which configuration.
2. Define the measurand or event, units, reference frame and time window. Record what “not observed” means relative to detection capability.
3. Trace acquisition: sensor/log source, calibration, placement, sampling, clock, filtering, exclusions and transformations.
4. Check basic consistency using an authorized reference, invariant, unit conversion or alternative extraction. Do not create a harmful event to obtain a better trace.
5. Separate systematic/common uncertainty from repeat variation without equating them with Type A/Type B evaluation categories.
6. Record missing evidence, changed settings and whether the result survives the checks. Keep the original observation and revised interpretation separately.
7. Decide whether the data support analysis, require reacquisition or leave the question unresolved.

## Expected effect

An observation that can be inspected without silently accepting its causal explanation. A clock mismatch or inclusion mismatch may become the leading hypothesis.

## Validation and counterevidence

Check that the displayed value can be traced to inputs and processing. If a different extraction changes the result, the effect is not yet established. A matching extraction supports consistency but not correctness of the original sensor.

## Limits

Some acquisition details may be inaccessible. Do not fill gaps from expected behavior. A metrological uncertainty evaluation may require specialist knowledge beyond this audit.

## Evidence and authorship

[NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md) [Reproducible computational research](../references/sandve-2013-reproducible-computational-research.md) [W3C provenance overview](../references/w3c-2013-prov-overview.md) provides the cited concepts or guidance. This particular procedure is authored synthesis, not an experimentally validated programme.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Measurements include the observation process](../principles/measurements-include-the-observation-process.md)
- [Measurement and uncertainty model](../models/measurement-and-uncertainty-model.md)

- [NIST essentials of measurement uncertainty](../references/nist-undated-measurement-uncertainty.md)
- [Reproducible computational research](../references/sandve-2013-reproducible-computational-research.md)
- [W3C provenance overview](../references/w3c-2013-prov-overview.md)

[Package home](../README.md)
