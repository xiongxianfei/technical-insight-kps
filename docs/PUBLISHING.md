---
language: "KPS 9.x"
package_version: "2.0.0"
---

# Publishing repository changes

## Key takeaway

Use the existing repository, one coherent pull request, and its required checks.

## Summary

Maintain `xiongxianfei/technical-insight-kps` through ordinary Git changes. The 2.0.0 archive application procedure is historical; no external application script or ZIP overlay is required for ongoing work.

## Prepare a change

1. Inspect the current branch and local edits, then fetch the remote. Preserve unrelated work.
2. Create a branch for the requested change. Update affected links, examples and instructions together.
3. Review changed source meanings and dependent summaries before refreshing their fingerprints. Run the commands in [Maintenance](MAINTENANCE.md).
4. Review the diff and state the actual checks and remaining limits in a PR to `main`.

## Publication authority

Push and publish when authorized. For user-authorized knowledge publications, merge after required checks under the existing authorization, respecting branch protections. Verify the remote result before reporting a merge. Create tags or official releases only when requested; local validation does not establish remote CI success.

## Historical migration

The [2.0.0 Method migration](history/2.0.0-method-migration.md) records retired filenames and the receiving Practice stages. It remains useful for old links; its former baseline and archive application instructions do not govern an ordinary change to the current repository.
