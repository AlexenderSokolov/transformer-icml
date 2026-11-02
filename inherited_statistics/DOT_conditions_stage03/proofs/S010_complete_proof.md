# S010 正源平滑时钟下界

编排说明（非原文）：以下逐字保留原已接纳版本的完整数学论证、必要定义、范围与科学解释，仅省略身份、内部控制和来源元数据。原有数学编号及 Euler clock 名称不变。新增标题与本说明不是原证明。依赖闭包与源哈希见 ../SOURCES.md，精确字节映射见 ../COPY_MAP.json。本次编排不是重新证明或对复制件的新数学审查。

编排时序注（非原文）：S010 的正源见证与结论保持有效。其末尾举例中未闭合的 M=K⁴、β=K⁻⁶ 窗口，已由后出的 S012 在完整源类闭合；这不修改 S010 原文的历史范围。

### Result

For every integer `K>=12`, `M>=1`, and public `0<beta<=K^-4`, let

\[
 n=M+1,\qquad g=\min\{1,\sqrt{K^5/n}\},\qquad
 \varepsilon=8\sqrt\beta,\qquad m=\lfloor K/4\rfloor,\quad L=m^2,
\]
\[
 q=\lfloor M/L\rfloor,\qquad
 \alpha=\min\left\{\frac12,\frac18\sqrt{\frac{m^3}{q+1}}\right\}.
\]
In the exact full-history, actual-terminal-row experiment defined below,

\[
\boxed{
 R_{D2}(K,M,\beta)
 \ \ge\ (1-\varepsilon)^n\frac\alpha8
 \ \ge\ 2^{-16}(1-8\sqrt\beta)^n g.}
\tag{S010}
\]

If additionally `n sqrt(beta)<=2`, then the unchanged original full-history add-one rule satisfies the matching-rate chain

\[
 2^{-16}e^{-32}g
 \le R_{D2}(K,M,\beta)
 \le R_{D2}^{+}(K,M,\beta)
 \le\min\{1,48\sqrt{K^5/n}\}.
\tag{C}
\]
The upper is the inherited L1MAX interface, not a new upper theorem. The lower is newly proved for a uniformly smoothed version of the inherited MM5 family, with the complete observation experiment and the **new smoothed target** kept throughout.

## 1. Exact setting, assumptions, and notation

The original setting files have no stable assumption IDs. The following local labels merely refer to their explicit primitive conditions, without changing them.

- **A1 (legal fixed source):** `A={0,...,K-1}`; a source is a fixed homogeneous table `theta=(theta_ab(c))`, each row a probability on A. Its pair kernel has `P_theta((a,b),(b,c))=theta_ab(c)` and all non-shift entries zero. The initial pair law `mu` may be arbitrary.
- **A2 (observation and loss):** `Y_i=(X_(i+1),X_(i+2))`, `0<=i<=M`. The full data are `H=X_1,...,X_(M+2)`, including the initial pair and the actual terminal pair `Y_M`. The unobserved next symbol is `X_(M+3)`. Loss is `TV(A(H),theta_(Y_M))`, with `TV(p,r)=||p-r||_1/2`; risk is its expectation over the source and algorithm randomization.
- **A3 (common information):** the predictor is one history-to-simplex probability kernel for the whole source class. It may depend on public `K,M,beta`, and may use a source-independent random seed. It does not see `theta,mu,pi`, latent smoothing coins, sign parameters, or the future.
- **A4 (class):** `(theta,mu)` belongs to `D_K(2,beta)` if there exists a stationary probability row `pi` for `P_theta` such that `P_theta^2(s,t)>=beta pi(t)` for **every** pair `s,t` in `A^2`. No stationary initialization is required. Beta is a public lower bound, not an oracle for the maximal coefficient.

Here `R_D2` is the infimum, over the common predictors in A3, of the supremum of A2 risk over A4. `R_D2^+` is the separate supremum for the original rule

\[
 C_{s,c}=\sum_{i=0}^{M-1}{\bf1}\{Y_i=s,X_{i+3}=c\},\quad
 n_s=\sum_c C_{s,c},\quad p_s^+(c)=\frac{C_{s,c}+1}{n_s+K},
\]
used at `s=Y_M` with all M observed departures. The symbol `n_s` is a row count, distinct from `n=M+1`.

**Notation and provenance.** The public-facing parameters `n,g,epsilon,m,L,q,alpha` are the displayed deterministic functions of `K,M,beta`; `n,g,epsilon` and the bound in (S010) are the primary exported interface. `m,L,q,alpha` also parameterize the optional stronger finite-family bound. The proof-local alphabets, Euler word, phase sets, sign family, initial law, full-history encoding, kernels `P_0,R,B`, pair-uniform row `U_pair`, invariant law `pi_epsilon`, coin event E, and tests are constructed and justified below, not primitive assumptions. All constants are explicit. In particular `33` and `64` arise in the membership calculation, `3/8` from testing, and `48` solely from L1MAX. The proof uses no unproved recurrence or invariant hypothesis.

## 2. Allowed source interfaces and attribution

1. **MM5** is accepted. Its readable proof Sections 2–8 supply the original four-alphabet Euler construction, six initial-phase cases, complete-history bijection, finite binary testing and constants. We reuse this machinery with attribution, explicitly restating and checking it for the loop-rotated word and changed target below. The black-box MM5 risk inequality is **not** used to obtain a multiplicative smoothed-target lower. At beta zero alone we inherit its accepted all-`K>=2,M>=1` conclusion `2^-16 min(1,sqrt(K^5/(M+1)))`.
2. **L1MAX** supplies exactly L1+: for every `K>=2,M>=1`, legal fixed theta and arbitrary mu, the original complete-history add-one risk is at most `min(1,48 sqrt(K^5/(M+1)))`. Its definitions coincide with A1–A3, and A4 only restricts that full source class, so its upper applies here. No neural implementation, precision, fault or cost conclusion is imported.

The novel obligations are the stronger loop rotation and all-start occupation control, the explicit normalized invariant-law construction and atom bound, the all-pair public-beta minorization, and the latent-event testing argument against the new target. No S001–S009 proof is redone or needed for the new derivation. The MM5 source's obsolete concluding upper-gap remark is not a premise.

## 3. Local lemma map


| Unit | Type and paper-ready label | Exact contribution |
|---|---|---|
| unit_001 | Lemma, lawful rotated clock (`lem:rotated-clock`) | Legal full table, public Euler word with p5=(0,0), phase transition invariant |
| unit_002 | Invariant, all-start one-visit (`inv:one-visit`) | Entry within two steps, distinct transient states, at most one visit per L-state block |
| unit_003 | Lemma, complete base experiment (`lem:full-experiment`) | All-remainder mu, full observed-history bijection, q iid training triples and actual terminal law |
| unit_004 | Lemma, exact invariant law (`lem:invariant-law`) | Normalized nonnegative B series, uniqueness, P-invariance and stationary resolvent |
| unit_005 | Lemma, atom and minorization (`lem:membership`) | pi_max<=1/L+epsilon; every-state D_K(2,beta) membership |
| unit_006 | Lemma, full conditional testing (`lem:conditional-testing`) | Neighboring full-history conditional TV<=1/4 and randomized bit error>=3/8 |
| unit_007 | Proposition, smoothed actual-target lower (`prop:smoothed-loss`) | Latent no-noise event, new target contrast, finite-prior risk >=(1-epsilon)^n alpha/8 |
| unit_008 | Proposition, capped rate and corollary (`prop:capped-rate`) | Explicit finite constants, bounded-survival matching and beta-zero boundary |

The assumptions of each unit are stated before its proof. Later uses of these local results refer to their titles/labels; no diagnostic claim is a proof input.

## 4. Local derivation

### unit_001: lemma — Lawful rotated clock (`lem:rotated-clock`)

**Statement.** Under A1 and integers `K>=12,M>=1`, with the public `m,L,alpha` above, there exists the following finite sign family of legal homogeneous tables `theta^{sigma,0}` on all K letters. Its closed phase sets are disjoint, and every permitted transition within them advances the phase by one modulo L. The Euler word can be chosen with `p_5=(0,0)` without adding any state or time information.

**Proof.** Take the disjoint groups

\[
 \mathcal C=\{0,\ldots,m-1\},\quad
 \mathcal U=\{m,\ldots,2m-1\},\quad
 \mathcal V=\{2m,\ldots,3m-1\},\quad
 \mathcal W=\{3m,\ldots,4m-1\},
\]
and enumerate `W` publicly as `w_1,...,w_m`. Let `b=floor(m/2)` and let `sigma` range over all signs indexed by `(s,j)` in `(U x V) x {1,...,b}`.

For completeness, the Euler word used by MM5 exists by a finite construction. On C put every directed edge, including loops. Each vertex has m incoming and m outgoing edges. A maximal unused-edge walk started at a vertex ends at that vertex: at a different endpoint its used incoming degree would exceed its used outgoing degree by one, leaving an unused outgoing edge by balance. Thus it is a closed walk. After removing it the unused graph is balanced. If any edge remains, a vertex of the current walk has an unused outgoing edge; otherwise, since the original graph is complete, all vertices and their outgoing edges would already have been exhausted. Starting there makes another closed unused-edge walk; splice it in and repeat. Each repetition uses at least one more edge, so this terminates in a circuit using every edge once. Reading consecutive vertices gives a periodic word `c_0,...,c_(L-1)` with period L, whose pairs `p_t=(c_t,c_(t+1))` enumerate `C^2` exactly once.

The loop `0->0` is an edge of the circuit. Rotate the word so that this edge is `p_5`; hence `c_5=c_6=0`. Fix one such rotated word for each m, independently of sigma and all data. This strengthens MM5's `c_5=0` requirement, with no change of its path structure. As `L>=9`, the indices `0,1,...,6` here do not wrap into one another, and `p_0,p_5,...,p_(L-1)` are distinct.

For every `s in U x V`, define a probability row `q_sigma(.|s)` by

\[
 q_\sigma(w_{2j-1}\mid s)=\frac{1+\alpha\sigma_{s,j}}m,
 \qquad q_\sigma(w_{2j}\mid s)=\frac{1-\alpha\sigma_{s,j}}m,
 \quad 1\le j\le b.
\tag{4.1}
\]
If m is odd the remaining coordinate `w_m` has mass `1/m`; all coordinates outside W have mass zero. Each paired sum is `2/m`, so the total is one; all W masses are at least `1/(2m)`.

Assign **every** row as follows, with periodic c-indices:

| Pair row | Successor-symbol law `theta^{sigma,0}` |
|---|---|
| `p_0` | `Unif(U)` |
| `(c_1,u)`, `u in U` | `Unif(V)` |
| `(u,v)`, `u in U, v in V` | `q_sigma(.|u,v)` |
| `(v,w)`, `v in V, w in W` | `delta_0` |
| `(w,0)`, `w in W` | `delta_(c_6)=delta_0` |
| `p_t`, `5<=t<L` | `delta_(c_(t+2))` |
| **Every remaining pair**, including `p_1,...,p_4` and pairs with unused letters | `delta_0` |

The categories are disjoint: the non-clock categories have different ordered alphabet types, and the clock pairs are all distinct. Every assigned row is normalized. The table uses only its current pair, not its phase label, time, history, or sign resampling. Each output is appended by the legal shift `(a,a')->(a',c)`. Let `P_0=P_{theta^{sigma,0}}`; the dependence on sigma remains fixed along a trajectory.

Define disjoint sets

\[
 \mathcal D_0=\{p_0\},\quad \mathcal D_1=\{c_1\}\times\mathcal U,
 \quad \mathcal D_2=\mathcal U\times\mathcal V,
 \quad \mathcal D_3=\mathcal V\times\mathcal W,
\]
\[
 \mathcal D_4=\mathcal W\times\{0\},\qquad
 \mathcal D_t=\{p_t\}\ (5\le t<L),\qquad
 \mathcal D=\bigcup_{t=0}^{L-1}\mathcal D_t.
\]
Disjointness follows from the same alphabet types and unique clock pairs. The table explicitly gives

\[
 p_0\to(c_1,A)\to(A,B)\to(B,Z)\to(Z,0)\to(0,0)=p_5,
\tag{4.2}
\]
followed by `p_5,p_6,...,p_(L-1),p_0`. Here A is uniform on U, B conditionally uniform on V, and Z has law `q_sigma(.|A,B)`. Every edge from `D_t` ends in `D_((t+1) mod L)`. This is a phase invariant of the existing pair state, not an external clock or a new observation. It proves closure of D and a return-phase spacing of L. ∎

### unit_002: invariant — All-start one-visit bound (`inv:one-visit`)

**Statement.** For every sign table in the Lawful rotated clock lemma, every starting pair `s in A^2`, every target pair t, and every nonnegative integer h, a base path visits t at most once among its L states at times `h,...,h+L-1`. In particular,

\[
 \sum_{j=0}^{L-1}P_0^j(s,t)\le1,\qquad
 \sum_{j=0}^{L-1}(\lambda P_0^{h+j})(t)\le1
\tag{4.3}
\]
for every probability row lambda and h>=0.

**Proof.** Use two named path invariants. **Phase invariant:** once a state lies in D, it stays there and its phase advances by one mod L, as proved in the Lawful rotated clock lemma. Hence two visits to a fixed t in D have times congruent modulo L, and cannot lie in L consecutive time indices.

**Transient-entry invariant:** if the start `(a,b)` lies outside D, its row is a default row and its next state is `(b,0)`. If this state is in D, entry has occurred in one step. If not, its row is again default, so the following state is `(0,0)=p_5 in D`. Thus entry occurs in at most two steps. The two possible outside states `(a,b)` and `(b,0)` cannot agree: their equality forces `a=b=0`, contradicting the first state's being outside D. After entry no outside state can recur, by closure. Therefore each target outside D is visited at most once in the whole path.

These two invariants cover all paths, including starts involving extra alphabet symbols and removed clock pairs. The number of visits in any L-state block is at most one pathwise. Taking expectations gives (4.3), including arbitrary lambda and later blocks. There is no stationary-start qualification. ∎

### unit_003: lemma — Complete base experiment (`lem:full-experiment`)

**Statement.** Under A1–A3 and the Lawful rotated clock lemma, there is a common sign-independent initial law `mu_{K,M}` such that the entire base observed history is in a public bijection with q training triples `D_1,...,D_q` and the actual terminal pair T. Their exact law is

\[
 D_i\text{ iid},\qquad
 \Pr_\sigma(D_i=(u,v,z))=m^{-2}q_\sigma(z\mid u,v),
 \qquad T\sim\operatorname{Unif}(\mathcal U\times\mathcal V),
\tag{4.4}
\]
with T independent of all training triples. T is `Y_M`, not an additional query sample. This holds for every residue of M and includes all initial observations.

**Proof.** Write `M=qL+d`, `0<=d<L`, and let `k=(2-d) mod L` in `{0,...,L-1}`. Fix public `v_* in V,w_* in W`. Use the following MM5 initialization with the rotated word:

| k | d | Initial pair law `mu_{K,M}` |
|---|---|---|
| 0 | 2 | `delta_(p_0)` |
| 1 | 1 | `delta_(c_1) tensor Unif(U)` |
| 2 | 0 | `Unif(U) tensor Unif(V)` |
| 3 | L-1 | `delta_(v_*) tensor delta_(w_*)` |
| 4 | L-2 | `delta_(w_*) tensor delta_0` |
| 5<=k<L | L+2-k | `delta_(p_k)` |

It is supported on D_k and does not depend on sigma, alpha, or beta. Initial pairs need not arise from unobserved earlier transitions. In particular the fixed `w_*` in phases 3–4 is not a label sampled from an unknown row.

The phase invariant implies `Y_t in D_((k+t) mod L)` for every `0<=t<=M`. The UV times are precisely

\[
 t_i=d+(i-1)L,\quad 1\le i\le q+1,\qquad t_{q+1}=M.
\tag{4.5}
\]
Only `t_1,...,t_q` are observed departures from UV. Define

\[
 D_i=(A_i,B_i,Z_i)=(X_{t_i+1},X_{t_i+2},X_{t_i+3}),\quad 1\le i\le q,
 \qquad T=(A_{q+1},B_{q+1})=Y_M.
\]
All training labels are observed; indeed `t_q=M-L<=M-1` when q>=1. The terminal label is unobserved.

Here is the full inverse encoding `G_{K,M}(D,T)`, not a data-discarding argument. If k is 0,3,4 or at least 5, start from its fixed pair in the table. If k=1, start from `(c_1,A_1)`; if k=2, start from `(A_1,B_1)`. When q=0 the first context is T. For times 0 through M-1 append a symbol according to the phase: at phase 0 append the next context's A; at phase 1 append that context's B; at a phase-2 departure append its specified training label Z; at phase 3 append 0; at phase 4 append `c_6=0`; at any phase 5 through L-1 append the unique clock successor. Stop at terminal phase 2 without producing a label. The phase-3/4 initial prefix uses the prescribed `v_*,w_*`, never an extra training label.

Every appended symbol respects the original shift. Overlapping occurrences of Z in `(B,Z)` and `(Z,0)` are the same symbol, not new observations. Every possible tuple `(D,T)` is realizable because all U,V choices and W labels have positive probability. Extracting the fixed indices (4.5) recovers the tuple; reconstructing an extracted tuple recovers each original symbol. This is a bijection on a common support independent of sigma.

The probability of its reconstructed history, obtained from the initial-pair mass and all M transitions, is exactly

\[
 \Pr_\sigma\{H=G_{K,M}(D,T)\}
 =m^{-2(q+1)}\prod_{i=1}^{q}q_\sigma(Z_i\mid A_i,B_i).
\tag{4.6}
\]
Each context has precisely two factors `1/m`: for k=1 the first A factor comes from the initial law; for k=2 the first A and B factors both do; all other A,B factors come from their uniform transitions. Each training Z has one q_sigma factor and no other transition has one. The fixed initial `w_*` has probability one. The empty product convention covers q=0. Formula (4.6) proves (4.4).

For M=1 this is k=1, q=0: the initial A and newly sampled B are the entire random terminal context. For M=2 it is k=0, q=0. If k=2 and M>=1 then q>=1, so the initially random pair is the first training context. These checks include the potentially exceptional initial observations. Conditional on any `T=s`, which has probability `1/m^2` for every sigma, the entire H remains bijectively encoded by D through the same `G_{K,M}(.,s)`. ∎

### unit_004: lemma — Exact invariant law of the smoothed legal kernel (`lem:invariant-law`)

**Statement.** For each base table of the Lawful rotated clock lemma and every `0<epsilon<1`, let `u(c)=1/K` and define

\[
 \theta^{\sigma,\varepsilon}_s=(1-\varepsilon)\theta^{\sigma,0}_s+\varepsilon u,
 \qquad P=P_{\theta^{\sigma,\varepsilon}}=(1-\varepsilon)P_0+\varepsilon R,
\tag{4.7}
\]
where `R((a,b),(b,c))=1/K` and its other entries are zero. Let `U_pair` be the uniform probability row on `A^2`, and let `Pi_U` be the kernel whose every row equals U_pair. Then with `B=P^2-epsilon^2 Pi_U`,

\[
 \pi_\varepsilon
 =\varepsilon^2\sum_{j=0}^{\infty}U_{\rm pair}B^j
 =\varepsilon^2 U_{\rm pair}(I-B)^{-1}
\tag{4.8}
\]
is a well-defined probability row, the unique invariant probability of P^2, and the unique invariant probability of P. It also obeys the exact convergent identity

\[
 \pi_\varepsilon
 =\varepsilon(\pi_\varepsilon R)
       \sum_{j=0}^{\infty}(1-\varepsilon)^jP_0^j.
\tag{4.9}
\]

**Proof.** Equation (4.7) mixes successor-symbol rows, so it preserves all legal shift structural zeros and remains homogeneous. For arbitrary pairs `s=(a,b)` and `t=(c,d)`, the two successive uniform-symbol choices produce t with probability `1/K^2`. Equivalently `R^2=Pi_U`. Expanding P^2 into its four nonnegative products gives

\[
 P^2(s,t)\ge\varepsilon^2/K^2.
\tag{4.10}
\]
Consequently B is entrywise nonnegative and each row sum is `1-epsilon^2`. Induction gives `B^j 1=(1-epsilon^2)^j 1`. In the maximum absolute row-sum matrix norm, the series `sum B^j` converges because its j-th norm is `(1-epsilon^2)^j`; finite geometric telescoping gives `(I-B) sum B^j=sum B^j (I-B)=I`. This proves the displayed inverse exists, rather than assuming it.

Each summand in (4.8) is nonnegative, and its total mass is `epsilon^2(1-epsilon^2)^j`. Summing gives total mass one. These absolute/geometric bounds justify multiplication of the series by finite matrices and reindexing. Hence

\[
 \pi_\varepsilon B=\pi_\varepsilon-\varepsilon^2 U_{\rm pair},\qquad
 \pi_\varepsilon P^2
 =\pi_\varepsilon B+\varepsilon^2(\pi_\varepsilon\mathbf1)U_{\rm pair}
 =\pi_\varepsilon.
\]

For uniqueness, put `Q=B/(1-epsilon^2)`, a stochastic kernel. If x,y are probability rows, then `(x-y)Pi_U=0` and

\[
 \|(x-y)P^2\|_1=(1-\varepsilon^2)\|(x-y)Q\|_1
 \le(1-\varepsilon^2)\|x-y\|_1.
\]
The last inequality follows by summing `|sum_s (x_s-y_s)Q(s,t)|<=sum_s|x_s-y_s|Q(s,t)` over t. Two P^2-invariant probabilities therefore have zero distance. Also `pi_epsilon P` is a probability and

\[
 (\pi_\varepsilon P)P^2=(\pi_\varepsilon P^2)P=\pi_\varepsilon P.
\]
Uniqueness for P^2 implies `pi_epsilon P=pi_epsilon`. Any P-invariant law is P^2-invariant, proving uniqueness for P as well.

Let `nu=pi_epsilon R`, a probability row. From stationarity and (4.7), iteration for each integer J>=1 gives

\[
 \pi_\varepsilon
 =\varepsilon\sum_{j=0}^{J-1}(1-\varepsilon)^j\nu P_0^j
   +(1-\varepsilon)^J\pi_\varepsilon P_0^J.
\tag{4.11}
\]
The last term is nonnegative with total mass `(1-epsilon)^J`, hence tends to zero in l1. The summands have summable masses `epsilon(1-epsilon)^j`, proving (4.9) and all its convergence assertions. The law may depend on sigma and epsilon, but is never supplied to the predictor. ∎

### unit_005: lemma — Stationary atom control and public-beta membership (`lem:membership`)

**Statement.** Under the Lawful rotated clock lemma, the All-start one-visit invariant, and the Exact invariant law lemma, every `0<epsilon<1` satisfies

\[
 \max_t\pi_\varepsilon(t)
 \le\frac{\varepsilon}{1-(1-\varepsilon)^L}
 \le\frac1L+\varepsilon.
\tag{4.12}
\]
For integers `K>=12,M>=1`, public `0<beta<=K^-4`, and `epsilon=8 sqrt(beta)`, every smoothed source `(theta^{sigma,epsilon},mu_{K,M})` belongs to `D_K(2,beta)`, with

\[
 \pi_\varepsilon(t)\le 33/K^2,\qquad
 P^2(s,t)\ge64\beta/K^2\ge\beta\pi_\varepsilon(t)
 \quad\hbox{for every }s,t.
\tag{4.13}
\]

**Proof.** In (4.9), split the nonnegative series into blocks `j=hL+r`, `0<=r<L`. For `nu=pi_epsilon R`, the All-start one-visit invariant gives

\[
 \sum_{r=0}^{L-1}(\nu P_0^{hL+r})(t)\le1.
\]
Within that block the geometric weight is at most `(1-epsilon)^(hL)`. Thus

\[
 \pi_\varepsilon(t)
 \le\varepsilon\sum_{h=0}^{\infty}(1-\varepsilon)^{hL}
 =\frac{\varepsilon}{1-(1-\varepsilon)^L}.
\]
This block rearrangement is justified by nonnegativity or by the l1 convergence in the Exact invariant law lemma. For the second bound in (4.12), integer Bernoulli's inequality gives

\[
 (1-\varepsilon)^{-L}
 =\left(1+\frac\varepsilon{1-\varepsilon}\right)^L
 \ge1+\frac{L\varepsilon}{1-\varepsilon}\ge1+L\varepsilon.
\]
It follows that `1-(1-epsilon)^L >= L epsilon/(1+L epsilon)`. Dividing the positive quantities yields `(4.12)`.

Write `K=4m+r`, `0<=r<=3`. Since K>=12 implies m>=3>=r, `K<=5m`, so `m>=K/5` and `1/L<=25/K^2`. Also

\[
 0<\varepsilon=8\sqrt\beta\le8/K^2\le8/144=1/18<1.
\]
The atom bound gives `pi_epsilon(t)<=25/K^2+8/K^2=33/K^2`. The two-noise lower (4.10) gives `P^2(s,t)>=epsilon^2/K^2=64 beta/K^2`; since `64>=33`, (4.13) follows. This is an every-pair statement, not a supported-start statement. The invariant law exists and is stationary by the Exact invariant law lemma, and A4 places no restriction on the common initial law. All unused-letter and default rows were smoothed as well. ∎

### unit_006: lemma — Full-history conditional binary testing (`lem:conditional-testing`)

**Statement.** Under A1–A3 and the Complete base experiment lemma with the displayed alpha, for two signs sigma,sigma' differing in one bit, the base full-history laws conditional on any `T=s in U x V` have total variation at most `1/4`. For any common randomized binary test of bit `(s,j)`, uniform averaging over the same finite sign hypercube gives conditional error probability at least `3/8` given `T=s`.

**Proof.** A single training triple under two neighboring signs has KL divergence

\[
 \frac1{m^2}\left[
 \frac{1+\alpha}{m}\log\frac{1+\alpha}{1-\alpha}
 +\frac{1-\alpha}{m}\log\frac{1-\alpha}{1+\alpha}\right]
 =\frac{2\alpha}{m^3}\log\frac{1+\alpha}{1-\alpha}.
\tag{4.14}
\]
All other coordinates agree; this value is the same in either flip direction. By the exact full-history bijection and product law (4.6), conditional on each T=s the full log likelihood ratio is the sum of q training log likelihood ratios. Its expectation is therefore exactly q times (4.14), not a bound obtained by discarding side information. The initial symbols and all repeated clock symbols have already been included in (4.6). The terminal marginal is independent of sigma, including when the flipped bit belongs to terminal row s.

For `0<alpha<=1/2`,

\[
 \log\frac{1+\alpha}{1-\alpha}
 =\int_0^\alpha\frac{2\,dx}{1-x^2}\le4\alpha.
\]
If alpha uses the square-root branch, `8q alpha^2/m^3=q/[8(q+1)]<=1/8`. If alpha=1/2, the branch condition is `m^3>=16(q+1)`, so `8q alpha^2/m^3=2q/m^3<=q/[8(q+1)]<=1/8`. Thus every relevant full conditional KL is at most `1/8`. When q=0 it is exactly zero.

Here are the finite testing tools, restated with proofs as in MM5. For two laws p,r on a common finite positive support, let `F={x:p(x)>=r(x)}` and put `a=p(F),c=r(F)`. Then `TV(p,r)=a-c`. Convexity of `x log x`, applied separately on F and its complement, gives `D(p||r)>=d(a||c)`, where d is binary KL. For `0<c<1`, the second derivative of d in a is `1/a+1/(1-a)>=4`; its value and first derivative at a=c vanish. Integration twice gives `d(a||c)>=2(a-c)^2`. Degenerate cases follow by the zero-TV case or limits. Hence `TV(p,r)<=sqrt(D(p||r)/2)<=1/4` here.

If a randomized test outputs + with probability `phi(x) in [0,1]` at data x, its two errors obey

\[
 p_+(\text{output }-)+p_-(\text{output }+)
 =1-\sum_x(p_+(x)-p_-(x))\phi(x)
 \ge1-\operatorname{TV}(p_+,p_-).
\tag{4.15}
\]
Indeed the positive difference terms contribute at most their sum, TV; negative ones do not increase the sum. For the full conditional laws this is at least `3/4`. A source-independent seed is integrated into phi, so the bound covers the full class of randomized kernels in A3.

Give all `2^(m^2 b)` sign vectors equal prior mass. For fixed s,j, hold other bits fixed and pair the two choices of `sigma_(s,j)`. The sum of their conditional errors is at least `3/4`; averaging all pairs divides this by two and yields at least `3/8`. The conditional prior remains uniform because `Pr_sigma(T=s)=m^-2` is common. All s,j use the same prior, not a separately chosen hard prior for each endpoint. ∎

### unit_007: proposition — Smoothed actual-target lower (`prop:smoothed-loss`)

**Statement.** Under A1–A4, the preceding six local results, and `K>=12,M>=1,0<beta<=K^-4,epsilon=8 sqrt(beta)`, every common randomized full-history predictor satisfies

\[
 \sup_{(\theta,\mu)\in D_K(2,\beta)}
 \mathbb E\operatorname{TV}(\mathsf A(H),\theta_{Y_M})
 \ge (1-\varepsilon)^{M+1}\frac\alpha8.
\tag{4.16}
\]

**Proof.** Fix the public parameters and any one permitted predictor. Realize each of the M observed departures of a smoothed source by an independent Bernoulli coin: with probability `1-epsilon` use its base row, and with probability epsilon append an independent uniform letter. All coins are independent of the initial pair, signs, algorithm seed, and the independent randomness used to implement the row choices. This generates precisely (4.7). Let E be the latent event that all M coins choose the base row. Then

\[
 \Pr_\sigma(E)=(1-\varepsilon)^M>0
\tag{4.17}
\]
for every sigma. Conditional on E, the initial law and all M base transition choices are unchanged, so **the entire observed history law** is the one in the Complete base experiment lemma. In particular `Y_M=T in U x V`; it has probability `m^-2` at each s, independently of sigma, and the conditional training law is (4.4). This does not assert E is independent of the observed H, nor discard any symbols. No coin labels, including E, are given to the predictor. We merely analyze its original common kernel on those histories.

For `T=s`, let `hat p=A(H)` and decode every bit by

\[
 \widehat\sigma_{s,j}=+1\quad\Longleftrightarrow\quad
 \widehat p(w_{2j-1})\ge\widehat p(w_{2j});
\]
otherwise output -1. Ties always go to +1. The **actual smoothed target** at this terminal row has difference

\[
 \theta^{\sigma,\varepsilon}_s(w_{2j-1})
 -\theta^{\sigma,\varepsilon}_s(w_{2j})
 =(1-\varepsilon)\frac{2\alpha\sigma_{s,j}}m.
\tag{4.18}
\]
The two uniform masses cancel. If the decoded sign is wrong, the predicted difference has the opposite weak sign, so its distance from (4.18) is at least `2(1-epsilon)alpha/m`. The triangle inequality on these two coordinates therefore gives

\[
 \frac12\left(
 |\widehat p(w_{2j-1})-\theta^{\sigma,\varepsilon}_s(w_{2j-1})|
 +|\widehat p(w_{2j})-\theta^{\sigma,\varepsilon}_s(w_{2j})|
 \right)
 \ge\frac{(1-\varepsilon)\alpha}{m}
      {\bf1}\{\widehat\sigma_{s,j}\ne\sigma_{s,j}\}.
\tag{4.19}
\]
When the true sign is negative, a tie is an error and the inequality still holds at its boundary. A positive true sign with a tie is deemed correct and creates no required contribution. Different j use disjoint coordinates. Coordinates outside these pairs, including all uniform-smoothed coordinates outside W, contribute nonnegative additional loss. Thus (4.19) sums to a lower bound on the actual full K-coordinate TV.

On E and T=s, the test is a fixed common randomized function of the complete encoded history `G_{K,M}(D,s)`. The Full-history conditional binary testing lemma applies and yields prior-average error at least `3/8` for each bit. Moreover the prior given E,T=s stays uniform, since `Pr_sigma(E,T=s)=(1-epsilon)^M/m^2` is common. Writing `Av_sigma` for the one uniform prior, nonnegativity of the loss permits

\[
\begin{aligned}
 \operatorname{Av}_\sigma\mathbb E_{\sigma,\varepsilon}
   \operatorname{TV}(\mathsf A(H),\theta^{\sigma,\varepsilon}_{Y_M})
 &\ge \operatorname{Av}_\sigma\mathbb E_{\sigma,\varepsilon}
       [{\bf1}_E\operatorname{TV}(\mathsf A(H),\theta^{\sigma,\varepsilon}_{Y_M})]\\
 &\ge (1-\varepsilon)^M
       \frac{(1-\varepsilon)\alpha}{m}\frac1{m^2}
       \sum_{s\in\mathcal U\times\mathcal V}\sum_{j=1}^b\frac38\\
 &= (1-\varepsilon)^{M+1}\frac{3\alpha b}{8m}
 \ \ge (1-\varepsilon)^{M+1}\frac\alpha8.
\end{aligned}
\tag{4.20}
\]
For m>=3, `b/m>=1/3`: for even m it is 1/2, and for odd m it is `(m-1)/(2m)>=1/3`. Loss outside E may contain useful information and may be small; it was discarded solely because it is nonnegative.

Every member of this finite family belongs to A4 by the Stationary atom control and public-beta membership lemma. For the fixed common A, its class supremum is at least its largest family risk, which is at least the finite average (4.20). This proves (4.16). Then the infimum over A gives the first inequality in (S010). Fixing beta before the infimum is legitimate: the testing proof applies to each A selected with that public beta. No infimum and supremum have been exchanged, and no single sign vector is asserted to fool every algorithm. In particular no false pointwise relation between old and smoothed TV losses has been used. ∎

### unit_008: proposition — Capped finite rate and bounded survival (`prop:capped-rate`)

**Statement.** Under the hypotheses of the Smoothed actual-target lower proposition, its finite-family bound implies (S010). Under the additional condition `n sqrt(beta)<=2`, it and the accepted L1MAX interface imply (C). The sequence `M=K^4,beta=K^-8,K>=12` is covered. At beta zero the original MM5 endpoint is available separately without any singular stationary inverse.

**Proof.** Put `z=sqrt(K^5/(M+1))` and `t=sqrt(m^3/(q+1))`. The exact capped amplitude satisfies

\[
 \frac\alpha8=\min\left\{\frac1{16},\frac t{64}\right\}
 \ge\frac1{64}\min\{1,t\}.
\tag{4.21}
\]
If q=0, `t=m^(3/2)>1`, so (4.21) is at least `1/64`, which exceeds `2^-16 g` for every M in this branch.

If q>=1, then `q+1<=2q<=2M/m^2`. Since `m>=K/5>=K/8`,

\[
 t^2\ge\frac{m^5}{2M}
 \ge\frac{K^5}{2\cdot8^5(M+1)}
 =\frac{z^2}{256^2}.
\tag{4.22}
\]
For z<=1, `min(1,t)>=z/256`; for z>=1, `t>=1/256` and hence `min(1,t)>=1/256`. In both cases `min(1,t)>=min(1,z)/256`. Combining (4.21)–(4.22) gives `alpha/8>=2^-14 g>=2^-16 g`. This retains conservative slack rather than changing the requested constant. Multiplying by the nonnegative survival factor in (4.16) proves (S010), including q=0 and all capped parameter ranges.

For `0<=x<=1/2`, the function `log(1-x)+2x` vanishes at zero and has derivative `(1-2x)/(1-x)>=0`. Therefore `log(1-epsilon)>=-2epsilon` since epsilon<=1/18. Consequently

\[
 (1-\varepsilon)^n\ge\exp(-2n\varepsilon)
 =\exp(-16n\sqrt\beta)\ge e^{-32}
 \quad\hbox{if }n\sqrt\beta\le2.
\tag{4.23}
\]
The lower side of (C) follows. A4 is a subclass of all A1 sources with arbitrary initialization, so accepted L1+ yields the upper in (C) for exactly the original all-M-departure predictor. The minimax inequality `R_D2<=R_D2^+` follows by choosing that one permissible rule. Also `min(1,48z)<=48min(1,z)=48g`, so the chain is indeed a matching rate with absolute constants in the specified bounded-survival region.

For `M=K^4,beta=K^-8`, beta<=K^-4 and `n sqrt(beta)=1+K^-4<=2`. Moreover `K^5>=K^4+1` for K>=12, so g=1. Thus the minimax risk is bounded below by the explicit positive constant `2^-16 e^-32`, while add-one risk is at most one. This is a constant-risk conclusion in that particular sequence, not a statement for every beta.

At beta=0, A4 imposes the vacuous inequality `P^2(s,t)>=0` besides finite-state stationarity. Every finite stochastic kernel has a stationary probability: take any rho, form `J^-1 sum_(j=0)^(J-1) rho P^j`, choose a convergent subsequence in the finite-dimensional compact simplex, and observe that the l1 difference after multiplication by P is at most `2/J`; its limit is stationary. Thus the class is the original full arbitrary-initialization class. Accepted MM5 and L1MAX give respectively `2^-16 g` and `min(1,48z)` for all `K>=2,M>=1`. This does **not** substitute epsilon=0 into (4.8), whose inverse argument assumes epsilon>0. For fixed K,M the positive-beta lower's survival factor tends to one, consistent with that exact endpoint. No new positive-beta extension to K<12 is claimed. ∎

## 5. Target-step assembly and obligation discharge

The Lawful rotated clock lemma establishes the full legal four-alphabet table and the stronger loop placement, using the inherited MM5 construction explicitly. Its phase invariant and the All-start one-visit invariant establish every-start entry, nonrepeating transient prefix, and all-block occupation control. The Complete base experiment lemma retains the full initial pair and every symbol for all M residues; it creates no external state and no independent replacement target.

The Exact invariant law lemma constructs, normalizes, and proves invariance and uniqueness of the smoothed stationary law, with both infinite-series limits justified. The Stationary atom control and public-beta membership lemma uses the all-start occupation bound to prove `pi_max<=33/K^2` and the all-pair two-step lower `64 beta/K^2`, thereby satisfying A4 for each family member.

The Full-history conditional binary testing lemma and the Smoothed actual-target lower proposition use the unchanged conditional full observation law, one common finite sign prior, randomized tests and the new target contrast. Their two factors `(1-epsilon)^M` and `1-epsilon` are separately justified. They establish the stronger finite-family bound without an additive continuity penalty. The Capped finite rate and bounded survival proposition proves the requested constants, matching bounded-survival corollary, concrete K^4/K^-8 sequence and nonsingular beta-zero endpoint.

No unsupplied invariant, numerical check, unreviewed diagnostic equation, or inherited risk inequality is used as a substitute for these proofs. The only black-box mathematical conclusions consumed are the exact L1MAX upper and the separately identified MM5 beta-zero endpoint. All source-family and testing reuse is attributed, rather than presented as a new original construction.

## 6. Explicit rate audit and limits

- Exposed variables: integers K>=12,M>=1 and public `0<beta<=K^-4`; the source and initialization can depend on these, and the hard sign can depend on the chosen algorithm. One fixed theta is used throughout each trajectory.
- No hidden constants: lower `2^-16`, smoothing `8`, stationary atom `33`, pair floor `64`, and bounded-survival exponent `32` are explicit. The inherited upper constant is 48.
- Mode: expected half-l1 TV at the actual same-trajectory terminal row, over full history and source-independent algorithm randomization. No high-probability, KL-risk, squared-TV, fixed-query, independent-query or randomly selected-time claim is substituted.
- Horizon: exactly M observed departures; n=M+1 in the survival/target product; q=floor(M/m^2) only counts the base unknown-row training departures.
- Auxiliary quantities: alpha is the stated capped public amplitude, not an unknown tunable oracle. The stationary law and coins are proof-local, hidden from the algorithm. The all-start occupation result is specific to this explicit family.
- Probability conversion: only nonnegative loss on the latent E is retained; E has exact probability `(1-epsilon)^M`. Testing costs `(1-epsilon)alpha/m` per wrong bit against the new target. Equation (4.20) performs the actual-row average.
- Capping and branch checks: q=0, q>=1, both amplitude branches, m odd/even, ties, M=1, M=2, extra letters, and every initialization phase are addressed explicitly.
- Baseline: the positive-beta lower tends to the requested MM5 constant for fixed K,M as beta decreases to zero; the beta-zero result is independently inherited with its full all-K scope. No inverse is evaluated at zero.
- **Not proved:** a sharp joint rate for all K,M,beta; an optimal exponential survival factor; necessity of a burn threshold; full weak-window closure; a positive-beta extension to K<12; any implementation/resource theorem. The upper/lower chain is claimed matching only under `n sqrt(beta)<=2`. Outside that region (S010) remains a valid lower but need not be competitive with other accepted lower bounds.
- For orientation only, at `M=K^4,beta=K^-6` the lower's survival factor is `(1-8K^-3)^(K^4+1)`, not a uniform positive constant. No conclusion about the true minimax rate in that remaining window follows from this proof.


MM5 source-to-new-claim map: its Section 2 is reused in the Lawful rotated clock lemma, with the new `c_6=0` rotation and outside-support analysis proved here; Sections 3–4 are instantiated in the Complete base experiment lemma; Sections 5–7 are restated for conditional testing and then modified for the smoothed target; Section 8 supplies the conservative finite constant pattern, explicitly rederived in the Capped finite rate proposition. The all-pair minorization and invariant-law resolvents are new arguments here, not claims imported from MM5. L1MAX Section 8 L1+ supplies only the unchanged original predictor upper.
