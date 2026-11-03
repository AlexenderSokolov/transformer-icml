#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,datetime
D=Path(__file__).resolve().parent;R=D.parent
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rec=lambda p,r:{'path':str(p.relative_to(R)),'sha256':h(p),'bytes':p.stat().st_size,'role':r}
rp=R/'intake/KH004_root_acceptance.json';q=json.loads(rp.read_text());p=R/q['proof']
assert h(p)==q['sha256'];assert h(R/q['review'])==q['review_sha256']
assert h(D/'revisions/KH004_initial_candidate.md')==q['sha256'];assert h(R/'reviews/KH004_audit_snapshots/KH004_received.md')==q['sha256']
assert (R/'reviews/KH004_audit_snapshots/received_to_reviewed.diff').read_bytes()==b''
assert json.loads((D/'KH004_author_diagnostics.json').read_text())['proof_sha256']==q['sha256']
assert q['sha256'] in (R/'reviews/KH004_independent_review_bindings.json').read_text()
a=[D/n for n in ['KH004_constant_crossing_window_obstruction.md','KH004_author_diagnostics.json','check_kh004.py','KH004_HANDOFF.md','build_kh004_bindings.py','revisions/KH004_initial_candidate.md']]
a +=[R/n for n in ['reviews/KH004_independent_full_review.md','reviews/KH004_independent_exact_checks.py','reviews/KH004_independent_exact_checks.json','reviews/KH004_independent_review_bindings.json','reviews/KH004_audit_snapshots/KH004_received.md','reviews/KH004_audit_snapshots/received_to_reviewed.diff']]
s={}
for u in ['KH001','KH002','KH003','BK001','SC003','BT002']:
 suf='_root_acceptance.json' if u=='KH003' else '_acceptance.json';z=R/f'intake/{u}{suf}';v=json.loads(z.read_text());assert h(R/v['proof'])==v['sha256'];s[str(z.relative_to(R))]='accepted receipt';s[v['proof']]='accepted inherited interface or unchanged baseline'
s['binary_erasure_transport/BT002_scalar_completion.md']='accepted comparison scalar completion'
out={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'unit':'KH004','status':'ROOT_ACCEPTED_EXACT_BINDINGS_VERIFIED','scope':'Exact triples plus genuine boundary windows; critical r=o(M^(1/3)); not sharp/full-history/local-encoder classification.','root_receipt':rec(rp,'root acceptance authority'),'artifacts':[rec(z,'accepted proof/review/check/snapshot') for z in a],'sources':[rec(R/z,r) for z,r in s.items()],'unreviewed_history_not_dependencies':[rec(D/n,'actual exploratory history; not accepted premise') for n in ['KH004_constant_crossing_exploration_unreviewed.md','NEXT_conditioned_occupation_route_unreviewed.md']],'revision_history':'No proof revision; both actual original and reviewer snapshots match accepted bytes, actual review diff empty.'}
(D/'KH004_ACCEPTED_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','artifacts':len(a),'sources':len(s),'unreviewed_history':2}))
