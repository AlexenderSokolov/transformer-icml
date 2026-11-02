# S009 原独立审查的科学部分

原审查日期：2026-10-28。原审查结论：ACCEPTED；无数学修复要求。证据为独立上下文 LLM 数学审查，不是形式验证。本件逐字摘录原审查的范围、逐引理推理与有限检查；省略身份、调度和运行元数据。审查针对原证明哈希，不能把此份编排误称为对复制件的新审查。各单元的历史限定只限定该单元，综合结论见中文摘要。

## Accepted Scope

The source is one fixed legal homogeneous second-order table on K symbols during each trajectory. The class consists of arbitrary initial pair laws and tables for which some stationary probability row pi and finite integer q>=1 satisfy `P^q(s,t)=pi(t)` for every starting and destination pair, including states outside stationary support. The estimator sees all `M+2` observed symbols, public K,M and the class definition, with an optional independent seed. It receives neither theta, mu, pi nor q. The loss is unconditional expected TV at the actual same-trajectory endpoint after M observed departures.

Within precisely this experiment, the displayed risk chain is valid with universal numerical constants. Also accepted are uniqueness of pi, equivalence of the existential-exponent class with `P^(K^2)=Pi`, and exact removal of every initial law by that deterministic dimension bound. The latter is a proved conclusion, not an extra source assumption or extra estimator input.

The two-step IID comparison is interpretation at the accepted S007/S005 scope. It does not become an IID-size upper for the larger finite-reset class. The nonnecessity example concerns the stationary-initialization guarantee, not a claim that every arbitrary-start unconstrained source has this minimax order.



## Per-Lemma Audit

### unit_001 — Lemma 1: Reset projection and nilpotent remainder, lines 95–125

- **Statement fidelity:** applies to any finite row-stochastic P with a stationary probability row pi; the legal shift case is a specialization. Existence of finite q is invoked only for the final nilpotence and uniqueness conclusions.
- **Projection algebra:** `Pi^2=Pi` uses normalization of pi; `P Pi=Pi` uses row stochasticity; `Pi P=Pi` uses stationarity. Subtraction yields both annihilation identities `A Pi=Pi A=0` for `A=P-Pi`.
- **Power identity:** the base case n=1 and induction multiplication are correct. For every n>=1, `A^n Pi=A^(n-1)(A Pi)=0`, including n=1. Thus `P^n=Pi+A^n`, and a witnessing exact reset indeed gives `A^q=0`. No unproved binomial commutativity or n=0 formula is used.
- **Uniqueness:** every stationary probability nu satisfies `nu=nu P^q=nu Pi=pi`. This is uniqueness of stationary probability law, exactly as stated.
- **Boundary/adversarial check:** there is no division by pi, no positive-minimum-mass assumption, and no restriction to its support. The algebra remains valid for zero pi coordinates and transient states. Abstract A=0/q=1 also causes no gap, even though legal K>=2 pair kernels cannot have one-step reset.
- **Contribution:** supplies the actual nilpotence premise and correct stationary projection for Lemma 2.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Lemma 2: Full kernel-chain bound, lines 127–147

- **Statement fidelity:** the dimension claim requires only a linear map on R^d and some finite q with `A^q=0`; q need not be known, minimal, or uniformly bounded in advance.
- **Monotonicity:** `V_j=ker A^j` starts at V_0={0} and is increasing, since A sends zero to zero.
- **Kernel-stall implication:** if `V_j=V_(j+1)` and x belongs to `V_(j+2)`, then Ax belongs to `V_(j+1)=V_j`; hence x belongs to `V_(j+1)`. The reverse inclusion is already proved. This argument works at j=0 as well as later j and iterates to every later kernel.
- **Use of finite q:** `V_q=R^d`. Therefore any proper V_j has j<q and cannot stall, since stabilization would contradict fullness at q. This is the required bridge from an unknown eventual exponent to strict dimension growth; it is actually proved, not inferred from monotonicity alone.
- **Dimension count:** assuming V_d proper makes each of the d inclusions starting from V_0 strict, so `dim V_d>=d`, a contradiction. No d-versus-d+1 off-by-one occurs. The argument proves `A^d=0` without needing a Jordan form or an external nilpotence theorem.
- **Source application:** Lemma 1 gives `P^d=Pi`; then `mu Pi=pi` and stationarity yield `mu P^b=pi` for every b>=d and every mu. A zero-mass stationary state can carry initial mass and is still covered. The converse uses q=d as a finite witness and keeps the stationary-pi clause.
- **Quantifier audit:** the uniform public bound is derived separately for each source on the same K^2-dimensional space. No estimator is given a witnessing q, and no supremum/limit or existential/universal exchange is hidden.
- **Contribution:** proves all-state class equivalence and the vanishing discrepancy needed by the upper.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Proposition 3: Original-rule arbitrary-start upper, lines 149–182

- **Dependency applicability:** in the long-horizon regime `M>=2d`, b=d is deterministic and satisfies `0<=b<=M-1`; `L=M-d>=d>=1`. Lemma 2 proves eta_d=0 for every mu. All hypotheses of the accepted ORIGINAL S004.2 interface are therefore met.
- **Algorithm fidelity:** the count still includes i=0,...,M-1. Burn b is analytical only; neither discarded observations nor hidden inputs are introduced. Exact stationarity at time d does not falsely make the entire history stationary.
- **Horizon/constant calculation:** `M-d+1>=(M+1)/2` follows immediately from M>=2d. Hence the coefficient is at most `48 sqrt(2)<68`, verified exactly by `4608<4624`. Monotonicity of the cap preserves the bound.
- **Short horizons:** integer M<2d implies `M+1<=2K^2`, so `K^3/(M+1)>=K/2>=1`. Thus a=1 and the asserted upper is exactly the TV cap one. This handles M=1, M=2d-1 and the equality case K=2,M=7 without an inadmissible burn.
- **Uniformity and final cap:** supremum over the entire class preserves the same numerical bound. The elementary `min(1,68t)<=68min(1,t)` is valid in both regimes. All constants are independent of theta, mu, pi and the unknown q.
- **Contribution:** all-parameter arbitrary-start bound for precisely the original estimator in the target theorem.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Proposition 4: Inherited all-estimator lower, lines 184–200

- **Class inclusion:** every E3 source supplies the explicit finite witness q=3 for Efin, with the same stationary pi and arbitrary-mu allowance. This is an inclusion of the actual legal-source experiments, not merely an algebraic matrix family.
- **Common-algorithm restriction:** an Efin estimator remains a source-independent map of the complete history and independent seed when evaluated on E3. Knowing the larger fixed class does not reveal an individual theta, mu, pi or q. It is consequently covered by S007's all-estimator lower on E3.
- **Minimax ordering:** for each fixed T, the larger supremum dominates the E3 supremum, which is at least a/100000. Only then is the infimum taken. No inference is made from a single-source add-one lower to minimax hardness.
- **All K and information:** S007 already proves the lower for K>=6 with its legal stationary checkerboard and for K=2,...,5 using stationary IID witnesses retaining all M+2 observations. The imported theorem is not silently reduced to the checkerboard's large-K range. Stationary lower witnesses are admissible members of the arbitrary-initialization class.
- **Contribution:** the full lower half of S009.1, with unchanged observed data, actual endpoint, loss and estimator authority.
- **Verdict:** PASS. Repair direction: None.

## Hidden Subclaim Scan

All new theorem-critical bridges appear in the four named local units. The power induction and kernel-stabilization induction expose their exact recurring assertions explicitly; no stochastic recurrence, generated event or extra invariant is assumed.



The extra interpretation claims were checked at their actual scope:

1. **One-step impossibility:** some destination pair has positive pi mass; a starting pair with a different second coordinate has a structural zero there. K>=2 ensures such a start exists. Sparse pi does not avoid this contradiction.
2. **Two-step IID identity:** the unique legal two-step product, summed over the final symbol, forces `theta_ab(c)=p(c)` for every a,b,c. Substitution gives pi=p tensor p. The converse is direct and permits zero p coordinates. The optimal IID rate/pooling comparison is the explicitly inherited S007/S005 interface, not a new unproved theorem used for S009.1.
3. **Stationary nonnecessity:** `00->01->11->10->00` is legal, uniform-stationary and a permutation cycle. Distinct states remain distinct under every positive power, so no exact reset exists, while S004 at b=0,eta_0=0 supplies the stationary bound. This does not extend a statement about stationary starts to all arbitrary starts.
4. **Sample scale:** delta<1/100000 excludes the saturated lower branch. Rearrangement gives the stated necessary `M+1>=10^(-10)K^3/delta^2`; the sufficient `68^2K^3/delta^2` follows from the original upper for delta<1. No high-probability interpretation or sharp threshold is claimed.

No fresh structural classification, approximate-nilpotence perturbation claim, minimum reset exponent or all-small-K strict inclusion is smuggled into these comparisons.

## Target Claim and Explicit Rate Audit

- The theorem proves exactly the existential finite all-state reset class with arbitrary initialization, not a class with a known q, bounded q assumed in advance, support-only reset, or stationary starts only.
- K>=2 and M>=1 are deterministic integers. The exposed rate is unconditional actual-endpoint E[TV] with exactly M departures and all M+2 observed symbols. There is no stopping-time, simultaneous-horizon, conditional-risk, independent-query, predictive-KL or squared-TV upgrade.
- The numerical constants 48/13 are inherited from S004, 1/100000 from S007, and 68 follows from the displayed exact inequality. The 13 term is removed only after eta_d=0 is proved. No dependence on q, a stationary minimum, source or confidence level is hidden.
- The public rate specialization is fully justified by Proposition 3: derived auxiliary burn, admissibility, zero discrepancy, horizon comparison and short-horizon cap are all explicit.
- Stationary initialization preserves the sharper accepted b=0, constant-48 upper. The constant-68 arbitrary-start class theorem is a stated conservative extension, not a claim that the baseline must be weakened.
- The IID subclass keeps its different, smaller minimax rate. Hardness of Efin is worst-case hardness of a larger class, not a lower bound for every constituent source or subclass.
- Exact finite equality is essential. Approximate convergence would not imply `A^q=0`, so no rate for a nonzero defect or variable mixing parameter follows from this proof.

## Notation Surface Audit

Public-facing objects are Efin, the two class risks, a(K,M), and the original estimator. Pair dimension d=K^2 and projection Pi are explicit setting-derived objects. A, V_j, q and the kernel/power indices are local algebra notation; b,L,eta are the accepted analytical S004 quantities with explicit specialization. All notation is scoped and no helper dictionary conceals an assumption or rate. The symbol A used for the matrix remainder is not confused with the separately named estimator T or alphabet mathcal A.

## Limited Independent Diagnostics

The symbolic proof above, not computation, establishes the all-parameter result. A reviewer-owned inline Python calculation using exact `fractions.Fraction` arithmetic additionally checked:

- Nilpotent Jordan chains for dimensions 1 through 10, including the nonminimal supplied witness q=d+3: kernel dimensions were exactly `min(j,d)` through j=d+3, and A^d was zero.
- A nonnilpotent diagonal map diag(0,1): kernel dimensions stalled at one and remained there, checking the logical distinction between monotonic growth and growth forced by eventual nilpotence.
- Two legal sparse IID pair kernels, K=2 with p=(1,0) and K=3 with p=(1/3,2/3,0): exact projection/annihilation identities, power decomposition, two-step reset and d-step reset all held, including rows outside stationary support.
- 390 exact horizon/constant boundary checks over K=2,...,50 at selected small, burn-boundary and large horizons; all short-regime ratios were at least one, all long-regime burns were admissible, and the squared constant comparison held.

All checks passed. They are finite sanity checks, not an exhaustive classification or formal proof. No diagnostic script or producer artifact was modified.

## Target-Step Assembly Audit and Review Rationale

1. Lemma 1 supplies the correct stationary projection identities and nilpotent remainder from an actual finite reset witness.
2. Lemma 2 supplies the fully proved dimension bound and arbitrary-mu reset, with no knowledge of the witness needed.
3. Proposition 3 specializes the accepted ORIGINAL S004 theorem and handles every horizon, yielding the uniform constant-68 upper.
4. Proposition 4 transfers the accepted all-K S007 lower through a valid source-class inclusion for every common complete-history estimator.
5. Original add-one is itself one admissible common estimator, so `R_fin<=R_fin^+`; combining the two propositions gives every inequality of S009.1.

There is no missing bridge, assumption strengthening, information leak, dependency mismatch or unsupported scope upgrade. **ACCEPTED with no retry** is therefore the smallest justified outcome. Neither producer revision nor a new statistical proof is needed for this standard corollary.

