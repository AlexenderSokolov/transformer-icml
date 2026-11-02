# S007 三步完全重置仍保留二阶难度

科学正文摘录。以下保留已接纳版本的数学文字与原有编号，不重写证明；仅省略提交身份、流程元数据和历史状态。来源与依赖见 `../SOURCES.md`，逐字节映射见 `../COPY_MAP.json`。本次编排不是新的独立数学审查。

## 1. Experiment, class, algorithms, and theorem

Fix integers `K>=2,M>=1`, and write `mathcal A={0,...,K-1}`. A homogeneous second-order transition table `theta_ab(c)` has nonnegative rows summing to one. Its legal pair kernel is

    P((a,b),(b,c))=theta_ab(c),

with zero probability on all non-shift transitions. Its initial pair law `mu` is arbitrary. Observe the ENTIRE history `H=(X_1,...,X_{M+2})`, and put `Y_i=(X_{i+1},X_{i+2})` for `0<=i<=M`. The target is exactly the unknown next-symbol row `theta_{Y_M}` at this same trajectory's actual endpoint, for the unobserved `X_{M+3}`.

Define `E_K^(3)` as the class of `(theta,mu)` for which there exists a stationary probability law `pi` on `mathcal A^2` satisfying

    P^3(s,t)=pi(t) for EVERY s,t in mathcal A^2.        (E3)

Here `Pi(s,t)=pi(t)`. The all-pairs quantifier includes pairs outside stationary support, if any. The law `pi` is source-specific and is not supplied to the estimator. Equivalently, (E3) is the all-pairs minorization condition with public `q=3,beta=1`, since both sides have row sum one. The initial law need not be stationary.

An admissible estimator `T(H,U)` takes values in the K-symbol probability simplex and may use public `K,M` and the class definition. Its optional seed U is independent of the source and data. Neither its program nor parameters read hidden `theta,mu,pi` or future symbols. Put

    R_3(K,M)=inf_T sup_{(theta,mu) in E_K^(3)}
                    E_{theta,mu} TV(T(H,U),theta_{Y_M}),

    C_s(c)=sum_{i=0}^{M-1}1{Y_i=s,X_{i+3}=c},
    n_s=sum_c C_s(c),       p_s^+(c)=(C_s(c)+1)/(n_s+K),

    R_3^+(K,M)=sup_{(theta,mu) in E_K^(3)}
                       E_{theta,mu} TV(p_{Y_M}^+,theta_{Y_M}).

Throughout `TV(p,q)=(1/2)sum_c |p(c)-q(c)|`. The rule `p^+` above uses ALL M observed departures; it is not a suffix rule or a pooled rule.

**Theorem S007.** For every integer `K>=2,M>=1`,

    (1/100000) a(K,M)
      <= R_3(K,M) <= R_3^+(K,M)
      <= min{1,80 sqrt(K^3/(M+1))} <= 80 a(K,M).       (1.1)

For `K>=6`, the lower proof actually gives `a(K,M)/34560`, using only sources with uniform stationary pair law, legal symbol probabilities in `[.95/K,1.05/K]`, exact `P^3=Pi`, and `P^2!=Pi`. Every lower witness is initialized in its true stationary law. The small-alphabet lower uses stationary IID witnesses instead.

## 2. Assumptions, dependencies, and local lemma map

Primitive assumptions are precisely the finite homogeneous legal shift experiment, deterministic integer K,M, the stated information restriction, and (E3). Uniform stationarity, the perturbation cancellations, the exact reset identity, and reverse-kernel bounds are **proved** properties of a constructed subclass, not extra assumptions on `E_K^(3)`.

The checked accepted interfaces are:

1. **S004 original full-history bound, equation S004.2 and Proposition 4.** For any legal theta, stationary pi, arbitrary mu, and deterministic `0<=b<=M-1`, let `L=M-b>=1` and `eta_b=TV(mu P^b,pi)`. For the original rule defined above,

       E TV(p_{Y_M}^+,theta_{Y_M})
         <= min{1,48 K^(3/2)/sqrt(L+1)+13 sqrt(K) eta_b^(3/4)}. (2.1)

   We use this with `b=3`, only when `M>=4`. Exact reset gives `eta_3=0`. This is explicitly the accepted ORIGINAL-count/original-stack theorem, not a reassignment of its separate suffix guarantee.

2. **S005 stationary-IID full-data lower, Theorem S005-A and its Section 4 proof.** Every full-history estimator based on `N=M+2` symbols has worst-case risk on legal IID tables `theta_ab(c)=p(c)` with stationary initialization `mu=p tensor p` at least

       [1/(32 sqrt(6))] min{1,sqrt(K/(M+1))}.          (2.2)

   That proof retains all N informative IID symbols, and covers randomized estimators, zero coordinates, odd K, and M=1. Such sources satisfy (E3), so this interface applies for `2<=K<=5` without changing either the available data or the target.

3. **S002 conditional reverse mechanism.** Its stationary reversal, complete-history likelihood, finite chain rule, decoding, and testing method guide the new family. The S002 lower theorem itself is NOT imported as an exact-three-reset lower: its family need not satisfy (E3). All required statements for the present family, including its four changed reverse rows rather than two, are rederived in Lemmas 2–4 below. Finite Pinsker and randomized testing are justified locally as well.


No new external-paper theorem is used. The numerical evidence below is a diagnostic, not an assumption or proof substitute.

| Local unit | Named result / label | Contribution |
|---|---|---|
| unit_001 | Lemma 1, Three-coordinate checkerboard reset (`lem:s007-reset`) | Legal uniform-stationary family with exact P^3=Pi |
| unit_002 | Lemma 2, Complete conditional reverse experiment (`lem:s007-reverse`) | Retains all observed symbols and controls reverse visits |
| unit_003 | Lemma 3, Four-row conditional information (`lem:s007-information`) | Uniform adjacent-source testing bound |
| unit_004 | Lemma 4, Endpoint decoding and averaging (`lem:s007-lower`) | K>=6 all-estimator lower |
| unit_005 | Proposition 5, Small alphabets (`prop:s007-small`) | K=2,...,5 lower via accepted stationary IID family |
| unit_006 | Proposition 6, Original-rule arbitrary-start upper (`prop:s007-upper`) | Upper for every member of E_K^(3) |

## 3. Local derivation

### unit_001: lemma — Three-coordinate checkerboard reset (`lem:s007-reset`)

**Statement.** For every `K>=6` and `0<alpha<=1/2`, there is a family of `2^(r^3)` legal second-order tables, where `m=floor(K/3)` and `r=floor(m/2)`, such that every table has uniform stationary pair law, entries in `[(1-alpha)/K,(1+alpha)/K]`, `P^3=Pi` for every pair, and `P^2!=Pi`.

**Construction and proof.** Choose the disjoint alphabet subsets

    A={0,...,m-1},  B={m,...,2m-1},  C={2m,...,3m-1}.

The remaining symbols, if any, are unused by perturbations. In each subset pair its first 2r symbols. For `0<=i,j,l<r`, define signed functions on the entire alphabet:

    u_i(2i)=+1,       u_i(2i+1)=-1,
    v_j(m+2j)=+1,     v_j(m+2j+1)=-1,
    w_l(2m+2l)=+1,    w_l(2m+2l+1)=-1,

and set each function to zero at all other symbols. Denote the two-point supports by `A_i,B_j,C_l`, respectively. For each sign vector `sigma=(sigma_ijl) in {-1,+1}^{r^3}`, put

    F_sigma(a,b,c)=(alpha/K) sum_{i,j,l} sigma_ijl u_i(a)v_j(b)w_l(c),
    theta_ab^sigma(c)=1/K+F_sigma(a,b,c).             (3.1)

For a fixed triple at most one summand is nonzero, because each coordinate belongs to at most one pair. Thus every perturbation is zero or `+/-alpha/K`, giving the claimed positive bounds. Each function u, v, w has sum zero, so for each fixed choice of the other two coordinates,

    sum_a F_sigma(a,b,c)=sum_b F_sigma(a,b,c)
                        =sum_c F_sigma(a,b,c)=0.     (3.2)

Here each sum is a separate identity, with its other coordinates fixed. Output cancellation makes every theta row stochastic. Input cancellation makes the uniform pair law `pi(a,b)=1/K^2` stationary:

    sum_a pi(a,b) theta_ab^sigma(c)
      =(1/K^2) sum_a theta_ab^sigma(c)=1/K^2.         (3.3)

Use only the legal shift transitions to define P. For any initial pair `(a,b)` and destination `(d,e)`, the three-step paths have the form

    (a,b) -> (b,c) -> (c,d) -> (d,e),

and hence

    P^3((a,b),(d,e))
      =sum_c theta_ab^sigma(c) theta_bc^sigma(d) theta_cd^sigma(e). (3.4)

Write the three perturbations in a summand as `F_1=F_sigma(a,b,c)`, `F_2=F_sigma(b,c,d)`, and `F_3=F_sigma(c,d,e)`. Every product of at least two of them vanishes POINTWISE:

- `F_1 F_2=0`: nonzero factors would require `b in B` and `b in A`.
- `F_2 F_3=0`: nonzero factors would require `c in B` and `c in A`.
- `F_1 F_3=0`: nonzero factors would require `c in C` and `c in A`.

The three sets are disjoint. The product of all three factors vanishes for the same reason. Expanding (3.4) therefore gives exactly

    P^3((a,b),(d,e))
      = K/K^3+(1/K^2) sum_c [F_sigma(a,b,c)
                            +F_sigma(b,c,d)+F_sigma(c,d,e)]
      =1/K^2.                                      (3.5)

The three sums vanish by output-, middle-, and input-coordinate cancellation, respectively. This proves (E3) on ALL initial and destination pairs, not only on perturbed blocks or on typical histories.

Finally take any `a in A_i,b in B_j,c in C_l`. Its perturbation is nonzero. Since `b in B` cannot be in A, `theta_bc^sigma(d)=1/K` for every d. The unique two-step pair path yields

    P^2((a,b),(c,d))
      =theta_ab^sigma(c)theta_bc^sigma(d)
      =[1+alpha sigma_ijl u_i(a)v_j(b)w_l(c)]/K^2
      !=1/K^2.                                     (3.6)

Thus `P^2!=Pi`. There is no time coordinate, phase clock, changing source, or special initial phase in this construction. We initialize it with the exact uniform stationary law (3.3). ∎

### unit_002: lemma — Complete conditional reverse experiment (`lem:s007-reverse`)

**Statement.** For a source constructed in Lemma 1, initialized with its uniform stationary law, fix any endpoint s. Conditional on `Y_M=s`, the ENTIRE observed history is exactly the reverse chain `Z_t=Y_{M-t}`, `0<=t<=M`, started at `Z_0=s`, with legal reverse transitions

    Q_sigma((b,c),(a,b))=theta_ab^sigma(c).          (3.7)

For every pair z, reverse start s, and `t>=2`,

    Pr_sigma^s(Z_t=z)<=(1+alpha)^2/K^2.              (3.8)

**Proof.** Stationarity and the common positive pair masses give the reverse formula `Q(y,x)=pi(x)P(x,y)/pi(y)`, which here is exactly (3.7). Input cancellation makes these rows sum to one. The pair path and the full symbol history determine each other bijectively: Y_0 gives the first two symbols, and each succeeding pair gives the next symbol. For each legal path ending at s, its conditional mass is

    [K^(-2) product_{i=0}^{M-1} P_sigma(y_i,y_{i+1})]/K^(-2)
      =product_{i=0}^{M-1} Q_sigma(y_{i+1},y_i).     (3.9)

Thus both original initial symbols and every intermediate observation remain in the conditional experiment. There is no independent query or deleted side information.

From `(u,v)` to `(a,b)` there is a unique legal two-step reverse path, via `(b,u)`. Therefore

    Q_sigma^2((u,v),(a,b))
      =theta_bu^sigma(v)theta_ab^sigma(u)
      <=(1+alpha)^2/K^2.                            (3.10)

For t>=2 average this bound over the law of `Z_{t-2}`. This proves (3.8), without asserting it at t=0 or t=1. ∎

### unit_003: lemma — Four-row conditional information (`lem:s007-information`)

**Statement.** Under Lemmas 1–2, let `mathsf P_sigma^s` be the law of the complete H conditional on `Y_M=s`. If `sigma'` differs from sigma in one bit `(i,j,l)`, then, uniformly in s and every other sign,

    D(mathsf P_sigma^s || mathsf P_sigma'^s)
      <=16 alpha^2/K+72 alpha^2 M/K^3.               (3.11)

With `alpha=a(K,M)/20`, this is at most `1/5`, and

    TV(mathsf P_sigma^s,mathsf P_sigma'^s)<1/2.       (3.12)

**Proof.** The reversed kernels differ in exactly the four rows

    D_ijl=B_j x C_l.                                (3.13)

Within any one of those rows, only the two outgoing first symbols in A_i change, exchanging `(1+alpha)/K` with `(1-alpha)/K`. Other output pairs may carry other signs but are unchanged. The exact changed-row relative entropy is consequently

    (2alpha/K) log((1+alpha)/(1-alpha))<=8alpha^2/K. (3.14)

The inequality uses `log((1+alpha)/(1-alpha))<=2alpha/(1-alpha)<=4alpha` for `alpha<=1/2`, obtained by bounding the integral of 1/x on `[1-alpha,1+alpha]`. Unchanged rows contribute zero.

There are M reversed departures, at `t=0,...,M-1`. The first two departure times are bounded separately, and (3.8) applies thereafter. Thus

    E_sigma^s sum_{t=0}^{M-1}1{Z_t in D_ijl}
      <=min(M,2)+(M-2)_+ 4(1+alpha)^2/K^2
      <=2+9M/K^2.                                  (3.15)

This is valid also for M=1 and M=2. Both conditional path laws start from the SAME deterministic s and are positive on the SAME finite legal-path support. Expand the logarithm of the product likelihood (3.9) and take its expectation; the finite relative-entropy chain rule gives

    D(mathsf P_sigma^s || mathsf P_sigma'^s)
      =sum_{t=0}^{M-1} E_sigma^s
             D(Q_sigma(Z_t,.) || Q_sigma'(Z_t,.))
      <=(8alpha^2/K)(2+9M/K^2),                     (3.16)

which is (3.11). There is no missing initial-law KL term or unobserved extra data in this equality.

For the specified amplitude, `alpha<=1/20` and

    alpha^2 M/K^3
      =(1/400) min{1,K^3/(M+1)} M/K^3 <=1/400.

Using only K>=2, (3.11) is at most

    16/(400 K)+72/400 <=1/50+9/50=1/5.              (3.17)

For completeness, finite Pinsker states `TV(p,q)<=sqrt(D(p||q)/2)` on a common finite positive support. To see it, take `B={p>=q}`, `u=p(B)`, `v=q(B)`, so `u-v=TV(p,q)`. The zero-TV case is immediate. Otherwise `0<v<1`; Jensen for the convex function `z log z` on B and its complement gives `D(p||q)>=d(u||v)`. As a function of u, binary relative entropy has value and derivative zero at u=v and second derivative `1/[u(1-u)]>=4`. Integrating twice and extending continuously at endpoints yields `d(u||v)>=2(u-v)^2`. Applying this to (3.17) gives `TV<=sqrt(1/10)<1/2`, proving (3.12). This KL is between complete-data laws for testing only; it is not a predictive-KL loss claim. ∎

### unit_004: lemma — Endpoint decoding and averaging (`lem:s007-lower`)

**Statement.** For `K>=6,M>=1`, the stationary family of Lemma 1 with `alpha=a(K,M)/20` satisfies, for EVERY admissible randomized estimator T,

    2^(-r^3) sum_sigma E_{theta^sigma,pi}
                         TV(T(H,U),theta^sigma_{Y_M})
      >=alpha r^3/K^3 >=a(K,M)/34560.                (3.18)

**Proof.** Fix an actual endpoint `s=(a,b)` with `a in A_i,b in B_j`. For each `0<=l<r`, let `c_l^+=2m+2l` and `c_l^-=2m+2l+1`. Decode the sign sigma_ijl from the estimator by

    hat_sigma_{s,l}=+1 if u_i(a)v_j(b)[T(c_l^+)-T(c_l^-)]>=0,
                    -1 otherwise.                  (3.19)

The tie rule is fixed and source-independent. The true signed difference is

    u_i(a)v_j(b)[theta_ab^sigma(c_l^+)-theta_ab^sigma(c_l^-)]
       =(2alpha/K) sigma_ijl.                       (3.20)

A wrong decoded sign, including an erroneous tie when the true sign is negative, forces the two-coordinate absolute error to be at least `2alpha/K`, by the triangle inequality applied to the difference. The C_l pairs are disjoint, so pointwise

    TV(T,theta_s^sigma)
      >=(alpha/K) sum_{l=0}^{r-1}1{hat_sigma_{s,l}!=sigma_ijl}. (3.21)

Place the uniform prior on the r^3 signs. Every source has terminal law `pi(s)=1/K^2`, so conditioning this prior on the actual endpoint leaves it uniform. Fix s and l, and pair each sign vector with its flip at `(i,j,l)`. The two full conditional data laws have TV below 1/2 by Lemma 3.

For any randomized binary test between finite laws p,q, let `f(h) in [0,1]` be its probability of choosing the first hypothesis after integrating its independent seed. The sum of its two error probabilities is

    1-sum_h f(h)[p(h)-q(h)] >=1-TV(p,q)>=1/2.       (3.22)

The bound follows because the sum over positive differences p-q is TV. Thus pairing and averaging the two signs, and then averaging the other signs, gives

    2^(-r^3) sum_sigma
      Pr_sigma^s{hat_sigma_{s,l}!=sigma_ijl}>=1/4.   (3.23)

This is conditional testing at the very SAME endpoint indexing the loss, not unconditional testing followed by a substituted query.

There are `(2r)(2r)=4r^2` active endpoints in the paired portion of `A x B`, each of mass `1/K^2`. Each has r disjoint output pairs. Average (3.21), use (3.23), and discard only the nonnegative loss at other endpoints:

    2^(-r^3) sum_sigma E_sigma TV(T,theta^sigma_{Y_M})
      >=(1/K^2)(4r^2)(alpha/K)(r/4)
      =alpha r^3/K^3.                              (3.24)

The needed rounding bound holds for every K>=6. For `6<=K<=11`, `r=1>=K/12`. For K>=12, write `K=6q+t`, `0<=t<=5`; then `m=2q+floor(t/3)` and `r=q=floor(K/6)`. Therefore `r>=K/6-1>=K/12`. Combining with `alpha=a/20` gives

    alpha r^3/K^3 >=a/(20*12^3)=a/34560.

For every T its supremum risk is at least this finite-prior average. The constructed family depends only on the public K,M and not on T, and its source is fixed along each trajectory. Taking infimum over all T proves the stated lower bound on R_3 for K>=6. Revealing the subclass's common uniform stationary law would not change the proof or reveal its signs. ∎

### unit_005: proposition — Small alphabets (`prop:s007-small`)

**Statement.** For `2<=K<=5,M>=1`,

    R_3(K,M)>=a(K,M)/(160 sqrt(6))>a(K,M)/100000.   (3.25)

**Proof.** If every transition row equals an unknown p, then `P^2=Pi_p`, where `pi_p=p tensor p` is stationary; hence `P^3=Pi_p P=Pi_p`. The stationary initialization `mu=pi_p` is therefore a legal member of E_K^(3). It makes all N=M+2 observed symbols IID p, and the actual target row is p, exactly as required for the accepted full-data lower (2.2). Any estimator for E_K^(3), restricted to this subclass, is one of the full-history estimators covered by that lower; knowledge of E3 rather than a hidden p supplies no extra parameter information.

Put `x=sqrt(K/(M+1))`. Since `min{1,Kx}<=K min{1,x}` for K>=1,

    min{1,sqrt(K/(M+1))}>=a(K,M)/K>=a(K,M)/5.

Apply (2.2). Finally `sqrt(6)<3` gives `160sqrt(6)<480<100000`. This proves (3.25), with no deletion of the first two informative observations and no nonstationary initialization. ∎

### unit_006: proposition — Original-rule arbitrary-start upper (`prop:s007-upper`)

**Statement.** For EVERY source and arbitrary initial law in E_K^(3), every K>=2,M>=1 satisfies the upper bound in (1.1) for the original full-history rule.

**Proof.** If M>=4, take the deterministic analytical burn `b=3`, so `L=M-3>=1`. Exact reset from every pair gives `mu P^3=pi` for every mu, including initial mass outside stationary support. Hence `eta_3=0`, and the checked ORIGINAL-rule bound (2.1) gives

    E TV(p_{Y_M}^+,theta_{Y_M})
      <=min{1,48 K^(3/2)/sqrt(M-2)}.                (3.26)

For M>=4,

    (M+1)/(M-2)=1+3/(M-2)<=5/2,
    48 sqrt(5/2)<76<80,

where the strict first numerical inequality follows by squaring: `48^2*(5/2)=5760<5776=76^2`. Thus (3.26) is at most `min{1,80 sqrt(K^3/(M+1))}`.

If M<=3, then `K^3/(M+1)>=8/4=2`, so a(K,M)=1 and the elementary TV cap one already proves the same bound. No inadmissible burn is used at these small horizons.

Take the supremum over E_K^(3). The original rule is one admissible common estimator, so `R_3<=R_3^+`. Finally, for `t=sqrt(K^3/(M+1))`, `min{1,80t}<=80 min{1,t}`. This completes the upper chain. The actual algorithm retains its first three departures and reads none of b, mu, pi, or theta; b=3 is only a choice in the proved risk bound. ∎

## 4. Target-step assembly and exact-condition interpretation

Lemma 1 supplies the new algebraic hard family. Lemmas 2–3 retain the full endpoint-conditional experiment and control information about each bit, including both startup departures. Lemma 4 turns this into actual-endpoint mean-TV risk and then an all-algorithm minimax lower for K>=6. Proposition 5 covers all remaining K using the accepted full-data stationary IID family. Both lower constants exceed the exported `1/100000`. Proposition 6 independently supplies the arbitrary-initialization original-add-one upper. This proves every inequality of Theorem S007.

The contrast to accepted S005 is precise. At all-row exact TWO-step reset, the unique pair path gives

    theta_ab(c)theta_bc(d)=pi(c,d).

Summing over d forces `theta_ab(c)=sum_d pi(c,d)=p(c)` for every a,b,c. This is the shared-row IID class, whose optimal expected-TV rate is `min{1,sqrt(K/(M+1))}` and for which the original rowwise add-one need not attain the improved class rate. At exact THREE-step reset, the three-coordinate cancellations in Lemma 1 allow `r^3` unknown sign directions while the initial pair is still forgotten exactly in three transitions. Its class minimax rate remains `min{1,sqrt(K^3/(M+1))}`, and the original rowwise add-one attains that rate.

Thus even a source-uniform, finite exact reset time does not by itself imply an IID-size statistical dimension. What changes at reset order two is a structural identity among all transition rows, not merely a better numerical mixing bound. This comparison has the SAME observed-history convention, actual endpoint, expected-TV loss, and arbitrary-initialization upper quantifiers in both classes.

The result does not claim that every individual three-reset source is hard; the IID subclass remains easier. It does not classify all kernels satisfying E3, characterize all q>3 reset classes, prove a sharp approximate-reset transition, or give optimal predictive-KL or expected-squared-TV rates. No implication that mixing is necessary for the previously accepted stationary rate is made. The q=3 theorem is the authorized exact condition boundary, not a replacement for the separate near-IID route.

## 5. Explicit rate, notation, and boundary audit

- **Exposed variables:** deterministic integers K>=2,M>=1; no unexposed parameter in either numerical theorem constant. The only loss exported is unconditional E[TV] at the actual terminal row. No high-probability, all-time, stopping-time, squared-loss, or predictive-KL upgrade is made.
- **Public-facing objects:** E_K^(3), R_3, R_3^+, a(K,M), and the frozen original rule. Its admissibility is identical to the frozen experiment.
- **Proof-local objects:** m,r,A/B/C and their pairs, u/v/w, sigma,F,alpha,Q,Z, the endpoint-conditional laws, the changed-row set, and decoded signs. They are constructed explicitly from K,M or the chosen hard family. They are not hidden inputs to T. The constants in the visits and KL bounds are derived in Lemma 3; the lower rounding constant is derived in Lemma 4; the upper constant comes from the checked S004 interface and the displayed horizon ratio.
- **Stationarity and homogeneity:** all lower witnesses use a genuine stationary pair law, fixed through the entire trajectory. The K>=6 family uses one common uniform pair law independent of all signs and horizons. There is no clock, added state, or horizon-aligned phase. Horizon dependence occurs only in the allowed choice of a fixed amplitude inside the minimax supremum.
- **Structural zeros:** only legal `(a,b)->(b,c)` transitions are used; positivity is asserted only for legal symbol probabilities. The whole class may have zeros; the upper proof permits them. The constructed positive legal-transition subclass is enough for the lower.
- **All observed information:** the new conditional likelihood includes the initial pair and all M transitions. The small-K imported lower includes all N=M+2 IID observations. Endpoint conditioning is a proof device, not extra estimator data or a changed loss.
- **Random endpoint and visit correlation:** no selected-row IID or conditional visit independence is asserted. Reversal and endpoint-uniform testing explicitly handle their dependence.
- **Small and odd alphabets:** K=2,...,5 have a separate valid stationary subclass proof. For K>=6 all unused symbols and unpaired symbols receive baseline entries; cancellation and the rounding estimate are valid for every remainder modulo six.
- **Small horizons:** startup visits are bounded separately at M=1,2, and the upper uses only the TV cap for M<=3. No zero-count division occurs anywhere in the lower. Zero-count behavior of the original upper is contained in the accepted S004 theorem.
- **Baseline consistency:** the conservative E3 class lower is not a claim that the IID subset's minimax risk has increased. The E3 class strictly allows non-IID tables for K>=6, while restricting to exact two-reset recovers S005's distinct, smaller class and pooled rate. The original upper uses the accepted exact-reset eta=0 specialization without pretending the entire arbitrary-start history is stationary.
- **Necessary/sufficient sample scale:** with c=1/100000, if `0<delta<c`, worst-case mean TV <=delta requires `M+1>=c^2 K^3/delta^2` by the lower. The original rule suffices whenever `M+1>=80^2 K^3/delta^2`. These loose constants express the proved `K^3/delta^2` scale, not a sharp threshold or a high-probability guarantee.

