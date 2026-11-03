#!/usr/bin/env python3
"""Read-only identity, binding and retained-arithmetic checks for a pinned public checkout."""
import hashlib,json,pathlib,sys,types,re,posixpath
if sys.flags.optimize:raise SystemExit('Optimized Python is not supported: arithmetic assertions must remain enabled.')
PREFIX='provenance/float_and_attack_boundaries_20261103/'
ROOT=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else pathlib.Path(__file__).absolute().parents[2]).absolute()
def read(path):
 p=pathlib.PurePosixPath(path)
 if p.is_absolute() or '..' in p.parts:raise ValueError('Unsafe repository-relative path')
 current=ROOT
 if current.is_symlink() or any(a.is_symlink() for a in current.parents):raise ValueError('Symlink checkout root or ancestor')
 for bit in p.parts:
  current=current/bit
  if current.is_symlink():raise ValueError('Symlink input refused')
 if not current.is_file():raise ValueError('Missing regular input: '+path)
 return current.read_bytes()
def unique(pairs):
 d={}
 for k,v in pairs:
  if k in d:raise ValueError('Duplicate JSON key')
  d[k]=v
 return d
def parse(b):return json.loads(b,object_pairs_hook=unique,parse_constant=lambda x:(_ for _ in ()).throw(ValueError('Nonfinite JSON constant')))
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_sha1':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
inv=parse(read('provenance/PUBLIC_INVENTORY.json'))
rows={}
for row in inv['files']:
 path=row['path']
 if path in rows:raise ValueError('Duplicate inventory path')
 rows[path]=row
verified=set()
def check(path,want=None):
 b=read(path);got=identity(b);entry=rows[path]
 if got!={k:entry[k] for k in got}:raise ValueError('Inventory mismatch: '+path)
 if want and got!=want:raise ValueError('Declared source identity mismatch: '+path)
 verified.add(path);return b
for path in sorted(rows):
 if path.startswith(PREFIX):check(path)
source=parse(read(PREFIX+'SOURCE_EXPORT_MAP.json'));recon=parse(read(PREFIX+'PUBLIC_EXPORT_RECONCILIATION.json'))
source_rows={x['path']:x for x in source['files']}
if len(source_rows)!=len(source['files']):raise ValueError('Duplicate source mapping')
if len(source_rows)!=258 or len(recon['bindings'])!=486:raise ValueError('Incomplete bounded source/binding census')
for path,f in source_rows.items():
 check(path,f['public'])
 if f['changed']!=(f['original']!=f['public']):raise ValueError('False changed-source flag')
deps={x['path']:x for x in recon['inherited_dependencies']}
if len(deps)!=len(recon['inherited_dependencies']) or len(deps)!=34:raise ValueError('Duplicate or incomplete inherited dependencies')
for path,d in deps.items():
 check(path,d['public'])
 if path in source_rows:raise ValueError('Inherited dependency overlaps new sources')
 if d['status'] not in ('EXACT_INHERITED_PUBLIC_SOURCE','EXACT_PUBLIC_PATH_ALIAS','DECLARED_INHERITED_EXPORT_PAIR'):raise ValueError('Invalid dependency class')
 if d['status']!='DECLARED_INHERITED_EXPORT_PAIR' and d['original_sha256']!=d['public']['sha256']:raise ValueError('False exact dependency')
for pair in recon['inherited_export_pairs']:
 m=parse(check(pair['identity_map']));matches=[x for x in m['files'] if x['path']==pair['path']]
 if len(matches)!=1 or matches[0]['original']!=pair['original'] or matches[0]['public']!=pair['public']:raise ValueError('Inherited identity map mismatch')
nonpublic={x['reference']:x for x in recon['nonpublic_metadata']}
if len(nonpublic)!=len(recon['nonpublic_metadata']) or len(nonpublic)!=8:raise ValueError('Duplicate or incomplete nonpublic references')
aliases={x['historical_path']:x for x in recon['aliases']}
if len(aliases)!=len(recon['aliases']) or len(aliases)!=6:raise ValueError('Duplicate or incomplete aliases')
for alias in aliases.values():
 if alias['original']!=alias['public'] or identity(check(alias['public_path']))!=alias['public']:raise ValueError('False byte alias')
 if not any(b['status']=='EXACT_PUBLIC_PATH_ALIAS' and b['public_path']==alias['public_path'] and b['original_sha256']==alias['original']['sha256'] and (b['reference']==alias['historical_path'] or (alias['historical_path']=='historical-replay-document' and b['reference']==alias['public_path'])) for b in recon['bindings']):raise ValueError('Alias lacks corresponding binding')
def owner_reference(binding):
 owner=binding['owner']
 if owner not in source_rows:raise ValueError('Binding owner outside selected sources')
 content=check(owner)
 locator=binding['locator']
 if set(locator)=={'line'}:
  if type(locator['line']) is not int or locator['line']<1:raise ValueError('Invalid positive line locator')
  line=content.decode().splitlines()[locator['line']-1]
  match=re.fullmatch(r'([0-9a-f]{64})[ \t]+\*?(.+?)\s*',line)
  if match is None:raise ValueError('Binding line is not a checksum entry')
  digest,reference=match.groups()
 elif set(locator)=={'json_key'}:
  keys=locator['json_key'];value=parse(content)
  if not isinstance(keys,list) or not keys or any((type(k) is int and k<0) or type(k) not in (str,int) for k in keys):raise ValueError('Invalid JSON locator')
  for key in keys[:-1]:value=value[key]
  digest=value[keys[-1]]
  reference=value['path'] if keys[-1]=='sha256' and isinstance(value,dict) and 'path' in value else keys[-1]
 else:raise ValueError('Unknown binding locator')
 if digest!=binding['original_sha256']:raise ValueError('Owner expected original hash mismatch')
 if not isinstance(reference,str):raise ValueError('Invalid owner reference')
 if binding['status']=='NONPUBLIC_HISTORICAL_METADATA':
  if reference!=binding['reference']:raise ValueError('Unavailable metadata reference mismatch')
  return
 candidates={posixpath.normpath(reference)}
 for ancestor in pathlib.PurePosixPath(owner).parents:
  candidates.add(posixpath.normpath(str(ancestor/reference)))
 if binding['reference'] not in candidates:raise ValueError('Binding reference/locator mismatch')
 if binding['status']=='EXACT_PUBLIC_PATH_ALIAS':
  if not any(a['public_path']==binding['public_path'] and (a['historical_path']==binding['reference'] or (a['historical_path']=='historical-replay-document' and a['public_path']==binding['reference'])) for a in aliases.values()):raise ValueError('Binding alias declaration missing')
 elif binding['reference']!=binding['public_path']:raise ValueError('Non-alias public path mismatch')
counts={}
seen_locators=set()
for b in recon['bindings']:
 locator_key=(b['owner'],json.dumps(b['locator'],sort_keys=True))
 if locator_key in seen_locators:raise ValueError('Duplicate binding locator')
 seen_locators.add(locator_key);owner_reference(b)
 state=b['status'];counts[state]=counts.get(state,0)+1
 if state=='NONPUBLIC_HISTORICAL_METADATA':
  n=nonpublic[b['reference']]
  if n['original_sha256']!=b['original_sha256'] or b['public_path'] is not None or b['public_sha256'] is not None:raise ValueError('Bad unavailable metadata declaration')
  continue
 target=b['public_path'];actual=identity(check(target))
 if state in ('EXACT_SELECTED_SOURCE','DECLARED_CURRENT_EXPORT_PAIR') and target not in source_rows:raise ValueError('Selected binding membership mismatch')
 if state in ('EXACT_INHERITED_PUBLIC_SOURCE','EXACT_PUBLIC_PATH_ALIAS','DECLARED_INHERITED_EXPORT_PAIR') and target not in deps:raise ValueError('Inherited binding membership mismatch')
 if actual['sha256']!=b['public_sha256']:raise ValueError('Binding public identity mismatch')
 if state in ('EXACT_SELECTED_SOURCE','EXACT_INHERITED_PUBLIC_SOURCE','EXACT_PUBLIC_PATH_ALIAS'):
  if actual['sha256']!=b['original_sha256']:raise ValueError('False exact source declaration')
 elif state=='DECLARED_CURRENT_EXPORT_PAIR':
  if source_rows[target]['original']==source_rows[target]['public']:raise ValueError('False changed-current binding')
  if source_rows[target]['original']['sha256']!=b['original_sha256']:raise ValueError('Current original mapping mismatch')
 elif state=='DECLARED_INHERITED_EXPORT_PAIR':
  if not any(x['path']==target and x['original']['sha256']==b['original_sha256'] and x['public']['sha256']==actual['sha256'] for x in recon['inherited_export_pairs']):raise ValueError('Missing inherited pair')
 else:raise ValueError('Unknown binding resolution')
if counts!=recon['counts']:raise ValueError('Binding count mismatch')
# Only this hash-checked, reviewed stdlib module runs; archived diagnostics do not.
module=types.ModuleType('retained_arithmetic')
module.__file__=str(ROOT/PREFIX/'verify_retained_records.py')
exec(compile(check(PREFIX+'verify_retained_records.py'),module.__file__,'exec'),module.__dict__)
results=module.verify_records(ROOT/'v10_research')
print(json.dumps({'status':'PASS','verified_public_files':len(verified),'selected_sources':len(source_rows),'binding_status_counts':counts,'nonpublic_historical_metadata_not_replayed':len(nonpublic),'retained_arithmetic':results,'limitations':['Identities assume a trusted pinned checkout; this is not a sandbox for malicious code.','No original script, RNG, model initialization, native executable, BLAS or training replay was run.','Private historical metadata is unavailable publicly; declared original/public pairs are not original-byte recovery.']},ensure_ascii=False,indent=2))
