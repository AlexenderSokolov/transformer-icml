from pathlib import Path
import hashlib,json,datetime
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
def item(p,role):
 b=p.read_bytes(); return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'role':role}
files={}
def add(p,role):
 p=ROOT/p
 if not p.is_file(): raise FileNotFoundError(p)
 files[str(p)]=item(p,role)
freeze=ROOT/'v10_research/delivery_stage8/SCIENTIFIC_FREEZE.json'
f=json.loads(freeze.read_text())
add(freeze.relative_to(ROOT),'Scientific freeze')
for name,h in f['receipts'].items():
 p=ROOT/name
 assert hashlib.sha256(p.read_bytes()).hexdigest()==h
 add(name,'Frozen acceptance receipt')
 receipt=json.loads(p.read_text())
 proofs=receipt.get('component_proofs',{receipt['proof']:receipt['sha256']})
 for path,sha in proofs.items():
  p=ROOT/'v10_research'/path
  assert hashlib.sha256(p.read_bytes()).hexdigest()==sha
  add(p.relative_to(ROOT),'Adopted proof; exact accepted bytes')
 add(Path('v10_research')/receipt['review'],'Independent LLM review; not formal verification')
for directory in ['source_symbol_corruption','source_symbol_corruption_mixing','binary_source_corruption','binary_erasure_transport','terminal_symbol_corruption']:
 for p in (ROOT/'v10_research'/directory).glob('*'):
  if p.is_file() and (p.name.endswith('.json') or 'review' in p.name or 'bindings' in p.name):
   if str(p) not in files:add(p.relative_to(ROOT),'Diagnostic/provenance companion; not a new theorem')
imports=['v10_intake/source/sources/dot-return/readable/proofs/R011_global_rates_and_constant_adaptation_v1.md','v10_research/intermediate_upper/IU001_beta_sensitive_precision_upper_v1.md','v10_research/arbitrary_frontier/AU001_residual_suffix_precision_upper_v1.md','v10_research/binary_all_start/BIF001_binary_all_initializations_frontier_v1.md','v10_research/binary_arbitrary/BAI003_uniform_absorbing_binary_upper_v2.md']
for path in imports:add(path,'Inherited clean/occupation interface; full proof retained in predecessor dossier')
for unit in ['IU001','AU001','BIF001','BAI003']:
 add(f'v10_research/intake/{unit}_acceptance.json','Inherited interface acceptance')
for path in ['v10_research/reviews/IU001_review_v1.md','v10_research/reviews/AU001_review_v1.md','v10_research/binary_all_start/BIF001_independent_review_v1.md','v10_research/binary_arbitrary/BAI003_review_v2.md','v10_research/prior_art/source_corruption_screen.md','v10_intake/source/DOT_START_PROMPT.txt','v10_intake/source/START_HERE.md','v10_research/manuscript_v5/SOURCE_MANIFEST.json']:
 add(path,'Inherited review, mandate, literature scope or predecessor dossier map')
# Retain the exact recursive dependency binding documents without representing their
# historical source reading/review as a new transitive proof audit.
for path in ['v10_research/binary_source_corruption/SC003_independent_full_review_bindings.json','v10_research/source_symbol_corruption_mixing/SC002_source_bindings.json','v10_research/binary_all_start/BIF001_source_bindings_v1.json','v10_research/binary_arbitrary/BAI003_source_bindings_v2.json']:
 add(path,'Version-specific predecessor chain map')
for path in ['cloud_work/conditions-20261028/research/resume_20261030/R011_global_rates_and_constant_adaptation_v1.md','cloud_work/conditions-20261028/research/resume_20261030/R011_root_acceptance.json','v10_intake/source/sources/dot-return/readable/reviews/R011_independent_review_v1.md']:
 add(path,'R011 original acceptance and full review; readable editorial copy distinct')
out={'title':'Next-Symbol Prediction from Adversarially Corrupted Markov Trajectories','scientific_freeze_utc':f['scientific_freeze_utc'],'freeze_sha256':hashlib.sha256(freeze.read_bytes()).hexdigest(),'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'path_base':'Workspace root','scope':'Six stage8 units only. BT001 conditional transport premise remains unproved. New elementary statistical-order tolerance corollary identified separately. No later exploration. Explicit inherited clean/occupation interfaces, not a fully rederived foundational chain.','sources':list(files.values()),'new_derivation':{'location':'corrupted_trajectories.tex, Corollary statistical-order tolerance','status':'Elementary scalar consequence; fresh manuscript audit requested separately'},'primary_source_readscope':{'Ghosh2004.01249v2':'Abstract, introduction, section 2.3 via frozen screen','ZuckermanITCS2026':'Abstract only via frozen screen','BhattICML2022':'Abstract only via frozen screen','HanJanaWu2106.13947v2':'Predecessor bibliography and common-prior/waiting-time context; no new proof claim','OConnorJMLR23_45':'Journal landing page abstract and metadata directly verified 2026-11-02; full paper not read'}}
(BASE/'SOURCE_MANIFEST.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'Bound {len(files)} exact sources; all frozen receipt and proof hashes match.')
