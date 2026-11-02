# S007 原独立审查的科学部分

原审查日期：2026-10-28。原审查结论：ACCEPTED；无数学修复要求。证据为独立上下文 LLM 数学审查，不是形式验证。本件逐字摘录原审查的范围、逐引理推理与有限检查；省略身份、调度和运行元数据。审查针对原证明哈希，不能把此份编排误称为对复制件的新审查。各单元的历史限定只限定该单元，综合结论见中文摘要。

## Accepted Scope

For every integer `K>=2,M>=1`, let `E_K^(3)` consist of legal homogeneous second-order tables and arbitrary initial pair laws such that a stationary pair law pi satisfies `P^3(s,t)=pi(t)` for **every** starting and destination pair. The common estimator sees exactly `X_1,...,X_{M+2}`, may use public K,M and the class definition, and has no access to hidden source parameters. The target is the next-symbol row at the actual same-trajectory endpoint `Y_M`, and the risk is unconditional expected TV. Writing `a=min{1,sqrt(K^3/(M+1))}`, the accepted conclusion is

    a/100000 <= R_3(K,M) <= R_3^+(K,M)
      <= min{1,80 sqrt(K^3/(M+1))} <= 80a.

The infimum includes randomized estimators with independent seeds. The original add-one in this chain retains all M departures; it is not replaced by a suffix or pooled estimator.

For K>=6 the stronger lower `a/34560` is established by the new stationary checkerboard family with legal symbol probabilities in `[.95/K,1.05/K]`. For K=2,...,5 the accepted S005 full-N stationary IID lower supplies the patch. Every lower witness has a genuine stationary initial pair law. No horizon-aligned phase, extra state coordinate, time-inhomogeneous transition, fixed query, independent test query, or discarded initial side information is used.

Acceptance excludes a classification of all E3 tables, a general q-reset theorem, a sharp approximate-reset transition, optimal predictive-KL or squared-TV rates, and any claim that mixing is necessary for the stationary rate or general fixed-K consistency.



## Per-Lemma Audit

### unit_001 — Lemma 1: Three-coordinate checkerboard reset, lines 94–154

- **Statement fidelity:** construction is for every K>=6 and every `0<alpha<=1/2`. The alphabet subsets and all paired supports are explicitly disjoint; r>=1. The independent r^3 bits are construction variables, not hidden assumptions on the whole E3 class.
- **Legality and stationarity:** every triple lies in at most one paired block, so the perturbation is zero or `+/-alpha/K`. Zero sums in the output coordinate make theta stochastic; zero sums in the first coordinate make every fixed destination `(b,c)` receive exactly mass `1/K^2` from the uniform pair law. Only legal `(a,b)->(b,c)` edges are introduced. Positivity refers to legal symbol probabilities, not to the structurally sparse one-step pair matrix.
- **All three cancellations:** the sum over the path's c is respectively the third-coordinate sum of `F(a,b,c)`, the second-coordinate sum of `F(b,c,d)`, and the first-coordinate sum of `F(c,d,e)`. Each vanishes with the other coordinates fixed. The middle-coordinate identity is essential and is actually proved by the v_j pairing.
- **All nonlinear terms:** `F_1F_2=0` requires b in both B and A; `F_2F_3=0` requires c in both B and A; `F_1F_3=0` requires c in both C and A. Thus every quadratic and the cubic term vanish pointwise, before summation. There is no unaccounted cross-block interaction or sign-dependent remainder.
- **Reset arithmetic:** the unique three-step form leaves only the one summed symbol c. The baseline is `K/K^3=1/K^2`, and the three zero linear sums eliminate every remaining term. The identity holds for ALL starting and destination pairs, including unused symbols, not merely under stationarity.
- **Not two-step reset:** choose any active a,b,c. Since b belongs to B and not A, the next row `(b,c)` is baseline for every output d. The two-step mass is `(1+/-alpha)/K^2`, unequal to uniform because alpha>0. Every sign vector therefore has `P^2!=Pi`.
- **Adversarial boundaries:** leftover and unpaired symbols remain exactly baseline; arbitrary remainders modulo six cause no missing normalization term. Genuine uniform stationary initialization is explicitly selected, with no phase or time coordinate.
- **Contribution:** valid E3 hard subclass and the common, positive endpoint law required later.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Lemma 2: Complete conditional reverse experiment, lines 156–179

- **Reverse kernel:** stationary reversal is `Q(y,x)=pi(x)P(x,y)/pi(y)`. Common uniform positive pi cancels the ratio and yields exactly `Q((b,c),(a,b))=theta_ab(c)`. Its row normalization is the already proved first-coordinate cancellation.
- **Entire history:** a legal pair path and its M+2 symbols are bijective. The original initial pair factor `1/K^2` is divided by the identical endpoint mass upon conditioning, leaving the product of ALL M reversed transitions. Both initial symbols remain encoded at the far end of the reversed path; this is not a count-only or shortened experiment.
- **Reverse two-step bound:** the unique path `(u,v)->(b,u)->(a,b)` has mass `theta_bu(v)theta_ab(u)`. Each factor is at most `(1+alpha)/K`, hence the displayed uniform bound. Averaging over `Z_{t-2}` extends it to every t>=2.
- **Boundary audit:** no smoothing claim is made at reverse t=0 or t=1. Every endpoint has positive mass. No independence of a selected row, visit count, or endpoint is asserted.
- **Contribution:** exact full-information conditional data law and valid later-time visit envelope.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Lemma 3: Four-row conditional information, lines 181–226

- **Changed-row count:** flipping bit `(i,j,l)` changes exactly `B_j x C_l`, FOUR reverse departure rows. In each, only the two outgoing a symbols in A_i change. Other i-block probabilities in that reverse row may depend on other signs but do not change and contribute zero to the adjacent KL. The older two-row constant is not mistakenly reused.
- **Exact row KL:** the two affected probabilities swap, so the divergence is `(2alpha/K)log((1+alpha)/(1-alpha))`. The integral/log estimate gives at most `8alpha^2/K` for alpha<=1/2. This applies in either orientation of the sign flip.
- **Startup accounting:** the M reverse departure times are exactly 0,...,M-1. The first `min(M,2)` contribute at most that amount; every subsequent visit to the four-row set has probability at most `4(1+alpha)^2/K^2<=9/K^2`. Therefore the conservative bound `2+9M/K^2` is valid also at M=1,2.
- **Conditional chain rule:** both adjacent laws start at the SAME deterministic endpoint s and are positive on the same finite legal-history support. The log product ratio expands into the M row divergences. There is no hidden initial-law KL: the complete conditional likelihood already canceled both stationary endpoint factors. Multiplication gives exactly `16alpha^2/K+72alpha^2 M/K^3`.
- **Amplitude/rate:** with `alpha=a/20`, alpha^2<=1/400 and `alpha^2 M/K^3<=1/400` in both cap regimes. The startup term is at most `16/(400K)<=1/50`; the later term is at most `9/50`. Thus D<=1/5 uniformly. Using K>=2 is conservative although the family itself needs K>=6.
- **Pinsker audit:** the finite positive support permits the two-cell Jensen reduction; the binary second derivative is at least four, giving `D>=2 TV^2`. Hence the data-law TV is at most `sqrt(1/10)<1/2`. KL is only a testing-information quantity, not a changed predictive loss.
- **Contribution:** endpoint-uniform adjacent-hypothesis testing control using every observed symbol.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Lemma 4: Endpoint decoding and averaging, lines 228–274

- **Pointwise decoder:** for an active endpoint `(a,b)` the known u_i(a)v_j(b) factor removes the endpoint's checkerboard orientation. The true signed output-pair difference is `(2alpha/K)sigma_ijl`. A wrong sign forces at least `2alpha/K` pairwise L1 error. A tie with true negative sign still incurs that full error; a true positive tie is not counted as an error.
- **TV factor:** disjoint C_l pairs can be summed without cancellation. The factor one-half in TV gives exactly `alpha/K` per wrong bit.
- **Conditional prior:** every source has terminal mass `1/K^2` at each s, so conditioning the uniform sign prior on the actual endpoint preserves it. This key fact is derived from stationarity and common pi, not presumed from trajectory independence.
- **Randomized testing:** the independent estimator seed can be integrated to a decision probability f(h) in [0,1]. The paired error sum is at least `1-TV>=1/2`; averaging the two bit values and the other signs gives at least 1/4 error per target bit. The tests may use all of H and the publicly known class.
- **Actual-endpoint weighting:** there are `4r^2` active endpoints, each of mass `1/K^2`, and r disjoint target bits per endpoint. Thus the Bayes risk is at least `(1/K^2)(4r^2)(alpha/K)(r/4)=alpha r^3/K^3`. Neither the four endpoint copies nor the probability of the actual endpoint is missing. Nonnegative loss outside these endpoints is safely discarded.
- **All-K rounding:** `r=floor(floor(K/3)/2)=floor(K/6)`. For 6<=K<=11, r=1>=K/12. For K>=12 the stated `K=6q+t` calculation gives r=q and `r>=K/6-1>=K/12`. Consequently the lower is at least `a/(20*12^3)=a/34560`.
- **Minimax quantifiers:** the family depends only on public K,M, is fixed within a trajectory, and is independent of T. Every admissible T has supremum risk at least its finite-prior average; only then is infimum taken. Revealing the family's common uniform pi would not reveal a sign or invalidate testing.
- **Contribution:** full-parameter large-alphabet lower on exactly the authorized loss and experiment.
- **Verdict:** PASS. Repair direction: None.

### unit_005 — Proposition 5: Small alphabets, lines 276–288

- **Subclass membership:** for IID transition rows p, the legal two-step kernel is `Pi_p` with stationary `pi_p=p tensor p`; multiplying by P gives `P^3=Pi_p`. This holds with zero coordinates and at every starting pair, including outside stationary support.
- **Full-data interface:** choosing the genuine stationary initial law pi_p makes ALL `N=M+2` symbols IID p. The actual target row is p identically, so the accepted S005 lower applies without deleting the first two observations or changing the query. An E3 estimator restricted to this family is a common full-data estimator covered by S005.
- **Capped conversion:** with `x=sqrt(K/(M+1))`, `min(1,Kx)<=K min(1,x)` for every x>=0. Thus the IID rate is at least a/K>=a/5 for K=2,...,5. The lower constant is `1/(160 sqrt(6))`, greater than `1/100000` since `160sqrt(6)<480`.
- **Boundary audit:** M=1 and all small K are included by the accepted full-N theorem. The stationary law may vary with the hidden p across sources, as allowed; it is never revealed to the estimator.
- **Contribution:** fills exactly the K<6 gap without falsely forcing a nonempty three-block checkerboard there.
- **Verdict:** PASS. Repair direction: None.

### unit_006 — Proposition 6: Original-rule arbitrary-start upper, lines 290–308

- **Dependency applicability:** for M>=4, b=3 is a valid deterministic analytical index, `L=M-3>=1`, and `P^3=Pi` on EVERY starting pair implies `mu P^3=pi` for every mu. This includes initial mass outside stationary support. Hence eta_3=0 in the accepted ORIGINAL S004.2 bound.
- **Algorithm fidelity:** S004.2 concerns the original all-M-departure count and original stack identity. No suffix-risk bound is reassigned to this algorithm, and no first-three-observation loss or hidden-input burn is introduced. The full initial history is not claimed to be stationary.
- **Horizon conversion:** S004.2 yields `min{1,48K^(3/2)/sqrt(M-2)}`. For M>=4, `(M+1)/(M-2)<=5/2`, and the exact calculation `48^2*(5/2)=5760<5776=76^2` gives the required constant below 80.
- **Small horizons:** for M<=3 and K>=2, `K^3/(M+1)>=2`; the cap one proves the asserted bound and a=1. No inadmissible b or zero denominator occurs.
- **Risk chain:** the unchanged original rule is one admissible common estimator, so `R_3<=R_3^+`; supremum preserves the uniform upper; `min(1,80t)<=80min(1,t)` gives the final displayed inequality.
- **Contribution:** arbitrary-initialization all-K,M upper for the same algorithm and loss as the theorem.
- **Verdict:** PASS. Repair direction: None.

## Hidden Subclaim Scan

All theorem-critical bridges are represented in the six local units: generated-family normalization and stationarity; full all-state reset; non-IID/two-step failure; full-history bijection; stationary reverse kernel; startup-aware chain rule; finite Pinsker; randomized testing; posterior-prior preservation at the actual endpoint; decoding and weighted averaging; capped small-K conversion; and accepted original-count upper specialization.

The prose comparison to exact two-step reset is valid: the unique legal two-step product, summed over its final d, forces every row to equal p. This is also the checked S005 exact class identification. Its smaller minimax rate and original-rule separation are accepted S005 conclusions, not inferred from the E3 lower. The new K^3 worst-case claim for a larger class does not assert hardness for its IID subset.

The sample-scale statement is a direct correct consequence: for `0<delta<c=1/100000`, risk<=delta together with the minimax lower forces the nonsaturated branch and `M+1>=c^2 K^3/delta^2`. The original upper gives sufficiency at `M+1>=80^2 K^3/delta^2`. These are loose mean-TV thresholds, not sharp constants or high-probability statements.

No hidden assumption of irreducibility, reversibility, selected-row IID samples, conditional visit independence, or stationarity of arbitrary-start full histories is used.



## Target Claim and Explicit Rate Audit

- The target is exactly unconditional `E[TV]` at the actual endpoint after M observed departures, with N=M+2 complete observed symbols.
- The theorem exposes only deterministic integer K>=2,M>=1. Constants are absolute; alpha, m, r and the partition are explicitly derived proof-local choices. There is no concealed source-, confidence-, mixing-time-, or initialization-dependent coefficient.
- The hard-family amplitude is valid for every finite horizon and both cap regimes. Its dependence on K,M is allowed in the minimax supremum, while its table remains fixed throughout each trajectory.
- Class E3, admissible information and arbitrary initial laws are explicitly defined. Uniform pi and all checkerboard cancellations are proved subclass properties, not strengthened assumptions on E3.
- The upper's analytical burn is fixed at three and is used only where admissible. The original estimator does not read it or any hidden law.
- No fixed-horizon statement is upgraded to stopping-time, simultaneous-time, conditional-risk, high-probability, predictive-KL or optimal squared-TV control.
- The conservative lower constant follows from `1/34560>1/100000` and the stronger small-K constant. The exact-reset upper retains the accepted ORIGINAL S004 interface, with only its explicitly bounded horizon loss.
- The q=2 baseline is not overwritten: exact two-step reset is structurally smaller and has the accepted IID scale. E3 includes that easier subclass; its larger worst-case risk is fully compatible with it.

## Notation Surface Audit

Public-facing objects are the E3 class, its two risks, the frozen original rule and a(K,M). The partition, paired support functions, sigma, F, alpha, reverse laws, changed-row set and decoded signs are explicitly defined proof-local objects. Theta, P, mu, pi, counts and endpoint notation retain the frozen experiment's meanings. No proof-local parameter is passed secretly to an estimator. The KL in Lemma 3 is clearly between conditional data laws rather than a predictive loss.

## Limited Independent Diagnostics

Acceptance rests on the all-parameter symbolic audit, not computation. A reviewer-owned inline Python calculation, separate from the producer checker, made the following limited checks:

1. For K=6,7,12, use alpha=1/20 and block signs `(-1)^(i+2j+3l)`. Encode theta as integer numerators `20+/-1` over `20K`, form the legal pair matrix, and verify all three coordinate-sum identities, row and column sums, exact integer `P_num^3=8000K` in every entry, and `P_num^2` not identically 400. Flip block (0,0,0) and verify its changed reverse rows are exactly the four B_0 x C_0 rows. **All three cases passed.**
2. For K=6, alpha=1/20 and its one-bit flip, enumerate complete endpoint-conditional histories only for M=1,2,3 and endpoints `(0,2)` and `(2,4)`. Exact rational probability arithmetic verified normalization and the full reversed product identity; floating logarithms verified path KL equals row KL times expected changed-row reverse departures, the displayed KL upper, and TV<1/2. **All six experiments passed.** Maximum KL was `0.0018533973806848791`, maximum TV `0.018518518518518517`, and largest chain-rule residual `1.5612511283791264e-17`.
3. A limited K=6,...,120 rounding check and exact rational constant checks passed. The mathematical proof of rounding and constants above, not that finite grid, supplies the general result.

The producer's larger diagnostic was neither needed nor rerun. No finite enumeration is represented as an all-parameter proof or formal certification.

## Target-Step Assembly Audit and Review Rationale

1. Lemma 1 constructs a legal, genuinely stationary-initialized E3 family with r^3 unknown signs and a common positive endpoint law.
2. Lemmas 2–3 retain the complete conditional observation and bound the information about each sign, including startup departures and all four changed reverse rows.
3. Lemma 4 converts those conditional tests to the actual-endpoint loss with the correct `4r^2/K^2` weighting and supplies the K>=6 minimax lower.
4. Proposition 5 supplies every remaining K using the checked S005 full-N stationary IID lower.
5. Proposition 6 supplies the arbitrary-mu original-rule upper from the checked S004 ORIGINAL-count interface, with valid small-horizon handling and constant conversion.

These chains prove the exact authorized all-K,M theorem and its two-versus-three-reset interpretation without a missing bridge, altered objective or dependency mismatch. **ACCEPTED with no retry** is the smallest justified outcome. No producer revision is required.

