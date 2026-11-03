#!/usr/bin/env python3
"""Independent KH003 exact finite diagnostics; not formal verification.
The reviewer inspected author diagnostics but this file does not import/run them.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter, defaultdict
from itertools import product
from math import isqrt
import hashlib, json, difflib, datetime
R=Path(__file__).resolve().parents[1]
D=R/'binary_certificate_adaptation_phase'
C=Counter(); examples={}; finite=[]; c=Q(1,4096); NASSERT=0
EXPECTED='09adb8433d97011dbe7772ed9b0f1f903ed245d73299db02d7d6bc477fc358a4'
def check(v,label):
    global NASSERT
    if not v: raise AssertionError(label)
    NASSERT+=1
    C[label]+=1
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
proof=D/'KH003_boundary_window_obstruction.md'
snap=R/'reviews/KH003_audit_snapshots/KH003_received.md'
check(sha(proof)==EXPECTED==sha(snap),'frozen_candidate_and_snapshot')
inputs=[proof,snap,Path(__file__).resolve()]
for u in ['KH001','KH002','BK001','KA001','SC003','BT002']:
    rp=R/f'intake/{u}_acceptance.json'; receipt=json.loads(rp.read_text()); inputs.append(rp)
    check(receipt['status']=='ROOT_ACCEPTED_AFTER_INDEPENDENT_LLM_REVIEW','root_acceptance_status')
    p=R/receipt['proof']; inputs.append(p)
    check(sha(p)==receipt['sha256'],'accepted_proof_hash')
    for name,h in receipt.get('component_proofs',{}).items():
        p=R/name; inputs.append(p); check(sha(p)==h,'accepted_component_hash')
    p=R/receipt['review']; inputs.append(p)
    if 'review_sha256' in receipt: check(sha(p)==receipt['review_sha256'],'accepted_review_hash')
before=D/'revisions/KH003_initial_candidate.md'
diff=D/'revisions/KH003_constant_window_clarification.diff'
rec=D/'revisions/KH003_constant_window_revision_record.json'
record=json.loads(rec.read_text()); inputs += [before,diff,rec,D/'KH003_boundary_window_exploration_unreviewed.md',D/'check_kh003.py',D/'KH003_author_diagnostics.json']
check(sha(before)==record['before_sha256'],'actual_before_hash')
check(sha(proof)==record['after_sha256'],'record_after_hash')
actual=''.join(difflib.unified_diff(before.read_text().splitlines(True),proof.read_text().splitlines(True),fromfile=before.name,tofile=proof.name))
check(actual==diff.read_text(),'actual_recorded_diff_exact')
start={str(p.relative_to(R)):sha(p) for p in set(inputs)}

def hist(w,n=3): return Counter(w[i:i+n] for i in range(len(w)-n+1))
def departures(w,s): return sum(w[i:i+2]==s for i in range(len(w)-2))
def canonical(w):
    h=hist(w); out='11'+'1'*h['111']
    for i in range(len(w)-2):
        edge=w[i:i+3]
        if edge not in ('111','000'):
            check(out[-2:]==edge[:2],'skeleton_legal_edge'); out+=edge[-1]
    return out+'0'*h['000']
def hamm(a,b): return sum(x!=y for x,y in zip(a,b))

# Complete endpoint-word enumeration, including all allowed structural widths.
for N in range(4,18):
    for mid in product('01',repeat=N-4):
        w='11'+''.join(mid)+'00'; z=canonical(w); v=w[::-1]; h=hist(w)
        M=N-2; J0=departures(w,'00'); JC=departures(w,'01')+departures(w,'10')
        check(len(z)==N and z[:2]=='11' and z[-2:]=='00','canonical_length_pairs')
        check(hist(z)==h,'all_triple_counts_preserved')
        check(h['100']==h['001']+1 and h['011']==h['110']-1,'endpoint_flows')
        E=M-h['000']-h['111']
        check(h['001']<=JC and E<=2*JC and h['000']==J0-h['001'],'loop_skeleton_geometry')
        check(departures(v,'00')==J0+1 and departures(v,'01')+departures(v,'10')==JC,'reverse_departure_correction')
        for j in range(2,N-1):
            x='1'*(N-j)+'0'*j
            check(hamm(z,x)<=3*JC+abs(J0-j),'fixed_presampling_j_Hamming')
        for r in range(2,N//2+1):
            B=w[:r]=='1'*r and w[-r:]=='0'*r
            check(B==(v[:r]=='0'*r and v[-r:]=='1'*r),'boundary_event_reversal')
            if B:
                check(h['111']>=r-2 and h['000']>=r-2,'conditioned_windows_force_loops')
                check(z[:r]==w[:r] and z[-r:]==w[-r:],'constant_windows_always_preserved')
                if r>=4 and hist(z,r)!=hist(w,r) and 'longer_pattern_counterexample' not in examples:
                    examples['longer_pattern_counterexample']={'r':r,'original':w,'canonical':z,'original_r_counts':dict(hist(w,r)),'canonical_r_counts':dict(hist(z,r))}
            if v[-r:]!='1'*r:
                # q is zero-based; the pair departure index is q.
                q=max(i for i in range(N-r,N-2) if v[i]=='0')
                check(v[q:q+3]=='011' and N-r<=q<=N-3,'last_zero_transition_witness')
                check(len(range(N-r,N-2))==r-2,'last_window_departure_positions')
        C['exhaustive_endpoint_words']+=1
check('longer_pattern_counterexample' in examples,'nonpreservation_longer_pattern_counts')

# Independent exact state/flag/trailing-run DP, including an exact transition flux union.
sources=[(Q(1,19),Q(1,11),Q(1,23)),(Q(2,9),Q(1,17),Q(3,29)),(Q(1,101),Q(3,20),Q(1,37)),(Q(3,16),Q(2,13),Q(1,7))]
for a,delta,tau in sources:
    qs=[a,delta,delta,1-tau]
    for M in [2,3,4,7,10,15,23,31]:
        N=M+2
        for r in range(2,N//2+1):
            law={(0,True,0):Q(1)}; late_flux=Q(0)
            for m in range(M):
                if m>=M-r+2:
                    late_flux+=delta*sum(v for (state,f,t),v in law.items() if state==1)
                nxt=defaultdict(Q)
                for (state,first,tail),mass in law.items():
                    for bit,p in [(0,1-qs[state]),(1,qs[state])]:
                        st=2*(state%2)+bit; first2=first and not(m+3<=r and bit)
                        tail2=min(r,tail+1) if bit else 0
                        nxt[st,first2,tail2]+=mass*p
                law=nxt
            check(sum(law.values())==1,'DP_probability_normalization')
            pe=sum(v for (s,f,t),v in law.items() if s==3)
            early=sum(v for (s,f,t),v in law.items() if not f)
            late=sum(v for (s,f,t),v in law.items() if s==3 and t<r)
            bad=sum(v for (s,f,t),v in law.items() if s==3 and (not f or t<r))
            check(early==1-(1-a)**(r-2),'first_window_exact_geometric')
            check(early<=(r-2)*a,'first_window_Bernoulli_bound')
            check(late<=late_flux<=(r-2)*delta,'last_window_exact_flux_union')
            check(bad<=early+late<=(r-2)*(a+delta),'boundary_unconditional_union')
            check(pe>0 and bad/pe<=(r-2)*(a+delta)/pe,'boundary_conditional_division')
            if r==2: check(early==late==bad==0,'r2_empty_failures')
            C['boundary_DP_cases']+=1

# Exact stationary word/reversed bridge identity and clean-error transfer.
for a,delta,tau in sources[:3]:
    qs=[a,delta,delta,1-tau]; x=1/((1-delta)/a+2+delta/tau); pi=[x*(1-delta)/a,x,x,x*delta/tau]
    def prob(w,stationary=True):
        s=int(w[:2],2); p=pi[s] if stationary else Q(s==0)
        for ch in w[2:]:
            bit=int(ch); p*=qs[s] if bit else 1-qs[s]; s=2*(s%2)+bit
        return p
    for N in range(4,12):
        M=N-2
        allw=[''.join(t) for t in product('01',repeat=N)]
        for w in allw: check(prob(w)==prob(w[::-1]),'exact_full_word_reversal')
        for r in range(2,N//2+1):
            fr=[w for w in allw if w[:r]=='1'*r and w[-r:]=='0'*r]
            pf=sum(map(prob,fr)); peB=sum(prob(w[::-1],False) for w in fr)
            check(pf==pi[0]*peB and pf>0,'stationary_Fr_reverse_bridge_mass')
            # Same statistic randomized estimator: two output probabilities, fixed 1/3 mixture.
            def loss(w,target):
                h=hist(w); p=Q(h['001']+1,h['000']+h['001']+2)
                return Q(1,3)*abs(p-target)+Q(2,3)*abs((1+p)/2-target)
            clean=sum(prob(w)*loss(w,a) for w in fr)/pf
            for j in sorted(set([r,N//2,N-r])):
                actual='1'*(N-j)+'0'*j; k=max(1,N//3); beta=a/4
                risk=Q(0); acc=Q(0); accepted_clean=Q(0)
                for w in fr:
                    z=canonical(w); mass=prob(w)/pf
                    ok=hamm(z,actual)<=k and z[:r]==actual[:r] and z[-r:]==actual[-r:]
                    output=z if ok else actual
                    check(hamm(output,actual)<=k and output[-2:]==actual[-2:],'pointwise_kernel_budget_terminal')
                    if ok:
                        acc+=mass; accepted_clean+=mass*loss(w,a)
                        check((hist(z),z[:r],z[-r:])==(hist(w),w[:r],w[-r:]),'every_accept_statistic_equality')
                    risk+=mass*loss(output,beta)
                check(accepted_clean<=clean,'accepted_clean_error_not_resampled')
                check(risk>=acc*(a-beta)-clean,'exact_randomized_loss_triangle_transfer')
                C['small_exact_kernel_cases']+=1
            C['stationary_window_cases']+=1

# Every finite hypothesis and all-state entries in actual huge valid instances.
def ceilq(q): return -(-q.numerator//q.denominator)
def rootfloor(n,p):
    lo=0; hi=1 << ((n.bit_length()+p-1)//p)
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**p<=n: lo=mid
        else: hi=mid
    return hi if hi**p<=n else lo
def finite_case(M,beta,k,r,label,actual_beta=None):
    if actual_beta is None: actual_beta=beta
    dn=isqrt(beta.denominator); nn=isqrt(beta.numerator)
    delta=Q(nn,dn); check(delta*delta==beta,'finite_exact_square_certificate')
    T=int(1/(8*beta)); Jlo=max(k,ceilq(16*c*r*k))
    check(M>=64 and Q(1,M)<=beta<=Q(1,16),'finite_beta_domain')
    check(32<=k<=T and k*k>=4*M and k*delta>=6/c and delta**5*k**3>=2**20 and delta**3*k*k>=2**21,'all_inherited_k_conditions')
    check(2<=r<=Q(k,4) and r*delta<=Q(1,16) and Jlo<=T,'all_additional_window_conditions')
    check(beta>=actual_beta>0 and k*k*actual_beta>=1,'actual_beta_benchmark_and_nesting')
    for j in sorted(set([Jlo,Jlo+1,(Jlo+T)//2,T-1,T])):
        if not Jlo<=j<=T: continue
        x=c*k/M; y=Q(j,M); w=1-y-2*x; a=c*k*(1-delta)/j; tau=x*delta/w; pi=[y,x,x,w]
        qs=[a,delta,delta,1-tau]
        P=[[Q(0) for _ in range(4)] for _ in range(4)]
        for s in range(4):
            for bit in [0,1]: P[s][2*(s%2)+bit]=qs[s] if bit else 1-qs[s]
        check(all(0<p<1 for p in qs) and all(p>0 for p in pi) and sum(pi)==1,'finite_legal_source')
        for t in range(4): check(sum(pi[s]*P[s][t] for s in range(4))==pi[t],'finite_stationary_coordinate')
        for s in range(4):
            for t in range(4):
                p2=sum(P[s][u]*P[u][t] for u in range(4))
                check(p2>=beta*pi[t]>=actual_beta*pi[t],'all_state_both_certificate_entries')
        check(a>=2*beta and a<=Q(1,16*r),'clean_gap_and_boundary_exit')
        check(2*r*(a+delta)<=Q(1,4),'conditional_boundary_constant')
        lam=c*k*delta/(4*j)
        check(lam*M/4>=3 and w-Q(1,4)>=Q(1,2),'reverse_endpoint_denominator_bound')
        fail=Q(229376)/(delta**5*k**3)+Q(450560)/(delta**3*k*k)
        check(fail<=Q(111,256),'inherited_good_count_failure')
        check(1-fail-Q(1,4)>=Q(81,256)>Q(1,4),'intersection_success')
        check(Q(j)-Q(5*k,16)>=Q(11*k,16)>=r-2,'zero_loop_lower_geometry')
        check(Q(M)-j-Q(3*k,8)>=Q(53*M,64)>=r-2,'one_loop_lower_geometry')
        check(Q(7*k,16)<k and j>=4*r and M+2-j>=r,'strict_distance_input_windows')
        check(Q(j,2*M)*Q(3,4)==Q(3*j,8*M),'stationary_conditioned_event_cost')
        check(Q(8*M,3*j)<=Q(4*M,j),'conditional_clean_error_relaxation')
        check(Q(1,8*M)*(a/8)>=c*k/(128*M*j) and Q(1,2*M)*Q(4*M,j)==Q(2,j),'risk_positive_penalty_coefficients')
        C['finite_clean_family_members']+=1
    finite.append({'label':label,'M':str(M),'beta_w':str(beta),'actual_beta':str(actual_beta),'k':str(k),'r':r,'J0':str(Jlo),'T':str(T)})

for t in [240,360,480]:
    M=2**t; beta=Q(1,M); L=2**(5*t//6)
    rs=[2,3,255,257,2**(t//12)+1,2**(t//6-16)+1]
    for r in rs:
        U=Q(M,r); ul=U*L; k=isqrt(ul.numerator//ul.denominator)
        check(k*k<=ul<(k+1)**2,'critical_geometric_floor')
        finite_case(M,beta,k,r,'critical_growing')
    for b in [t//2+12,2*t//3,t,t+24,2*t-48]:
        bw=min(t,b); actual=Q(1,2**b); beta=Q(1,2**bw)
        # k^12=U^6 L^6=max(M^3 beta_w^-6,beta_w^-11,beta^-3 beta_w^-6).
        # This avoids accidentally rounding the fractional exponent in beta_w^-5/6.
        radical=max(2**(3*t+6*bw),2**(11*bw),2**(3*b+6*bw)); k=rootfloor(radical,12)
        check(k**12<=radical<(k+1)**12,'bounded_window_exact_nested_radical_floor')
        for r in [2,17,257,1000]: finite_case(M,beta,k,r,'bounded_width_nested',actual)

# Nonempty harmonic range can have just one j; no unspoken J0<T assumption.
finite_case(2**240,Q(1,2**240),2**210,2**35,'single_suffix_J0_equals_T')
check(finite[-1]['J0']==finite[-1]['T'],'single_suffix_range_endpoint')

# Finite null masses, retain BOTH exponents and true target beta_w.
for M in [64,96,144,256]:
    for beta in [Q(1,M),Q(2,M),Q(3,M)]:
        rflip=Q(1,2*M); p1=beta/(beta+rflip); T=int(1/(8*beta))
        for j in range(2,T+1):
            v=p1*(1-rflip)**(M+1-j)*rflip*(1-beta)**(j-1)
            check(Q(1,8*M)<=v<=Q(1,2*M),'exact_nonconstant_null_mass_bounds')
            check((1-rflip)**(M+1-j)>=(1-rflip)**M>=Q(1,2),'null_long_prefix_cost')
            check((1-beta)**(j-1)>=Q(7,8),'null_suffix_cost')
            C['finite_null_words']+=1
        # Null all-state ratio check, also shows target is not rare 1->0 rate.
        TT=[[1-beta,beta],[rflip,1-rflip]]; pis=[1-p1,p1]
        for u,v,s,tbit in product(range(2),repeat=4):
            ratio=TT[v][s]/pis[s]
            check(ratio>=beta+rflip>=beta,'asymmetric_null_all_state_ratio')
        check(TT[0][1]==beta and beta!=rflip,'null_true_target_not_reverse_rate')

# Exact probability-set and signed-weight scalar checks, independent of path model.
for pB in [Q(3,4),Q(4,5),Q(15,16),Q(1)]:
    lo=max(Q(0),Q(145,256)+pB-1)
    check(lo>=Q(81,256) and lo/pB>=Q(81,256),'intersection_conditional_denominator_direction')
for P0 in [Q(0),Q(1,100),Q(1,5)]:
    for D0 in [Q(0),Q(1,100),Q(1,4),Q(2)]:
        for mass in [Q(1,8),Q(1,5),Q(1,2)]:
            check(mass*(P0-D0)>=Q(1,8)*P0-Q(1,2)*D0,'signed_bracket_separate_weights')
for name,h in start.items(): check(sha(R/name)==h,'all_inputs_unchanged_end')
check(sha(proof)==EXPECTED,'candidate_still_frozen_end')
out={'unit':'KH003','status':'PASS_EXACT_TESTED_INSTANCES_ONLY','generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'candidate_sha256':EXPECTED,'assertion_total':NASSERT,'counts':dict(C),'structural_examples':examples,'complete_finite_parameter_cases':finite,'input_sha256':start,'independence':'Fresh reviewer implementation; author diagnostics were inspected but are not imported or executed.','limitations':'Exact finite corroboration, not formal verification. Small-word/DP/kernel examples test structural identities outside the huge theorem domain. Asymptotic and universal-map claims are addressed analytically in the separate full review.'}
(R/'reviews/KH003_independent_exact_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'assertion_total':out['assertion_total'],'counts':dict(C),'examples':examples},indent=2))
