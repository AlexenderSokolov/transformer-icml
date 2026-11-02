# IR001 — An IID precision floor from summed replacement influences

2026-11-02. Research candidate; fresh independent review pending. No earlier or frozen artifact is modified. No novelty or formal-verification claim.

## 1. Exact experiment and theorem

Let M>=1 and N=M+2. Observe N independent Bernoulli(p) bits, p in I=[1/4,3/4]. A public source-independent random seed R is allowed, including all encoder randomness; conditions below hold for every seed (or outside one source-independent null set). The unknown p is not public metadata. The decoder receives the seed, a boundary label S comprising at most b bits at fixed public positions, and exactly D>=1 terminal coordinates, each downward quantized at real resolution Q>=1. Repeated/overlapping boundary positions count only once. Public positions can depend on R but not the data or p. Any other exact query fields must be functions of S and public metadata, not additional information about the history.

For each seed and each formal boundary branch s in {0,1}^b, an ideal coordinate function f_(s,d):{0,1}^N -> R has deterministic replacement bounds

    |f_(s,d)(x)-f_(s,d)(x with bit i flipped)| <= c_i^(s,d),
    c_i^(s,d)>=0,   sum_i c_i^(s,d)<=B,                         (1)

where B>=1 is a common public bound, not a data-dependent random variable. These inequalities hold on ALL formal histories with s frozen, not merely histories consistent with s. No smoothness of f is assumed. The actually computed precut bank a satisfies, on every history,

    max_d |a_d(x)-f_(S(x),d)(x)| <= E/Q,                       (2)

with fixed E>=0. Its message is floor(Q a_d)/Q coordinatewise. The decoder is unrestricted and may use additional independent randomness but has no history reread or other source-dependent port. B may grow with depth or any public budget. Output boundedness can be imposed but is not needed for this theorem; it is needed for a separate global alphabet count.

There is c=c(D,b,E)>0, uniform over N,Q,B and all functions satisfying this contract, such that

    inf_encoder,decoder sup_(p in I) E_p |p_hat-p| >= c/(QB).    (IR)

For prediction of an IID binary next-symbol distribution, total variation loss is exactly this loss (or dominates it if the decoder can put mass on other symbols). This IID witness belongs to every stationary second-order minorization class P²>=beta Pi, 0<=beta<=1, by defining every row to be the same Bernoulli(p) law and starting at its product pair law. Thus (IR) transfers as a lower bound to any larger such source class. It also transfers to arbitrary-initialization minimax classes containing these stationary initializations; it is not an upper guarantee for them.

One explicit set of deliberately loose constants is

    F=D 2^b, C=100F, L=F+b,
    P0=128 sqrt(L(C+1)), K=ceil(2E+6)+1, R0=8 K^D,
    c=min{1/[128 sqrt(C+1)], 1/[32 R0 P0]}.

## 2. Small history and a deterministic influence reveal

Put m=ceil(C Q² B²). If N<m, grant the full history. Let p_±=1/2±1/(16sqrt(N)); these points lie in I. Their gap is delta=1/(8sqrt(N)); the one-bit chi-square divergence is <=1/(12N), since p_-(1-p_-)>=3/16. The N-bit chi-square divergence is <=exp(1/12)-1<=1/11, so total variation is <1/4. The minimum-density triangle inequality gives average absolute estimation loss >=delta(1-TV)/2>=3/(64sqrt(N)), in particular >=1/(128sqrt(N)). Since N<m<= (C+1)Q²B², this proves the first constant. The two-point prior is independent of encoder seeds. There is no M versus N endpoint substitution here.

Otherwise N>=m. Use the ONE prior uniform on I, for every seed. Fix and grant the seed. For every pair (s,d), choose the m indices with largest c_i^(s,d), breaking ties publicly. Let U be the union of these sets and all boundary positions. It is deterministic given the seed, independent of p and the sampled bits. Write n=|U| and Y=X_U. Then

    m<=n<=Fm+b<=Lm<=L(C+1)Q²B².                              (3)

Grant Y to the decoder. This is a lower-bound oracle, not an uncharged feature of an upper construction. Given Y=y and p, every remaining bit is still independent Bernoulli(p), and the actual S is determined. For every unrevealed index and every frozen pair,

    c_i^(s,d)<=B/m,   sum_(i notin U) c_i^(s,d)<=B.            (4)

Indeed its pair's own top m are all revealed. Zero influences and N=m cause no exceptions.

## 3. Conditional tubes and mean derivatives

Fix any revealed pattern y and p. Efron–Stein applied to the remaining independent bits gives for h_(s,d)(p)=E_p[f_(s,d)(X)|Y=y]

    Var_p(f_(s,d)|Y=y) <=(1/2) sum_(i notin U) (c_i^(s,d))²
                       <=B²/(2m).                          (5)

(The sharper Bernoulli coefficient p(1-p) is unnecessary.) Chebyshev and a union bound over F pairs show that all ideal coordinates lie within 1/Q of their conditional means with probability at least 1-F Q²B²/(2m)>=.995. This holds for EVERY y,p; no heavy-pattern event is needed.

The product expectation is a polynomial in p. Differentiating one remaining factor at a time gives the exact identity

    h'_(s,d)(p)=sum_(i notin U) E_p[f_(s,d)(X_i=1)-f_(s,d)(X_i=0)|Y=y],

where the other unrevealed bits are independent Bernoulli(p). Hence |h'_(s,d)|<=B by (1). This identity holds with revealed bits fixed and s frozen; it does not differentiate the posterior or impose the event S=s on free bits.

## 4. Oracle posterior including boundary modes

Under the uniform prior let t be the number of ones in Y and z=t/n. The posterior density on I is proportional to p^t(1-p)^(n-t). Define I_y=I intersect [z-3/sqrt(n), z+3/sqrt(n)]. Hoeffding gives joint probability P(p notin I_Y)<=2exp(-18). By Markov, the event T consisting of patterns y whose posterior mass of I_y is at least .99 has probability >=1-200exp(-18)>.99.

For y in T, I_y is nonempty. Let p0 be z clamped to I, the posterior mode, and ell(p)=t log p+(n-t)log(1-p). On I,

    |ell'(p0)|<=16sqrt(n),   |ell''(p)|<=16n.

The first follows from dist(z,I)<=3/sqrt(n) and p0(1-p0)>=3/16, and the second from p,1-p>=1/4. From p0 at least one direction stays in I for length 1/4. On a segment of length delta0=1/(64sqrt(n)) in that direction, Taylor's theorem gives ell(p)>=ell(p0)-1/4-1/512>ell(p0)-log 2. Integrating the unnormalized density over this segment proves

    sup_I posterior_density <=128sqrt(n)<=P0 QB.             (6)

This covers truncated modes on either boundary, including t=0,n whenever T holds, and requires no normal approximation.

## 5. Constant good alphabet and Bayes risk

Fix y in T, and let s be its now-known actual boundary branch. Cover I_y by a mesh with gaps at most 1/(QB), including endpoints. The number of points is at most 2+6QB/sqrt(n)<=8, by n>=m>=Q²B². Since each h_(s,d) is B-Lipschitz, its bank is within 1/Q of the bank at a mesh point. On the simultaneous tube from Section 3, the ideal bank is within another 1/Q; (2) adds E/Q. Thus each actual integer label k_d=floor(Q a_d) is within E+3 of the corresponding Q h_(s,d) mesh coordinate. An interval of length 2E+6 contains at most K=ceil(2E+6)+1 integers. Therefore all labels arising when p in I_y and the tube holds belong to a fixed, p-independent set of at most R0=8K^D labels. The label set can depend on y and the seed. It need not be an event measurable from the transmitted label. S contributes no additional factor because it is fixed by y.

The joint posterior probability of this good event is at least .99-.005>=.98. Fix decoder randomness. For these at most R0 labels its p-estimates are at most R0 real numbers, even though it also sees y and the seed. Their epsilon-neighborhoods, with epsilon=1/(8R0 P0 QB), have posterior mass at most 2R0 epsilon P0 QB=1/4 by (6). The good event outside these neighborhoods has probability at least .98-.25, and error there is >=epsilon. Hence conditional Bayes risk is at least 1/(16R0 P0 QB). Average decoder randomness and then y; P(T)>.99 yields the conservative bound 1/(32R0 P0 QB).

The original experiment is less informative than the revealed one. Finally average encoder seeds: the uniform prior and all constants were common to every seed. A source supremum dominates that Bayes average, so infimizing over admissible randomized encoders/decoders proves (IR). The small-history and large-history branches are selected by deterministic N,m, not seed-dependent or data-dependent priors.

## 6. Bounded-primitive causal attention application

Use CA001 v3's fixed primitive bounds, dense public masks if desired, and GD001's corrected synthetic-terminal contract. Dense masks are public and independent of the sampled history and boundary branch. As in CA001's scope note, arbitrary boundary dependence in historical tables gives a finite-side-information extension with causal attention within each frozen branch, not necessarily end-to-end temporal causality. The end-to-end causal subclass confines any future-boundary dependence to the synthetic terminal processing/query and decoder; the lower applies to both. Write A_tu=1{u<=t}/t and Hmat=aI+b_att A for the common nonnegative perturbation majorant. Here a,b_att are the fixed constants from the attention weight-and-value perturbation calculation; they are unrelated to the boundary-bit count b. A is row-stochastic, so Hmat^l has row sums (a+b_att)^l. Fixed-radius r historical local tables have diameter <=Delta, and terminal projection has Lipschitz constant G. The initial synthetic terminal state depends ONLY on public data and the frozen finite boundary S, so it is unchanged by replacements on formal histories within a frozen branch. Each source bit i affects only historical initial states u in [i,min(N,i+r-1)]. Consequently the actual deterministic replacement bounds can be chosen as

    c_i=G Delta sum_(u=i)^min(N,i+r-1) (Hmat^l)_(T,u),
    sum_i c_i<=r G Delta sum_(u<T)(Hmat^l)_(T,u)
             <=r G Delta(a+b_att)^l.                        (7)

This sums ACTUAL matrix-entry majorants, not the larger logarithmic pointwise envelopes. It includes early source bits and has no factorial square-sum constant. The matrix majorant need not be an actual attention matrix; its row-sum identity is sufficient. Branch-specific primitives use the same majorant by the all-formal-history uniform contract. Positionwise stages are included by increasing a to their common Lipschitz bound. Neither growing internal circuits hidden in one layer nor arbitrary internally rounded maps are allowed.

For l>=1 set

    B_l=max{1,r G Delta(a+b_att)^l},
    C_depth=max{2,max(1,r G Delta) max(1,a+b_att)}.

Then B_l<=C_depth^l and (IR), for implementations satisfying the fixed E/Q contract, gives

    R_IID >= c(D,b,E)/(Q C_depth^l).                          (8)

This applies to the same ideal bounded-primitive family and its certified finite approximants; no arithmetic audit is manufactured by (7). No new unquantized terminal port is granted. Output boundedness only enters the separate cardinality lower below.

## 7. Depth consequence and relation to folded-grid capacity

Independently, full-history testing yields order N^(-1/2). If D=J coordinates are in [0,1] before their declared final grid (or their actual range is enlarged only by fixed E/Q), fixed boundary size gives a total alphabet O_(J,b,E)(Q^J), hence an order Q^(-J) lower by the elementary interval-covering argument. These floors combine by maximum, not addition or an assumption that one prior witnesses every term.

For fixed J>=2, suppose M is comparable to Q^(2J), Q tends to infinity, primitive constants and E,b,J stay fixed, and a family achieves R_IID<=A/sqrt(M) with fixed A. Then (8) forces C_depth^l >=c sqrt(M)/(A Q)>=c' Q^(J-1), hence

    l >= ((J-1)log Q + log c')/log C_depth = Omega(log Q).

FG001 supplies the complementary candidate construction at Q=2^h: J bounded folded coordinates, primitive depth O(1+(J-1)h), and fully paid finite evaluator attain risk <=1/(2sqrt(M))+2/Q^J, with uniform E=1. Thus, within the common admitted primitive/interface scope and at this IID capacity frontier, depth order Theta(log Q) follows once FG001 and this theorem are separately accepted. This is NOT an all-Q sharp exponential-base risk theorem, a full Markov minimax upper theorem, or a universal depth-independent 1/Q floor. More generally (8) gives the necessary l >=log_+(c sqrt(M)/(AQ))/log C_depth; additive constants and feasibility Q^J comparable to or above sqrt(M) must be handled separately in any matching statement.

## 8. Evidence boundary

Source bindings accompany this file. UI001's posterior-reveal mechanism is adapted, but the local denominator/maximizing-pattern argument is entirely replaced by (4)–(5). CA001's actual matrix-entry row sum, with GD001's corrected terminal initialization and formal-branch domain, supplies the causal application. FG001 is context and a separately reviewed candidate construction, not an assumption used in proving (IR). Diagnostics corroborate finite algebra, posterior bounds, and exact discrete conditional identities; they cannot prove uniform claims. No external publication/upload or priority search was performed, and no prior accepted files were edited.
