"""Independent post-completion audit. Execute only after the run has stopped.

Reads retained arrays, deterministic PRNG states, checkpoints, and recorded
updates. It creates no new observations and performs no fit: calculated
gradients and Adam steps are compared with recorded values only.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse, csv, hashlib, json, math, struct
from functools import lru_cache
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
P=HERE.parent
ROOT=P.parent.parent
SCALE=np.array([64,64,32,32,32,32,1,1,1],dtype=np.float64)
EPS=1/66**2

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load_csv(p):
 with Path(p).open(newline='') as f:return list(csv.DictReader(f))
def approx(a,b,tol=5e-12):
 a=np.asarray(a);b=np.asarray(b)
 if a.shape!=b.shape:return False
 return bool(np.all(np.isfinite(a)) and np.all(np.isfinite(b)) and np.allclose(a,b,rtol=tol,atol=tol))
def close(a,b,tol=5e-12):
 assert approx(a,b,tol),f'mismatch: {a!r} vs {b!r}'

def stats(words):
 w=np.asarray(words,dtype=np.int64);assert w.ndim==2 and w.shape[1]==66 and np.isin(w,(0,1)).all()
 u=2*w[:,-2]+w[:,-1];pair=2*w[:,:64]+w[:,1:65];tail=w[:,2:66];same=pair==u[:,None]
 f=same[:,:32];l=same[:,32:];a0=(f*(1-tail[:,:32])).sum(1);a1=(f*tail[:,:32]).sum(1)
 b0=(l*(1-tail[:,32:])).sum(1);b1=(l*tail[:,32:]).sum(1)
 j=a0+a1+b0+b1;c=a1+b1;d=a0+a1
 q=.125+.75*np.where(d>0,np.divide(c,j,out=np.zeros_like(j,dtype=float),where=j>0),w[:,-2])
 x=np.column_stack(((a0+b0)/64,(a1+b1)/64,a0/32,a1/32,b0/32,b1/32,w[:,-2],w[:,-1],np.full(len(w),1/64)))
 return np.column_stack((j,c,d,u)),q,x

def wordset(w):return set(map(bytes,np.asarray(w,dtype=np.uint8)))
def keyset(g):return set(map(tuple,g))
def sigmoid(z):
 s=np.empty_like(z);pos=z>=0;s[pos]=1/(1+np.exp(-z[pos]));v=np.exp(z[~pos]);s[~pos]=v/(1+v);return s

def forward(x,p):
 s=sigmoid(np.tanh((x*SCALE)@p['W']+p['b'])@p['v']+p['c'][0]);return EPS+(1-2*EPS)*s

def loss_grad(x,y,p):
 xs=x*SCALE;h=np.tanh(xs@p['W']+p['b']);s=sigmoid(h@p['v']+p['c'][0]);q=EPS+(1-2*EPS)*s
 loss=np.mean(-y*np.log(q)-(1-y)*np.log1p(-q))
 d=((q-y)/(q*(1-q)))*(1-2*EPS)*s*(1-s)/len(y)
 dh=d[:,None]*p['v'][None,:]*(1-h*h)
 return float(loss),{'W':xs.T@dh,'b':dh.sum(0),'v':h.T@d,'c':np.array([d.sum()])}

def weighted_grad(data,p,rare_i,common_i,coll_i,frac,arm):
 x=data['train'][2];y=data['train'][1];cx=data['collision'][2];cy=data['collision'][1]
 chunks=[(x[rare_i],y[rare_i]),(x[common_i],y[common_i]),(cx[coll_i],cy[coll_i])]
 weights=[.5*frac,.5*(1-frac),.5] if arm=='corrected' else [.25,.25,.5]
 computed=[loss_grad(xx,yy,p) for xx,yy in chunks]
 return sum(w*r[0] for w,r in zip(weights,computed)),{k:sum(w*r[1][k] for w,r in zip(weights,computed)) for k in p}

def metrics(y,q):
 ae=np.abs(y-q);kl=y*np.log(y/q)+(1-y)*np.log((1-y)/(1-q))
 return dict(n=len(y),mean_KL=float(kl.mean()),mean_abs_error=float(ae.mean()),q95_abs_error=float(np.quantile(ae,.95)),max_abs_error=float(ae.max()),count_over_0_1=int(np.sum(ae>.1)))

def journal(path):
 header=struct.Struct('<8sQ32s')
 with Path(path).open('rb') as f:
  while True:
   where=f.tell();raw=f.read(header.size)
   if not raw:return
   assert len(raw)==header.size,('short journal header',where)
   magic,n,digest=header.unpack(raw);assert magic==b'RWUPD01!' and 0<n<=10_000_000
   payload=f.read(n);assert len(payload)==n and hashlib.sha256(payload).digest()==digest
   length=struct.unpack('<I',payload[:4])[0];meta=json.loads(payload[4:4+length]);blob=payload[4+length:]
   assert meta['version']==1 and meta['dtype']=='<f8' and meta['order']=='C' and meta['count']==353 and len(blob)==2*353*8
   names=meta['names'];shapes=meta['shapes'];assert names==sorted(shapes)
   nums=np.frombuffer(blob,dtype='<f8');offset=0;out=[]
   for _ in range(2):
    part={}
    for k in names:
     n=int(np.prod(shapes[k]));part[k]=nums[offset:offset+n].reshape(shapes[k]).copy();offset+=n
    out.append(part)
   assert offset==706 and all(np.isfinite(v).all() for part in out for v in part.values())
   yield meta,out[0],out[1]

def audit(run,console_file):
 assert run.is_dir() and (run/'results.json').is_file() and (run/'ARTIFACT_HASHES.json').is_file(),'run incomplete; do not audit until stopped'
 cfg=json.loads((P/'protocol.json').read_text());seedlist=cfg['initialization_seeds'];steps=cfg['optimization']['steps'];assert len(seedlist)==3 and steps==2000
 seal=json.loads((P/'PRE_RUN_HASHES.json').read_text());approval=json.loads((P/'REVIEW_AND_RUN_APPROVAL.json').read_text())
 assert approval['independent_review']=='approved' and approval['root_permission']=='approved' and approval['files']==seal['files']
 for k,v in seal['files'].items():assert sha(ROOT/k)==v,('sealed input changed',k)
 manifest=json.loads((run/'ARTIFACT_HASHES.json').read_text());actual={str(f.relative_to(run)) for f in run.rglob('*') if f.is_file()}-{'ARTIFACT_HASHES.json'}
 assert actual==set(manifest),(actual-set(manifest),set(manifest)-actual)
 for k,v in manifest.items():assert sha(run/k)==v,('artifact hash mismatch',k)
 report_bindings=json.loads((P/'RESULTS_BINDINGS.json').read_text())['files']
 for k,v in report_bindings.items():assert sha(ROOT/k)==v,('report binding mismatch',k)
 result=json.loads((run/'results.json').read_text());assert result['status']=='SIX_FITS_COMPLETE_NOT_INDEPENDENTLY_REVIEWED'
 checks=json.loads((run/'pre_fit_checks.json').read_text());assert checks['frozen_data_sha256']==sha(run/'frozen_data.npz')
 frozen=np.load(run/'frozen_data.npz',allow_pickle=False);saved=np.load(run/'final_predictions.npz',allow_pickle=False)
 names=('train','natural','rare_heldout','collision','structural_heldout','structural_previous8','structural_unseen20')
 words={k:frozen[k+'_words'] for k in names};data={k:stats(words[k]) for k in names}
 for k in names:
  assert np.array_equal(data[k][1],frozen[k+'_Q'])
  if k+'_groups' in frozen:assert np.array_equal(data[k][0],frozen[k+'_groups'])
 cw=[]
 for r in (8,54):cw.append(np.array([0]+[1]*r+[0,0]+[1]*(62-r)+[0],dtype=np.int8))
 expected_collision=np.stack(cw+[1-w for w in cw]);assert np.array_equal(expected_collision,words['collision'])
 coll=keyset(data['collision'][0]);assert len(coll)==4
 prior=set()
 for file in (ROOT/'v10_research/readout_conditioning_calibration_20261103/calibration_v1/frozen_data.npz',ROOT/'v10_research/rare_weight_ablation_20261103/ablation_v1/frozen_data.npz'):
  with np.load(file,allow_pickle=False) as z:
   for n in z.files:
    if n.endswith('_words'):prior.update(keyset(stats(z[n])[0]))
 enum=json.loads((ROOT/'v10_research/rare_state_enumeration_20261103/rare_states.json').read_text())['rows']
 enumwords=np.array([[int(c) for c in r['word']] for r in enum],dtype=np.int8);eg=stats(enumwords)[0]
 newmask=np.array([tuple(g) not in prior for g in eg]);reserved=keyset(eg[newmask]);assert newmask.sum()==20 and len(reserved)==18 and not (reserved&coll)
 assert np.array_equal(enumwords[newmask],words['structural_unseen20'])
 old_hash_mask=np.array([row['split']=='holdout' for row in enum]);assert np.array_equal(enumwords[old_hash_mask],words['structural_heldout'])
 oldcal=np.load(ROOT/'v10_research/readout_conditioning_calibration_20261103/calibration_v1/frozen_data.npz',allow_pickle=False)
 oldcal_groups=keyset(stats(np.concatenate([oldcal[k+'_words'] for k in ('train','validation','collision','boundary')]))[0])
 prev_mask=np.array([tuple(k) not in oldcal_groups for k in eg[old_hash_mask]])
 assert int(prev_mask.sum())==8 and np.array_equal(enumwords[old_hash_mask][prev_mask],words['structural_previous8'])
 assert len(saved.files)==42
 @lru_cache(None)
 def held(k):
  k=tuple(map(int,k))
  if k in coll:return False
  return k in reserved or int.from_bytes(hashlib.sha256(('v10-rare-split-20261103:'+','.join(map(str,k))).encode('ascii')).digest(),'big')%5==0
 def rare(g):return (g[:,0]<=6)|(g[:,2]==0)
 assert not any(held(tuple(k)) for k in data['train'][0])
 assert all(held(tuple(k)) for k in data['rare_heldout'][0]) and rare(data['rare_heldout'][0]).all()
 trainkeys=keyset(np.r_[data['train'][0],data['collision'][0]])
 assert not trainkeys&keyset(data['rare_heldout'][0]) and not trainkeys&reserved
 # Reconstruct every committed candidate batch from its original RNG state and
 # every original word from its saved latent inputs. This is replay, not sampling.
 batch_summary={}; candidate_total=0
 for setname,dataset in [('train','train'),('natural','natural'),('hold','rare_heldout')]:
  folder=run/'candidate_batches'/setname;files=sorted(folder.glob('batch_*.npz'));intents=sorted(folder.glob('batch_*.intent.json'))
  assert len(files)==len(intents)>0; selected_parts=[];total_eligible=0;drawn=0;previous=None;goal=cfg['training_prior_words'] if setname=='train' else cfg['natural_prior_evaluation_words'] if setname=='natural' else cfg['rare_group_heldout_words']
  initial=np.random.default_rng(cfg['data_seeds']['training' if setname=='train' else 'natural_evaluation' if setname=='natural' else 'rare_group_heldout']).bit_generator.state
  for i,(fp,ip) in enumerate(zip(files,intents)):
   assert fp.name==f'batch_{i:04d}.npz' and ip.name==f'batch_{i:04d}.intent.json'
   intent=json.loads(ip.read_text());z=np.load(fp,allow_pickle=False);n=len(z['words']);M=64
   assert n==cfg['draw_batch_size'] and len(files)<=cfg['maximum_draw_batches_per_rejection_set']
   before=json.loads(str(z['rng_before']));after=json.loads(str(z['rng_after']))
   assert intent=={'set':setname,'batch_index':i,'n':n,'M':M,'rng_before':before}
   assert before==(initial if previous is None else previous);previous=after;assert int(z['global_candidate_start'])==drawn
   gen=np.random.Generator(np.random.PCG64(0));gen.bit_generator.state=before
   probs=gen.random((n,4));starts=gen.integers(0,4,n);uniforms=np.stack([gen.random(n) for _ in range(M)])
   assert np.array_equal(probs,z['probabilities']) and np.array_equal(starts,z['starts']) and np.array_equal(uniforms,z['uniforms']) and gen.bit_generator.state==after
   w=np.empty((n,66),dtype=np.int8);w[:,0]=starts//2;w[:,1]=starts%2;ix=np.arange(n)
   for j in range(M):w[:,j+2]=(uniforms[j]<probs[ix,2*w[:,j]+w[:,j+1]])
   assert np.array_equal(w,z['words'])
   if setname=='natural':eligible=np.ones(n,bool)
   else:
    g=stats(w)[0];hh=np.array([held(tuple(k)) for k in g]);eligible=~hh if setname=='train' else (hh&rare(g))
   assert np.array_equal(eligible,z['eligible'])
   mask=np.zeros(n,bool);mask[np.flatnonzero(eligible)[:max(0,goal-sum(len(x) for x in selected_parts))]]=True
   assert np.array_equal(mask,z['selected']);selected_parts.append(w[mask]);total_eligible+=int(eligible.sum());drawn+=n
  selected=np.concatenate(selected_parts);assert len(selected)==goal and np.array_equal(selected,words[dataset]);candidate_total+=drawn
  saved_info=checks['train_sampling' if setname=='train' else 'natural_sampling' if setname=='natural' else 'holdout_sampling']
  assert saved_info=={'drawn':drawn,'accepted_before_truncation':total_eligible,'saved':goal}
  batch_summary[setname]={'batches':len(files),'drawn':drawn,'saved':len(selected),'eligible_before_truncation':total_eligible}
 # Verify the deterministic minibatch index stream exactly.
 tr=rare(data['train'][0]);ri=np.where(tr)[0];ni=np.where(~tr)[0];p=len(ri)/len(tr)
 assert len(ri) and len(ni) and checks['rare_count']==len(ri) and checks['nonrare_count']==len(ni)
 initial=json.loads(str(frozen['minibatch_rng_before']));g=np.random.Generator(np.random.PCG64(0));g.bit_generator.state=initial
 assert initial==np.random.default_rng(cfg['data_seeds']['minibatches']).bit_generator.state
 ir=frozen['prior_rare_indices'];inn=frozen['prior_nonrare_indices'];ic=frozen['collision_indices']
 assert ir.shape==(steps,32) and inn.shape==(steps,32) and ic.shape==(steps,64)
 for j in range(steps):
  assert np.array_equal(ir[j],g.choice(ri,32)) and np.array_equal(inn[j],g.choice(ni,32)) and np.array_equal(ic[j],g.integers(0,4,64))
 assert g.bit_generator.state==json.loads(str(frozen['minibatch_rng_after']))
 # Compare every prepared gradient and post-update parameter to a separate
 # loss/backprop/Adam reconstruction using only frozen words and saved indices.
 updates=load_csv(run/'updates.csv');checkpoint_rows=load_csv(run/'checkpoint_metrics.csv');final_rows=load_csv(run/'final_metrics.csv')
 assert len(updates)==12000 and len(checkpoint_rows)==24 and len(final_rows)==6
 iterator=iter(journal(run/'full_updates.bin'));index=0;max_grad=0.;max_param=0.;max_state=0.;max_loss=0.;max_pred=0.;max_metric=0.;final_details=[]
 for seed in seedlist:
  initial_params=[]
  for arm in ('corrected','rare_boost'):
   cp0=np.load(run/'checkpoints'/f'{arm}_{seed}_step0.npz',allow_pickle=False)
   assert str(cp0['condition'])=='half_count_scaled' and np.array_equal(cp0['scale'],SCALE) and int(cp0['optimizer_step'])==0
   keys=('W','b','v','c');parameters={k:cp0['param_'+k].copy() for k in keys};mom={k:cp0['adam_m_'+k].copy() for k in keys};second={k:cp0['adam_v_'+k].copy() for k in keys}
   assert {k:parameters[k].shape for k in keys}=={'W':(9,32),'b':(32,),'v':(32,),'c':(1,)}
   initial_params.append({k:v.copy() for k,v in parameters.items()});assert all(np.all(v==0) for v in (*mom.values(),*second.values()))
   beta1,beta2,eps,lr=map(lambda k:float(cp0[k]),('beta1','beta2','epsilon','readout_lr'))
   assert (beta1,beta2,eps,lr)==(.9,.999,1e-8,.003) and float(cp0['pool_lr'])==.01
   def check_checkpoint(step):
    nonlocal max_state,max_pred,max_metric
    cp=np.load(run/'checkpoints'/f'{arm}_{seed}_step{step}.npz',allow_pickle=False)
    assert int(cp['optimizer_step'])==step and str(cp['condition'])=='half_count_scaled' and np.array_equal(cp['scale'],SCALE)
    assert tuple(float(cp[k]) for k in ('beta1','beta2','epsilon','readout_lr','pool_lr'))==(beta1,beta2,eps,lr,.01)
    for k in keys:
     for label,dct in [('param_',parameters),('adam_m_',mom),('adam_v_',second)]:
      err=float(np.max(np.abs(cp[label+k]-dct[k])));max_state=max(max_state,err);assert err<5e-12
    rows=[r for r in checkpoint_rows if r['arm']==arm and int(r['seed'])==seed and int(r['step'])==step];assert len(rows)==1;row=rows[0]
    preds={k:forward(data[k][2],parameters) for k in names}
    evals={k:(data[k][1],preds[k]) for k in names if k!='train'}
    evals.update(train_rare=(data['train'][1][tr],preds['train'][tr]),train_nonrare=(data['train'][1][~tr],preds['train'][~tr]))
    for name,(y,q) in evals.items():
     for key,value in metrics(y,q).items():
      diff=abs(float(row[name+'_'+key])-value);max_metric=max(max_metric,diff);assert diff<5e-12
    if step==steps:
     fr=next(r for r in final_rows if r['arm']==arm and int(r['seed'])==seed);assert row==fr
     for k in names:
      err=float(np.max(np.abs(preds[k]-saved[f'{arm}_{seed}_{k}'])));max_pred=max(max_pred,err);assert err<5e-12
     final_details.append({'seed':seed,'arm':arm,'rare_heldout_MAE':metrics(data['rare_heldout'][1],preds['rare_heldout'])['mean_abs_error'],'natural_KL':metrics(data['natural'][1],preds['natural'])['mean_KL'],'collision_max':metrics(data['collision'][1],preds['collision'])['max_abs_error'],'unseen20_MAE':metrics(data['structural_unseen20'][1],preds['structural_unseen20'])['mean_abs_error'],'unseen20_max':metrics(data['structural_unseen20'][1],preds['structural_unseen20'])['max_abs_error']})
   check_checkpoint(0)
   for j in range(steps):
    meta,recorded,post=next(iterator);row=updates[index];index+=1
    assert (meta['arm'],meta['seed'],meta['step'])==(arm,seed,j+1) and (row['arm'],int(row['seed']),int(row['step']))==(arm,seed,j+1)
    loss,calc=weighted_grad(data,parameters,ir[j],inn[j],ic[j],p,arm);max_loss=max(max_loss,abs(loss-float(row['weighted_CE'])));close(loss,float(row['weighted_CE']))
    for k in keys:
     err=float(np.max(np.abs(calc[k]-recorded[k])));max_grad=max(max_grad,err);assert err<5e-12
     mom[k]=beta1*mom[k]+(1-beta1)*recorded[k];second[k]=beta2*second[k]+(1-beta2)*recorded[k]**2
     parameters[k]-=lr*(mom[k]/(1-beta1**(j+1)))/(np.sqrt(second[k]/(1-beta2**(j+1)))+eps)
     err=float(np.max(np.abs(parameters[k]-post[k])));max_param=max(max_param,err);assert err<5e-12
    close(float(row['gradient_l2']),float(np.sqrt(sum(np.sum(recorded[k]**2) for k in keys))))
    close(float(row['raw_W_l2']),float(np.linalg.norm(parameters['W'])))
    close(float(row['effective_W_l2']),float(np.linalg.norm(SCALE[:,None]*parameters['W'])))
    for k in range(9):close(float(row[f'W_gradient_row_{k}_l2']),float(np.linalg.norm(recorded['W'][k])))
    if j+1 in (200,1000,2000):check_checkpoint(j+1)
  assert all(np.array_equal(initial_params[0][k],initial_params[1][k]) for k in keys)
 try:next(iterator);raise AssertionError('extra journal entry')
 except StopIteration:pass
 assert index==12000
 screens=[]
 for seed in seedlist:
  a,b=[next(r for r in final_details if r['seed']==seed and r['arm']==arm) for arm in ('corrected','rare_boost')]
  passed=b['rare_heldout_MAE']<=.8*a['rare_heldout_MAE'] and b['natural_KL']-a['natural_KL']<=.002 and b['collision_max']<=.05
  reported=next(x for x in result['screen'] if x['seed']==seed);assert passed==reported['pass']
  close(b['rare_heldout_MAE']/a['rare_heldout_MAE'],reported['rare_heldout_error_ratio']);close(b['natural_KL']-a['natural_KL'],reported['natural_KL_increase']);close(b['collision_max'],reported['collision_max_error'])
  screens.append({'seed':seed,'pass':passed,'ratio':b['rare_heldout_MAE']/a['rare_heldout_MAE'],'natural_KL_change':b['natural_KL']-a['natural_KL'],'collision_max':b['collision_max']})
 assert result['screen_all_pass']==all(x['pass'] for x in screens)
 # Reconcile JSON/CSV, checkpoint console events and final status without
 # claiming a complete write-ahead record alone proves an update was committed.
 for r in result['final_metrics']:
  row=next(x for x in final_rows if x['arm']==r['arm'] and int(x['seed'])==r['seed'])
  for k,v in r.items():
   if isinstance(v,str):assert row[k]==v
   else:close(float(row[k]),float(v))
 events=[json.loads(line) for line in Path(console_file).read_text().splitlines() if line.startswith('{')]
 logcheck=[e for e in events if 'arm' in e and 'step' in e];assert len(logcheck)==24
 for event in logcheck:
  row=next(x for x in checkpoint_rows if x['arm']==event['arm'] and int(x['seed'])==event['seed'] and int(x['step'])==event['step'])
  for k,v in event.items():
   if isinstance(v,str):assert row[k]==v
   else:close(float(row[k]),float(v))
 assert events[-1]['status']=='done' and events[-1]['screen']==result['screen']
 return {'status':'PASS','reviewed_sealed_inputs':len(seal['files']),'output_hashes':len(manifest),'author_result_bindings':len(report_bindings),'console_sha256':sha(console_file),'candidate_batches':batch_summary,'candidate_words_reconstructed':candidate_total,'train_rare':int(tr.sum()),'heldout_group_intersection_train':len(trainkeys&keyset(data['rare_heldout'][0])),'reserved_group_intersection_train':len(trainkeys&reserved),'natural_train_distinct_word_overlap':len(wordset(words['natural'])&wordset(words['train'])),'reserved_features':int(newmask.sum()),'reserved_groups':len(reserved),'minibatch_steps_checked':steps,'journal_entries_checked':index,'checkpoints_checked':24,'final_prediction_arrays_checked':len(saved.files),'max_loss_error':max_loss,'max_gradient_error':max_grad,'max_adam_parameter_error':max_param,'max_checkpoint_state_error':max_state,'max_prediction_error':max_pred,'max_metric_error':max_metric,'screens':screens,'final_details':final_details}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--run',type=Path,default=P/'confirmation_v1');ap.add_argument('--console',type=Path,default=P/'confirmation_console.log');args=ap.parse_args()
 print(json.dumps(audit(args.run,args.console),indent=2,sort_keys=True,allow_nan=False))
