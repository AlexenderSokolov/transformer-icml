#!/usr/bin/env python3
"""Read-only verification for the exact full shared-source training archive."""
import hashlib,json,pathlib,re,sys,types,os,stat
if sys.flags.optimize:raise SystemExit('Optimized Python is unsupported.')
PREFIX='provenance/full_shared_source_training_20261103/'
ROOT=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else pathlib.Path(__file__).absolute().parents[2]).absolute()
def require(ok,msg):
 if not ok:raise ValueError(msg)
def read(relative):
 require(type(relative) is str and relative and not relative.startswith('/') and all(p not in ('','.','..') for p in relative.split('/')),'Unsafe relative path')
 for flag in ('O_NOFOLLOW','O_DIRECTORY','O_NONBLOCK'):require(hasattr(os,flag),'Safe descriptor traversal unavailable')
 root=os.fspath(ROOT);require('..' not in root.split('/'),'Parent traversal refused')
 parts=[p for p in os.path.abspath(root).split('/') if p]+relative.split('/')
 fd=None;ff=None
 try:
  flags=os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW;fd=os.open('/',flags)
  for bit in parts[:-1]:
   nxt=os.open(bit,flags,dir_fd=fd);os.close(fd);fd=nxt
  ff=os.open(parts[-1],os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK,dir_fd=fd);before=os.fstat(ff)
  require(stat.S_ISREG(before.st_mode) and 0<before.st_size<=16*1024*1024,'Not bounded regular file')
  with os.fdopen(ff,'rb') as handle:
   ff=None;data=handle.read(16*1024*1024+1);after=os.fstat(handle.fileno())
  require(len(data)==before.st_size,'Incomplete read')
  require(all(getattr(before,a)==getattr(after,a) for a in ('st_dev','st_ino','st_size','st_mtime_ns','st_ctime_ns')),'Input changed during read')
  return data
 finally:
  if ff is not None:os.close(ff)
  if fd is not None:os.close(fd)
def pairs(items):
 d={}
 for k,v in items:
  if k in d:raise ValueError('Duplicate JSON key')
  d[k]=v
 return d
def parse(b):return json.loads(b,object_pairs_hook=pairs,parse_float=lambda _:(_ for _ in ()).throw(ValueError('Floating JSON forbidden')),parse_constant=lambda _:(_ for _ in ()).throw(ValueError('Nonfinite JSON')))
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_sha1':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
inv=parse(read('provenance/PUBLIC_INVENTORY.json'));rows={x['path']:x for x in inv['files']}
if len(rows)!=len(inv['files']):raise ValueError('Duplicate inventory path')
verified=set()
def check(path,want=None):
 b=read(path);got=ident(b)
 if got!={k:rows[path][k] for k in got}:raise ValueError('Inventory mismatch: '+path)
 if want is not None and got!=want:raise ValueError('Declared identity mismatch: '+path)
 verified.add(path);return b
for path in sorted(rows):
 if path.startswith(PREFIX):check(path)
mp=parse(read(PREFIX+'SOURCE_EXPORT_MAP.json'));recon=parse(read(PREFIX+'PUBLIC_EXPORT_RECONCILIATION.json'));selected={x['path']:x for x in mp['files']}
EXPECTED_SOURCES={'v10_research/full_shared_source_training_20261103_1054/FULL_TRAJECTORY_BASELINE.md': {'bytes': 10820, 'sha256': 'c884985e61780fac45c44f4ccbc3ab04c1ab53beec679b10e02df17e324465a7', 'git_blob_sha1': '30f7a95184bf2c127de6e46381961c4d5e2d51f3'}, 'v10_research/full_shared_source_training_20261103_1054/INDEPENDENT_REVIEW.md': {'bytes': 1449, 'sha256': '34c47344fae7c915b821702bb86d9daa9f7b0064b840b6dec17847cf8700d8a1', 'git_blob_sha1': '6f034b653f71ad8207160d097b8b058325401b66'}, 'v10_research/full_shared_source_training_20261103_1054/REVIEW_CORRECTION.md': {'bytes': 540, 'sha256': '2c98dd13ac1c0c0aef6162434a03cade7a7bbdfe0e0b97e98a2e182f5910e4d1', 'git_blob_sha1': 'd4608df7c993ba213080cf6ec904b65d07b147dd'}}
if set(selected)!=set(EXPECTED_SOURCES) or len(mp['files'])!=3:raise ValueError('Incomplete/duplicate selected sources')
for path,m in selected.items():
 if m['changed'] or m['original']!=m['public'] or m['public']!=EXPECTED_SOURCES[path]:raise ValueError('Unexpected source edit')
 check(path,m['public'])
deps={x['path']:x for x in recon['inherited_dependencies']}
EXPECTED_DEPS={'v10_research/positional_manuscript_consolidated_20261103/main.tex': {'bytes': 33339, 'sha256': '5c4a5a91e08a4ba0eaf40eff7b19010b88f3e6f3d616f80bdfa58ad1756f8fa1', 'git_blob_sha1': '337d30fb8bbb8d410cfdd6574346a4bcdf023ce9'}, 'v10_research/positional_manuscript_consolidated_20261103/sections/proofs_negative.tex': {'bytes': 28723, 'sha256': 'c33000a5e7b98eb395d8ccae7c104b60d4cf7d30900607d64f4102c9bf9302c7', 'git_blob_sha1': 'bb1351ffab5b63dc12dd1a695e174c3b8f08f136'}, 'v10_research/positional_manuscript_consolidated_20261103/sections/proofs_positive.tex': {'bytes': 32814, 'sha256': 'a629caebe01e614a71738f2036bd9016708f35871a15b6902dd98be967f69e88', 'git_blob_sha1': 'a5dea704fdaa9d87b47f8344b0a89ad25c309e91'}, 'v10_research/clean_training_objective_20261103/CANDIDATE.md': {'bytes': 13917, 'sha256': '1405c661827773bba64c8d8ae91f8eb8a9b2bf17ffc6a66e3be69525f1674bb2', 'git_blob_sha1': 'cadbd0c2ff3b9e5f9e74566d8ef43828dbd503b7'}, 'v10_research/positional_gate_training_20261103/CANDIDATE.md': {'bytes': 12550, 'sha256': '91dcb755e6544fa04e728ab92bf48a7cb864e1e28fc9e4cbdbe0fc38257cb0be', 'git_blob_sha1': 'e3f5e0867e619d03af7fa9e72289c718a934a3de'}, 'v10_research/binary_budget_adaptation/AB001_joint_blindness_obstruction.md': {'bytes': 9876, 'sha256': '865b65e296c39c632aa619c1d2588ad8b9d221efd6e8d799c8b15814b40a1e3d', 'git_blob_sha1': '4405bbd9773437aef5d6a421cba98c52444f8cb7'}, 'v10_research/balanced_joint_finite_cut/BCJ001_theorem.md': {'bytes': 19465, 'sha256': '95d5aac1ee2504955e55c1e82241c8a07d219661e2620c6e083acf5c8701554d', 'git_blob_sha1': '8575ab03ac332796cc73a11e41e0620d7b3df8d2'}, 'v10_research/intake/BCJ001_root_acceptance.json': {'bytes': 1122, 'sha256': '27c1aa7efdc86752c63fd0b1f41b9c303a2aedff965ce81721f3abca7c54699f', 'git_blob_sha1': '7912a1931734bd4dd845fd03b9e0458bbd377089'}, 'v10_research/balanced_joint_finite_cut/BCJ001_independent_full_review.md': {'bytes': 13368, 'sha256': '1e74c502da8fcda31603fc7fc2fa1229747521c3774da55aaf21c8a29a14f64b', 'git_blob_sha1': 'afeeed252adabe83e66c850a248e3287baf4f432'}, 'v10_research/shared_source_vs_fresh_prior_20261103_1031/BASELINE_AND_COROLLARY.md': {'bytes': 12930, 'sha256': '165a1d1787efd3504b5a273e956798c906352543472cf4876750677f8642fa2c', 'git_blob_sha1': 'e85aa6b9786baefada71db9da5e0184417c5b3b2'}, 'v10_research/shared_source_vs_fresh_prior_20261103_1031/INDEPENDENT_REVIEW_AND_CORRECTIONS.md': {'bytes': 1528, 'sha256': '6544d64e5e1bfb05ca2a5ef9ed3e9137314b1c8a1fea6dda38a65fa74281ef59', 'git_blob_sha1': 'cc0c2dad0a7188d4afcfda63672402acb056445a'}, 'provenance/source_matched_learning_20261103/SOURCE_EXPORT_MAP.json': {'bytes': 14093, 'sha256': 'adf3749bdbb1a25fa113f568eb5b8d083e2377729069db9b99632aa264112c0a', 'git_blob_sha1': '6b877ba4d531f9bea70839fa5669edb359f881bb'}, 'provenance/source_matched_learning_20261103/PUBLIC_EXPORT_RECONCILIATION.json': {'bytes': 17425, 'sha256': '483339b7f0ec20c373c5e8cd2e70c58455a25cea58c6d26c488a115a94768b96', 'git_blob_sha1': '7d6d924733f9c8677fc8aed44a9dc6ac453d9628'}}
if set(deps)!=set(EXPECTED_DEPS) or len(recon['inherited_dependencies'])!=13:raise ValueError('Incomplete/duplicate inherited closure')
for path,d in deps.items():
 if path in selected or d['original_public_status']!=('BYTE_IDENTICAL' if path.startswith('v10_research/') else 'EXACT_PUBLISHED_METADATA') or d['identity']!=EXPECTED_DEPS[path]:raise ValueError('Invalid inherited classification')
 check(path,d['identity'])
if recon['changes'] or recon['aliases'] or recon['unresolved_scientific_bindings']:raise ValueError('Unexpected changed-source declaration')
# Census all explicit SHA-256 occurrences in the selected prose and checksum manifests.
census=set()
for path in selected:
 if path.endswith(('.md','.sha256')):
  for n,line in enumerate(check(path).decode().splitlines(),1):
   for h in re.findall(r'\b[0-9a-f]{64}\b',line):
    key=(path,n,h)
    if key in census:raise ValueError('Repeated same hash occurrence at one location')
    census.add(key)
seen=set();counts={}
for b in recon['bindings']:
 owner=b['owner'];n=b['line'];h=b['expected_original_sha256'];target=b['public_target'];status=b['status']
 if owner not in selected or type(n) is not int or n<1:raise ValueError('Invalid binding owner/line')
 key=(owner,n,h)
 if key in seen or key not in census:raise ValueError('Duplicate or false binding location')
 seen.add(key);line=check(owner).decode().splitlines()[n-1]
 if h not in re.findall(r'\b[0-9a-f]{64}\b',line):raise ValueError('Missing source hash at location')
 declared=b['declared_path']
 if declared is not None:
  m=re.fullmatch(r'([0-9a-f]{64})\s+\*?(.+)',line)
  if m is None or m.group(1)!=h or m.group(2)!=declared or declared!=target:raise ValueError('Checksum target declaration mismatch')
 if status=='EXACT_SELECTED_SOURCE':
  if target not in selected:raise ValueError('False selected binding class')
 elif status=='EXACT_INHERITED_PUBLIC_SOURCE':
  if target not in deps:raise ValueError('False inherited binding class')
 else:raise ValueError('Unknown binding class')
 if ident(check(target))['sha256']!=h:raise ValueError('Binding target hash mismatch')
 counts[status]=counts.get(status,0)+1
if seen!=census or len(seen)!=1 or counts!={'EXACT_INHERITED_PUBLIC_SOURCE':1} or counts!=recon['counts']:raise ValueError('Incomplete explicit binding census')
for field,n in [('direct_dependency_paths',3),('prior_context_paths',9),('prior_public_resolution_paths',2)]:
 values=recon.get(field)
 if type(values) is not list or len(values)!=n or any(type(x) is not str for x in values) or len(set(values))!=n:raise ValueError('Malformed dependency path declaration: '+field)
# The prior map is checked as an immutable published resolution boundary, not executed.
prior=parse(check('provenance/source_matched_learning_20261103/PUBLIC_EXPORT_RECONCILIATION.json'))
if {x['path']:x['identity'] for x in prior['inherited_dependencies']}!={p:EXPECTED_DEPS[p] for p in recon['prior_context_paths']}:raise ValueError('Earlier public context declaration mismatch')
if set(recon['direct_dependency_paths'])!={'v10_research/positional_manuscript_consolidated_20261103/sections/proofs_negative.tex','v10_research/shared_source_vs_fresh_prior_20261103_1031/BASELINE_AND_COROLLARY.md','v10_research/shared_source_vs_fresh_prior_20261103_1031/INDEPENDENT_REVIEW_AND_CORRECTIONS.md'}:raise ValueError('Wrong direct dependency set')
if set(recon['prior_public_resolution_paths'])!={'provenance/source_matched_learning_20261103/SOURCE_EXPORT_MAP.json','provenance/source_matched_learning_20261103/PUBLIC_EXPORT_RECONCILIATION.json'}:raise ValueError('Wrong earlier resolution set')
print(json.dumps({'status':'PASS','verified_public_files':len(verified),'selected_sources':3,'explicit_bindings':1,'inherited_public_context_files':13,'numeric_diagnostics':0,'scope_limits':['Proof-only stage: no empirical or numerical diagnostic exists or is generated.','Source identity and reference checks do not prove the mathematical claims or establish novelty.','No historical programs, sampling, models, native research executable or network was used.','Earlier public resolution is a bounded dependency boundary; missing project history remains missing.','Trusted pinned inventory and helper are identity roots, not an untrusted-code sandbox or formal proof.']},ensure_ascii=False,indent=2))
