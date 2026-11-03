#!/usr/bin/env python3
"""Outer-helper tests; synthetic metadata is not scientific case generation."""
import copy, hashlib, importlib.util, io, json, os
from pathlib import Path
import subprocess, sys, tempfile, unittest
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
p=HERE/'verify_public_archive.py'
if p.exists():
    spec=importlib.util.spec_from_file_location('outer',p);V=importlib.util.module_from_spec(spec);spec.loader.exec_module(V)
else:V=None

class OuterTests(unittest.TestCase):
    def setUp(self):self.assertIsNotNone(V,'outer validator not yet implemented')
    def rejects(self,fn,*args):
        with self.assertRaises(V.ArchiveError):fn(*args)
    def record(self,i,size=1):return {'path':'v10_research/route_a_sensitivity_bottleneck_20261103_1341/file'+str(i)+'.txt','bytes':size,'sha256':'a'*64,'git_blob_sha1':'b'*40}
    def manifest(self):return {'schema':'t1t2-followon-stage-files-v1','source_count':46,'files':[self.record(0)],'self_reference_boundary':'Manifest excludes itself and the global inventory.','scoped_directories':['v10_research/route_a_sensitivity_bottleneck_20261103_1341',V.STAGE_DIR]}
    def source_map(self):
        rows=[]
        for i in range(46):
            size=709285 if i==0 else 1
            original={'bytes':size,'sha256':'a'*64,'git_blob_sha1':'b'*40}
            public=dict(original)
            if i<15:public.update(sha256='c'*64,git_blob_sha1='d'*40,bytes=size-(26 if i==0 else 0))
            rows.append({'source_record_id':'FIX'+str(i).zfill(3),'path':self.record(i)['path'],'original':original,'public':public,'changed':i<15})
        return {'schema':'t1t2-followon-source-export-v1','source_count':46,'original_total_bytes':709330,'export_total_bytes':709304,'byte_exact_count':31,'changed_count':15,'files':rows}
    def test_strict_json_types_duplicates_limits(self):
        for s in ['{"a":1,"a":2}','{"a":NaN}','1.0','1e999','9'*100,'['*50+'0'+']'*50]:self.rejects(V.strict_json,s.encode())
        self.assertEqual(V.strict_json(b'{"a":true}'),{'a':True})
    def test_manifest_exact_schema_paths_and_ids(self):
        m=self.manifest();self.assertEqual(len(V.validate_manifest(m)),1)
        for change in [lambda x:x.update(source_count=True),lambda x:x.update(extra=1),lambda x:x['files'][0].update(bytes=True),lambda x:x['files'][0].update(path='../bad'),lambda x:x['files'][0].update(path='/bad'),lambda x:x['files'][0].update(sha256='A'*64),lambda x:x['files'].append(dict(x['files'][0]))]:
            obj=copy.deepcopy(m);change(obj);self.rejects(V.validate_manifest,obj)
    def test_manifest_rejects_self_and_global_inventory(self):
        for path in [V.MANIFEST_PATH,'provenance/PUBLIC_INVENTORY.json']:
            m=self.manifest();m['files'][0]['path']=path;self.rejects(V.validate_manifest,m)
    def test_source_map_totals_counts_and_identity_relations(self):
        m=self.source_map();entries={x['path']:dict(path=x['path'],**x['public']) for x in m['files']}
        self.assertEqual(len(V.validate_source_map(m,entries)),46)
        changes=[lambda x:x.update(source_count=True),lambda x:x.update(changed_count=14),lambda x:x['files'][0].update(changed=0),lambda x:x['files'][0]['public'].update(sha256='e'*64),lambda x:x['files'][0].update(changed=False),lambda x:x['files'][1].update(source_record_id=x['files'][0]['source_record_id']),lambda x:x['files'][1].update(path=x['files'][0]['path']),lambda x:x.update(original_total_bytes=1)]
        for change in changes:
            obj=copy.deepcopy(m);change(obj);self.rejects(V.validate_source_map,obj,entries)
    def test_source_map_must_match_manifest_public_identity(self):
        m=self.source_map();entries={x['path']:dict(path=x['path'],**x['public']) for x in m['files']};entries[m['files'][0]['path']]['bytes']+=1
        self.rejects(V.validate_source_map,m,entries)
    def test_hash_binding_and_git_blob_hash(self):
        data=b'abc\n';r={'path':'x','bytes':4,'sha256':'edeaaff3f1774ad2888673770c6d64097e391bc362d7d6fb34982ddf0efd18cb','git_blob_sha1':'8baef1b4abc478178b004d62031cf7fe6db6f903'}
        self.assertEqual(V.check_bytes(data,r),r)
        self.rejects(V.check_bytes,b'abd\n',r)
        q=dict(r,git_blob_sha1='0'*40);self.rejects(V.check_bytes,data,q)
    def test_safe_root_and_no_follow_tree_listing(self):
        with tempfile.TemporaryDirectory(dir=os.environ.get('TEST_TMPDIR')) as td:
            p=Path(td);(p/'scope').mkdir();(p/'scope'/'x').write_bytes(b'abc\n')
            with V.SafeTree(p) as tree:
                self.assertEqual(tree.read('scope/x',10),b'abc\n');self.assertEqual(tree.files_under('scope'),{'scope/x'})
                for s in ['../x','/etc/passwd','scope//x','scope/../x','scope\\x','scope/\x00x']:self.rejects(tree.read,s,10)
                (p/'scope'/'link').symlink_to(p/'scope'/'x');self.rejects(tree.read,'scope/link',10);self.rejects(tree.files_under,'scope')
    def test_bound_read_rejects_fifo_large_and_root_link(self):
        with tempfile.TemporaryDirectory(dir=os.environ.get('TEST_TMPDIR')) as td:
            p=Path(td);os.mkfifo(p/'fifo');(p/'x').write_bytes(b'012345');(p/'alias').symlink_to(p,target_is_directory=True)
            with V.SafeTree(p) as tree:
                self.rejects(tree.read,'fifo',10);self.rejects(tree.read,'x',5)
            self.rejects(V.SafeTree,p/'alias')
    def test_extra_files_only_within_selected_scopes(self):
        with tempfile.TemporaryDirectory(dir=os.environ.get('TEST_TMPDIR')) as td:
            p=Path(td);(p/'scope').mkdir();(p/'scope'/'a').write_text('a');(p/'inherited').mkdir();(p/'inherited'/'old').write_text('old')
            with V.SafeTree(p) as tree:
                V.check_scopes(tree,{'scope/a'},{'scope'})
                (p/'scope'/'extra').write_text('extra');self.rejects(V.check_scopes,tree,{'scope/a'},{'scope'})
    def test_inherited_list_is_explicit_bounded_unique_and_disjoint(self):
        rows=[self.record(1)];self.assertEqual(V.inherited_rows({'inherited_public_files':rows,'documentary':'unchanged prose'},{}),rows)
        for doc,entries in [({},{}),({'inherited_public_files':rows+rows},{}),({'inherited_public_files':rows},{rows[0]['path']:rows[0]}),({'inherited_public_files':[self.record(i) for i in range(31)]},{})]:
            self.rejects(V.inherited_rows,doc,entries)

    def test_manifest_anchor_rejects_before_untrusted_metadata(self):
        with tempfile.TemporaryDirectory(dir=os.environ.get('TEST_TMPDIR')) as td:
            p=Path(td)/V.MANIFEST_PATH;p.parent.mkdir(parents=True);p.write_bytes(b'{"schema":"untrusted"}')
            self.rejects(V.verify_archive,td,'0'*64)

    def test_cli_requires_manifest_anchor_and_is_optimized_safe(self):
        for opts in [[],['--manifest-sha256','0'*64]]:
            q=subprocess.run([sys.executable,'-I','-B','-O',str(HERE/'verify_public_archive.py'),*opts],capture_output=True,text=True,timeout=120)
            self.assertNotEqual(q.returncode,0);self.assertEqual(q.stderr,'');self.assertEqual(json.loads(q.stdout)['status'],'FAIL')

    def test_numeric_report_is_bound_to_manifest_entries(self):
        self.assertTrue(hasattr(V,'bind_numeric_result'),'numeric-to-manifest binding has not been implemented')
        paths=[
            'v10_research/route_a_sensitivity_bottleneck_20261103_1341/population_cases.jsonl',
            'v10_research/route_a_sensitivity_bottleneck_20261103_1341/reverse_moment_cases.jsonl',
            'v10_research/route_a_bos_causal_compile_20261103_1411/exhaustive_cases_v1.jsonl']
        key_hashes=['65cbb8a525be743ddf679b842e2ec858687124d15d0cc9d8af17f3e8e40fe6d4','66be101bf1cf65756a622f1686aef0a0bcc2e2d54509341eaa4bdc4444d5b084','e60b46b652983099336a3bb3aa3718b7ea65be1b2e338a7a479387ce113482cc']
        rows=[{'path':p,'records':count,'bytes':size,'observed_sha256':'a'*64,'ordered_input_sha256':key} for p,count,size,key in zip(paths,[90,8,1008],[11178,67949,420366],key_hashes)]
        result={'status':'PASS','scope':'retained consistency only','total_records':1106,'files':rows}
        entries={p:{'path':p,'bytes':size,'sha256':'a'*64,'git_blob_sha1':'b'*40} for p,size in zip(paths,[11178,67949,420366])}
        V.bind_numeric_result(result,entries)
        changes=[lambda r:r['files'][0].update(observed_sha256='b'*64),lambda r:r['files'][0].update(bytes=0),lambda r:r['files'][0].update(path=paths[1]),lambda r:r['files'][0].update(records=89),lambda r:r['files'][0].update(ordered_input_sha256='0'*64),lambda r:r.update(total_records=1105),lambda r:r.update(status='FAIL'),lambda r:r['files'].pop(),lambda r:r['files'].reverse()]
        for change in changes:
            obj=copy.deepcopy(result);change(obj);self.rejects(V.bind_numeric_result,obj,entries)

    def test_root_parent_traversal_is_not_normalized_away(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td);(p/'sub').mkdir()
            self.rejects(V.SafeTree,str(p)+'/sub/..')

    def test_nonisolated_cli_fails_before_archive_reads(self):
        q=subprocess.run([sys.executable,'-B',str(HERE/'verify_public_archive.py')],capture_output=True,text=True,timeout=30)
        self.assertEqual(q.returncode,2);self.assertEqual(json.loads(q.stdout)['status'],'FAIL')

    def test_inherited_global_inventory_is_rejected(self):
        row=self.record(1);row['path']='provenance/PUBLIC_INVENTORY.json'
        self.rejects(V.inherited_rows,{'inherited_public_files':[row]}, {})

if __name__=='__main__':unittest.main(verbosity=2)
