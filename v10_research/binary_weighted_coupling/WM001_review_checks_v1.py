from pathlib import Path
import sympy as s
import json,hashlib
out=Path(__file__).resolve().parent
r,v=s.symbols('r v',positive=True)
P=s.Matrix([[1-r**3,r**3,0,0],[0,0,s.Rational(1,2),s.Rational(1,2)],[r,1-r,0,0],[0,0,r,1-r]])
D=1+r/2+2*r*r
pi=s.Matrix([[1,r*r,r*r,r/2]])/D
assert (pi*P-pi).applyfunc(s.factor)==s.zeros(1,4)
T=s.Matrix([[(1-r**3)**2,r*(1-r**3),r/2,r*r],[r/2,(1-r)/(2*r*r),1/(2*r),(1-r)/r],[r*(1-r**3),r*r,(1-r)/(2*r*r),(1-r)/r],[r*r,(1-r)/r,(1-r)/r,2*(1-r)**2/r]])
actual=s.Matrix(4,4,lambda i,j:(P*P)[i,j]/(D*pi[j]))
assert (T-actual).applyfunc(s.factor)==s.zeros(4)
# Substitution covers 0<r<=1/8 by v>=0; both polynomial coefficients nonnegative.
cert=[]
for i in range(4):
 for j in range(4):
  num,den=s.fraction(s.cancel((T[i,j]-r*r).subs(r,1/(8+v))))
  assert all(c>=0 for c in s.Poly(num,v).all_coeffs())
  assert all(c>=0 for c in s.Poly(den,v).all_coeffs()) and den.subs(v,0)>0
  cert.append({'cell':[i,j],'numerator':str(num),'denominator':str(den)})
exact=[]
for eps in [s.Rational(1,8),s.Rational(1,10),s.Rational(1,16)]:
 n=int(s.floor(1/(16*eps*eps)))
 K=P.subs(r,eps); pp=pi.subs(r,eps); U=K**n
 q=s.Matrix([eps**3,s.Rational(1,2),eps,eps])
 assert U[3,3]>=s.Rational(3,8)
 marginal=sum(abs(U[3,j]-pp[j])*q[j] for j in range(4))
 future=sum(abs(U[3,j]-pp[j])*(U*q)[j] for j in range(4))
 assert marginal>=5*eps/16 and future>=15*eps/128
 exact.append({'epsilon':str(eps),'n':n,'pcc':float(U[3,3]),'marginal':float(marginal),'future':float(future)})
result={'symbolic_stationarity':True,'symbolic_ratio_table':True,'domain_nonnegativity_certificates':cert,'exact_rational_horizons':exact}
(out/'WM001_review_checks_v1.json').write_text(json.dumps(result,indent=2)+'\n')
files=['WM001_full_support_weighted_mixing_obstruction_v1.md','WM001_diagnostics_v1.py','WM001_diagnostics_v1.json','WM001_source_bindings_v1.json']
(out/'WM001_review_bindings_v1.json').write_text(json.dumps({f:hashlib.sha256((out/f).read_bytes()).hexdigest() for f in files},indent=2)+'\n')
print('PASS: symbolic identities, all 16 domain inequalities, exact finite-horizon residuals.')
