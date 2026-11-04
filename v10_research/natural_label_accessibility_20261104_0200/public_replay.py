#!/usr/bin/env python3
"""Offline audit of saved scientific states, not a new fit or private service audit.
All numerical checks in historical postrun_audit.py are invoked unchanged.
The two explicitly replaced gates concern public provenance, not numerical results.
"""
import argparse,hashlib,importlib,json,os,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def replay(root):
 root=Path(root).resolve();index=json.loads((HERE/'PUBLIC_ARCHIVE_INDEX.json').read_text())
 captures={r['restore_directory']:r for r in index['captures']}
 original_binding=index['frozen_original_source_manifest_sha256']
 def verify_members(c):
  base=root if c['restore_directory']=='.' else root/c['restore_directory']
  for r in c['members']:
   p=base/r['path'];b=p.read_bytes()
   assert len(b)==r['public_bytes'] and sha(b)==r['public_sha256'],str(p)
   if r['path'].endswith(('.py','.npy','.npz')):assert r['byte_identical'] and sha(b)==r['original_sha256'],r['path']
 def frozen_sources_public():
  verify_members(captures['.'])
  assert sha((root/'SOURCE_MANIFEST.json').read_bytes())==original_binding
  return len(json.loads((root/'SOURCE_MANIFEST.json').read_text())['files'])
 def captured_public(directory,kind):
  c=captures[directory.relative_to(root).as_posix()];assert c['kind']==kind;verify_members(c)
  # Original hash is an identity linkage only, not a claim that the redacted archive
  # still has the original bytes. The separate public hash is the current identity.
  return {'sha256':c['original_archive_sha256'],'original_bytes':c['original_archive_bytes'],'public_sha256':c['public_archive_sha256'],'public_bytes':c['public_archive_bytes'],'members':len(c['members']),'private_storage_audit_performed':False}
 source_map=json.loads((HERE/'PUBLIC_TEXT_SOURCE_MAP.json').read_text())
 for name in ('postrun_audit.py','postrun_analysis_audit.py'):
  r=next(x for x in source_map['files'] if x['path']=='supplement/'+name)
  assert r['byte_identical'] and sha((root/name).read_bytes())==r['original_sha256']
 for c in captures.values():verify_members(c)
 sys.path.insert(0,str(root));audit=importlib.import_module('postrun_audit')
 audit.ROOT=root;audit.frozen_sources=frozen_sources_public;audit.captured=captured_public
 reports=[audit.audit(r) for r in range(4)]
 cfg=json.loads((root/'protocol.json').read_text());res=json.loads((root/'analysis/all_results.json').read_text());primary={c:[] for c in cfg['conditions']}
 for r in range(4):
  for c in cfg['conditions']:
   summary=json.loads((root/f'runs/rep{r}'/c/'summary.json').read_text())
   assert res['cells'][f'rep{r}_{c}']==summary
   means=[]
   for M in cfg['test_horizons']:
    with np.load(root/f'runs/rep{r}'/c/f'evaluation_M{M}.npz',allow_pickle=False) as a:
     if M in cfg['train_horizons']:means.append(float(a['model_kl_B'].mean()))
   primary[c].append(sum(means)/len(means))
 assert res['primary_replicate_means']==primary
 screens={}
 for pool in ('uniform','learned'):
  natural=np.array(primary[pool+'_y']);teacher=np.array(primary[pool+'_B']);gaps=natural-teacher
  actual=res['screening'][pool];count=int(sum(natural<=cfg['primary_threshold_nats']));median=float(np.median(gaps))
  passed=count>=3 and median<=cfg['natural_minus_teacher_median_threshold_nats']
  assert actual['replicates_at_or_below_threshold']==count and actual['median_paired_natural_minus_teacher']==median and actual['passes_descriptive_screen']==passed
  screens[pool]={'count':count,'median_gap':median,'passes':passed}
 assert not all(x['passes'] for x in screens.values())
 return {'schema':'public-offline-saved-state-audit-v1','status':'PASS','saved_updates_checked':sum(c['saved_update_transitions_checked'] for r in reports for c in r['conditions'].values()),'replicates':reports,'primary_means':primary,'screens':screens,'joint_hypothesis_passes':False,'new_random_draws':0,'new_fits':0,'private_storage_audit_performed':False,'scope':'Public member identities plus unchanged historical numerical state/gradient/prediction checks. Provenance-only gates replaced by public hashes; no private service receipts fabricated.'}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('restored',type=Path);p.add_argument('--report',type=Path,required=True);a=p.parse_args()
 for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
  if os.environ.get(k)!='1':raise ValueError(k+' must be 1 before Python/NumPy starts')
 result=replay(a.restored)
 with a.report.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({'status':result['status'],'saved_updates_checked':result['saved_updates_checked'],'joint_hypothesis_passes':False}))
