---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:mo:investigation-and-intelligence-routing-model"
type: "model"
version: "2.0.0"
status: "active"
uses_concepts: ["ti:c:technology-intelligence"]
---

# Investigation and intelligence routing model

## Key takeaway

Select the route by the uncertainty, not by the prestige of a framework.

## Summary

Technical investigation tests explanations of behavior. Technology intelligence assesses external possibilities for a decision. A disputed technical claim transfers from intelligence to investigation; a newly exposed capability gap can send investigation back to intelligence.

## Representation

```text
Decision and evidence gap
  |-- behavior or causal claim -> investigation -> qualified explanation
  |-- emerging possibility -> intelligence -> scoped opportunity assessment
                               |                     |
                               +---- disputed claim -+
```

## Selection logic

Use 5W2H to clarify the question. Use named techniques only when their outputs match the gap: Fishbone generates candidate causes, DOE addresses designed comparisons, a radar chart displays comparable dimensions, and TRL assesses demonstration status. None supplies the other output automatically.

## Handoff record

Carry the exact claim, source, configuration, environment, uncertainty and the decision affected. Never upgrade a proposed test to an executed result during handoff. Keep source review, interpretation and design preference separate.

## Example and limits

A low-power monitoring announcement prompts a landscape. Its claim of unchanged detection quality becomes an investigation question on representative traces. A roadmap remains conditional while that claim is unresolved. This routing is our Practice design, not an empirical law or a compulsory sequence.

## Deeper knowledge

[Method map](../METHOD-MAP.md) selects concrete techniques. [Technology intelligence](../concepts/technology-intelligence.md) defines the external-information task.
