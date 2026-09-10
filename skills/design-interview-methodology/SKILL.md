---
name: design-interview-methodology
description: Guide system design interview preparation and practice with a timed four-phase framework covering requirements, high-level design, focused deep dives, and wrap-up. Use when Codex needs to coach, structure, critique, or facilitate a system design interview, whiteboard architecture exercise, mock interview, or time-boxed architectural discussion.
---

# Design Interview Methodology

Use a requirements-first, evidence-driven process. Keep the design proportional to the stated scale, narrate the reasoning, and make every major decision expose its trade-off.

## Choose the interaction style

Infer the style from the request:

- **Facilitate:** Move through the framework interactively. Ask one focused group of questions at a time and wait for the candidate's answer.
- **Coach:** Explain what to do next, offer prompts or hints, and critique the candidate's reasoning without taking over the design.
- **Demonstrate:** Produce a complete worked design while explicitly walking through all four phases.
- **Review:** Map an existing answer onto the four phases, identify missing evidence, and prioritize the highest-impact improvements.

If the request is ambiguous, default to coaching. Do not silently answer the interview for a candidate who is practicing interactively.

## Run the four phases

Use these time budgets for a 45–60 minute session. Scale them proportionally when the available time differs.

| Phase | Time | Outcome |
| --- | ---: | --- |
| 1. Requirements | 5–10 min | Agreed scope, scale, and quality targets |
| 2. High-level design | 10–15 min | Major components, APIs, data model, and end-to-end flows |
| 3. Deep dive | 15–20 min | Defensible detail on one or two critical design risks |
| 4. Wrap-up | 5–10 min | Bottlenecks, trade-offs, failure handling, and evolution path |

### 1. Establish requirements

Clarify the smallest useful functional scope before proposing components. Establish scale, traffic shape, latency, availability, consistency, durability, geography, retention, privacy, and abuse constraints only where they materially affect the design.

Perform back-of-the-envelope calculations when scale influences architecture. State assumptions, units, and arithmetic. Prefer a few decision-relevant estimates—peak requests per second, storage growth, bandwidth, or fan-out—over exhaustive math.

Do not advance until the core use cases and the most important non-functional constraints are explicit. When the interviewer leaves facts unspecified, make a reasonable assumption and say what decision it affects.

### 2. Build the high-level design

Start with the simplest end-to-end architecture that satisfies the agreed requirements. Add components only in response to a named constraint or failure mode.

Cover:

1. The public contract: key APIs or events.
2. The minimum data model and important indexes or partition keys.
3. The main write and read paths, narrated step by step.
4. Trust boundaries, ownership boundaries, and asynchronous work.
5. A visible connection between each non-obvious component and the requirement that justifies it.

Keep the diagram readable. Avoid decorating it with every familiar infrastructure component.

### 3. Deep-dive on critical risks

Let the interviewer choose the topic when they signal a preference. Otherwise select one or two areas that are both architecturally risky and central to the requirements, such as database scaling, cache correctness, consistency, ordering, hot partitions, search, rate limiting, or multi-region failover.

For each deep dive:

1. Define the invariant or target.
2. Compare at least two viable approaches.
3. Choose one and explain why it fits the current scale and constraints.
4. Cover normal flow, failure behavior, recovery, and observability.
5. Quantify the trade-off when credible numbers can be derived; do not invent precise figures.

### 4. Wrap up deliberately

Reserve time to summarize the design rather than ending mid-component. Identify the first likely bottleneck, the trigger that would require redesign, and the next scaling step. Revisit the most consequential trade-offs, degradation behavior, data loss or consistency exposure, and important edge cases.

Close with a concise evolution path: what is intentionally deferred now, and what evidence would justify adding it later.

## Maintain strong interview behavior

- Narrate assumptions and reasoning; do not design silently.
- Tie technology choices to requirements instead of naming favorite products.
- Follow interviewer redirection promptly.
- Recover from uncertainty by stating what is known, reasoning from constraints, and moving on when needed.
- Prefer explicit trade-offs to claims that one option is universally best.
- Track time and compress later phases gracefully rather than omitting the wrap-up.

Read [references/interview-playbook.md](references/interview-playbook.md) when you need detailed question prompts, component-selection heuristics, phase checklists, common failure patterns, or a scoring rubric.

## Shape the response

For an interactive session, keep each turn focused and end with the next candidate decision or question. For a worked answer, label the four phases and make assumptions auditable. For critique, separate observations from recommended fixes and rank fixes by interview impact.

Do not mistake maximal architecture for a strong answer. Evaluate whether the reasoning is structured, requirements-linked, quantitative where useful, failure-aware, and candid about trade-offs.
