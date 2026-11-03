#!/usr/bin/env python3
"""Read-only selected T1/T2 follow-on public-archive checker. This does not prove the science.

Run: python -I -B verify_public_archive.py ROOT --manifest-sha256 TRUSTED_SHA256
The trusted SHA must come from an external release receipt or an independently
trusted commit/inventory, not merely a newly computed hash of an untrusted manifest.
Only the separately authored, fixed-hash retained-record verifier is executed.
No original archived research program is imported or executed.
"""
import sys
# Check before non-builtin imports: isolated mode prevents archive module shadowing.
if not sys.flags.isolated or not sys.dont_write_bytecode:
    print('{"status":"FAIL","error":"Run this helper with python -I -B."}')
    raise SystemExit(2)
import csv
from fractions import Fraction
import hashlib
import io
import json
import os
import re
import stat

STAGE_DIR='provenance/t1t2_followon_20261103'
MANIFEST_PATH=STAGE_DIR+'/STAGE_FILE_MANIFEST.json'
SOURCE_MAP_PATH=STAGE_DIR+'/SOURCE_EXPORT_MAP.json'
RECONCILIATION_PATH=STAGE_DIR+'/PUBLIC_EXPORT_RECONCILIATION.json'
MODULE_PATH=STAGE_DIR+'/validator/verify_retained_records.py'
MODULE_SHA256='95f7da4de8376330c19605fb2c5b715fd18089960b17b1e8286d3141eae2cca4'
SOURCE_DIRECTORIES={
    'v10_research/route_b_source_novelty_20261103_1312',
    'v10_research/independent_single_head_review_20261103_131631_2',
    'v10_research/route_a_sensitivity_bottleneck_20261103_1341',
    'v10_research/route_a_bos_causal_compile_20261103_1411',
    'v10_research/independent_no_bos_compile_review_20261103_1415',
    'v10_research/route_a_causal_prior_audit_20261103_1409',
}
MAX_FILE=16*1024*1024
MAX_TOTAL=64*1024*1024
MAX_JSON=4*1024*1024
MAX_FILES=512
GLOBAL_INVENTORIES={'provenance/PUBLIC_INVENTORY.json'}

class ArchiveError(ValueError):pass

def require(ok,message):
    if not ok:raise ArchiveError(message)

def keys(obj,names):require(type(obj) is dict and set(obj)==set(names.split()),'unexpected or missing schema fields')
def integer(x,low=0,high=MAX_TOTAL):
    require(type(x) is int and low<=x<=high,'invalid bounded integer');return x

def digest(x,length):
    require(type(x) is str and re.fullmatch('[0-9a-f]{'+str(length)+'}',x) is not None,'invalid digest');return x

def safe_path(path):
    require(type(path) is str and 0<len(path)<=512 and not path.startswith('/') and '\\' not in path,'unsafe path')
    parts=path.split('/');require(len(parts)<=20 and all(x not in ('','.','..') and '\x00' not in x and all(ord(c)>=32 for c in x) for x in parts),'unsafe path components')
    return path

def strict_json(raw):
    require(type(raw) is bytes and len(raw)<=MAX_JSON,'JSON byte limit')
    def pairs(values):
        o={}
        for k,v in values:require(k not in o,'duplicate JSON key');o[k]=v
        return o
    def parse_int(s):require(len(s.lstrip('-'))<=32,'JSON integer too long');return int(s)
    def reject(s):raise ArchiveError('floats and nonfinite values are forbidden')
    try:o=json.loads(raw.decode('utf-8'),object_pairs_hook=pairs,parse_int=parse_int,parse_float=reject,parse_constant=reject)
    except (ValueError,UnicodeDecodeError,RecursionError) as exc:raise ArchiveError('invalid strict JSON') from exc
    budget=[0]
    def check(x,depth):
        budget[0]+=1;require(depth<=16 and budget[0]<=50000,'JSON structure limit')
        if type(x) is dict:
            require(len(x)<=128,'too many JSON keys')
            for k,v in x.items():require(len(k)<=256,'JSON key too long');check(v,depth+1)
        elif type(x) is list:
            require(len(x)<=1024,'JSON array too long')
            for v in x:check(v,depth+1)
        elif type(x) is str:require(len(x)<=65536,'JSON string too long')
    check(o,0);return o

class SafeTree:
    """Bounded descriptor reads and scans, never following symlink components."""
    def __init__(self,root):
        require(hasattr(os,'O_NOFOLLOW') and os.open in os.supports_dir_fd,'safe descriptor reads unavailable')
        self.fd=None;fd=None
        try:
            fd=os.open('/',os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW)
            root=os.fspath(root)
            require(type(root) is str and '\x00' not in root and '..' not in root.split('/'),'unsafe root')
            absolute=root if root.startswith('/') else os.getcwd()+'/'+root
            for p in absolute.split('/')[1:]:
                if p not in ('','.'):
                    nxt=os.open(p,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=fd);os.close(fd);fd=nxt
            self.fd=fd
        except (OSError,ValueError,TypeError) as exc:
            if fd is not None:os.close(fd)
            raise ArchiveError('invalid non-symlink root') from exc
    def __enter__(self):return self
    def __exit__(self,*args):
        if self.fd is not None:os.close(self.fd);self.fd=None
    def directory(self,path):
        safe_path(path);fd=None
        try:
            fd=os.dup(self.fd)
            for p in path.split('/'):
                nxt=os.open(p,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=fd);os.close(fd);fd=nxt
            result=fd;fd=None;return result
        except (OSError,ValueError,TypeError) as exc:raise ArchiveError('unsafe or missing directory: '+path) from exc
        finally:
            if fd is not None:os.close(fd)
    def read(self,path,limit=MAX_FILE):
        safe_path(path);fd=None;f=None
        try:
            parts=path.split('/');fd=self.directory('/'.join(parts[:-1])) if len(parts)>1 else os.dup(self.fd)
            f=os.open(parts[-1],os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK,dir_fd=fd)
            before=os.fstat(f);require(stat.S_ISREG(before.st_mode) and before.st_size<=limit,'input not a bounded regular file')
            chunks=[];size=0
            while True:
                b=os.read(f,min(65536,limit+1-size))
                if not b:break
                chunks.append(b);size+=len(b);require(size<=limit,'input grew beyond limit')
            after=os.fstat(f)
            require((before.st_dev,before.st_ino,before.st_size,before.st_mtime_ns,before.st_ctime_ns)==(after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns,after.st_ctime_ns),'input changed during read')
            require(size==before.st_size,'input size changed during read')
            return b''.join(chunks)
        except (OSError,ValueError,TypeError) as exc:raise ArchiveError('unsafe or unreadable file: '+path) from exc
        finally:
            if f is not None:os.close(f)
            if fd is not None:os.close(fd)
    def files_under(self,path):
        safe_path(path);found=set();visited=[0]
        def walk(fd,prefix,depth):
            require(depth<=20,'directory depth limit')
            names=os.listdir(fd);require(len(names)<=MAX_FILES,'directory width limit')
            for name in sorted(names):
                visited[0]+=1;require(visited[0]<=1024,'directory entry limit');p=safe_path(prefix+'/'+name)
                info=os.stat(name,dir_fd=fd,follow_symlinks=False)
                if stat.S_ISDIR(info.st_mode):
                    child=os.open(name,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=fd)
                    try:walk(child,p,depth+1)
                    finally:os.close(child)
                else:require(stat.S_ISREG(info.st_mode),'nonregular or symlink scoped entry');found.add(p)
        fd=self.directory(path)
        try:walk(fd,path,0)
        except OSError as exc:raise ArchiveError('scope changed or became unreadable') from exc
        finally:os.close(fd)
        return found

def identity(o):
    keys(o,'bytes sha256 git_blob_sha1');integer(o['bytes'],0,MAX_FILE);digest(o['sha256'],64);digest(o['git_blob_sha1'],40);return o

def file_entry(o):
    keys(o,'path bytes sha256 git_blob_sha1');safe_path(o['path']);identity({k:o[k] for k in ('bytes','sha256','git_blob_sha1')});return o

def validate_manifest(o):
    keys(o,'schema source_count files self_reference_boundary scoped_directories')
    require(o['schema']=='t1t2-followon-stage-files-v1' and integer(o['source_count'])==46,'manifest schema/count')
    require(type(o['self_reference_boundary']) is str and 0<len(o['self_reference_boundary'])<=4096,'missing self-reference explanation')
    require(type(o['files']) is list and 1<=len(o['files'])<=MAX_FILES,'manifest file limit')
    scopes=o['scoped_directories'];require(type(scopes) is list and 1<=len(scopes)<=40,'scope limit');require(len({safe_path(p) for p in scopes})==len(scopes),'duplicate scopes')
    out={};total=0
    for row in o['files']:
        file_entry(row);p=row['path'];require(p not in out and p!=MANIFEST_PATH and p not in GLOBAL_INVENTORIES,'duplicate, self, or global manifest entry');out[p]=row;total+=row['bytes']
    require(total<=MAX_TOTAL,'manifest total byte limit');return out

def validate_source_map(o,entries):
    keys(o,'schema source_count original_total_bytes export_total_bytes byte_exact_count changed_count files')
    require(o['schema']=='t1t2-followon-source-export-v1','source-map schema')
    for name,value in [('source_count',46),('original_total_bytes',709330),('export_total_bytes',709304),('byte_exact_count',31),('changed_count',15)]:require(integer(o[name])==value,'source-map expected '+name)
    require(type(o['files']) is list and len(o['files'])==46,'source-map length')
    paths=set();ids=set();orig=0;pub=0;changed=0
    for row in o['files']:
        keys(row,'source_record_id path original public changed');p=safe_path(row['path']);rid=row['source_record_id']
        require(type(rid) is str and re.fullmatch('[A-Za-z0-9_-]{1,64}',rid) is not None and rid not in ids,'invalid or duplicate source ID');ids.add(rid)
        require(p not in paths and p in entries and p.rsplit('/',1)[0] in SOURCE_DIRECTORIES,'missing/duplicate/unscoped source path');paths.add(p)
        a=identity(row['original']);b=identity(row['public']);require(type(row['changed']) is bool,'changed must be boolean')
        require((a!=b)==row['changed'],'changed flag disagrees with exact identity')
        require(b=={k:entries[p][k] for k in ('bytes','sha256','git_blob_sha1')},'source public identity differs from stage manifest')
        orig+=a['bytes'];pub+=b['bytes'];changed+=row['changed']
    require(orig==o['original_total_bytes'] and pub==o['export_total_bytes'],'source-map byte totals')
    require(changed==15 and 46-changed==31,'source-map disposition counts');return paths

def check_bytes(data,row):
    file_entry(row);require(len(data)==row['bytes'],'file size mismatch: '+row['path'])
    require(hashlib.sha256(data).hexdigest()==row['sha256'],'SHA-256 mismatch: '+row['path'])
    require(hashlib.sha1(b'blob '+str(len(data)).encode('ascii')+b'\0'+data).hexdigest()==row['git_blob_sha1'],'Git blob SHA-1 mismatch: '+row['path']);return row

def check_scopes(tree,expected,scopes):
    for scope in sorted(scopes):
        wanted={p for p in expected if p.startswith(scope+'/')};require(tree.files_under(scope)==wanted,'missing or extra file in scope: '+scope)

def inherited_rows(reconciliation,entries):
    require(type(reconciliation) is dict and 'inherited_public_files' in reconciliation,'missing explicit inherited file list')
    rows=reconciliation['inherited_public_files'];require(type(rows) is list and len(rows)<=30,'inherited file list limit')
    paths=set()
    for row in rows:
        file_entry(row);p=row['path'];require(p not in paths and p not in entries and p!=MANIFEST_PATH and p not in GLOBAL_INVENTORIES,'duplicate/overlapping/global inherited path');paths.add(p)
    require(sum(x['bytes'] for x in rows)+sum(x['bytes'] for x in entries.values())<=MAX_TOTAL,'combined inherited/stage byte limit');return rows

def bind_numeric_result(result,entries):
    """Bind the reopened numeric reads to the same manifest-verified byte identities."""
    keys(result,'status scope total_records files')
    require(result['status']=='PASS' and integer(result['total_records'])==1106,'numeric result status/count mismatch')
    require(type(result['scope']) is str and 0<len(result['scope'])<=1024,'invalid numeric result scope')
    require(type(result['files']) is list and len(result['files'])==3,'numeric file result count mismatch')
    expected=(
        ('v10_research/route_a_sensitivity_bottleneck_20261103_1341/population_cases.jsonl',90,'65cbb8a525be743ddf679b842e2ec858687124d15d0cc9d8af17f3e8e40fe6d4'),
        ('v10_research/route_a_sensitivity_bottleneck_20261103_1341/reverse_moment_cases.jsonl',8,'66be101bf1cf65756a622f1686aef0a0bcc2e2d54509341eaa4bdc4444d5b084'),
        ('v10_research/route_a_bos_causal_compile_20261103_1411/exhaustive_cases_v1.jsonl',1008,'e60b46b652983099336a3bb3aa3718b7ea65be1b2e338a7a479387ce113482cc'),
    )
    for row,(path,count,input_digest) in zip(result['files'],expected):
        keys(row,'path records bytes observed_sha256 ordered_input_sha256')
        require(row['path']==path and path in entries,'numeric path mismatch')
        require(integer(row['records'])==count,'numeric saved-record count mismatch')
        require(integer(row['bytes'])==entries[path]['bytes'],'numeric byte length differs from manifest')
        require(digest(row['observed_sha256'],64)==entries[path]['sha256'],'numeric observed hash differs from manifest')
        require(digest(row['ordered_input_sha256'],64)==input_digest,'numeric input coverage hash mismatch')

def verify_archive(root,manifest_sha256):
    digest(manifest_sha256,64)
    with SafeTree(root) as tree:
        manifest_raw=tree.read(MANIFEST_PATH,MAX_JSON);require(hashlib.sha256(manifest_raw).hexdigest()==manifest_sha256,'stage manifest does not match external trusted SHA-256')
        manifest=strict_json(manifest_raw);entries=validate_manifest(manifest)
        require(all(p in entries for p in (SOURCE_MAP_PATH,RECONCILIATION_PATH,MODULE_PATH)),'required metadata/module not listed')
        saved={}
        for p,row in sorted(entries.items()):
            raw=tree.read(p);check_bytes(raw,row)
            if p in (SOURCE_MAP_PATH,RECONCILIATION_PATH,MODULE_PATH):saved[p]=raw
        sources=validate_source_map(strict_json(saved[SOURCE_MAP_PATH]),entries)
        expected_scopes={p.rsplit('/',1)[0] for p in sources};require(expected_scopes==SOURCE_DIRECTORIES,'source directory set mismatch');expected_scopes.add(STAGE_DIR)
        require(set(manifest['scoped_directories'])==expected_scopes,'declared scopes disagree with new source directories')
        require(all(p in sources or p.startswith(STAGE_DIR+'/') for p in entries),'non-source file outside stage provenance')
        check_scopes(tree,set(entries)|{MANIFEST_PATH},expected_scopes)
        inherited=inherited_rows(strict_json(saved[RECONCILIATION_PATH]),entries)
        for row in inherited:check_bytes(tree.read(row['path']),row)
        module=saved[MODULE_PATH];require(hashlib.sha256(module).hexdigest()==MODULE_SHA256 and entries[MODULE_PATH]['sha256']==MODULE_SHA256,'retained verifier identity mismatch')
        # This one explicitly pinned, newly authored verifier is not an archived research program.
        namespace={'__name__':'verified_retained_records','__file__':MODULE_PATH}
        exec(compile(module,MODULE_PATH,'exec',dont_inherit=True),namespace)
        try:numeric=namespace['verify_records'](root)
        except (ValueError,OSError,csv.Error) as exc:raise ArchiveError('retained-record validation failed: '+str(exc)) from exc
        bind_numeric_result(numeric,entries)
        # Reconcile again after the numeric pass; no global atomic-snapshot claim is made.
        for p,row in sorted(entries.items()):check_bytes(tree.read(p),row)
        for row in inherited:check_bytes(tree.read(row['path']),row)
        require(tree.read(MANIFEST_PATH,MAX_JSON)==manifest_raw,'manifest changed during validation')
        check_scopes(tree,set(entries)|{MANIFEST_PATH},expected_scopes)
    return {'status':'PASS_SELECTED_ARCHIVE_AND_RETAINED_RECORD_CONSISTENCY','manifest_sha256':manifest_sha256,'stage_files_verified':len(entries),'source_count':46,'byte_exact_sources':31,'mapped_sources':15,'original_total_bytes':709330,'export_total_bytes':709304,'inherited_files_verified':len(inherited),'verifier_sha256':MODULE_SHA256,'numeric_result':numeric,'scope':'Selected stage bytes, declared source/export identities, explicit inherited file identities, new-directory extra-file checks, and retained-record consistency. Not proof certification, source-rights clearance, or full historical closure.'}

def main(argv=None):
    args=sys.argv[1:] if argv is None else argv
    try:
        require(len(args)==3 and args[1]=='--manifest-sha256','usage: python -I -B verify_public_archive.py ROOT --manifest-sha256 TRUSTED_SHA256')
        report=verify_archive(args[0],args[2])
    except (ArchiveError,OSError,ValueError,csv.Error) as exc:
        print(json.dumps({'status':'FAIL','error':str(exc)},sort_keys=True));return 1
    print(json.dumps(report,sort_keys=True,indent=2));return 0

if __name__=='__main__':sys.exit(main())
