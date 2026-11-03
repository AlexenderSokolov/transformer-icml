#!/usr/bin/env python3
"""Exhaustive deterministic bank collision search; no RNG or model construction."""
import os,sys,json,platform,hashlib
import numpy as np
sys.path.insert(0,os.path.abspath('v10_research/learned_position_pilot_20261103'))
import pilot
np.set_printoptions(precision=17)
print('python',sys.version,'numpy',np.__version__,'platform',platform.platform(),flush=True)
print('thread env', {k:os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},flush=True)
np.show_config()
for M in range(2,21):
    n=1<<(M+2); block=2048; seen={}; L=M//2; R=M-L
    alpha=np.zeros((3,M)); alpha[0]=1/M; alpha[1,:L]=1/L; alpha[2,L:]=1/R
    for start in range(0,n,block):
        a=np.arange(start,min(start+block,n),dtype=np.uint64)
        w=((a[:,None] >> np.arange(M+1,-1,-1,dtype=np.uint64)) & 1).astype(np.int8)
        e=pilot.local_selected(w); f=np.einsum('hi,bic->bhc',alpha,e,optimize=True)
        j=e.sum((1,2)).astype(int); c=e[:,:,1].sum(1).astype(int); d=e[:,:L,:].sum((1,2)).astype(int); ee=e[:,:L,1].sum(1).astype(int)
        for i in range(len(a)):
            key=(int(w[i,-2]),int(w[i,-1]),int(j[i]),int(c[i]),int(d[i]),int(ee[i]))
            bits=f[i].view(np.uint64).tobytes()
            if key in seen and seen[key][0]!=bits:
                old=seen[key]
                print('COLLISION',json.dumps({'M':M,'bank_with_terminal':key,'first_index':old[1],'second_index':int(a[i]),'first_word':old[2], 'second_word':w[i].tolist(),'first_features':old[3],'second_features':f[i].reshape(-1).tolist(),'first_feature_hex':old[4],'second_feature_hex':[float(x).hex() for x in f[i].reshape(-1)],'first_batch':old[5],'second_batch_start':start}),flush=True);sys.exit(0)
            if key not in seen:seen[key]=(bits,int(a[i]),w[i].tolist(),f[i].reshape(-1).tolist(),[float(x).hex() for x in f[i].reshape(-1)],start)
    print('complete',M,'words',n,'banks',len(seen),flush=True)
print('No collisions in search')
