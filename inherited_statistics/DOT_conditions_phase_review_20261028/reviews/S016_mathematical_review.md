# S016 独立数学审查

编排说明（非原文）：本文件是已接纳版本的完整科学正文副本，保留全部局部证明或对应独立审查推理；身份、控制记录、原提交状态及管理性来源哈希表另行省略。原件不修改。以下英文原文的年代与结论范围保持不变，本次编排不构成新的数学审查。原编号可能跳跃；完整来源与新增／删略区间见 SOURCES.md、COPY_MAP.json。

历史口径（非原文）：S016、S017 关于未获新的原规则上界、临界统计间隙的说法属于当时结果；S018 只闭合精确临界序列。S019 已进一步在 1≤M≤K⁴、0≤β≤1/2 上闭合原规则与共同 minimax 的 H 匹配，包含 S017 全部固定射线。当前综合结论以外层中文导读及该明确接纳范围为准。旧数值证书的数学结论没有被推翻。

原文内 Section 7/9 的来源身份表等管理交叉引用，统一由本包 SOURCES.md 的同名原件身份与依赖入口补足；其省略不删除被引用的科学接口。有限检查叙述是原作者／原独立审查已执行的历史事实，本次装配未重跑这些数学检查。检查脚本与运行结果在原研究记录保留，不随科学包公开；定理依据完整符号证明而非有限枚举。

原审查与证明对应的四个单位为 lem:s016-small、lem:s016-dominance、lem:s016-absorb、prop:s016-envelope。

**ACCEPTED. All four local units PASS.** The frozen proof establishes the full-domain lower envelope

    R_D2(K,M,beta) >= 2^-17 max(F,D,T)

for every integer `K>=2,M>=1` and public `beta in [0,1]`, in the unchanged arbitrary-start, legal order-two, complete-history, actual-terminal expected-TV experiment. The new bridge pays the exact star count/phase overhead and changed-target factor. It uses the star construction only where `T>F`; everywhere else an accepted floor controls T.

The sharper inherited `F/180`, `2^-16 D`, all-beta IID floor, and exact endpoint baselines remain valid. The S011 public-selector upper U and its original/suffix/pooled assignments are retained unchanged. **No full joint matching or new original-add-one upper is accepted or asserted.**


## Exact Accepted Scope

Sources are fixed homogeneous normalized tables on the K-symbol alphabet, with only legal shifts `(a,b)->(b,c)`, arbitrary initial pair law mu, and some hidden stationary probability pi such that `P^2(s,t)>=beta pi(t)` for **every** pair of states. Zero transitions, sparse pi, reducibility and mu singular to pi are permitted. Beta is a shared public lower bound, not the source's hidden exact coefficient.

Every common randomized predictor may use the entire `M+2`-symbol history, public `K,M,beta` and an independent seed, but no hidden source parameters, signs, stationary witness, phase/refresh labels or future symbols. The target is the actual terminal row and the loss remains unconditional expected half-L1 TV at a fixed deterministic horizon.

Use the proof's exact definitions

    n=M+1, delta=1-beta,
    i=min(1,sqrt(K/n)), a=min(1,sqrt(K^3/n)),
    g=min(1,sqrt(K^5/n)), hstar=min(1,sqrt(K^4/n)),
    F=max(i,min(delta,a)), D=delta^n g, T=delta^(M/2) hstar.

At beta zero set `D=g,T=hstar`; at beta one set `D=T=0`. For every fixed common predictor B, the accepted stronger assembly is

    sup_((theta,mu) in D_K(2,beta)) L_B(theta,mu)
       >= max(F/180, 2^-16 D, 2^-17 T)
       >= 2^-17 max(F,D,T).

Taking the infimum over B gives the target. This also lower-bounds each fixed algorithm's worst risk, but does not create an upper bound for that algorithm.



## Per-Lemma Audit

### unit_001 — Lemma 1: Endpoint and small-parameter coverage (`lem:s016-small`)

- **Statement fidelity:** covers both beta endpoints, M=1 and every excluded small alphabet without narrowing the theorem.
- **Caps:** `i<=a<=hstar<=g<=1` follows from monotonicity of the same cap. At beta zero, F=a and `max(F,D,T)=g`; the accepted `2^-16 g` baseline is stronger and explicitly retained. At beta one, D=T=0 and F=i; all exponents are positive, so no `0^0` convention or null-event conditioning occurs.
- **M=1:** n=2 and K>=2 imply i=F=1. This is handled before any use of `delta^(M/2)<=delta`; the latter would be false in general when M=1.
- **Small K:** with `x=sqrt(K/n)`, both branches of `min(1,K^2 x)<=K^2 min(1,x)` hold. Therefore `hstar<=g<=144i`. The exact comparison `144*32sqrt(6)<144*32*3=13824<65536` makes the accepted IID floor strictly larger than `2^-16 g`, hence sufficient for T.
- **Dependency direction and information:** the S006 stationary IID witnesses are valid members of the arbitrary-mu class for every beta. They keep all M+2 informative symbols. No larger-class lower is restricted in the invalid direction, and no data are removed from a lower experiment.
- **Assembly:** the small-case T bound and inherited F,D bounds concern the same predictor supremum and combine by maximum, not by summing risks.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Lemma 2: Dominance forces slow hazard (`lem:s016-dominance`)

- **Statement fidelity:** the local domain `K>=13,M>=2,0<beta<1,T>F` is explicit. T>F is a deterministic case condition, not a new theorem hypothesis or generated event.
- **Dominance:** if delta<a, then `delta^(M/2)<=delta` and hstar<=1 give `T<=delta<=max(i,delta)=F`, a contradiction. Thus delta>=a; since i<=a, F=a. As delta<1, a<1 and `n>K^3`; integer n=M+1 gives **M>=K^3**, including equality.
- **Both hstar caps:** for n<=K^4, `hstar/a=sqrt(n/K^3)<=sqrt(K)`; for n>=K^4, the ratio is exactly sqrt(K). Equality at n=K^4 is consistent and no division by zero occurs.
- **Exact logarithm:** T>a yields `delta^(M/2)>a/hstar>=K^-1/2`. Monotonicity of log, its positive argument and division by M/2 give `-log(delta)<log(K)/M` with the correct sign. No approximation of log by beta is used.
- **Contribution:** supplies precisely the finite hazard and horizon control needed to pay the star phase error, without modifying its exponent.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Lemma 3: Finite star phase-penalty absorption (`lem:s016-absorb`)

- **Accepted interface:** S015 Propositions 6–7 supply a lawful family with a common sign-independent horizon-aligned initial law and, for every B, `sup_D L_B>=delta^(H_M+1) alpha/8`, `|H_M-M(m+1)/L|<=L`, and `alpha/8>=2^-12 hstar`. Their finite domain is satisfied here. Full-history testing and the changed target already contribute the exact additional factor delta.
- **Count and floor bounds:** L=2m gives `H_M+1<=M/2+M/(2m)+L+1`. Writing K-1=4m+e with 0<=e<=3 proves m>=K/8 and L<=K/2 on this domain, including K=13,m=3,L=6.
- **Exponent direction:** since 0<delta<1, the upper bound on H_M+1 produces a **lower** bound on its power. With lambda=-log(delta)>0, the factor removed from `delta^(M/2)` is exactly `exp[-lambda(M/(2m)+L+1)]`. Both the phase error and changed-target +1 are retained.
- **Finite absorption:** Lemma 2 and nonnegative factors give

      lambda(M/(2m)+L+1)
         < log(K)/(2m)+(L+1)log(K)/M
         <= 4log(K)/K+(K/2+1)log(K)/K^3.

  Thus no finite count error is discarded inside an exponential.
- **Uniform constant:** the derivative of x/2-log(x) is nonnegative for x>=2, and `log(2)<1` follows from the displayed integral. Hence the last expression is at most `2+1/(4K)+1/(2K^2)<=9/4<3`. The proof of e<3 by the factorial/geometric-series comparison is strict and valid; therefore `e^3<27<32` and `exp(-3)>1/32`.
- **Amplitude:** S015's q=0 and q>=1 arguments preserve both amplitude branches and both hstar caps. Its exact constant 2^-12 times the new factor greater than 2^-5 gives `sup_D L_B>2^-17 T`. No family-only upper or S015 asymptotic result is used.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Proposition 4: All-parameter maximum assembly (`prop:s016-envelope`)

- **Exhaustion:** Lemma 1 covers beta endpoints, M=1 and K<=12. On the remaining domain, T<=F is controlled by F/180, while T>F invokes Lemmas 2–3. Equality T=F is explicitly in the first branch.
- **Same universal predictor:** public K,M,beta are fixed first. Every bound is on the supremum for that same arbitrary common randomized B. Different witness families may be used for the different terms, but their risks are not added and no single source is claimed hard for every predictor.
- **Supremum/infimum:** each class supremum dominates each valid finite-prior average. Taking a maximum of scalar lower bounds is legitimate even if the maximizing sources differ. The right side is independent of B, so the subsequent algorithm infimum preserves it. No exchange of infimum and source supremum is performed.
- **Constants:** 1/180 and 2^-16 are both at least 2^-17. This gives exactly the target constant, with the stronger displayed maximum retained.
- **Contribution:** closes the full closed parameter domain without a new assumption, hidden-source advice, new algorithm or additional mathematical route.
- **Verdict:** PASS. Repair direction: None.

## Independent Adversarial Checks

Acceptance rests on the symbolic audit above. A reviewer-owned inline Python command, not a reused producer checker, exited successfully with `ALL PASS`. No checker file was written.

1. **18,212 exact count cases:** m=3,...,60, all residues d=0,...,2m-1, and q in `{0,1,2,17,100000}`, excluding M=0. Exact rational arithmetic checked the count-error and full H_M+1 overhead inequalities. In **10,904** q<=2 cases, direct enumeration of every scheduled phase independently matched H_M and the terminal phase 2.
2. **7,320 exact squared-amplitude checks:** K=13,...,500 and fifteen small/clock/cap-boundary/polynomial horizons. Squared nonnegative quantities and `Fraction` arithmetic checked `alpha/8>=2^-12 hstar` with both caps, and the floor bounds were checked exactly.
3. **28,056 scalar probes:** K=2,...,100 plus 127,256,1000, with small/clock and K^3/K^4/K^5 boundary horizons and fourteen endpoint/interior hazard choices. Checked endpoint identities, M=1, and the full combined lower certificate against `2^-17 max(F,D,T)`. Stable exponents used lambda directly rather than forming a tiny beta by subtraction.
4. **3,276 strict T>F cases** within those probes checked delta>=a, a<1, M>=K^3, both hstar ratios, exact log control, the sign of the count-to-power comparison, and the final star/T constant. The largest sampled overhead was approximately 0.461932; this observation is not used instead of the uniform analytic bound.
5. **159 small-K cap cases** checked the IID comparison independently. Numeric scalar comparisons allowed relative tolerances at most 1e-13; strict dominance probes used a 1e-12 separation from the boundary. Exact count/amplitude checks did not use floating arithmetic.

These finite checks corroborate but do not establish the infinite-parameter theorem and are not formal certification.

## Hidden Subclaim and Assumption Audit

The four named units account for all new mathematics: boundary coverage, dominance/logarithm control, phase-error absorption, and per-algorithm maximum assembly. Floor comparisons, cap branches, integer horizon conversion and the elementary exponential constant are proved within the named units. There is no missing independent load-bearing subclaim.

Primitive assumptions are exactly the fixed legal-shift experiment, normalized homogeneous table, public domains, arbitrary initialization, hidden stationary witness, all-state minorization and information restriction. Membership, conditional laws, count formulas and amplitude bounds are accepted derived S015 conclusions. The local T>F case is discharged within an exhaustive deterministic split. No stationarity of mu, full support, irreducibility, reversibility, observed phase/coin labels or selected-row IID assumption is introduced.

## Target Claim, Explicit Rate and Baseline Audit

- Every integer K>=2,M>=1 and every beta in [0,1] is covered. Exponents n and M/2 are strictly positive; beta endpoints are direct definitions, not limits.
- The norm, expectation, actual terminal query, complete history and deterministic horizon do not change. There is no high-probability, random-time, independent-query, squared-TV, predictive-KL or stopping-time replacement.
- All constants are explicit and independent of K,M,beta,source,mu,pi,signs and predictor. The inherited constants are correctly attributed; the new 2^-5 loss is justified by the exact finite exponential comparison.
- The stronger all-beta IID floor is retained. At beta zero the original `2^-16 g` lower and unchanged-original `u_g(M)<=48g` upper remain true. At beta one the positive IID floor and pooled upper at most i remain true. Conservative common packaging does not replace these inherited theorem-facing baselines.
- The new uniform statement is a standard derived envelope from accepted results. It does not independently solve the remaining joint minimax problem or establish a literature-priority claim.

## Retained Upper and Algorithm Audit

Compared S016 Section 7 directly with S011's definitions and complete envelope proof. The formulas for u_s, u_g, endpoint-safe h_b, U_+, U_suf, U_pool and U agree, including each cap, exponent, burn range and coefficient 48/13. The burn set remains nonempty at M=1 and every retained suffix has at least one departure.

Only U_+ is assigned to the unchanged full-history add-one rule. Its optimization over b is an optimization of bounds, not a change to its counts. U_suf belongs to the separate suffix rule using the smallest public minimizer; U_pool belongs to empirical pooling. The selector uses public certificates with the fixed original/suffix/pooled tie order, not source-dependent true risk. No restricted-family upper is promoted to a full-class upper. The beta-zero identity U=u_g(M) and beta-one pooled statement are preserved. No global lower/upper matching is inferred.

## Notation Surface Audit

The public objects are the class/risk, i,a,g,hstar,F,D,T and the separately inherited algorithm-labelled U certificates. The star integers m,L,q,d,k, the phase set, r_M,H_M and alpha are explicitly translated proof-local accepted objects. Lambda=-log(delta), the temporary cap variable x and the real-variable function f are locally defined algebra. hstar is distinct from the burn factor h_b and exact count H_M; H remains the data history. None of these proof-local objects grants hidden information to an algorithm.

## Target-Step Assembly Audit and Review Rationale

Accepted S012 supplies F and D throughout the domain. Lemma 1 provides all boundary/small-case T control. In the remaining domain, either the existing F floor dominates T or Lemma 2 supplies exactly the finite conditions needed by Lemma 3. Lemma 3 applies the accepted full-data S015 lower without dropping its count error or changed target. Proposition 4 combines the bounds on each fixed predictor's class supremum and only then takes the infimum. S011's separate upper is inherited unchanged.

This noncircular chain proves the exact bounded contract without changing any assumption, interface, target, constant or algorithm quantifier. **ACCEPTED with no retry** is the smallest justified outcome. The unresolved global matching and original-add-one upper questions are outside the assigned conclusion, not hidden defects or purportedly completed work.



