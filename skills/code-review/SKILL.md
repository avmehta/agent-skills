---
name: code-review
description: Review a branch, PR, or work-in-progress diff against repository standards and its originating specification. Use when the user asks to review changes or review since a commit, branch, tag, or merge-base.
---

# Code Review

Review the change along two independent axes:

- **Standards** — does the diff follow repository instructions and avoid material design/code smells?
- **Spec** — does it implement the requested outcome without omissions, incorrect behavior, or scope creep?

Keep the axes separate so one cannot hide failure in the other.

## 1. Pin the comparison

Resolve the fixed point before reviewing:

1. Use the point the user supplied.
2. For a PR, use its verified base branch and merge-base.
3. For an ordinary feature branch with a unique configured default/upstream base, infer and report it.
4. Ask only when multiple plausible bases would materially change the diff.

Capture `git diff <fixed-point>...HEAD` and `git log <fixed-point>..HEAD --oneline`. Confirm the ref resolves and the diff is non-empty. Preserve unrelated working-tree changes.

## 2. Find the governing sources

Identify the spec from, in order:

1. a user-supplied issue, document, or acceptance criteria;
2. the PR body or issue references in commits;
3. a matching plan/spec in the repository;
4. the explicit request in the current conversation.

If no spec exists, report that limitation and review standards plus evident regressions. Do not block on installing or configuring an issue-tracker workflow.

Standards sources include `AGENTS.md`, `CONTRIBUTING.md`, architecture/domain decisions, style guides, and area-specific instructions.

## 3. Establish the baseline

Before assigning a finding to the change:

- distinguish introduced behavior from pre-existing problems;
- reproduce high-impact claims when a safe, proportionate check exists;
- record baseline test/type/build failures separately;
- note skipped, opt-in, fake-only, or environment-blocked tests;
- inspect whether changed behavior is covered through the real user-facing path.

Passing test totals are evidence only for what those tests exercise.

## 4. Review standards

Check documented rules first. Then use these as judgment heuristics, not automatic violations:

- mysterious naming;
- duplicated logic;
- feature envy or message chains;
- data clumps or primitive obsession;
- repeated switches;
- shotgun surgery or divergent change;
- speculative generality;
- middle-man abstractions;
- inheritance that implementers mostly refuse.

Repository standards override generic heuristics. Skip issues already enforced reliably by tooling.

## 5. Review the specification

Check for:

- missing or partial requirements;
- behavior that was not requested;
- implementation that appears present but is wrong;
- contract/schema/runtime disagreement;
- unhappy paths, ownership, lifecycle, compatibility, and rollback required by the spec;
- acceptance criteria supported only by mocks or tests that cannot fail on the real bug.

Quote or link the governing requirement for every spec finding.

## 6. Use delegation conditionally

When parallel agents are both available and authorized, independent Standards and Spec passes can reduce anchoring. Otherwise perform the two passes sequentially yourself. The review must not fail merely because delegation is unavailable.

## 7. Report and preserve resolution

For each finding include location, evidence, impact, and the smallest useful fix. Classify it as:

- `blocker`;
- `fix now`;
- `accepted trade-off`;
- `deferred gate`;
- `false positive` after reproduction.

Report under `Standards` and `Spec`, followed by verification gaps and a concise merge recommendation. Do not merge or rerank the two axes into a single score.

When updating a saved review, preserve the original finding and add a dated resolution or supersession note. Never erase the decision history after the code changes.

