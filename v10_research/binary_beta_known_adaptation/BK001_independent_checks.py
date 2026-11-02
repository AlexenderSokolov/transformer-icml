#!/usr/bin/env python3
"""Independent finite corroboration of BK001; not formal verification.

Built without reading the author diagnostics. Exact Fraction/SymPy arithmetic;
exhaustive short-word identities do not substitute for the general proof.
"""
from __future__ import annotations
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PROOF = HERE / 'BK001_histogram_adaptation_obstruction.md'
EXPECTED = 'edbfc9cd372df7497ff7462eded0e6c85a3ee4f99f21bd7310f460bd1f0fcb5a'
PAIRS = tuple(product((0, 1), repeat=2))

def digest(p): return sha256(p.read_bytes()).hexdigest()
def mul(A, B):
    return [[sum((A[i][s]*B[s][j] for s in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def pair_matrix(theta):
    P = [[F(0) for _ in PAIRS] for _ in PAIRS]
    for i, (u,v) in enumerate(PAIRS):
        for z in (0,1):
            P[i][PAIRS.index((v,z))] = theta[i] if z else 1-theta[i]
    return P

def symbolic_checks():
    x,y,d = sp.symbols('x y d', positive=True)
    w=1-y-2*x; e=1-d; a=x*e/y; t=x*d/w
    P=sp.Matrix([[1-a,a,0,0],[0,0,e,d],[e,d,0,0],[0,0,t,1-t]])
    pi=sp.Matrix([[y,x,x,w]])
    assert all(sp.cancel(v)==0 for v in list(pi*P-pi))
    prescribed=sp.Matrix([[(1-a)**2,(1-a)*a,a*e,a*d],
                         [e*e,e*d,d*t,d*(1-t)],
                         [e*(1-a),e*a,d*e,d*d],
                         [t*e,t*d,(1-t)*t,(1-t)**2]])
    assert all(sp.cancel(v)==0 for v in list(P*P-prescribed))
    return {'stationarity_symbolic_zero_residuals':4,
            'two_step_matrix_symbolic_zero_residuals':16}

def parameter_checks():
    c=F(1,4096); records=[]; certificate_entries=0
    for n in (4096,4097,5001,8192,65537,1000003):
        M=n**10; k=n**9; T=M//8; d=F(1,n**5); e=1-d
        beta=F(1,M); x=c*k/M; lam=c*k/(4*n**15)
        assert d*d==beta and 0<lam<1 and k<=T
        assert M//3>=F(M,4)
        atom_tail=1/(1+lam*(M//3))
        elementary_tail=1/(1+c*n**4/16)
        assert atom_tail<=elementary_tail<=F(1,2*n)
        js=sorted({k,k+1,(k+T)//2,T-1,T})
        for j in js:
            y=F(j,M); w=1-y-2*x; a=x*e/y; t=x*d/w
            pi=[y,x,x,w]; theta=[a,d,d,1-t]
            assert sum(pi)==1 and all(0<z<1 for z in pi)
            assert 0<d<=F(1,4) and d<=a<=c<=F(1,4)
            assert 0<x<=c and 0<y<=F(1,8) and w>=F(3,4)
            assert 0<t<=F(1,4) and y*a==x*e and w*t==x*d
            P=pair_matrix(theta); P2=mul(P,P); P3=mul(P2,P)
            assert all(sum(row)==1 for row in P)
            assert mul([pi],P)[0]==pi
            ratios=[]
            for i in range(4):
                for z in range(4):
                    assert P2[i][z]>=beta*pi[z]
                    ratios.append(P2[i][z]/(beta*pi[z]))
                    certificate_entries+=1
            assert min(P3[i][3] for i in range(4))>=a*d/2>=lam
            assert w*(y-elementary_tail)>=y/4
            assert M*y==j and M*(2*x)==2*c*k
            var00=7*M*y/lam; varcross=7*M*2*x/lam
            bad00=var00/(F(k,4)**2)*4/y
            badcross=varcross/(F(k,32)**2)*4/y
            expected00=F(1792,c)*F(n**25,k**3)
            expectedcross=229376*F(n**25,k*k*j)
            assert bad00==expected00
            assert badcross==expectedcross<=F(229376,n*n)
            total=F(1792/c+229376,n*n)
            assert bad00+badcross<=total<=F(231,512)<F(1,2)
            assert 2*c*k<=F(k,32) and F(7*k,16)<k
            records.append({'n':n,'j':str(j),
                'minimum_certificate_ratio_exact':str(min(ratios)),
                'minimum_three_step_atom_ratio_exact':str(min(P3[i][3] for i in range(4))/lam),
                'cross_occupation_mean_denominator':(2*c*k).denominator,
                'conditional_union_bound_exact':str(bad00+badcross)})
        r=F(1,2*M)
        null_theta=[r,1-r,r,1-r]
        P=pair_matrix(null_theta); P2=mul(P,P)
        null_pi=[(1-r)/2,r/2,r/2,(1-r)/2]
        assert mul([null_pi],P)[0]==null_pi
        assert all(P2[i][j]>=beta*null_pi[j] for i in range(4) for j in range(4))
        assert min(P2[i][j]/null_pi[j] for i in range(4) for j in range(4))==beta
        assert d>=2*r
    assert any(q['cross_occupation_mean_denominator']>1 for q in records)
    assert F(1792/c+229376,4096**2)==F(231,512)
    return {'cases':records,'all_state_inequalities_checked':certificate_entries,
            'null_all_state_inequalities_checked':6*16,
            'n4096_failure_bound_exact':'231/512',
            'n4096_success_bound_exact':'281/512',
            'nonintegral_expected_cross_occupation_cases':sum(q['cross_occupation_mean_denominator']>1 for q in records)}

def canonicalize(word):
    edges=list(zip(word,word[1:],word[2:]))
    hist=Counter(edges)
    skeleton=[edge for edge in edges if edge not in ((0,0,0),(1,1,1))]
    z=[1,1]
    for edge in [(1,1,1)]*hist[(1,1,1)]+skeleton+[(0,0,0)]*hist[(0,0,0)]:
        assert tuple(z[-2:])==edge[:2]
        z.append(edge[-1])
    return tuple(z),hist,len(skeleton)

def exhaustive_word_checks():
    words=comparisons=0; largest_N=20; sample=None
    for N in range(4,largest_N+1):
        for middle in product((0,1),repeat=N-4):
            word=(1,1)+middle+(0,0)
            z,h,E=canonicalize(word); words+=1
            assert len(z)==N and z[:2]==word[:2] and z[-2:]==word[-2:]
            assert Counter(zip(z,z[1:],z[2:]))==h
            U=h[(0,0,1)]; V=h[(1,1,0)]
            J00=sum(value for edge,value in h.items() if edge[:2]==(0,0))
            J01=sum(value for edge,value in h.items() if edge[:2]==(0,1))
            J10=sum(value for edge,value in h.items() if edge[:2]==(1,0))
            cross=J01+J10; L0=h[(0,0,0)]
            assert h[(1,0,0)]==U+1 and h[(0,1,1)]==V-1
            assert U<=J10-1 and V<=J01+1 and U+V<=cross
            assert E==U+V+cross and L0==J00-U
            for j in range(2,N-1):
                target=(1,)*(N-j)+(0,)*j
                distance=sum(a!=b for a,b in zip(z,target)); comparisons+=1
                assert distance<=E+abs(L0-j)<=3*cross+abs(J00-j)
                assert z[:2]==target[:2] and z[-2:]==target[-2:]
                # A distance-checked replacement is strict budget; at one less it rejects.
                k=distance
                output=z if distance<=k else target
                assert sum(a!=b for a,b in zip(output,target))<=k
                if k:
                    output=z if distance<=k-1 else target
                    assert sum(a!=b for a,b in zip(output,target))<=k-1
                if word!=z and sample is None:
                    sample={'original':''.join(map(str,word)),
                            'canonical':''.join(map(str,z)),
                            'common_histogram':{''.join(map(str,e)):v for e,v in sorted(h.items())}}
    assert words==2**17-1
    return {'max_word_length':largest_N,'endpoint_11_to_00_words':words,
            'fixed_null_suffix_comparisons':comparisons,
            'sample_nonidentity_canonicalization':sample}

def risk_checks():
    # Enumerate elementary scalar triangle/success inequalities on a rational grid.
    checks=0
    for a in (F(1,16),F(1,8),F(1,4),F(1,2)):
        for r in (F(0),a/4,a/2):
            for q in (F(i,16) for i in range(17)):
                assert abs(q-r)>=a-r-abs(q-a)
                for p in (F(1,2),F(3,4),F(1)):
                    assert p*(a-r)>=a/4
                    checks+=1
    # Exact sign control is essential; a common nonnegative coefficient can be
    # multiplied by the null-mass lower bound, a negative one is replaced by 0.
    return {'scalar_triangle_and_acceptance_instances':checks,
            'signed_coefficient_condition':'Replace common v by 1/(8M) only when ck/(64M)-S/2 >= 0; otherwise use risk >= 0.',
            'asymptotic_onset_exact':'If n^4 >= 64*C/c, then c/(64*n)-C/(2*n^5) >= c/(128*n).'}

def dependencies():
    records={}
    for unit in ('AB001','AB002','AB003','SC003','BT002'):
        receipt_path=ROOT/'intake'/f'{unit}_acceptance.json'
        receipt=json.loads(receipt_path.read_text())
        source_path=ROOT/receipt['proof']
        assert digest(source_path)==receipt['sha256']
        records[unit]={'proof':str(source_path.relative_to(ROOT)),
            'proof_sha256':digest(source_path),
            'receipt_sha256':digest(receipt_path),
            'receipt_status':receipt['status']}
        if unit=='BT002':
            for relative,expected in receipt['component_proofs'].items():
                assert digest(ROOT/relative)==expected
            records[unit]['component_proofs']=receipt['component_proofs']
    return records

if __name__=='__main__':
    assert digest(PROOF)==EXPECTED, 'Candidate changed; re-audit required.'
    result={'status':'PASS_FINITE_EXACT_DIAGNOSTICS_NOT_FORMAL_VERIFICATION',
        'generated_utc':datetime.now(timezone.utc).isoformat(),
        'proof_sha256':digest(PROOF),'script_sha256':digest(Path(__file__)),
        'dependencies':dependencies(), 'symbolic':symbolic_checks(),
        'parameters':parameter_checks(), 'canonicalization':exhaustive_word_checks(),
        'risk':risk_checks(),
        'limitations':['Finite parameter samples do not prove all n and j.',
          'Short-word exhaustive canonicalization does not by itself prove arbitrary length.',
          'No massive-horizon bridge probabilities are enumerated; they are bounded analytically in the review.',
          'Independent LLM corroboration only; no formal or external peer review or root acceptance.']}
    assert digest(PROOF)==EXPECTED
    dest=HERE/'BK001_independent_checks.json'
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'proof_sha256':result['proof_sha256'],
        'parameter_cases':len(result['parameters']['cases']),
        'certificate_entries':result['parameters']['all_state_inequalities_checked'],
        'canonicalization':result['canonicalization'], 'output':str(dest)},indent=2))
