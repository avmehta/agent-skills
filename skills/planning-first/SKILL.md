---
name: planning-first
description: Route substantial software work through discovery, scope alignment, clarification when needed, an explicit plan, proportional challenge, approval, implementation, verification, and durable handoff. Use for features, refactors, migrations, integrations, or multi-step changes where coding before agreement would create rework.
---

# Planning First

Use gates, not ceremony. Keep read-only questions and tiny reversible edits lightweight. The user's instructions and an already-approved specification take precedence over this workflow.

## 1. Discover

Inspect repository instructions, current behavior, relevant tests, durable project context, repository/branch status, and existing changes. Treat documentation as context to verify, not automatic truth. Preserve unrelated work.

Classify important sources when their roles differ:

- **current behavior** — verified code or running-system evidence;
- **approved decision or contract** — intended behavior that governs implementation;
- **vision** — direction, not a claim of present capability;
- **historical evidence** — what was previously discussed or attempted;
- **unverified claim** — requires evidence before it can govern behavior.

Completion: the current state and change boundary are evidence-backed.

## 2. Anchor scope

Record a compact scope anchor:

- requested outcome;
- operating stage and intended audience;
- minimum acceptable proof;
- explicit non-goals and later-stage maturity;
- approval state and the exact scope covered by any waiver.

Do not silently upgrade a prototype, one-user tool, or research MVP into a production platform. Safety-critical future gates may remain documented without becoming current implementation scope.

## 3. Clarify only what matters

Use the `socratic-planning` workflow only when product behavior, constraints, failure handling, or acceptance evidence remain ambiguous and cannot be learned from available context. Skip redundant interviewing when the user supplied an approved plan or explicitly waived the approval pause for a defined scope.

Completion: another engineer could plan without inventing product behavior.

## 4. Plan

Present the smallest plan that proves the requested outcome. Include affected seams, ordered changes, failure handling, migration or rollback when relevant, assumptions, and observable verification. Separate now, next, and later.

Completion: the plan is concrete enough to critique and implement.

## 5. Challenge proportionally

Use `contrarian-review` for consequential work. Require the review to test both insufficiency and excess: could the plan fail, and is it building more maturity than the finish line requires? Patch blockers before proceeding.

Completion: verdict is `READY TO IMPLEMENT`.

## 6. Approve

Do not modify production code before explicit approval unless the user already approved the governing spec or explicitly waived this gate. A waiver covers only the stated scope. It does not authorize destructive actions, external production changes, new paid dependencies, or material scope expansion.

## 7. Implement

1. Locate the approved spec/ticket and canonical status ledger.
2. Inspect repository instructions, dirty state, current branch, and baseline checks.
3. Implement only the explicit ticket or clearly next unblocked slice.
4. Create a branch, commit, push, or PR only when requested or already part of the approved workflow.
5. Prefer test-first work where a stable behavioral seam exists; do not force TDD where it would test an imagined interface.
6. Run focused checks during the change and proportionate broader checks at the end.
7. Verify the user-visible acceptance path, not merely test totals.
8. Keep baseline failures, skipped/opt-in tests, environment limitations, and untested behavior separate from regressions caused by the change.
9. Review the final diff against both repository standards and the approved outcome. Use `code-review` when it applies and is available.
10. Update the project's canonical documentation. Never infer that an open PR is merged.

If discovery materially changes behavior, cost, risk, or scope, return to planning for that delta.

Completion: acceptance evidence is recorded and unverified areas are named.

## 8. Preserve

Use `wrap-up` for consequential or multi-session work. Prefer the project's canonical tracker over duplicated status notes, preserve historical decisions, and leave one exact next unblocked action.

