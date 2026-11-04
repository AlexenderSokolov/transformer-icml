"""Explicit allowlist ZIP capture and independent byte-roundtrip verification.
Receipts are evidence records, not security boundaries. Never fabricate service IDs.
"""
import argparse, hashlib, json, os, zipfile
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def dump(path,obj):
    path=Path(path)
    with path.open('x',encoding='utf-8') as f:
        json.dump(obj,f,indent=2,allow_nan=False);f.write('\n');f.flush();os.fsync(f.fileno())

def allowed_name(name):
    p=PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or not p.parts or str(p)!=name:raise ValueError('unsafe archive name')
    return name

def make_archive(root,files,destination,kind,source_manifest_sha256):
    root=Path(root).resolve();destination=Path(destination)
    if destination.exists():raise FileExistsError(destination)
    if len(files)!=len(set(files)):raise ValueError('duplicate archive paths')
    entries=[]
    for n in files:
        allowed_name(n);p=root/n
        if p.is_symlink() or not p.resolve().is_relative_to(root):raise ValueError('symlink/escape')
        if not p.is_file():raise FileNotFoundError(p)
        entries.append({'path':n,'bytes':p.stat().st_size,'sha256':sha(p)})
    m={'schema':'v10_capture_manifest_v1','kind':kind,'source_manifest_sha256':source_manifest_sha256,'files':entries,'created_utc':now()}
    with zipfile.ZipFile(destination,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for e in entries:z.write(root/e['path'],e['path'])
        z.writestr('CAPTURE_MANIFEST.json',json.dumps(m,indent=2)+'\n')
    verify_archive(destination)
    return destination

def verify_archive(path):
    with zipfile.ZipFile(path) as z:
        if z.testzip() is not None:raise ValueError('corrupt ZIP')
        names=z.namelist()
        if len(names)!=len(set(names)):raise ValueError('duplicate ZIP members')
        for n in names:allowed_name(n)
        m=json.loads(z.read('CAPTURE_MANIFEST.json'))
        expected=[e['path'] for e in m['files']]+['CAPTURE_MANIFEST.json']
        if sorted(names)!=sorted(expected):raise ValueError('archive not exact allowlist')
        for e in m['files']:
            b=z.read(e['path'])
            if len(b)!=e['bytes'] or hashlib.sha256(b).hexdigest()!=e['sha256']:raise ValueError('member mismatch '+e['path'])
        if m['kind']=='source':
            if 'SOURCE_MANIFEST.json' not in names:raise ValueError('source manifest missing')
            if hashlib.sha256(z.read('SOURCE_MANIFEST.json')).hexdigest()!=m['source_manifest_sha256']:raise ValueError('source manifest hash mismatch')
            sm=json.loads(z.read('SOURCE_MANIFEST.json'))
            source_names=[e['path'] for e in sm['files']]
            if len(source_names)!=len(set(source_names)):raise ValueError('duplicate source manifest path')
            for e in sm['files']:
                allowed_name(e['path'])
                if e['path'] not in names or hashlib.sha256(z.read(e['path'])).hexdigest()!=e['sha256']:raise ValueError('source member binding mismatch')
            if 'SCIENTIFIC_REVIEW.json' not in names:raise ValueError('source independent review missing')
            review=json.loads(z.read('SCIENTIFIC_REVIEW.json'))
            if review.get('status')!='PASS' or review.get('source_manifest_sha256')!=m['source_manifest_sha256']:raise ValueError('source independent review mismatch')
    return m

def make_receipt(original,roundtrip,library_file_id):
    if not library_file_id.startswith('libfile_'):raise ValueError('actual Library ID required')
    if sha(original)!=sha(roundtrip):raise ValueError('roundtrip bytes differ')
    a=verify_archive(original);b=verify_archive(roundtrip)
    if a!=b:raise ValueError('manifests differ')
    return {'schema':'v10_capture_receipt_v1','kind':a['kind'],'source_manifest_sha256':a['source_manifest_sha256'],'archive_sha256':sha(original),'archive_bytes':Path(original).stat().st_size,'library_file_id':library_file_id,'roundtrip_verified':True,'verified_utc':now(),'member_count':len(a['files'])}

def require_receipt(receipt,archive,kind,source_manifest_sha256):
    r=json.loads(Path(receipt).read_text());m=verify_archive(archive)
    if r.get('schema')!='v10_capture_receipt_v1' or r.get('roundtrip_verified') is not True:raise ValueError('verified capture required')
    if r.get('kind')!=kind or m['kind']!=kind:raise ValueError('capture kind mismatch')
    if r.get('source_manifest_sha256')!=source_manifest_sha256 or m['source_manifest_sha256']!=source_manifest_sha256:raise ValueError('source binding mismatch')
    if r.get('archive_sha256')!=sha(archive) or r.get('archive_bytes')!=Path(archive).stat().st_size:raise ValueError('archive binding mismatch')
    if not r.get('library_file_id','').startswith('libfile_'):raise ValueError('capture identity missing')
    return r

def verify_local_payload(root,archive):
    m=verify_archive(archive)
    for e in m['files']:
        p=Path(root)/e['path']
        if not p.is_file() or p.is_symlink() or p.stat().st_size!=e['bytes'] or sha(p)!=e['sha256']:raise ValueError('local payload mismatch '+e['path'])
    return m

if __name__=='__main__':
    p=argparse.ArgumentParser();sp=p.add_subparsers(dest='command',required=True)
    v=sp.add_parser('receipt');v.add_argument('--original',required=True);v.add_argument('--roundtrip',required=True);v.add_argument('--library-file-id',required=True);v.add_argument('--output',required=True)
    v=sp.add_parser('verify');v.add_argument('archive')
    a=p.parse_args()
    if a.command=='verify':print(json.dumps(verify_archive(a.archive),indent=2))
    else:dump(a.output,make_receipt(a.original,a.roundtrip,a.library_file_id));print(a.output)
