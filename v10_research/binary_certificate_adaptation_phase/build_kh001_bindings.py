#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,datetime,difflib
D=Path(__file__).resolve().parent;R=D.parent
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rec=lambda p,role:{'path':str(p.relative_to(R)),'sha256':h(p),'bytes':p.stat().st_size,'role':role}
rp=R/'intake/KH001_acceptance.json';q=json.loads(rp.read_text());p=R/q['proof']
assert h(p)==q['sha256'];assert h(R/q['review'])==q['review_sha256']
assert h(R/'reviews/KH001_audit_snapshots/KH001_received.md')==q['sha256']
assert (R/'reviews/KH001_audit_snapshots/received_to_reviewed.diff').read_bytes()==b''
v=json.loads((D/'revisions/KH001_pre_freeze_revision_record.json').read_text());b=D/'revisions/KH001_pre_freeze_editorial.md'
assert h(b)==v['before_sha256'];assert h(p)==v['after_sha256']
actual=''.join(difflib.unified_diff(b.read_text().splitlines(True),p.read_text().splitlines(True),fromfile=b.name,tofile=p.name))
assert actual==(D/'revisions/KH001_pre_freeze_editorial.diff').read_text()
assert json.loads((D/'KH001_author_diagnostics.json').read_text())['proof_sha256']==q['sha256']
assert json.loads((R/'reviews/KH001_independent_exact_checks.json').read_text())['candidate_sha256']==q['sha256']
a=[D/n for n in ['KH001_histogram_strong_side_obstruction.md','KH001_author_diagnostics.json','check_kh001.py','KH001_HANDOFF.md','build_kh001_bindings.py','revisions/KH001_pre_freeze_editorial.md','revisions/KH001_pre_freeze_editorial.diff','revisions/KH001_pre_freeze_revision_record.json']]
a +=[R/n for n in ['reviews/KH001_independent_full_review.md','reviews/KH001_independent_exact_checks.py','reviews/KH001_independent_exact_checks.json','reviews/KH001_independent_review_bindings.json','reviews/KH001_audit_snapshots/KH001_received.md','reviews/KH001_audit_snapshots/received_to_reviewed.diff']]
s={}
for unit in ['BK001','KA001','SC003','BT002']:
 z=R/f'intake/{unit}_acceptance.json';v=json.loads(z.read_text());assert h(R/v['proof'])==v['sha256'];s[str(z.relative_to(R))]='accepted dependency receipt';s[v['proof']]='accepted source'
s['binary_erasure_transport/BT002_scalar_completion.md']='accepted comparison scalar completion'
out={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'unit':'KH001','status':'ROOT_ACCEPTED_EXACT_BINDINGS_VERIFIED','scope':'Histogram+initial/final PAIRS only; stronger-side prescribed curves and combined power-law classification, not full history.','root_receipt':rec(rp,'root acceptance authority'),'artifacts':[rec(x,'accepted unit/review/check/actual revision artifact') for x in a],'sources':[rec(R/x,r) for x,r in s.items()],'unreviewed_history_not_dependency':rec(D/'KH001_RESEARCH_HISTORY.md','retrospective actual research history; not proof premise'),'revision_history':'One actual pre-freeze editorial revision; exact before copy and true diff verified. No revision during frozen review.'}
(D/'KH001_ACCEPTED_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','artifacts':len(a),'sources':len(s)}))
