"""Finite scalar checks, not proof or original-network execution."""
import math,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
checks=0
branches={k:0 for k in 'ABCD'}
def le(a,b):
    global checks
    checks+=1
    assert a<=b*(1+2e-12)+1e-300,(a,b)
def W(z,t): return (1+math.log1p(z/t))/z
Ms=sorted(set([64,65,127,128,255,256,257,1000,4095,4096,4097]+[2**j for j in range(6,501,7)]))
for M in Ms:
    a=math.sqrt(M); s=1/a
    betas=sorted(set([0,1/M**2,0.5/M**2,2/M**2,1/M,0.5/M,2/M,1/256,math.nextafter(1/256,1),1/8,1/2,1]+[2.**(-j) for j in range(1,501,17)]))
    Qs=sorted(set([16.,2.**max(4,math.floor(math.log2(a))),2.**max(4,math.ceil(math.log2(a))),2.**max(4,math.ceil(math.log2(M))),2.**max(4,math.ceil(1.25*math.log2(M)))]))
    for beta in betas:
        t=M*max(math.sqrt(beta),1/M)
        f=1+math.log1p(a/t); star=a*f
        for Q in Qs:
            kappas=sorted(set([1,2,3,16,100,10000]+[max(1,math.floor(v/Q)+e) for v in (M/4,M**.75,star) for e in (0,1)]))
            for k in kappas:
                z=k*Q; w=W(z,t)
                le(w,.25); le(W(2*z,t),w)
                if beta>1/256:
                    branch='A'; le(w,1/Q+2*s)
                elif z>M/4:
                    branch='B'; le(w,5*s)
                elif z>M**.75:
                    branch='C'; le(w,5*s)
                else:
                    branch='D'; x=z/t;y=M/z
                    le(x,z);le(math.log(z),3*math.log(y))
                    L=math.log1p(min(x,y)/8)/z
                    le(math.log1p(x),24*math.log1p(min(x,y)/8))
                    le(w,1/Q+24*L)
                branches[branch]+=1
                # Necessity scalar implication, including its exact premise boundary.
                B=max(1,a*w)
                le(star/B**2,z)
                for B in (1,2,10,100,10000):
                    if a*w<=B:
                        le(star/B**2,z)
                if Q>=a and z>=star: le(w,2*s)
        # Legal dyadic allocation and arbitrary fixed-factor sufficient thresholds.
        Q=2.**max(4,math.ceil(math.log2(a)))
        k=max(1,math.ceil(star/Q)); le(a,Q);le(Q,2*a);le(star,k*Q)
        le(W(k*Q,t),2*s)
        for b in (.001,.1,.5,1,2,10,1000):
            le(W(b*star,t),2*max(1,1/b)*s)
        le(W(star,t),2*s)
# Integer construction and direct real-envelope lower scalar inequalities.
for M in Ms:
    a=math.sqrt(M)
    for beta in (0,1/M**2,1/M,1/256,1):
        t=M*max(math.sqrt(beta),1/M)
        for Q in (max(16,a/2),max(16,a),max(16,2*a)):
            fq=1+math.log1p(Q/t); k=math.ceil(fq)
            le(fq,k); le(k,2*fq); le(W(k*Q,t),2/Q)
            for kr in (1.,1.001,2.5,17.25,1e6):
                le(fq/(kr*Q),W(kr*Q,t))
        if beta==1/M:
            le(1+math.log1p(a/t),1+math.log(2))
# Continuous cut-boundary checks independent of integer/dyadic realizability.
for M in Ms:
    for base in (M/4,M**.75):
        for z in (math.nextafter(base,0),base,math.nextafter(base,math.inf)):
            if z>=M/4: le(W(z,1),5/math.sqrt(M))
            if z>=M**.75: le(W(z,1),5/math.sqrt(M))
# Statistical elementary bound and source hash binding integrity.
for M in Ms:
    n=M+2;delta=1/(16*math.sqrt(n))
    kl=n*2*delta*(math.log1p(2*delta)-math.log1p(-2*delta))
    le(kl,1/8);le(1/(256*math.sqrt(M)),1/(128*math.sqrt(n)))
bindings=json.loads((HERE/'BS001_source_bindings_v1.json').read_text())
for source in bindings['sources']:
    assert hashlib.sha256((HERE.parent/source['path']).read_bytes()).hexdigest()==source['sha256']
result={'status':'PASS','scalar_assertions':checks,'branch_instances':branches,'M_count':len(Ms),'max_log2_M':math.log2(max(Ms)),'source_hashes_verified':len(bindings['sources']),'limitations':'Finite floating-point algebra checks only; not universal proof, formal verification, or original-network execution.'}
(HERE/'BS001_diagnostics_v1.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
