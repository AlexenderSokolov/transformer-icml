import numpy as np,hashlib,json,csv
from pathlib import Path
root=Path(__file__).resolve().parents[2];base=root/'rare_weight_ablation_20261103'; src=base/'ablation_v1'; data=np.load(src/'frozen_data.npz'); preds=np.load(src/'final_predictions.npz'); pre=json.load(open(src/'pre_fit_checks.json')); results=json.load(open(src/'results.json'))
def stats(w):
 n=len(w);u=2*w[:,-2]+w[:,-1];a=np.zeros((n,2,2),int)
 for i in range(64):
  m=2*w[:,i]+w[:,i+1]==u;np.add.at(a,(np.arange(n)[m],np.full(n,i//32)[m],w[m,i+2]),1)
 j=a.sum((1,2));c=a[:,:,1].sum(1);d=a[:,0,:].sum(1);f=w[:,-2];q=.125+.75*np.where(d>0,np.divide(c,j,out=np.zeros(n),where=j>0),f); x=np.column_stack([a[:,:,0].sum(1),c,a[:,0,:],a[:,1,:],w[:,-2:],np.full(n,1/64)]);return np.column_stack([j,c,d,u]),q,x
collision={(1,0,0,2),(1,0,1,2),(1,1,0,1),(1,1,1,1)}
def isheld(k):
 k=tuple(int(a) for a in k)
 return k not in collision and int.from_bytes(hashlib.sha256(('v10-rare-split-20261103:'+','.join(map(str,k))).encode()).digest(),'big')%5==0
def gen(n,rng):
 p=rng.random((n,4));starts=rng.integers(0,4,n);w=np.empty((n,66),np.int8);w[:,0]=starts//2;w[:,1]=starts%2
 for i in range(64):w[:,i+2]=rng.random(n)<p[np.arange(n),2*w[:,i]+w[:,i+1]]
 return w
for label,seed,ntake in [('train',20261103301,2048),('rare_heldout',20261103303,1024)]:
 rng=np.random.default_rng(seed);sel=[];accepted=0;drawn=0
 while accepted<ntake:
  w=gen(8192,rng);g,_,_=stats(w);hold=np.array([isheld(k) for k in g]); rare=(g[:,0]<=6)|(g[:,2]==0);mask=~hold if label=='train' else (hold&rare);sel.append(w[mask]);accepted+=int(mask.sum());drawn+=len(w)
 print(label,'reconstruction matches',np.array_equal(np.concatenate(sel)[:ntake],data[label+'_words']),'drawn',drawn,'accepted before truncation',accepted,'rejected',drawn-accepted,'accepted discarded',accepted-ntake)
w=gen(8192,np.random.default_rng(20261103302));print('natural reconstruction matches',np.array_equal(w,data['natural_words']))
sets={};max_y=0
for name in ['train','natural','rare_heldout','collision','structural_heldout','structural_novel']:
 k,y,x=stats(data[name+'_words']);sets[name]=(k,y,x);max_y=max(max_y,float(np.max(abs(y-data[name+'_Q']))));print(name,'n',len(y),'groups',len(set(map(tuple,k))),'hold groups',sum(isheld(kk) for kk in k))
print('max teacher discrepancy',max_y)
tk=sets['train'][0];hk=sets['rare_heldout'][0];sk=sets['structural_heldout'][0];ck=sets['collision'][0];nk=sets['structural_novel'][0];old=np.load(root/'readout_conditioning_calibration_20261103/calibration_v1/frozen_data.npz');oldg=set(map(tuple,stats(np.concatenate([old[n+'_words'] for n in ['train','validation','collision','boundary']]))[0]));print('group intersections',len(set(map(tuple,tk))&set(map(tuple,hk))),len(set(map(tuple,tk))&set(map(tuple,sk))),'novel groups old intersection',len(set(map(tuple,nk))&oldg));print('saved collision unique groups',set(map(tuple,ck)))
rare=(tk[:,0]<=6)|(tk[:,2]==0);R=np.where(rare)[0];N=np.where(~rare)[0];p=len(R)/len(tk);rng=np.random.default_rng(20261103304);irs=[];ins=[];ics=[]
for i in range(2000):irs.append(rng.choice(R,32));ins.append(rng.choice(N,32));ics.append(rng.integers(0,4,64))
print('p',p,'stream matches',np.array_equal(irs,data['prior_rare_indices']),np.array_equal(ins,data['prior_nonrare_indices']),np.array_equal(ics,data['collision_indices']))
rows=list(csv.DictReader(open(src/'checkpoint_metrics.csv')));maxerr=0
for r in rows:
 arm=r['arm'];seed=r['seed'];step=r['step'];z=np.load(src/'checkpoints'/f'{arm}_{seed}_step{step}.npz')
 for name in ['natural','rare_heldout','collision','structural_heldout','structural_novel','train_rare','train_nonrare']:
  basekey='train' if name.startswith('train_') else name;k,y,x=sets[basekey]
  if name.startswith('train_'):
   m=rare if name=='train_rare' else ~rare;y=y[m];x=x[m]
  h=np.tanh(x@z['W']+z['b']);v=h@z['v']+z['c'][0];q=1/66**2+(1-2/66**2)/(1+np.exp(-v));err=abs(y-q);kl=y*np.log(y/q)+(1-y)*np.log((1-y)/(1-q));expected=[kl.mean(),err.mean(),np.quantile(err,.95),err.max(),np.sum(err>.1)];actual=[float(r[name+'_'+c]) for c in ['mean_KL','mean_abs_error','q95_abs_error','max_abs_error','count_over_0_1']];maxerr=max(maxerr,float(np.max(abs(np.array(expected)-actual))))
  if step=='2000' and not name.startswith('train_'):maxerr=max(maxerr,float(np.max(abs(q-preds[f'{arm}_{seed}_{name}']))))
print('checkpoint rows',len(rows),'max checkpoint/prediction metric discrepancy',maxerr)
for seed in [20261103201,20261103202,20261103203]:
 z1=np.load(src/'checkpoints'/f'corrected_{seed}_step0.npz');z2=np.load(src/'checkpoints'/f'rare_boost_{seed}_step0.npz'); print('initial weights equal',seed,all(np.array_equal(z1[k],z2[k]) for k in z1.files))
 y=sets['natural'][1];a=preds[f'corrected_{seed}_natural'];b=preds[f'rare_boost_{seed}_natural'];kl=lambda q:y*np.log(y/q)+(1-y)*np.log((1-y)/(1-q));delta=kl(b)-kl(a);print('natural KL paired mean,SE',seed,delta.mean(),delta.std(ddof=1)/np.sqrt(len(delta)),'MAE change',np.mean(abs(b-y))-np.mean(abs(a-y)))
for file in ['PRE_RUN_HASHES.json','ablation_v1/ARTIFACT_HASHES.json']:
 record=json.load(open(base/file));mapping=record['files'] if 'files' in record else record;path=root.parent if file=='PRE_RUN_HASHES.json' else src;bad=[name for name,digest in mapping.items() if not (path/name).exists() or hashlib.sha256((path/name).read_bytes()).hexdigest()!=digest];print(file,'num',len(mapping),'bad',bad)
# Independently calculate the first weighted CE and its gradient for each initial checkpoint.
updates=list(csv.DictReader(open(src/'updates.csv'))); lookup={(r['arm'],r['seed'],r['step']):r for r in updates}; print('updates rows',len(updates)); max_obj_err=max_grad_err=0
for seed in [20261103201,20261103202,20261103203]:
 for arm in ['corrected','rare_boost']:
  z=np.load(src/'checkpoints'/f'{arm}_{seed}_step0.npz');grads={k:np.zeros_like(z[k]) for k in ['W','b','v','c']};obj=0
  indices=[data['prior_rare_indices'][0],data['prior_nonrare_indices'][0],data['collision_indices'][0]]; weights=[p*.5,(1-p)*.5,.5] if arm=='corrected' else [.25,.25,.5]
  for group,idx,wt in zip(['train','train','collision'],indices,weights):
   y=sets[group][1][idx];x=sets[group][2][idx]; h=np.tanh(x@z['W']+z['b']);sig=1/(1+np.exp(-(h@z['v']+z['c'][0])));ep=1/66**2;q=ep+(1-2*ep)*sig;obj+=wt*np.mean(-y*np.log(q)-(1-y)*np.log1p(-q));dl=wt/len(y)*(q-y)/(q*(1-q))*(1-2*ep)*sig*(1-sig);dh=dl[:,None]*z['v'][None,:]*(1-h*h);grads['W']+=x.T@dh;grads['b']+=dh.sum(0);grads['v']+=h.T@dl;grads['c']+=np.array([dl.sum()])
  gnorm=np.sqrt(sum(np.sum(g*g) for g in grads.values())); r=lookup[(arm,str(seed),'1')];max_obj_err=max(max_obj_err,abs(obj-float(r['weighted_CE'])));max_grad_err=max(max_grad_err,abs(gnorm-float(r['gradient_l2'])))
print('first-step weighted objectives max err',max_obj_err,'gradient norms max err',max_grad_err)
for seed in [20261103201,20261103202,20261103203]:
 pair=[r for r in results['final_metrics'] if r['seed']==seed]; print('seed',seed,*[(r['arm'],'novel_mae',r['structural_novel_mean_abs_error'],'fullstruct_max',r['structural_heldout_max_abs_error'],'held_mae',r['rare_heldout_mean_abs_error'],'natural_mae',r['natural_mean_abs_error'],'natural_kl',r['natural_mean_KL']) for r in pair])
trainpredmax=0
for arm in ['corrected','rare_boost']:
 for seed in [20261103201,20261103202,20261103203]:
  z=np.load(src/'checkpoints'/f'{arm}_{seed}_step2000.npz');x=sets['train'][2];v=np.tanh(x@z['W']+z['b'])@z['v']+z['c'][0];q=1/66**2+(1-2/66**2)/(1+np.exp(-v));trainpredmax=max(trainpredmax,float(np.max(abs(q-preds[f'{arm}_{seed}_train']))))
print('final training predictions max discrepancy',trainpredmax)
