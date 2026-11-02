"""Regression tests for strict public-export integrity (not mathematical proof)."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / 'tools' / 'public_verify.py'

class PublicIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'provenance').mkdir()
        (self.root / 'proof.md').write_bytes(b'Unchanged mathematical source.\n')
        self.rows = [{'path': 'proof.md', 'bytes': 30, 'sha256': hashlib.sha256((self.root / 'proof.md').read_bytes()).hexdigest()}]
        self.rows[0]['bytes'] = len((self.root / 'proof.md').read_bytes())
        self.write_manifest()

    def write_manifest(self):
        (self.root / 'provenance' / 'PUBLIC_INVENTORY.json').write_text(json.dumps({'files': self.rows}))

    def verify(self):
        self.assertTrue(MODULE.is_file(), 'The public integrity verifier must be implemented.')
        spec = importlib.util.spec_from_file_location('public_verify', MODULE)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.verify(self.root)

    def test_exact_export_passes(self):
        self.assertEqual(self.verify()['files_verified'], 1)

    def test_undeclared_mathematical_tamper_is_rejected(self):
        (self.root / 'proof.md').write_bytes(b'Altered mathematical source.\n')
        with self.assertRaises(ValueError): self.verify()

    def test_missing_file_is_rejected(self):
        (self.root / 'proof.md').unlink()
        with self.assertRaises(ValueError): self.verify()

    def test_extra_file_is_rejected(self):
        (self.root / 'unexpected.txt').write_text('not declared')
        with self.assertRaises(ValueError): self.verify()

    def test_unsafe_manifest_path_is_rejected(self):
        self.rows[0]['path'] = '../escape'
        self.write_manifest()
        with self.assertRaises(ValueError): self.verify()

    def test_symlink_is_rejected(self):
        (self.root / 'proof.md').unlink()
        (self.root / 'proof.md').symlink_to('/dev/null')
        with self.assertRaises(ValueError): self.verify()

    def test_duplicate_manifest_path_is_rejected(self):
        self.rows.append(dict(self.rows[0]))
        self.write_manifest()
        with self.assertRaises(ValueError): self.verify()

if __name__ == '__main__': unittest.main()
