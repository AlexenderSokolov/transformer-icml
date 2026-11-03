#!/usr/bin/env python3
"""Read-only selected T1/T2 unknown-u/full-trace public-archive checker. This does not prove the science.

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

STAGE_DIR='provenance/t1t2_unknown_u_20261103'
MANIFEST_PATH=STAGE_DIR+'/STAGE_FILE_MANIFEST.json'
SOURCE_MAP_PATH=STAGE_DIR+'/SOURCE_EXPORT_MAP.json'
RECONCILIATION_PATH=STAGE_DIR+'/PUBLIC_EXPORT_RECONCILIATION.json'
MODULE_PATH=STAGE_DIR+'/validator/verify_full_trace.py'
MODULE_SHA256='a841acbc14134b9f2682ab5aaabe7b993e02ac3e06a11b8f548ee4eadae6d096'
TRACE_MANIFEST_PATH=STAGE_DIR+'/FULL_TRACE_CHUNKS.json'
TRACE_PATH='v10_research/route_a_bos_causal_compile_20261103_1411/full_trace_cases_v1.jsonl'
SOURCE_DIRECTORIES={
'v10_research/rare_reverse_matched_rate_20261103_1451',
'v10_research/independent_reverse_rate_review_20261103_1453',
'v10_research/rare_unknown_u_addone_20261103_1502',
'v10_research/independent_unknown_u_addone_review_20261103_1504',
'v10_research/rare_unknown_u_addone_20261103_1502_review_independent_20261103_1504',
'v10_research/route_a_compact_causal_20261103_1423',
'v10_research/independent_compact_causal_review_20261103_1425',
'v10_research/route_a_bos_causal_compile_20261103_1411',
}

MAX_FILE=16*1024*1024
MAX_TOTAL=256*1024*1024
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
    keys(o,'bytes sha256 git_blob_sha1');integer(o['bytes'],0,128*1024*1024);digest(o['sha256'],64);digest(o['git_blob_sha1'],40);return o

def file_entry(o):
    keys(o,'path bytes sha256 git_blob_sha1');safe_path(o['path']);identity({k:o[k] for k in ('bytes','sha256','git_blob_sha1')});integer(o['bytes'],0,MAX_FILE);return o


def validate_manifest(o):
    keys(o,'schema source_count files self_reference_boundary scoped_directories')
    require(o['schema']=='t1t2-unknown-u-stage-files-v1' and integer(o['source_count'])==41,'manifest schema/count')
    require(type(o['self_reference_boundary']) is str and 0<len(o['self_reference_boundary'])<=4096,'self reference boundary')
    require(type(o['files']) is list and 1<=len(o['files'])<=MAX_FILES,'manifest file limit')
    scopes=o['scoped_directories'];require(type(scopes) is list and len(scopes)<=40,'scope list');require(len({safe_path(p) for p in scopes})==len(scopes),'duplicate scopes')
    out={}
    for row in o['files']:
        file_entry(row);p=row['path'];require(p not in out and p!=MANIFEST_PATH and p not in GLOBAL_INVENTORIES,'duplicate/self/global entry');out[p]=row
    require(sum(r['bytes'] for r in out.values())<=MAX_TOTAL,'manifest total bytes');return out

def validate_source_map(o,entries):
    keys(o,'schema source_count original_total_bytes export_total_bytes byte_exact_count changed_count files')
    require(o['schema']=='t1t2-unknown-u-source-export-v1','source-map schema')
    for name,value in [('source_count',41),('original_total_bytes',79916758),('export_total_bytes',79916776),('byte_exact_count',34),('changed_count',7)]:require(integer(o[name])==value,'source-map expected '+name)
    require(type(o['files']) is list and len(o['files'])==41,'source-map length')
    paths=set();ids=set();physical=set();orig=pub=changed=0;split=None
    for row in o['files']:
        keys(row,'source_record_id path original public changed storage');p=safe_path(row['path']);rid=row['source_record_id']
        require(type(rid) is str and re.fullmatch('UAR[0-9]{3}',rid) is not None and rid not in ids,'source ID');ids.add(rid)
        require(p not in paths and '/'.join(p.split('/')[:2]) in SOURCE_DIRECTORIES,'duplicate/unscoped source');paths.add(p)
        a=identity(row['original']);b=identity(row['public']);require(type(row['changed']) is bool and (a!=b)==row['changed'],'changed flag')
        storage=row['storage'];require(type(storage) is dict and 'kind' in storage,'source storage')
        if storage['kind']=='file':
            keys(storage,'kind path');require(storage['path']==p and p in entries,'source file path');require(b=={k:entries[p][k] for k in ('bytes','sha256','git_blob_sha1')},'source public identity');physical.add(p)
        else:
            keys(storage,'kind manifest_path');require(storage['kind']=='lossless_chunks' and p==TRACE_PATH and split is None,'unexpected split source');require(storage['manifest_path']==TRACE_MANIFEST_PATH and TRACE_MANIFEST_PATH in entries,'split manifest');require(a==b and not row['changed'],'split source changed');split=row
        orig+=a['bytes'];pub+=b['bytes'];changed+=row['changed']
    require(split is not None and len(physical)==40,'split/physical count');require(orig==o['original_total_bytes'] and pub==o['export_total_bytes'] and changed==7,'source totals');return paths,physical,split

def check_bytes(data,row):
    file_entry(row);require(len(data)==row['bytes'],'file size: '+row['path']);require(hashlib.sha256(data).hexdigest()==row['sha256'],'SHA-256: '+row['path']);require(hashlib.sha1(b'blob '+str(len(data)).encode('ascii')+b'\0'+data).hexdigest()==row['git_blob_sha1'],'Git identity: '+row['path'])

def inherited_rows(recon,entries):
    require(type(recon) is dict and 'inherited_public_files' in recon,'inherited list missing');rows=recon['inherited_public_files'];require(type(rows) is list and len(rows)==88,'inherited list count');paths=set()
    for row in rows:
        file_entry(row);p=row['path'];require(p not in paths and p not in entries and p!=MANIFEST_PATH and p not in GLOBAL_INVENTORIES,'inherited duplicate/overlap');paths.add(p)
    require(sum(r['bytes'] for r in rows)+sum(r['bytes'] for r in entries.values())<=MAX_TOTAL,'combined size');return rows

def check_scopes(tree,expected,scopes):
    for scope in sorted(scopes):require(tree.files_under(scope)=={p for p in expected if p.startswith(scope+'/')},'missing/extra scoped file: '+scope)

def verify_split(tree,raw,split,entries):
    m=strict_json(raw);keys(m,'schema source chunks bindings');require(m['schema']=='t1t2-full-trace-chunks-v1','chunk schema');s=m['source'];keys(s,'path bytes sha256 rows');require(s['path']==TRACE_PATH and integer(s['bytes'])==split['public']['bytes'] and s['sha256']==split['public']['sha256'] and integer(s['rows'])==1008,'logical trace identity')
    require(type(m['chunks']) is list and len(m['chunks'])==20,'chunk count');h=hashlib.sha256();g=hashlib.sha1(b'blob '+str(s['bytes']).encode('ascii')+b'\0');offset=0;record=1
    for i,c in enumerate(m['chunks'],1):
        keys(c,'path index offset bytes first_record last_record sha256');p=safe_path(c['path']);require(p==STAGE_DIR+'/full_trace_chunks/part'+str(i).zfill(3)+'.jsonl' and integer(c['index'])==i,'chunk order/path');require(integer(c['offset'])==offset and integer(c['first_record'])==record,'chunk offset/records');require(p in entries and integer(c['bytes'],1,4*1024*1024)==entries[p]['bytes'] and c['sha256']==entries[p]['sha256'],'chunk manifest identity')
        data=tree.read(p);check_bytes(data,entries[p]);require(data.endswith(b'\n') and data.count(b'\n')==integer(c['last_record'],record,1008)-record+1,'chunk line boundaries');h.update(data);g.update(data);offset+=len(data);record=c['last_record']+1
    require(offset==s['bytes'] and record==1009 and h.hexdigest()==s['sha256'] and g.hexdigest()==split['public']['git_blob_sha1'],'concatenated source identity');return m

def bind_result(result,trace):
    require(type(result) is dict and result.get('status')=='PASS_ARCHIVED_BYTES_AND_SAVED_SCHEMA_ONLY','trace helper status')
    require(result.get('scientific_replay') is False and result.get('reconstructed') is False,'helper exceeded read-only mode')
    for k,v in [('bytes',79712544),('rows',1008),('chunks',20),('N3_records',16),('recorded_J_zero',236),('recorded_passed',1008),('recorded_failed',0),('recorded_true_assertions',157248)]:require(integer(result.get(k))==v,'trace result '+k)
    require(result.get('sha256')==trace['source']['sha256'] and result.get('source_path')==TRACE_PATH,'trace result identity')

def verify_archive(root,manifest_sha256):
    digest(manifest_sha256,64)
    with SafeTree(root) as tree:
        raw=tree.read(MANIFEST_PATH,MAX_JSON);require(hashlib.sha256(raw).hexdigest()==manifest_sha256,'untrusted stage manifest');manifest=strict_json(raw);entries=validate_manifest(manifest)
        required=(SOURCE_MAP_PATH,RECONCILIATION_PATH,MODULE_PATH,TRACE_MANIFEST_PATH);require(all(p in entries for p in required),'missing metadata/helper');saved={}
        for p,r in sorted(entries.items()):
            data=tree.read(p);check_bytes(data,r)
            if p in required:saved[p]=data
        sources,physical,split=validate_source_map(strict_json(saved[SOURCE_MAP_PATH]),entries);scopes={'/'.join(p.split('/')[:2]) for p in sources};require(scopes==SOURCE_DIRECTORIES,'source scope set');scopes.add(STAGE_DIR);require(set(manifest['scoped_directories'])==scopes,'declared scope set')
        require(all(p in physical or p.startswith(STAGE_DIR+'/') for p in entries),'non-source outside provenance');inherited=inherited_rows(strict_json(saved[RECONCILIATION_PATH]),entries)
        for r in inherited:check_bytes(tree.read(r['path']),r)
        expected=set(entries)|{MANIFEST_PATH}|{r['path'] for r in inherited};check_scopes(tree,expected,scopes)
        trace=verify_split(tree,saved[TRACE_MANIFEST_PATH],split,entries);module=saved[MODULE_PATH];require(hashlib.sha256(module).hexdigest()==MODULE_SHA256 and entries[MODULE_PATH]['sha256']==MODULE_SHA256,'pinned helper hash')
        namespace={'__name__':'verified_full_trace','__file__':MODULE_PATH};exec(compile(module,MODULE_PATH,'exec',dont_inherit=True),namespace)
        # Newly authored helper only; omission of destination preserves read-only mode.
        try:result=namespace['verify'](root,entries[TRACE_MANIFEST_PATH]['sha256'])
        except (ValueError,OSError,TypeError,KeyError,RecursionError) as exc:raise ArchiveError('trace helper failed: '+str(exc)) from exc
        bind_result(result,trace)
        # Reconcile reopened reads. This is not an atomic snapshot of a hostile filesystem.
        for p,r in sorted(entries.items()):check_bytes(tree.read(p),r)
        for r in inherited:check_bytes(tree.read(r['path']),r)
        require(tree.read(MANIFEST_PATH,MAX_JSON)==raw,'manifest changed');check_scopes(tree,expected,scopes)
    return {'status':'PASS_SELECTED_ARCHIVE_AND_SAVED_TRACE','manifest_sha256':manifest_sha256,'stage_files_verified':len(entries),'source_count':41,'byte_exact_sources':34,'mapped_sources':7,'logical_original_bytes':79916758,'logical_export_bytes':79916776,'inherited_files_verified':len(inherited),'helper_sha256':MODULE_SHA256,'trace_result':result,'scope':'Exact public files, mapped original identities, lossless logical trace reconstruction identity and saved-record consistency. No archived science execution, formal proof, novelty or full historical replay.'}

def main(argv=None):
    args=sys.argv[1:] if argv is None else argv
    try:
        require(len(args)==3 and args[1]=='--manifest-sha256','usage: python -I -B verify_public_archive.py ROOT --manifest-sha256 TRUSTED_SHA256');report=verify_archive(args[0],args[2])
    except (ArchiveError,OSError,ValueError,TypeError,KeyError,RecursionError) as exc:print(json.dumps({'status':'FAIL','error':str(exc)},sort_keys=True));return 1
    print(json.dumps(report,sort_keys=True,indent=2));return 0
if __name__=='__main__':sys.exit(main())
