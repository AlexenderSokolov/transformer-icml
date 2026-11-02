# S015 星形时钟闭合对数弱混合窗口

编排说明（非原文）：以下逐字保留原已接纳版本的完整数学论证、必要定义、范围与科学解释，仅省略身份、内部控制、来源元数据、重复提交摘要及运行记录。原有数学编号及 Euler clock 名称不变。新增标题与本说明不是原证明。依赖闭包与源哈希见 ../SOURCES.md，精确字节映射见 ../COPY_MAP.json。本次编排不是重新证明或对复制件的新数学审查。

编排时序说明（非原文）：本原版本已获独立审查及接纳。它更新 Stage03 的历史对数窗口开放叙述：M=K⁴、β=ln(K)/(4K⁴) 处，公共算法的全类 minimax 率为 Θ(K⁻¹⁄⁸)。这不是精确极限常数，也不是原始全历史 add-one 的匹配上界。MM5 仅贡献被明确归因的构造／检验方法；新几何及全部桥梁在本文重证。原作者有限检查保留，未由编排重跑。

For every integer `K>=13,M>=1` and public `0<beta<1`, put

    delta=1-beta, m=floor((K-1)/4), L=2m, q=floor(M/L),
    alpha=min{1/2,(1/8)sqrt(m^3/(q+1))}.

The legal star family below belongs to the unchanged arbitrary-start class `D_K(2,beta)`. Its exact publicly determined vulnerable-departure count H_M gives, for every common randomized full-history predictor, the finite-prior lower

    average_sigma E TV(B(H),theta^sigma_(Y_M)) >= delta^(H_M+1) alpha/8.   (SC)

The source-blind constant predictor `delta_0` has risk **exactly** `delta^(H_M+1)` on every member of this family. This is a family-only upper, not a full-class upper. Also

    alpha/8 >= 2^-12 min{1,sqrt(K^4/(M+1))}.                                (AMP)

Along `M=K^4,beta=(log K)/(4K^4)`, the right side of (SC) divided by `K^-1/8` tends to `1/(512sqrt(2))`. The accepted S011/S012 public common-predictor upper U divided by `K^-1/8` tends to one. Consequently the common full-class minimax risk on this particular sequence is **Theta(K^-1/8)**.

For the SAME family, if C_ref denotes at least one of the M canonical symbol-refresh coins being one, every common predictor also satisfies

    average_sigma E[TV(B(H),theta^sigma_(Y_M)) 1_(C_ref)]
       >= (alpha/8)[delta^(H_M+1)-delta^(M+1)].                              (AFTER)

Its right side has the same `K^-1/8` lower-certificate asymptotic. Thus neither a universal aggregate bound `C_0(a+sqrt(beta))` nor a full-class total bound `O(a+delta^M g+sqrt(beta))` can hold in the stated common-algorithm experiment, where `a=min(1,sqrt(K^3/(M+1)))` and `g=min(1,sqrt(K^5/(M+1)))`.

This is a **material_partial** advance: it closes the specified logarithmic window and negates the two precise proposed bounds. It does not give the full joint `(K,M,beta)` rate or a matching upper for original full-history add-one. It does not contradict S012's exact upper for its different old family. S014 is a separate route and supplies no premise.

## 1. Step identity, exact target and primitive setting

The original experiment is unchanged. On `A={0,...,K-1}`, a fixed homogeneous normalized table theta induces only legal transitions

    P_theta((a,b),(b,c))=theta_ab(c),

and zero on non-shift transitions. Initial pair law mu is arbitrary. Membership of `D_K(2,beta)` means some hidden stationary probability pi satisfies

    pi P_theta=pi,     P_theta^2(s,t)>=beta pi(t) for EVERY s,t in A^2.     (1)

Zeros, sparse pi, and mu singular to pi are permitted. A source may be selected separately at each public `K,M,beta`, but is unchanged within its trajectory. Observe the entire `H=(X_1,...,X_(M+2))`, with `Y_j=(X_(j+1),X_(j+2))`, `0<=j<=M`. Exactly M departures, indexed `j=0,...,M-1`, are observed. The target is the actual endpoint row `theta_(Y_M)` for unobserved `X_(M+3)`.

A common predictor B is any probability kernel from the full H to the K-simplex, allowed public `K,M,beta` and an independent seed, but no hidden table, mu, pi, signs, refresh labels, or future. Risk is `E TV(B(H),theta_(Y_M))`, where `TV(p,r)=||p-r||_1/2`. Define

    R_D2(K,M,beta)=inf_B sup_((theta,mu) in D_K(2,beta))
                          E TV(B(H),theta_(Y_M)).                          (2)

The finite construction theorem assumes `K>=13,M>=1,0<beta<1`; no small-alphabet patch or endpoint assertion is needed for its target. The accepted stronger general beta-zero baseline and beta-one IID baseline remain unchanged, not replaced by the weaker K^4 witness.

The primitive conditions are exactly this finite legal experiment, information restriction, and class definition. The setting has no stable primitive assumption IDs; its content is stated rather than assigning fictitious upstream IDs. All phase, membership, source-independent conditioning, product-data and target-contrast claims below are derived invariants, not new assumptions.

## 2. Cited result applications and local lemma map

### Accepted interfaces and the uses made of them

1. **Frozen MM5** readable proof Sections 1–9. Its full-history machinery constructs paired-sign W rows, all-residue initial laws, an exact history/product-experiment bijection, and finite conditional sign tests. We explicitly reuse this design but reprove every new star-period/zero-output/event bridge and the exact conditional path law. The old black-box risk theorem is NOT applied with an unchanged target. Its Euler `L=m^2>=9` geometry is NOT imported; here `L=2m>=6`. The complete finite testing proof is reproduced below, including the new contrast delta.
2. **Accepted S011, Theorem S011**, for exactly (1)–(2): with `u_s(ell)=min(1,48sqrt(K^3/(ell+1)))`, `u_g(ell)=min(1,48sqrt(K^5/(ell+1)))`, `h_b=delta^floor(b/2)` for beta<1, the three separate certificates are

       U_+=min{u_g(M), min_(0<=b<=M-1)
                 min{1,48sqrt(K^3/(M-b+1))+13sqrt(K)h_b^(3/4)}},
       U_suf=min_(0<=b<=M-1)
                 min{u_g(M-b),u_s(M-b)+h_b u_g(M-b)},
       U_pool=min{1,(1/2)sqrt(K/M)+2delta},
       U=min{U_+,U_suf,U_pool}.                                            (3)

   A deterministic public selector between original add-one, a deterministic public-bound-minimizing suffix add-one, and pooling has full-class risk at most U. Only U_+ is a certificate for original full-history add-one. Our entire domain satisfies this interface's finite legal-shift/arbitrary-mu/all-pair assumptions. Its upper is used in Proposition 8 below, with no source-dependent algorithm choice.
3. **Accepted S012, Proposition 9**, on exactly `M=K^4,beta=(log K)/(4K^4)`: `U/K^-1/8 ->1`, with the very same U in (3), and `U_+=U_pool=1` eventually. Its uniform-over-burn lower bound on the suffix certificate and matching admissible public suffix are restated and checked in Proposition 8. S012 Proposition 8's old-family `delta^(M+1)` upper is used only as a scope comparison, never as a restriction on the new family.


| Local unit | Result and stable reference | Contribution |
|---|---|---|
| unit_001 | Lemma 1, Legal star geometry (`lem:s015-star`) | Explicit distinct pairs, disjoint table, m=3 wrap |
| unit_002 | Invariant 2, Base phases and vulnerable rows (`inv:s015-phase`) | Legal length-L cycle, exact vulnerable/safe partition |
| unit_003 | Lemma 3, Every-pair minorization (`lem:s015-member`) | pi=delta00, all rows including deleted/default, exact coefficient |
| unit_004 | Lemma 4, Every-residue complete experiment (`lem:s015-history`) | Six initial laws, full bijection, exact q labels/actual endpoint |
| unit_005 | Lemma 5, Vulnerable-only event (`lem:s015-event`) | Complete conditional law, common prior, exact first-failure target |
| unit_006 | Proposition 6, Changed-target finite testing (`prop:s015-lower`) | Randomized full-history lower and exact family-only upper |
| unit_007 | Proposition 7, Exact count and finite amplitude (`prop:s015-count`) | H_M decomposition, finite K^4 simplification |
| unit_008 | Proposition 8, Matched logarithmic window (`prop:s015-window`) | Controlled errors, constants, full-class common-minimax match |
| unit_009 | Proposition 9, Same-witness refresh negatives (`prop:s015-after`) | Canonical residual, aggregate bracket, precise upper-bound negations |

## 3. Local derivation

### unit_001: Lemma 1 — Legal star geometry (`lem:s015-star`)

**Statement.** Under Section 1 with `K>=13,M>=1,0<beta<1` and the public m,L,q,alpha above, the following construction is a normalized homogeneous legal-shift table on all K-squared rows. Its L distinct base star pairs and replacement rows are well-defined even at m=3,L=6.

**Proof.** Reserve central/reset symbol 0 and take disjoint nonzero groups

    C={1,...,m}, U={m+1,...,2m}, V={2m+1,...,3m}, W={3m+1,...,4m}.

They lie in A since `4m+1<=K`. Label W by `w_j=3m+j`. Define the periodic word, for `0<=j<m`,

    c_(2j)=j+1, c_(2j+1)=0, c_(t+L)=c_t,
    p_t=(c_t,c_(t+1)),                  0<=t<L.                             (4)

Its even pairs are `(j+1,0)`; its odd pairs are `(0,j+2)` with the peripheral index wrapping from m to 1. Even pairs are distinct, odd pairs are distinct, and an even pair cannot equal an odd pair because peripheral symbols are nonzero. Thus all L pairs are distinct. In particular `c_1=c_5=0` for every m>=3, and c_6 is a nonzero peripheral (equal to 1 at m=3).

Let `r=floor(m/2)` and `I=(U x V) x {1,...,r}`. For each sign vector `sigma in {-1,+1}^I`, fixed for the whole experiment, set for s in U x V

    q_sigma(w_(2h-1)|s)=(1+alpha sigma_(s,h))/m,
    q_sigma(w_(2h)|s)  =(1-alpha sigma_(s,h))/m,            1<=h<=r.          (5)

When m is odd, give the leftover w_m mass 1/m; W-external coordinates have mass zero. Each paired sum is 2/m, so each q_sigma is a probability vector. Each W coordinate is at least `1/(2m)>0` since `0<alpha<=1/2`.

Define disjoint phase sets

    D_0={p_0}, D_1={0} x U, D_2=U x V, D_3=V x W, D_4=W x {0},
    D_t={p_t} for 5<=t<L,        D=union_(t=0)^(L-1) D_t.                  (6)

Distinct alphabet types separate D_1,...,D_4 from each other and from star pairs. The star-pair uniqueness separates D_0,D_5,...,D_(L-1). No phase contains 00. Define the full base table Q_sigma by

    at p_0:      Unif(U),
    at (0,u):    Unif(V),                          u in U,
    at (u,v):    q_sigma(.|u,v),                   (u,v) in U x V,
    at (v,w):    delta_0,                          (v,w) in V x W,
    at (w,0):    delta_(c_6),                      w in W,
    at p_t:      delta_(c_(t+2)),                  5<=t<L,
    elsewhere:   delta_0.                                                  (7)

All assignments are disjoint by (6); every other pair is explicitly filled by the last line. In particular deleted p_1,...,p_4 and every leftover-letter row are default rows. Define the actual table by

    theta_sigma(s)=delta Q_sigma(s)+beta delta_0,        s in D;
    theta_sigma(s)=delta_0,                              s not in D.        (8)

Since Q_sigma is itself delta_0 outside D, equivalently (8) is `beta delta_0+delta Q_sigma(s)` on EVERY row. These are normalized nonnegative rows with no dependence on time, counts or realized randomness. Appending a symbol from a row always induces exactly `(a,b)->(b,z)`, so this is a legal homogeneous order-two source on the original alphabet and pair space. No external phase state has been added.

The five-step base replacement is exactly

    p_0 -> (0,A) -> (A,B) -> (B,Z) -> (Z,0) -> (0,c_6)=p_5.                (9)

It uses `c_1=c_5=0`. The draws are A uniform on U, B conditionally uniform on V, Z conditionally q_sigma given A,B. After p_5, the retained transitions follow `p_5,p_6,...,p_(L-1),p_0`. At m=3, the explicit word is `(1,0,2,0,3,0)`, L=6, c_6=c_0=1 and p_5=(0,1). The sole retained transition appends c_7=c_1=0 and returns from p_5 to p_0=(1,0). Thus all six phases and the five-step replacement are valid with one retained step; no old L>=9 condition is required. ∎

### unit_002: Invariant 2 — Base phases and vulnerable rows (`inv:s015-phase`)

**Statement.** Under Lemma 1, every base transition from D_t goes to `D_((t+1) mod L)`. The base support D is closed and has exact cycle period L. Base outputs are nonzero precisely at the phases

    V_phase={0,1,2,4} union {6,8,...,L-2},       |V_phase|=m+1.              (10)

At every other phase the base and actual row both equal delta_0. For every vulnerable row `(a,b)`, `b in {0} union U union V` and `(b,0)` is a genuinely default row.

**Proof.** The first five successors in (9) prove the phase transition for t=0,...,4. For a retained clock pair p_t, appending c_(t+2) gives p_(t+1), including the modular return t=L-1. This proves the phase invariant and closure. From any D_t the base reaches p_0 within at most L steps. Conversely positive U/V choices and positivity of all W labels make every state in D reachable from p_0. Every return to p_0 must be at a multiple of L by disjoint phases, and a return in exactly L steps occurs with probability one. Hence this closed base class is irreducible and its return-time gcd is L. This statement is about the base class, not periodicity of the absorbing actual chain.

At phase 0 outputs lie in U, at phase 1 in V, at phase 2 in W, and at phase 4 the output is nonzero c_6. Phase 3 outputs 0. For retained t, even t gives even t+2 and a nonzero peripheral, whereas odd t gives odd t+2 and 0. The retained evens are exactly 6,8,...,2m-2, a set of m-3 elements (empty at m=3). Adding four exceptional vulnerable phases gives m+1. The safe phases are 3 and retained odds `5,7,...,2m-1`; their count is `1+(m-2)=m-1`. Every safe actual row remains delta_0 under (8), so coin refresh at such a row has no observational effect.

Vulnerable phase 0 has second coordinate 0, phase 1 a U coordinate, phase 2 a V coordinate, phase 4 coordinate 0, and every retained even pair has second coordinate 0. None of `(0,0)`, `(u,0)` for u in U, or `(v,0)` for v in V occurs in (6): the only active ending-zero rows are p_0, retained even star pairs, and W x {0}, whose first coordinates are respectively in C,C,W. Therefore all relevant `(b,0)` rows are default. This explicit check, rather than a general claim about all ending-zero rows, is essential. ∎

### unit_003: Lemma 3 — Every-pair minorization (`lem:s015-member`)

**Statement.** Under Lemma 1 and Invariant 2, `pi=delta_(0,0)` is stationary and `P_sigma^2(s,t)>=beta pi(t)` for EVERY pair s,t. The maximal coefficient relative to this pi is exactly beta; pi is unique for beta>0, so no alternative stationary witness increases that coefficient.

**Proof.** State 00 is default, has row delta_0 and is absorbing; hence pi is stationary. For ANY starting pair s=(a,b), the unique two-step path ending at 00 must append 0 then 0, giving

    P_sigma^2((a,b),(0,0))=theta_sigma(a,b)(0) theta_sigma(b,0)(0).          (11)

If s is vulnerable, its base row has no mass at 0, so the first factor is beta. Invariant 2 proves that `(b,0)` is default, giving second factor 1 and product exactly beta.

If s is safe active or default, its actual row is delta_0 and the first factor is 1. Every row of (8) gives probability at least beta to 0, so the second factor is at least beta. This includes a default start ending in a peripheral or W: its successor `(b,0)` can be vulnerable active, but then the second factor is beta, not incorrectly claimed to be one. Thus (11)>=beta for all K-squared starts, including every removed star pair and leftover-letter pair. At other destinations pi(t)=0, so the required inequality is nonnegativity. The all-state membership claim follows for arbitrary mu.

Vulnerable rows exist (phase 0 suffices), and (11)=beta there; hence a larger coefficient for this pi fails. For completeness, uniqueness is derived rather than assumed. The kernel `R=(P_sigma^2-beta Pi)/delta`, where every row of Pi is pi, is stochastic. Stationarity gives pi R=pi. Any stochastic kernel contracts TV by the triangle inequality, since `sum_t |sum_s (nu(s)-rho(s))R(s,t)|<=sum_s |nu(s)-rho(s)|`. If nu were another stationary law, then

    TV(nu,pi)=TV(nu P_sigma^2,pi P_sigma^2)
              =delta TV(nu R,pi R)<=delta TV(nu,pi).

Since delta<1 this forces nu=pi. This extra conclusion is not needed to permit sparse pi or singular mu, but confirms exact coefficient even across stationary witnesses. ∎

### unit_004: Lemma 4 — Every-residue complete experiment (`lem:s015-history`)

**Statement.** Under Lemma 1 and Invariant 2, write `M=qL+d`, `0<=d<L`, and `k=(2-d) mod L`. There is a common sign-independent initial law such that the base experiment's entire M+2-symbol history is in public bijection with q labeled triples plus its actual terminal U x V pair. Its exact law is (14) below; the endpoint is uniform and independent of those q triples.

**Proof: initialization and indices.** Fix public `v_* in V,w_* in W`. Use the following mu, the same for every sign:

| k | d | Initial pair law | Initial residual segment |
|---|---|---|---|
| 0 | 2 | `delta_(p_0)` | Draw A then B |
| 1 | 1 | `delta_0 tensor Unif(U)` | Initial A, then draw B |
| 2 | 0 | `Unif(U) tensor Unif(V)` | Initial pair already A,B |
| 3 | L-1 | `delta_(v_*,w_*)` | Append 0 then c_6 to reach p_5 |
| 4 | L-2 | `delta_(w_*,0)` | Append c_6 to reach p_5 |
| 5<=k<L | L+2-k | `delta_(p_k)` | Follow retained clock, then draw A,B |

All laws lie in D_k. An arbitrary initial pair is not required to have been generated by an unobserved earlier transition, so initial w_* in phases 3/4 is fixed information, not an unknown-row label. The laws depend on public K,M but not sigma or alpha. Their singularity relative to delta00 is allowed.

Induction using Invariant 2 gives `Y_j in D_((k+j) mod L)` for all `0<=j<=M`. Thus the U x V visit times are exactly

    t_i=d+(i-1)L,             1<=i<=q+1,           t_(q+1)=M.               (12)

Exactly the first q are observed departures. Define

    E_i=(A_i,B_i,Z_i)=(X_(t_i+1),X_(t_i+2),X_(t_i+3)),        1<=i<=q,
    T=(A_(q+1),B_(q+1))=(X_(M+1),X_(M+2))=Y_M.                            (13)

If q>=1 the last training departure is M-L<=M-1, so its label is observed even at L=6. The terminal label is never observed. At M=1, q=0,k=1: initial A and one newly drawn B form T. At M=2, q=0,k=0: two draws form T. At arbitrary q=0 there are no training labels. The case q=0,k=2 would imply M=0 and is outside the domain. Every residue and initial case remains valid when L=6.

**Proof: complete public bijection.** Given any tuple `(E_1,...,E_q,T)` in `(U x V x W)^q x (U x V)`, reconstruct H without knowing sigma or alpha. For fixed initial cases k=0,3,4 or k>=5 use their specified initial pair. For k=1 use `(0,A_1)`; for k=2 use `(A_1,B_1)`, with index 1 referring to T if q=0. Follow the public phase sequence for the M departures. Phase 0 appends the A coordinate of the next scheduled U x V context; phase 1 appends its B coordinate; an observed phase 2 appends its specified Z_i; phase 3 appends 0; phase 4 appends c_6; all retained phases append c_(t+2). Stop at the terminal phase 2 without appending its label. In an initial phase-3/4 segment use the fixed w_*, not a nonexistent training sample.

This appends one symbol at a time, preserving overlaps of adjacent pairs. In particular the occurrence of Z_i in `(B_i,Z_i)` and `(Z_i,0)` is one observed draw appearing twice in overlapping pairs, not an independent extra sample. The phase schedule and the tuple specify every initial and subsequent symbol. Every tuple has positive base probability because all U,V choices and all W labels do. Extracting at (13) recovers the tuple; reconstructing after extraction recovers every symbol of the original H. Hence this is a bijection, denoted `Rec_(K,M)`, on the full common base support, not a discarded statistic used in the wrong lower-bound direction.

**Proof: exact full path law.** Multiply `mu(Y_0) product_(j=0)^(M-1) Q_sigma(Y_j)(X_(j+3))`. Every one of the q+1 contexts contributes two factors 1/m, one for A and one for B. At k=1 the first A factor comes from mu; at k=2 both first-context factors come from mu; in the other cases they come from the two uniform transitions. Each factor occurs exactly once. The q labels contribute their q_sigma factors. Every filler and fixed initial symbol contributes factor one. Therefore

    P_base,sigma(H=Rec_(K,M)(E_1,...,E_q,T))
       =m^(-2(q+1)) product_(i=1)^q q_sigma(Z_i|A_i,B_i).                  (14)

For q=0 the product is empty and the mass is m^-2. Thus the FULL observation experiment is exactly q IID triples with law `m^-2 q_sigma(z|u,v)`, together with the uniform actual endpoint T independent of all triples. Conditional on any `T=s`, the triple law is unchanged and full H is reconstructed by the same public map `Rec_(K,M)(.,s)`. This independence is proved only for this constructed experiment; T is the actual terminal pair, not an independent query added to the data. ∎

### unit_005: Lemma 5 — Vulnerable-only event and exact first-failure target (`lem:s015-event`)

**Statement.** Under Lemmas 1, 4 and Invariant 2, realize the actual source using independent Bernoulli(beta) coins `J_0,...,J_(M-1)` independent of the initial draw, all base draws and the algorithm seed. Define

    T_v={j:0<=j<M, (k+j) mod L in V_phase},
    H_M=|T_v|,
    G={J_j=0 for every j in T_v}.                                          (15)

Then `P_sigma(G)=delta^H_M`, and conditional on G the entire history has exactly (14), with `P_sigma(T=s|G)=m^-2`. The uniform sign prior remains common/uniform after conditioning on G and T=s. Off G the actual terminal row is delta_0, even if the first failed vulnerable coin is the last observed departure.

**Proof.** Since (8) equals `beta delta_0+delta Q_sigma` on every row, append 0 if J_j=1 and otherwise sample from Q_sigma at the current pair. Conditional on each actual past this has exactly the original table law, including safe and default rows. A convenient construction uses independent uniform random variables for base sampling at each time; their measurable sampling functions use the fixed row and sigma. The coins are independent of those random variables and initial draws. They are latent proof variables, not observations given to B.

T_v is deterministic from the public integers and phases, not a stopping set based on realized states. Its H_M coin restrictions give `P_sigma(G)=delta^H_M>0`, the same for every sigma. On G, prove by induction that the actual path agrees with the path using the same base randomness and all base transitions. Initially both use mu in D_k. At a scheduled vulnerable phase the coin is forced zero. At a scheduled safe phase both Q_sigma and the refreshed output are delta_0, regardless of the coin. In either case the same symbol is appended, so Invariant 2 advances both paths to the same next phase. Thus all M+2 symbols agree. Conditioning on G only restricts independent coins and does not change the base randomness; the conditional full law is precisely (14).

It follows that `P_sigma(G,T=s)=delta^H_M/m^2` for every sign and s. Under the one uniform sign prior these event probabilities are common, so conditioning on G,T=s leaves that prior uniform; no claim is made that the posterior remains uniform after the rest of H is observed. The independent algorithm seed is also unaffected.

On G-complement let tau be the first scheduled vulnerable time with J_tau=1. Before tau all earlier vulnerable coins are zero, so the same induction gives the base phase at tau even if safe refreshes have occurred. At this vulnerable row `(a,b)`, Invariant 2 gives `b in {0} union U union V` and proves `(b,0)` genuinely default. The failed coin appends 0 and the next pair is therefore default. Its next output is necessarily 0, after which the pair is 00 forever. If tau=M-1, the terminal pair is already `(b,0)` and its target row is delta_0; no extra observation is required to make the target default. If tau<M-1 the same remains true thereafter. Hence off G the terminal target equals delta_0. This argument uses the first failed vulnerable coin, not the first coin of any kind. ∎

### unit_006: Proposition 6 — Changed-target finite testing and exact family upper (`prop:s015-lower`)

**Statement.** Under Lemmas 1, 3–5 and Invariant 2, for every common randomized full-history predictor B the single uniform prior on `{-1,+1}^I` satisfies (SC). Therefore `R_D2>=delta^(H_M+1) alpha/8`. For each sign, the common constant predictor `B_0(H)=delta_0` has risk exactly `delta^(H_M+1)` on the constructed family and its mu. Consequently that family's restricted minimax risk lies between these two quantities; its upper is not asserted for the full class.

**Proof: full conditional information.** Fix any actual `T=s in U x V` and signs differing only at one bit `(s_0,h_0)`. By Lemmas 4–5, given G,T=s their full histories are public bijective images of the q-fold triple product in (14). One triple's KL in either flip direction is exactly

    (1/m^2)[((1+alpha)/m)log((1+alpha)/(1-alpha))
             +((1-alpha)/m)log((1-alpha)/(1+alpha))]
       =(2alpha/m^3)log((1+alpha)/(1-alpha)).                              (16)

Only the two labels at context s_0 differ; the odd unpaired coordinate contributes zero. For q independent triples the likelihood ratio multiplies and its log adds. Thus the FULL conditional-history KL equals q times (16), including when s_0=s. Since

    log((1+alpha)/(1-alpha))=integral_0^alpha 2/(1-x^2) dx<=4alpha,

this KL is at most `8q alpha^2/m^3<=1/8`. To check both truncation branches, the square-root branch gives `8q alpha^2/m^3=q/[8(q+1)]`; the alpha=1/2 branch requires `m^3>=16(q+1)` and gives `2q/m^3<=q/[8(q+1)]`. At q=0 the KL is zero. Conditioning on G has not multiplied the information by a latent-coin factor; it has restored the complete base law exactly.

For completeness, finite Pinsker with the present half-L1 normalization says `TV(P,Q)<=sqrt(KL(P||Q)/2)`. On the set E where P>=Q, write u=P(E),v=Q(E); then `TV(P,Q)=u-v`. Convexity of x log x on E and its complement gives `KL(P||Q)>=u log(u/v)+(1-u)log((1-u)/(1-v))`. As a function of u this binary divergence has value and derivative zero at u=v and second derivative `1/u+1/(1-u)>=4`, so integrating twice gives at least `2(u-v)^2`. Boundary/trivial cases follow by limits or zero TV. The laws here have a finite common positive support. Thus their TV is at most 1/4.

For any common randomized test, integrate its independent seed to obtain a plus-output probability `varphi(H) in [0,1]`. Its two errors obey

    P_+(error)+P_-(error)
       =1-sum_H (P_+(H)-P_-(H))varphi(H)>=1-TV(P_+,P_-)>=3/4.              (17)

The first inequality follows by summing only the positive differences, whose sum is TV. Under the uniform cube prior, fix all other bits and pair the two values of the tested bit; there are `2^(|I|-1)` pairs. Divide their summed errors by `2^|I|` to get conditional prior-average error at least 3/8. By Lemma 5 the same prior is valid given G,T=s. This is one prior for all endpoints and bits, not an endpoint-dependent prior.

**Proof: actual changed target.** On G, the target at the actual T=s is

    theta_sigma(s)=beta delta_0+delta q_sigma(.|s),
    theta_sigma(s)(w_(2h-1))-theta_sigma(s)(w_(2h))
       =2delta alpha sigma_(s,h)/m.                                       (18)

From `p_hat=B(H,R)` decode plus when `p_hat(w_(2h-1))>=p_hat(w_(2h))`, otherwise minus; ties go to plus. On an error the coordinate-contrast error is at least `2delta alpha/m`. The triangle inequality gives half-L1 loss on that coordinate pair at least `delta alpha/m` times the error indicator. A negative truth with a predicted tie is an error and obeys this inequality; a positive truth with a tie is not counted. Disjoint W pairs can be summed, and all other coordinates add nonnegative loss. Therefore, ON G,

    TV(p_hat,theta_sigma(Y_M))
       >=(delta alpha/m) sum_(h=1)^r 1{decoded sign differs from sigma_(T,h)}. (19)

For fixed s,h the predictor composed with `Rec_(K,M)(.,s)` is a common test of the complete conditional data. Apply (17), average the same prior and the actual endpoint weights m^-2, and obtain

    average_sigma E[loss | G]
       >=(delta alpha/m)(1/m^2) sum_(s in U x V) sum_(h=1)^r 3/8
       =3delta alpha r/(8m)>=delta alpha/8.                                (20)

Here r/m>=1/3: it is 1/2 for even m and `(m-1)/(2m)>=1/3` for odd m>=3. Multiplying by common `P_sigma(G)=delta^H_M` and retaining nonnegative loss off G proves (SC). The extra delta in (18) is essential; this is not an unchanged-target application of MM5. Lemma 3 puts every family source in D_K(2,beta). For any fixed B its class supremum is at least its finite-family maximum, at least its prior average; only then take infimum over B. No single sign is alleged hard for every algorithm.

**Proof: exact family upper.** On G, (18) has exactly delta mass away from 0, so its TV distance from delta_0 is delta. Off G, Lemma 5 proves the actual target is already delta_0. Thus the constant predictor has pathwise loss `delta 1_G` and expected risk `delta^(H_M+1)` for each sign, without knowing sigma, mu or pi. It may be used as a family-only upper because it is a common valid predictor; no supremum over the full class has been controlled by this calculation. ∎

### unit_007: Proposition 7 — Exact vulnerable count and finite K^4 amplitude (`prop:s015-count`)

**Statement.** Under Section 1, Lemma 1 and Invariant 2, with H_M defined in Lemma 5, let `M=qL+d` and `k=(2-d) mod L`. With

    r_M=sum_(j=0)^(d-1) 1{(k+j) mod L in V_phase},

(empty sum zero), the count in (15) satisfies

    H_M=q(m+1)+r_M,
    |H_M-M(m+1)/L|<=L.                                                    (21)

The amplitude satisfies (AMP) for every finite K>=13,M>=1. Hence the lower in (SC) is also at least `2^-12 delta^(H_M+1) min(1,sqrt(K^4/(M+1)))`, with H_M retained exactly.

**Proof: count.** Starting at any phase, each length-L block visits each residue exactly once. Invariant 2 counts m+1 vulnerable phases per such block. Decompose the M steps into q full blocks then d steps; the d-step suffix starts again at phase k, so its vulnerable count is exactly r_M above. Since `0<=r_M<=d`, and `0< (m+1)/L <=1`,

    |r_M-d(m+1)/L|<=d<=L-1<L

when d>0, and the difference is zero when d=0. This proves (21), including all residues; no random-state count is substituted for the deterministic coin set. The error is used only in the later asymptotic specialization, not hidden in the finite exponential.

**Proof: finite amplitude.** Write `K-1=4m+e`, `0<=e<=3`. Then `m=(K-1-e)/4>=(K-4)/4>=K/8` since K>=13. Let `t=sqrt(m^3/(q+1))` and `z=sqrt(K^4/(M+1))`. Directly from alpha,

    alpha/8=min{1/16,t/64}>=(1/64)min{1,t}.                                (22)

If q=0, m>=3 gives `m^3>=27>16`, hence alpha=1/2 and alpha/8=1/16, which is at least `2^-12 min(1,z)`.

If q>=1, then `q+1<=2q<=M/m`, because q=floor(M/(2m)). Thus

    t^2>=m^4/M>=K^4/[8^4(M+1)]=z^2/64^2.                                 (23)

For z<=1, either t>=1 or t<1, and in both cases `min(1,t)>=z/64`; for z>=1, t>=1/64 implies `min(1,t)>=1/64`. Therefore `min(1,t)>=(1/64)min(1,z)`. Combining with (22) gives `alpha/8>=1/4096 min(1,z)=2^-12 min(1,z)`. This proves every finite cap and small-horizon case. The exponent K^4 arises from m^3 information scale times period 2m; it is not MM5's stronger unrestricted K^5 baseline. ∎

### unit_008: Proposition 8 — Matched common-minimax logarithmic window (`prop:s015-window`)

**Statement.** Under the unchanged class and common-algorithm experiment, let integers K tend to infinity with `M=K^4,beta=(log K)/(4K^4)`. Then

    alpha ->1/(64sqrt(2)),
    delta^(H_M+1)/K^-1/8 ->1,
    [delta^(H_M+1)alpha/8]/K^-1/8 ->1/(512sqrt(2)).                         (24)

Together with the accepted full-class upper (3),

    1/(512sqrt(2)) <= liminf_(K->infinity) K^(1/8) R_D2
                   <= limsup_(K->infinity) K^(1/8) R_D2 <=1.               (25)

In particular `R_D2=Theta(K^-1/8)` on this sequence. Formula (25) bounds liminf/limsup; it does not assert a limiting exact minimax constant. Original full-history add-one has no matching upper from this argument; its certificate U_+ is eventually one.

**Proof: admissibility and amplitude.** Every integer K>=13 has M>=1 and `0<beta<1`: for K>1, `log K<K` gives beta<1/(4K^3)<1. Since `m/K->1/4`, `L/K->1/2`. The error in a floor is less than one, so

    q/K^3=[floor(K^4/(2m))]/K^3 ->2,
    m^3/(q+1)=(m/K)^3/[q/K^3+K^-3] ->1/128.

Consequently the square-root amplitude tends to `(1/8)/sqrt(128)=1/(64sqrt(2))`, strictly below 1/2; the minimum defining alpha has that limit.

**Proof: survival with explicit beta error.** By Proposition 7 write

    H_M=M(m+1)/(2m)+e_M=M/2+M/(2m)+e_M,       |e_M|<=L.                   (26)

For `0<=x<1`, integration yields

    0<=-log(1-x)-x=integral_0^x t/(1-t) dt<=x^2/[2(1-x)].                 (27)

Using `H_M<=M`, (26), beta M=(log K)/4 and (27),

    |log(delta^(H_M+1))+(log K)/8|
       <=(log K)/(8m)+beta(L+1)+(M+1)beta^2/(2delta).                     (28)

Indeed the linear term's difference from `(log K)/8` is `(log K)/(8m)+beta(e_M+1)`, and the logarithmic remainder costs at most `(H_M+1)beta^2/(2delta)`. Each displayed bound is finite and source-independent. Since m>=K/8 and L<=K/2, its first term is at most `(log K)/K`, its second at most `(log K)(K/2+1)/(4K^4)`, and its third tends to zero as a constant times `(log K)^2/K^4`, with delta tending to one. Thus the right side tends to zero. Exponentiating proves the middle limit in (24); the amplitude limit proves the third. No O(L) term has been discarded inside a finite-horizon theorem.

**Proof: exact accepted upper interface and matching choice.** S011 applies to this identical class and provides `R_D2<=U`. S012 Proposition 9 proves `U/K^-1/8->1`; the following short scalar check restates why it is an optimized common bound, not just one arbitrary burn.

For every suffix length `ell=M-b`, `1<=ell<=M`, we have `ell+1<=K^4+1<K^5`, so `u_g(ell)=1`. Each `h_b>=h_(M-1)`. Since `0<h_b<=1`, every suffix candidate in (3) is at least `h_b>=h_(M-1)`. Formula (27) with `floor((M-1)/2)=M/2+O(1)` yields

    |log(h_(M-1))+(log K)/8|<=beta+M beta^2/(4delta) ->0.                 (29)

For an upper take public `ell_*=floor(K^(7/2))`, `b_*=M-ell_*`, an allowed choice with `1<=ell_*<=M`. Its stationary term is at most `48K^-1/4`, and

    |log(h_(b_*))+(log K)/8|
       <=beta(ell_*/2+1)+M beta^2/(4delta) ->0,                           (30)

because `beta ell_*<=(log K)/(4sqrt(K))->0`. Hence the suffix candidate at b_* is `K^-1/8(1+o(1))+48K^-1/4`. Dividing the last additive term by K^-1/8 gives `48K^-1/8->0`. Equations (29)–(30) sandwich the optimized `U_suf/K^-1/8` between quantities tending to one.

For all b, the original penalty is at least

    13sqrt(K)h_(M-1)^(3/4)=13K^(13/32)(1+o(1)) ->infinity.

Thus every original capped candidate is one eventually, uniformly over b, and u_g(M)=1; hence U_+=1. Also U_pool=1 eventually since 2delta>1. The suffix bound tends to zero, so U=U_suf eventually. This rechecks the inherited ratio-one certificate on the exact parameter sequence without changing its algorithm assignment.

Finally Proposition 6's lower holds for every common B and thus for R_D2. Combining it with `R_D2<=U` and (24) proves (25). For explicit order constants, the two proven certificate limits imply that for all sufficiently large K the lower is at least `[1/(1024sqrt(2))]K^-1/8` and U is at most `2K^-1/8`; these are absolute constants. Their eventual validity follows from the quantitative errors (28)–(30) and the displayed amplitude ratio, not from absorbing an uncontrolled source-dependent term.

The new construction allows safe zero outputs and only m+1 harmful opportunities per 2m phases. S012's distinct all-nonzero base has every observed phase vulnerable and exact family risk delta^(M+1), of order K^-1/4 here. Those two family upper bounds concern different source sets and are compatible. Nothing here changes S012 or claims a matching original-add-one risk. ∎

### unit_009: Proposition 9 — Same-witness aggregate refresh and total-bound negations (`prop:s015-after`)

**Statement.** Under Lemmas 1, 3–5, Invariant 2 and Proposition 6, the stationary symbol marginal of the family is `p=delta_0`, and (8) is the canonical decomposition `theta_sigma(s)=beta p+delta Q_sigma(s)` on every row. For its independent canonical coins and `C_ref={some J_j=1, 0<=j<M}`, inequality (AFTER) holds for EVERY common randomized predictor. The constant delta_0 predictor has exact after-refresh contribution

    E[loss 1_(C_ref)]=delta^(H_M+1)-delta^(M+1)                             (31)

for each sign. Along Proposition 8's logarithmic sequence the right side of (AFTER), divided by K^-1/8, tends to `1/(512sqrt(2))`. This rules out both of the proposed universal upper expressions stated at the start.

**Proof: canonical rows and event law.** Lemma 3 gives pi=delta00, so either stationary symbol marginal is delta_0. Equation (8) on active rows and Q_sigma=delta_0 on every default row prove the canonical decomposition on ALL rows, including safe rows. Its Bernoulli coin implementation is exactly the construction in Lemma 5, not a different reset mechanism. The auxiliary refresh labels are not exposed to the algorithm.

The event of all M coins being zero is a subset of G, with probability delta^M. Therefore

    P_sigma(G intersect C_ref)=delta^H_M-delta^M.                          (32)

If H_M=M, this event is null and (AFTER) has zero right side, which follows from nonnegative loss without conditioning on a null event. If H_M<M, since 0<delta<1, (32)>0. On G, vulnerable coins are zero, so G intersect C_ref means at least one SAFE coin is one. The full base history equality proved in Lemma 5 holds regardless of every safe-coin value. The event depends only on independent coins, not initial or base random variables; hence conditioning on G intersect C_ref leaves the ENTIRE history law (14) unchanged. In particular, for all s and signs,

    P_sigma(G intersect C_ref,T=s)=(delta^H_M-delta^M)/m^2.                (33)

The conditional sign prior is common and uniform, and the predictor seed unchanged. The conditional information/test proof in Proposition 6 applies without modification because the full law and the NEW target (18) are exactly the same. Its conditional prior-average loss is at least delta alpha/8. Multiply by (32), then discard the nonnegative contribution from C_ref outside G to obtain (AFTER). It holds also in the null case already separated.

For B_0, Proposition 6 gave pathwise loss `delta 1_G`. Multiplying by `1_(C_ref)` and taking expectation gives exactly `delta(delta^H_M-delta^M)`, proving (31). This statement is about a latent-event contribution to actual loss in the fixed canonical implementation; it is not a conditional-prediction target or a claim that the event is observable.

**Proof: asymptotic negative consequences.** Along the logarithmic sequence, (27) gives

    |log(delta^(M+1))+(log K)/4|
       <=beta+(M+1)beta^2/(2delta) ->0,
    delta^(M+1)=K^-1/4(1+o(1)).                                           (34)

By (24), `delta^(H_M+1)=K^-1/8(1+o(1))`, so the ratio of the second term in (31) to the first is `K^-1/8(1+o(1))->0`. Equations (24),(34) and the alpha limit prove the claimed lower-certificate asymptotic for (AFTER). In particular safe refreshes, although changing no emitted symbol, occur often enough to retain almost all of this hard-experiment contribution inside C_ref.

Now set `a=min(1,sqrt(K^3/(M+1)))` and `g=min(1,sqrt(K^5/(M+1)))`. On this sequence,

    a=K^-1/2(1+o(1)),       g=1,
    sqrt(beta)=(sqrt(log K))/(2K^2)=o(K^-1/2),
    delta^M=K^-1/4(1+o(1)).                                               (35)

Suppose there were a universal finite C_0 and common predictors (which may vary with public parameters) such that every admitted source's canonical aggregate contribution obeyed `E[loss 1_(C_ref)]<=C_0(a+sqrt(beta))`. Averaging that same bound over our finite family would keep the upper. But (AFTER) says the average is at least `[1/(512sqrt(2))+o(1)]K^-1/8`, whose ratio to `a+sqrt(beta)` grows as `[1/(512sqrt(2))+o(1)]K^(3/8)`. This contradicts every fixed finite C_0. Equivalently, for each common algorithm and sufficiently large parameters there is a sign violating that uniform upper. This applies in particular to unchanged original add-one, but is an all-common-algorithm obstruction.

Similarly, by (35),

    a+delta^M g+sqrt(beta)=K^-1/4(1+o(1)).                                 (36)

If any common predictor family had full-class total risk bounded by a universal constant times (36), or if the minimax risk admitted such an upper, Proposition 6 would contradict it: the lower/putative-upper ratio grows as `[1/(512sqrt(2))+o(1)]K^(1/8)`. Thus the specified total O-expression is false. These are negations of two exact proposed bounds, not an impossibility of all upper-bound methods, not a third research route, and not a full joint-rate formula. ∎

## 4. Target-step assembly

Lemma 1 (`lem:s015-star`) constructs the full lawful star table, and Invariant 2 (`inv:s015-phase`) proves both the period geometry and the exact harmful/safe classification, including L=6. Lemma 3 (`lem:s015-member`) uses that classification in the legal two-step product, covering every starting row rather than just the sampled support. Lemma 4 (`lem:s015-history`) proves the all-residue initial law and full-history bijection. Lemma 5 (`lem:s015-event`) proves the positive common conditioning event and terminal target off it. These generated facts jointly justify Proposition 6 (`prop:s015-lower`): full conditional information and changed W contrasts yield the unconditional finite-family/class lower, and first-failure absorption yields the separate exact family upper.

Proposition 7 (`prop:s015-count`) proves the exact count and all finite amplitude constants without modifying the exponential. Proposition 8 (`prop:s015-window`) supplies the controlled public specialization bridge and combines ONLY with the accepted S011/S012 common upper to match the specified minimax sequence. Proposition 9 (`prop:s015-after`) restricts the same experiment to a canonical refresh event and proves the two requested negative corollaries. No assertion in the planning diagnostic is used as evidence, and S014 is not a premise.

## 5. Explicit rate, scope and assumption audit

- **Exposed domain:** integer K>=13,M>=1 and public real 0<beta<1. All construction quantities m,L,q,d,k,r,alpha,H_M are deterministic explicit functions of the public parameters. Beta endpoints are outside the conditional proof. The accepted full arbitrary-start K^5 baseline at beta zero and IID baseline at beta one remain valid independently; no weaker star-witness replacement is asserted.
- **Probability/norm/horizon:** fixed-horizon expected half-L1 TV at the SAME trajectory's actual terminal row; M departures and ALL M+2 symbols are retained. Conditional experiments are proof tools with exact common positive probabilities. Aggregate (AFTER) is an unconditional indicator-weighted contribution, not a conditional loss divided by P(C_ref). No independent query, discarded-data lower, squared-TV loss, predictive KL objective, stopping time or high-probability upgrade is used.
- **Constants and limits:** 1/8 in testing and 2^-12 in the finite amplitude are proved here; 48,13 and certificate U are inherited through accepted S011. In (24)–(36) only K varies with exact M,beta as stated. All constants and error bounds are numerical and independent of source, signs, algorithm, mu, pi, K,M,beta. No parameter-dependent exponential constant is hidden in a finite bound.
- **Term bridges:** the two amplitude branches, q=0/q>=1, cap comparisons and m>=K/8 are explicit. Count error is retained in (28). The extra phase charge `(log K)/(8m)` and quadratic log remainder both tend to zero by displayed estimates. Suffix selection is public and admissible; its `48K^-1/4` term divided by K^-1/8 vanishes explicitly. The negative-bound comparisons use the exact polynomial ratios in (35)–(36).
- **Primitive versus derived:** normalized legal homogeneity, arbitrary mu, all-pair class definition and common information are primitive. New table normalization, phase support, safe output, default successor, stationary witness, coefficient, complete likelihood, event independence, prior preservation and conditional test law are conclusions of named local results. The lower does not assume generated-event correctness. All conditioning on G is legal since delta>0; G intersect C_ref is conditioned on only when H_M<M.
- **Algorithm/family distinctions:** lower claims hold before infimum for every common randomized full-history kernel. B_0 is common but its exact risk is only on the constructed finite family. The full-class upper U belongs to a public selector of distinct rules. No suffix upper is assigned to original full-history add-one, whose current certificate remains one in the matched window.
- **Remaining scope:** the full arbitrary-start joint `(K,M,beta)` minimax rate remains unresolved outside accepted matched regimes. No novelty, literature priority, formal verification, network implementation, resource/fault result, positive-support replacement, general-q result or hidden-parameter adaptivity claim is made. S012's old-family limitation is preserved and legitimately bypassed by different sources; S013/S014 supply no premise.

## 6. Notation surface and actual read/action record

Public-facing objects are the unchanged class/risk, finite lower (SC), finite amplitude (AMP), exact count formula, specified-window minimax order and precisely quantified negative corollaries. The upper certificates U/U_+/U_suf/U_pool retain their accepted meanings. The construction alphabet blocks, cyclic word, pair phases, sign cube, rows Q_sigma/q_sigma, r,d,k, labeled triples, reconstruction Rec, coin variables, events G/C_ref and decoded tests are proof-local; they are never additional inputs or hidden advice to B. H is the observed history; H_M is the deterministic count, not its length or a stopping variable. D_t denotes a phase set, whereas E_i denotes a labeled training triple. V is the symbol block, while V_phase is the set of vulnerable residues. C is the peripheral symbol block, while C_ref is the refresh event. No alias is used in place of a proof of a property.

## 8. Supplementary finite checks

An inline producer-owned Python command completed all of the following; no separate checker file was written. These tests corroborate, not replace, the preceding all-parameter proofs.

1. **31,112 exact full-row checks**, using `fractions.Fraction`: m=3,...,8, every K=4m+1,...,4m+4, beta in {1/5,1/2}. The script formed the explicit star word and full table, checked disjoint phases, normalization, every base successor phase, safe/vulnerable outputs, all-start two-step mass at 00 at least beta, and equality plus genuinely default successors for vulnerable rows.
2. **32 exact full augmented-history experiments**, m=3 with M=1,...,17 and m=4 with M=1,...,15, beta=1/5 and rational alpha=1/2 with mixed signs. The structural/probability identities hold for any positive alpha<=1/2, independently of the prescribed testing amplitude. A forward recursion branched each departure over its Bernoulli coin and Q-row symbol, merging by `(complete history, G indicator, C_ref indicator)`. It inspected **127,207 augmented atoms** and **49,173 base histories**. It checked normalization, every-residue endpoint/label count, extraction/reconstruction of every observed symbol, exact path factors (14), exact G and G-intersect-C_ref masses, full-law proportionality on both events, zero constant-predictor loss off G, and the exact total/aggregate family risks. Both initial fixed-W cases, M=1,2, q=0 and multiple cycles were included.
3. **40,376 exact integer count/visit cases**, m=3,...,100 and every M=1,...,4L: terminal phase 2, exact UV visits and observed q labels, exact block/partial H_M formula and count error bound.
4. **9,880 scalar probes**, K=13,...,1000 at horizons from {1,2,L-1,L,L+1,2L-1,2L,K^3,K^4,K^6}: both testing-amplitude cap inequalities and finite 2^-12 K^4 amplitude comparison. These square-root probes alone used ordinary floating arithmetic with tolerance 1e-15.

All checks passed. No check is represented as infinite-parameter certification, formal verification, a new mathematical premise, or an independent review.
