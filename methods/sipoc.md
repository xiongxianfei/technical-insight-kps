---
language: "KPS 9.x"
reviewed: "2026-10-08"
id: "ti:me:sipoc"
type: "method"
version: "2.0.0"
status: "active"
references: ["ti:r:asq-undated-sipoc"]
method_origin: "established"
technique_kind: "analytical technique"
---

# SIPOC

## Key takeaway

Expose the boundary and handoffs of a process before investigating detailed mechanisms.

## Summary

Expose the boundary and handoffs of a process before investigating detailed mechanisms. Use it for the stated output, not as a substitute for evidence or an entire engineering workflow.

## Established basis

**Technique:** SIPOC. **Role:** analytical technique. The named technique is reused from [SIPOC CM Diagram](../references/asq-undated-sipoc.md). The worksheet, engineering example and local safeguards below are our exposition and application; they are not a new method, an official standard implementation or evidence that this workflow is effective.

## Inputs and prerequisites

An identifiable process, starting and ending events, participants with process knowledge, and the intended customer or downstream user.

## Rationale

Inputs, recipients and output criteria can be omitted when a team jumps directly into internal steps. A high-level map makes those missing handoffs discussable.

## Procedure

1. Choose the start and end boundary and state the output being examined.
2. List a short sequence of major process steps rather than every implementation action.
3. Associate necessary inputs with suppliers and outputs with recipients or customers.
4. Write the observable acceptance condition for each important output; record constraints and measures separately when useful.
5. Walk one normal and one exception case with process participants. Correct omissions before using the map to select an investigation.

## Worked example

**Synthetic example, not a measured investigation.** For baseline publication: supplier = build process; input = reviewed files; process = select, hash, publish; output = manifest; customer = verifier. A mismatch may arise because the customer uses a different payload boundary. This is a hypothesis from the map, not a proven cause.

## Working template

| Supplier | Input | Process step | Output | Customer | Output criterion |
|---|---|---|---|---|---|
| Named source | Required item | Major action | Delivered item | Recipient | Observable condition |

## Output and validation

Deliver a boundary map validated against representative cases. Check that each important output has a recipient and criterion, including exception handling.

## Limits and optional tools

SIPOC is a process overview, not a timing model, full architecture or causal graph. Do not infer a single owner for every real-world shared responsibility from the table.

Paper or Markdown is sufficient unless the calculation or experiment requires more. A spreadsheet or established analysis package is optional; AI may suggest candidates but does not supply verified evidence, measurements or permissions. The downstream Practice selects and combines this technique; it need not be used in every investigation.

## Deeper knowledge

[SIPOC CM Diagram](../references/asq-undated-sipoc.md). [Select a technique](../METHOD-MAP.md). [Investigation Practice](../practices/discover-and-validate-a-technical-insight.md). [Technology opportunity Practice](../practices/investigate-a-technical-opportunity.md).
