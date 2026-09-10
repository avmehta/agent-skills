import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

MODULE_PATH = Path(__file__).resolve().parents[1] / 'install.py'
spec = importlib.util.spec_from_file_location('installer', MODULE_PATH)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.dest = self.root / 'path with spaces' / 'skills'
        self.repo = self.root / 'repo'
        self.repo.mkdir()
        shutil.copytree(installer.ROOT / 'skills', self.repo / 'skills')
        shutil.copytree(installer.ROOT / 'templates', self.repo / 'templates')
        self.original_root = installer.ROOT
        installer.ROOT = self.repo
        self.names = sorted(p.name for p in (self.repo / 'skills').iterdir())

    def tearDown(self):
        installer.ROOT = self.original_root
        self.temp.cleanup()

    def test_complete_install_and_idempotence(self):
        installer.install(self.dest, self.names)
        before = {n: installer.digest(self.dest / n) for n in self.names}
        self.assertEqual(len(before), 23)
        self.assertTrue((self.dest / 'teach-course/assets/course.css').exists())
        self.assertTrue((self.dest / 'playwright-cli/references/tracing.md').exists())
        state_before = (self.dest / installer.STATE_NAME).read_bytes()
        installer.install(self.dest, self.names)
        self.assertEqual(before, {n: installer.digest(self.dest / n) for n in self.names})
        self.assertEqual(state_before, (self.dest / installer.STATE_NAME).read_bytes())

    def test_dry_run_writes_nothing(self):
        agents = self.root / 'config' / 'AGENTS.md'
        installer.install(self.dest, self.names, dry_run=True, agents_file=agents)
        self.assertFalse(self.dest.exists())
        self.assertFalse(agents.parent.exists())

    def test_collision_preflight_prevents_partial_install(self):
        conflict = self.dest / self.names[-1]
        conflict.mkdir(parents=True)
        (conflict / 'SKILL.md').write_text('Keep this local skill', encoding='utf-8')
        with self.assertRaises(ValueError):
            installer.install(self.dest, self.names)
        self.assertEqual([p.name for p in self.dest.iterdir()], [self.names[-1]])
        self.assertEqual((conflict / 'SKILL.md').read_text(encoding='utf-8'), 'Keep this local skill')

    def test_update_managed_copy(self):
        names = ['planning-first']
        installer.install(self.dest, names)
        source = self.repo / 'skills/planning-first/SKILL.md'
        source.write_text(source.read_text(encoding='utf-8') + '\nTest revision\n', encoding='utf-8')
        installer.install(self.dest, names, update=True)
        self.assertEqual((self.dest / 'planning-first/SKILL.md').read_bytes(), source.read_bytes())
        self.assertEqual(json.loads((self.dest / installer.STATE_NAME).read_text(encoding='utf-8'))['skills']['planning-first'], installer.digest(self.dest / 'planning-first'))

    def test_local_edit_blocks_update(self):
        installer.install(self.dest, ['planning-first'])
        local = self.dest / 'planning-first/SKILL.md'
        local.write_text(local.read_text(encoding='utf-8') + '\nMy local change\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'locally modified'):
            installer.install(self.dest, ['planning-first'], update=True)
        self.assertTrue(local.read_text(encoding='utf-8').endswith('My local change\n'))

    def test_unmanaged_update_is_refused(self):
        target = self.dest / 'planning-first'
        target.mkdir(parents=True)
        (target / 'SKILL.md').write_text('Unmanaged', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'unmanaged'):
            installer.install(self.dest, ['planning-first'], update=True)

    def test_removed_source_file_is_removed_on_managed_update(self):
        installer.install(self.dest, ['planning-first'])
        (self.repo / 'skills/planning-first/agents/openai.yaml').unlink()
        installer.install(self.dest, ['planning-first'], update=True)
        self.assertFalse((self.dest / 'planning-first/agents/openai.yaml').exists())

    def test_identical_existing_copy_can_be_adopted(self):
        shutil.copytree(self.repo / 'skills/planning-first', self.dest / 'planning-first')
        installer.install(self.dest, ['planning-first'])
        self.assertIn('planning-first', json.loads((self.dest / installer.STATE_NAME).read_text(encoding='utf-8'))['skills'])

    def test_global_instructions_preserved_and_not_duplicated(self):
        agents = self.root / 'AGENTS.md'
        original = '# My global instructions\n\nKeep this rule.\n'
        agents.write_text(original, encoding='utf-8')
        installer.install(self.dest, ['planning-first'], agents_file=agents)
        contents = agents.read_text(encoding='utf-8')
        self.assertTrue(contents.startswith(original.rstrip()))
        self.assertEqual(contents.count(installer.BEGIN), 1)
        backups = list(self.root.glob('AGENTS.md.backup-*'))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(encoding='utf-8'), original)
        installer.install(self.dest, ['planning-first'], agents_file=agents)
        self.assertEqual(agents.read_text(encoding='utf-8'), contents)
        self.assertEqual(len(list(self.root.glob('AGENTS.md.backup-*'))), 1)

    def test_changed_global_agreement_blocks_all_writes(self):
        agents = self.root / 'AGENTS.md'
        contents = installer.BEGIN + '\nDifferent rule\n' + installer.END
        agents.write_text(contents, encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'different planning'):
            installer.install(self.dest, self.names, agents_file=agents)
        self.assertFalse(self.dest.exists())
        self.assertEqual(agents.read_text(encoding='utf-8'), contents)

    def test_invalid_state_fails_before_writes(self):
        self.dest.mkdir(parents=True)
        (self.dest / installer.STATE_NAME).write_text('{bad json', encoding='utf-8')
        with self.assertRaises(ValueError):
            installer.install(self.dest, self.names)
        self.assertFalse((self.dest / self.names[0]).exists())

    def test_state_commit_failure_rolls_back_files_and_instructions(self):
        installer.install(self.dest, ['planning-first'])
        local = self.dest / 'planning-first/SKILL.md'
        before = local.read_bytes()
        state = (self.dest / installer.STATE_NAME).read_bytes()
        source = self.repo / 'skills/planning-first/SKILL.md'
        source.write_text(source.read_text(encoding='utf-8') + '\nNew revision\n', encoding='utf-8')
        agents = self.root / 'AGENTS.md'
        agents.write_text('Original rules\n', encoding='utf-8')
        with patch.object(installer.os, 'replace', side_effect=OSError('Simulated state write failure')):
            with self.assertRaises(OSError):
                installer.install(self.dest, ['planning-first', 'research'], update=True, agents_file=agents)
        self.assertEqual(local.read_bytes(), before)
        self.assertEqual((self.dest / installer.STATE_NAME).read_bytes(), state)
        self.assertFalse((self.dest / 'research').exists())
        self.assertEqual(agents.read_text(encoding='utf-8'), 'Original rules\n')

    def test_symlink_target_is_refused(self):
        other = self.root / 'other'
        other.mkdir()
        self.dest.mkdir(parents=True)
        try:
            (self.dest / 'planning-first').symlink_to(other, target_is_directory=True)
        except OSError:
            self.skipTest('Creating symlinks is unavailable in this environment')
        with self.assertRaisesRegex(ValueError, 'real skill directory'):
            installer.install(self.dest, ['planning-first'])
        self.assertTrue(other.exists())


if __name__ == '__main__':
    unittest.main()
