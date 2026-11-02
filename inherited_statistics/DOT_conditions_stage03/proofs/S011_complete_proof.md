# S011 区分算法的上界证书与匹配区域

编排说明（非原文）：以下逐字保留原已接纳版本的完整数学论证、必要定义、范围与科学解释，仅省略身份、内部控制和来源元数据。原有数学编号及 Euler clock 名称不变。新增标题与本说明不是原证明。依赖闭包与源哈希见 ../SOURCES.md，精确字节映射见 ../COPY_MAP.json。本次编排不是重新证明或对复制件的新数学审查。

编排时序注（非原文）：§5 的 M=K⁴、β=K⁻⁶ 结论仍是 S011 三个数值上界证书等于 1 的正确计算，但 S012 后来给出真风险的匹配一般率；本阶段剩余窗口见 S012 Proposition 9。

## 1. Exact setting, algorithms, and target theorem

Fix integers `K>=2,M>=1`, and a public real `beta in [0,1]`. The alphabet is `A={0,...,K-1}`. A homogeneous second-order table `theta_ab(c)` has nonnegative entries and every row sums to one; zero legal entries are allowed. Its pair kernel is

    P((a,b),(b,c))=theta_ab(c),

with all non-shift transitions zero. Let `D_K(2,beta)` consist of `(theta,mu)` for which some probability law `pi` on `A^2` satisfies

    pi P=pi,            P^2(s,t)>=beta pi(t) for EVERY s,t in A^2.       (D)

The initial pair law `mu` is arbitrary, not necessarily pi or absolutely continuous with respect to it. The witnesses `theta,mu,pi` are hidden. Beta is a public lower bound, not an oracle disclosing a source's maximal coefficient. A source may vary with fixed `K,M,beta` in a supremum but is unchanged within one trajectory.

Observe the full history `H=(X_1,...,X_(M+2))`, with

    Y_j=(X_(j+1),X_(j+2)),                    0<=j<=M.

Exactly M departures are observed. The target is `theta_(Y_M)` for the unobserved `X_(M+3)`. A common algorithm is a probability kernel from the whole H to `Delta_K`, may use public `K,M,beta` and an independent seed, and does not read hidden source parameters or the future. Define

    L_B(theta,mu)=E TV(B(H),theta_(Y_M)),       TV(p,q)=||p-q||_1/2,
    R_D2=inf_B sup_(theta,mu in D_K(2,beta)) L_B(theta,mu),
    R_D2^+=sup_(theta,mu in D_K(2,beta)) L_(p^+)(theta,mu).

All expectations retain the actual endpoint and all its dependence on the same history. No independent query, random-time query, predictive KL, squared-TV risk, or stopping horizon is substituted.

The ORIGINAL full-history rowwise rule is

    C_s(c)=sum_(j=0)^(M-1) 1{Y_j=s,X_(j+3)=c},
    n_s=sum_c C_s(c),             p_s^+(c)=(C_s(c)+1)/(n_s+K).

For a deterministic integer `0<=b<=M-1`, let `L=M-b>=1` and define the distinct SUFFIX rule

    C_s^[b](c)=sum_(j=b)^(M-1) 1{Y_j=s,X_(j+3)=c},
    n_s^[b]=sum_c C_s^[b](c),
    p_s^(+,[b])(c)=(C_s^[b](c)+1)/(n_s^[b]+K).

Both output at `s=Y_M`. The suffix uses the complete length-L suffix, including its first pair, but discards b departures. The POOLED empirical rule is

    E_pool(c)=(1/M)sum_(j=0)^(M-1)1{X_(j+3)=c}.

Its denominator is positive even at M=1. It is neither of the rowwise rules.

Define public scalar quantities

    n=M+1,   delta=1-beta,
    i=min{1,sqrt(K/n)},
    a=min{1,sqrt(K^3/n)},
    g=min{1,sqrt(K^5/n)},
    F=max{i,min{delta,a}},                     0<i<=a<=g<=1,
    u_s(L)=min{1,48sqrt(K^3/(L+1))},
    u_g(L)=min{1,48sqrt(K^5/(L+1))}.

For every integer `b>=0` use the envelope

    h_b=(1-beta)^floor(b/2),                    0<=beta<1;
    h_b=1 if b<2, and h_b=0 if b>=2,            beta=1.                 (1.1)

In particular at beta zero `h_b=1` for every b. No `0^0` is used at beta one.

The three finite certificates are

    U_+=min{u_g(M),
            min_(0<=b<=M-1) min{1,
               48sqrt(K^3/(M-b+1))+13sqrt(K)h_b^(3/4)}},              (1.2)

    U_suf=min_(0<=b<=M-1)
                min{u_g(M-b),u_s(M-b)+h_b u_g(M-b)},                  (1.3)

    U_pool=min{1,(1/2)sqrt(K/M)+2delta},
    U=min{U_+,U_suf,U_pool}.                                         (1.4)

**Theorem S011.** On the entire domain in this section,

    F/180 <= R_D2 <= U,
    R_D2 <= R_D2^+ <= U_+.                                          (1.5)

The upper U is attained as a certificate by a deterministic public selector between the original rule, a public-bound-minimizing suffix rule, and the pooled rule. It is not an oracle selecting the smaller unknown risk. Only U_+ in (1.2) is assigned to the original rule.

If either

    delta<=a,                                                       (N)

or

    h_floor(M/2)<=1/(M+1),                                         (B)

then

    F/180 <= R_D2 <= U <= min{1,81F}.                               (1.6)

Under (N), the sharper `U<=min{1,3F}` holds. The same bound (1.6) holds for **all** `beta>=1/2`, including all small M. At beta zero the full general rate g is inherited; at beta one the arbitrary-start common minimax rate is i. The lawful mixing-envelope counterexample and the exact finite certificate-gap sequence are proved in Propositions 6 and 7 below.

## 2. Allowed assumptions, accepted interfaces, and lemma map

Primitive conditions are exactly the finite experiment, homogeneity/legal shift, the parameter domains, arbitrary initialization, the existential stationary witness and all-state inequality (D), and the common-algorithm information restriction. Conditions (N) and (B) are public deterministic scalar tests for stated corollaries, not assumptions on a generated event. All contraction, row-center, stationarity-of-copy-family and scalar-domination properties used later are derived or imported below.

The following are accepted, exact-target dependencies.

1. **S003, Theorem S003.1 (upper interface).** For any legal source and length `L>=1`, if its initial law is within TV eta of some stationary law, its original length-L add-one risk is at most `min{u_g(L),u_s(L)+eta u_g(L)}`. We instantiate this only on the genuine length-L suffix, whose initial law is `mu P^b`. Its lower theorem is not transferred to the smaller mixing class by substituting a mixing envelope for eta.
2. **S004, S004.2 and Lemma 5/Corollary 6.** For every deterministic burn `0<=b<=M-1`, the unchanged original rule obeys

       L_(p^+)(theta,mu)
          <=min{1,48sqrt(K^3/(M-b+1))
                       +13sqrt(K) TV(mu P^b,pi)^(3/4)}.             (2.1)

   This is a separate original-count/original-stack result, not the suffix risk bound. Its contraction interface applies under all-state minorization; the q=2 bridge is also proved below, including beta zero. Its copy-last-symbol example supplies the previously accepted family; the exact coefficient and faster-envelope obstruction are derived afresh here.
3. **S006, Lemmas 1 and 5.** The pooled bound `min{1,(1/2)sqrt(K/M)+2z}` holds for arbitrary initial law if all rows are within TV z of one hidden probability center. The q=2 product/summation calculation gives such a center with `z=1-beta`. This algebra does not use the initial law; it is repeated below. We do not import S006's stationary upper as an arbitrary-start theorem.
4. **S006, Theorem S006-B (lower interface).** For every common full-history possibly randomized algorithm, its worst risk on the stationary-initialized subclass satisfying (D) is at least `F/180`. This is the accepted combination of the stationary IID floor and the scaled legal stationary checkerboard family, not an arbitrary-state-space lower or a single-source add-one counterexample. Its stronger IID component is `i/(32sqrt(6))` and its structural component for beta<1 is `min{a/10,1-sqrt(beta)}/18`.
5. **L1MAX, L1+ (statistical interface only).** For every legal theta and arbitrary mu, the original rule's risk is at most `u_g(M)`. No implementation, resource or fault statement is consumed. **MM5**, only at beta zero, gives the all-common-full-history-randomized-algorithm lower `2^-16 g`. Their exact statements, readable statistical interfaces, independent reports and frozen acceptance index were checked; their predecessor proofs are inherited, not newly certified.

For lower bounds, fix public `K,M,beta` first. An algorithm using those public values is still one fixed history kernel within the dependencies' universal algorithm quantifier. Every hard subclass shares the public beta bound. Suprema are taken before the algorithm infimum; no common source is asserted to be hard for all algorithms and horizons simultaneously.

| Local unit | Named result / label | Role |
|---|---|---|
| unit_001 | Lemma 1, All-state contraction (`lem:s011-contract`) | Derive the correct h_b for arbitrary initialization |
| unit_002 | Proposition 2, Algorithm-separated envelope (`prop:s011-envelope`) | Original, suffix, pooled, public selection and stationary lower |
| unit_003 | Proposition 3, Matched public regimes (`prop:s011-regimes`) | Complete finite proof of (N), (B) and constants |
| unit_004 | Corollary 4, Strong-beta finite specialization (`cor:s011-strong`) | All beta>=1/2, integer exponent and small M |
| unit_005 | Proposition 5, Exact parameter endpoints (`prop:s011-endpoints`) | General beta-zero and arbitrary-start IID beta-one boundaries |
| unit_006 | Proposition 6, Legal slow copy family (`prop:s011-copy`) | Stationarity, exact coefficient, marginal and negative envelope |
| unit_007 | Proposition 7, Exact certificate gap (`prop:s011-gap`) | Every K>=12 at M=K^4,beta=K^-6; not a risk identification |

## 3. Local derivation of the envelope and matched regimes

### unit_001: Lemma 1 — All-state contraction (`lem:s011-contract`)

**Statement.** Under the setting and (D), for every deterministic integer `b>=0`, `TV(mu P^b,pi)<=h_b`, with h_b in (1.1), including both beta endpoints.

**Proof.** Every finite stochastic kernel Q contracts TV: the triangle inequality gives

    sum_t |sum_s (nu(s)-rho(s))Q(s,t)|
       <=sum_s |nu(s)-rho(s)|sum_t Q(s,t)=||nu-rho||_1.

Let Pi have every row pi. If `0<=beta<1`, the residual matrix

    Q=(P^2-beta Pi)/(1-beta)

is stochastic by (D) and the row sums. Stationarity gives `pi Q=pi`. For any probability nu,

    nu P^2-pi=(1-beta)(nu Q-pi Q).

Thus each two-step block contracts distance to pi by `(1-beta)`. For `b=2r+j`, `j in {0,1}`, iterate r blocks and apply contraction to the final j steps; the bound is `(1-beta)^r TV(mu,pi)<=h_b`. This also covers beta zero with no spurious contraction claim. If beta=1, row sums force `P^2=Pi`. Consequently `mu P^b=pi` for b>=2; before two steps contraction alone gives distance at most one. This is exactly the separate beta-one definition. No reversibility or stationary support condition is used. ∎

### unit_002: Proposition 2 — Algorithm-separated envelope (`prop:s011-envelope`)

**Statement.** Under the full setting, the three rules defined in Section 1 have their respective uniform certificates (1.2)–(1.4), their public selector has risk at most U, and the stationary subclass gives `R_D2>=F/180`.

**Proof: original.** For every allowed b, substitute Lemma 1 into the accepted original-rule inequality (2.1). Independently, L1MAX gives `u_g(M)`. Since the algorithm is the SAME unchanged p^+ in every such inequality, its worst risk is at most their finite minimum U_+. This is an analytical optimization; the original algorithm does not read b or h_b.

**Proof: suffix.** Fix an allowed deterministic b. Under the same fixed theta, `(X_(b+1),...,X_(M+2))` is exactly a full `L+2`-symbol experiment with initial pair law `mu P^b` and `L=M-b` departures. Its endpoint is the original Y_M. Lemma 1 gives distance at most h_b from the same stationary pi. S003's length-L upper therefore gives

    L_(p^(+,[b]))(theta,mu)
       <=min{u_g(L),u_s(L)+h_b u_g(L)}.                            (3.1)

The set of allowed b has exactly M elements and is nonempty. Let b_* be the smallest minimizer of the explicit right side of (3.1). This is a deterministic function of public `K,M,beta`, not of observations or hidden risks. The fixed algorithm `p^(+,[b_*])` has uniform certificate U_suf. For M=1 the only choice is b_*=0; no empty optimization or zero-length suffix occurs. It is this suffix algorithm, not the original full-history rule, that receives the S003 transfer.

**Proof: pooling, with its necessary arbitrary-start bridge.** The unique legal two-step path gives

    P^2((a,b),(c,d))=theta_ab(c)theta_bc(d)>=beta pi(c,d).

Sum over d and set `p(c)=sum_d pi(c,d)`. Then p is a probability vector and `theta_ab(c)>=beta p(c)` for every row, even off stationary support. If beta<1, the row `(theta_ab-beta p)/(1-beta)` is a probability vector, so `TV(theta_ab,p)<=1-beta=delta`. If beta=1, equal row sums force every row exactly p. This proves the all-row center property without any assumption on mu or division by p(c).

Here is the S006 martingale bridge in the present indexing. With `F_j=sigma(X_1,...,X_(j+2))`, put `D_j=e_(X_(j+3))-theta_(Y_j)`, `0<=j<M`. Its conditional mean given F_j is zero and its conditional squared Euclidean norm has expectation `1-||theta_(Y_j)||_2^2<=1`. For j<k, D_j is F_k-measurable, hence `E<D_j,D_k>=0`. Therefore

    E||sum_j D_j||_2^2<=M,
    E TV(E_pool,(1/M)sum_j theta_(Y_j))<=(1/2)sqrt(K/M).

The second inequality is L1/L2 comparison followed by expectation Cauchy–Schwarz. The average row and the actual terminal row are each within delta of p pathwise. Their triangle contributions total at most `2delta`, proving U_pool after the probability-vector cap one. There is no claim that the observed symbols are IID when beta<1, and no hidden center is given to E_pool.

**Proof: selector.** Compare the three public numbers `U_+,U_suf,U_pool`. Choose the first smallest one in the fixed order original, suffix, pooled, and run its associated rule; the suffix branch uses b_* just defined. The entire branch choice is deterministic from public parameters. Each branch has its uniform certificate, so this single common selector has worst risk at most their minimum U. This argument would not justify selecting by source-specific true risks; none are used. Admissibility also gives `R_D2<=R_D2^+`.

**Proof: lower.** Each `(theta,pi)` in the accepted stationary class `D_K^stat(2,beta)` defines an allowed arbitrary-start member by taking mu=pi. For every fixed common B,

    sup_(D_K(2,beta)) L_B
        >=sup_(D_K^stat(2,beta)) L_B >=F/180.

Taking infimum over B proves the lower. Fixed public beta changes only the common kernel being tested, not its information restriction or the lower's full-history quantifier. This completes (1.5). ∎

### unit_003: Proposition 3 — Matched public regimes (`prop:s011-regimes`)

**Statement.** Under the setting, condition (N) gives `U<=min{1,3F}`. Condition (B) gives `U_+<=min{1,81a}` and `U<=min{1,81F}`. With Proposition 2's lower these are matching common-minimax rates on their displayed domains.

**Proof.** First the capped scalar bound

    U_pool<=i+2delta                                                 (3.2)

holds for every parameter. If i=1 the cap suffices. If i<1 then

    [(1/2)sqrt(K/M)]/i=(1/2)sqrt((M+1)/M)<=sqrt(2)/2<=1,

using M>=1. If delta<=a, `F=max{i,delta}`, so `U<=U_pool<=i+2delta<=3F`. This proves (N), including equality and zero delta.

For (B), take the public burn `b=floor(M/2)`, which always satisfies `0<=b<=M-1`, and `L=ceil(M/2)`. Put `T=sqrt(K^3/n)` only within this proof. Since `L+1>=n/2`,

    48sqrt(K^3/(L+1))<=48sqrt(2)T.

Condition (B) gives

    sqrt(K)h_b^(3/4)<=sqrt(K)n^(-3/4)<=T,

where the last ratio is `1/[K n^(1/4)]<=1`. Thus the original candidate in U_+ at this burn is at most

    min{1,(48sqrt(2)+13)T}<=min{1,81T}<=min{1,81a}.               (3.3)

For the strict numerical comparison, `sqrt(2)<17/12` because `2<289/144`, and `48(17/12)+13=81`. The last capped equality/inequality in (3.3) follows separately from T<=1 (a=T) and T>=1 (both caps one).

If delta>=a then F=a and (3.3) gives `U<=81F`. If delta<a, (3.2) instead gives `U<=3F<=81F`. All these certificates are at most one. This proves (1.6) under (B) and preserves the separate original-rule claim in (3.3). The sufficient condition is not asserted to be necessary. ∎

### unit_004: Corollary 4 — Strong-beta finite specialization (`cor:s011-strong`)

**Statement.** For every `K>=2,M>=1,beta>=1/2`, (1.6) holds, with the same absolute constants. The half-window condition (B) holds for every such beta when M>=32.

**Proof.** First suppose M>=32. Write `M=4r+j`, `0<=j<=3`, so `r=floor(M/4)>=8`. The elementary bound `2^r>=4r+4` holds at r=8 since `256>=36`. If it holds for r, then

    2^(r+1)>=8r+8>=4(r+1)+4,

so induction proves it for every r>=8. Hence `M+1<=4r+4<=2^r`. Integer division gives `floor(floor(M/2)/2)=floor(M/4)=r`. For `1/2<=beta<1`,

    h_floor(M/2)<=(1/2)^r<=1/(M+1).

For beta=1, `floor(M/2)>=16>=2` and the separately defined h is zero. Proposition 3 now applies.

If `M<32`, the integer n=M+1 satisfies n<=32. Since K>=2,

    a=min{1,sqrt(K^3/n)}>=sqrt(8/32)=1/2.

The original risk certificate U_+ is at most one and therefore at most `2a`. If delta>=a use F=a and `U<=U_+<=2F`; if delta<a use (3.2) and `U<=3F`. (In this strong-beta small-M domain delta<=1/2<=a, so the latter pooling regime already suffices except for the harmless equality.) In all cases `U<=min{1,81F}`, and Proposition 2 supplies `F/180`. No asymptotic bound fills a missing small-M case. ∎

### unit_005: Proposition 5 — Exact parameter endpoints (`prop:s011-endpoints`)

**Statement.** At beta zero, `D_K(2,0)` is the full arbitrary-initialization class and

    2^-16 g<=R_D2(K,M,0)<=R_D2^+(K,M,0)<=u_g(M)<=48g.             (3.4)

The envelope U itself equals u_g(M) there. At beta one the table is precisely all-row IID, with arbitrary initial pair still allowed, and

    i/(32sqrt(6))<=R_D2(K,M,1)
        <=U_pool=min{1,(1/2)sqrt(K/M)}<=i.                       (3.5)

**Proof.** Every finite stochastic P has a stationary probability law: the Cesaro averages `T^-1 sum_(j=0)^(T-1)nu P^j` lie in a compact finite simplex, and their P-invariance defect is `(nu P^T-nu)/T`, of L1 norm at most `2/T`. A convergent subsequence gives a stationary law. At beta zero the minorization says only nonnegativity, so no source is excluded. MM5 and L1MAX give (3.4), with the same unrestricted initialization, observation, target and universal algorithm quantifiers. Fixing beta=0 does not weaken that quantifier. In the envelope, h_b=1 makes every S004 original candidate cap at one because `13sqrt(K)>1`; hence U_+=u_g(M). For suffixes, `min{u_g(L),u_s(L)+u_g(L)}=u_g(L)`, whose minimum over L=1,...,M is u_g(M). Finally U_pool=1. Therefore U=u_g(M) exactly.

At beta one the product/summation argument in Proposition 2 forces every theta row to be the same p, and stationarity yields `pi=pi P^2=p tensor p`. Conversely such an all-row table has `P^2(s,(c,d))=p(c)p(d)`, so qualifies for any arbitrary mu. The initial two symbols need not be IID. Given either initial pair, however, the M transition outputs have product law `p^(tensor M)`, and the pooled martingale bound already gives the asserted upper without needing this independence observation. The accepted S006 stationary IID witnesses take `mu=p tensor p`, retain all M+2 informative IID observations, and give the lower `i/(32sqrt(6))`; this valid subclass lower applies to the arbitrary-mu class. Thus (3.5) is not obtained by discarding initial information from a lower experiment.

The original rowwise rule does not inherit (3.5). S006's accepted algorithm-separation conclusion, based on S005's stationary IID sequence, already rules out its uniform multiplicative optimality there. In particular the even-K sequence `M=floor(K^2/100)`, half the p-coordinates `3/(2K)` and half `1/(2K)`, with initial `p tensor p`, has original risk at least `391/1600` while pooled risk tends to zero. This is a same-source algorithm comparison, not a minimax lower. ∎

## 4. A lawful obstruction to uniformly faster mixing

### unit_006: Proposition 6 — Legal slow copy family (`prop:s011-copy`)

**Statement.** Fix K>=2 and `epsilon in [0,1]`. Define

    T(b,c)=(1-epsilon)1{c=b}+epsilon/K,
    theta_ab(c)=T(b,c),
    pi(a,b)=K^-1 T(a,b).                                           (4.1)

This is a legal homogeneous pair-shift table with stationary law pi. Its maximal all-state two-step minorization coefficient relative to pi is exactly epsilon; it is also the largest possible coefficient over stationary witnesses. From `mu=delta_(0,0)`, for `0<=epsilon<1` and every integer t>=0, the second-coordinate law of Y_t is

    (1-epsilon)^t delta_0+[1-(1-epsilon)^t]u,
    u(c)=1/K,                                                      (4.2)

and therefore

    TV(mu P^t,pi)>=(1-1/K)(1-epsilon)^t.                            (4.3)

At epsilon=1, the second marginal equals delta_0 at t=0 and u for t>=1. Consequently, for any fixed K>=2, any positive fixed c and any finite nonnegative C, there is no bound

    TV(mu P^t,pi)<=C exp(-c sqrt(beta)t)                             (4.4)

valid for every beta>0, every member of `D_K(2,beta)`, every initial law and every integer t>=0. This remains false if c,C are allowed to depend on the fixed K but not on beta or the source.

**Proof: legality and stationarity.** Every row in (4.1) is a probability vector; the induced transition remains exactly `(a,b)->(b,c)`, not an arbitrary K^2-state matrix. T is doubly stochastic: its row and column sums are `(1-epsilon)+epsilon=1`. Therefore pi has total mass one and

    sum_a pi(a,b)theta_ab(c)
       =K^-1 [sum_a T(a,b)]T(b,c)=K^-1 T(b,c)=pi(b,c).

This is stationarity at every destination pair, including epsilon zero and one. Its second-coordinate marginal is u.

**Proof: exact coefficient.** The unique two-step product gives

    P^2((a,b),(c,d))=T(b,c)T(c,d)
       >=(epsilon/K)T(c,d)=epsilon pi(c,d).                      (4.5)

For epsilon>0 all T(c,d) are positive, and hence at every target pair

    P^2((a,b),(c,d))/pi(c,d)=K T(b,c)
             =epsilon+K(1-epsilon)1{b=c}.

Choose b different from c, possible because K>=2. The ratio is exactly epsilon, so no coefficient larger than epsilon works relative to pi. This includes epsilon one. For epsilon zero, choose target `(c,c)` with pi mass 1/K and a starting second coordinate b different from c; then the numerator is zero. Thus its exact coefficient is zero too.

For epsilon>0 the stationary witness is unique: any stationary nu satisfies, using the two-step contraction derived from (4.5),

    TV(nu,pi)=TV(nu P^2,pi P^2)<=(1-epsilon)TV(nu,pi),

forcing equality to zero, with epsilon one covered by exact reset. At epsilon zero, the chain enters the diagonal after one step and remains at its diagonal symbol. Every stationary law is therefore supported on diagonal pairs. Any such law gives positive mass to some `(c,c)`, and a start with b different from c again has two-step mass zero there. Hence no other stationary witness permits a positive coefficient. This proves the maximal-witness statement without assuming uniqueness at epsilon zero.

**Proof: marginal and TV.** If nu_t is the second marginal from `(0,0)`, then `nu_0=delta_0` and `nu_(t+1)=nu_t T=(1-epsilon)nu_t+epsilon u`. Induction gives (4.2). At epsilon one apply the recurrence directly at t=0 and thereafter, rather than using `0^0`. Projection to the second coordinate contracts TV, and

    TV((1-epsilon)^t delta_0+[1-(1-epsilon)^t]u,u)
        =(1-epsilon)^t TV(delta_0,u)
        =(1-1/K)(1-epsilon)^t,

which proves (4.3). At epsilon zero it remains constant, as expected.

**Proof: impossibility of (4.4).** Choose epsilon=beta in `(0,1/2]`, so the family belongs to the exact public-beta class and even has maximal coefficient beta. Put `t=floor(1/beta)`. Since

    -log(1-beta)=integral_0^beta (1-x)^(-1) dx<=2beta,

and `beta t<=1`, (4.3) gives the uniform positive lower

    TV(mu P^t,pi)>=(1-1/K)exp(-2beta t)>=(1-1/K)e^-2.             (4.6)

On the other hand,

    sqrt(beta)t>=beta^(-1/2)-sqrt(beta) -> infinity

as beta decreases to zero, so the right side of (4.4) tends to zero for every fixed c>0 and finite C. If C=0 the contradiction is immediate. Thus (4.4) is false. K is fixed throughout this limit; no growth of the state space hides the contradiction. The obstruction concerns uniform TV convergence to stationarity only. It does not lower-bound estimation risk, rule out a structure-sensitive prediction algorithm, or show that any certificate floor is statistically necessary. ∎

## 5. Exact finite certificate gap

### unit_007: Proposition 7 — Exact certificate gap (`prop:s011-gap`)

**Statement.** For every integer `K>=12`, set `M=K^4,beta=K^-6`. Then

    U_+=U_suf=U_pool=U=1,                                      (5.1)
    F=a=sqrt(K^3/(K^4+1)),
    1/sqrt(2K)<=a<=1/sqrt(K).                                 (5.2)

Consequently the inherited lower `F/180` is of order K^-1/2 along this sequence while all three displayed upper certificates remain capped at one. These are numerical values of available certificates, not equalities for R_D2 or for any estimator's true worst risk.

**Proof.** Let b be any admitted burn and L=M-b. Since `L+1<=K^4+1<K^5` for K>=2, `u_g(L)=1`, including b=0. Write `r=floor(b/2)`. Bernoulli's inequality `(1-x)^r>=1-rx` for `0<=x<=1` and integer r>=0 follows by induction (multiply the previous bound by 1-x and retain the nonnegative `r x^2` term). It yields

    h_b=(1-K^-6)^r>=1-rK^-6>=1-1/(2K^2),                      (5.3)

because `r<=b/2<M/2=K^4/2`. The displayed weak inequality is convenient and uniform over every burn.

In particular `h_b>=1/2`. Since `h_b in [0,1]`, `h_b^(3/4)>=h_b`, so

    13sqrt(K)h_b^(3/4)>=(13/2)sqrt(K)>1.

Every capped original S004 term in (1.2) is therefore one, as is u_g(M). Hence U_+=1; this establishes the statement uniformly over the finite analytical optimization, not only at a selected burn.

For the suffix certificate, monotonicity in L and `48>=1` give

    u_s(L)>=u_s(M)>=a>=1/sqrt(2K)>1/(2K^2).                    (5.4)

The penultimate inequality uses `K^4+1<=2K^4`. For the last inequality, both sides are positive and `4K^4>2K` for K>=1. Equations (5.3)–(5.4), together with u_g(L)=1, imply

    u_s(L)+h_b u_g(L)>1

for **every** admitted b. Thus the inner minimum in (1.3) is one for every b, so U_suf=1. Finally `2delta=2(1-K^-6)>1`, giving U_pool=1. This proves (5.1) for every K>=12, stronger than an unspecified eventual threshold.

The rate a is uncapped because `K^3<K^4+1`, and its two displayed comparisons in (5.2) follow from `K^4<=K^4+1<=2K^4`. Likewise `i=a/K`. For K>=12, `a<=1/sqrt(K)<1/2`, whereas `delta=1-K^-6>1/2`, so `min{delta,a}=a>=i` and F=a. Therefore Proposition 2's stationary lower is between `1/(180sqrt(2K))` and `1/(180sqrt(K))` as a certificate. If retaining S006's sharper two-component stationary certificate, it equals a/180 here: `min{a/10,1-sqrt(beta)}=a/10`, and `i/(32sqrt(6))<=a/180` since `32sqrt(6)K>=180` for K>=12. None of these comparisons says the actual minimax risk is that small or that the true upper risk is one. ∎

## 6. Target-step assembly, explicit rates and non-overclaims

The contraction lemma and the accepted original-rule bound give U_+ without changing the estimator. S003 on the actual suffix yields the stronger U_suf, while the all-row product/summation and S006 martingale bridge yield U_pool for arbitrary mu. The public selector and stationary subclass inclusion prove Proposition 2 and (1.5). Proposition 3 supplies the complete finite absorption bridge for (N)/(B); Corollary 4 checks its integer and small-M strong-beta specialization. Proposition 5 preserves the exact beta-zero general-rate and beta-one IID-rate baselines. Proposition 6 proves the lawful route obstruction, and Proposition 7 establishes the exact finite certificate gap. These named results cover every bounded S011 obligation; none uses S010 as a premise.

- **Exposed parameters:** every integer K>=2,M>=1 and public beta in [0,1]; deterministic burns 0,...,M-1. For the copy family epsilon is in [0,1] and t is a deterministic nonnegative integer. Its obstruction holds at fixed K as beta decreases to zero. For the gap sequence K varies over integers >=12 with the displayed exact M,beta choices.
- **Constants:** 48 and 13 are inherited from the accepted upper interfaces; 1/180 and 1/(32sqrt(6)) from the accepted stationary lower. Constants 3 and 81 and all finite threshold comparisons are proved here. There are no hidden constants depending on K,M,beta, theta, mu, pi or the algorithm. The obstruction quantifies over arbitrary fixed c>0 and finite C, rather than choosing beta-dependent constants.
- **Probability/horizon/norm:** all prediction statements are finite-horizon expected actual-endpoint TV. The copy obstruction is deterministic TV between marginal probability laws at fixed t. There are no confidence parameters, almost-sure upgrades, stopping times or uniform-over-horizon statistical assertions. No rate is squared or converted to predictive KL.
- **Algorithm distinction:** b in U_+ is analysis only; b_* in U_suf is part of a genuinely different algorithm. Both optimizations are over finite public numbers, never source-dependent quantities. The pooled branch is essential to the asserted common near-IID guarantee. The statement does not prohibit other optimal algorithms, but it cannot assign pooling's improvement to the unchanged rowwise rule.
- **Boundaries:** K=2, M=1, beta zero/one, zero rows or stationary masses, inaccessible stationary pairs and arbitrary initial pairs are covered by the stated interfaces and explicit separate cases. At M=1 only b=0 is allowed. Beta-one contraction is handled without 0^0. Positive-amplitude stationary testing is inherited only where beta<1; beta one uses the separate IID floor.
- **Sufficiency versus necessity:** (B) is a sufficient public burn test, not a necessary threshold for prediction. The copy family invalidates a proposed faster-TV shortcut, not a faster statistical rate. The gap sequence measures failure of these certificates to meet, not impossibility of better upper analysis or stronger lower constructions.
- **Wider unresolved question:** the full arbitrary-start joint `(K,M,beta)` minimax rate in the remaining weak-beta domain is not established. No guessed interpolation, arbitrary K^2-state hard family, general-q extension, unknown-beta adaptation, or neural/resource/fault result is offered. The separate S010 route is outside this proof's mathematical dependency graph.
- **Notation/provenance:** `D_K,R_D2,R_D2^+`, the three estimators, `i,a,g,F,h_b`, and `U_+,U_suf,U_pool,U` are public-facing expressions explicitly defined from the setting. `L,b_*,T` in the absorption proof, residual kernels, p, filtration increments, copy marginals and scalar induction indices are proof-local objects whose properties are proved at use. The stationary law in (D) is a primitive existential witness; no generated invariant is silently assumed.

