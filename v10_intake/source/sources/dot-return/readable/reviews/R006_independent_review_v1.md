编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R009 的词语指向问题与 R011 的历史依赖状态另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R006 independent mathematical review v1

## Verdict / useful result

**ACCEPT.** Frozen R006 proves (A) for the ENTIRE legal absorbing-stationary subclass with witness pi=delta_00, arbitrary initial pair law, all integers K>=2 and M>=1, all 0<beta<1, every integer w>=1, and every augmented event of mass at most q0. It then proves the unchanged full-history original add-one risk bound min(1,8000/K) on M=K^5, beta=log(K)/K^5. No mathematical revision is required.

The extension beyond the restricted star geometry is genuine: the proof permits all normalized rows satisfying theta_ab(0)t_b>=beta, including strict inequality, arbitrary nonzero-symbol transitions, t_b=1, zero h, and off-support initialization. The matching lower for this entire subclass is ONLY the accepted asymptotic star-subclass Omega(1/K) lower. This does not prove an arbitrary-pi upper, a global all-K exact lower, a sharp-adaptation result for ALG, or scientific novelty.

## Procedure and exact bindings

Independent mathematical review. All of frozen R006 and the complete R001, R002 and R004 proofs were read. Their complete independent reports were inspected. S020 Sections 3–5.3 through the beginning of its scalar-series verification were additionally inspected for the precise splitting and event-stack interface. The accepted R002 Section 2 lower and Section 6 reduction, accepted R004 GS, and accepted R001 joint augmentation are the inherited interfaces; no independent reproof of all historical primitive lower constructions is claimed.

No R007 content was read or used. No frozen-source edit was performed. Diagnostics are not a premise and were not rerun. This is independent mathematical review, not formal verification.

Scientific input identities below have public locators in SOURCE_INDEX.json. All hashes were computed from current readable bytes.

| Object | SHA-256 |
|---|---|
| `R006_absorbing_cutset_v1.md` | `c0e368ffc620e8f9a48c66a7092dd047f6fec04bcce8bf468fc4be8d970dc7d5` |
| `R001_mixed_prefix_and_blind_transfer.md` | `e27867bef5a59ce76fd3e343e781b31d04ed52938cb12a5a294343b1d4434ad1` |
| `R002_critical_prefix_obstruction_and_arrival.md` | `87f86a5a7f4a291e50bb78a761b765f3e3f0289bec31c823e2ed30eb65a4bc98` |
| `R004_grouped_regeneration_v1.md` | `f83f79f77ca377cb8a8991eef6a39eed4f9dabb02d810078a83e437ddaa9c2b0` |
| `R001_independent_review_v1.md` | `9238ec0d916ae1b2c3c8bb5a7daacfb9df69d9928864d0d0f11a2f5a2133eadf` |
| `R002_independent_review_v1.md` | `69a3cc715dadf2f112ce6310280010548a3fdb5ad2c6f7f839e95915b2a30590` |
| `R004_independent_review_v1.md` | `d1975609265a1055df3a5bb2f3c7c7a6eaaf0bac2f841fc418caada11c58bbe4` |
| `S020 (SOURCE_INDEX.json)` | `a478d1219c97b479f0c96d0124a6d3fff023e18a4177361a758003db4b1de8eb` |

The bound R001, R002 and R004 proofs have independent acceptance. R002 accepts bounded results but expressly does not prove (O); that obligation is a target, NOT a premise of the present review. Stale producer-status prose is historical.

## 1. Exact class, experiment, and parameterization

The observed M+2 symbols give M departures at pair times 0,...,M-1 and the actual endpoint Y_M. The original add-one uses precisely those full departure counts. There is no independent query state or truncated-data predictor.

Stationarity of delta_00 is equivalent to theta_00(0)=1. By legal shift structure the unique two-step path from (a,b) to 00 emits 0 twice, so its mass is theta_ab(0)theta_b0(0)=theta_ab(0)t_b. All other minorization right-hand sides vanish. Hence the all-state minorization is EXACTLY the stated inequality. Applying it to (b,0) gives t_b>=beta; division by t_b is legal, yielding theta_ab(0)>=beta/t_b. Neither equality nor a shared residual excursion law follows or is assumed.

## 2. General absorption point mass

For the killed kernel Q, f_t(x)=sum_y Q^(t-l)(x,y)f_l(y) holds for every 1<=l<=t, including l=t. Every matrix entry is at most one, so this is at most sum_y f_l(y). Summing in l bounds t f_t(x) by D, since the mutually exclusive first-killing times from each y have total mass at most one. This remains true when some states never get killed. Averaging against any initial subprobability preserves D/t. Initial cemetery mass contributes only at time zero.

Thus the lemma does not secretly assume eventual absorption, a small hazard, diagonalizability, recurrence properties, or independent excursions. Its use for the original chain killed on entry to 00 has at most K^2-1 noncemetery states.

## 3. Substochastic h-transform, singularities, arbitrary starts

For b nonzero, all successors with emitted c nonzero have h=1; the c=0 successor has h=1-t_b, even when this is zero. Consequently Ph=1-theta_ab(0)t_b<=delta. For a nonzero and b=0, the zero-emission successor is 00 and every other successor has h=1, giving Ph=1-t_a=h(a,0). These are the two required row-sum inequalities.

Restricting to S={h>0} makes all divisions valid. Summing R over S loses no positive h term, so its row sum is at most one. Missing mass genuinely goes to a cemetery and is not normalized away. The initial nu=mu h has mass at most one; its missing initial mass is also killed. This treats arbitrary mu, including mu concentrated at 00 or at a pair (a,0) with t_a=1.

A path ending at h>0 cannot have visited h=0 earlier: 00 is absorbing, and any other zero-h pair emits 0 surely and immediately reaches 00. Therefore every original path relevant to the nonsingular endpoint bound is represented by an R-surviving path. Multiplying the R factors telescopes h, giving exactly

    R-path mass = original-path mass * h(Y_M) * delta^(-M+N0).

Inverting it costs delta^(M-N0)/h(Y_M), not the reverse power. This is a complete-path identity and supplies no conditional iid stack claim.

Consecutive zero-ending noncemetery pairs would force 00 by shift legality. Thus among the M departure times their number N0 is at most ceil(M/2), for both horizon parities and every start. The zero-ending positive-h cutset has at most K-1 members, regardless of excursion geometry. The state count |S| is at most D=K^2-1.

## 4. Full-count cutset charge and convex chord

For each fixed start c in the cutset, b_l(c) is the surviving length-l probability with fewer than w previous occurrences of its actual endpoint. Along a single killed R trajectory, each live state is flagged at most w times: its first, second, ..., w-th occurrence, with the count before that occurrence. Summing l=0,...,M therefore gives at most |S|w<=Dw. Killing cannot create additional live flags, and the cemetery is not counted. Taking expectation proves the needed sum_l b_l(c)<=Dw for each c.

For i<M and Y_i=c, the suffix from i through M has M-i departures, all contained among the original M departures. The event that the FULL endpoint count is below w implies that the suffix endpoint count is below w. Conditional on the state at i (and survival there), the latter is an ordinary killed R suffix. Hence

    P_R(F, alive at M, Y_i=c)
      <=P_R(Y_i=c)b_(M-i)(c)<=b_(M-i)(c).

This is a one-sided event inclusion, not an assertion that empirical loss decreases with sample size. Summing i and c uses each suffix length 1,...,M once per c; adding l=0 only increases the bound. It proves E_R[N0 1_F; alive at M]<=|C|Dw<=K^3w. Subprobability initialization changes none of these inequalities.

The convex function delta^(-x) lies BELOW its chord between 0 and L=ceil(M/2). Here L>=1, so no division by zero arises. At endpoints with h>=1/2, the likelihood inversion and chord yield

    2delta^M + 2(delta^(M-L)-delta^M)K^3w/L.

Since M-L=floor(M/2), delta^(M-L)=q0 and 1/L<=2/M. This proves (C). The constant term uses only that the R surviving event probability is at most one. This remains valid if S or C is empty. All nonzero-ending endpoints have h=1; zero-ending endpoints with t_a<=1/2 have h>=1/2, including the boundary equality.

## 5. Dangerous endpoints, recent absorption, and all w

If Y_M=(a,0) is dangerous, t_a>1/2, absorption could not have happened earlier. Its conditional next-step first-absorption probability is t_a. Summing these contributions gives P(dangerous)<=2P(tau_00=M+1)<=2D/(M+1). This handles t_a=1 exactly, without dividing by zero h and without bounding hazard by beta. It does not require the next symbol to be observed: this is a probability identity under the same source law.

For Y_M=00 and first entry time t<=M, exactly M-t counted departures are 00, also when t=0. If 1<=w<=M/2 and J<w, integrality gives t=M-w+1,...,M. In particular t>0 and t>M/2. The D/t lemma therefore gives at most 2Dw/M for these w times. No initial absorbing atom is lost.

Adding (C), the dangerous bound (using w>=1), and recent absorption gives

    P(J<w)<=2delta^M+4(q0 K^3+K^2)w/M.

Since (M+1)/M<=2 this is at most 2delta^M+bw with the displayed b. Intersecting with ANY event E cannot increase this unconditional count probability; its mass cap independently gives q0. No property of the augmentation is needed for (A), even if it is not a finite label system.

If w>M/2, then 8K^3w/(M+1)>4K^3M/(M+1)>=16, so the q0 part of bw alone already exceeds q0. The trivial event-mass bound proves (A). This covers all large w, including w>M, and M=1, where no positive integer w is in the small-w branch. Thus no short-horizon or parity exception is missing.

## 6. Critical constants, obligation, and statistical conversion

On M=K^5, beta=log K/K^5, beta<1/16 follows from log K<K and K>=2. Hence delta>15/16. The inequalities delta^M<=exp(-beta M)=1/K and

    q0<=delta^(-1/2)exp(-beta M/2)<=2/sqrt(K)

hold for either parity. Therefore b<=8K^-3+16K^-5/2<=24K^-5/2. Also -log(delta)<=beta/delta gives log(1/q0)<=8log(K)/15<=K. Multiplying yields q0 b[K+log(1/q0)]<=96/K^2.

For (O), K^2/(M+1)<=K^-3<=beta K^2/log 2. Thus (A) implies the desired occupation scale on this ray for this subclass, with a universal constant. This is an actual new proof of that restricted target, not a reliance on the previously unproved full-class obligation. No claim that the proposed beta K^2 version holds at every parameter follows from this comparison.

For risk use the finite compatible augmentation of R001. Its E=pair-no-success intersect symbol-success satisfies P(E)<=q0, so (A) applies. R002's accepted trimming reduction removes up to epsilon=2delta^M mass at the smallest J levels with at most one independent fractional boundary coin. The remaining event has threshold mass at most bw and mass at most q0. Here q0>0, epsilon>=0 and b>0, so all reviewed reduction domains hold; if epsilon exceeds event mass it is simply removed entirely. The coin preserves the original unconditional stack marginal. S020's event-stack inequality applies without conditioning original stacks on E or the trimmed event.

The resulting E contribution is at most

    2/K+80sqrt(96)/K <=802/K.

G has mass delta^M, so its loss contribution is at most 1/K directly by the loss cap. R004 GS applies since beta<1/16<1/2; a=sqrt(K^3/(K^5+1))<=1/K, giving the pair-success contribution at most 6400/K. The actual R001 cover G,E,Eplus is valid even with overlaps; nonnegative loss permits overcounting. Consequently the total risk is at most 7203/K and independently at most one, proving the stated looser min(1,8000/K).

The same original add-one formula is used for every source and beta. No witness, initial law, table, label, excursion, or transformed path is a predictor input.

## 7. Matching and limits

Accepted R002 Section 2 uses the legal S015 star family with pi=delta_00 and gives a true statistical minimax lower Omega(1/K) asymptotically on this ray. Since that family is contained in the entire absorbing subclass, minimax monotonicity transfers this lower to the larger subclass. Together with the uniform upper from R006, it proves that subclass minimax and worst original-add-one risk are Theta(1/K) asymptotically.

This is not a lower for every individual source, not a finite exact lower for all K, and not a derivation from a count obstruction or an upper certificate. The full-class D2(a) floor is not used; general IID laws need not lie in this subclass. No arbitrary-pi upper or ALG sharp-adaptation conclusion is established. The stated failed avenues correctly identify the h=0 singularity, invalid conditional-iid shortcut, false small-hazard premise, and insufficiency of a fixed N0 threshold.

## Final disposition

**ACCEPT, no substantive or editorial correction required for the stated results.** No unresolved scientific check remains. Frozen candidate bytes were left unchanged. The independent acceptance here is scoped exactly to the absorbing-stationary subclass and its stated critical-ray statistical consequence.
