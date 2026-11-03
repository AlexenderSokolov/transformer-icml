"""Two fixed binary words, fixed weights; no RNG or random initialization."""
import os,sys,platform,json,hashlib
from fractions import Fraction
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parents[2];sys.path.insert(0,str(P/'learned_position_pilot_20261103'));import pilot
M=1025;L=M//2;a=np.ones(M+2,dtype=np.int8);b=np.ones(M+2,dtype=np.int8);a[[515,518]]=0;b[[519,522]]=0
assert tuple(a[-2:])==tuple(b[-2:])==(1,1) and np.count_nonzero(a!=b)==4

def counts(w):
 H=[[0]*8 for _ in range(2)];J=C=D=E=0;u=tuple(w[-2:])
 for i in range(M):
  triple=tuple(map(int,w[i:i+3]));H[int(i>=L)][4*triple[0]+2*triple[1]+triple[2]]+=1
  if triple[:2]==u:
   J+=1;C+=triple[2];D+=int(i<L);E+=int(i<L)*triple[2]
 return (J,C,D,E),H
bank_a,ha=counts(a);bank_b,hb=counts(b);assert bank_a==bank_b==(1021,1019,512,512);print('M',M,'L',L,'endpoint',tuple(a[-2:]),'edit Hamming',int(np.count_nonzero(a!=b)),'bank',bank_a,'full triple halves equal',ha==hb,'H',ha)
J,C,D,E=bank_a;xs=[Fraction(J-C,M),Fraction(C,M),Fraction(D-E,L),Fraction(E,L),Fraction(J-D-C+E,M-L),Fraction(C-E,M-L),1,1,Fraction(1,M)];print('exact rational inputs',list(map(str,xs)))
model=pilot.Model.__new__(pilot.Model);model.mode='half';model.params={'a':np.zeros((2,8)),'W':np.zeros((9,32)),'b':np.zeros(32),'v':np.zeros(32),'c':np.zeros(1)}
model.params['W'][1,0]=2.**53;model.params['b'][0]=-float.fromhex('0x1.fd00bfd00bfd6p-1')*2.**53;model.params['v'][0]=1.;assert model.params['W'][1,0]==9007199254740992.
T=(C+1)/(J+2);print('target B',T,'exact',str(Fraction(C+1,J+2)),'epsilon',1/(M+2.)**2)
print('environment python',sys.version,'numpy',np.__version__,'platform',platform.platform(),'threads',{k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']});np.show_config()
for name,w in [('AB',np.stack([a,b])),('BA',np.stack([b,a])),('AA',np.stack([a,a])),('BB',np.stack([b,b])),('A',a[None,:]),('B',b[None,:])]:
 q,c=model.forward(w,cache=True);loss=pilot.cross_entropy(np.full(len(w),T),q);print(name,json.dumps({'feature1_hex':[float(v).hex() for v in c['x'][:,1]],'full_x_hex':[[float(v).hex() for v in x] for x in c['x']],'preactivation':(c['x']@model.params['W']+model.params['b'])[:,0].tolist(),'q':q.tolist(),'loss':loss.tolist()}))
 if name=='AB':
  assert c['x'][0,1].hex()=='0x1.fd00bfd00bfd6p-1' and c['x'][1,1].hex()=='0x1.fd00bfd00bfd7p-1';assert abs(q[0]-.5)<1e-15 and abs(q[1]-.6816993976515352)<1e-15 and loss[0]>loss[1]
 if name=='BA':assert abs(q[1]-.5)<1e-15 and abs(q[0]-.6816993976515352)<1e-15
print('legal transformation A->B k=4; identity A cost 0; no randomness or source/label enters CE selection')
for f in [P/'learned_position_pilot_20261103/pilot.py',Path(__file__)]:print('sha256',f.name,hashlib.sha256(f.read_bytes()).hexdigest())
