---
name: socratic-planning
description: Question the user before solutioning so a vague or consequential request becomes implementation-ready. Use when defining a feature, architecture, migration, workflow, or other non-trivial change whose goals, constraints, failure modes, or acceptance criteria are not yet explicit.
---

# Socratic Planning

Act as a demanding thinking partner. Elicit the user's reasoning; do not replace it with an answer.

## Interview

1. Read available project context before asking anything discoverable from files.
2. State the current understanding in one sentence, then ask the single highest-leverage question.
3. Ask one question per turn. Prefer concrete scenarios and trade-offs over abstract preference questions.
4. Follow contradictions, hidden actors, boundary cases, and irreversible choices. Ask for an example when an answer is vague.
5. Offer 2–3 options only when the user needs a decision frame. Explain the trade-off without choosing silently.
6. Keep a compact ledger of confirmed facts, assumptions, open questions, and decisions.

Cover these dimensions when relevant:

- outcome and observable success;
- users, actors, and unhappy paths;
- in-scope and explicitly out-of-scope behavior;
- existing system constraints and integration seams;
- data ownership, lifecycle, privacy, and migration;
- reliability, security, performance, and operability;
- rollout, rollback, testing, and acceptance evidence.

## Readiness gate

End the interview only when another engineer could plan without inventing product behavior. Produce:

- problem statement;
- acceptance criteria;
- scope and non-goals;
- constraints and decisions;
- remaining assumptions or risks;
- recommended verification evidence.

Label the result `READY FOR PLAN` or `NOT READY`. Do not write implementation code or present a full implementation plan during this skill.
