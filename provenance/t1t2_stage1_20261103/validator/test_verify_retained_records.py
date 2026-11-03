#!/usr/bin/env python3
"""Deterministic tests on fresh fixture copies; never executes archived programs."""
import contextlib
import copy
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
MODULE = HERE / 'verify_retained_records.py'
if MODULE.exists():
    spec = importlib.util.spec_from_file_location('retained_validator', MODULE)
    V = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(V)
else:
    V = None

class RetainedTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(V, 'Retained-record validator has not been implemented')

    def fixture(self, name):
        return json.loads((HERE/'fixtures'/name).read_text())

    def rejects(self, fn, *args):
        with self.assertRaises(V.VerificationError):
            fn(*args)

    def test_strict_json_rejects_duplicate_and_nonfinite(self):
        for s in ['{"x":1,"x":2}', '{"x":NaN}', '{"x":Infinity}', '{"x":-Infinity}', '{"x":1e999}', '{"x":1.0}']:
            with self.subTest(s=s): self.rejects(V.strict_json, s)
        self.assertEqual(V.strict_json('{"x":[1,true,"1/2"]}'), {'x':[1,True,'1/2']})

    def test_json_bounded_depth_integer_and_line(self):
        for s in ['['*40+'0'+']'*40, '9'*200, '"'+'x'*70000+'"']:
            self.rejects(V.strict_json, s)

    def test_canonical_rationals_reject_bad_forms(self):
        for value in [True, 1, 0.5, '01','-0','+1','1/1','2/4','1/-2','1/0',' 1','1 ','1.0','1e4','9'*200]:
            with self.subTest(value=value): self.rejects(V.rational, value)
        self.assertEqual(str(V.rational('-3/7')), '-3/7')
        self.assertEqual(str(V.rational('0')), '0')

    def test_exact_record_types_counts_and_bound(self):
        base=self.fixture('exact.json'); self.assertEqual(V.validate_record('exact',base), [3,'000',1])
        for field,value in [('N',True),('J',0),('C',1),('word','001'),('error','3'),('upper','-1'),('K',7),('extra',0)]:
            obj=copy.deepcopy(base);obj[field]=value
            with self.subTest(field=field): self.rejects(V.validate_record,'exact',obj)

    def test_spline_typed_schema_and_saved_consistency(self):
        base=self.fixture('spline.json'); self.assertEqual(V.validate_record('spline',base), [3,[0,0,0],1,0])
        for field,value in [('passed',1),('passed',False),('m',2),('terminal_query',[0,1]),('shifts_tenths',[0,0,2]),('absolute_error','0'),('bound_total','0'),('e_h','1'),('J',True)]:
            obj=copy.deepcopy(base);obj[field]=value
            with self.subTest(field=field,value=value): self.rejects(V.validate_record,'spline',obj)

    def test_family_schema_probability_sums_and_duplicate_words(self):
        base=self.fixture('family.json'); self.assertEqual(V.validate_record('family',base), ['1/100','1/4','3/4',2])
        changes=[lambda x:x.update(path_total='0'),lambda x:x.update(assertions=True),lambda x:x['inputs'].update(N=True),lambda x:x['path_probabilities'][0].update(P='1/2'),lambda x:x['path_probabilities'][1].update(word='00'),lambda x:x['P'][0].append('0')]
        for change in changes:
            obj=copy.deepcopy(base);change(obj);self.rejects(V.validate_record,'family',obj)

    def test_two_worlds_nested_schema_and_stored_words(self):
        base=self.fixture('worlds.json'); self.assertEqual(len(V.validate_record('worlds',base)),2)
        for change in [lambda x:x.update(rng=0),lambda x:x['cases'][0]['factors'][0].update(outcome=True),lambda x:x['cases'][0].update(J=[0,2,1,1]),lambda x:x['cases'][0].update(trajectory_probability='1'),lambda x:x.update(equal_prior_lower='0')]:
            obj=copy.deepcopy(base);change(obj);self.rejects(V.validate_record,'worlds',obj)

    def test_tsv_corrected_and_discarded_buggy_history(self):
        for kind,count in [('corrected',168),('buggy',9)]:
            data=(HERE/'fixtures'/(kind+'.tsv')).read_bytes()
            result=V.validate_stream(kind,io.BytesIO(data))
            self.assertEqual(result['records'],count)
            self.assertEqual(result['discarded_history'],kind=='buggy')
            self.rejects(V.validate_stream,kind,io.BytesIO(data.replace(b'J00\tJ01',b'J00\tJ00',1)))
            self.rejects(V.validate_stream,kind,io.BytesIO(data+b'\n'))

    def test_jsonl_rejects_blank_duplicate_records_and_missing_newline(self):
        line=(HERE/'fixtures'/'exact.json').read_bytes()
        self.rejects(V.validate_stream,'exact',io.BytesIO(line+line))
        self.rejects(V.validate_stream,'exact',io.BytesIO(line+b'\n'))
        self.rejects(V.validate_stream,'exact',io.BytesIO(line.rstrip(b'\n')))

    def test_safe_reads_reject_traversal_absolute_symlinks_fifo(self):
        with tempfile.TemporaryDirectory(dir=os.environ.get('TEST_TMPDIR')) as td:
            root=Path(td);(root/'d').mkdir();(root/'d'/'x').write_bytes(b'{}\n');(root/'link').symlink_to(root/'d',target_is_directory=True);(root/'d'/'link').symlink_to(root/'d'/'x');os.mkfifo(root/'fifo')
            with V.SafeRoot(root) as safe:
                with safe.open('d/x') as f:self.assertEqual(f.read(),b'{}\n')
                for name in ['../d/x','/etc/passwd','d/../d/x','d//x','link/x','d/link','fifo','d']:
                    self.rejects(safe.open,name)
            alias=root/'rootlink';alias.symlink_to(root/'d',target_is_directory=True)
            self.rejects(V.SafeRoot,alias)

    def test_addenda_saved_schema_counts_and_bounds(self):
        for kind,field,value in [('collision','collision_radius','0'),('port_collision','passed',False),('positionwise','required_q_error','0'),('terminal_paths','radius','1'),('refined','error','9')]:
            base=self.fixture(kind+'.json'); self.assertIsInstance(V.validate_record(kind,base),list)
            obj=copy.deepcopy(base);obj[field]=value
            with self.subTest(kind=kind): self.rejects(V.validate_record,kind,obj)
            obj=copy.deepcopy(base);obj['unexpected']=0
            self.rejects(V.validate_record,kind,obj)

    def test_frozen_coverage_rejects_valid_but_incomplete_file(self):
        with tempfile.TemporaryDirectory(dir=os.environ.get('TEST_TMPDIR')) as td:
            target=Path(td)/V.FILE_SPECS[0]['path'];target.parent.mkdir(parents=True)
            target.write_bytes((HERE/'fixtures'/'spline.json').read_bytes())
            self.rejects(V.verify_records,td)

    def test_boolean_integer_confusion_and_nested_unexpected_fields(self):
        for kind in ('family','exact','spline','worlds','collision','port_collision','positionwise','terminal_paths','refined'):
            obj=self.fixture(kind+'.json')
            self.rejects(V.validate_record,kind,dict(obj,unexpected_field=0))
        obj=self.fixture('terminal_paths.json');obj['heads'][0]['matching_J']=True
        self.rejects(V.validate_record,'terminal_paths',obj)
        obj=self.fixture('positionwise.json');obj['row_occupancies']['11']=False
        self.rejects(V.validate_record,'positionwise',obj)

    def test_safe_reads_refuse_oversized_and_invalid_utf8(self):
        with tempfile.TemporaryDirectory(dir=os.environ.get('TEST_TMPDIR')) as td:
            path=Path(td)/'large'
            with path.open('wb') as f:f.truncate(V.MAX_FILE+1)
            with V.SafeRoot(td) as root:self.rejects(root.open,'large')
        self.rejects(V.validate_stream,'exact',io.BytesIO(b'\xff\n'))

    def test_refined_absent_bound_rejected(self):
        obj=self.fixture('refined.json');obj['bound9']=None
        self.rejects(V.validate_record,'refined',obj)

    def test_negative_family_pi_rejected(self):
        obj=self.fixture('family.json');obj['pi'][0]='-1/100';obj['pi'][1]='7/20'
        self.rejects(V.validate_record,'family',obj)

    def test_errors_survive_optimized_python(self):
        script="import sys; sys.path.insert(0,sys.argv[1]); import verify_retained_records as v;\ntry: v.rational('2/4')\nexcept v.VerificationError: print('rejected')\nelse: raise SystemExit(9)"
        p=subprocess.run([sys.executable,'-B','-O','-c',script,str(HERE)],capture_output=True,text=True,timeout=10)
        self.assertEqual(p.returncode,0,p.stderr);self.assertEqual(p.stdout,'rejected\n')

if __name__=='__main__': unittest.main(verbosity=2)
