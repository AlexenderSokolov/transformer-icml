#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,datetime,difflib
D=Path(__file__).resolve().parent;R=D.parent
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rec=lambda p,r:{'path':str(p.relative_to(R)),'sha256':h(p),'bytes':p.stat().st_size,'role':r}
rp=R/'intake/AF001_root_acceptance.json';q=json.loads(rp.read_text());p=R/q['proof']
assert h(p)==q['sha256'];assert h(R/q['review'])==q['review_sha256'];assert h(R/'reviews/AF001_audit_snapshots/AF001_received.md')==q['sha256']
v=json.loads((D/'AF001_revision_record.json').read_text());b=D/v['actual_before']
assert h(b)==v['before_sha256'];assert h(p)==v['after_sha256']
assert ''.join(difflib.unified_diff(b.read_text().splitlines(True),p.read_text().splitlines(True),fromfile=b.name,tofile=p.name))==(D/'AF001_CB005_acceptance_status.diff').read_text()
assert json.loads((D/'AF001_author_diagnostics.json').read_text())['proof_sha256']==q['sha256']
assert q['sha256'] in (R/'reviews/AF001_independent_review_bindings.json').read_text()
a=[D/n for n in ['AF001_full_history_domain_classification.md','AF001_author_diagnostics.json','check_af001.py','AF001_HANDOFF.md','build_af001_bindings.py','AF001_initial_candidate.md','AF001_CB005_acceptance_status.diff','AF001_revision_record.json','diagnostic_history/check_af001_initial_receipt_path.py','diagnostic_history/check_af001_receipt_and_status.diff','diagnostic_history/actual_first_run_failure.txt','preceding_handoffs_integrity_audit.json']]
a +=[R/n for n in ['reviews/AF001_independent_full_review.md','reviews/AF001_independent_exact_checks.py','reviews/AF001_independent_exact_checks.json','reviews/AF001_independent_review_bindings.json','reviews/AF001_audit_snapshots/AF001_received.md']]
cb=(D/'diagnostic_history/check_af001_initial_receipt_path.py').read_text();ca=(D/'check_af001.py').read_text()
assert ''.join(difflib.unified_diff(cb.splitlines(True),ca.splitlines(True),fromfile='initial_author_checker',tofile='final_author_checker'))==(D/'diagnostic_history/check_af001_receipt_and_status.diff').read_text()
s={}
for u in ['KA001','CB004','CB005','BK002','AB001','SC003','BT002','KH002']:
 suf='_root_acceptance.json' if u in ['CB004','CB005'] else '_acceptance.json';z=R/f'intake/{u}{suf}';v=json.loads(z.read_text());assert h(R/v['proof'])==v['sha256'];s[str(z.relative_to(R))]='accepted direct receipt';s[v['proof']]='accepted direct interface'
 if u=='CB005':
  assert h(R/v['review'])==v['review_sha256'];s[v['review']]='fresh full all-start dependency review'
s['binary_erasure_transport/BT002_scalar_completion.md']='accepted benchmark scalar completion'
out={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'unit':'AF001','status':'ROOT_ACCEPTED_EXACT_BINDINGS_VERIFIED','scope':'Exact arbitrary-domain supplied-beta full-history all-budget adaptation criterion, BOTH initialization conventions. Public beta selector, not generally beta-blind union.','root_receipt':rec(rp,'root acceptance authority'),'artifacts':[rec(z,'accepted synthesis/review/check or actual revision artifact') for z in a],'sources':[rec(R/z,r) for z,r in s.items()],'revision_history':'One actual dependency-status-only update after CB005 acceptance; exact original/diff verified. No frozen-review proof revision. Author checker receipt-basename fix preserved separately.'}
(D/'AF001_ACCEPTED_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','artifacts':len(a),'sources':len(s)}))
