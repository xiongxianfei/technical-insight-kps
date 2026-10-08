---
package_version: "1.0.0"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Start here

## Key takeaway

Choose one question and one decision before selecting a model or experiment.

## Summary

This guide gives a usable first session for engineering investigation. You do not need to read the complete library. Begin with existing observations and a safe desk analysis, then deepen only where a consequential uncertainty remains.

## A first investigation

1. Write the decision or capability you care about. Replace “use technology X” with the outcome that technology is supposed to enable.
2. Record one observation with conditions, units, source and configuration. Write the interpretation separately.
3. Name two plausible accounts when alternatives exist. Include a measurement or context account if relevant.
4. State a predicted consequence for each and identify a difference you could inspect safely.
5. Find the precise external knowledge needed for that difference. Record source contribution and limits, not just a URL.
6. Choose a calculation, fixture, simulation or approved test. State the expected effect and counter-signal before interpreting new results.
7. Record what actually ran, what was observed, what remains uncertain and what decision follows.

## Example starting question

“Why is the new design cooler early?” is not yet enough. A useful version is: “At the same input power and ambient conditions, is the smaller rise during the first 100 seconds explained by greater heat storage rather than better long-run heat removal?” Existing logs and an analytic model may answer part of the question without changing equipment. See [Worked examples](WORKED-EXAMPLES.md) for a synthetic calculation, not a measured product result.

## Which Practice fits

[Discover and validate](practices/discover-and-validate-a-technical-insight.md) supplies the full loop. [Opportunity investigation](practices/investigate-a-technical-opportunity.md) begins from a capability gap. [Claim assessment](practices/assess-a-technical-claim.md) begins from an assertion. [Application and transfer](practices/apply-and-transfer-an-insight.md) begins from existing understanding.

## Do not mistake completion for proof

A completed form or passing checker does not prove a mechanism. It is acceptable to stop with an effect observed but the mechanism unresolved, a result limited to simulation, or a recommendation to obtain specialist evidence. Never invent a successful test to make the narrative complete.
