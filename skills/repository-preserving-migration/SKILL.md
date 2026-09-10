---
name: repository-preserving-migration
description: Safely make a repository lean, restart Git history, remove tracked artifacts, or reorganize a repository while preserving valuable local data. Use when the user mentions fresh history, `.gitignore`, untracking files, excluding weights/datasets/media, Git bundles, history cleanup, or repository migration. Do not use for ordinary commits or small file moves.
---

# Repository-Preserving Migration

Preserve valuable data while changing what Git tracks or publishes. “Keep it off GitHub” does not mean “delete it from disk.”

## Distinguish the operations

Name the requested operation precisely before acting:

- **Preserve locally** — file remains on disk.
- **Ignore** — `.gitignore` prevents new untracked copies from being added; it does not affect already-tracked files.
- **Untrack** — remove a path from the Git index while preserving the working-tree file.
- **Remove from current snapshot** — file is absent from the new commit but may remain in earlier history.
- **Remove from history** — rewrite or replace Git history so old blobs will not be published.
- **Backup history** — create and verify a private bundle or untouched source repository.
- **Delete from disk** — destructive and separate; never infer it from “clean,” “lean,” or “do not push.”

## Preflight

1. Read repository instructions and inspect status, remotes, branches, worktrees, submodules, ignored files, tracked files, stashes, and object size.
2. Identify the exact source and destination repositories. Treat the source as read-only unless the user explicitly includes it.
3. Classify files into:
   - publishable source/config/docs;
   - valuable local artifacts to preserve but not track;
   - generated/recoverable artifacts;
   - secrets or sensitive data;
   - genuine deletion candidates.
4. State the preservation invariant, exact destructive targets, recovery method, and whether history will change.
5. Ask only when a missing choice changes preservation or publishing materially. A request to “start fresh and keep the local data” already resolves the central choice.

## Execute

- Prefer a separate destination repository or recoverable archive over rewriting the only copy.
- Use `.gitignore` for future additions and index-only removal for already-tracked files that must remain locally.
- If old blobs must not reach a new remote and history is not needed, prefer a clean snapshot repository over a complex rewrite.
- If history matters, create and verify a backup before rewriting it.
- Keep models, datasets, checkpoints, media, secrets, and generated arrays outside the publishable object graph when requested.
- Preserve unrelated repositories and nested `.git` histories unless the user explicitly changes the topology.
- Do not commit or push unless the user requested that external state change.

## Verify

Before commit or push, report:

1. working-tree files preserved, with counts/sizes where useful;
2. staged paths and largest staged/Git objects;
3. tracked files that violate the exclusion policy;
4. ignored-file checks for representative protected artifacts;
5. history/object audit when the remote must never receive old blobs;
6. backup verification and checksum when a bundle/archive was created;
7. repository status, remotes, branch, and whether anything was committed or pushed.

Never claim data is safe merely because `.gitignore` contains a pattern. Verify both filesystem preservation and Git exclusion.

