#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,datetime,difflib
D=Path(__file__).resolve().parent;R=D.parent
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rec=lambda p,role:{'path':str(p.relative_to(R)),'sha256':h(p),'bytes':p.stat().st_size,'role':role}
rp=R/'intake/KH002_acceptance.json';q=json.loads(rp.read_text());p=R/q['proof']
assert h(p)==q['sha256'];assert h(R/q['review'])==q['review_sha256']
for name in ['revisions/KH002_initial_candidate.md']:
 assert h(D/name)==q['sha256']
assert h(R/'reviews/KH002_audit_snapshots/KH002_received.md')==q['sha256']
assert json.loads((D/'KH002_author_diagnostics.json').read_text())['proof_sha256']==q['sha256']
v=json.loads((R/'reviews/KH002_independent_exact_checks.json').read_text())
# The reviewer manifest separately records the reviewed candidate version.
assert q['sha256'] in (R/'reviews/KH002_independent_review_bindings.json').read_text()
a=[D/n for n in ['KH002_histogram_domain_classification.md','KH002_author_diagnostics.json','check_kh002.py','KH002_HANDOFF.md','build_kh002_bindings.py','revisions/KH002_initial_candidate.md','revisions/check_kh002_before_receipt_schema_guard.py','revisions/check_kh002_receipt_schema_guard.diff','revisions/check_kh002_failed_first_run.txt']]
a +=[R/n for n in ['reviews/KH002_independent_full_review.md','reviews/KH002_independent_exact_checks.py','reviews/KH002_independent_exact_checks.json','reviews/KH002_independent_review_bindings.json','reviews/KH002_audit_snapshots/KH002_received.md']]
b=(D/'revisions/check_kh002_before_receipt_schema_guard.py').read_text();z=(D/'check_kh002.py').read_text()
assert ''.join(difflib.unified_diff(b.splitlines(True),z.splitlines(True),fromfile='before',tofile='after'))==(D/'revisions/check_kh002_receipt_schema_guard.diff').read_text()
s={}
for unit in ['KH001','KA001','SC003','BT002']:
 z=R/f'intake/{unit}_acceptance.json';u=json.loads(z.read_text());assert h(R/u['proof'])==u['sha256'];s[str(z.relative_to(R))]='exact accepted receipt';s[u['proof']]='accepted dependency'
s['binary_erasure_transport/BT002_scalar_completion.md']='accepted comparison scalar completion'
out={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'unit':'KH002','status':'ROOT_ACCEPTED_EXACT_BINDINGS_VERIFIED','scope':'Exact arbitrary-domain criterion ONLY for triple histogram plus initial/final pairs.','root_receipt':rec(rp,'root acceptance authority'),'artifacts':[rec(z,'accepted proof/review/check/snapshot or actual diagnostic-revision artifact') for z in a],'sources':[rec(R/z,r) for z,r in s.items()],'proof_revision_history':'None; actual original and independent snapshots equal accepted bytes. Only author checker optional-receipt-field guard changed after documented first-run KeyError.'}
(D/'KH002_ACCEPTED_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','artifacts':len(a),'sources':len(s)}))
