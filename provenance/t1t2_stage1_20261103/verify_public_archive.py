#!/usr/bin/env python3
"""Read-only selected T1/T2 public-archive checker. This does not prove the science.

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

STAGE_DIR='provenance/t1t2_stage1_20261103'
MANIFEST_PATH=STAGE_DIR+'/STAGE_FILE_MANIFEST.json'
SOURCE_MAP_PATH=STAGE_DIR+'/SOURCE_EXPORT_MAP.json'
RECONCILIATION_PATH=STAGE_DIR+'/PUBLIC_EXPORT_RECONCILIATION.json'
MODULE_PATH=STAGE_DIR+'/validator/verify_retained_records.py'
MODULE_SHA256='aa95d0d02a2ada571e4e33414e244705319be61a245d7a7ffaf862a15d633dd2'
MIXED_PARENT='v10_research/strong_mixing_precision'
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
            for p in os.path.abspath(os.fspath(root)).split('/')[1:]:
                if p:
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
            require((before.st_dev,before.st_ino,before.st_size,before.st_mtime_ns)==(after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns),'input changed during read')
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
    require(o['schema']=='t1t2-stage-files-v1' and integer(o['source_count'])==134,'manifest schema/count')
    require(type(o['self_reference_boundary']) is str and 0<len(o['self_reference_boundary'])<=4096,'missing self-reference explanation')
    require(type(o['files']) is list and 1<=len(o['files'])<=MAX_FILES,'manifest file limit')
    scopes=o['scoped_directories'];require(type(scopes) is list and 1<=len(scopes)<=40,'scope limit');require(len({safe_path(p) for p in scopes})==len(scopes),'duplicate scopes')
    out={};total=0
    for row in o['files']:
        file_entry(row);p=row['path'];require(p not in out and p!=MANIFEST_PATH and p not in GLOBAL_INVENTORIES,'duplicate, self, or global manifest entry');out[p]=row;total+=row['bytes']
    require(total<=MAX_TOTAL,'manifest total byte limit');return out

def validate_source_map(o,entries):
    keys(o,'schema source_count original_total_bytes export_total_bytes byte_exact_count changed_count files')
    require(o['schema']=='t1t2-source-export-v1','source-map schema')
    for name,value in [('source_count',134),('original_total_bytes',17898206),('export_total_bytes',17898737),('byte_exact_count',83),('changed_count',51)]:require(integer(o[name])==value,'source-map expected '+name)
    require(type(o['files']) is list and len(o['files'])==134,'source-map length')
    paths=set();ids=set();orig=0;pub=0;changed=0
    for row in o['files']:
        keys(row,'source_record_id path original public changed');p=safe_path(row['path']);rid=row['source_record_id']
        require(type(rid) is str and re.fullmatch('[A-Za-z0-9_-]{1,64}',rid) is not None and rid not in ids,'invalid or duplicate source ID');ids.add(rid)
        require(p not in paths and p in entries and p.startswith('v10_research/'),'missing/duplicate/unscoped source path');paths.add(p)
        a=identity(row['original']);b=identity(row['public']);require(type(row['changed']) is bool,'changed must be boolean')
        require((a!=b)==row['changed'],'changed flag disagrees with exact identity')
        require(b=={k:entries[p][k] for k in ('bytes','sha256','git_blob_sha1')},'source public identity differs from stage manifest')
        orig+=a['bytes'];pub+=b['bytes'];changed+=row['changed']
    require(orig==o['original_total_bytes'] and pub==o['export_total_bytes'],'source-map byte totals')
    require(changed==51 and 134-changed==83,'source-map disposition counts');return paths

def check_bytes(data,row):
    file_entry(row);require(len(data)==row['bytes'],'file size mismatch: '+row['path'])
    require(hashlib.sha256(data).hexdigest()==row['sha256'],'SHA-256 mismatch: '+row['path'])
    require(hashlib.sha1(b'blob '+str(len(data)).encode('ascii')+b'\0'+data).hexdigest()==row['git_blob_sha1'],'Git blob SHA-1 mismatch: '+row['path']);return row

def check_scopes(tree,expected,scopes):
    for scope in sorted(scopes):
        wanted={p for p in expected if p.startswith(scope+'/')};require(tree.files_under(scope)==wanted,'missing or extra file in scope: '+scope)

def inherited_rows(reconciliation,entries):
    require(type(reconciliation) is dict and 'inherited_public_files' in reconciliation,'missing explicit inherited file list')
    rows=reconciliation['inherited_public_files'];require(type(rows) is list and len(rows)<=20,'inherited file list limit')
    paths=set()
    for row in rows:
        file_entry(row);p=row['path'];require(p not in paths and p not in entries and p!=MANIFEST_PATH,'duplicate/overlapping inherited path');paths.add(p)
    require(sum(x['bytes'] for x in rows)<=MAX_TOTAL,'inherited byte limit');return rows

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
        expected_scopes={p.rsplit('/',1)[0] for p in sources};expected_scopes.discard(MIXED_PARENT);expected_scopes.add(STAGE_DIR)
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
        # Reconcile again after the numeric pass; no global atomic-snapshot claim is made.
        for p,row in sorted(entries.items()):check_bytes(tree.read(p),row)
        for row in inherited:check_bytes(tree.read(row['path']),row)
        require(tree.read(MANIFEST_PATH,MAX_JSON)==manifest_raw,'manifest changed during validation')
        check_scopes(tree,set(entries)|{MANIFEST_PATH},expected_scopes)
    return {'status':'PASS_SELECTED_ARCHIVE_AND_RETAINED_RECORD_CONSISTENCY','manifest_sha256':manifest_sha256,'stage_files_verified':len(entries),'source_count':134,'byte_exact_sources':83,'mapped_sources':51,'original_total_bytes':17898206,'export_total_bytes':17898737,'inherited_files_verified':len(inherited),'verifier_sha256':MODULE_SHA256,'numeric_result':numeric,'scope':'Selected stage bytes, declared source/export identities, explicit inherited file identities, new-directory extra-file checks, and retained-record consistency. Not proof certification, source-rights clearance, or full historical closure.'}

def main(argv=None):
    args=sys.argv[1:] if argv is None else argv
    try:
        require(len(args)==3 and args[1]=='--manifest-sha256','usage: python -I -B verify_public_archive.py ROOT --manifest-sha256 TRUSTED_SHA256')
        report=verify_archive(args[0],args[2])
    except (ArchiveError,OSError,ValueError,csv.Error) as exc:
        print(json.dumps({'status':'FAIL','error':str(exc)},sort_keys=True));return 1
    print(json.dumps(report,sort_keys=True,indent=2));return 0

if __name__=='__main__':sys.exit(main())
