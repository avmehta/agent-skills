# Paired lesson contract

## Folder

Use `Lesson NN - descriptive topic/` unless the workspace already defines another convention.

Create:

- `lesson.html` — polished learner-facing narrative.
- `lesson.ipynb` — executable companion in the same conceptual order.
- `exercises.ipynb` — incomplete and debugging work; setup cells must run.
- `SOLUTIONS.ipynb` — complete answers with a prominent do-not-open warning.
- `literature.md` — verified local and primary sources, relevance, and publication status.
- `progress.md` — checkpoint evidence, mastery rubric, and exact resume point.
- `AUDIT.md` — audience, purpose, dependencies, provenance, and validation status for every file.
- `pyproject.toml` and lockfile when Python dependencies are needed.
- `assets/` only for lesson-specific assets; prefer course-level shared assets.

## Shared sequence

Both `lesson.html` and `lesson.ipynb` must use these stable IDs where applicable:

1. `s01-objective`
2. `s02-intuition`
3. `s03-formal-model`
4. `s04-derivation`
5. `s05-hand-example`
6. `s06-code`
7. `s07-checkpoints`
8. `s08-misconceptions`
9. `s09-literature`
10. `s10-exit-criteria`

HTML sections use matching `id` attributes. Notebook section headings include the ID in braces, for example `## Formal model {#s03-formal-model}`. Add links between corresponding artifacts using relative paths and anchors.

## HTML requirements

- Work offline when practical and avoid framework dependencies.
- Link a shared stylesheet rather than duplicating CSS.
- Use semantic headings, keyboard-accessible controls, visible focus states, sufficient contrast, descriptive link text, and alt text.
- Include print styles and fit comfortably at narrow widths.
- Put equations in readable notation. If a remote equation renderer is used, include a plain-text fallback and document the dependency.
- Include interactive widgets only when they produce a tighter feedback loop than a static question. Preserve usability when JavaScript is disabled.
- Cite claims near the relevant text and link the primary source.

## Notebook requirements

- Use Markdown cells for definitions and derivations and small code cells for one idea at a time.
- State expected tensor shapes beside equations and in code comments.
- Seed randomness; avoid hidden state; use relative paths; default to CPU.
- Restart the kernel and run all cells in order before delivery.
- Clear accidental large outputs and secrets. Keep intentional compact outputs that aid understanding.
- Do not rely on `SOLUTIONS.ipynb` or import code from it.

## Synchronization rules

The HTML explains and navigates; the notebook makes the same model executable. They need not duplicate every sentence, but must agree on:

- notation and assumptions;
- equation numbering and section IDs;
- dimensions and hand-calculated values;
- code outputs and conclusions;
- checkpoint IDs and exit criteria;
- citations and claim strength.

When revising one surface, audit the paired surface in the same change.

## Exercise and solution safety

- Give every item a stable ID such as `Q1-concept`, `Q2-derive`, or `Q3-debug`.
- Include conceptual, mathematical, code, debugging, transfer, and research/design tasks when relevant.
- Keep solutions only in `SOLUTIONS.ipynb` until an attempt.
- Check notebooks for hidden cells, stored outputs, metadata, comments, filenames, or imports that reveal answers.

## Required validation

1. Parse all notebooks as JSON.
2. Execute `lesson.ipynb` and the setup cells of `exercises.ipynb` from a clean environment.
3. Verify expected results and all hand calculations independently.
4. Confirm every required file and shared section ID exists.
5. Check relative links and local assets.
6. Render and visually inspect the HTML at desktop and narrow widths and in print preview when browser tooling is available.
7. Record commands, environment, date, and results in `AUDIT.md`.
