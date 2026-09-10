# Personal agent skills

Avi's portable collection of **23 personal skills**, including the planning-first, contrarian-review and socratic-planning workflows. Those three skills are preserved byte-for-byte from the source snapshot, including their UI metadata.

Clone this repository anywhere. The installer uses Python's standard library and copies complete skill folders into the current system's `~/.agents/skills` directory. It does not require symlinks, administrator access, npm or a package manager.

## Install on macOS or Linux

Install Git, Python 3.10+ and Codex first. Authenticate with GitHub to access this private repository; `gh auth login` is one option if GitHub CLI is installed.

```sh
git clone https://github.com/avmehta/agent-skills.git
cd agent-skills
python3 install.py --dry-run
python3 install.py --with-global-instructions
```

`--with-global-instructions` appends the included planning agreement to `$CODEX_HOME/AGENTS.md` (default `~/.codex/AGENTS.md`). It preserves unrelated instructions and saves a backup when changing an existing file. Omit the flag if you only want the skills. An existing, different planning block is left untouched and must be reconciled manually.

## Install on Windows

Install Git, Python 3.10+ and Codex. In PowerShell:

```powershell
git clone https://github.com/avmehta/agent-skills.git
cd agent-skills
py -3 install.py --dry-run
py -3 install.py --with-global-instructions
```

If Python is available as `python` rather than `py -3`, use that command. The installer chooses your Windows home directory automatically. Installation does not make macOS-specific helper programs available on Windows; see [dependencies](docs/DEPENDENCIES.md).

## Update after pulling

```sh
git pull --ff-only
python3 install.py --update
```

On Windows, use `py -3 install.py --update`. Re-run with `--with-global-instructions` only if you also want to check/install that agreement.

The installer compares installed copies with its previous manifest before updating. It refuses to overwrite locally modified or unrelated folders. Identical existing skills can be adopted without changing their contents. Resolve a conflict by comparing the installed copy with this repository, preserving any edits, and moving the conflicting copy to your own backup location before reinstalling. There is deliberately no force-overwrite option.

Run one installer at a time for a given destination. The rollback handles ordinary write failures, not abrupt machine shutdowns; keep your Git checkout as the recoverable source.

Treat this Git checkout as the source of truth: edit skills here, commit/push, then update the installed copies. Edits made directly in an installed copy do not automatically sync back to Git.

## Smaller or custom installations

```sh
# Planning trio plus wrap-up, research and code-review (6 skills)
python3 install.py --profile core --with-global-instructions

# List without writing
python3 install.py --list

# Use another agent's supported skill directory, or a project-scoped Codex directory
python3 install.py --dest /path/to/project/.agents/skills
```

Changing profiles never removes existing skills. A core-only update only updates that profile. Existing installations in both `~/.agents/skills` and `~/.codex/skills` can create duplicate names; this installer does not relocate or delete the old copies. Reconcile duplicates manually after backing up and comparing them.

Codex's documented personal discovery path is `~/.agents/skills`. See [the official skill documentation](https://learn.chatgpt.com/docs/build-skills). If a new skill does not appear, restart Codex. Other agents may read this skill format, but their tool names and behavior are not verified by this repository.

## Collection

| Area | Skills |
|---|---|
| Planning | planning-first, socratic-planning, contrarian-review, grilling |
| Engineering | code-review, codebase-design, diagnosing-bugs, domain-modeling, prototype, repository-preserving-migration, resolving-merge-conflicts, wrap-up |
| Research and browsing | research, notebooklm, playwright-cli |
| Presentation | lavish |
| Learning and interviews | create-lesson, teach-lesson, teach-course, teach-technical, design-interview-methodology, system-design |
| Chart analysis | tradingview-chart-analysis |

## Portability and scope

- Includes all supporting files from the 23 personal skill directories.
- Removes machine-specific `/Users/...` dependencies from the teaching skill copies using configurable workspace roots and a relative sibling-skill reference. Teaching behavior and competing lesson formats were not redesigned.
- Course repositories, reference collections and learner progress are separate data. Point teaching skills at your own copies; see [dependencies and paths](docs/DEPENDENCIES.md).
- Bundled Codex skills and plugin caches are excluded. Reinstall their owning plugins in the target app and authenticate each account separately. A skill file alone does not install a connector or runtime.
- Credentials, browser state, account tokens, models and datasets are excluded. Shell examples naming credential environment variables are documentation, not saved credentials.

## Verify

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The installer tests run only in temporary directories. They cover complete copying, idempotence, safe updates, modified-file protection, global instruction preservation, paths with spaces and rollback. They do not prove that every external CLI or skill workflow works on every OS.

See [provenance](docs/PROVENANCE.md), [scope and verification plan](docs/PLAN.md), and [current status](docs/STATUS.md).
