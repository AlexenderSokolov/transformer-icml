"""Read-only reconstruction of retained run; no data generation or optimization."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import csv, hashlib, json, math
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent.parent
ROOT=P.parent.parent
RUN=P/'ablation_v1'

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def loadcsv(path):
 with path.open(newline='') as f:return list(csv.DictReader(f))
def stats(words):
 w=np.asarray(words,dtype=np.int64)
 assert w.ndim==2 and w.shape[1]==66 and np.isin(w,(0,1)).all()
 terminal=2*w[:,-2]+w[:,-1]
 pair=2*w[:,:64]+w[:,1:65];tail=w[:,2:66];match=pair==terminal[:,None]
 first=match[:,:32];last=match[:,32:]
 a0=np.sum(first*(1-tail[:,:32]),axis=1);a1=np.sum(first*tail[:,:32],axis=1)
 b0=np.sum(last*(1-tail[:,32:]),axis=1);b1=np.sum(last*tail[:,32:],axis=1)
 j=a0+a1+b0+b1;c=a1+b1;d=a0+a1
 target=.125+.75*np.where(d>0,np.divide(c,j,out=np.zeros_like(j,dtype=float),where=j>0),w[:,-2])
 X=np.column_stack([(a0+b0)/64,(a1+b1)/64,a0/32,a1/32,b0/32,b1/32,w[:,-2],w[:,-1],np.full(len(w),1/64)])
 return np.column_stack([j,c,d,terminal]),target,X

def metric(y,q):
 ae=np.abs(y-q);kl=y*np.log(y/q)+(1-y)*np.log((1-y)/(1-q))
 return dict(n=len(y),mean_KL=kl.mean(),mean_abs_error=ae.mean(),q95_abs_error=np.quantile(ae,.95),max_abs_error=ae.max(),count_over_0_1=np.sum(ae>.1))
def predict(x,m):
 assert np.array_equal(m['effective_W'],m['W']*m['scale'][:,None]);z=np.tanh(x@m['effective_W']+m['b'])@m['v']+m['c'][0]
 s=np.empty_like(z);pos=z>=0;s[pos]=1/(1+np.exp(-z[pos]));r=np.exp(z[~pos]);s[~pos]=r/(1+r)
 eps=1/66**2;return eps+(1-2*eps)*s

def main():
 h=json.loads((RUN/'ARTIFACT_HASHES.json').read_text());mismatches=[k for k,v in h.items() if not (RUN/k).is_file() or sha(RUN/k)!=v]
 allfiles={str(f.relative_to(RUN)) for f in RUN.rglob('*') if f.is_file()}-{'ARTIFACT_HASHES.json'}
 assert set(h)==allfiles and not mismatches
 sealed=json.loads((P/'PRE_RUN_HASHES.json').read_text());assert all(sha(ROOT/k)==v for k,v in sealed['files'].items())
 data=np.load(RUN/'frozen_data.npz');saved=np.load(RUN/'final_predictions.npz');names=['train','natural','rare_heldout','collision','structural_heldout','structural_novel']
 W={k:data[k+'_words'] for k in names};T={k:stats(W[k]) for k in names};max_target=0
 for k in names:
  G,Y,X=T[k];max_target=max(max_target,float(np.max(np.abs(Y-data[k+'_Q']))))
  if k+'_groups' in data:assert np.array_equal(G,data[k+'_groups'])
 assert max_target<1e-14
 G={k:T[k][0] for k in names};group_set=lambda a:set(map(tuple,a))
 collision=group_set(G['collision']);assert len(collision)==4
 def held(key):
  key=tuple(map(int,key));txt='v10-rare-split-20261103:'+','.join(map(str,key))
  return key not in collision and int.from_bytes(hashlib.sha256(txt.encode('ascii')).digest(),'big')%5==0
 def rare(g):return (g[:,0]<=6)|(g[:,2]==0)
 assert not any(map(held,G['train'])) and not any(map(held,G['collision']))
 assert all(map(held,G['rare_heldout'])) and all(rare(G['rare_heldout']))
 assert all(map(held,G['structural_heldout'])) and all(G['structural_heldout'][:,0]<=3)
 tg=group_set(np.r_[G['train'],G['collision']]);hg=group_set(G['rare_heldout']);sg=group_set(G['structural_heldout'])
 assert not(tg&hg) and not(tg&sg)
 old=np.load(ROOT/'v10_research/readout_conditioning_calibration_20261103/calibration_v1/frozen_data.npz')
 og=group_set(stats(np.concatenate([old[k+'_words'] for k in ('train','validation','collision','boundary')]))[0])
 expected=np.array([tuple(k) not in og for k in G['structural_heldout']])
 assert np.array_equal(W['structural_novel'],W['structural_heldout'][expected])
 assert len(W['structural_novel'])==8 and len(group_set(G['structural_novel']))==7
 structural=json.loads((ROOT/'v10_research/rare_state_enumeration_20261103/rare_states.json').read_text())['rows']
 sw=np.array([[int(c) for c in r['word']] for r in structural if r['split']=='holdout'],dtype=np.int8)
 assert np.array_equal(sw,W['structural_heldout'])
 wordset=lambda w:set(map(bytes,np.asarray(w,dtype=np.uint8)))
 overlap=len(wordset(W['natural'])&wordset(W['train']));assert overlap==14
 trainrare=rare(G['train']);assert int(trainrare.sum())==133
 for k,mask,n in [('prior_rare_indices',trainrare,32),('prior_nonrare_indices',~trainrare,32)]:
  ix=data[k];assert ix.shape==(2000,n) and (ix>=0).all() and (ix<len(mask)).all() and mask[ix].all()
 ci=data['collision_indices'];assert ci.shape==(2000,64) and (ci>=0).all() and (ci<4).all()
 metrics_rows=loadcsv(RUN/'checkpoint_metrics.csv');assert len(metrics_rows)==24
 finals=loadcsv(RUN/'final_metrics.csv');assert len(finals)==6
 updates=loadcsv(RUN/'updates.csv');assert len(updates)==12000
 result=json.loads((RUN/'results.json').read_text());assert result['screen_all_pass'] and len(result['screen'])==3
 assert len(result['final_metrics'])==6
 for item in result['final_metrics']:
  row=next(r for r in finals if r['arm']==item['arm'] and int(r['seed'])==item['seed'])
  for key,v in item.items():
   assert row[key]==v if isinstance(v,str) else float(row[key])==v
 console=[json.loads(line) for line in (P/'run_console.log').read_text().splitlines() if line.startswith('{')]
 assert len(console)==26 and console[-1]['status']=='done' and console[-1]['screen']==result['screen']
 for item in console[1:-1]:
  row=next(r for r in metrics_rows if r['arm']==item['arm'] and int(r['seed'])==item['seed'] and int(r['step'])==item['step'])
  for key,v in item.items():
   assert row[key]==v if isinstance(v,str) else float(row[key])==v
 seedlist=[20261103201,20261103202,20261103203];arms=['corrected','rare_boost'];steps=[0,200,1000,2000]
 max_prediction=0.;max_metric=0.;metric_count=0;details=[]
 for seed in seedlist:
  init=[]
  for arm in arms:
   u=[r for r in updates if r['arm']==arm and int(r['seed'])==seed]
   assert len(u)==2000 and [int(r['step']) for r in u]==list(range(1,2001))
   assert all(math.isfinite(float(r[k])) for r in u for k in r if k not in ('arm',))
   for step in steps:
    fp=RUN/'checkpoints'/f'{arm}_{seed}_step{step}.npz';m=np.load(fp)
    assert str(m['condition'])=='half_count_scaled'
    assert np.array_equal(m['scale'],[64,64,32,32,32,32,1,1,1])
    if step==0:init.append([m[k] for k in ('W','b','v','c')])
    rows=[r for r in metrics_rows if r['arm']==arm and int(r['seed'])==seed and int(r['step'])==step];assert len(rows)==1;row=rows[0]
    qs={k:predict(T[k][2],m) for k in names}
    evals={k:(T[k][1],qs[k]) for k in names if k!='train'}
    evals.update(train_rare=(T['train'][1][trainrare],qs['train'][trainrare]),train_nonrare=(T['train'][1][~trainrare],qs['train'][~trainrare]))
    for k,(y,q) in evals.items():
     for metric_name,v in metric(y,q).items():
      max_metric=max(max_metric,abs(float(v)-float(row[k+'_'+metric_name])));metric_count+=1
    if step==2000:
     finalrow=next(r for r in finals if r['arm']==arm and int(r['seed'])==seed);assert finalrow==row
     for k in names:max_prediction=max(max_prediction,float(np.max(np.abs(qs[k]-saved[f'{arm}_{seed}_{k}']))))
     details.append({'seed':seed,'arm':arm,'novel_MAE':float(np.mean(np.abs(T['structural_novel'][1]-qs['structural_novel']))),'natural_KL':float(metric(T['natural'][1],qs['natural'])['mean_KL']),'collision_max':float(np.max(np.abs(T['collision'][1]-qs['collision']))),'natural_MAE':float(np.mean(np.abs(T['natural'][1]-qs['natural']))),'heldout_MAE':float(np.mean(np.abs(T['rare_heldout'][1]-qs['rare_heldout']))),'heldout_max':float(np.max(np.abs(T['rare_heldout'][1]-qs['rare_heldout']))),'structural_max':float(np.max(np.abs(T['structural_heldout'][1]-qs['structural_heldout'])))})
  assert all(np.array_equal(a,b) for a,b in zip(*init))
 assert max_metric<1e-13 and max_prediction<1e-13
 screens=[]
 for seed in seedlist:
  a,b=[next(r for r in details if r['seed']==seed and r['arm']==arm) for arm in arms]
  ratio=b['novel_MAE']/a['novel_MAE'];increase=b['natural_KL']-a['natural_KL'];passed=ratio<=.8 and increase<=.002 and b['collision_max']<=.05
  reported=next(r for r in result['screen'] if r['seed']==seed)
  assert passed==reported['pass'] and abs(ratio-reported['structural_novel_error_ratio'])<1e-13 and abs(increase-reported['natural_KL_increase'])<1e-13 and abs(b['collision_max']-reported['collision_max_error'])<1e-13
  screens.append({'seed':seed,'ratio':ratio,'natural_KL_change':increase,'collision_max':b['collision_max'],'pass':passed})
 checks=json.loads((RUN/'pre_fit_checks.json').read_text());assert checks['frozen_data_sha256']==sha(RUN/'frozen_data.npz') and checks['train_sampling']['drawn']+checks['holdout_sampling']['drawn']-2048-1024==128000
 print(json.dumps({'status':'PASS','sealed_input_hashes_verified':len(sealed['files']),'run_output_hashes_verified':len(h),'max_literal_target_error':max_target,'max_final_prediction_error':max_prediction,'max_checkpoint_metric_error':max_metric,'checkpoint_metric_values_checked':metric_count,'checkpoint_count':24,'final_prediction_arrays_checked':len(saved.files),'updates_rows_checked':len(updates),'train_rare':int(trainrare.sum()),'natural_train_distinct_word_overlap':overlap,'group_counts':{'train':len(tg),'rare_holdout':len(hg),'structural_holdout':len(sg),'structural_novel':len(group_set(G['structural_novel']))},'heldout_intersection_train':len(tg&hg),'structural_intersection_train':len(tg&sg),'old_intersection_novel':len(og&group_set(G['structural_novel'])),'screens':screens,'final_recomputed':details},indent=2,sort_keys=True))
if __name__=='__main__':main()
