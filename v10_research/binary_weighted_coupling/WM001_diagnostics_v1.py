import json, hashlib
from pathlib import Path
import numpy as np
import sympy as sp
root=Path(__file__).resolve().parent
checks=[]
for k in range(3,11):
 r=sp.Rational(1,2**k); D=1+r/2+2*r*r
 P=sp.Matrix([[1-r**3,r**3,0,0],[0,0,sp.Rational(1,2),sp.Rational(1,2)],[r,1-r,0,0],[0,0,r,1-r]])
 pi=sp.Matrix([[1,r*r,r*r,r/2]])/D
 assert pi*P==pi
 ratios=[(P*P)[i,j]/pi[j] for i in range(4) for j in range(4)]
 assert min(ratios)==r*r*D
 n=int(1/(16*r*r)); U=np.linalg.matrix_power(np.array(P,dtype=float),n); pf=np.array(pi,dtype=float)[0]
 q=np.array([float(r**3),.5,float(r),float(r)])
 marginal=float(np.abs(U[3]-pf)@q)
 future=float(np.abs(U[3]-pf)@(U@q))
 assert U[3,3]>=.375-1e-9
 assert marginal>=float(5*r/16)-1e-9
 assert future>=float(15*r/128)-1e-9
 checks.append(dict(epsilon=str(r),n=n,beta=str(r*r*D),pcc=float(U[3,3]),marginal=marginal,future=future,marginal_over_epsilon=marginal/float(r),future_over_epsilon=future/float(r)))
(root/'WM001_diagnostics_v1.json').write_text(json.dumps(dict(exact_checks_passed=True,checks=checks),indent=2)+'\n')
files=['binary_upper/BU001_weighted_return_upper_v2.md','binary_stationary_frontier/BS001_binary_stationary_frontier_v1.md','binary_arbitrary/BAI001_arbitrary_initialization_obstructions_v1.md','binary_arbitrary/BAI003_uniform_absorbing_binary_upper_v2.md']
(root/'WM001_source_bindings_v1.json').write_text(json.dumps({f:hashlib.sha256((root.parent/f).read_bytes()).hexdigest() for f in files},indent=2)+'\n')
print(json.dumps(checks,indent=2))
