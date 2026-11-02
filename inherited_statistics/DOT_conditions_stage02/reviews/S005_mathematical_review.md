# S005 原独立审查的科学部分

原审查日期：2026-10-28。原审查结论：ACCEPTED；无数学修复要求。证据为独立上下文 LLM 数学审查，不是形式验证。本件逐字摘录原审查的范围、逐引理推理与有限检查；省略身份、调度和运行元数据。审查针对原证明哈希，不能把此份编排误称为对复制件的新审查。各单元的历史限定只限定该单元，综合结论见中文摘要。

编排说明（非原文）：以下保留原审查实际执行的有限检查及结果；原检查脚本不随本包交付，已省略内部运行命令。本次编排未重新运行这些历史数学枚举。

## Accepted Scope

For every integer `K>=2,M>=1`, with a legal homogeneous second-order pair-shift source satisfying `P^2(s,t)=pi(t)` for all starting and destination pairs and with arbitrary initial pair law mu, the source table has every row equal to an unknown p and `pi=p tensor p`. With the entire history `H=X_1^{M+2}` available, the admissible pooled rule using `X_3,...,X_{M+2}` satisfies

    [1/(32 sqrt(6))] min{1,sqrt(K/(M+1))}
      <= inf_B sup_{p,mu} E TV(B(H,U),p)
      <= sup_{p,mu} E TV(B_pool,p)
      <= min{1,(3/2)sqrt(K/(M+1))}.

The infimum includes randomized common estimators with independent seeds. The lower bound retains all `N=M+2` observations in its experiment.

For every even `K>=10`, the stated two-level p and `M=floor(K^2/100)` give the original rule's same-source actual-endpoint risk at least `391/1600`, whereas the pooled rule's same-source risk is bounded by its uniform upper `min{1,15/sqrt(K)}`. Thus the original worst-case/minimax-risk ratio diverges along this sequence.

Acceptance does **not** include an all-K,M matching characterization of the original rule, any predictive-KL or optimal squared-TV rate, an approximate-reset parameter theorem, a q>2 exact-reset characterization, or a new literature-priority claim.



## Per-Lemma Audit

### unit_001 — Lemma 1: Exact-reset equivalence and likelihood, lines 91–116

- **Statement fidelity:** the ALL-starting-pairs and ALL-destination-pairs condition is the authorized class, not a stationary-support-only condition.
- **Validity:** the unique legal two-step route gives `P^2((a,b),(c,d))=theta_ab(c)theta_bc(d)`. Summing over d uses only row stochasticity and forces `theta_ab(c)=sum_d pi(c,d)` for every a,b,c. Substitution proves the product pi; the converse and stationarity follow directly.
- **Assumption audit:** independence of the M transition-output symbols is derived by the complete path likelihood factorization, not assumed from stationarity. Arbitrary mu is independent of this suffix under that factorization, even when it depends on p across experiments.
- **Boundaries:** no division by p occurs; zero symbol probabilities, unreachable stationary pairs, and initial pairs outside stationary support are covered. q=2 is essential to the displayed argument; q>2 is explicitly not exported.
- **Target contribution:** the actual endpoint's transition row equals p on every possible history, so the reduction to distribution estimation does not substitute an independent or fixed query.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Lemma 2: Pooled arbitrary-start upper, lines 118–153

- **Validity:** each count has mean `Mp(c)` and variance `Mp(c)(1-p(c))`. Summing the coordinate absolute-deviation bounds and applying Cauchy–Schwarz yields exactly `(1/2)sqrt((K-1)/M)` for empirical mean TV.
- **Smoothing:** the mixture coefficients M/(M+K) and K/(M+K) are exact. The claimed maximal uniform-distribution bias `TV(u,p)<=1-1/K` follows from the supplied overlap calculation, including sparse p.
- **Rate simplification:** `M(M+1)<=(M+K)^2` proves the empirical term bound; `(K-1)/(M+K)<=K/(M+1)` bounds smoothing. With `x=K/(M+1)<=1`, `x<=sqrt(x)` gives the 3/2 coefficient; for x>=1 the cap by one proves the stated minimum.
- **Admissibility/boundaries:** M>=1 makes the empirical vector well defined. The rule reads only public K,M and observed transition outputs. No initial-law or stationary-law parameter is accessed. K=2, M=1 and zeros are included.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Lemma 3: Affinity and randomized testing, lines 155–185

- **Validity:** Cauchy–Schwarz applied to the difference and sum of square roots gives `TV<=sqrt(1-aff^2)` with the correct TV factor 1/2. The expectation difference for any f in [0,1] is bounded by the positive part of Q-R, proving the randomized testing inequality.
- **Product step:** the affinity product identity is an exact finite expansion, so zero-probability outcomes cause no problem.
- **Loss distinction:** these distances are between data laws, used only to control testing errors. There is no conversion of predictive TV to KL, squared TV, or another prediction objective.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Lemma 4: Full-N common-estimator lower, lines 187–251

- **Class membership/full data:** each hypercube vector is a probability vector with amplitude epsilon<=1/4. The allowed stationary initialization `mu_sigma=p_sigma tensor p_sigma` yields exactly `Q_sigma=p_sigma^(tensor N)`, where N=M+2. Both initial symbols remain informative observations; none are discarded, conditioned away, or revealed as the parameter.
- **Decoding:** a wrong decoded pair sign forces pairwise L1 error at least epsilon/d. The disjoint pair sum and TV normalization give `epsilon/(2d)` per wrong bit. The tie convention causes no gap: a negative true sign decoded as positive at a tie still incurs that full difference.
- **Information calculation:** adjacent-sign affinity is `(d-1)/d+sqrt(1-epsilon^2)/d`. Hence `1-rho<=epsilon^2/d`; product affinity and the geometric inequality give `TV(Q_sigma,Q_sigma^j)<=sqrt(2N epsilon^2/d)<=1/sqrt(8)<1/2`.
- **Randomized algorithms:** integrating the independent seed conditional on each finite history produces an admissible randomized bit-test f. The two adjacent risks sum to at least 1/2; averaging both bit values gives at least 1/4 error for each coordinate. No deterministic-estimator-only restriction is imposed.
- **Quantifier/order check:** for every common B, its prior-average risk is at least epsilon/8, and its source supremum is no smaller. Only then is infimum over B taken. The finite family may depend on public K,M and is fixed within each trajectory.
- **Boundaries:** d=floor(K/2)>=1; K=2 is valid, odd K uses one zero coordinate, and the capped epsilon covers both d/N regimes.
- **Verdict:** PASS. Repair direction: None.

### unit_005 — Theorem S005-A assembly and constant, lines 253–261

- **Validity:** `floor(K/2)>=K/3` for every K>=2, and `M+2<=2(M+1)` for every M>=1. Therefore `d/N>=K/[6(M+1)]`.
- **Cap conversion:** `min{1,sqrt(z/6)}>=(1/sqrt(6))min{1,sqrt(z)}` holds in both z regimes. Combining with epsilon/8 gives the exact lower constant `1/(32 sqrt(6))`.
- **Assembly:** pooled admissibility puts its worst-case risk above the infimum; Lemma 2 provides the uniform upper. No incompatible initializations are mixed: a stationary subclass is valid for a lower on the arbitrary-mu class, while the upper holds for every mu.
- **Verdict:** PASS. Repair direction: None.

### unit_006 — Lemma 5: Endpoint collisions and overlap, lines 263–283

- **Validity/index audit:** for i=0,...,M-2 the prior pair and terminal pair use four distinct IID coordinates, with match probability `(sum p^2)^2`. Their number is M-1. For the remaining i=M-1 the equality event is exactly `X_M=X_{M+1}=X_{M+2}`, with probability `sum p^3`.
- **Dependence:** linearity of expectation, not independence of the collision indicators, proves the formula. Overlap between different prior pairs is irrelevant.
- **Boundary M=1:** there are no nonoverlap pairs, and the sole event is equality of X1,X2,X3. The formula retains this event rather than incorrectly using a four-symbol probability.
- **Verdict:** PASS. Repair direction: None.

### unit_007 — Theorem S005-B: Original-rule countersequence, lines 285–325

- **Source audit:** the even-K two-level p is strictly positive, sums to one, has TV(p,u)=1/4, second moment 5/(4K), and third moment 7/(4K^2). The all-row IID table and product initial law satisfy the same source class.
- **Arithmetic:** the exact collision expectation is `(25M+3)/(16K^2)`, at most `9M/(4K^2)` for M>=1. Markov/union control gives `P(J=0)>=1-EJ` without a conditional-independence assertion.
- **Original rule:** on J=0 the frozen original row-specific count vector is zero, so its actual terminal prediction is exactly u. Nonnegativity off the event justifies the loss lower bound; no suffix or pooled guarantee is assigned to the original rule.
- **Countersequence constants:** even K>=10 ensures `floor(K^2/100)>=1`; M/K^2<=1/100 gives `(1/4)(1-9/400)=391/1600`. The strict inequality `M+1>K^2/100` yields the pooled upper `min{1,15/sqrt(K)}`.
- **Uniform-optimality negation:** the worst-case original risk dominates this single-source risk, while the minimax upper tends to zero. The positive lower in S005-A makes the displayed risk ratio well defined; its lower coefficient is `391/24000`. An infinite even-K subsequence suffices. A single-source lower is not misidentified as an all-estimator minimax lower.
- **Verdict:** PASS. Repair direction: None.

### unit_008 — Interpretation and exported boundary checks, lines 327–380

- The all-row q=2,beta=1 minorization equivalence follows from stochastic row sums; no beta<1 or q>2 IID implication is exported.
- Public information, arbitrary initialization, odd K, small M and zeros match the proved domains. The O(M+K) count-operation/O(K) storage observation is a straightforward implementation statement, not a neural or computational optimality claim.
- For `0<delta<c=1/(32 sqrt(6))`, `c min{1,sqrt(K/(M+1))}<=delta` forces the nonsaturated branch and gives `M+1>=K/(6144 delta^2)`. The pooled upper gives the sufficient `(9/4)K/delta^2` threshold. These are worst-case mean-TV, not high-probability claims.
- The distinctions `E[TV^2]<=E[TV]` and `(E[TV])^2<=E[TV^2]` are correct. The proof does not square a mean-TV upper bound or transfer it to unbounded KL.
- No all-parameter original-rule risk, approximate-reset optimal dependence, or external novelty claim is silently supplied.
- **Verdict:** PASS. Repair direction: None.

## Hidden Subclaim Scan

Every theorem-critical bridge is included in the eight units above. The elementary facts inside them—uniform bias overlap, capped rate conversion, randomized-seed integration, finite affinity product, stationary-subclass restriction, full-N information retention, and endpoint overlap counting—are explicitly derived. No unproved random-row IID assertion, stationarity of an arbitrary-start full history, hidden-support restriction, source-dependent estimator, or conditional-query replacement is used.





## Target Claim and Explicit Rate Audit

- Risk is exactly unconditional **expected TV at the actual same-trajectory endpoint**, with M observed transitions and N=M+2 observed symbols.
- K,M are arbitrary deterministic integers in the displayed domains. Constants are numerical and independent of p,mu,K,M or the estimator; there are no concealed tolerances, confidence parameters or mixing parameters.
- Theorem A is an all-K,M two-sided common-algorithm minimax rate; Theorem B is an explicit original-rule countersequence, not a stronger all-K,M original-rule characterization.
- Pooled add-one, original full-history rowwise add-one, and rowwise suffix/burn-in are distinguished throughout. The pooled upper is not a reassignment of a suffix or original-rule bound.
- Exact-reset specialization is justified by Lemma 1 rather than inherited from an unreviewed S004 interface. The full-N lower and arbitrary-initialization upper have compatible quantifiers.
- The countersequence varies K and M together with a fixed source within every trajectory. No fixed-K inconsistency claim follows or is made.

## Notation Surface Audit

Public objects are E_K, the pooled rule, original rule, their risks, and the displayed constants/rates. N, d, epsilon, sigma, rho, f and J are explicitly defined proof-local helpers. No helper supplies hidden information to an estimator. The target p is unknown and is not confused with a provided stationary law; simplex notation and all probability modes are clear.

## Adversarial and Reproducible Checks

Acceptance rests on the symbolic audit, not finite computation. After reading its source, the producer diagnostic was rerun; it passed exact collision enumeration for K=2,4 and M=1,...,4, finite-grid constant checks, and the separation fraction.

A separate reviewer-owned inline Python calculation independently enumerated all IID histories for six explicitly chosen p vectors: `(1,0)`, `(1/3,2/3)`, `(3/4,1/4)`, `(1/2,1/2,0)`, `(1/2,1/3,1/6)`, and `(3/8,3/8,1/8,1/8)`, each with M=1,...,4. In all **24 cases**, exact rational arithmetic verified the collision formula, the true original-risk lower `TV(u,p)P(J=0)>=TV(u,p)(1-EJ)`, and the directly computed pooled risk against its bound. Sparse support and the M=1 overlap were included.

The reviewer separately enumerated full N-symbol laws for adjacent hypercube points with K=2,...,5 and N=3,4,5. All **12 cases** verified product affinity numerically to tolerance 1e-12, the affinity-to-TV inequality, and adjacent-law TV below 1/2. Exact fraction arithmetic independently returned `391/1600` and ratio coefficient `391/24000`. These limited checks are arithmetic/indexing diagnostics only, not infinite-parameter or formal verification.

## Target-Step Assembly Audit and Review Rationale

1. Lemma 1 establishes the class identification, arbitrary-initialization likelihood factorization, and exact actual-endpoint target equality.
2. Lemma 2 gives the admissible pooled upper uniformly over the entire class.
3. Lemmas 3–4 preserve the entire N-symbol experiment and all randomized common estimators, giving the lower; the explicit capped conversion produces Theorem S005-A.
4. Lemma 5 counts the original endpoint's past context matches including the sole one-symbol overlap. The stated source, zero-count event, and horizon comparison yield Theorem S005-B on the same objective.

These independent local chains prove the exact assigned scope without a missing bridge or dependency. **ACCEPTED with no retry** is the smallest justified outcome. The lack of a matching original-rule all-K,M rate is an explicitly excluded successor question, not a defect in this proof.

