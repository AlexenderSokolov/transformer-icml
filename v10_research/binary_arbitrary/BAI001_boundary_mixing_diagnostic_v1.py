"""Finite corroboration only; analytic certificate is in BAI001 section 6."""
import json
import numpy as np
rows=[]
for e in [.1,.01,.001]:
    M=int(1/e)
    P=np.array([[1.,0,0,0],[0,0,.5,.5],[e,1-e,0,0],[0,0,.5,.5]])
    pi=np.array([1.,0,0,0]); beta=e/2
    q=np.array([0.,.5,e,.5])
    mu=np.array([0.,1,0,0])@np.linalg.matrix_power(P,M)
    rows.append(dict(e=e,M=M,beta=beta,stationary_residual=float(abs(pi@P-pi).max()),
      minorization_min=float((P@P-beta*pi).min()),terminal_law=mu.tolist(),
      minority_weighted_terminal_mass=float(mu@q),analytic_lower=(1-e)**M/16,
      positive_a_exceptional_ratio=e*e*(1+3*e*e)))
print(json.dumps(rows,indent=2))
