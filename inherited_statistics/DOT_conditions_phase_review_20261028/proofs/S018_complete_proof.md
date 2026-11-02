# S018 原完整历史规则的再生末行计数 完整证明

编排说明（非原文）：本文件是已接纳版本的完整科学正文副本，保留全部局部证明或对应独立审查推理；身份、控制记录、原提交状态及管理性来源哈希表另行省略。原件不修改。以下英文原文的年代与结论范围保持不变，本次编排不构成新的数学审查。原编号可能跳跃；完整来源与新增／删略区间见 SOURCES.md、COPY_MAP.json。

历史口径（非原文）：S016、S017 关于未获新的原规则上界、临界统计间隙的说法属于当时结果；S018 只闭合精确临界序列。S019 已进一步在 1≤M≤K⁴、0≤β≤1/2 上闭合原规则与共同 minimax 的 H 匹配，包含 S017 全部固定射线。当前综合结论以外层中文导读及该明确接纳范围为准。旧数值证书的数学结论没有被推翻。

原文内 Section 7/9 的来源身份表等管理交叉引用，统一由本包 SOURCES.md 的同名原件身份与依赖入口补足；其省略不删除被引用的科学接口。有限检查叙述是原作者／原独立审查已执行的历史事实，本次装配未重跑这些数学检查。检查脚本与运行结果在原研究记录保留，不随科学包公开；定理依据完整符号证明而非有限枚举。

补充检查出处（非原文）：正文末尾的 The script 指原作者补充检查，不是本包 verify_copies.py。

## 1. Exact experiment and public conclusions

Fix integers `K>=2,M>=1` and public `0<beta<1`. Let `A={0,...,K-1}`. A fixed homogeneous table theta has nonnegative rows summing to one. Its only possible pair transitions are

    P((a,b),(b,c))=theta_ab(c).

Let mu be ANY initial pair law. Membership in `D_K(2,beta)` means there is a hidden probability pi with

    pi P=pi,             P^2(s,z)>=beta pi(z) for EVERY s,z in A^2.   (D)

Zeros, sparse stationary support and mu singular to pi are allowed. The observed history is the whole `H=(X_1,...,X_(M+2))`; put `Y_i=(X_(i+1),X_(i+2))`, `0<=i<=M`. Exactly M departures are observed; the target is `theta_(Y_M)` for unobserved `X_(M+3)`. Define

    C_s(c)=sum_(i=0)^(M-1) 1{Y_i=s, X_(i+3)=c},
    n_s=sum_c C_s(c),          J=n_(Y_M),
    p_s^+(c)=(C_s(c)+1)/(n_s+K),
    loss(H)=TV(p^+_(Y_M),theta_(Y_M)),    TV(p,q)=||p-q||_1/2.

The original rule uses ALL M departures. It receives no latent labels, stationary law, source, residual kernel, selected burn or auxiliary observations. A general common predictor B may use public K,M,beta, full H and an independent seed but no hidden source information or future. Set

    R_D2=inf_B sup_((theta,mu) in D_K(2,beta)) E TV(B(H),theta_(Y_M)),
    R_D2^+=sup_((theta,mu) in D_K(2,beta)) E loss(H).

Fix any analysis parameter `0<epsilon<1`, and define

    delta=1-beta, r=floor(M/2), B_e=K+ln(K^2 M/epsilon).

The notation B_e avoids confusing this scalar with a general predictor B. All logarithms are natural.

**Theorem 4 (finite original-rule bound; `thm:s018-geometric`).** Under this exact setting,

    R_D2^+ <= min{1, epsilon+delta^r
                   +sum_(j=1)^r beta delta^(j-1)
                     min{1,4K sqrt(B_e/(M-2j+1))}}.                 (G)

When M=1 the sum is empty and the bound is one. The theorem does not optimize epsilon or alter the algorithm.

**Theorem 5 (exact critical matching; `thm:s018-critical`).** At `M=K^4` and `beta=ln(K)/K^4`, every integer K>=2 satisfies

    a/180 <= R_D2 <= R_D2^+ <= min{1,128a},
    a=sqrt(K^3/(K^4+1)).                                         (C)

## 2. Accepted interfaces, assumptions, notation, and local map

The primitive assumptions are precisely the finite legal homogeneous experiment, the stated parameter domains, arbitrary mu, existential stationary pi, all-pairs minorization (D), and the public information restriction. No generated event, regeneration, occupancy property or independent selected sample is assumed.



1. **S004 Lemma 2, arbitrary-start finite stacks.** With initial pair mu independent of independent row symbols `xi_(s,l)~theta_s`, the original full history is reproduced by consuming the next unused symbol of the current row. For each row, `C_s-n_s theta_s=S_(s,n_s)`, where `S_(s,n)=sum_(l=1)^n(e_(xi_(s,l))-theta_s)`. All deterministic prefixes through M exist in the accepted length-2M stacks. This is an exact full-history identity for arbitrary mu, not a conditional-IID statement. We use no S004 Holder/floor risk bound; the needed exponential concentration is proved locally in Lemma 1.
2. **S001 Section 3, stationary terminal occupancy.** For the SAME legal theta started at ANY stationary pi, and every integer departure length L>=1 and integer w>=1, the actual terminal count `J_L=sum_(i=0)^(L-1)1{Z_i=Z_L}` obeys

       P_pi(J_L<w)<=min{1,K^2 w/(L+1)}.                           (SO)

   The S001 proof/review were fully read. The suffix in Lemma 2 has precisely this marginal law conditional only on its first-success label. L=0 is NOT imported: it is proved separately in Lemma 3. No irreducibility, mixing, stationary-mass lower bound or conditional count independence is required.
3. **S011 Theorem S011 and Proposition 2, accepted lower interface.** In the exact arbitrary-start full-history common-algorithm class above, put

       i=min{1,sqrt(K/(M+1))},
       a_0=min{1,sqrt(K^3/(M+1))},
       F=max{i,min{1-beta,a_0}}.

   Then `R_D2>=F/180`. This is a stationary-subclass all-common-algorithm lower inherited through its accepted S006 interface, not a single-source add-one lower. S011's proof explicitly includes the stationary subclass before taking the algorithm infimum. Fixing public beta leaves every tested predictor a common history kernel. Its exact experiment, dependency statement and full lower inclusion were read with review/gate; earlier hard-family predecessors are inherited, not freshly recertified. Theorem 5 below proves F=a for ALL K>=2 on the exact critical sequence.

No new external literature result is invoked. Bounded-range concentration, finite splitting, scalar integration and all critical constants are proved here. The diagnostic is never cited as a mathematical premise.

| Local unit | Named statement / stable label | Contribution |
|---|---|---|
| unit_001 | Lemma 1, Unconditional simultaneous original-stack control (`lem:s018-stack`) | Finite MGF/sign union; on-event smoothed selected-row loss; epsilon paid unconditionally |
| unit_002 | Lemma 2, Exact full-history pair splitting (`lem:s018-split`) | All midpoints, exact tau weights, conditional-only-on-tau stationary suffix, count monotonicity |
| unit_003 | Lemma 3, Stationary capped negative moment (`lem:s018-moment`) | Integer-to-real event conversion, layer cake, L=0 |
| unit_004 | Theorem 4, Finite original-rule geometric bound (`thm:s018-geometric`) | Composition of TWO separate exact-law representations, no joint independence |
| unit_005 | Theorem 5, All-K critical matching (`thm:s018-critical`) | Exact constants/floors/parity, epsilon, no-success, inherited lower |

Public-facing quantities are the original class/risks/rule and the two displayed conclusions. The scalar epsilon is an analysis tolerance, not an algorithm input. `B_e,delta,r` are explicit deterministic expressions in public parameters. The stack event E, signs, sums, split labels, residual Q_2, tau, suffix counts, stationary comparison path Z and function `f_(B_e)(x)=min{1,2sqrt(B_e/(x+1))}` for x>=0 are proof-local objects constructed/proved in the indicated lemmas. Their bounds are derived, not assumptions. In Theorem 5, `h=floor(M/4)` is also proof-local. There are no free unspecified constants.

## 3. Local derivation

### unit_001: Lemma 1 — Unconditional simultaneous original-stack control (`lem:s018-stack`)

**Statement.** Fix any K>=2,M>=1, legal homogeneous theta, arbitrary mu, and 0<epsilon<1; no minorization is needed in this lemma. Let `B_e=K+ln(K^2M/epsilon)`. There is an exact-history row-stack realization and an event E with `P(E^c)<=epsilon` such that on E,

    loss(H)<=f_(B_e)(J),
    f_(B_e)(x)=min{1,2sqrt(B_e/(x+1))}, x>=0.

Consequently, under the ORIGINAL history law,

    E loss(H)<=epsilon+E f_(B_e)(J).                              (S)

**Proof: exact finite stacks.** Instantiate the accepted S004 interface with independent length-2M row stacks, independent of `Y_0~mu`. Its path identity can also be seen directly: a prescribed symbol prefix `x_1,...,x_(i+2)` fixes the initial pair and exactly each consumed stack prefix, so has probability

    mu(x_1,x_2) product_(t=0)^(i-1) theta_(x_(t+1),x_(t+2))(x_(t+3)).

This is the original path probability, including zero-probability paths; no conditioning on a null prefix is involved. The count identity holds on every generated path. Only deterministic row prefixes of lengths 1,...,M will enter the next argument.

**Bounded-range exponential MGF from primitives.** If a finite random variable V is supported in an interval [u,v] of length d, let `phi(lambda)=ln E exp(lambda(V-EV))`. Every tilted law has the same support. Its variance is at most `d^2/4`: writing m=(u+v)/2 gives `Var(V)<=E(V-m)^2<=d^2/4`, under that tilted law as well. Differentiating the finite positive sum gives `phi''(lambda)=Var_lambda(V)<=d^2/4`, while `phi(0)=phi'(0)=0`. Twice integrating from zero proves, for lambda>=0,

    E exp(lambda(V-EV))<=exp(lambda^2 d^2/8).

This includes a constant V (d=0); no variance or mass is divided by. Fix a deterministic row s, deterministic n in {1,...,M}, and deterministic sign vector `u in {-1,+1}^K`. Each centered summand of `<u,S_(s,n)>` is `u_(xi)-E u_(xi)`, has mean zero and range length at most 2. Independence of these deterministic stack coordinates and the MGF bound give

    E exp(lambda <u,S_(s,n)>)<=exp(n lambda^2/2).

For t>=0, exponential Markov followed by lambda=t/n gives

    P(<u,S_(s,n)> > t)<=exp(-t^2/(2n)).                           (3.1)

The identity `||v||_1=max_(u in {-1,+1}^K)<u,v>` holds for every real vector v: each term is bounded above by |v_c| and signs matching the coordinates attain their sum. Define E as the simultaneous event

    ||S_(s,n)||_1<=sqrt(2nB_e)
       for ALL K^2 rows s and ALL deterministic n=1,...,M.

A union bound over exactly K^2 M 2^K choices in (3.1) gives

    P(E^c)<=K^2 M 2^K exp(-B_e)
           =epsilon exp(K(ln 2-1))<=epsilon.                     (3.2)

Here ln 2<1, for example by integrating 1/x<1 over (1,2). This probability is UNCONDITIONAL under the row product construction and its arbitrary original initial law. No estimate on `P(E^c | Y_M,J,tau,midpoint)` is made or needed.

**Selected row, smoothing and zero counts.** On E, for every row with n>=1, its empirical vector `p_hat=C_s/n` has

    TV(p_hat,theta_s)=||S_(s,n)||_1/(2n)
                    <=sqrt(B_e/(2n))<=sqrt(B_e/(n+1)),

since n+1<=2n. Let u_K be the uniform probability. The exact identity

    p_s^+=[n/(n+K)]p_hat+[K/(n+K)]u_K

gives `TV(p_s^+,theta_s)<=TV(p_hat,theta_s)+K/(n+K)`. For n>=1,

    K/(n+K)<=sqrt(K/(n+1))<=sqrt(B_e/(n+1)).

The first inequality after squaring is `K(n+1)<=(n+K)^2`, whose difference is `n^2+Kn+K^2-K>=0`; the second uses `B_e>=K` (indeed K^2M/epsilon>1). Thus, with the probability-vector cap one, the loss at EVERY row and count is at most `f_(B_e)(n)`. At n=0, the add-one vector is u_K and loss<=1=`f_(B_e)(0)`, since B_e>=K>=2. No empirical row with zero denominator is formed.

Because E is simultaneous BEFORE selection, the inequality holds at the actual dependent row `Y_M` and its actual count J without conditioning. Finally,

    E loss <= E[loss 1_E]+P(E^c)
            <=E[f_(B_e)(J)1_E]+epsilon
            <=E f_(B_e)(J)+epsilon.

Exact equality of the original and stack history laws transfers both expectations to the original experiment, proving (S). ∎

### unit_002: Lemma 2 — Exact full-history pair splitting (`lem:s018-split`)

**Statement.** Under Section 1, let r=floor(M/2). There is a SECOND exact-history auxiliary construction with independent Bernoulli(beta) block labels and first successful block tau in {1,...,r} (tau=infinity if none), such that

    P(tau=j)=beta delta^(j-1),     P(tau=infinity)=delta^r.          (3.3)

Conditional ONLY on tau=j, the suffix `(Y_(2j),...,Y_M)` has the ordinary length `L_j=M-2j` stationary P-path law. With the SAME actual endpoint define

    J_suffix,j=sum_(i=2j)^(M-1) 1{Y_i=Y_M}.

Then J>=J_suffix,j pathwise. In particular, for the decreasing bounded function in Lemma 1,

    E f_(B_e)(J)
      <=delta^r+sum_(j=1)^r beta delta^(j-1)
                   E_pi f_(B_e)(J_(M-2j)).                       (3.4)

Here the left expectation is under the original history law, and `J_L` on the right is the actual terminal count of an ordinary stationary P experiment with L departures, including J_0=0.

**Proof: normalized residual and full observed history.** Let `Pi(s,z)=pi(z)` and

    Q_2(s,z)=(P^2(s,z)-beta pi(z))/delta.

All entries are nonnegative by (D), delta>0, and every row sum is `(1-beta)/delta=1`. Also `pi Q_2=pi`, although no residual-path stationarity is needed. Importantly Q_2 is a TWO-STEP pair kernel, not a claimed one-departure legal symbol table.

Draw Y_0 from mu. For blocks k=1,...,r draw mutually independent labels I_k with `P(I_k=1)=beta`, independent of all sampling randomness and Y_0. Given the pair s at time 2k-2, on success draw the endpoint at time 2k from pi using fresh randomness independent of the history through pair time 2k-2; on failure draw it from Q_2(s,.) using fresh randomness. If s=(a,b) and this endpoint is z=(c,d), reconstruct the midpoint deterministically as (b,c), so the complete block is

    (a,b) -> (b,c) -> (c,d),

and append BOTH observed symbols c,d. This is the unique legal two-step route: the first shift must leave second coordinate b as the next first coordinate; the second endpoint forces the newly emitted first symbol to be c. Its marginal block probability is exactly

    beta pi(c,d)+delta Q_2((a,b),(c,d))
       =P^2((a,b),(c,d))=theta_ab(c)theta_bc(d).                   (3.5)

If this product is zero, nonnegativity forces BOTH beta pi(c,d) and delta Q_2(s,(c,d)) to be zero, so a forbidden/zero-probability block is never selected. No bridge distribution or division by P^2 or pi is used. If M is odd, append one final ordinary theta departure from Y_(2r), using independent fresh randomness. If M is even, no final departure is added.

For any complete symbol history, multiply its initial-pair probability, each block factor in (3.5), and its possible final one-step factor. The result is exactly

    mu(x_1,x_2) product_(i=0)^(M-1) theta_(x_(i+1),x_(i+2))(x_(i+3)),

the full ORIGINAL symbol-history law. Every observed midpoint is retained; matching just the even skeleton would not suffice. Conditional on labels the process need not have one-step kernel P, but its unconditional complete history has precisely the fixed homogeneous theta law. The original source is not changed within a trajectory.

**First success and the exact suffix identity.** Set tau=min{k:I_k=1}, with infinity for no success. Independence of labels gives (3.3), also when r=0 (no-success probability one). For any j<=r and any prescribed legal suffix path `z_0,...,z_(L_j)`, the construction gives the EXACT joint identity

    P(tau=j, (Y_(2j),...,Y_M)=(z_0,...,z_(L_j)))
      =beta delta^(j-1) pi(z_0)
                       product_(ell=0)^(L_j-1) P(z_ell,z_(ell+1)). (3.6)

To verify it, condition on the first j-1 failure labels. Their residual Q_2 endpoint path, starting at mu, has total probability one after summing its prefixes. At block j, the success endpoint has probability pi(z_0) regardless of that starting pair. The intervening midpoint is reconstructed and then summed as part of the unrestricted prefix; no midpoint restriction is imposed. The label factor is beta delta^(j-1). All later labels remain unconstrained and independent; marginalizing each future block gives exactly (3.5), and an odd final step gives P. Thus the remaining factors are the displayed ordinary path product. Illegal suffixes have zero mass on both sides. If L_j=0, the product is empty and equals one.

Dividing (3.6) by its strictly positive label probability proves the stated conditional suffix law. Since pi is stationary, this is a stationary path in exactly the S001 sense. It does NOT assert that the suffix remains stationary conditional on the full observed prefix or on the observed midpoint at time 2j-1. That midpoint contains the first coordinate of Y_(2j), and such conditioning can reveal endpoint information. We use only conditioning on tau=j.

**Count comparison and geometric integration.** For every full history and every j, the suffix count sums a subset of the terms defining J, with exactly the same Y_M; hence J>=J_suffix,j. The function f_(B_e) is nonincreasing and lies in [0,1], so on tau=j,

    f_(B_e)(J)<=f_(B_e)(J_suffix,j).

On no success, simply bound f_(B_e)(J)<=1. Partitioning expectation by tau, using (3.3) and the conditional marginal (3.6), gives (3.4). No prefix observations are discarded from the estimator; the suffix is only an analytical count comparison. ∎

### unit_003: Lemma 3 — Stationary capped negative moment (`lem:s018-moment`)

**Statement.** Let K>=2, B_e>=K and integer L>=0. For any legal homogeneous theta and any stationary law pi, let J_L be its length-L actual terminal count, with J_0=0. Then

    E_pi f_(B_e)(J_L)<=min{1,4K sqrt(B_e/(L+1))}.                  (3.7)

**Proof.** First suppose L>=1. The accepted S001 occupancy interface (SO) applies to this same theta, pi, L and actual endpoint, with `c=K^2/(L+1)`. For 0<t<1, set x=4B_e/t^2. The exact event is

    {f_(B_e)(J_L)>t}={J_L+1<x}={J_L<ceil(x)-1}.

Indeed J_L is integer: if x is integer the threshold is x-1, whereas between successive integers the threshold is the lower integer. The integer `w=ceil(x)-1` is positive because x>4B_e>=8, and satisfies w<x in both cases. Applying (SO) at THIS integer w gives

    P(f_(B_e)(J_L)>t)<=min{1,cw}<=min{1,4B_e c/t^2}.             (3.8)

There is no unsupported real-threshold substitution. Layer cake, valid for this bounded nonnegative random variable, follows directly by integrating `1{t<f_(B_e)(J_L)}` over t in (0,1) and interchanging a finite sum and integral. Write z=4B_e c>0. The scalar integral is

    integral_0^1 min{1,z/t^2}dt
      =1                              if z>=1,
      =sqrt(z)+z(1/sqrt(z)-1)
       =2sqrt(z)-z                    if 0<z<1.

In either case it is at most one and at most 2sqrt(z). Consequently (3.8) yields

    E_pi f_(B_e)(J_L)<=min{1,2sqrt(z)}
                     =min{1,4K sqrt(B_e/(L+1))}.

If L=0, no departure is counted: J_0=0 regardless of the sampled endpoint. The left side is one because B_e>=2, and the right side is also one because `4Ksqrt(B_e)>=1`. This proves the separate zero-length case, including a sparse pi. ∎

### unit_004: Theorem 4 — Finite original-rule geometric bound (`thm:s018-geometric`)

**Statement.** Under Section 1, for every analysis epsilon in (0,1), the ORIGINAL full-history rule satisfies (G).

**Proof.** Fix one theta, mu and witnessing pi in the source class. On the first row-stack auxiliary space, Lemma 1 proves

    E_original loss<=epsilon+E_original f_(B_e)(J).

This is already an inequality between expectations under the ORIGINAL complete-history law. On the second pair-split auxiliary space, Lemma 2 bounds that same original scalar expectation by its geometric stationary-suffix mixture. Lemma 3 bounds each stationary expectation at L=M-2j, including L=0. Therefore

    E_original loss<=epsilon+delta^r
       +sum_(j=1)^r beta delta^(j-1)
                      min{1,4Ksqrt(B_e/(M-2j+1))}.

There is no joint construction of stack event E and split labels: none is needed. In particular no independence between E and tau is presumed, and epsilon is never divided by a label probability. Equality of the complete-history pushforward laws is the sole bridge between the two spaces.

Every bound is uniform in theta, mu and pi; the final expression contains only K,M,beta,epsilon. Loss<=1 supplies the outer cap. Take the source supremum to obtain (G). The original rule is a common admissible deterministic algorithm, so separately `R_D2<=R_D2^+`. At M=1, r=0, delta^0=1 (delta>0), and the capped expression is one; this is a genuine boundary case, not an omitted suffix. ∎

### unit_005: Theorem 5 — All-K critical matching (`thm:s018-critical`)

**Statement.** Fix exactly `M=K^4,beta=ln(K)/K^4` for any integer K>=2. Then (C) holds with the stipulated universal constants 1/180 and 128; no constant correction or sufficiently-large-K restriction is needed.

**Proof: admissibility and scalar budget.** For x>1, `ln x=integral_1^x du/u < x-1 < x`. Thus `0<beta<K^-3<=1/8<1`. Also M>=16 and

    a=sqrt(K^3/(M+1))<K^(-1/2)<=1/sqrt(2)<1,

so the S011 a_0 is uncapped here. Choose epsilon=1/K in Theorem 4. It lies in (0,1), and

    B_e=K+ln(K^2 K^4 K)=K+7ln K<=4K.                            (5.1)

For a complete finite justification, the derivative of ln x/x is `(1-ln x)/x^2`, so its maximum on x>0 is 1/e at x=e. Moreover `e>1+1+1/2=5/2>7/3`, hence `1+7/e<4`. This proves (5.1), with room to spare. The basic upper bound e<3 follows from `n!>=2^(n-1)` for n>=2, strictly for n>=3, and summing the exponential series; in particular `exp(1/2)<sqrt(3)<2`. These elementary constants will also cover the no-success atom.

Put `r=floor(M/2)` and `h=floor(M/4)`. By (5.1), each stationary-suffix term in (G) is bounded by

    min{1,8sqrt(K^3/(M-2j+1))}.                                 (5.2)

**Early success j<=h.** For every such j,

    M-2j+1>=M/2+1>=(M+1)/2.

Thus (5.2) is at most `8sqrt(2)a`. The weights are nonnegative with

    sum_(j=1)^h beta delta^(j-1)=1-delta^h<=1.

The total early contribution is therefore at most `8sqrt(2)a`. Nothing requires this bound to be less than one.

**Late success h<j<=r, with exact parity denominators.** Here j-1>=h and `delta^(j-1)<=delta^h`. The positive integers `M-2j+1` are distinct. If M is even, the final one is 1 and corresponds to the L=0 atom proved in Lemma 3; if M is odd, the final one is 2 and the last ordinary departure has L=1. In both cases the denominators form a subset of {1,...,M}, so

    sum_(j=h+1)^r (M-2j+1)^(-1/2)
      <=sum_(ell=1)^M ell^(-1/2)
      <=1+integral_1^M x^(-1/2)dx
      =2sqrt(M)-1<=2sqrt(M).                                   (5.3)

The integral comparison holds because x^(-1/2) is decreasing; each ell>=2 term is at most its integral over [ell-1,ell]. Enlarging (5.2) by its uncapped square-root branch, including its shortest-suffix atoms, gives

    late <=8 beta delta^h K^(3/2) [2sqrt(M)]
          =16 (ln K)delta^h sqrt(K^3/M)
          <=16sqrt(2)a (ln K)delta^h,                            (5.4)

because `sqrt(K^3/M)/a=sqrt((M+1)/M)<=sqrt(2)` for M>=1.

The inequality `ln(1-beta)<=-beta` follows by integrating `1/(1-u)>=1` over u in [0,beta]. Since `h>=M/4-1`,

    delta^h<=exp(-beta h)<=exp(beta) K^(-1/4).

For x>=1, writing y=ln x gives `(ln x)x^(-1/4)=y exp(-y/4)`. Its derivative in y is `exp(-y/4)(1-y/4)`, so the maximum is 4/e at y=4. Since beta<1, `exp(beta)<e`; hence

    (ln K)delta^h<=exp(beta)(ln K)K^(-1/4)<=4.                    (5.5)

Equations (5.4)–(5.5) give the claimed late budget `64sqrt(2)a`. No near-terminal success is deleted or assigned a uniformly long suffix.

**No success and epsilon.** Integer parity gives `r>=M/2-1/2` (equality for odd M), so

    delta^r<=exp(-beta r)<=exp(beta/2)K^(-1/2)
            <2K^(-1/2)<3a.                                    (5.6)

For the last strict inequality,

    [2K^(-1/2)]/a=2sqrt(1+K^-4)<=2sqrt(17/16)=sqrt(17)/2<3.

Also epsilon<=a: after squaring, `1/K^2<=K^3/(K^4+1)` is exactly `K^4+1<=K^5`, which holds because `K^4(K-1)>=16>1` for K>=2. These are all-K inequalities.

Combining the four contributions in (G),

    epsilon+delta^r+early+late
       <=(4+72sqrt(2))a<128a,                                  (5.7)

where, for example, `sqrt(2)<3/2` gives `4+72sqrt(2)<112<128`. The theorem's cap one covers small K without adding a threshold. This proves the upper in (C) for the unchanged original algorithm.

**Accepted lower at exactly these finite parameters.** The admissibility bound already proved `beta<K^-3<=1/8`, so delta>7/8. On the other hand `a<K^-1/2<=1/sqrt(2)<7/8`, the final inequality following from `1/2<49/64`. Thus min(delta,a)=a. Furthermore `i=sqrt(K/(K^4+1))=a/K<=a`, uncapped. S011's exact quantity is therefore F=a for EVERY integer K>=2, not only asymptotically. Its accepted common-algorithm lower gives `R_D2>=a/180`. The admissibility of the original rule gives the middle inequality `R_D2<=R_D2^+`; no additional lower family or source-dependent algorithm choice is involved. This completes (C). ∎

## 4. Target-step assembly and dependence audit

The noncircular assembly is:

1. S004 exact original-source stacks plus the locally proved deterministic-sign MGF/union and smoothing give Lemma 1's unconditional `E loss<=epsilon+E f_(B_e)(J)`.
2. All-state (D), the UNIQUE legal midpoint and independent block labels give Lemma 2's EXACT full-history split realization, conditional-only-on-tau suffix marginal and literal count floor.
3. S001 stationary occupancy with the exact integer threshold gives Lemma 3's capped negative moment; L=0 is locally proved.
4. Equality of the two original-history pushforward laws, not a coupling/independence assertion between auxiliary labels, composes these results into Theorem 4.
5. Theorem 5 supplies every finite scalar inequality and matches the S011 lower through the explicit identity F=a.

The good-event failure is paid ONCE and unconditionally. We never apply a stack concentration bound to the source conditioned on successful splitting. We never assert iid observations conditional on a selected terminal row or count. We never assert stationarity conditional on the observed midpoint or full prefix. The split labels, theta, mu, pi and Q_2 are analysis-only. The actual estimator remains the exact displayed add-one formula on all original counts.

This method deliberately replaces the old L4/Holder handling of an additive occupancy floor. A finite simultaneous loss/count bridge permits paying the no-success probability with its full exponent. That is an analytical improvement, not permission to turn a symbol refresh into a stationary pair or to improve the state-TV mixing envelope.

## 5. Boundary, obstruction, baseline and information audit

- **M=1:** no pair blocks, empty sum, no-success probability one; Theorem 4 gives the risk cap. The stack event still covers its single deterministic length. No stationary L=1 claim is inserted into an unregenerated path.
- **Even/odd M:** all two-symbol blocks preserve their middle observed pairs. An odd final departure is generated by the original theta. Even final success yields the L=0 count atom, explicitly bounded by one. Denominators are always positive; the final values 1 and 2 are retained in (5.3).
- **Zero counts:** `f_(B_e)(0)=1`; no empirical zero denominator is used. Add-one's denominator is always n+K>0.
- **Zeros and sparse pi:** Q_2 is defined by division only by delta>0, never pi(z) or P^2(s,z). When the original block probability vanishes, both mixture components vanish. Zero-pi states are harmless in the stationary suffix and remain covered under arbitrary mu before regeneration.
- **Singular mu/off-support starts:** (D) is required for EVERY starting pair, exactly what makes Q_2 stochastic from every possible initial state. No density ratio or absolute continuity is assumed.
- **Fixed source/full observations:** the auxiliary block mixture recovers every original full-history probability, not just its even skeleton. The same theta defines the actual terminal target throughout. No source switch, external clock or extra sample is introduced.
- **S013 exact slow state-TV:** its accepted `delta^floor(t/2)` envelope obstruction is respected. Our no-success term is precisely `delta^floor(M/2)`, not delta^M or a faster exponential. We make no statistical lower from state-TV, consistent with its known-family zero-loss predictor.
- **S014 canonical SYMBOL refresh:** the canonical one-step decomposition uses the stationary symbol marginal p and replaces only the emitted symbol; its new pair is `(old_second,new_symbol)` and need not have law pi. S014's product-start/immediate-refresh counterexample remains valid. Our analytical success samples a FULL pair at an even endpoint under the different two-step kernel; the midpoint depends on that pair and is retained. We claim stationarity only after marginalizing that midpoint/prefix and conditioning solely on tau=j. We claim no after-canonical-refresh bound and do not transfer the accepted no-refresh event upper to its complement.
- **S015 harmless symbol refreshes:** its canonical `C_ref` can occur while the star remains statistically active. No identification or implication between C_ref and our pair-split success is made. At its distinct `beta=ln K/(4K^4)` sequence the retained no-pair-success term is of order K^-1/8, not the stationary scale K^-1/2; thus this proof does not imply either refuted `O(a+sqrt(beta))` canonical aggregate bound or `O(a+delta^M g+sqrt(beta))` total bound. Its family-only upper is not promoted to a class upper.
- **S017 old certificate:** its accepted critical statement concerns the numerical value/order of the OLD optimized S011 certificate U, not a lower bound on true risk. That certificate remains `Theta(a sqrt(ln K/ln ln K))` on its critical domain. The new theorem gives a sharper original-rule certificate on only the exact contracted `rho=4,gamma=1` sequence. It changes no old numerical optimization result and draws no unproved extension to other rays.
- **Stationary and fast-mixing baselines:** accepted S001/S004 results remain independently available. The geometric expression is a further, sometimes conservative bound; it need not reproduce the sharper S001 constant 48 when mu happens already to equal pi. No baseline theorem is revoked or replaced by a weaker expression. It is not claimed optimal at beta near one.
- **Beta endpoints:** Theorem 4 assumes 0<beta<1 and does not define Q_2 at beta=1. Accepted unrestricted beta-zero and pooled IID beta-one statements remain unchanged. No general q or unknown-beta result is asserted.
- **Loss and quantifiers:** all risk bounds are finite deterministic-horizon EXPECTED half-L1 TV at the actual terminal row, not squared TV, predictive KL, a random-time risk, an independent test query or a conditional-risk theorem. One fixed source is used within each path; the supremum may vary it with public parameters. Original add-one is one common rule, while the S011 lower applies to every common possibly randomized rule before infimization.

## 6. Explicit rate audit and proof status

The finite bound exposes all K,M,beta,epsilon dependence and every short-suffix/no-success term. The only extra logarithm is explicit in `B_e=K+ln(K^2M/epsilon)`; on the exact assigned polynomial horizon epsilon=1/K gives `B_e<=4K`, so no logarithmic rate loss is needed there. The constants 2 (loss/count), 4 (stationary negative moment), 8sqrt(2) (early), 64sqrt(2) (late), 3 (no success), 1 (epsilon), and final 128 have local derivations. The lower 1/180 is the named accepted S011 interface. No constant depends on source, initialization, hidden stationary law or estimator.

The auxiliary labels are finite and never observed by the algorithm. The stack event uses only deterministic finite rows/lengths before selection. The layer-cake integral is of a bounded variable and uses exact integer-event conversion. All mixture sums are finite; only the elementary scalar exponential-series comparison for e uses a convergent numerical series. No interchange of source supremum with a hidden minimization is used.



The script uses exact Fraction arithmetic for four binary sources (uniform IID, non-IID uniform-stationary checkerboard, sparse absorbing, sparse IID), two initial laws (including a point mass singular to sparse pi), beta=1/5, and M=1,...,7. It checks the full symbol-history marginal of the split construction, exact first-success weights, complete stationary suffix distribution conditional only on each tau=j, and the same-endpoint count comparison. Output: **56 experiments, 1,590 direct histories, 5,742 augmented atoms, 96 exact conditional suffix-law identities, 4,176 pathwise count comparisons, and 336 integer occupation-mixture checks — all PASS.** Both odd/even horizons and zero-length suffixes are included.

It also checks 8,000 exact rational strict-event threshold identities (including integer x), 9,900 integer squared-smoothing inequalities, 96 small-horizon stationary capped-moment comparisons, and the displayed deliberately slack critical scalar inequalities for K=2,...,10,000. Moment/scalar comparisons use Python floating point; the small-horizon moment cap is conservative and these checks do not test an infinite-range moment theorem. None of the checks replaces the symbolic proofs, constitutes independent review, or establishes all-source/all-K validity by enumeration.




