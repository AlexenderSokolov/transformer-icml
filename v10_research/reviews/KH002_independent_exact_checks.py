#!/usr/bin/env python3
"""Independent finite corroboration for KH002; not a formal proof.

Written from the candidate and accepted mathematical interfaces, without reading
or importing either author's diagnostics. Pass/fail uses integer/Fraction
arithmetic only; roots are certified by bounding powers on both sides.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
CAND = 'binary_certificate_adaptation_phase/KH002_histogram_domain_classification.md'
SNAP = 'reviews/KH002_audit_snapshots/KH002_received.md'
EXPECTED = '970bfefb6041cdb989148819eb526c789d86591992375b84b05de2dd72bf9702'
counts = Counter()
hashes = {}

def check(p, group):
    assert p, group
    counts[group] += 1

def sha(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

def bind(path, expected=None):
    h = sha(path)
    if expected is not None:
        check(h == expected, 'immutable_hash_assertions')
    hashes[path] = h
    return h

def check_receipt(unit):
    path = f'intake/{unit}_acceptance.json'
    bind(path)
    data = json.loads((ROOT/path).read_text())
    check(data['status'] == 'ROOT_ACCEPTED_AFTER_INDEPENDENT_LLM_REVIEW', 'accepted_receipts')
    bind(data['proof'], data['sha256'])
    if data.get('review'):
        bind(data['review'], data.get('review_sha256'))
    for path, h in data.get('component_proofs', {}).items():
        bind(path, h)

for p in [CAND, SNAP]:
    bind(p, EXPECTED)
for unit in ['KH001', 'KA001', 'SC003', 'BT002', 'BK001']:
    check_receipt(unit)

def iroot(n, d):
    """Integer floor d-th root, exact Newton iteration and final adjustment."""
    if n == 0:
        return 0
    x = 1 << ((n.bit_length()+d-1)//d)
    while True:
        y = ((d-1)*x + n//x**(d-1))//d
        if y >= x:
            break
        x = y
    while (x+1)**d <= n:
        x += 1
    while x**d > n:
        x -= 1
    return x

def root_floor(q, d):
    a = iroot(q.numerator//q.denominator, d)
    check(a**d <= q < (a+1)**d, 'certified_root_floors')
    return a

def selected_budget(M, beta):
    bw = max(beta, Q(1, M))
    U = 1/bw
    # sqrt(U L) is the max of (U^2 M)^(1/4), U^(11/12),
    # (U^2/beta)^(1/4). Floor commutes with a finite maximum.
    radicands = [(U*U*M, 4), (U**11, 12), (U*U/beta, 4)]
    parts = [root_floor(q, d) for q, d in radicands]
    k = max(parts)
    check(all(k >= a for a in parts), 'budget_maximum')
    check(any(k == a for a in parts), 'budget_maximum')
    for q, d in radicands:
        check(k**d * 2**d >= q, 'floor_half_root_lower')
    T = (U/8).__floor__()
    return bw, U, k, T, parts

def finite_conditions(M, beta, bw, k, T):
    return [32 <= k <= T, k*k >= 4*M,
            k*k*bw >= (6*4096)**2,
            bw**5*k**6 >= 2**40,
            bw**3*k**4 >= 2**42,
            k*k*beta >= 1]

def mul(A, B):
    return [[sum(A[i][t]*B[t][j] for t in range(4))
             for j in range(4)] for i in range(4)]

def pair_matrix(probs):
    P = [[Q(0) for _ in range(4)] for _ in range(4)]
    for state, p in enumerate(probs):
        v = state % 2
        P[state][2*v] = 1-p
        P[state][2*v+1] = p
    return P

def source_checks(M, beta, bw, k, T):
    nd, dd = isqrt(bw.numerator), isqrt(bw.denominator)
    if nd*nd != bw.numerator or dd*dd != bw.denominator:
        return
    delta = Q(nd,dd)
    c = Q(1,4096)
    for j in sorted({k, k+1, (k+T)//2, T-1, T}):
        x, y = c*k/M, Q(j,M)
        w = 1-y-2*x
        a = c*k*(1-delta)/j
        tau = x*delta/w
        pi = [y,x,x,w]
        P = pair_matrix([a,delta,delta,1-tau])
        P2 = mul(P,P)
        check(all(0 < z < 1 for z in pi+[a,delta,tau]), 'legal_source_parameters')
        check(sum(pi) == 1, 'stationary_mass_normalization')
        for u in range(4):
            check(sum(P[u]) == 1, 'stochastic_rows')
            check(sum(pi[v]*P[v][u] for v in range(4)) == pi[u], 'stationarity')
            for v in range(4):
                check(P2[u][v] >= bw*pi[v], 'witness_certificate_entries')
                check(P2[u][v] >= beta*pi[v], 'actual_beta_certificate_entries')
        check(a >= 2*bw >= 2*beta, 'correct_comparison_target_gap')
        counts['clean_family_instances'] += 1
    r = Q(1,2*M)
    ps = [r/(r+bw), bw/(r+bw)]
    trans = [[1-bw,bw],[r,1-r]]
    pi = [ps[u]*trans[u][v] for u in range(2) for v in range(2)]
    P = pair_matrix([bw,1-r,bw,1-r])
    P2 = mul(P,P)
    check(P[0][1] == bw, 'null_true_target_is_witness_beta')
    if beta < bw:
        check(P[0][1] != beta, 'null_target_not_actual_certificate')
    for u in range(4):
        check(sum(pi[v]*P[v][u] for v in range(4)) == pi[u], 'null_stationarity')
        for v in range(4):
            check(P2[u][v] >= bw*pi[v], 'null_witness_certificate_entries')
            check(P2[u][v] >= beta*pi[v], 'null_actual_certificate_entries')
            check(P2[u][v]/pi[v] == trans[u%2][v//2]/ps[v//2], 'null_ratio_identity')
    counts['null_instances'] += 1

# Exact finite-domain/union equivalence, zero certificate and bounded-horizon
# control, including equality on both band boundaries at square horizons.
for M in list(range(64,130)) + [144,256,1024,4096]:
    for B in [Q(1),Q(3,2),Q(2),Q(16),Q(65536)]:
        betas = {Q(0),Q(1),Q(1,M*M),Q(1,M),Q(1,2*M),
                 min(Q(1),B/(M*M)),min(Q(1),B/(2*M*M)),
                 min(Q(1),2*B/(M*M))}
        if isqrt(M)**2 == M:
            edge = 1/(B*isqrt(M))
            betas |= {min(Q(1),edge),min(Q(1),edge/2),min(Q(1),2*edge)}
        for beta in betas:
            weak = M*M*beta <= B
            strong = beta > 0 and beta*beta*M*B*B >= 1
            G2 = Q(0) if beta == 0 else min(M**4*beta*beta,1/(beta*beta*M))
            check((G2 <= B*B) == (weak or strong), 'domain_union_equivalence')
            check(G2 <= M**4, 'bounded_horizon_bound')
            check(G2*G2 <= M**3, 'sharp_bounded_horizon_crosscheck')
            if beta == 0:
                check(weak and G2 == 0, 'beta_zero_branch')

# Broad rational points: all three L terms can control the geometric choice;
# both actual=witness and actual<witness are included. These instances are
# deliberately at sufficiently large horizons to meet KH001's finite domain.
examples = []
for q in [384,768,1536]:
    M = 2**q
    for gamma in [Q(9,16),Q(3,5),Q(2,3),Q(3,4),Q(5,6),Q(1),
                  Q(7,6),Q(4,3),Q(3,2),Q(7,4),Q(15,8),Q(31,16)]:
        p = 2*((gamma*q).__floor__()//2)
        for scale in [Q(1),Q(3,2),Q(2,3)]:
            beta = scale/2**p
            bw,U,k,T,parts = selected_budget(M,beta)
            for cnd in finite_conditions(M,beta,bw,k,T):
                check(cnd, 'complete_finite_domain')
            check(0 < beta <= bw <= Q(1,16), 'nested_certificate_domain')
            check(Q(1,M) <= bw, 'witness_lower_certificate_domain')
            check(k <= T <= M//8 < M, 'strict_legal_budget')
            check(beta*M*M >= 1, 'actual_binary_cutoff')
            # Exact rational form of the squared benchmark auxiliary bound.
            check(k*k*beta >= 1, 'actual_benchmark_log_upper_condition')
            check(4*M <= k*k, 'actual_benchmark_clean_floor_condition')
            check(T+1 > k, 'positive_harmonic_log')
            check(Q(T+1)*8 > U >= Q(T)*8, 'T_floor_sandwich')
            for i,a in enumerate(parts):
                if a == k:
                    counts[f'L_term_{i+1}_controls_floor'] += 1
            counts['actual_below_witness_cases' if beta < bw else 'actual_equal_witness_cases'] += 1
            counts['complete_budget_cases'] += 1
            source_checks(M,beta,bw,k,T)
            if scale == 1 and q == 768:
                examples.append({'log2_M':q,'beta_power':p,
                                 'k_bit_length':k.bit_length(),
                                 'witness_beta_equals_actual':beta==bw,
                                 'T_over_k_integer_lower':T//k,
                                 'k_over_sqrtM_integer_lower':k//isqrt(M)})

# Slowly escaping boundaries, sparse horizons, and a sequence repeatedly
# crossing 1/M. No floating-point rates are used as proof of a limit.
for n in [32,48,64,96,128]:
    q = 2*n*n
    M = 2**q
    choices = [Q(2**(4*n),M*M), Q(1,2**(q//2+4*n)),
               Q(2**(2*n),M) if n%3 else Q(1,M*2**(2*n))]
    for beta in choices:
        bw,U,k,T,_ = selected_budget(M,beta)
        for cnd in finite_conditions(M,beta,bw,k,T):
            check(cnd, 'slow_and_crossing_finite_domain')
        check(M*M*beta >= 2**(4*n), 'both_ratios_escape_weak')
        check(beta*beta*M <= Q(1,2**(8*n)), 'both_ratios_escape_strong')
        check(T+1 > k and k <= M, 'slow_and_crossing_legal_budget')
        counts['slow_and_crossing_cases'] += 1

# Generic exact positive-part/clean-penalty scalar accounting. Logarithm is
# represented by an arbitrary nonnegative factor: the inference is algebraic.
c = Q(1,4096)
for M in [64,256,4096]:
    for k in [1,isqrt(M),M//8,M]:
        for S in [Q(0),c*k/(256*M),c*k/(128*M),c*k/(64*M),Q(1)]:
            for ell in [Q(0),Q(1,2),Q(1),Q(1000)]:
                lower = max(Q(0),(c*k/(64*M)-S)*ell)
                check(lower >= 0, 'risk_positive_part')
                if S <= c*k/(128*M):
                    check(lower >= c*k*ell/(128*M), 'half_positive_risk_bound')
                    check(lower/(2*Q(k,M)) >= c*ell/256, 'actual_profile_ratio_bound')

for p,h in list(hashes.items()):
    check(sha(p) == h, 'end_of_run_hash_assertions')

out = {'unit':'KH002','status':'PASS','time_utc':datetime.now(timezone.utc).isoformat(),
       'candidate_sha256':EXPECTED,'assertions':sum(counts[k] for k in counts if not
       (k.endswith('_cases') or k.endswith('_instances') or k.startswith('L_term_'))),
       'counts':dict(sorted(counts.items())), 'representative_exact_cases':examples,
       'input_hashes':dict(sorted(hashes.items())),
       'scope':'Independent finite exact diagnostics; not formal verification. Universal limits, public-domain quantifiers, and estimator/kernel universality are audited in the separate full review.'}
(ROOT/'reviews/KH002_independent_exact_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'assertions':out['assertions'],'counts':out['counts']},indent=2))
