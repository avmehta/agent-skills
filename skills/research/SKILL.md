---
name: research
description: Investigate a repository or technical decision using high-trust primary sources and produce evidence-backed findings. Use for API facts, implementation comparisons, technology assessments, or reading legwork; use specialized OpenAI, academic, or deep-research skills when those narrower workflows apply.
---

# Research

Answer the decision the user actually needs to make. Work directly by default. Delegate only when the user or active instructions authorize it and parallel research would materially help.

## Workflow

1. State the question, decision, current baseline, and what evidence would change the recommendation.
2. Inspect relevant repository code and project documentation when the decision affects an existing system.
3. Use primary sources: official documentation, specifications, papers, source repositories, release notes, or first-party APIs. Use secondary sources only for clearly labeled context or field experience.
4. Separate evidence, inference, and uncertainty. Verify facts that may have changed.
5. When comparing technologies or models:
   - confirm benchmark protocols are actually comparable;
   - compare candidates with the project's real, possibly modified baseline;
   - include integration, migration, retraining, licensing, hardware, latency, and operational costs;
   - prefer an application-specific bakeoff when general benchmarks cannot answer the product question.
6. Recommend keep, adopt, trial, or reject, with the smallest next experiment and explicit success metrics.

Persist a concise Markdown decision memo when the user requests it or project instructions require durable research. Match the repository's documentation convention and cite claims near their sources. Do not create a file for a simple answer merely because this skill was invoked.

