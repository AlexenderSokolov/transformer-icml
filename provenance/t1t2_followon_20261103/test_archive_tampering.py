#!/usr/bin/env python3
"""Tamper checks on new copies of a supplied retained archive only.

Run: python -I -B test_archive_tampering.py PUBLIC_ROOT TRUSTED_MANIFEST_SHA256
No archived scientific program is run; no scientific cases are generated.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile

if not sys.flags.isolated or not sys.dont_write_bytecode:raise SystemExit('Use python -I -B')
HERE=Path(__file__).parent
WRAPPER_SHA256='e9048f6ea2d9c171b31755eda3d34e283f6dfe679576c5f0dad82f304b3ca2ad'
p=HERE/'verify_public_archive.py'
if hashlib.sha256(p.read_bytes()).hexdigest()!=WRAPPER_SHA256:raise SystemExit('wrapper pin mismatch')
spec=importlib.util.spec_from_file_location('pinned_outer_checker',p)
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
if len(sys.argv)!=3:raise SystemExit('Expected PUBLIC_ROOT TRUSTED_MANIFEST_SHA256')
source=Path(sys.argv[1]);trusted=sys.argv[2]
# Require a valid baseline before making any corrupt copy.
v.verify_archive(source,trusted)
with v.SafeTree(source) as tree:
    manifest_raw=tree.read(v.MANIFEST_PATH,v.MAX_JSON)
    manifest=v.strict_json(manifest_raw)
    entries=v.validate_manifest(manifest)
    recon=v.strict_json(tree.read(v.RECONCILIATION_PATH))
    inherited=v.inherited_rows(recon,entries)
    all_paths=set(entries)|{v.MANIFEST_PATH}|{x['path'] for x in inherited}
    saved={p:tree.read(p) for p in all_paths}
results=[]

def reject(label,root,anchor,expected):
    try:v.verify_archive(root,anchor)
    except v.ArchiveError as exc:
        message=str(exc)
        if expected not in message:raise RuntimeError(label+': unexpected rejection '+message)
        results.append({'case':label,'status':'CORRECTLY_REJECTED','reason':message})
    else:raise RuntimeError(label+': unexpectedly accepted')

def write_json(path,value):path.write_text(json.dumps(value,sort_keys=True,indent=2)+'\n')

def repin(root,manifest,path):
    data=(root/path).read_bytes()
    for row in manifest['files']:
        if row['path']==path:
            row.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob_sha1=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())
            break
    else:raise RuntimeError('test target not in stage manifest')
    write_json(root/v.MANIFEST_PATH,manifest)
    return hashlib.sha256((root/v.MANIFEST_PATH).read_bytes()).hexdigest()

reject('wrong_external_manifest_anchor',source,'0'*64,'external trusted SHA-256')
modes=['byte_corruption','extra_source_file','extra_provenance_file','symlink_source','duplicate_manifest_key','pinned_module_corruption','source_map_total_corruption','source_map_changed_flag_corruption','global_inherited_inventory']
if inherited:modes.append('inherited_byte_corruption')
for mode in modes:
    with tempfile.TemporaryDirectory(prefix='archive-tamper-tests-') as td:
        root=Path(td)/'copy';root.mkdir()
        for relative,data in saved.items():
            target=root/relative;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
        current=json.loads(manifest_raw)
        source_map=json.loads(saved[v.SOURCE_MAP_PATH])
        source_path=source_map['files'][0]['path']
        if mode=='byte_corruption':
            target=root/source_path;b=target.read_bytes();target.write_bytes(bytes([b[0]^1])+b[1:]);reject(mode,root,trusted,'SHA-256 mismatch')
        elif mode in ('extra_source_file','extra_provenance_file'):
            directory=(root/source_path).parent if mode=='extra_source_file' else root/v.STAGE_DIR
            (directory/'unexpected_test_copy.txt').write_bytes(b'benign corruption fixture\n');reject(mode,root,trusted,'missing or extra file in scope')
        elif mode=='symlink_source':
            target=root/source_path;target.unlink();target.symlink_to(source/source_path);reject(mode,root,trusted,'unsafe or unreadable file')
        elif mode=='duplicate_manifest_key':
            data=manifest_raw.replace(b'{',b'{"schema":"duplicate",',1)
            (root/v.MANIFEST_PATH).write_bytes(data);reject(mode,root,hashlib.sha256(data).hexdigest(),'invalid strict JSON')
        elif mode=='pinned_module_corruption':
            target=root/v.MODULE_PATH;target.write_bytes(target.read_bytes()+b'\n# deterministic corruption\n')
            anchor=repin(root,current,v.MODULE_PATH);reject(mode,root,anchor,'retained verifier identity mismatch')
        elif mode in ('source_map_total_corruption','source_map_changed_flag_corruption'):
            if mode=='source_map_total_corruption':source_map['original_total_bytes']+=1
            else:source_map['files'][0]['changed']=not source_map['files'][0]['changed']
            write_json(root/v.SOURCE_MAP_PATH,source_map);anchor=repin(root,current,v.SOURCE_MAP_PATH)
            reject(mode,root,anchor,'source-map expected original_total_bytes' if mode=='source_map_total_corruption' else 'changed flag disagrees')
        elif mode=='global_inherited_inventory':
            obj=json.loads(saved[v.RECONCILIATION_PATH]);obj['inherited_public_files'].append({'path':'provenance/PUBLIC_INVENTORY.json','bytes':0,'sha256':hashlib.sha256(b'').hexdigest(),'git_blob_sha1':hashlib.sha1(b'blob 0\0').hexdigest()})
            write_json(root/v.RECONCILIATION_PATH,obj);anchor=repin(root,current,v.RECONCILIATION_PATH)
            reject(mode,root,anchor,'duplicate/overlapping/global inherited path')
        elif mode=='inherited_byte_corruption':
            target=root/inherited[0]['path'];data=target.read_bytes();target.write_bytes((bytes([data[0]^1])+data[1:]) if data else b'x')
            reject(mode,root,trusted,'SHA-256 mismatch' if data else 'file size mismatch')
print(json.dumps({'status':'PASS_SELECTED_ARCHIVE_TAMPER_TESTS','wrapper_sha256':WRAPPER_SHA256,'reference_manifest_sha256':trusted,'cases':results},sort_keys=True,indent=2))
