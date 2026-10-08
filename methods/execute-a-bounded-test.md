---
id: "ti:me:execute-a-bounded-test"
type: "method"
version: "1.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored synthesis; evidence and inference distinguished"
confidence: "scoped and revisable; not validated as a complete framework"
uses_concepts: ["ti:c:provenance"]
uses_models: ["ti:mo:measurement-and-uncertainty-model"]
references: ["ti:r:sandve-2013-reproducible-computational-research", "ti:r:nasa-7009b-2024-models-and-simulations", "ti:r:li-2019-collecting-data-cochrane"]
---

# Execute a bounded test

## Key takeaway

Execute the approved comparison and preserve what happened, including departures from the plan.

## Summary

Use only after the setup, authority, safeguards and analysis plan are sufficient for the task. This method emphasizes configuration, fidelity, observation and stopping—not generic instructions to manipulate equipment.

## Inputs and prerequisites

Approved plan, competent personnel, validated setup where required, measurement readiness, permission to use data and clear abort/rollback authority. Do not infer readiness from a completed template.

## Rationale

An intended intervention and an actual intervention can differ. Results without configuration and fidelity records may test a different question from the one claimed.

## Procedure

1. Confirm permitted scope, safeguards, rollback, contact/stop responsibilities and the measurement checks. Stop when any prerequisite is missing.
2. Record input/configuration versions, initial conditions, timing, calibration and the planned order. Identify raw-data locations without exposing secrets.
3. Execute the prescribed condition without unrecorded opportunistic changes. Verify the manipulation occurred and that controls remained appropriate.
4. Record outputs, failures, missingness and deviations. Preserve failed runs instead of excluding them merely because they conflict with expectations.
5. Stop at a hazard, unexpected adverse effect, invalid measurement or predetermined stopping condition. Do not reproduce harmful conditions for a stronger comparison.
6. Lock or version the evidence and analysis inputs. Separate observations, operator comments and interpretations.
7. Report whether the test was executed as designed, partly executed or not executed. Route invalid execution to replanning rather than a verdict on the mechanism.

## Expected effect

A result with enough context to determine what was tested. No outcome is marked successful solely because a run completed.

## Validation and counterevidence

Check expected and actual configuration, manipulation and observation window. If they differ materially, the evidence may be informative but is not the planned test. Record this before examining whether the headline outcome is favourable.

## Limits

Operational, lab, security, health and human-subject requirements override this generic method. Reproducibility does not justify publicly sharing private or restricted artifacts.

## Evidence and authorship

[Reproducible computational research](../references/sandve-2013-reproducible-computational-research.md) [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md) [Cochrane collecting data guidance](../references/li-2019-collecting-data-cochrane.md) provides the cited concepts or guidance. This particular procedure is authored synthesis, not an experimentally validated programme.

## Deeper knowledge

The essential explanation or procedure is above. These links provide reusable detail and source inspection.

- [Provenance](../concepts/provenance.md)
- [Measurement and uncertainty model](../models/measurement-and-uncertainty-model.md)

- [Reproducible computational research](../references/sandve-2013-reproducible-computational-research.md)
- [NASA standard for models and simulations](../references/nasa-7009b-2024-models-and-simulations.md)
- [Cochrane collecting data guidance](../references/li-2019-collecting-data-cochrane.md)

[Package home](../README.md)
