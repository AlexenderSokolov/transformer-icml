# S018 独立数学审查

编排说明（非原文）：本文件是已接纳版本的完整科学正文副本，保留全部局部证明或对应独立审查推理；身份、控制记录、原提交状态及管理性来源哈希表另行省略。原件不修改。以下英文原文的年代与结论范围保持不变，本次编排不构成新的数学审查。原编号可能跳跃；完整来源与新增／删略区间见 SOURCES.md、COPY_MAP.json。

历史口径（非原文）：S016、S017 关于未获新的原规则上界、临界统计间隙的说法属于当时结果；S018 只闭合精确临界序列。S019 已进一步在 1≤M≤K⁴、0≤β≤1/2 上闭合原规则与共同 minimax 的 H 匹配，包含 S017 全部固定射线。当前综合结论以外层中文导读及该明确接纳范围为准。旧数值证书的数学结论没有被推翻。

原文内 Section 7/9 的来源身份表等管理交叉引用，统一由本包 SOURCES.md 的同名原件身份与依赖入口补足；其省略不删除被引用的科学接口。有限检查叙述是原作者／原独立审查已执行的历史事实，本次装配未重跑这些数学检查。检查脚本与运行结果在原研究记录保留，不随科学包公开；定理依据完整符号证明而非有限枚举。

原行号导航（非原文）：本审查每个单位标题中的 lines 均为原证明行号。87–149→lem:s018-stack；151–206→lem:s018-split；208–234→lem:s018-moment；236–252→thm:s018-geometric；254–325→thm:s018-critical。S004 原 153–177 行对应 lem:s004-stacks；S001 原 70–115 行对应其 Section 3 平稳占用；S011 原 15–190 行对应定义及 prop:s011-envelope。这些命名正文在嵌套早期科学归档中，不要求读私有文件。

**ACCEPTED. All five local units PASS.** The frozen proof establishes the finite geometric bound for the **unchanged original full-history add-one rule**, and at exactly `M=K^4, beta=ln(K)/K^4` establishes, for every integer `K>=2`,

    a/180 <= R_D2 <= R_D2^+ <= min{1,128a},
    a=sqrt(K^3/(K^4+1)).

The critical upper is an actual original-rule risk certificate, not merely an optimized old suffix certificate. Its validity does not require independence between the row-stack event and regeneration labels. The accepted S017 order of the OLD numerical certificate remains unchanged. This is a material partial resolution of the exact contracted critical sequence, not a full joint-rate theorem, general-ray classification, formal verification or novelty certification.


## Exact Accepted Scope

Fix integers `K>=2,M>=1`, public `0<beta<1`, an arbitrary initial pair law mu, and one fixed normalized nonnegative homogeneous order-two table theta. Its legal pair kernel is `P((a,b),(b,c))=theta_ab(c)` with structural zeros elsewhere. Some hidden probability pi satisfies `pi P=pi` and `P^2(s,z)>=beta pi(z)` for **every** starting and destination pair. Sparse pi, zero transitions and initialization singular to pi are allowed.

Every `M+2` observed symbol is retained. There are exactly M observed departures, and the target is the actual terminal row `theta_(Y_M)`. Loss is expected half-L1 TV. The original estimator uses all M departure counts and the displayed add-one formula. It does not receive theta, mu, pi, split labels, a residual kernel, a selected burn or future data.

For each analysis tolerance `0<epsilon<1`, write `delta=1-beta`, `r=floor(M/2)` and `B_e=K+ln(K^2 M/epsilon)`. The accepted finite conclusion is exactly

    R_D2^+ <= min{1, epsilon+delta^r
                   +sum_(j=1)^r beta delta^(j-1)
                       min{1,4K sqrt(B_e/(M-2j+1))}}.

At the exact critical parameters, epsilon=1/K yields the displayed all-K sandwich with constants 1/180 and 128. The lower applies to every common possibly randomized full-history predictor using the public parameters and an independent seed. No lower is inferred from one source's add-one loss or from state-law mixing.

## Accepted-Interface Audit

1. **S004 Lemma 2, Arbitrary-start finite stacks (`lem:s004-stacks`), proof lines 153–177; review unit_002.** The initial law is arbitrary and independent of independent length-2M row stacks of the same fixed theta. Consuming the next stack symbol reproduces the entire original symbol history and gives `C_s-n_s theta_s=S_(s,n_s)` pathwise. S018 uses precisely this interface, not S004's Holder/floor bound or a stationary conditional-IID assertion. Deterministic prefixes through M exist.
2. **S001 Section 3, stationary occupancy, proof lines 70–115; review units_001–002.** For every stationary pi of the same legal source, deterministic integer length L>=1 and integer w>=1, its actual endpoint count obeys `P_pi(J_L<w)<=min(1,K^2w/(L+1))`. Its deterministic finite-window argument uses block stationarity only; no positive mass, recurrence, irreducibility or mixing hypothesis is hidden. S018's first-success suffix has exactly that law. The L=0 case is supplied locally rather than imported.
3. **S011 Theorem S011 and Proposition 2 (`prop:s011-envelope`), proof lines 15–190; review unit_002.** Its experiment, full observation, public-beta information restriction and arbitrary-mu class agree exactly. The accepted lower is `R_D2>=F/180`, `F=max(i,min(1-beta,a_0))`, `i=min(1,sqrt(K/(M+1)))`, `a_0=min(1,sqrt(K^3/(M+1)))`. The stationary subclass inclusion is made for every common predictor before taking its infimum. Fixing public beta does not disclose a hidden source. S018 proves the finite identity F=a on the required sequence instead of assuming it asymptotically.



Earlier S006/S002 hard-family and Euler L1MAX/GU predecessors are inherited through these exact accepted interfaces, not freshly reaudited here. No external literature result is needed by this local proof.

## Per-Lemma Audit

### unit_001 — Lemma 1: Unconditional simultaneous original-stack control (`lem:s018-stack`), lines 87–149

- **Statement fidelity:** every legal homogeneous theta, arbitrary mu, all admitted K,M and epsilon; minorization is not used. The conclusion concerns the original actual-terminal loss and count.
- **Full-history realization:** a prescribed symbol prefix fixes exactly the initial pair and consumed stack prefixes. Their product equals the original path probability, including zeros. Unused deterministic prefixes remain product-distributed; at most M symbols per row are consumed.
- **MGF:** the finite log-MGF has second derivative equal to tilted variance. Every tilted law stays in the same interval; variance is at most the squared half-range. Integrating from zero gives `exp(lambda^2 d^2/8)`. A sign coordinate has range at most two, so the n-summand exponent is `n lambda^2/2`; lambda=t/n gives the stated tail. The constant-row and t=0 cases introduce no division by variance.
- **Uniform event:** `||v||_1=max_u <u,v>` for the `2^K` sign vectors. Union over all K^2 rows and all deterministic n=1,...,M gives `K^2 M 2^K exp(-B_e)=epsilon exp(K(ln2-1))<=epsilon`. This probability is unconditional. The event is simultaneous before terminal-row/count selection.
- **TV and smoothing:** `||S||_1/(2n)<=sqrt(B_e/(2n))<=sqrt(B_e/(n+1))` for n>=1. The exact add-one mixture costs at most `K/(n+K)`. Squaring the claimed comparison reduces to `(n+K)^2-K(n+1)=n^2+Kn+K^2-K>=0`. Since B_e>=K, the two terms give `2sqrt(B_e/(n+1))`; the probability-vector cap gives f. At n=0 the empirical row is not formed and f(0)=1 bounds the loss.
- **Expectation bridge:** `E loss<=E[f(J)1_E]+P(E^c)<=E f(J)+epsilon` uses no independence. In particular neither epsilon nor the event is conditioned on a terminal row, realized count, first-success label or observed midpoint.
- **Adversarial checks:** independent multinomial-prefix checks cover nonuniform and zero-coordinate row laws and larger deterministic counts; these supplement the symbolic all-row union, not a selected-row conditioning argument.
- **Contribution:** establishes an original-law scalar loss/count bridge, replacing the old 3/4-power floor treatment without modifying the algorithm.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Lemma 2: Exact full-history pair splitting (`lem:s018-split`), lines 151–206

- **Statement fidelity:** the same theta, arbitrary mu, all-state two-step minorization and interior beta; r=floor(M/2). The suffix claim is conditional only on the first-success label.
- **Residual and legal path:** Q_2 is nonnegative by the all-state hypothesis and has row sum one because delta>0. It is a two-step pair kernel, not a one-symbol table. From `(a,b)` to `(c,d)` the only legal two-departure route is `(a,b)->(b,c)->(c,d)`. The success/failure mixture gives exactly `theta_ab(c)theta_bc(d)` and appends BOTH c and d.
- **Zeros/off-support states:** if this product vanishes, both nonnegative mixture masses vanish. No division by P^2 or pi is used. All-state minorization ensures the construction remains defined from an initial pair outside stationary support. The only residual denominator is delta>0.
- **Full law and parity:** multiplying block factors and, for odd M, the final ordinary one-step factor recovers every complete original history probability. Matching only the even skeleton would be insufficient, but the proof explicitly reconstructs each unique midpoint. Conditional on all labels the one-step law need not be P; the proof correctly uses only the unconditional full-history identity.
- **First-success identity (3.6):** the first j-1 failure labels contribute delta^(j-1); their normalized residual prefix has total mass one. At block j its endpoint is sampled from pi independently of the pre-block state. The intervening midpoint is summed as part of an unrestricted prefix, not held fixed. All later labels are unconstrained and integrate to ordinary blocks; the odd final step is ordinary. Thus the exact joint law is `beta delta^(j-1) pi(z_0) product P(z_l,z_(l+1))`. Dividing only by the positive label probability is legitimate.
- **Conditioning trap:** observing midpoint `(b,c)` reveals the first coordinate c of the successful endpoint. Hence the suffix generally is NOT stationary after conditioning on that midpoint or full prefix. S018 expressly forbids that stronger statement and never uses it. The independent checker includes a nonuniform pi whose coordinate-conditioned law differs from pi.
- **Count transfer:** full and suffix counts use the SAME Y_M, and the suffix index set is literally contained in the full departure set. Thus J>=J_suffix on every path; decreasing f gives the correct direction. No assertion that actual empirical loss itself decreases on adding prefix data is made. No-success contributes at most delta^r, including r=0.
- **Adversarial checks:** exact full-symbol-history and first-success suffix-law checks include genuine non-IID ternary tables, nonuniform stationary laws, singular starts, sparse pi, maximal admissible beta creating residual zeros, M=1, both parities and L=0.
- **Contribution:** supplies the geometric stationary-count mixture while preserving every original observation and the fixed source.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Lemma 3: Stationary capped negative moment (`lem:s018-moment`), lines 208–234

- **Statement fidelity:** stationary ordinary P path, every integer L>=0 and B_e>=K; J_L is its actual terminal count.
- **Exact integer conversion:** for 0<t<1, set x=4B_e/t^2. Then `f(J)>t` iff `J+1<x`, equivalently `J<ceil(x)-1`. At integral x the cutoff is x-1; at nonintegral x it is floor(x). The chosen integer w is positive and strictly less than x because x>4B_e>=8. Applying S001 at this w gives (3.8); no real-threshold occupancy theorem is presumed.
- **Layer cake:** on the finite path space, integrating the indicator for t<f(J) gives f(J) pointwise and finite-sum interchange is legitimate. The integral of `min(1,z/t^2)` is 1 for z>=1 and `2sqrt(z)-z` otherwise. It is both <=1 and <=2sqrt(z); z=4B_e K^2/(L+1) yields the exact coefficient 4K.
- **Zero length:** J_0=0, f(0)=1, and the displayed right-hand cap is also one. This separately proves the even-final-success atom without invoking S001 outside its domain.
- **Adversarial checks:** 11,700 exact rational threshold comparisons include exact and nonintegral x. Additional lower-tail-saturating occupation distributions test the moment bound in 16 genuinely nontrivial below-one-cap cases, unlike tiny path tests where this cap is often automatically one.
- **Contribution:** bounds each stationary suffix expectation without conditioning on its terminal row/count or assigning IID status to selected visits.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Theorem 4: Finite original-rule geometric bound (`thm:s018-geometric`), lines 236–252

- **Separate spaces:** Lemma 1 first exports an inequality between expectations of functions of the ORIGINAL full history. Lemma 2 bounds the scalar original-law expectation E f(J) using a different exact-history realization. Equal complete-history pushforward laws are sufficient; there is no joint law or independence assumption about the two auxiliary constructions.
- **Integration:** Lemma 3 is instantiated at exactly L=M-2j, including zero. First-success weights are nonnegative with total 1-delta^r. No-success and every short-suffix atom remain present; epsilon is paid once, not rescaled by any success probability.
- **Supremum/admissibility:** the expression is uniform over theta, mu and every witnessing pi and contains only public deterministic parameters and epsilon. Taking the source supremum preserves it. The cap follows from loss<=1. Original add-one is an admissible common deterministic predictor, giving `R_D2<=R_D2^+` in the correct direction.
- **M=1:** r=0, the sum is empty and delta^0=1 with delta>0, giving the trivial but valid cap one. No unregenerated stationary suffix is silently inserted.
- **Contribution:** proves exactly the contracted finite original-rule bound, not a suffix-rule guarantee relabeled as full-history risk.
- **Verdict:** PASS. Repair direction: None.

### unit_005 — Theorem 5: All-K critical matching (`thm:s018-critical`), lines 254–325

- **Domains and B_e:** `ln K<K` yields `0<beta<K^-3<=1/8`. M>=16 and a<1. The choice epsilon=1/K lies in (0,1), and B_e=K+7ln K. The maximum ln(x)/x=1/e plus e>5/2>7/3 proves B_e<=4K for every K>=2, not just asymptotically.
- **Early labels:** j<=h=floor(M/4) implies `M-2j+1>=(M+1)/2`. The uncapped root branch is <=8sqrt(2)a, and the early geometric weights sum to <=1.
- **Late labels:** j>h implies delta^(j-1)<=delta^h. Denominators are distinct positive integers and end at 1 for even M or 2 for odd M. Enlarging them to 1,...,M gives sum <=2sqrt M; using the uncapped root branch is a valid upper even for the shortest suffix. The exact multiplication gives `16(ln K)delta^h sqrt(K^3/M)<=16sqrt(2)a(ln K)delta^h`.
- **Late exponent:** h>=M/4-1 gives delta^h<=exp(beta)K^-1/4. The scalar maximum `max_(y>=0) y exp(-y/4)=4/e` and beta<1 imply `(ln K)delta^h<=4`. Thus the late contribution is <=64sqrt(2)a. No uniformly long suffix is assigned to late labels.
- **No-success and tolerance:** r>=M/2-1/2 gives delta^r<=exp(beta/2)K^-1/2<2K^-1/2. Since `2K^-1/2/a=2sqrt(1+K^-4)<=sqrt(17)/2<3`, this is <3a. Also epsilon<=a is exactly `K^4+1<=K^5` after squaring, valid for all K>=2.
- **Total constant:** `1+3+8sqrt(2)+64sqrt(2)=4+72sqrt(2)<128`. Every absorbed term has a displayed finite inequality; small K is covered by the outer cap without a hidden threshold or constant correction.
- **Lower and information:** delta>7/8>a, and i=a/K<=a, with both square-root rates uncapped. Hence S011's exact F equals a for every K>=2. Its lower therefore gives a/180 under the same common full-history algorithm quantifier. No new family or source-dependent algorithm is introduced.
- **Adversarial checks:** finite parity sums for M=1,...,1000 and 180-digit scalar checks for 1,026 K values (including powers up to 10^30) passed. These do not replace the symbolic all-K inequalities.
- **Contribution:** closes the exact assigned critical statistical gap for both common minimax risk and unchanged original add-one worst risk.
- **Verdict:** PASS. Repair direction: None.

## Hidden Subclaim, Assumption and Notation Audit

The five units account for every independent mathematical bridge: full-history stacks; finite interval MGF and sign union; selected-row smoothing/zero-count handling; stochastic residual; unique legal midpoint/full-law identity; first-success conditional suffix law; pathwise count comparison; integer-tail conversion and integration; separate-space expectation transfer; finite critical constants and exact lower specialization. The local map and named statements match the proofs. No additional nontrivial missing lemma is hidden in assembly prose.

Primitive assumptions are exactly the finite fixed homogeneous legal experiment, public parameter domains, arbitrary initialization, existential stationary witness with all-state two-step minorization, full observations, actual-terminal expected TV and common-predictor information restriction. The good event, regenerative suffix, residual stochasticity, count inequality and moment bound are derived, not smuggled into the theorem as conditions. No reversibility, full support, lower stationary mass or conditional visit independence is added.

The classes, risks, original rule and two theorem conclusions are public-facing. B_e, epsilon, f, E, signs, stacks, Q_2, labels, tau, suffix counts and h are explicitly proof-local and derived from stated data/parameters. Epsilon is an analysis tolerance, not an estimator input. B_e is explicitly distinguished from the general predictor B. Helper notation does not hide a constant, extra observation or assumption.

## Explicit Rate and Baseline Audit

- The finite result exposes K,M,beta,epsilon and keeps both the no-success atom and the complete geometric short-suffix sum. All constants are absolute and independent of source, initialization, stationary law and estimator.
- The final risk is deterministic-finite-horizon expected half-L1 TV. The high-probability stack event is only an internal tool with its failure probability paid unconditionally. There is no high-probability, conditional-risk, all-time or stopping-time upgrade.
- The logarithm `ln(K^2 M/epsilon)` is not dropped generally. Only on the exact prescribed sequence does epsilon=1/K yield B_e<=4K and remove a logarithmic rate loss.
- S001's stationary upper and existing fast-mixing results remain available independently; the new geometric bound can be conservative there. S018 explicitly does not replace S001's sharper constant or claim optimality near beta one.
- The q=2, beta endpoints are not expanded: this theorem requires 0<beta<1, so Q_2 never divides by zero. The accepted beta-zero and beta-one results are left intact.
- S013's sharp state-TV envelope is respected: the no-success term is exactly delta^floor(M/2), not a falsely faster delta^M. No statistical lower is inferred from state-TV.
- S014's canonical SYMBOL refresh produces `(old_second,new_symbol)` and need not give pi. S018 instead analytically samples a whole pair at a TWO-STEP endpoint, retains the dependent midpoint, and conditions only on the first-success label. The two mechanisms are not identified.
- S015's harmless symbol refreshes and weighted aggregate counterexample remain valid. At its different beta=ln(K)/(4K^4) sequence, the new formula retains a no-pair-success term of order K^-1/8. It does not imply either refuted canonical-refresh or delta^M total bound.
- S017's old optimized U remains of its accepted critical order; its lower bound on a numerical certificate is not a lower bound on true risk. S018 supplies a new, smaller certificate on only the exact contracted sequence and makes no general-ray or full-joint-rate extension.

## Independent Reproducible Checks

The reviewer wrote a new checker without reading, copying, importing or executing the producer checker.




The checker solves exact rational stationary equations for three explicitly recorded non-IID tables: binary nonuniform stationary, ternary full support, and ternary with sparse stationary support. Each is tested at one-third of its exact maximal two-step coefficient and at that maximal coefficient, exercising zero residual entries. Initial laws are a point mass (singular to pi for the sparse example) and a nonuniform full-support law. Binary horizons are 1,...,8; full-support ternary horizons 1,...,5; sparse ternary horizons 1,...,6.

Unlike a reused trajectory simulator, it expands independent label patterns over complete symbol histories using success mass beta*pi(z) and residual mass P^2(s,z)-beta*pi(z), then compares exact complete-history and suffix dictionaries against directly multiplied ordinary one-step laws. Globally checked residual nonnegativity/normalization also covers zero original-history mass.

Results, all PASS:

- **76** full-history experiments, **14,880** positive ordinary histories, **93,530** positive augmented atoms.
- **124** complete first-success stationary suffix-law identities and **79,814** same-endpoint pathwise count comparisons.
- One explicit coordinate-conditioned stationary-law calculation showing why observed midpoint conditioning cannot be added.
- **11,700** exact rational threshold comparisons.
- **24** deterministic multinomial row-tail checks, including zero-coordinate rows and n up to 97.
- **24** lower-tail-saturating occupation-distribution moment checks, of which **16** have a bound strictly below one. For example K=2,L=1000,B=2 gives expectation about 0.324004 versus bound 0.357592; K=2,L=10000,B=2 gives about 0.109745 versus 0.113131.
- **1,000** finite parity/denominator-sum checks.
- **1,026** critical scalar probes at 180-digit Decimal precision, K=2,...,1000 and powers 10^4,...,10^30.



Path, stationarity, coefficient, count and threshold checks use exact Fraction arithmetic. Multinomial-tail, moment and parity comparisons use floating point with stated small tolerances; the critical scalar probes use 180-digit Decimal arithmetic. Tiny path enumeration is not presented as testing the nontrivial large-horizon moment regime; that receives a separate adversarial distribution check. None establishes infinite-parameter validity or formal verification. Acceptance rests on the symbolic review above.


## Target-Step Assembly and Review Rationale

1. Accepted S004 stacks plus Lemma 1's local deterministic-prefix analysis give `E_original loss<=epsilon+E_original f(J)`.
2. Lemma 2 supplies the exact-law first-success mixture for that SAME scalar original-law expectation using all-state minorization and the unique legal midpoint.
3. Accepted S001 occupancy plus Lemma 3 bounds each ordinary stationary suffix count, including local L=0 handling.
4. Theorem 4 composes these distributional bounds, preserves every weight/atom, caps by one, and takes the source supremum for the unchanged original rule.
5. Theorem 5 supplies every finite critical specialization inequality and combines the upper with the exact accepted S011 lower through F=a.

This chain is noncircular, source-faithful and complete for the bounded S018 contract. **ACCEPTED with no retry** is the smallest justified status. No repair to the submitted proof, upstream dependency or target interface is needed. Further scientific work outside this exact sequence is not certified or closed by this local review; the next action for this unit is root consumption and gating, not expanding the theorem here.



