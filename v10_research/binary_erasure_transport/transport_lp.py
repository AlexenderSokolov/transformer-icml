"""Microcanonical renewal-word transport diagnostic, not asymptotic proof."""
import itertools, math,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

def words(s,l):
 n=s+l
 return [''.join('101' if i in inds else '01' for i in range(n)) for inds in map(set,itertools.combinations(range(n),l))]
def solve(s,l):
 x=words(s,l); y=words(s+3,l-2); a=len(x); b=len(y)
 if a*b>2000000:return None
 xx=np.array([[int(c) for c in w] for w in x]); yy=np.array([[int(c) for c in w] for w in y])
 d=np.sum(xx[:,None,:]!=yy[None,:,:],axis=2)
 A=lil_matrix((a+b,a*b))
 for i in range(a): A[i,i*b:(i+1)*b]=1
 for h in range(b): A[a+h,h::b]=1
 eq=np.r_[np.full(a,1/a),np.full(b,1/b)]
 r=linprog(d.ravel(),A_eq=A.tocsr(),b_eq=eq,bounds=(0,None),method='highs')
 assert r.success,r.message
 return dict(s=s,l=l,j=2*s+3*l,source_size=a,target_size=b,min_expected_hamming=r.fun,nearest_min=int(d.min()),worst_nearest_source=int(d.min(axis=1).max()),worst_nearest_target=int(d.min(axis=0).max()))
if __name__=='__main__':
 out=[]
 for l in [2,3,4,5,6]:
  for s in [0,1,2,3,4,6,8,10]:
   z=solve(s,l)
   if z:out.append(z); print(z,flush=True)
 with open('v10_research/binary_erasure_transport/transport_lp_results.json','w') as f:json.dump(out,f,indent=2)
