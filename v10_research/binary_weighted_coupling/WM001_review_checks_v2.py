from pathlib import Path
import sympy as s
import json,hashlib
out=Path(__file__).resolve().parent
r,h,u,v=s.symbols('r h u v',positive=True)
P=s.Matrix([[1-r,r,0,0],[0,0,1-h,h],[s.Rational(1,2),s.Rational(1,2),0,0],[0,0,r*h,1-r*h]])
D=s.Rational(3,2)+2*r;pi=s.Matrix([[s.Rational(1,2),r,r,1]])/D
assert (pi*P-pi).applyfunc(s.factor)==s.zeros(1,4)
T=s.Matrix([[2*(1-r)**2,1-r,1-h,r*h],[1-h,(1-h)/(2*r),h*h,h*(1-r*h)],[1-r,s.Rational(1,2),(1-h)/(2*r),h/2],[r*h,h/2,h*(1-r*h),(1-r*h)**2]])
actual=s.Matrix(4,4,lambda i,j:(P*P)[i,j]/(D*pi[j]))
assert (T-actual).applyfunc(s.factor)==s.zeros(4)
cert=[]
for i in range(4):
 for j in range(4):
  # Every domain point is represented by u,v>=0.
  num,den=s.fraction(s.cancel((T[i,j]-h*h).subs({r:1/(32+u),h:1/((32+u)*(1+v))})))
  assert all(c>=0 for c in s.Poly(num,u,v).coeffs())
  assert all(c>=0 for c in s.Poly(den,u,v).coeffs()) and den.subs({u:0,v:0})>0
  cert.append({'cell':[i,j],'numerator':str(num),'denominator':str(den)})
exact=[]
for eps,hv in [(s.Rational(1,32),s.Rational(1,32)),(s.Rational(1,32),s.Rational(1,64)),(s.Rational(1,40),s.Rational(1,40))]:
 n=int(s.floor(1/(16*eps*hv)));K=P.subs({r:eps,h:hv});pp=pi.subs(r,eps);U=K**n
 q=s.Matrix([eps,hv,s.Rational(1,2),eps*hv])
 marginal=sum(abs(U[0,j]-pp[j])*q[j] for j in range(4))
 future=sum(abs(U[0,j]-pp[j])*(U*q)[j] for j in range(4))
 assert U[0,0]>=s.Rational(3,4) and marginal>=5*eps/12 and future>=5*eps/16
 exact.append({'epsilon':str(eps),'h':str(hv),'n':n,'pww':float(U[0,0]),'marginal':float(marginal),'future':float(future)})
result={'symbolic_stationarity':True,'symbolic_ratio_table':True,'all_domain_certificate_nonnegativity':cert,'exact_rational_horizons':exact}
(out/'WM001_review_checks_v2.json').write_text(json.dumps(result,indent=2)+'\n')
files=['WM001_full_support_weighted_mixing_obstruction_v2.md','WM001_diagnostics_v2.py','WM001_diagnostics_v2.json','WM001_source_bindings_v2.json','WM001_review_v1.md']
(out/'WM001_review_bindings_v2.json').write_text(json.dumps({f:hashlib.sha256((out/f).read_bytes()).hexdigest() for f in files},indent=2)+'\n')
print('PASS: symbolic two-parameter identities, all 16 whole-domain inequalities, exact finite-horizon residuals.')
