#!/usr/bin/env python3
"""Fixed-input, fixed-readout reproduction. No generator or Model constructor invoked."""
import sys,os,platform,json
import numpy as np
sys.path.insert(0,os.path.abspath('v10_research/learned_position_pilot_20261103'));import pilot
sys.path.insert(0,os.path.abspath('v10_research/four_counter_dp_20261103'));import four_counter
M=1025; a=np.ones(M+2,dtype=np.int8);b=a.copy();a[[515,518]]=0;b[[519,522]]=0
model=pilot.Model.__new__(pilot.Model);model.mode='half';model.params={'a':np.zeros((2,8)),'W':np.zeros((9,32)),'b':np.zeros(32),'v':np.zeros(32),'c':np.zeros(1)}
model.params['W'][1,0]=2.**53;model.params['b'][0]=-float.fromhex('0x1.fd00bfd00bfd6p-1')*2.**53;model.params['v'][0]=1.
print('python',sys.version,'numpy',np.__version__,'platform',platform.platform(),'thread_env',{k:os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')});np.show_config()
print('zeros A/B',[515,518],[519,522],'Hamming',int(np.sum(a!=b)),'bankA',four_counter.feature_bank(tuple(map(int,a))),'bankB',four_counter.feature_bank(tuple(map(int,b))))
for name,batch in [('AB',np.stack([a,b])),('BA',np.stack([b,a])),('AA',np.stack([a,a])),('BB',np.stack([b,b]))]:
 q,cache=model.forward(batch,cache=True);B=pilot.statistics(a[None,:])['B'][0];loss=pilot.cross_entropy(np.full(2,B),q)
 print(name,json.dumps({'x':[[float(x).hex() for x in row] for row in cache['x']], 'q':q.tolist(),'q_hex':[float(x).hex() for x in q],'hidden0':cache['hidden'][:,0].tolist(),'clean_target_B':float(B),'cross_entropy':loss.tolist()}))
