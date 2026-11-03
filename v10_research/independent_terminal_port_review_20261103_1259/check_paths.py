from itertools import product
from collections import defaultdict
from fractions import Fraction as F
import json
from functools import lru_cache

def stats(bits):
 J=[0]*4; C=[0]*4
 for i in range(2,len(bits)):
  z=2*bits[i-2]+bits[i-1];J[z]+=1;C[z]+=bits[i]
 q=2*bits[-2]+bits[-1];A=C[0]+C[1];B=C[0]+C[2];return J,C,q,A,B

def possible(J,C,A,B,end,start=None):
 vals=[]
 for x in range(J[0]+1):
  c=(x,A-x,B-x,C-A-B+x)
  if any(z<0 or z>j for z,j in zip(c,J)):continue
  counts=tuple(v for j,z in zip(J,c) for v in (j-z,z))
  @lru_cache(None)
  def dfs(pos, e):
   if not sum(e):return pos==end
   for b in (0,1):
    k=2*pos+b
    if e[k]:
     f=list(e);f[k]-=1
     if dfs(2*(pos%2)+b,tuple(f)):return True
   return False
  if any(dfs(a,counts) for a in ((start,) if start is not None else range(4))):vals.append(x)
 return vals

out=open('paths.jsonl','x'); counter=0
for N in range(3,9):
 words=list(product((0,1),repeat=N)); groups=defaultdict(set); starts=defaultdict(set)
 for b in words:
  J,C,q,A,B=stats(b);key=(q,tuple(J),sum(C),A,B); groups[key].add(C[0]); starts[(key,2*b[0]+b[1])].add(C[0])
 for b in words:
  J,C,q,A,B=stats(b); key=(q,tuple(J),sum(C),A,B); start=2*b[0]+b[1]; full=possible(J,sum(C),A,B,q); fixed=possible(J,sum(C),A,B,q,start)
  assert set(full)==groups[key] and set(fixed)==starts[(key,start)]
  heads=[]
  for coordinate, epos in [(0,F(2)),(1,F(1,2))]:
   query=b[-2+coordinate]; eq=[j for j in range(4) if ((j//2 if coordinate==0 else j%2)==query)]; jm=sum(J[j] for j in eq); cm=sum(C[j] for j in eq); M=N-2;D=epos*jm+(1/epos)*(M-jm);v=(epos*cm+(1/epos)*(sum(C)-cm))/D
   recovered=(D*v-(1/epos)*sum(C))/(epos-(1/epos));assert recovered==cm
   heads.append({'exp_beta':str(epos),'matching_J':jm,'matching_C':cm,'D':str(D),'q':str(v),'recovered':str(recovered)})
  vals=[(F((x if q==0 else A-x if q==1 else B-x if q==2 else sum(C)-A-B+x)+1,J[q]+2)) for x in full];radius=(max(vals)-min(vals))/2
  assert radius==F(max(full)-min(full),2*(J[q]+2))
  record={'N':N,'word':''.join(map(str,b)),'start':start,'terminal':q,'J':J,'C_by_state':C,'C_total':sum(C),'A':A,'B':B,'F_any_start':full,'F_fixed_start':fixed,'alpha':1,'B_values':list(map(str,vals)),'radius':str(radius),'heads':heads};out.write(json.dumps(record,sort_keys=True)+'\n');counter+=1
out.close();print('PASS:',counter,'fully retained cases; exact group-vs-Euler feasibility, both start modes, α=1 radius, signed β rational inversion.')
