# S012 允许稀疏平稳律的吸收时钟下界

编排说明（非原文）：以下逐字保留原已接纳版本的完整数学论证、必要定义、范围与科学解释，仅省略身份、内部控制和来源元数据。原有数学编号及 Euler clock 名称不变。新增标题与本说明不是原证明。依赖闭包与源哈希见 ../SOURCES.md，精确字节映射见 ../COPY_MAP.json。本次编排不是重新证明或对复制件的新数学审查。

编排符号补充（非原文）：§2 的 R_min 指不加 minorization 限制的全部合法齐次表 θ 与任意初始律 μ 上的 inf_B sup L_B；即 MM5 的一般初始化 minimax 风险。它不等于固定原规则的 R_D2⁺。

For every integer `K>=2,M>=1` and public `beta in [0,1]`, in the arbitrary-initialization, legal second-order-shift class `D_K(2,beta)` defined below,

    R_D2(K,M,beta) >= max{ F/180,
                          2^-16 (1-beta)^(M+1) min(1,sqrt(K^5/(M+1))) }.       (S012)

The inherited IID floor remains `i/(32 sqrt(6))`, in particular at beta one, where the second term of (S012) is zero and does not describe the rate. If `(M+1) beta<=1`, the unchanged original full-history add-one rule and common minimax risk have matching general rate `g=min(1,sqrt(K^5/(M+1)))`, with the explicit sandwich in Corollary 7. Thus the old sequence `M=K^4,beta=K^-6` is now matched, not a remaining true-risk gap.


## 1. Exact experiment, allowed assumptions, and theorem

Fix integers `K>=2,M>=1` and public `beta in [0,1]`. Write `A={0,...,K-1}`. A source is a fixed homogeneous table `theta=(theta_ab(c))` with nonnegative normalized rows, and an arbitrary initial pair law mu. Its kernel is exactly the legal shift

    P_theta((a,b),(b,c))=theta_ab(c),

and zero on non-shift transitions. The source belongs to `D_K(2,beta)` when some hidden probability law pi satisfies

    pi P_theta=pi,       P_theta^2(s,t)>=beta pi(t) for EVERY s,t in A^2.      (1.1)

Zero entries, reducibility, and zero stationary masses are permitted. In particular mu need not equal pi or be absolutely continuous with respect to pi. Beta is a public lower bound, not an oracle giving the maximal coefficient. At fixed public parameters the source can be selected in a supremum, but it cannot change during a trajectory.

The data are the entire `H=(X_1,...,X_(M+2))`; let

    Y_t=(X_(t+1),X_(t+2)),             0<=t<=M.

There are exactly M observed departures, at t=0,...,M-1. The target is the SAME actual terminal row `theta_(Y_M)` for the unobserved `X_(M+3)`. A common predictor B is a probability kernel from the entire H to the K-simplex. It may use public `K,M,beta` and an independent random seed, but no hidden source, pi, signs, hazard labels, or future symbols. Put

    L_B(theta,mu)=E TV(B(H),theta_(Y_M)),       TV(p,q)=||p-q||_1/2,
    R_D2=inf_B sup_((theta,mu) in D_K(2,beta)) L_B(theta,mu).

Keep separately the original full-history rowwise add-one rule

    C_s(c)=sum_(t=0)^(M-1) 1{Y_t=s,X_(t+3)=c},
    N_s=sum_c C_s(c),             p_s^+(c)=(C_s(c)+1)/(N_s+K),
    R_D2^+=sup_(D_K(2,beta)) E TV(p^+_(Y_M),theta_(Y_M)).

The only primitive assumptions are these exact finite-domain, homogeneity, legal-shift, initialization, observation, information and class conditions. The original setting has no stable assumption IDs; this paragraph records their content rather than inventing upstream IDs. All clock support, stationary membership, phase invariants, survival probabilities and conditional experiments below are derived, not added hypotheses.

Use the public quantities

    n=M+1, delta=1-beta,
    i=min(1,sqrt(K/n)), a=min(1,sqrt(K^3/n)), g=min(1,sqrt(K^5/n)),
    F=max{i,min{delta,a}}.                                                   (1.2)

**Theorem S012.** In this exact experiment, (S012) holds on the full stated domain. More strongly, for `K>=13` and `0<beta<1`, set

    m=floor((K-1)/4), L=m^2, q=floor(M/L), r=floor(m/2),
    alpha=min{1/2,(1/8)sqrt(m^3/(q+1))}.                                     (1.3)

There is the explicit finite family below, with a common horizon-aligned initial law and stationary witness `pi=delta_(0,0)`, such that EVERY common randomized B has prior-average risk at least

    delta^n alpha/8 >= 2^-16 delta^n g.                                     (1.4)

The exact constant predictor `B_0(H)=delta_0` has risk `delta^n` on EVERY member of this family. Corollary 7 and Proposition 9 give the required bounded-hazard and scalar-window conclusions.

## 2. Accepted interfaces and local lemma map

The following are inherited exact-target results, not new proofs or imported assumptions about this new family.

1. **MM5**, readable proof Sections 1–9 and complete independent report: the unrestricted arbitrary-initialization class has `R_min>=2^-16 g` for every K,M and every common randomized complete-history predictor. Its Sections 2–8 also give the four-alphabet Euler clock, six initial-phase cases, complete-history bijection and finite testing machinery. We reuse that design with explicit attribution, but prove the relabeled table, changed off-support behavior, complete conditional data experiment and NEW target contrast below. We do **not** infer (1.4) from an old black-box risk lower bound. The all-K MM5 theorem is used directly only for beta zero.
2. **L1MAX**, statistical interface L1+: for every legal homogeneous source and arbitrary initial law, the ORIGINAL full-history add-one risk is at most `min{1,48sqrt(K^5/n)}`. Restricting its source supremum to (1.1) is legitimate. No implementation, resource, precision or fault result is used.
3. **S006, Lemma 3:** its actual stationary IID witnesses, with all M+2 informative observations retained, give `i/(32sqrt(6))` for every public beta. Every such IID table has `P^2(s,(c,d))=p(c)p(d)` and initial `p tensor p`, so is an allowed subclass of the present arbitrary-mu class. This supplies the small-K patch, not a stationary-initialization assumption on the clock.
4. **S011, Theorem S011 and Proposition 5:** the present exact class has `R_D2>=F/180`; its algorithm-separated upper certificates are reproduced exactly in Proposition 9. At beta zero it has the MM5/L1MAX general-rate endpoints; at beta one it consists of all-row IID tables with arbitrary mu and has the pooled upper `min{1,(1/2)sqrt(K/M)}<=i`. These inherited results already checked the needed S003/S004/S006 interfaces; we do not recertify those predecessor proofs.
5. **S010**, accepted positive-uniform-smoothing theorem, is only used for the preservation/comparison statement: on `K>=12,0<beta<=K^-4` its lower `2^-16(1-8sqrt(beta))^n g` remains valid, with the extra positive-source feature. No S010 proof mechanism is used to derive the absorbing family.

All these lower interfaces quantify over every fixed common predictor, including one that sees the shared public beta. Consequently each bound holds before the infimum, and distinct hard subclasses can be combined by a maximum, not by adding their risks.


| Local unit | Named result and stable label | Contribution |
|---|---|---|
| unit_001 | Lemma 1, Reserved-symbol legal clock (`lem:s012-clock`) | Full table, finite Euler existence, active support and phase invariant |
| unit_002 | Lemma 2, Sparse stationary law and exact minorization (`lem:s012-member`) | All K-squared starting pairs, including every inactive row |
| unit_003 | Lemma 3, Every-remainder complete experiment (`lem:s012-history`) | Six initial laws, full-history bijection, no-hazard conditional law |
| unit_004 | Lemma 4, Full conditional information and tests (`lem:s012-info`) | Actual-endpoint neighboring KL/TV and randomized error |
| unit_005 | Proposition 5, New-target finite-family lower (`prop:s012-lower`) | Changed W contrast, one prior, unconditional expected TV |
| unit_006 | Proposition 6, All-K constants and endpoint assembly (`prop:s012-allk`) | m/K comparison, small K, max with F, beta endpoints |
| unit_007 | Corollary 7, Bounded-hazard matching (`cor:s012-bounded`) | Explicit survival bound and old sequence closure |
| unit_008 | Proposition 8, Exact same-family upper (`prop:s012-family-upper`) | Constant source-blind predictor and route limitation |
| unit_009 | Proposition 9, Remaining scalar-certificate window (`prop:s012-window`) | Optimized all-burn lower/upper certificate calculations |

## 3. Local derivation

### unit_001: Lemma 1 — Reserved-symbol legal clock (`lem:s012-clock`)

**Statement.** Under Section 1's experiment, for every `K>=13`, `M>=1`, and `beta in [0,1]`, the construction in this lemma is a normalized homogeneous legal-shift table on ALL K-squared rows. The active base dynamics have a disjoint cyclic phase partition of length L, all their symbols are nonzero, and their active support is closed under every base transition.

**Proof.** Use (1.3), so `m>=3,L>=9`. Reserve symbol 0 and take the disjoint sets

    C={1,...,m}, U={m+1,...,2m}, V={2m+1,...,3m}, W={3m+1,...,4m}.

Since `4m<=K-1`, these sets are in A and exclude 0. Any remaining symbols are still in A and will receive default rows. Label W as `w_1,...,w_m` in increasing order.

There is a cyclic word `c_0,...,c_(L-1)` on C, extended periodically, such that `p_t=(c_t,c_(t+1))` enumerates each ordered C-pair once. Here is the finite existence argument. Place every directed edge between C-vertices, including loops. Each vertex has equal indegree and outdegree m. A maximal unused-edge walk cannot terminate away from its starting point: the terminal vertex would have one more used incoming than outgoing edge, and degree balance would leave an outgoing edge unused. Thus it closes. Removing used edges preserves balance. If any unused edge remains, some vertex of the current closed tour has an unused outgoing edge: otherwise all outgoing edges of every visited vertex would already have been traversed, and completeness would imply every vertex was visited and every edge used. Start another closed unused-edge walk at such a vertex and splice it into the tour. The used edge count strictly increases and is at most m-squared, so finitely many splices exhaust all edges. Reading vertices gives the word. Rotate it so `c_5=1`, possible since vertex 1 occurs; this public choice depends only on m. A loop rotation with `c_5=c_6=1` is also possible but is not needed. All pairs `p_0,p_5,...,p_(L-1)` are distinct.

For the finite sign index set `I=(U x V) x {1,...,r}`, choose `sigma in {-1,+1}^I`, fixed for the whole trajectory. For every `s=(u,v) in U x V`, define

    q_sigma(w_(2j-1)|s)=(1+alpha sigma_(s,j))/m,
    q_sigma(w_(2j)|s)  =(1-alpha sigma_(s,j))/m,          1<=j<=r.             (3.1)

When m is odd, the unpaired `w_m` has mass 1/m. Every other coordinate is zero. Each pair sums to 2/m, so these rows normalize; each W coordinate is at least `1/(2m)>0`.

Define the disjoint phase sets

    D_0={p_0}, D_1={c_1} x U, D_2=U x V, D_3=V x W,
    D_4=W x {1},             D_t={p_t} for 5<=t<L,
    D=union_(t=0)^(L-1) D_t.                                                 (3.2)

Disjointness follows from the ordered alphabet types and the distinct C-pairs. In particular no state in D has a zero coordinate. Define active base rows `theta_0^sigma` by

    at p_0:          Unif(U),
    at (c_1,u):      Unif(V),                  u in U,
    at (u,v):        q_sigma(.|u,v),           (u,v) in U x V,
    at (v,w):        delta_1,                  (v,w) in V x W,
    at (w,1):        delta_(c_6),              w in W,
    at p_t:          delta_(c_(t+2)),          5<=t<L.                         (3.3)

These are exactly the disjoint categories in (3.2), so there are no conflicting assignments. The new FULL table is

    theta_beta^sigma(s) = delta theta_0^sigma(s)+beta delta_0,  s in D;
    theta_beta^sigma(s) = delta_0,                            s not in D.    (3.4)

Every row is normalized and nonnegative. The table does not depend on time, counts, realized hazards or past signs. At each step it appends one symbol through `(a,b)->(b,c)`, hence is a genuine order-two shift on the original state space, not a general K-squared-state surrogate or a clock with added states. The default includes removed clock pairs `p_1,...,p_4`, every pair involving leftover letters unless already listed (none is), every pair involving 0, and all other inactive rows. In particular **every ending-0 row is inactive and outputs 0**.

The active base path from p_0 is

    p_0 -> (c_1,A) -> (A,B) -> (B,Z) -> (Z,1) -> (1,c_6)=p_5,                (3.5)

where A is uniform on U, B is uniform on V conditionally on the past, and Z has row (3.1). The equality uses `c_5=1`; the return state is `(w,1)`, NOT `(w,0)`. Continuation from p_5 to p_6,...,p_(L-1),p_0 is deterministic. Every base output in (3.3) is nonzero. Equation (3.5) replaces exactly five steps, preserving length L. Inspection of every category proves the phase invariant

    base transition from D_t goes into D_((t+1) mod L).                     (3.6)

Thus D is closed under the base, and phases are read from the actual pair itself. This proves all stated properties. No irreducibility or periodicity assertion about the full modified chain is needed. ∎

### unit_002: Lemma 2 — Sparse stationary law and exact all-pair membership (`lem:s012-member`)

**Statement.** Under Lemma 1's construction, for every sign and `beta in [0,1]`, `pi=delta_(0,0)` is stationary and

    P_beta^2(s,(0,0)) = beta,   s in D;
    P_beta^2(s,(0,0)) = 1,      s not in D.                                  (3.7)

Consequently (1.1) holds for EVERY starting and destination pair, for any initial mu.

**Proof.** Row (0,0) is inactive, outputs 0, and leaves (0,0) unchanged, so pi is stationary. From any inactive `(a,b)`, the first output is 0; the next pair `(b,0)` is inactive by Lemma 1 and its next output is 0. This proves the second line, including deleted clock pairs, leftover-letter pairs, all pairs containing 0 and arbitrary off-support starts.

From active `(a,b)`, the first output is 0 with probability exactly beta, since the base has no mass at 0. On that event the second output is deterministically 0. Otherwise the first output is some nonzero c and the next pair belongs to D. Regardless of its second output d, the pair after two steps is `(c,d)`, which cannot equal (0,0) because c is nonzero. This proves the first line, including beta zero and one. For the destination (0,0), (3.7) is at least beta. Every other destination has pi mass zero and the inequality follows from nonnegativity. Thus no pair is omitted and no positivity or stationary-support lower bound is assumed. ∎

### unit_003: Lemma 3 — Every-remainder complete-history experiment (`lem:s012-history`)

**Statement.** Under Lemma 1 with `0<beta<1`, there is a common initial law `mu_(K,M)` supported in D such that, on no hazard in the M observed departures, the full observed H is in public bijection with q labeled triples and the actual terminal pair. The conditional law is exactly the product experiment (3.11), retaining every observed symbol and all initial information. No hazard labels or extra observations are given to B.

**Proof: all initial phases.** Write `M=qL+d`, `0<=d<L`, and let `k=(2-d) mod L` in `{0,...,L-1}`. Fix public `v_* in V,w_* in W`. Choose the following initial pair law, common to all signs:

| k | d | Initial pair law | Initial segment before the first UV pair |
|---|---|---|---|
| 0 | 2 | `delta_(p_0)` | Draw A then B |
| 1 | 1 | `delta_(c_1) tensor Unif(U)` | Initial A, then draw B |
| 2 | 0 | `Unif(U) tensor Unif(V)` | Initial pair already (A,B) |
| 3 | L-1 | `delta_(v_*,w_*)` | `(v_*,w_*) -> (w_*,1) -> p_5`, then clock |
| 4 | L-2 | `delta_(w_*,1)` | `(w_*,1) -> p_5`, then clock |
| 5<=k<L | L+2-k | `delta_(p_k)` | Follow clock before drawing A,B |

Every law is supported in D_k, excludes 0 and is independent of sigma and alpha. It may be singular with respect to pi; that is permitted by Section 1. The initial pair is not required to come from an unobserved earlier transition. In phases 3 and 4 the fixed `w_*` is therefore retained as initial data, not falsely counted as a q_sigma label.

Under the base, (3.6) implies by induction `Y_t in D_((k+t) mod L)` for `0<=t<=M`. Hence the UV visits are exactly

    t_j=d+(j-1)L,            1<=j<=q+1,          t_(q+1)=M.                  (3.8)

Of these, only t_1,...,t_q are observed departures. Define

    Q_j=(A_j,B_j,Z_j)=(X_(t_j+1),X_(t_j+2),X_(t_j+3)), 1<=j<=q,
    T=(A_(q+1),B_(q+1))=(X_(M+1),X_(M+2))=Y_M.                             (3.9)

All training labels are observed, since `t_q=M-L` when q>=1. The final label is not observed. At M=1 one has q=0,d=1,k=1 and obtains T from initial A and one new B. At M=2 one has q=0,d=2,k=0 and draws A then B. At q=0 there are no training labels; k=2 with q=0 would require M=0 and never occurs in the domain.

**Proof: full bijection under the base.** Write `D_train=(Q_1,...,Q_q)`. Given any element of `(U x V x W)^q x (U x V)`, reconstruct H as follows. For k=0,3,4 or k>=5 use the specified fixed initial pair. For k=1 use `(c_1,A_1)`; for k=2 use `(A_1,B_1)`, taking the subscript-1 A,B from T when q=0. Run the public phase schedule. At phase 0 append the A coordinate of the next scheduled UV context; at phase 1 append its B coordinate; at each observed phase 2 append its specified Z_j; at phase 3 append 1; at phase 4 append c_6; at phases 5,...,L-1 append the specified clock successor. Stop at phase 2 at time M, with T, without appending a final label. In an initial phase-3/4 residual segment use the fixed v_*,w_* from the table, not a nonexistent training triple.

Every step appends exactly one legal symbol, so overlaps are automatically consistent. The same Z_j in successive pairs `(B_j,Z_j),(Z_j,1)` is one observed symbol, not a second draw. All prescribed U,V choices and W labels have positive base probability. Thus every such tuple gives a unique supported full history, which we denote `G_(K,M)(D_train,T)`. Extraction at (3.9) recovers the tuple, and reconstruction after extraction recovers every symbol of H, including the initial residual segment. This proves a public bijection on the common base support, rather than a one-way compression that might lose information.

Multiply the complete path probability `mu(Y_0) product_(t=0)^(M-1) theta_0^sigma(Y_t)(X_(t+3))`. Each context A and B contributes exactly one factor 1/m, including the factors supplied by the initial law at k=1 or 2. Each training label contributes one q_sigma factor. All remaining factors, including the initial fixed w_*, are one. Thus

    P_0,sigma(H=G_(K,M)(D_train,T))
       =m^(-2(q+1)) product_(j=1)^q q_sigma(Z_j|A_j,B_j).                   (3.10)

An empty product is one. Consequently the ENTIRE base experiment is exactly

    Q_1,...,Q_q IID with law
       P_sigma(Q_j=(u,v,w))=m^-2 q_sigma(w|u,v),
    T uniform on U x V and independent of D_train.                          (3.11)

The independence in (3.11) is proved only for this constructed family; it is not an assertion about random endpoint visits in general sources. T is the actual endpoint, not an added independent test query.

**Proof: modified experiment and survival.** Realize (3.4) by M independent Bernoulli(beta) coins `J_0,...,J_(M-1)`, independent of the initial draw, base transition draws and algorithm seed. At an active row, output 0 when its coin is 1, otherwise draw from the active base row. At an inactive row output 0 regardless of the coin. Conditional on any prefix, the next output law is exactly (3.4), so this auxiliary realization has the original full path law. The coins are analysis variables only.

Let `E={J_0=...=J_(M-1)=0}`. Since the initial state is active and the base is closed, E means all M transitions are base transitions, and

    P_sigma(E)=delta^M,
    P_sigma(E,T=s)=delta^M/m^2,                   s in U x V.                (3.12)

Conditionally on E, the full H therefore has (3.10) and (3.11). Conversely any first coin 1 occurs while still active and creates the first 0 output; the process then remains in ending-0 states and at (0,0). Thus E is also the event of no zero among observed outputs (and here all initial symbols are nonzero). Its recognizability is not used to give B any side information. In particular histories containing 0 remain part of the original experiment; we have not removed them from the risk or the algorithm's domain. ∎

### unit_004: Lemma 4 — Full conditional information and common randomized tests (`lem:s012-info`)

**Statement.** In Lemma 3's modified experiment, for every fixed actual endpoint `s in U x V` and every two sign vectors differing in one bit, the FULL conditional history laws given `(E,T=s)` have KL at most 1/8 and TV at most 1/4. For any common randomized binary test of that bit, its two conditional error probabilities sum to at least 3/4. Under the single uniform prior on all signs, the conditional bit error averaged over signs is at least 3/8.

**Proof.** Each conditioning event has positive common probability `delta^M/m^2` by (3.12). The conditional D_train law is exactly the q-fold product in (3.11), with the full history obtained by the same bijection `G_(K,M)(.,s)`. A single sign flip at `(s_0,j_0)` changes only two labels for context s_0. Its one-triple KL, in either direction, is exactly

    (2alpha/m^3) log((1+alpha)/(1-alpha)).                                   (3.13)

All other coordinates cancel; an unpaired W coordinate contributes zero. Taking the logarithm of the product likelihood ratio and its expectation gives the FULL conditional-history KL

    (2q alpha/m^3) log((1+alpha)/(1-alpha)) <= 8q alpha^2/m^3 <= 1/8.         (3.14)

For the first inequality, `log((1+alpha)/(1-alpha))=integral_0^alpha 2/(1-x^2) dx<=4alpha` since alpha<=1/2. If the square-root branch in (1.3) is selected, the last expression is `q/[8(q+1)]<=1/8`. If alpha=1/2, its selection implies `m^3>=16(q+1)`, so `8q alpha^2/m^3=2q/m^3<=q/[8(q+1)]<=1/8`. At q=0 the conditional data contain only the deterministic reconstruction for that T and KL is zero.

For clarity, the finite KL–TV inequality used here is `TV(P,Q)<=sqrt(KL(P||Q)/2)`. It follows by grouping the set `A_+={x:P(x)>=Q(x)}` and its complement. If `u=P(A_+),v=Q(A_+)`, the grouping inequality from convexity of `x log x` gives `KL(P||Q)>=u log(u/v)+(1-u)log((1-u)/(1-v))`. This binary divergence, as a function of u, has value and first derivative zero at u=v and second derivative `1/u+1/(1-u)>=4`; integrating twice gives at least `2(u-v)^2=2TV(P,Q)^2`. Trivial boundary cases follow by continuity or equality of P,Q. The laws in (3.14) have a finite common positive support, so no infinite-divergence issue arises. Thus their TV is at most 1/4.

For a randomized test, integrate its independent seed and let `varphi(H) in [0,1]` be the probability of output +. For the plus and minus hypotheses,

    P_+(error)+P_-(error)
       =1-sum_H (P_+(H)-P_-(H))varphi(H)
       >=1-TV(P_+,P_-) >=3/4.                                               (3.15)

This is valid for any common probability kernel; the conditional distribution of the seed is unchanged because it is independent of the source path and coins. Take the uniform prior on the finite cube `{-1,+1}^{m^2 r}`. By (3.12), conditioning on E and T=s leaves this PRIOR uniform, because the event probability is the same for every sign. (No uniform-posterior claim after observing the rest of H is made.) Fix all other bits and pair the two values of the tested bit. Each pair's conditional errors sum to at least 3/4 by (3.15); averaging `2^(m^2 r-1)` pairs and dividing by `2^(m^2 r)` yields 3/8. The argument applies also when the changed bit is at the endpoint s itself. ∎

### unit_005: Proposition 5 — New-target finite-family lower (`prop:s012-lower`)

**Statement.** Under Lemmas 1–4 with `K>=13,M>=1,0<beta<1` and the public amplitude (1.3), every common randomized complete-history predictor has prior-average ACTUAL expected-TV risk at least `delta^(M+1) alpha/8`. Therefore the same quantity lower-bounds R_D2.

**Proof.** Fix B before selecting any sign. On E the actual pair is T=s in U x V, but the target is the NEW row

    theta_beta^sigma(s)=beta delta_0+delta q_sigma(.|s),                     (3.16)

not the base q_sigma row. Given the predictor's output `p_hat=B(H,R)`, decode a bit at the actual row by + when `p_hat(w_(2j-1))>=p_hat(w_(2j))`, and minus otherwise, with ties assigned +. The true W-coordinate contrast in (3.16) is

    theta_beta^sigma(s)(w_(2j-1))-theta_beta^sigma(s)(w_(2j))
       =2delta alpha sigma_(s,j)/m.                                         (3.17)

If that test is wrong, the predicted contrast has the opposite sign or is zero, so the absolute contrast error is at least `2delta alpha/m`. The triangle inequality on the two coordinates implies their half-L1 contribution is at least `delta alpha/m` times the error indicator. A minus truth with a predicted tie is an error and obeys this bound; a plus truth with a tie is not counted. Summing over the r disjoint W-coordinate pairs gives the pathwise bound ON E

    TV(p_hat,theta_beta^sigma(Y_M))
       >=(delta alpha/m) sum_(j=1)^r 1{decoded bit differs from sigma_(T,j)}. (3.18)

Predicted mass at 0 or other coordinates contributes only additional nonnegative TV. This explicitly handles the changing target without asserting an invalid transfer of old TV losses.

For fixed s,j, compose B with the full reconstruction `G_(K,M)(D_train,s)` and integrate its seed. This gives the same [0,1]-valued test function of the complete conditional data for every sign. Lemma 4 therefore applies with conditional prior error at least 3/8. Averaging (3.18) under the one uniform sign prior and the actual endpoint weights in (3.12) yields

    Av_sigma E_sigma[TV(B(H),theta_beta^sigma(Y_M)) | E]
       >=(delta alpha/m)(1/m^2) sum_(s in U x V) sum_(j=1)^r 3/8
       =3delta alpha r/(8m) >=delta alpha/8,                                 (3.19)

because `r/m>=1/3` for every m>=3: it is 1/2 for even m and `(m-1)/(2m)>=1/3` for odd m. Multiply (3.19) by the common probability `P_sigma(E)=delta^M`; the contribution to loss on E-complement is nonnegative. Thus

    Av_sigma L_B(theta_beta^sigma,mu_(K,M)) >=delta^(M+1) alpha/8.            (3.20)

We do not assert that zero-containing histories are uninformative; their loss is simply not needed in this lower bound. Lemma 2 places every fixed source in the intended class. For this fixed B, its full-class supremum is at least the maximum over the finite family and hence its average. Taking the infimum over B only now gives the claimed minimax lower. The hard sign may depend on B and the public horizon; no single sign is asserted hard for every predictor or every M. ∎

### unit_006: Proposition 6 — All-K constants, maximum combination, and endpoints (`prop:s012-allk`)

**Statement.** Under Section 1, the complete all-K bound (S012) holds. The standalone IID floor `i/(32sqrt(6))` is retained on the entire beta interval. At beta zero the inherited full general-rate sandwich is preserved; at beta one the common risk remains between `i/(32sqrt(6))` and `min{1,(1/2)sqrt(K/M)}<=i`.

**Proof: high-K capped comparison.** For K>=13 write `K-1=4m+e`, `0<=e<=3`. Then `m=(K-1-e)/4>=(K-4)/4>=K/8` since K>=8. From (1.3), with `t=sqrt(m^3/(q+1))`,

    alpha/8=min{1/16,t/64}>=(1/64)min{1,t}.                                  (3.21)

If q=0, m>=3 gives `m^3>=27>16`, so alpha=1/2 and alpha/8=1/16; the desired `2^-16 g` bound follows from g<=1. If q>=1, then `q+1<=2q<=2M/m^2`, whence, for `z=sqrt(K^5/(M+1))`,

    t^2=m^3/(q+1)>=m^5/(2M)
        >=K^5/[2*8^5*(M+1)]=z^2/256^2.                                     (3.22)

If z<=1, either t>=1 and `min(1,t)>=z/256`, or t<1 and the same follows from t>=z/256. If z>=1, t>=1/256 gives `min(1,t)>=1/256`. Hence in all cases `min(1,t)>=(1/256)min(1,z)`. Equations (3.21)–(3.22) give `alpha/8>=2^-14 g>=2^-16 g`. Combining with Proposition 5 proves the hazard lower for K>=13 and 0<beta<1, including all capped and small-M regimes.

**Proof: small K without a new clock.** For `2<=K<=12`, put `x=sqrt(K/n)`. Then `g=min(1,K^2 x)<=K^2 min(1,x)=K^2 i<=144i`: if x>=1 the cap proves it, and if x<1 the right side is K-squared x. The accepted S006 IID floor applies on EVERY beta class and gives

    R_D2>=i/(32sqrt(6))
         >=g/(144*32sqrt(6)) >2^-16 g >=2^-16 delta^n g.                     (3.23)

Indeed `sqrt(6)<3` and `144*32*3=13824<65536`. There is no invented small-alphabet clock or lost initial observations.

**Proof: endpoint beta zero.** Every finite stochastic kernel has a stationary probability law: for any initial law nu, the Cesaro averages `T^-1 sum_(j=0)^(T-1) nu P^j` have invariance defect `(nu P^T-nu)/T` with L1 norm at most 2/T, and a convergent subsequence in the finite simplex has zero defect. Thus at beta zero condition (1.1) excludes no source. The accepted all-K MM5 lower and L1MAX upper give

    2^-16 g<=R_D2(K,M,0)<=R_D2^+(K,M,0)<=min{1,48sqrt(K^5/n)}.               (3.24)

This is the original baseline with no conservative change in its displayed constant or rate.

**Proof: beta one and the independent IID floor.** For beta one, the rows of P-squared and pi have equal total mass, so (1.1) forces `P^2(s,t)=pi(t)` for all s,t. The unique legal two-step path gives `P^2((a,b),(c,d))=theta_ab(c)theta_bc(d)`. Summing over d shows every row equals `p(c)=sum_d pi(c,d)`. Then `P^2(s,(c,d))=p(c)p(d)`, so pi is `p tensor p`. Conversely any all-row IID table has this P-squared and is admitted with arbitrary mu. The inherited S011 pooled upper is `min{1,(1/2)sqrt(K/M)}`. If i=1 this is at most i; otherwise its uncapped term divided by i is `(1/2)sqrt((M+1)/M)<=sqrt(2)/2<1`. The stationary IID subclass from S006 gives the same positive floor `i/(32sqrt(6))` for beta one and every other beta, always retaining all M+2 IID data symbols in that lower experiment. The zero hazard term at beta one is only a valid zero bound; it is not labeled optimal or used instead of this floor.

**Proof: maximum assembly and S010 preservation.** S011 gives F/180 for every fixed B on the identical public class. Proposition 5 and the endpoint/small-K cases give `2^-16 delta^n g` for every such B. The supremum risk for B is at least both, hence at least their maximum. Taking the infimum proves (S012), not a sum of different-source losses. On S010's domain, `beta<=8sqrt(beta)` and `0<1-8sqrt(beta)<=delta`; its lower certificate is therefore no larger than the new conservative hazard certificate. The positive-source theorem remains valid with its distinct extra witness property; nothing in this argument edits or invalidates S010. ∎

### unit_007: Corollary 7 — Bounded-hazard matching (`cor:s012-bounded`)

**Statement.** Under Section 1, if `n beta<=1`, then

    2^-16 exp(-2) g <= R_D2 <= R_D2^+
                          <=min{1,48sqrt(K^5/n)}<=48g.                     (3.25)

In particular at `M=K^4,beta=K^-6`, for every integer K>=2, g=1 and the same positive absolute lower constant holds.

**Proof.** Since n=M+1>=2, the condition implies `beta<=1/2`. For `0<=beta<=1/2`,

    -log(1-beta)=integral_0^beta (1-x)^(-1) dx<=2beta,

including beta zero by direct evaluation. Therefore `delta^n>=exp(-2n beta)>=exp(-2)`. Apply Proposition 6 and then L1MAX to the unchanged original estimator on the restricted class; admissibility of that estimator gives `R_D2<=R_D2^+`. The final comparison follows by separating `sqrt(K^5/n)<=1` from its complement. For the stated sequence, `n beta=K^-2+K^-6<=1/4+1/64<1`, and `K^5>K^4+1` for K>=2, so g=1. The previously unresolved certificate example is consequently matched in true general-rate order. This does not claim (3.25) whenever n beta is arbitrary or beta is close to one. ∎

### unit_008: Proposition 8 — Exact same-family upper and route limitation (`prop:s012-family-upper`)

**Statement.** For the exact family (3.4) and horizon-aligned initial law in Lemma 3, the common source-blind predictor `B_0(H)=delta_0` has risk

    L_(B_0)(theta_beta^sigma,mu_(K,M))=delta^(M+1)                           (3.26)

for every sigma. The identity holds also for the same constructed tables at beta zero and one. For `0<beta<1` the minimax risk restricted to this family lies between `delta^n alpha/8` and `delta^n`.

**Proof.** For 0<beta<1, on E the actual target is (3.16), whose mass outside 0 is exactly delta. Thus its TV from delta_0 equals delta. On E-complement the first observed hazard has occurred. If it is the last observed departure, the terminal pair has form `(b,0)` and is inactive. If it occurs earlier, the next output is 0 and all subsequent pairs are (0,0). Either way the actual terminal row is delta_0 and the predictor has loss zero. This includes a hazard at t=0 and M=1. Equation (3.12) now gives exactly `P(E)delta=delta^(M+1)` for every sign. At beta zero there is never a hazard, the base terminal target is supported on W and the loss is one. At beta one, M>=1 ensures a first zero is observed and the terminal row is delta_0; the loss is zero. These agree with (3.26), since n>=2.

Proposition 5 supplies the restricted-family lower for every B; B_0 supplies the restricted-family upper without using signs or any hidden parameter. This upper applies ONLY to the family and its specified mu. It is not a bound over the full D_K(2,beta) class. In particular it limits what a stronger testing proof on these same sources can show; it does not rule out a different hard family or a sharper full-class upper. ∎

### unit_009: Proposition 9 — Remaining scalar-certificate window (`prop:s012-window`)

**Statement.** Under the accepted S011 definitions, let integers K tend to infinity with

    M=K^4,       beta=(log K)/(4K^4).                                       (3.27)

Define the new combined displayed lower certificate

    B_low=max{F/180,2^-16 delta^n g}.                                       (3.28)

Then `B_low=Theta(K^-1/4)`, whereas the optimized S011 upper certificate U is `Theta(K^-1/8)`. In fact `B_low/(2^-16 K^-1/4)->1` and `U/K^-1/8->1`. For this same absorbing family alpha is eventually 1/2, so its restricted-family minimax risk is `Theta(K^-1/4)`. These are statements about specified certificates and the restricted family, not an identification of R_D2 on the full class.

**Proof: exact upper interfaces.** The accepted S011 certificates for the present arbitrary-start experiment are, with `0<=b<=M-1` an integer and `ell=M-b>=1`,

    h_b=delta^floor(b/2)                         (beta<1),
    u_s(ell)=min{1,48sqrt(K^3/(ell+1))},
    u_g(ell)=min{1,48sqrt(K^5/(ell+1))},

    U_+=min{u_g(M), min_(0<=b<=M-1)
                        min{1,48sqrt(K^3/(M-b+1))+13sqrt(K)h_b^(3/4)}},
    U_suf=min_(0<=b<=M-1)
                        min{u_g(M-b),u_s(M-b)+h_b u_g(M-b)},
    U_pool=min{1,(1/2)sqrt(K/M)+2delta},
    U=min{U_+,U_suf,U_pool}.                                                (3.29)

Here U_+ is assigned to the unchanged original rule, U_suf to a genuinely different deterministic public-bound-minimizing suffix add-one rule, and U_pool to empirical pooling. A public comparison of these three bounds gives `R_D2<=U`; it is not a choice based on unknown true risks. Formula (3.27) has 0<beta<1, so the separate S011 beta-one definition of h is not invoked. No new broad upper theorem is proved here.

**Proof: scalar expansions with controlled errors.** For `0<=x<1`, integration gives

    0<=-log(1-x)-x=integral_0^x t/(1-t) dt<=x^2/[2(1-x)].                   (3.30)

Along (3.27), beta tends to zero,

    n beta=(log K)/4+o(1),
    M beta^2=(log K)^2/(16K^4)->0.

Multiplying (3.30) by n therefore gives

    log(delta^n)=-(log K)/4+o(1),
    delta^n=K^-1/4(1+o(1)).                                                 (3.31)

The same bound with `floor((M-1)/2)=M/2+O(1)` gives

    h_(M-1)=K^-1/8(1+o(1)).                                                (3.32)

All error constants in these displays are numerical; only K varies in the stated sequence. There are no source-dependent limits.

For K>=2, `K^5>K^4+1` gives g=1, while

    a=sqrt(K^3/(K^4+1))=K^-1/2(1+o(1)),   i=a/K.

Since delta tends to one and a tends to zero, eventually `delta>=a` and F=a. Therefore `(F/180)/(2^-16 delta^n g)=O(K^-1/4)->0`. Equations (3.28) and (3.31) prove the stated lower-certificate asymptotic. Retaining the stronger IID floor does not change this order, since i is of order K^-3/2. Retaining the finite-family bound in (1.4) also has this order: using m>=K/8 and `q+1<=M/m^2+1`,

    m^3/(q+1)>=m^5/(M+m^2)
       >=(K/8)^5/(K^4+K^2)=K/[8^5(1+K^-2)] -> infinity.                    (3.33)

Thus alpha=1/2 eventually; by Propositions 5 and 8 this family's minimax risk lies between `delta^n/16` and `delta^n`. The lower-certificate statement does not turn either endpoint into an equality for full-class risk.

**Proof: every suffix/burn, and a matching public choice.** For every admissible ell, `ell+1<=M+1=K^4+1<K^5`, so `u_g(ell)=1`. Since b<=M-1 and 0<delta<1, `h_b>=h_(M-1)`. Therefore every suffix candidate in (3.29) satisfies

    min{1,u_s(ell)+h_b}>=h_b>=h_(M-1),
    U_suf>=h_(M-1).                                                        (3.34)

This is a uniform lower bound on the optimized certificate, not merely an estimate at a single burn.

For the upper comparison take the deterministic public length

    ell_*=floor(K^(7/2)),             b_*=M-ell_*.

It lies in `1<=ell_*<=M` and `0<=b_*<=M-1`. Since `ell_*+1>K^(7/2)`,

    u_s(ell_*)<=48K^-1/4,
    beta ell_* <=(log K)/(4sqrt(K))->0.                                    (3.35)

Moreover `beta floor(b_*/2)=(log K)/8+o(1)` and `beta^2 floor(b_*/2)<=M beta^2->0`. Equation (3.30) gives `h_(b_*)=K^-1/8(1+o(1))`. Thus the suffix candidate at b_* is at most

    48K^-1/4+K^-1/8(1+o(1))=K^-1/8(1+o(1)).                               (3.36)

Combining (3.32), (3.34), and (3.36) proves `U_suf/K^-1/8->1` without needing the exact finite minimizing burn.

**Proof: the other certificate branches.** For every admitted b,

    13sqrt(K)h_b^(3/4)
       >=13sqrt(K)h_(M-1)^(3/4)
       =13K^(1/2-3/32)(1+o(1))=13K^(13/32)(1+o(1))->infinity.              (3.37)

Hence every capped original burn term is one eventually, uniformly in b; the generic u_g(M) is also one. Thus U_+=1 eventually. Since delta tends to one, `2delta>1` eventually and U_pool=1. The suffix candidate (3.36) tends to zero, so eventually U=U_suf, establishing the asserted U asymptotic.

Finally `K^-1/8/K^-1/4=K^1/8` diverges. The distinct exponential constants behind delta^n and h_(M-1) cannot be hidden in a uniform multiplicative constant when M beta grows as log K. The new lower closes the old K^-6 sequence but leaves this narrower certificate window; the present proof neither asserts its upper exponent is necessary nor invents a full sharp interpolation. ∎

## 4. Target-step assembly, explicit-rate and assumption audit

Lemma 1 builds a full legal table with reserved 0 and the correct `(w,1)` return, and proves the active phase invariant. Lemma 2 establishes the actual sparse stationary witness and the EVERY-pair minorization, including all inactive starts. Lemma 3 supplies the six initial laws and a complete, reversible encoding of the conditional full history, not reduced data. Lemma 4 computes its actual-endpoint conditional information and common randomized testing errors. Proposition 5 converts those errors through the NEW row contrast (3.17) and the exact survival probability into unconditional expected TV. Proposition 6 supplies all-K constants, the proper maximum with the accepted stationary-subclass lower, and both beta endpoints. Corollary 7 proves the bounded-hazard rate bridge using the inherited original-rule upper. Proposition 8 establishes the exact same-family limitation. Proposition 9 verifies all burns in the narrow remaining scalar window using the accepted algorithm-separated envelope. This accounts for every S012 contract export without using the diagnostic as evidence.

- **Exposed variables and constants:** finite K>=2,M>=1,beta in [0,1]; for the clock K>=13 and 0<beta<1 when conditioning on E. The construction parameters (1.3) and every initial phase are deterministic from public K,M. Constants 2^-16, 1/180, 1/(32sqrt(6)), 48 and 13 have the identified baseline/interface provenance; all new comparisons and factors 1/8, exp(-2), 1/16 are proved above. No hidden constant depends on K,M,beta,source,pi,mu or predictor. Theta/o(1) occur only on the exact scalar sequence (3.27), with numerical constants.
- **Modes:** all statistical risks are finite deterministic-horizon expected half-L1 TV at the actual same-trajectory endpoint. Conditional data laws are proof tools with the explicit unconditional conversion (3.20). No predictive-KL loss, squared-TV rate, independent query, random time, stopping horizon, high-probability claim or all-time guarantee is substituted.
- **Public-facing objects:** the class, risk, original estimator, (1.2), final bounds, and optionally the stronger finite-family parameters (1.3). The certificate quantities in (3.29) retain their inherited public meanings. Alphabets, Euler word, signs, base table, D_t,D, k,d, labeled tuples, reconstruction G, hazard coins/E and decoded tests are proof-local objects justified in named results, not extra algorithm inputs. The stationary pi is the original hidden existential witness; Lemma 2 constructs it rather than assuming its support.
- **Primitive versus generated:** (1.1) is a class hypothesis for arbitrary sources, but membership of the new family is a conclusion of Lemma 2. Closure/phase, all-remainder coverage, conditional product law, survival and contrast are conclusions, not theorem hypotheses. Conditioning on E is only local and has common positive probability where used. Beta-one cases do not condition on a probability-zero survival event.
- **Baselines:** beta zero preserves the accepted all-K MM5/L1MAX chain (3.24). Beta one retains the positive IID floor and pooled i upper rather than misreporting the zero absorbing bound as a rate. Small K is handled by an actual stationary IID subclass with full data. S010's positive-source result is preserved, not re-proved or relabeled false.
- **Algorithm comparison:** lower bounds allow the full randomized history kernel; upper (3.25) is for unchanged full-history add-one. Suffix/pool certificates in Proposition 9 belong to different algorithms. The constant predictor in Proposition 8 is only a witness-family upper. The single finite sign prior used for all tested coordinates and all endpoints is retained after conditioning on E,T, never after arbitrary full-history conditioning.
- **Remaining scope:** the full joint arbitrary-start minimax rate outside matched regimes is not solved. The concrete gap in Proposition 9 concerns available certificates, not a proven impossibility. No new route beyond this contracted construction, general-q problem, unknown-beta adaptation, positive-support redefinition, network implementation, resource or fault work is launched.


An inline producer sanity check additionally verified 5,766 integer phase/departure-index instances (m=3,...,20, M=1,...,2m-squared+2) and 4,131 finite scalar constant probes (K=2,...,300 with small, clock-boundary and large horizons). The phase checks were integer-exact; square-root constant probes used ordinary floating arithmetic. All passed. These checks are supplementary and do not replace any general proof or independent review.
