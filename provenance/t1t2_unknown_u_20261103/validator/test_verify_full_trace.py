#!/usr/bin/env python3
"""Deterministic synthetic software tests. No archived code, models, or RNG."""
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import unittest

HERE = Path(__file__).absolute().parent

class FullTraceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        p = HERE / 'verify_full_trace.py'
        if not p.is_file():
            raise AssertionError('NEW full-trace helper is not implemented yet')
        spec = importlib.util.spec_from_file_location('new_full_trace_helper', p)
        cls.m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.m)

    def setUp(self):
        self.work = HERE / ('synthetic-work-' + str(os.getpid()) + '-' + self._testMethodName)
        self.work.mkdir(mode=0o700)

    def tearDown(self):
        shutil.rmtree(self.work)

    def bad(self, fn, *args):
        with self.assertRaises(self.m.VerificationError):
            fn(*args)

    def transport(self):
        raw = b'{"a":1}\n{"a":2}\n'
        a, b = raw[:8], raw[8:]
        (self.work/'a.jsonl').write_bytes(a)
        (self.work/'b.jsonl').write_bytes(b)
        chunks = []
        offset = 0
        for i, data in enumerate((a,b),1):
            chunks.append({'path':('a' if i==1 else 'b')+'.jsonl','index':i,'offset':offset,'bytes':len(data),'first_record':i,'last_record':i,'sha256':hashlib.sha256(data).hexdigest()})
            offset += len(data)
        source={'path':'v10_research/synthetic/fixture.jsonl','bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'rows':2}
        return raw, source, chunks

    def test_strict_json_valid(self):
        self.assertEqual(self.m.strict_json(b'{"a":1,"b":true,"c":null}'), {'a':1,'b':True,'c':None})

    def test_strict_json_corruption(self):
        for data in (b'{"a":1,"a":2}', b'NaN', b'Infinity', b'1.0', b'1e999', b'\xff', b'\xef\xbb\xbf{}', b'{} {}', b'['*40+b'0'+b']'*40, b'1'*80):
            with self.subTest(data=data[:24]): self.bad(self.m.strict_json,data)

    def test_strict_json_rejects_surrogate_keys(self):
        self.bad(self.m.strict_json,b'{"\\ud800":0}')
        self.bad(self.m.strict_json,b'{"x":"\\udfff"}')

    def test_safe_paths(self):
        for path in ('','/a','../a','a/../b','a//b','a/./b','a\\b','a\x00b','a\nb','a\x7fb'):
            self.bad(self.m.safe_path,path)
        self.assertEqual(self.m.safe_path('a/b.jsonl'),'a/b.jsonl')

    def test_no_follow_file_and_ancestor(self):
        (self.work/'inside').mkdir(); (self.work/'inside'/'x').write_bytes(b'{}')
        (self.work/'filelink').symlink_to('inside/x'); (self.work/'dirlink').symlink_to('inside',target_is_directory=True)
        with self.m.SafeTree(self.work) as tree:
            self.assertEqual(tree.read('inside/x',16),b'{}')
            self.bad(tree.read,'filelink',16); self.bad(tree.read,'dirlink/x',16)
        self.bad(self.m.SafeTree,self.work/'dirlink')

    def test_fifo_rejected_without_blocking(self):
        os.mkfifo(self.work/'fifo')
        with self.m.SafeTree(self.work) as tree:self.bad(tree.read,'fifo',16)

    def test_transport_streams_exact_bytes(self):
        raw,source,chunks=self.transport(); seen=[]
        with self.m.SafeTree(self.work) as tree:
            result=self.m.stream_chunks(tree,source,chunks,lambda row,index:seen.append((row,index)))
        self.assertEqual(result,{'bytes':len(raw),'sha256':source['sha256'],'rows':2,'chunks':2})
        self.assertEqual(seen,[({'a':1},1),({'a':2},2)])
        self.assertEqual(sorted(p.name for p in self.work.iterdir()),['a.jsonl','b.jsonl'])

    def test_corrupt_chunk_and_wrong_order(self):
        raw,source,chunks=self.transport()
        with self.m.SafeTree(self.work) as tree:
            broken=copy.deepcopy(chunks);broken[0]['sha256']='0'*64
            self.bad(self.m.stream_chunks,tree,source,broken,None)
            broken=copy.deepcopy(chunks);broken[1]['offset']+=1
            self.bad(self.m.stream_chunks,tree,source,broken,None)
            broken=copy.deepcopy(chunks);broken[1]['first_record']=1
            self.bad(self.m.stream_chunks,tree,source,broken,None)
            broken=copy.deepcopy(source);broken['sha256']='0'*64
            self.bad(self.m.stream_chunks,tree,broken,chunks,None)
            broken=copy.deepcopy(chunks);broken[1]['path']='a.jsonl'
            self.bad(self.m.stream_chunks,tree,source,broken,None)

    def test_missing_newline_rejected(self):
        raw,source,chunks=self.transport();data=b'{"a":2}'
        (self.work/'b.jsonl').write_bytes(data)
        chunks[1].update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        source.update(bytes=15,sha256=hashlib.sha256(raw[:-1]).hexdigest())
        with self.m.SafeTree(self.work) as tree:self.bad(self.m.stream_chunks,tree,source,chunks,None)

    def test_rationals_are_canonical_and_typed(self):
        self.assertEqual(self.m.rational({'numerator':-1,'denominator':2}),(-1,2))
        for v in ({'numerator':0,'denominator':2},{'numerator':2,'denominator':2},{'numerator':1,'denominator':0},{'numerator':True,'denominator':1},{'numerator':1,'denominator':-2},1,{'numerator':1,'denominator':2,'x':0}):self.bad(self.m.rational,v)

    def test_sparse_shapes(self):
        self.m.sparse({'dimension':4,'entries':[[0,q(1)],[3,q(-2)]]},4)
        for entries in ([[0,q(0)]],[[1,q(1)],[1,q(2)]],[[3,q(1)],[0,q(1)]],[[4,q(1)]],[[True,q(1)]],[[0,1]]):
            self.bad(self.m.sparse,{'dimension':4,'entries':entries},4)

    def test_synthetic_row_shape_and_recorded_status(self):
        row=synthetic_row(self.m)
        self.m.validate_row(row,1)
        mutations=[('passed',False),('case_index',True),('failure_stage','bad'),('N',True),('bit_vector',[False,0,0]),('schema','other')]
        for k,v in mutations:
            r=copy.deepcopy(row);r[k]=v;self.bad(self.m.validate_row,r,1)
        r=copy.deepcopy(row);r['first_ffn'][0]['gates'][0]['type']='other';self.bad(self.m.validate_row,r,1)
        r=copy.deepcopy(row);r['first_attention'][0]['heads'][0]['edges'][0]['weight']=1;self.bad(self.m.validate_row,r,1)
        r=copy.deepcopy(row);r['assertions']['exception_free']=False;self.bad(self.m.validate_row,r,1)
        r=copy.deepcopy(row);r['assertions']['extra']=True;self.bad(self.m.validate_row,r,1)
        r=copy.deepcopy(row);r['second_attention']['zero_head_write']['entries']=[[0,q(1)]];self.bad(self.m.validate_row,r,1)
        r=copy.deepcopy(row);r['oracle']['candidates'][0]['match']=1;self.bad(self.m.validate_row,r,1)

    def test_coverage_rejects_missing_duplicate_and_wrong_order(self):
        self.bad(self.m.validate_row,synthetic_row(self.m),2)
        coverage=self.m.Coverage();coverage.accept(synthetic_row(self.m),1)
        self.bad(coverage.finish)
        self.bad(coverage.accept,synthetic_row(self.m),2)

    def test_exclusive_reconstruction(self):
        raw,source,chunks=self.transport();dest=self.work/'new-destination'
        with self.m.SafeTree(self.work) as tree:
            result=self.m.reconstruct(tree,source,chunks,dest)
            self.assertEqual((dest/source['path']).read_bytes(),raw)
            self.assertEqual(result,source['path'])
            self.bad(self.m.reconstruct,tree,source,chunks,dest)
        self.assertEqual((dest/source['path']).read_bytes(),raw)

    def test_reconstruction_rejects_symlink_parent_and_cleans_partial_file(self):
        raw,source,chunks=self.transport();real=self.work/'real';real.mkdir();(self.work/'link').symlink_to('real',target_is_directory=True)
        with self.m.SafeTree(self.work) as tree:
            self.bad(self.m.reconstruct,tree,source,chunks,self.work/'link'/'new')
            broken=copy.deepcopy(chunks);broken[1]['sha256']='0'*64
            dest=self.work/'failed';self.bad(self.m.reconstruct,tree,source,broken,dest)
            self.assertFalse((dest/source['path']).exists())

    def test_transport_detects_midread_change(self):
        raw,source,chunks=self.transport()
        def mutate(row,index):
            if index==1:
                (self.work/'a.jsonl').write_bytes(b'{"a":9}\n')
        with self.m.SafeTree(self.work) as tree:
            self.bad(self.m.stream_chunks,tree,source,chunks,mutate)

    def test_transport_rejects_byte_and_record_bound_errors(self):
        raw,source,chunks=self.transport()
        for key,value in (('bytes',True),('bytes',self.m.MAX_CHUNK+1),('index',True),('offset',-1),('last_record',3),('path','../a.jsonl')):
            broken=copy.deepcopy(chunks);broken[0][key]=value
            with self.m.SafeTree(self.work) as tree:self.bad(self.m.stream_chunks,tree,source,broken,None)
        for content in (b'\n',b'{"a":1}\r\n',b' '*(self.m.MAX_LINE+1)+b'\n'):
            (self.work/'a.jsonl').write_bytes(content)
            broken=copy.deepcopy(chunks);broken[0].update(bytes=len(content),sha256=hashlib.sha256(content).hexdigest());broken[1]['offset']=len(content)
            combined=copy.deepcopy(source);combined.update(bytes=len(content)+chunks[1]['bytes'],sha256=hashlib.sha256(content+b'{"a":2}\n').hexdigest())
            with self.m.SafeTree(self.work) as tree:self.bad(self.m.stream_chunks,tree,combined,broken,None)

    def test_bindings_resolve_original_and_public_bytes(self):
        bindings=[];entries=[]
        for index,field in enumerate(self.m.BINDING_HASHES,1):
            path=self.m.SOURCE_PATH.rsplit('/',1)[0]+'/'+self.m.BINDING_FILES[field]
            target=self.work/path;target.parent.mkdir(parents=True,exist_ok=True)
            payload=('synthetic public '+field+'\n').encode();target.write_bytes(payload)
            public={'bytes':len(payload),'sha256':hashlib.sha256(payload).hexdigest(),'git_blob_sha1':hashlib.sha1(b'blob '+str(len(payload)).encode()+b'\0'+payload).hexdigest()}
            entries.append({'source_record_id':'S'+str(index),'path':path,'original':{'bytes':self.m.BINDING_BYTES[field],'sha256':self.m.BINDING_HASHES[field],'git_blob_sha1':'0'*40},'public':public,'changed':True,'storage':{'kind':'file','path':path}})
            bindings.append({'field':field,'original_path':path,'original_sha256':self.m.BINDING_HASHES[field],'public_path':path,'public_bytes':len(payload),'public_sha256':public['sha256'],'source_map':{'path':'map.json','sha256':'0'*64,'source_record_id':'S'+str(index)}})
        source_map={'schema':'t1t2-unknown-u-source-export-v1','source_count':4,'files':entries}
        raw=json.dumps(source_map).encode();(self.work/'map.json').write_bytes(raw)
        for b in bindings:b['source_map']['sha256']=hashlib.sha256(raw).hexdigest()
        with self.m.SafeTree(self.work) as tree:
            self.m.validate_bindings(tree,bindings)
            broken=copy.deepcopy(bindings);broken[0]['original_sha256']='0'*64;self.bad(self.m.validate_bindings,tree,broken)
            broken=copy.deepcopy(bindings);broken[0]['source_map']['sha256']='0'*64;self.bad(self.m.validate_bindings,tree,broken)
            broken=copy.deepcopy(bindings);broken[0]['source_map']['source_record_id']='MISSING';self.bad(self.m.validate_bindings,tree,broken)
            broken=copy.deepcopy(bindings);broken[0]['public_bytes']+=1;self.bad(self.m.validate_bindings,tree,broken)
            (self.work/bindings[0]['public_path']).write_bytes(b'changed')
            self.bad(self.m.validate_bindings,tree,bindings)

    def test_command_requires_isolation_and_no_bytecode(self):
        result=subprocess.run([sys.executable,'-B',str(HERE/'verify_full_trace.py'),'--help'],capture_output=True,text=True)
        self.assertNotEqual(result.returncode,0)
        self.assertIn('python -I -B',result.stdout)

def q(n=0,d=1):return {'numerator':n,'denominator':d}
def v(d):return {'dimension':d,'entries':[]}
def synthetic_row(m):
    # Deliberately not a model evaluation: simple placeholders exercise the stored
    # schema. Passing schema checks is not evidence that assertions are true.
    n=3;hd=36;md=72
    edge=lambda j:{'j':j,'K':v(hd),'V':q(),'dot_coefficient_ln2':q(),'score_coefficient_ln2':q(),'row_max_coefficient_ln2':0,'row_shift_coefficient_ln2':0,'centered_coefficient_ln2':0,'weight':q(1),'numerator_contribution':q(),'denominator_contribution':q(1)}
    head=lambda lag,i:{'lag':lag,'Q_coefficient_ln2':v(hd),'edges':[edge(j) for j in range(1,i+1)],'numerator':q(),'denominator':q(1),'output':q()}
    gates=[]
    for typ in ('K','Q'):
        for j,pattern in enumerate(([0,0],[0,1],[1,0],[1,1])):
            g={k:q() for k in ('input_1','input_2','sum','preactivation_1','preactivation_2','hinge_1','hinge_2','output')}
            g.update(type=typ,pattern=pattern,oracle=0,destination=(9 if typ=='K' else 13)+j);gates.append(g)
    a={'Q_coefficient_ln2':v(hd),'edges':[dict(edge(j),first_flag=q(),match=q()) for j in range(1,4)],'numerator':q(),'denominator':q(1),'output':q(),'probabilities':[q(1),q()],'pre_residual_state':v(md),'output_projection_write':v(md),'zero_head_write':v(md),'zero_ffn_write':v(md),'post_residual_state':v(md)}
    r={'schema':'one_hot_full_trace_v1',**m.BINDING_HASHES,'case_index':1,'N':n,'bits':'000','eta':q(1,4),'b':4,'c':7,'D':6,'head_dim':hd,'model_dim':md,'bit_vector':[0,0,0],'failure_stage':None,'partial_work':None,'passed':True,
       'layout':{'one':0,'x':1,'v':2,'z':3,'positions':[4,6],'copy1':7,'copy2':8,'K':[9,12],'Q':[13,16],'Y':17,'output':18},
       'projection_maps':{k:[] for k in ('offn','o1_lag1','o1_lag2','o2','q1_lag1','q1_lag2','k1_lag1','k1_lag2','v1','q2','k2','v2')},
       'input_states':[v(md) for i in range(n)],'first_attention':[{'i':i,'heads':[head(1,i),head(2,i)],'pre_residual_state':v(md),'output_projection_writes':[v(md),v(md)],'post_attention_residual_state':v(md)} for i in range(1,4)],
       'first_ffn':[{'i':i,'gates':copy.deepcopy(gates),'Y_input_x':q(),'Y_z':q(),'Y_hinge':q(),'Y':q(),'ffn_features':v(9),'pre_residual_state':v(md),'ffn_write':v(md),'post_residual_state':v(md)} for i in range(1,4)],'second_attention':a,
       'oracle':{'target':[0,0],'candidates':[{'j':3,'pair':[0,0],'match':True,'value':0}],'J':1,'C':0,'add_one':q(1,3),'absolute_error':q(),'contamination_bound':q()},
       'assertions':{k:True for k in m.assertion_keys(n)},'stage_status':{k:'completed' for k in ('case_setup','first_attention','first_ffn','second_attention_and_oracle')}}
    return r

if __name__=='__main__':unittest.main(verbosity=2)
