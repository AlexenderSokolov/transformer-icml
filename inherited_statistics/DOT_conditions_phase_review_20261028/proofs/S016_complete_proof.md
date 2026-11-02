# S016 全参数弱混合下包络 完整证明

编排说明（非原文）：本文件是已接纳版本的完整科学正文副本，保留全部局部证明或对应独立审查推理；身份、控制记录、原提交状态及管理性来源哈希表另行省略。原件不修改。以下英文原文的年代与结论范围保持不变，本次编排不构成新的数学审查。原编号可能跳跃；完整来源与新增／删略区间见 SOURCES.md、COPY_MAP.json。

历史口径（非原文）：S016、S017 关于未获新的原规则上界、临界统计间隙的说法属于当时结果；S018 只闭合精确临界序列。S019 已进一步在 1≤M≤K⁴、0≤β≤1/2 上闭合原规则与共同 minimax 的 H 匹配，包含 S017 全部固定射线。当前综合结论以外层中文导读及该明确接纳范围为准。旧数值证书的数学结论没有被推翻。

原文内 Section 7/9 的来源身份表等管理交叉引用，统一由本包 SOURCES.md 的同名原件身份与依赖入口补足；其省略不删除被引用的科学接口。有限检查叙述是原作者／原独立审查已执行的历史事实，本次装配未重跑这些数学检查。检查脚本与运行结果在原研究记录保留，不随科学包公开；定理依据完整符号证明而非有限枚举。

In the unchanged arbitrary-start, legal order-two, full-history, actual-terminal expected-TV experiment, for every integer `K>=2,M>=1` and public `beta in [0,1]`, define

    n=M+1, delta=1-beta,
    i=min(1,sqrt(K/n)), a=min(1,sqrt(K^3/n)),
    g=min(1,sqrt(K^5/n)), hstar=min(1,sqrt(K^4/n)),
    F=max(i,min(delta,a)), D=delta^n g, T=delta^(M/2) hstar.

Then

    R_D2(K,M,beta) >= 2^-17 max(F,D,T).                              (S016)

Both beta endpoints are defined directly below. This is a **standard derived envelope** from actually accepted S006/S011/S012/S015, not a new source construction or a full joint minimax formula. The new finite bridge pays the star clock's exact phase/count penalty only in the parameter region `T>F`; elsewhere the existing floor covers T. The inherited S012 bounds `F/180` and `2^-16 D`, the stronger IID floor, and the original beta-zero baseline are retained, not replaced by the conservative common constant in (S016).

Separately, the accepted S011 public selector still gives `R_D2<=U`. Its original/suffix/pooled assignments are unchanged. No global matching of the new lower and U, and no new original-add-one upper, is claimed.



## 2. Exact experiment, theorem and assumption provenance

Let `A={0,...,K-1}`. A source has a fixed homogeneous probability table `theta=(theta_ab(c))`, with every row nonnegative and normalized. Its pair kernel has exactly the legal transitions

    P_theta((a,b),(b,c))=theta_ab(c),

and zero on non-shift transitions. The initial pair law mu is arbitrary. The class `D_K(2,beta)` consists of `(theta,mu)` such that some hidden probability pi on `A^2` satisfies

    pi P_theta=pi,      P_theta^2(s,t)>=beta pi(t) for EVERY s,t in A^2. (1)

Zero transitions, sparse stationary mass, reducibility, and mu singular to pi are permitted. Beta is a public lower bound, not an oracle giving an exact source coefficient. At fixed `K,M,beta`, the source can vary in the supremum, but it remains unchanged during one trajectory.

Observe all `H=(X_1,...,X_(M+2))`, put `Y_j=(X_(j+1),X_(j+2))` for `0<=j<=M`, and retain all M observed departures. A common predictor B is a probability kernel from the full H to the K-simplex. It may use public `K,M,beta` and an independent seed, but not theta, mu, pi, hidden signs, refresh/phase labels, or future symbols. The target is the actual same-trajectory terminal row `theta_(Y_M)` for unobserved `X_(M+3)`. Define

    L_B(theta,mu)=E TV(B(H),theta_(Y_M)),     TV(p,q)=(1/2)||p-q||_1,
    R_D2(K,M,beta)=inf_B sup_((theta,mu) in D_K(2,beta)) L_B(theta,mu).  (2)

Theorem S016 is (S016) for (1)–(2) on the full closed parameter domain. For `0<delta<=1`, real powers mean `delta^r=exp(r log(delta))`. The exponents n and M/2 are strictly positive. At beta zero set `D=g,T=hstar`; at beta one set `D=T=0`. Thus no `0^0`, limit convention, or null-event conditioning is needed.

The only primitive assumptions are the experiment, parameter domains, legal homogeneous table, arbitrary initialization, all-state minorization and information restriction just stated. The source setting does not assign stable primitive assumption IDs, so their content is recorded without invented upstream IDs. Exact star membership, full-history testing and the count/amplitude interfaces are accepted derived conclusions, not new assumptions. The inequality `T>F` is a public deterministic condition used in a local case of an exhaustive proof, not a generated event or extra theorem hypothesis.

## 3. Cited result applications



Each lower holds for every fixed common randomized B before taking the algorithm infimum. Fixing the public `K,M,beta` therefore leaves one admissible kernel in each predecessor's universal quantifier.

### 3.1 Accepted stationary IID floor

S006 Lemma 3 (`lem:s006-iid`) gives, from its explicit stationary IID family with all `M+2` informative symbols retained,

    sup_((theta,mu) in D_K(2,beta)) L_B(theta,mu) >= i/(32 sqrt(6))       (3)

for every common B and every beta. The source mapping is all rows equal to an unknown p, with `mu=pi=p tensor p`. Its legal kernel satisfies `P^2(s,(c,d))=p(c)p(d)=pi(c,d)`, so these witnesses belong to every present class, including the arbitrary-mu class. This is a valid subclass inclusion of actual stationary witnesses, not a restriction of a larger-class lower in the wrong direction. The public beta is the same across each tested family; no hidden p is provided to B.

### 3.2 Accepted absorbing lower and endpoint baselines

S012 Theorem S012 and Proposition 6 (`prop:s012-allk`) apply to precisely (1)–(2) and state

    sup_((theta,mu) in D_K(2,beta)) L_B(theta,mu)
       >= max(F/180, 2^-16 D).                                      (4)

Its proof/review preserve both caps, small K, all public beta and every common full-history randomized predictor. We inherit this result, including its full-data testing, rather than re-proving or altering the absorbing family.

S011 Proposition 5 (`prop:s011-endpoints`), also preserved in S012 Proposition 6, gives the exact endpoints:

    beta=0:  2^-16 g <= R_D2 <= R_D2^+ <= u_g(M) <=48g;
    beta=1:  i/(32 sqrt(6)) <= R_D2
                 <=min(1,(1/2)sqrt(K/M)) <=i.                        (5)

Here `R_D2^+` is the worst risk of unchanged full-history add-one, and `u_g` is defined in Section 7. At beta zero every finite stochastic kernel has a stationary probability and (1) is vacuous, so the accepted general baseline genuinely applies. At beta one the legal two-step identity, summed over its final coordinate, forces every theta row equal to one hidden p; arbitrary mu remains allowed. The lower there uses stationary IID witnesses with all M+2 observations, while the upper may pool just the M transition outputs. No observation is discarded from a lower experiment. These accepted endpoint conclusions are retained with their original constants.

### 3.3 Accepted star-clock finite interface

For `K>=13,M>=1,0<beta<1`, S015 Propositions 6 and 7 (`prop:s015-lower`, `prop:s015-count`) supply lawful sources in the identical class, with a common sign-independent horizon-aligned initial law. Define the public integers and amplitude

    m=floor((K-1)/4), L=2m, q=floor(M/L),
    alpha=min(1/2, sqrt(m^3/(q+1))/8).

Write `M=qL+d`, `0<=d<L`, and `k=(2-d) mod L`. With the accepted vulnerable phase set

    V_phase={0,1,2,4} union {6,8,...,L-2},
    r_M=sum_(j=0)^(d-1) 1{(k+j) mod L in V_phase},
    H_M=q(m+1)+r_M,

the empty sum is zero and the accepted conclusions are

    sup_((theta,mu) in D_K(2,beta)) L_B(theta,mu)
        >= delta^(H_M+1) alpha/8,                                    (6)
    |H_M-M(m+1)/L|<=L,
    alpha/8 >= 2^-12 hstar.                                          (7)

The supremum bound follows from S015's single finite-prior lower for every B. Its accepted full-history bijection keeps initial and overlapping-symbol information; its actual-endpoint testing includes the changed target contrast delta; the latent coin event has exact common mass `delta^H_M`. The `+1` in (6) therefore cannot be removed. Its sources are homogeneous legal pair shifts, satisfy (1) from every pair, and leave all source signs and coin labels hidden. All present uses satisfy its stated finite domain. We do not use its restricted-family upper as a full-class upper, its separate asymptotic result, or any diagnostic as a premise.

For clarity about all inherited amplitude caps: the S015 proof handles q=0 by `m>=3`, `m^3>=27>16`, giving `alpha/8=1/16`. If q>=1, then `q+1<=2q<=M/m` and `m>=K/8`; with `t=sqrt(m^3/(q+1))`, `z=sqrt(K^4/n)`, it obtains `t>=z/64`, `alpha/8>=min(1,t)/64`, and `min(1,t)>=min(1,z)/64`. Thus (7) covers both alpha branches and both hstar caps. These are the accepted finite calculations, not an asymptotic substitution.

### 3.4 Accepted algorithm-separated upper

S011 Theorem S011 and Proposition 2 (`prop:s011-envelope`) apply to exactly (1)–(2) and give `R_D2<=U`, attained as a uniform certificate by a deterministic public selector. Section 7 reproduces its formulas and assignments. This is inherited intact; S016 supplies no upper proof or source-specific algorithm choice.

## 4. Local lemma map

| Local unit | Named result / stable label | Contribution |
|---|---|---|
| unit_001 | Lemma 1, Endpoint and small-parameter coverage (`lem:s016-small`) | Direct beta endpoints, M=1, small K and cap comparisons |
| unit_002 | Lemma 2, Dominance forces slow hazard (`lem:s016-dominance`) | On T>F derive F=a<1, M>=K^3 and exact logarithmic control |
| unit_003 | Lemma 3, Finite star phase-penalty absorption (`lem:s016-absorb`) | Pay H_M overhead, both floor bounds, uniform exp(-3)>1/32 |
| unit_004 | Proposition 4, All-parameter maximum assembly (`prop:s016-envelope`) | Combine inherited floors with new T control before infimum |

## 5. Local derivation

### unit_001: Lemma 1 — Endpoint and small-parameter coverage (`lem:s016-small`)

**Statement.** Under the full setting and accepted interfaces (3)–(5), the conclusion (S016) holds whenever beta is 0 or 1, M=1, or `2<=K<=12`. The inherited stronger baseline bounds remain valid.

**Proof.** Monotonicity of the capped square root and `K<=K^3<=K^4<=K^5` give

    0<i<=a<=hstar<=g<=1,       0<=D<=g,       0<=T<=hstar<=g.          (8)

At beta zero, `delta=1`, so `F=max(i,a)=a`, `D=g`, `T=hstar`. Equation (8) gives `max(F,D,T)=g`. The accepted general lower `2^-16 g` from (5) proves the requested weaker common-constant bound, and is explicitly retained as the sharper baseline.

At beta one, `delta=0`, the direct definitions give `D=T=0`, and `F=i`. Equation (3) proves (S016) because `sqrt(6)<3`, so `32 sqrt(6)<96<2^17`. The positive IID floor and pooled upper in (5), rather than the vanishing transient terms, continue to describe this endpoint.

If M=1, then n=2 and K>=2 imply `i=1`, so `F=1`. By (8), D,T<=1, and (4) yields `R_D2>=1/180>=2^-17 max(F,D,T)`. This handles the fractional exponent M/2=1/2 without using the later inequality `delta^(M/2)<=delta`.

Finally let `2<=K<=12`, with any M and beta. Set `x=sqrt(K/n)>0`. The exact cap inequality

    min(1,K^2 x)<=K^2 min(1,x)

holds because if x>=1 the right side is K^2>=1, whereas if x<1 the left side is at most K^2 x. Thus

    hstar<=g=min(1,K^2 x)<=K^2 i<=144i.

By (3), for every fixed B its class supremum is at least

    i/(32 sqrt(6)) >= g/(144*32 sqrt(6)) >2^-16 g >=2^-16 T.          (9)

The strict numerical comparison is exact: `sqrt(6)<3` and `144*32*3=13824<65536=2^16`. Together with (4), all three terms are controlled with constants at least `2^-17`. Their maximum is therefore bounded as required; their risks are not added. This proves all stated small-parameter cases. ∎

### unit_002: Lemma 2 — Dominance forces slow hazard (`lem:s016-dominance`)

**Statement.** Under the rate definitions with `K>=13,M>=2,0<beta<1`, if `T>F`, then

    delta>=a,    F=a<1,    M>=K^3,
    hstar/a<=sqrt(K),     -log(delta)<log(K)/M.                       (10)

**Proof.** Here `0<delta<1` and `M/2>=1`. If delta<a, then

    T=delta^(M/2) hstar <=delta<=max(i,delta)=F,

where the first inequality uses hstar<=1 and `delta^(M/2)<=delta`. This contradicts T>F, so delta>=a. Since i<=a, we now have `F=max(i,a)=a`. Also `a<=delta<1`, hence the cap in a is inactive: `a=sqrt(K^3/n)<1`, so `n>K^3`. Both n and K^3 are integers and n=M+1, giving `M>=K^3`, including equality.

To check the hstar cap explicitly, if `n<=K^4`, then `hstar=1` and

    hstar/a=sqrt(n/K^3)<=sqrt(K).

If `n>=K^4`, then `hstar=sqrt(K^4/n)` and the ratio is exactly sqrt(K). The common boundary is consistent. Thus `a/hstar>=K^-1/2`, and both a,hstar are strictly positive.

The strict dominance now gives

    delta^(M/2)>a/hstar>=K^-1/2.

The logarithm is increasing on positive numbers; taking logarithms and multiplying by -1 yields

    (M/2)(-log(delta))<(1/2)log(K).

Division by M/2>0 proves (10). No approximation `-log(delta)≈beta` has been used. ∎

### unit_003: Lemma 3 — Finite star phase-penalty absorption (`lem:s016-absorb`)

**Statement.** Under the full setting, the accepted star interface (6)–(7), and the local conditions `K>=13,M>=2,0<beta<1,T>F`, every fixed common B satisfies

    sup_((theta,mu) in D_K(2,beta)) L_B(theta,mu) >2^-17 T.            (11)

More explicitly, with the exact accepted H_M,

    delta^(H_M+1)
       >=delta^(M/2) exp[-4log(K)/K -(K/2+1)log(K)/K^3]
       >=exp(-3) delta^(M/2).                                      (12)

**Proof: the exact overhead.** The accepted count estimate (7) and L=2m give

    H_M+1 <= M(m+1)/(2m)+L+1
            =M/2+M/(2m)+L+1.                                     (13)

Write `K-1=4m+e`, with integer `0<=e<=3`. Then

    m=(K-1-e)/4 >=(K-4)/4 >=K/8,
    L=2m <=(K-1)/2 <=K/2,                                         (14)

where the first comparison to K/8 requires only K>=8 and hence holds here. In particular m>0. These finite floor bounds apply also at K=13,m=3,L=6.

Let the proof-local number `lambda=-log(delta)>0`. Since delta<1, increasing an exponent decreases its power. By (13),

    delta^(H_M+1)
       >=delta^(M/2) exp[-lambda(M/(2m)+L+1)].                     (15)

Lemma `lem:s016-dominance` gives `lambda<log(K)/M` and `M>=K^3`. All factors in the overhead are nonnegative. Together with (14),

    lambda(M/(2m)+L+1)
       < log(K)/(2m)+(L+1)log(K)/M
       <= 4log(K)/K +(K/2+1)log(K)/K^3.                           (16)

This proves the first inequality of (12); weakening a strict intermediate inequality to a non-strict one is harmless. In particular the entire `M/(2m)+L+1` cost is paid. We have neither replaced H_M by M/2 nor removed the changed-target `+1`.

**Proof: a uniform finite constant.** For every real x>=2, define `f(x)=x/2-log(x)`. Its derivative is `1/2-1/x>=0`. Also

    log(2)=integral_1^2 (1/t) dt <1,

so f(2)>0, proving `log(K)<=K/2` on the present domain. Therefore the final overhead in (16) is at most

    2+1/(4K)+1/(2K^2) <=2+1/8+1/8=9/4<3,                         (17)

using K>=2 in the second inequality. This establishes the second inequality of (12), with an absolute finite constant, not an asymptotic or decimal estimate.

For the last numerical conversion, the elementary exponential series gives

    exp(1)=1+1+sum_(j=2)^infinity 1/j! <2+sum_(j=2)^infinity 2^(-(j-1))=3.

Indeed `j!>=2^(j-1)` for j>=2, with strict inequality for j>=3, so the termwise convergent comparison is strict. Consequently

    exp(3)=exp(1)^3<27<32,       exp(-3)>1/32.                     (18)

Apply the accepted finite amplitude in (7), then (12) and (18), to (6):

    sup_D L_B >=delta^(H_M+1) alpha/8
              >=2^-12 exp(-3) delta^(M/2) hstar
              >2^-17 T.

This is (11). The only source/test content is the actually accepted full-data star theorem; all new exponent absorption is the finite algebra just proved. ∎

### unit_004: Proposition 4 — All-parameter maximum assembly (`prop:s016-envelope`)

**Statement.** Under exactly (1)–(2), for every `K>=2,M>=1,beta in [0,1]` and every fixed common randomized predictor B,

    sup_((theta,mu) in D_K(2,beta)) L_B(theta,mu)
        >=max(F/180, 2^-16 D, 2^-17 T)
        >=2^-17 max(F,D,T).                                      (19)

Taking the infimum over B proves Theorem S016.

**Proof.** The first two entries of the first maximum are (4) everywhere. It remains to prove the third for the same fixed B.

Lemma `lem:s016-small` proves that entry for beta endpoints, M=1 or K<=12: its proofs use per-B bounds (3)–(5), not an algorithm-specific favorable choice. In the remaining domain `K>=13,M>=2,0<beta<1`, there are exactly two cases. If T<=F, then (4) gives

    sup_D L_B>=F/180>=T/180>=2^-17 T,

since `180<2^17`. If T>F, Lemma `lem:s016-absorb` proves the entry. These cases exhaust the domain and prove all three simultaneous scalar lower bounds on the same supremum.

Taking their maximum is legitimate even if the witnessing source families differ. More explicitly, for each B a supremum over the whole class dominates each relevant finite-prior average separately; a different hard source may be selected for different terms or predictors. We do not add their risks, require a single source hard for every B, or reveal which source/family/sign was selected to the predictor. Since `1/180>=2^-17` and `2^-16>=2^-17`, the second inequality in (19) follows. Finally the right side does not depend on B, so taking its infimum preserves it. ∎

## 6. Target-step assembly and limits of the conclusion

The accepted full-domain S012 lower supplies F and D. Lemma `lem:s016-small` handles the exact endpoints, M=1 and every excluded small alphabet. In the remaining domain, the elementary case T<=F needs no star theorem. Lemma `lem:s016-dominance` derives the parameter restrictions forced by the opposite case, and Lemma `lem:s016-absorb` converts the accepted exact-count star lower into its portable T term with the entire finite overhead paid. Proposition `prop:s016-envelope` takes a maximum before the algorithm infimum. This proves exactly the all-parameter contract.

The uniform lower also applies to the worst risk of each fixed common algorithm, including original add-one, because (19) precedes the infimum. This does **not** give that algorithm any new upper. S015's exact family-only upper is not used to control the full class. No full joint minimax matching, new hard family, asymptotic ray classification, or statement about a different loss/query experiment is inferred.

## 7. Retained S011 upper and algorithm assignments

For every integer ell>=1 define

    u_s(ell)=min(1,48sqrt(K^3/(ell+1))),
    u_g(ell)=min(1,48sqrt(K^5/(ell+1))).

For integers b>=0 let `h_b=delta^floor(b/2)` if beta<1. At beta=1 define `h_b=1` for b<2 and `h_b=0` for b>=2, directly. In particular there is no `0^0` at that endpoint. The inherited certificates are

    U_+=min{u_g(M), min_(0<=b<=M-1)
               min{1,48sqrt(K^3/(M-b+1))+13sqrt(K)h_b^(3/4)}},
    U_suf=min_(0<=b<=M-1)
               min{u_g(M-b),u_s(M-b)+h_b u_g(M-b)},
    U_pool=min{1,(1/2)sqrt(K/M)+2delta},
    U=min{U_+,U_suf,U_pool}.                                      (20)

All burn minima are over deterministic integers; their range contains b=0 even at M=1. The exact assignments are:

- **Original add-one:** at the actual endpoint s=Y_M, count every departure j=0,...,M-1 and output `(C_s(c)+1)/(sum_c C_s(c)+K)`. Its worst class risk is bounded by U_+ only. Optimizing the bound over b does not change these original counts.
- **Suffix add-one:** count only departures j=b,...,M-1 and output its separately smoothed row at the same Y_M. Use the smallest public minimizer of the U_suf expression. The retained suffix has M-b>=1 departures and its first pair; its certificate is U_suf, not an upper for the original rule.
- **Pooled empirical:** output `M^-1 sum_(j=0)^(M-1) e_(X_(j+3))`; its certificate is U_pool. It is distinct from either rowwise rule.
- **Public selector:** compare the three explicit certificates using the fixed S011 tie order original, suffix, pooled. The chosen common algorithm has worst risk at most U. It uses no hidden source-specific risk or label.

Thus the retained inequalities are `R_D2<=U` and `R_D2<=R_D2^+<=U_+`. Equation (20) is inherited mathematics, not newly sharpened here. At beta zero the original endpoint equality `U=u_g(M)` and the sharper baseline (5) are preserved; at beta one the original positive IID floor and pooled upper are preserved. The lower in (S016) and U are **not claimed to match globally**.

## 8. Explicit rate, notation and action audit

- **Exposed variables:** every integer K>=2,M>=1 and every public beta in [0,1]; n=M+1 and delta=1-beta are definitions. There are no asymptotic limits, confidence parameters, auxiliary tolerances or unspecified constants in S016.
- **Probability/horizon/norm:** fixed deterministic horizon, unconditional expectation of half-L1 TV at the actual terminal row; complete M+2 observations remain available. No independent-query, random-time, squared-TV, predictive-KL, stopping-time or high-probability replacement occurs.
- **Constants:** 1/180 and 2^-16 are accepted S012 constants; `1/(32sqrt(6))` is the accepted S006 IID constant; 2^-12 and the exact count are accepted S015 constants/interfaces. The new factor `exp(-3)>1/32` is proved in Lemma `lem:s016-absorb`; hence 2^-17 is explicit and independent of K,M,beta,source,mu,pi,signs and predictor. Constants 48 and 13 in U are retained S011 constants.
- **Public-facing notation:** the class/risk and i,a,g,hstar,F,D,T specify the theorem; U and its branches are inherited algorithm-labelled certificates. The scalar hstar is not the burn contraction h_b and not the exact integer H_M. The data history H is distinct from H_M.
- **Proof-local objects:** m,L,q,d,k,V_phase,r_M,H_M,alpha are translated accepted star objects; lambda is the locally defined positive `-log(delta)`. Neither lambda's bound nor the count overhead is assumed. The temporary x in the small-K cap proof and the temporary real-variable function f in the logarithm proof are local algebra only. Source signs, coins and phase machinery stay hidden from all algorithms.
- **Caps and boundaries:** the separate cases in Lemma `lem:s016-small` handle M=1, both beta endpoints and K<=12. Lemma `lem:s016-dominance` explicitly handles both hstar cap branches and proves when the a cap is inactive. The inherited star amplitude retains q=0, both amplitude branches and both z cap branches. No exact exponent is weakened without the displayed dominance condition and finite comparison.
- **Baseline fidelity:** the common 2^-17 packaging is deliberately conservative. The inherited stronger F/180, 2^-16 D, all-beta IID floor, exact beta-zero `2^-16 g` lower/original u_g upper, and beta-one IID sandwich remain true and explicitly retained. No earlier theorem is edited or weakened.


