#!/usr/bin/env python3
"""Exhaustive first mismatch to float division reconstructed bank; no RNG."""
import os,sys,json,platform
import numpy as np
sys.path.insert(0,os.path.abspath('v10_research/learned_position_pilot_20261103'));import pilot
sys.path.insert(0,os.path.abspath('v10_research/four_counter_dp_20261103'));import four_counter
print('numpy',np.__version__,'python',sys.version,'platform',platform.platform())
for M in range(2,18):
 L=M//2;R=M-L;alpha=np.zeros((3,M));alpha[0]=1/M;alpha[1,:L]=1/L;alpha[2,L:]=1/R
 n=1<<(M+2)
 for start in range(0,n,2048):
  a=np.arange(start,min(start+2048,n),dtype=np.uint64);w=((a[:,None]>>np.arange(M+1,-1,-1,dtype=np.uint64))&1).astype(np.int8)
  e=pilot.local_selected(w);f=np.einsum('hi,bic->bhc',alpha,e,optimize=True)
  for i in range(len(w)):
   bank=four_counter.feature_bank(w[i]); recon=four_counter.model_inputs(M,w[i,-2:],bank)[:6];actual=f[i].flatten()
   if any(float(x).hex()!=float(y).hex() for x,y in zip(actual,recon)):
    print(json.dumps({'M':M,'word':w[i].tolist(),'bank':[int(x) for x in bank],'actual':[float(x).hex() for x in actual],'model_inputs':[float(x).hex() for x in recon], 'batch_start':start,'batch_size':len(w)},indent=2));sys.exit(0)
 print('complete',M,'words',n)
