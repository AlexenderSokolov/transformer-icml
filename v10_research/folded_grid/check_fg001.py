from fractions import Fraction as F
from itertools import product
import json, pathlib, hashlib
ROOT=pathlib.Path(__file__).parent

def tent(x): return 2*min(x,1-x)
def labels(x,J,h):
    Q=2**h; out=[]
    for j in range(J):
        out.append((Q*x).__floor__())
        if j<J-1:
            for _ in range(h): x=tent(x)
    return out

def decode(ks,h):
    Q=2**h; lo,hi,a,b=F(0),F(1),F(1),F(0)
    for k in ks:
        if k==Q:
            p=(1-b)/a
            assert lo<=p<=hi
            return p,p
        u,v=(F(k,Q)-b)/a,(F(k+1,Q)-b)/a
        lo=max(lo,min(u,v)); hi=min(hi,max(u,v))
        assert lo<=hi
        if k%2: a,b=-Q*a,k+1-Q*b
        else: a,b=Q*a,Q*b-k
    return lo,hi

cases=0; endpoint_cases=0; maxerr=F(0); worst=None
for J in range(2,6):
  for h in range(1,5):
    D=2**(J*h)
    # Exhaust every fine-grid input for reasonable grids; otherwise boundary and deterministic samples.
    us=range(D+1) if D<=65536 else sorted(set([0,1,D//2-1,D//2,D//2+1,D-1,D]+[i*D//1000 for i in range(1001)]))
    for U in us:
      x=F(U,D); ks=labels(x,J,h); lo,hi=decode(ks,h)
      assert lo<=x<=hi and hi-lo<=F(1,D)
      # Independently execute integer lattice recurrence.
      V=U; ik=[]
      for j in range(J):
        ik.append((2**h*V)//D)
        if j<J-1:
          for _ in range(h): V=2*min(V,D-V)
      assert ik==ks
      endpoint_cases+=int(2**h in ks); cases+=1
for J in range(2,5):
  for h in range(1,4):
    D=2**(J*h)
    for M in range(1,101):
      for A in range(M+1):
        x=F(A,M); U=D*A//M; xhat=F(U,D)
        ks=labels(xhat,J,h); lo,hi=decode(ks,h)
        assert lo<=xhat<=x and x-lo<=F(2,D)
        ratio=(x-lo)*D
        if ratio>maxerr: maxerr=ratio; worst=[J,h,M,A]
        # Every intermediate exact lattice fold is within ideal Lipschitz bound.
        ideal,finite=x,xhat
        for r in range((J-1)*h+1):
          assert abs(ideal-finite)<=F(2**r,D)
          assert abs(ideal-finite)<=F(1,2**h)
          ideal,finite=tent(ideal),tent(finite)
        cases+=1
out={'status':'PASS','exact_cases':cases,'label_Q_cases':endpoint_cases,'max_error_in_Q_minus_J_units':str(maxerr),'worst_case':worst,'limits':'Finite exact arithmetic diagnostics, not proof nor emitted network audit','theorem_sha256':hashlib.sha256((ROOT/'FG001_theorem.md').read_bytes()).hexdigest()}
(ROOT/'FG001_diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
