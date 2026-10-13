---
language: "KPS 9.x"
package_version: "2.0.0"
---

# Maintaining Technical Insight KPS

## Key takeaway

Read the Markdown directly; use the existing checks when changing the library.

## Summary

Knowledge remains in the five role folders and `references/`. Reader routes, worked examples and blank templates live in `guides/`; authoring, indexes, review and publication guidance live in `docs/`. Obsolete release reports stay in Git history; the useful Method responsibility map remains in `docs/METHOD-MIGRATION.md`. The layout cleanup does not change knowledge identities, Practice stages or the pinned KPS contract.

## Commands

Run from the repository root with Python 3 and its standard library:

```bash
python3 validate.py .
python3 -m unittest discover -s tests -v
```

The same commands run in CI. For a packaged snapshot, also run `python3 validate.py . --manifest` after updating its checksum inventory. The manifest is a byte-level inventory, not a scientific review or a command to run after every edit.

## Why these scripts remain

| File | Concrete purpose |
|---|---|
| `validate.py` | Find broken links, invalid metadata, incomplete structure and changed dependencies; verify archive integrity when requested |
| `tests/test_package.py` | Verify the bundled checker against its recorded upstream digest |
| `tools/example_calculations.py` and `tests/test_examples.py` | Check the thermal, factorial and file-set examples used in the guides |
| `tests/test_methods.py` | Check Method source declarations and synthetic technique arithmetic |

No script is required for reading, choosing a Practice or syncing with Git. Copied validator regressions, completed-migration inventories and keyword assertions have been removed under the test allowlist. These small tools stay local so the package can be checked without sibling repositories or a package installation. Core owns shared validation behavior; adopting a newer copy requires an explicit compatibility review.

## Editing and dependency review

Read [Authoring](AUTHORING.md), change the owning document and inspect affected summaries. Only after that review may `python3 validate.py . --accept-reviewed-summaries` record new fingerprints. Ordinary validation never accepts them automatically. Keep personal investigations and confidential records outside this repository.

Text uses LF line endings under `.gitattributes`, because dependency fingerprints and archive checksums use exact bytes. A checkout conversion is not a content review. Restore the intended line endings before investigating checksum failures.

## Layout migration

Update bookmarks to the paths below. Old root document URLs do not automatically redirect. Links inside this repository have been rebased; the knowledge-role paths and stage anchors remain stable.

| Former root path | Current path |
|---|---|
| `START-HERE.md` | [guides/START-HERE.md](../guides/START-HERE.md) |
| `METHOD-MAP.md` | [guides/METHOD-MAP.md](../guides/METHOD-MAP.md) |
| `INTEGRATED-EXAMPLE.md` | [guides/INTEGRATED-EXAMPLE.md](../guides/INTEGRATED-EXAMPLE.md) |
| `INTEGRATED-PRACTICES.md` | [guides/INTEGRATED-PRACTICES.md](../guides/INTEGRATED-PRACTICES.md) |
| `WORKED-EXAMPLES.md` | [guides/WORKED-EXAMPLES.md](../guides/WORKED-EXAMPLES.md) |
| `TEMPLATES.md` | [guides/TEMPLATES.md](../guides/TEMPLATES.md) |
| `BOUNDARIES.md` | [guides/BOUNDARIES.md](../guides/BOUNDARIES.md) |
| `AUTHORING.md` | [docs/AUTHORING.md](AUTHORING.md) |
| `COMPATIBILITY.md` | [docs/COMPATIBILITY.md](COMPATIBILITY.md) |
| `INDEX.md` | [docs/INDEX.md](INDEX.md) |
| `WHY-MAP.md` | [docs/WHY-MAP.md](WHY-MAP.md) |
| `SOURCE-REVIEW.md` | [docs/SOURCE-REVIEW.md](SOURCE-REVIEW.md) |
| `SOURCE-SYNTHESIS.md` | [docs/SOURCE-SYNTHESIS.md](SOURCE-SYNTHESIS.md) |
| `PUBLISHING.md` | [docs/PUBLISHING.md](PUBLISHING.md) |
| `CONTRIBUTING.md` | [.github/CONTRIBUTING.md](../.github/CONTRIBUTING.md) |
| `MIGRATION.md` | [docs/METHOD-MIGRATION.md](METHOD-MIGRATION.md) |

## Verification limits

Report current command results in each change PR. Obsolete execution logs and the duplicate transition inventory are not retained in the current tree. Structural and arithmetic checks do not establish empirical effectiveness or independent expert review.

## Layout dependency review

The 2026-10-13 cleanup preserved the text, metadata, knowledge identities and stage headings of all 94 knowledge and Reference objects. Changes within these files only point existing links to relocated support documents. The receiving summaries keep the same claims and conditions; their dependency fingerprints were refreshed for these path-only changes. This is an editorial and mechanical review, not independent scientific review.

## Test allowlist

Run the actual package validator, verify its pinned digest, and retain checks of Method source declarations and synthetic calculations with their meaningful boundary cases. The matching full validator regression suite remains in Core at commit `60972c57199ae8bc21d4b7a00ac55552b4105277`; `upstream-lock.json` records this ownership. Historical Method migrations remain documented but do not fix the future file count, require every Method to be used by a Practice, or impose a particular sentence. Keep archive checksum checks for packaged snapshots.

## Packaged archive checks

The Git source tree does not keep `MANIFEST.sha256`. When distributing an archive, generate it inside a clean staging copy of the package, then verify the extracted archive. From that copy's root:

```bash
python3 - <<'PYMANIFEST'
from pathlib import Path
import validate
root = Path('.')
Path('MANIFEST.sha256').write_text(''.join(
    validate.sha(path) + '  ' + path.relative_to(root).as_posix() + '\n'
    for path in validate.manifest_payload_files(root)
), encoding='utf-8')
PYMANIFEST
python3 validate.py . --manifest
```

The existing payload helper excludes Git metadata and caches. Repeat the manifest check after extracting the archive; this verifies bytes and file coverage, not evidence quality.
