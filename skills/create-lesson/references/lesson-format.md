# Required Lesson Folder Format

Use `Lesson NN - descriptive topic/` with two-digit numbering so lessons sort correctly. Do not use a bare `lesson 1` name unless the user explicitly insists on that exact spelling.

Create:

- `README.md`: learner-facing lesson in conversational stages. Include objectives, prerequisites, ELI5 model and its limits, formal model, derivation, hand example, code walkthrough, checkpoints, misconceptions, literature, exit criteria, and next step.
- `AUDIT.md`: manifest explaining why every file exists, its audience, dependencies, provenance, and validation status.
- `lesson.ipynb`: executable teaching notebook tied directly to the lesson’s equations.
- `exercises.ipynb`: incomplete or faulty code for the learner to finish or debug. Definitions may contain placeholders, but setup cells must execute cleanly.
- `SOLUTIONS.ipynb`: worked conceptual, mathematical, and code answers. Begin with a warning not to open it before attempting the checkpoints.
- `literature.md`: verified local sources and primary literature, with why each source matters and publication status.
- `progress.md`: mastery rubric with `not assessed`, `learning`, `can solve with hints`, `independent`, and `interview-ready`; leave initial assessment honest rather than pre-awarding mastery.
- `pyproject.toml` and `uv.lock`: a reproducible uv-managed environment for notebooks and lesson code.

Prefer Jupyter notebooks for teaching code unless the user requests scripts. Manage Python dependencies and commands with uv. Use relative links among files. Keep dependencies minimal and list `uv sync` and `uv run` commands near the start of `README.md`. Put optional extension material after the core mastery gate.

Design the live flow so `README.md` explicitly tells the learner where to stop and answer. Each stop should ask one focused question or a tightly related mini-set whose response determines the next move.
