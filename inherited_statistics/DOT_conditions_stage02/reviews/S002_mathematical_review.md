# S002 原独立审查的科学部分

原审查日期：2026-10-28。原审查结论：ACCEPTED；无数学修复要求。证据为独立上下文 LLM 数学审查，不是形式验证。本件逐字摘录原审查的范围、逐引理推理与有限检查；省略身份、调度和运行元数据。审查针对原证明哈希，不能把此份编排误称为对复制件的新审查。各单元的历史限定只限定该单元，综合结论见中文摘要。

编排说明（非原文）：以下保留原审查实际执行的有限检查及结果；原检查脚本不随本包交付，已省略内部运行命令。本次编排未重新运行这些历史数学枚举。

## Accepted Mathematical Interface

For every integer `K >= 2`, `M >= 1`, and every full-history estimator with an independent seed, the stationary legal order-two pair-shift minimax expected actual-endpoint TV risk obeys

\[
R_{\rm stat}(K,M)\ge\frac1{180}\min\{1,\sqrt{K^3/(M+1)}\}.
\]

The same lower bound is witnessed by a subclass with the common, known stationary pair law `pi(a,b)=1/K^2`, symbol transition probabilities in `[0.9/K,1.1/K]`, and `P^2(s,t) >= 0.81 pi(t)`. Its uniform even-time contraction is also proved. This is a lower bound only; no matching upper bound, add-one optimality, or literature-priority conclusion is accepted by this review.



## Per-Lemma Audit

### Unit 1 — Legal stationary hypercube (lines 34–68; S002.2–S002.3)

- **Statement/assumptions:** `r=floor(K/2)`, `d=K r^2`, independent signs, and `0<alpha<=1/2` are explicit. These are construction choices, not hidden assumptions on the full stationary source class.
- **Validity:** for fixed `(a,b)`, each output-symbol pair cancels its perturbations; for fixed `(b,c)`, each first-symbol pair does likewise. Unpaired rows/columns have exactly `1/K` entries. Thus each fixed-middle-symbol matrix is doubly stochastic, and uniform pair mass is preserved by the legal shift kernel.
- **Boundary/adversarial check:** zero non-shift transitions are retained; positivity is only asserted for legal symbol transitions. Odd `K`, including `K=3`, requires no unmentioned completion of a block. `Y_0` is exactly uniform, independent of the horizon-dependent amplitude; no deterministic phase alignment appears.
- **Contribution:** gives a legal finite prior family and the sign-independent endpoint probability `1/K^2`, the essential cancellation for conditional testing.
- **Verdict:** PASS. Repair direction: None.

### Unit 2 — Entire endpoint-conditional history and reversed smoothing (lines 70–101; S002.4–S002.7)

- **Validity:** stationarity gives `Q((b,c),(a,b))=theta_ab(c)`. For a legal pair path, the initial pair mass in the joint path probability and terminal mass in the conditioning denominator are the same `1/K^2`, so the conditional path density is precisely the product of all `M` reversed transitions.
- **Information audit:** the map from `X_1,...,X_(M+2)` to `Y_0,...,Y_M` is bijective on legal paths: recover the first two symbols from `Y_0`, then each new final coordinate. Thus the reverse experiment contains the initial pair and all intervening observations, not a count statistic or truncated history.
- **Two-step audit:** the unique reverse route from `(u,v)` to `(a,b)` is through `(b,u)`, with product `theta_bu(v) theta_ab(u)`. Its upper bound is `(1+alpha)^2/K^2`, giving the displayed bound at every `t>=2` by averaging over the earlier state.
- **Boundary:** every endpoint has positive mass, so no exceptional conditional law or zero-probability endpoint is suppressed. No reversal or smoothing bound is misapplied at times 0 or 1.
- **Verdict:** PASS. Repair direction: None.

### Unit 3 — Exact single-bit KL and startup visits (lines 103–142; S002.8–S002.11)

- **Changed-kernel audit:** flipping `(b,i,j)` changes exactly the reversed departure rows `(b,2j)` and `(b,2j+1)`. Each row swaps only the probabilities at first symbols `2i,2i+1`; no other row carries information about that bit in a single reverse transition.
- **Exact row KL:** writing `p+=(1+alpha)/K`, `p-=(1-alpha)/K`, the sum is `(p+-p-) log(p+/p-)=2 alpha/K log((1+alpha)/(1-alpha))`. The upper bound `8 alpha^2/K` follows for `alpha<=1/2` from the stated integral bound.
- **Startup audit:** reverse departure times are exactly `0,...,M-1`. Both first departures are conservatively bounded by 1; the remaining departure probabilities are at most `2(1+alpha)^2/K^2`. This yields `min(M,2)+(M-2)_+ 2(1+alpha)^2/K^2 <= 2+9M/(2K^2)` with no lost endpoint term.
- **KL audit:** the two conditional path laws have the same deterministic reverse initial state and the same strictly positive legal-path support. Expanding the log likelihood ratio and taking the expectation therefore gives the displayed finite chain rule with no initial-distribution KL term. Multiplication yields exactly `16 alpha^2/K + 36 alpha^2 M/K^3`.
- **Uniformity:** the argument is uniform in endpoint, bit position, every other sign, and horizon. In particular the target endpoint may itself lie in a changed row.
- **Verdict:** PASS. Repair direction: None.

### Unit 4 — Amplitude and complete-history testing distance (lines 144–165; S002.12–S002.14)

- **Rate algebra:** `alpha=beta/10`, `beta=min(1,sqrt(K^3/(M+1)))` imply `alpha<=0.1`, `alpha^2<=0.01`, and `alpha^2 M/K^3<=0.01` in both regimes. With `K>=2`, the startup term is at most `0.08`; the later term is at most `0.36`.
- **Conversion:** `D<=0.44` gives path-law `TV<=sqrt(0.22)<1/2`. This is information control used for binary testing, not a replacement of the target expected TV by KL or expected squared TV. The requisite finite Pinsker proof is separately checked below.
- **Scope:** the amplitude may depend on the publicly fixed `K,M`, but no selected source changes during a trajectory. All entries consequently lie in the declared `[0.9/K,1.1/K]` interval.
- **Verdict:** PASS. Repair direction: None.

### Unit 5 — Target-row loss controls decoded errors (lines 167–199; S002.15–S002.18)

- **Validity:** for a paired endpoint `(a,b)`, the true epsilon-signed coordinate difference in output block `j` is `(2 alpha/K) sigma_bij`. The estimator's decoded sign has a fixed, source-independent tie rule.
- **Tie/adversarial check:** if the true sign is negative, a zero estimated difference is an error and still has distance `2 alpha/K` from the true signed difference. If the true sign is positive, an error requires a negative estimated difference, giving at least that distance as well.
- **Loss arithmetic:** the triangle inequality bounds the pairwise L1 error below by the difference error. Disjoint output pairs can be summed, and the factor `1/2` in TV yields `alpha/K` times the number of decoding errors. No cancellation across coordinate pairs can invalidate this lower bound.
- **Scope:** this is pointwise for every history and seed with the actual endpoint fixed, with nonnegative losses at unpaired endpoints simply omitted. No empirical count is used or assumed positive.
- **Verdict:** PASS. Repair direction: None.

### Unit 6 — Conditional randomized testing (lines 201–216; S002.19)

- **Conditional-prior audit:** every sign vector gives exactly the same terminal law, hence conditioning the uniform sign prior on the endpoint leaves it uniform. This is explicitly proved by the common marginal, not assumed from visit independence.
- **Testing audit:** pair signs differing only in `(b,i,j)` for that particular endpoint's row. The estimator uses the same randomization kernel under both hypotheses. Integrating its independent seed gives a measurable decision probability in `[0,1]`; the sum of errors is at least `1-TV`, hence at least `1/2`.
- **Averaging constant:** `2^(d-1)` disjoint two-hypothesis pairs, each with sum of errors at least `1/2`, give prior-average error at least `1/4`. No probability-of-endpoint factor is forgotten here; it enters the next unit.
- **Information scope:** the distance is the conditional law of the full history for the same endpoint indexing the target. This closes the random-terminal-row/full-side-information issue without introducing an independent test query.
- **Verdict:** PASS. Repair direction: None.

### Unit 7 — Endpoint averaging, constant, and minimax quantifiers (lines 218–239; S002.20–S002.21)

- **Averaging:** there are `2rK` retained endpoints, each with mass `1/K^2`, and `r` target bits at each. The lower bound is therefore `(1/K^2)(2rK)(alpha/K)(r/4)=alpha r^2/(2K^2)`.
- **Constant:** `r/K=1/2` for even `K`, while `(K-1)/(2K)>=1/3` for odd `K>=3`. Thus the risk is at least `alpha/18=beta/180`, including the worst rounding case `K=3` and `K=2`.
- **Quantifiers:** for each fixed `K,M` the finite family is independent of the estimator. Every deterministic or randomized estimator satisfies the Bayes-average lower bound, so its supremum risk is at least that average; taking the infimum preserves the bound. Disclosing the common pair law and subclass properties does not defeat any step, because the test/kernel can depend on those common facts.
- **Verdict:** PASS. Repair direction: None.

### Unit 8 — Boundary claims and uniform two-step Doeblin corollary (lines 241–267; S002.22–S002.23)

- **Boundary audit:** the eleven listed boundary claims are substantiated by the earlier units. No irreducibility, positivity, or mixing assumption is inserted into the larger class; using a strictly positive legal-transition subclass for a lower bound is sufficient.
- **Minorization:** the unique forward two-step route from `(a,b)` to `(c,d)` passes through `(b,c)`. Its probability is `theta_ab(c) theta_bc(d) >= (1-alpha)^2/K^2 >= 0.81 pi(c,d)`.
- **Contraction:** `R=(P^2-0.81 Pi)/0.19` has nonnegative entries, row sums 1, and `pi R=pi`. Hence `mu P^2-pi=0.19(mu R-pi R)`, and TV contraction under a Markov kernel iterated `t` times gives `0.19^t TV(mu,pi)`. The asserted positive, irreducible subclass is valid since every two-step pair transition is positive; one-step structural zeros remain.
- **Interpretation:** a class whose only additional restriction is this uniform constant mixing guarantee still contains the hard hypercube at each horizon, so that guarantee alone cannot remove the `K^3` lower dependence. No upper bound or claim that mixing is necessary follows or is asserted.
- **Verdict:** PASS. Repair direction: None.

### Unit 9 — Self-contained finite Pinsker argument (lines 269–285)

- **Applicability:** the conditional legal-history laws form a common finite positive support. The event `B={p>=q}` satisfies `p(B)-q(B)=TV(p,q)`; when TV is nonzero, `0<q(B)<1`.
- **Derivation:** Jensen for `z log z` gives the two-cell log-sum reduction. Binary relative entropy has value and first derivative zero at `u=v`, and second derivative `1/[u(1-u)]>=4`. Two integrations, with continuous endpoint extension, yield `D>=2 TV^2` in exactly the direction needed for the testing-distance upper bound.
- **Verdict:** PASS. Repair direction: None.

## Hidden Subclaim Scan

All nontrivial mathematical claims in prose were included above: bijectivity of the history/pair-path representation; common conditional prior; startup support and visits; arbitrary random seed handling; minimax average-to-sup conversion; odd-symbol loss discard; irreducibility of the subclass; invariance of the residual Doeblin kernel; and TV contraction. No unproved generated invariant or new dependency was found.

## Target Claim and Explicit Rate Audit

The exposed variables are precisely integer `K>=2` and `M>=1`; `1/180` is universal. The target mode remains the expectation of TV at the actual terminal pair using the complete observed history. Each horizon is fixed but arbitrary; there is no stopping-time, all-time, or high-probability upgrade. KL and path-law TV are intermediate testing objects, not substituted final risks. The alpha/beta choice, startup absorption, and rounding constant are all displayed with valid inequalities. The result is material partial progress on the larger contract: it closes the candidate minimax lower side and leaves the stationary upper/add-one question untouched.

## Notation Surface and Dependencies

All notation is locally defined and compatible with the binding contract. The public exported objects are the minimax risk statement and explicitly described hard subclass/contraction. The sign coordinates, reverse laws, changed rows, decoded signs, alpha and beta are proof-local. No opaque hidden constant or unexplained regularity assumption appears. Finite KL chain rule, binary testing, and Pinsker are justified directly in current notation; finite-sum rearrangements need no limiting interchange. No MM5/nonstationary initialization result or external theorem is imported.

## Independent Adversarial Computation

Ran an independently written enumerator, without reading the producer's checker:





It enumerates every sign vector, single-bit flip, endpoint, and full symbol history for `K=2,3`, `M=1,2,3,4`, at `alpha=0.1` (the theorem's amplitude for these cases). There are 992 directed conditional experiments. It checks normalization of every endpoint-conditional history law, forward/reverse full-history identity, exact path KL versus row KL times reverse departure visits, the startup-inclusive visit bound, the displayed KL bound, and Pinsker.

- Largest normalization/identity/chain-rule residual: `2.220446049250313e-16`.
- Largest conditional KL in this finite grid: `0.0522747161678904`.
- Largest conditional TV in this finite grid: `0.13836250000000008`.
- All assertions passed.

These are floating-point sanity checks for indexing and boundary errors only. Acceptance rests on the symbolic proof audit, not on finite enumeration or numerically verified constants.

## Target-Step Assembly Audit and Review Rationale

Legal stationarity gives the common positive endpoint marginal and exact reversed full-history experiment. The single-bit information estimate, including both startup departures, bounds conditional testing distance uniformly. Pointwise actual-row TV controls bit errors, and conditional testing gives a constant average error per bit. Correct endpoint and sign averaging then yields the stated `1/180` lower bound for every allowed estimator; the independent two-step kernel calculation gives the stated mixing corollary. These units close the exact S002 contract with no missing bridge or altered risk. The smallest retry target is therefore None.

