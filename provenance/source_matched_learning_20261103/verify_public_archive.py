#!/usr/bin/env python3
"""Read-only verification for the exact source-matched learning archive."""
import hashlib,json,pathlib,re,sys,types,os,stat
if sys.flags.optimize:raise SystemExit('Optimized Python is unsupported.')
PREFIX='provenance/source_matched_learning_20261103/'
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
EXPECTED_SOURCES={'v10_research/half_gate_iid_identifiability_20261103_1009/CLARIFICATION.md': {'bytes': 1289, 'sha256': '77ecf53733fa59ad18f6a782793e51cbe2233be69927e653e5ddfbf86ce94b71', 'git_blob_sha1': 'bd4a1d207c83f51611f190d7f86eab86344fa8cb'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/DIAGNOSTIC_NOTES.md': {'bytes': 959, 'sha256': 'a01cca6f29a5bb1e4c7eb4315e39f15ba5824c0eaf633fd1ccb873f6845051b5', 'git_blob_sha1': 'fef0f0fa067d720ee6095b54c8e8ca8b02ca940f'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/NOTE.md': {'bytes': 5796, 'sha256': '7ec2be2957f705b844cbae6d2a1b8325d6580bd655581b3df3daaba1fa493ea6', 'git_blob_sha1': '898ff96224b774465680776cac61cf046eb5ab12'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/check.py': {'bytes': 920, 'sha256': 'ee81293723e33d83fdfd448428f4947b4d594e3c112ca986b9f7b87decb33cf5', 'git_blob_sha1': 'de915323d98b0f0c0d4ec335ca567e62a1e5ef8a'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/check_comprehensive.py': {'bytes': 2041, 'sha256': '41105debf4bc33583731f8a4fb6037e2efc90993f96d01592cce9f7e77d3bd8a', 'git_blob_sha1': '0162d1c53c4adea937899ea940b6ccaa43a36367'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/comprehensive_records.jsonl': {'bytes': 3807328, 'sha256': 'd339b7546de48371690fbf7ee20a7db2bbefae7b59f439c0a71820efd7ac7466', 'git_blob_sha1': 'cb8d8b578942d5d851596b232742584f66e06416'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/comprehensive_run.log': {'bytes': 68, 'sha256': 'd093cde00b148163e37e8348c09f10512863e3a8be500170444c0a7f434754ed', 'git_blob_sha1': '4aef57d541834ebd47ec5eca408ec1244c10660b'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/diagnostic.log': {'bytes': 10141, 'sha256': '1eef8b2c234a8fc71718b3f25d9a18546f48271b207527ba4b1e99a05a69a8c1', 'git_blob_sha1': 'f3d5b2d3e7a3338712381d5d2dfd4ba9ea03e69f'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/review_independent_20261103_1010/CLARIFICATION_REVIEW.md': {'bytes': 1825, 'sha256': 'abf308b388044c0392aa7156a143307c0658f728415291730817675997d41381', 'git_blob_sha1': 'e365aefadfe3260367a4d0a51f460e68260e089f'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/review_independent_20261103_1010/REVIEW.md': {'bytes': 4811, 'sha256': '697705f5d54a68435b99f4eef9948dac5c0ab69b7dbbf5db46679c02d3b93cb1', 'git_blob_sha1': 'f7f15dbe45a4f0ad9210f637823ec3025cef0bc7'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/review_independent_20261103_1010/clarification_review_hashes.sha256': {'bytes': 1110, 'sha256': 'bf5bf49ffda20211b19b56bcd4fbcbed445903926fa6ebd966038ad5aa2f8a48', 'git_blob_sha1': '5093f9868cb545402469f9dd9519c5804ae27085'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/review_independent_20261103_1010/comprehensive_recheck.log': {'bytes': 93, 'sha256': 'df43b3e3498e70f77826ca0d2791a11b142e6ccead868f38f2655486c52f9872', 'git_blob_sha1': 'cfced0fae0174c2d59163fabd404b0ca6098d74e'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/review_independent_20261103_1010/comprehensive_recheck_records.jsonl.gz': {'bytes': 4919489, 'sha256': '91efdb794a1efd8dc3b2df14e9d842c0bd625271905847818fed4ffba4b47601', 'git_blob_sha1': '51129957506e9a35a0dd37157790e87d3116b9d9'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/review_independent_20261103_1010/comprehensive_source_verification.log': {'bytes': 334, 'sha256': 'f7c3e097a1a8303598188a40c16e06a1a67169590740dd5062c6a20d2d631abd', 'git_blob_sha1': 'd94ecbd2ff89235862fb4cec2c7cc3834891d9c8'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/review_independent_20261103_1010/comprehensive_sources.sha256': {'bytes': 582, 'sha256': '839ab7b04fae5beaaf44c455bfa194b05ff36ba39e73c881f0e65e9d8925e132', 'git_blob_sha1': 'b7f610add081d406445d71b2b2d4dc4a37dd517c'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/review_independent_20261103_1010/review_hashes.sha256': {'bytes': 344, 'sha256': '4373e5c9726481c6de720800816982d82024b9411a5a7a46ca2b73769b8f1ad0', 'git_blob_sha1': '6f1f77d89b556ed2ad347e904cbd2e7ff8dceaa8'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/review_independent_20261103_1010/source_binding.sha256': {'bytes': 544, 'sha256': 'a0d3eaca55f197bdf1eaab96b63ac86b05183ed2ea09e2b010f4dbd818e14cb8', 'git_blob_sha1': '7014dfcc959d6027b63708c8abb2a9ae6f557619'}, 'v10_research/half_gate_iid_identifiability_20261103_1009/review_independent_20261103_1010/verify_records.py': {'bytes': 2008, 'sha256': '18d7494487f4ea9c81e3679b5ca78c28e122a14783c5e9e0c4e597b379996b39', 'git_blob_sha1': '510cf4d9c2d0942b148bd8fa6835685d16ee21a2'}, 'v10_research/matched_slow_source_audit_20261103_1016/INDEPENDENT_REVIEW.md': {'bytes': 1285, 'sha256': '613a1880442796595c9b90c7547712498f5c0eabcca998e9ca747dc1ec55c54e', 'git_blob_sha1': 'f351a3af309114328a8a7d19abc9a80f92cf6731'}, 'v10_research/matched_slow_source_audit_20261103_1016/PAIRED_SOURCE_SCOPE_AUDIT.md': {'bytes': 10340, 'sha256': 'a30e7bf706113557b58b1070d53d845ed15e0557b0467c277ef53f41ff150fd0', 'git_blob_sha1': 'e425f0fd2fc91f21c68b68e50d7af2d461d91cb5'}, 'v10_research/matched_slow_source_audit_20261103_1016/RESOURCE_DETAIL.md': {'bytes': 1250, 'sha256': '19fb35bc52ea3b3b345fc7601eca06489b7b21144a2f6948af66d205e361cbca', 'git_blob_sha1': 'a9e333c8cde6c08a1d1fd15615dacf588dc64702'}, 'v10_research/matched_slow_source_audit_20261103_1016/REVIEW_CLARIFICATION.md': {'bytes': 811, 'sha256': '64d25c8a50f1b49fb1954bfeb50802c73886761e3589fae8abbf759c449eedab', 'git_blob_sha1': 'fbca5f5c16fd3290bb9642b64793efae69b0da15'}, 'v10_research/matched_slow_source_audit_20261103_1016/SOURCE_BINDINGS.md': {'bytes': 626, 'sha256': 'ee6ee6e2c06efa0c3defef2f4409a93a0813d32b560738d9a51080dc35a0dce8', 'git_blob_sha1': '15f02116fd4d2576341445d3f7cf034d79e832eb'}, 'v10_research/shared_source_vs_fresh_prior_20261103_1031/BASELINE_AND_COROLLARY.md': {'bytes': 12930, 'sha256': '165a1d1787efd3504b5a273e956798c906352543472cf4876750677f8642fa2c', 'git_blob_sha1': 'e85aa6b9786baefada71db9da5e0184417c5b3b2'}, 'v10_research/shared_source_vs_fresh_prior_20261103_1031/INDEPENDENT_REVIEW_AND_CORRECTIONS.md': {'bytes': 1528, 'sha256': '6544d64e5e1bfb05ca2a5ef9ed3e9137314b1c8a1fea6dda38a65fa74281ef59', 'git_blob_sha1': 'cc0c2dad0a7188d4afcfda63672402acb056445a'}}
if set(selected)!=set(EXPECTED_SOURCES) or len(mp['files'])!=25:raise ValueError('Incomplete/duplicate selected sources')
for path,m in selected.items():
 if m['changed'] or m['original']!=m['public'] or m['public']!=EXPECTED_SOURCES[path]:raise ValueError('Unexpected source edit')
 check(path,m['public'])
deps={x['path']:x for x in recon['inherited_dependencies']}
EXPECTED_DEPS={'v10_research/positional_manuscript_consolidated_20261103/main.tex': {'bytes': 33339, 'sha256': '5c4a5a91e08a4ba0eaf40eff7b19010b88f3e6f3d616f80bdfa58ad1756f8fa1', 'git_blob_sha1': '337d30fb8bbb8d410cfdd6574346a4bcdf023ce9'}, 'v10_research/positional_manuscript_consolidated_20261103/sections/proofs_negative.tex': {'bytes': 28723, 'sha256': 'c33000a5e7b98eb395d8ccae7c104b60d4cf7d30900607d64f4102c9bf9302c7', 'git_blob_sha1': 'bb1351ffab5b63dc12dd1a695e174c3b8f08f136'}, 'v10_research/positional_manuscript_consolidated_20261103/sections/proofs_positive.tex': {'bytes': 32814, 'sha256': 'a629caebe01e614a71738f2036bd9016708f35871a15b6902dd98be967f69e88', 'git_blob_sha1': 'a5dea704fdaa9d87b47f8344b0a89ad25c309e91'}, 'v10_research/clean_training_objective_20261103/CANDIDATE.md': {'bytes': 13917, 'sha256': '1405c661827773bba64c8d8ae91f8eb8a9b2bf17ffc6a66e3be69525f1674bb2', 'git_blob_sha1': 'cadbd0c2ff3b9e5f9e74566d8ef43828dbd503b7'}, 'v10_research/positional_gate_training_20261103/CANDIDATE.md': {'bytes': 12550, 'sha256': '91dcb755e6544fa04e728ab92bf48a7cb864e1e28fc9e4cbdbe0fc38257cb0be', 'git_blob_sha1': 'e3f5e0867e619d03af7fa9e72289c718a934a3de'}, 'v10_research/binary_budget_adaptation/AB001_joint_blindness_obstruction.md': {'bytes': 9876, 'sha256': '865b65e296c39c632aa619c1d2588ad8b9d221efd6e8d799c8b15814b40a1e3d', 'git_blob_sha1': '4405bbd9773437aef5d6a421cba98c52444f8cb7'}, 'v10_research/balanced_joint_finite_cut/BCJ001_theorem.md': {'bytes': 19465, 'sha256': '95d5aac1ee2504955e55c1e82241c8a07d219661e2620c6e083acf5c8701554d', 'git_blob_sha1': '8575ab03ac332796cc73a11e41e0620d7b3df8d2'}, 'v10_research/intake/BCJ001_root_acceptance.json': {'bytes': 1122, 'sha256': '27c1aa7efdc86752c63fd0b1f41b9c303a2aedff965ce81721f3abca7c54699f', 'git_blob_sha1': '7912a1931734bd4dd845fd03b9e0458bbd377089'}, 'v10_research/balanced_joint_finite_cut/BCJ001_independent_full_review.md': {'bytes': 13368, 'sha256': '1e74c502da8fcda31603fc7fc2fa1229747521c3774da55aaf21c8a29a14f64b', 'git_blob_sha1': 'afeeed252adabe83e66c850a248e3287baf4f432'}}
if set(deps)!=set(EXPECTED_DEPS) or len(recon['inherited_dependencies'])!=9:raise ValueError('Incomplete/duplicate inherited closure')
for path,d in deps.items():
 if path in selected or d['original_public_status']!='BYTE_IDENTICAL' or d['identity']!=EXPECTED_DEPS[path]:raise ValueError('Invalid inherited classification')
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
if seen!=census or len(seen)!=26 or counts!={'EXACT_SELECTED_SOURCE':17,'EXACT_INHERITED_PUBLIC_SOURCE':9} or counts!=recon['counts']:raise ValueError('Incomplete explicit binding census')
module_bytes=check(PREFIX+'verify_retained_records.py')
if hashlib.sha256(module_bytes).hexdigest()!='ea3397077f5b8bcdb8c51d7823f979fdf4005946599d712e79f2d67892096624':raise ValueError('Retained module identity mismatch')
mod=types.ModuleType('retained_iid');mod.__file__=str(ROOT/PREFIX/'verify_retained_records.py');exec(compile(module_bytes,mod.__file__,'exec'),mod.__dict__)
result=mod.verify_records(ROOT/'v10_research')
print(json.dumps({'status':'PASS','verified_public_files':len(verified),'selected_sources':25,'explicit_bindings':26,'inherited_context_files':9,'retained_arithmetic':result,'scope_limits':['Only the two later exact archives are arithmetically checked; original missing tails/wrapper failure output are not recovered.','No historical scripts, sampling, model initialization, native research executable or network was used.','Trusted pinned inventory is an identity root, not an untrusted-code sandbox or formal proof.']},ensure_ascii=False,indent=2))
