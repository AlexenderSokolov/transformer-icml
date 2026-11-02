#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,datetime
D=Path(__file__).resolve().parent;R=D.parent
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rec=lambda p,role:{'path':str(p.relative_to(R)),'sha256':h(p),'bytes':p.stat().st_size,'role':role}
rp=R/'intake/KA001_acceptance.json';v=json.loads(rp.read_text())
assert h(R/v['proof'])==v['sha256'];assert h(R/v['review'])==v['review_sha256']
assert h(D/'revisions/KA001_initial_candidate.md')==v['sha256']
assert h(R/'reviews/KA001_audit_snapshots/KA001_received.md')==v['sha256']
assert (R/'reviews/KA001_audit_snapshots/received_to_reviewed.diff').read_bytes()==b''
assert json.loads((D/'KA001_author_diagnostics.json').read_text())['proof_sha256']==v['sha256']
assert json.loads((R/'reviews/KA001_independent_exact_checks.json').read_text())['reviewed_candidate_sha256']==v['sha256']
a=[D/n for n in ['KA001_certificate_phase_partial.md','KA001_author_diagnostics.json','check_ka001.py','KA001_HANDOFF.md','build_ka001_bindings.py','revisions/KA001_initial_candidate.md']]
a += [R/n for n in ['reviews/KA001_independent_full_review.md','reviews/KA001_independent_exact_checks.py','reviews/KA001_independent_exact_checks.json','reviews/KA001_independent_review_bindings.json','reviews/KA001_audit_snapshots/KA001_received.md','reviews/KA001_audit_snapshots/received_to_reviewed.diff']]
s={}
for u in ['BK002','AB003','SC003','BT002','SC002','IU001','AU001']:
 p=R/f'intake/{u}_acceptance.json';q=json.loads(p.read_text());assert h(R/q['proof'])==q['sha256'];s[str(p.relative_to(R))]='inherited acceptance';s[q['proof']]='accepted inherited proof'
s['binary_erasure_transport/BT002_scalar_completion.md']='accepted lower scalar completion'
s['binary_beta_known_adaptation/BK002_FIXED_POSITIVE_BETA_PROVENANCE.md']='generic-upper citation clarification'
out={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'unit':'KA001','status':'ROOT_ACCEPTED_EXACT_BINDINGS_VERIFIED','scope':'Partial full-history certificate-dependent adaptation: weak and strong positive, strictly intermediate curve negative; critical gap unresolved.','root_receipt':rec(rp,'root acceptance authority'),'artifacts':[rec(p,'accepted unit/review/diagnostic/snapshot') for p in a],'sources':[rec(R/p,role) for p,role in s.items()],'revision_history':'No KA001 proof revision; original author and fresh reviewer snapshots match accepted bytes; actual review diff empty.'}
(D/'KA001_ACCEPTED_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','artifacts':len(a),'sources':len(s)}))
