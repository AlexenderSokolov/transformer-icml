import json,numpy as np
from pathlib import Path
root=Path(__file__).resolve().parents[2]; f=np.load(root/'readout_conditioning_calibration_20261103/calibration_v1/frozen_data.npz'); pred=np.load(root/'readout_conditioning_calibration_20261103/calibration_v1/final_predictions.npz')
def calc(words):
 n=len(words);a=np.zeros((n,2,2),dtype=int);u=2*words[:,-2]+words[:,-1]
 for i in range(64):
  for j,w in enumerate(words):
   if 2*w[i]+w[i+1]==u[j]:a[j,i//32,w[i+2]]+=1
 J=a.sum((1,2));C=a[:,:,1].sum(1);D=a[:,0,:].sum(1);y=np.where(D>0,np.divide(C,J,out=np.zeros(n),where=J>0),words[:,-2])*.75+.125
 x=np.column_stack([a[:,:,0].sum(1),C,a[:,0,:],a[:,1,:],words[:,-2:]]); s=list(zip(J,C,D,u));return x,s,y
T,st,Y=calc(f['train_words']);V,sv,Z=calc(f['validation_words']);C,sc,YC=calc(f['collision_words']);B,sb,YB=calc(f['boundary_words']);print('literal Q max discrepancy',max(np.max(np.abs(y-f[k+'_Q'])) for k,y in [('train',Y),('validation',Z),('collision',YC),('boundary',YB)]));groups={}
for x,y in [(T,Y),(V,Z),(C,YC),(B,YB)]:
 for row,q in zip(x,y):groups.setdefault(tuple(row),set()).add(q)
print('unique features',len(groups),'contradictions',sum(len(v)>1 for v in groups.values())); trainstats=set(st); colstats=set(sc);trainfeatures=set(map(tuple,T)); print('worst validation 1242',sv[1242],V[1242].tolist(),Z[1242], 'train stat hits',st.count(sv[1242]), 'train feat hits',list(map(tuple,T)).count(tuple(V[1242])))
inds=np.where(np.all(T[:,6:]==V[1242,6:],axis=1))[0];dist=np.abs(T[inds,:6]-V[1242,:6]).sum(1);print('minimum L1',np.min(dist),'nearest train',inds[dist==np.min(dist)].tolist()); print('word 1699',st[1699],Y[1699],'draws',np.sum(f['prior_batch_indices']==1699),'797',st[797],Y[797],'draws',np.sum(f['prior_batch_indices']==797))
for seed in [20261103201,20261103202,20261103203]:
 q=pred[f'half_count_scaled_{seed}_validation'];p=pred[f'half_count_scaled_{seed}_train'];err=abs(q-Z);te=abs(p-Y);idx=np.where(err>.1)[0];kl=Z*np.log(Z/q)+(1-Z)*np.log((1-Z)/(1-q)); print(seed,'tail',len(idx),'absent train+collision stat',sum(sv[i] not in trainstats and sv[i] not in colstats for i in idx),'tail matching training full',sum(tuple(V[i]) in trainfeatures for i in idx),'worst index',np.argmax(err),'worst q',q[1242],'worst kl',kl[1242],'tail KL fraction',np.sum(kl[idx])/np.sum(kl),'train >.1',sum(te>.1),'train max',te.max(),'train worst idx',np.argmax(te),'train worst q',p[1699],'near q',p[797])
print('gate integer equivalence exhaustive',all((j>0 and 512*d>=j)==(d>=1) for j in range(65) for d in range(j+1)))
print('feature upper bound',4*(33*34//2)**2,'epsilon',1/66**2,'logit extrema',np.log((.125-1/66**2)/(1-1/66**2-.125)),np.log((.875-1/66**2)/(1-1/66**2-.875)))
