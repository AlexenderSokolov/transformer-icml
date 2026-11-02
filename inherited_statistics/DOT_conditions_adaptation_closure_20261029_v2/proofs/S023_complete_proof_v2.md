# S023 吸收结构与部分零返回族 完整科学证明 v2

编排说明（非原文）：本副本保留完整科学证明或完整科学审查推理；省略身份控制、私有位置、原提交状态、重复管理表及执行记录。原件未改，复制字节不改写。精确复制／删略／新增区间、原件全文身份见 COPY_MAP.json；原章节号及审查所引行号沿用原件，按同名章节与公式定位。SOURCES.md 给准确科学版本和可读闭包。有限检查仅为补充证据，不是形式验证；本次装配没有重做数学审查。

当前只接纳 S023 v2。完整 v1 审查指出 R1 字面时钟 K 域及 R2 广义推论缺失前提；有界 v2 复核已修复而不追认 v1。Theorem A 是任意初始律的原规则上界；Theorem B 是固定公开族、μ=δ_cc 的 tailored 共同预测器上界，不是原规则结论。完整失败审查和有界复核见 reviews/；修复中文说明见 CORRECTION_S023_AND_NEXT.md。

## 0. Useful results and limits

The full-class `M=K^5, beta=ln(K)/(2K^5)` gap remains open. The conjectural TARGET

`E[loss_original 1_H0] <= C[a+delta^(M+1)g+delta^(M/2)hstar]`

is not assumed. New local results are:

1. For **every absorbing witness** pi=delta_00, every complete history ending outside 00 forces all end-aligned pair labels to fail: `P(H0,Y_M!=00)=P(Y_M!=00)`. Accepted Euler and star joint informative masses are still delta^M and delta^H_M, not delta^r. Their conditional active masses under H0 are delta^(M-r) and delta^(H_M-r).
2. For the entire **first-zero-absorbing family**, all nonzero row laws arbitrary and unknown, and arbitrary initial mu, unchanged original full-history add-one has risk `<=min(1,48delta^M g+10i)`. Hence TARGET holds on this large non-product subclass for beta<=1/2, and its requested-ray risk is O(K^-1/2).
3. A new **genuinely partial-zero stochastic-return family** has a seven-state observable category chain, no disjoint cyclic phase schedule, and m² arbitrary unknown m-label rows. Its complete-history likelihood gives a tailored common predictor risk
   `<=delta min{p_M,14sqrt(p_M m^3/(M+1))}`,
   where p_M is the actual UV-terminal probability. This is O(K^-1) on the K^5 ray, uniformly in the public stochastic-delay and partial-zero parameters. It is not an original-add-one upper on this partial-zero family.

These do not rule out harder state-dependent recipes. The next uncovered mechanism is in §8.

## 1. Experiment and information

Integers K>=2,M>=1; one fixed legal homogeneous table theta, transitions `(a,b)->(b,c)` of probability theta_ab(c). Observe all `X_1,...,X_(M+2)`, put `Y_j=(X_(j+1),X_(j+2))`, and count departures 0,...,M-1. Target is the actual theta_(Y_M), and departure M is unobserved. Loss is unconditional expected half-L1 TV. All-state membership is `pi P=pi, P²(s,t)>=beta pi(t)` for all K² starts and destinations. Arbitrary mu may be singular to pi.

Original add-one is `p_s^+(c)=(C_s(c)+1)/(n_s+K)` at s=Y_M; no labels, table, pi or extra samples are its inputs. The tailored family predictor below uses only explicitly public geometry/beta/tau/eta and the observed history, never unknown rows. It is totalized on every history.

Write `delta=1-beta,n=M+1,r=floor(M/2),p=M-2r`, and
`g=min(1,sqrt(K^5/n)), a=min(1,sqrt(K^3/n)), i=min(1,sqrt(K/n)), hstar=min(1,sqrt(K^4/n))`.
Unless separately stated, 0<beta<1.

## 2. Exact absorbing residual and no-pair-success law

Assume theta_00=delta_0, pi=delta_00, and all-state minorization. S020's end-aligned split first generates p ordinary departures, then r two-step blocks, independently labeling each block a success with probability beta. Success endpoint is 00, failure endpoint has `Q2=(P²-beta Pi)/delta`. The unique midpoint from (a,b) to (c,d) is (b,c); both emitted symbols remain observed.

For every supported complete history h, its exact joint mass with no successful block is

`P(H0,H=h)=mu(y_0)[ordinary prefix] product_(j=0)^(r-1) [P²(y_(p+2j),y_(p+2j+2))-beta 1{y_(p+2j+2)=00}]`. (2.1)

The prefix is its single ordinary transition if p=1, and one otherwise. This multiplies delta Q2, not independent symbol-refresh events. Summing gives P(H0)=delta^r. On a positive-mass history,

`P(H0|H=h)=product_(blocks ending 00) [1-beta/P²(block start,00)]`. (2.2)

Zero-probability histories require no division. Since 00 is absorbing, Y_M!=00 implies no earlier pair is 00. Consequently for any complete-history event E contained in {Y_M!=00},

`P(H0,E)=P(E),   P(E|H0)=delta^(-r)P(E)`. (2.3)

This includes easy as well as informative endpoints. H0 can contain absorbed histories: Q2 can absorb. It is neither no absorption nor no symbol refresh.

**Construction-specific domain for §§2.1–2.3:** the literal accepted S012 Euler and S015 star geometries and initialized experiments are used only for K>=13, M>=1 and 0<beta<1. Here m=floor((K-1)/4)>=3; their periods are respectively m²>=9 and 2m>=6. The general identities (2.1)–(2.3) above still hold for every K>=2. Small-K IID patches in a risk-envelope theorem are not small-K versions of these constructions.

### 2.1 Accepted Euler: all residual rows

Use S012's exact active D, base Q and horizon-aligned mu. Every active base output is nonzero; theta_s=beta delta_0+delta Q_s on D, all other rows equal delta_0, and all ending-zero rows are inactive. From active s=(a,b), Q2 has:

- active endpoint (c,d): mass `delta Q_s(c)Q_(b,c)(d)`;
- easy endpoint (c,0), c!=0: mass `beta Q_s(c)`;
- endpoint 00: zero mass, since its original beta mass is subtracted.

The disjoint active/easy totals are delta and beta. Every inactive residual row is delta_00. Thus after the optional prefix, an active residual step survives with probability delta. The prefix survives with probability delta^p, and

`P(Y_M in D|H0)=delta^(r+p)=delta^(M-r)`.

In the accepted initialized experiment G is the full base event and terminal membership in D is terminal membership in UV. Thus `P(H0,G)=delta^M` and `P(G|H0)=delta^(M-r)`. Given G, its entire base-history product law is unchanged.

### 2.2 Accepted star: exact block probabilities, including off-support rows

Use S015's exact initialized phase, D and safe/vulnerable types. Safe outputs are zero, vulnerable base outputs nonzero; no two safe phases are consecutive. A vulnerable refresh enters a genuinely default row and absorbs on the next departure. An active two-step block is:

- **VV:** residual active mass delta, following the two-base-step law; residual easy ending-zero mass beta from refreshing its second departure; zero mass at 00.
- **VS or SV:** original active mass delta and original 00 mass beta; subtraction/division leave the two-base-step active law with total mass one.

For VV the first base symbol is nonzero, so the second-refresh endpoint is not 00 and has default target. The next phase type is determined independently of that symbol. SS cannot occur.

At any inactive/default start (a,b), its first output is zero and the full residual row is

`Q2((a,b),(0,d))=[theta_(b,0)(d)-beta 1{d=0}]/delta`.

If (b,0) is vulnerable active, this is its nonzero base law mapped to (0,d); otherwise it is delta_00. Arbitrary off-support residual starts can therefore reenter D. This is not possible along the initialized first-failure path and is not suppressed.

Let v_0 count vulnerable departures in the possible ordinary prefix; let v_j in {1,2} count them in block j. The exact S015 count is `H_M=v_0+sum_j v_j`. Conditional on H0, base survival is

`delta^v_0 product_j delta^(v_j-1)=delta^(H_M-r)`.

Hence `P(H0,G)=delta^H_M` and `P(G|H0)=delta^(H_M-r)`. Every block contains a vulnerable departure, so this is <=1. Safe symbol-refresh coins change nothing, so G is not “no symbol refresh.” Given G, the complete S015 product experiment is retained; no analogous assertion is made on the larger H0 event.

### 2.3 What the requested ray actually diagnoses

For S012 at M=K^5, beta=ln K/(2K^5), `P(G|H0)=delta^(M-r)=Theta(K^-1/4)`, so its informative joint mass is Theta(K^-1/2). For S015, its exact accepted count satisfies `H_M=M/2+M/(2m)+e_M`, `|e_M|<=2m`, `m=floor((K-1)/4)`. Hence `beta(H_M-r)=O(ln K/K)->0` and `P(G|H0)->1`. The star does **not** acquire a further K^-1/4 survival penalty on H0; its smaller statistical information scale is essential. The accepted star conditional estimation scale is Theta(K^-1/2) on this ray, giving its restricted total risk Theta(K^-3/4). These facts rule out a universal assertion that H0 becomes easy just because its residual usually absorbs; the actual tradeoff must include statistical complexity as well as absorption.

## 3. Full state-dependent recipe: exact residual and true stationary law

Choose t_b in [beta,1] for nonzero b, t_0=1, and arbitrary probability vectors r_ab supported on nonzero symbols for every non-00 pair. Set

`h_(a,0)=t_a, h_(a,b)=beta/t_b (b!=0)`,
`theta_ab=h_ab delta_0+(1-h_ab)r_ab`, and theta_00=delta_0.

Every row normalizes and is a legal shift. Unique two-step paths give P²((a,b),00)=beta for b!=0 and t_a>=beta for b=0. Thus pi=delta_00 is stationary and witnesses all-state membership. It is **unique**: a stationary nu would satisfy `nu(00^c)<=delta nu(00^c)` by two-step absorption, forcing nu(00^c)=0.

For b!=0 write u_b=beta/t_b. The complete residual is

- `Q2((a,b),00)=0`;
- `Q2((a,b),(0,d))=u_b(1-t_b)r_(b,0)(d)/delta`, d!=0;
- `Q2((a,b),(c,d))=(1-u_b)r_ab(c)theta_(b,c)(d)/delta`, c!=0, any d.

For a!=0,b=0 it is

- `Q2((a,0),00)=(t_a-beta)/delta`;
- `Q2((a,0),(c,d))=(1-t_a)r_(a,0)(c)theta_(0,c)(d)/delta`, c!=0, any d;
- zero at other endpoints.

Finally Q2(00,00)=1. These formulas follow directly from the product path and sum to one. Partial-zero returns are therefore not free beta-refresh-safe memory: residual killing at (a,0) is (t_a-beta)/delta, and the preceding nonzero row pays hazard beta/t_a. At t_a=beta those preceding rows output zero surely; at t_a=1 the ending-zero row absorbs. This tradeoff alone does not prove TARGET.

## 4. Theorem A: original-rule bridge for arbitrary first-zero-absorbing rows

For every K>=2,M>=1,0<beta<1, take arbitrary unknown nonzero-supported probability vectors r_ab whenever b!=0, and define **all** rows by

`theta_ab=beta delta_0+delta r_ab` for b!=0; `theta_a0=delta_0` for all a.

Allow every mu. This is §3 with every nonzero t_b=1, so membership and unique stationarity are proved. There is no clock, phase, endpoint-uniformity or product-experiment restriction. Then

`sup_(r,mu) E loss_original <= min{1,48delta^M g+10i}`. (4.1)

For beta<=1/2 it follows that

`E[loss_original 1_H0] <=96delta^(M+1)g+10a`. (4.2)

### Proof: entire base experiment, not conditional row stacks

First condition mu on its second coordinate being nonzero; its first coordinate may be zero. Before the first zero output use independent beta coins. The event G of no zero among the M observed outputs has probability delta^M. Given G, the **entire** history is exactly that of a fixed ordinary legal base source R with rows r_ab for b!=0 and delta_0 for b=0, under the same conditional mu. Only independent coins were constrained. Initial symbols, including any initial zero, are retained.

L1MAX's accepted unconditional general-source theorem applies to this full base experiment and the same K-symbol original add-one: expected TV to its base terminal row is <=min(1,48g). The actual terminal target is beta delta_0+delta times that row, at TV distance beta. Thus G contributes at most

`delta^M min(1,48g)+beta delta^M`. (4.3)

This is not an application of a general theorem to Q2 or generic H0-conditioned data.

### Proof: exact absorption-time loss and all final-step cases

Let T be the zero-based first-zero departure index. For 0<=t<M, P(T=t)=beta delta^t, independent of unknown rows. Before this departure no pair ends in zero. If t=M-1, the terminal pair is (b,0) with b!=0, has zero past departures, and original loss to delta_0 is (K-1)/K. If t<=M-2, terminal pair is 00, with exactly M-t-2 observed departures, all zero. Hence the exact failure contribution is

`B_M=(K-1)beta delta^(M-1)/K + sum_(t=0)^(M-2) beta delta^t (K-1)/(M-t-2+K)`. (4.4)

Every history, including final-departure absorption and terminal count zero, is included. Each displayed conditional loss is <=min(1,K/(M-t)). For all t>=0, `beta(1-beta)^t<=1/(t+1)`: maximize at beta=1/(t+1) for t>0; t=0 is trivial. Split the failure sum at t=M/2. Early t contribute at most `min(1,2K/M)<=2sqrt(K/M)`. Each late atom is <=2/M. With u=M-t, `min(1,K/u)<=sqrt(K/u)` and `sum_(u=1)^M u^(-1/2)<=2sqrt(M)` give late contribution <=4sqrt(K/M). Therefore

`B_M<=min(1,6sqrt(K/M))<=9i`. (4.5)

Here `(M+1)/M<=2`, and the i cap covers i=1. Also beta delta^M<=1/M, which is <=sqrt(K/(M+1)) for K>=2,M>=1; the cap case is trivial. Thus beta delta^M<=i. Combine (4.3)-(4.5).

If the initial second coordinate is zero, no unknown row is visited. Starting at 00 gives count M and loss (K-1)/(M+K); starting at (a,0),a!=0, gives count M-1 and loss (K-1)/(M-1+K). Both are <=min(1,K/M)<=2i. Convexity over initial-law cases proves arbitrary mu. Finally use loss>=0, i<=a and delta^M<=2delta^(M+1) when beta<=1/2 for (4.2). The predictor never receives T or G. ∎

At the requested ray, delta^M<=K^-1/2, g<=1 and i<=K^-2, giving `48K^-1/2+10K^-2`. At beta=0 the direct base argument gives inherited min(1,48g); at beta=1 every row is delta_0 and the direct deterministic-count calculation applies. These family endpoints do not replace full-class IID/minimax endpoints.

## 5. A lawful genuinely partial-zero stochastic-return family

### 5.1 All rows, all parameters, initial law and membership

Take integers m>=1,K>=3m+2. Choose distinct public symbols 0,c and pairwise disjoint public sets U,V,W of size m, disjoint from 0,c. Extra symbols are permitted. Fix public `0<beta<1, tau in [beta,1], eta in [0,1]`. Put `t_c=tau`, `t_b=1` for every other nonzero symbol, `t_0=1`, and use §3's hazards. Write u=beta/tau, v=(1-u)eta. For each unknown context (a,b) in U×V choose an arbitrary probability p_ab on W. The following specifies **every** nonzero component r_ab:

- b=c, any a: `(1-eta)delta_c+eta Unif(U)`;
- b in U, any a: Unif(V);
- b in V,a in U: p_ab;
- b in V,a outside U: Unif(W);
- b in W or an unused nonzero symbol, any a: delta_c;
- b=0,a!=0: delta_c.

Set theta_ab by §3 and theta_00=delta_0. These categories are disjoint and exhaustive. In particular theta_(c,0)=tau delta_0+(1-tau)delta_c; all other ending-zero rows are delta_0. Initialize `mu=delta_(c,c)`, common across every unknown row law and every horizon.

All rows are normalized legal shifts; §3 gives all-state P²>=beta Pi and the true unique stationary law pi=delta_00. When beta<tau<1, the clock's ending-zero row genuinely returns after a zero with positive probability, and its preceding c-ending rows have hazard u>beta. When also 0<eta<1 and tau>beta, the cc state has a positive self-loop and also exits to different actual pairs. Thus it cannot belong to a disjoint deterministic cyclic phase scheme with L>1; L=1 does not satisfy S021's zero/nonzero output dichotomy. This is genuinely outside the accepted template, not a changed period.

### 5.2 Exact public category chain

On the specified initialized support, define categories of the actual pair:

`C={cc,0c} union (W×{c}), Z={c0}, Uc={c}×U, Vc=U×V, Wc=V×W, E=(U union V union W)×{0}, A={00}`.

The seven categories are disjoint and encompass every reachable pair. They are deterministic functions of observed symbols, not latent labels. Call their process Z_j and its transition matrix A_cat. In row order C,Z,Uc,Vc,Wc,E,A its only nonzero transitions are

| from | to and probability |
|---|---|
| C | C: (1-u)(1-eta); Z: u; Uc: v=(1-u)eta |
| Z | C: 1-tau; A: tau |
| Uc | Vc: delta; E: beta |
| Vc | Wc: delta; E: beta |
| Wc | C: delta; E: beta |
| E | A: 1 |
| A | A: 1 |

The current category determines all transition probabilities irrespective of individual symbols or unknown p_ab. Thus this is an exact homogeneous seven-state Markov chain started at C, with all zeros and parameter boundaries allowed. No independence of category and symbol histories is asserted without the factorization below.

Put `E_M={Y_M in U×V}={Z_M=Vc}` and

`p_M=e_C A_cat^M e_Vc`. (5.1)

This is the *actual* terminal probability, not a random-time surrogate. For M>=2, the only predecessors of Vc and Uc give the exact identity

`p_M=delta v P(Z_(M-2)=C)<=delta(1-beta/tau)eta`. (5.2)

For M=1 it is zero. In particular eta<=K^-2 gives p_M<=K^-2. Stochastic mean-delay tuning does not preserve horizon alignment for free.

### 5.3 Complete observed-history likelihood, including failures

For any supported history h, extract its category trace z=(z_0,...,z_M). Its public weight is `w(z)=product_(j=0)^(M-1) A_cat(z_j,z_(j+1))`. At each C→Uc transition one observed U symbol is drawn uniformly; at each Uc→Vc transition one V symbol is drawn uniformly; each Vc→Wc transition draws one W symbol with law p_uv at the actual current UV context. Every other output is deterministic given the category transition. Therefore the **entire original** history likelihood is

`P_p(H=h)=w(z) m^[-N_(C,Uc)(z)-N_(Uc,Vc)(z)] product_(j: z_j=Vc,z_(j+1)=Wc) p_(Y_j)(X_(j+3))`. (5.3)

This includes all initial symbols (cc, deterministic), every emitted label once, partial final contexts, and every absorption/failure history. The same W symbol appearing in two overlapping pairs contributes one factor, not two. Reconstruction from the trace and the listed draw values appends each symbol in order and recovers all of h. Conversely extraction recovers every draw, so no side information is discarded. The trace has probability w(z): summing over each normalized draw in generation order proves this, even with zeros in p. In particular its law is independent of unknown rows. The trace cannot secretly encode unknown label values because it retains only the fixed disjoint symbol categories, and all future category transitions are independent of these values.

On E_M, every earlier Vc departure is Vc→Wc: a Vc→E failure would enter A and could never return. Let `Q=sum_(j=0)^(M-1)1{Z_j=Vc}`. Conditional on a trace z ending Vc, Q=q, there are exactly q complete context/label triples and a final actual UV context T. Formula (5.3) simplifies exactly to

`P_p(H=h | Z_0^M=z)=m^[-2(q+1)] product_(l=1)^q p_(S_l)(W_l)`. (5.4)

Thus the triples are IID, their contexts uniform on U×V, and actual T is uniform and independent of them. This is established only in this specified family, by its complete likelihood. Let N_s count observed departures from s. For every s in U×V and 0<=k<=q,

`P(E_M,Q=q,T=s,N_s=k)=P(Z_M=Vc,Q=q) m^-2 Bin(q,1/m²){k}`. (5.5)

In particular `P(E_M,T=s)=p_M/m²`; conditional on z,T=s, its selected W labels are IID from p_s. Equations (5.1),(5.5) give the actual-endpoint/unknown-row-visit joint, not an independent query added to the experiment. Since E_M implies Y_M!=00, §2 further gives `P(H0,E_M,Q=q,T=s,N_s=k)` equal to the same expression; conditioning on H0 divides by delta^r. None of this says no zero symbols were seen: c→0→c returns remain possible.

### 5.4 Neighboring likelihood and changed target, with no omitted failure data

For a paired-sign specialization `p_s(w_(2j-1))=(1+alpha sigma_(s,j))/m`, `p_s(w_(2j))=(1-alpha sigma_(s,j))/m`, 0<alpha<=1/2 (odd leftover 1/m), (5.3) shows the complete likelihood ratio between neighboring signs is the product of their ratios at **all** Vc→Wc observed departures, including ones before a later failure. No failure history is asserted uninformative.
More explicitly, let L_W count **all** observed Vc→Wc transitions, on absorbed and unabsorbed histories alike. Conditioning on any public category trace gives one uniform independent context for each such label, so the unconditional complete-history neighboring KL is exactly `E[L_W](2alpha/m³)log((1+alpha)/(1-alpha))`. Its expectation is computed under the common category law and is sign-independent. Orphan final contexts are observed but have the same uniform law under both neighbors.

Conditional on z ending Vc and T=s, neighbors differing at any one row/bit have exact KL

`q (2alpha/m³) log((1+alpha)/(1-alpha)) <=8q alpha²/m³`. (5.6)

The trace is itself observed and has the same law under both signs. Therefore, if p_M>0, the full law conditional on E_M,T=s has the same expression with q replaced by `E[Q|E_M]`; this follows by summing the conditional KL over the common trace law, not by discarding it. No assertion that this expectation is small is made.

The actual unknown target is `theta_s=beta delta_0+delta p_s`, so each changed paired coordinate contrast is `2delta alpha sigma/m`. A wrongly decoded bit costs at least delta alpha/m in half-L1. The target is not the base p_s. These formulas identify exactly what a legitimate lower test would have to pay; the upper below instead shows this whole family is too easy.

## 6. Theorem B: all-delay finite risk obstruction for that family

For every parameter choice in §5 and all M>=1, there is one observable predictor, common across **all arbitrary** unknown p_ab, with

`sup_p E TV(A(H),theta_(Y_M)) <= delta min{p_M,14sqrt(p_M m³/(M+1))}`. (6.1)

No prior, shrinking amplitude, deterministic period, or horizon alignment is needed. The geometry and beta,tau,eta are public within this restricted experiment; unknown mixtures of such public families are outside the theorem.

### Predictor and conditional risk

Outside U×V, output the exact public row of §5 (which need not equal delta_0). At an actual UV endpoint, if the full history is outside the public category reconstruction support, output delta_0. Otherwise use its full observed UV-row label counts: empirical W-law if N_s>0, Unif(W) if N_s=0, and output beta delta_0+delta times that law. This gives a normalized common kernel on all histories; no latent event or unknown-source support is queried.

For any W-law on m symbols and n>=1 IID labels, coordinate variance and Cauchy-Schwarz give empirical expected TV <=(1/2)sqrt(m/n)<=sqrt(m/(n+1)). At n=0 the default loss <=1<=sqrt(m/(n+1)). Given z,T=s, (5.5) gives N_s~Bin(q,1/m²), and

`E[1/(N_s+1)]=[1-(1-1/m²)^(q+1)]m²/(q+1)<=m²/(q+1)`.

The binomial identity includes q=0 and m=1. Hence its conditional risk is at most `delta min(1,sqrt(m³/(q+1)))`. Outside E_M the predictor is exact, regardless of information already present in the failure history. Thus

`risk <=delta E[1_E_M min(1,sqrt(m³/(Q+1)))]`. (6.2)

### Actual-terminal category occupation, without conditioning on a label path

Apply S020 Lemma 1 to the homogeneous **seven-state category chain**, not the K² pair chain. For completeness, if b_t(y)=P_y(J_t<w) and B_t=max_y b_t(y), suffix count inclusion gives B_t<=B_l for l<=t. On any path, fewer-than-w previous visits can flag each of seven states at most w times. Summing expectations over seven starts gives `sum_(t=0)^M B_t<=49w`; monotonicity gives `P(J_M<w)<=min(1,49w/(M+1))`. This permits reducibility, zero transitions and any category start. It does not presume stationary initialization.

On E_M the terminal category is Vc and J_M=Q. Consequently

`P(E_M,Q<w)<=min(p_M,49w/(M+1))` for integer w>=1. (6.3)

Let B=m³, c=49/(M+1). For 0<t<1, the strict event `min(1,sqrt(B/(Q+1)))>t` is `{Q<ceil(B/t²)-1}`. If its integer threshold is positive it is <=B/t²; otherwise the event is empty. Thus its joint mass with E_M is at most `min(p_M,cB/t²)`. Integration yields

`E[1_E_M min(1,sqrt(B/(Q+1)))] <= integral_0^1 min(p_M,cB/t²)dt <=min(p_M,2sqrt(p_M cB))`.

For p_M=0 the expectation is zero; otherwise split at sqrt(cB/p_M) when this is below one, obtaining `2sqrt(p_M cB)-cB`; when it is >=1 the integral is p_M. Substitute into (6.2) to prove (6.1). This count is the actual same-trajectory terminal category, not a randomly selected time or an auxiliary test endpoint. ∎

Since p_M<=1 and m<=K, the requested ray gives risk <=14K^-1. For M>=K^5 the exact finite bound is <=14delta sqrt(m³/(M+1)), with its displayed probability cap. The basic absorption inequality also yields p_M<=delta^floor(M/2), but no such extra estimate is needed for this obstruction. This result is a restricted-family upper, not a full-class or original-rule upper.

## 7. Verification, domains and preserved failures

The author-owned `structural_survival_check_v1.py` was executed with exact `Fraction` arithmetic for kernel, history, likelihood and joint-law comparisons. Saved `structural_survival_check_v1.json` reports PASS, with:

- 3,437 all-row membership/residual normalization checks;
- 18 accepted Euler/star experiments (M=1,...,9), 2,271 complete histories, and 495 exact active-block survival checks;
- 273 first-zero experiments for K=2,3, three beta values, M=1,...,7, and every point initial pair, with 9,333 complete histories; exact near-terminal absorption smoothing sums and H0 laws were checked;
- 64 partial-zero experiments for m=1,2, M=1,...,8, and interior/degenerate tau/eta choices, with 4,515 complete histories and 80 exact endpoint/visit-binomial joint atoms. Full histories, public trace likelihoods, true terminal probabilities, and H0 identity were compared exactly.

Only comparisons to displayed square-root numerical risk bounds use floating arithmetic with 1e-12 tolerance. Finite tests corroborate the symbolic proofs; they are not independent review, an infinite-domain proof, or formal verification. The source proofs/reviews and gates are read as exact predecessors, not re-certified wholesale.

Finite scope: the general absorbing identities in §2 and §§3–4 use every K>=2,M>=1,0<beta<1. The literal S012/S015 construction-specific statements in §§2.1–2.3 retain their inherited K>=13,M>=1,0<beta<1 domains and exact horizon-aligned initial laws; no small-K clock construction is asserted. The TARGET corollary in §4 additionally requires beta<=1/2. Both M parities, r=0, terminal count zero, arbitrary mu in Theorem A, and zero row probabilities are explicit. Theorem B uses K>=3m+2,m>=1,mu=delta_cc,0<beta<1,tau in [beta,1],eta in [0,1]; it does **not** claim arbitrary initialization or unknown public geometry. Its exact factorization includes m=1, although paired-sign testing is meaningful only at m>=2. Endpoint beta=0,1 remarks in Theorem A are direct separate arguments, not a residual-kernel extension. No N2 moderate-log result is extrapolated.

Preserved failed or rejected inferences:

1. H0 is not no symbol refresh, no zero output, or no absorption. Equations (2.1)-(2.3) and the exact VV/VS/SV split replace that mistake.
2. Star H0 paths are not usually easy on the K^5 ray: their active conditional probability tends to one. Only Euler gets the extra conditional survival power; see §2.3.
3. A geometric waiting time of order K² cannot be substituted for a horizon-aligned deterministic clock while retaining an O(1) endpoint probability. Equation (5.2) gives the actual dilution, and Theorem B proves a stronger all-delay statistical obstruction.
4. Conditional iid rows are **not** claimed after generic residual or stopping-count conditioning. Theorem A conditions only independent symbol coins to obtain an entire ordinary base source. Theorem B first proves its full public trace likelihood and only then uses its exact product experiment.
5. Absorbed/failure histories are not discarded as “uninformative.” Their original-rule smoothing is paid exactly in (4.4); their unknown-label likelihood remains in (5.3) and the full-history KL. The tailored predictor's zero loss outside UV arises because those target rows are public, not because their data contain no information.
6. A raw K³ residual occupation coefficient, or a full-class TARGET conclusion, does not follow from either subclass. Seven-state lumping works only because the stated category process has a genuine source-independent homogeneous Markov law and the complete product bridge is proved.

## 8. Remaining obstruction and next necessary step

The broad t_b=1 boundary is now controlled for original add-one without a product-clock assumption. The simple escape into a genuine partial-zero geometric-return clock is also controlled, but only for its public-family predictor. Neither establishes TARGET for general intermediate t_b or for general stationary pi.

**Explicitly restricted d-category scope consequence.** Retain §5's original legal all-row D2(beta) experiment and fixed-public-family information contract, with integers m>=1,K>=3m+2,M>=1, 0<beta<1, the same common public initialization mu=delta_cc, and no hidden row laws or latent labels supplied to the predictor. A d-category extension (integer d>=1) is covered only if it additionally retains **all** of the following premises:

1. There is a public map from the actual pair to d categories. Under the common initialization its process is a homogeneous d-state Markov chain with transition probabilities and initial category law independent of the unknown row laws. Its whole observed trace is a deterministic function of the original complete symbol history. The query category is exactly a common public set S of m² actual pair states; write E for the event that the actual Y_M belongs to S and p=P(E), common across hidden rows.
2. There is a common public set W of m nonzero label symbols. For every s in S the actual target row is **exactly** `theta_s=beta delta_0+delta p_s`, where p_s is the same unknown probability on W that generates the product labels below. No different target law or target scaling is permitted.
3. Conditional on every positive-probability public category trace ending in the query category, the **entire** observed symbol history has a public invertible reconstruction from q IID labeled pairs `(S_l,W_l)`, with S_l uniform on S and W_l conditionally distributed as p_(S_l), plus the actual endpoint T=Y_M, uniform on S and independent of those q pairs. No remaining observed initial/return/failure information is discarded by that reconstruction. Each `(S_l,W_l)` is precisely an earlier actual query pair and its observed next symbol, in departure order; no fictitious training sample is introduced. The integer q is exactly the number of earlier observed departures from the actual query category, so on E it equals the terminal category's previous-visit count.
4. All actual target rows outside S are public, independent of the hidden p_s, and are output exactly there. The initialization is the stated common mu=delta_cc, not a source-dependent law or an asserted arbitrary-initialization extension.
5. The same observable completion as §6 is available: at a query endpoint on the public reconstruction support use the empirical W-law of its observed labels, or Unif(W) at zero count, mixed as `beta delta_0+delta qhat_s`; on a query-endpoint history outside that public support use delta_0. The support guard does not depend on hidden row probabilities. Thus this is one normalized common predictor on all complete histories, without extra observations or hidden advice.

Under precisely these retained premises, the written proof gives `delta min(p,2d sqrt(p m³/(M+1)))`: m² equiprobable contexts times m labels supply m³, the displayed actual target relation supplies delta, and only the category occupation coefficient changes from 49 to d². This preserves the valid conditional corollary; it is not a claim that arbitrary stochastic returns satisfy these hypotheses, nor a new construction or theorem expansion.

Thus the next useful lower candidate must break at least one of those actual conditions, not merely alter eta, tau, the delay mean, or the shrinking cube amplitude. The most concrete remaining recipe-level mechanism is a partial-zero return system with **growing actual clock complexity and label-dependent return law**, so the actual endpoint/visit process no longer collapses to a constant-state public Markov category chain and its observed return histories can depend on unknown labels. The next bounded question should require:

- all K² rows using the §3 hazard recipe and an explicit common initialization;
- a proved complete-history likelihood, including how return paths reveal signs;
- the actual endpoint joint with unknown-row departures, not a standalone long-survival probability;
- the new-target contrast 1-h_s, and no assumed product law after survival;
- either a legitimate lower larger than K^-1/2 on the requested ray, or an observable-predictor/weighted-original-loss obstruction for that specified larger family.

On the upper side, the exact unresolved bridge is to turn the reciprocal pair of hazards beta/t_b and t_b into a **weighted original-row loss/count inequality** without assuming those public lumping/product properties. A generic K²-state residual count bound still discards this information. Theorem A cannot be extended to t_b<1 by conditioning on “no zero,” because legal nonabsorbing zero-return histories would be deleted and their likelihood and endpoints would change. Theorem B cannot be promoted to original add-one by substituting its known outside-target rows for original empirical rows.

No counterexample to TARGET was found in the proved families. That is not evidence of global truth and not a scientific closure of the full D2 problem. re-running fixed product clocks or the same geometric-delay family would add no necessary frontier.
