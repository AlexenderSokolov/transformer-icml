#!/usr/bin/env python3
"""Offline package-only integrity, predecessor binding, source restoration and freeze checks."""
from pathlib import Path
import argparse,hashlib,json,zipfile,io,datetime,functools
P=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def safe(q):
 p=Path(q);assert not p.is_absolute() and '..' not in p.parts and '\\' not in q,q
@functools.lru_cache(None)
def cached_get(chain):
 for q in chain:safe(q)
 if len(chain)==1:return (P/chain[0]).read_bytes()
 b=cached_get(chain[:-1])
 with zipfile.ZipFile(io.BytesIO(b)) as z:
  names=z.namelist();assert len(set(names))==len(names)
  for n in names:
   safe(n);assert (z.getinfo(n).external_attr>>16)&0o170000!=0o120000,n
  return z.read(chain[-1])
def get(chain):return cached_get(tuple(chain))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--restore',type=Path);a=ap.parse_args()
 m=json.loads((P/'SOURCE_MANIFEST.json').read_text())
 if a.restore:assert not a.restore.exists() or not any(a.restore.iterdir()),'Restore target must be empty'
 for q in P.rglob('*'):assert not q.is_symlink(),q
 expected={r['path'] for r in m['files']}|{'SOURCE_MANIFEST.json','SHA256SUMS.txt'}
 assert expected=={str(p.relative_to(P)) for p in P.rglob('*') if p.is_file()}
 for r in m['files']:
  safe(r['path'])
  b=(P/r['path']).read_bytes();assert sha(b)==r['sha256'] and len(b)==r['bytes'],r['path']
 checksummed=set()
 for line in (P/'SHA256SUMS.txt').read_text().splitlines():
  h,q=line.split('  ',1);assert q not in checksummed;checksummed.add(q);assert sha((P/q).read_bytes())==h,q
 assert checksummed==expected-{'SHA256SUMS.txt'}
 rows=json.loads((P/'SOURCE_RESTORATION_MAP.json').read_text())['files']; by={r['source_path']:r for r in rows};assert len(by)==len(rows)
 for path,h in json.loads((P/'SCIENCE_FREEZE_INPUTS.json').read_text())['files'].items():assert by[path]['source_sha256']==h
 for r in rows:
  safe(r['source_path'])
  if r['source_sha256']==r['export_sha256']:assert r['source_bytes']==r['export_bytes']
  b=get(r['package_chain']);assert sha(b)==r['export_sha256'],r['source_path']
  assert len(b)==r['export_bytes'],r['source_path']
  if r['source_sha256']!=r['export_sha256']:
   assert r['edits'] and not r['source_path'].endswith('.py')
   lines=b.decode().splitlines(keepends=True)
   for edit in r['edits']:
    assert sha(lines[edit['line']-1].encode())==edit.get('export_line_sha256',sha(edit['export_line'].encode()))
    assert lines[edit['line']-1]==edit['export_line']
    assert 0<=edit['source_byte_start']<edit['source_byte_end']<=r['source_bytes']
  if a.restore:
   rel=Path(r['source_path']);assert not rel.is_absolute() and '..' not in rel.parts
   q=a.restore/rel;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(b)
 freeze=json.loads((P/'SCIENTIFIC_FREEZE.json').read_text());assert freeze['scientific_freeze_utc']=='2026-11-02T09:22:25.495805+00:00'
 for path,h in freeze['receipts'].items():assert by[path]['source_sha256']==h
 deps=json.loads((P/'DEPENDENCY_SOURCE_MAP.json').read_text())['structured_hash_references']
 for d in deps:assert by[d['source_path']]['source_sha256']==d['sha256'],d
 for u in ['SC001','SC002','SC003','BT001','BT002','EP001']:
  ac=json.loads(get(by['v10_research/intake/'+u+'_acceptance.json']['package_chain']))
  assert ac['sha256']==by['v10_research/'+ac['proof']]['source_sha256']
  if ac.get('review_sha256'):assert ac['review_sha256']==by['v10_research/'+ac['review']]['source_sha256']
  for path,h in ac.get('component_proofs',{}).items():assert by['v10_research/'+path]['source_sha256']==h
  assert datetime.datetime.fromisoformat(ac['time_utc'])<=datetime.datetime.fromisoformat('2026-11-02T09:22:25.495805+00:00')
  assert ac['status']==('ROOT_ACCEPTED_SCOPED_OBSTRUCTION_AND_CONDITIONAL_REDUCTION' if u=='BT001' else 'ROOT_ACCEPTED_AFTER_INDEPENDENT_LLM_REVIEW')
 pred=P/'inherited/DOT_v10_precision_stage7_20261102.zip';assert sha(pred.read_bytes())=='99c206d50896496af74758a0560b50e4e7d2ee5f9334d1187dcb5dbce8ff9308' and pred.stat().st_size==16200656
 with zipfile.ZipFile(pred) as z:assert z.testzip() is None
 print(json.dumps({'status':'PASS','payload_files':len(m['files']),'restored_paths':len(rows),'structured_bindings':len(deps),'new_accepted_units':['SC001','SC002','SC003','BT001','BT002','EP001'],'scientific_freeze_utc':'2026-11-02T09:22:25.495805+00:00','restore':str(a.restore) if a.restore else None}))
if __name__=='__main__':main()
