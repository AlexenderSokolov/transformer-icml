import json,hashlib
from pathlib import Path
import numpy as np
import sympy as sp
root=Path(__file__).resolve().parent
r,h=sp.symbols('r h',positive=True);D=sp.Rational(3,2)+2*r
P=sp.Matrix([[1-r,r,0,0],[0,0,1-h,h],[sp.Rational(1,2),sp.Rational(1,2),0,0],[0,0,r*h,1-r*h]])
pi=sp.Matrix([[sp.Rational(1,2),r,r,1]])/D
assert (pi*P-pi).applyfunc(sp.simplify)==sp.zeros(1,4)
expected=sp.Matrix([[2*(1-r)**2,1-r,1-h,r*h],[1-h,(1-h)/(2*r),h*h,h*(1-r*h)],[1-r,sp.Rational(1,2),(1-h)/(2*r),h/2],[r*h,h/2,h*(1-r*h),(1-r*h)**2]])
actual=sp.Matrix(4,4,lambda i,j:(P*P)[i,j]/(D*pi[j]))
assert (actual-expected).applyfunc(sp.simplify)==sp.zeros(4,4)
checks=[]
for j in range(5,10):
 for power in [1,2,3]:
  rv=sp.Rational(1,2**j);hv=rv**power;sub={r:rv,h:hv};pr=P.subs(sub);pv=pi.subs(sub);dv=D.subs(sub)
  ratios=[(pr*pr)[i,k]/pv[k] for i in range(4) for k in range(4)]
  assert min(ratios)==hv*hv*dv
  n=int(1/(16*rv*hv)); U=np.linalg.matrix_power(np.array(pr,dtype=float),n);pif=np.array(pv,dtype=float)[0];q=np.array([float(rv),float(hv),.5,float(rv*hv)])
  marg=float(np.abs(U[0]-pif)@q);future=float(np.abs(U[0]-pif)@(U@q))
  assert U[0,0]>=.75-1e-5
  assert marg>=float(5*rv/12)-1e-5
  assert future>=float(5*rv/16)-1e-5
  checks.append(dict(epsilon=str(rv),h=str(hv),n=n,beta=str(hv*hv*dv),pww=float(U[0,0]),marginal=marg,future=future,marginal_over_sqrt_floor=marg*np.sqrt(n),future_over_sqrt_floor=future*np.sqrt(n)))
(root/'WM001_diagnostics_v2.json').write_text(json.dumps(dict(symbolic_stationarity=True,symbolic_all_cells=True,checks=checks),indent=2)+'\n')
files=['binary_upper/BU001_weighted_return_upper_v2.md','binary_stationary_frontier/BS001_binary_stationary_frontier_v1.md','binary_arbitrary/BAI001_arbitrary_initialization_obstructions_v1.md','binary_arbitrary/BAI003_uniform_absorbing_binary_upper_v2.md']
(root/'WM001_source_bindings_v2.json').write_text(json.dumps({f:hashlib.sha256((root.parent/f).read_bytes()).hexdigest() for f in files},indent=2)+'\n')
print('All symbolic and numeric checks pass; cases:',len(checks))
