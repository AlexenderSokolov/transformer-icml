# S006 原独立审查的科学部分

原审查日期：2026-10-28。原审查结论：ACCEPTED；无数学修复要求。证据为独立上下文 LLM 数学审查，不是形式验证。本件逐字摘录原审查的范围、逐引理推理与有限检查；省略身份、调度和运行元数据。审查针对原证明哈希，不能把此份编排误称为对复制件的新审查。各单元的历史限定只限定该单元，综合结论见中文摘要。

## Accepted Scope

For every integer `K>=2,M>=1`, let the homogeneous order-two source have its legal pair-shift kernel and be initialized at the stationary pair law pi appearing in its class definition. The entire `M+2`-symbol history is available, and the loss is expected TV to the actual terminal row `theta_{Y_M}`.

1. For the class admitting an unknown center p with `max_s TV(theta_s,p)<=rho`, for public `rho in [0,1]`,

       F(K,M,rho)/180 <= R_near(K,M,rho)
         <= sup_C E TV(B_rho,theta_{Y_M})
         <= min{1,48 F(K,M,rho)}.

2. For the stationary all-pairs class `P^2(s,t)>=beta pi(t)`, for public `beta in [0,1]`,

       F(K,M,1-beta)/180 <= R_D2stat(K,M,beta)
         <= sup_D E TV(B_(1-beta),theta_{Y_M})
         <= min{1,48 F(K,M,1-beta)}.

3. The sharper public-selector upper is `min{U_stat,U_pool(z)}`, as defined in the proof, and `F<=min{a_stat,b_iid+z}<=2F`.

4. The general pooled martingale upper alone holds for arbitrary initial law. The matched stationary statements do not thereby extend to arbitrary initialization. No sharp q>2 statement or all-parameter original-rule risk formula is accepted or asserted.

All infima include randomized common estimators with independent seeds. The class parameters are bound parameters, not exact unknown radii/minorization coefficients disclosed by an oracle.



## Per-Lemma Audit

### unit_001 — Lemma 1: Pooled martingale bound (`lem:s006-pool`)

- **Statement fidelity:** arbitrary initial law is an explicitly stronger local lemma; the all-row radius is the exact hypothesis, not an occupation-weighted alternative.
- **Filtration/indexing:** `F_i=sigma(X_1,...,X_(i+2))` contains `Y_i`; `D_i=e_(X_(i+3))-theta_(Y_i)` is F_(i+1)-measurable with conditional mean zero. For i<j, F_(i+1) is contained in F_j, giving `E<D_i,D_j>=0`. No independence of observed successors is assumed.
- **Second moment and TV:** conditional squared Euclidean norm has expectation `1-||theta_(Y_i)||_2^2<=1`. Thus the summed second moment is at most M. The L1/L2 inequality and expectation Cauchy–Schwarz give the precise `(1/2)sqrt(K/M)` bound, with the TV normalization retained.
- **Actual endpoint:** q_bar and the actual terminal row are both within z of the same fixed source-specific center pathwise. The two triangle contributions total 2z even though the terminal row and sample are dependent. No endpoint conditioning, selected-row IID assumption, or independent test query occurs.
- **Admissibility/boundaries:** p and q_bar are proof-local. The algorithm never receives either. M>=1 prevents division by zero; sparse p, unvisited endpoint rows, nonstationarity and reducibility do not affect the argument. Cap one is valid because the output and target are probability vectors.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Lemma 2: Scaled stationary checkerboard (`lem:s006-cube`)

- **Legality and stationarity:** paired perturbations cancel across output symbols and across first symbols. Consequently each row sums to one and uniform pair mass is exactly invariant for the legal shift kernel. The same uniform law initializes every sign vector.
- **Radius/odd K:** a paired first-symbol row has exactly 2r perturbed coordinates of magnitude alpha/K, so its TV from uniform is r alpha/K<=alpha/2; an unpaired first-symbol row is uniform. This includes K=3, the worst r/K case.
- **Minorization:** the unique two-step route multiplies two entries each at least `(1-alpha)/K`; hence `P^2>=(1-alpha)^2 Pi` for every pair of states.
- **Full conditional history:** uniform initial and terminal factors cancel, yielding the reverse-path product for all M transitions. The symbol history and legal pair path are bijective. Thus the information calculation retains both initial symbols and every intervening observation, not just visit counts.
- **Information scaling:** S002's changed reverse rows, startup departure allowance, finite-chain KL formula and positive common legal-path support remain valid for every `0<alpha<=a/10`. The bound `16alpha^2/K+36alpha^2 M/K^3<=.08+.36=.44` follows in both capped a regimes; Pinsker gives conditional TV below 1/2.
- **Loss/testing/averaging:** a wrong target sign costs alpha/K of TV on its disjoint output pair. Randomized testing gives error at least 1/4 after sign-pair averaging. The sign prior stays uniform given the actual endpoint because its marginal is the same for every source. Exactly 2rK retained endpoints, r output pairs each, and mass 1/K^2 give `alpha r^2/(2K^2)>=alpha/18`.
- **Public parameters/zeros:** fixed public rho/beta may be arguments of the same estimator/test without revealing signs. No empirical count is divided by or assumed positive. The lemma is only invoked at positive alpha; zero-amplitude endpoints are treated separately later.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Lemma 3: Stationary IID floor (`lem:s006-iid`)

- **Class membership:** all rows p with initial pair law p tensor p belong to every near-IID radius class, and satisfy `P^2=Pi`, so belong to every beta class. Every observed symbol is IID p, and the actual terminal target is identically p.
- **Correct dependency direction:** S005's explicit stationary family, not just its larger-class minimax theorem, supplies the lower. The entire data law is `p_sigma^(tensor (M+2))`, including the two informative initial symbols.
- **Testing constant:** epsilon is `(1/4)min{1,sqrt(d/N)}`; neighboring full-data TV is below 1/2. A wrong bit costs epsilon/(2d) of predictive TV, yielding epsilon/8 after averaging d bits. The inequalities `d>=K/3` and `N<=2(M+1)` give exactly `b/(32sqrt(6))` with caps.
- **Boundaries/information:** odd K's zero leftover probability is legal, as are K=2 and M=1. Public class parameters are identical across hypotheses; the independent seed is integrated into the same randomized test. No hidden center is given to the estimator.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Proposition 4: Near-IID transition (`prop:s006-near`)

- **Selector:** comparing U_pool(rho) and U_stat uses only public K,M,rho and has a fixed tie rule. Hence its class supremum risk is at most their minimum. This is not a source-aware oracle selecting the smaller unknown realized risk.
- **Upper simplification:** `U_stat<=48a`. If b=1, cap one gives `U_pool(z)<=b+2z`; otherwise `(1/2)sqrt(K/M)<=b` follows from M>=1. For rho>=a use the stationary bound and F=a; for rho<a use `b+2rho<=3max{b,rho}=3F`. Taking the additional risk cap gives the exact displayed upper.
- **Lower membership:** at rho>0, `alpha=min{a/10,2rho}` is positive, satisfies the information constraint, and makes every row radius at most rho. Both entries are at least `min{a,rho}/10`, so alpha/18 gives the asserted `min{a,rho}/180`.
- **Combination:** the IID floor and structural lower each hold for every estimator with those public parameters. Their maximum, not their sum, is a lower for its supremum risk. Since `1/(32sqrt(6))>1/180`, the resulting coefficient is 1/180 for F.
- **Equivalence/endpoints:** rho=0 uses only the IID floor and makes no zero-amplitude testing invocation. The two-case proof of `F<=min{a,b+rho}<=2F` is valid even when a=b or a=1.
- **Verdict:** PASS. Repair direction: None.

### unit_005 — Lemma 5: Two-step structure (`lem:s006-d2`)

- **All-row summation:** the exact legal-route identity `P^2((a,b),(c,d))=theta_ab(c)theta_bc(d)` holds irrespective of stationary support. Summing minorization over d gives `theta_ab(c)>=beta p(c)` for every a,b,c, with `p(c)=sum_d pi(c,d)` a probability vector.
- **Radius:** for beta<1, `(theta_ab-beta p)/(1-beta)` is nonnegative and sums to one, giving TV at most 1-beta. The proof does not divide by p(c) and is valid when some coordinates or pair masses vanish.
- **Exact beta=1:** equal row sums force theta_ab=p, and stationarity gives `pi=pi P^2=p tensor p`. Conversely that product-initialized all-row IID source satisfies equality. At beta=0 minorization is simply nonnegativity.
- **Scope:** only containment of classes is claimed. The q=2 unique-route formula is essential; no q>2 or arbitrary-initialization matched-risk conclusion is inferred. The derived center remains hidden from the predictor.
- **Verdict:** PASS. Repair direction: None.

### unit_006 — Proposition 6: Beta-uniform interpolation (`prop:s006-beta`)

- **Upper:** Lemma 5 supplies membership in the stationary near-IID class with public radius z=1-beta, so Proposition 4 applies without revealing pi or p.
- **Lower amplitude:** for beta<1, `alpha=min{a/10,1-sqrt(beta)}` is strictly positive and at most a/10. It ensures `(1-alpha)^2>=beta`, so the scaled stationary family lies in the exact class.
- **Uniformity:** writing delta=1-beta, `delta/2<=1-sqrt(beta)<=delta` proves each minimum entry is at least `min{a,delta}/10`. This gives `min{a,delta}/180`, with no vanishing extra beta-dependent multiplicative constant. Using a minimum rather than a product is the decisive correct improvement.
- **Endpoints and maximum:** beta=1 uses the IID floor, not a degenerate testing family or a fixed-beta limit. Beta=0 recovers alpha=a/10. Combining the structural and IID witnesses by a maximum proves F/180 throughout the closed interval.
- **Verdict:** PASS. Repair direction: None.

### unit_007 — Corollary 7: Regimes and algorithm distinction (`cor:s006-regimes`)

- **Rate regimes:** b<=a directly gives F=b for z<=b, F=z for b<=z<=a, and F=a for z>=a. Overlapping boundary equalities are consistent.
- **Algorithm scope:** for z>=a the original rule's 48a upper and class minimax a/180 lower give its correct worst-case order. For z<=a the pooled bound is at most 3F; this is not assigned to the original rule.
- **Exact classes:** rho=0 forces every row equal to p and stationary pi=p tensor p; rho=1 includes every stationary table because TV<=1. Lemma 5 supplies the beta endpoints.
- **Same-target separation:** S005's even-K stationary IID sequence belongs to both exact endpoints. Its original-rule risk is at least 391/1600, while the empirical pooled upper `(1/2)sqrt(K/M)` tends to zero for `M=floor(K^2/100)`. Since b tends to zero too, a universal original-rule/minimax factor cannot hold. This is not misused as a single-source all-algorithm lower.
- **Verdict:** PASS. Repair direction: None.

## Hidden Subclaim, Assumption and Notation Audit

The seven units account for every substantive bridge. The finite martingale second moment, pathwise center comparison, conditional sign prior, full-N IID experiment, exact endpoints, minimax quantifier order, and capped scalar equivalence are all proved or explicitly mapped to accepted dependency calculations. No generated event, fast-mixing property, recurrence hypothesis or source-specific selector is assumed without proof.

Primitive conditions are exactly the fixed experiment, legal homogeneous table, stationary initialization for the two theorems, public parameter domains and the stated row-radius/minorization hypotheses. Lemma 1's arbitrary initial law is local; it does not remove stationarity from the combined result. The existential center is a fixed proof witness for each source, so no cross-source measurable selection is needed.

Public objects are the two classes, risks, a,b,F, the two actual estimators and their public selector. Filtrations, D_i, q_bar, signs, reverse laws, amplitudes and residual rows are proof-local. The local first-symbol a versus rate a_stat reuse is explicitly disambiguated in the text; no inequality uses the wrong object. No unnecessary helper is supplied to an algorithm.



## Target Claim and Explicit Rate Audit

- Exposed variables are all integers K>=2,M>=1 and all rho,beta in [0,1]. Constants 1/180 and 48 are absolute and independent of all source/class parameters.
- Risk remains unconditional expected TV at the actual same-trajectory endpoint, with exactly M observed departures and the complete M+2-symbol data. No conditional-query, independent-query, stopping-time, high-probability, TV-squared or predictive-KL claim replaces it.
- Random endpoint/count dependence is not removed: the pooled proof is martingale/pathwise, the inherited original bound explicitly covers it, and the lower uses full endpoint-conditional data laws. Zero counts never require an empirical row denominator in the pooled branch, and add-one always has n_s+K>0.
- The two amplitude minima and their lower comparisons preserve joint radius/beta dependence. No fixed-beta asymptotic constant is substituted for a beta-uniform rate.
- Baselines are preserved: rho=1/beta=0 recover the full stationary a rate; rho=0/beta=1 recover the exact stationary IID b rate. The sharper selector bound preserves the pooled endpoint upper, notwithstanding the deliberately coarse universal 48 summary.
- Along any parameter sequence, the universal inequalities indeed give risk tending to zero iff both b and min{z,a} tend to zero. This follows directly from F being their maximum, not from an additional mixing claim.

## Limited Adversarial Computation

Acceptance rests on the symbolic audit, not finite enumeration. A reviewer-owned inline Python command checked only the following small cases; no producer checker or large grid was used:

1. For `(K,M)=(2,3),(3,2)` and checkerboard amplitudes `alpha=1/10,1/100`, constructed the all-positive-sign table and its `(b,i,j)=(0,0,0)` flip. Exact Fraction arithmetic verified stochastic rows/columns, uniform stationarity, the all-row TV radius and the two-step minorization.
2. For each of those four table/amplitude cases, enumerated full histories under uniform stationary initialization and under the point initialization `(0,0)`. All **8 cases** exactly verified normalization and `E||sum_i D_i||_2^2=sum_i E||D_i||_2^2<=M`; directly computed pooled risk obeyed the claimed bound.
3. In the four stationary cases, retained every full history and conditioned on each endpoint. All **26 conditional-data comparisons** normalized exactly; numerically computed neighboring KL and TV obeyed the submitted KL bound and TV<1/2. These cover odd K and a genuinely reduced amplitude.
4. Six hand-selected scalar probes `(K,M,z)=(2,1,0),(3,2,1),(2,10^8,10^-8),(100,10^6,.001),(10,10^8,.1),(3,1000,.4)` checked caps, F/G comparison, the public-selector summary upper, and both amplitude comparisons, including z=0 and z=1. The beta amplitude was evaluated stably as `min{a/10,z/(1+sqrt(1-z))}`.

Every check passed. Floating-point checks used tolerance 1e-14 where necessary; no claim of formal or infinite-parameter verification follows from them.

## Target-Step Assembly Audit and Review Rationale

The noncircular assembly is:

1. Lemma 1 plus accepted S001 gives two admissible upper bounds; Proposition 4's public selector and cap algebra yield the near-IID upper.
2. Lemma 2 supplies the radius-compliant scaled stationary structural lower; Lemma 3 supplies the stationary IID floor. Proposition 4 combines their maximum to give the matching near-IID lower.
3. Lemma 5 maps all-row q=2 minorization to the required hidden-center radius condition, yielding the Doeblin upper.
4. Proposition 6 independently embeds the correctly minimum-scaled lower family in the minorization class, adds the IID floor by maximum, and handles both endpoints explicitly.
5. Corollary 7 gives the exact three regimes and inherits only the valid stationary same-target original-rule countersequence.

These units prove the exact authorized S006 claim with no changed target, missing bridge or failed dependency. **ACCEPTED with no retry** is therefore the smallest justified outcome. The arbitrary-initialization/q>2 sharp questions and the all-parameter original-rule risk remain outside this proof, not silently completed by this acceptance.

