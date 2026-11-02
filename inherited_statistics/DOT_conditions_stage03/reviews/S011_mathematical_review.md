# S011 原独立数学审查的科学正文

编排说明（非原文）：原独立审查日期为 2026-10-28，结论 ACCEPTED，无数学修复要求。以下保留原审查的完整逐引理推理、科学适用范围与有限检查事实；身份及运行元数据省略。审查绑定原证明哈希，而非这份新复制件。独立上下文 LLM 审查不是形式验证，也不是外部同行评审。下文有限检查是原审查历史结果，本次编排未重跑；原命令、脚本和运行记录不在本包内。

编排时序注（非原文）：原审查接受的是 S011 当时的精确结论；其旧 M=K⁴、β=K⁻⁶ 例子后来由 S012 闭合，但 S011 的证书数值与原审查均未被改写。

## Accepted Mathematical Scope

Fix all integers `K>=2,M>=1` and public `beta in [0,1]`. Sources are homogeneous legal order-two pair shifts, with arbitrary initial pair law mu and some hidden stationary pi satisfying `P^2(s,t)>=beta pi(t)` for every pair of states. Algorithms may use the complete `M+2`-symbol history, public parameters and an independent seed, but no hidden source, stationary law or future observation. The target remains the actual terminal row, and the loss is expected TV, normalized by one half.

Write `n=M+1`, `delta=1-beta`, `i=min(1,sqrt(K/n))`, `a=min(1,sqrt(K^3/n))`, `g=min(1,sqrt(K^5/n))`, and `F=max(i,min(delta,a))`. Use the proof's explicit endpoint-safe `h_b`, and `u_s(L)=min(1,48sqrt(K^3/(L+1)))`, `u_g(L)=min(1,48sqrt(K^5/(L+1)))`. The accepted finite certificates are exactly

    U_+ = min{u_g(M),
              min_(0<=b<=M-1) min{1,
                48sqrt(K^3/(M-b+1))+13sqrt(K)h_b^(3/4)}},
    U_suf = min_(0<=b<=M-1)
              min{u_g(M-b),u_s(M-b)+h_b u_g(M-b)},
    U_pool = min{1,(1/2)sqrt(K/M)+2delta},
    U = min{U_+,U_suf,U_pool}.

Then

    F/180 <= R_D2 <= U,
    R_D2 <= R_D2^+ <= U_+.

Only `U_+` is assigned to unchanged original rowwise add-one. `U_suf` belongs to a genuinely different deterministic public-bound-minimizing suffix rule; `U_pool` belongs to empirical pooling. A deterministic public comparison selects the branch attaining certificate U, not the smaller unknown true risk.

If `delta<=a`, then `U<=min(1,3F)`. If `h_floor(M/2)<=1/(M+1)`, then `U_+<=min(1,81a)` and `U<=min(1,81F)`. The common minimax sandwich with constants `1/180,81` holds for every `beta>=1/2`, with all small M covered. At beta zero the full general g rate and exact certificate identity `U=u_g(M)` are retained; at beta one the arbitrary-start common minimax rate is i, without transferring that optimality to the original rowwise rule.

The exact copy-family coefficient, fixed-K mixing-envelope negation, and all-burn finite certificate gap are accepted with precisely their stated, non-statistical-obstruction scope.


## Per-Lemma Audit

### unit_001 — Lemma 1: All-state contraction (`lem:s011-contract`)

- **Statement/fidelity:** arbitrary mu, the same existential stationary witness, every deterministic b, and both beta endpoints are retained.
- **Validity:** finite-kernel TV contraction follows from the displayed triangle inequality. For beta<1 the residual matrix is nonnegative and stochastic, and stationarity gives `pi Q=pi`; the two-step defect is exactly `(1-beta)(nu Q-pi Q)`. Iteration plus the final zero or one step gives `delta^floor(b/2)TV(mu,pi)<=h_b`.
- **Boundaries:** beta zero uses Q=P² without asserting contraction stronger than one. Beta one forces `P²=Pi` by equal row sums, so b>=2 resets exactly and b<2 uses only the probability cap. There is no `0^0`, reversibility or absolute-continuity assumption.
- **Contribution:** the required uniform initialization bound for the two distinct upper transfers.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Proposition 2: Algorithm-separated envelope (`prop:s011-envelope`)

- **Original:** S004.2 applies to the unchanged original estimator for each allowed b and the same stationary pi. Inserting Lemma 1 is legitimate because the right side increases with eta. L1MAX independently gives `u_g(M)`. A finite minimum of uniform bounds on the same estimator is valid; no new original algorithm is secretly selected.
- **Suffix reindexing:** `(X_(b+1),...,X_(M+2))` has `M-b+2` symbols, initial pair `Y_b~mu P^b`, L=M-b departures, and final pair Y_M. S003's actual-terminal length-L upper therefore gives exactly `min(u_g(L),u_s(L)+h_b u_g(L))`. Its positive-part proof and accepted scope allow arbitrary initialization, including mass outside stationary support. Its lower is not imported here.
- **Public burn:** there are exactly M choices. Choosing the smallest public-bound minimizer produces one deterministic common estimator, not a data-dependent stopping rule or hidden-risk oracle. At M=1 only b=0 is legal and L=1.
- **All-row center:** the unique legal two-step route gives `theta_ab(c)theta_bc(d)`. Summing all d yields `theta_ab(c)>=beta p(c)` with `p(c)=sum_d pi(c,d)`. The residual-row argument gives distance at most delta for every row; beta=1 uses equality of row sums. There is no division by a possibly zero stationary mass.
- **Arbitrary-mu pooling:** D_j is F_(j+1)-measurable and mean zero given F_j. For j<k it is F_k-measurable, so all cross terms vanish. Conditional second moment is `1-||theta_(Y_j)||_2²<=1`, giving the exact `(1/2)sqrt(K/M)` TV term. Both average and actual terminal rows lie within delta of the fixed hidden center pathwise, adding at most 2delta despite sample/endpoint dependence. The predictor never receives that center. M>=1 makes the empirical denominator valid.
- **Selection and lower quantifiers:** each branch has its own uniform certificate, so a fixed public tie rule gives U. For every fixed common possibly randomized B, its arbitrary-start supremum dominates its stationary-subclass supremum, which S006 bounds by F/180. Infimum is taken only afterwards. Fixing public beta still leaves one history kernel within S006's universal quantifier; no source-independent hard witness for all algorithms/horizons is claimed.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Proposition 3: Matched public regimes (`prop:s011-regimes`)

- **Near-IID bridge:** if i=1 the risk cap proves `U_pool<=i+2delta`; otherwise the ratio of the stochastic pooled term to i is `(1/2)sqrt((M+1)/M)<=sqrt(2)/2`. Under delta<=a, F=max(i,delta), yielding the exact capped 3F bound.
- **Burn admissibility:** `b=floor(M/2)` lies in 0,...,M-1 even at M=1, with `L=ceil(M/2)` and `L+1>=n/2`.
- **Absorption:** under (B), `sqrt(K)h_b^(3/4)<=sqrt(K)n^-3/4<=sqrt(K^3/n)`; the ratio is `1/(K n^1/4)<=1`. The stationary term costs at most `48sqrt(2)` times the same square root. The exact rational comparison `sqrt(2)<17/12` gives `48sqrt(2)+13<81`.
- **Caps and F:** separately treating the square root below/above one preserves `min(1,81a)`. When delta>=a, F=a; when delta<a, the pooled branch gives 3F. Thus no near-IID bound is incorrectly assigned to the original rule. (B) is sufficient, not necessary.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Corollary 4: All strong-beta parameters (`cor:s011-strong`)

- **Integer exponent:** writing M=4r+j gives `floor(floor(M/2)/2)=r` and `M+1<=4r+4`. The base r=8 and induction prove `2^r>=4r+4`; hence M>=32 and beta>=1/2 imply (B). Beta one instead uses the explicit zero branch of h.
- **Small M:** for M<32, n<=32 and K>=2 imply `a>=1/2`. The probability cap is at most 2a; alternatively delta<=1/2<=a puts the entire small-M strong-beta domain in the pooled regime. The proof covers equality and all finite M, not just eventual asymptotics.
- **Contribution:** the same absolute constants 1/180 and 81 apply throughout beta>=1/2.
- **Verdict:** PASS. Repair direction: None.

### unit_005 — Proposition 5: Exact endpoints (`prop:s011-endpoints`)

- **Beta zero class:** finite Cesaro averages have invariance defect of L1 norm at most 2/T, so compactness gives a stationary law for every legal table. The beta-zero minorization is vacuous; hence MM5 and L1MAX apply to exactly the unrestricted initialization class. Their full-history/randomized-algorithm/actual-terminal quantifiers are preserved.
- **Beta zero certificates:** h_b=1 makes every S004 candidate cap at one. The suffix inner minimum is u_g(L), minimized at L=M; pooling caps at one. Thus U=U_+=U_suf=u_g(M), and the stated `2^-16 g` versus `48g` bounds follow.
- **Beta one structure:** the all-row summation forces every row equal to p, and stationarity gives `pi=p tensor p`; the converse is the explicit constant-row two-step kernel. Arbitrary initial pairs remain allowed. Only the M transition outputs are automatically IID p; the initial pair need not be.
- **Beta one rates:** pooling's displayed bound is at most i. The S006 stationary IID subclass lower retains all M+2 informative symbols and gives `i/(32sqrt(6))`, valid within the larger arbitrary-mu class. There is no discarded-data lower-bound reversal.
- **Algorithm separation:** S006's accepted S005 countersequence supplies the original-rule risk 391/1600 and vanishing pooled risk. The sequence is over even K with M>=1 (equivalently K>=10 for its formula), as explicitly specified in S006. S011 uses it asymptotically, not at inadmissible zero-departure values. This is a same-source comparison, not an all-algorithm lower from a single source.
- **Verdict:** PASS. Repair direction: None.

### unit_006 — Proposition 6: Legal slow copy family (`prop:s011-copy`)

- **Legality/stationarity:** T is doubly stochastic, theta_ab(c)=T(b,c) defines exactly the legal shift, and `pi(a,b)=T(a,b)/K` is normalized. Summing incoming mass gives `sum_a pi(a,b)theta_ab(c)=T(b,c)/K`, including both epsilon endpoints.
- **Exact coefficient:** `P²((a,b),(c,d))=T(b,c)T(c,d)>=epsilon pi(c,d)`. For epsilon>0 every target mass is positive, and cancellation gives the ratio `K T(b,c)=epsilon+K(1-epsilon)1{b=c}`. Choosing b different from c attains epsilon. At epsilon=0 a positive diagonal target and a different starting second symbol give ratio zero.
- **Stationary-witness maximization:** for positive epsilon, two-step contraction forces any stationary nu to equal pi. At epsilon zero, every stationary law is diagonal because one step enters the diagonal; each witness has some positive diagonal mass and admits an all-state zero numerator from a different symbol. Thus the maximal coefficient over all stationary witnesses is genuinely epsilon, not just the coefficient for one selected pi.
- **Marginal/TV:** the second-coordinate recurrence is `nu_(t+1)=(1-epsilon)nu_t+epsilon u`, with point-mass initial marginal. Its exact solution and projection contraction give the submitted pair-TV lower for t>=0. Epsilon one is treated directly rather than using `0^0`.
- **Uniform-envelope negation:** set epsilon=beta<=1/2 and t=floor(1/beta). The integral bound `-log(1-beta)<=2beta` gives pair TV at least `(1-1/K)e^-2`; meanwhile `sqrt(beta)t>=beta^-1/2-sqrt(beta)` diverges. This contradicts every fixed positive c and finite nonnegative C, even with constants depending on the fixed K but not beta/source. C=0 is immediate. K is not varying in this limit.
- **Nonclaim:** this is a marginal mixing obstruction only, not a prediction minimax lower, not an impossibility of structure-sensitive estimation, and not evidence that a certificate floor is necessary.
- **Verdict:** PASS. Repair direction: None.

### unit_007 — Proposition 7: Every-burn finite certificate gap (`prop:s011-gap`)

- **Generic cap:** for every burn, `L+1<=K^4+1<K^5`, so u_g(L)=1. This covers the standalone original generic term as well.
- **Contraction floor:** with r=floor(b/2), Bernoulli's inequality gives `h_b>=1-rK^-6>=1-1/(2K²)` for every b<=M-1. The finite induction is valid for r=0 and all integer r. Hence `h_b>=1/2` and `13sqrt(K)h_b^(3/4)>1`, so every original burn candidate caps at one, not merely the half-window candidate.
- **Suffix minimum:** `u_s(L)>=u_s(M)>=a>=1/sqrt(2K)>1/(2K²)`. Combining this with the h floor and u_g(L)=1 makes every suffix sum strictly greater than one; the inner minimum is therefore one for all burns. Pooling also caps at one because 2delta>1.
- **Lower value and constants:** a is uncapped, i=a/K, and for K>=12, a<1/2<delta, so F=a. The two inequalities bounding a by `1/sqrt(2K)` and `1/sqrt(K)` are exact. The sharper S006 structural amplitude is a/10 here; its IID term is smaller because `32sqrt(6)K>=180`. Thus its combined numerical stationary certificate is also a/180 on this sequence.
- **Scope:** the proof establishes numerical certificate values, not `R_D2=1`, not true risk one for any estimator, and not `R_D2` of order K^-1/2. The remaining upper/lower separation is preserved.
- **Verdict:** PASS. Repair direction: None.

## Independent Adversarial Checks

Acceptance rests on the symbolic review above. A reviewer-owned inline Python command performed these additional finite checks; no producer checker was reused and no helper file was written:

1. Exact `Fraction` matrices for K=2,3 and epsilon in `{0,1/5,1/2,1}`: **8** legal copy families checked for stationarity and exact minimal all-state P²/pi ratio. At epsilon zero, point and nonuniform mixed diagonal stationary witnesses were also checked to have maximal coefficient zero.
2. For those families and t=0,...,6: **56** exact marginal-recurrence and pair-TV projection comparisons, including reset t=0 and nonunique-stationary epsilon zero.
3. Three binary tables (copy epsilon 1/5, IID uniform, and a non-IID checkerboard with amplitude 1/3), two nonstationary initial laws, and M=1,2,4: **18** exact full-history enumerations checked normalization, martingale squared-sum orthogonality, second moment <=M, and pooled risk versus the bound. The moment identities used rational arithmetic; the final square-root comparison used floating tolerance 1e-14.
4. Across those same experiments: **42** exact suffix-law pushforwards checked against the length-(M-b) path law initialized at mu P^b, for every permitted burn.
5. **384** public scalar probes over K in `{2,3,12,50}`, M in `{1,2,3,4,15,31,32,33,35,63,64,1000}`, and eight beta choices including 0,1,1/2 and near-IID boundaries checked caps, all finite minima, (N), (B), strong-beta conclusions and endpoint identities. Floating tolerances were at most 1e-13.
6. Direct evaluation of all **49,297** burns at K=12 and K=13, M=K^4,beta=K^-6 confirmed each of the three certificates equals one and F=a. This finite sanity check does not replace the proof for every K>=12.

All checks passed. No numerical test is claimed as formal or infinite-parameter verification.

## Hidden Subclaim, Assumption and Notation Audit

The seven named units account for contraction, the three estimator bounds, public optimization, stationary-subclass lower inclusion, finite regime absorption, strong-beta integer threshold, endpoint recovery, exact copy coefficient over stationary witnesses, marginal recurrence, envelope negation and every-burn certificate arithmetic. Supporting finite facts are proved locally or explicitly supplied by the checked interface. No independent missing lemma is hidden in assembly prose.

Primitive conditions are exactly the legal homogeneous finite experiment, public domains, arbitrary mu, existential stationary pi and all-state minorization. Conditions (N)/(B) are public deterministic scalar conditions for corollaries. Stationary closeness, row-center radius, martingale orthogonality, copy stationarity and coefficient extremality are derived, not silently assumed. No reversibility, full support, recurrence, selected-row IID, hidden-parameter oracle or generated-event hypothesis is added.

The public objects are the declared class/risks, three rules, rate scalars and certificates. Residual kernels, p, filtration increments, copy marginals, induction indices and temporary T are proof-local. The two uses of T (temporary rate in Proposition 3 and first-order kernel in Proposition 6) are confined to different named units. The stationary witness remains hidden. The finite tie rules remove any need for source-dependent measurable optimization.

## Target Claim and Explicit Rate Audit

- All K>=2,M>=1,beta in [0,1] and deterministic burns 0,...,M-1 are covered, with separate epsilon in [0,1] and integer t>=0 for the copy result. M=1 never permits an empty or zero-length suffix.
- Every statistical statement is deterministic-finite-horizon **expected actual-endpoint TV**, preserving exactly M departures and the full available M+2 symbols. A predictor may ignore initial information; a lower bound may not, and the imported lower does not. No predictive-KL, squared-TV, independent-query, randomized-time, high-probability or stopping-time substitution occurs.
- Constants 48,13 and the lower constants have exact accepted sources. Constants 3,81 and threshold 32 have complete finite derivations. No hidden constant depends on K,M,beta,mu,theta,pi or the algorithm. In the mixing negation K,c,C are fixed while beta decreases; in the gap K varies with the stated exact M,beta.
- Beta zero retains the unrestricted g baseline and U=u_g(M); beta one retains the IID common rate i with arbitrary initial pair. No stationary upper is simply relabeled arbitrary-start. Pooling is essential to the proved common near-IID guarantee, though the result does not claim it is the unique possible optimal algorithm.
- No mathematical claim is obtained from the unaccepted diagnostic or S010. No generic K²-state example is substituted for a legal pair shift. General q, unknown-beta adaptivity, neural implementation, codecs and faults remain outside scope.

## Target-Step Assembly Audit and Review Rationale

1. Lemma 1 plus accepted S004.2 and L1MAX proves the unchanged original certificate.
2. Lemma 1 plus exact suffix reindexing and the accepted S003 upper proves the separate suffix certificate.
3. The legal two-step product/summation identity plus the locally reproduced S006 martingale bridge proves pooled risk for arbitrary mu.
4. Public finite selection and S006 stationary-subclass inclusion give the common sandwich.
5. Proposition 3 and Corollary 4 prove the explicit matched regimes with all caps and finite cases; Proposition 5 preserves both exact endpoints and the algorithm distinction.
6. Proposition 6 supplies a fully lawful fixed-K route obstruction; Proposition 7 supplies the uniform-over-burn numerical certificate gap without upgrading it to true-risk information.

This noncircular chain proves the exact bounded S011 contract. **ACCEPTED with no retry** is the smallest justified outcome. The unresolved weak-beta joint minimax window is outside the assigned conclusion and is explicitly left open, not treated as a flaw or silently closed.

