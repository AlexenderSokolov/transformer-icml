# S014 原独立数学审查的科学正文

编排说明（非原文）：原独立审查日期为 2026-10-28，结论 ACCEPTED，无数学修复要求。以下保留原审查的完整逐引理推理、科学适用范围与有限检查事实；身份及运行元数据省略。审查绑定原证明哈希，而非这份新复制件。独立上下文 LLM 审查不是形式验证，也不是外部同行评审。下文有限检查是原审查历史结果，本次编排未重跑；原命令、脚本和运行记录不在本包内。

编排时序说明（非原文）：全文中“未决定 aggregate”的结论是 S014 该族的历史范围，不是最新全类状态。S015 的不同星形族现已给出反证。保留原审查对 unit_009 的严格限制；未将 aligned-total 比较升级成 family-wide total 上界。有限检查编号沿原文，纯来源绑定项省略。

编排定位说明（非原文）：下文保留的 “line 384's local qualification” 指原证明 `S014_proof_v1.md` 第 384 行，对应本包 `proofs/S014_complete_proof.md` 第 366 行，即 Proposition 9 的结尾段落。此处保留的是原件行号，不是复制件行号；原审查正文不作改写。

## Useful Result

**ACCEPTED.** All nine local units establish the bounded S014 contract. The proof supplies a genuine statistical obstruction, quantified over every common randomized full-history predictor, to uniformly restoring the stationary scale after one stationary-symbol refresh or merely from product initialization with the stationary second-symbol marginal. It does not infer statistical hardness from state-TV distance.

The general original-add-one result is only the no-refresh contribution

    E[1_E0 TV(p^+_(Y_M),theta_(Y_M))]
      <= (1-beta)^M min{1,u_g(M)+beta}.

For the new lawful launch family, product-start risk has finite-prior lower `delta^(N+1)alpha/8`, while the prefixed immediate-refresh conditional risk has lower `delta^M alpha/8`, with `M=N+1`. The immediate-refresh event has probability beta, which must multiply its unconditional contribution. Along the specified logarithmic sequence the lower is order `K^-1/4`, whereas `a_h+sqrt(beta)` is order `K^-1/2`.

**Scope of unit_009:** the common predictor B_0 has weighted after-refresh risk `beta delta^M<=sqrt(beta)` throughout the constructed prefixed family. Its displayed total-risk comparison with `a_M+delta^M g_M+sqrt(beta)` is proved **only on sequence (1.10), where g_M=1**. No family-wide total-scale upper is accepted from that comparison, and no full-class weighted or total upper is proved. The nonrefutation language is read as this precise limitation of the submitted lower and sequence, not a stronger unproved theorem.

## Exact Accepted Mathematical Scope

The general source is a fixed homogeneous normalized nonnegative second-order table on `{0,...,K-1}`, with legal shift `(a,b)->(b,c)` and arbitrary initial pair law. Some hidden stationary pi satisfies `P^2(s,t)>=beta pi(t)` for every starting and destination pair. Zero transitions, zero stationary masses, reducibility and initialization singular to pi remain allowed. Algorithms may use the entire `h+2` observed symbols, public `K,h,beta`, and an independent seed, but not hidden parameters, auxiliary coins or future data. Risk is expected half-L1 TV at the actual terminal row after exactly h departures.

1. **General event upper:** for every `K>=2,M>=1,0<beta<1`, stationarity and all-pair minorization give the hidden marginal p and legal residual Q. The unchanged original count rule has the displayed no-refresh-event contribution upper. This is not a complement-event or total-risk bound.
2. **Launch family:** for `K>=14`, `m=floor((K-2)/4)`, `L=m^2`, integer `q>=1`, `N=2+qL`, `M=N+1`, and `alpha=min(1/2,sqrt(m^3/(q+1))/8)`, the new full table has stationary witness `delta_(0,0)` and exact coefficient beta relative to it.
3. **Product initialization:** at `mu=delta_ell tensor delta_0`, every common full-history randomized B has uniform-sign-prior risk at least `delta^(N+1)alpha/8`; the one common B_0=`delta_0` has exact family risk `delta^(N+1)`.
4. **Immediate-refresh prefix:** starting instead at `(0,ell)` with M departures, conditional on `tau=0` the whole observed experiment is the product experiment with one fixed initial symbol attached. Every common B has prior-average conditional risk at least `delta^M alpha/8`; B_0 has conditional risk `delta^M`. The event probability is beta under every sign, so the corresponding unconditional lower contribution is `beta delta^M alpha/8`.
5. **Uniform-restoration negation:** along (1.10), `q=floor(K^4/L)`, `beta=log(K)/(4N)`, `M=N+1`, the lower divided by `a_h+sqrt(beta)` diverges for h=N and h=M. Thus no finite universal C and no choice of common predictors at public parameters can provide the proposed uniform bound in either stated experiment.
6. **Weighted boundary:** first-refresh disintegration is exact. The family-wide B_0 weighted contribution is `beta delta^M`; the total comparison established in the proof is restricted to (1.10). Neither an unweighted conditional lower nor this aligned example decides the full-class aggregate question.

The evidence classification is **obstruction**. No arbitrary-residue extension, beta-endpoint theorem, product-class upper, full joint minimax solution, or subsequent S015 premise is part of this acceptance.

## Per-Lemma Audit

### unit_001 — Lemma 1: Symbol decomposition and original no-refresh bridge (`lem:s014-no-refresh`)

- **Statement fidelity:** retains all K>=2, M>=1 and 0<beta<1, all rows including off-support rows, hidden p, original full history/counts, changing terminal target, and event-contribution scope.
- **Algebra and assumptions:** the only two-step legal path gives `P^2((a,b),(c,d))=theta_ab(c)theta_bc(d)`. Summing d yields `theta_ab(c)>=beta p(c)` without division by any stationary mass. Pi's stationarity equates its two marginals. The residual rows are nonnegative with sum one; no minorization or stationarity of Q is required.
- **Exact realization:** independent finite refresh coins, p-draws and residual row samples reproduce each positive-probability prefix law. Null prefixes have zero probability in both constructions. Conditioning all coins to zero has probability delta^M independent of initialization and residual samples, and leaves precisely the whole Q experiment with the original mu.
- **Target bridge:** pointwise `TV(theta_s,Q_s)=beta TV(p,Q_s)<=beta`; the terminal s may depend on the entire residual history. Triangle inequality and the exact accepted L1+ interface bound the unchanged add-one rule by `u_g(M)+beta`; the loss cap then gives the stated minimum before multiplication by delta^M.
- **Adversarial checks:** sparse p, zero entries, zero terminal visit count and nonstationary Q cause no missing denominator or applicability condition. The algorithm is never given p or coin labels. No suffix or conditional-IID shortcut occurs.
- **Contribution:** establishes only the general no-refresh bridge required by export 1.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Lemma 2: Launch clock and phase invariant (`lem:s014-launch`)

- **Statement fidelity:** constructs every one of K-squared residual rows under the exact new K,m,ell domain, with both launch categories in addition to the inherited active architecture.
- **Euler existence:** the balanced finite directed graph argument closes every unused-edge walk; completeness ensures a splice vertex until all edges are exhausted. Rotation to `c_5=1` is possible for L>=9 and does not require `c_6=1`. Retained clock pairs are distinct.
- **Legality and normalization:** `4m<=K-2` reserves both 0 and ell. Ordered alphabet types make the active phases disjoint; launch rows contain 0 and do not overlap active rows or each other. Paired W masses total 2/m, the odd leftover has mass 1/m, and alpha<=1/2 guarantees positive W support. Defaults cover all unassigned rows, including leftover letters and removed clock pairs.
- **Recurring invariant:** the five-step path reaches `(1,c_6)=e_5`; deterministic clock successors and the wrap return to the next phase. All active residual outputs are nonzero and not ell. The two launch steps are exactly `(ell,0)->(0,A)->(A,B)`.
- **Adversarial checks:** independently tested non-loop return `c_6!=1`, m=3, odd/even m, all leftover alphabet residues, launch/default intersections and every residual phase successor. No time-dependent row or added state is introduced.
- **Contribution:** full construction and named phase invariant for every subsequent statistical claim.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Lemma 3: Sparse stationary witness and every-pair minorization (`lem:s014-member`)

- **Stationarity:** row 00 is default and absorbing, so pi=`delta_00` is stationary and both symbol marginals are `delta_0`.
- **R category:** active or launch rows have first-zero probability beta. Their second coordinate is not ell, so the ensuing `(b,0)` row is default and supplies a second zero surely. Exact two-step mass at 00 is beta.
- **Ending-ell exception:** every `(a,ell)` is default, but its next pair `(ell,0)` is exceptional. Its first zero occurs surely and its second only with probability beta. Thus this whole category has mass beta, not one; `(0,ell)` and `(ell,ell)` are included.
- **Remaining default rows:** their second coordinate differs from ell, so both zeros occur surely. The three categories are disjoint and exhaustive. Every other destination has zero pi mass and requires only nonnegativity. An attaining R row shows the coefficient relative to this pi is exactly beta.
- **Adversarial checks:** all K-squared starting rows were checked, not just reachable rows. No absolute-continuity or full stationary support assumption is added.
- **Contribution:** lawful membership of every finite-prior source and the product-start marginal identity.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Lemma 4: Complete aligned history and survival invariant (`lem:s014-history`)

- **Entry and visits:** two launch steps reach D_2 at absolute time 2. The phase recurrence gives precisely `2,2+L,...,2+qL=N` as UV times. Exactly q are observed unknown departures; the last is the actual unobserved-departure target.
- **Entire-data bijection:** G starts with fixed ell,0, inserts the two launch coordinates, every label once, every deterministic filler, and the final context T. Its extraction inverse uses the displayed original symbol indices. Repeated appearances of a label in consecutive pairs are not extra observations. All tuples have positive probability and no sign-dependent reconstruction is used.
- **Product law:** each of q+1 context pairs supplies two 1/m factors, each of q labels one q_sigma factor, and everything else one. This proves the full conditional-history law, IID training triples and uniform independent actual T only in this special family. The weight of `(E,T=s)` is the positive common `delta^N/m^2`.
- **Survival/absorption:** killing at t=0 reaches 00; at t=1 it reaches `(u,0)`; later it reaches `(b,0)` with b active and not ell. All are default, so the exceptional launch row cannot be reentered. E is recognizable by no zero among appended outputs, excluding the fixed initial zero. No label is added to the observation.
- **Adversarial checks:** exact full-history enumerations tested two cycles at m=3 and one at m=4, with the actual prescribed amplitudes, plus every killed history including last-step killing. Endpoint placement, probabilities and every observed symbol were retained.
- **Contribution:** supplies the full experiment needed for a statistical, rather than state-TV or reduced-data, lower.
- **Verdict:** PASS. Repair direction: None.

### unit_005 — Proposition 5: Full-history finite-prior testing (`prop:s014-product-lower`)

- **Conditional information:** `(E,T=s)` has the same probability under all signs, so its conditioning preserves the prior, not a posterior after all H. G at fixed T is a common bijection. One-bit KL is exactly `(2alpha/m^3)log((1+alpha)/(1-alpha))`, and the complete conditional-history KL is q times this value even for a bit in the actual endpoint row.
- **Amplitude and testing:** the integral logarithm bound and both cap branches give KL<=1/8. The finite convexity/binary-divergence proof gives TV<=1/4 with the correct normalization. Integrating any independent algorithm seed gives a common [0,1]-valued test, error sum>=3/4, and bit error>=3/8 under one uniform cube prior.
- **New target:** its W contrast is `2delta alpha sigma/m`, not the old contrast. An incorrect decoded sign costs at least `delta alpha/m` half-L1 loss on that coordinate pair. Disjoint coordinate pairs can be summed; the tie convention is sound; other predicted mass cannot cancel those losses.
- **Actual risk and quantifiers:** averaging over actual endpoint weights 1/m^2 and r/m>=1/3 gives conditional risk>=delta alpha/8, then multiplying delta^N gives delta^(N+1)alpha/8. Off-E loss is discarded only as nonnegative, not declared uninformative. B is fixed before choosing its hard sign; infimum over B is taken afterwards. All public construction knowledge remains common and does not break testing.
- **Adversarial checks:** m=3 neighboring q=2 full product calculation gives KL 0.043803186686903875 and TV 13/243, below the required bounds. Both amplitude branches and arbitrary randomized outputs were checked symbolically.
- **Contribution:** the required finite-prior statistical lower on the product-initialized subclass.
- **Verdict:** PASS. Repair direction: None.

### unit_006 — Proposition 6: Exact family-only upper (`prop:s014-family-upper`)

- **On survival:** the actual UV target puts mass delta outside 0, so B_0's loss is exactly delta.
- **After killing:** even a last-step refresh leaves an ending-0 default terminal row with target already delta_0. Earlier killing reaches 00. The exceptional `(ell,0)` cannot be reached after killing, including killing in either launch step.
- **Exact risk and scope:** multiplication by delta^N gives delta^(N+1) for every sign. B_0 is common and requires no source or stationary-law input. This bounds only the explicitly constructed family; it is not a product-class or general-class upper.
- **Adversarial checks:** exact path enumeration retained every nonsurviving path and verified zero loss there, including launch and last-departure cases.
- **Contribution:** accurate family sandwich and limitation on what this family demonstrates.
- **Verdict:** PASS. Repair direction: None.

### unit_007 — Proposition 7: Immediate-refresh prefix (`prop:s014-prefix`)

- **First transition:** `(0,ell)` is default; both refresh and residual components equal delta_0. Therefore the observed X_3 is 0 regardless of J_0, and the suffix starts exactly at `(ell,0)`.
- **Conditioning:** `tau=0` is precisely J_0=1, of probability beta for every sign, independent of future coins, residual sampling and the seed. The N remaining departures use the same fixed table.
- **Full-information equality:** `Z_i=X_(i+1)` gives `H_M=(0,Z_1,...,Z_(N+2))`. The fixed deleted-in-suffix initial 0 is recovered exactly; terminal pair and unobserved target agree. Composing any full-M-history predictor with this map is a common full-N-history predictor with public M=N+1.
- **Risk and event weight:** the conditional lower is delta^(N+1)alpha/8=delta^M alpha/8; the B_0 conditional risk is delta^M. Multiplying the exact beta probability yields the unconditional contribution beta delta^M alpha/8. A revealed tau=0 is merely a constant common label within this conditional experiment, not a hidden oracle. The original algorithm is not given it.
- **Adversarial checks:** every enumerated prefixed path had exactly the probability of its complete product suffix. Visible independence of X_3 and J_0 does not erase the weight of the auxiliary event.
- **Contribution:** shows why first-symbol refreshing does not provide the proposed uniform conditional statistical bridge.
- **Verdict:** PASS. Repair direction: None.

### unit_008 — Corollary 8: Aligned logarithmic negation (`cor:s014-log`)

- **Admissibility and horizon:** the floor relation gives `K^4-L+2<N<=K^4+2`, hence N~K^4 and M=N+1~K^4. For all K>=14 the selected q>=1 and 0<beta<1. N is explicitly a departure count, not the old package's observed-symbol notation.
- **Amplitude:** m>=K/8 and q+1<=K^4/m^2+1 give `m^3/(q+1)>=K/(2*8^5)`. The stated numerical sufficient threshold implies alpha=1/2. This is source- and algorithm-independent.
- **Exponential control:** the integral remainder for -log(1-beta) yields `|log(delta^(N+1))+(log K)/4|<=beta+(N+1)beta^2/(2delta)->0`. Thus exact horizon shifts have not been silently absorbed in an exponent.
- **Scales:** a_N and a_M are each asymptotic to K^-1/2; `sqrt(beta)=sqrt(log K)/(2sqrt(N))=o(K^-1/2)`. The lower-to-proposed-upper ratio is asymptotic to K^1/4/16.
- **Negation order:** for any finite C, choose a sufficiently large public parameter point; every common B then has some sign source exceeding the claimed upper. The hard sign may depend on B. No single universally hard sign, add-one-only obstruction, or arbitrary-horizon claim is substituted.
- **Adversarial checks:** independently checked floor/admissibility/g_M identities for K=14,...,1000; asymptotics rest on the analytic error bounds, not these probes.
- **Contribution:** the two precise uniform-restoration impossibilities.
- **Verdict:** PASS. Repair direction: None.

### unit_009 — Proposition 9: Weighted scope boundary (`prop:s014-weighted`)

- **Disintegration:** independent coins give `P(tau=t)=beta delta^t` and `P(tau=infinity)=delta^h`. These positive-probability events partition the finite experiment. Conditional losses retain the entire prefix and the actual terminal target; none is replaced by a stationary-start risk.
- **Exact family identities:** in the prefixed experiment, B_0 has positive loss delta precisely when all N suffix coins vanish, irrespective of J_0. Total risk is delta^M. Among these paths a refresh has occurred precisely when J_0=1, giving weighted after-refresh risk beta delta^M. No-refresh contribution is delta^(M+1); the two sum to delta^M.
- **Global weighted-family comparison:** for every permitted K,q,beta and every sign, beta delta^M<=beta<=sqrt(beta). Thus this particular common predictor fits the putative weighted scale throughout the family, not just on the logarithmic sequence. This is still not a full-class upper, nor an upper for every predictor or for the original add-one rule.
- **Limited total comparison:** the proof invokes `M+1<=K^4+4<K^5` specifically on (1.10), so g_M=1 there and total B_0 risk delta^M is bounded by the proposed total expression with constant one there. The proof does **not** show B_0 obeys that total scale for all q and beta. The opening nonrefutation language is constrained by this explicit proof and line 384's local qualification; it is not accepted as a stronger family-wide total theorem.
- **Boundary consequence:** the conditional lower gives a weighted lower beta delta^M alpha/8, of order `K^(-17/4)log K` on the sequence, much smaller than a_M. The submitted large conditional risk therefore does not refute either weighted target. Their full-class validity remains open in this dependency set.
- **Contribution:** precisely separates a false uniform conditional bridge from an undecided weighted aggregate target.
- **Verdict:** PASS. Repair direction: None. Downstream citation must preserve the global-weighted / aligned-total distinction.

## Hidden Subclaim Scan

All independent load-bearing claims are accounted for by the nine named units: legal decomposition and target bridge; full clock/launch table and recurrence; all-pair membership; complete history, survival and absorption; full conditional information and common testing; actual new-target loss; exact family upper; prefix information equivalence and event weight; logarithmic specialization; and disintegration with scope boundary. The supporting Euler existence, Pinsker argument, finite prior pairing and numerical bounds are explicitly proved within their units.

The new entry-state obligations are not outsourced to S012: `(ell,0)` and `(0,u)` are new exceptions, rows ending ell are treated separately, and `(0,ell)`'s deterministic first transition is traced. The fixed initial zero is retained and distinguished from a killing output. No nontrivial independent claim is hidden in the assembly, and no diagnostic or subsequent candidate is used as a premise.

## Target Claim, Assumption and Baseline Audit

The six contract exports follow in their exact domains. Primitive assumptions are only the fixed finite legal-shift source, observation and information restrictions, existential stationary law/all-pair minorization and displayed public parameter restrictions. Residual legality, clock closure, recurrence, source membership, support, survival, endpoint independence and probability identities are derived. E, `(E,T=s)` and tau=0 are used as local conditional events with common positive probabilities already established.

The general bound preserves the original add-one estimator, not a suffix estimator. The lower uses every observed symbol and the actual endpoint rather than a reduced-data or independent-query substitute. No general random-row conditional-IID assumption is introduced. Zero counts remain valid through the accepted L1+ interface. Product stationary-second-marginal initialization is not asserted to be pair stationary: this family has `delta_(ell,0)!=delta_00`, while genuine stationary initialization stays at 00. Thus the counterexample does not contradict the stationary theorem or imply all stationary pair laws are products.

## Explicit Rate Audit

All finite constants are displayed and numerical: 48 comes only from L1+; the testing constants follow from the exact KL, half-L1 contrast, r/m>=1/3 and amplitude cap. The statistical mode is deterministic finite-horizon expected TV, with conditional claims explicitly tagged and multiplied by delta^N or beta when used unconditionally. K alone varies in (1.10); source, sign, history and algorithm do not enter hidden asymptotic constants.

The new target contributes an extra delta beyond the no-refresh path probability. The prefixed horizon is exactly M=N+1. Both a_N and a_M and their different +1 denominators are controlled. The generic +beta target bridge is not dropped. No beta endpoint, all-time, stopped-horizon, squared-TV or high-probability upgrade is claimed. The weighted/total distinction in unit_009 is essential to the accepted rate scope.

## Notation Surface and Assembly Audit

The public-facing objects are the exact experiment/class, original estimator, rates and finite conditional/event lower and upper statements. The alphabets, Euler word, phase sets, signs, residual Q, coins, tests and reconstruction G are proof-local. Public m,L,q,N,M,alpha are deterministic restrictions, not hidden observation-chosen tuning. Notation provenance is explicit, and no helper dictionary hides an assumption.

Assembly is noncircular: Lemma 1 uses the accepted arbitrary-source original-rule interface; Lemmas 2–3 build lawful new sources; Lemma 4 proves the whole conditional experiment; Proposition 5 derives the new-target lower; Proposition 6 supplies a family-only upper; Proposition 7 transports through the exact fixed prefix; Corollary 8 proves the rate negations; Proposition 9 limits their aggregate implications. Named theorem-style references, rather than bare audit-unit IDs, carry the mathematical dependencies.

## Independent Adversarial Checks

Acceptance rests on the general symbolic audit. A reviewer-owned inline Python command, not a reused producer checker, also performed the following checks. It created no checker file.


2. **9,412 exact full-table row checks** with `Fraction`, m=3,4,5, every K=4m+2,...,4m+5, beta in `{1/7,4/5}` and alpha=1/3. Euler rotations deliberately had `c_5=1,c_6!=1`. Checked normalization, stationarity at 00, all three exact two-step-mass categories, disjoint phases and every residual phase successor. The fixed alpha here tests structural claims, not the chosen testing amplitude.
3. **7,585 full residual histories** and **33,148 complete actual/prefixed histories**, at `(m,q,alpha)=(3,2,3/8)` and `(4,1,1/2)`, beta=2/7, K=4m+5. These use the actual prescribed amplitudes. Checked every path mass, number and indices of UV visits, endpoint weights, complete path-product factors, exact survival factors, absorption targets, exact B_0 risk and equality of each prefixed visible history probability to its full product suffix probability. The two cases have respectively 6,561 and 1,024 residual histories, and 14,377 and 2,197 histories in each actual/prefixed experiment.
4. **729 neighboring conditional product atoms** at m=3,q=2,alpha=3/8. Exact TV was `13/243`; floating KL was `0.043803186686903875`, agreeing with the exact displayed formula to below 1e-14. The common full-history bijection transfers this to the complete conditional observations.
5. **987 aligned finite parameter probes**, K=14,...,1000, checked q>=1, beta admissibility, the exact N floor bounds, m>=K/8, N>=K^4/2 and g_M=1. They supplement, rather than establish, the asymptotic proof.

All checks passed. These are finite sanity/adversarial checks, not formal verification. The event-weight identities were checked algebraically from the independently verified prefix independence and positive-loss path characterization; no claim is made to have enumerated all latent coin strings separately.

The exact bounded contract is proved without a new assumption, changed interface, missing bridge or dependency repair. ACCEPTED with no retry is therefore justified. The only scope caution is explicit, not a repair to a missing proof: the unit_009 total comparison is the aligned-sequence comparison actually stated in its derivation, not a global family-total certificate. Downstream summaries should preserve that distinction.
