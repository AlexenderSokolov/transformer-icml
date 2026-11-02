# WM001 — Full-support weighted endpoint mixing does not give the binary cutoff

2026-11-02. New method-obstruction lemma; not a precision lower bound. No accepted source or frozen delivery changed.

## 1. Exact full-support family and all-state certificate

Order pair states as W=00,A=01,B=10,C=11. For 0<ε≤1/8 set

    a=ε³, b=1/2, e=t=ε,
    P=[[1−ε³,ε³,0,0],
       [0,0,1/2,1/2],
       [ε,1−ε,0,0],
       [0,0,ε,1−ε]].

Its stationary distribution is strictly positive:

    D=1+ε/2+2ε²,    π=(1,ε²,ε²,ε/2)/D.

Stationarity follows either by multiplication or ya=xe and wt=xb. Its exact maximal all-state two-step minorization constant is

    β*=ε²D.                                               (1)

Here is the full matrix of ratios P²(i,j)/(Dπ_j):

    [[(1−ε³)², ε(1−ε³), ε/2, ε²],
     [ε/2, (1−ε)/(2ε²), 1/(2ε), (1−ε)/ε],
     [ε(1−ε³), ε², (1−ε)/(2ε²), (1−ε)/ε],
     [ε², (1−ε)/ε, (1−ε)/ε, 2(1−ε)²/ε]].

For 0<ε≤1/8 every entry is at least ε², and equality holds at (W,C),(B,A),(C,W). This verifies every source-target cell, including all four initial states, and proves (1). In particular this is not a singular-support example or an invalid positive-a approximation to a boundary certificate.

The row-minority weights are

    q=(ε³,1/2,ε,ε).                                      (2)

## 2. A finite-horizon persistent-active estimate

Start at C. Reflect the B→W transition back to A, obtaining the stochastic active chain on A,B,C

    R=[[0,1/2,1/2],[1,0,0],[0,ε,1−ε]].

Write r_A(k),r_B(k),r_C(k) for its time-k distribution starting at C. Initially r_A(0)=r_B(0)=0, r_B(1)=ε. For k≥2,

    r_B(k)=r_A(k−1)/2+εr_C(k−1)
          =r_B(k−2)/2+εr_C(k−1)≤r_B(k−2)/2+ε.

Induction gives r_B(k)≤2ε at every k≥0, and r_A(k)=r_B(k−1)≤2ε for k≥1. Therefore r_C(k)≥1−4ε.

Couple the reflected and original chains until a B departure chooses W, with probability ε on each such departure. A union bound over the first n transitions gives

    P(coupling separates by n)≤ε Σ_(k=0)^(n−1) r_B(k)≤2nε².

This coupling is used only up to its first separation; no statement about subsequent original returns from W is needed. Hence, for every n≥0,

    P^n(C,C)≥1−4ε−2nε².                                (3)

Set n=floor(1/(16ε²)). Since ε≤1/8, n≥4 and

    P^n(C,C)≥3/8,    π_C=ε/(2D)≤1/16,
    |P^n(C,C)−π_C|≥5/16.                               (4)

## 3. Both proposed endpoint inequalities fail

For the same family and μ=δ_C, (2)–(4) imply

    Σ_s q_s |(μP^n)_s−π_s| ≥ (5/16)ε.                  (5)

They also imply the stronger future-weighted residual lower bound

    Σ_s |(μP^n)_s−π_s| (P^n q)(s)
      ≥ |P^n(C,C)−π_C| q_C P^n(C,C)
      ≥ (15/128)ε.                                    (6)

All terms are nonnegative, so retaining just s=C is legitimate. The future factor is exactly P^nq, not a marginal substitute.

For any fixed positive constants C0,c0, both

    C0/n+C0 exp(−c0 n sqrt(β*))

and the same expression with n replaced by M=2n are o(ε) as ε decreases to zero: n is asymptotic to 1/(16ε²), sqrt(β*)=εsqrt(D), and therefore n sqrt(β*) is asymptotic to 1/(16ε). Equations (5) and (6) refute universal inequalities of those forms. In particular (6) directly refutes the proposed u=m=M/2 complete-suffix transfer bound with q-terminal domination, even in the strictly full-support class.

## 4. Scope: a method obstruction, not an arbitrary-start precision separation

The active chain has a long lifetime, but it starts active and accumulates many visits to its likely terminal state C. Endpoint-only couplings erase this count information. Nothing above lower-bounds the unchanged SB001 decoder's error, or disproves the desired arbitrary-start binary precision upper/frontier.

The valid conclusions are only that (i) full stationary support does not rescue square-root-beta weighted marginal mixing with a C/n remainder, and (ii) even weighting the residual at a midpoint by future expected terminal minority probability does not rescue that bound. A successful argument must retain occupation counts or another path-sensitive quantity.

## 5. Provenance and verification

Direct context: accepted BU001 v2 weighted stationary-return upper; BS001 stationary frontier; BAI001 arbitrary-initialization obstruction record; accepted BAI003 v2 absorbing-boundary upper. Exact source hashes are in WM001_source_bindings_v1.json. The proof is self-contained and does not import a new upper/lower theorem from these sources.

WM001_diagnostics_v1.py checks exact rational stationarity and all 16 certificate ratios on a grid, and finite numerical residuals. The checks corroborate, not replace, the universal symbolic inequalities above. This is author work pending independent review, not formal verification or external novelty/publication.
