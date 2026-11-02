# UI001 — A weight-range-uniform stationary IID precision floor

2026-11-02. Author theorem; independent audit pending. No frozen source is changed.

## Statement and source contract

Use exactly BA001's one-block local ratio model, as restated in SH001 §1: M>=64, n=M+2, trailing windows L_i of length at most r (public padding), i=3,...,n, at most D scalar ratios, weights in [1,κ], values in [-1,1], downward quantization floor(QB_d)/Q, and exact boundary side S consisting of the first/last min(r,n) symbols. D,r>=1 are fixed. κ>=1 and Q>=1 are arbitrary finite REAL numbers. Position-specific tables and boundary-query-dependent tables are arbitrary source-independent real tables. The decoder is unrestricted but sees only this bank, S and public metadata; independent encoder/decoder randomness is allowed. All BA001 exclusions (nonlocal interior features, extra interior side fields, history rereads, hard selected-key masks, recursive global blocks) remain.

There is c=c(D,r)>0, independent of κ,M,Q,K,β and table contents, such that the minimax risk even over stationary binary IID sources is

    R_IID >= c/Q.                                             (UI1)

Consequently the stationary second-order source class satisfying the all-state certificate P²(s,t)>=βΠ(t) has the same lower for EVERY β in [0,1]. This is not a full two-resource minimax theorem or an upper construction.

Here are deliberately loose constructive constants:

    H=3^(2r), F=DH, q=4^(-r), L=rF+2r,
    J=(2rL+1)/q, V=4r²J/q,
    C=ceil(max{1,400F(2r-1)/q²,3200FV}),
    P0=128 sqrt(L(C+1)), R0=(2+48r)9^D,
    c=min{1/(128sqrt(C+3)), 1/(32R0 P0)}.

These constants are architectural only. Their inefficiency is irrelevant to uniformity in an arbitrarily growing weight range.

## 1. IID experiment and small-history case

On symbols C0,C1 take all n observations IID Bernoulli(p). Define every second-order row, including unsupported pair states, as this same law. Its stationary pair distribution is the product law and P²(s,t)=Π(t) for all s,t. The true next-symbol C1 probability is p at every terminal context. Hence TV loss is at least |estimate(C1)-p|.

Put m=ceil(CQ²). If M<m, grant the decoder the full history. The two points p±=1/2±1/(16sqrt(n)) have history KL at most 1/8, total variation at most 1/4, and absolute-estimation Bayes risk at least 1/(128sqrt(n)), by the elementary testing calculation in BA001 §6. Since n=M+2<m+2<=(C+3)Q², this proves UI1 with its first constant. This branch and its prior do not depend on encoder seeds.

Henceforth M>=m. Use ONE prior p uniform on I=[1/4,3/4]. Fix and grant an encoder seed; the same prior and constants work for every seed.

## 2. A public heavy-window reveal

There are at most H binary boundary patterns s (including consistent overlaps). Freeze each q(s) in the tables, without conditioning the sample on S=s. For every d,s,i let a_dsi be the maximum weight over attainable binary patterns in L_i, with padding fixed. It is a public number in [1,κ]. Select m distinct positions with largest a_dsi, with public tie-breaking, for each d,s. Reveal all bits in all these selected windows and all boundary bits. This is a fixed set U of distinct positions, chosen independently of p and of the sampled bits. Write N=|U| and B=X_U, in public order. Since every selected window contains its endpoint and there are m distinct selected endpoints,

    m <= N <= rFm+2r <= Lm.                                (2.1)

Giving B strengthens the experiment; it does not alter the original encoder or charge any upper construction. Conditional on B, all remaining bits are still independent Bernoulli(p). B also fixes the actual S.

For each selected position choose one maximizing local pattern. Its indicator has expectation at least q under every p in I. Indicators attached to disjoint trailing windows are independent; each overlaps at most 2r-2 other selected windows. Therefore the variance of their sum is at most (2r-1)m. Chebyshev gives probability at most 4(2r-1)/(q²m) of fewer than qm/2 maximizing patterns. Union over at most F pairs (d,s) gives a failure probability at most .01. Call the complementary event E. Crucially E is determined by B, and

    P_p(E)>=.99 for every p in I.                          (2.2)

For a fixed d,s let a_* be the largest maximum among its unselected positions, or zero if none. On E, the sum W of its selected weights, now entirely known, satisfies

    W >= (qm/2) a_*.                                     (2.3)

No independence between different branches or between E and S is used. Padding or short windows only increase the probability lower bound q.

## 3. Conditional concentration independent of κ

Fix a revealed pattern B in E and p in I. For one frozen pair d,s write A,Dn for the numerator and denominator, μ_A=E_p[A|B], μ=E_p[Dn|B], and h=μ_A/μ. Thus |h|<=1 and μ>0. Selected contributions are constants. All unselected a_i are at most a_*.

Partition unselected windows into those intersecting U and those disjoint from U. There are at most rN intersecting windows, because each revealed bit occurs in at most r windows. Their total maxima are at most rN a_* <=rLm a_* <=(2rL/q)μ, by (2.3). Each disjoint window retains an IID binary pattern, so its conditional expected weight is at least q a_i. Consequently

    sum_unselected a_i <= J μ,  J=(2rL+1)/q.               (3.1)

This step explicitly handles partially revealed windows: their conditional maxima can be unattainable, and no q a_i expectation bound is asserted for them.

Resample one remaining independent bit. Either sum A or Dn changes by at most 2 sum_{i affected,unselected} a_i. There are at most r such indices; Cauchy–Schwarz and the Efron–Stein inequality therefore give

    Var(A|B), Var(Dn|B)
      <=2r² sum_unselected a_i²
      <=2r² a_* J μ <= V μ²/m,                            (3.2)

where (2.3) gives a_*<=2μ/(qm). If there are no unselected positions, both variances are zero and the same conclusion holds without division by a_*.

Chebyshev at threshold μ/(4Q), for both sums and all at most F frozen pairs, shows with conditional probability at least .99 that all corresponding deviations are at most their respective μ/(4Q): the failure bound is at most 32FVQ²/m<=.01. On this event Dn>=3μ/4, and exact ratio subtraction yields

    |A/Dn-h| <= (|A-μ_A|+|Dn-μ|)/Dn <=2/(3Q)<1/Q.         (3.3)

The comparison is a ratio of conditional expectations, not the conditional expectation of a ratio. This argument holds for EVERY p in I and EVERY B in E; goodness may depend on p.

For later use, the conditional curves are uniformly Lipschitz. A remaining-bit pattern on any window has at most r free bits, and the absolute logarithmic derivative of its Bernoulli probability on I is at most 4r. Positivity of weights and |v|<=1 imply

    |μ_A'|<=4rμ,  |μ'|<=4rμ,  hence |h'|<=8r.             (3.4)

Constant terms have derivative zero. This proof applies unchanged to partially revealed windows and arbitrary positional tables, with no κ factor.

## 4. The oracle posterior, correctly accounted for

The uniform prior DOES NOT remain uniform after observing B. Let t be the number of its N ones and y=t/N. The posterior density on I is proportional to p^t(1-p)^(N-t). Define

    I_B=I intersect [y-3/sqrt(N), y+3/sqrt(N)].

Hoeffding and prior integration give joint probability P(p notin I_B)<=2 exp(-18). By Markov, the set T of B for which posterior mass of I_B is at least .99 has probability at least 1-200 exp(-18). In particular I_B is nonempty on T, and distance(y,I)<=3/sqrt(N). Thus

    P(B in E intersect T)>=.99-200 exp(-18)>.98.           (4.1)

For completeness, posterior density has a uniform bound on T. Put ℓ(p)=t log p+(N-t)log(1-p), and let p0 be y clamped to I, its maximum. The formula ℓ'(p)=N(y-p)/(p(1-p)) gives |ℓ'(p0)|<=16sqrt(N), while |ℓ''(p)|<=16N on I. From p0 at least one direction remains in I for length 1/4. Integrate along that direction for δ=1/(64sqrt(N)); Taylor's theorem gives

    ℓ(p)>=ℓ(p0)-16sqrt(N)δ-8Nδ² > ℓ(p0)-log 2.

The posterior normalizer is therefore at least exp(ℓ(p0))/(128sqrt(N)), so

    sup_I posterior_density <=128sqrt(N)<=P0 Q,           (4.2)

using N<=Lm<=L(C+1)Q². This includes modes on either truncation boundary, and t=0 or t=N whenever they satisfy T. No asymptotic normal approximation is used.

## 5. Constant good alphabet after the reveal

Fix B in E intersect T. Its actual side S=s is known; only this branch is needed from now on. The interval I_B has length at most 6/sqrt(N). A mesh with gaps at most 1/(8rQ) needs at most

    2+48rQ/sqrt(N) <=2+48r

points. By (3.4), each comparison bank is within 1/Q of a mesh bank in max norm. By (3.3), on the tube event each actual ratio bank is within another 1/Q. Downward quantization changes each scaled coordinate by less than one, also for negative values and real Q. Thus all complete good quantized banks lie in a fixed, p-independent union of mesh boxes, containing at most R0=(2+48r)9^D integer vectors. Nine integers per coordinate is conservative. There is no extra boundary alphabet factor: B already fixes S and all exact boundary-query fields.

Conditionally on B, the joint posterior probability of p in I_B AND the tube event is at least .99-.01=.98. For any fixed decoder random seed, its output C1 masses for the at most R0 good bank labels form at most R0 real estimates. Radius ε=1/(8R0 P0 Q) neighborhoods of these estimates have posterior mass at most 2R0 ε P0 Q=1/4, by (4.2). Thus conditional expected absolute error is at least

    (.98-.25)ε >=1/(16R0 P0 Q).

Average decoder randomness, then B using (4.1), to obtain Bayes risk at least 1/(32R0 P0 Q). Finally average encoder seeds: the prior was the same for every seed, so the source supremum dominates this Bayes average even for randomized encoders. Infima over all admissible encoder/decoder pairs preserve the bound. This proves UI1.

## Scope and evidence limits

The reveal is only a lower-bound oracle, not an admissible uncharged model feature. It uses O_{D,r}(Q²) bits; their posterior width is exactly why a constant rather than O(Q) good alphabet suffices. All constants are explicit and independent of arbitrarily growing κ. If r>=n the small-history branch applies automatically with the displayed C; no exceptional conditional proof is needed. At-most-D encoders can be padded by fixed zero ratios.

Direct source bindings: BA001 v1 exact model and §§6,8; SH001 v1 §1 and its distinction between fixed-square-root-band sharpness and an all-Q result. Both acceptance records were read. No original-network execution, literature priority, formal verification, deep-family extension or full (κ,Q) matching surface is asserted. Diagnostics only corroborate finite inequalities and numerical examples; they do not replace this proof.
