import json,csv,hashlib,sys,numpy as np
from pathlib import Path
B=Path(__file__).resolve().parent.parent; O=B/'confirmation_v1';sys.path.insert(0,str(B.parent/'readout_conditioning_calibration_20261103'));import calibration as c
D=np.load(O/'frozen_data.npz');P=np.load(O/'final_predictions.npz');C=list(csv.DictReader(open(O/'checkpoint_metrics.csv'))); F=list(csv.DictReader(open(O/'final_metrics.csv')));R=json.load(open(O/'results.json'));assert F==[x for x in C if x['step']=='2000']; assert len(F)==len(R['final_metrics'])==6 and all(all(str(v)==row.get(k) for k,v in x.items()) for x,row in zip(R['final_metrics'],F))
for seed in [20261103601,20261103602,20261103603]:
 a=np.load(O/'checkpoints'/f'corrected_{seed}_step0.npz');b=np.load(O/'checkpoints'/f'rare_boost_{seed}_step0.npz');mod=c.Readout(seed,'half_count_scaled');assert all(np.array_equal(a[k],b[k]) for k in a.files) and all(np.array_equal(a['param_'+k],v) for k,v in mod.params.items())
 for arm in ['corrected','rare_boost']:
  for step in [0,200,1000,2000]:
   z=np.load(O/'checkpoints'/f'{arm}_{seed}_step{step}.npz');assert int(z['optimizer_step'])==step and str(z['condition'])=='half_count_scaled' and np.array_equal(z['scale'],[64,64,32,32,32,32,1,1,1]);assert all(float(z[k])==v for k,v in [('readout_lr',.003),('pool_lr',.01),('beta1',.9),('beta2',.999),('epsilon',1e-8)])
 print('seed',seed,'paired and declared initialization, 8 full checkpoint hyperparameters verified')
 for typ in ['rare_heldout','natural']:
  y=D[typ+'_Q'];a=P[f'corrected_{seed}_{typ}'];b=P[f'rare_boost_{seed}_{typ}'];delta=abs(b-y)-abs(a-y);print(typ,'paired difference',delta.mean(),'MCSE',delta.std(ddof=1)/len(delta)**.5)
parsed=[]
for line in (B/'confirmation_console.log').read_text().splitlines():
 try:parsed.append(json.loads(line))
 except ValueError:pass
logs=[x for x in parsed if all(k in x for k in ['arm','seed','step'])];assert len(logs)==len(C)==24 and all(all(str(v)==row.get(k) for k,v in obj.items()) for obj,row in zip(logs,C));done=[x for x in parsed if x.get('status')=='done'];assert len(done)==1 and done[0]['screen']==R['screen'];print('console rows, results, final metrics verified; console sha256',hashlib.sha256((B/'confirmation_console.log').read_bytes()).hexdigest())
maxdiff=0.
for seed in [20261103601,20261103602,20261103603]:
 for arm in ['corrected','rare_boost']:
  z=np.load(O/'checkpoints'/f'{arm}_{seed}_step2000.npz');w=D['train_words'];u=2*w[:,-2]+w[:,-1];a=np.zeros((len(w),2,2),int)
  for i in range(64):
   m=2*w[:,i]+w[:,i+1]==u;np.add.at(a,(np.arange(len(w))[m],np.full(len(w),i//32)[m],w[m,i+2]),1)
  x=np.column_stack([a[:,:,0].sum(1),a[:,:,1].sum(1),a[:,0,:],a[:,1,:],w[:,-2:],np.full(len(w),1/64)]);h=np.tanh(x@z['param_W']+z['param_b']);v=h@z['param_v']+z['param_c'][0];q=1/66**2+(1-2/66**2)/(1+np.exp(-v));maxdiff=max(maxdiff,float(np.max(abs(q-P[f'{arm}_{seed}_train']))))
print('final training predictions max diff',maxdiff);assert maxdiff<1e-14
