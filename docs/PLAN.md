# Portable personal skills package

## Outcome and approved scope

The user requested a new Git repository, a push of their skills, and setup on other systems, while explicitly valuing planning-first, contrarian-review and socratic-planning. This authorizes the new package and remote push. It does not authorize redesigning existing workflows, changing the active installation, deleting data or copying account credentials.

Default destination: private `avmehta/agent-skills`. Source: the 23 personal skills, with bundled system/plugin skills documented as separate dependencies.

## Implementation plan

1. Snapshot personal skill folders with supporting files and provenance hashes.
2. Preserve the favorite trio exactly; replace machine-specific teaching paths only in repository copies.
3. Add a Python standard-library copy installer, an optional preserved global planning agreement and platform setup instructions.
4. Verify install/update behavior in temporary locations, local modifications and conflict protection, relative references, source preservation and Git exclusions.
5. Create a private remote, push the commit, and verify the remote commit and visibility.

## Proportional contrarian review

- **Wrong scope:** bundling all plugin cache folders would look complete while losing tool registration and account access. Mitigation: personal folders only, explicit plugin dependencies.
- **Loss of preferred behavior:** applying the audit recommendations would change the three workflows the user likes. Mitigation: original hashes are enforced.
- **Machine assumptions:** hard-coded home paths and optional macOS voice helpers fail elsewhere. Mitigation: configurable teaching roots, sibling paths and explicit helper limits.
- **Overwrite risk:** updates can erase locally edited skills. Mitigation: preflight all selected targets, track hashes and refuse modified/unmanaged replacements; roll back on ordinary write failure.
- **Installation vs execution:** a copy test does not prove NotebookLM, TradingView or Playwright connectivity. Mitigation: clearly bounded verification and separate setup documentation.

No current blocker remains to creating and testing the isolated package. No production application code or active skill installation needs to change.

## Acceptance evidence

- Exactly 23 personal skills with referenced resources.
- Preferred three skill directories unchanged from the source snapshot.
- Fresh installation, repeat installation, update, collision and local-edit cases tested in temporary locations.
- macOS/Linux/Windows setup commands documented; native platform test results reported separately.
- No token files, browser profiles, caches, datasets or course progress in Git.
- Verified private GitHub repository and matching pushed commit.
