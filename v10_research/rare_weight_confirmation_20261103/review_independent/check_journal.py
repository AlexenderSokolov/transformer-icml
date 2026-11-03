import numpy as np,hashlib,json,csv,struct,time
from pathlib import Path
B=Path(__file__).resolve().parent.parent;O=B/'confirmation_v1';D=np.load(O/'frozen_data.npz');rows=list(csv.DictReader(open(O/'updates.csv'))); assert len(rows)==12000

def features(w):
 n=len(w);u=2*w[:,-2]+w[:,-1];a=np.zeros((n,2,2),int)
 for i in range(64):
  m=2*w[:,i]+w[:,i+1]==u;np.add.at(a,(np.arange(n)[m],np.full(n,i//32)[m],w[m,i+2]),1)
 return np.column_stack([a[:,:,0].sum(1),a[:,:,1].sum(1),a[:,0,:],a[:,1,:],w[:,-2:],np.full(n,1/64)])
X={k:features(D[k+'_words']) for k in ['train','collision']};Y={k:D[k+'_Q'] for k in X};p=115/2048; names=['W','b','c','v']; hdr=struct.Struct('<8sQ32s');seq=[(arm,seed) for seed in [20261103601,20261103602,20261103603] for arm in ['corrected','rare_boost']];param=m=var=None;maxg=maxpost=maxcsv=maxck=maxmom=maxloss=0;count=0;erridentity=0;cp=0
with open(O/'full_updates.bin','rb') as f:
 while True:
  header=f.read(hdr.size)
  if not header:break
  assert len(header)==hdr.size; magic,size,digest=hdr.unpack(header);payload=f.read(size);assert magic==b'RWUPD01!' and len(payload)==size and hashlib.sha256(payload).digest()==digest
  n=struct.unpack('<I',payload[:4])[0];meta=json.loads(payload[4:4+n]); nums=np.frombuffer(payload[4+n:],dtype='<f8');assert meta['names']==names and meta['count']==353 and len(nums)==706
  groups=[];off=0
  for part in range(2):
   d={}
   for k in names:
    shape=meta['shapes'][k];n1=int(np.prod(shape));d[k]=nums[off:off+n1].reshape(shape).copy();off+=n1
   groups.append(d)
  grad,post=groups;arm,seed=seq[count//2000];step=count%2000+1;assert (meta['arm'],meta['seed'],meta['step'])==(arm,seed,step);row=rows[count];assert (row['arm'],int(row['seed']),int(row['step']))==(arm,seed,step)
  if step==1:
   z=np.load(O/'checkpoints'/f'{arm}_{seed}_step0.npz');assert int(z['optimizer_step'])==0 and np.array_equal(z['scale'],[64,64,32,32,32,32,1,1,1]);param={k:z['param_'+k].copy() for k in names};m={k:z['adam_m_'+k].copy() for k in names};var={k:z['adam_v_'+k].copy() for k in names};cp+=1
  ws=[.5*p,.5*(1-p),.5] if arm=='corrected' else [.25,.25,.5];inds=[D['prior_rare_indices'][step-1],D['prior_nonrare_indices'][step-1],D['collision_indices'][step-1]];g={k:np.zeros_like(param[k]) for k in names};loss=0
  for typ,idx,wt in zip(['train','train','collision'],inds,ws):
   x=X[typ][idx];y=Y[typ][idx];h=np.tanh(x@param['W']+param['b']);v=h@param['v']+param['c'][0];s=1/(1+np.exp(-v));ep=1/66**2;q=ep+(1-2*ep)*s;loss+=wt*np.mean(-y*np.log(q)-(1-y)*np.log1p(-q));d=wt/len(y)*(q-y)/(q*(1-q))*(1-2*ep)*s*(1-s);dh=d[:,None]*param['v']*(1-h*h);g['W']+=x.T@dh;g['b']+=dh.sum(0);g['v']+=h.T@d;g['c']+=np.array([d.sum()])
  for k in names:maxg=max(maxg,float(np.max(abs(g[k]-grad[k]))))
  maxloss=max(maxloss,abs(loss-float(row['weighted_CE'])))
  norm=np.sqrt(sum(np.sum(grad[k]**2) for k in names));maxcsv=max(maxcsv,abs(norm-float(row['gradient_l2'])))
  for i in range(9):maxcsv=max(maxcsv,abs(np.linalg.norm(grad['W'][i])-float(row[f'W_gradient_row_{i}_l2'])))
  for k in names:
   m[k]=.9*m[k]+.1*grad[k];var[k]=.999*var[k]+.001*grad[k]**2;update=.003*(m[k]/(1-.9**step))/(np.sqrt(var[k]/(1-.999**step))+1e-8);param[k]-=update;maxpost=max(maxpost,float(np.max(abs(param[k]-post[k]))));param[k]=post[k].copy()
  maxcsv=max(maxcsv,abs(np.linalg.norm(param['W'])-float(row['raw_W_l2'])),abs(np.linalg.norm(np.array([64,64,32,32,32,32,1,1,1])[:,None]*param['W'])-float(row['effective_W_l2'])))
  if step in (200,1000,2000):
   z=np.load(O/'checkpoints'/f'{arm}_{seed}_step{step}.npz');assert int(z['optimizer_step'])==step and float(z['readout_lr'])==.003 and float(z['beta1'])==.9 and float(z['beta2'])==.999 and float(z['epsilon'])==1e-8
   for k in names:maxck=max(maxck,float(np.max(abs(param[k]-z['param_'+k]))));maxmom=max(maxmom,float(np.max(abs(m[k]-z['adam_m_'+k]))),float(np.max(abs(var[k]-z['adam_v_'+k]))))
   cp+=1
  count+=1
assert count==12000 and cp==24
print('journal records, all input minibatch gradients recalculated',count,'model/Adam checkpoints',cp,'max gradient difference',maxg,'max weighted loss',maxloss,'max Adam proposed param difference',maxpost,'max CSV norm difference',maxcsv,'max checkpoint param difference',maxck,'max Adam moment difference',maxmom)
assert maxg<1e-10 and maxloss<1e-11 and maxpost<1e-11 and maxcsv<1e-10 and maxck<1e-11 and maxmom<1e-11
