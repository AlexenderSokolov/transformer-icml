import sys,csv,json,hashlib
from pathlib import Path
import numpy as np
base=Path(__file__).resolve().parent.parent; sys.path.insert(0,str(base));import pilot
A=base/'smoke_v1'; R=base/'independent_replay'
paths=np.load(A/'evaluation_paths.npz');metrics=np.load(A/'trajectory_metrics.npz');mp=np.load(R/'trajectory_metrics.npz'); pp=np.load(R/'evaluation_paths.npz')
print('paths equal',set(paths.files)==set(pp.files),all(np.array_equal(paths[k],pp[k]) for k in paths.files),'metric arrays equal',set(metrics.files)==set(mp.files),all(np.array_equal(metrics[k],mp[k]) for k in metrics.files))
models={}
for name in ['learned_clean','learned_edit','uniform_edit','random_edit','half_edit']:
 ck=np.load(A/'checkpoints'/f'{name}_200.npz'); model=pilot.Model(0,str(ck['mode']));model.params={k:ck[k].copy() for k in ['a','W','b','v','c']};models[name]=model
predictors={k:v.predict for k,v in models.items()}
for name in ['learned_clean','learned_edit']:
 m=pilot.Model(0,'uniform');m.params={k:v.copy() for k,v in models[name].params.items()};predictors[name+'_uniform_ablation']=m.predict
for name in ['B','A','Q']:predictors[name]=lambda w,name=name:pilot.statistics(w)[name]
rows=list(csv.DictReader(open(A/'stress_evaluation.csv')));max_tv=0; max_summary=0;bad_attacks=0
for row in rows:
 M=int(row['M']);source=row['source'];s=int(row['initial']);k=int(row['k']);fam=row['attack_family'];name=row['condition'];w=paths[f'stress_M{M}_{source}_s{s}_words'];p=paths[f'stress_M{M}_{source}_s{s}_p']; idx=metrics[f'M{M}_{source}_s{s}_k{k}_{fam}_{name}_attack']; cand=pilot.proposals(w,k,fam); z=cand[idx,np.arange(len(w))];q=predictors[name](z);u=2*w[:,-2]+w[:,-1];tv=abs(q-p[np.arange(len(w)),u]); key=f'M{M}_{source}_s{s}_k{k}_{fam}_{name}_tv';max_tv=max(max_tv,float(np.max(abs(tv-metrics[key]))));max_summary=max(max_summary,abs(tv.mean()-float(row['TV'])),abs(tv.std(ddof=1)/len(tv)**.5-float(row['TV_MC_SE'])));bad_attacks+=int(np.any(np.sum(z!=w,axis=1)>k) or np.any(z[:,-2:]!=w[:,-2:]))
print('stress rows',len(rows),'max tv difference',max_tv,'max mean/SE difference',max_summary,'invalid cells',bad_attacks)
for M in [64,128,256]:
 for name,p in pilot.stress_sources(M).items():
  P=np.zeros((4,4))
  for u in range(4):P[u,2*(u%2)]=1-p[u];P[u,2*(u%2)+1]=p[u]
  mat=P.T-np.eye(4);mat[-1]=1;pi=np.linalg.solve(mat,[0,0,0,1]);print('certificate',M,name,'min P^2',np.min(P@P),'1/M',1/M,'min P²-pi/M',np.min(P@P-pi[None,:]/M))
clean=list(csv.DictReader(open(A/'clean_evaluation.csv')));ce_err=0;tv_err=0
for row in clean:
 M=int(row['M']);name=row['condition'];w=paths[f'clean_M{M}_words'];p=paths[f'clean_M{M}_p'];u=2*w[:,-2]+w[:,-1];target=p[np.arange(len(w)),u];q=predictors[name](w);b=pilot.statistics(w)['B'];tv=abs(q-target);ce=pilot.cross_entropy(b,q)-pilot.cross_entropy(b,b);tv_err=max(tv_err,abs(tv.mean()-float(row['TV']))); 
 if np.all(np.isfinite(ce)):ce_err=max(ce_err,abs(ce.mean()-float(row['excess_KL'])),abs(ce.std(ddof=1)/len(ce)**.5-float(row['excess_KL_MC_SE'])))
print('clean rows',len(clean),'max TV mean discrepancy',tv_err,'max KL mean/SE discrepancy',ce_err)
for name in ['random_edit','learned_edit']:
 for M in [64,128,256]:
  alpha,_=models[name].pooling(M);print(name,M,'head-first-half',*[round(float(x),8) for x in alpha[1:,:M//2].sum(axis=1)],'largest relative uniform departure',np.max(abs(alpha[1:]*M-1)))
maxlossdiff=0;different_tie_indices=0
for row in rows:
 M=int(row['M']);source=row['source'];s=int(row['initial']);k=int(row['k']);fam=row['attack_family'];name=row['condition'];w=paths[f'stress_M{M}_{source}_s{s}_words'];pred=predictors[name];cand=pilot.proposals(w,k,fam);q=pred(cand.reshape(-1,M+2)).reshape(len(cand),len(w));b=pilot.statistics(w)['B'];loss=pilot.cross_entropy(b[None,:],q);expected=loss.argmax(axis=0);stored=metrics[f'M{M}_{source}_s{s}_k{k}_{fam}_{name}_attack'];different_tie_indices+=int(np.sum(expected!=stored));
 # Compare finite maxima separately to avoid inf - inf.
 best=loss.max(axis=0); selected=loss[stored,np.arange(len(w))]; finite=np.isfinite(best); maxlossdiff=max(maxlossdiff,float(np.max(np.abs(best[finite]-selected[finite]),initial=0)));different_tie_indices+=int(np.sum(np.isinf(best)!=np.isinf(selected)))
print('independent finite proposal loss maximum discrepancy',maxlossdiff,'selected index/inf mismatch',different_tie_indices)
count=0;inf_ties=0;identity=0;tv_subopt=0;total=0;maximum_gap=0
for row in rows:
 if row['condition']!='A' or int(row['k'])==0:continue
 M=int(row['M']);source=row['source'];s=int(row['initial']);k=int(row['k']);fam=row['attack_family'];w=paths[f'stress_M{M}_{source}_s{s}_words'];p=paths[f'stress_M{M}_{source}_s{s}_p'];u=2*w[:,-2]+w[:,-1];theta=p[np.arange(len(w)),u]; cand=pilot.proposals(w,k,fam);q=pilot.statistics(cand.reshape(-1,M+2))['A'].reshape(len(cand),len(w));loss=pilot.cross_entropy(pilot.statistics(w)['B'][None,:],q);idx=loss.argmax(axis=0);hasinf=np.isinf(loss).any(axis=0);tie=np.sum(np.isinf(loss),axis=0)>1;tv=abs(q-theta);chosen=tv[idx,np.arange(len(w))];gap=tv.max(axis=0)-chosen;total+=len(w);count+=int(hasinf.sum());inf_ties+=int(tie.sum());identity+=int((hasinf&(idx==0)).sum());tv_subopt+=int((gap>1e-12).sum());maximum_gap=max(maximum_gap,float(gap.max()))
print('A stress nonzero-k candidate sets',total,'infinite max',count,'multiple infinity',inf_ties,'infinite identity selected',identity,'selected TV not candidate max',tv_subopt,'max individual TV gap',maximum_gap)
