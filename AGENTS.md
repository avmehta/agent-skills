# Working on this collection

Preserve the user's planning-first, contrarian-review and socratic-planning workflows. Packaging or portability work does not authorize changing their decision process or applying recommendations from an earlier audit.

Keep every skill with its referenced files and helpers. Preserve existing upstream attribution. Do not copy credentials, account state, course progress, datasets, plugin caches or system skills into this repository.

For substantive behavioral changes, inspect, clarify unresolved decisions, write a concrete plan, challenge it proportionately and obtain approval before implementation unless the user already approved that scope. Honor explicit waivers. Routine packaging and verification should remain proportional.

Run `python scripts/validate.py` and `python -m unittest discover -s tests -v` after packaging or installer changes. Test installations in temporary directories, never against the contributor's live skills. Verify source/remote status before claiming a push or release completed.

Use `docs/STATUS.md` for a concise, truthful checkpoint and exact next action. Do not add personal memory, raw logs or secrets to it.
