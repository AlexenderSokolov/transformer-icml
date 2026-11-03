from pathlib import Path
import numpy as np,csv,hashlib,json
B=Path(__file__).resolve().parent.parent; A=B/'calibration_v1'; R=B/'review_independent'/'replay';f=np.load(A/'frozen_data.npz'); preds=np.load(A/'final_predictions.npz')
def oracle(w,kind):
 w=np.asarray(w);n=len(w);U=2*w[:,64]+w[:,65];triple=np.zeros((n,4,2),int);D=np.zeros(n,int)
 for i in range(64):
  j=2*w[:,i]+w[:,i+1];np.add.at(triple,(np.arange(n),j,w[:,i+2]),1);D+=(i<32)&(j==U)
 sub=triple[np.arange(n),U];J=sub.sum(axis=1);C=sub[:,1];a=np.divide(C,J,out=np.zeros(n,float),where=J>0);gate=(J>0)&(512*D>=J);teacher=.75*np.where(gate,a,w[:,-2])+.125
 e=np.stack([(2*w[:,i]+w[:,i+1]==U)[:,None]*(np.stack([1-w[:,i+2],w[:,i+2]],axis=1)) for i in range(64)],axis=1);full=e.mean(axis=1);first=e[:,:32].mean(axis=1);last=e[:,32:].mean(axis=1)
 if kind=='uniform_control':first=last=full
 x=np.column_stack([full,first,last,w[:,-2:],np.full(n,1/64)])
 return triple,J,C,D,teacher,x
for split in ['train','validation','collision','boundary']:
 h,j,c,d,y,x=oracle(f[split+'_words'],'half_normalized'); print(split,'teacher_max_diff',np.max(abs(y-f[split+'_Q'])),'n',len(y));
 if split in ('collision','boundary'):print(split,'J,C,D,Q',list(zip(j.tolist(),c.tolist(),d.tolist(),y.tolist())),'H0',h[0].reshape(-1).tolist())
# Validate PCG data independently by rebuilding calls and transitions.
for split,seed in [('train',20261103204),('validation',20261103205)]:
 rng=np.random.default_rng(seed);n=2048;p=rng.random((n,4));s=rng.integers(0,4,n);w=np.empty((n,66),np.int8);w[:,0]=s//2;w[:,1]=s%2
 for i in range(64):w[:,i+2]=rng.random(n)<p[np.arange(n),2*w[:,i]+w[:,i+1]]
 print(split,'independent_rng_rebuild',np.array_equal(w,f[split+'_words']))
rng=np.random.default_rng(20261103206);ip=[];ic=[]
for _ in range(2000):ip.append(rng.integers(0,2048,64));ic.append(rng.integers(0,4,64))
print('minibatches rebuild',np.array_equal(ip,f['prior_batch_indices']),np.array_equal(ic,f['collision_batch_indices']))
a={bytes(x) for x in f['train_words']};b={bytes(x) for x in f['validation_words']};print('train validation distinct exact word overlap',len(a&b),'unique train',len(a),'unique validation',len(b));print('collision exact overlap train/validation',len(a&{bytes(x) for x in f['collision_words']}),len(b&{bytes(x) for x in f['collision_words']}))
records=list(csv.DictReader(open(A/'checkpoint_metrics.csv')));worst=0;maxinit=0
for row in records:
 name=row['condition'];seed=row['seed'];step=row['step'];ck=np.load(A/'checkpoints'/f'{name}_{seed}_step{step}.npz');
 for split in ['train','validation','collision','boundary']:
  h,j,c,d,y,x=oracle(f[split+'_words'],name);xs=x*ck['scale'];z=np.tanh(xs@ck['W']+ck['b'])@ck['v']+ck['c'][0];q=(1/66**2)+(1-2/66**2)/(1+np.exp(-z));
  if step=='2000':worst=max(worst,float(np.max(abs(q-preds[f'{name}_{seed}_{split}']))))
  kl=y*np.log(y/q)+(1-y)*np.log((1-y)/(1-q))
  if split in ['train','validation']:
   worst=max(worst,abs(kl.mean()-float(row[split+'_prior_KL'])),abs(kl.std(ddof=1)/len(y)**.5-float(row[split+'_prior_KL_MC_SE'])))
  if split=='collision':worst=max(worst,abs(kl.mean()-float(row['validation_collision_KL'])),abs(np.max(abs(q-y))-float(row['validation_collision_max_abs_error'])))
  if split=='boundary':worst=max(worst,abs(np.max(abs(q-y))-float(row['boundary_max_abs_error'])))
print('all checkpoints 36 independently recomputed max diff',worst)
for seed in [20261103201,20261103202,20261103203]:
 a=np.load(A/'checkpoints'/f'half_normalized_{seed}_step0.npz');b=np.load(A/'checkpoints'/f'half_count_scaled_{seed}_step0.npz');print('matched init effective W maxdiff',seed,np.max(abs(a['W']-b['W']*b['scale'][:,None])))
for seed in [20261103201,20261103202,20261103203]:
 name='half_count_scaled';q=preds[f'{name}_{seed}_validation'];y=f['validation_Q'];ab=abs(q-y);print('scaled holdout abs error',seed,'max',ab.max(),'over .05',np.count_nonzero(ab>.05),'over .1',np.count_nonzero(ab>.1),'over .25',np.count_nonzero(ab>.25))
manifest=json.loads((A/'ARTIFACT_HASHES.json').read_text());print('hash check',len(manifest),'bad',sum(hashlib.sha256((A/k).read_bytes()).hexdigest()!=v for k,v in manifest.items()))
if R.exists() and (R/'final_predictions.npz').exists():
 for file in ['frozen_data.npz','final_predictions.npz']:
  x=np.load(A/file);y=np.load(R/file);print('replay',file,'equal',set(x.files)==set(y.files) and all(np.array_equal(x[k],y[k]) for k in x.files))
