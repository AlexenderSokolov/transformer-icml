"""Independent FOT001 finite corroboration; does not import author checker."""
from itertools import product
from collections import Counter
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import hashlib,json
base=Path(__file__).resolve().parent
checks=Counter()
def edge(w): return Counter(w[i:i+2] for i in range(len(w)-1))
def triple(w): return Counter(w[i:i+3] for i in range(len(w)-2))
def relocate(w,r):
    # Rebuild from retained triple edge labels, not an altered vertex list.
    l,h=r-2,len(w)-r
    triples=[w[i:i+3] for i in range(l,h)]
    loops=Counter(z for z in triples if z in ((0,0,0),(1,1,1)))
    kept=[z for z in triples if z not in loops]
    vertices=[w[l:l+2]]+[z[1:] for z in kept]
    p=next((i for i,s in enumerate(vertices) if s==(1,1)),None)
    q=next((i for i,s in enumerate(vertices) if s==(0,0) and p is not None and i>p),None)
    if q is None:return None
    out=list(w[:l+2])
    for i in range(len(vertices)):
        if i==p:out += [1]*loops[(1,1,1)]
        if i==q:out += [0]*loops[(0,0,0)]
        if i<len(kept):out.append(kept[i][2])
    out += w[h+2:]
    return tuple(out)
a,t=Q(1,5),Q(1,11)
for N in range(2,13):
    masses=Counter()
    for bits in product((0,1),repeat=N-1):
        w=(1,)+bits+(0,); e=edge(w); v,u=e[(0,0)],e[(0,1)]
        prob=a/(a+t)*a**u*(1-a)**v*t**e[(1,0)]*(1-t)**e[(1,1)]
        masses[v,u]+=prob
        if w[:2]!=(1,1) or w[-2:]!=(0,0):continue
        tr=triple(w); j=sum(n for z,n in tr.items() if z[:2]==(0,0)); cross=sum(n for z,n in tr.items() if z[0]!=z[1])
        assert j==v-1 and cross==e[(0,1)]+e[(1,0)]
        assert edge(w[::-1])[(0,1)]==u+1
        checks['endpoint_count_identities']+=1
        for r in range(2,(N+1)//2+1):
            z=relocate(w,r)
            if z is None:continue
            assert len(z)==N+1 and triple(z)==tr and z[:r]==w[:r] and z[-r:]==w[-r:]
            target=(1,)*(N+1-j)+(0,)*j
            assert sum(b!=d for b,d in zip(z,target))<=3*cross+4*r-5
            if j>=2:
                assert z[-2:]==target[-2:]==(0,0)
                assert sum(n for s,n in triple(target).items() if s[:2]==(0,0))==j-2
            checks['independent_edge_relocations']+=1
    for v in range(N+1):
        for u in range(N+1):
            H=N-v-u
            value=0 if H<1 or u>H-1 else a/(a+t)*comb(v+u,u)*a**u*(1-a)**v*t*comb(H-1,u)*t**u*(1-t)**(H-1-u)
            assert masses[v,u]==value
            checks['exact_weighted_mixture_cells']+=1
for a,t in [(Q(1,4),Q(1,16)),(Q(1,64),Q(1,256)),(Q(1,4),Q(1,4))]:
    T=((1-a,a),(t,1-t)); pi=(t/(a+t),a/(a+t))
    for N in range(2,9):
        moments=[Q(0)]*5; seconds=[Q(0)]*5
        for w in product((0,1),repeat=N+1):
            pr=pi[w[0]]
            for i in range(N):pr*=T[w[i]][w[i+1]]
            e=edge(w); vals=[e[(0,0)],e[(0,1)],e[(1,0)],e[(0,1)]+e[(1,0)],e[(0,0)]+e[(0,1)]]
            for i,z in enumerate(vals):moments[i]+=pr*z; seconds[i]+=pr*z*z
        for m,s in zip(moments,seconds):
            assert s-m*m<=3*m/a
            checks['exact_variance_bounds']+=1
    for b,d,s,z in product((0,1),repeat=4):
        assert T[d][s]*T[s][z]/(pi[s]*T[s][z])==T[d][s]/pi[s]>=a+t
        checks['alternative_certificate_entries']+=1
for N in (64,65,128,1024):
    beta=Q(1,N-1);q=beta/2;T=((1-beta,beta),(q,1-q));pi=(Q(1,3),Q(2,3))
    for b,d,s,z in product((0,1),repeat=4):
        assert T[d][s]*T[s][z]>=beta*pi[s]*T[s][z]
        checks['null_certificate_entries']+=1
    for j in range(2,N//8+1):
        assert Q(2,3)*(1-q)**(N-j)*q*(1-beta)**(j-1)>=Q(1,8*N)
        checks['null_masses']+=1
c=Q(1,2**16);A=2**12;x=4096
failure=2*((224+24576*c*c)/2**20+Q(16,A)+Q(32,x))+Q(16,x)
assert failure<Q(1,16)
assert Q(1,64)*Q(1,128)*c*Q(1,8)==Q(1,2**32)
result={'status':'PASS','counts':dict(checks),'failure_bound':str(failure),'failure_bound_decimal':float(failure),'candidate_sha256':hashlib.sha256((base.parent/'FOT001_candidate.md').read_bytes()).hexdigest(),'limitations':'Finite corroboration only. Analytic review is separate; no acceptance action.'}
(base/'independent_audit_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
