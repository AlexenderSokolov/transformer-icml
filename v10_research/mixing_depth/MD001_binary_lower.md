# MD001 binary depth-uniform lower lemma

2026-11-02. New author component; no independent acceptance is implied. All accepted sources and freezes remain unchanged.

## 1. Uniform model and statement

Use exactly GD001 lower §1's fixed per-stage primitive budgets, fixed output dimension D, fixed historical local radius r, fixed boundary-symbol budget b0, and public dense causal masks. Set K=2. This change of alphabet does not change its deterministic influence proof: that proof uses diameters and Lipschitz constants, not K>=3; K>=3 was needed only by its source witness. Initial synthetic terminal state depends only on public data and the frozen boundary label, including EVERY terminal local-window symbol. Historical local tables are below the terminal row. All frozen branches satisfy the ideal contracts on all formal histories. Every primitive is counted; no growing per-layer DAG is hidden.

Let Γ_l>=1 be GD001 §1's late-coordinate influence bound, with Γ_l<=C^l for a fixed C>=2, l>=1. Thus replacing any one source symbol at index i>=(M+3)/2 changes any terminal ideal coordinate by at most Γ_l/M. This already includes all r affected local-table states. The finite evaluator has pre-cut error <=E/Q uniformly in l and every formal history, where E is FIXED; GD001 uniform FA supplies E=1 at paid precision P=4h+c(l+2), increasing P further if needed. Rounding itself is not assumed Lipschitz. Decoder sees only the Q-grid bank, boundary S, and source-independent public metadata/randomness.

Write e=max(sqrt(β),1/M), z=Γ_l Q, H_b=2^b0. Define constants

    τ=34 sqrt(32 D H_b),
    N_box=ceil(2τ+2E+4)+1,
    A_B=36 H_b N_box^D,
    c_B=1/(524288 A_B).

For M>=64, β<=1/256 and 1<=z<=M/4, the stationary minimax risk satisfies

    R_stat >= (c_B/z) ln(1+min{z/(M e),M/z}/8).       (BL1)

All constants are independent of depth l, Γ_l, M, β and Q. Consequently they are independent of compander gain γ, which is a distinct upper-construction parameter. The statement also lower-bounds arbitrary-start minimax risk, by inclusion of stationary starts.

## 2. Binary stationary witness and reference path domination

Use the exact accepted BI001 v2 witness. With pair states W=00,A=01,B=10,C=11, a=1/(2M), p in I=[1/4,3/4], set

    θ_W(1)=a, θ_A(1)=p, θ_B(1)=1-e, θ_C(1)=1/2,
    x=(e/a+2+2p)^(-1), Π=(xe/a,x,x,2px).

BI001 §1 verifies ΠP=Π, Π_W>=1/4, and the all-state certificate P²>=βΠ, using e²>=β and e<=1/16. It is initialized at its own Π, not at a deterministic zero prefix.

Put U=min{1/(4e),M²/(4z²)} and J=floor U. Then U>=4, J>=4, J>=U/2, J<=M/4, eJ<=1/4, and z sqrt(J)/M<=1/2. For 4<=j<=J consider disjoint events E_j with N-j initial zeros, N=M+2, followed by an initial 1 and j-1 transitions of the active chain

    R_p=[[0,1-p,p],[1,0,0],[0,1/2,1/2]]

on A,B,C, starting at A. Its reference law is ν_pj. Actual path mass relative to ν_pj is

    Π_W(1-a)^(M-j) a (1-e)^(N_B) >=1/(32M),

where N_B<=j-1 counts transitions from B. This is pointwise path-measure domination. E_j probability depends on p, so no posterior-uniformity or conditional-IID assertion is made. The SAME uniform prior over I is used for every j. Every random suffix symbol is in the late half. The actual next-symbol law at terminal A is Bernoulli(p).

## 3. Coupling transfers late influence to nonlinear-output concentration

Fix any boundary label s and output coordinate f_s. Freeze s before sampling the reference chain, without conditioning on boundary consistency. Since R_p²(u,B)>=1/8 for every u,p, couple two active chains in two-step blocks using their common (1/8)δ_B atom. Once they meet, use identical future transitions; fill intervening steps by conditional bridges. Expected differing states, counting the initial state, are at most 2 sum_{k>=0}(7/8)^k=16. Emitted-bit disagreements are bounded by state disagreements.

For any two resulting continuations with the same prefix, telescope single-symbol replacements in the complete formal histories. Each disagreement costs at most Γ_l/M. Hence their expected f_s difference is at most 16Γ_l/M, and certainly at most 34Γ_l/M. No extra r is inserted, since Γ_l already counts local preprocessing. Intermediate hybrid histories need not be valid Markov paths; the all-formal-history contract makes telescoping legitimate.

Reveal the j-1 reference transitions. Conditional continuation expectations after any two next states differ by at most 34Γ_l/M, giving Doob conditional range at most that value. Orthogonality, and the safe range-square variance bound, yield

    Var_ν(f_s) <=34² Γ_l² j/M².                    (BL2)

Differentiate the finite reference path-probability polynomial in p. Each insertion of R'_p is zero except row A, whose B,C entries are -1,+1. The difference of continuation expectations is bounded by 34Γ_l/M, and prefix probabilities sum to one. Summing j-1 insertions gives

    |d E_ν(f_s)/dp| <=34 Γ_l j/M.                  (BL3)

These are statements about the IDEAL nonlinear output, not derivatives of the discontinuous finite evaluator. They are the BC001 §§2–3 argument with GD001's uniform late influence, not its old depth-dependent global square-sum constant.

## 4. Rescaled tube with a depth-independent alphabet

Chebyshev and union over D H_b coordinates/branches imply that with probability >=31/32 every coordinate satisfies

    |f_s-E_ν f_s| <=τ Γ_l sqrt(j)/M.

Choose a mesh in I with spacing <=M/(34zj). At most 2+17zj/M <=36(1+zj/M) centers suffice per branch. BL3 puts each scaled mean Q E_ν f_s within one of its branch's scaled mesh centers in maximum norm. Since z sqrt(j)/M<=1/2, concentration costs <=τ/2 in scaled coordinates, finite approximation costs E, and downward floor costs <1. Thus every good integer grid bank is in a box of radius τ/2+E+2 about a mesh center. N_box bounds the number of integer possibilities in EACH coordinate: its defining length 2τ+2E+4 safely exceeds twice that radius. The complete good-message alphabet, including actual S and granted j, therefore has at most

    R_j=A_B(1+zj/M)

labels, independent of p. Crucially A_B has NO l- or Γ_l-dependence. Source-independent seeds may be granted, then fixed throughout this argument, with the same constants and prior.

## 5. Terminal-A finite-message lemma and harmonic summation

BI001's direct computation R_p³(u,A)>=1/8 gives ν_pj(terminal A)>=1/8 for j>=4. Together with the good-event probability, ν_pj(good and terminal A)>=3/32 for every p. Fix the decoder seed. Around its at most R_j predictions of symbol1 on good messages put intervals of radius |I|/(64R_j). Their union has uniform-prior probability <=1/32. Integrating over p, good-and-terminal-A paths outside those intervals have probability >=1/16. Their true next-symbol parameter is p; binary TV is absolute parameter error. Therefore

    E_prior,ν[loss 1_terminalA] >=1/(2048R_j).

Average seeds, apply pathwise domination, and sum the disjoint E_j:

    R_stat >=[1/(65536 A_B M)] sum_{j=4}^J (1+zj/M)^(-1).

For u=z/M<=1/4 and j=k+4, 1+u(k+4)<=2(1+uk). The decreasing-function integral over k from 0 to J-3 and J-3>=J/4 give

    sum_{j=4}^J (1+uj)^(-1)
       >=ln(1+u(J-3))/(2u)>=ln(1+uJ)/(8u).

Since uJ>=min{z/(Me),M/z}/8, this proves BL1, including J=4. Decoder outputs can be arbitrary real simplex vectors.

## 6. Fixed-square-root-band necessity

Fix 0<c_-<=c_+, target multiplier C_risk>0, and legal Q in [c_-sqrt(M),c_+sqrt(M)]. Put f=1+ln(1+Q/(Me)). Every procedure with R<=C_risk/sqrt(M) has

    Γ_l >=c_* f,                                      (BL4)

where c_*>0 depends only on fixed architecture bounds, c_+, E, C_risk. Here is a complete finite-domain argument; no uniform growing-depth 1/Q floor is used.

Choose F>=2(1+ln8), F>=1, sufficiently large that for all t>=F,

    (exp(t-1)-1)/(8c_+²t)>=exp(t/2)-1.

Such F exists by exponential domination. If β>1/256, e>=1/16, so f<=1+16Q/M<=1+2c_+ and Γ_l>=f/(1+2c_+). If β<=1/256 but z>M/4, Γ_l>sqrt(M)/(4c_+), while f<=1+Q<=(1/8+c_+)sqrt(M), so Γ_l>=f/[4c_+(1/8+c_+)]. These branches do not use BL1 outside its domain.

In the remaining domain BL1 applies. If f<=F then Γ_l>=f/F; if Γ_l>=f the result is immediate. Otherwise f>F and 1<=Γ_l<f. Write x=Q/(Me)=exp(f-1)-1. First,

    ln(1+Γ_l x/8)>=f-1-ln8>=f/2.

Also e>=1/M implies x<=Q, and Q²/M<=c_+² implies

    M/(Γ_l Q)>=x/(Γ_l c_+²)>x/(f c_+²).

The choice of F gives ln(1+M/(8Γ_l Q))>=f/2. BL1 and the target risk imply Γ_l>=c_B f/(2c_+ C_risk). Thus one may take the minimum of these four case constants and 1 for c_*.

Since Γ_l<=C^l, this gives l>=ln(c_* f)/ln C. For l>=1 this is equivalently a uniform lower l>=c_depth(1+ln f): on large f use the logarithmic bound, and on its remaining bounded range use l>=1. This concerns actual primitive depth, not PURE Boolean expansion depth. If a convention permits depth zero, use 1+l throughout. Stationary subclass inclusion gives the identical necessity for guarantees over all initializations. Sufficiency is a separate upper construction, not asserted by this component.

## Provenance and limits

Read GD001 lower derivation and uniform FA extension with root receipt 2026-11-02 06:55:04 UTC; BI001 v2 with root receipt 05:52:32 UTC; BC001 §§1–4 with root receipt 06:20:02 UTC. BL1 is the new depth-rescaled synthesis of accepted source and coupling arguments, requiring fresh independent review. This note claims no all-Q depth frontier, no depth-uniform grid-floor lower, no arbitrary internally rounded-network theorem, no uncharged exact side information, and no publication or external novelty.
