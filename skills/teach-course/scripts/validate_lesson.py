#!/usr/bin/env python3
"""Validate the structural contract of a paired HTML/Jupyter lesson."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

FILES = {
    "lesson.html", "lesson.ipynb", "exercises.ipynb", "SOLUTIONS.ipynb",
    "literature.md", "progress.md", "AUDIT.md",
}
SECTIONS = [
    "s01-objective", "s02-intuition", "s03-formal-model", "s04-derivation",
    "s05-hand-example", "s06-code", "s07-checkpoints", "s08-misconceptions",
    "s09-literature", "s10-exit-criteria",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_lesson.py LESSON_FOLDER", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).resolve()
    errors: list[str] = []
    for name in sorted(FILES):
        if not (root / name).is_file():
            errors.append(f"missing required file: {name}")

    html = (root / "lesson.html").read_text(encoding="utf-8") if (root / "lesson.html").is_file() else ""
    notebooks: dict[str, dict] = {}
    for name in ("lesson.ipynb", "exercises.ipynb", "SOLUTIONS.ipynb"):
        path = root / name
        if not path.is_file():
            continue
        try:
            notebooks[name] = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f"invalid notebook {name}: {exc}")

    lesson_text = "\n".join(
        "".join(cell.get("source", []))
        for cell in notebooks.get("lesson.ipynb", {}).get("cells", [])
    )
    for section in SECTIONS:
        if not re.search(rf"\bid=[\"']{re.escape(section)}[\"']", html):
            errors.append(f"lesson.html missing section id: {section}")
        if section not in lesson_text:
            errors.append(f"lesson.ipynb missing section id: {section}")

    solutions = notebooks.get("SOLUTIONS.ipynb", {})
    solution_text = "\n".join(
        "".join(cell.get("source", [])) for cell in solutions.get("cells", [])
    ).lower()
    if solutions and not any(term in solution_text[:1200] for term in ("warning", "do not open", "attempt")):
        errors.append("SOLUTIONS.ipynb needs an opening attempt-first warning")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Structural validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
