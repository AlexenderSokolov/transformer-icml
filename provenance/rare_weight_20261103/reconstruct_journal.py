#!/usr/bin/env python3
"""Reassemble the original journal bytes outside the public checkout without overwriting."""
from pathlib import Path
import argparse,hashlib,json,os,tempfile
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
def require(ok,message):
    if not ok:raise RuntimeError(message)
def digest(path):
    h=hashlib.sha256();n=0
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b);n+=len(b)
    return n,h.hexdigest()
def relative(path):
    p=Path(path);require(not p.is_absolute() and '..' not in p.parts,'Unsafe relative archive path');return p
def manifest():
    inv={x['path']:x for x in json.loads((ROOT/'provenance/PUBLIC_INVENTORY.json').read_text())['files']}
    for p in [Path(__file__),HERE/'JOURNAL_CHUNKS.json']:
        key=p.relative_to(ROOT).as_posix();require(key in inv,'Missing active inventory entry');n,h=digest(p);require((n,h)==(inv[key]['bytes'],inv[key]['sha256']),'Public archive metadata mismatch')
    m=json.loads((HERE/'JOURNAL_CHUNKS.json').read_text());offset=0
    for index,c in enumerate(m['chunks']):
        require(c['index']==index and c['offset']==offset,'Noncontiguous chunk manifest');key=relative(c['path']).as_posix();require(key in inv and c['bytes']==inv[key]['bytes'] and c['sha256']==inv[key]['sha256'] and c['git_blob_sha1']==inv[key]['git_blob_sha1'],'Chunk identity differs from active inventory');offset+=c['bytes']
    require(offset==m['source_identity']['bytes'],'Chunk total differs from original journal');return m

def reconstruct(output_root):
    m=manifest();dest=Path(output_root).resolve();require(not dest.is_relative_to(ROOT.resolve()),'Reconstruct only outside the public checkout')
    target=dest/relative(m['source_path']);require(not target.exists() and not target.is_symlink(),'Refusing to overwrite existing journal')
    require(target.parent.resolve().is_relative_to(dest),'Destination escapes output root');target.parent.mkdir(parents=True,exist_ok=True);require(target.parent.resolve().is_relative_to(dest),'Destination escapes output root')
    fd,name=tempfile.mkstemp(prefix='.journal-reconstruction-',dir=target.parent);temp=Path(name);h=hashlib.sha256();git=hashlib.sha1(b'blob '+str(m['source_identity']['bytes']).encode()+b'\0');total=0
    try:
        with os.fdopen(fd,'wb') as out:
            for c in m['chunks']:
                ch=hashlib.sha256();count=0
                with (ROOT/relative(c['path'])).open('rb') as f:
                    for b in iter(lambda:f.read(1048576),b''):out.write(b);ch.update(b);h.update(b);git.update(b);count+=len(b);total+=len(b)
                require(count==c['bytes'] and ch.hexdigest()==c['sha256'],'Corrupt or truncated journal chunk')
            out.flush();os.fsync(out.fileno())
        require(total==m['source_identity']['bytes'] and h.hexdigest()==m['source_identity']['sha256'] and git.hexdigest()==m['source_identity']['git_blob_sha1'],'Reconstructed journal identity mismatch')
        os.link(temp,target) # exclusive publication: fails if another file already exists
    finally:
        temp.unlink(missing_ok=True)
    return {'source_path':m['source_path'],'source_identity':m['source_identity'],'chunk_count':len(m['chunks']),'status':'EXACT_BYTE_RECONSTRUCTION_VERIFIED'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output-root',type=Path,required=True);args=p.parse_args();require(not args.output_root.resolve().is_relative_to(ROOT.resolve()),'Reconstruct only outside the public checkout');require(not args.output_root.exists() and not args.output_root.is_symlink(),'Output root must be new');args.output_root.mkdir(parents=True,exist_ok=False);r=reconstruct(args.output_root);print(json.dumps(r,indent=2))
    with (args.output_root/'JOURNAL_RECONSTRUCTION.json').open('x') as out:out.write(json.dumps(r,indent=2)+'\n')
