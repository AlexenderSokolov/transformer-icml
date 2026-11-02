# S017 独立数学审查

编排说明（非原文）：本文件是已接纳版本的完整科学正文副本，保留全部局部证明或对应独立审查推理；身份、控制记录、原提交状态及管理性来源哈希表另行省略。原件不修改。以下英文原文的年代与结论范围保持不变，本次编排不构成新的数学审查。原编号可能跳跃；完整来源与新增／删略区间见 SOURCES.md、COPY_MAP.json。

历史口径（非原文）：S016、S017 关于未获新的原规则上界、临界统计间隙的说法属于当时结果；S018 只闭合精确临界序列。S019 已进一步在 1≤M≤K⁴、0≤β≤1/2 上闭合原规则与共同 minimax 的 H 匹配，包含 S017 全部固定射线。当前综合结论以外层中文导读及该明确接纳范围为准。旧数值证书的数学结论没有被推翻。

原文内 Section 7/9 的来源身份表等管理交叉引用，统一由本包 SOURCES.md 的同名原件身份与依赖入口补足；其省略不删除被引用的科学接口。有限检查叙述是原作者／原独立审查已执行的历史事实，本次装配未重跑这些数学检查。检查脚本与运行结果在原研究记录保留，不随科学包公开；定理依据完整符号证明而非有限枚举。

原行号导航（非原文）：审查提到原证明 188–191 行，指 lem:s017-lower 中式 (14) 后三个显式误差界，已原样保留；这些是原件行号，不是本副本行号。其余单位按同名稳定标签在 proofs/S017_complete_proof.md 定位。

**ACCEPTED. All six local units PASS.** The frozen proof establishes the bounded fixed-ray contract:

    M=ceil(K^rho), beta=gamma log(K)/M, fixed 3<rho<=4 and gamma>0:
    gamma != rho-3  =>  R_D2=Theta_(rho,gamma)(K^(-min(gamma,rho-3)/2)).

At the critical equality, it proves only the requested order of the **existing optimized numerical certificate**,

    U=Theta_rho(a sqrt(log K/log log K)),   a/180 <= R_D2 <= U,

with `a=min(1,sqrt(K^3/(M+1)))`. The proof does not infer a necessary minimax logarithmic factor from the lower bound on U. The common-predictor upper belongs to the accepted public selector, not to unchanged original full-history add-one. This is a material partial, standard derived consequence, not a full joint-rate solution.


## Exact Experiment and Accepted-Interface Audit

The homogeneous table has normalized nonnegative rows on the original K-symbol alphabet and only legal shifts `(a,b)->(b,c)`. Initialization is arbitrary. The hidden stationary witness satisfies the two-step minorization for **every** starting and target pair. Sparse stationary support, zero edges and initialization singular to that witness remain allowed. A common randomized predictor sees all M+2 observed symbols, public K,M,beta and an independent seed, not hidden source information, latent coin labels or the future. Its target is the actual terminal row, under expected half-L1 TV. S017's experiment is identical to the accepted interfaces, not a stationary-initialization or independent-query substitute.

1. **S011, Theorem S011 and Proposition 2.** Checked against the complete accepted proof/review. The quantities `i,a,g,F,u_s,u_g,h_b`, each finite certificate in S017 (3), the integer burn range `0,...,M-1`, and the sandwich `F/180<=R_D2<=U` agree exactly. The accepted suffix branch uses M-b departures and predicts at the same Y_M. Its smallest public-bound minimizer, followed by a fixed public branch tie rule, gives one common algorithm. Only U_+ is assigned to original add-one. The inherited lower applies for each common predictor before the infimum.
2. **S015, Propositions 6–7.** Checked against the complete accepted proof/review. The amplitude has the exact `q+1` denominator with `m=floor((K-1)/4)`, `L=2m`, `q=floor(M/L)`. The lower is `delta^(H_M+1) alpha/8`, not `delta^H_M alpha/8`. The extra delta is the changed-target contrast. The exact remainder count, vulnerable phases, horizon-aligned common initialization and all-source membership are as restated. The elementary count facts `0<=H_M<=M` and `H_M=M/2+M/(2m)+e_M`, `|e_M|<=L`, are genuine accepted conclusions. The full-history testing argument and hidden signs/coins remain part of that accepted interface; S017 does not substitute a marginal-mixing lower for risk.
3. **S012, Proposition 9; S015, Proposition 8.** The earlier exact ray `rho=4,gamma=1/4` retains `U/K^(-1/8) ->1` and the accepted stronger minimax liminf/limsup constants. S017 correctly derives its new rays from the finite interfaces rather than promoting the one-ray theorem to an unproved multi-parameter result. The previous stronger constants are preserved independently and are not claimed to follow from the deliberately coarser new bound 3 in Proposition 3.

The eventual ray domain meets all predecessor hypotheses: K>=13, M>=1 and 0<beta<1. The lower bounds combine by maximum for each fixed common predictor, followed by its infimum. A shared hard source for all algorithms is not asserted. S016 is neither needed nor consumed.

## Per-Lemma Audit

### unit_001 — Lemma 1: Rounded rays and uniform contraction (`lem:s017-round`)

- **Statement fidelity:** establishes eventual admissibility, the exact a scale, F=a, the generic cap for every suffix, and one uniform logarithmic error over every legal burn.
- **Ceiling/denominator:** writing `M=K^rho+zeta`, `0<=zeta<1`, gives `K^rho<=M` and `M+1<=K^rho+2`. Thus a is eventually uncapped and (6) is valid. Since i=a/K and eventually `delta>1/2>a`, F=a follows without a hidden source condition.
- **Uniform generic cap:** `ell+1<=M+1<=K^4+2<K^5` for K>=2 and rho<=4. Therefore u_g(ell)=1 for the whole legal suffix set and the original generic term; this is not merely true at a trial optimizer.
- **Logarithmic remainder:** integration gives `0<=v=-log(delta)-beta<=beta^2/(2delta)`. With `r=floor(b/2)`, the exact identity is `log h_b+beta b/2=beta(b/2-r)-rv`. Its absolute value is bounded by `beta+M beta^2/(4delta)=E_0`, uniformly in b. The identity beta M/2=B then gives (7).
- **Extreme burn/parity:** at b=M-1, `M/2-floor((M-1)/2)` is either 1/2 or 1, so the same E_0 proves (8). Both parities and b=0 are covered.
- **Vanishing errors:** beta tends to zero and `M beta^2<=gamma^2(log K)^2/K^rho` tends to zero with fixed rho,gamma. No burn-dependent o(1) is optimized illicitly.
- **Contribution:** supplies the exact rate scale and every-burn input used by all later units.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Lemma 2: Star and stationary lower scales (`lem:s017-lower`)

- **Exact floors:** `m=(K/4)(1-eta)` with `1/K<=eta<=4/K`, and `kappa=q+1-M/(2m)` lies in `(0,1]`, including exact integer M/(2m). Algebra gives `m^3/(q+1)=2m^4/(M+2m kappa)` and precisely (13); the lower and upper multiplicative bounds tend to one.
- **Amplitude:** this ratio is asymptotic to `K^(4-rho)/128`. For fixed rho<4 it eventually exceeds 16, so alpha is exactly 1/2. At rho=4 it tends to 1/128, giving `A_4=1/(64 sqrt(2))`; no residue subsequence is needed. The nonuniformity as rho approaches 4 from below is honestly retained.
- **Survival:** use the accepted exact H_M and its deterministic error only after writing `H_M+1-M/2=M/(2m)+e_M+1`. The linear error is at most `gamma log K/(2m)+beta(L+1)`, and the remainder is at most `(M+1)beta^2/(2delta)` because H_M<=M. These are exactly (14), including the extra target exponent one.
- **Error sizes:** `m>=K/8`, `L<=K/2`, `M>=K^rho` give all three displayed bounds (188–191), each tending to zero. Thus exponentiation yields a relative `1+o(1)` survival comparison, not an uncontrolled exponential-order assertion.
- **Quantifiers/constants:** eventually alpha>=A_rho/2 and survival>=K^(-gamma/2)/2, yielding A_rho/32 after division by 8. The stationary certificate is a/180. Both apply before the algorithm infimum, so their maximum is legitimate and no source-dependent constant appears.
- **Contribution:** the matching nonstationary lower below criticality and the retained stationary lower above/at it.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Proposition 3: Below-critical matching (`prop:s017-below`)

- **Public admissibility:** `epsilon=(rho-3-gamma)/2>0` gives `3+gamma+epsilon=rho-epsilon<rho`. Therefore `ell_*=floor(K^(3+gamma+epsilon))` is eventually at least one and at most M; b_*=M-ell_* is legal.
- **Denominator and absorption:** `floor(t)+1>t` yields `u_s(ell_*)<=48K^(-(gamma+epsilon)/2)`. Also ell_*/M<=K^-epsilon, so the logarithmic contraction error is at most `B K^-epsilon+E_0 ->0` and beta ell_* tends to zero.
- **Finite eventual bounds:** once that error is at most log 2 and `48K^(-epsilon/2)<=1`, the two terms total at most `3K^(-gamma/2)`. The cap only decreases the upper; u_g=1 is already uniform.
- **Algorithm/source distinction:** the trial is analysis only. The actual accepted selector minimizes public certificates using K,M,beta and needs no hidden source or extra ray-parameter oracle. It can ignore a deterministic prefix while retaining the same actual endpoint. This is not an original-add-one rate statement.
- **Matching:** Lemma 2 supplies `(A_rho/32)K^(-gamma/2)` for every common predictor, yielding the stated fixed-ray Theta rate.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Proposition 4: Above-critical matching (`prop:s017-above`)

- **Fixed fraction:** `t=(1+(rho-3)/gamma)/2` lies strictly between `(rho-3)/gamma` and one. The integer burn floor(tM) is always in 0,...,M-1; the retained suffix is positive.
- **Stationary term:** `ell_*+1>=(1-t)M+1>=(1-t)(M+1)` gives `u_s(ell_*)<=[48/sqrt(1-t)]a`, with cap harmless.
- **Floor/contraction:** `|log h_b+tB|<=E_0+beta/2` follows from the uniform burn identity and `0<=tM-floor(tM)<1`. Thus eventually h_b<=2K^(-t gamma/2).
- **Term ratio:** the exact ceiling comparison gives (19), with exponent `-(gamma-(rho-3))/4<0`. Hence h_b/a tends to zero and is eventually at most one. The upper (20) follows from a legal suffix, and the independent stationary lower is a/180.
- **Constant scope:** `1/sqrt(1-t)` and the threshold can diverge near criticality; the statement correctly fixes rho,gamma and disclaims uniformity there. Equation (6) converts a to the requested polynomial rate without dropping its M+1 denominator prematurely.
- **Verdict:** PASS. Repair direction: None.

### unit_005 — Lemma 5: Critical numerical reduction (`lem:s017-critical`)

- **Exact grid:** `x_ell=(ell+1)/(M+1)` retains every integer suffix. The identity `x_ell-ell/M=(M-ell)/(M(M+1))` is nonnegative and at most 1/M, including ell=1 and ell=M.
- **Uniform ratio:** at gamma=rho-3, `log[h/(a exp(Bx))]=epsilon_b+B(ell/M-x)+(1/2)log((M+1)/K^rho)`. Its absolute value is at most `E_0+B/M+1/K^rho ->0`; B/M=beta/2 gives exactly (23). The factors 1/2 and 2 therefore hold at one threshold for the entire legal grid.
- **Exact stationary term/cap:** `u_s=min(1,48a x^(-1/2))` is an identity, not asymptotic notation. Since every u_g=1, the finite suffix optimization becomes (22) exactly. No continuous infimum has replaced the grid.
- **Other branches:** every h_b>=h_(M-1). Equation (8) therefore uniformly bounds the original penalty below by `13K^(1/2-3gamma/8)exp(-3E_0/4)`. Critical gamma is in `(0,1]`, so the exponent is at least 1/8 and all original candidates eventually cap at one. Its generic term is also one. Pooling caps at one because beta<1/2 eventually.
- **Scope:** these are numerical values/comparisons of accepted certificates. U_+=1 is not a claim that the original estimator's true risk equals one.
- **Verdict:** PASS. Repair direction: None.

### unit_006 — Proposition 6: Critical optimized certificate (`prop:s017-opt`)

- **Scale:** `T_K=a sqrt(B/log B)` tends to zero for fixed positive gamma, since a<=K^(-gamma/2) and the remaining factor grows at most as sqrt(log K). Thus log B>=1, T_K<1 and 140T_K<1 eventually are valid deterministic thresholds.
- **Every-grid lower, small x:** if x<=log B/(2B), then the stationary term is at least `min(1,48sqrt(2)T_K)>=T_K/2`. The full candidate `min(1,u_s+h)` is at least u_s because u_s<=1. This explicitly handles the inner cap-one case.
- **Every-grid lower, large x:** otherwise (21) gives `h>=(a/2)sqrt(B)>=T_K/2`. The full candidate is at least the actual h because h is in [0,1]. Hence the lower is valid for every legal suffix, including outer-cap-one candidates, and survives finite minimization.
- **Rounded trial:** `y=log B/(4B)` lies in (0,1) eventually and My>=2. Then `ell_*=floor(My)` is a legal positive integer at most M-1. The strict inequality ell_*+1>My and `(M+1)/M<=2` give the bound `48sqrt(8)T_K` in (28).
- **Contraction at that trial:** applying (7) directly uses ell_*/M<=y and pays the exact `(M+1)/K^rho` ratio. The resulting bound is `h/a<=2B^(1/4)`. Because `sqrt(log B)/B^(1/4) ->0`, this costs at most 2T_K eventually. The explicit comparison `48sqrt(8)+2<140` is correct.
- **Caps/minimum:** the trial tends to zero and is eventually below one. Lemma 5 gives U_+=U_pool=1, so U=U_suf. No cap-one candidate can undercut T_K/2 or change the upper order.
- **Log conversion:** `log B=log log K+log(gamma/2)` and the stated fixed-parameter threshold imply (31), with constants `sqrt(gamma/3)` and `sqrt(gamma)`. At criticality these depend only on rho.
- **Essential direction check:** Proposition 6 establishes `c T_K<=U<=C T_K`, not `c T_K<=R_D2`. The only statistical lower invoked is independently a/180. The text explicitly forbids reversing R_D2<=U. Thus the requested critical statistical gap is accurately preserved.
- **Verdict:** PASS. Repair direction: None.

## Independent Adversarial Checks

Acceptance rests on the symbolic audit, not numerical experiments. Reviewer-owned inline Python commands in the tool trace, without reusing a producer checker or writing a checker file, completed successfully:

1. **1,753,524 individual legal burns** for K in `{13,17,24}`, rho in `{13/4,7/2,4}`, and gamma in `{(rho-3)/2,rho-3,2(rho-3)}`: checked the all-burn logarithmic inequality (7), u_g=1, the minimum-burn inequality (8), and the survival error (14). The horizons `ceil(K^rho)` were computed by exact integer root comparisons, so noninteger ceiling cases are included. Logarithmic checks used ordinary floating arithmetic with absolute tolerance 1e-13.
2. Among those, **584,508 critical grid instances** checked the exact grid log-error bound (23), including both parities and endpoints; no asymptotic small-K claim was assumed.
3. **8,170 exact integer/Fraction count cases**, m=3,...,40 and M=1,...,5L: directly enumerated vulnerable positions, checked exact block/remainder counts, 0<=H_M<=M and the stated count deviation.
4. **864 exact Fraction q+1 identities**, K=13,...,300 and the three rho values above: checked kappa in (0,1], the exact `2m^4/(M+2m kappa)` identity, and K/8<=m<=K/4.
5. **36 large legal trial cases**, K=`10^d` with d in `{8,20,80,200}`, the same three rho values, and below/equal/above-critical gamma: checked trial admissibility. An initial 100-digit probe was repeated at **1,100 digits** to avoid large-integer floor ambiguity. Below-critical power floors and above-critical fractional burns in this repeated check were computed with exact integer arithmetic; critical trial floors agreed with a **1,300-digit** recomputation. There were **23** successful finite upper-bound checks where the displayed eventual sufficient conditions held, and **121** critical legal-candidate lower probes. These sampled large candidates do not replace the every-grid symbolic proof and are not asserted to compute exact optimized U.



All checks passed. They are finite sanity checks, not formal certification or an infinite-parameter argument.

## Hidden Subclaim Scan

The six named units account for all load-bearing new claims: rounded admissibility/scales, all-burn contraction errors, star amplitude/survival specialization, the two off-critical admissible trials, exact critical grid/caps, and capped finite-grid optimization. Elementary integration and scalar growth comparisons are proved at their use. The assembly uses these named results and the exact accepted interfaces; no unlisted new family, new statistical method, unaccepted diagnostic, or hidden independent bridge is invoked.

## Target Claim and Explicit Rate Audit

- The only asymptotic variable is integer K. Fixed real rho lies in (3,4], fixed gamma is positive, and M,beta retain their exact ceiling/log definitions. At criticality gamma equals rho-3 exactly. Every statement is eventual, not an unsupported small-K or endpoint theorem.
- Constants and thresholds may depend only on fixed rho,gamma, or rho alone at criticality. They never depend on K, the source, stationary/initial law, signs, algorithm or seed. Explicit absorption inequalities are displayed; no source-dependent exponential constant is hidden.
- All risks remain deterministic-horizon expected actual-terminal half-L1 TV. The full-history lower quantifiers and accepted conditional-to-unconditional factor are preserved. No high-probability, stopping-time, squared-loss, predictive-KL or independent-query conversion occurs.
- The public selector is valid without knowing the fixed ray parameters separately: it uses K,M,beta and finite explicit certificates. Trial parameters are analytical witnesses only. The original/suffix/pooled algorithm assignments remain separate.
- The previously accepted rho=4,gamma=1/4 result is recovered in order and its sharper constants and ratio-one upper remain available unchanged. Other S011/S012/S015 conclusions are preserved, not replaced by this narrower theorem.
- The actual critical risk is not identified beyond the stated sandwich. No necessary logarithmic penalty, exact leading constant, uniform near-critical result, rho>4 extension, full joint formula, unknown-beta adaptation, or network/resource/fault result is asserted.

## Assumption and Notation Surface Audit

Primitive assumptions are exactly the finite legal experiment, arbitrary initialization, public parameters, all-state minorization with hidden stationary witness, and common-algorithm information restriction. The accepted star membership/count/testing conclusions are inherited derived facts. All new scalar comparisons and eventual conditions are proved in local units rather than assumed. The setting has no stable assumption IDs, so restating their actual content is the honest scaled-contract treatment.

The minimal exports are the original class/risk, fixed rays, a, and inherited U. The certificate notation keeps its S011 meaning; star parameters/count keep their S015 meaning. B,E_0,epsilon_b,x_ell,T_K,y,t,epsilon,zeta,eta,kappa,e_M are explicitly proof-local and deterministic. H_M is only the vulnerable count, not an observed history or stopping variable. No proof-local latent quantity becomes predictor input.

## Target-Step Assembly Audit and Review Rationale

Lemma 1 and Lemma 2 give exact scales and the maximum of two genuine statistical lowers. Proposition 3 matches the star lower below criticality; Proposition 4 matches the stationary lower above it. At equality, Lemma 5 reduces the unchanged numerical certificate on its exact finite grid and eliminates the other branches; Proposition 6 proves its optimized order while keeping the independently inherited risk sandwich. This is a noncircular chain proving the precise bounded contract.

**ACCEPTED with no retry** is the smallest justified outcome. There is no missing local proof, changed interface, assumption strengthening or dependency repair. The unresolved true critical rate and broader joint-rate problem are stated limitations, not silently completed claims.



