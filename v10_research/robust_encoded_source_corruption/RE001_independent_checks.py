#!/usr/bin/env python3
"""Independent exact diagnostics for RE001; not formal verification or emitted evaluator audit."""
from fractions import Fraction as F
from itertools import product
from math import isqrt
from collections import Counter
from pathlib import Path
import hashlib, json, random, time
ROOT=Path(__file__).resolve().parents[1]; HERE=Path(__file__).resolve().parent
START=time.time()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def clip(x,lo=F(0),hi=F(1)): return max(lo,min(hi,x))
def floorq(x,Q): return F((x*Q).__floor__(),Q)
def le_root(v,a,b):
    """Exact v<=a+sqrt(b)."""
    return v<=a or (v-a)**2<=b

def comp_table(L):
    points=[F(0),F(1,4**L)]+[F(1,4**j) for j in reversed(range(L))]
    vals=[F(0)]; slopes=[2**L]+[2**j for j in reversed(range(L))]
    for a,b,s in zip(points,points[1:],slopes): vals.append(vals[-1]+s*(b-a))
    return list(zip(points,vals))
def g(x,L):
    ts=comp_table(L)
    for (a,ga),(b,gb) in zip(ts,ts[1:]):
        if a<=x<=b:return ga+(x-a)*(gb-ga)/(b-a)
    raise AssertionError((x,L))
def gi(z,L):
    ts=comp_table(L)
    for (a,ga),(b,gb) in zip(ts,ts[1:]):
        if ga<=z<=gb:return a+(z-ga)*(b-a)/(gb-ga)
    raise AssertionError((z,L))
def upper_root(r,eps):
    if eps==0:return F(0)
    p=0
    while F(1,2**p)>eps:p+=1
    v=r*2**(2*p);j=isqrt(v.numerator//v.denominator)
    if j*j*v.denominator<v.numerator:j+=1
    S=F(j,2**p)
    assert S*S>=r
    assert S<=eps or (S-eps)**2<=r
    return S

def counts(word): return Counter(tuple(word[j:j+3]) for j in range(len(word)-2))
result={"status":"PASS","scope":"Independent exact rational/algebra/geometry/schedule checks; no expected-risk Monte Carlo, no complete emitted generic-FA evaluator audit, not formal verification."}
# Exhaust all protected-pair word pairs in two alphabets; no edit separation.
pairs=[];editchecks=0
for K,M in [(2,4),(3,3)]:
    prefixes=list(product(range(K),repeat=M))
    for end in product(range(K),repeat=2):
        for pre in prefixes:
            word=pre+end;c=counts(word)
            assert sum(c.values())==M
            for pre2 in prefixes:
                word2=pre2+end;c2=counts(word2);k=sum(a!=b for a,b in zip(pre,pre2))
                l1=sum(abs(c[z]-c2[z]) for z in c.keys()|c2.keys())
                assert l1<=6*k
                x=[F(c[end+(b,)],M) for b in range(K)]
                xp=[F(c2[end+(b,)],M) for b in range(K)]
                J=sum(word[j:j+2]==end for j in range(M))
                assert sum(x)==F(J,M) and sum(abs(a-b) for a,b in zip(x,xp))<=F(6*k,M)
                if editchecks%9==0:pairs.append((K,M,k,x,xp,J,end))
                editchecks+=1
# Include legal M domain, edit all first M symbols in some instances, protected endpoint fixed.
rng=random.Random(28274601)
for _ in range(350):
    K=rng.choice([2,3,4]);M=rng.choice([64,65,127,256]);k=rng.choice([0,1,2,M//2,M])
    w=tuple(rng.randrange(K) for _ in range(M+2));z=list(w)
    for j in rng.sample(range(M),k):z[j]=(z[j]+rng.randrange(1,K))%K
    c,c2=counts(w),counts(z);end=w[-2:]
    assert tuple(z[-2:])==end
    assert sum(abs(c[a]-c2[a]) for a in c.keys()|c2.keys())<=6*k
    x=[F(c[end+(b,)],M) for b in range(K)];xp=[F(c2[end+(b,)],M) for b in range(K)]
    pairs.append((K,M,k,x,xp,int(sum(x)*M),end))
result['exhaustive_protected_word_pair_checks']=editchecks
result['theorem_domain_random_word_pairs']=350
# Exact symmetric inverse, new edit composition, normalized outputs and local binary envelope.
rowchecks=binchecks=zerorows=falsemass=0
for K,M,k,x,xp,J,end in pairs:
    r=sum(x)
    for L,eps in [(0,F(0)),(1,F(1,64)),(4,F(1,1024))]:
        tau=F(k,M)+eps**2+eps/F(2**L)
        for sg in [tuple(1 for _ in x),tuple(-1 for _ in x),tuple(1 if j%2 else -1 for j in range(K))]:
            y=[gi(clip(g(v,L)+q*eps,F(0),g(F(1),L)),L) for v,q in zip(xp,sg)]
            for v,w in zip(xp,y): assert le_root(abs(w-v),4*eps**2+2*eps/F(2**L),16*eps**2*v)
            d=sum(abs(v-w) for v,w in zip(x,y))
            a=F(12*k,M)+8*K*eps**2+2*K*eps/F(2**L)
            assert le_root(d,a,16*K*eps**2*r)
            den=r+F(K,M);den2=sum(y)+F(K,M)
            p=[(v+F(1,M))/den for v in x];ph=[(v+F(1,M))/den2 for v in y]
            tv=sum(abs(v-w) for v,w in zip(p,ph))/2
            assert sum(ph)==1 and min(ph)>=0 and tv<=min(F(1),d/den)
            rowchecks+=1
            if J==0:zerorows+=1;falsemass+=int(sum(y)>0)
            if K==2:
                S=upper_root(sum(y),eps);Bhat=12*eps*S+68*tau
                assert d<=Bhat and le_root(Bhat,132*tau,324*eps**2*r)
                B=M*Bhat;exitbit=1-end[0];C=M*x[exitbit]
                qh=max(F(0),M*y[exitbit]-B)/(M*sum(y)+B+2)
                assert 0<=qh<=C/F(J+2)
                for q in [F(0),F(1,7),F(1,2),F(6,7),F(1)]:
                    emp=abs(C/F(J)-q) if J else F(0)
                    weighted=min(q,(528*M*tau+2)/F(J+2))
                    rem=abs(qh-q)-2*emp-weighted
                    assert rem<=0 or rem**2<=72**2*eps**2*F(M,J+2)
                    binchecks+=1
result.update(row_inverse_composition_normalization_checks=rowchecks,binary_exact_pathwise_checks=binchecks,empty_clean_row_checks=zerorows,artificial_positive_empty_row_checks=falsemass)
# Independent recursive rational edge construction; no borrowed author geometry code.
def edges(R,N):
    if R==1:return [(F(0),F(1),(F(0),),(F(1),))]
    child=edges(R-1,N);eta=F(1,2*N**(R-1)+2);out=[]
    for i in range(N):
        for a,b,x,y in (child if i%2==0 else reversed(child)):
            if i%2:a,b,x,y=1-b,1-a,y,x
            out.append(((i+(1-eta)*a)/N,(i+(1-eta)*b)/N,x+(F(i,N),),y+(F(i,N),)))
        last=out[-1][3]
        out.append(((i+1-eta)/N,F(i+1,N),last,last[:-1]+(F(i+1,N),)))
    return out

def point(t,es):
    for a,b,x,y in es:
        if a<=t<=b:return tuple(xx+(t-a)/(b-a)*(yy-xx) for xx,yy in zip(x,y))
    raise AssertionError(t)
def nearest(q,es):
    best=None
    for num,(a,b,x,y) in enumerate(es):
        axis=next(j for j,(xx,yy) in enumerate(zip(x,y)) if xx!=yy)
        f=clip((q[axis]-x[axis])/(y[axis]-x[axis]));z=tuple(xx+f*(yy-xx) for xx,yy in zip(x,y))
        rec=(sum((zz-qq)**2 for zz,qq in zip(z,q)),num,a+f*(b-a))
        if best is None or rec[:2]<best[:2]:best=rec
    return best[2]
geom=clipchecks=0
for R,N in [(2,2),(2,4),(2,8),(3,2),(3,4),(4,2)]:
    Q=1<<((64*R*N-1).bit_length());rho=F(1,Q);u=rho+F(2,Q);eps=8*R*u/F(N**(R-1));es=edges(R,N)
    assert 4*R*u*N<=1
    assert es[0][0]==0 and es[-1][1]==1
    assert all(es[i][1]==es[i+1][0] for i in range(len(es)-1))
    xs={F(0),F(1)}|{a for a,b,x,y in es}|{b for a,b,x,y in es}|{F(j,17) for j in range(18)}
    for t in xs:
        ideal=point(t,es)
        for fs in product([-1,1],repeat=R):
            raw=tuple(v+F(s,Q) for v,s in zip(ideal,fs));actual=tuple(clip(v) for v in raw)
            for z,a,v in zip(raw,actual,ideal):
                assert 0<=a<=1 and abs(a-v)<=abs(z-v)<=F(1,Q);clipchecks+=1
            for signs in [fs,tuple(-z for z in fs)]:
                q=tuple(floorq(clip(a+rho*s),Q) for a,s in zip(actual,signs))
                th=nearest(q,es)
                assert (th-t)**2<=8*R*u*u/F(N**(2*(R-1)))
                assert 2*abs(th-t)<=eps
                geom+=1
result.update(packed_exact_tube_noise_geometry_checks=geom,pre_fault_exact_clip_checks=clipchecks)
# Exact finite-scale rational schedule (no float logs/roots). Include budgets unlike c/Q.
sched=snake=scalar=0
for R in range(2,7):
    for M in [64,65,127,128,255,256,1023,1024]+[2**j+r for j in range(12,101,4) for r in [-1,0,1]]:
        jj=(M.bit_length()-1)//2;t0=F(1,2**jj)
        assert t0*t0*M>=1 and t0*t0*M<4
        m=(M+1).bit_length();chi=2**((m-1).bit_length());assert m<=chi<2*m
        for h in range(1,35):
            Q=2**h
            for rho in [F(0),F(1,Q),F(3,2*Q),F(1,2**max(1,h//2))]:
                u=rho+F(2,Q)
                if u**R>t0/F((8*R)**(R-1)):continue
                if u<=t0:epsilon=2*u;scalar+=1
                else:
                    N=2
                    while t0*N**(R-1)<u:N*=2
                    assert 4*R*u*N<=1
                    assert N==2 or t0*(N//2)**(R-1)<u
                    epsilon=8*R*u/F(N**(R-1));snake+=1
                assert epsilon<=8*R*t0
                sched+=1
result.update(exact_finite_scale_schedule_checks=sched,scalar_schedule_checks=scalar,snake_schedule_checks=snake)
# Arbitrarily long full target descriptions can coexist with tiny selected N.
# This corroborates the review's need to charge b_t0, not just output scale.
longtargets=0
for B in [128,1024,4096]:
    Q=256;u=F(3,Q);t0=F((1<<B)+1,1<<(B+6));R=2
    assert u<t0 and t0.numerator.bit_length()>B
    assert u**R<=t0/F((8*R)**(R-1))
    longtargets+=1
result['long_full_description_scalar_target_cases']=longtargets

# Exact accepted-source hashes including component proofs, with current separate clip note.
receipts={}
for unit in ['MG001','MG002','GD001','GN001','JP001','SC002','SC003','BT002']:
    rp=ROOT/'intake'/f'{unit}_acceptance.json';r=json.loads(rp.read_text())
    assert r['status']=='ROOT_ACCEPTED_AFTER_INDEPENDENT_LLM_REVIEW'
    assert sha(ROOT/r['proof'])==r['sha256']
    comp=r.get('component_proofs',{})
    for p,h in comp.items():assert sha(ROOT/p)==h
    receipts[unit]={'receipt_sha256':sha(rp),'proof_sha256':r['sha256'],'component_count':len(comp)}
result['dependency_receipts']=receipts
result['clip_clarification_sha256']=sha(ROOT/'robust_markov_prediction/MG_final_clip_clarification.md')
result['clip_review_sha256']=sha(ROOT/'robust_markov_prediction/MG_final_clip_clarification_independent_review.md')
result['theorem_sha256']=sha(HERE/'RE001_theorem.md')
result['script_sha256']=sha(Path(__file__))
result['elapsed_seconds']=round(time.time()-START,3)
(HERE/'RE001_independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
