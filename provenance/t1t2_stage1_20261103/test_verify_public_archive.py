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
    def record(self,i,size=1):return {'path':'v10_research/fixture/file'+str(i)+'.txt','bytes':size,'sha256':'a'*64,'git_blob_sha1':'b'*40}
    def manifest(self):return {'schema':'t1t2-stage-files-v1','source_count':134,'files':[self.record(0)],'self_reference_boundary':'Manifest excludes itself and the global inventory.','scoped_directories':['v10_research/fixture',V.STAGE_DIR]}
    def source_map(self):
        rows=[]
        for i in range(134):
            size=1 if i>=2 else (8949000 if i==0 else 8949074)
            original={'bytes':size,'sha256':'a'*64,'git_blob_sha1':'b'*40}
            public=dict(original)
            if i>=83:public.update(sha256='c'*64,git_blob_sha1='d'*40,bytes=size+(481 if i==83 else 1))
            rows.append({'source_record_id':'FIX'+str(i).zfill(3),'path':self.record(i)['path'],'original':original,'public':public,'changed':i>=83})
        return {'schema':'t1t2-source-export-v1','source_count':134,'original_total_bytes':17898206,'export_total_bytes':17898737,'byte_exact_count':83,'changed_count':51,'files':rows}
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
        self.assertEqual(len(V.validate_source_map(m,entries)),134)
        changes=[lambda x:x.update(source_count=True),lambda x:x.update(changed_count=50),lambda x:x['files'][0].update(changed=0),lambda x:x['files'][0]['public'].update(sha256='c'*64),lambda x:x['files'][83].update(changed=False),lambda x:x['files'][1].update(source_record_id=x['files'][0]['source_record_id']),lambda x:x['files'][1].update(path=x['files'][0]['path']),lambda x:x.update(original_total_bytes=1)]
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
                for s in ['../x','/etc/passwd','scope//x','scope/../x']:self.rejects(tree.read,s,10)
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
        for doc,entries in [({},{}),({'inherited_public_files':rows+rows},{}),({'inherited_public_files':rows},{rows[0]['path']:rows[0]}),({'inherited_public_files':[self.record(i) for i in range(21)]},{})]:
            self.rejects(V.inherited_rows,doc,entries)

    def test_manifest_anchor_rejects_before_untrusted_metadata(self):
        with tempfile.TemporaryDirectory(dir=os.environ.get('TEST_TMPDIR')) as td:
            p=Path(td)/V.MANIFEST_PATH;p.parent.mkdir(parents=True);p.write_bytes(b'{"schema":"untrusted"}')
            self.rejects(V.verify_archive,td,'0'*64)

    def test_cli_requires_manifest_anchor_and_is_optimized_safe(self):
        for opts in [[],['--manifest-sha256','0'*64]]:
            q=subprocess.run([sys.executable,'-I','-B','-O',str(HERE/'verify_public_archive.py'),*opts],capture_output=True,text=True,timeout=120)
            self.assertNotEqual(q.returncode,0);self.assertEqual(q.stderr,'');self.assertEqual(json.loads(q.stdout)['status'],'FAIL')

if __name__=='__main__':unittest.main(verbosity=2)
