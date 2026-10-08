---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:mo:readiness-evidence-model"
type: "model"
version: "2.0.0"
status: "active"
references: ["ti:r:nasa-2023-technology-readiness-levels"]
uses_principles: ["ti:p:readiness-evidence-is-context-dependent"]
---

# Readiness evidence model

## Key takeaway

Map each readiness criterion to its subject, evidence and unresolved gap.

## Summary

This model represents a scoped readiness claim as technology plus framework plus relevant environment plus evidence. It keeps demonstrated and claimed status distinct without creating a machine-enforceable project metamodel.

## Representation

```text
Technology and configuration + intended environment
                    |
              chosen TRL framework
                    |
      criterion -> evidence -> applicability gap
                    |
       justified level or explicitly unresolved claim
```

## Terms and relationships

The subject is the assessed component or integrated system. A criterion is a condition from the chosen framework. Evidence is a located report or observation associated with a dated configuration. A gap is missing or nonrepresentative evidence, not necessarily proof of failure.

| Criterion | Subject and environment | Evidence inspected | Gap | Proposed next check |
|---|---|---|---|---|
| Relevant environment demonstration | Named prototype and target duty | No result supplied | Environmental evidence absent | Define an authorized representative demonstration |

## Application and assumptions

Work criterion by criterion. Do not average component TRLs into a system TRL. Do not let a maturity score substitute for the performance, cost or safety requirements of the use case. The model assumes evidence identity and scope can be reviewed; otherwise report an unverified claim.

## Limits and evidence

The layout is authored representation informed by [NASA](../references/nasa-2023-technology-readiness-levels.md). It is not an official NASA assessment form or certification. [Context dependent readiness](../principles/readiness-evidence-is-context-dependent.md) explains why the scope is retained.
