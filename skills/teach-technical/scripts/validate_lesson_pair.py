#!/usr/bin/env python3
"""Validate the structural contract for a Teach Technical lesson pair."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def cell_text(cell: dict) -> str:
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else str(source)


def main() -> None:
    if len(sys.argv) != 3:
        fail("usage: validate_lesson_pair.py LESSON.html NOTEBOOK.ipynb")

    lesson = Path(sys.argv[1])
    notebook = Path(sys.argv[2])
    if not lesson.is_file():
        fail(f"lesson does not exist: {lesson}")
    if not notebook.is_file():
        fail(f"notebook does not exist: {notebook}")
    if lesson.stem != notebook.stem:
        fail(f"stems differ: {lesson.stem!r} != {notebook.stem!r}")
    if not re.fullmatch(r"\d{4}-[a-z0-9]+(?:-[a-z0-9]+)*", lesson.stem):
        fail("pair stem must be NNNN-lowercase-dash-case")

    try:
        data = json.loads(notebook.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid notebook JSON: {exc}")

    if data.get("nbformat") != 4:
        fail("notebook must use nbformat 4")
    cells = data.get("cells")
    if not isinstance(cells, list) or not cells:
        fail("notebook must contain cells")
    markdown = [cell_text(c) for c in cells if c.get("cell_type") == "markdown"]
    code = [cell_text(c) for c in cells if c.get("cell_type") == "code"]
    if not markdown:
        fail("notebook needs Markdown guidance")
    if len(code) < 3:
        fail("notebook needs at least three code cells")
    joined_markdown = "\n".join(markdown).lower()
    for label in ("prediction", "practice", "retrieval", "primary source"):
        if label not in joined_markdown:
            fail(f"missing required notebook section: {label}")

    html = lesson.read_text(encoding="utf-8")
    if notebook.name not in html:
        fail("HTML lesson does not link to its notebook")
    if lesson.name not in "\n".join(markdown):
        fail("notebook does not link to its HTML lesson")

    print(f"OK: valid Teach Technical pair: {lesson.name} + {notebook.name}")


if __name__ == "__main__":
    main()
