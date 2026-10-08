---
language: "KPS 9.x"
reviewed: "2026-10-08"
package_version: "2.0.0"
---

# Synthetic sensor opportunity example

## Key takeaway

A concrete worksheet can improve the question without turning invented example data into evidence.

## Summary

This example reuses the sensor opportunity from the integrated release and makes the named techniques explicit. All candidates, numbers and proposed tests are synthetic. No literature search, patent review, experiment, field trial or performance result actually occurred.

## Frame with 5W2H

| Prompt | Illustrative answer |
|---|---|
| Who | Maintenance users and the engineering decision owner |
| What | Evaluate low-power anomaly monitoring |
| When | During intermittent connectivity; time horizon not yet agreed |
| Where | A hypothetical remote sensor installation |
| Why | Timely detection may help maintenance decisions |
| How | Incumbent transmits data; candidates change sampling or analysis |
| How much | Energy, detection and latency thresholds still require an owner decision |

This yields a bounded question, not a conclusion: can a candidate reduce energy without violating the agreed detection and latency limits in the target duty cycle?

## Organize hypotheses and causes

Use a Fishbone table with sensing, mounting, environment, sampling, computation, communications and measurement. Candidate A triggers sampling; candidate B runs a small local detector. Hypotheses include reduced transmission, added computation, missed short events and differences in evaluation traces. Each needs a prediction and a rival. Five Whys may deepen a branch but cannot supply the missing observations.

## Investigate external possibilities

A real Horizon Scan would record dated original signals and counter-signals. A structured literature and patent landscape would record coverage and family definitions. TRL assessment would inspect an actual artifact, environment and criterion-level evidence. No TRL or patent-rights conclusion is assigned here because none of that evidence has been collected.

## Generate candidate configurations

The tentative conflict is frequent sensing versus energy use. TRIZ separation prompts suggest time- or condition-dependent activity. A morphological field combines sensing (continuous or triggered), computation (local or remote) and transmission (immediate or batched). A plausible combination is not a demonstrated viable product. Check global interactions after pairwise compatibility.

## Plan a discriminating test

A DOE plan would specify representative independent units or traces, factors, randomization where justified, replication, response definitions and safety/authority limits. Detection, energy and latency are different outcomes. For illustration only, the four response values 10, 14, 15 and 13 yield different effects of factor A at the two levels of B. The difference of effects is -6. Without replication or a justified error model, this is no significance result.

## Compare without false precision

For an illustrative radar input table, use fixed bounds and outward-desirable mapping:

| Dimension | Direction | Bounds | A raw | B raw | A mapped | B mapped |
|---|---|---|---|---|---|---|
| Energy in mJ per event | Lower | 10 to 50 | 20 | 35 | 0.75 | 0.375 |
| Accuracy | Higher | 0.80 to 1.00 | 0.92 | 0.96 | 0.60 | 0.80 |
| Mass in grams | Lower | 80 to 180 | 120 | 100 | 0.60 | 0.80 |

The declared units and values describe only this hypothetical example, not a real device. A real comparison would also specify the event, test population and operating context. The table supports a description of assumed tradeoffs, not a winning product. A chart would retain this table, uncertainty and missing values. Do not use polygon area as a decision criterion.

Our mathematical counterexample uses four equally spaced radial axes: values (1,1,0.2,0.2) have polygon area 0.72, while the same values reordered (1,0.2,1,0.2) have area 0.40. The sum is unchanged. Axis ordering alone changes area, so apparent size is not intrinsic overall merit.

A Pugh matrix instead compares +, 0, - or unknown to an incumbent by criterion. A weighted decision matrix requires defensible score scales and preference weights. Neither can waive a hard constraint or replace missing measurements.

## Decide a bounded research step

Heilmeier questions separate the need, incumbent limitation, proposed novelty, technical basis, beneficiaries, risks, resources and falsifiable milestones. The conditional roadmap may move from defining outcomes to source review, a controlled fixture, integrated prototype and authorized representative demonstration. Each gate can continue, redesign or stop. No calendar commitment or operational deployment follows automatically.

## Current working summary

Actual results: none. Supported preference: none. Next question: which representative evidence would separate communication savings from extra computation and missed detections? Authority: no live trial or deployment is implied.

## Deeper knowledge

[Investigation](practices/discover-and-validate-a-technical-insight.md), [Opportunity](practices/investigate-a-technical-opportunity.md), [5W2H](methods/5w2h.md), [DOE](methods/design-of-experiments.md), [Radar](methods/radar-chart.md), [Pugh](methods/pugh-matrix.md) and [Roadmapping](methods/technology-roadmapping.md) provide procedures. The arithmetic is checked by `test_transition.py`, not by fabricated field data.
