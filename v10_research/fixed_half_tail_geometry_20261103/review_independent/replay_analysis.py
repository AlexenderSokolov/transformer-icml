#!/usr/bin/env python3
"""Frozen-data / fixed-checkpoint descriptive diagnostics. No model fitting."""
from pathlib import Path
import sys, json, hashlib
from collections import Counter
import numpy as np
P=Path(__file__).resolve().parent.parent
SRC=P.parent/'readout_conditioning_calibration_20261103'
sys.path.insert(0,str(SRC))
import calibration as c
D=np.load(SRC/'calibration_v1/frozen_data.npz'); PRED=np.load(SRC/'calibration_v1/final_predictions.npz')

def keyed(words):
 x=c.features(words,'half_count_scaled')*c.SCALE
 return np.rint(x[:,:8]).astype(int) # first six count coordinates, then endpoint

def summary(words):
 s=c.literal_statistics(words)
 X=keyed(words)
 return [(int(r[0]),int(r[1]),int(r[2]),int(2*words[i,-2]+words[i,-1])) for i,r in enumerate(np.column_stack([s['J'],s['C'],s['D']]))],X,s

def ser(t):return [int(a) for a in t]
train_keys, tx, ts=summary(D['train_words']); val_keys,vx,vs=summary(D['validation_words']); col_keys,cx,cs=summary(D['collision_words'])
train_features=Counter(map(tuple,tx)); val_features=Counter(map(tuple,vx)); train_stat=Counter(train_keys); val_stat=Counter(val_keys)
all_features={}
for label,words in [('train',D['train_words']),('validation',D['validation_words']),('collision',D['collision_words']),('boundary',D['boundary_words'])]:
 keys,x,s=summary(words)
 for k,q in zip(map(tuple,x),s['Q']):all_features.setdefault(k,set()).add(float(q))
conflicts=[(k,v) for k,v in all_features.items() if len(v)>1]
res={'scope':'Frozen data and retained checkpoints only. No training, selected new words or claims about all-source risks.', 'input_hashes':{},'feature_conflicts_among_frozen':len(conflicts),'unique_feature_vectors':len(all_features),'train_stat_J_le_2':{},'val_stat_J_le_2':{},'models':{},'worst_word':{},'all_word_geometry':'For M=64, J in {0,...,64}, D is integer, D<=J. Therefore J>0 and 512D>=J iff D>=1. The first six feature counts give J and C and D exactly; endpoint first bit F is coordinate 7 (one-indexed). Q=0.125+0.75*(C/J if D>=1 else F), proving no feature collisions with different Q on all valid words.'}
for f in [SRC/'calibration.py',SRC/'calibration_v1/frozen_data.npz',SRC/'calibration_v1/final_predictions.npz']:
 res['input_hashes'][str(f.relative_to(P.parent.parent))]=hashlib.sha256(f.read_bytes()).hexdigest()
for name,ct in [('train_stat_J_le_2',train_stat),('val_stat_J_le_2',val_stat)]:
 res[name]={str(k):v for k,v in sorted(ct.items()) if k[0]<=2}
# nearest training/collision rows measured in count-coordinate Euclidean and L1 metrics, same endpoints
idx=1242; x=vx[idx]; word=D['validation_words'][idx]; mask=np.all(tx[:,6:8]==x[6:8],axis=1); inds=np.where(mask)[0]
d=np.abs(tx[inds,:6]-x[:6]); L1=d.sum(axis=1); near=inds[np.argsort(L1,kind='stable')[:10]]
res['worst_word']={'index':idx,'word':''.join(map(str,word)),'features_count':ser(x),'stat_J_C_D_U':ser(val_keys[idx]),'Q':float(vs['Q'][idx]),'identical_train_full_feature_count':train_features[tuple(x)],'identical_train_stat_count':train_stat[val_keys[idx]],'closest_training_same_endpoint':[{'index':int(i),'L1_count_6':int(np.abs(tx[i,:6]-x[:6]).sum()),'features_count':ser(tx[i]),'stat_J_C_D_U':ser(train_keys[i]),'Q':float(ts['Q'][i])} for i in near], 'collision_features':[{'features_count':ser(cx[i]),'stat_J_C_D_U':ser(col_keys[i]),'Q':float(cs['Q'][i])} for i in range(4)]}
for seed in [20261103201,20261103202,20261103203]:
 pred=PRED[f'half_count_scaled_{seed}_validation']; err=np.abs(pred-vs['Q']); tail=np.where(err>.1)[0]; ordered=np.argsort(-err)
 res['models'][str(seed)]={'mean_abs_error':float(err.mean()),'median_abs_error':float(np.median(err)),'max_abs_error':float(err.max()),'over_0_1_count':len(tail),'over_0_1_J_count':dict(Counter(map(int,vs['J'][tail]))),'over_0_1_D_count':dict(Counter(map(int,vs['D'][tail]))),'over_0_1_unrepresented_full_feature_count':sum(tuple(vx[i]) not in train_features for i in tail),'over_0_1_unrepresented_stat_count':sum(val_keys[i] not in train_stat for i in tail),'over_0_1_in_sample_collision_stat_count':sum(val_keys[i] in col_keys for i in tail),'top_20':[{'index':int(i),'Q':float(vs['Q'][i]),'pred':float(pred[i]),'error':float(err[i]),'J_C_D_U':ser(val_keys[i]),'features_count':ser(vx[i]),'train_identical_feature_count':train_features[tuple(vx[i])], 'train_identical_stat_count':train_stat[val_keys[i]]} for i in ordered[:20]]}
(Path(__file__).resolve().parent/'REPLAY_RESULTS.json').write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
print(json.dumps({'unique_features':res['unique_feature_vectors'],'conflicts':len(conflicts),'worst_word':res['worst_word'],'tail_summary':{k:{a:b for a,b in v.items() if a!='top_20'} for k,v in res['models'].items()}},indent=2))
# Further retained-checkpoint statistics; zero updates or selection.
for seed in [20261103201,20261103202,20261103203]:
 pred=PRED[f'half_count_scaled_{seed}_validation']; tr=PRED[f'half_count_scaled_{seed}_train']
 err=np.abs(pred-vs['Q']); te=np.abs(tr-ts['Q']); losses=c.kl(vs['Q'],pred); tail=err>.1
 res['models'][str(seed)].update({'validation_total_KL_sum':float(losses.sum()),'validation_tail_KL_sum':float(losses[tail].sum()),'worst_word_KL':float(losses[1242]),'train_over_0_1_count':int((te>.1).sum()),'train_max_error':float(te.max()),'nearest_train_predictions':[{'index':int(j),'Q':float(ts['Q'][j]),'prediction':float(tr[j])} for j in [797,1885,177,376,464,1764]],'validation_tail_with_identical_train_full_feature':[{'validation_index':int(j),'matching_train_indices':np.flatnonzero(np.all(tx==vx[j],axis=1)).tolist(),'Q':float(vs['Q'][j]),'prediction':float(pred[j])} for j in np.where(tail)[0] if tuple(vx[j]) in train_features]})
(Path(__file__).resolve().parent/'REPLAY_RESULTS.json').write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
print('ADDITIONAL_DIAGNOSTICS')
print(json.dumps({k:{a:b for a,b in v.items() if a in ['validation_total_KL_sum','validation_tail_KL_sum','worst_word_KL','train_over_0_1_count','train_max_error','nearest_train_predictions','validation_tail_with_identical_train_full_feature']} for k,v in res['models'].items()},indent=2))
for seed in [20261103201,20261103202,20261103203]:
 tr=PRED[f'half_count_scaled_{seed}_train'];te=np.abs(tr-ts['Q']); top=int(np.argmax(te))
 paths={}
 for split,i,x,q in [('shared_validation_worst',1242,vx[1242],vs['Q'][1242]),('nearest_training_797',797,tx[797],ts['Q'][797]),('training_worst',top,tx[top],ts['Q'][top])]:
  # first six are scaled counts, two terminal coordinates, last fixed coordinate is 1/64.
  xx=np.r_[x,1/64]
  rows=[]
  for step in [0,200,1000,2000]:
   z=np.load(SRC/f'calibration_v1/checkpoints/half_count_scaled_{seed}_step{step}.npz')
   h=np.tanh(xx@z['W']+z['b']);sig=1/(1+np.exp(-(h@z['v']+z['c'][0])));eps=1/66**2;out=eps+(1-2*eps)*sig
   rows.append({'step':step,'prediction':float(out),'fraction_hidden_abs_gt_0_99':float(np.mean(np.abs(h)>.99))})
  paths[split]={'index':int(i),'Q':float(q),'features_count':ser(x),'stat_J_C_D_U':ser(val_keys[i] if split=='shared_validation_worst' else train_keys[i]),'minibatch_index_draws':None if split=='shared_validation_worst' else int((D['prior_batch_indices']==i).sum()),'checkpoint_predictions':rows}
 res['models'][str(seed)]['selected_trajectory_diagnostics']=paths
(Path(__file__).resolve().parent/'REPLAY_RESULTS.json').write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
print('CHECKPOINT_TRAJECTORIES')
print(json.dumps({k:v['selected_trajectory_diagnostics'] for k,v in res['models'].items()},indent=2))
