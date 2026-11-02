#!/usr/bin/env python3
"""Verify exact scientific-review bindings; does not imply manuscript acceptance."""
from pathlib import Path
import json,hashlib,sys
D=Path(__file__).resolve().parent
ROOT=D.parents[1]
b=json.loads((D/'SOURCE_BINDINGS.json').read_text())
fail=[];n=0
for group in ('targets','sources','audit_artifacts'):
 for r in b[group]:
  p=ROOT/r['path']; n+=1
  if not p.exists(): fail.append({'path':r['path'],'reason':'missing'});continue
  data=p.read_bytes();h=hashlib.sha256(data).hexdigest()
  if h!=r['sha256'] or len(data)!=r['bytes']:fail.append({'path':r['path'],'reason':'hash or length mismatch','got':h})
for rel in ('independent_exact_checks.json','sc001_sc002/independent_exact_diagnostics.json'):
 d=json.loads((D/rel).read_text())
 if d.get('status')!='PASS':fail.append({'path':rel,'reason':'not passing'})
print(json.dumps({'status':'PASS' if not fail else 'FAIL','bound_file_comparisons':n,'failures':fail,'scope':'Exact artifact identity and passing diagnostic records only; mathematical verdict is in AUDIT_REPORT.md; not acceptance.'},indent=2))
sys.exit(bool(fail))
