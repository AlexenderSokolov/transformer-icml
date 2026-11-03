import numpy as np,hashlib,json,csv
from pathlib import Path
R=Path(__file__).resolve().parents[2];B=R/'rare_weight_confirmation_20261103';O=B/'confirmation_v1';D=np.load(O/'frozen_data.npz');P=np.load(O/'final_predictions.npz');cfg=json.load(open(B/'protocol.json'))
def calc(w):
 n=len(w);u=2*w[:,-2]+w[:,-1];a=np.zeros((n,2,2),int)
 for i in range(64):
  m=2*w[:,i]+w[:,i+1]==u;np.add.at(a,(np.arange(n)[m],np.full(n,i//32)[m],w[m,i+2]),1)
 j=a.sum((1,2));c=a[:,:,1].sum(1);d=a[:,0,:].sum(1);q=.125+.75*np.where(d>0,np.divide(c,j,out=np.zeros(n),where=j>0),w[:,-2]);x=np.column_stack([a[:,:,0].sum(1),c,a[:,0,:],a[:,1,:],w[:,-2:],np.full(n,1/64)]);return np.column_stack([j,c,d,u]),q,x
oldgroups=set()
for name in ['readout_conditioning_calibration_20261103/calibration_v1/frozen_data.npz','rare_weight_ablation_20261103/ablation_v1/frozen_data.npz']:
 z=np.load(R/name)
 for k in z.files:
  if k.endswith('_words'):oldgroups.update(map(tuple,calc(z[k])[0]))
rows=json.load(open(R/'rare_state_enumeration_20261103/rare_states.json'))['rows'];struct=np.array([[int(c) for c in r['word']] for r in rows],np.int8);structg=calc(struct)[0];reserve=set(tuple(k) for k in structg if tuple(k) not in oldgroups); print('reserve groups',len(reserve),'vectors',sum(tuple(k) in reserve for k in structg))
collision={(1,0,0,2),(1,0,1,2),(1,1,0,1),(1,1,1,1)}
def held(k):
 k=tuple(int(v) for v in k);return k in reserve or (k not in collision and int.from_bytes(hashlib.sha256(('v10-rare-split-20261103:'+','.join(map(str,k))).encode()).digest(),'big')%5==0)
sets={}
for label,seed,key,n in [('train',20261103501,'train',2048),('natural',20261103502,'natural',8192),('hold',20261103503,'rare_heldout',1024)]:
 path=O/'candidate_batches'/label; files=sorted(path.glob('batch_*.npz')); intents=sorted(path.glob('*.intent.json')); assert len(files)==len(intents)>0;rng=np.random.default_rng(seed);chosen=[];accepted=0;drawn=0
 for i,(file,intentp) in enumerate(zip(files,intents)):
  z=np.load(file);intent=json.load(open(intentp));n0=len(z['words']);before=json.dumps(rng.bit_generator.state,sort_keys=True);assert json.loads(before)==intent['rng_before'] and str(z['rng_before'])==before and intent['batch_index']==i and intent['set']==label
  p=rng.random((n0,4));initial=rng.integers(0,4,n0);unif=np.stack([rng.random(n0) for _ in range(64)]);assert np.array_equal(p,z['probabilities']) and np.array_equal(initial,z['starts']) and np.array_equal(unif,z['uniforms']) and str(z['rng_after'])==json.dumps(rng.bit_generator.state,sort_keys=True)
  w=np.empty((n0,66),np.int8);w[:,0]=initial//2;w[:,1]=initial%2
  for j in range(64):w[:,j+2]=unif[j]<p[np.arange(n0),2*w[:,j]+w[:,j+1]]
  assert np.array_equal(w,z['words']);k,_,_=calc(w);h=np.array([held(v) for v in k]);rr=(k[:,0]<=6)|(k[:,2]==0);eligible=np.ones(n0,bool) if label=='natural' else (~h if label=='train' else h&rr); sel=np.zeros(n0,bool);ind=np.flatnonzero(eligible);sel[ind[:max(0,n-accepted)]]=True; assert np.array_equal(eligible,z['eligible']) and np.array_equal(sel,z['selected']) and int(z['global_candidate_start'])==drawn
  accepted+=sum(eligible);drawn+=n0;chosen.append(w[sel])
 assert np.array_equal(np.concatenate(chosen),D[key+'_words']);print(label,'batches',len(files),'drawn',drawn,'eligible',accepted,'selected',n,'all raw/seed/flags verified')
for name in ['train','natural','rare_heldout','collision','structural_heldout','structural_previous8','structural_unseen20']:
 k,y,x=calc(D[name+'_words']);assert np.array_equal(y,D[name+'_Q']);sets[name]=(k,y,x);print(name,'n',len(y),'groups',len(set(map(tuple,k))),'hold count',sum(held(v) for v in k))
tr=sets['train'][0];th=set(map(tuple,np.concatenate([tr,sets['collision'][0]])));hh=set(map(tuple,sets['rare_heldout'][0]));s20=set(map(tuple,sets['structural_unseen20'][0]));assert not(th&hh) and not(th&s20) and not(oldgroups&s20) and s20==reserve;print('group exclusions verified')
rare=(tr[:,0]<=6)|(tr[:,2]==0);p=rare.mean();rng=np.random.default_rng(20261103504);assert str(D['minibatch_rng_before'])==json.dumps(rng.bit_generator.state,sort_keys=True);ir=[];inn=[];ic=[]
for i in range(2000):ir.append(rng.choice(np.where(rare)[0],32));inn.append(rng.choice(np.where(~rare)[0],32));ic.append(rng.integers(0,4,64))
assert np.array_equal(ir,D['prior_rare_indices']) and np.array_equal(inn,D['prior_nonrare_indices']) and np.array_equal(ic,D['collision_indices']) and str(D['minibatch_rng_after'])==json.dumps(rng.bit_generator.state,sort_keys=True);print('minibatch RNG verified p',p)
rows=list(csv.DictReader(open(O/'checkpoint_metrics.csv')));errmax=0
for r in rows:
 arm=r['arm'];seed=r['seed'];step=r['step'];z=np.load(O/'checkpoints'/f'{arm}_{seed}_step{step}.npz')
 for name in ['natural','rare_heldout','collision','structural_heldout','structural_previous8','structural_unseen20','train_rare','train_nonrare']:
  source='train' if name.startswith('train_') else name;k,y,x=sets[source]
  if name.startswith('train_'):m=rare if name=='train_rare' else ~rare;y=y[m];x=x[m]
  h=np.tanh(x@z['param_W']+z['param_b']);v=h@z['param_v']+z['param_c'][0];q=1/66**2+(1-2/66**2)/(1+np.exp(-v));e=abs(y-q);kl=y*np.log(y/q)+(1-y)*np.log((1-y)/(1-q)); exp=[len(y),kl.mean(),e.mean(),np.quantile(e,.95),e.max(),sum(e>.1)];act=[float(r[name+'_'+j]) for j in ['n','mean_KL','mean_abs_error','q95_abs_error','max_abs_error','count_over_0_1']];errmax=max(errmax,float(np.max(abs(np.array(exp)-act))))
  if step=='2000' and not name.startswith('train_'):errmax=max(errmax,float(np.max(abs(q-P[f'{arm}_{seed}_{name}']))))
print('checkpoint metric rows',len(rows),'max discrepancy',errmax)
for file,path in [('PRE_RUN_HASHES.json',R.parent),('REVIEW_AND_RUN_APPROVAL.json',R.parent),('confirmation_v1/ARTIFACT_HASHES.json',O)]:
 rec=json.load(open(B/file));h=rec.get('files',rec);bad=[x for x,v in h.items() if not (path/x).is_file() or hashlib.sha256((path/x).read_bytes()).hexdigest()!=v];print(file,'count',len(h),'bad',bad)
review=B/'independent_review_20261103';marker=json.load(open(B/'REVIEW_AND_RUN_APPROVAL.json'));print('review markers match',hashlib.sha256((review/'REVIEW.md').read_bytes()).hexdigest()==marker['review_sha256'],hashlib.sha256((review/'REVIEW_INPUT_HASHES.json').read_bytes()).hexdigest()==marker['review_input_manifest_sha256'])
for seed in [20261103601,20261103602,20261103603]:
 a=next(r for r in rows if r['arm']=='corrected' and int(r['seed'])==seed and r['step']=='2000');b=next(r for r in rows if r['arm']=='rare_boost' and int(r['seed'])==seed and r['step']=='2000');print('seed',seed,'primary ratio',float(b['rare_heldout_mean_abs_error'])/float(a['rare_heldout_mean_abs_error']),'natural_KL_diff',float(b['natural_mean_KL'])-float(a['natural_mean_KL']),'natural_MAE_diff',float(b['natural_mean_abs_error'])-float(a['natural_mean_abs_error']),'reserve20_mean_corr_boost',a['structural_unseen20_mean_abs_error'],b['structural_unseen20_mean_abs_error'],'reserve20_max_corr_boost',a['structural_unseen20_max_abs_error'],b['structural_unseen20_max_abs_error'])
