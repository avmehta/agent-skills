#!/usr/bin/env python3
"""Validate package structure, local links and preservation; no third-party modules."""

import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FAVORITES = {'planning-first', 'contrarian-review', 'socratic-planning'}
PORTABLE = {'create-lesson', 'teach-lesson', 'teach-course', 'teach-technical'}


def main():
    failures = []
    snapshot = json.loads((ROOT / 'docs/source-snapshot.json').read_text(encoding='utf-8'))['skills']
    actual_names = {p.name for p in (ROOT / 'skills').iterdir() if p.is_dir()}
    expected_names = {r['name'] for r in snapshot}
    if actual_names != expected_names or len(actual_names) != 23:
        failures.append('Skill names/count differ from the 23-skill source snapshot')
    checked_links = 0
    for entry in snapshot:
        skill = ROOT / 'skills' / entry['name']
        source_files = {f['path']: f['sha256'] for f in entry['files']}
        current_files = {p.relative_to(skill).as_posix() for p in skill.rglob('*')
                         if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
        if current_files != set(source_files):
            failures.append(f'{entry["name"]}: supporting-file inventory changed')
        for rel, old_hash in source_files.items():
            path = skill / rel
            if not path.is_file():
                failures.append(f'Missing: {path.relative_to(ROOT)}')
                continue
            if path.is_symlink():
                failures.append(f'Nonportable symlink: {path.relative_to(ROOT)}')
            if not (entry['name'] in PORTABLE and rel == 'SKILL.md'):
                if hashlib.sha256(path.read_bytes()).hexdigest() != old_hash:
                    failures.append(f'Unexpected change from snapshot: {path.relative_to(ROOT)}')
            if path.suffix == '.md':
                text = path.read_text(encoding='utf-8')
                if '/Users/avi/' in text:
                    failures.append(f'Machine-specific path: {path.relative_to(ROOT)}')
                # Fenced examples describe generated files, not bundled dependencies.
                prose = re.sub(r'^```[^\n]*\n.*?^```[^\n]*$', '', text, flags=re.M | re.S)
                for target in re.findall(r'\]\(([^\s)]+)\)', prose):
                    if target.startswith(('#', 'http:', 'https:', 'mailto:', 'plugin:', 'app:')):
                        continue
                    if any(c in target for c in '<>{}$') or target.startswith('/'):
                        continue
                    local = target.split('#')[0]
                    if local and Path(local).suffix in {'.md', '.py', '.sh', '.css'}:
                        checked_links += 1
                        if not (path.parent / local).exists():
                            failures.append(f'Broken relative link: {path.relative_to(ROOT)} -> {target}')
        entrypoint = skill / 'SKILL.md'
        if entrypoint.exists():
            text = entrypoint.read_text(encoding='utf-8')
            if not text.startswith('---\n') or '\n---' not in text[4:]:
                failures.append(f'Invalid frontmatter: {entry["name"]}')
                continue
            front = text[4:].split('\n---', 1)[0]
            name = re.search(r'^name:\s*[\"\']?([a-z0-9-]+)', front, re.M)
            if not name or name.group(1) != entry['name'] or not re.search(r'^description:\s*\S', front, re.M):
                failures.append(f'Missing/mismatched name or description: {entry["name"]}')
    if failures:
        print('\n'.join('ERROR: ' + f for f in failures), file=sys.stderr)
        return 1
    print(f'PASS: 23 complete skills; {checked_links} local links; original files preserved except four declared portable entrypoints.')
    print('PASS: planning-first, contrarian-review and socratic-planning match their complete source snapshots.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
