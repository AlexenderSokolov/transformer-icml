# S014 首次符号刷新不足以恢复平稳统计率

编排说明（非原文）：以下逐字保留原已接纳版本的完整数学论证、必要定义、范围与科学解释，仅省略身份、内部控制、来源元数据、重复提交摘要及运行记录。原有数学编号及 Euler clock 名称不变。新增标题与本说明不是原证明。依赖闭包与源哈希见 ../SOURCES.md，精确字节映射见 ../COPY_MAP.json。本次编排不是重新证明或对复制件的新数学审查。

编排时序与范围说明（非原文）：本原版本已获独立审查及接纳。其“aggregate 尚未决定”仅指 S014 自身发射族及当时依赖集；后出的 S015 用不同星形族否定了两个明确提议，不撤销 S014。B₀ 的 weighted-family 上界覆盖该族全域，而 total-scale 比较只在 (1.10) 且 g_M=1 时证明。下文 N 是 departure 数。原作者有限检查保留；本次编排未重跑。

## 1. Exact setting and exported statements

For any integer departure horizon `h>=1`, observe the entire history `H_h=(X_1,...,X_(h+2))`, with actual pairs

    Y_t=(X_(t+1),X_(t+2)), 0<=t<=h.

The target is `theta_(Y_h)`, the law of the unobserved next symbol. Here `theta` is one fixed normalized nonnegative second-order table on `A={0,...,K-1}`, and its legal pair kernel is

    P((a,b),(b,c))=theta_ab(c),

with zero probability on non-shift transitions. A source `(theta,mu)` belongs to `D_K(2,beta)` if there exists a hidden probability law pi on `A^2` such that

    pi P=pi,                  P^2(s,t)>=beta pi(t) for EVERY s,t.       (1.1)

Initialization mu is otherwise arbitrary. Zero entries, reducibility, and zero stationary masses remain permitted. A common randomized predictor B is a probability kernel from the whole `H_h` to the K-simplex, may depend on public `K,h,beta`, and has no access to hidden parameters, stationary law, auxiliary refresh coins, or future symbols. Its seed is independent of source/path/auxiliary sampling. Loss is

    L_h(B;theta,mu)=E TV(B(H_h),theta_(Y_h)),  TV(v,w)=||v-w||_1/2.       (1.2)

No endpoint, visit count, or zero-count correlation is discarded. The original rowwise rule uses exactly the h observed departures:

    C_s(c)=sum_(t=0)^(h-1)1{Y_t=s,X_(t+3)=c},
    n_s=sum_c C_s(c),         p_s^+(c)=(C_s(c)+1)/(n_s+K).               (1.3)

Define `delta=1-beta`, and for a departure horizon h define

    a_h=min{1,sqrt(K^3/(h+1))},  g_h=min{1,sqrt(K^5/(h+1))},
    u_g(h)=min{1,48sqrt(K^5/(h+1))}.                                   (1.4)

The universal upper-certificate claim is Lemma 1: `K>=2,h=M>=1,0<beta<1`. The counterexample uses the explicitly contracted narrower domain

    K>=14, m=floor((K-2)/4)>=3, L=m^2, integer q>=1,
    N=2+qL, M=N+1, r=floor(m/2),
    alpha=min{1/2,(1/8)sqrt(m^3/(q+1))}.                               (1.5)

**Horizon convention:** N in this unit is a number of departures, not the generic package's shorthand for the number of observed symbols. The product experiment has `N+2` symbols and target `theta_(Y_N)`; the prefixed experiment has `M+2=N+3` symbols and target `theta_(Y_M)`. This explicit relettering changes no experiment.

For the finite family constructed below, the same initial law and finite uniform sign prior work for every common B at fixed public parameters:

    Av_sigma L_N(B;theta^sigma,delta_ell tensor p)
        >=delta^(N+1) alpha/8,                                            (1.6)
    L_N(delta_0;theta^sigma,delta_ell tensor p)=delta^(N+1) for every sigma. (1.7)

Here `ell=K-1` and `p=delta_0` is genuinely the stationary symbol marginal. In the prefixed experiment starting at `(0,ell)`, let `tau` be the first auxiliary refresh coin equal to one. Then

    P_sigma(tau=0)=beta,
    Av_sigma E_sigma[TV(B(H_M),theta^sigma_(Y_M)) | tau=0]
        >=delta^M alpha/8,                                                (1.8)
    E_sigma[TV(delta_0,theta^sigma_(Y_M)) | tau=0]=delta^M.                 (1.9)

Thus the contribution on this event is at least `beta delta^M alpha/8` after the finite-prior average, not the larger unweighted expression.

On the exact aligned sequence

    q=floor(K^4/L), N=2+qL, beta=(log K)/(4N), M=N+1,                    (1.10)

equations (1.6) and (1.8) refute a universal finite-C upper `C(a_h+sqrt(beta))`, respectively on the product-initialized class at h=N and on the conditional immediate-refresh experiment at h=M. This is a statement against **every** possible common algorithm, not merely against add-one. Family-only upper (1.7)/(1.9) is never promoted to a full-class upper.

## 2. Allowed assumptions, dependencies, and local map

The primitive conditions are exactly the finite legal-shift setting, fixed source during a trajectory, full-history observation, actual endpoint expected half-L1 loss, common-predictor information restriction, arbitrary initialization and (1.1). The counterexample parameters (1.5), and later sequence (1.10), are public deterministic restrictions, not generated-event assumptions. No new positivity, stationarity-of-initialization, mixing, independent query, or conditional-IID premise is imposed.

**Checked inherited interfaces.**

1. **L1MAX, L1+** bounds (1.3)'s full-history actual risk by `u_g(h)` for every legal homogeneous table and every initial law. Lemma 1 applies this to the legal residual table Q and the original mu at horizon M. Q need not satisfy (1.1). The predictor is the same deterministic map on the same entire history, with all its original counts; it is not a suffix rule. The statistical interface is inherited, not a re-audit of Euler implementation/fault results or its GU predecessor.
2. Accepted **S011, Proposition 2**, has the exact all-pair product identity and summation `theta_ab(c)>=beta sum_d pi(c,d)`. This identity is re-derived in Lemma 1, so the new proof does not rely on an unexamined reset interpretation. Its exact class/algorithm definitions are the ones used here.
3. Accepted **S012, Lemmas 1, 3, 4 and Proposition 5**, and the fully read underlying **MM5**, supply the attributed Euler-clock/sign-testing mechanism. The active clock is relabeled to reserve 0 as in S012. The two launch categories, ending-ell case, new initialization, new complete-history bijection, prefix experiment and new-target contrast are all proved below; neither an old black-box risk lower nor a diagnostic substitutes for them. The fixed return is `(w,1)`, with `c_5=1`.

MM5 and L1MAX are frozen externally accepted **LLM-checked proofs**, not formal kernel certification. No literature-priority claim is made for finite Euler tours or elementary testing.

| Local unit | Named result / stable label | Role |
|---|---|---|
| unit_001 | Lemma 1, Symbol decomposition and original no-refresh bridge (`lem:s014-no-refresh`) | General exact realization and limited weighted event upper |
| unit_002 | Lemma 2, Launch clock and phase invariant (`lem:s014-launch`) | Full residual table, disjointness, normalization and recurring phase |
| unit_003 | Lemma 3, Every-pair minorization (`lem:s014-member`) | Sparse stationary witness and exceptional ending-ell category |
| unit_004 | Lemma 4, Complete aligned history (`lem:s014-history`) | Two entry steps, survival, q labels and actual endpoint bijection |
| unit_005 | Proposition 5, Full-history finite-prior testing (`prop:s014-product-lower`) | Conditional neighboring laws and changed-target actual risk |
| unit_006 | Proposition 6, Exact family-only upper (`prop:s014-family-upper`) | Absorption on every nonsurviving path |
| unit_007 | Proposition 7, Immediate-refresh prefix experiment (`prop:s014-prefix`) | Full prefix retained, conditional risk and exact beta weight |
| unit_008 | Corollary 8, Aligned logarithmic negation (`cor:s014-log`) | Admissibility, exact horizon shifts and divergent rate ratio |
| unit_009 | Proposition 9, Weighted scope boundary (`prop:s014-weighted`) | Exact disintegration; no aggregate refutation from this family |

## 3. Local derivation

### unit_001: Lemma 1 — Symbol decomposition and original no-refresh bridge (`lem:s014-no-refresh`)

**Statement.** Under Section 1 with `K>=2,M>=1,0<beta<1`, select any witnessing pi in (1.1), and let `p(c)=sum_d pi(c,d)`. Then p is also the second-coordinate stationary marginal, every row satisfies `theta_s>=beta p`, and

    Q_s=(theta_s-beta p)/delta                                             (3.1)

is a legal normalized residual symbol table. Independent Bernoulli(beta) refresh coins with independent p-draws give exactly the original source law. If `E0` is no refresh among its M departures, then

    E[1_E0 TV(p^+_(Y_M),theta_(Y_M))]
        <=delta^M min{1,u_g(M)+beta}.                                     (3.2)

**Proof.** The unique two-step legal path gives, for every a,b,c,d,

    P^2((a,b),(c,d))=theta_ab(c)theta_bc(d)>=beta pi(c,d).

Summing over d gives `theta_ab(c)>=beta p(c)`. Row normalization gives the nonnegative row (3.1) total mass `(1-beta)/delta=1`. Thus Q itself is a legal homogeneous second-order symbol table. The first marginal of pi is a probability. Under one pair shift the next first coordinate is the current second coordinate; `pi P=pi` therefore implies `sum_d pi(c,d)=sum_a pi(a,c)`, establishing the marginal terminology without any support assumption.

On a finite product probability space take the initial pair with law mu, M independent Bernoulli(beta) coins `J_t`, independent p-draws, and sufficient independent row samples from each Q_s. All are independent of the algorithm seed. At departure t, append its p-draw if `J_t=1`, otherwise the next unused Q sample for the current row. Conditional on any positive-probability prefix its next-symbol law is `beta p+delta Q_s=theta_s`. Multiplying these conditional laws gives exactly the original full-history law; null prefixes have zero mass in both constructions. No labels or p are revealed to the algorithm.

The event `E0={J_0=...=J_(M-1)=0}` has probability `delta^M`, independent of mu and residual sampling. Conditional on E0 the entire history is exactly the homogeneous Q experiment with original mu, including the actual endpoint and all M departures. The map (1.3) therefore remains the ORIGINAL estimator. Pointwise on a residual history,

    TV(theta_(Y_M),Q_(Y_M))=beta TV(p,Q_(Y_M))<=beta,
    TV(p^+_(Y_M),theta_(Y_M))<=TV(p^+_(Y_M),Q_(Y_M))+beta.

L1+ applies because Q has legal normalized rows and arbitrary initial mu; it retains every random-endpoint/count dependence and the case `n_(Y_M)=0`. The conditional expectation is at most `u_g(M)+beta` and also at most one. Multiplication by `delta^M` proves (3.2). This is only an event contribution; the entire complementary risk is not controlled by this proof. ∎

### unit_002: Lemma 2 — Launch clock and phase invariant (`lem:s014-launch`)

**Statement.** Under (1.5), one can construct a full residual table `Q^sigma` on every K-squared row, with the two specified launch categories, and then `theta^sigma=beta delta_0+delta Q^sigma`. Every row is normalized, assignments are disjoint, transitions are legal shifts, and the active residual clock obeys the named phase invariant below.

**Proof.** Put `ell=K-1` and use disjoint alphabets

    C={1,...,m}, U={m+1,...,2m}, V={2m+1,...,3m}, W={3m+1,...,4m}.

Since `4m<=K-2`, these are inside A and exclude both 0 and ell. Label W in increasing order `w_1,...,w_m`. Remaining alphabet symbols are retained and receive default rows where not specified.

There exists a periodic word `c_0,...,c_(L-1)` on C such that the pairs `e_t=(c_t,c_(t+1))`, `0<=t<L`, enumerate C-squared exactly once (indices periodic). A finite construction is as follows. In the complete directed graph on C, including loops, every vertex has equal in/out degree m. A maximal unused-edge walk closes: if it ended at a different vertex, that terminal vertex's used incoming degree would exceed its used outgoing degree by one, leaving an unused outgoing edge. Remove the closed walk's edges, preserving balance. If edges remain, some vertex of the tour has an unused outgoing edge; otherwise completeness forces all vertices visited and all their outgoing edges used. Start a new closed walk there and splice it. Each splice consumes at least one of the finite m-squared edges. The completed tour supplies the word. Rotate it to have `c_5=1`; vertex 1 occurs, and `L>=9`. Fix one such word for each m, independently of signs/data.

For each `s in U x V` and `1<=j<=r`, let `sigma_(s,j) in {-1,+1}`. The finite cube of these signs indexes the family. Define the W-supported probability vector

    q_sigma(w_(2j-1)|s)=(1+alpha sigma_(s,j))/m,
    q_sigma(w_(2j)|s)=(1-alpha sigma_(s,j))/m.                             (3.3)

For odd m the leftover `w_m` has mass 1/m. Each pair sums to 2/m; all W entries are at least `1/(2m)`. Thus every such row is a probability vector on the same positive W support.

Define the phase sets

    D_0={e_0}, D_1={c_1} x U, D_2=U x V, D_3=V x W,
    D_4=W x {1}, D_t={e_t} for 5<=t<L, D=union_t D_t.                    (3.4)

They are disjoint: the ordered alphabet types separate D_1,...,D_4 and C-squared, while the e_t are distinct. All coordinates in D are nonzero and differ from ell. On D define the active residual rows

    Q_(e_0)=Unif(U),              Q_(c_1,u)=Unif(V),
    Q_(u,v)=q_sigma(.|u,v),      Q_(v,w)=delta_1,
    Q_(w,1)=delta_(c_6),         Q_(e_t)=delta_(c_(t+2)), 5<=t<L.          (3.5)

Now add exactly the launch rows

    Q_(ell,0)=Unif(U),           Q_(0,u)=Unif(V), u in U,                 (3.6)

and set **every other row** to `delta_0`. These include all rows ending in ell, all ending-0 rows except `(ell,0)`, unused C-pairs `e_1,...,e_4`, and all leftover-letter rows unless explicitly specified (none is). The launch categories contain 0, so are disjoint from D; they are also mutually disjoint. Within (3.5), disjointness follows from (3.4). There is no competing assignment.

All Q rows are probabilities, hence so are all theta rows `beta delta_0+delta Q_s`. The fixed table contains no time or count dependence. Appending a symbol always means `(a,b)->(b,c)`, so there are no additional clock states or non-shift transitions.

**Active phase invariant (`inv:s014-phase`).** Under residual transitions, a state in D_t goes to D_((t+1) mod L). Indeed the five-step segment is

    e_0 -> (c_1,A) -> (A,B) -> (B,Z) -> (Z,1) -> (1,c_6)=e_5,             (3.7)

with A in U, B in V, Z in W. The last equality uses `c_5=1`; the return state is not `(Z,0)`. Thereafter the deterministic clock rows go from e_t to e_(t+1), including the wrap to e_0. Every active residual output is nonzero and not ell. This checks every phase and proves the invariant and closure by induction. The launch path is

    (ell,0) -> (0,A) -> (A,B) in D_2,                                   (3.8)

with two successive uniform choices. It also never outputs 0 or ell. ∎

### unit_003: Lemma 3 — Sparse stationary witness and every-pair minorization (`lem:s014-member`)

**Statement.** Under Lemma 2 and `0<beta<1`, every sign's table has the stationary law `pi=delta_(0,0)`, symbol marginal `p=delta_0`, and satisfies (1.1) for every starting and destination pair. More exactly, writing

    R=D union {(ell,0)} union ({0} x U),

its two-step mass at 00 is beta for every row in R **and every row ending in ell**, and is one at all other starting rows. Thus its maximal coefficient relative to this pi is exactly beta.

**Proof.** Row 00 is default and outputs 0 with probability one, making pi stationary. Its two coordinate marginals are both `delta_0`. For every row s in R, the residual output has no zero mass, hence `theta_s(0)=beta`. If `s=(a,b)` belongs to R, its second coordinate b is not ell. Therefore `(b,0)` is default, even when b=0, and `theta_(b,0)(0)=1`. The exact two-step path formula gives

    P^2(s,(0,0))=theta_s(0) theta_(b,0)(0)=beta.                           (3.9)

Every starting row ending in ell is default, because ell appears in no active coordinate and the sole launch row involving ell is `(ell,0)`. From `(a,ell)` the first output is thus 0 with probability one, but the next row `(ell,0)` is exceptional and outputs 0 with probability beta. This gives two-step mass beta, not one. This case includes `(0,ell)` and `(ell,ell)`.

A remaining starting row is default and has second coordinate b different from ell. Its first output is 0 surely, and `(b,0)` is default, so its two-step mass at 00 is one. These three categories exhaust all K-squared rows and do not overlap. At every destination other than 00 the right side `beta pi(t)` is zero, so nonnegativity proves the remaining inequalities. Some rows attain (3.9), so the coefficient is exact. No assertion about stationary support or absolute continuity of the initial law was used. ∎

### unit_004: Lemma 4 — Complete aligned history and survival invariant (`lem:s014-history`)

**Statement.** Under Lemmas 2–3, initialize at `mu=delta_(ell,0)=delta_ell tensor p` and observe N departures as in (1.5). In the standard independent refresh realization of Lemma 1, let `E={J_0=...=J_(N-1)=0}`. Then `P_sigma(E)=delta^N`. Conditional on E, UV states occur exactly at

    t_j=2+(j-1)L, 1<=j<=q+1, t_(q+1)=N.                               (3.10)

There are q observed unknown-row departures and the actual terminal UV row. The ENTIRE conditional history is in a common public bijection with q labeled triples and this actual endpoint, with exact product law (3.12) below.

**Proof.** Independent coins at every row reproduce theta because its mixture is defined on every row. Conditional on all N coins being zero, (3.8) gives the first two steps from the fixed pair `(ell,0)` to D_2. The phase invariant then gives

    Y_t in D_((t-2+2) mod L)=D_(t mod L), 2<=t<=N,                       (3.11)

where times are absolute from the launch start. Hence UV visits are precisely (3.10). The first q visits are observed departures because the last such time is N-L<N, and the visit at N is the target with no observed departure. Define

    (A_j,B_j,Z_j)=(X_(t_j+1),X_(t_j+2),X_(t_j+3)), 1<=j<=q,
    T=(A_(q+1),B_(q+1))=(X_(N+1),X_(N+2))=Y_N.

There are exactly q complete active clock cycles between the entry UV state at time 2 and the final UV state at time N. In particular no unknown label is supplied by initialization, which is the fixed observed pair ell,0.

For a tuple `((A_j,B_j,Z_j)_(j=1)^q,T)` in `(U x V x W)^q x (U x V)`, reconstruct every symbol of H_N as follows. Begin with ell,0; append A_1 and B_1 for the two launch departures. At the UV visit t_j, j<=q, append Z_j; next append 1 and then c_6; follow the deterministic clock to e_0; append A_(j+1), then B_(j+1). For j=q these last coordinates are T. Stop at time N, without a terminal label. All intermediate clock symbols are fixed. This procedure appends only one successor symbol at a time and respects every pair overlap. The appearances of Z_j in consecutive pairs are a single observed symbol, not additional random data.

Call this reconstruction G. Every tuple is possible because all U/V choices and all W labels have positive residual probability. Extraction at the displayed indices is inverse to G; reconstructing an extracted history also restores its fixed initial ell,0 and every filler. Thus G is a full-data bijection, not a potentially information-losing statistic. It depends on public construction choices, not signs or alpha. Its conditional path probability is

    P_sigma(H_N=G(D_train,T) | E)
       =m^(-2(q+1)) product_(j=1)^q q_sigma(Z_j|A_j,B_j).                 (3.12)

There are q+1 uniform context pairs, two factors 1/m each, and q label factors; all other factors are one. Hence, conditional on E, the q triples are IID with law `m^-2 q_sigma(z|u,v)` and T is uniform on U x V, independent of those triples. This is proved only for this constructed experiment, not assumed for random terminal rows generally. In particular

    P_sigma(E,T=s)=delta^N/m^2                                           (3.13)

for every s and sigma.

**Survival/absorption invariant (`inv:s014-survival`).** Before a first coin 1 the process is at `(ell,0)`, or `{0} x U`, or D according as time is 0, 1, or later. A first coin 1 appends 0. At time 0 this produces 00. At time 1 it produces `(u,0)` with u in U. At later times it produces `(b,0)` with b an active nonzero letter distinct from ell. These states are all default ending-0 states, so the next output is 0 and all subsequent pairs are 00. In particular the exceptional launch state `(ell,0)` cannot be reached after this first killing refresh. This proves induction to absorption and also shows that E is the event of no zero among the N observed outputs, despite the fixed zero already present in the initial pair. Recognizability is not needed or given as additional input. All nonsurviving histories remain in the original predictor domain and risk. ∎

### unit_005: Proposition 5 — Full-history finite-prior testing and product lower (`prop:s014-product-lower`)

**Statement.** Under Lemmas 2–4 and (1.5), every common randomized full-history predictor B satisfies (1.6) for the single uniform prior on all `m^2 r` sign bits. This lower is valid on the product stationary-second-marginal subclass of `D_K(2,beta)`.

**Proof: complete conditional information.** Fix any endpoint `s in U x V`. Every event `(E,T=s)` has the same positive probability (3.13) under all signs. Conditioning on this event leaves the uniform sign prior uniform; this does not assert a uniform posterior after the rest of the data is observed. Two sign vectors differing only at `(s_0,j_0)` change two label probabilities at the one context s_0. Their one-triple KL in either direction is exactly

    (2alpha/m^3) log((1+alpha)/(1-alpha)).                               (3.14)

The common full-history bijection G with T fixed, and the q-fold product in (3.12), give FULL conditional-history KL equal to q times (3.14), also when s_0 equals the actual conditioned endpoint s. No data-processing inequality is being used in the invalid direction of dropping informative data. Since

    log((1+alpha)/(1-alpha))=integral_0^alpha 2/(1-x^2) dx<=4alpha,

this KL is at most `8q alpha^2/m^3<=1/8`. On the square-root branch the last value is `q/[8(q+1)]`; if alpha=1/2, its selection implies `m^3>=16(q+1)`, giving the same upper bound. Both cap branches are covered.

For completeness, the finite KL-to-TV bound here is `TV(P,Q)<=sqrt(KL(P||Q)/2)`. Group the event `{x:P(x)>=Q(x)}` and its complement. Convexity of x log x shows KL is at least the binary divergence between their masses u,v. For fixed v the binary divergence in u has value and derivative zero at u=v and second derivative `1/u+1/(1-u)>=4`. Integration twice gives at least `2(u-v)^2=2TV(P,Q)^2`. The common finite positive support permits this argument, with boundaries by continuity. The neighboring full conditional-history TV is consequently at most 1/4.

For any randomized binary test integrate the independent seed, giving a common probability `varphi(H) in [0,1]` of output +. Its error probabilities under neighboring plus/minus signs obey

    P_+(error)+P_-(error)
      =1-sum_H(P_+(H)-P_-(H))varphi(H)>=1-TV(P_+,P_-)>=3/4.              (3.15)

Fix the other bits and pair the two values of the tested bit. Under the same uniform cube prior, (3.15) implies average conditional bit error at least 3/8, for each endpoint s and its each bit j. Conditioning on E,T does not change the seed law since the seed is independent of the path and coins.

**Proof: changed target and actual endpoint.** On E the target at T=s is the NEW row

    theta^sigma_s=beta delta_0+delta q_sigma(.|s),
    theta^sigma_s(w_(2j-1))-theta^sigma_s(w_(2j))
        =2delta alpha sigma_(s,j)/m.                                    (3.16)

Decode a bit from B's output as + when its first listed W-coordinate is at least the second, otherwise -. If this test is wrong, the predicted contrast differs from the true contrast by at least `2delta alpha/m`. The triangle inequality shows that pair's half-L1 loss is at least `delta alpha/m`. A tie with minus truth is an error and satisfies the bound; a tie with plus truth is not counted. Summing disjoint W pairs gives pointwise on E

    TV(B(H_N),theta^sigma_(Y_N))
       >=(delta alpha/m) sum_(j=1)^r 1{decoded bit != sigma_(T,j)}.        (3.17)

Mass assigned to other coordinates only adds nonnegative loss. Composing B with the common complete reconstruction G at each fixed s gives exactly the common tests used in (3.15), no hidden-parameter oracle. Averaging first over full data and the one sign prior, then the actual endpoint probabilities 1/m^2, gives

    Av_sigma E_sigma[TV(B(H_N),theta^sigma_(Y_N)) | E]
        >=(delta alpha/m)(1/m^2) sum_s sum_(j=1)^r 3/8
        =3delta alpha r/(8m)>=delta alpha/8.                             (3.18)

For m>=3, r/m is 1/2 if m is even and `(m-1)/(2m)>=1/3` if odd. Multiply (3.18) by the common survival probability delta^N and discard only the nonnegative risk on E-complement. This proves (1.6) without claiming those other histories uninformative.

Finally each constructed table satisfies Lemma 3 and has `p=delta_0`, while initialization is literally `nu tensor p` with `nu=delta_ell`; its second marginal is stationary and independent of its first. It is not pair-stationary: `delta_(ell,0)!=delta_(0,0)`. For any fixed B, the source supremum over that subclass dominates the finite-prior average just obtained. Only afterwards may one take infimum over B. The hard sign may depend on the algorithm/public horizon; no single sign is asserted hard for all predictors. ∎

### unit_006: Proposition 6 — Exact family-only upper (`prop:s014-family-upper`)

**Statement.** For the constructed family at product start and N departures, the common predictor `B_0(H)=delta_0` has risk exactly `delta^(N+1)` on every sign, proving (1.7). The finite-family common minimax risk is therefore between `delta^(N+1)alpha/8` and `delta^(N+1)`.

**Proof.** On E the actual row is (3.16), with mass exactly delta outside 0, so the TV loss of B_0 is delta. On E-complement, the survival/absorption invariant ensures the terminal state is either an ending-0 default state (if killing was last) or 00. Its target is already delta_0 and loss is zero. This includes a first refresh during either launch step and does not overlook the exceptional `(ell,0)`: after killing, no preceding coordinate can be ell. Therefore the risk is `P(E)delta=delta^(N+1)`. This predictor reads no signs, p, or coin labels. It is only a uniform upper on this specified family and initialization, not on the product subclass or D_K as a whole. ∎

### unit_007: Proposition 7 — Immediate-refresh prefix with exact event weight (`prop:s014-prefix`)

**Statement.** Under Lemmas 2–4 and (1.5), run the same table from `(X_1,X_2)=(0,ell)` for total `M=N+1` departures. In the standard all-row independent-coin realization define `tau=min{t:J_t=1}` among `0,...,M-1`, and `tau=infinity` if none. The first output X_3 is deterministically 0. Conditional on tau=0, the entire experiment is exactly the N-departure product experiment with a fixed observed initial prefix attached. Every common full-M-history predictor satisfies (1.8), event probability is beta, and B_0 satisfies (1.9). The lower is not multiplied by any further conditioning probability except where explicitly shown.

**Proof.** The row `(0,ell)` is default. Its residual Q and its refresh distribution p both equal delta_0. Thus `X_3=0` under either value of J_0. The event `tau=0` is precisely `{J_0=1}`, has probability beta under every sign, and is independent of all future coins, residual samples, and seed. After the first departure the pair is `(ell,0)` surely. Subsequent dynamics use exactly the original theta table, with N departures remaining.

To make the full information equality explicit, put `Z_i=X_(i+1)` for `1<=i<=N+2`. The suffix `Z_1,...,Z_(N+2)` starts at ell,0 and is the complete N-departure product history, while the original full history is exactly

    H_M=(0,Z_1,...,Z_(N+2)).                                              (3.19)

The final pair of this suffix is `(Z_(N+1),Z_(N+2))=(X_(M+1),X_(M+2))`, the original actual terminal pair. The unobserved next symbol is likewise the same. The mapping in (3.19) retains, rather than deletes, every observed symbol: the omitted X_1 in the suffix is recovered as the fixed 0. All public parameters of the two experiments are linked by M=N+1.

Fix a predictor B on all `M+2` symbols. Composing it with the fixed-prefix map (3.19) produces a common randomized predictor on the N-departure product experiment, allowed to depend on the same public constants. It is common across all signs and its seed remains independent. Proposition 5 therefore gives

    Av_sigma E_sigma[TV(B(H_M),theta^sigma_(Y_M)) | tau=0]
        >=delta^(N+1)alpha/8=delta^M alpha/8.

Proposition 6 gives the exact corresponding B_0 conditional risk delta^M. An auxiliary conditional experiment may explicitly reveal the value tau=0; on this event it is a fixed common sign-independent label and simply yields another common composed predictor. The lower remains valid even with that label. The actual original predictor is not given it, nor any other label or p.

Since the conditioning probability is beta for each sign, finite averaging yields exactly

    Av_sigma E_sigma[1_{tau=0} TV(B(H_M),theta^sigma_(Y_M))]
       =beta Av_sigma E_sigma[TV(B(H_M),theta^sigma_(Y_M)) | tau=0]
       >=beta delta^M alpha/8.                                          (3.20)

It is invalid to remove beta when interpreting this as an unconditional contribution. In fact the first visible output is independent of J_0 because both component rows are delta_0, so the unconditional prefix experiment also has the same visible suffix law; this observation does not change the event weight in (3.20). ∎

### unit_008: Corollary 8 — Aligned logarithmic sequence negates uniform restoration (`cor:s014-log`)

**Statement.** For integer K tending to infinity along (1.10), all conditions (1.5) and `0<beta<1` hold, and

    N~K^4, M~K^4, alpha=1/2 eventually,
    delta^(N+1)=delta^M=K^(-1/4)(1+o(1)),
    a_N~K^(-1/2), a_M~K^(-1/2),
    sqrt(beta)=O(K^(-2)sqrt(log K))=o(K^(-1/2)).                         (3.21)

Consequently no finite universal C and no selection of common predictors at public parameters can uniformly bound the product-initialized subclass risk at N by `C(a_N+sqrt(beta))`; nor can such a bound uniformly control the immediate-refresh conditional risk at total M by `C(a_M+sqrt(beta))` (or by the equivalent remaining-horizon a_N version).

**Proof: parameter admissibility and exact horizon control.** For K>=14, m>=3 and `m<=K/4`, so `L<=K^2/16`. Consequently `K^4/L>=16K^2>1` and q is an integer at least one. The floor relation yields

    K^4-L+2 < N <= K^4+2,
    |N/K^4-1| <= (L+2)/K^4 <= 1/(16K^2)+2/K^4.                         (3.22)

Thus N/K^4 and M/K^4 tend to one, with M=N+1 kept exactly. Also `N>K^4-L>=K^4-K^2/16>K` for K>=14. Since `log K<K`, the beta in (1.10) lies strictly between zero and 1/4, in particular below one.

For all K>=14, write `K-2=4m+e`, `0<=e<=3`, so `m>=(K-5)/4>=K/8`. Since `q+1<=K^4/m^2+1`,

    m^3/(q+1)>=m^5/(K^4+m^2)
      >=K^5/[8^5(K^4+K^2)]
      =K/[8^5(1+K^-2)] >=K/(2*8^5).                                   (3.23)

For example all `K>=32*8^5` make the final expression at least 16. Hence alpha=1/2 eventually, with a numerical threshold justified explicitly. No threshold depends on a source or algorithm.

**Proof: survival with controlled remainder.** For `0<=x<1`, integration gives

    0<=-log(1-x)-x=integral_0^x t/(1-t)dt<=x^2/[2(1-x)].                 (3.24)

Here `N beta=(log K)/4` exactly, while

    (N+1)beta=(log K)/4+beta,
    (N+1)beta^2 <= (N+1)(log K)^2/(16N^2) ->0

by (3.22). Multiplying (3.24) by N+1 gives

    |log(delta^(N+1))+(log K)/4|
        <=beta+(N+1)beta^2/(2delta) ->0.                                (3.25)

Exponentiating proves the survival expression in (3.21), equally delta^M because M=N+1. There is no replacement of N with K^4 inside an exponential without this error control.

The cap in a_N is inactive eventually because `K^3/(N+1)->0`; (3.22) gives `a_N K^(1/2)->1`, and the same for `a_M` because its denominator is M+1=N+2. Furthermore

    sqrt(beta)=sqrt(log K)/(2sqrt(N)),
    sqrt(beta)/K^(-1/2) = sqrt(K log K)/(2sqrt(N)) ->0.                  (3.26)

For example (3.22) implies `N>=K^4/2` throughout this domain, giving the explicit bound `sqrt(beta)<=K^-2 sqrt(log K/2)`. All o(1) and O constants in these sequence statements are numerical; only K varies.

**Proof: common-algorithm negation.** By Propositions 5 and 7, for every common B at each fixed K the appropriate source supremum is at least `delta^M/16` once alpha=1/2. From (3.21), for either h=N or h=M,

    [delta^M/16]/[a_h+sqrt(beta)] ~ K^(1/4)/16 ->infinity.               (3.27)

For any finite C choose a sufficiently large integer K to make this ratio larger than C. Then EVERY common predictor at that parameter point has some sign source violating the proposed upper. This order is stronger than a bad result for one estimator: B is fixed first, the finite-prior average applies, the worst sign is selected, and only then could the infimum over B be taken. It also covers predictors which know the entire public construction, as none of that common information changes (3.15). This proves exactly the two claimed negations; no arbitrary all-residue horizon assertion is needed. ∎

### unit_009: Proposition 9 — Weighted aggregate boundary and exact disintegration (`prop:s014-weighted`)

**Statement.** Under the general symbol-refresh construction with h departures and any common predictor, writing `loss_h=TV(B(H_h),theta_(Y_h))` for the loss, first-refresh disintegration is

    E loss_h = delta^h E[loss_h | tau=infinity]
                +sum_(t=0)^(h-1) beta delta^t E[loss_h | tau=t].           (3.28)

For the particular prefixed launch family, B_0 has exact weighted after-refresh contribution `beta delta^M`, and exact total risk delta^M. The new conditional lower (3.20), and this launch family itself, do not refute a possible full-class weighted after-refresh upper `O(a_M+sqrt(beta))`, nor the proposed full-class total upper `O(a_M+delta^M g_M+sqrt(beta))`. Their validity on the full class is not settled by this unit.

**Proof.** The independent coins give `P(tau=t)=delta^t beta`, because coins before t are zero, the coin at t is one, and future coins are unconstrained. Probability of none is delta^h. These events partition the probability space; all have positive probability under `0<beta<1`. Bounded finite-experiment conditional expectation therefore gives (3.28) exactly. The t-th term is weighted, even if its conditional loss is comparatively large. Conditional losses keep the full observed prefixes and actual terminal targets.

In the prefix family, the first departure always produces 0 and starts the launch suffix. By the survival/absorption invariant, B_0's loss is delta exactly when the N suffix coins `J_1,...,J_(M-1)` are all zero, and is zero otherwise. This statement does not constrain J_0. Its total risk is consequently `delta^N delta=delta^M`. Of the positive-loss paths, the event `tau<M` occurs exactly if J_0=1. Thus

    E_sigma[1_{tau<M} TV(B_0(H_M),theta^sigma_(Y_M))]
        =beta delta^N delta=beta delta^M                                (3.29)

for every sign. The no-refresh part is `delta^(M+1)` and these two parts sum to delta^M, consistently with (3.28). Meanwhile (3.20) lower-bounds the worst-sign/prior contribution by `beta delta^M alpha/8`, not by `delta^M alpha/8`.

Because `0<beta<1` and `delta^M<=1`, expression (3.29) is at most `beta<=sqrt(beta)`. Thus this finite family actually has a common predictor satisfying the putative weighted scale with constant one. On (1.10), `M+1<=K^4+4<K^5` for K>=14, so g_M=1. Its exact total risk delta^M is then at most `a_M+delta^M g_M+sqrt(beta)`, again with constant one. Along the sequence the weighted lower is merely of order `K^(-17/4) log K`, whereas a_M has order `K^-1/2`; this can also be read directly from beta times (3.21). Therefore a large conditional loss in this construction cannot be advertised as a refutation of either weighted aggregate target.

This is a local nonrefutation statement, not an upper theorem for all sources and not a claim that no different family can decide the aggregate question. In the bounded S014 dependency set, that question remains open. Neither the old false faster-state-TV route nor stronger testing on this same launch family is revived. ∎

## 4. Target-step assembly and explicit-rate audit

Lemma 1 proves the universal no-refresh original-rule bridge from exact all-pair minorization, with hidden p and auxiliary coins never supplied to the algorithm. Lemmas 2–3 construct the entire lawful table and discharge every stationary/minorization requirement, including default rows ending in ell. Lemma 4 establishes the launch entry, recurring phase and absorption invariants, and a bijection retaining every observed symbol. Proposition 5 proves the new-target actual risk lower by testing the FULL conditional data and then restoring the exact survival probability. Proposition 6 gives the exact family-only upper. Proposition 7 retains the deterministic prefix and exposes the extra event weight beta. Corollary 8 verifies the aligned sequence and quantifier-level rate negation. Proposition 9 proves why these results do not decide the weighted aggregate target.

- **Exposed parameters:** general K>=2,M>=1,0<beta<1 for Lemma 1; counterexample K>=14,q>=1 and exact N=2+qL, M=N+1. Every finite lower coefficient and horizon shift is displayed. No all-residue expansion or beta endpoint theorem is claimed.
- **Fixed versus varying:** theta and its signs remain fixed during a trajectory. K alone varies in (1.10); all construction/algorithm choices at each parameter point obey the same public-parameter information rule. Every asymptotic constant is numerical and cannot depend on signs, source, pi, nu, history, algorithm or seed.
- **Mode:** deterministic finite horizon, expected actual half-L1 TV; conditional expectations are explicitly tagged by E or tau=0, then weighted by delta^N or beta where used unconditionally. KL is only a testing tool. There is no squared-TV, high-probability, independent-query, all-time or stopped-horizon replacement.
- **Random endpoint and counts:** the actual endpoint remains part of the full history and target. No conditional-IID assertion is made about general random visits or row counts. The finite family obtains its special product identity only by complete reconstruction. Add-one's zero counts remain defined via n_s+K, and Lemma 1 invokes the exact accepted interface handling them.
- **Baseline distinction:** the generic no-refresh result uses the unchanged original rule; it does not borrow a suffix bound. The active clock/testing architecture is attributed to MM5/S012; the new launch and prefix alter its initialized experiment and are proved afresh. On stationary initialization pi this particular family stays at 00, so the product-start obstruction does not contradict the accepted stationary rate. A stationary second-coordinate marginal, even with an independent first coordinate as in `mu=nu tensor p`, does not imply `mu=pi`. No inclusion of all stationary initial laws in this product subclass is claimed; stationary pair laws need not be products.
- **Remaining scope:** no full product-class upper or general arbitrary-start joint minimax formula is proved. Family upper and conditional lower do not solve the weighted target. New subsequent candidates, if any, are outside this frozen proof.

## 5. Notation and assumption provenance

Public-facing objects are the exact class/experiment, original estimator, rate functions, and exported finite lower/event bounds with their domains. The aligned parameters m,L,q,N,M,alpha are deterministic public expressions for the stated counterexample, not hidden tuning chosen from the observations. The threshold in (3.23) is a derived numerical sufficient threshold.

The symbol distribution p is the original hidden stationary witness's marginal, constructed algebraically in Lemma 1. Residual Q, coins J, E/E0, tau, phase sets, Euler word, signs, q_sigma, reconstruction G, labeled triples and tests are proof-local. Their existence, legality, phase, absorption, product-law and probability assertions are derived in the named units; none is silently elevated to a primitive assumption. The finite uniform prior is common across all tested bits and endpoints. Conditional hypotheses E, T=s, and tau=0 occur only in explicitly conditional claims with positive common probabilities proved before use.

The coefficient 48 is inherited solely from L1+. The factors 1/8, 3/8, and 1/16 are justified by the explicit sign contrast, neighboring-law testing, r/m bound and amplitude cap. No undefined finite constant or source-dependent boundedness assertion is used. The generic package has no stable assumption IDs, so actual primitive content is stated rather than inventing historical assumption labels.

A producer-owned inline exact-rational sanity check verified 4,706 full rows across m=3,4,5 and every K from 4m+2 through 4m+5 at beta=1/5: normalization, all starting-pair masses at 00, and every residual phase successor. Separate checks at the actual prescribed amplitudes (m=3,q=2,alpha=3/8) and (m=4,q=1,alpha=1/2) inspected 7,585 complete residual histories and 33,148 complete product/prefixed actual histories. They checked full conditional path factors, actual endpoint placement, survival factors, absorption targets, exact delta^(N+1) risk and equality of every prefixed path law to its product law. All checks passed. These finite checks supplement the general proof; they are not formal or independent review, and no checker file was created.
