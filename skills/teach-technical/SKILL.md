---
name: teach-technical
description: Teach a technical, mathematical, scientific, or programming topic as a stateful course pairing every HTML lesson with a verified Jupyter notebook. Use when the learner asks for technical teaching, live Python/PyTorch examples, executable derivations, computational experiments, coding practice, or a lesson series that should include notebooks.
---

# Teach Technical

Specialize the active `teach-course` workflow for technical, mathematical, scientific, and programming instruction.

## Base teaching contract

Read and follow [the sibling teach-course skill](../teach-course/SKILL.md) completely, including its lesson contract. Preserve its governing context, paired-artifact structure, progress records, assets, live-teaching behavior, and mastery standard. When this skill adds a stricter technical requirement, use the stricter requirement.

## Technical workspace addition

Add `./notebooks/*.ipynb` to the teaching workspace. Every technical lesson must have one notebook with the same number and slug:

```text
lessons/0007-scaled-dot-product-attention.html
notebooks/0007-scaled-dot-product-attention.ipynb
```

The HTML lesson and notebook form one lesson. Link each to the other. Do not publish one half without the other unless the user explicitly asks for only one artifact.

## Workflow

1. Follow `teach-course` to establish the mission, prior learning evidence, and zone of proximal development.
2. Read `references/NOTEBOOK-CONTRACT.md` before designing or reviewing a notebook.
3. Design one tightly scoped win shared by the HTML lesson and notebook.
4. Write the HTML lesson for conceptual compression, derivation, primary-source grounding, and retrieval practice.
5. Write the notebook for live computation, inspection, modification, and immediate feedback. Do not merely copy the HTML prose into Markdown cells.
6. Run `scripts/validate_lesson_pair.py <lesson.html> <notebook.ipynb>`.
7. Execute the notebook from a clean kernel with an available Jupyter runner. Fix every unexpected error and inspect saved outputs. If execution is impossible, state that plainly; never call the notebook verified.
8. Open both artifacts for the learner when possible and ask them to return evidence from the practice cells.

## Pairing requirements

- Keep notation, terminology, assumptions, and tensor-shape conventions consistent across both artifacts and the course glossary.
- Make every notebook deterministic where practical: seed randomness and state device/dtype assumptions.
- Use small CPU-friendly examples first. Add GPU experiments only when they materially teach systems behavior.
- Show intermediate values and shapes, not only final outputs.
- Require a prediction before important cells are run.
- Include at least one learner modification or implementation task and an immediate, execution-safe feedback check.
- Include a final retrieval prompt that asks the learner to explain observed behavior without reading the output.
- Cite the same primary source used by the HTML lesson.
- Record demonstrated learning only after the learner returns evidence; notebook coverage alone is not mastery.

## Verification standard

Validation checks structure; execution checks behavior. Both are required. Use the workspace's intended Python environment when known. Keep execution outputs in the delivered notebook when they help the learner compare results; clear noisy, machine-specific, or irrelevant output.
