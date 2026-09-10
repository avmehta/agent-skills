---
name: create-lesson
description: Create the next rigorous, interactive lesson in Avi's six-month language-model and staff-MLE curriculum. Use when asked to generate, build, draft, revise, or continue a numbered lesson in LLM_COURSE_ROOT, including lesson notes, math, runnable code, exercises, literature, and mastery checks.
---

# Create Lesson

## Portable workspace resolution

Resolve `LLM_COURSE_ROOT` from the workspace explicitly selected in the request, then the environment variable of that name, then the current workspace if it contains the curriculum, otherwise `Documents/LLMs` under the current user's home directory. Use the resolved path wherever this skill names `LLM_COURSE_ROOT`; never treat the variable name as a literal directory. On Windows use the actual user-home path, not a POSIX home path.

The course and its reference data are separate from this installed skill. Inspect the selected course's instructions before creating or changing files. If required material is missing, report the missing dependency rather than inventing it.

Resolve `GPT_REFERENCE_ROOT` and `AI_REFERENCE_ROOT` from their environment variables, otherwise from `Documents/git_repos/how-to-train-your-gpt` and `Documents/education/ai` under the current user's home. Preserve any stricter source requirements in the course instructions.

Create one cumulative lesson at a time. Follow `LLM_COURSE_ROOT/AGENTS.md` as the governing teaching specification.

## Workflow

1. Inspect existing `Lesson NN - topic/` folders and select the next two-digit number. Use the user’s requested topic; otherwise choose the next prerequisite from the curriculum and briefly explain the dependency.
2. Review the learner’s prior answers, tracked gaps, and previous lesson’s exit criteria when available. Make reasonable assumptions when Lesson 1 has no history.
3. Inspect relevant material in:
   - `GPT_REFERENCE_ROOT`
   - `AI_REFERENCE_ROOT`
4. Search the web for primary literature. Include foundational work and relevant recent follow-up, replication, or critique. Verify titles, authors, years, publication status, and direct links. Distinguish preprints from peer-reviewed work.
5. Create the lesson folder inside `LLM_COURSE_ROOT`. Read [lesson-format.md](references/lesson-format.md) and produce all required files.
6. Make the learner-facing lesson conversational. Stop at checkpoints and ask for a response; do not expose solutions before an attempt unless the learner requests them.
7. Test every code file. Check imports, deterministic seeds, tensor shapes, assertions, expected output, and CPU compatibility unless GPU use is essential.
8. Check every worked calculation independently. Define symbols and keep dimensions explicit.
9. Verify all internal file links and summarize what was created. Begin the live lesson with the first checkpoint rather than dumping the answer key into the conversation.

## Quality Gates

- Teach each core idea through an ELI5 analogy with stated limits, a precise formulation, math, a hand calculation, and runnable code.
- Use short conversational stages rather than one uninterrupted lecture.
- Include conceptual, derivation, code, debugging, transfer, paper-analysis, and staff-level follow-up questions where appropriate.
- Keep solutions in a separate file and clearly mark it as locked until an attempt.
- Connect code lines to equations and annotate tensor shapes.
- Include misconceptions, failure modes, compute and memory costs, and concrete tradeoffs.
- Cite local paths actually inspected and web sources actually verified.
- End with measurable exit criteria and the next lesson’s dependency.
- Prefer depth and complete understanding over excessive topic coverage.
