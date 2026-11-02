#!/usr/bin/env python3
"""Unchanged scientific scripts; exact metadata reconciliation only per consumed binding.
Every execution gets an isolated pristine package-only restoration copy.
"""
from pathlib import Path
import subprocess,sys,json,hashlib,tempfile,shutil
P=Path(__file__).resolve().parent
REPORT=Path(sys.argv[1]) if len(sys.argv)>1 else None
if REPORT:assert not REPORT.resolve().is_relative_to(P.resolve()),'Report must be outside checksummed package'
D=Path(tempfile.mkdtemp(prefix='stage8-diagnostics-'));BASE=D/'base'
subprocess.run([sys.executable,str(P/'verify_package.py'),'--restore',str(BASE)],check=True)
rows=json.loads((P/'SOURCE_RESTORATION_MAP.json').read_text())['files'];by={r['source_path']:r for r in rows};sha=lambda b:hashlib.sha256(b).hexdigest()
package_manifest_hash=sha((P/'SOURCE_MANIFEST.json').read_bytes());runner_hash=sha(Path(__file__).read_bytes())
scripts=sorted(k for k in by if not by[k].get('original_input_verbatim') and k.endswith('.py') and Path(k).name not in ['build_guide.py','verify_guide.py','build_addendum.py','verify_addendum.py','make_manifest.py'])
aliases={};unique={}
for script in sorted(scripts,key=lambda s:(len(Path(s).parts),len(s),s)):
 h=by[script]['source_sha256']
 if h in unique:aliases[script]={'canonical_script':unique[h],'identical_script_sha256':h}
 else:unique[h]=script
scripts=sorted(unique.values());changes=[];results=[]
expected_failures={'v10_research/stage8_science_audit/diagnostic_revisions/independent_exact_checks.v1.py': ('d8476e9a15389ed43957ee28566cee08e62a98e2453f6874abecad7aed7b6c97','lower_and_upper_constant_slack')}
def reconcile(work,script,name,kind,prefix):
 q=work/name;original=q.read_bytes();x=json.loads(original);assert sha(original)==by[name]['export_sha256']
 entries=list(enumerate(x[kind])) if isinstance(x[kind],list) else list(x[kind].items())
 for key,e in entries:
  path=e['path'] if isinstance(e,dict) else key;h=e['sha256'] if isinstance(e,dict) else e
  source=prefix+path;r=by[source];assert h==r['source_sha256']
  actual=sha((work/source).read_bytes());assert actual==r['export_sha256']
  if h!=actual:
   pointer='/'+kind+'/'+(str(key)+'/sha256' if isinstance(e,dict) else key.replace('~','~0').replace('/','~1'))
   changes.append({'script':script,'binding_file':name,'json_pointer':pointer,'source_path':source,'original_sha256':h,'export_sha256':actual,'basis':'exact declared routing-only source/export delta in this script disposable copy'})
   if isinstance(e,dict):e['sha256']=actual
   else:x[kind][key]=actual
 q.write_text(json.dumps(x,indent=2))
for i,s in enumerate(scripts):
 work=D/f'run_{i:02d}';shutil.copytree(BASE,work)
 # Reconcile only bindings actually consumed by this script; unrelated bindings stay pristine.
 if '/two_resource_frontier/' in s:
  reconcile(work,s,'v10_research/two_resource_frontier/TR001_source_bindings_v1.json','sources','v10_research/')
 if '/binary_stationary_frontier/' in s:
  reconcile(work,s,'v10_research/binary_stationary_frontier/BS001_source_bindings_v1.json','sources','v10_research/')
 if s=='v10_research/manuscript_v4/AUDIT_FRESH_CHECKS.py':
  reconcile(work,s,'v10_research/depth_initialization_guide/SOURCE_BINDINGS.json','files','v10_research/')
 if s in ['v10_research/manuscript_v5/audit_science_fresh/check_provenance.py','v10_research/manuscript_v5/audit_science_fresh/bind_final.py']:
  reconcile(work,s,'v10_research/manuscript_v5/SOURCE_MANIFEST.json','sources','')
 if s=='v10_research/manuscript_v5/audit_science_fresh/bind_final.py':
  reconcile(work,s,'v10_research/precision_robustness_guide/SOURCE_BINDINGS.json','files','')
 script_hash=sha((work/s).read_bytes());assert script_hash==by[s]['export_sha256']==by[s]['source_sha256']
 r=subprocess.run([sys.executable,str(work/s)],cwd=work,text=True,capture_output=True)
 assert sha((work/s).read_bytes())==script_hash
 expected=expected_failures.get(s)
 matched=(script_hash==expected[0] and r.returncode!=0 and 'AssertionError: '+expected[1] in r.stderr) if expected else r.returncode==0
 results.append({'script':s,'script_sha256':script_hash,'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'expected_outcome':'HISTORICAL_AUDIT_HARNESS_FAILURE' if expected else 'PASS','matched_expected_outcome':matched});print(s,r.returncode,flush=True)
 shutil.rmtree(work)
result={'status':'PASS' if all(r['matched_expected_outcome'] for r in results) else 'FAIL','restore':str(D),'package_manifest_sha256':package_manifest_hash,'runner_sha256':runner_hash,'binding_reconciliations':changes,'byte_identical_script_aliases':aliases,'passing_current_scripts':sum(r['expected_outcome']=='PASS' and r['returncode']==0 for r in results),'expected_historical_failures':sum(r['expected_outcome']=='HISTORICAL_AUDIT_HARNESS_FAILURE' and r['matched_expected_outcome'] for r in results),'unexpected_failures':sum(not r['matched_expected_outcome'] for r in results),'checks':results,'scope':'Each unchanged scientific script executes in a pristine isolated package restoration. Only its explicitly consumed metadata pointers are reconciled. Original author/review outputs remain immutable evidence. Finite diagnostics are not proof, formal verification or original-network execution. Original-input historical operational scripts are retained verbatim, not re-executed. Document builders/native verifiers have separate clean-rebuild audit. Superseded audit-harness v1 is intentionally replayed as an expected historical failure; it is not counted as a passing scientific diagnostic.'}
out=REPORT or D/'PACKAGE_DIAGNOSTIC_RERUN.json';out.write_text(json.dumps(result,indent=2));print(out);assert result['status']=='PASS'
