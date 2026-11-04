#!/usr/bin/env python3
"""Verify all public chunks/members and losslessly restore privacy-screened captures.
Original manifests remain historical evidence. This tool uses PUBLIC_ARCHIVE_INDEX.
No private service credentials, downloads, random sampling, or training are used.
"""
import argparse, hashlib, json, zipfile, shutil
from pathlib import Path, PurePosixPath
HERE=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def safe(name):
 p=PurePosixPath(name)
 if p.is_absolute() or '..' in p.parts or str(p)!=name or '\\' in name:raise ValueError('unsafe path')
 return p

def restore(destination):
 destination=Path(destination).resolve()
 if destination.exists():raise FileExistsError('Use a new output directory, never overwrite evidence.')
 destination.mkdir(parents=True)
 index=json.loads((HERE/'PUBLIC_ARCHIVE_INDEX.json').read_text())
 total=0
 for c in index['captures']:
  zpath=destination/f'_capture_{c["capture"]:02d}.zip'
  with zpath.open('xb') as f:
   for part in c['chunks']:
    b=(HERE/safe(part['path'])).read_bytes()
    if len(b)!=part['bytes'] or sha(b)!=part['sha256']:raise ValueError('chunk mismatch: '+part['path'])
    f.write(b)
  b=zpath.read_bytes()
  if len(b)!=c['public_archive_bytes'] or sha(b)!=c['public_archive_sha256']:raise ValueError('archive mismatch')
  base=destination if c['restore_directory']=='.' else destination/safe(c['restore_directory'])
  with zipfile.ZipFile(zpath) as z:
   names=z.namelist();expected={r['path']:r for r in c['members']}
   if len(names)!=len(set(names)) or set(names)!=set(expected):raise ValueError('archive membership mismatch')
   for name in names:
    p=base/safe(name);b=z.read(name);r=expected[name]
    if len(b)!=r['public_bytes'] or sha(b)!=r['public_sha256']:raise ValueError('member mismatch: '+name)
    if name.endswith(('.npy','.npz')) and (not r['byte_identical'] or sha(b)!=r['original_sha256']):raise ValueError('scientific bytes changed')
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('xb') as f:f.write(b)
    total+=1
  zpath.unlink()
 for name in ('postrun_audit.py','postrun_analysis_audit.py'):
  source=HERE/'supplement'/name;shutil.copyfile(source,destination/name)
 shutil.copyfile(HERE/'PUBLIC_ARCHIVE_INDEX.json',destination/'PUBLIC_ARCHIVE_INDEX.json')
 print(json.dumps({'status':'PASS','public_archives':len(index['captures']),'members_restored':total,'numeric_members_unchanged':True}))
 return destination
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('destination',type=Path);a=p.parse_args();restore(a.destination)
