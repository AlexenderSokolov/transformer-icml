from itertools import product, combinations
from fractions import Fraction as F
from collections import defaultdict
M=4; k=1
sources=[([F(1,8),F(3,8),F(5,8),F(7,8)],[F(1,10),F(2,10),F(3,10),F(4,10)]),([F(2,7),F(1,7),F(6,7),F(3,7)],[F(4,10),F(3,10),F(2,10),F(1,10)])]
weights=[F(2,5),F(3,5)]
def prob(h,theta,mu):
    out=mu[2*h[0]+h[1]]
    for i in range(M):
        q=theta[2*h[i]+h[i+1]]
        out*= q if h[i+2] else 1-q
    return out
def sig(h):
    n=[0]*8
    for i in range(M): n[4*h[i]+2*h[i+1]+h[i+2]]+=1
    return tuple(h[:2]+h[-2:]+tuple(n))
def pred(z):
    return F((2*z[0]+z[1]+3*z[-1])%5,4)
def edits(h):
    for j in range(k+1):
        for ix in combinations(range(M),j):
            a=list(h)
            for i in ix: a[i]=1-a[i]
            yield tuple(a)
groups=defaultdict(set); target=F(0); g=F(0); sourcevar=F(0); supervised=F(0); labelvar=F(0); lsa=F(0)
for h in product(range(2),repeat=M+2):
    ws=[w*prob(h,t,m) for w,(t,m) in zip(weights,sources)]; mass=sum(ws)
    if not mass:continue
    qs=[t[2*h[-2]+h[-1]] for t,_ in sources]; p=sum(w*q for w,q in zip(ws,qs))/mass
    groups[sig(h)].add(p)
    v=sum(w*(q-p)**2 for w,q in zip(ws,qs))/mass
    gp=max((pred(z)-p)**2 for z in edits(h))
    direct=max(sum(w*(pred(z)-q)**2 for w,q in zip(ws,qs))/mass for z in edits(h))
    obs=max((1-p)*pred(z)**2+p*(1-pred(z))**2 for z in edits(h))
    labelmax=(1-p)*max(pred(z)**2 for z in edits(h))+p*max((1-pred(z))**2 for z in edits(h))
    assert direct==gp+v and obs==gp+p*(1-p)
    g+=mass*gp;sourcevar+=mass*v;target+=mass*direct
    labelvar+=mass*p*(1-p);supervised+=mass*obs;lsa+=mass*labelmax
assert all(len(ps)==1 for ps in groups.values())
assert target==g+sourcevar and supervised==g+labelvar and lsa>=supervised
print('words:',2**(M+2),'groups:',len(groups),'colliding groups:',sum(1 for key in groups if sum(sig(h)==key for h in product(range(2),repeat=M+2))>1))
print('identity verified exactly; legal true-source squared risk:',target,'supervised:',supervised,'label-aware:',lsa)
