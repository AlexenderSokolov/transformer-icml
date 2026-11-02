#!/usr/bin/env python3
"""Rebuild exact local source/artifact inventory; does not create acceptance receipts."""
from pathlib import Path
import hashlib,json,datetime
HERE=Path(__file__).resolve().parent
RESEARCH=HERE.parent
WORK=RESEARCH.parent
sources={
 'source_corruption_manuscript/corrupted_trajectories.tex':'comparison model and full known-k minimax synthesis',
 'source_corruption_manuscript/binary.tex':'binary known-k upper/lower manuscript',
 'source_corruption_manuscript/nonbinary_endpoint.tex':'generic count stability/occupation and beta=1 pooling interfaces',
 'binary_source_corruption/SC003_theorem.md':'direct inherited clean empirical, terminal occupation, and weighted occupation interfaces',
 'binary_source_corruption/SC003_independent_full_review.md':'accepted direct-interface review',
 'binary_source_corruption/SC003_source_bindings.json':'transitive R011 and occupation provenance',
 'binary_erasure_transport/BT002_entropy_bridge_lower.md':'known-k binary minimax lower comparison',
 'binary_erasure_transport/BT002_scalar_completion.md':'known-k binary lower all-regime completion',
 'binary_erasure_transport/BT002_independent_review.md':'known-k lower review',
 'binary_all_start/BIF001_binary_all_initializations_frontier_v1.md':'full-support arbitrary-start weighted occupation for A>0',
 'binary_all_start/BIF001_independent_review_v1.md':'weighted occupation source review',
 'binary_arbitrary/BAI003_uniform_absorbing_binary_upper_v2.md':'arbitrary-start singleton-support weighted occupation',
 'binary_arbitrary/BAI003_review_v2.md':'singleton-support source delta review',
}
for unit in ['SC003','BT002','BIF001','BAI003']:
 sources[f'intake/{unit}_acceptance.json']='exact inherited-source acceptance receipt'
def record(path,role):
 data=path.read_bytes()
 return {'path':str(path.relative_to(WORK)),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'role':role}
src=[record(RESEARCH/p,r) for p,r in sources.items()]
r011=WORK/'v10_intake/source/sources/dot-return/readable/proofs/R011_global_rates_and_constant_adaptation_v1.md'
if r011.exists(): src.append(record(r011,'transitive original clean add-one source; invoked through accepted SC003 interface'))
art=[]
for path in sorted(HERE.rglob('*')):
 if not path.is_file() or path.name in ['AB_SOURCE_BINDINGS.json'] or '__pycache__' in path.parts:continue
 role='new research artifact'
 if 'draft_history' in path.parts:role='preserved pre-renaming draft/history; not authoritative unit ID'
 if path.name.startswith('review_'):role='fresh independent LLM review or independent finite diagnostic'
 art.append(record(path,role))
receipts=[]
for unit in ['AB001','AB002','AB003']:
 p=RESEARCH/f'intake/{unit}_acceptance.json'
 if p.exists():
  data=json.loads(p.read_text()); proof=RESEARCH/data['proof']
  assert hashlib.sha256(proof.read_bytes()).hexdigest()==data['sha256']
  if 'review_sha256' in data:assert hashlib.sha256((RESEARCH/data['review']).read_bytes()).hexdigest()==data['review_sha256']
  receipts.append(record(p,'root-created exact-version acceptance receipt'))
for path in [HERE/'AB001_author_diagnostics.json',HERE/'review_joint_blindness_checks.json']:
 data=json.loads(path.read_text()); hashes=data.get('proof_hashes',data.get('source_sha256',{}))
 for name,h in hashes.items():assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==h
for path in [HERE/'AB003_author_diagnostics.json',HERE/'review_ab003_checks.json']:
 if path.exists():
  data=json.loads(path.read_text()); h=data.get('proof_sha256')
  if h:assert hashlib.sha256((HERE/'AB003_small_budget_hard_threshold.md').read_bytes()).hexdigest()==h
  for name,h in data.get('source_sha256',{}).items():
   assert hashlib.sha256((RESEARCH/name).read_bytes()).hexdigest()==h
out={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Binary full-history protected-endpoint budget adaptation; no external novelty/formal verification claim.',
 'acceptance_authority':'Only separate root-created intake receipts establish acceptance; candidate headers preserved.',
 'sources':src,'artifacts':art,'root_receipts':receipts,
 'id_history':'Initial BA001/BA002 author drafts collided with historical bounded-attention BA001; AB001/AB002 are authoritative. ID-only delta independently reviewed; exact originals preserved under draft_history.'}
(HERE/'AB_SOURCE_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','sources':len(src),'artifacts':len(art),'root_receipts':len(receipts)},indent=2))
