# Notebook contract

Read this file whenever creating or reviewing a notebook for `teach-technical`.

## Required sequence

1. **Title and pairing link** — match the HTML lesson's number and slug and link back to it.
2. **Observable win** — state one thing the learner will calculate, implement, diagnose, or experimentally establish.
3. **Setup** — minimal imports, deterministic seed, device/dtype declaration, and no hidden state from earlier notebooks.
4. **Prediction** — ask for a concrete prediction before the first revealing computation.
5. **Worked experiment** — translate the lesson's core equation or algorithm into transparent Python/PyTorch.
6. **Inspection** — print or visualize intermediate values, shapes, invariants, or gradients.
7. **Practice** — require the learner to modify or complete something. Starter cells must remain safe to execute in their initial state.
8. **Feedback** — check shape, value, invariant, gradient, or behavior immediately. Report incomplete work without crashing the clean execution run.
9. **Perturbation** — change one assumption or parameter and ask the learner to explain the result.
10. **Retrieval** — end with one short explanation prompt answered away from the preceding prose.
11. **Primary source** — link the paper, official documentation, or other high-trust source that grounds the lesson.

## Cell design

- Prefer many small, named computations over one opaque cell.
- Explain why code exists; do not narrate obvious syntax.
- Keep mathematical symbols aligned with variable names where readable (`Q`, `K`, `V`, `d_k`).
- State shapes next to equations and assert important contracts in code.
- Use `torch.testing.assert_close` for numerical equivalence and explicit checks for shape or normalization invariants.
- Never require secrets, network access, or paid compute for a foundational lesson.
- Avoid heavyweight dependencies when NumPy, PyTorch, Matplotlib, or the standard library suffices.

## Safe practice pattern

An unattempted exercise must not make notebook verification fail. Initialize the learner result to `None` or use a syntactically valid placeholder, then have the feedback cell print a specific next step when incomplete. Once attempted, the same feedback cell should distinguish a wrong result from a correct one.

```python
learner_output = None  # Replace with your implementation.

if learner_output is None:
    print("Not attempted yet: construct the [T, T] score matrix.")
elif learner_output.shape != expected.shape:
    print(f"Shape mismatch: expected {expected.shape}, got {learner_output.shape}.")
else:
    torch.testing.assert_close(learner_output, expected)
    print("Correct — now explain why the last two axes have these sizes.")
```

Do not place a complete solution immediately above the practice cell. A worked example may use smaller data or a different case without making the target task a copy exercise.

## Execution check

Execute from top to bottom in a fresh kernel. Confirm:

- no unexpected exceptions or dependence on out-of-order state;
- output values support the claims in the HTML lesson;
- expected tensor shapes and invariants are visible;
- practice feedback is helpful in its untouched state;
- runtime is proportionate to a compact lesson;
- saved outputs contain no local paths, credentials, personal data, or irrelevant logs.
