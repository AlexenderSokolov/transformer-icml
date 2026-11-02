# PL001 — A logarithmic precision obstruction at the complete finite SRC master cut

2026-11-02. **Author candidate, not yet independently reviewed or accepted.**

## Result first

For every fixed alphabet size **K≥5**, horizon **M≥6**, and **h≥4**, put Q=2^h and execute the original SRC-Pi *statistical master prefix* with its actual finite log/exponential evaluator and the complete 9K+1 post-quantization master bank. Allow an arbitrary decoder, arbitrary computation, arbitrary real simplex output, source-independent randomness, and **all** of the exact side information allowed at that cut. No raw-history reread or extra clean statistical port is added. Then

    inf_decoder sup_(theta,mu in D2(0))
      E TV(decoder,theta_(Y_M))
        ≥ ln(1+8Q)/(1024 Q).                              (PL1)

This is an **internal master-quantization** lower bound, not an output-grid lower bound. In particular, it survives unrestricted real outputs and unlimited decoder computation.

Together with the inherited full-history D2(0) minimax lower bound, the restricted minimax risk is at least

    max{2^(-17) min(1,sqrt(K^5/(M+1))),
        ln(1+8Q)/(1024 Q)}.                              (PL2)

The two lower witnesses need not coincide. They are not added.

Consequently, for each fixed K≥5, obtaining O_K(M^(-1/2)) risk uniformly over D2(0), hence also obtaining the all-beta minimax rate with the same fixed prefix, requires

    Q=Omega_K(sqrt(M) ln M),
    h≥(1/2)log2 M+log2 ln M-O_K(1).                     (PL3)

The same necessity holds if the decoder is told beta=0. It is not a price of beta-blindness. NB002's candidate sufficient Q=Theta_K(sqrt(M) log M) therefore has the right fixed-K order for this specific complete master interface, if NB002 is independently accepted. This does **not** establish alphabet-uniform optimality or a result for K=2,3,4. The witness below has a periodic active class and proves only the beta=0 lower; no positive-beta lower is claimed.

The original *complete old suffix* was stated only for h≥max(4,ceil(log2 M)+1). Here, as in NB002, only its same finite master prefix is retained and h≥4 is allowed. This is an explicitly enlarged prefix domain, not a retroactive claim that the old smoothing suffix was legal there. All its head denominators remain positive. The lower proof below uses the exact finite formulas, not the ideal-head error envelope.

## 1. Exact experiment and relevant source facts

The source is the full deterministic fact

    v10_intake/source/sources/euler-stage6/facts/fef8372728290b45.md

especially proof §§2,4,8. At the final synthetic position q=N+1, keys are exactly t=3,...,N, N=M+2. The master bank is

    P1(q1,v1), P2(q2,v2), T(hvec,h0),
    uniform(alpha,nu,f,rho),

with respectively 2K,2K,2K,3K+1 coordinates. The exact query/mode/endpoint/flag bits and public metadata remain available. Clean finite numerator/denominator/exponential/remainder working words and historical projections are released before this cut. The decoder cannot inspect the history again. No port is artificially removed in PL1.

Write R=2^p, where p=4h+4ceil(log2(M+K+4))+64. The finite log constants satisfy L2≤ln2 and L3≤ln3. For a finite score s, the evaluator starts T0=R, then

    T_r=floor(T_(r-1) (R s)/(r R)), r=1,...,8p,
    W(s)=sum_(r=0)^(8p) T_r.

It has, exactly,

    W(0)=R,
    R≤W(L2)≤2R,
    R≤W(2L2)≤4R,
    R≤W(L2+L3)≤6R.                                    (1)

These inequalities follow directly by induction T_r/R≤s^r/r! and the lower term T0=R; no asymptotic numerical approximation is used. An output coordinate for bit values v_t is exactly

    (1/Q) floor(Q sum_t W(s_t)v_t / sum_t W(s_t)).       (2)

The denominator is at least MR. Thus these very prefix formulas remain defined at every h≥4 irrespective of Q/M. All integer accumulators and public constants are those already specified in SRC; this proof does not create an alternate encoder.

## 2. One homogeneous five-symbol source family

Use five distinct symbols W,A,B,C0,C1 in the K-letter alphabet. For p0∈[1/4,3/4], fix a homogeneous second-order table as follows:

    theta_WW(W)=1-1/M, theta_WW(A)=1/M;
    theta_WA(B)=1;
    theta_AB(C1)=p0, theta_AB(C0)=1-p0;
    theta_(B,Ci)(A)=1, theta_(Ci,A)(B)=1, i=0,1.

Set every remaining row to delta_W, for definiteness, and initialize X1=X2=W. There is no time-varying transition rule. The source parameter p0 is unknown to the decoder. All tables belong to D2(0): a finite chain has a stationary probability law, and the beta=0 minorization is vacuous. One explicit stationary law gives each phase of the active three-cycle total mass 1/3, with the C1 and C0 branch states weighted p0 and 1-p0.

Let T≥1 be the first departure from WW that emits A. Then

    P(T=t)=(1/M)(1-1/M)^(t-1),                         (3)

independently of p0. The next symbol is B. Subsequent complete cycles are

    (A,B) --emit Ci--> (B,Ci) --emit A--> (Ci,A)
          --emit B--> (A,B).

Every cycle has exactly three departures, independently of its coin value. The coin choices on successive AB departures are independent Bernoulli(p0), by the specified homogeneous Markov law.

For

    j=0,...,Jmax, Jmax=floor((M-3)/3),
    t_j=M-1-3j,
    E_j={T=t_j},

we have t_j≥2 and the actual terminal endpoint is **exactly (A,B)**. There are j completed active cycles and exactly j observed AB departures. The target next-symbol distribution is theta_AB, including at j=0. Let S be the number of C1 coin outcomes; conditional on E_j,

    S~Binomial(j,p0).                                  (4)

The complete observed transition multiset is

|Triple|Count|
|---|---:|
|WWW|t_j-1|
|WWA|1|
|WAB|1|
|ABC1, BC1A, C1AB|S each|
|ABC0, BC0A, C0AB|j-S each|

The counts sum to t_j+1+3j=M. This table is independent of the order of the j coins. In particular X1=X2=X3=W on these events; every initial local flag and its allowed exact copy is fixed. The actual endpoint, actual query, mode and final local flags are fixed. Position/type metadata is public. Allowing the decoder **extra exact j** (equivalently exact t_j on these events) can only make the lower bound stronger; we do allow this extra oracle in the argument. No full-history bit is being silently suppressed.

## 3. All masters, including the finite evaluator

The query is (A,B). For P1 and P2, only AB keys have nonzero score; all other triples in the table have both query matches false. Their integer weights are

    w4=W(2L2), w6=W(L2+L3),

on AB keys and R on the others. For T, only BCi keys have nonzero score, with integer weight w2=W(L2). Set

    D1=MR+(w4-R)j,
    D2=MR+(w6-R)j,
    DT=MR+(w2-R)j.                                    (5)

These exact finite integer denominators depend on M,h,K,j, not on S, p0, or the order of the coin choices. This explicitly incorporates the evaluator: w6 is the direct evaluation at L2+L3, not a product of two rounded exponentials.

The **only** master coordinates that vary with S are the following seven pairs. In the table, displayed expressions are the integer numerators of the Q-grid master words; the master itself is that integer divided by Q.

|Coordinate pair (C1,C0)|Exact integer numerator pair|
|---|---|
|q1|floor(Q w4 S/D1), floor(Q w4(j-S)/D1)|
|v1|floor(Q R S/D1), floor(Q R(j-S)/D1)|
|q2|floor(Q w6 S/D2), floor(Q w6(j-S)/D2)|
|v2|floor(Q R S/D2), floor(Q R(j-S)/D2)|
|hvec|floor(Q w2 S/DT), floor(Q w2(j-S)/DT)|
|alpha|floor(Q S/M), floor(Q(j-S)/M)|
|nu|floor(Q S/M), floor(Q(j-S)/M)|

All remaining coordinates are independent of S. This includes every h0,f,rho coordinate, not merely the main frequency heads. More explicitly, h0_W has numerator floor(Q R/DT), f_W and rho have numerator floor(Q/M), and other h0/f entries are zero. The W,A,B head coordinates follow directly from the preceding triple table and depend only on j,t_j. Additional alphabet coordinates are zero. Exact query/endpoint/flag side information has already been fixed or granted in §2.

This shows that, conditional on E_j, the *entire permitted decoder input* is a deterministic function of S (and public/granted j), even though the original history has up to 2^j possible active arrangements. We neither condition the terminal row as if it were an independent query nor remove the endpoint; the source makes that endpoint deterministic on the selected events.

## 4. A joint-cell count, not a coordinate-product bound

For fixed j, let D_j be the number of distinct complete master vectors attainable as S ranges over the integers 0,...,j. Every listed C1 coordinate is nondecreasing and every C0 coordinate is nonincreasing. A monotone integer coordinate can change at most its total endpoint integer difference times. Therefore the total number of distinct joint vectors is at most one plus the sum of all these endpoint differences. This is a union of threshold crossings along a one-dimensional ordered sequence, **not** the product of coordinate cardinalities.

For each pair of the form floor(aS),floor(a(j-S)), the endpoint-difference sum is exactly 2floor(aj), at most 2aj. Because all numerators vanish at S=0 on the C1 side and S=j on the C0 side, no additional per-coordinate rounding constant is needed. From (1),(5),

    D_j ≤ 1+2jQ(4/M+1/M+6/M+1/M+2/M+1/M+1/M)
        = 1+32Qj/M.                                   (6)

Also D_j≤j+1, but we do not need that refinement. Duplicate alpha/nu coordinates were counted twice, which is a safe overcount. This is where all the extra master ports are paid for in the information argument: they alter the constant 32, but do not create a multiplicative number of distinguishable cells.

## 5. Finite-message Bayes quantization lemma

**Lemma.** Let P be uniform on an interval I of length ell. Suppose a possibly noisy experiment, conditional on P, emits one of at most D messages. Any decoder with source-independent randomness and real scalar output Z satisfies

    E|Z-P| ≥ ell/(4D).                                 (7)

**Proof.** First fix the decoder's source-independent seed. Its at most D scalar output values are z1,...,zD, and for every realization |Z-P|≥min_d |zd-P|. For any u≥0, the union of radius-u intervals around these D values covers at most 2Du length inside I. Hence, with P uniform,

    P(min_d |zd-P|>u) ≥ 1-2Du/ell, 0≤u≤ell/(2D).

Integrating this tail gives ell/(4D). The bound is uniform in the fixed seed, so averaging the seed proves the result. This does not presume that the message is a deterministic quantization of P; it covers arbitrary stochastic channels, including the binomial noise in (4). Equivalently, one may remove decoder randomness by conditional Jensen. ∎

Apply the lemma with the prior p0 uniform on [1/4,3/4], ell=1/2, conditional on E_j and granting exact j. Because P(E_j) is independent of p0, the prior remains uniform after this conditioning. The target has theta_AB(C1)=p0, and every simplex prediction z satisfies

    TV(z,theta_AB)≥|z(C1)-p0|.

By (6),(7), every decoder has conditional Bayes risk at least

    1/[8(1+32Qj/M)].                                  (8)

This is an estimation lower bound for the true next-symbol law, not merely a discrepancy from empirical add-one counts. Binomial noise cannot circumvent it, and no lower bound on the size of j is needed.

## 6. Geometric averaging supplies the logarithm

For M≥2 and every selected j, (3) yields

    P(E_j)≥(1/M)(1-1/M)^(M-1)≥1/(eM)>1/(4M).          (9)

For completeness, ln(1-x)≥-x/(1-x) at 0≤x<1, applied with x=1/M, proves the middle bound. Events E_j are disjoint. Discarding the nonnegative loss outside their union and applying (8),(9), the Bayes risk is at least

    (1/(32M)) sum_(j=0)^Jmax 1/(1+32Qj/M).

The summand is decreasing. Its left-endpoint sum is at least its integral over [0,Jmax+1], so this is at least

    (1/(1024Q)) ln(1+32Q(Jmax+1)/M).                   (10)

For M≥6, Jmax+1=floor(M/3)≥M/4. Equation (10) proves PL1. A supremum over the source parameter p0 is at least its uniform-prior average, so the result holds for minimax risk. The maximizing p0 may depend on the decoder,M,h, as is allowed by a uniform lower bound; within every experiment theta is homogeneous and fixed.

We restricted t_j≥2 only to make even X3 constant. With the precisely stated original cut this is not necessary: allowing t_j=1 leaves F_t=z_t lag1_t fixed as well and gives the same displayed lower for M≥2. The conservative theorem PL1 uses M≥6 and the t_j≥2 restriction, so no small-horizon or flag interpretation is needed.

## 7. Necessary precision and exact scope

Suppose for fixed K≥5 that a sequence of such decoders has sup_D2(0) risk≤C_K/sqrt(M+1). PL1 implies

    Q/ln(1+8Q) ≥ sqrt(M+1)/(1024 C_K).

Since h≥4, ln(1+8Q) is bounded below by a positive absolute constant, first Q≥c_K sqrt M. Substituting this into the logarithm then gives Q≥c'_K sqrt M ln M for sufficiently large M. Taking log2 yields PL3. Constants may depend on K and the requested risk factor; no sharp numerical constant is claimed.

This shows a true distinction between two experiments:

1. **Output-only Q-simplex grid, full history retained:** paid direct counts plus ordered output rounding have additional error O(K/Q), and the root's output-grid lower gives the matching order. At fixed K, Q=Theta(sqrt M) suffices.
2. **Fixed bounded-score SRC master prefix, uniform internal Q-grid, arbitrary suffix:** PL1 forces the extra logarithm in Q for fixed K≥5, even without an output grid. NB002's candidate upper has the matching fixed-K logarithmic scale.

It does not follow that every uniformly quantized attention architecture, every bounded-score encoder, every alternative normalization, or every paid extra-port implementation needs the logarithm. The proof uses the *fixed* full SRC statistics and their exact side-information contract. It also says nothing about lower bounds on neural depth/width, other arithmetic word lengths, training, or global resource optimality. The arithmetic precision p remains Theta(log M+h), separately from master precision h.

## 8. Failure log and remaining checks

- Initial concern: a normalized queried-row count alone is insufficient for an SRC lower, because the other 9K+1 masters and the endpoint may encode the parameter. **Resolved for this witness:** all of them are included in §3, and the *joint* label count is bounded in §4.
- Initial concern: a geometric wait plus generic active IID segment produces many empirical triple counts and can make coordinate partitions refine each other. That approach needs a concentration/tube argument. **Not used:** fixed-length return cycles make every relevant statistic a function of the single binomial count S, exactly.
- Initial concern: ideal exponential formulas need not describe the real finite bank. **Resolved:** §§1,3 use integer w2,w4,w6 from the actual recurrence and direct full-score evaluation.
- A scalar pathwise numerical error upper bound cannot prove a lower bound against an arbitrary decoder. **Avoided:** this proof is a finite-message Bayes argument for the whole bank.
- The source has a period-three active class, so its positive-beta two-step minorization fails. **Unresolved beyond present scope:** no claim for beta>0 or K<5 is made.
- The full theorem needs independent review, including exact side-port/lifecycle reading. The accompanying diagnostic is only an exact finite arithmetic check of the formulas and does not substitute for the proof or claim to run the unavailable original emitter.

## Sources/provenance

- Full SRC fact and proof, `v10_intake/source/sources/euler-stage6/facts/fef8372728290b45.md`, particularly §§2,4,8: fixed master coordinates, finite recurrence and side-port lifecycle.
- `v10_intake/source/RESEARCH_STATE.md`: full homogeneous-source experiment and D2(beta) definition; inherited R011 lower scale.
- `v10_research/network_bridge/NB002_conservative_guard_sublinear_grid_v1.md`: independently reviewed/accepted status must be checked by root; only the candidate matching upper and enlarged prefix domain are compared here, not assumed to prove the lower.
- `v10_research/root/output_grid_lower_v1.md`: different output-only benchmark; no internal lower is inferred from it.

New proof method: a five-symbol regenerative witness with fixed three-step active return length, exact finite-master affine reduction, monotone joint-cell counting, and one-dimensional finite-message Bayes quantization. This candidate does not assert external novelty.
