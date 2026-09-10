---
name: contrarian-review
description: Adversarially stress-test a proposed plan, design, migration, or architecture before implementation. Use when assumptions need challenge or the user requests a contrarian, pre-mortem, red-team, or devil's-advocate review.
---

# Contrarian Review

Treat the plan as a claim that must survive contact with reality. Be specific, fair, and proportional to the requested operating stage.

## Review

1. Restate the promised outcome, intended audience/stage, minimum proof, and load-bearing assumptions.
2. Build a pre-mortem: imagine the work shipped and failed six months later. Explain the most plausible causes.
3. Attack each relevant surface:
   - wrong problem, missing stakeholder, or source used for the wrong purpose;
   - scope ambiguity and unowned decisions;
   - invalid technical assumptions or leaky seams;
   - data loss, concurrency, security, privacy, and abuse;
   - migration, compatibility, rollout, rollback, and operability;
   - verification gaps and tests that could pass while behavior is wrong;
   - unnecessary complexity and a materially simpler route.
4. Ask: **What is the cheapest plan that proves the requested outcome?** Identify later-stage machinery that can be documented and deferred.
5. For every credible issue, give a concrete counterexample, severity, and cheapest useful mitigation.
6. Separate blockers, owner-accepted risks, and future gates. Do not turn a future production requirement into current scope unless the requested stage needs it.
7. Stop when the credible set is exhausted; do not manufacture objections.

## Verdict

Return:

- `BLOCKERS`: defects that must change before coding;
- `RISKS ACCEPTED`: explicit trade-offs the owner may knowingly take;
- `DEFERRED GATES`: important requirements for a later operating stage;
- `SIMPLER PROOF`: the cheapest credible route to the outcome;
- `PLAN PATCH`: the smallest edits that close current blockers;
- `VERDICT`: `REJECT`, `REVISE`, or `READY TO IMPLEMENT`.

Do not implement the plan. `READY TO IMPLEMENT` requires every current-scope blocker to be resolved or explicitly owned with a rollback path.

