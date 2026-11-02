#!/usr/bin/env python3
"""Read-only public integrity check. Not mathematical verification."""
from pathlib import Path
import hashlib, io, json, zipfile
ROOT=Path(__file__).resolve().parent

def sha(b):return hashlib.sha256(b).hexdigest()
def check_partition(spans,n,start,end):
 p=0
 for s in sorted(spans,key=lambda x:x[start]):
  assert s[start]==p and s[end]>=p,(p,s)
  p=s[end]
 assert p==n,(p,n)
def resolve(loc):
 parts=loc.split('!/')
 b=(ROOT/parts[0]).read_bytes()
 for member in parts[1:]:
  with zipfile.ZipFile(io.BytesIO(b)) as z:b=z.read(member)
 return b

def main():
 manifest=ROOT/'SHA256SUMS.txt'
 count=0
 for line in manifest.read_text().splitlines():
  h,p=line.split('  ',1);assert sha((ROOT/p).read_bytes())==h,p;count+=1
 listed={x.split('  ',1)[1] for x in manifest.read_text().splitlines()}
 actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and p.name!='SHA256SUMS.txt'}
 assert listed==actual,(listed^actual)
 cm=json.loads((ROOT/'COPY_MAP.json').read_text())
 copied=omitted=editorial=0
 for rec in cm['records']:
  b=(ROOT/rec['output']).read_bytes();assert len(b)==rec['output_bytes'] and sha(b)==rec['output_sha256']
  for s in rec['spans']:
   out=b[s['output_byte_start']:s['output_byte_end']]
   assert sha(out)==s['sha256']
   assert len(out)==s['source_byte_end']-s['source_byte_start']
  for s in rec['editorial_output_spans']:assert sha(b[s['output_byte_start']:s['output_byte_end']])==s['sha256']
  check_partition(rec['spans']+rec['omitted_source_spans'],rec['source_bytes'],'source_byte_start','source_byte_end')
  check_partition(rec['spans']+rec['editorial_output_spans'],rec['output_bytes'],'output_byte_start','output_byte_end')
  copied+=len(rec['spans']);omitted+=len(rec['omitted_source_spans']);editorial+=len(rec['editorial_output_spans'])
 for rec in cm['binary_copies']:
  b=(ROOT/rec['output']).read_bytes();assert sha(b)==rec['source_sha256']==rec['output_sha256']
  assert len(b)==rec['source_bytes']==rec['output_bytes']
 ix=json.loads((ROOT/'SOURCE_INDEX.json').read_text())
 for rec in ix['sources']:
  b=resolve(rec['locator']);assert len(b)==rec['bytes'] and sha(b)==rec['sha256'],rec['id']
 s=ix['S015_original_to_public'];b=resolve(s['public_locator']);m=resolve(s['mapping_locator'])
 assert sha(b)==s['public_sha256'] and len(b)==s['public_bytes'] and sha(m)==s['mapping_sha256']
 rec=next(r for r in json.loads(m)['records'] if r['source_sha256']==s['original_sha256'])
 assert rec['output_sha256']==s['public_sha256'] and rec['source_bytes']==s['original_bytes']
 for sp in rec['spans']+rec['editorial_output_spans']:assert sha(b[sp['output_byte_start']:sp['output_byte_end']])==sp['sha256']
 recursive_files=recursive_manifests=0
 def walk(data):
  nonlocal recursive_files,recursive_manifests
  with zipfile.ZipFile(io.BytesIO(data)) as z:
   names=set(z.namelist())
   for n in names:
    if n.endswith('/'):continue
    recursive_files+=1;bb=z.read(n)
    if n.endswith('/SHA256SUMS.txt'):
     parent=n.rsplit('/',1)[0]+'/';recursive_manifests+=1
     for line in bb.decode().splitlines():
      if not line.strip():continue
      h,p=line.split('  ',1);assert sha(z.read(parent+p.lstrip('./')))==h,(n,p)
    if n.endswith('.zip'):walk(bb)
 walk((ROOT/'inherited/DOT_conditions_adaptation_closure_20261029_v2.zip').read_bytes())
 print(json.dumps(dict(status='PASS integrity only, not mathematical verification',manifest_files=count,scientific_copies=len(cm['records']),copied_spans=copied,omitted_spans=omitted,editorial_spans=editorial,source_entries=len(ix['sources']),recursive_inherited_files=recursive_files,recursive_inherited_manifests=recursive_manifests,S015_distinct_identities='PASS',source_original_omissions='Require separately retained original inputs; not represented as verified by this public-only run'),ensure_ascii=False,indent=2))
if __name__=='__main__':main()
