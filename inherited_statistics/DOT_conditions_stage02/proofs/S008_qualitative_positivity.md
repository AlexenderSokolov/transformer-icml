# S008 定性正性不改变精确最坏风险

科学正文摘录。以下保留已接纳版本的数学文字与原有编号，不重写证明；仅省略提交身份、流程元数据和历史状态。来源与依赖见 `../SOURCES.md`，逐字节映射见 `../COPY_MAP.json`。本次编排不是新的独立数学审查。

编排补充引用（非原文）：§8 的 MM5/L1MAX 接口见本包 `../SOURCES.md` 与 `../inherited/` 的对应科学正文；原内部记录路径已省略。

## 1. Result, experiment, and precise quantifiers

Fix finite integers K≥2 and M≥1. Write A={0,…,K−1}, S=A², and let
θ=(θ_ab(c)) be a homogeneous second-order symbol-transition table. Each row
is a probability law on A; zeros are allowed in the full class. Its legal
pair-shift kernel is

    Pθ((a,b),(b,c))=θ_ab(c),

with zero entries for non-shift transitions. Starting from the pair law μ,
observe the **entire** history H=(X₁,…,X_{M+2}), equivalently the entire pair
path (Y₀,…,Y_M), where Y_i=(X_{i+1},X_{i+2}). These two observed objects
determine each other bijectively on legal paths. No initial pair or other
observed side information is dropped. The unobserved next-symbol target is
θ_{Y_M}, at the actual same-trajectory endpoint.

A common randomized predictor is an arbitrary kernel A_H(dp) from the finite
history space into the probability simplex Δ_K. It may depend on public K,M
and use randomness independent of the source and observations, but cannot
read θ, μ, any stationary law, or the future. Put

    r_A(θ,μ)=E_{θ,μ} ∫ TV(p,θ_{Y_M}) A_H(dp).

Define four source classes:

    F_K = {(θ,μ): θ any legal table, μ any pair probability law},
    F_K,pos = {(θ,μ)∈F_K: θ_ab(c)>0 for every a,b,c},
    S_K = {(θ,π): πPθ=π},
    S_K,pos = {(θ,π)∈S_K: θ_ab(c)>0 for every a,b,c}.

The full stationary class permits zero-mass states, reducibility, multiple
closed classes and arbitrary stationary mixtures, and periodicity. The
strict-positivity condition is only on **legal symbol transitions**: the
pair matrix Pθ itself still has structural zeros. There is no prescribed
common positive lower bound on θ_ab(c), and no mixing parameter is supplied
to A. In particular, all four comparisons use the same set of possible
source-blind history-to-output kernels.

**Theorem S008 (exact per-algorithm worst-risk equalities).** For every fixed
K,M and every such common randomized predictor A,

    sup_{(θ,μ)∈F_K,pos} r_A(θ,μ)
      = sup_{(θ,μ)∈F_K} r_A(θ,μ),                         (1.1)

and, separately,

    sup_{(θ,π)∈S_K,pos} r_A(θ,π)
      = sup_{(θ,π)∈S_K} r_A(θ,π).                         (1.2)

Consequently these equalities remain true after taking inf_A on both sides.
They also apply to the original full-history add-one predictor, without
changing the algorithm. These are equality of suprema, not assertions that
the positive subclasses contain worst-risk maximizers or that the numerical
minimax values have been evaluated in closed form.

The proof gives approximation bounds **uniform over all A**, not merely
continuity for a fixed deterministic algorithm. The two approximation
constructions are different and are not silently combined into a theorem
for classes that only require an initial law to be TV-close to a stationary
law. Section 8 records that limitation.

## 2. Full-path telescope with the correct orientation

We first prove a finite-state fact, using no stationary-law continuity
theorem. Let P,Q be kernels on any finite state space and μ,ν initial laws.
Let L_{μ,P} be the law of the complete M-transition path Z₀,…,Z_M. Define

    d(s)=TV(P(s,·),Q(s,·)).

Then

    TV(L_{μ,P},L_{ν,Q})
      ≤ TV(μ,ν)+Σ_{i=0}^{M−1} E_{μ,P} d(Z_i).             (2.1)

The expectations in (2.1) are under the **original P chain**. This
orientation matters when only its stationary-weighted row error is small.

**Proof.** For j=0,…,M, let B_j be the probability law on full paths with
initial law μ, its first j transitions from P, and its remaining M−j
transitions from Q:

    B_j(z₀,…,z_M)
      = μ(z₀) [Π_{i=0}^{j−1} P(z_i,z_{i+1})]
                [Π_{i=j}^{M−1} Q(z_i,z_{i+1})].

Thus B_M=L_{μ,P} and B₀=L_{μ,Q}. For j≥1, B_j−B_{j−1} has the factor
(P−Q)(z_{j−1},z_j), with a P prefix and a Q suffix. Summing its absolute
value over the full paths, the Q suffix sums to one. Hence

    TV(B_j,B_{j−1})
      = Σ_s (μP^{j−1})(s) TV(P(s,·),Q(s,·)).              (2.2)

This calculation does not discard any observed coordinate: every B_j is
a law on the complete path. Moreover, because the initial state is one of
those coordinates,

    TV(L_{μ,Q},L_{ν,Q})=TV(μ,ν).                          (2.3)

The triangle inequality through B_M,…,B₀ and then L_{ν,Q} proves (2.1).
Zero probabilities cause no difficulty; the proof uses products and finite
sums, never a conditional probability on a null event. ∎

For legal pair-shift kernels, the injection c↦(b,c) in each row gives

    TV(Pθ((a,b),·),Pθ′((a,b),·))
      = TV(θ_ab,θ′_ab).                                  (2.4)

Also the full pair path and full symbol history have identical TV distance
under the bijection above. Thus (2.1) controls the laws of exactly all data
seen by the algorithm, not merely their endpoints or counts.

## 3. Risk continuity including the changing endpoint target

For two tables θ,θ′ and two initialization laws μ,ν, write L,L′ for their
full history laws, and put d(s)=TV(θ_s,θ′_s). For every common randomized A,

    |r_A(θ,μ)−r_A(θ′,ν)|
      ≤ TV(L,L′)+E_{θ,μ}d(Y_M).                          (3.1)

**Proof.** Define the bounded functions on the full history space

    ℓθ(h)=∫ TV(p,θ_{y_M(h)}) A_h(dp),
    ℓθ′(h)=∫ TV(p,θ′_{y_M(h)}) A_h(dp).

Both take values in [0,1]. The reverse triangle inequality for TV, applied
for the same h and same output p, gives

    |ℓθ(h)−ℓθ′(h)|≤d(y_M(h)).

Use the exact decomposition

    E_Lℓθ−E_{L′}ℓθ′
      = E_L(ℓθ−ℓθ′)+(E_Lℓθ′−E_{L′}ℓθ′).

For any function f∈[0,1] on a finite space,
|E_Lf−E_{L′}f|≤TV(L,L′): sum the positive and negative parts of L−L′,
whose masses each equal TV(L,L′). This proves (3.1). The loss difference is
averaged under the **original** terminal law. Integrating A_h proves the
claim for arbitrary randomized kernels; no deterministic-algorithm or
seed-selection reduction is needed. ∎

This target term is essential: changing only the data law while retaining
the wrong θ-target would not prove the asserted risk comparison.

## 4. Arbitrary initialization: direct row-mixture regularization

Fix any (θ,μ)∈F_K. For 0<ε<1 let u(c)=1/K and set

    θ^ε_s=(1−ε)θ_s+εu,      μ^ε=μ.                       (4.1)

Every legal transition is at least ε/K>0, so (θ^ε,μ)∈F_K,pos. Row distances
satisfy, simultaneously for every state including states of zero original
probability,

    d_ε(s)=TV(θ_s,θ^ε_s)=ε TV(θ_s,u)≤ε.                 (4.2)

By (2.1), (2.4), and the equality of initial laws,

    TV(L_{θ,μ},L_{θ^ε,μ})≤Mε.                           (4.3)

Equation (3.1) and (4.2) therefore give

    |r_A(θ,μ)−r_A(θ^ε,μ)|≤(M+1)ε                       (4.4)

for every A, every θ, and every μ. One may cap either TV or risk difference
by one. The uncapped form is convenient for taking ε↓0 at fixed M.

No stationary law is selected in this construction. Arbitrary unknown μ,
including a deterministic initial pair or a horizon-dependent choice in
the outer supremum, is retained exactly.

## 5. Stationary initialization: regularize the stationary triple flow

Fix any (θ,π)∈S_K, where π may be any stationary mixture and may have zeros.
Define its stationary triple flow by

    T_abc=π_ab θ_ab(c).

The two relevant pair marginals are

    Σ_c T_abc=π_ab,      Σ_a T_abc=π_bc.                 (5.1)

The second identity is exactly πPθ=π. For 0<ε<1 set

    T^ε_abc=(1−ε)T_abc+ε/K³,
    π^ε_ab=(1−ε)π_ab+ε/K²,
    θ^ε_ab(c)=T^ε_abc/π^ε_ab.                           (5.2)

All denominators are strictly positive, so (5.2) is defined even at
π_ab=0. The outgoing marginal identity from (5.1) implies

    Σ_c T^ε_abc=π^ε_ab,

so each θ^ε row sums to one and every legal transition is strictly
positive. The incoming marginal identity gives

    Σ_a π^ε_ab θ^ε_ab(c)
      = Σ_a T^ε_abc
      = (1−ε)π_bc+ε/K²
      = π^ε_bc.                                        (5.3)

Thus π^ε is exactly stationary for P_{θ^ε}, not merely approximately
stationary; (θ^ε,π^ε)∈S_K,pos. This constructs the approximation to the
**selected** original stationary law π, even when θ has many such laws.
It does not rely on a uniquely selected stationary law of the original θ.

Write d_ε(s)=TV(θ_s,θ^ε_s) and

    D_ε=Σ_s π_s d_ε(s).

For every row s, including π_s=0, define

    λ_s=(ε/K²)/[(1−ε)π_s+ε/K²].

Then 0<λ_s≤1 and (5.2) can be written

    θ^ε_s=(1−λ_s)θ_s+λ_s u,
    d_ε(s)=λ_s TV(θ_s,u)≤λ_s.                           (5.4)

If π_s=0 then λ_s=1, θ^ε_s=u, and π_s d_ε(s)=0, regardless of how
different the original null-state row was. For π_s>0,

    π_s λ_s
      = (ε/K²) π_s/[(1−ε)π_s+ε/K²]
      ≤ ε/[K²(1−ε)].

There are at most K² such states. Consequently

    D_ε≤ε/(1−ε).                                       (5.5)

We use this simple sufficient bound; no claim of pointwise row convergence
at π-null states is made. Initial-law variation is also controlled:

    TV(π,π^ε)=ε TV(π,U_S)≤ε,                            (5.6)

where U_S is the uniform pair law.

Apply (2.1) with P=Pθ, Q=P_{θ^ε}, μ=π, ν=π^ε. Every original prefix
state Y_i has law π, so each original-prefix expectation in that telescope
is D_ε. Therefore, for the laws of the **full observed histories**,

    TV(L_{θ,π},L_{θ^ε,π^ε})≤ε+M D_ε.                  (5.7)

Under the original experiment the actual endpoint Y_M also has law π;
hence its expected target-row variation is exactly D_ε. Equation (3.1)
now yields, uniformly over all A,

    |r_A(θ,π)−r_A(θ^ε,π^ε)|
      ≤ ε+(M+1)D_ε
      ≤ ε+(M+1)ε/(1−ε).                                (5.8)

Both the data-law comparison and target comparison use original π weights.
There is no substitution of perturbed occupation weights into (5.5), no
division by π_s at a zero-mass state, and no claim that the full table
θ^ε converges uniformly by rows to θ. These distinctions are why this
stationary construction works for reducible sources and stationary mixtures.

## 6. Suprema first, then infimum; exact add-one consequences

Fix A,K,M. Denote the positive-class supremum in (1.1) by W_A,pos.
For any full-class source (θ,μ), (4.4) gives, for every 0<ε<1,

    r_A(θ,μ)≤r_A(θ^ε,μ)+(M+1)ε
               ≤W_A,pos+(M+1)ε.

Let ε↓0, then take the supremum over (θ,μ)∈F_K. This proves the full-class
supremum is at most W_A,pos. The reverse inequality follows from
F_K,pos⊆F_K. Thus (1.1) holds, without requiring any supremum to be attained.

Exactly the same argument, with (5.8) and ε↓0 at fixed M, proves (1.2).
Both constructions are legitimate fixed homogeneous sources within each
experiment. In the outer finite-horizon supremum the approximation
parameter may be chosen arbitrarily small, potentially depending on K,M,A
or the desired risk tolerance; it is never changed along a trajectory.
There is no assertion that one fixed ε gives a vanishing bound as M→∞.

Since the equalities hold for **every** element of the common predictor
space, taking inf_A gives

    R_min,pos(K,M)=R_min(K,M),
    R_stat,pos(K,M)=R_stat(K,M).                         (6.1)

This is not an exchange of infimum and supremum or of an infimum and a
limit. We first establish pointwise equality of the two functions of A,
and then take their infima. Allowing knowledge of the qualitative class
label introduces no extra observations and does not alter the set of
possible kernels A_H. Unknown π remains unknown on both sides.

The original add-one predictor has, for s∈S,

    C_s(c)=Σ_{i=0}^{M−1}1{Y_i=s,X_{i+3}=c},
    n_s=Σ_c C_s(c),      p⁺_s(c)=(C_s(c)+1)/(n_s+K),

and predicts p⁺_{Y_M}. It is one of the common predictors above, so

    R_addone,pos(K,M)=R_addone(K,M),
    R⁺_stat,pos(K,M)=R⁺_stat(K,M).                       (6.2)

No suffix estimator, burn-in, independent test query, or squared-TV loss
is used anywhere in these identities.

## 7. Positivity really implies unique mixing — but only source by source

For a table with every legal θ_ab(c)>0, let

    m_θ=min_{a,b,c} θ_ab(c)>0.

For any initial pair (a,b) and target pair (c,d), there is exactly one
two-step legal path, through (b,c), and therefore

    Pθ²((a,b),(c,d))=θ_ab(c)θ_bc(d)≥m_θ²>0.            (7.1)

Thus Pθ is irreducible. Also Pθ²(s,s)>0, and
Pθ³(s,s)=Σ_t Pθ(s,t)Pθ²(t,s)>0, since every Pθ row has positive total mass.
Return lengths 2 and 3 have greatest common divisor one; the chain is
aperiodic. Structural one-step zeros have not been removed or mistaken for
a failure of positivity of legal transitions.

For completeness, put δ_θ=K²m_θ²∈(0,1]. Equation (7.1) gives

    Pθ²(s,·)≥δ_θ U_S(·).                               (7.2)

If δ_θ<1, writing Pθ²=δ_θ U_S+(1−δ_θ)R for a Markov kernel R proves
TV contraction by at most 1−δ_θ. Indeed a Markov kernel contracts TV by
the finite-sum triangle inequality, and the common U_S component cancels.
Iteration on the complete finite-dimensional probability simplex gives a
unique fixed point π_θ of Pθ² and convergence to it. If δ_θ=1,
Pθ²(s,·)=U_S directly and the same conclusion is immediate.
Since (π_θPθ)Pθ²=π_θPθ, uniqueness of the Pθ² fixed point implies
π_θPθ=π_θ. Every Pθ-stationary law is Pθ²-stationary, so π_θ is also its
unique stationary law. Further π_θ(t)≥m_θ²>0 by (7.1), and contraction gives

    TV(νPθ^t,π_θ)≤(1−δ_θ)^{floor(t/2)}                (7.3)

for every initial law ν; for exponent zero use the trivial upper bound one.
This proves source-by-source convergence without invoking unproved
continuity of stationary-law selection.

There is no source-uniform positive lower bound on δ_θ in the qualitative
class. An explicit illustration is

    θ^ε_ab(c)=(1−ε)1{c=b}+ε/K,      0<ε<1.             (7.4)

This is a strictly positive legal second-order table (in fact first order).
Its unique stationary pair law is

    π^ε_ab=(1/K)[(1−ε)1{b=a}+ε/K],

as a direct incoming-flow calculation verifies. From initial pair (0,0),
for each fixed finite t, the pair law tends to δ_(0,0) as ε↓0: with
probability at least (1−ε)^t all t transitions use the copying component.
Meanwhile π^ε tends to the uniform law on the K diagonal pairs. Thus

    lim_{ε↓0} TV(δ_(0,0)(P_{θ^ε})^t,π^ε)=1−1/K.       (7.5)

In particular no bound converging to zero with t can hold uniformly over
this strict-positive class and all initial laws. More directly for the
statistical question, (1.1)–(1.2) say its finite-horizon worst risks are
**exactly** unchanged. Qualitative irreducibility, aperiodicity, unique
stationarity and per-source mixing therefore cannot by themselves yield
improved uniform joint-(K,M) risks: each class defined by any combination
of those properties lies between the positive subclass and its full class,
so the same supremum equality follows by inclusion, with initialization
restricted in the same way on both sides. No conclusion is drawn here for
a class supplied with an additional quantitative lower bound or mixing
parameter, or for other structural restrictions not containing all
strict-positive sources.

## 8. Imported rate corollaries and exact scope boundary

Only this section imports already accepted statistical interfaces; the
exact finite-experiment equalities above are proved independently of them.
The frozen MM5/L1MAX interface gives, for all K≥2,M≥1,

    2^(−16) min{1,sqrt(K⁵/(M+1))}
      ≤ R_min(K,M) ≤ R_addone(K,M)
      ≤ min{1,48 sqrt(K⁵/(M+1))}.

Combining this accepted interface with (6.1)–(6.2) gives the identical
chain with R_min,pos and R_addone,pos. This is an imported rate corollary,
not a new proof or reinterpretation of MM5, and not a claim that MM5's
original zero-edge witness itself belongs to the positive subclass.

The accepted S001 upper and S002 lower interfaces give

    (1/180) min{1,sqrt(K³/(M+1))}
      ≤ R_stat(K,M) ≤ R⁺_stat(K,M)
      ≤ min{1,48 sqrt(K³/(M+1))}.

The same chain holds for R_stat,pos and R⁺_stat,pos. S002 already has a
strict-positive hard family, but the stronger exact equality (1.2), for
every common algorithm and every finite K,M, does not follow merely from
that order lower bound; it follows from stationary-flow regularization.
Thus the accepted arbitrary-initialization K⁵ and stationary K³
sample-complexity exponents are unchanged by qualitative legal-transition
positivity alone.

**Not an extension to TV-close-initialization classes.** The construction
in Section 4 keeps μ but generally changes whatever stationary law was
used to certify a constraint such as TV(μ,π)≤η. Section 5 preserves a
chosen stationary experiment by changing both θ and π, but can replace
rows at π-null states by uniform rows with an order-one error. An arbitrary
nearby μ may assign positive mass to such states, so the stationary π
weighting in (5.5), (5.7), and the target term is then unavailable. These
observations do not show such an extension false; they show it is **not
proved here**. We assert (1.1) and (1.2) separately, not their interpolation.

**Evidence classification.** This is a standard finite-experiment
density/continuity corollary, with stationary-flow regularization and an
explicit full-path telescope. It is not a novel proof tool or a literature
priority claim. It supplies a precise qualitative-versus-quantitative
condition boundary within the authorized statistical branch. It adds no
network, resource, compression, training, or fault-mechanism assertion.

## 9. Proof dependency and verification checklist

Load-bearing chain for (1.1): finite path telescope → bounded-target risk
comparison → direct row mixture → pointwise-in-A supremum equality.

Load-bearing chain for (1.2): finite path telescope → bounded-target risk
comparison → balanced triple-flow mixture → original-stationary weighted
row bound → pointwise-in-A supremum equality.

Checks supplied explicitly:

- All M observed transitions and the observed initial/terminal pairs remain
  in the data law; the target is the actual unobserved next-symbol row.
- The hybrid path telescope uses original P prefixes, not Q prefixes.
- The risk decomposition uses the original terminal law for target error.
- π-null states never require division by π; arbitrary unknown π is
  selected source by source and is not disclosed to A.
- Stationary mixtures, reducibility and periodicity of the original source
  are allowed throughout Section 5.
- Perturbed sources are fixed and homogeneous during each trajectory.
- Randomized kernels are included directly; bounds are uniform over A.
- Suprema are compared before taking infima, with no optimizer assumption.
- Every legal transition is positive; non-shift entries of P remain zero.
- Strict positivity gives P²>0 and source-dependent mixing, not a uniform
  quantitative gain or a claim about the TV-close initialization class.
