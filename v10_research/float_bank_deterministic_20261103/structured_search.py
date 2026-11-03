#!/usr/bin/env python3
"""Exhaustive low-Hamming-weight words, no random generation or model initialization."""
import os,sys,json,itertools,platform
import numpy as np
sys.path.insert(0,os.path.abspath('v10_research/learned_position_pilot_20261103'));import pilot
print('python',sys.version,'numpy',np.__version__,'platform',platform.platform(),flush=True)
print('env', {k:os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},flush=True)
np.show_config()
for M in (23,32,33,64,65,127,128,129,256,257,512,513):
 L=M//2; R=M-L; alpha=np.zeros((3,M)); alpha[0]=1/M; alpha[1,:L]=1/L; alpha[2,L:]=1/R
 seen={}; n=0; buffer=[]
 def process(buffer):
  global n
  w=np.asarray(buffer,dtype=np.int8);e=pilot.local_selected(w);f=np.einsum('hi,bic->bhc',alpha,e,optimize=True)
  j=e.sum((1,2)).astype(int);c=e[:,:,1].sum(1).astype(int);d=e[:,:L,:].sum((1,2)).astype(int);ee=e[:,:L,1].sum(1).astype(int)
  for i in range(len(w)):
   key=(int(w[i,-2]),int(w[i,-1]),int(j[i]),int(c[i]),int(d[i]),int(ee[i])); bits=f[i].view(np.uint64).tobytes(); n+=1
   if key in seen and seen[key][0]!=bits:
    old=seen[key];print('COLLISION',json.dumps({'M':M,'bank_with_terminal':key,'first_word':old[1], 'second_word':w[i].tolist(),'first_feature_hex':old[2], 'second_feature_hex':[float(x).hex() for x in f[i].reshape(-1)],'examined':n}),flush=True);sys.exit(0)
   if key not in seen:seen[key]=(bits,w[i].tolist(),[float(x).hex() for x in f[i].reshape(-1)])
 for base in (0,1):
  for u in itertools.product((0,1),repeat=2):
   # Every binary word with <=2 deviations among the editable M positions, and 0 or 1 baseline.
   for k in range(3):
    for positions in itertools.combinations(range(M),k):
     w=[base]*M+list(u)
     for i in positions:w[i]=1-base
     buffer.append(w)
     if len(buffer)==1024:process(buffer);buffer=[]
 if buffer:process(buffer)
 print('complete',M,'words',n,'banks',len(seen),flush=True)
print('No collisions in search')
