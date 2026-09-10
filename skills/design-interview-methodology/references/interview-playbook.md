# System Design Interview Playbook

## Contents

- [Requirements prompts](#requirements-prompts)
- [Estimation prompts](#estimation-prompts)
- [High-level design checklist](#high-level-design-checklist)
- [Deep-dive menu](#deep-dive-menu)
- [Wrap-up checklist](#wrap-up-checklist)
- [Common failure patterns](#common-failure-patterns)
- [Evaluation rubric](#evaluation-rubric)

## Requirements prompts

Use only the prompts that can change the design.

### Functional scope

- Who are the actors, and what are their primary journeys?
- Which operations are in scope for the first design?
- What is explicitly out of scope?
- Are there administrative, moderation, analytics, or deletion flows?

### Quality attributes

| Attribute | Useful questions |
| --- | --- |
| Scale | How many active users, objects, and peak requests per second? What is the read/write ratio? |
| Latency | Which operations are interactive? What p50 or p99 target matters? |
| Availability | Which paths must remain available? Is degraded behavior acceptable? |
| Consistency | Which invariants require immediate agreement? Where is staleness acceptable, and for how long? |
| Durability | What data loss, if any, is acceptable? What retention or recovery target applies? |
| Geography | Are users or regulations region-specific? Is multi-region operation required? |
| Security | What authentication, authorization, privacy, tenancy, or abuse boundaries matter? |

### Phase exit checklist

- Core use cases and exclusions are agreed.
- Decision-relevant scale is estimated.
- The top two or three quality attributes are prioritized.
- Ambiguous facts are recorded as assumptions.

## Estimation prompts

Choose calculations that test feasibility or influence component choice:

- Average and peak reads or writes per second
- Storage per object and growth per day or year
- Ingress and egress bandwidth
- Cache working-set size and plausible hit rate
- Fan-out, shard count, or queue backlog under a spike

Show the equation and units. Round aggressively. Call out whether an estimate uses average or peak load. Use the result to make a design decision.

## High-level design checklist

### Public contract

- Sketch only the APIs or events needed for core flows.
- Include identity, pagination, idempotency, or error semantics when material.

### Data model

- Name primary entities and relationships.
- Identify access patterns before selecting indexes or partition keys.
- State which system is authoritative for each important datum.

### Component heuristics

| Component | Add when justified by |
| --- | --- |
| Load balancer | Multiple stateless instances or failure isolation |
| API gateway | Shared authentication, routing, quotas, or policy enforcement |
| CDN | Cacheable content served to geographically distributed users |
| Cache | Repeated reads, expensive computation, or a strict latency target |
| Queue or log | Asynchronous work, burst absorption, replay, or producer/consumer decoupling |
| Search index | Full-text, relevance ranking, or access patterns unsuitable for the source database |
| Object storage | Large immutable blobs or media |
| Read replica | Read scaling where replication lag is acceptable |
| Sharding | A demonstrated data or throughput limit that vertical scaling cannot meet |

### Flow narration

For each critical flow, identify entry point, validation, state changes, asynchronous boundaries, response point, and failure behavior.

## Deep-dive menu

| Topic | Questions to resolve |
| --- | --- |
| Database scaling | Partition key, hot spots, indexes, replication, resharding, and query patterns |
| Caching | Key design, population, invalidation, TTL, stampede control, and stale-read behavior |
| Consistency | Invariants, transaction boundary, conflicts, retries, idempotency, and reconciliation |
| Messaging | Delivery semantics, ordering scope, deduplication, retries, poison messages, and backpressure |
| Search | Indexing pipeline, freshness, ranking, filtering, and source-of-truth recovery |
| Rate limiting | Protected resource, limit scope, algorithm, distributed state, and fail-open/closed choice |
| Multi-region | Traffic routing, data placement, failover, split brain, recovery, and regulatory boundaries |

Evaluate options using requirements, complexity, operational burden, failure modes, cost, and an explicit evolution trigger.

## Wrap-up checklist

- Restate the architecture and the two most important decisions.
- Identify the first bottleneck at the stated scale and at roughly 10× scale.
- Describe behavior when a dependency is slow or unavailable.
- Surface data loss, staleness, duplicate-work, and security exposure.
- Name intentionally deferred features or infrastructure.
- Give the measurement or threshold that would trigger the next design change.

## Common failure patterns

| Pattern | Correction |
| --- | --- |
| Jumping to a solution | Clarify scope and constraints first. |
| Over-engineering | Start with a minimal design and justify every addition. |
| Vague scale claims | Estimate the load that matters to the decision. |
| Technology-first choices | Explain the capability required before naming an implementation. |
| Ignoring failure | Cover timeouts, retries, idempotency, degradation, and recovery where relevant. |
| No trade-offs | State the benefit, cost, rejected alternative, and reversal trigger. |
| Silent diagramming | Narrate each flow and assumption. |
| Running out of time | Compress the deep dive and preserve a deliberate wrap-up. |

## Evaluation rubric

Rate each dimension as **missing**, **developing**, **strong**, or **exceptional**. Support every rating with observed evidence.

1. **Problem framing:** Clarifies actors, scope, exclusions, and priorities.
2. **Quantitative reasoning:** Estimates the right quantities and uses them in decisions.
3. **Architecture:** Produces a coherent minimal system with complete core flows.
4. **Technical depth:** Defends detailed choices and invariants in critical areas.
5. **Trade-offs:** Compares alternatives and identifies costs and reversal triggers.
6. **Reliability and operations:** Covers failures, recovery, observability, and degradation.
7. **Communication:** Narrates clearly, responds to guidance, and manages time.

Conclude critique with the top three improvements in priority order and one concrete practice exercise for each.
