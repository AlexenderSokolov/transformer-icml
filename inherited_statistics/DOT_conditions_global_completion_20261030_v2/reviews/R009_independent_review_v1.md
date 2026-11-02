编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R009 的词语指向问题与 R011 的历史依赖状态另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R009 independent mathematical review v1

## Verdict and useful result

**ACCEPT.** The frozen R009 proves (A+) for every legal D2(beta) source, arbitrary stationary pi and arbitrary initialization, integer K>=2, M>=1, and 0<beta<=1/2. In particular,

    P(E0 intersect {N>=1}, J<w) <= min(q0,10 q0 K^3 w/(M+1))

for every positive integer w, with **no additive delta^M remainder**. The weaker (A) follows, and the original full-history add-one risk at M=K^5, beta=log(K)/K^5 is at most min(1,8000/K). No substantive mathematical revision is required.

One nonblocking editorial correction: Section 5 says “the second term is at most 8 q0 K^3 w/n”; this calculation refers to the FIRST term of (7). Its subsequent “last term” correctly refers to the anchor term. The algebra proves the intended bound (indeed coefficient 8+1/4 suffices), so this wording does not invalidate the theorem. Frozen proof bytes were not edited.

This is independent mathematical review, not formal verification or a novelty certification. No author diagnostic is used as a mathematical premise. No source was modified.

## Exact readable source bindings

Public scientific locators are in SOURCE_INDEX.json. The table records actual locally hashed bytes. Full R009, R001, R002 and R004 bodies, their complete reviews were read. S020's exact splitting and event-stack proof were read directly, including its finite augmentation, maximal tail, layer integration and numerical sums; these were checked against L1MAX and S001's stationary occupation argument. Other S020 comparisons are not premises here. The R001/R002/R004 proof and review hashes were matched to actual files.

| Exact path | SHA-256 |
|---|---|
| `proofs/R009_general_pi_tilted_cutset_v1.md` | `9dd08689930e438d71f671aa210866cd7e1e49ab13ba686a6b85c00b3f4d14c4` |
| `R001 (SOURCE_INDEX.json)` | `e27867bef5a59ce76fd3e343e781b31d04ed52938cb12a5a294343b1d4434ad1` |
| `R001_review (SOURCE_INDEX.json)` | `9238ec0d916ae1b2c3c8bb5a7daacfb9df69d9928864d0d0f11a2f5a2133eadf` |
| `R002 (SOURCE_INDEX.json)` | `87f86a5a7f4a291e50bb78a761b765f3e3f0289bec31c823e2ed30eb65a4bc98` |
| `R002_review (SOURCE_INDEX.json)` | `69a3cc715dadf2f112ce6310280010548a3fdb5ad2c6f7f839e95915b2a30590` |
| `R004 (SOURCE_INDEX.json)` | `f83f79f77ca377cb8a8991eef6a39eed4f9dabb02d810078a83e437ddaa9c2b0` |
| `R004_review (SOURCE_INDEX.json)` | `d1975609265a1055df3a5bb2f3c7c7a6eaaf0bac2f841fc418caada11c58bbe4` |
| `S020 (SOURCE_INDEX.json)` | `a478d1219c97b479f0c96d0124a6d3fff023e18a4177361a758003db4b1de8eb` |
| `L1MAX (SOURCE_INDEX.json)` | `b430fe3d176ecefc00ac575670ea13ffc5d5799f9e232a10375333a0547f44e4` |
| `S001 (SOURCE_INDEX.json)` | `7fa8b2119f84d9f382da80516aa8b3c277ebd2c4587dffd58d24bf16b11a77d4` |

The count proof is self-contained and does not import R006's absorbing-pi result. R006 and unavailable S026–S032 originals are not mathematical premises of this review. The lower-order comparison uses the already accepted restricted-star lower reported and checked in R002; this review does not claim a new independent re-audit of all S015 lower-bound bytes. The new upper and count result do not require that lower.

## 1. Full-history likelihood, zeros and joint labels

The unique legal path in a pair block from (a,b) to (c,d) has midpoint (b,c) and mass L=theta_ab(c)theta_bc(d). Canonical pair splitting assigns failure mass L-beta pi(c,d). Thus for a positive-probability complete history, the posterior failure probabilities multiply across disjoint aligned blocks, giving product W. This remains a complete-symbol-history identity, not merely a skeleton identity: there is no choice of midpoint to integrate incorrectly.

Summing the all-state minorization in d gives theta_ab(c)>=beta p(c) for every row. Therefore T=(theta-beta p)/delta is legal, even off support. Canonical symbol splitting has independent labels conditional on the full history, with posterior success beta p(c)/theta_ab(c). Conditional-product coupling of the pair and symbol posterior kernels is exactly the compatible construction in R001. Its weighted marginal gives

    theta_ab(c) E[z^(symbol label)|history edge]
      =theta_ab(c)-beta(1-z)p(c)=delta T_ab(c)+beta z p(c).

Multiplication proves (1) for every history event F. No unconditional independence between the two systems is asserted. Since the path space and label space are finite, Z_F is a finite polynomial with nonnegative coefficients and its differentiation and integration are elementary exact operations. In particular Z_F(1)-Z_F(0) is precisely the E-weighted history probability, not an approximation involving typical refresh counts.

If L=0, minorization forces pi(c,d)=0. At least one ordinary edge is zero, and that edge has p(output)=0 and T(output)=0. Its A_z is identically zero. Thus the whole block polynomial vanishes identically, including derivatives of the product; W=0 on this null block causes no lost positive term or division by zero. After discarding W in a marked block the bound still increases a nonnegative summand. No posterior kernel at a null history is needed for the probabilistic identity.

The symbol-label marginal has independent Bernoulli(beta) labels before conditioning, so P(N=0)=delta^M. The pair marginal similarly has P(E0)=delta^r. Conditional-product attachment preserves both facts.

## 2. Convex chord and killed normalization

For a fixed row s, each factor A_z has nonnegative constant and linear coefficient. With fixed W>=0 the row sum f_s(z) is a quadratic with nonnegative coefficients; in particular its second derivative is nonnegative. Hence the convex chord is an UPPER bound, as required:

    f_s(z)<=(1-z)f_s(0)+z f_s(1)
          <=(1-z)delta^2+z delta=delta a_z.

At z=0, dropping W gives row sum delta^2 because T is stochastic. At z=1, summing L-beta pi gives exactly delta, also at zero-L entries. The common scale is delta a_z, not a state-dependent normalization. B_z=H_z/(delta a_z) is therefore substochastic for every row, with delta a_z>0. Adding an absorbing cemetery creates one fixed homogeneous chain for each fixed z. Its live l-step mass is the H_z path mass divided by (delta a_z)^l. Cemetery visits are excluded from the count. No assertion of stationarity or recurrence of B_z is needed.

An A_z row sums to a_z, giving the anchor bound exactly. Prefixes of j H_z blocks have mass at most (delta a_z)^j; this holds for any starting distribution, including off-support ones, without conditioning it into stationarity.

## 3. First-w charge and the fixed start families

For a single killed B_z path, at live time l the event in f_l(nu) flags its current state only if fewer than w earlier live-path occurrences have appeared. Each of K^2 live states can be flagged at most w times. Killing cannot create further flags. Taking expectations proves sum_l f_l(nu)<=K^2 w for any fixed subprobability nu, including l=0.

Both displayed families in (4) are probability laws. For the first, summing d yields p(c); the second is delta_c tensor p. For each fixed z these families do not depend on l, j, the prefix, or mu. Dependence on z is harmless because charging is done pointwise in z before integrating. Summing the first-w bound over K starts pays K^3 w per family, not K^4 w. Zero p entries are retained with zero weight and never divided by.

Crucially, the actual prefix marginals are NOT declared fixed or independent of the suffix length. They are bounded coordinatewise by their total mass, leaving a sum over the K fixed starts. This is precisely the valid way to pay for arbitrary location-dependent prefixes.

## 4. Marked-block calculation and original-count inclusion

Differentiate each A_z in (1), replacing the marked edge by beta p. Every W is fixed in z. Dropping only the marked block's W is lawful by nonnegativity and 0<=W<=1. Keeping all other W is essential to the common contraction and is done explicitly.

Write k_z=delta a_z, and let j be the marked block index, l=r-j-1. The prefix ending at its start has mass at most a_z^e k_z^j.

For a first-edge mark, condition only in the deterministic summation sense on the prefix's second coordinate b. The marked block endpoint mass is beta a_z nu_b^first. For a second-edge mark, first push the prefix through the unmarked A_z edge; its mass becomes at most a_z^(e+1) k_z^j, and use its output-coordinate marginal c with endpoint law nu_c^second and multiplier beta. Each marginal coordinate is at most the whole prefix mass. In both cases the remaining l killed blocks supply k_z^l, yielding the common coefficient

    beta a_z^(e+1) k_z^(j+l)
      =beta a_z^(e+1) k_z^(r-1).

Thus no hidden extra r, a_z, delta, or beta factor is missing. As j varies, l takes each value 0,...,r-1 exactly once. The fixed-family first-w bounds therefore give (5).

The suffix begins at pair time e+2(j+1) and terminates exactly at M. Its counted times are e+2(j+1), e+2(j+2), ..., M-2, all original departures, and its target is the very same Y_M. Consequently J<w implies the suffix-skeleton count is <w. This remains true when l=0, where the suffix count is zero. Dropping the earlier count restriction only enlarges the path sum. The proof never removes observations from the estimator, claims empirical error decreases with count, or moves the endpoint.

For odd M the sole initial anchor mark has mass beta. The r later blocks have total mass at most k_z^r, irrespective of its resulting starting pair. Dropping F gives the additional beta k_z^r term. There is exactly one such term for e=1 and none for e=0, proving (6).

## 5. Exact integration, caps and finite cases

The paired term in (6) is 2 beta delta^(r-1) a_z^(r+e) K^3 w. Integrating with da_z=beta dz gives

    2 delta^(r-1)(1-delta^(r+e+1))/(r+e+1) K^3 w.

The anchor integrates to e delta^r(1-delta^(r+1))/(r+1). These are exactly (7). There is no need to divide by a vanishing z or beta endpoint; beta>0 and delta>=1/2 in the theorem. All integrals are of bounded finite polynomials.

For n=2r+e+1 and r>=1, the first term divided by q0 K^3w/n is at most

    (2/delta) n/(r+e+1) <=8.

If e=1, n=2(r+1), so the anchor term is at most 2q0/n; as K^3 w>=8 this is at most (1/4)q0 K^3w/n. Thus the coefficient 10 has slack. This explicitly resolves the first/second-term typo without relying on the author's intended wording.

When M=1, r=0 and q0=1, the asserted linear cap is at least 40, so the trivial probability cap proves (A+) directly without using an r-1 exponent bound. Large w is unrestricted, and all positive integer thresholds, including those above M, are valid. The independent cap P(E)<=q0 completes (A+). Adding Z_F(0)<=delta^M and separately retaining P(E0)=q0 gives (A). Nothing adds delta^M back into (A+).

## 6. Original-stack bridge and grouped successes

S020 Lemma 2 applies to arbitrary finite augmented history events with mass bounded ABOVE by q, not necessarily equal to q. Its exact augmentation attaches a posterior label kernel after generating the full original history from independent original-theta stacks. The unconditional stack marginal, deterministic-prefix maxima and tail remain unchanged. Tail integration uses min(event mass, unconditional tail), not a concentration assertion conditioned on labels or the selected row.

I checked its maximal tail against L1MAX's independent finite stacks, bounded differences on the entire L1 prefix maximum, and union over K^2 rows. S020's dyadic layers use integer threshold 2v, retain J=0, and include smoothing. The series and constants give less than 80 sqrt(q b [K+log(1/q)]) when c=b/q. Thus R002 (7) with epsilon=0 is directly applicable here, without an actual trimming operation or fresh error event. The domain q=q0 in (0,1], b>0 holds.

R004 GS is applied only to pair-success events. Its early union has stationary suffix length at least r and count coefficient K^2/(r+1). Its late dyadic groups use mass upper bounds q_v=beta v delta^h<1 and suffix denominator at least v, including the zero-length final suffix. I checked the algebra of its finite geometric sums and uniform scalar bounds: early <=114a, late <=5920a, hence GS <=6400a. S001's stationary occupation is based on finite-window charging, not an iid-row premise. No moderate-log domain is silently imposed. The R001 joint construction preserves every pair-label marginal needed by GS.

## 7. Critical constants and full-class scope

For M=K^5 and beta=log(K)/K^5, log K<K gives beta<1/K^4<=1/16, so delta>15/16. Directly,

    delta^M<=exp(-M beta)=1/K,
    q0<=delta^(-e/2) K^(-1/2)<=2 K^(-1/2),
    log(1/q0)=r[-log delta]
      <=(M/2) beta/delta <=(8/15)log K<=K.

Thus b=10q0 K^3/(M+1)<=20 K^(-5/2), and
q0 b [K+log(1/q0)]<=80/K^2. The event-stack risk is at most
80sqrt(80)/K<=720/K. The no-symbol event contributes <=1/K. GS contributes <=6400 sqrt(K^3/(K^5+1))<=6400/K. The nonnegative cover G,E,Eplus is valid even though G may overlap Eplus. Its total is <=7121/K, hence <=8000/K; the separate TV cap one is valid for the same original add-one rule.

Every new bound is uniform over theta, pi and mu, so taking the full class supremum is legitimate. The rule receives no latent labels, source table, pi, beta or initialization. Together with the accepted restricted-star Omega(1/K) lower from R002 (a subclass of this full class), this gives the stated asymptotic critical minimax and original worst-risk order. That is not an all-parameter minimax classification or an automatic blind-selector theorem.

## 8. Preserved failed routes and limitations

Section 7(a)'s obstruction is valid on the stated finite setting: integration of Ph<=delta^e h against pi forces (1-delta^e)h=0 pi-almost surely. In an irreducible finite chain Ph<=h forces h constant by propagation from a minimum. This does not constrain a genuinely substochastic H_z in the same way.

For 7(b), the first-order sticky example has the displayed stationary pair law and satisfies the two-step minorization because its first factor is at least beta/K. Before hitting a specified different symbol c, each transition avoids c with probability 1-beta/K, giving the stated avoidance law. On the critical ray the total weighted avoidance tends to one. This diagnoses an unweighted taboo route, not a counterexample to E0-weighted occupation or a risk lower.

The proof avoids the rejected typical-refresh-count conditioning and its binomial-tail remainder. It does not export an absorbing-pi potential to arbitrary pi, replace original data by iid residual rows, or infer a statistical lower from a count obstruction. The editorial term-reference nit is the only defect found; it is preserved above. Author diagnostic execution claims were not independently certified and are not needed for acceptance.

## Final disposition

**ACCEPT, with the nonblocking Section 5 term-reference correction recorded.** No substantive gap or unresolved scientific dependency for (A+)/(A)/(B) remains. The original frozen proof hash is unchanged. This report is the independent mathematical review artifact.
