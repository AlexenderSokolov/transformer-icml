#!/usr/bin/env python3
"""Independently decode literal saved binary words and retained final checkpoints."""
from pathlib import Path
from collections import defaultdict
import json, numpy as np
P=Path(__file__).resolve().parent;S=P.parent/'readout_conditioning_calibration_20261103';d=np.load(S/'calibration_v1/frozen_data.npz');p=np.load(S/'calibration_v1/final_predictions.npz')
features=[];qs=[]; groups={}
for split in ['train','validation','collision','boundary']:
 words=d[split+'_words'];x=[];truth=[]
 for w in words:
  U=tuple(int(a) for a in w[-2:]); a=np.zeros((2,2),int)
  for i in range(64):
   if tuple(int(t) for t in w[i:i+2])==U:a[int(i>=32),int(w[i+2])]+=1
  j=int(a.sum()); C=int(a[:,1].sum()); D=int(a[0].sum()); F=U[0]
  assert 0<=D<=j<=64 and ((j>0 and 512*D>=j)==(D>0))
  q=.125+.75*(C/j if D>0 else F)
  truth.append(q);x.append([int(a[:,0].sum()),int(a[:,1].sum()),int(a[0,0]),int(a[0,1]),int(a[1,0]),int(a[1,1]),*U,1/64])
 x=np.asarray(x);truth=np.asarray(truth)
 assert np.allclose(truth,d[split+'_Q'],rtol=0,atol=0)
 for row,q in zip(x,truth):groups.setdefault(tuple(row),set()).add(q)
 features.append(len(words));qs.append(float(np.max(np.abs(truth-d[split+'_Q']))));
 for seed in [20261103201,20261103202,20261103203]:
  z=np.load(S/f'calibration_v1/checkpoints/half_count_scaled_{seed}_step2000.npz')
  logits=np.tanh(x@z['W']+z['b'])@z['v']+z['c'][0]; ss=1/(1+np.exp(-logits));epsilon=1/66**2
  out=epsilon+(1-2*epsilon)*ss
  assert np.allclose(out,p[f'half_count_scaled_{seed}_{split}'],rtol=0,atol=1e-14)
assert all(len(q)==1 for q in groups.values())
print(json.dumps({'independently_decoded_words':sum(features),'split_counts':features,'max_target_discrepancy':max(qs),'unique_feature_vectors':len(groups),'feature_Q_conflicts':sum(len(q)>1 for q in groups.values()),'all_final_scaled_predictions_reconstructed':True,'prediction_tolerance':1e-14,'gate_equivalence_checked_for_each_word':True,'scope':'finite tests complement the all-word proof, not a substitute for it'},indent=2))
