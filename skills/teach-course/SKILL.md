---
name: teach-course
description: Create, revise, and teach rigorous stateful lessons that pair a polished standalone HTML lesson with executable Jupyter notebooks. Use when the user asks to learn a topic, create or continue a numbered lesson, build both HTML and notebook lesson materials, run a lesson interactively, resume prior learning, assess mastery, or maintain a cumulative course workspace.
---

# Teach Course

## Portable workspace resolution

Resolve `LLM_COURSE_ROOT` from the workspace explicitly selected in the request, then the environment variable of that name, then the current workspace if it contains the curriculum, otherwise `Documents/LLMs` under the current user's home directory. Use the resolved path wherever this skill names `LLM_COURSE_ROOT`; never treat the variable name as a literal directory. On Windows use the actual user-home path, not a POSIX home path.

The course and its reference data are separate from this installed skill. Inspect the selected course's instructions before creating or changing files. If required material is missing, report the missing dependency rather than inventing it.

Create durable lesson artifacts and teach them live. Treat the files as the course record and the conversation as the classroom.

## Governing context

1. Read the workspace's `AGENTS.md` and curriculum or mission files before acting.
2. Preserve local naming and structure when a course already exists.
3. For `LLM_COURSE_ROOT`, follow `AGENTS.md`, `CURRICULUM_PLAN.md`, and the required local reference-material rules.
4. Use current primary sources when claims may have changed. Separate evidence, inference, and speculation.

## Choose the mode

- **Create or revise:** Build or update the complete paired lesson artifact.
- **Teach, continue, resume, or review:** Read the lesson and progress state, then conduct a live interactive session.
- **Unspecified:** Infer from the request. If the requested lesson does not exist, create it, then begin teaching at its first checkpoint.

## Create the paired lesson

Read [references/lesson-contract.md](references/lesson-contract.md) completely before creating or revising a lesson.

1. Inspect existing lessons, learner records, prior answers, open gaps, and the previous exit criteria.
2. Inspect relevant local source material required by the workspace. Do not modify reference repositories unless explicitly asked.
3. Research foundational and current primary literature. Verify titles, authors, dates, publication status, direct links, and important critiques or replications.
4. Create one tightly scoped lesson with two coordinated surfaces:
   - `lesson.html`: polished, self-contained conceptual narrative, derivations, diagrams, checkpoints, citations, and links into the notebooks.
   - `lesson.ipynb`: executable derivations, numerical examples, visualizations, experiments, and code walkthroughs in the same sequence and notation.
5. Create learner exercises and locked worked solutions as separate notebooks. Never place solution code in learner-visible notebook metadata, outputs, HTML comments, or hidden cells.
6. Keep HTML and notebook synchronized by stable section IDs such as `s01-intuition`, `s02-formal-model`, and `s03-derivation`. Cross-link corresponding sections.
7. Use shared assets from the course before creating new ones. For a new workspace, begin with `assets/course.css`; adapt [assets/course.css](assets/course.css) rather than duplicating styles inline.
8. Test every notebook from a clean kernel. Verify imports, seeds, dimensions, assertions, expected outputs, CPU compatibility, and numerical calculations.
9. Run `scripts/validate_lesson.py <lesson-folder>`. Fix every reported error before delivery.
10. Record provenance and validation status in `AUDIT.md`, then begin the live lesson at the first unresolved checkpoint.

## Teach live

1. Read `lesson.html`, `lesson.ipynb`, `exercises.ipynb`, and `progress.md`. Do not open `SOLUTIONS.ipynb` until grading an attempted item or when the learner explicitly asks.
2. State the immediate objective and expected stopping point in two or three sentences.
3. Teach one coherent idea per turn. End most turns with one focused prediction, derivation, calculation, code task, or explanation request and wait.
4. Start with an ELI5 model and explicitly mark its limits. Then define every symbol, track dimensions, derive transitions, calculate a small example, and connect equations to executable cells and behavior.
5. Diagnose the first incorrect reasoning step. Give the smallest useful hint, allow another attempt, then show a complete worked solution when appropriate.
6. Require explanation, derivation, implementation, debugging, transfer, paper critique, and design defense before declaring mastery.
7. Handle interruptions directly. Resolve clarifications and prerequisite gaps, record valuable tangents, and return to the last unresolved checkpoint.
8. Use the notebook interactively: ask for predictions before running cells and compare observed results with the learner's model.

## Preserve learning state

At a pause or natural checkpoint:

1. Update `progress.md` with evidence, misconceptions, completed checkpoints, current mastery state, and the exact resume point.
2. Add a learning record for a durable non-obvious insight or a changed learning strategy.
3. Give at most one small retrieval task unless more homework is requested.
4. Resume later with a recall question, not a replay of completed exposition.

Use mastery states: `not assessed`, `learning`, `can solve with hints`, `independent`, and `interview-ready`. Award the last state only after delayed, from-memory math, code, debugging, transfer, and follow-up questioning.

## Quality bar

- Design for the learner's demonstrated zone of proximal development and mission.
- Keep each lesson finishable in the workspace's stated time box.
- Prefer depth over topic count; track unfinished work explicitly.
- Include ELI5 intuition and limits, precise formulation, full derivation, hand calculation, runnable code, misconceptions, complexity, failure modes, literature, exercises, and measurable exit criteria.
- Make HTML readable, accessible, responsive, printable, and useful without a server.
- Make notebooks linear, restartable, deterministic, and free of unexplained state.
- Keep terminology, equations, tensor shapes, examples, and checkpoint numbering identical across surfaces.
