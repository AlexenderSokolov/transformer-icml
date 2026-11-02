#!/usr/bin/env python3
"""Content integrity only; not mathematical/formal verification."""
from pathlib import Path
import argparse,hashlib,io,json,zipfile
ap=argparse.ArgumentParser();ap.add_argument('--source-dir',type=Path);args=ap.parse_args()
ROOT=Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
def get(loc):
 parts=loc.split('!/')
 b=(ROOT/parts[0]).read_bytes()
 for name in parts[1:]:
  with zipfile.ZipFile(io.BytesIO(b)) as z:b=z.read(name)
 return b
def cover(parts,total):
 pos=0
 for a,b in sorted(parts):assert a==pos and b>=a,(pos,a,b);pos=b
 assert pos==total,(pos,total)
manifest={}
for line in (ROOT/'SHA256SUMS.txt').read_text().splitlines():
 h,n=line.split('  ',1);assert n not in manifest;manifest[n]=h;assert sha((ROOT/n).read_bytes())==h,n
actual={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and p.name!='SHA256SUMS.txt'}
assert set(manifest)==actual,'Manifest file inventory mismatch'
m=json.loads((ROOT/'COPY_MAP.json').read_text())
for r in m['records']:
 out=(ROOT/r['output']).read_bytes();assert len(out)==r['output_bytes'] and sha(out)==r['output_sha256']
 ss=[];oo=[]
 for s in r['spans']:
  bb=out[s['output_byte_start']:s['output_byte_end']];assert sha(bb)==s['sha256'];assert len(bb)==s['source_byte_end']-s['source_byte_start']
  ss.append((s['source_byte_start'],s['source_byte_end']));oo.append((s['output_byte_start'],s['output_byte_end']))
 for s in r['omitted_source_spans']:ss.append((s['source_byte_start'],s['source_byte_end']))
 for s in r['editorial_output_spans']:
  assert sha(out[s['output_byte_start']:s['output_byte_end']])==s['sha256'];oo.append((s['output_byte_start'],s['output_byte_end']))
 cover(ss,r['source_bytes']);cover(oo,len(out))
 if args.source_dir:
  src=(args.source_dir/r['source']).read_bytes();assert len(src)==r['source_bytes'] and sha(src)==r['source_sha256']
  for s in r['spans']:assert src[s['source_byte_start']:s['source_byte_end']]==out[s['output_byte_start']:s['output_byte_end']]
  for s in r['omitted_source_spans']:assert sha(src[s['source_byte_start']:s['source_byte_end']])==s['sha256']
for r in m['binary_copies']:
 b=get(r['output']);assert len(b)==r['output_bytes']==r['source_bytes'] and sha(b)==r['output_sha256']==r['source_sha256']
ix=json.loads((ROOT/'SOURCE_INDEX.json').read_text())
for r in ix['sources']:
 b=get(r['locator']);assert len(b)==r['bytes'] and sha(b)==r['sha256'],r['id']
for r in ix['inherited_archive_inventory']:
 b=get(r['locator']);assert len(b)==r['bytes'] and sha(b)==r['sha256']
s15=ix['S015_original_to_public'];assert sha(get(s15['public_locator']))==s15['public_sha256'];assert sha(get(s15['mapping_locator']))==s15['mapping_sha256']
assert len(list((ROOT/'inherited').glob('*.zip')))==1
assert not any('R007' in n for n in actual)
print(json.dumps({'status':'PASS','manifest_files':len(manifest),'scientific_copies':len(m['records']),'indexed_sources':len(ix['sources']),'frozen_source_verification':bool(args.source_dir),'scope':'Integrity only, not a new mathematical review'},ensure_ascii=False,indent=2))
