# S017 固定多项式对数射线与旧临界证书 完整证明

编排说明（非原文）：本文件是已接纳版本的完整科学正文副本，保留全部局部证明或对应独立审查推理；身份、控制记录、原提交状态及管理性来源哈希表另行省略。原件不修改。以下英文原文的年代与结论范围保持不变，本次编排不构成新的数学审查。原编号可能跳跃；完整来源与新增／删略区间见 SOURCES.md、COPY_MAP.json。

历史口径（非原文）：S016、S017 关于未获新的原规则上界、临界统计间隙的说法属于当时结果；S018 只闭合精确临界序列。S019 已进一步在 1≤M≤K⁴、0≤β≤1/2 上闭合原规则与共同 minimax 的 H 匹配，包含 S017 全部固定射线。当前综合结论以外层中文导读及该明确接纳范围为准。旧数值证书的数学结论没有被推翻。

原文内 Section 7/9 的来源身份表等管理交叉引用，统一由本包 SOURCES.md 的同名原件身份与依赖入口补足；其省略不删除被引用的科学接口。有限检查叙述是原作者／原独立审查已执行的历史事实，本次装配未重跑这些数学检查。检查脚本与运行结果在原研究记录保留，不随科学包公开；定理依据完整符号证明而非有限枚举。

Fix real `rho in (3,4]` and `gamma>0`. For integer K tending to infinity, set

    M=ceil(K^rho),      beta=gamma log(K)/M,      delta=1-beta,
    a=min{1,sqrt(K^3/(M+1))}.

In the unchanged arbitrary-start, legal second-order, full-history, actual-terminal expected half-L1 TV experiment,

    gamma != rho-3:
    R_D2(K,M,beta)=Theta_(rho,gamma)(K^(-min{gamma,rho-3}/2)).          (A)

The upper belongs to the accepted **public common-predictor selector**, not to unchanged original full-history add-one. At the critical equality `gamma=rho-3`, the EXISTING optimized S011 numerical certificate has order

    U(K,M,beta)=Theta_rho(a sqrt(log K/log log K)),                     (B)
    a/180 <= R_D2(K,M,beta) <= U(K,M,beta)                             (C)

for all sufficiently large K. The extra logarithmic factor in (B) is a gap between these certificates, **not a necessary minimax factor or a solved critical risk rate**. Neither an exact leading constant nor a full joint `(K,M,beta)` formula is asserted.

This is a standard bounded derived consequence of accepted S011/S012/S015, not a new hard family or a new statistical method. Its source-relevant progress is `material_partial`: it identifies the fixed off-critical rays and isolates a narrower critical certificate gap. Constants and thresholds may depend on the fixed rho,gamma, but never on K, a source, signs, an initial/stationary law, or an algorithm. No uniformity near `gamma=rho-3` is claimed.


- Exact assigned target: (A), the numerical critical certificate (B) with only sandwich (C), all integer/floor/cap and uniform-over-burn checks, and fixed-parameter scope. S016 is independent and is not a dependency. No new family, third route, general-rho>4 extension, unknown-beta adaptation, or full joint formula is part of this step.

For clarity the underlying experiment is restated. On `A_K={0,...,K-1}`, a fixed homogeneous table theta has normalized nonnegative rows and induces only legal shifts

    P_theta((a,b),(b,c))=theta_ab(c).

Non-shift transitions are zero. The pair initialization mu is arbitrary. Membership in `D_K(2,beta)` means there exists a hidden stationary probability pi such that

    pi P_theta=pi,       P_theta^2(s,t)>=beta pi(t) for EVERY s,t.       (1)

Zero edges, sparse stationary support, and mu singular to pi are permitted. The table remains fixed throughout a trajectory, though the supremum may choose a different source at different public parameters. The observations are ALL `X_1,...,X_(M+2)`, and `Y_j=(X_(j+1),X_(j+2))` for `0<=j<=M`. Exactly M departures have been observed. A common possibly randomized predictor A may read this full history and public `K,M,beta`, plus an independent seed, but no hidden table, mu, pi, signs, latent coin labels, or future symbol. Its target is the actual row `theta_(Y_M)` for unobserved `X_(M+3)`, and

    R_D2=inf_A sup_((theta,mu) in D_K(2,beta))
                   E TV(A(X_1^(M+2)),theta_(Y_M)),
    TV(p,q)=(1/2) sum_c |p(c)-q(c)|.                                    (2)

Primitive conditions are exactly (1)–(2), the stated finite legal experiment and fixed-ray parameters. The frozen model has no stable assumption IDs; their actual content is stated rather than inventing upstream IDs. All scalar limiting/comparability properties below are proved, not added assumptions. Statements apply only for sufficiently large integer K, in particular `K>=13` and `0<beta<1`; no small-K or beta-endpoint claim is needed or substituted.

## 2. Accepted interfaces, source mapping, and local lemma map





### Accepted result applications

1. **S011, Theorem S011 and Proposition 2 (algorithm-separated envelope).** For the exact class and experiment (1)–(2), put

       i=min{1,sqrt(K/(M+1))},
       g=min{1,sqrt(K^5/(M+1))},
       F=max{i,min{delta,a}},
       u_s(ell)=min{1,48sqrt(K^3/(ell+1))},
       u_g(ell)=min{1,48sqrt(K^5/(ell+1))},
       h_b=delta^floor(b/2),                  0<beta<1.

   The finite certificates, with integer `0<=b<=M-1` and `ell=M-b`, are

       U_+=min{u_g(M), min_b min{1,
                 48sqrt(K^3/(M-b+1))+13sqrt(K)h_b^(3/4)}},
       U_suf=min_b min{u_g(M-b),u_s(M-b)+h_b u_g(M-b)},
       U_pool=min{1,(1/2)sqrt(K/M)+2delta},
       U=min{U_+,U_suf,U_pool}.                                         (3)

   Its conclusion is `F/180<=R_D2<=U`. A deterministic selector compares the three public certificates, uses a fixed tie rule, and in the suffix branch chooses the smallest public-bound-minimizing burn. All choices depend only on public K,M,beta, never on a source-specific risk. Only U_+ belongs to unchanged original rowwise add-one. The suffix rule uses departures b,...,M-1 and predicts at the SAME Y_M; it is a genuinely different algorithm.

2. **S015, Propositions 6–7 (finite star lower and count).** For every `K>=13,M>=1,0<beta<1`, let

       m=floor((K-1)/4), L=2m, q=floor(M/L),
       alpha=min{1/2,(1/8)sqrt(m^3/(q+1))}.

   The accepted legal star family lies in (1), with a common horizon-aligned initial law and hidden stationary witness `delta_(0,0)`. Every common full-history randomized predictor has prior-average actual-terminal TV risk at least

       delta^(H_M+1) alpha/8,                                           (4)
       H_M=q(m+1)+r_M,
       r_M=sum_(j=0)^(d-1) 1{(k+j) mod L in V_phase},
       d=M-qL, k=(2-d) mod L,
       V_phase={0,1,2,4} union {6,8,...,L-2}.

   An empty remainder sum is zero. In particular

       0<=H_M<=M,
       H_M=M/2+M/(2m)+e_M,       |e_M|<=L.                              (5)

   These are accepted full-experiment lower and exact count statements, not a mixing-TV lower being relabeled as statistical risk. Every condition is met by our eventual ray domain. The same family is used unchanged; no latent labels or source advice are given to the predictor.

3. **S012, Proposition 9 (accepted scalar precedent), and S015, Proposition 8.** At `M=K^4,beta=log K/(4K^4)`, S012 established the value/order of exactly (3), and S015 combined its star lower with that upper to establish common-minimax order K^-1/8. We retain these statements and their stronger original constants. The new scalar calculations below derive the full bounded fixed-ray assertions directly from (3)–(5); the old one-ray statement is not treated as a theorem about unproved other rays. S012's other all-domain and restricted-family conclusions remain unchanged and are not re-proved here.

For each fixed common A the source supremum dominates both the stationary-subclass bound and (4), so these lower bounds combine by a **maximum**, never a sum. The algorithm infimum is taken only afterward. All parameter specializations are deterministic and preserve the accepted full-history quantifier.

| Local unit | Named result / stable label | Contribution |
|---|---|---|
| unit_001 | Lemma 1, Rounded rays and uniform contraction (`lem:s017-round`) | Admissibility, exact denominator scale, all-burn log errors |
| unit_002 | Lemma 2, Star and stationary lower scales (`lem:s017-lower`) | Floor-sensitive amplitude and vulnerable survival |
| unit_003 | Proposition 3, Below-critical matching (`prop:s017-below`) | Admissible short public suffix and rate |
| unit_004 | Proposition 4, Above-critical matching (`prop:s017-above`) | Fixed fractional burn and rate |
| unit_005 | Lemma 5, Critical numerical reduction (`lem:s017-critical`) | Uniform legal grid, other branches exactly capped |
| unit_006 | Proposition 6, Critical optimized certificate (`prop:s017-opt`) | Cap-safe lower and rounded trial upper |

## 3. Local derivation

### unit_001: Lemma 1 — Rounded rays and uniform contraction (`lem:s017-round`)

**Statement.** Under (1)–(2) and fixed `3<rho<=4,gamma>0`, with the ray parameters above, eventually K>=13 and `0<beta<1/2`; a is uncapped, F=a, and

    a=K^(-(rho-3)/2) sqrt(K^rho/(M+1)),
    (1+2/K^rho)^(-1/2) <= a/K^(-(rho-3)/2) <=1.                         (6)

For every admitted suffix `1<=ell<=M`, `u_g(ell)=1`. Define proof-local

    B=(gamma/2)log K,
    E_0=beta+M beta^2/(4delta).

Then E_0 tends to zero and, uniformly over EVERY admitted integer burn b=M-ell,

    log h_b=-B+B ell/M+epsilon_b,       |epsilon_b|<=E_0.              (7)

In addition,

    |log h_(M-1)+B|<=E_0.                                              (8)

**Proof.** Write `M=K^rho+zeta`, where `0<=zeta<1`. Thus `K^rho<=M<K^rho+1` and `M+1<=K^rho+2`. Since `beta<=gamma log K/K^rho ->0`, the domain conditions hold eventually. Because rho>3, `K^3/(M+1)<=K^(3-rho)->0`, proving uncapping and (6). The exact i is then a/K, so i<=a. Eventually `delta>1/2>a`, giving F=a. Since rho<=4 and K>=2,

    ell+1<=M+1<=K^rho+2<=K^4+2<K^5.

Consequently u_g(ell)=1 for all suffixes, including the generic original term; this finite inequality does not depend on b.

For `0<=x<1`, direct integration yields

    0<=-log(1-x)-x=integral_0^x t/(1-t)dt<=x^2/[2(1-x)].              (9)

Put `r=floor(b/2)` and `v=-log delta-beta`. Then `0<=v<=beta^2/(2delta)` and

    log h_b+beta b/2=beta(b/2-r)-r v.

Since `0<=b/2-r<1` and r<=M/2, its absolute value is at most E_0. The identity `beta M/2=B` proves (7), without a nonuniform b-dependent remainder. For b=M-1, `0<=M/2-floor((M-1)/2)<=1`; the same calculation gives (8). Finally

    M beta^2=gamma^2(log K)^2/M<=gamma^2(log K)^2/K^rho ->0,

so E_0 tends to zero. All errors are deterministic and source-independent. ∎

### unit_002: Lemma 2 — Star and stationary lower scales (`lem:s017-lower`)

**Statement.** Under the fixed-ray assumptions of Lemma 1 and accepted star interface (4)–(5),

    m^3/(q+1) ~ K^(4-rho)/128,
    alpha -> A_rho,
    A_rho=1/2 if rho<4,       A_4=1/(64sqrt(2)),                        (10)
    delta^(H_M+1)=K^(-gamma/2)(1+o(1)).                                (11)

For rho<4, alpha is in fact exactly 1/2 eventually. Thus, for all sufficiently large K,

    R_D2 >= max{ a/180, (A_rho/32) K^(-gamma/2) }.                      (12)

Every threshold may depend on fixed rho,gamma; the constants in (12) do not depend on a source or algorithm.

**Proof: all floor and amplitude errors.** Write `K-1=4m+e`, where `e in {0,1,2,3}`, and `eta=(1+e)/K`. Then `m=(K/4)(1-eta)`, `1/K<=eta<=4/K`, and `K/8<=m<=K/4` for K>=13. Let

    kappa=q+1-M/(2m),                 0<kappa<=1.

The exact identity

    m^3/(q+1)
      =2m^4/(M+2m kappa)
      =[K^(4-rho)/128]
         (1-eta)^4 / [1+(zeta+2m kappa)/K^rho]                         (13)

handles both floors and the required q+1 denominator. In particular the last multiplicative factor lies between

    (1-4/K)^4/[1+(1+K/2)/K^rho]       and       1.

Both bounds tend to one, proving (10)'s first asymptotic. For rho<4 it diverges, so eventually `m^3/(q+1)>=16` and alpha=1/2. For rho=4 the ratio tends to 1/128, and the square-root branch tends to `1/(8sqrt(128))=1/(64sqrt(2))<1/2`; taking the minimum preserves this limit. No integer subsequence or residue restriction was used.

**Proof: exact vulnerable exponent.** Apply (9) to the accepted count (5), keeping the target's extra exponent one:

    |log(delta^(H_M+1))+B|
      <= gamma log K/(2m) + beta(L+1)
                         +(M+1)beta^2/(2delta).                       (14)

Indeed the linear discrepancy is `beta M/(2m)+beta(e_M+1)`, and the quadratic remainder is at most `(H_M+1)beta^2/(2delta)<= (M+1)beta^2/(2delta)`. The three displayed errors have the respective explicit bounds

    gamma log K/(2m) <= 4gamma log K/K,
    beta(L+1) <= gamma(log K)(K/2+1)/K^rho,
    (M+1)beta^2/(2delta)
      <= [gamma^2(log K)^2/(2delta K^rho)](1+1/M).

All tend to zero. Thus the extra phase charge, beta times the O(L) count error, the extra target delta, and the beta-squared-horizon error are all paid. Exponentiation proves (11).

For sufficiently large K, (10) gives `alpha>=A_rho/2` and (14) gives `delta^(H_M+1)>=K^(-gamma/2)/2`. Therefore (4) is at least `(A_rho/32)K^(-gamma/2)`. Lemma 1 and the accepted stationary bound give a/180. Each bound holds for every common predictor before its infimum, so the maximum argument after (5) proves (12). ∎

### unit_003: Proposition 3 — Below-critical matching (`prop:s017-below`)

**Statement.** Under (1)–(2), fixed `3<rho<=4` and `0<gamma<rho-3`, conclusion (A) holds with rate K^(-gamma/2). An admissible public trial suffix proves its upper; the actual algorithm may be the existing public selector from (3).

**Proof.** Fix `epsilon=(rho-3-gamma)/2>0`. Let

    ell_*=floor(K^(3+gamma+epsilon)),       b_*=M-ell_*.

For large K, ell_*>=1. Its defining exponent is strictly below rho, so `ell_*<=K^(3+gamma+epsilon)<K^rho<=M`; hence b_* is an admitted integer burn. The denominator remains ell_*+1, and

    u_s(ell_*)<=48K^(-(gamma+epsilon)/2),
    ell_*/M<=K^-epsilon,
    beta ell_*<=gamma(log K)K^-epsilon ->0.                            (15)

The first inequality follows from `floor(t)+1>t` even when t is an integer. Lemma 1 gives

    |log h_(b_*)+B|<=B K^-epsilon+E_0 ->0.                             (16)

Thus for all sufficiently large K the right side of (16) is at most log 2 and `48K^(-epsilon/2)<=1`. With u_g=1, the trial candidate and (3) give the explicit upper

    R_D2<=U<=U_suf<=u_s(ell_*)+h_(b_*)<=3K^(-gamma/2).                 (17)

The minimum cap in (3) can only reduce this upper. Lemma 2 supplies the matching lower `(A_rho/32)K^(-gamma/2)`. The trial depends only on fixed ray parameters and public K; more importantly, no such extra ray input is needed by the claimed predictor, since the accepted minimizer of (3) uses only public K,M,beta and is at least as good in certificate value. This is not a hidden-source oracle or a claim about original add-one. ∎

### unit_004: Proposition 4 — Above-critical matching (`prop:s017-above`)

**Statement.** Under (1)–(2), fixed `3<rho<=4` and `gamma>rho-3`, conclusion (A) holds with rate K^(-(rho-3)/2). Again the upper is a common-selector/suffix conclusion, not an original-rule conclusion.

**Proof.** Choose the fixed number

    t=(1+(rho-3)/gamma)/2,

which lies strictly between `(rho-3)/gamma` and 1. Let `b_*=floor(tM)` and `ell_*=M-b_*`. Since 0<t<1 and M is a positive integer, `0<=b_*<=M-1` and `ell_*>=1`. Also

    ell_*+1 >= (1-t)M+1 >= (1-t)(M+1),
    u_s(ell_*) <= [48/sqrt(1-t)] a.                                    (18)

The second inequality uses the eventual uncapped a from Lemma 1; the cap in u_s only helps. Formula (7), equivalently its proof before replacing b by M-ell, and `0<=tM-b_*<1` imply

    |log h_(b_*)+tB|<=E_0+beta/2 ->0.

Thus eventually `h_(b_*)<=2K^(-t gamma/2)`. By (6),

    h_(b_*)/a
      <=2sqrt(1+2/K^rho) K^(-(t gamma-(rho-3))/2)
      =2sqrt(1+2/K^rho) K^(-(gamma-(rho-3))/4) ->0.                     (19)

Choose K large enough that the last quantity is at most one. Then (3), (18)–(19) give

    R_D2<=U<=U_suf<=[48/sqrt(1-t)+1]a.                                 (20)

The accepted stationary lower is a/180. Since (6) compares a with K^(-(rho-3)/2), this is the required Theta conclusion. For example (6) gives the eventual lower `K^(-(rho-3)/2)/(180sqrt(3))`, while (20) gives the displayed fixed-parameter upper constant. The factor 1/sqrt(1-t) and the threshold in (19) explain why no uniform near-critical claim is made. ∎

### unit_005: Lemma 5 — Critical numerical reduction (`lem:s017-critical`)

**Statement.** Under (1)–(2), fixed `3<rho<=4` and critical `gamma=rho-3`, let `B=(gamma/2)log K`. For every legal suffix define the exact grid coordinate

    x_ell=(ell+1)/(M+1),        1<=ell<=M.

For all sufficiently large K, uniformly over the whole grid,

    (a/2)exp(B x_ell) <= h_(M-ell) <= 2a exp(B x_ell),                  (21)
    u_s(ell)=min{1,48a x_ell^(-1/2)},
    U_suf=min_(1<=ell<=M) min{1,u_s(ell)+h_(M-ell)}.                   (22)

Also `U_+=U_pool=1` eventually. These are properties of the numerical certificates, not risk lower bounds.

**Proof: exact grid and uniform error.** Now `K^(-gamma/2)=sqrt(K^3/K^rho)`, whereas the exact a uses M+1. By Lemma 1,

    log[h_(M-ell)/(a exp(B x_ell))]
       =epsilon_(M-ell)+B(ell/M-x_ell)
                               +(1/2)log((M+1)/K^rho).

The grid correction is explicit:

    0<=x_ell-ell/M=(M-ell)/[M(M+1)]<=1/M.

Moreover `0<=log((M+1)/K^rho)<=2/K^rho` by `log(1+u)<=u`, which follows by integrating `(1+u)^(-1)<=1`. Thus the absolute log ratio is bounded, independently of ell, by

    E_0+B/M+1/K^rho
      =3beta/2+M beta^2/(4delta)+1/K^rho ->0.                           (23)

Choosing the same eventual threshold so this is at most log 2 proves (21). The denominator identity for u_s is exact. Lemma 1 supplies u_g=1 for EVERY ell, so (3) reduces exactly to (22). In particular floors have not been replaced by a continuous infimum.

**Proof: the other two branches.** Since `0<delta<1`, all b<=M-1 have `h_b>=h_(M-1)`. Equation (8) yields

    13sqrt(K)h_b^(3/4)
      >=13K^(1/2-3gamma/8)exp(-3E_0/4)
      =13K^(1/2-3gamma/8)(1+o(1)).                                    (24)

Here `0<gamma=rho-3<=1`, so the exponent is at least 1/8. For example, once E_0<=log 2, the lower is at least `13*2^(-3/4)K^(1/8)>1`. This bound is uniform over ALL burns. Each original burn candidate is therefore capped at one, and its generic term is one by Lemma 1, proving U_+=1. Since beta<1/2 eventually, `2delta>1` and U_pool=1. ∎

### unit_006: Proposition 6 — Critical optimized certificate (`prop:s017-opt`)

**Statement.** Under the critical hypotheses of Lemma 5, for all sufficiently large K,

    (1/2)a sqrt(B/log B) <= U_suf <=140a sqrt(B/log B),                 (25)
    U=U_suf.

Consequently (B)–(C) hold. This proposition lower-bounds only the existing numerical certificate U, not the true risk of any estimator.

**Proof: scale and cap control.** B tends to infinity since fixed gamma>0. Let the proof-local scale be

    T_K=a sqrt(B/log B).

For B>=e, `T_K<=a sqrt(B)<=sqrt(gamma/2)K^(-gamma/2)sqrt(log K)->0`. The last limit follows on writing y=log K: `exp(-gamma y/2)sqrt(y)->0` for fixed gamma>0, for instance from the power-series lower bound for exp(gamma y/4). Thus eventually log B>=1, T_K<1, and 140T_K<1. These thresholds are deterministic functions of the fixed rho.

For any legal ell with `x_ell<=log B/(2B)`, the exact stationary term in (22) obeys

    u_s(ell)>=min{1,48sqrt(2)T_K} >= T_K/2.                             (26)

The second inequality uses T_K<1 and 48sqrt(2)>1/2, and therefore explicitly includes the stationary-cap-one case. The full candidate `min{1,u_s+h}` is at least u_s because `u_s<=1` and h>=0. For any other legal ell, (21) gives

    h_(M-ell)>=(a/2)exp((log B)/2)
              =(a/2)sqrt(B)>=(1/2)T_K.                               (27)

The full candidate is at least h, since the actual h is in [0,1]. Equations (26)–(27) cover EVERY legal integer ell, not just a putative optimizer; hence they prove the lower in (25). Any candidate whose outer cap equals one is also at least T_K/2, so caps cannot defeat the lower.

**Proof: a legal rounded upper trial.** Put

    y=(log B)/(4B),       ell_*=floor(M y),       b_*=M-ell_*.

Eventually `0<y<1` and `M y>=2`. To justify the latter, B is a fixed multiple of log K and `M>=K^rho`, so `M/B->infinity` while log B eventually exceeds one. Therefore `1<=ell_*<=M-1`; b_* is admitted. Using `ell_*+1>M y` and `(M+1)/M<=2`,

    u_s(ell_*)<=48sqrt(K^3/(ell_*+1))
        <=48a sqrt((M+1)/(M y))
        <=48sqrt(8)T_K.                                                (28)

For the contraction term use (7) directly, avoiding any extra grid-rounding cost: since ell_*/M<=y,

    h_(b_*)/a
      <=exp[E_0+(1/2)log((M+1)/K^rho)] exp(By)
      <=2B^(1/4)                                                       (29)

eventually. The same bounds as (23) justify the uniform factor 2. Since

    B^(1/4)/sqrt(B/log B)=sqrt(log B)/B^(1/4) ->0,

it is at most one eventually; equivalently log B<=sqrt(B), which follows for example for every B>=exp(4) by differentiating sqrt(B)-log B. Combining (28)–(29) gives the admissible trial upper

    U_suf<=u_s(ell_*)+h_(b_*)
         <=[48sqrt(8)+2]T_K<140T_K.                                   (30)

This tends to zero and is eventually strictly below one. Thus the optimum cannot be improved by a cap-one candidate. Lemma 5 gives U_+=U_pool=1, so (3) implies U=U_suf. This proves (25), with all finite-grid, denominator and cap checks retained.

**Proof: conversion to the requested logarithms and risk statement.** Because gamma is fixed and positive,

    B=(gamma/2)log K,
    log B=log log K+log(gamma/2).

For `log log K>=2|log(gamma/2)|` and positive log log K,

    (1/2)log log K <=log B<=(3/2)log log K.

Consequently

    sqrt(gamma/3) sqrt(log K/log log K)
      <=sqrt(B/log B)
      <=sqrt(gamma) sqrt(log K/log log K).                             (31)

These constants depend only on rho at criticality. Equations (25) and (31) prove (B). Independently, Lemma 1 and the accepted S011 statistical sandwich give (C) with the exact lower a/180. No inference `R_D2>=constant*T_K` is licensed by the numerical lower in (25); that would reverse the relation `R_D2<=U`. The true critical rate remains unidentified between the stated lower and upper. ∎

## 4. Target-step assembly and preserved boundaries

Lemma 1 (`lem:s017-round`) supplies exact eventual admissibility, denominator scale, generic caps and a single all-burn contraction error bound. Lemma 2 (`lem:s017-lower`) specializes the accepted star family without changing its full-history experiment, retains the exact count until its error is controlled, and combines it by maximum with the stationary subclass. Proposition 3 (`prop:s017-below`) supplies a valid public trial below criticality; Proposition 4 (`prop:s017-above`) supplies a fractional-burn trial above it. These prove (A) on every stipulated fixed noncritical ray.

At the exact critical equality, Lemma 5 (`lem:s017-critical`) proves the all-grid comparison and shows that the other existing certificates equal one. Proposition 6 (`prop:s017-opt`) proves the capped numerical optimization order and establishes a vanishing legal trial, yielding (B). The independent accepted statistical sandwich yields only (C), not a necessary logarithmic penalty. This noncircular chain establishes the entire bounded S017 target.

The original S015 case `rho=4,gamma=1/4` lies below the critical value 1 and is recovered at order K^-1/8. Its accepted sharper liminf/limsup constants and ratio-one certificate statement remain available unchanged; (A) does not replace them. S011's all-domain original/suffix/pooled distinctions and endpoint results, S012's all-domain absorbing lower and exact different-family upper, and all other accepted conclusions remain unchanged. This proof neither reads nor relies on S016.

The boundary isolated here is between two proven **fixed-ray** mechanisms: the inherited star initialization lower dominates below criticality, whereas a fixed fractional burn suffices to attain the stationary scale above it. At criticality this analysis leaves a statistical gap of order sqrt(log K/log log K) in the displayed certificates. It does not establish necessity of that factor, necessity of a particular burn choice, or a universal threshold outside the fixed-ray family.

## 5. Explicit rate, notation, and assumption audit

- **Exposed variables and fixed mode:** integer K tends to infinity, with fixed real `3<rho<=4,gamma>0`; M and beta are exactly the ceiling/log expressions, never asymptotic replacements inside finite definitions. At criticality gamma is exactly rho-3. Statements are eventual, not all-K claims.
- **Hidden constants:** may depend on fixed rho,gamma (only rho at criticality); never on K, theta, mu, pi, signs, the predictor or its seed. The proofs display deterministic error bounds and inequalities defining each eventual threshold. No claim is uniform as gamma approaches rho-3, rho approaches 3, or rho approaches 4 from below. The discontinuity in the eventual amplitude branch at rho=4 is expressly retained.
- **Probability/norm/horizon:** deterministic finite horizon M at each K; expected actual-terminal half-L1 TV under the original full-history experiment. The asymptotics concern these deterministic risk/certificate sequences. No high-probability, all-time, stopping-time, independent-query, squared-TV or KL-loss substitution occurs.
- **Probability conversion:** no new conditioning or probability conversion is introduced. The accepted star lower already includes its vulnerable-event probability and changed-target extra delta. Formula (14) preserves both, while the stationary and star risk lower bounds combine before the infimum by maximum.
- **Algorithm information:** the actual selector uses only K,M,beta and finite public minimization. Trial choices involving fixed ray constants serve analysis only. The full history remains available even when a selected suffix algorithm discards a deterministic prefix. No source-specific selector, unknown-beta estimator or original-add-one optimality is asserted.
- **Public-facing notation:** the original class/risk, fixed ray, a, and inherited U are the minimal exports. The other inherited certificate symbols retain S011 meanings. The inherited m,L,q,alpha,H_M and exact remainder data are proof-local instantiated accepted objects, not new algorithm inputs. The proof-local B,E_0,epsilon_b,x_ell,T_K,y,t,epsilon,zeta,eta,kappa,e_M are explicit deterministic expressions or locally bounded errors; no free assumed bounded quantity is introduced. The ordinary history is not denoted H_M, which is solely the accepted deterministic vulnerable count.
- **Constant provenance:** 48,13 and 1/180 are inherited from S011; alpha/8 and exact H_M are inherited from S015. All new constants, amplitude limits, log-error bounds, threshold choices, factors 2,3,32 and critical 140 are derived in the named local units. No source-dependent exponential constant is hidden in an order symbol.
- **Primitive versus derived:** only the finite experiment, information restrictions, all-state class definition and fixed-ray ranges are primitive. Legal star membership/full conditional testing/count are accepted S015 conclusions. All ceiling/floor asymptotics, survival equivalences, admissible burns, caps, grid comparisons and numerical optimizations are proved here. There is no unproved generated-object hypothesis in the theorem.
- **Scope:** no new family, third route, general-rho>4 result, full joint formula, unknown-beta adaptation, novelty/literature-priority finding, formal verification or Euler implementation/resource/fault conclusion. The critical certificate lower is never promoted to a statistical lower. Scientific scope remains the bounded contract, not a mandatory endpoint for the broader research program.


## 8. Supplementary producer checks

An inline producer-owned Python calculation in the tool trace checked **1,032,955** individual legal suffix/burn instances across `(K,rho)=(13,4),(17,4),(16,3.5),(25,3.5)` and gamma from `0.125,0.5,1,2,rho-3` (including repeated values where listed). These choices have exact integer K^rho. It checked the every-burn logarithmic inequality (7), generic cap condition, critical grid error bound (23), minimum-burn inequality (8), exact count bound (5), and star survival error (14). It also checked **30** large-parameter trial candidates, rho in `{3.5,4}`, K in `{10^4,10^8,10^16,10^32,10^60}`, and gamma below/equal/above rho-3, for admissibility and finite capped certificate values. The logarithmic and square-root comparisons used floating arithmetic with absolute tolerance 1e-14 where needed. All passed.

These finite checks are supplementary sanity checks, not a proof of the asymptotic orders, a continuous-to-integer optimization justification, an independent review, or formal verification. The general floor/ceiling and all-burn claims rest on the displayed symbolic proofs. No checker file was written.




