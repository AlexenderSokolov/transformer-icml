"""Independent finite diagnostics for CA001 v3; not a formal proof or FA certificate."""
import numpy as np, math, json, hashlib
from pathlib import Path
rng=np.random.default_rng(30012026)
checks={}; violations=[]
def check(name, condition):
    checks[name]=checks.get(name,0)+1
    if not condition: violations.append(name)
# Triangular powers, actual entry row/square sums and local multiplicities.
for T in [2,3,8,16,32,67,129]:
 A=np.tril(np.ones((T,T)))/np.arange(1,T+1)[:,None]
 for L in range(1,7):
  Ap=np.linalg.matrix_power(A,L)
  w=1+np.log(T/np.arange(1,T+1))
  check('triangular_log_envelope',np.all(Ap[-1]<=w**(L-1)/T+1e-12))
  for a,b in [(0,1),(.3,.8),(1,0),(1.2,.4)]:
   K=(a+b)**L-a**L
   d=np.linalg.matrix_power(a*np.eye(T)+b*A,L)[-1,:-1]
   m=2*L-2; Im=sum(math.comb(m,k)*math.factorial(k) for k in range(m+1))
   check('entry_envelope',np.all(d<=K*w[:-1]**(L-1)/T+1e-10))
   check('actual_row_sum',sum(d)<=(a+b)**L+1e-10)
   check('square_integral_bound',np.dot(d,d)<=K*K*Im/T+1e-10)
   for r in [1,2,4,7]:
    e=np.array([sum(d[i:min(len(d),i+r)]) for i in range(len(d))])
    check('local_multiplicity_row',sum(e)<=r*(a+b)**L+1e-9)
    check('local_multiplicity_square',np.dot(e,e)<=r*r*K*K*Im/T+1e-9)
# Nonlinear score/value perturbations: arbitrary pair endpoints and dense masks.
for t in range(1,65):
 for k in range(15):
  x=rng.normal(size=t); y=rng.normal(size=t)
  c=1/3; mask=rng.choice(t,size=max(1,math.ceil(c*t)),replace=False)
  for ids,den in [(np.arange(t),1),(mask,c)]:
   def logits(z): return .7*np.tanh(z[-1]+z[ids])
   sx,sy=logits(x),logits(y)
   def softmax(z):
    e=np.exp(z-np.max(z));return e/sum(e)
   ax,ay=softmax(sx),softmax(sy)
   C=math.exp(1.4)/den; delta=np.abs(x-y)
   check('softmax_l1_weight_change',sum(abs(ax-ay))<=2*C/t*sum(abs(sx-sy))+1e-12)
   ox=ax@np.tanh(x[ids]); oy=ay@np.tanh(y[ids])
   bound=2*C*.7*delta[-1]+C*(1+1.4)/t*sum(delta)
   check('attention_query_key_value_bound',abs(ox-oy)<=bound+1e-12)
   # Positionwise .3 residual + .4 pooled value is .4-Lipschitz for sum norm.
   check('layer_recurrence',abs(.3*(x[-1]-y[-1])+.4*(ox-oy))<=.4*((1+2*C*.7)*delta[-1]+C*2.4/t*sum(delta))+1e-12)
# Stationarity/minorization, event probabilities and harmonic constants.
for M in [64,65,100,256,1024,10000]:
 for beta in [0,1/M,1/64,1/16]:
  b0=max(beta,1/M); alpha=1/(2*M); eta=b0-alpha
  for p in [.25,.37,.5,.75]:
   pi=np.array([eta/b0,alpha*(1-p)/b0,alpha*p/b0,0.])
   P=np.array([[1-alpha,alpha*(1-p),alpha*p,0], [eta,(1-eta)*(1-p),(1-eta)*p,0], [eta,(1-eta)*(1-p),(1-eta)*p,0],pi])
   check('source_stationarity',np.max(abs(pi@P-pi))<1e-12)
   check('all_state_minorization',np.all(P>=b0*pi-1e-12))
   for Q in [1,math.sqrt(M),M/4]:
    U=min(1/(4*b0),M*M/(4*Q*Q));J=math.floor(U+1e-12)
    check('suffix_domain',J>=4 and J<=M/4 and Q*math.sqrt(J)/M<=.5+1e-12)
    ej=pi[0]*(1-alpha)*alpha*(1-alpha)**(M-J)*(1-eta)**(J-1)
    check('rare_event_probability',ej>=1/(32*M)-1e-14)
    s=sum(1/(1+Q*j/M) for j in range(2,J+1))
    check('harmonic_constant',s>=M/(4*Q)*math.log1p(Q*J/M)-1e-12)
    check('harmonic_argument',Q*J/M>=(1/8)*min(Q/(M*b0),M/Q)-1e-12)
 for Q in [math.sqrt(M)*1.0001,M/4+1,M,100*M]:
  check('iid_large_Q_constant',1/(128*math.sqrt(M+2))>=1/(256*Q))
# Exact early-token averaging counterexample (real network, final input fixed zero).
early=[]
for T in [8,32,128,512,2048]:
 H=sum(1/i for i in range(1,T+1)); influence=H/T
 early.append({'T':T,'terminal_influence':influence,'T_times_influence':H})
 check('real_averaging_counterexample',abs(sum((1/i)/T for i in range(1,T+1))-influence)<1e-12)
report={'candidate_sha256':hashlib.sha256(Path('v10_research/causal_attention/CA001_causal_bounded_softmax_candidate_v3.md').read_bytes()).hexdigest(),'checks':checks,'total_checks':sum(checks.values()),'violations':violations,'early_token_actual_zero_logit_network':early,'scope':'Finite diagnostics supplement written analytic review; neither formal proof nor finite-arithmetic certification.'}
out=Path('v10_research/reviews/CA001_independent_checks_v3.json');out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
assert not violations
