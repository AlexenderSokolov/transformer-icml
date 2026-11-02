# S003 初始 TV 距离的匹配过渡

科学正文摘录。以下保留已接纳版本的数学文字与原有编号，不重写证明；仅省略提交身份、流程元数据和历史状态。来源与依赖见 `../SOURCES.md`，逐字节映射见 `../COPY_MAP.json`。本次编排不是新的独立数学审查。

## 1. Exact experiment, source class, and theorem

Fix integers `K≥2`, `M≥1` and a public real `0≤η≤1`. Let `A={0,…,K−1}` and `S=A²`. A homogeneous order-two source is a table `θ=(θ_ab(c))` of probability rows; zero entries are allowed. Its legal pair kernel is

    Pθ((a,b),(b,c)) = θ_ab(c),

with all non-shift transitions zero. Within one experiment θ is fixed. The initial pair has law μ, and the complete observation is `H=(X₁,…,X_{M+2})`. Put

    Y_i=(X_{i+1},X_{i+2}),                  0≤i≤M,
    C_s(c)=Σ_{i=0}^{M−1}1{Y_i=s,X_{i+3}=c},
    n_s=Σ_c C_s(c),
    p⁺_s(c)=(C_s(c)+1)/(n_s+K).

Exactly M departures are observed; Y_M is the actual terminal pair, and its next departure X_{M+3} is unobserved. The loss is `TV(q,θ_{Y_M})=(1/2)Σ_c|q(c)−θ_{Y_M}(c)|`, always in `[0,1]`.

Define

    C_η(K) = {(θ,μ): there exists π∈Δ(S)
               with πPθ=π and TV(μ,π)≤η}.

The stationary law π is only an existential witness. It may depend on θ and μ, need not be unique, and is not given to the algorithm. No irreducibility, aperiodicity, reversibility, mixing, strictly positive transition, or stationary-mass lower bound is assumed.

A common algorithm `A_η` is a probability kernel from the **whole** observed history to `Δ_K`, allowed to depend on public K,M and η, and allowed a source-independent random seed. It does not read θ, μ, any witnessing π, a hidden mixture component, or future symbols. Let

    L_A(θ,μ) = E_{θ,μ,A} TV(A(H),θ_{Y_M}),
    R_η(K,M) = inf_A sup_{(θ,μ)∈C_η(K)} L_A(θ,μ),
    R⁺_η(K,M)= sup_{(θ,μ)∈C_η(K)} L_{p⁺}(θ,μ).

All risks use the same trajectory and actual terminal row, not an independent query, fixed row, random time, squared TV, or KL target. The supremum may select a source and initialization separately at each K,M,η and for each algorithm; the selected table stays fixed along its path.

Write

    n=M+1,
    A₀=K^(3/2)/sqrt(n),       B₀=K^(5/2)/sqrt(n),
    a=min{1,A₀},             b=min{1,B₀},
    u_s=min{1,48A₀},         u_g=min{1,48B₀},
    r=max{a,ηb}.

**Theorem S003.** For every admitted K,M,η,

    max{a/180, 2^(-16)ηb}
      ≤ R_η(K,M) ≤ R⁺_η(K,M)
      ≤ min{u_g, u_s+ηu_g}.                            (S003.1)

In particular,

    2^(-16) max{a,ηb}
      ≤ R_η(K,M) ≤ R⁺_η(K,M)
      ≤ min{1,48(a+ηb),48b}
      ≤ 96 max{a,ηb}.                                (S003.2)

Thus the same unchanged original full-history add-one rule attains the minimax order `Θ(max{a,ηb})`, with universal constants independent of K,M,η. “Exact transition” means this uniformly matching rate function including its caps, **not** an exact numerical minimax value or sharp constants.

Dependency separation: S002 is needed only for the stationary `a` lower term. The upper chain and the `ηb` lower term have no dependence on S002.

## 2. Imported premises and their precise roles


       sup_{πPθ=π} L_A(θ,π) ≥ a/180.                   (P-stat)



3. **Frozen L1MAX, admitted arbitrary-initialization add-one upper:** It gives for **every** θ and initial law ν

       L_{p⁺}(θ,ν) ≤ u_g.                             (P-upper)

   Only this statistical conclusion is imported. L1MAX's implementation, fault, and cost statements are not premises or outputs here.
4. **Frozen MM5, admitted all-common-algorithm arbitrary-initialization lower:** It gives for every fixed common full-history algorithm

       sup_{θ,ν} L_A(θ,ν) ≥ 2^(-16)b.                 (P-lower)



Fixing public η converts any algorithm in this theorem into one fixed common history kernel. Consequently (P-stat) and (P-lower), which quantify over **every** such kernel at fixed K,M, apply to it even if its design uses η. Neither lower theorem needs to have η listed as a source parameter. No source-dependent side information is added. If η is not disclosed, the algorithm class is smaller: the same lower remains valid, and the η-blind add-one provides the same upper, so the order is unchanged.

## 3. Finite existence of a stationary pair law

Every stochastic matrix on the finite nonempty set S has at least one stationary probability law. Here is the needed elementary proof, with no irreducibility assumption.

Choose any probability row vector ρ and for integer T≥1 define the Cesàro mean

    π_T = (1/T)Σ_{j=0}^{T−1} ρPθ^j.

Each π_T lies in the finite-dimensional compact simplex. There is a subsequence converging to some probability row π. Moreover the sum telescopes:

    π_T Pθ−π_T = (ρPθ^T−ρ)/T,
    ||π_T Pθ−π_T||₁ ≤ 2/T → 0.

Matrix multiplication is continuous, so taking the convergent subsequence gives `πPθ=π`. This proves existence even for reducible or periodic kernels and zero edges. The pair-shift structural zeros do not obstruct it: Pθ is a legitimate stochastic matrix on K² states.

For the lower construction a stationary law is chosen separately for each fixed θ. No measurable global selector `θ↦πθ`, continuity of that selector, or common stationary law across the family is required: each supremum comparison is pointwise in one source. The choice is not an algorithmic input.

## 4. Exact linearity of complete-path actual-terminal risk

Fix θ, K,M,η and one algorithm A throughout this section. For every initial state y define the probability law `Pθ^y` of the complete history starting deterministically at `Y₀=y`. This is defined even if y has probability zero under an initialization under consideration. For each full history h, let

    ℓ_A,θ(h) = E_A[TV(A(h),θ_{Y_M(h)})] ∈ [0,1],
    f_A,θ(y)=Σ_h Pθ^y(h) ℓ_A,θ(h) ∈ [0,1].

The algorithm seed is integrated under its same source-independent law. Both the actual endpoint in the target and the algorithm output remain functions of the **same complete history** h.

The elementary path formula

    Pθ,μ(H=h)= μ(y₀(h)) Π_{i=0}^{M−1}θ_{Y_i(h)}(x_{i+3})

implies, by a finite sum,

    L_A(θ,μ)=Σ_y μ(y) f_A,θ(y).                       (LIN)

Thus, for any two initial laws ν₀,ν₁ and `0≤t≤1`,

    L_A(θ,(1−t)ν₀+tν₁)
      =(1−t)L_A(θ,ν₀)+tL_A(θ,ν₁).                  (4.1)

This is linearity in the initial law at fixed θ and fixed algorithm, **not** linearity of TV as a function of the output or target. The target and conditional path laws may be strongly correlated with the observations. No conditional-iid statement, independent testing row, or loss replacement is made. The same argument holds for arbitrary randomized probability kernels, not just finitely supported random seeds.

## 5. Upper bound on the whole TV-neighborhood class

Fix any `(θ,μ)∈C_η(K)` and choose a stationary witnessing π with `TV(μ,π)≤η`. Define nonnegative measures

    δ(y)=(μ(y)−π(y))_+,
    e=Σ_yδ(y)=TV(μ,π)≤η.

The equality uses that μ and π have equal total mass, so positive and negative signed masses agree. Pointwise `μ≤π+δ`.

If e=0, then μ=π and S001 directly gives `L_{p⁺}(θ,μ)≤u_s`. If e>0, let `ν=δ/e`, an arbitrary probability law on S. Applying the nonnegative function `f_{p⁺,θ}` from (LIN) to the measure domination gives

    L_{p⁺}(θ,μ)
      ≤ L_{p⁺}(θ,π)+eL_{p⁺}(θ,ν)
      ≤ u_s+eu_g ≤ u_s+ηu_g.                        (5.1)

The second inequality uses S001 on π and (P-upper) on ν. This is valid even though ν may depend on both μ and θ: (P-upper) is uniform over all such initial laws. We do **not** assert that every TV-close μ can be written `(1−e)π+eν`; generally that asserted contamination representation would be false. Only the correct positive-part domination is needed for the upper.

Independently, (P-upper) applies directly to μ, giving `L_{p⁺}(θ,μ)≤u_g`. Taking the supremum proves

    R⁺_η≤min{u_g,u_s+ηu_g}.                           (5.2)

The original add-one algorithm is admissible, uses precisely the original M departures, and does not even need to know η. Therefore `R_η≤R⁺_η`.

To verify the capped simplification, for every x≥0,

    min{1,48x}≤48min{1,x}.

Hence `u_s≤48a`, `u_g≤48b`, and also `u_g≤1`. It follows from (5.2) that

    R⁺_η≤min{1,48(a+ηb),48b}≤96r.                   (5.3)

No uncapped rate has been substituted through a minimum in the wrong direction.

## 6. Matching lower bounds and their quantifiers

### 6.1 Stationary subclass — accepted S002 interface

For every stationary `(θ,π)`, choosing μ=π gives distance zero and hence membership in every `C_η(K)`. For every fixed common algorithm A, (P-stat) therefore gives

    sup_{(θ,μ)∈C_η(K)} L_A(θ,μ)
      ≥ sup_{πPθ=π}L_A(θ,π) ≥ a/180.                 (6.1)

The same bound holds after taking the infimum over A. Knowledge of η does not circumvent the universal algorithm quantifier, as explained in §2. This is the only use of S002.

### 6.2 Contamination of an arbitrary-initialization source — independent of S002

Fix any one common algorithm A, including any dependence on the fixed public η. For **every** legal θ and arbitrary initial law ν, §3 supplies a stationary law πθ. Define the new initialization

    μ_{θ,ν,η}=(1−η)πθ+ην.

Then

    TV(μ_{θ,ν,η},πθ)=ηTV(ν,πθ)≤η,                     (6.2)

so this source/initialization belongs to `C_η(K)`. By the exact same-kernel path-risk identity (4.1) and nonnegativity,

    L_A(θ,μ_{θ,ν,η})
      =(1−η)L_A(θ,πθ)+ηL_A(θ,ν)
      ≥ηL_A(θ,ν).                                    (6.3)

The entire observed initial pair and every subsequent symbol are present on both sides. A source-dependent πθ may change the information content of the stationary component, but cannot invalidate this exact decomposition. The algorithm is not given the mixing-component label or πθ. In particular, any information inferred from a ν-generated complete history is already allowed in the MM5 experiment for the very same A.

Taking the supremum over θ,ν in this pointwise comparison and applying (P-lower) gives

    sup_{C_η(K)} L_A ≥ η sup_{θ,ν}L_A(θ,ν)
                    ≥ η2^(-16)b.                    (6.4)

For η=0 the last lower bound is simply zero; no division by η occurs. This supremum formulation does not assume a supremum is attained. Alternatively the explicit finite MM5 hard families provide witnesses, to which the same contamination construction applies.

Only after deriving (6.4) for each fixed A do we take the algorithm infimum. Therefore

    R_η≥η2^(-16)b.                                   (6.5)

The algorithm, source, and supremum quantifiers are not interchanged. A single source is not claimed to defeat every algorithm, every η, or every horizon simultaneously.

### 6.3 Assembly

Combining (6.1) and (6.5) gives the maximum of the two lower bounds, not their sum at a purported common witness:

    R_η≥max{a/180,ηb/65536}≥2^(-16)max{a,ηb},

because `1/180≥1/65536`. Together with §5 this proves (S003.1)–(S003.2). The lower necessarily also applies to the original add-one as one admissible algorithm; the separate upper establishes that algorithm's order optimality.

## 7. Exact rate regimes and sample implications

These are algebraic consequences of the capped rate function and its matching-risk inequalities, not new independent tools.

### 7.1 Horizon and initialization-distance regimes

Since `B₀=K A₀` and `a≤b`, the crossover is `η=a/b`. Explicitly:

| Range of n=M+1 | a | b | r=max{a,ηb} |
|---|---|---|---|
| `n≤K³` | 1 | 1 | 1 |
| `K³≤n≤K⁵` | `sqrt(K³/n)` | 1 | `max{sqrt(K³/n),η}` |
| `n≥K⁵` | `sqrt(K³/n)` | `sqrt(K⁵/n)` | `sqrt(K³/n) max{1,Kη}` |

At shared boundaries the expressions agree. In particular:

* If `0≤η≤1/K`, then `ηb≤a` at every horizon and `r=a`. A TV departure of this scale does not worsen the stationary minimax order, uniformly in M.
* If `1/K<η≤1`, the sequence of rate regimes as n grows is: 1 up to K³; `sqrt(K³/n)` from K³ to `K³/η²`; a plateau η from `K³/η²` to K⁵; and `ηsqrt(K⁵/n)` after K⁵. Endpoint intervals may have zero length, and no interval is claimed to contain an integer for every K,η.
* At η=0, `C₀(K)` is exactly the stationary-initialization class, so the theorem recovers its rate.
* At η=1, §3 and `TV(μ,π)≤1` show that `C₁(K)` is the entire arbitrary-initialization class. Thus `r=b` and the imported general rate is recovered.

The class only asserts existence of a nearby stationary law; it does not impose a common π across sources or closeness to every stationary law.

### 7.2 Sample sufficient versus necessary directions

For any `0<ε<1`, the rate function itself satisfies the exact equivalence

    r≤ε  iff  n≥K³/ε²
       and [η≤ε or n≥η²K⁵/ε²].                       (7.1)

Indeed `a≤ε` forces the uncapped stationary expression to be at most ε. For the other term, if η≤ε then `ηb≤ε` is automatic; if η>ε it forces `b≤ε/η<1`, exactly the second sample inequality. This proves (7.1), including η=0 without dividing by zero.

Useful fully quantitative implications for `0<τ<1` are:

* **Sufficiency for original add-one:** from (S003.2), `r≤τ/96` guarantees `R⁺_η≤τ`. Equivalently it suffices that

      n≥96² K³/τ²,
      and [η≤τ/96 or n≥96²η²K⁵/τ²].                 (7.2)

  A sometimes sharper coarse-accuracy statement follows from (5.1): if `τ>η`, then

      n≥48²K³/(τ−η)²                                (7.3)

  suffices, because `R⁺_η≤48sqrt(K³/n)+η`. In particular, for `η≤τ/2`, `n≥96²K³/τ²` suffices.

* **Necessity for any common algorithm:** if its uniform risk on the class is at most τ and `τ<1/180`, (6.1) forces

      n≥K³/(180²τ²).                                 (7.4)

  If additionally `η>0` and `τ<η/65536`, (6.5) forces

      n≥η²K⁵/(65536²τ²).                             (7.5)

  The strict conditions are what remove the corresponding caps. If they do not hold, one cannot infer these uncapped necessary sample inequalities from that bound. Uniformly, `r≤65536τ` is necessary; when `τ<1/65536`, substitute ε=`65536τ` into (7.1) for its exact capped form.

In the sufficiently small-error regime `0<τ<min{1/180,η/65536}` with η>0, these upper and lower inequalities match the sample order

    max{K³,η²K⁵}/τ²

up to universal constants. At η=0 the matching stationary sample order is `K³/τ²` for sufficiently small τ. One must **not** assert the term `η²K⁵/τ²` is always necessary when the requested accuracy is coarser than η: the cap in b and the plateau are substantive. These statements concern statistical sample numbers, not neural resources, training, internal bits, fault tolerance, or sharp constants.

## 8. Boundary and non-overclaim audit

* **K=2, M=1 and all finite small parameters:** every new step is a finite simplex/path calculation valid at these parameters. The imported interfaces explicitly cover them; no asymptotic extension supplies a missing case. At M=1, `a=b=1`, so the capped rate is one.
* **η=0 and e=0:** handled separately before normalization. No undefined ν, η-reciprocal, or positive-contamination assumption is used.
* **η=1:** the full-class equality uses the finite stationary existence proof, rather than an unstated ergodicity assumption.
* **Zero edges and zero-mass states:** deterministic-initial-state path laws are defined everywhere, while the loss and linearity are finite sums; no conditional expectation on a null event is required.
* **Nonunique stationary laws and mixtures of closed classes:** upper proof works with any witness realizing the class condition; lower needs only one witness per θ. Neither requires the chain to approach that stationary law from all states.
* **TV closeness versus contamination:** the upper treats all TV-close initializations, not just a smaller contamination subclass; the lower legitimately uses a contamination subclass contained in the full class. Its distance may be strictly less than η, which is allowed by the “≤η” definition.
* **Source-dependent stationary law and side information:** πθ is a proof witness, not advice to the algorithm. Every visible symbol is retained in (LIN) and in the lower's MM5 comparison.
* **Public η:** the lower fixes it before the universal common-algorithm comparison. The upper algorithm remains unchanged and η-blind.
* **Risk versus estimator:** no claim that adding more history monotonically reduces empirical estimation error is used. This is the exact original full-history add-one risk throughout.
* **Quantifier boundary:** source/horizon-wise suprema and the algorithm infimum remain in the stated order; the two lower witnesses are combined by a maximum only.
* **Scientific classification:** positive-part measure domination, mixture linearity, finite stationary existence, and contamination of an existing lower are standard comparison arguments. This unit is an **initialization transition/tightness corollary** of accepted statistical premises, not a new-tool or literature-priority claim. Its substantive contribution is the full η-dependent capped minimax boundary, including the original algorithm and matching necessity.




Dependency graph:

    S001 accepted stationary add-one upper
      + L1MAX accepted arbitrary-initialization add-one upper
      + new explicit positive-part/complete-path comparison
        → S003 upper for the full TV-neighborhood class.

    Finite stationary existence + complete-path mixture identity
      + MM5 accepted arbitrary-initialization all-algorithm lower
        → S003 ηb lower, independently of S002.

    S002 accepted stationary all-algorithm lower
      + stationary subclass inclusion
        → S003 a lower.

    Both lower sides + upper
        → capped matching transition and sample/regime corollaries.



## 编排补充的依赖说明

(P-stat) 是 S002 的平稳下界；S001 给出 L_{p⁺}(θ,π)≤u_s。L1MAX 给出任意初始化的 (P-upper)，MM5 给出任意共同算法的 (P-lower)。其中 b 是 S003 的一般初始化率，不是 S006 的 IID 率。所有继承接口的完整科学证明片段和来源哈希见 inherited/ 与 SOURCES.md。
