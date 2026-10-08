---
package_version: "1.0.0"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Compatibility

## Key takeaway

Domain content evolves independently while its authoring contract remains compatible with KPS 9.x.

## Summary

The package version is 1.0.0. Compatibility is declared against the KPS major line; the exact inspected release and source commit are recorded separately. The five object roles and Markdown requirements are adopted, not redefined.

## Declarations

```yaml
package_version: "1.0.0"
kps_language: "9.x"
validated_with: "9.0.1"
markdown_profile: "practical-markdown-v1"
```

KPS source commit: `60972c57199ae8bc21d4b7a00ac55552b4105277`. Major-line compatibility is an intent bounded by this contract, not a statement that future versions have already been tested.

## Independence

All local knowledge links resolve within this package. External URLs identify source publications or the authoring authority. Neither Swim nor REM is required. Domain examples illustrate multiple disciplines without importing their project schemas.

## Tooling provenance

`validate.py` and `test_validate.py` are byte-identical to the files at the inspected KPS commit, including the shared manifest-payload selection fix. The MIT notice is retained. `test_examples.py` is local domain verification code.

## Limits

The validator implements a conservative subset of widely supported Markdown and single-line JSON-compatible YAML. It is not a general Markdown/YAML parser. This release does not claim testing in every renderer or conformance with NASA, ISO or any engineering certification system.
