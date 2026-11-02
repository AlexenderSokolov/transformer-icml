"""Author/contributor diagnostics only; all research notes remain unreviewed."""
from fractions import Fraction as F
from pathlib import Path
from math import log,sqrt
import random,json,hashlib
root=Path(__file__).resolve().parent
rng=random.Random(202611021223)
states=((0,0),(0,1),(1,0),(1,1))
def pairP(a,b,e,t):
    th=(a,b,1-e,1-t)
    return [[(th[i] if z else 1-th[i]) if y==v else F(0) for v,z in states] for i,(x,y) in enumerate(states)]
def square(P):
    return [[sum((P[i][h]*P[h][j] for h in range(4)),F(0)) for j in range(4)] for i in range(4)]
def xlog(n,p):
    return 0. if n==0 else n*log(float(p))
counts={'stationary_flow_exact':0,'certificate_elimination_exact':0,'likelihood_numeric':0,'cost_split_exact':0}
max_log_excess=-float('inf');arg=None
for z in range(1500):
    a,b,e,t=[F(rng.randrange(1,100),100) for _ in range(4)]
    x=1/(e/a+2+b/t);y=x*e/a;w=x*b/t;pi=(y,x,x,w)
    P=pairP(a,b,e,t);P2=square(P)
    beta=min(P2[i][j]/pi[j] for i in range(4) for j in range(4))
    assert 0<beta<=1
    assert y*a==x*e and w*t==x*b
    assert e*e>=beta*y and b*b>=beta*w
    assert beta*x*x<=t*t*w and beta*x*x<=a*a*y
    assert beta*(y*a)**2<=t*t*w
    counts['stationary_flow_exact']+=1
    assert beta<=b*t/x==b*t*e/a+2*b*t+b*b
    assert b*t/x<=b*b+3*b*t/a
    counts['certificate_elimination_exact']+=1
    for _ in range(4):
        J=rng.randrange(1,10001);k=rng.randrange(1,J+1);L=rng.randrange(J,5*J+1)
        p=F(k,J);tmle=F(1,L+1)
        logell=xlog(1,t)+xlog(L,1-t)+xlog(k+1,e)+xlog(k,1-b)+xlog(k,a)+xlog(J-k,1-a)
        logmle=xlog(1,tmle)+xlog(L,1-tmle)+xlog(k,p)+xlog(J-k,1-p)
        rhs=log(4)-k*sqrt(float(beta))/8
        excess=logell-logmle-rhs
        assert excess<1e-8,(a,b,e,t,L,J,k,beta,excess)
        counts['likelihood_numeric']+=1
        if excess>max_log_excess:
            max_log_excess=excess;arg={'a':str(a),'b':str(b),'e':str(e),'t':str(t),'L':L,'J':J,'k':k,'beta':str(beta)}
        if a>=p/2:
            cost=k*b+F(L,2)*t
            if b*b>=beta/2:
                assert cost*cost>=F(k*k,2)*beta
            else:
                assert b*t>=beta*F(k,12*J)
                assert cost*cost>=F(k*k,6)*beta
            counts['cost_split_exact']+=1
out={'status':'PASS','review_status':'UNREVIEWED_CONTRIBUTOR_DIAGNOSTIC','counts':counts,
'arithmetic':'Fraction exact for flow, certificate and cost checks; floating logarithms only for explicitly numeric likelihood checks',
'maximum_likelihood_log_excess':max_log_excess,'corresponding_case':arg,
'notes_sha256':hashlib.sha256((root/'same_beta_route_barriers_unreviewed.md').read_bytes()).hexdigest(),
'limitation':'Finite diagnostics are not a proof or independent review; source notes explicitly retain supplied-beta full-history adaptation as open.'}
(root/'route_barriers_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
