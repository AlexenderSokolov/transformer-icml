#!/usr/bin/env python3
"""Fresh exact diagnostics, not a universal proof or formal verification.

Written independently of check_jb001.py and predecessor diagnostic programs.
All assertion arithmetic uses Python integers or fractions.Fraction.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
RNG = random.Random(202611021217)
COUNTS = Counter()
PROOF_HASH = sha256((HERE / 'JB001_theorem.md').read_bytes()).hexdigest()


def ceil_sqrt(m):
    r = isqrt(m)
    return r + (r*r < m)


def clip(x):
    return min(F(1), max(F(0), x))


def floor_grid(x, q):
    return F((x*q).numerator // (x*q).denominator, q)


def decode(row, m):
    # Same map implemented directly on grid labels; no budget/certificate input.
    b = 12*ceil_sqrt(m)
    return row[0]/sum(row) if m*row[0] > b else F(0)


def pathwise(c, j, cp, rp, d, b):
    assert 0 <= c <= j and isinstance(c, int) and isinstance(j, int)
    assert cp >= 0 and rp >= 0 and 0 <= 2*d <= b
    assert abs(cp-c)+abs(rp-(j-c)) <= d
    jp = cp+rp
    p = F(c, j) if j else F(0)
    phat = cp/jp if cp > b else F(0)
    assert 0 <= phat <= 1
    COUNTS['active' if cp > b else 'inactive'] += 1
    if cp > b:
        assert c > d and j >= 1
        assert abs(phat-p) <= 2*d/j
        assert phat <= 4*p
        assert abs(phat-p) <= min(4*p, 2*d/j)
    # On each interval the gap is affine. Include every breakpoint and the
    # threshold's right-hand limit, which may be smaller than its point value.
    qs = {F(0), F(1), p, phat, F(6)*d/(j+2)}
    if j:
        qs.add(F(3*b, j))
    qs = sorted(q for q in qs if 0 <= q <= 1)
    qs += [(x+y)/2 for x,y in zip(qs, qs[1:])]
    for q in qs:
        e = abs(p-q) if j else F(0)
        threshold = q if q > 0 and q*j <= 3*b else F(0)
        rhs = 5*e+4*min(q, 6*d/(j+2))+threshold
        assert abs(phat-q) <= rhs, (c,j,cp,rp,d,b,q)
        COUNTS['critical_probability_inequalities'] += 1
    if j and 0 < F(3*b,j) < 1:
        q = F(3*b,j)
        rhs_right = 5*abs(p-q)+4*min(q,6*d/(j+2))
        assert abs(phat-q) <= rhs_right
        COUNTS['threshold_right_limits'] += 1
    COUNTS['relaxed_real_pseudorows'] += 1


def test_real_pseudocounts():
    # Fractions with odd denominators are deliberately not grid-realizable.
    for m in (64,65,80,100,143,144,145,255,256,257,1024,4096,65536):
        b = 12*ceil_sqrt(m)
        for d in (F(0),F(1,7),F(5,3),F(b,6),F(b,2)-F(1,13),F(b,2)):
            for j in sorted({0,1,2,m//8,m//2,m,b//2,b,b+1,2*b,4*b}):
                if j > m:
                    continue
                candidates = {0,j,j//2,min(j,b),min(j,b+1),min(j,b//2)}
                for c in sorted(candidates):
                    for a in (F(0),-d,d,-d/3,d/3):
                        for r in (F(0),-(d-abs(a)),d-abs(a)):
                            if c+a >= 0 and j-c+r >= 0:
                                pathwise(c,j,c+a,j-c+r,d,b)
        # Threshold equality and genuinely fractional strict crossings.
        for j in (m//2,m):
            for c in (min(j,b-1),min(j,b),min(j,b+1)):
                for gap in (F(-1,17),F(0),F(1,17)):
                    cp = F(b)+gap
                    rp = F(j-c)
                    d = abs(cp-c)
                    if 2*d <= b:
                        pathwise(c,j,cp,rp,d,b)
    for _ in range(18000):
        m = RNG.choice((64,65,144,255,256,1024,4096,65536))
        b = 12*ceil_sqrt(m)
        j = RNG.randrange(m+1)
        c = RNG.randrange(j+1)
        den = RNG.choice((3,5,7,11,16,31))
        d = F(RNG.randrange(b*den//2+1),den)
        a = F(RNG.randrange(-d.numerator,d.numerator+1), d.denominator)
        remain = d-abs(a)
        r = remain*F(RNG.randrange(-9,10),9)
        if c+a >= 0 and j-c+r >= 0:
            pathwise(c,j,c+a,j-c+r,d,b)


def histogram(word):
    counts = [0]*8
    for i in range(len(word)-2):
        counts[4*word[i]+2*word[i+1]+word[i+2]] += 1
    return counts


def taylor_weight(p, shift):
    d = 1 << p
    a = 2*shift
    term = d
    w = term
    for j in range(1,8*a*a+2+p+1):
        term = term*(d*shift)//(j*d)
        w += term
    assert w >= d > 0
    return w


def test_exact_uniform_bank():
    for m in list(range(64,201)) + [255,256,257,1023,1024]:
        for h in range(4,10):
            q = 1 << h
            for p in (h,h+1,h+5):
                d = 1 << p
                w = taylor_weight(p,1)
                for c in range(m+1):
                    # Full-width accumulators and positive-weight cancellation.
                    out = (w*d*c)//(m*w)
                    assert out == d*c//m
                    assert out*q//d == q*c//m
                    assert (out == 0) if c == 0 else True
                    assert (out == d) if c == m else True
                    COUNTS['uniform_cancellation_nested_floor'] += 1
    # Direct clipping/flooring, exact perturbations with non-dyadic denominators.
    for m in (64,65,127,128,255,256,1024):
        for q in (16,32,64,256):
            for d in (q,2*q,32*q):
                for c in sorted({0,1,2,m//3,m//2,m-1,m}):
                    a = F(d*c//m,d)
                    for delta in (F(0),F(1,97),F(1,q),F(1,4)):
                        for eta in (-delta,-delta/3,F(0),delta/7,delta):
                            z = floor_grid(clip(a+eta),q)
                            assert abs(z-F(c,m)) <= delta+F(1,d)+F(1,q)
                            assert 0 <= z <= 1 and (z*q).denominator == 1
                            COUNTS['scalar_noisy_clipped_bank'] += 1


def test_noisy_edited_words():
    for m in (64,65,96,127,128,144,255,256,1024,4096):
        q = 1 << max(4,(4*ceil_sqrt(m)-1).bit_length())
        for repeat in range(75):
            mode = repeat % 5
            word = ([0]*(m+2) if mode == 0 else [1]*(m+2) if mode == 1
                    else [i%2 for i in range(m+2)] if mode == 2
                    else [int(i%37==0) for i in range(m+2)] if mode == 3
                    else [RNG.randrange(2) for _ in range(m+2)])
            clean = histogram(word)
            for k in sorted({0,1,isqrt(m)//4,isqrt(m)//2}):
                corrupted = list(word)
                for i in RNG.sample(range(m),k):
                    corrupted[i] ^= 1
                edited = histogram(corrupted)
                assert corrupted[-2:] == word[-2:]
                assert sum(abs(x-y) for x,y in zip(clean,edited)) <= 6*k
                for delta in (F(0),F(1,3*q),F(1,q),F(1,2*ceil_sqrt(m))):
                    tau = F(k,m)+delta+F(1,q)
                    if tau*tau*m > 1:
                        continue
                    for factor in (1,2,32):
                        dgrid = factor*q
                        a = [F(dgrid*c//m,dgrid) for c in edited]
                        etas = [RNG.choice((-delta,-delta/3,F(0),delta/7,delta)) for _ in a]
                        if repeat % 7 == 0:
                            etas = [delta]*8
                        if repeat % 11 == 0:
                            etas = [-delta]*8
                        z = [floor_grid(clip(x+eta),q) for x,eta in zip(a,etas)]
                        b = 12*ceil_sqrt(m)
                        error = 6*k+2*m*(delta+F(2,q))
                        assert error <= 6*m*tau and 2*error <= b
                        u = 2*word[-2]+word[-1]
                        designated = 1-word[-2]
                        idx = 2*u+designated
                        other = 2*u+1-designated
                        cp,rp = m*z[idx],m*z[other]
                        c,j = clean[idx],clean[idx]+clean[other]
                        assert abs(cp-c)+abs(rp-(j-c)) <= error
                        result = decode([z[idx],z[other]],m)
                        assert result == (cp/(cp+rp) if cp > b else 0)
                        pathwise(c,j,cp,rp,error,b)
                        COUNTS['word_noise_cases'] += 1
                        COUNTS['nonintegral_selected_pseudorows'] += int(cp.denominator != 1 or rp.denominator != 1)
                        COUNTS['nonunit_total_pseudohistograms'] += int(sum(z) != 1)
                        COUNTS['boundary_clipped_coordinates'] += sum(x+eta < 0 or x+eta > 1 for x,eta in zip(a,etas))


def test_constants():
    for m in range(64,100001):
        b = 12*ceil_sqrt(m)
        assert b*b >= 144*m
        # Squared positive quantities certify the finite threshold coefficient.
        assert 64**2*(3*b+1)**2*m <= 2600**2*(m+1)**2
        COUNTS['finite_m_threshold_constants'] += 1
    rest = 2600+16+32*16672
    assert (2**20-rest)**2 > (5*8193)**2*32
    assert 144*16672 == 2400768 < 2**22
    # The singleton bound for A>=2 is <=264A/M.
    for m in (64,65,255,256,65536):
        for a in (F(2),F(15,7),F(13,2),F(m),F(1000000,3)):
            assert 256*a/m+F(16,m+2) <= 264*a/m
            COUNTS['singleton_A_domain_constants'] += 1


def bindings():
    result = {}
    for unit in ('JP001','AB003','SC003','BIF001','BAI003','BC001','FA001'):
        receipt_path = BASE/'intake'/f'{unit}_acceptance.json'
        receipt = json.loads(receipt_path.read_text())
        proof = BASE/receipt['proof']
        digest = sha256(proof.read_bytes()).hexdigest()
        assert digest == receipt['sha256'], (unit,digest,receipt['sha256'])
        entry = {
            'proof':str(proof.relative_to(BASE)), 'proof_sha256':digest,
            'receipt':str(receipt_path.relative_to(BASE)),
            'receipt_sha256':sha256(receipt_path.read_bytes()).hexdigest(),
            'accepted_proof_hash_matches':True,
            'status':receipt['status'],
        }
        if unit in ('JP001','AB003'):
            review = BASE/receipt['review']
            review_hash = sha256(review.read_bytes()).hexdigest()
            assert review_hash == receipt['review_sha256']
            entry['review'] = str(review.relative_to(BASE))
            entry['review_sha256'] = review_hash
            entry['accepted_review_hash_matches'] = True
        result[unit] = entry
    return result


def main():
    test_real_pseudocounts()
    test_exact_uniform_bank()
    test_noisy_edited_words()
    test_constants()
    dependencies = bindings()
    assert sha256((HERE/'JB001_theorem.md').read_bytes()).hexdigest() == PROOF_HASH
    output = {
        'status':'PASS',
        'scope':'Independent exact finite diagnostics, not formal verification or universal proof',
        'theorem':'JB001_theorem.md', 'theorem_sha256':PROOF_HASH,
        'diagnostic_script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'all_assertion_arithmetic':'integers and exact rational fractions; no floating comparisons',
        'counts':dict(COUNTS), 'accepted_dependencies':dependencies,
    }
    (HERE/'JB001_independent_checks.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'status':output['status'],'theorem_sha256':PROOF_HASH,'counts':dict(COUNTS)},indent=2))


if __name__ == '__main__':
    main()
