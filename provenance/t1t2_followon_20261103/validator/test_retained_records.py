#!/usr/bin/env python3
"""Safety tests on copied retained samples and deterministic corruptions only.

Usage: python -I -B test_retained_records.py PUBLIC_ROOT
Never imports an archived scientific program or generates scientific cases.
"""
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

PUBLIC_ROOT = Path(sys.argv.pop(1)) if len(sys.argv) > 1 else Path('.')
MODULE = Path(__file__).with_name('verify_retained_records.py')
SENS = 'v10_research/route_a_sensitivity_bottleneck_20261103_1341/'
COMP = 'v10_research/route_a_bos_causal_compile_20261103_1411/'
PATHS = (SENS+'population_cases.jsonl', SENS+'reverse_moment_cases.jsonl', COMP+'exhaustive_cases_v1.jsonl')
if MODULE.is_file():
    spec = importlib.util.spec_from_file_location('new_retained_checker', MODULE)
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
else:
    checker = None

class RetainedRecordTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(checker, 'read-only checker has not been implemented')
        self.temporary = tempfile.TemporaryDirectory(prefix='retained-record-tests-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)/'copy'
        self.root.mkdir()
        for rel in PATHS:
            dest=self.root/rel; dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(PUBLIC_ROOT/rel,dest)

    def mutate(self,index,change):
        path=self.root/PATHS[index]
        rows=[json.loads(x) for x in path.read_text().splitlines()]
        change(rows)
        path.write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in rows))

    def reject(self):
        with self.assertRaises(checker.VerificationError): checker.verify_records(self.root)

    def test_accepts_all_saved_records_without_writes(self):
        before={p.relative_to(self.root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in self.root.rglob('*') if p.is_file()}
        result=checker.verify_records(self.root)
        self.assertEqual(result['status'],'PASS')
        self.assertEqual(result['total_records'],1106)
        self.assertEqual([x['records'] for x in result['files']],[90,8,1008])
        after={p.relative_to(self.root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before,after)

    def test_rejects_missing_row(self):
        self.mutate(0,lambda rows: rows.pop()); self.reject()
    def test_rejects_duplicate_input(self):
        self.mutate(0,lambda rows: rows.__setitem__(1,copy.deepcopy(rows[0]))); self.reject()
    def test_rejects_reordered_keys(self):
        self.mutate(0,lambda rows: rows.reverse()); self.reject()
    def test_rejects_population_equality_corruption(self):
        self.mutate(0,lambda rows: rows[0].__setitem__('loss_plus','0')); self.reject()
    def test_rejects_reverse_moment_bound_corruption(self):
        self.mutate(1,lambda rows: rows[0].__setitem__('var_r','1000')); self.reject()
    def test_rejects_reverse_status_corruption(self):
        self.mutate(1,lambda rows: rows[0].__setitem__('all_bounds',False)); self.reject()
    def test_rejects_no_bos_equality_corruption(self):
        self.mutate(2,lambda rows: rows[0].__setitem__('absolute_error',{'numerator':0,'denominator':1})); self.reject()
    def test_rejects_no_bos_count_range(self):
        self.mutate(2,lambda rows: rows[0].__setitem__('C',2)); self.reject()
    def test_rejects_no_bos_terminal_corruption(self):
        self.mutate(2,lambda rows: rows[0].__setitem__('terminal',[1,1])); self.reject()
    def test_rejects_false_gate_status(self):
        self.mutate(2,lambda rows: rows[0].__setitem__('gates_exact',False)); self.reject()
    def test_rejects_boolean_as_integer(self):
        self.mutate(2,lambda rows: rows[0].__setitem__('C',False)); self.reject()
    def test_rejects_noncanonical_string_rational(self):
        self.mutate(0,lambda rows: rows[0].__setitem__('u','2/32')); self.reject()
    def test_rejects_noncanonical_object_rational(self):
        self.mutate(2,lambda rows: rows[0].__setitem__('eta',{'numerator':2,'denominator':8})); self.reject()
    def test_rejects_zero_denominator(self):
        self.mutate(2,lambda rows: rows[0].__setitem__('eta',{'numerator':1,'denominator':0})); self.reject()
    def test_rejects_oversized_rational(self):
        self.mutate(1,lambda rows: rows[0].__setitem__('mean_r','1/'+('9'*2049))); self.reject()
    def test_rejects_extra_field(self):
        self.mutate(0,lambda rows: rows[0].__setitem__('unretained',0)); self.reject()
    def test_rejects_missing_field(self):
        self.mutate(0,lambda rows: rows[0].pop('lambda')); self.reject()
    def test_rejects_duplicate_json_key(self):
        path=self.root/PATHS[0];b=path.read_bytes();path.write_bytes(b.replace(b'{',b'{"u":"1/16",',1));self.reject()
    def test_rejects_nonfinite_json(self):
        path=self.root/PATHS[0];b=path.read_bytes();path.write_bytes(b.replace(b'"1/16"',b'NaN',1));self.reject()
    def test_rejects_json_float(self):
        path=self.root/PATHS[0];b=path.read_bytes();path.write_bytes(b.replace(b'"1/16"',b'0.0625',1));self.reject()
    def test_rejects_invalid_utf8(self):
        path=self.root/PATHS[0];path.write_bytes(b'\xff\n');self.reject()
    def test_rejects_truncated_json(self):
        path=self.root/PATHS[0];path.write_bytes(path.read_bytes()[:-3]);self.reject()
    def test_rejects_blank_line(self):
        path=self.root/PATHS[0];path.write_bytes(path.read_bytes()+b'\n');self.reject()
    def test_rejects_missing_final_newline(self):
        path=self.root/PATHS[0];path.write_bytes(path.read_bytes().rstrip(b'\n'));self.reject()
    def test_rejects_deep_json(self):
        path=self.root/PATHS[0];path.write_text('['*2000+'0'+']'*2000+'\n');self.reject()
    def test_rejects_oversized_line(self):
        path=self.root/PATHS[0];path.write_bytes(b' '*20000+b'\n');self.reject()
    def test_rejects_oversized_file(self):
        with (self.root/PATHS[0]).open('wb') as f:f.truncate(1024*1024)
        self.reject()
    def test_rejects_missing_file(self):
        (self.root/PATHS[0]).unlink();self.reject()
    def test_rejects_file_symlink(self):
        p=self.root/PATHS[0];p.unlink();p.symlink_to(PUBLIC_ROOT/PATHS[0]);self.reject()
    def test_rejects_directory_symlink(self):
        p=self.root/'v10_research';q=self.root/'held';p.rename(q);p.symlink_to(q,target_is_directory=True);self.reject()
    def test_rejects_root_symlink(self):
        p=Path(self.temporary.name)/'linked';p.symlink_to(self.root,target_is_directory=True)
        with self.assertRaises(checker.VerificationError):checker.verify_records(p)
    def test_rejects_fifo_without_blocking(self):
        p=self.root/PATHS[0];p.unlink();os.mkfifo(p);self.reject()
    def test_rejects_unsafe_relative_paths(self):
        with checker.SafeRoot(self.root) as safe:
            for rel in ('../file','/etc/passwd','a//b','./a','a/../b','a\\b','a\x00b'):
                with self.subTest(path=rel),self.assertRaises(checker.VerificationError):safe.read(rel)

if __name__=='__main__':unittest.main(verbosity=2)
