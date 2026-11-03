#!/usr/bin/env python3
"""Materialize exact published scientific inputs and the losslessly split journal outside checkout."""
from pathlib import Path
import argparse,hashlib,json,sys
if not __debug__:
    raise RuntimeError('Optimized Python is not supported; historical scientific assertions must remain active')
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE))
import reconstruct_journal as journal
def require(ok,message):
    if not ok:raise RuntimeError(message)
def digest(b):return hashlib.sha256(b).hexdigest()
def safe(path):
    p=Path(path);require(not p.is_absolute() and '..' not in p.parts,'Unsafe source path');return p

def prepare(destination):
    requested=Path(destination);require(not requested.exists() and not requested.is_symlink(),'Destination must not exist');dest=requested.resolve();require(not dest.exists(),'Destination must not exist');require(not dest.is_relative_to(ROOT.resolve()),'Use a destination outside the public checkout')
    inv={x['path']:x for x in json.loads((ROOT/'provenance/PUBLIC_INVENTORY.json').read_text())['files']}
    for p in [Path(__file__),HERE/'SOURCE_EXPORT_MAP.json',HERE/'PUBLICATION_SCOPE_AND_CHECKS.json']:
        key=p.relative_to(ROOT).as_posix();b=p.read_bytes();require(key in inv and len(b)==inv[key]['bytes'] and digest(b)==inv[key]['sha256'],'Public replay metadata identity mismatch')
    mapping=json.loads((HERE/'SOURCE_EXPORT_MAP.json').read_text());scope=json.loads((HERE/'PUBLICATION_SCOPE_AND_CHECKS.json').read_text())
    inputs={x['path']:x['public']['sha256'] for x in mapping['files'] if x['storage']=='same_path'}
    inputs.update({x['path']:x['sha256'] for x in scope['exact_inherited_dependencies']})
    for path,h in inputs.items():
        b=(ROOT/safe(path)).read_bytes();require(path in inv and h==inv[path]['sha256'] and len(b)==inv[path]['bytes'] and digest(b)==h,'Public source identity mismatch: '+path)
    chunked=[x for x in mapping['files'] if x['storage']=='lossless_chunks'];require(len(chunked)==1,'Unexpected chunked source count');m=journal.manifest();require(chunked[0]['path']==m['source_path'] and chunked[0]['original']==m['source_identity'],'Journal source map mismatch')
    dest.mkdir(parents=True,exist_ok=False)
    for path,h in inputs.items():
        p=dest/safe(path);require(p.parent.resolve().is_relative_to(dest),'Copy destination escapes output root');p.parent.mkdir(parents=True,exist_ok=True);require(p.parent.resolve().is_relative_to(dest),'Copy destination escapes output root');b=(ROOT/path).read_bytes();require(digest(b)==h,'Source changed during copy')
        with p.open('xb') as out:out.write(b)
        require(digest(p.read_bytes())==h,'Copy mismatch')
    reconstructed=journal.reconstruct(dest)
    receipt={'status':'EXACT_PUBLIC_INPUTS_MATERIALIZED','copied_files':len(inputs),'journal':reconstructed,'source_binding_policy':'Historical seals and programs are unchanged. The sole normalized historical traceback is explicitly mapped; it is not a sealed training input and no seal or validation predicate is modified.','training_or_new_sampling':False}
    with (dest/'PUBLIC_REPLAY_PREPARATION.json').open('x') as out:out.write(json.dumps(receipt,indent=2)+'\n')
    return receipt
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--destination',type=Path,required=True);a=p.parse_args();print(json.dumps(prepare(a.destination),indent=2))
