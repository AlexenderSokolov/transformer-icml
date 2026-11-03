#!/usr/bin/env python3
"""Deterministic location sweep, identical batch shape and position. No RNG."""
import os,sys,platform,json
import numpy as np
sys.path.insert(0,os.path.abspath('v10_research/learned_position_pilot_20261103'));import pilot
sys.path.insert(0,os.path.abspath('v10_research/four_counter_dp_20261103'));import four_counter
print('numpy',np.__version__,'python',sys.version,'platform',platform.platform(), 'threads',os.environ.get('OPENBLAS_NUM_THREADS'),flush=True);np.show_config()
for M in (257,513,1025,2049,4097,8193):
 for B in (2,16,128,1024):
  alpha=np.zeros((3,M));L=M//2;alpha[0]=1/M;alpha[1,:L]=1/L;alpha[2,L:]=1/(M-L)
  seen={}; choices=list(range(L+3,M-4,max(1,M//256)));tested=0
  for start in range(0,len(choices),B):
   locations=choices[start:start+B];batch=np.ones((B,M+2),dtype=np.int8)
   for row,i in enumerate(locations):batch[row,[i,i+3]]=0
   # Padding with all-ones words retains batch dimension and kernel selection.
   e=pilot.local_selected(batch);f=np.einsum('hi,bic->bhc',alpha,e,optimize=True)
   for slot,i in enumerate(locations):
    bank=tuple(map(int,four_counter.feature_bank(tuple(map(int,batch[slot]))))); key=bank; signature=f[slot].view(np.uint64).tobytes();tested+=1
    if key in seen and seen[key][0]!=signature:
     old=seen[key]; print('COLLISION',json.dumps({'M':M,'batch_size':B,'bank':bank,'zeroA':[old[1],old[1]+3],'zeroB':[i,i+3],'featuresA':old[2],'featuresB':[float(x).hex() for x in f[slot].flat],'slotA':old[3],'slotB':slot}),flush=True);sys.exit(0)
    if key not in seen:seen[key]=(signature,i,[float(x).hex() for x in f[slot].flat],slot)
  print('complete',M,B,'tested',tested,'banks',len(seen),flush=True)
print('no collision')
