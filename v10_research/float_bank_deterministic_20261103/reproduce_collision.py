#!/usr/bin/env python3
"""Fixed constants only. Model allocated without __init__, hence no RNG calls."""
import os,sys,platform,json
import numpy as np
sys.path.insert(0,os.path.abspath('v10_research/learned_position_pilot_20261103'));import pilot
sys.path.insert(0,os.path.abspath('v10_research/four_counter_dp_20261103'));import four_counter
M=257;w=np.ones((2,M+2),dtype=np.int8);w[0,[130,133]]=0;w[1,[250,256]]=0
print('python',sys.version,'numpy',np.__version__,'platform',platform.platform())
print('env', {k:os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')});np.show_config()
print('zeros',[[int(j) for j in np.where(row==0)[0]] for row in w],'hamming',int(np.sum(w[0]!=w[1])))
banks=[four_counter.feature_bank(tuple(map(int,row))) for row in w];print('banks',banks);assert banks[0]==banks[1]
model=pilot.Model.__new__(pilot.Model);model.mode='half';alpha,_=model.pooling(M)
for n in (1,2,4,16,128,1024):
 fs=[]
 for row in w:
  batch=np.tile(row,(n,1));e=pilot.local_selected(batch);f=np.einsum('hi,bic->bhc',alpha,e,optimize=True);fs.append(f)
 equal=np.all(fs[0].view(np.uint64)==fs[1].view(np.uint64),axis=(1,2));firstdiff=np.flatnonzero(~equal)
 print('n',n,'different_same_slot_count',len(firstdiff),'first_different_indices',firstdiff[:12].tolist(),'first_word_positions_signatures', {str(i):[float(x).hex() for x in fs[0][i].flat] for i in set([0,n-1])}, 'second_word_positions_signatures', {str(i):[float(x).hex() for x in fs[1][i].flat] for i in set([0,n-1])})
 if len(firstdiff):
  slot=int(firstdiff[0]); print('DIFF_SLOT',slot, 'feature_A', [float(x).hex() for x in fs[0][slot].flat], 'feature_B',[float(x).hex() for x in fs[1][slot].flat]);
  # Both in SAME call at positions in same BLAS lane category, if available.
  same=np.flatnonzero((~equal)&(np.arange(n)!=slot)); j=int(same[0]) if len(same) else slot
  batch=np.tile(w[0],(n,1));batch[j]=w[1]
  e=pilot.local_selected(batch);f=np.einsum('hi,bic->bhc',alpha,e,optimize=True)
  print('same batch slots',slot,j,'feature_A', [float(x).hex() for x in f[slot].flat], 'feature_B',[float(x).hex() for x in f[j].flat])
  base=float(f[slot,0,1]);scale=float(2**50);model.params={'a':np.zeros((2,8)),'W':np.zeros((9,32)),'b':np.zeros(32),'v':np.zeros(32),'c':np.zeros(1)};model.params['W'][1,0]=scale;model.params['b'][0]=-base*scale;model.params['v'][0]=1.
  q,c=model.forward(batch,cache=True);print('fixed readout', {'W_1_0':scale,'b_0':model.params['b'][0],'v_0':1,'q_A':float(q[slot]),'q_B':float(q[j]),'featureA':[float(x).hex() for x in c['x'][slot,:6]],'featureB':[float(x).hex() for x in c['x'][j,:6]]})
