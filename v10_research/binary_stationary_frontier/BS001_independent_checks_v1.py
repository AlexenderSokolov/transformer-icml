"""Independently designed finite BS001 checks; no author diagnostic imported."""
import json, math, random, hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rng=random.Random(202611020602)
counts={k:0 for k in ['cases','A','B','C','D','threshold_necessity','threshold_sufficiency','integer_allocation','receipt_hashes']}
maxima={'A_ratio':0.,'B_W_over_s':0.,'C_W_over_s':0.,'D_ratio':0.,'suff_aW':0.,'band_QW':0.}
def le(x,y):
    assert x<=y*(1+2e-12)+1e-14, (x,y)
def W(z,t):return (1+math.log1p(z/t))/z
Ms=[64,65,127,128,255,256,257,1024,4096,65536,10**6,10**12,10**24,10**48]
cases=[]
for M in Ms:
    betas=[0,1,1/M**2,1/M,1/256,math.nextafter(1/256,0),math.nextafter(1/256,1)]
    for beta in betas:
        # Include real-envelope branch boundaries, beyond actual integer theorem.
        for z in [16, M/4,math.nextafter(M/4,math.inf),M**.75,math.nextafter(M**.75,math.inf),M, M*M]:
            cases.append((M,beta,16,z/16))
        for h in [4,5, max(4,math.ceil(math.log2(math.sqrt(M)))),max(4,math.ceil(math.log2(M)))]:
            for k in [1,2,3,17,1024]:cases.append((M,beta,2**h,k))
for _ in range(25000):
    M=math.exp(rng.uniform(math.log(64),math.log(1e60)))
    beta=0 if rng.random()<.1 else math.exp(rng.uniform(-300,0))
    Q=2**rng.randint(4,110)
    k=math.exp(rng.uniform(0,100))
    cases.append((M,beta,Q,k))
for M,beta,Q,k in cases:
    a=math.sqrt(M); s=1/a; t=M*max(math.sqrt(beta),1/M); z=k*Q
    value=W(z,t); counts['cases']+=1
    le(value, .25)
    if beta>1/256:
        bound=1/Q+2*s;le(value,bound);counts['A']+=1
        maxima['A_ratio']=max(maxima['A_ratio'],value/bound)
    if z>M/4:
        le(value,5*s);counts['B']+=1
        maxima['B_W_over_s']=max(maxima['B_W_over_s'],value/s)
    if z>M**.75:
        le(value,5*s);counts['C']+=1
        maxima['C_W_over_s']=max(maxima['C_W_over_s'],value/s)
    if beta<=1/256 and z<=min(M/4,M**.75):
        L=math.log1p(min(z/t,M/z)/8)/z
        bound=1/Q+24*L;le(value,bound);counts['D']+=1
        maxima['D_ratio']=max(maxima['D_ratio'],value/bound)
    # Direct universal inversion, take a B satisfying both hypotheses.
    f=1+math.log1p(a/t); Z=a*f
    B=max(1,a/Q,a*value)
    le(a/B,Q);le(Z/(B*B),z);counts['threshold_necessity']+=1
    le(W(Z,t),2/a);counts['threshold_sufficiency']+=1
    maxima['suff_aW']=max(maxima['suff_aW'],a*W(Z,t))
    # Actual budget allocation: integer envelope and legal dyadic grid.
    QQ=2**max(4,math.ceil(math.log2(a))); kk=max(1,math.ceil(Z/QQ))
    le(a,QQ);le(QQ,2*a);le(Z,kk*QQ);le(W(kk*QQ,t),2/a)
    ff=1+math.log1p(QQ/t); kk2=math.ceil(ff)
    le(kk2,2*ff);le(W(kk2*QQ,t),2/QQ)
    maxima['band_QW']=max(maxima['band_QW'],QQ*W(kk2*QQ,t))
    counts['integer_allocation']+=1
bindings={}
for unit in ['BU001','BI001','UI001','TR001','SB001']:
    rec=root/'intake'/f'{unit}_acceptance.json'; j=json.loads(rec.read_text())
    proof=root/j['proof']; actual=hashlib.sha256(proof.read_bytes()).hexdigest()
    assert actual==j['sha256'],unit
    bindings[unit]={'proof':str(proof.relative_to(root)),'sha256':actual,'receipt_sha256':hashlib.sha256(rec.read_bytes()).hexdigest()}
    counts['receipt_hashes']+=1
out={'status':'PASS','counts':counts,'maxima':maxima,'bindings':bindings,
     'limits':'Finite floating-point scalar checks with relative tolerance 2e-12; exact receipt SHA-256 checks. Not a proof, full kernel re-audit, formal verification or external review.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
