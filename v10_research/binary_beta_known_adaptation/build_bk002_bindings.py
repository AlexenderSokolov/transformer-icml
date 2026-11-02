#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,datetime
D=Path(__file__).resolve().parent;R=D.parent
receipt_path=R/'intake/BK002_acceptance.json';receipt=json.loads(receipt_path.read_text())
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rec(p,role):return {'path':str(p.relative_to(R)),'sha256':h(p),'bytes':p.stat().st_size,'role':role}
assert h(R/receipt['proof'])==receipt['sha256']
assert h(R/receipt['review'])==receipt['review_sha256']
assert h(D/'revisions/BK002_initial_candidate.md')==receipt['sha256']
assert h(R/'reviews/BK002_audit_snapshots/BK002_reference_sampler_received.md')==receipt['sha256']
assert (R/'reviews/BK002_audit_snapshots/received_to_reviewed.diff').read_bytes()==b''
for p in [D/'BK002_author_diagnostics.json',R/'reviews/BK002_independent_exact_checks.json']:
 assert json.loads(p.read_text())['proof_sha256']==receipt['sha256']
artifacts=[(D/n,'accepted-unit artifact or clarification') for n in ['BK002_full_history_supplied_beta_obstruction.md','BK002_author_diagnostics.json','check_bk002.py','BK002_HANDOFF.md','BK002_FIXED_POSITIVE_BETA_PROVENANCE.md','build_bk002_bindings.py','revisions/BK002_initial_candidate.md']]
artifacts +=[(R/n,'fresh independent review/check/snapshot artifact') for n in ['reviews/BK002_independent_full_review.md','reviews/BK002_independent_exact_checks.py','reviews/BK002_independent_exact_checks.json','reviews/BK002_independent_review_bindings.json','reviews/BK002_audit_snapshots/BK002_reference_sampler_received.md','reviews/BK002_audit_snapshots/received_to_reviewed.diff']]
context=['BK002_exploration_and_optional_simplification_unreviewed.md','same_beta_route_barriers_unreviewed.md','macrocycle_transport_barrier_unreviewed.md']
source_paths={'binary_budget_adaptation/AB003_small_budget_hard_threshold.md':'accepted small-budget/envelope sufficiency',
'binary_source_corruption/SC003_theorem.md':'known-k binary upper and model comparison',
'binary_erasure_transport/BT002_entropy_bridge_lower.md':'known-k binary minimax comparison lower',
'binary_erasure_transport/BT002_scalar_completion.md':'known-k comparison all-regime completion',
'source_symbol_corruption_mixing/SC002_theorem.md':'generic upper only for ancillary fixed-positive-beta remark',
'source_corruption_manuscript/corrupted_trajectories.tex':'comparison experiment and scope'}
for unit in ['AB003','SC003','BT002','SC002']:
 q=R/f'intake/{unit}_acceptance.json';v=json.loads(q.read_text());assert h(R/v['proof'])==v['sha256'];source_paths[f'intake/{unit}_acceptance.json']='exact inherited-source receipt'
out={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'unit':'BK002','status':'ROOT_ACCEPTED_EXACT_BINDINGS_VERIFIED','scope':'Supplied-beta unknown-actual-budget FULL-HISTORY obstruction, uniform in beta; sharp public range-envelope iff O(sqrt M).',
'root_receipt':rec(receipt_path,'root acceptance authority'),'artifacts':[rec(p,role) for p,role in artifacts],
'sources':[rec(R/p,role) for p,role in source_paths.items()],
'unreviewed_history_not_dependencies':[rec(D/p,'UNREVIEWED related research; not an accepted premise') for p in context],
'proof_revision_history':'No BK002 proof revision; author and independent received snapshots equal accepted bytes, actual review diff empty.'}
(D/'BK002_ACCEPTED_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','artifacts':len(artifacts),'sources':len(source_paths),'unreviewed_history':len(context)}))
