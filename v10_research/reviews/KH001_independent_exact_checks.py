#!/usr/bin/env python3
"""Independent exact corroboration of KH001; not formal verification.

No author diagnostic code is read or imported. All pass/fail computations use
integer/rational arithmetic or exact symbolic identities. Small exhaustive
examples are structural tests, not main-theorem finite-domain instances.
"""
from fractions import Fraction as F
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib, json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'binary_certificate_adaptation_phase/KH001_histogram_strong_side_obstruction.md'
SNAPSHOT = ROOT/'reviews/KH001_audit_snapshots/KH001_received.md'
EXPECTED = '311adf683a22370fe765f61045a96af4a201e611ceeb9136f53a2b1f8cc7fd27'
counts = Counter()
def ck(p, tag):
    assert p, tag
    counts[tag] += 1
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
ck(digest(PROOF)==EXPECTED==digest(SNAPSHOT), 'frozen_candidate_hash')
bindings = {}
for unit in ['BK001','BK002','KA001','SC003','BT002']:
    p=ROOT/f'intake/{unit}_acceptance.json'; r=json.loads(p.read_text())
    ck(r['status']=='ROOT_ACCEPTED_AFTER_INDEPENDENT_LLM_REVIEW','acceptance_status')
    ck(digest(ROOT/r['proof'])==r['sha256'],'accepted_proof_hash')
    for name,h in r.get('component_proofs',{}).items():
        ck(digest(ROOT/name)==h,'accepted_component_hash')
    if 'review_sha256' in r:
        ck(digest(ROOT/r['review'])==r['review_sha256'],'accepted_review_hash')
    for p2 in [p,ROOT/r['proof'],ROOT/r['review']]:
        bindings[str(p2.relative_to(ROOT))]=digest(p2)
    for name in r.get('component_proofs',{}): bindings[name]=digest(ROOT/name)

def mat(a,b,e,t):
    return [[1-a,a,F(0),F(0)],[F(0),F(0),1-b,b],
            [e,1-e,F(0),F(0)],[F(0),F(0),t,1-t]]
def mm(A,B):
    return [[sum(A[i][h]*B[h][j] for h in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def row(v,A): return [sum(v[i]*A[i][j] for i in range(4)) for j in range(4)]

# Generic binary-order-2 reversal with no b=1-e assumption.
a,b,e,t = sp.symbols('a b e t', positive=True)
x=1/(e/a+2+b/t); pi=sp.Matrix([[x*e/a,x,x,x*b/t]])
P=sp.Matrix(mat(a,b,e,t)); D=sp.diag(*list(pi))
R=sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
for z in pi*P-pi: ck(sp.factor(z)==0,'symbolic_stationarity')
for z in R*D.inv()*P.T*D*R-P: ck(sp.factor(z)==0,'symbolic_reversal')
d=sp.symbols('d',positive=True)
Pd=sp.Matrix(mat(a,d,1-d,t)); q=1-d
display=sp.Matrix([[(1-a)**2,(1-a)*a,a*q,a*d],
                   [q*q,q*d,d*t,d*(1-t)],
                   [q*(1-a),q*a,d*q,d*d],
                   [t*q,t*d,(1-t)*t,(1-t)**2]])
for z in Pd**2-display: ck(sp.expand(z)==0,'symbolic_full_square')

c=F(1,4096)
legal=[]; noninteger_means=0
for den in [2**36,2**40+1,2**44+3,2**50+11]:
    delta=F(1,den); beta=delta*delta
    for M in [den**2,den**2+17,den**3]:
        T=(1/(8*beta)).numerator//(1/(8*beta)).denominator
        for k in sorted(set([T//2,T//2+1,T])):
            ck(M>=64 and F(1,M)<=beta<=F(1,16),'legal_beta_domain')
            ck(32<=k<=T and k*k>=4*M and k*delta>=6/c,'legal_k_domain')
            ck(delta**5*k**3>=2**20 and delta**3*k*k>=2**21,'legal_concentration_domain')
            for j in sorted(set([k,(2*k+T)//3,(k+T)//2,T])):
                y=F(j,M); x=c*k/M; w=1-y-2*x
                aa=c*k*(1-delta)/j; tt=x*delta/w
                pp=[y,x,x,w]; A=mat(aa,delta,1-delta,tt)
                A2=mm(A,A); A3=mm(A2,A); lam=c*k*delta/(4*j)
                ck(all(0<z<1 for z in pp) and sum(pp)==1,'legal_stationary_mass')
                ck(all(sum(r)==1 and all(0<=z<=1 for z in r) for r in A),'legal_transition_rows')
                ck(row(pp,A)==pp,'exact_stationarity')
                ck(aa>=delta>=2*beta and aa<=c and w>=F(3,4) and tt<=F(1,4),'parameter_bounds')
                for u,v in product(range(4),repeat=2):
                    ck(A2[u][v]>=beta*pp[v],'all16_alternative_certificate')
                for u in range(4): ck(A3[u][3]>=aa*delta/2>=lam,'all4_three_step_atom')
                # The endpoint common-atom residual is a stochastic row. The
                # product residual construction has exactly the two marginals.
                rem=[[ (A3[u][v]-(lam if v==3 else 0))/(1-lam)
                       for v in range(4)] for u in range(4)]
                for u in range(4):
                    ck(sum(rem[u])==1 and min(rem[u])>=0,'coupling_residual_row')
                for u,v in product(range(4),repeat=2):
                    joint=[[lam*(p==3 and q==3)+(1-lam)*rem[u][p]*rem[v][q]
                            for q in range(4)] for p in range(4)]
                    ck([sum(z) for z in joint]==A3[u],'coupling_first_marginal')
                    ck([sum(joint[p][q] for p in range(4)) for q in range(4)]==A3[v],
                       'coupling_stationary_copy_marginal')
                alpha_bound=1/(1+lam*(M//3))
                ck(alpha_bound<=F(1,4) and w-alpha_bound>=F(1,2),'endpoint_denominator_bound')
                p1=384*F(j,1)/(c*delta*k*k)
                p2=1792*F(j*j,1)/(c*delta*k**3)
                p3=229376*F(j,1)/(delta*k*k)
                B=229376/(delta**5*k**3)+450560/(delta**3*k*k)
                ck(2*(p1+p2+p3)<=B<=F(111,256)<F(1,2),'conditioned_failure_bound')
                ck(F(k,8)+F(k,32)+1<=F(3*k,16)<F(k,4),'departure_endpoint_correction_budget')
                ck(F(3*k,16)+F(k,4)==F(7*k,16)<k,'strict_hamming_allowance')
                ck(F(M,1)*x==c*k and F(M,1)*y==j,'stationary_means_not_sample_counts')
                noninteger_means += (2*c*k).denominator != 1
                # Null all-state certificate, rebuilt from its symbol kernel.
                r=F(1,2*M); Tn=[[1-beta,beta],[r,1-r]]
                pin=[r/(beta+r),beta/(beta+r)]
                pn=[pin[u]*Tn[u][v] for u,v in product(range(2),repeat=2)]
                An=mat(beta,1-r,1-beta,r); An2=mm(An,An)
                for u,v in product(range(4),repeat=2):
                    ck(An2[u][v]>=beta*pn[v],'all16_asymmetric_null_certificate')
                ck(pin[1]>=F(2,3) and beta*j<=F(1,8),'null_weight_domain')
                ck(pin[1]*(1-M*r)*r*(1-(j-1)*beta)>=F(1,8*M),'null_weight_bernoulli_lower')
                ck(r==F(1,2*M) and An[0][1]==beta,'null_target_is_beta_not_r')
                legal.append({'M':str(M),'beta':str(beta),'k':str(k),'j':str(j)})

# Constant arithmetic, including each union-bound contribution separately.
ck(2*F(384,8)/c+2*F(229376,8)==450560,'failure_constant_k2')
ck(2*F(1792,64)/c==229376,'failure_constant_k3')
ck(F(229376,2**20)==F(7,32),'failure_constant_first_fraction')
ck(F(450560,2**21)==F(55,256),'failure_constant_second_fraction')
ck(F(7,32)+F(55,256)==F(111,256),'failure_constant_total')
ck(F(1,8)*F(1,2)*F(1,4)==F(1,64),'positive_risk_coefficient')
ck(F(1,2)*2==1,'clean_error_risk_coefficient')

def pairs(w): return [2*w[i]+w[i+1] for i in range(len(w)-1)]
def hist(w): return Counter(4*w[i]+2*w[i+1]+w[i+2] for i in range(len(w)-2))
def dep(w): return Counter(pairs(w)[:-1])
def can(w):
    h=hist(w); edges=[w[i:i+3] for i in range(len(w)-2) if w[i:i+3] not in [(0,0,0),(1,1,1)]]
    out=[1]*(h[7]+2)
    for edge in edges:
        ck(tuple(out[-2:])==edge[:2],'canonical_legal_edge')
        out.append(edge[2])
    out += [0]*h[0]
    return tuple(out)
def dist(a,b): return sum(x!=y for x,y in zip(a,b))
word_total=0; suffix_total=0
for N in range(4,17):
    for interior in product([0,1],repeat=N-4):
        word=(1,1)+interior+(0,0); z=can(word); h=hist(word); J=dep(word)
        rev=word[::-1]; Jr=dep(rev); cross=J[1]+J[2]
        ck(len(z)==N and z[:2]==(1,1) and z[-2:]==(0,0),'canonical_endpoints_and_length')
        ck(hist(z)==h,'canonical_full_histogram')
        ck(Jr[0]==J[0]+1 and Jr[1]+Jr[2]==cross,'exact_reverse_departure_correction')
        ck(h[4]==h[1]+1 and h[3]==h[6]-1,'exact_endpoint_edge_flows')
        for j in range(2,N-1):
            null=(1,)*(N-j)+(0,)*j
            ck(dist(z,null)<=3*cross+abs(J[0]-j),'fixed_null_suffix_hamming_bound')
            suffix_total+=1
        word_total+=1

# Full stationary word reversal and bridge identities on exact small models.
def stationary(a,b,e,t):
    x=1/(e/a+2+b/t); return [x*e/a,x,x,x*b/t]
def prob(w,A,pp):
    ys=pairs(w); p=pp[ys[0]]
    for u,v in zip(ys,ys[1:]): p*=A[u][v]
    return p
small_models=[(F(1,3),F(2,5),F(1,7),F(3,8)),
              (F(1,17),F(1,9),F(8,9),F(1,23)),
              (F(3,7),F(2,3),F(3,4),F(1,5))]
for a,b,e,t in small_models:
    pp=stationary(a,b,e,t); A=mat(a,b,e,t)
    for N in range(4,11):
        Fmass=F(0); reversed_from00=F(0)
        for w in product([0,1],repeat=N):
            pw=prob(w,A,pp)
            ck(pw==prob(w[::-1],A,pp),'exact_full_word_reversal')
            if w[:2]==(1,1) and w[-2:]==(0,0):
                Fmass+=pw
                reversed_from00+=prob(w[::-1],A,pp)/pp[0]
        ck(Fmass==pp[0]*reversed_from00,'exact_endpoint_bridge_probability')
    # Check full-word null exponents independently for moderate integer M.
for M in [8,16,31,64]:
    for beta in [F(1,M),F(2,M),F(1,5)]:
        r=F(1,2*M); pi1=beta/(beta+r)
        pp=stationary(beta,1-r,1-beta,r); A=mat(beta,1-r,1-beta,r)
        for j in range(2,M+1):
            w=(1,)*(M+2-j)+(0,)*j
            ck(prob(w,A,pp)==pi1*(1-r)**(M+1-j)*r*(1-beta)**(j-1),
               'exact_null_full_word_exponent')

# Algebraic irrational delta checks, including an irrational beta itself.
# The analytic proof, separately audited, permits every real beta in the domain.
irrational_cases=[]
for delta in [sp.sqrt(2)/2**45,sp.sqrt(3)/2**45,(1+sp.sqrt(2))/2**46]:
    beta=sp.expand(delta**2); M=2**120; k=2**82; j=2**85
    xx=sp.Rational(1,4096)*k/M; yy=sp.Rational(j,M); ww=1-yy-2*xx
    aa=sp.Rational(1,4096)*k*(1-delta)/j; tt=xx*delta/ww
    ck(bool(k*delta>=6/c) and bool(delta**5*k**3>=2**20) and bool(delta**3*k*k>=2**21)
       and bool(beta>=sp.Rational(1,M)) and bool(beta<=sp.Rational(1,16))
       and bool(beta*j<=sp.Rational(1,8)) and k*k>=4*M and k<=j,
       'algebraic_irrational_delta_domain')
    pp=[yy,xx,xx,ww]; A=sp.Matrix(mat(aa,delta,1-delta,tt)); A2=A*A
    for u,v in product(range(4),repeat=2):
        ck(bool(sp.simplify(A2[u,v]-beta*pp[v])>=0),'algebraic_all16_certificate')
    irrational_cases.append({'delta':str(delta),'beta':str(beta),'beta_is_rational':bool(beta.is_rational)})

ck(noninteger_means>0,'nonintegral_stationary_mean_cases_present')
ck(digest(PROOF)==EXPECTED==digest(SNAPSHOT),'frozen_candidate_hash_end')
result={
    'status':'PASS','kind':'independent exact diagnostics; not formal verification',
    'candidate_sha256':EXPECTED,'assertions':sum(counts.values()),'counts':dict(counts),
    'legal_family_cases':len(legal),'noninteger_mean_cases':noninteger_means,
    'exhaustive_structural_words':word_total,'fixed_suffix_comparisons':suffix_total,
    'irrational_delta_cases':irrational_cases,'accepted_dependency_bindings':bindings,
    'legal_cases':legal,
    'limits':'Finite tests corroborate tested instances only. Generic symbolic identities are exact. Universal real-beta, coupling, asymptotic, common-map and observation-restriction arguments are separately reviewed in prose.'}
out=ROOT/'reviews/KH001_independent_exact_checks.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['legal_cases','accepted_dependency_bindings']},indent=2))
