#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,datetime,difflib
D=Path(__file__).resolve().parent;R=D.parent
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rec=lambda p,r:{'path':str(p.relative_to(R)),'sha256':h(p),'bytes':p.stat().st_size,'role':r}
rp=R/'intake/KH003_root_acceptance.json';q=json.loads(rp.read_text());p=R/q['proof']
assert h(p)==q['sha256'];assert h(R/q['review'])==q['review_sha256'];assert h(R/'reviews/KH003_audit_snapshots/KH003_received.md')==q['sha256']
v=json.loads((D/'revisions/KH003_constant_window_revision_record.json').read_text());b=D/v['actual_before_snapshot'];assert h(b)==v['before_sha256'];assert h(p)==v['after_sha256']
assert ''.join(difflib.unified_diff(b.read_text().splitlines(True),p.read_text().splitlines(True),fromfile=b.name,tofile=p.name))==(D/'revisions/KH003_constant_window_clarification.diff').read_text()
assert json.loads((D/'KH003_author_diagnostics.json').read_text())['proof_sha256']==q['sha256'];assert json.loads((R/'reviews/KH003_independent_exact_checks.json').read_text())['candidate_sha256']==q['sha256']
a=[D/n for n in ['KH003_boundary_window_obstruction.md','KH003_author_diagnostics.json','check_kh003.py','KH003_HANDOFF.md','build_kh003_bindings.py','revisions/KH003_initial_candidate.md','revisions/KH003_constant_window_clarification.diff','revisions/KH003_constant_window_revision_record.json']]
a +=[R/n for n in ['reviews/KH003_independent_full_review.md','reviews/KH003_independent_exact_checks.py','reviews/KH003_independent_exact_checks.json','reviews/KH003_independent_review_bindings.json','reviews/KH003_inherited_bindings_audit.json']]
a +=list(sorted((R/'reviews/KH003_audit_snapshots').iterdir()))
s={}
for u in ['KH001','KH002','BK001','KA001','SC003','BT002']:
 z=R/f'intake/{u}_acceptance.json';v=json.loads(z.read_text());assert h(R/v['proof'])==v['sha256'];s[str(z.relative_to(R))]='accepted receipt';s[v['proof']]='accepted inherited source'
s['binary_erasure_transport/BT002_scalar_completion.md']='accepted comparison scalar completion'
out={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'unit':'KH003','status':'ROOT_ACCEPTED_EXACT_BINDINGS_VERIFIED','scope':'Exact triples plus first/last-r windows; critical r=o(M^(1/6)); bounded-width domain criterion. Not a sharp width threshold or full-history result.','root_receipt':rec(rp,'root acceptance authority'),'artifacts':[rec(z,'accepted proof/review/diagnostic or actual revision artifact') for z in a],'sources':[rec(R/z,r) for z,r in s.items()],'unreviewed_history_not_dependency':rec(D/'KH003_boundary_window_exploration_unreviewed.md','actual exploration; not accepted premise'),'review_independence':'Fresh independent mathematical/code review; reviewer inspected author diagnostics first, so not a blind diagnostic audit.'}
(D/'KH003_ACCEPTED_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','artifacts':len(a),'sources':len(s)}))
