#!/usr/bin/env python3
"""Bind read-only mathematical dependencies and verify accepted source receipts."""
from pathlib import Path
import hashlib,json,datetime
D=Path(__file__).resolve().parent;ROOT=D.parent
units=['MG001','MG002','GD001','GN001','JP001','SC002','SC003','BT002']
extra=['robust_markov_prediction/MG_final_clip_clarification.md','robust_markov_prediction/MG_final_clip_clarification_independent_review.md','robust_markov_prediction/MG_final_clip_clarification_review_binding.json','source_corruption_manuscript/README.md','source_corruption_manuscript/corrupted_trajectories.tex','source_corruption_manuscript/nonbinary_endpoint.tex','source_corruption_manuscript/binary.tex','delivery_stage8/SCIENTIFIC_FREEZE.json']
files=set(extra);checks=[]
for unit in units:
 path=ROOT/'intake'/f'{unit}_acceptance.json';r=json.loads(path.read_text());files.add(str(path.relative_to(ROOT)))
 targets={r['proof']:r['sha256']};targets.update(r.get('component_proofs',{}))
 for proof,expected in targets.items():
  actual=hashlib.sha256((ROOT/proof).read_bytes()).hexdigest();assert actual==expected,(unit,proof,expected,actual)
  checks.append(dict(unit=unit,proof=proof,expected=expected,actual=actual,match=True));files.add(proof)
 for review in [r.get('review')]+r.get('reviews',[]):
  if review:files.add(review)
 if r.get('review_sha256'):
  assert hashlib.sha256((ROOT/r['review']).read_bytes()).hexdigest()==r['review_sha256']
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','scope':'Exact direct dependency proof/receipt bindings; this does not extend receipt acceptance to RE001.','receipt_source_checks':checks,'files':{s:hashlib.sha256((ROOT/s).read_bytes()).hexdigest() for s in sorted(files)}}
(D/'RE001_source_bindings.json').write_text(json.dumps(out,indent=2)+'\n')
(D/'RE001_dependency_receipt_check.json').write_text(json.dumps({'status':'PASS','checks':checks},indent=2)+'\n')
print(json.dumps({'status':'PASS','files_bound':len(files),'accepted_proof_checks':len(checks)},indent=2))
