# BA001 — Stationary precision lower for one bounded local attention-summary block

2026-11-02. **Author candidate; independent review pending.** This is a family-level extension of accepted IP002, not a claim about arbitrary deep Transformers, novelty, or external validation. No accepted file is altered.

## Result and exact model

Fix integers D,r>=1 and constants 0<a<=b<infinity. There are K>=3 source symbols and a history X_1,...,X_n, n=M+2. For each i=3,...,n define L_i to be the last r symbols ending at i, with a fixed public padding symbol before position 1. A shorter window, or any function of this window, is allowed. Let S contain the first min(r,n) and last min(r,n) symbols. Its overlapping entries, if any, are duplicated consistently. The encoder may compute any source-independent exact query q(S) from S and public metadata.

For each d=1,...,D and i=3,...,n, public tables specify

    w_di(L_i,q), v_di(L_i,q),  a<=w_di<=b, |v_di|<=1.

Tables may be different at every position, may depend on K,M,Q and known beta, and may contain arbitrary real constants. They must be independent of the unknown source law. The one global summary block returns exactly

    B_d = sum_i w_di(L_i,q(S)) v_di(L_i,q(S)) / sum_i w_di(L_i,q(S)),
    Z_d = floor(Q B_d)/Q.

Every head uses all M displayed positions; in particular its denominator is at least aM. Query-dependent hard masks, variable selected domains, precomputed nonlocal features, source-dependent tables, an unbounded number of local-copy ports, and history rereads are **not** included. A fixed deterministic mask can be incorporated only if the resulting effective weights still satisfy the stated positive lower bound. Finite arithmetic implementations are included if their actual outputs have the displayed ratio form with uniformly bounded actual weights; idealization of a different finite operation is not implicit.

The decoder sees Z=(Z_1,...,Z_D), S, and public metadata only. It can perform unlimited computation, use source-independent randomness, and output any real simplex vector. Giving the whole S is a conservative grant; any deterministic exact side fields or local-copy outputs derived from these boundary windows are included. No infinite-range extra query bit may depend on the interior history. Source-independent encoder randomness also may be allowed if the model bounds hold for every seed: grant that seed to the decoder and apply the proof conditionally.

The unknown source is a homogeneous second-order source with stationary pair law Pi and all-state certificate P^2(s,t)>=beta Pi(t). Initialization is at its own hidden stationary Pi. Loss is TV between the output and the true next-symbol law at the actual terminal pair. Let R denote minimax expected loss, with the supremum over this stationary source class, for any encoder in the preceding family. The bound is uniform over encoders, so also holds if the encoder is chosen optimally within the family.

Put beta0=max(beta,1/M). For M>=64, beta in [0,1/16], and **every real Q>=1** (hence every legal dyadic Q>=16),

    R >= c(D,r,a,b)/Q * ln(1+(1/8) min{Q/(M beta0), M/Q}).        (BA1)

One explicit positive constant is as follows:

    H=3^(2r), T=br sqrt(40 D H), L=4br/a,
    C=4T/a, N=ceil(2C+4)+1,
    A=H (2+L) N^D, c=1/(8192 A).

The upper bound |v|<=1 is substantive normalization. If instead |v|<=V for fixed V, the same proof gives constants depending also on V, by replacing numerator bounds accordingly. Uniformity independent of an unspecified unbounded value range is not claimed. Alternatively one can require |v|<=b and absorb V into b. D and r are fixed independently of M,Q; when they grow, the formula with its deteriorating constant still holds but its fixed-family precision interpretation does not follow automatically.

## 1. One stationary three-symbol family and one prior

For completeness we reproduce the IP002 witness, rather than treating its original fixed-bank theorem as an architecture-general theorem. Choose distinct W,C0,C1. Put alpha=1/(2M), eta=beta0-alpha, and p in I=[1/4,3/4], p_0=1-p,p_1=p. Define

    T(W,W)=1-alpha, T(W,Ci)=alpha p_i,
    T(Ci,W)=eta,    T(Ci,Cj)=(1-eta)p_j,
    pi(W)=eta/beta0, pi(Ci)=alpha p_i/beta0.

Every unused-symbol row equals pi; unlisted probabilities are zero. Direct substitution gives pi T=pi and T(x,y)>=beta0 pi(y) for all symbols, including unused starting symbols. Embed by theta_(u,v)(x)=T(v,x), and set Pi(u,v)=pi(u)T(u,v). Then Pi is stationary for the pair chain and

    P^2((u,v),(x,y))=T(v,x)T(x,y)>=beta0 Pi(x,y)>=beta Pi(x,y).

The process starts at this actual Pi. Its dependence on p is permitted and is not supplied to the decoder. Importantly Pi(W,W)=(1-alpha/beta0)(1-alpha)>=1/4 is p-independent.

For now suppose 1<=Q<=M/4. Set

    U=min{1/(4 beta0), M^2/(4Q^2)}, J=floor(U).

Then J>=4, J>=U/2, J<=M/4, beta0 J<=1/4 and Q sqrt(J)/M<=1/2. For 2<=j<=J let E_j be the word event W^(n-j) followed by j active letters. Its probability is

    e_j=Pi(W,W) alpha (1-alpha)^(M-j)(1-eta)^(j-1)>=1/(32M).

It is independent of p. Conditional on E_j, the j active bits are IID Bernoulli(p), before conditioning on any query or boundary data. The events are disjoint. Throughout we use **one prior**, p uniform on I; it remains uniform conditional on every E_j. Grant a decoder the additional oracle j on E_j and a bottom label outside their union. This only strengthens it.

At every selected terminal word, the true next-law remains

    eta delta_W+(1-eta)[(1-p)delta_C0+p delta_C1].                  (1)

The past no-exit event does not remove the future exit mass eta.

## 2. Freeze the query, not the endpoint-conditioned source

Fix j. On these words, S ranges over a set of cardinality at most H=3^(2r), regardless of K. (Some of the entries are fixed W and some patterns are impossible; counting them does no harm.) For each possible S-value s, freeze q=q(s) in all head tables, but continue sampling the entire j-coin suffix unconditionally under E_j. Denote the resulting numerator and denominator sums by A_ds and D_ds. Define deterministic comparison coordinates

    h_ds(p)= E_p[A_ds | E_j] / E_p[D_ds | E_j].                    (2)

These are ratios of expectations, **not** expectations of ratios. Both the random and mean denominators are >=aM, and |h_ds|<=1. At the actual side value S=s, the actual head equals A_ds/D_ds. We will prove statements simultaneously for all s, so never assert IID after conditioning on a query.

Changing one active coin changes at most r local windows, even with position-dependent tables. A numerator term is in [-b,b], a denominator term in [a,b]. Consequently both sums have bounded-difference constants at most 2br per active coin. The Efron–Stein inequality gives

    Var(A_ds | E_j), Var(D_ds | E_j) <= 2 b^2 r^2 j.               (3)

For clarity, Efron–Stein here follows by replacing one coin with an independent copy and summing half the expected squared changes; each change is bounded by 2br. It applies to independent, not identically distributed table outputs because the underlying coins are independent.

Chebyshev, (3), and a union bound over 2DH sums imply that, for every p, with conditional probability at least 9/10, all their deviations from their respective means are at most T sqrt(j), where T=br sqrt(40DH). Call this parameter-dependent event G_pj. Indeed the failure bound is at most 4DH b^2r^2/T^2=1/10.

Subtracting the ratios exactly, using |h_ds|<=1, yields on G_pj

    |A_ds/D_ds-h_ds| <= (|A_ds-E A_ds|+|D_ds-E D_ds|)/(aM)
                         <= (2T/a) sqrt(j)/M.                   (4)

The larger constant C=4T/a in the theorem is therefore conservative. Equation (4) pays numerator and denominator fluctuations separately and introduces no expectation-of-ratio shortcut.

## 3. A Lipschitz curve even with arbitrary positional encodings

For a function f of the j bits, differentiating its product-Bernoulli expectation gives

    d/dp E_p f = sum_(ell=1)^j E_p[f(B with B_ell=1)-f(B with B_ell=0)].

This identity is a finite polynomial identity; all other bits in each summand are IID Bernoulli(p). Apply it to each fixed-query sum. The same per-coin 2br bound gives

    |(E A_ds)'|, |(E D_ds)'| <= 2brj.

Differentiating (2), and using |h_ds|<=1 and E D_ds>=aM, proves

    |h_ds'(p)| <= 4brj/(aM)=L j/M.                               (5)

Thus the D-dimensional comparison curve is L j/M-Lipschitz in maximum norm. It need not be monotone, and no coordinatewise crossing-count claim is used. Source-independent tables may change arbitrarily with M,Q: (3) and (5) are uniform in their contents. The polynomial differentiation bound uses only locality/influence, so it does not require a bounded number of table types or an empirical-count sufficient statistic.

## 4. Tube covering and the complete decoder alphabet

For each s choose a mesh of I of spacing at most M/(LQj), including its endpoints. Since L>0, it uses at most

    2+LQj/(2M) <= (2+L)(1+Qj/M)

points. By (5), every h_s(p) is within 1/Q in maximum norm of one mesh point. Since Q sqrt(j)/M<=1/2, (4) implies on G_pj that each actual unquantized coordinate is within (C+1)/Q of its mesh coordinate, conservatively. Downward quantization adds less than 1/Q. Hence each integer quantized coordinate QZ_d lies in an interval of radius C+2 about the scaled mesh value. An interval of length 2C+4 contains at most floor(2C+4)+1 integers, which is at most N=ceil(2C+4)+1. Negative values cause no exception because downward rounding always differs from its input by a number in [0,1).

Thus a fixed mesh box contains at most N^D integer banks. Union over s, retaining s itself in the message, proves that on G_pj the **entire** decoder input (Z,S,j,public metadata) belongs to one fixed p-independent set of at most

    R_j=A(1+Qj/M), A=H(2+L)N^D                                  (6)

labels. R_j may be rounded up without effect, or treated as a real upper bound on the actual integer cardinality. Impossible boundary patterns are omitted. The good event depends on p; the containing set does not. Exact outputs of boundary-query computations may be enormous real constants, but at fixed public inputs they have at most H possible values, already counted by s.

## 5. Finite-message Bayes lower and harmonic averaging

We record the elementary lemma to avoid confusing a high-probability tube with a deterministic channel. Let p be uniform on an interval of length ell. Suppose for each p a good event has probability >=9/10 and all complete good messages are in a fixed set of at most R labels. Any randomized scalar decoder then satisfies E|Z-p|>=ell/(16R). Fix its independent seed: at most R good-message output values have radius ell/(8R) neighborhoods covering length at most ell/4. Under the joint prior experiment, the probability of both being good and outside these neighborhoods is at least 9/10-1/4. Multiplying by ell/(8R) is larger than ell/(16R). Average over the seed. No uniform posterior after G is asserted.

For a simplex output v, set z=v(C1)/(1-eta). The actual target (1) gives TV(v,theta)>= (1-eta)|z-p|. Since eta<=1/16, in particular 1-eta>=1/2, the lemma with ell=1/2 and (6) yields

    E_prior[loss | E_j] >= 1/[64 A(1+Qj/M)].

The common prior, disjoint E_j and e_j>=1/(32M) now give

    E_prior loss >= 1/(2048 AM) sum_(j=2)^J 1/(1+Qj/M).

With u=Q/M<=1/4, elementary comparison with the integral gives

    sum_(j=2)^J 1/(1+uj) >= (1/(4u)) ln(1+uJ),
    uJ >= (1/8) min{Q/(M beta0), M/Q}.

For the first inequality, put j=k+2, use 1+u(k+2)<=(1+2u)(1+uk), 1/(1+2u)>=1/2, integrate the decreasing function over [0,J-1], use J-1>=J/2, and then ln(1+x/2)>=ln(1+x)/2. This proves BA1 with c=1/(8192A) throughout Q<=M/4. The source supremum dominates the single-prior average, uniformly for every decoder and encoder; infima preserve the bound.

## 6. Larger Q: a full-history lower closes the stated all-Q domain

This paragraph is separate from the rare-suffix tube. For Q>M/4 use stationary binary IID sources, which satisfy the all-state D2(beta) requirement for every beta<=1 after defining every pair row as the same binary distribution. Set n=M+2, delta=1/(16sqrt(n)), and p_±=1/2±delta. The n-symbol history laws satisfy

    KL(P_+ || P_-) <= n (2delta)^2/[p_-(1-p_-)] <= 32n delta^2=1/8,
    TV(P_+,P_-) <= sqrt(KL/2)<=1/4.

The Bernoulli KL bound follows from log x<=x-1; p_-(1-p_-)>=1/8. Thresholding an estimate of the next-symbol C1 mass at 1/2 converts it to a test; any wrong test has absolute error at least delta. The average test error is at least (1-TV)/2, so the average TV risk is at least 3delta/8>=1/(128sqrt(M+2)). This lower holds even with full history, hence for every summary considered here.

On the other hand, ln(1+x)<=x and Q>M/4 imply that the RHS of BA1 is at most c M/(8Q^2)<2c/M. Since A>=1, c<=1/8192; for M>=64,

    2c/M <= 1/(4096M) <= 1/(128sqrt(M+2)).

Thus BA1 also holds for Q>M/4. This all-Q completion is weaker than the separately accepted original-SRC IID c/Q theorem; that architecture-specific theorem is **not** imported for this larger family. BA1 alone is not a uniform c/Q floor; §8 separately proves such a floor for the present family.

## 7. Scope, consequences, and open comparisons

* This is an obstruction for one dense global summary block over bounded local windows and bounded exact boundary side information. It permits arbitrary position encodings in those local tables and arbitrary real-valued nonlinear decoding after quantization. It does not permit recursively computed global features or unbounded historical ports.
* The logarithm survives stationary initialization and known M,beta,Q; the source law and stationary law remain hidden. The same prior is retained across all suffix lengths and boundary messages.
* With fixed D,r,a,b, BA1 directly forces Q=Omega(sqrt(M) ln M) if beta=0 and risk is O(M^-1/2): for Q<=sqrt(M), min{Q,M/Q}=Q and ln(1+Q/8)/Q decreases, so the bound at Q=sqrt(M) already exceeds any fixed multiple of M^-1/2 eventually. For sqrt(M)<Q<=M^(3/4), min>=M^(1/4), giving the conclusion; larger Q already suffices in magnitude. Likewise on M=t^4,beta=t^-3 the bound itself first excludes Q<=t^2 for eventual O(t^-2) risk (the function ln(1+Q/(8t))/Q is decreasing there and min=Q/t), then for t^2<Q<=t^(5/2) the log is Omega(ln t), yielding Q=Omega(t^2 ln t). No family-wide c/Q theorem is required for these two implications.
* Matching upper bounds for arbitrary members of this family do not follow. Inclusion of a specific encoder (such as the actual finite SRC prefix) requires checking its exact local windows, dense domains, weights, boundary side contract and value normalization. With D=9K+1 that application has a constant depending on K; removing inactive zero coordinates can recover a stronger support-based constant separately. This manuscript does not replace that interface audit.
* Hard masks and unbounded values are not cosmetic exclusions. A mask can restrict a head to the active suffix and remove its dilution by M. Growing value range can amplify rare-window contributions relative to the quantization grid. Exact nonlocal features can simply contain an unquantized estimator. None is covered by BA1.

## 8. Separate stationary IID c/Q bound for the same encoder family

The preceding proof did not import the original-SRC IID theorem. Here is the required independent extension. For the same family, M>=64 and every Q>=1, and now every beta in [0,1], define

    A_I=H(2+2L)N^D, c_I=1/(256 A_I).

Then

    R >= c_I/Q.                                                   (BA2)

Take all n=M+2 symbols IID Bernoulli(p) on C0,C1, p uniform on [1/4,3/4]. Define every second-order row, including unsupported initial pairs, to be this same binary distribution. The stationary pair law is the product law and P^2(s,t)=Pi(t) for every s,t. Thus the all-state certificate holds for every beta<=1, and the true next-law is the same Bernoulli(p), irrespective of terminal query.

Freeze every possible boundary window s as in §2. There are at most 2^(2r)<=H possibilities. Now all n coins can vary. Replacing one changes at most r summands, so the same Efron–Stein argument gives variance at most 2b^2r^2 n for each numerator and denominator. With T=br sqrt(40DH), a simultaneous good event of probability >=9/10 has deviations at most T sqrt(n). The ratio-of-means comparison curve h_s satisfies

    ||B_s-h_s||_infinity <= 2T sqrt(n)/(aM),
    ||h_s'(p)||_infinity <= 4brn/(aM) <= 2L,

because n<=2M. These statements again precede any conditioning on the actual boundary; all query values are covered simultaneously.

When 1<=Q<=sqrt(M), the scaled tube radius is at most 2sqrt(2)T/a<C. A parameter mesh of spacing at most 1/(2LQ) uses at most 2+LQ <=(2+2L)Q points. Its approximation error is at most 1/Q. Adding downward rounding, each integer coordinate lies in an interval of radius C+2, so each box contains at most N^D banks. Including the exact side value s gives at most A_I Q complete good-message labels. The finite-message lemma, with ell=1/2, gives average next-law TV risk at least 1/(32 A_I Q), which is stronger than BA2.

When Q>sqrt(M), §6's stationary IID two-point full-history lower gives

    R >= 1/(128sqrt(M+2)) >= 1/(256 Q) >= c_I/Q,

where sqrt(M+2)<=sqrt(2M), and 128sqrt(2)<256. This establishes BA2 over all Q without any claim that the O(Q) tube count persists when Q/sqrt(M) grows. The two branches may use different IID priors; each independently lower-bounds the same minimax experiment.

For beta<=1/16 the simultaneous conclusions are the **maximum**, not the sum, of BA1 and BA2. The already proved full-history IID floor is also available. These statements hold uniformly over admissible encoders, including encoders chosen as a function of public M,Q,beta. They do not grant arbitrary historical computations in the values, masked suffix selection, or extra exact statistics.

## Provenance

The witness/source contract and event calculation were checked against accepted `intermediate_precision/IP002_stationary_finite_domain_master_lower_v1.md` and `intake/IP002_acceptance.json`. The finite-message method and original SRC boundary/evaluator contract were also read in `strong_mixing_precision/SM002_iid_complete_master_precision_lower_v1.md`. The present bounded-differences and derivative proof is explicit and does not assume those fixed-prefix results generalize automatically. No external literature priority investigation, original emitted-network execution or formal proof checking has been performed.
