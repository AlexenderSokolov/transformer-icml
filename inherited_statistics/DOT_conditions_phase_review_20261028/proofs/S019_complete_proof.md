# S019 有界历史弱混合域的原规则匹配 完整证明

编排说明（非原文）：本文件是已接纳版本的完整科学正文副本，保留全部局部证明或对应独立审查推理；身份、控制记录、原提交状态及管理性来源哈希表另行省略。原件不修改。以下英文原文的年代与结论范围保持不变，本次编排不构成新的数学审查。原编号可能跳跃；完整来源与新增／删略区间见 SOURCES.md、COPY_MAP.json。

历史口径（非原文）：S016、S017 关于未获新的原规则上界、临界统计间隙的说法属于当时结果；S018 只闭合精确临界序列。S019 已进一步在 1≤M≤K⁴、0≤β≤1/2 上闭合原规则与共同 minimax 的 H 匹配，包含 S017 全部固定射线。当前综合结论以外层中文导读及该明确接纳范围为准。旧数值证书的数学结论没有被推翻。

原文内 Section 7/9 的来源身份表等管理交叉引用，统一由本包 SOURCES.md 的同名原件身份与依赖入口补足；其省略不删除被引用的科学接口。有限检查叙述是原作者／原独立审查已执行的历史事实，本次装配未重跑这些数学检查。检查脚本与运行结果在原研究记录保留，不随科学包公开；定理依据完整符号证明而非有限枚举。

In the unchanged arbitrary-initialization, legal order-two, full-history, actual-terminal expected half-L1 TV experiment, every integer `K>=2`, integer `1<=M<=K^4` and public `0<=beta<=1/2` satisfy

    2^-18 H <= R_D2(K,M,beta) <= R_D2^+(K,M,beta) <= min{1,128H},
    a=min{1,sqrt(K^3/(M+1))}, delta=1-beta,
    v=delta^(M/2), H=max{a,v}.                                    (S019)

The upper belongs to **unchanged original full-history add-one**, not a suffix predictor. This is a standard interface corollary of the actually accepted S018 finite bound and S016 lower envelope, with elementary finite scalar specialization. It introduces no source family or statistical method. It also gives matching original-rule and common-minimax orders on all fixed S017 rays, including their critical equality. It does not establish a full joint rate outside the stated strip.


## 1. Exact experiment, assumptions and accepted interfaces

On `A_K={0,...,K-1}`, a source has one fixed homogeneous table `theta=(theta_ab(c))` of nonnegative normalized rows. Its pair kernel has only legal shifts

    P_theta((a,b),(b,c))=theta_ab(c).

The initial pair law mu is arbitrary. The class `D_K(2,beta)` consists of such `(theta,mu)` for which some hidden probability pi satisfies

    pi P_theta=pi,       P_theta^2(s,t)>=beta pi(t) for EVERY s,t.  (1)

Zeros, sparse stationary support, reducibility and mu singular to pi are allowed. Beta is a public lower bound, not a disclosed exact source coefficient. Observe the full history `X_1,...,X_(M+2)` and put `Y_j=(X_(j+1),X_(j+2))`, `0<=j<=M`. Exactly M departures are observed. For the unobserved `X_(M+3)`, the prediction target is the actual terminal row `theta_(Y_M)`. A common predictor A may use the full history, public K,M,beta and an independent seed, but no hidden theta, mu, pi, latent labels or future. Define

    R_D2=inf_A sup_((theta,mu) in D_K(2,beta))
                  E TV(A(X_1^(M+2)),theta_(Y_M)),
    TV(p,q)=(1/2)sum_c |p(c)-q(c)|.

The original rule counts every departure, without burning a prefix:

    C_s(c)=sum_(j=0)^(M-1)1{Y_j=s,X_(j+3)=c},
    n_s=sum_c C_s(c),       p_s^+(c)=(C_s(c)+1)/(n_s+K).

Its worst class risk at `s=Y_M` is `R_D2^+`. This common deterministic predictor needs only K and the observed history; neither beta nor any analysis parameter is an input. In particular `R_D2<=R_D2^+<=1`.

Primitive assumptions are exactly this experiment and (1), plus the public finite-strip domain in (S019). They have no stable upstream assumption IDs, so actual content is given rather than invented identifiers. The bounds below are accepted conclusions or locally proved scalar inequalities, not extra source hypotheses.

### Named accepted result applications

1. **S018 Theorem 4, Finite original-rule geometric bound (`thm:s018-geometric`).** In precisely this experiment, for every `K>=2,M>=1,0<beta<1` and analysis tolerance `0<epsilon<1`, put

       r=floor(M/2),       B_e=K+ln(K^2 M/epsilon).

   Its conclusion is

       R_D2^+ <= min{1, epsilon+delta^r
                      +sum_(j=1)^r beta delta^(j-1)
                          min{1,4K sqrt(B_e/(M-2j+1))}}.          (G)

   The bound is uniform over the entire class and arbitrary mu, for the displayed original counts. All midpoint, no-success and zero-length-suffix issues are part of the accepted theorem. We inherit its proof, not assume a new regeneration property or re-prove its coupling. The local invocation below has `0<beta<=1/2<1` and `epsilon=1/K in (0,1)`. Beta zero is handled without (G).

2. **S016 Theorem S016 and Proposition 4, All-parameter maximum assembly (`prop:s016-envelope`).** In exactly the same common-predictor experiment, for every `K>=2,M>=1,beta in [0,1]`, put

       i=min{1,sqrt(K/(M+1))}, g=min{1,sqrt(K^5/(M+1))},
       hstar=min{1,sqrt(K^4/(M+1))}, F=max{i,min{delta,a}}.

   Then

       R_D2 >= 2^-17 max{F,delta^(M+1)g,v hstar}.                 (L)

   Its proof supplies the lower for every fixed common randomized predictor before the algorithm infimum. The beta-zero endpoint is already included directly. Its stronger `F/180`, `2^-16 delta^(M+1)g`, IID floor and endpoint baselines remain available. No family-only upper or state-TV lower is used here.

3. **S017 Lemma 1, Rounded rays and uniform contraction (`lem:s017-round`).** Used only for the final consequence, not the finite-strip proof. For fixed `3<rho<=4,gamma>0`, `M=ceil(K^rho)`, `beta=gamma ln(K)/M`, eventually `0<beta<1/2`, a is uncapped and `a/K^(-(rho-3)/2)->1`. Its proved logarithmic inequality is

       0<=-ln(1-beta)-beta<=beta^2/[2(1-beta)],
       M beta^2<=gamma^2(ln K)^2/K^rho ->0.                       (R)

   This supplies controlled exponent conversion on each fixed ray, not a uniform replacement of v throughout the strip.



## 2. Local lemma map

| Unit | Named result / stable label | Contribution |
|---|---|---|
| unit_001 | Lemma 1, Finite-strip lower comparison (`lem:s019-lower`) | Preserve both caps and the closed beta-zero endpoint |
| unit_002 | Lemma 2, Uniform geometric upper budget (`lem:s019-budget`) | Scalar tolerance, early/late parity sums, exact no-success term |
| unit_003 | Theorem 3, Bounded-strip original-rule matching (`thm:s019-strip`) | Boundary branches, cap and common-algorithm assembly |
| unit_004 | Corollary 4, Fixed-ray consequence (`cor:s019-rays`) | Finite-strip inclusion and accepted controlled-log conversion |

## 3. Local derivation

### unit_001: Lemma 1 — Finite-strip lower comparison (`lem:s019-lower`)

**Statement.** Under the experiment and finite-strip assumptions of (S019), the accepted lower (L) implies `R_D2>=2^-18 H`.

**Proof.** Since `delta>=1/2` and `0<a<=1`, both delta and a are at least a/2. Thus `F>=min(delta,a)>=a/2`, including a=1. Also `M+1<=K^4+1` and `K^4>=16` imply

    hstar>=sqrt(K^4/(K^4+1))>=sqrt(16/17)>1/2.                   (2)

The first comparison preserves the cap: both 1 and the uncapped square root defining hstar are at least its displayed right side. Consequently (L), after dropping only its nonnegative middle entry, gives

    R_D2>=2^-17 max{F,v hstar}
         >=2^-17 max{a/2,v/2}=2^-18 H.

This applies at beta zero because (L) already includes that endpoint; then delta=v=H=1. More sharply, `M+1<=K^4+1<=K^5` gives g=1, so S016's retained beta-zero baseline `R_D2>=2^-16` remains true. No lower witnesses are changed or combined by addition. ∎

### unit_002: Lemma 2 — Uniform geometric upper budget (`lem:s019-budget`)

**Statement.** Under the same experiment and strip, if `0<beta<=1/2` and a<1, the accepted bound (G) at epsilon=1/K gives

    R_D2^+ <= min{1, [1+8sqrt(2)+64sqrt(2/e)]a+sqrt(2)v}.         (3)

**Proof: analysis tolerance and finite logarithm.** Here `a=sqrt(K^3/(M+1))` and, by integrality, `M>=K^3>=8`. Set epsilon=1/K. Since `M<=K^4`,

    B_e=K+ln(K^3 M)<=K+7ln K<=4K.                              (4)

For the last inequality, `(ln x)/x` has derivative `(1-ln x)/x^2` and maximum 1/e on x>0. The exponential series gives `e>1+1+1/2=5/2>7/3`, so `1+7/e<4`. Also epsilon<=a follows, after squaring, from

    M+1<=K^4+1<=K^5,

where `K^4(K-1)>=16>1`. All constants are finite and independent of beta. The inner term of (G) is therefore at most

    min{1,8sqrt(K^3/(M-2j+1))}.                                (5)

**Early labels.** Put `h=floor(M/4)` and retain `r=floor(M/2)`. For `1<=j<=h`,

    M-2j+1>=M/2+1>=(M+1)/2.

Thus (5) is at most `8sqrt(2)a`. The geometric weights sum to `1-delta^h<=1`, so their early contribution is at most `8sqrt(2)a`. The use of the uncapped branch is an upper bound even when it exceeds one.

**Late labels, including the shortest suffixes.** If `h<j<=r`, then `delta^(j-1)<=delta^h`. The denominators `M-2j+1` are distinct positive integers: for even M they end at 1 (the accepted L=0 suffix), and for odd M they end at 2 (L=1). They form a subset of `{1,...,M}`, so

    sum_(j=h+1)^r (M-2j+1)^(-1/2)
       <=sum_(ell=1)^M ell^(-1/2)
       <=1+integral_1^M x^(-1/2)dx<=2sqrt(M).                   (6)

The integral comparison uses the decreasing integrand. Enlarging each capped term by the root branch, (6) yields

    late<=16 beta delta^h K^(3/2)sqrt(M)
         =16(beta M)delta^h sqrt(K^3/M)
         <=16sqrt(2)a(beta M)delta^h.                            (7)

The last step is `sqrt((M+1)/M)<=sqrt(2)`. Set the proof-local scalar `y=beta M>0`. Since `ln(1-beta)<=-beta`, by integrating `1/(1-u)>=1`, and `h>=M/4-1`,

    delta^h<=exp(-beta h)<=exp(beta)exp(-y/4).

The derivative of `y exp(-y/4)` is `exp(-y/4)(1-y/4)`, giving its maximum 4/e on y>=0. Since beta<=1/2,

    y delta^h<=exp(1/2)(4/e)=4/sqrt(e).

Together with (7), this bounds the entire late contribution by `64sqrt(2/e)a`. No late-success atom was deleted and no uniformly long suffix was assumed.

**Exact no-success exponent.** Integer parity gives `0<=M/2-r<=1/2`. Since `delta>=1/2`,

    delta^r=v delta^(-(M/2-r))<=sqrt(2)v.                        (8)

This compares the exact powers; it does not replace v by `exp(-beta M/2)`. The tolerance, early, late and no-success bounds inserted into (G) prove (3). ∎

### unit_003: Theorem 3 — Bounded-strip original-rule matching (`thm:s019-strip`)

**Statement.** Under exactly the experiment and finite-strip assumptions of (S019), the full chain (S019) holds, with the original add-one formula unchanged.

**Proof.** Lemma `lem:s019-lower` supplies the lower on the whole closed strip. The common admissibility of original add-one gives `R_D2<=R_D2^+`.

If beta=0, then v=H=1 and the probability-vector bound gives `R_D2^+<=1=min(1,128H)` without invoking S018 at an excluded endpoint. If a=1, likewise H=1 and this same trivial upper suffices. In particular every small horizon `M+1<=K^3`, including M=1, is covered before using Lemma `lem:s019-budget`; zero-length sums and denominators at small M cannot create an omitted case.

In the remaining domain `0<beta<=1/2,a<1`, Lemma `lem:s019-budget` and a,v<=H give the upper coefficient

    C=1+8sqrt(2)+64sqrt(2/e)+sqrt(2)<128.                        (9)

For a purely rigorous numerical comparison, e>2 implies `sqrt(2/e)<1`, and `sqrt(2)<3/2`. Hence `C<1+12+64+3/2=157/2<128`; no floating calculation is needed. Together with the risk cap one, this proves the required upper. Every source supremum in the accepted upper is the whole class (1); the lower retains every common predictor before infimization. No suffix algorithm, source-dependent choice or latent information is assigned to original add-one. ∎

### unit_004: Corollary 4 — Fixed-ray consequence (`cor:s019-rays`)

**Statement.** Under the same experiment, fix `3<rho<=4,gamma>0`, and set `M=ceil(K^rho)`, `beta=gamma ln K/M`. Then, including `gamma=rho-3`,

    R_D2=Theta_(rho,gamma)(K^(-min{rho-3,gamma}/2)),
    R_D2^+=Theta_(rho,gamma)(K^(-min{rho-3,gamma}/2)).              (10)

**Proof.** The accepted Lemma `lem:s017-round` supplies eventual beta<=1/2 and the scale of a. If rho<4, then for `K>=max{2,2^(1/(4-rho))}`, `K^rho<=K^4/2`, so `ceil(K^rho)<=K^rho+1<=K^4`. If rho=4, M=K^4 exactly. Thus Theorem `thm:s019-strip` eventually applies.

For the exact power, the accepted controlled remainder (R) gives

    -M beta^2/(4delta)<=ln(v K^(gamma/2))<=0,

whose left side tends to zero. Therefore `v/K^(-gamma/2)->1`, while `a/K^(-(rho-3)/2)->1`. Their maximum has the scale in (10), and the finite theorem bounds both risks above and below at that scale. Fixed-ray thresholds may depend on rho,gamma; the finite-strip constants 2^-18 and 128 do not. This is a direct consequence, not a separate family construction or general-ray project. ∎

## 4. Assembly, rate and baseline audit

- **Contribution:** `material_partial` relative to the wider condition-layering research objective, and complete for this bounded contract. The original-rule/common-minimax distinction is resolved on the whole strip, including the previously unresolved fixed critical rays. This standard corollary follows the accepted S018 finite theorem plus S016 lower; it carries no independent novelty claim.
- **Exposed variables:** all integer K>=2, integer 1<=M<=K^4 and real beta in [0,1/2]. The constants are universal, independent of K,M,beta,source,mu,pi and predictor. Epsilon=1/K is eliminated as an analysis-only parameter. The ray consequence fixes rho,gamma before taking K to infinity.
- **Exact rate and boundaries:** a retains its cap; v retains the exact exponent `(1-beta)^(M/2)`. Since delta>=1/2, no zero-base or `0^0` convention is needed. Beta=0 and a=1 are explicit, beta=1/2 is included, both M parities and final denominator values 1 and 2 are retained, and no stationary suffix of negative length occurs.
- **Probability and information:** deterministic finite horizon, unconditional expected half-L1 TV at the same actual terminal row, all original observations. There is no high-probability, stopping-time, squared-TV, predictive-KL, independent-query or conditional-risk substitution. Original add-one requires no class-parameter knowledge, but this is not a claim about selecting or estimating an unknown source class or optimal adaptation outside the strip.
- **Inherited baselines:** S016's stronger lower entries, IID floor and beta endpoints remain true; the beta-zero stronger lower was explicitly retained above. S018's sharper exact-sequence theorem `a/180<=R_D2<=R_D2^+<=min(1,128a)` at `M=K^4,beta=ln K/K^4` remains independently available, not replaced by the conservative H packaging. All stationary and fast-mixing accepted bounds remain valid. The old S017 numerical certificate still has its accepted critical order `Theta_rho(a sqrt(ln K/ln ln K))`; a sharper new risk certificate does not change that numerical optimization fact.
- **Scope exclusions:** no conclusion for M>K^4 or beta>1/2; no new hard family, third substantive route, full joint classification, optimal-IID original-rule claim, finite-network/codec/fault result, formal verification or literature-priority claim.
- **Notation/provenance:** the public interface is only the class/risks, a,delta,v,H and (S019). The data history is not abbreviated H, avoiding conflict with the rate. S016's i,g,hstar,F and S018's epsilon,B_e,r are translated accepted objects; h,y and C are proof-local deterministic expressions with every bound proved above. No generated-object condition is added to the source assumptions. All exact source/concentration/test mathematics is inherited through the two accepted interfaces, not newly certified at its earlier predecessors.


