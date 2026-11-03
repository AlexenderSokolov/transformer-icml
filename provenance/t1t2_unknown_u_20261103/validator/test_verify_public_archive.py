#!/usr/bin/env python3
"""Deterministic tests of the new public archive verifier, not scientific replay.

Run: python -I -B test_verify_public_archive.py [--helper PATH]
Repeat with -O. Default helper: ../verify_public_archive.py from this file.
Fixtures are synthetic, exclusively newly created, and removed after each test.
No archived research module, model, random generator or network call is used.
"""
import sys
if not sys.flags.isolated or not sys.dont_write_bytecode:
    raise SystemExit('Run tests with python -I -B.')
import copy
import hashlib
import json
import os
from pathlib import Path
import runpy
import shutil
import subprocess
import unittest

args = sys.argv[1:]
helper = Path(__file__).resolve().parent.parent / 'verify_public_archive.py'
if args[:1] == ['--helper'] and len(args) >= 2:
    helper = Path(args[1]).resolve()
    args = args[2:]
ns = runpy.run_path(str(helper), run_name='outer_helper_test_subject')
Error = ns['ArchiveError']
STAGE = ns['STAGE_DIR']


def identity(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
            'git_blob_sha1': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()}


def entry(path, raw=b'fixture\n'):
    return dict(path=path, **identity(raw))


def manifest():
    return {'schema': 't1t2-unknown-u-stage-files-v1', 'source_count': 41,
            'files': [entry(STAGE + '/fixture.txt')],
            'self_reference_boundary': 'The trusted external anchor covers this manifest.',
            'scoped_directories': [STAGE]}


def source_map_fixture():
    rows, entries = [], {}
    dirs = sorted(ns['SOURCE_DIRECTORIES'])
    for i in range(40):
        p = dirs[i % len(dirs)] + '/fixture' + str(i).zfill(3) + '.txt'
        original = identity(b'x' * (204175 if i == 0 else 1))
        public = identity(b'x' * original['bytes'] + b'y' * (12 if i == 0 else (1 if i < 7 else 0)))
        rows.append({'source_record_id': 'UAR' + str(i + 1).zfill(3), 'path': p,
                     'original': original, 'public': public, 'changed': i < 7,
                     'storage': {'kind': 'file', 'path': p}})
        entries[p] = dict(path=p, **public)
    trace = {'bytes': 79712544, 'sha256': 'a' * 64, 'git_blob_sha1': 'b' * 40}
    rows.append({'source_record_id': 'UAR041', 'path': ns['TRACE_PATH'],
                 'original': trace, 'public': dict(trace), 'changed': False,
                 'storage': {'kind': 'lossless_chunks', 'manifest_path': ns['TRACE_MANIFEST_PATH']}})
    entries[ns['TRACE_MANIFEST_PATH']] = entry(ns['TRACE_MANIFEST_PATH'])
    return {'schema': 't1t2-unknown-u-source-export-v1', 'source_count': 41,
            'original_total_bytes': 79916758, 'export_total_bytes': 79916776,
            'byte_exact_count': 34, 'changed_count': 7, 'files': rows}, entries


class SchemaTests(unittest.TestCase):
    def test_integer_bounds_and_boolean(self):
        self.assertEqual(ns['integer'](4, 0, 4), 4)
        for bad in (True, False, -1, 5, '2', 2.0, None):
            with self.subTest(bad=bad), self.assertRaises(Error): ns['integer'](bad, 0, 4)

    def test_digest(self):
        self.assertEqual(ns['digest']('a' * 64, 64), 'a' * 64)
        for bad in ('A' * 64, 'a' * 63, 'g' * 64, None):
            with self.subTest(bad=bad), self.assertRaises(Error): ns['digest'](bad, 64)

    def test_paths(self):
        self.assertEqual(ns['safe_path']('a/b.txt'), 'a/b.txt')
        for bad in ('', '/a', '../a', 'a/../b', 'a//b', './a', 'a\\b', 'a\x00b', 'a\nb', 'a' * 513):
            with self.subTest(bad=bad), self.assertRaises(Error): ns['safe_path'](bad)

    def test_strict_json_valid(self):
        self.assertEqual(ns['strict_json'](b'{"a":[1,true,null,"text"]}'), {'a': [1, True, None, 'text']})

    def test_strict_json_invalid(self):
        invalid = [b'', b'{"a":1,"a":2}', b'{"a":1.5}', b'{"a":NaN}', b'{"a":Infinity}',
                   b'{"a":-Infinity}', b'\xff', b'{} trailing', b'1' * 33,
                   b'[' * 18 + b'0' + b']' * 18,
                   json.dumps([0] * 1025).encode(), json.dumps({'k' * 257: 0}).encode(),
                   json.dumps({str(i): 0 for i in range(129)}).encode(),
                   json.dumps('x' * 65537).encode()]
        for raw in invalid:
            with self.subTest(length=len(raw)), self.assertRaises(Error): ns['strict_json'](raw)

    def test_byte_and_git_checks(self):
        row = entry('a.txt', b'abc')
        ns['check_bytes'](b'abc', row)
        for changed in [dict(row, bytes=4), dict(row, sha256='0' * 64), dict(row, git_blob_sha1='0' * 40)]:
            with self.subTest(changed=changed), self.assertRaises(Error): ns['check_bytes'](b'abc', changed)
        with self.assertRaises(Error): ns['check_bytes'](b'abd', row)

    def test_manifest_valid(self):
        self.assertEqual(len(ns['validate_manifest'](manifest())), 1)

    def test_manifest_duplicate_self_inventory(self):
        for path in (ns['MANIFEST_PATH'], 'provenance/PUBLIC_INVENTORY.json'):
            m = manifest(); m['files'] = [entry(path)]
            with self.subTest(path=path), self.assertRaises(Error): ns['validate_manifest'](m)
        m = manifest(); m['files'] *= 2
        with self.assertRaises(Error): ns['validate_manifest'](m)

    def test_manifest_schema_bounds(self):
        variants = [('source_count', True), ('source_count', 40), ('schema', 'other'),
                    ('files', []), ('scoped_directories', [STAGE, STAGE]),
                    ('self_reference_boundary', '')]
        for key, value in variants:
            m = manifest(); m[key] = value
            with self.subTest(key=key), self.assertRaises(Error): ns['validate_manifest'](m)
        m = manifest(); m['extra'] = 1
        with self.assertRaises(Error): ns['validate_manifest'](m)
        m = manifest(); m['files'][0]['bytes'] = ns['MAX_FILE'] + 1
        with self.assertRaises(Error): ns['validate_manifest'](m)

    def test_source_map_valid(self):
        m, entries = source_map_fixture()
        paths, physical, split = ns['validate_source_map'](m, entries)
        self.assertEqual((len(paths), len(physical), split['path']), (41, 40, ns['TRACE_PATH']))

    def test_source_map_rejects_invalid_binding(self):
        for field, value in [('source_record_id', 'UAR002'), ('changed', False), ('path', '../escape')]:
            m, entries = source_map_fixture(); m['files'][0][field] = value
            with self.subTest(field=field), self.assertRaises(Error): ns['validate_source_map'](m, entries)
        m, entries = source_map_fixture(); m['files'][0]['public']['sha256'] = '0' * 64
        with self.assertRaises(Error): ns['validate_source_map'](m, entries)
        m, entries = source_map_fixture(); m['files'][-1]['storage']['manifest_path'] = 'other'
        with self.assertRaises(Error): ns['validate_source_map'](m, entries)
        m, entries = source_map_fixture(); m['files'][-1]['changed'] = True
        with self.assertRaises(Error): ns['validate_source_map'](m, entries)

    def test_inherited_list_constraints(self):
        rows = [entry('old/file' + str(i)) for i in range(88)]
        self.assertEqual(len(ns['inherited_rows']({'inherited_public_files': rows}, {})), 88)
        for altered in (rows[:-1], rows[:-1] + [rows[0]]):
            with self.assertRaises(Error): ns['inherited_rows']({'inherited_public_files': altered}, {})
        with self.assertRaises(Error): ns['inherited_rows']({'inherited_public_files': rows}, {rows[0]['path']: rows[0]})

    def test_result_binding(self):
        result = {'status': 'PASS_ARCHIVED_BYTES_AND_SAVED_SCHEMA_ONLY', 'scientific_replay': False,
                  'reconstructed': False, 'bytes': 79712544, 'rows': 1008, 'chunks': 20,
                  'N3_records': 16, 'recorded_J_zero': 236, 'recorded_passed': 1008,
                  'recorded_failed': 0, 'recorded_true_assertions': 157248,
                  'sha256': 'a' * 64, 'source_path': ns['TRACE_PATH']}
        trace = {'source': {'sha256': 'a' * 64}}
        ns['bind_result'](result, trace)
        for key, value in [('scientific_replay', True), ('reconstructed', True), ('recorded_passed', 1007),
                           ('recorded_failed', False), ('sha256', 'b' * 64), ('status', 'PASS')]:
            with self.subTest(key=key), self.assertRaises(Error): ns['bind_result'](dict(result, **{key: value}), trace)


class FilesystemTests(unittest.TestCase):
    serial = 0
    def setUp(self):
        type(self).serial += 1
        self.root = Path('/tmp') / ('v10-outer-test-' + str(os.getpid()) + '-' + str(self.serial))
        self.root.mkdir(mode=0o700)  # exclusive: no existing path is ever reused
        (self.root / 'scope').mkdir()
        (self.root / 'scope/data.txt').write_bytes(b'fixture\n')
    def tearDown(self):
        shutil.rmtree(self.root)

    def test_safe_read_and_exact_scope(self):
        with ns['SafeTree'](self.root) as tree:
            self.assertEqual(tree.read('scope/data.txt'), b'fixture\n')
            ns['check_scopes'](tree, {'scope/data.txt'}, {'scope'})
            with self.assertRaises(Error): ns['check_scopes'](tree, set(), {'scope'})
            with self.assertRaises(Error): ns['check_scopes'](tree, {'scope/data.txt', 'scope/missing'}, {'scope'})

    def test_size_limit_and_missing(self):
        with ns['SafeTree'](self.root) as tree:
            with self.assertRaises(Error): tree.read('scope/data.txt', 2)
            with self.assertRaises(Error): tree.read('scope/missing')

    def test_file_symlink_and_fifo(self):
        (self.root / 'scope/link').symlink_to('data.txt')
        os.mkfifo(self.root / 'scope/pipe')
        with ns['SafeTree'](self.root) as tree:
            for path in ('scope/link', 'scope/pipe'):
                with self.subTest(path=path), self.assertRaises(Error): tree.read(path)
            with self.assertRaises(Error): tree.files_under('scope')

    def test_directory_and_root_symlink(self):
        (self.root / 'linked').symlink_to('scope', target_is_directory=True)
        with ns['SafeTree'](self.root) as tree:
            with self.assertRaises(Error): tree.read('linked/data.txt')
        with self.assertRaises(Error): ns['SafeTree'](self.root / 'linked')

    def test_root_parent_traversal(self):
        with self.assertRaises(Error): ns['SafeTree'](str(self.root) + '/../')

    def test_excess_scope_entries(self):
        for i in range(ns['MAX_FILES']): (self.root / 'scope' / ('extra' + str(i))).write_bytes(b'')
        with ns['SafeTree'](self.root) as tree:
            with self.assertRaises(Error): tree.files_under('scope')

    def test_bad_anchor_fails_without_changes(self):
        target = self.root / ns['MANIFEST_PATH']; target.parent.mkdir(parents=True)
        raw = json.dumps(manifest()).encode(); target.write_bytes(raw)
        before = sorted((str(p.relative_to(self.root)), p.read_bytes()) for p in self.root.rglob('*') if p.is_file())
        with self.assertRaises(Error): ns['verify_archive'](self.root, '0' * 64)
        after = sorted((str(p.relative_to(self.root)), p.read_bytes()) for p in self.root.rglob('*') if p.is_file())
        self.assertEqual(before, after)

    def test_subprocess_isolation_and_failure_protocol(self):
        for flags, expected in [(['-B'], 2), (['-I'], 2), (['-I', '-B'], 1)]:
            p = subprocess.run([sys.executable] + flags + [str(helper)], capture_output=True, text=True, timeout=10)
            self.assertEqual(p.returncode, expected)
            self.assertEqual(json.loads(p.stdout)['status'], 'FAIL')
            self.assertFalse(p.stderr)


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]] + args, verbosity=2)
