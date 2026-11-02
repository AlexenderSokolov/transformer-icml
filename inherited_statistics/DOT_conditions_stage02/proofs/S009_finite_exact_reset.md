# S009 存在有限完全重置的匹配推论

科学正文摘录。以下保留已接纳版本的数学文字与原有编号，不重写证明；仅省略提交身份、流程元数据和历史状态。来源与依赖见 `../SOURCES.md`，逐字节映射见 `../COPY_MAP.json`。本次编排不是新的独立数学审查。

For the class of legal second-order sources for which **some finite, source-dependent integer q** satisfies `P^q=Pi` on **all** starting pairs, with arbitrary initial pair law, the common-algorithm minimax actual-endpoint mean-TV risk is

    a(K,M)=min{1,sqrt(K^3/(M+1))}

up to absolute constants, for every `K>=2,M>=1`. The ORIGINAL complete-history rowwise add-one attains this order, with explicit constants

    a(K,M)/100000 <= R_fin(K,M) <= R_fin^+(K,M)
       <= min{1,68 sqrt(K^3/(M+1))} <= 68 a(K,M).       (S009.1)

No reset exponent, stationary law, or initial law is supplied to the estimator. The finite-dimensional argument below proves that the existential reset condition already implies `P^(K^2)=Pi`, uniformly over this class. This is an elementary nilpotence argument plus accepted statistical theorems: **a standard finite-dimensional/statistical corollary, not a new kernel classification or a sharp approximate-mixing theorem.**


## 1. Experiment, class, information, and theorem

Fix deterministic integers `K>=2,M>=1`. Write `mathcal A={0,...,K-1}`, `S=mathcal A^2`, and `d=|S|=K^2`. A legal homogeneous second-order table `theta=(theta_ab(c))` has nonnegative rows of sum one. Its pair transition matrix is

    P((a,b),(b,c))=theta_ab(c),

and is zero on non-shift transitions. Initial law `mu` is an arbitrary probability law on S. Observe **all** `H=(X_1,...,X_{M+2})`, equivalently `Y_i=(X_{i+1},X_{i+2})`, `0<=i<=M`. The target is the row `theta_{Y_M}` at the actual same-trajectory endpoint, for the unobserved next symbol `X_{M+3}`.

For a probability row vector pi on S, let `Pi` denote the matrix whose every row is pi. Define `E_K^fin` to be the class of `(theta,mu)` for which

    there exist a stationary probability law pi (pi P=pi)
    and a finite integer q>=1 such that
    P^q(s,t)=pi(t) for EVERY s,t in S.                 (Efin)

The quantifier is `for each source there exists some finite q`; neither a chosen q nor a uniform bound on it is an additional input assumption. The law pi and a witnessing q are hidden source descriptors. In particular, mu may put mass on pairs with pi mass zero. The all-starting-pairs quantifier cannot be replaced by a condition only on the support of pi.

An admissible estimator `T(H,U)` takes values in the probability simplex on mathcal A. It may use public K,M and the stated class definition; its optional random seed U is independent of source and data. It may not read hidden theta,mu,pi,q or future symbols. Define

    R_fin(K,M)=inf_T sup_{(theta,mu) in E_K^fin}
                         E_{theta,mu} TV(T(H,U),theta_{Y_M}),

    C_s(c)=sum_{i=0}^{M-1}1{Y_i=s,X_{i+3}=c},
    n_s=sum_c C_s(c),       p_s^+(c)=(C_s(c)+1)/(n_s+K),

    R_fin^+(K,M)=sup_{(theta,mu) in E_K^fin}
                         E_{theta,mu} TV(p_{Y_M}^+,theta_{Y_M}).

Here `TV(p,r)=(1/2)sum_c |p(c)-r(c)|`. Both risks concern unconditional **expected TV**, not TV squared, predictive KL, a fixed query, an independent test query, a random-time average, or a conditional-endpoint risk. The original rule uses all M departures, including every observation before a reset. A deterministic burn index appearing below belongs only to its analysis.

**Theorem S009 (finite-reset class corollary).** Under precisely this experiment and information restriction, (S009.1) holds for every `K>=2,M>=1`. Moreover, (Efin) is equivalent to the same class definition with the specific exponent `q=d=K^2`, and its stationary law is unique. The bound on the exponent is a derived finite-dimensional fact, not additional side information about an individual source.

## 2. Allowed assumptions, checked interfaces, and lemma map

Primitive conditions are exactly the finite legal pair-shift experiment, homogeneity, the displayed information restriction, and the class hypothesis (Efin). The fact that a reset occurs by d, uniqueness of pi, and the vanishing initialization discrepancy are proved below; they are not silently assumed. No positivity, reversibility, positive stationary minimum, stationary initialization, or known reset time is imposed on the whole class.




1. **S004 ORIGINAL full-history theorem, equation S004.2 and Proposition 4.** For any legal theta, stationary pi, arbitrary mu, and deterministic integer `0<=b<=M-1`, put `L=M-b>=1` and `eta_b=TV(mu P^b,pi)`. Then the original all-M-departure rule above satisfies

       E TV(p_{Y_M}^+,theta_{Y_M})
         <= min{1,48 K^(3/2)/sqrt(L+1)
                        +13 sqrt(K) eta_b^(3/4)}.     (2.1)

   This theorem was proved using original-count domination and an original-stack argument. Its separate suffix theorem is **not** the interface used here. All its assumptions hold for an Efin source; the deterministic burn's admissibility and eta_b=0 will be checked in Proposition 3.

2. **S007 exact-three-reset all-estimator lower, Theorem S007.** Let `E_K^(3)` be the same legal-source/arbitrary-mu class with `P^3=Pi` for every starting pair and a stationary pi. For every `K>=2,M>=1`, and every admissible complete-history estimator T,

       sup_{(theta,mu) in E_K^(3)}
         E TV(T(H,U),theta_{Y_M}) >= a(K,M)/100000.   (2.2)

   Its lower witnesses have genuine stationary initialization. For K>=6 they are the legal uniform-stationary checkerboard family with `P^3=Pi` and `P^2!=Pi`; for K=2,...,5 the theorem uses an accepted stationary-IID lower retaining all M+2 observations. Randomized estimators are covered. We import the accepted all-K theorem, not merely the large-alphabet construction. Membership in Efin and admissibility of restricted estimators will be discharged in Proposition 4.

For interpretation, S004's exact-two-reset identity and S007's accepted comparison to S005 identify the IID boundary: all-state `P^2=Pi` forces every theta row to be a single unknown law p, whose optimal mean-TV rate is `min{1,sqrt(K/(M+1))}`; pooling the symbol data achieves the smaller order and original rowwise add-one need not. The algebraic identity is rechecked in Section 5. This IID statistical comparison is inherited from the accepted S007/S005 interface and is **not needed to establish (S009.1)**.

No new external-paper theorem is invoked. The nilpotence fact is proved completely rather than cited. The mathematical dependencies inherited by S004/S007 are used at their accepted interfaces, not independently re-proved in this corollary.

| Local unit | Named result and stable label | Contribution |
|---|---|---|
| unit_001 | Lemma 1, Reset projection and nilpotent remainder (`lem:s009-algebra`) | Pi algebra, `P^n=Pi+(P-Pi)^n`, uniqueness |
| unit_002 | Lemma 2, Full kernel-chain bound (`lem:s009-kernel-chain`) | Some finite reset implies all-state reset by d=K^2 |
| unit_003 | Proposition 3, Original-rule arbitrary-start upper (`prop:s009-original-upper`) | All K,M upper with absolute constant 68 |
| unit_004 | Proposition 4, Inherited all-estimator lower (`prop:s009-lower`) | E3 inclusion and constant 1/100000, including small K |

## 3. Local derivation

### unit_001: lemma — Reset projection and nilpotent remainder (`lem:s009-algebra`)

**Statement.** Let P be any row-stochastic matrix on a finite d-state set, let pi be a stationary probability row vector, and let Pi have every row pi. Then

    Pi^2=Pi,    P Pi=Pi P=Pi.

Writing `A=P-Pi`, one has `A Pi=Pi A=0` and, for every integer `n>=1`,

    P^n=Pi+A^n.                                      (3.1)

Consequently if `P^q=Pi` for some finite integer `q>=1`, then `A^q=0`, and pi is the unique stationary probability law. These statements permit zero coordinates of pi.

**Proof.** For states s,t, the probability normalization and stationarity give respectively

    (Pi^2)(s,t)=sum_u pi(u)pi(t)=pi(t),
    (P Pi)(s,t)=sum_u P(s,u)pi(t)=pi(t),
    (Pi P)(s,t)=sum_u pi(u)P(u,t)=pi(t).

Subtracting these identities gives `A Pi=(P-Pi)Pi=0` and `Pi A=Pi(P-Pi)=0`. For n=1, (3.1) is the definition of A. If it holds for n, multiply by `P=Pi+A` and obtain

    P^(n+1)=(Pi+A^n)(Pi+A)
           =Pi^2+Pi A+A^n Pi+A^(n+1)
           =Pi+A^(n+1),

where `A^n Pi=A^(n-1)(A Pi)=0` for n>=1. This proves (3.1) by induction, without an unproved commuting-binomial expansion. Taking n=q under the reset hypothesis gives `A^q=0`.

If nu is any stationary probability row vector for P, then repeated stationarity and reset give

    nu=nu P^q=nu Pi=pi,

the last equality following from `sum_s nu(s)=1`. Thus pi is unique. Every calculation uses only finite sums and no division by pi; zero stationary masses cause no exception. ∎

### unit_002: lemma — Full kernel-chain bound (`lem:s009-kernel-chain`)

**Statement.** Let A be a linear map on the real d-dimensional vector space `R^d`. If `A^q=0` for some finite integer q>=1, then `A^d=0`. Therefore every source in Efin satisfies `P^d=Pi`, with `d=K^2`, and `mu P^b=pi` for every initial probability law mu and every integer b>=d. Conversely, `P^d=Pi` with stationary pi is a witness for (Efin).

**Proof of the dimension claim.** Set `V_j=ker(A^j)` for integers j>=0, using `A^0=I`, so `V_0={0}`. If `x in V_j`, then `A^(j+1)x=A(A^j x)=0`; hence

    V_0 subset V_1 subset V_2 subset ... .            (3.2)

We first prove that one equality in this chain forces all later spaces to remain equal. Suppose `V_j=V_(j+1)`. If `x in V_(j+2)`, then `Ax in V_(j+1)=V_j`, so `A^(j+1)x=A^j(Ax)=0`. Thus `x in V_(j+1)`. Inclusion in the other direction follows from (3.2), and consequently `V_(j+2)=V_(j+1)=V_j`. Applying this same implication successively to adjacent equal spaces proves by induction that

    V_(j+r)=V_j for every integer r>=0.              (3.3)

Under `A^q=0`, `V_q=R^d`, and all `V_j` with j>=q are full by (3.2). If V_j is proper, then necessarily j<q. An equality `V_j=V_(j+1)` would imply by (3.3) that `V_q=V_j` is proper, a contradiction. Thus whenever V_j is proper, the next inclusion is strict.

If V_d were proper, all `V_0,...,V_d` would be proper by (3.2). Each of the d inclusions from V_0 to V_d would then be strict. A strict inclusion of finite-dimensional subspaces increases dimension by at least one: a vector in the larger space but outside the smaller one extends any basis of the smaller space to a linearly independent set. Since `dim V_0=0`, it would follow that `dim V_d>=d`, contradicting properness in a d-dimensional space. Therefore `V_d=R^d`, exactly the assertion `A^d=0`.

**Application to the source.** By Lemma 1, a witnessing finite reset exponent for an Efin source gives `A^q=0` for `A=P-Pi`. The dimension claim yields `A^d=0`, and (3.1) then gives `P^d=Pi`. If b>=d, write `b=d+r` with r>=0. Stationarity implies `pi P^r=pi`; hence

    mu P^b=mu Pi P^r=pi P^r=pi.                     (3.4)

In particular the conclusion holds for every mu, including mass outside the stationary support. Conversely, d is a finite positive integer, so `P^d=Pi` itself supplies the required witness q=d. This proves the announced class equivalence, without determining the minimal exponent or classifying the possible kernels. ∎

### unit_003: proposition — Original-rule arbitrary-start upper (`prop:s009-original-upper`)

**Statement.** In the frozen experiment, for every `K>=2,M>=1` and every `(theta,mu) in E_K^fin`, the ORIGINAL all-history add-one satisfies

    E TV(p_{Y_M}^+,theta_{Y_M})
       <= min{1,68 sqrt(K^3/(M+1))}.                 (3.5)

**Proof.** First suppose `M>=2d`, where `d=K^2`. Choose the deterministic **analytical** burn `b=d`. It is admissible for (2.1): `d>=1`, `d<=M-1`, and `L=M-d>=d>=1`. Lemma 2 gives `mu P^d=pi`, so `eta_d=0`. Applying the accepted ORIGINAL-rule bound (2.1) therefore yields

    E TV(p_{Y_M}^+,theta_{Y_M})
       <=min{1,48 K^(3/2)/sqrt(M-d+1)}.             (3.6)

The algorithm in (3.6) still counts **every** departure `i=0,...,M-1`. We have not replaced it by a suffix algorithm, and we have not asserted that its initial full history is stationary. Exact stationarity at time d is used only through the separately proved original-rule interface.

Because `M>=2d`,

    M-d+1 >= (M+1)/2,
    48 K^(3/2)/sqrt(M-d+1)
       <=48 sqrt(2) sqrt(K^3/(M+1))
       <68 sqrt(K^3/(M+1)).                         (3.7)

The numerical strict inequality is exact: `48^2*2=4608<4624=68^2`, with positive quantities. This proves (3.5) in this regime.

Now suppose `M<2d`. Since M is an integer, `M+1<=2d=2K^2`, whence

    K^3/(M+1) >= K/2 >=1.                          (3.8)

Thus `a(K,M)=1` and `min{1,68 sqrt(K^3/(M+1))}=1`. Every probability-vector TV loss is at most one, so this same bound holds without choosing any burn. This includes M=1 and the boundary `K=2,M=7`, where the ratio in (3.8) can equal one.

The two regimes cover all K,M. Supremum over Efin preserves the uniform inequality. Finally, for any t>=0,

    min{1,68t} <=68 min{1,t}:

if t<=1 the left side is at most 68t, and if t>=1 it is at most 1<=68. Applying this with `t=sqrt(K^3/(M+1))` proves the upper part of (S009.1). No unknown witnessing q or hidden law is used by the rule, nor even by the deterministic choice b=d. ∎

### unit_004: proposition — Inherited all-estimator lower (`prop:s009-lower`)

**Statement.** Under the frozen experiment and information restriction, every `K>=2,M>=1` satisfies

    R_fin(K,M)>=a(K,M)/100000.                      (3.9)

**Proof.** If `(theta,mu) in E_K^(3)`, its stationary pi and finite integer q=3 witness (Efin). Consequently

    E_K^(3) subset E_K^fin.                        (3.10)

Fix any estimator T allowed for Efin. Its rule is a common, source-independent map of the full H and an independent seed, with only public K,M and fixed class information. Restricting the experiments to E3 gives an admissible complete-history estimator for E3: one can use exactly the same map without learning any hidden parameter. Knowledge of the larger class does not furnish an oracle unavailable to such a restricted estimator. The all-estimator accepted lower (2.2) and class inclusion therefore give

    sup_{E_K^fin} E TV(T(H,U),theta_{Y_M})
       >=sup_{E_K^(3)} E TV(T(H,U),theta_{Y_M})
       >=a(K,M)/100000.                            (3.11)

Taking the infimum over all Efin estimators proves (3.9). The dependency is already uniform for K=2,...,5 as well as K>=6, so no empty checkerboard construction or unproved small-K extrapolation is being used. Every hard lower witness is a genuine stationary-initialized member of the arbitrary-mu Efin class; there is no restriction of the upper to stationary starts. All M+2 observed symbols and the same actual endpoint remain available in the lower. ∎

## 4. Target assembly, sample scale, and scope of optimality

Lemma 1 converts the reset condition to nilpotence with the correct stationary projection. Lemma 2 proves the complete finite-dimensional kernel-chain implication and hence the public dimension bound d. Proposition 3 uses that derived bound only inside the accepted ORIGINAL S004 theorem, with admissibility, small horizons, and constant 68 checked explicitly. Proposition 4 imports the accepted exact-three-reset lower on a genuine subclass, for all alphabet sizes and horizons.

The rule p^+ is one admissible common estimator, so by the definition of infimum `R_fin<=R_fin^+`. Combining this fact with Propositions 3 and 4 proves every inequality of (S009.1). There is no interchange of a limit and supremum or exchange of an existential q with an estimator's knowledge: the finite-dimensional bound is proved pointwise for each source and is the same function K^2 for every source at that K.

For precision `delta` with `0<delta<1/100000`, any common rule whose worst-case Efin mean-TV risk is at most delta must satisfy

    M+1 >= (1/100000)^2 K^3/delta^2.                (4.1)

Indeed the lower in (S009.1) rules out the saturated branch a=1, and then its nonsaturated inequality rearranges to (4.1). Conversely the original rule suffices for `0<delta<1` whenever

    M+1 >= 68^2 K^3/delta^2.                       (4.2)

These loose constants express the proved `K^3/delta^2` worst-case sample scale. They are not sharp thresholds or high-probability claims.

The matching order describes the worst case over Efin. It does not claim that every member is hard, that rowwise add-one exploits every smaller structural subclass, or that a reset is necessary for this order on a differently initialized class. It also does not determine an optimal risk as a function of a specified minimal q, an approximate-reset defect, or a variable mixing parameter.

## 5. Exact-condition boundaries and same-target comparison

### All-state one-step reset is impossible; two-step reset is special

For K>=2, `P=Pi` cannot hold on all starting pairs. A probability pi has some positive entry at `t=(c,e)`. Choose a starting pair `s=(a,b)` with b different from c. The structural shift zero gives `P(s,t)=0`, contradicting `Pi(s,t)=pi(t)>0`. Thus a witnessing exponent q=1 is impossible even when pi has zeros. This does not make Efin empty: IID transition tables have a two-step witness.

For exact two-step reset, the unique legal path gives

    P^2((a,b),(c,e))=theta_ab(c)theta_bc(e)=pi(c,e).

Summing over e and using that each theta row sums to one yields

    theta_ab(c)=sum_e pi(c,e)=:p(c)

for every a,b,c. Hence every transition row is the same p, and substitution gives `pi(c,e)=p(c)p(e)`. Conversely these IID rows give that product law and all-state two-step reset, including zero coordinates of p. The initial pair may still be arbitrary.

The accepted S007/S005 comparison assigns this exact-two-reset class the smaller optimal expected-TV rate `min{1,sqrt(K/(M+1))}`, with pooled symbol estimation achieving it; original context-specific add-one need not. Efin does not inherit this improved rate merely because it contains IID sources. Already its exact-three-reset subclass has the full K^3 minimax difficulty by the accepted S007 lower. For K>=6 that subclass even contains legal strictly positive symbol-transition tables with `P^3=Pi` but `P^2!=Pi`. Thus finite exact forgetting and the strong row-sharing structure forced by two-step reset are different conditions.

This comparison keeps the same observed-history convention, unconditional actual-endpoint expected-TV loss, and arbitrary-initialization upper scope. The two-step IID lower may use stationary initialization as a subclass, just as the Efin lower does. No conclusion is asserted here about strict class inclusions for each small K, or a full description of kernels of any reset order.

### Sufficiency is not necessity

Exact finite reset is sufficient to erase arbitrary initialization by a bounded dimension-dependent time, recovering the stationary-order worst-case rate for the unchanged original rule. It is not necessary for the stationary-initialization guarantee supplied by S004 at `b=0,eta_0=0`.

For example, at K=2 the deterministic legal pair cycle

    00 -> 01 -> 11 -> 10 -> 00

has a uniform stationary pair law. Starting from that law, the original S004 bound at b=0 applies directly with constant 48 and rate a(K,M). But no positive power of this permutation matrix has all equal rows: distinct starting states remain distinct under every iterate of the cycle. Hence this source has no finite all-state reset. This is a concrete nonnecessity statement for stationary starts, not a claim that the entire arbitrary-start unconstrained class has the Efin minimax order.

### What the existential-q conclusion does and does not say

- A single trajectory always uses one fixed theta; only the choice of source, its witness q, and mu may vary across a minimax supremum. No time-inhomogeneous reset mechanism is introduced.
- A finite q may depend on the source and on K. On the fixed K^2-dimensional pair state space, existence nevertheless implies a uniform bound d=K^2. Nothing here asserts a K-independent bound for the whole union over K, or that d is the optimal dimension bound.
- Exact equality after finitely many steps is essential to the nilpotence premise. Approximate convergence does not give `A^q=0`; the proof cannot be applied to a small nonzero defect by dropping that defect. No sharp growing-q, approximate-forgetting, or general mixing-time rate is claimed.
- The conclusion `E_K^fin=E_K^(K^2)` is an exponent reduction, not a structural classification of all legal shift kernels. The non-IID witnesses are supplied by the accepted E3 theorem, not by a claim that all nilpotent matrices yield legal pair sources.

## 6. Explicit-rate, notation, and boundary audit

- **Exposed variables and constants:** only deterministic integers K>=2,M>=1 occur in (S009.1). The numerical lower `1/100000` is inherited from accepted S007; 48 and 13 come from accepted S004; 68 is justified by (3.7). There is no hidden dependence on q,pi,mu,theta, a stationary minimum mass, or a confidence parameter.
- **Probability/horizon/norm mode:** finite-horizon unconditional E[TV] at the actual terminal pair, after exactly M observed departures. No stopping-time, simultaneous-horizon, high-probability, TV-squared, or predictive-KL upgrade is asserted.
- **Public-facing notation:** Efin, R_fin, R_fin^+, a(K,M), and the original rule. K,M,theta,P,mu,pi,Y,C,n and TV retain the frozen meanings. The pair dimension d=K^2 and reset projection Pi are directly defined from those objects.
- **Proof-local notation:** `A=P-Pi`, `V_j=ker A^j`, the indices q,n,j,r, the deterministic analytical burn b=d, its L=M-d and eta_b, and comparison law p in the two-step boundary. Kernel stabilization, nilpotence, d-step reset, and eta_d=0 are derived facts, never new primitive assumptions.
- **No hidden estimator information:** the unknown existential q is not passed to the algorithm or inferred from observed data. Even the analysis uses the derived public d. The original rule never discards a prefix or chooses a data-dependent burn.
- **Zero stationary mass and zero legal transitions:** all matrix arguments use finite sums and no division by pi. Exact reset includes every starting pair, so initial mass outside stationary support is removed by d just as any other initial mass. S004's accepted upper explicitly covers zero counts and sparse pi. No positive denominator beyond the always-positive `n_s+K` is assumed.
- **Small horizons:** M<2d uses only the valid TV cap and the exact inequality a=1. M>=2d uses an admissible b and L>=1. The equality boundary M=2d and the smallest K=2 are included.
- **Small alphabets and all observed information:** the lower cites the accepted all-K S007 theorem, including its stationary full-N IID treatment of K=2,...,5. No initial symbols or endpoint side information are removed.
- **Arbitrary initialization:** pi is a class witness and is uniquely determined, but mu remains unconstrained. The lower selects allowed stationary examples; the upper is uniform over all mu. These different roles are not conflated.
- **Baseline reduction:** when mu=pi, using the same S004 interface with b=0 still gives the sharper accepted constant-48 stationary bound. The constant-68 class statement is a conservative uniform arbitrary-start summary, not a weakening or replacement of that inherited special-case result. The IID subclass retains its separate smaller optimal rate; a lower bound for the larger Efin class is not a lower bound for every smaller class.
