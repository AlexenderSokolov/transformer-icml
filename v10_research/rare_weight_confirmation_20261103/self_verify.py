"""Read-only reconciliation of committed raw data and completed update trajectory.

Never computes training gradients or performs fitting; Adam arithmetic is reconstructed
solely from the recorded gradient journal. Saved PRNG states are replayed only to
verify captured candidate arrays, not to generate fresh experimental observations.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1';os.environ['MKL_NUM_THREADS']='1'
import json,csv,hashlib
from pathlib import Path
import numpy as np
import experiment as e
P=Path(__file__).resolve().parent;O=P/'confirmation_v1';cfg=e.CFG

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
seal=e.verify_seal();approval=e.require_review_approval();art=json.loads((O/'ARTIFACT_HASHES.json').read_text());bad=[k for k,v in art.items() if sha(O/k)!=v];assert not bad
f=np.load(O/'frozen_data.npz');data_checks={}
for label,key,n in [('train','train',cfg['training_prior_words']),('natural','natural',cfg['natural_prior_evaluation_words']),('hold','rare_heldout',cfg['rare_group_heldout_words'])]:
 directory=O/'candidate_batches'/label;files=sorted(directory.glob('batch_*.npz'));intents=sorted(directory.glob('*.intent.json'));assert len(files)==len(intents)>0
 rng=np.random.default_rng(cfg['data_seeds'][{'train':'training','natural':'natural_evaluation','hold':'rare_group_heldout'}[label]])
 selected=[];total=0;drawn=0
 for index,(path,ip) in enumerate(zip(files,intents)):
  d=np.load(path,allow_pickle=False);intent=json.loads(ip.read_text());before=e.state_json(rng)
  assert intent['set']==label and intent['batch_index']==index and intent['n']==len(d['words']) and intent['M']==64
  assert intent['rng_before']==json.loads(before) and str(d['rng_before'])==before
  probe=e.candidate_batch(len(d['words']),64,rng)
  for k in ['words','probabilities','starts','uniforms','rng_before','rng_after']:assert np.array_equal(d[k],probe[k]),(label,index,k)
  keys,rare=e.group_stats(d['words']);held=e.holdout(keys);eligible=np.ones(len(keys),bool) if label=='natural' else (~held if label=='train' else (held&rare))
  expected=np.zeros(len(keys),bool);ids=np.flatnonzero(eligible);expected[ids[:max(0,n-total)]]=True
  assert np.array_equal(eligible,d['eligible']) and np.array_equal(expected,d['selected']) and int(d['global_candidate_start'])==drawn
  selected.append(d['words'][expected]);total+=int(eligible.sum());drawn+=len(keys)
 assert np.array_equal(np.concatenate(selected),f[key+'_words'])
 data_checks[label]={'batches':len(files),'drawn':drawn,'saved':n,'eligible':total,'actual_candidate_arrays_reconstructed':True}

keys_train,_=e.group_stats(np.concatenate([f['train_words'],f['collision_words']]));keys_hold,_=e.group_stats(f['rare_heldout_words']);keys_20,_=e.group_stats(f['structural_unseen20_words']);assert not(set(map(tuple,keys_train))&set(map(tuple,keys_hold)));assert not(set(map(tuple,keys_train))&set(map(tuple,keys_20)));assert not(set(map(tuple,keys_20))&e.prior_input_groups())
summary_rows=list(csv.DictReader((O/'updates.csv').open()));assert len(summary_rows)==12000
metrics_rows=list(csv.DictReader((O/'checkpoint_metrics.csv').open()));assert len(metrics_rows)==24
last_key=None;opt=None;model=None;records=0;maxdiff=0.0;checkpoints=0
for index,(meta,grad,post) in enumerate(e.read_update_records(O/'full_updates.bin')):
 key=(meta['arm'],meta['seed']);step=int(meta['step']);row=summary_rows[index];assert (row['arm'],int(row['seed']),int(row['step']))==(key[0],key[1],step)
 if key!=last_key:
  assert step==1
  model=e.c.Readout(key[1],'half_count_scaled');opt=e.c.pilot.Adam(model.params,readout_lr=.003,beta1=.9,beta2=.999,epsilon=1e-8)
  z=np.load(O/'checkpoints'/f'{key[0]}_{key[1]}_step0.npz')
  for name in model.params:assert np.array_equal(model.params[name],z['param_'+name]) and np.array_equal(opt.m[name],z['adam_m_'+name]) and np.array_equal(opt.v[name],z['adam_v_'+name])
  checkpoints+=1;last_key=key
 opt.step(model.params,grad)
 for name in post:
  diff=float(np.max(np.abs(model.params[name]-post[name])));maxdiff=max(maxdiff,diff);assert np.array_equal(model.params[name],post[name]),(key,step,name,diff)
 assert abs(float(row['gradient_l2'])-np.sqrt(sum(np.sum(g*g) for g in grad.values())))<1e-12
 assert abs(float(row['effective_W_l2'])-np.linalg.norm(model.effective_W()))<1e-12
 if step in [200,1000,2000]:
  z=np.load(O/'checkpoints'/f'{key[0]}_{key[1]}_step{step}.npz');assert int(z['optimizer_step'])==step
  for name in model.params:assert np.array_equal(model.params[name],z['param_'+name]) and np.array_equal(opt.m[name],z['adam_m_'+name]) and np.array_equal(opt.v[name],z['adam_v_'+name])
  checkpoints+=1
 records+=1
assert records==12000 and checkpoints==24
# Reconstruct every final prediction and all final metric values from weights.
preds=np.load(O/'final_predictions.npz');result=json.loads((O/'results.json').read_text());maxpred=0.;maxmetric=0.
for row in result['final_metrics']:
 arm=row['arm'];seed=row['seed'];model=e.c.Readout(seed,'half_count_scaled');opt=e.c.pilot.Adam(model.params);e.restore_checkpoint(O/'checkpoints'/f'{arm}_{seed}_step2000.npz',model,opt)
 for name in ['train','natural','rare_heldout','collision','structural_heldout','structural_previous8','structural_unseen20']:
  x=e.c.features(f[name+'_words'],'half_count_scaled');q=model.predict(x);saved=preds[f'{arm}_{seed}_{name}'];maxpred=max(maxpred,float(np.max(np.abs(q-saved))));assert np.allclose(q,saved,rtol=0,atol=1e-14)
  if name!='train':
   for k,v in e.metrics(f[name+'_Q'],q).items():
    delta=abs(float(v)-float(row[name+'_'+k]));maxmetric=max(maxmetric,delta);assert delta<1e-12
assert result['status']=='SIX_FITS_COMPLETE_NOT_INDEPENDENTLY_REVIEWED'
print(json.dumps({'status':'author_reconciliation_passed_not_independent_audit','sealed_files':len(seal['files']),'output_hashes':len(art),'candidate_batches':data_checks,'journal_prepared_records_reconciled_with_csv_and_adam':records,'model_and_adam_checkpoints_reconciled':checkpoints,'max_journal_parameter_discrepancy':maxdiff,'max_final_prediction_discrepancy':maxpred,'max_final_metric_discrepancy':maxmetric,'training_group_intersections':0,'structural_unseen20_previous_input_group_intersections':0},indent=2,sort_keys=True))
