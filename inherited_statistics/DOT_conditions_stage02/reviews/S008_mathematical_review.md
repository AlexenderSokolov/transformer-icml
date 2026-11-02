# S008 原独立审查的科学部分

原审查日期：2026-10-28。原审查结论：ACCEPTED；无数学修复要求。证据为独立上下文 LLM 数学审查，不是形式验证。本件逐字摘录原审查的范围、逐引理推理与有限检查；省略身份、调度和运行元数据。审查针对原证明哈希，不能把此份编排误称为对复制件的新审查。各单元的历史限定只限定该单元，综合结论见中文摘要。

## Accepted Scope

For every finite integer K≥2 and M≥1, and for every common source-blind randomized predictor using the complete M+2-symbol history, strict positivity of every legal symbol transition, without a prescribed common positive lower bound, leaves the exact finite-horizon supremum of actual-endpoint expected TV loss unchanged:

1. Over all homogeneous second-order sources and arbitrary initial pair laws.
2. Separately, over all homogeneous second-order sources and all their stationary initial pair laws, including stationary mixtures, reducible sources, periodic sources, and zero-mass states in the full class.

These are per-algorithm equalities before taking an infimum. Hence both minimax values and the original full-history add-one worst risks are unchanged. The source-positive subclasses need not contain maximizers. Qualitative irreducibility, aperiodicity, uniqueness of stationary law, and source-by-source mixing, alone or in combinations containing every strictly positive legal table, inherit the same equality by class inclusion, with the initialization regime kept fixed.

The proof additionally establishes source-dependent two-step contraction for a strictly positive legal table and explicitly demonstrates the lack of a uniform mixing-to-zero bound over that whole qualitative class. The K⁵ arbitrary-initialization and K³ stationary rate statements are accepted only as corollaries of the already accepted baseline interfaces. This review does not newly certify their predecessor proofs, claim literature novelty, or extend equality to TV-close-to-stationary initialization classes.



## Per-Lemma Audit

### unit_001 — Complete-path telescope, §2, lines 70–118

- **Statement fidelity:** finite state space, arbitrary stochastic P,Q, arbitrary initial laws μ,ν, and exactly M observed transitions. The state at time zero remains observed.
- **Exact hybrid orientation:** B_j uses P for departures 0,…,j−1 and Q thereafter. In B_j−B_{j−1}, the changed departure is j−1, with a P prefix and Q suffix. All common factors are nonnegative. After taking the absolute value, summing the Q suffix gives one, then summing the P prefix gives `(μP^(j−1))(s)`. This proves the exact equality (2.2), not merely an informal coupling analogy.
- **Initialization term:** the common Q conditional path law is supported on a different initial-coordinate fiber for each initial state. Thus its full-path TV is exactly TV(μ,ν); the equality would not follow if the initial coordinate were discarded.
- **Triangle inequality:** the sum of the M adjacent-hybrid distances plus the initial-law distance gives (2.1), with every expectation under the ORIGINAL P chain. A reversed hybrid construction would not provide the stationary weights required later; the submitted construction has the correct orientation.
- **Pair/symbol fidelity:** output c maps injectively to pair (b,c) for each row (a,b), giving (2.4). Legal complete pair paths and complete symbol histories are bijective, so TV is preserved rather than merely contracted by a lossy statistic.
- **Boundary checks:** zeros cause no undefined conditionals; M=1 has one adjacent hybrid; no endpoint/count independence is used.
- **Contribution:** full-experiment perturbation bound with original-prefix weighting, suitable for both regularizations.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Risk continuity with the moving actual target, §3, lines 120–151

- **Common algorithm:** the same history-to-output kernel A_h is integrated under both sources. Each resulting loss function is in [0,1], even for an arbitrary randomized output distribution on Δ_K.
- **Target variation:** reverse triangle inequality for TV holds pointwise for the same h and p, hence `|ℓθ(h)−ℓθ′(h)|≤TV(θ_yM,θ′_yM)` after integration. It does not require independence of the endpoint, output, counts, or history.
- **Correct decomposition:** `E_L(ℓθ−ℓθ′)+(E_Lℓθ′−E_L′ℓθ′)` keeps the target-row error under the ORIGINAL terminal law. The bounded second term is controlled by full-history TV, with coefficient one, not two, because ℓθ′ lies in [0,1].
- **Adversarial check:** replacing this calculation by a comparison of data laws alone would be invalid when θ changes. The submitted formula includes precisely the otherwise missing target term.
- **Randomization:** no common fixed seed maximizing risk or deterministic reduction is assumed; integrating the source-independent kernel proves the statement directly and uniformly over A.
- **Contribution:** (3.1) controls the actual risk, not a surrogate with the old target held fixed.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Arbitrary-start positive row approximation, §4, lines 153–178

- **Class membership:** `(1−ε)θ_s+εu` is a stochastic row with each legal symbol probability at least ε/K. Structural non-shift pair entries stay zero. The arbitrary μ is retained exactly.
- **Row bound:** the difference is ε(u−θ_s), so its TV is exactly `ε TV(θ_s,u)≤ε` at EVERY state, including states unvisited under the original source.
- **Full-path and target costs:** the telescope contributes at most Mε and the original-terminal target contributes at most ε, yielding (M+1)ε. All M observed transitions are counted; there is no off-by-one replacement of M by the number of symbols.
- **Scope:** arbitrary unknown, deterministic, or horizon-selected μ is allowed. The perturbed table is homogeneous and fixed within an experiment. No stationary law is selected or needed.
- **Boundary checks:** K=2, M=1, deterministic original rows, and nonstationary starts in zero-stationary-mass states satisfy the same proof. The loose bound can exceed one for large ε; it remains valid and is only used as ε↓0 at fixed M.
- **Contribution:** positive-source approximation of every unrestricted-initialization risk, uniformly over all algorithms.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Balanced stationary triple-flow approximation, §5, lines 180–264

- **Original stationary source:** `T_abc=π_ab θ_ab(c)` has outgoing pair marginal π_ab by row stochasticity and incoming pair marginal π_bc by πPθ=π. These identities hold for arbitrary selected stationary mixtures; no uniqueness is assumed.
- **Regularized marginals:** adding ε/K³ to each triple and multiplying the old flow by 1−ε produces both pair marginals `(1−ε)π+εU_S`. Every denominator π_s^ε is at least ε/K², and every triple numerator is positive. Consequently θ^ε is stochastic, strictly positive on legal edges, and π^ε is exactly stationary, as (5.3) verifies. No arbitrary stationary-selection continuity theorem is invoked.
- **Null-state rows:** when π_s=0, the formula defines θ_s^ε=u and λ_s=1. It never divides by π_s. Although the original θ_s may differ from u by an order-one amount, its contribution π_s d_ε(s) is exactly zero. Thus neither uniform row convergence nor pointwise convergence at null rows is smuggled in.
- **Weighted distance:** for π_s>0, `π_s λ_s≤ε/[K²(1−ε)]`; there are at most K² such states. Together with `d_ε(s)≤λ_s`, this gives `D_ε≤ε/(1−ε)`. This deliberately nonsharp bound is enough. Initial-law TV is exactly `ε TV(π,U_S)≤ε`.
- **Full path:** all original prefix states have law π, hence the telescope sum is exactly M D_ε before the initial-law bound. The perturbed prefixes need not have small original-weighted row errors, and are not substituted into the argument.
- **Endpoint target:** the ORIGINAL terminal state also has law π, so its expected target-row difference is D_ε. The resulting bound is `ε+(M+1)D_ε≤ε+(M+1)ε/(1−ε)`, with no omitted target term.
- **Mixture approximation:** the construction preserves closeness to the specifically chosen π even for multiple closed classes, mixtures of components, and periodic components. It need not preserve the old transition rows at zero-mass states; the exact original-weighted argument is why that is harmless here.
- **Contribution:** uniform-in-A risk approximation of every full stationary experiment by genuinely stationary strictly positive experiments.
- **Verdict:** PASS. Repair direction: None.

### unit_005 — Per-algorithm suprema, minimax, and original add-one, §§1 and 6

- **Quantifier order:** for fixed A,K,M, each full-class source is bounded above by the positive-class supremum plus a tolerance tending to zero. Taking ε↓0 for that source, and only then taking its supremum, gives the nontrivial inequality. Subset inclusion gives the opposite inequality. The stationary argument uses its separate bound from unit_004.
- **No interchange:** equality holds for each A as a pointwise identity of two worst-risk functionals. Taking infima over the identical kernel space therefore needs no minimax theorem, optimizer, compactness of the positive class, or infimum/limit exchange.
- **Class information:** knowing the qualitative class label does not change the set of possible source-blind history-to-simplex kernels; it does not reveal hidden θ, μ, or π. The proof does not compare algorithms with different per-source side information.
- **Finite-horizon source selection:** ε may depend on K,M,A or the desired tolerance in the outer supremum. Each chosen source is nevertheless fixed and homogeneous along the observed trajectory. There is no claim that one fixed ε works uniformly as M→∞.
- **Original rule:** counts use departures i=0,…,M−1, the target row is Y_M, and `(C_s(c)+1)/(n_s+K)` is defined at n_s=0. This exact predictor belongs to the common kernel space, proving its separate worst-risk identities without converting a suffix estimator's bound into an original-rule bound.
- **Full-data and correlation audit:** the proof compares complete history laws and pointwise losses. It neither removes initial side information nor replaces the dependent random last row/visit count by a fixed row or an independent query.
- **Contribution:** exact equations (1.1), (1.2), (6.1), and (6.2), not merely matching rate orders.
- **Verdict:** PASS. Repair direction: None.

### unit_006 — Source-dependent mixing and qualitative-class inclusion, §7, lines 310–375

- **Two-step matrix:** the unique legal path `(a,b)→(b,c)→(c,d)` gives `P²((a,b),(c,d))=θ_ab(c)θ_bc(d)≥mθ²`. Thus every two-step entry is positive even though one-step structural zeros remain.
- **Irreducibility and aperiodicity:** all states communicate in two steps. Positive P²(s,s) and P³(s,s), the latter obtained by averaging positive P²(t,s) against a probability row, give return lengths 2 and 3 and period one.
- **Minorization normalization:** row stochasticity implies mθ≤1/K, so δθ=K²mθ² lies in (0,1]. The bound is exactly `P²≥δθ U_S`. For δθ<1 the residual is a stochastic kernel and cancels the common component, yielding TV contraction by 1−δθ.
- **Stationary existence/uniqueness:** the cited iteration on the complete finite simplex is valid: adjacent iterates of a strict contraction have geometrically decreasing distances, hence form a Cauchy sequence whose limit is a unique fixed point. The δθ=1 case is the constant map to U_S. Commutation with P proves that the P²-fixed point is also P-stationary; every P-stationary law is P²-stationary. This supplies, rather than assumes, the unique stationary law.
- **Convergence:** iteration supplies (7.3) at even times and applying P's TV contraction supplies odd times. The exponent-zero convention covers t=0,1, including δθ=1. Stationarity and the positive two-step matrix also give πθ(t)≥mθ².
- **No uniform gain:** the copying-plus-uniform family is a legal strictly positive table with the displayed stationary pair law. For fixed t its path from (0,0) stays there with probability at least (1−ε)^t, while π^ε tends to uniform mass on the K diagonal pairs. Finite-dimensional continuity of TV gives limit 1−1/K. Therefore a bound tending to zero with t cannot hold uniformly in that class, already at fixed K≥2.
- **Inclusion conclusion:** any class defined by the listed qualitative properties, and containing all legal strictly positive tables, lies between that positive class and the full class. The exact per-A equalities therefore sandwich its supremum as well. The proof correctly keeps arbitrary-start and stationary-start regimes separate and excludes quantitative/structural subclasses not containing all positive sources.
- **Contribution:** positivity genuinely gives strong per-source properties, but these properties alone do not lower the uniform worst risk.
- **Verdict:** PASS. Repair direction: None.

### unit_007 — Accepted rate inheritance and non-extension boundary, §8, lines 377–422

- **Arbitrary-start interface:** the exact constants and K⁵/(M+1) dependence agree with its accepted MM5/L1MAX chain. Substituting exact minimax and original-rule worst-risk equalities preserves both constants and all K,M regimes.
- **Stationary interface:** the stated 1/180, 48, and K³/(M+1) match the accepted S001/S002 chain and recomputed proof/review hashes. The positivity of S002's family is correctly described as sufficient for a rate lower, but not as a proof of exact per-A supremum equality.
- **No unsupported predecessor upgrade:** S008 does not newly prove MM5, reinterpret its witness as already positive, or use its horizon-aligned nonstationary initialization as a stationary witness. The stationary equality is supplied locally by balanced flows.
- **TV-close warning:** keeping μ in the row-mixture construction does not generally preserve a given constraint TV(μ,π)≤η because the stationary law can change. In the stationary-flow construction, μ≠π may charge original π-null rows with order-one row changes, so the π-weighted bounds no longer directly control its path or target. These observations justify the precise statement “not proved here,” not a false impossibility claim.
- **Evidence and scope:** standard finite-experiment density/continuity and stationary-flow regularization are an accurate classification, not a priority claim. No network, computation, training, compression, or fault-mechanism conclusion is added.
- **Contribution:** valid imported rate corollaries and an explicit boundary preventing unjustified interpolation between the two equalities.
- **Verdict:** PASS. Repair direction: None.

## Hidden Subclaim Scan

The potentially hidden bridges are all locally justified: legal-history bijection; the exact hybrid TV equality; bounded randomized-loss TV continuity; changing target control; positive-table membership; balanced stationary pair marginals; zero-mass-row treatment; selected-mixture approximation; common algorithm space; suprema-before-infima; positive two-step transition matrix; existence and uniqueness under contraction; lack of a uniform qualitative mixing bound; and the intermediate-class sandwich.

No argument assumes independent samples conditional on a random row or visit count, positive counts, positive original π, a unique original stationary law, reversibility, a uniform minorization coefficient over the qualitative class, or a time-varying source.



## Target Claim and Explicit Rate Audit

- The public experiment is exactly the frozen complete M+2-symbol history, M observed departures, and the unconditional mean-TV loss against θ at the actual terminal pair.
- K,M are finite fixed integers with K≥2,M≥1. The equality is uniform over algorithms and all full-class sources at those K,M; ε is proof-local, in (0,1), and sent to zero with K,M fixed.
- Perturbation costs are explicit: (M+1)ε for arbitrary initialization, and ε+(M+1)ε/(1−ε) for stationary initialization. No hidden source, algorithm, or mixing dependence is present.
- δθ and mθ are explicitly source-dependent and used only for the separate per-source mixing claim. They are not supplied to the estimator or hidden in a uniform rate constant.
- No fixed-horizon statement is upgraded to a stopping-time, horizon-uniform, high-probability, conditional-risk, predictive-KL, or squared-TV result.
- Rate inheritance preserves the accepted all-K,M caps and constants exactly. Equality of risks is stronger than a conservative rate reduction, so the baseline is recovered without loss.
- The distinction between equality of suprema and existence of a positive maximizing source is expressly preserved.

## Notation Surface Audit

Public objects are the four source classes, common risk functional, four exact worst-risk consequences, and the qualitative boundary. Hybrid laws B_j, row differences d, flow T, mixture weight λ, and weighted distance D are explicitly defined proof-local helpers. U_S and u distinguish uniform pair and symbol laws. P retains the legal pair-shift meaning when specialized from the general finite-state lemma. Unknown π is selected per source and never passed to A. No helper notation conceals an unproved invariant or new algorithmic input.

## Limited Independent Diagnostics

Acceptance rests on the symbolic proof audit, not finite enumeration. A reviewer-owned inline Python check used exact `fractions.Fraction` arithmetic and enumerated full symbol histories for 22 parameter cases:

- K=2 copying dynamics with a 1/3–2/3 mixture of absorbing diagonal classes, and K=2 deterministic alternation with its stationary two-cycle; M=1,…,4.
- K=3 with stationary mass 1/3 each on (0,0), (1,2), and (2,1): one absorbing component plus a periodic component; M=1,…,3. All other rows deterministically output zero.
- In each case ε=1/7 and ε=1/101.

The script verified exact original and perturbed stationarity, stochasticity and strict positivity, replacement of every original π-null row by uniform, D≤ε/(1−ε), initial TV≤ε, complete-path TV≤ε+MD, and each individual hybrid equality with the original-prefix expectation. It also checked the changing-target risk inequality for the same genuinely randomized history-dependent kernel: choose a point mass at the first observed symbol with probability `(1+(sum(h) mod 2))/3`, and otherwise output the uniform probability vector. Finally, direct row mixtures were checked from deterministic nonstationary starts, including a π-null pair, for the Mε path and (M+1)ε risk bounds. **All 22 cases passed.**

These small exact checks stress null rows, stationary mixtures, periodicity, observed initial side information, randomized prediction, and the M=1 boundary. They are not represented as an all-parameter proof or formal certification. No producer checker was edited or relied upon.

## Target-Step Assembly Audit and Review Rationale

1. The complete-path telescope controls all information available to the common algorithm, with original-source prefixes.
2. Risk continuity adds the indispensable original-terminal target perturbation.
3. Direct row mixing approximates every arbitrary-start source in both data law and target loss.
4. Balanced triple-flow mixing approximates every selected stationary experiment, including mixtures and null rows, with a vanishing original-stationary weighted error.
5. Each approximation yields equality of suprema for every algorithm by ε↓0 and inclusion; only then are infima taken or the original rule fixed.
6. The positivity-derived per-source properties and intermediate-class inclusion explain the qualitative-versus-quantitative boundary.
7. Accepted rate interfaces are substituted only after exact equality is established; TV-close initialization and additional structural/quantitative restrictions remain outside the claim.

These chains prove the exact authorized S008 interfaces with no missing mathematical bridge or changed objective. **ACCEPTED with no retry** is the smallest justified outcome. There is no requested producer repair.

