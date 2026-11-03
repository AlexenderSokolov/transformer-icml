from itertools import product
from pathlib import Path
import importlib.util,sys
sys.dont_write_bytecode=True;p=Path(__file__).resolve().parents[1];spec=importlib.util.spec_from_file_location('author_verifier',p/'verify.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
checks=0
for M in range(1,9):
 for w in product((0,1),repeat=M+2):
  J=[0]*4;C=[0]*4;D=[0]*4
  for i in range(M):
   a,b,c=w[i:i+3];u=2*a+b;J[u]+=1;C[u]+=int(c==1-a);D[u]+=int(i<M//2)
  assert v.bank_of(w)==tuple(J+C+D)
  u=2*w[-2]+w[-1];assert v.bank_of(w,True)==(J[u],C[u],D[u]);checks+=1
 print('M',M,'cumulative independent literal word bank checks',checks)
print('PASS')
