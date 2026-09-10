#!/usr/bin/env python3
"""Install the personal skill collection using only Python's standard library."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
STATE_NAME = '.agent-skills-install.json'
CORE = {'planning-first', 'socratic-planning', 'contrarian-review', 'wrap-up', 'research', 'code-review'}
BEGIN = '<!-- BEGIN planning-first-agent-kit -->'
END = '<!-- END planning-first-agent-kit -->'


def digest(folder: Path) -> str:
    """Hash relative paths and bytes; reject symlinked content."""
    if folder.is_symlink() or not folder.is_dir():
        raise ValueError(f'Expected a real skill directory: {folder}')
    result = hashlib.sha256()
    for path in sorted(folder.rglob('*')):
        if path.name == '.DS_Store' or '__pycache__' in path.parts or path.suffix == '.pyc':
            continue
        if path.is_symlink():
            raise ValueError(f'Refusing symlink inside skill: {path}')
        if path.is_file():
            result.update(path.relative_to(folder).as_posix().encode('utf-8') + b'\0')
            result.update(path.read_bytes() + b'\0')
    return result.hexdigest()


def instructions_change(path: Path) -> tuple[str, str] | None:
    """Append the requested block, preserving unrelated global instructions."""
    if path.is_symlink():
        raise ValueError(f'Refusing to edit symlinked instructions: {path}')
    existing = path.read_text(encoding='utf-8') if path.exists() else ''
    template = (ROOT / 'templates' / 'planning-first-AGENTS.md').read_text(encoding='utf-8').strip()
    if BEGIN in existing or END in existing:
        if existing.count(BEGIN) != 1 or existing.count(END) != 1:
            raise ValueError(f'Ambiguous planning markers in {path}; reconcile manually.')
        start, end = existing.index(BEGIN), existing.index(END) + len(END)
        if existing[start:end].strip() != template:
            raise ValueError(f'A different planning agreement exists in {path}; reconcile manually.')
        return None
    return existing, existing.rstrip() + ('\n\n' if existing.strip() else '') + template + '\n'


def install(destination: Path, names: list[str], update: bool = False,
            dry_run: bool = False, agents_file: Path | None = None) -> list[str]:
    destination = destination.expanduser().absolute()
    if destination.is_symlink():
        raise ValueError(f'Refusing a symlinked install root: {destination}')
    state_path = destination / STATE_NAME
    if state_path.is_symlink():
        raise ValueError(f'Refusing symlinked install state: {state_path}')
    state = json.loads(state_path.read_text(encoding='utf-8')) if state_path.exists() else {'version': 1, 'skills': {}}
    if state.get('version') != 1 or not isinstance(state.get('skills'), dict):
        raise ValueError('Unsupported installation state; no files changed.')
    planned = []
    hashes = dict(state['skills'])
    messages = []
    # Preflight every selected destination and instructions file before writing.
    for name in names:
        source = ROOT / 'skills' / name
        wanted = digest(source)
        target = destination / name
        if target.exists() or target.is_symlink():
            current = digest(target)
            if current == wanted:
                hashes[name] = wanted
                messages.append(f'Unchanged: {name}')
                continue
            if not update:
                raise ValueError(f'{target} differs. Use --update for a previously managed installation.')
            if state['skills'].get(name) != current:
                raise ValueError(f'{target} is unmanaged or locally modified. Preserve/reconcile it manually; no files changed.')
            messages.append(f'Update: {name}')
        else:
            messages.append(f'Install: {name}')
        planned.append((source, target))
        hashes[name] = wanted
    agent_change = instructions_change(agents_file) if agents_file else None
    if agent_change:
        messages.append(f'Append planning agreement: {agents_file}')
    if dry_run:
        return ['Dry run; no files changed.'] + messages
    destination.mkdir(parents=True, exist_ok=True)
    # Stage on the destination filesystem; keep originals until the state commit.
    with tempfile.TemporaryDirectory(prefix='.agent-skills-stage-', dir=destination) as scratch:
        stage = Path(scratch)
        for source, target in planned:
            shutil.copytree(source, stage / target.name,
                            ignore=shutil.ignore_patterns('.DS_Store', '__pycache__', '*.pyc'))
        moved = []
        agents_backup = None
        agents_written = False
        try:
            for _, target in planned:
                backup = stage / (target.name + '.previous')
                had_original = target.exists()
                if had_original:
                    target.rename(backup)
                moved.append((target, backup, had_original))
                (stage / target.name).rename(target)
            if agent_change and agents_file:
                agents_file.parent.mkdir(parents=True, exist_ok=True)
                if agents_file.exists():
                    fd, backup_name = tempfile.mkstemp(prefix=agents_file.name + '.backup-', dir=agents_file.parent)
                    os.close(fd)
                    agents_backup = Path(backup_name)
                    shutil.copy2(agents_file, agents_backup)
                agents_written = True
                agents_file.write_text(agent_change[1], encoding='utf-8')
            staged_state = stage / STATE_NAME
            staged_state.write_text(json.dumps({'version': 1, 'skills': hashes}, indent=2) + '\n', encoding='utf-8')
            os.replace(staged_state, state_path)
        except Exception:
            for target, backup, had_original in reversed(moved):
                if target.exists():
                    shutil.rmtree(target)
                if had_original:
                    backup.rename(target)
            if agents_written and agents_file:
                if agents_backup:
                    shutil.copy2(agents_backup, agents_file)
                elif agents_file.exists():
                    agents_file.unlink()
            raise
    if agents_backup:
        messages.append(f'Global instructions backup: {agents_backup}')
    return messages + [f'Ready: {len(names)} skills at {destination}',
                       'If skills do not appear, restart Codex. External tools/plugins require separate setup.']


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path, default=Path.home() / '.agents' / 'skills', help='Install root (default: ~/.agents/skills)')
    parser.add_argument('--profile', choices=['all', 'core'], default='all', help='Core installs the planning trio, wrap-up, research and code-review')
    parser.add_argument('--update', action='store_true', help='Update only managed, unmodified skill copies after git pull')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--list', action='store_true', help='List selected skills without installing')
    parser.add_argument('--with-global-instructions', action='store_true', help='Append the planning agreement to the selected global AGENTS.md, without replacing existing content')
    parser.add_argument('--agents-file', type=Path, default=Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'AGENTS.md')
    args = parser.parse_args()
    names = sorted(p.name for p in (ROOT / 'skills').iterdir() if (p / 'SKILL.md').is_file() and (args.profile == 'all' or p.name in CORE))
    if args.list:
        print('\n'.join(names))
        return 0
    try:
        for line in install(args.dest, names, args.update, args.dry_run,
                            args.agents_file.expanduser().absolute() if args.with_global_instructions else None):
            print(line)
    except (ValueError, OSError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
