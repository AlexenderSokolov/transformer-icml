# S001 平稳占用尾界与原 add-one 上界

科学正文摘录。以下保留已接纳版本的数学文字与原有编号，不重写证明；仅省略提交身份、流程元数据和历史状态。来源与依赖见 `../SOURCES.md`，逐字节映射见 `../COPY_MAP.json`。本次编排不是新的独立数学审查。

## 1. Exact theorem and scope

Let integers K≥2 and M≥1 be fixed. Let A={0,…,K−1}, S=A², and let θ=(θ_s(c)) be any homogeneous second-order transition table, allowing zero probabilities. Its pair transition matrix is

    Pθ((a,b),(b,c))=θ_ab(c),

and all other pair transitions are zero. Let π be **any** stationary probability law of Pθ; no irreducibility, aperiodicity, reversibility, mixing, positive-mass lower bound, or strict positivity is assumed. The initial pair (X₁,X₂) has law π. Observe exactly X₁,…,X_{M+2}. Define

    Y_i=(X_{i+1},X_{i+2}),                       0≤i≤M,
    C_s(c)=Σ_{i=0}^{M−1} 1{Y_i=s, X_{i+3}=c},
    n_s=Σ_c C_s(c)=Σ_{i=0}^{M−1}1{Y_i=s},
    J=n_{Y_M},
    p⁺_s(c)=(C_s(c)+1)/(n_s+K).

The terminal pair Y_M is observed but its departure is not; the target is the conditional law θ_{Y_M} of X_{M+3}. All expectations below use this same-trajectory, actual-terminal experiment. The estimator is the **original full-history add-one rule**, not a suffix average, not a predictor at an independent query, and not a random-time predictor.

**Theorem S001.** Uniformly over all such (θ,π),

    P(J<w) ≤ min{1, K²w/(M+1)}     for every integer w≥1,       (UC-stat)

and

    E TV(p⁺_{Y_M},θ_{Y_M})
       ≤ min{1,48 K^(3/2)/sqrt(M+1)}.                          (S001)

Consequently, with the frozen definitions,

    R_stat(K,M) ≤ R⁺_stat(K,M)
       ≤ min{1,48 sqrt(K³/(M+1))}.

The left inequality only says that original add-one is an admissible common predictor; **no stationary minimax lower bound, equality of orders, or optimality assertion is proved here**. The algorithm knows K,M and the complete observed history only. In particular it does not receive π or θ.



## 3. New finite-window stationary occupancy lemma

### 3.1 Purely deterministic count

Let M≥1 and w≥1 be integers. For any finite state sequence y₀,…,y_{2M}, fix a state s and, for t=M,…,2M, define

    a_t = 1{y_t=s, Σ_{i=t−M}^{t−1}1{y_i=s}<w}.

Then

    Σ_{t=M}^{2M} a_t ≤ w.                              (3.1)

**Proof.** Suppose instead that at least w+1 flags occur and list any w+1 of them chronologically as t₁<⋯<t_{w+1}. Set t=t_{w+1}. Each earlier t_j satisfies

    t−M ≤ M ≤ t_j ≤ t−1,

because t≤2M, t_j≥M and the indices are distinct integers. Thus all w earlier flagged times lie in the length-M window {t−M,…,t−1}, and all carry state s. This window contains at least w occurrences of s, contradicting a_t=1. This proves (3.1). If w>M+1, the conclusion also follows trivially from the number of candidate times; the same contradiction proof is valid without a separate restriction on w. ∎

The count is w rather than w−1: for instance a single new occurrence in this candidate interval may be flagged for w=1. Its validity does not involve any stochastic law, stopping time, recurrence, or independence.

### 3.2 Stationarity converts the count to one terminal event

For any stationary process Y on a finite alphabet, apply (3.1) to Y₀,…,Y_{2M}. For t=M,…,2M the segment (Y_{t−M},…,Y_t) has the same law as (Y₀,…,Y_M). Therefore all M+1 flags have the same probability, and

    (M+1) P(Y_M=s, Σ_{i=0}^{M−1}1{Y_i=s}<w)
      = E Σ_{t=M}^{2M} a_t
      ≤ w.

Thus, for every fixed s,

    P(Y_M=s,n_s<w) ≤ min{P(Y_M=s), w/(M+1)}.            (3.2)

Only stationarity of consecutive length-(M+1) blocks is needed; no ergodic theorem or mixing estimate is used. The proof uses nonnegative indices only. The extension to time 2M is an auxiliary probability construction, not extra observations available to the predictor.

For the present source, start the pair Markov chain at π and extend it to time 2M with the same θ. Its state marginal at every time is π, since πPθ=π. More explicitly, for every a≥0 and legal states y₀,…,y_M,

    P(Y_a=y₀,…,Y_{a+M}=y_M)
       = π(y₀) Π_{r=0}^{M−1} Pθ(y_r,y_{r+1}),

independent of a. This verifies exactly the block stationarity used above, including zero probabilities and any reducible or periodic chain.

The events {Y_M=s,n_s<w}, s∈A², are disjoint and their union is {J<w}. Summing (3.2) over the K² states and also applying the probability cap one gives

    P(J<w) ≤ min{1,K²w/(M+1)},

which is UC-stat. States with π(s)=0 contribute zero. A mixture of stationary laws of multiple closed classes is included automatically. This completes the new occupancy argument **before** using it in a rate assertion.

From now on put

    c = K²/(M+1),        T_stat = sqrt(Kc)=K^(3/2)/sqrt(M+1).

## 4. Inherited finite row-stack realization and maximal-moment bound

This section records the full relevant mechanism of frozen L1MAX §§2–5. It is not a conditional-iid argument.

### 4.1 Finite coupling

Take an initial pair of law π and, independently of it, variables

    ξ_{s,l} ~ θ_s,       s∈A², 1≤l≤2M,

independent across all rows and indices. Whenever the trajectory departs row s for the (j+1)-st time, use ξ_{s,j+1} as the next symbol and take the legal pair shift (a,b)↦(b,ξ_{s,j+1}). At most M symbols of any row are consumed by the observed path, so the finite stacks suffice.

For every prescribed finite symbol prefix x₁,…,x_{i+2}, the construction imposes exactly the initial-pair condition and the consumed prefix constraints in each row stack, with no constraints on unused stack entries. Its probability is

    π(x₁,x₂) Π_{r=0}^{i−1} θ_{x_{r+1},x_{r+2}}(x_{r+3}).

This equals the original homogeneous path probability. A zero-probability prefix has probability zero on both sides; no conditioning on a null event is invoked. Thus the finite observed-history law is unchanged.

Define, simultaneously in all rows,

    S_{s,j}=Σ_{l=1}^j(e_{ξ_{s,l}}−θ_s),      S_{s,0}=0.

Then the count identity is pathwise:

    (C_s(c)−n_s θ_s(c))_{c∈A}=S_{s,n_s}.                (4.1)

In particular the terminal row, its count, and its stack deviations can be dependent. No iid property conditional on any of them is asserted.

### 4.2 Mean and concentration at deterministic prefixes

For deterministic 1≤v≤M define

    F_{s,v}=max_{0≤j≤2v}||S_{s,j}||₁,
    Z_v=max_{s∈A²}F_{s,v}.

The deterministic-prefix process S_{s,j} is a vector martingale. The finite nonnegative-submartingale L² maximal bound gives

    E max_{j≤2v}||S_{s,j}||₂² ≤4E||S_{s,2v}||₂²≤8v,

since the last second moment is 2v(1−||θ_s||₂²)≤2v. Consequently

    E F_{s,v}≤sqrt(K) E max_{j≤2v}||S_{s,j}||₂≤sqrt(8Kv).   (4.2)

For clarity the finite maximal bound follows by partitioning {H≥λ} by its first hitting time, yielding λP(H≥λ)≤E[W_m1{H≥λ}]. Integrating 2dλ and applying Cauchy–Schwarz gives EH²≤2E(W_mH)≤2||W_m||₂||H||₂, hence EH²≤4EW_m². Bounded variables justify every integral and the zero-norm case is immediate.

Changing one of the 2v independent symbols in a fixed stack changes every affected partial sum by e_b−e_a, whose L¹ norm is at most 2. Therefore it changes F_{s,v} by at most 2. The bounded-difference MGF bound is

    E exp(λ(F_{s,v}−E F_{s,v})) ≤exp(vλ²).

One finite proof exposes coordinates successively. Each conditional martingale difference has mean zero and range length at most 2. For any finite random variable B in an interval of length d, the log-MGF has second derivative Var_λ(B)≤d²/4; integrating twice proves E exp(λ(B−EB))≤exp(λ²d²/8). Conditional application and iteration over 2v coordinates give the displayed bound. Exponential Markov with λ=t/(2v) yields

    P(F_{s,v}−E F_{s,v}>t)≤exp(−t²/(4v)),       t≥0.    (4.3)

The range length is for the full L¹ prefix maximum, so this concentration deviation receives no extra factor sqrt(K).

### 4.3 Maximum over rows and exact coefficient

Set b=sqrt(8Kv), a=sqrt(8v ln K). By (4.2)–(4.3) and a union over K² rows,

    P(Z_v>b+a+t)
       ≤ K² exp(−(a+t)²/(4v))
       ≤ exp(−t²/(4v)),                         t≥0.

This union does not need independence between row maxima. With R=(Z_v−b−a)_+, tail integration gives

    ER⁴ ≤∫₀^∞4t³ exp(−t²/(4v))dt=32v².

Minkowski then gives

    ||Z_v||₄ ≤sqrt(8Kv)+sqrt(8v ln K)+32^(1/4)sqrt(v).

Since ln K/K≤1/e<3/8 and K≥2,

    ||Z_v||₄/sqrt(Kv)
       ≤sqrt(8)+sqrt(3)+2^(3/4)<25/4.                  (4.4)

For an exact rational check, sqrt(8)<283/100, sqrt(3)<1733/1000 and 2^(3/4)<1683/1000, whose sum is 6246/1000<25/4. Their respective squared/fourth-power comparisons are 80089>80000, 3003289>3000000, and 8022993935121>8000000000000. This proves the imported bound with the stated constant and with no π-dependence. Deterministic rows and zero variance are included.

## 5. Inherited numerical dyadic bound

For real a>0 define the deterministic series

    D(a)=Σ_{l=0}^∞2^(−l/2) min{1,a2^l}^(3/4).

Then

    D(a)≤10sqrt(a).                                    (5.1)

If a≥1, D(a)=1/(1−2^(−1/2))=2+sqrt(2)<7/2≤10sqrt(a). If 0<a<1, choose L≥0 with a2^L≤1<a2^(L+1). Splitting at L gives

    Σ_{l=0}^L a^(3/4)2^(l/4)
       ≤sqrt(a)/(1−2^(−1/4)),
    Σ_{l=L+1}^∞2^(−l/2)
       <sqrt(a)/(1−2^(−1/2)).

Since 2^(−1/4)<27/32, the first denominator inverse is <32/5. The second is 2+sqrt(2)<7/2. Their sum is <99/10<10. The exact dyadic threshold term belongs to the first sum. Only this numerical series is infinite; no extra stacks at v>M will be introduced.

## 6. Actual selected-row error, without conditioning away dependence

For J≥1 only, define the empirical terminal row p̂_{Y_M}=C_{Y_M}/J. For deterministic v=2^l≤M set E_v={v≤J<2v}. The pathwise identity (4.1) gives on E_v

    TV(p̂_{Y_M},θ_{Y_M})
       =||S_{Y_M,J}||₁/(2J)≤Z_v/(2v).                 (6.1)

Apply Hölder **unconditionally** with exponents 4 and 4/3. By (4.4), E_v⊆{J<2v}, and UC-stat at the integer threshold w=2v,

    E[TV(p̂_{Y_M},θ_{Y_M})1_{E_v}]
       ≤ ||Z_v||₄ P(E_v)^(3/4)/(2v)
       ≤(25/8)sqrt(K) v^(−1/2) min{1,2cv}^(3/4).      (6.2)

This is the exact place where c enters the selected-row bound. No statement about iid samples conditional on Y_M, J or E_v is made; all their correlations remain in the expectation to which Hölder is applied. A zero-probability E_v has zero left side.

The finitely many layers l=0,…,floor(log₂M) partition {1≤J≤M}. In particular J=M is covered even when M is a power of two; then its layer starts at v=M, and the auxiliary stack maximum through 2M exists. Sum (6.2) and extend only its nonnegative numerical right side using (5.1), with a=2c:

    E[TV(p̂_{Y_M},θ_{Y_M})1_{J≥1}]
       ≤(25/8)sqrt(K)D(2c)
       ≤(125sqrt(2)/4)sqrt(Kc)
       =(125sqrt(2)/4)T_stat.                         (6.3)

The notation on the left means the empirical loss defined on {J≥1} and extended by zero elsewhere; it never forms a zero-denominator empirical row. Neither a probability maximum nor a new experiment is substituted for the original terminal loss.

## 7. Smoothing, real thresholds, and the exact final constant

For real A≥0, UC-stat implies

    E min{1,A/(J+K)}≤Ψ(cA)≤2sqrt(cA),                  (7.1)

where

    Ψ(0)=0,
    Ψ(z)=z(1+ln(1/z)) for 0<z<1,
    Ψ(z)=1 for z≥1.

For A=0 the assertion is immediate. For A>0 and 0<t<1, put x=A/t−K. The event {min{1,A/(J+K)}>t} is {J<x}. If x≤0 it is empty. If x>0, integer-valued J implies

    {J<x}={J<ceil(x)},
    1≤ceil(x)≤x+1=A/t−K+1≤A/t.

Apply UC-stat at integer w=ceil(x) to bound this probability by min{1,cA/t}. Tail integration over t∈(0,1) yields Ψ(cA); the inequality min{1,cA/t}≤sqrt(cA/t) yields its upper bound 2sqrt(cA). This proof includes noninteger A, exact integer x, and J=0.

When J≥1, writing u for the uniform law on A,

    p⁺_{Y_M}=[J/(J+K)]p̂_{Y_M}+[K/(J+K)]u.

Thus its TV loss is at most the empirical loss plus K/(J+K). At J=0, p⁺_{Y_M}=u and the loss is at most one. Separating these cases and enlarging only the nonnegative smoothing term gives

    E TV(p⁺_{Y_M},θ_{Y_M})
       ≤P(J=0)
        +E[TV(p̂_{Y_M},θ_{Y_M})1_{J≥1}]
        +E min{1,K/(J+K)}.                            (7.2)

UC-stat at w=1 gives

    P(J=0)≤min{1,c}≤sqrt(c)≤sqrt(Kc)=T_stat.

Equation (7.1) with A=K gives a smoothing contribution ≤2sqrt(Kc)=2T_stat. Equation (6.3) supplies the empirical term. Therefore

    E TV(p⁺_{Y_M},θ_{Y_M})
       ≤[125sqrt(2)/4+3]T_stat
       <48T_stat,                                    (7.3)

because sqrt(2)<36/25 (as 2<1296/625), and

    (125/4)(36/25)+3=48.

Finally TV between probability vectors is always at most one. Taking the supremum over exactly the stationary source class proves

    R⁺_stat(K,M)≤min{1,48K^(3/2)/sqrt(M+1)}.

This constant derivation is exactly the L1MAX Sections 7–8 transfer with c replaced by its separately proved stationary coefficient, rather than a substitution into an already fixed K⁵ theorem.

## 8. Boundary and non-overclaim ledger

* **K=2, M=1, and all finite small values:** the deterministic count uses M+1 candidate endpoints; row stacks have length 2M; the sole v=1 layer is valid when M=1. The cap one applies whenever the rate expression is large.
* **J=0:** the empirical row is never divided by zero. Its contribution is defined only on {J≥1}; the zero-count loss is bounded separately. All smoothing denominators are J+K>0.
* **Large w:** UC-stat applies to every integer w≥1, even w>M, with the probability cap retained. Hence w=2v remains legal in the final dyadic layer.
* **Zero transition probabilities and deterministic rows:** the finite product-space path identity, bounded differences, variance, and maximal inequalities remain valid. Null prefixes are not conditioned upon.
* **Zero stationary mass / unreachable pairs:** such states have zero terminal probability. They may stay in the auxiliary K²-row maximum without invalidating or weakening the stated uniform constant beyond what is already budgeted.
* **Reducibility, mixtures of closed classes, periodicity:** only πPθ=π and finite block stationarity are used. There is no unique-stationary-law or convergence-to-stationarity step.
* **No extra information to the algorithm:** the extension to time 2M for §3 and unused row-stack variables for §4 are proof devices. The output remains the exact full-history add-one formula on the original M departures; it sees neither these devices nor θ,π.
* **Correlations:** the actual terminal row, its count, and all row errors remain selected from the same path. Inequality (6.1) is pathwise and (6.2) is unconditional, so no false selected-row iid claim appears.
* **No lower-bound transfer:** arbitrary-initialization MM5 is not moved to stationary initialization. Neither uniform iid add-one risk nor this upper bound is used as an all-algorithms minimax lower bound.


## 9. Concise dependency graph

    New deterministic finite-window count (3.1)
       + stationary block law
         → UC-stat with c=K²/(M+1)

    Frozen L1MAX finite row stacks and deterministic-prefix L⁴ maximum
       + frozen numerical dyadic sum
       + UC-stat, used only unconditionally at integer thresholds
         → actual selected-row empirical bound (6.3)

    UC-stat + exact add-one mixture identity + real-threshold truncation
       + (6.3) + probability cap
         → S001 original-add-one upper with constant 48.

There is no dependency on a stationary lower bound, a KL theorem, a mixing hypothesis, a network implementation, or an unknown stationary distribution supplied to the estimator.
