# S019 独立数学审查

编排说明（非原文）：本文件是已接纳版本的完整科学正文副本，保留全部局部证明或对应独立审查推理；身份、控制记录、原提交状态及管理性来源哈希表另行省略。原件不修改。以下英文原文的年代与结论范围保持不变，本次编排不构成新的数学审查。原编号可能跳跃；完整来源与新增／删略区间见 SOURCES.md、COPY_MAP.json。

历史口径（非原文）：S016、S017 关于未获新的原规则上界、临界统计间隙的说法属于当时结果；S018 只闭合精确临界序列。S019 已进一步在 1≤M≤K⁴、0≤β≤1/2 上闭合原规则与共同 minimax 的 H 匹配，包含 S017 全部固定射线。当前综合结论以外层中文导读及该明确接纳范围为准。旧数值证书的数学结论没有被推翻。

原文内 Section 7/9 的来源身份表等管理交叉引用，统一由本包 SOURCES.md 的同名原件身份与依赖入口补足；其省略不删除被引用的科学接口。有限检查叙述是原作者／原独立审查已执行的历史事实，本次装配未重跑这些数学检查。检查脚本与运行结果在原研究记录保留，不随科学包公开；定理依据完整符号证明而非有限枚举。

原行号导航（非原文）：85–98→lem:s019-lower；100–150→lem:s019-budget；152–164→thm:s019-strip；166–179→cor:s019-rays。其 S018 原 42–48 与 236–252 行均指 thm:s018-geometric；S016 原 5–16 与 238–256 行均指 Theorem S016／prop:s016-envelope；S017 原 108–146 行指 lem:s017-round。这些原行号不冒称为本副本行号，均可用相同命名标题在本包定位。

**ACCEPTED. All four local units PASS.** The frozen proof establishes, for every integer `K>=2`, integer `1<=M<=K^4` and public `0<=beta<=1/2`,

    2^-18 H <= R_D2(K,M,beta) <= R_D2^+(K,M,beta) <= min{1,128H},
    a=min{1,sqrt(K^3/(M+1))}, delta=1-beta,
    v=delta^(M/2), H=max{a,v}.

The upper belongs to **unchanged original full-history add-one**. The constants are universal on the entire closed strip, and the exponential is the exact `(1-beta)^(M/2)`, not a uniform substitution by `exp(-beta M/2)`. The fixed S017 rays `M=ceil(K^rho), beta=gamma ln(K)/M`, with fixed `3<rho<=4, gamma>0`, consequently have matching common-minimax and original-rule order `K^(-min{rho-3,gamma}/2)`, including critical equality. Only the eventual ray thresholds may depend on rho,gamma.

This is a standard interface corollary of accepted S016/S018, with the controlled-log S017 consequence. It is material partial progress for the larger research objective, not a new source family, statistical method, full joint-rate theorem or novelty/formal-certification claim.


## Exact Experiment and Accepted-Interface Audit

The table theta is fixed, homogeneous, normalized and nonnegative on the K-symbol alphabet. Its pair kernel has only legal shifts `(a,b)->(b,c)`. Initialization mu is arbitrary. A hidden stationary probability pi satisfies `pi P=pi` and `P^2(s,t)>=beta pi(t)` for **every** pair of states. Structural zeros, sparse stationary support, reducibility and mu singular to pi remain allowed. Public beta is a lower bound, not a revealed exact source coefficient.

There are exactly M observed departures in all `M+2` observed symbols. The target is the actual terminal row `theta_(Y_M)` for the next unobserved symbol, under unconditional expected half-L1 TV at a fixed deterministic horizon. Common predictors may use the entire history, public K,M,beta and an independent seed, but no hidden source, initial/stationary law, latent labels or future. Original add-one uses every observed departure and outputs `(C_s(c)+1)/(n_s+K)` at the same terminal s. It requires only K and the history.

1. **S018 Theorem 4 (`thm:s018-geometric`), proof lines 42–48 and 236–252; review unit_004.** The exact accepted interface is, for `K>=2,M>=1,0<beta<1,0<epsilon<1`,

       R_D2^+ <= min{1,epsilon+delta^r
                     +sum_(j=1)^r beta delta^(j-1)
                         min{1,4K sqrt(B_e/(M-2j+1))}},
       r=floor(M/2), B_e=K+ln(K^2 M/epsilon).

   S019 restates every coefficient, cap, exponent and denominator correctly. The full-class source supremum and arbitrary initialization are the same. This is an original-rule theorem, not a suffix predictor theorem. In its nontrivial branch, S019 has `0<beta<=1/2<1` and chooses valid analysis tolerance epsilon=1/K. Beta zero is handled without invoking it. Reading the complete S018 proof/review confirmed that no-success, the even L=0 atom, odd final departure, all midpoints, unconditional epsilon and two separate exact-history representations are already in this accepted interface. S019 does not add a stronger conditional-stationarity or independence premise; no fresh coupling proof is needed or claimed.

2. **S016 Theorem S016 and Proposition 4 (`prop:s016-envelope`), proof lines 5–16 and 238–256; review unit_004.** Its full closed-domain conclusion is

       R_D2 >= 2^-17 max{F,delta^(M+1)g,delta^(M/2)hstar},
       i=min{1,sqrt(K/(M+1))}, g=min{1,sqrt(K^5/(M+1))},
       hstar=min{1,sqrt(K^4/(M+1))}, F=max{i,min{delta,a}}.

   S019 uses exactly this interface and retains its endpoint definitions. The underlying stronger lower is proved for each fixed common randomized predictor before taking its infimum; thus it applies to the class/algorithm quantifiers here. The source families supplying different entries are not added, revealed, or replaced by a single-source add-one example. The retained beta-zero baseline is `2^-16 g`, with g=1 on this strip.

3. **S017 Lemma 1 (`lem:s017-round`), proof lines 108–146; review unit_001.** For fixed `3<rho<=4,gamma>0`, it supplies eventual `0<beta<1/2`, the uncapped a ratio tending to one, and

       0<=-ln(1-beta)-beta<=beta^2/(2delta),
       M beta^2<=gamma^2(ln K)^2/K^rho ->0.

   S019 uses only this controlled-log and rounded-ray interface in its final consequence. The accepted S017 old-U optimization has a distinct numerical-certificate scope; it is not a lower bound on true risk and does not prohibit a better new risk certificate.



## Per-Lemma Audit

### unit_001 — Lemma 1: Finite-strip lower comparison (`lem:s019-lower`), lines 85–98

- **Statement fidelity and assumptions:** exact closed strip and accepted lower (L), with no additional source condition. The conclusion is the required universal `2^-18 H`.
- **a cap and F:** delta>=1/2 and 0<a<=1 give delta>=a/2 and a>=a/2. Hence `F>=min(delta,a)>=a/2`, including a=1. No uncapped a is silently substituted in this unit.
- **hstar cap:** `M+1<=K^4+1` and K^4>=16 imply both branches defining hstar are at least `sqrt(K^4/(K^4+1))>=sqrt(16/17)>1/2`. This remains valid at M=K^4, where hstar is slightly below one and cannot simply be replaced by one.
- **Maximum assembly:** dropping the nonnegative middle entry of (L) yields `2^-17 max(F,v hstar)>=2^-18 max(a,v)`. This is domination of scalar entries on the same class risk, not addition of hard-family losses.
- **Endpoint:** at beta=0, delta=v=H=1 and the accepted closed-domain lower applies directly. Also `M+1<=K^4+1<=K^5` proves g=1, preserving the stronger beta-zero `2^-16` baseline.
- **Adversarial boundaries:** K=2,M=16 tests the smallest hstar ratio; M=K^3-1 and M=K^3 test both sides of a=1; beta=0 and beta=1/2 test the closed endpoints. Exact cap checks and high-precision scalar probes corroborate these inequalities.
- **Contribution:** supplies both the stationary-scale and survival-scale lower throughout the strip.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Lemma 2: Uniform geometric upper budget (`lem:s019-budget`), lines 100–150

- **Statement fidelity:** local conditions `0<beta<=1/2,a<1` are explicit. Integrality gives M>=K^3>=8; this is the correct boundary, including M=K^3.
- **Tolerance and logarithm:** epsilon=1/K is in (0,1). From M<=K^4, `B_e=K+ln(K^3 M)<=K+7ln K`. The maximum of ln(x)/x is 1/e, and the displayed exponential-series lower bound e>5/2>7/3 implies B_e<=4K for every K>=2. The tolerance comparison follows exactly by squaring: epsilon<=a iff M+1<=K^5, which is true even at M=K^4. No limiting K threshold is used.
- **Inner root:** replacing B_e by 4K changes `4K sqrt(B_e/d)` to at most `8sqrt(K^3/d)`. Increasing a capped term to its uncapped root is a valid upper bound, including when the latter exceeds one.
- **Early sum:** h=floor(M/4) gives `M-2j+1>=(M+1)/2` for j<=h. Each root is at most `8sqrt(2)a`; the exact nonnegative geometric weights sum to `1-delta^h<=1`. The early bound is therefore correct.
- **Late sum and parity:** for j>h, `delta^(j-1)<=delta^h`. All denominators are distinct positive integers in 1,...,M; their final values are 1 for even M and 2 for odd M. Enlarging to the full integer set and using the decreasing-integrand comparison gives sum <=2sqrt(M). This keeps, rather than discards, the shortest stationary suffixes.
- **Late scalar budget:** multiplication gives exactly `16 beta delta^h K^(3/2)sqrt(M) =16(beta M)delta^h sqrt(K^3/M) <=16sqrt(2)a(beta M)delta^h`. With y=beta M, h>=M/4-1 and ln(delta)<=-beta give `delta^h<=exp(beta)exp(-y/4)`. The derivative maximum `max_(y>=0) y exp(-y/4)=4/e` and beta<=1/2 yield `y delta^h<=4/sqrt(e)`, hence late <=`64sqrt(2/e)a`. Every multiplicative constant is accounted for.
- **Exact no-success term:** `0<=M/2-floor(M/2)<=1/2` and delta>=1/2 imply `delta^r = v delta^(-(M/2-r))<=sqrt(2)v`. This keeps the exact power. Using an exponential inequality only for a bounded late-sum multiplier does not replace the theorem's survival term.
- **Adversarial checks:** the retained checker evaluates the actual accepted finite G sum in 455 cases across both parities, tiny/interior/endpoint beta, and cap-transition/upper-strip horizons. It also checks the late denominators for all M=1,...,2000 and large-K log-domain scalar comparisons without underflow.
- **Contribution:** establishes exactly (3) from the accepted original-rule bound, without altering the estimator or conditioning on a latent label.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Theorem 3: Bounded-strip original-rule matching (`thm:s019-strip`), lines 152–164

- **Exhaustion:** beta=0 gives v=H=1 and upper one without invoking S018 outside its domain. The a=1 branch likewise has H=1 and includes every `M+1<=K^3`, in particular M=1. The remaining branch is precisely Lemma 2's domain. There is no unhandled small horizon or empty-sum case.
- **Constants:** since a,v<=H, the upper coefficient is `C=1+8sqrt(2)+64sqrt(2/e)+sqrt(2)`. The rigorous comparisons e>2 and sqrt(2)<3/2 give `C<1+12+64+3/2=157/2<128`. This does not rely on floating-point evidence.
- **Outer cap:** combining the numerical bound with probability-vector risk <=1 gives exactly min(1,128H), not an uncapped or asymptotic statement.
- **Algorithms and quantifiers:** original add-one is one common admissible deterministic predictor, so `R_D2<=R_D2^+`. The accepted S018 bound is uniform over the entire class; the S016 lower retains every common randomized predictor. Epsilon and all split parameters remain analysis-only; the original rule receives neither beta nor a selected burn.
- **Adversarial boundary:** beta=1/2 is included in the nontrivial lemma; beta=0 is separate. The checker includes eight genuinely below-one final-budget cases so numerical corroboration is not confined to a trivial outer cap.
- **Contribution:** assembles the exact contracted finite sandwich, with constants independent of all source and public parameters.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Corollary 4: Fixed-ray consequence (`cor:s019-rays`), lines 166–179

- **Statement fidelity:** rho and gamma are fixed before taking integer K to infinity; `3<rho<=4,gamma>0`, including gamma=rho-3. Both common-minimax and original-rule orders are claimed.
- **Rounded strip inclusion:** for rho<4, the displayed threshold `K>=max{2,2^(1/(4-rho))}` gives K^rho<=K^4/2. Then `ceil(K^rho)<=K^rho+1<=K^4`, since K^4/2>=1. For rho=4, M=K^4 exactly. The argument is valid (and conservatively eventual); it does not silently replace ceil(K^rho) by K^rho.
- **Other admissibility:** accepted S017 Lemma 1 supplies eventual beta<1/2 and the exact a ratio tending to one, with a uncapped. The finite S019 theorem therefore applies eventually on each fixed ray.
- **Exact exponential conversion:** multiplying the accepted logarithmic remainder by -M/2 yields `-M beta^2/(4delta)<=ln(v K^(gamma/2))<=0`, because M beta=gamma ln K exactly. The left side tends to zero with delta eventually bounded below by 1/2. Thus the v ratio tends to one, rather than merely matching an uncontrolled exponential order.
- **Maximum and criticality:** the maximum of the two positive asymptotically equivalent power scales has the smaller decay exponent; equality of the exponents introduces no logarithm. The finite lower bounds R_D2 and hence R_D2^+, while the finite original upper bounds both from above.
- **Uniformity:** `2^-18` and 128 remain universal on the strip. Eventual conversion/admissibility thresholds may depend on fixed rho,gamma. No uniform-in-ray-threshold or full joint-parameter exponential replacement is asserted.
- **Old U:** a better true-risk certificate leaves the accepted order of the old optimized numerical U unchanged. The proof expressly preserves that distinction.
- **Contribution:** resolves the stated original-rule distinction on all fixed S017 rays, including the critical ray, as a consequence rather than a new family or route.
- **Verdict:** PASS. Repair direction: None.

## Hidden Subclaim and Assumption Audit

The four named units cover all local mathematics: lower cap comparison; finite logarithm/tolerance and early/late/no-success budget; full closed-strip assembly; and rounded-ray/logarithm conversion. The derivative, integral, parity and elementary constant calculations are explicitly proved within those units. No hidden independent lemma, source construction, target change or generated-event hypothesis is needed.

Primitive assumptions are only the frozen legal homogeneous experiment, arbitrary initialization, existential stationary witness with all-state minorization, public strip domains and information restriction. All stochastic/count facts are accepted S018 conclusions; all lower-family facts are inherited through S016. The a<1 and beta>0 conditions are exhaustive deterministic proof cases, not extra final hypotheses. No full support, irreducibility, reversibility, stationary mu, independently sampled terminal query or conditional-IID selected visits is added.

## Target Claim, Explicit Rate and Baseline Audit

- The finite result covers every admitted K,M,beta, with no hidden eventual threshold. It keeps the cap in a and exact exponent M/2 in v. Delta>=1/2 avoids zero-base conventions altogether.
- The mode stays deterministic finite horizon, unconditional expectation, actual-terminal half-L1 TV, full observed history. There is no high-probability, stopping-time, random-time, squared-TV, KL or conditional-risk substitution.
- Constants are explicit and independent of K,M,beta,source,mu,pi and predictor. Analysis epsilon=1/K is completely eliminated from the final statement and never becomes estimator input.
- S016's stronger entries, IID floor and endpoint baselines remain true. On this strip g=1 at beta zero, and its stronger `2^-16` baseline is explicitly retained. The conservative common `2^-18` packaging does not revoke that baseline.
- S018's exact-sequence `a/180<=R_D2<=R_D2^+<=min(1,128a)` remains independently available; it is not replaced by the weaker general H packaging. Other accepted stationary/fast-mixing bounds remain independent certificates.
- S017's old-U critical numerical order remains true. Its former unresolved true-risk gap can be closed by a new upper without invalidating a statement about the old expression.
- No result for M>K^4, beta>1/2, unknown-class selection/adaptation, optimal-IID original-rule risk, full joint classification, general q, finite network/codec/fault costs or literature priority is inferred.

## Notation Surface Audit

The public objects are the original class/risks/rule and a,delta,v,H with the finite sandwich. H denotes the rate, not an abbreviated data history. S016's i,g,hstar,F and S018's epsilon,B_e,r are explicitly translated accepted quantities. Proof-local h,y,C are directly defined scalar expressions and bounded in place. No helper notation hides a source condition, unknown constant, extra observation or algorithmic oracle.

## Independent Reproducible Checks


Results: **PASS**, with 7,021 exact squared-cap/integer-horizon cases; 2,000 direct late-denominator/parity horizons; 455 direct evaluations of the accepted geometric sum; and 403 scalar cases at 180-digit Decimal precision, including eight with final `128H<1`.



Exact comparisons use integers/Fraction. Direct sums use binary64 with additive tolerance `2e-12 max(1,abs(rhs))`; large scalars use 180-digit Decimal with tolerance `1e-160 max(1,abs(rhs))`. When the exact no-success logarithm is below -1000, only its log comparison is checked, rather than treating underflowed powers as evidence; those cases are not counted in the nontrivial below-one budget set. All domains, grids and exclusions are explicit in the retained script. No source simulation or reproof of S018 coupling is undertaken. These finite checks corroborate the local algebra, not infinite-parameter validity or formal verification; the verdict rests on the symbolic audit.


## Target-Step Assembly and Review Rationale

Accepted S016 gives the full-domain lower envelope; Lemma 1 compares its F and v*hstar entries to a and v with both caps preserved. Accepted S018 gives the original-rule geometric upper; Lemma 2 bounds its tolerance, every early/late-success term and exact no-success atom uniformly on the nontrivial strip. Theorem 3 supplies the omitted trivial branches, universal finite constant and common-algorithm sandwich. Corollary 4 checks rounded strip membership and uses the accepted controlled logarithm to identify the fixed-ray rates. This is a noncircular, source-faithful chain establishing exactly the binding contract.

**ACCEPTED with no retry** is the smallest justified outcome. No target, dependency, assumption, constant or algorithm assignment requires repair. The next action for this submitted unit is root consumption/gating; this review neither self-creates that gate nor claims the larger branch scientifically closed.



