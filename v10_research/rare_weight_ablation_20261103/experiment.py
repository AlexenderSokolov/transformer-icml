"""Presealed matched rare-weight experiment; no artifact overwrite."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1';os.environ['MKL_NUM_THREADS']='1'
from pathlib import Path
import sys, json, hashlib, csv, platform, traceback, argparse, time
from datetime import datetime,timezone
import numpy as np
P=Path(__file__).resolve().parent
CAL=P.parent/'readout_conditioning_calibration_20261103'
sys.path.insert(0,str(CAL));import calibration as c
CFG=json.loads((P/'protocol.json').read_text());SALT='v10-rare-split-20261103'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,o):Path(p).write_text(json.dumps(o,indent=2,sort_keys=True,allow_nan=False)+'\n')
def group_stats(words):
 s=c.pilot.statistics(words)
 keys=np.column_stack([s['J'],s['C'],s['D'],s['U']]).astype(int)
 return keys,(s['J']<=6)|(s['D']==0)
def collision_keys():return set(map(tuple,group_stats(c.collision_words())[0]))
def split_key(key):
 key=tuple(int(x) for x in key)
 if key in collision_keys():return False
 return int.from_bytes(hashlib.sha256((SALT+':'+','.join(map(str,key))).encode('ascii')).digest(),'big')%5==0
def holdout(keys):
 unique,inverse=np.unique(keys,axis=0,return_inverse=True)
 return np.array([split_key(k) for k in unique],dtype=bool)[inverse]
def weighted_loss_grad(model,xs,ys,weights):
 grads=[];losses=[]
 for x,y in zip(xs,ys):
  loss,grad,_=model.loss_grad(x,y);losses.append(loss);grads.append(grad)
 g={k:sum(w*gg[k] for w,gg in zip(weights,grads)) for k in grads[0]}
 return float(np.dot(weights,losses)),g

def prior_draw(n,rng):return c.pilot.prior_batch(n,64,rng)[0]
def rejection_draw(n,seed,want):
 rng=np.random.default_rng(seed);parts=[];total=0;drawn=0
 for _ in range(CFG['maximum_draw_batches_per_rejection_set']):
  words=prior_draw(CFG['draw_batch_size'],rng);keys,rare=group_stats(words);isheld=holdout(keys)
  mask=(~isheld) if want=='train' else (isheld&rare)
  selected=words[mask];parts.append(selected);total+=len(selected);drawn+=len(words)
  if total>=n:return np.concatenate(parts)[:n],{'drawn':drawn,'accepted_before_truncation':total,'saved':n}
 raise RuntimeError(f'{want} rejection draw cap reached after {drawn}; accepted {total} of {n}')

def metrics(y,p):
 e=np.abs(y-p);k=c.kl(y,p)
 return {'n':len(y),'mean_KL':float(k.mean()),'mean_abs_error':float(e.mean()),'q95_abs_error':float(np.quantile(e,.95)),'max_abs_error':float(e.max()),'count_over_0_1':int(np.sum(e>.1))}
def model_record(m,x,y):return metrics(y,m.predict(x))
def savecsv(path,rows):
 with open(path,'w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def seal():
 path=P/'PRE_RUN_HASHES.json'
 if path.exists():raise FileExistsError(path)
 files=[P/'protocol.json',P/'PRE_RUN_REPORT.md',P/'experiment.py',P/'test_experiment.py',CAL/'calibration.py',P.parent/'learned_position_pilot_20261103/pilot.py']
 structural=P.parent/'rare_state_enumeration_20261103'/'rare_states.json'
 if not structural.exists():raise FileNotFoundError('Required independently verified structural holdout missing: '+str(structural))
 files += [structural,CAL/'calibration_v1/frozen_data.npz',P/'static_tests.log'] + [P.parent/'rare_state_enumeration_20261103'/name for name in ['REPORT.md','VERIFICATION.json','SOURCE_BINDINGS.json','enumerate_rare.py','verify_independent.py','test_enumeration.py']]
 dump(path,{'status':'SEALED_BEFORE_NEW_DATA_GENERATION_OR_FITTING','sealed_utc':datetime.now(timezone.utc).isoformat(),'files':{str(f.relative_to(P.parent.parent)):sha(f) for f in files}})
 print(path.read_text())
def verify_seal():
 data=json.loads((P/'PRE_RUN_HASHES.json').read_text())
 for p,h in data['files'].items():
  if sha(P.parent.parent/p)!=h:raise RuntimeError('sealed input changed: '+p)
 return data

def run(out):
 sealdata=verify_seal();out=Path(out)
 if not out.is_absolute():out=P/out
 out.mkdir(exist_ok=False,parents=True);(out/'checkpoints').mkdir()
 start=time.perf_counter()
 try:
  import unittest,test_experiment
  with (out/'tests.log').open('w') as f:
   result=unittest.TextTestRunner(stream=f,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(test_experiment))
  if not result.wasSuccessful():raise AssertionError('unit tests failed before sampling')
  train,tinfo=rejection_draw(CFG['training_prior_words'],CFG['data_seeds']['training'],'train')
  val=prior_draw(CFG['natural_prior_evaluation_words'],np.random.default_rng(CFG['data_seeds']['natural_evaluation']))
  hold,hinfo=rejection_draw(CFG['rare_group_heldout_words'],CFG['data_seeds']['rare_group_heldout'],'hold')
  col=c.collision_words();struct=json.loads((P.parent/'rare_state_enumeration_20261103'/'rare_states.json').read_text());rows=struct['rows'];allstruct=np.array([[int(b) for b in row['word']] for row in rows],dtype=np.int8)
  sk,srare=group_stats(allstruct);sheld=holdout(sk)
  assert len(rows)==128 and all(len(row['word'])==66 for row in rows)
  for i,row in enumerate(rows):
   assert tuple(sk[i])==(row['J'],row['C'],row['D'],row['U'])
   assert sheld[i]==(row['split']=='holdout')
   assert c.literal_statistics(allstruct[i:i+1])['Q'][0]==row['Q_numerator']/row['Q_denominator']
   xx=c.features(allstruct[i:i+1],'half_count_scaled')[0]*c.SCALE
   assert np.array_equal(xx[2:6],[row['a0'],row['a1'],row['b0'],row['b1']])
  structure=allstruct[sheld];assert len(structure)==11
  previous=np.load(CAL/'calibration_v1/frozen_data.npz');prevwords=np.concatenate([previous[n+'_words'] for n in ['train','validation','collision','boundary']]);prevkeys,_=group_stats(prevwords);oldgroups=set(map(tuple,prevkeys));novelmask=np.array([tuple(k) not in oldgroups for k in sk[sheld]],bool);novelstructure=structure[novelmask]
  assert len(novelstructure)==8 and len(set(map(tuple,sk[sheld][novelmask])))==7
  tk,tr=group_stats(train);vk,vr=group_stats(val);hk,hr=group_stats(hold);ck,cr=group_stats(col);zk,zr=group_stats(structure)
  assert not holdout(tk).any() and not holdout(ck).any() and holdout(hk).all() and hr.all() and holdout(zk).all() and (zk[:,0]<=3).all()
  train_groups=set(map(tuple,np.r_[tk,ck]));held_groups=set(map(tuple,hk));struct_groups=set(map(tuple,zk))
  assert not (train_groups&held_groups) and not (train_groups&struct_groups)
  assert len(structure)>0 and tr.any() and (~tr).any()
  y={name:c.literal_statistics(w)['Q'] for name,w in [('train',train),('natural',val),('rare_heldout',hold),('collision',col),('structural_heldout',structure),('structural_novel',novelstructure)]}
  words={'train':train,'natural':val,'rare_heldout':hold,'collision':col,'structural_heldout':structure,'structural_novel':novelstructure}
  x={name:c.features(w,'half_count_scaled') for name,w in words.items()}
  for name in words:
   assert np.max(abs(c.decode_features(x[name])-y[name]))<1e-14
   assert np.max(abs(c.pilot.statistics(words[name])['Q']-y[name]))<1e-14
  rareidx=np.where(tr)[0];commonidx=np.where(~tr)[0];p=len(rareidx)/len(train);steps=CFG['optimization']['steps'];rng=np.random.default_rng(CFG['data_seeds']['minibatches'])
  ir=np.empty((steps,32),int);inn=np.empty((steps,32),int);ic=np.empty((steps,64),int)
  for i in range(steps):ir[i]=rng.choice(rareidx,32);inn[i]=rng.choice(commonidx,32);ic[i]=rng.integers(0,4,64)
  packed={name+'_words':v for name,v in words.items()};packed.update({name+'_Q':v for name,v in y.items()});packed.update(prior_rare_indices=ir,prior_nonrare_indices=inn,collision_indices=ic,train_groups=tk,natural_groups=vk,rare_heldout_groups=hk,structural_heldout_groups=zk)
  np.savez_compressed(out/'frozen_data.npz',**packed)
  wordset=lambda w:set(map(bytes,np.asarray(w,dtype=np.uint8)))
  checks={'train_sampling':tinfo,'holdout_sampling':hinfo,'p_empirical_rare':p,'rare_count':len(rareidx),'nonrare_count':len(commonidx),'train_group_count':len(train_groups),'rare_heldout_group_count':len(held_groups),'structural_heldout_group_count':len(struct_groups),'structural_heldout_feature_count':len(structure),'structural_novel_feature_count':len(novelstructure),'structural_novel_group_count':7,'train_intersection_rare_groups':len(train_groups&held_groups),'train_intersection_struct_groups':len(train_groups&struct_groups),'natural_train_distinct_word_overlap':len(wordset(val)&wordset(train)),'heldout_train_distinct_word_overlap':len(wordset(hold)&wordset(train)),'rare_factors_corrected':[2*p,2*(1-p)],'rare_factors_boost':[1,1],'frozen_data_sha256':sha(out/'frozen_data.npz')}
  dump(out/'pre_fit_checks.json',checks);print(json.dumps({'pre_fit_checks':checks}),flush=True)
  predictions={};checkpoint_rows=[];update_rows=[];final=[]
  for seed in CFG['initialization_seeds']:
   for arm in ['corrected','rare_boost']:
    model=c.Readout(seed,'half_count_scaled');opt=c.pilot.Adam(model.params,readout_lr=.003,beta1=.9,beta2=.999,epsilon=1e-8)
    weights=np.array([.5*p,.5*(1-p),.5]) if arm=='corrected' else np.array([.25,.25,.5])
    def checkpoint(step):
     model.save(out/'checkpoints'/f'{arm}_{seed}_step{step}.npz');row={'arm':arm,'seed':seed,'step':step}
     for name in ['natural','rare_heldout','collision','structural_heldout','structural_novel']:
      row.update({name+'_'+k:v for k,v in model_record(model,x[name],y[name]).items()})
     for label,mask in [('train_rare',tr),('train_nonrare',~tr)]:
      row.update({label+'_'+k:v for k,v in model_record(model,x['train'][mask],y['train'][mask]).items()})
     checkpoint_rows.append(row);print(json.dumps(row),flush=True);return row
    checkpoint(0)
    for j in range(steps):
     loss,grad=weighted_loss_grad(model,[x['train'][ir[j]],x['train'][inn[j]],x['collision'][ic[j]]],[y['train'][ir[j]],y['train'][inn[j]],y['collision'][ic[j]]],weights)
     if not np.isfinite(loss) or not all(np.isfinite(g).all() for g in grad.values()):raise FloatingPointError('nonfinite loss or gradient')
     opt.step(model.params,grad)
     if not all(np.isfinite(v).all() for v in model.params.values()):raise FloatingPointError('nonfinite parameter')
     row={'arm':arm,'seed':seed,'step':j+1,'weighted_CE':loss,'gradient_l2':float(np.sqrt(sum(np.sum(g*g) for g in grad.values()))),'effective_W_l2':float(np.linalg.norm(model.effective_W())),'raw_W_l2':float(np.linalg.norm(model.params['W']))}
     row.update({f'W_gradient_row_{i}_l2':float(np.linalg.norm(grad['W'][i])) for i in range(9)});update_rows.append(row)
     if j+1 in CFG['optimization']['checkpoints']:last=checkpoint(j+1)
    final.append(last)
    for name in words:predictions[f'{arm}_{seed}_{name}']=model.predict(x[name])
  savecsv(out/'updates.csv',update_rows);savecsv(out/'checkpoint_metrics.csv',checkpoint_rows);savecsv(out/'final_metrics.csv',final);np.savez_compressed(out/'final_predictions.npz',**predictions)
  screens=[]
  for seed in CFG['initialization_seeds']:
   a=next(r for r in final if r['arm']=='corrected' and r['seed']==seed);b=next(r for r in final if r['arm']=='rare_boost' and r['seed']==seed)
   screens.append({'seed':seed,'structural_novel_error_ratio':b['structural_novel_mean_abs_error']/a['structural_novel_mean_abs_error'],'natural_KL_increase':b['natural_mean_KL']-a['natural_mean_KL'],'collision_max_error':b['collision_max_abs_error'],'pass':bool(b['structural_novel_mean_abs_error']<=.8*a['structural_novel_mean_abs_error'] and b['natural_mean_KL']-a['natural_mean_KL']<=.002 and b['collision_max_abs_error']<=.05)})
  dump(out/'results.json',{'status':'SIX_FITS_COMPLETE_NOT_INDEPENDENTLY_REVIEWED','sealed_inputs':sealdata,'environment':{'python':sys.version,'numpy':np.__version__,'platform':platform.platform(),'blas_threads':1},'seconds':time.perf_counter()-start,'screen':screens,'screen_all_pass':all(x['pass'] for x in screens),'final_metrics':final})
  dump(out/'ARTIFACT_HASHES.json',{str(f.relative_to(out)):sha(f) for f in sorted(out.rglob('*')) if f.is_file()});print(json.dumps({'status':'done','screen':screens}),flush=True)
 except Exception as e:
  dump(out/'FAILURE.json',{'error':str(e),'type':type(e).__name__,'traceback':traceback.format_exc(),'elapsed_seconds':time.perf_counter()-start});raise
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('command',choices=['seal','run']);p.add_argument('--output',default='ablation_v1');a=p.parse_args();seal() if a.command=='seal' else run(a.output)
