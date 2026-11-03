import csv,json,hashlib,math,itertools,importlib.util
from pathlib import Path
from fractions import Fraction
import numpy as np
R=Path(__file__).resolve().parent; B=R.parent
spec=importlib.util.spec_from_file_location('reviewed',R/'replay/experiment.py'); e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
checks={}; bindings={}
for manifest in ['PRE_RUN_HASHES.json','ARTIFACT_HASHES.json']:
    m=json.loads((B/manifest).read_text())
    for f,h in m.items():
        actual=hashlib.sha256((B/f).read_bytes()).hexdigest(); assert h==actual,(f,h,actual);bindings[f]=actual
checks['all_original_manifest_bindings_match']=True
rows=list(csv.DictReader((B/'aggregates.csv').open())); batches=list(csv.DictReader((B/'batch_means.csv').open())); jr=json.loads((B/'results.json').read_text())['results']; maxerr=0
assert len(rows)==70 and len(batches)==7000
for row,rr in zip(rows,jr):
    m=int(row['M']); k=row['metric']; matches=[r for r in batches if int(r['M'])==m and r['metric']==k]
    assert [int(r['batch']) for r in matches]==list(range(100))
    x=[float(r['mean']) for r in matches]; avg=math.fsum(x)/100; se=math.sqrt(math.fsum((v-avg)**2 for v in x)/99)/10
    for key,value in [('mean',avg),('MC_SE',se),('approx95_low',avg-1.96*se),('approx95_high',avg+1.96*se)]:
        err=abs(value-float(row[key]));maxerr=max(err,maxerr);assert err<3e-16,(m,k,key,err); assert float(row[key])==rr[key]
checks['recomputed_70_aggregates_from_7000_batches_max_error']=maxerr
for f in ['aggregates.csv','batch_means.csv','synthetic_clean_objective.png']:
    assert (B/f).read_bytes()==(R/'replay'/f).read_bytes(),f
checks['full_replay_CSVs_and_PNG_byte_identical']=True
# Independent literal scalar path engine, intentionally no author's from_words or literal oracle.
ncase=0
rng=np.random.Generator(np.random.PCG64(8816027))
for M in [0,1,2,3,5,17,63,64,65,128,256,512,1024,2048,4096]:
    n=19;p=rng.random((n,4));start=rng.integers(0,4,size=n);vs=rng.random((M,n));z=e.simulate(p,start,M,uniforms=vs)
    for i in range(n):
        w=[int(start[i])//2,int(start[i])%2]
        for t in range(M): w.append(int(vs[t,i]<p[i,2*w[-2]+w[-1]]))
        u=2*w[-2]+w[-1];selected=[t for t in range(M) if w[t:t+2]==w[-2:]]
        J=len(selected); C=sum(w[t+2]==1-w[-2] for t in selected);D=sum(t<M//2 for t in selected)
        b=(sum(w[t+2] for t in selected)+1)/(J+2);acc=J>0 and 512*D>=J;a=C/J if acc else 0;a=a if w[-2]==0 else 1-a
        for k,v in [('J',J),('C',C),('D',D),('B',b),('A',a),('accepted',acc),('u',u),('p',p[i,u])]:assert z[k][i]==v,(M,i,k)
        if M>=64:
            q=(1-2/math.sqrt(M))*a+1/math.sqrt(M);out=e.metrics({k:v[i:i+1] for k,v in z.items()},M)
            cross=-b*math.log(q)-(1-b)*math.log1p(-q)
            kl=b*math.log(b/q)+(1-b)*math.log((1-b)/(1-q))
            assert abs(out['expected_logloss_Q'][0]-cross)<1e-14
            assert abs(out['excess_KL_B_Q'][0]-kl)<1e-14
        ncase+=1
checks['independent_scalar_cases']=ncase
# Independent exact-rational integrated likelihood and extension, M=0..8.
def counts(w):
    return [[sum(w[t:t+2]==(a,b) and w[t+2]==c for t in range(len(w)-2)) for c in (0,1)] for a,b in itertools.product((0,1),repeat=2)]
def mass(w):
    out=Fraction(1,4)
    for n0,n1 in counts(w):out*=Fraction(math.factorial(n0)*math.factorial(n1),math.factorial(n0+n1+1))
    return out
nw=0
for M in range(9):
    total=Fraction(0)
    for w in itertools.product((0,1),repeat=M+2):
        h=counts(w);a,b=h[2*w[-2]+w[-1]];mw=mass(w); total+=mw
        assert mass(w+(1,))/mw==Fraction(b+1,a+b+2);nw+=1
    assert total==1
checks['independent_exact_rational_words']=nw
weak=[]
for r in rows:
    if r['metric']=='weak_tail':
        M=int(r['M']);exact=1-(1-2/math.sqrt(M))**4;assert exact==float(r['exact_weak_tail']);weak.append((float(r['mean'])-exact)/float(r['MC_SE']))
checks['weak_tail_z_scores']=weak
(R/'BINDINGS.json').write_text(json.dumps(bindings,indent=2)+'\n');(R/'CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n');print(json.dumps(checks,indent=2))
