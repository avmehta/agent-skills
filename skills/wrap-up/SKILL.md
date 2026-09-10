---
name: wrap-up
description: Close a work session by verifying repository and external status, updating canonical project memory, recording decisions and tests, and leaving one resumable next action. Use when the user asks to wrap up, checkpoint, hand off, log the session, or preserve context.
---

# Wrap Up

Create a truthful checkpoint that a fresh agent can resume without replaying the conversation.

## Gather evidence

1. Inspect repository status, branch, diff, and recent commits where applicable.
2. Verify referenced PR, merge, deployment, or external state before changing its status.
3. Read the canonical plan, status ledger, decisions, and test evidence used in the session.
4. Distinguish discussed, proposed, approved, implemented locally, committed, pushed, merge-ready, merged, deployed, verified, deferred, and superseded.
5. Record skipped or opt-in tests, baseline failures, environment limitations, and untested acceptance paths separately from passing checks.
6. Redact secrets, credentials, personal data, and sensitive raw output.

## Persist in the right place

Use this order:

1. the user's explicit destination;
2. the project's documented canonical tracker or durable-memory convention;
3. an existing session/handoff note that should be advanced;
4. a new `<repo>/.agent/session-logs/YYYY-MM-DD - <slug>.md` only when a separate checkpoint is useful;
5. the OS temporary directory when the workspace must remain unchanged.

Update the canonical ledger first. Preserve earlier decisions and reviews with dated resolution or supersession notes; do not rewrite history. Link related records rather than duplicating large status sections.

## Checkpoint content

Include, in the project's established format:

- outcome and current status;
- decisions and rationale;
- scoped changes and their repositories/branches/commits/PRs;
- verification commands and truthful outcomes;
- open risks and deliberate deferrals;
- one exact next unblocked action;
- references to canonical artifacts.

If no project format exists, use:

```markdown
---
date: YYYY-MM-DD
project: project-name
tags: [agent-session, project-name]
---
# Session: concise outcome

## Outcome
## Decisions and rationale
## Changes
## Verification
## Open risks and questions
## Exact next step
## References
```

Return the saved path and a five-line maximum resume summary. Completion requires updated canonical memory or an explicit explanation of why persistence was unavailable.

