# S004 混合条件下原算法与 suffix 算法

科学正文摘录。以下保留已接纳版本的数学文字与原有编号，不重写证明；仅省略提交身份、流程元数据和历史状态。来源与依赖见 `../SOURCES.md`，逐字节映射见 `../COPY_MAP.json`。本次编排不是新的独立数学审查。

## 1. Exact setting and exported conclusions

Fix integers `K>=2`, `M>=1`. Let `A={0,...,K-1}`, `S=A²`, and let theta be any homogeneous second-order transition table, with zero legal transition probabilities permitted. Its pair kernel is

    P((a,b),(b,c))=theta_ab(c),

with zero entries on non-shift transitions. Let pi be any stationary probability law of P, and let the initial pair law mu be arbitrary. Observe exactly `X_1,...,X_{M+2}`, equivalently `Y_i=(X_{i+1},X_{i+2})`, `0<=i<=M`. The target is always the actual endpoint row `theta_{Y_M}` for the unobserved `X_{M+3}`.

For a deterministic integer burn index `0<=b<=M-1`, set

    L=M-b >= 1,                 eta_b=TV(mu P^b,pi).

The ORIGINAL full-history rule and the genuinely different suffix rule are

    C_s(c)=sum_{i=0}^{M-1} 1{Y_i=s,X_{i+3}=c},
    n_s=sum_c C_s(c),           p^+_s(c)=(C_s(c)+1)/(n_s+K),

    C_s^[b](c)=sum_{i=b}^{M-1} 1{Y_i=s,X_{i+3}=c},
    n_s^[b]=sum_c C_s^[b](c),   p_s^{+, [b]}(c)=(C_s^[b](c)+1)/(n_s^[b]+K).

Both predict at the SAME observed endpoint `Y_M`. The suffix rule discards the first b departures, not the endpoint or an independently selected query. At `b=0` the two rules coincide.

**Theorem S004 (source-specific finite bounds).** For every source, stationary pi, arbitrary mu and deterministic b as above,

    E_{theta,mu} TV(p_{Y_M}^{+, [b]},theta_{Y_M})
      <= min{1, u_stat(K,L)+eta_b},                         (S004.1)

where `u_stat(K,L)=min{1,48 K^(3/2)/sqrt(L+1)}`, and, separately,

    E_{theta,mu} TV(p^+_{Y_M},theta_{Y_M})
      <= min{1, 48 K^(3/2)/sqrt(L+1)
                   +13 sqrt(K) eta_b^(3/4)}.              (S004.2)

The essential original-count bridge is, for every integer `w>=1`,

    P_{theta,mu}(n_{Y_M}<w)
      <= min{1,K²w/(L+1)+eta_b}.                           (S004.3)

The full-history estimator in (S004.2) is unchanged and does not read b, pi, mu, theta, or eta_b. Thus b is only an analytical choice for this bound. For (S004.1), b is part of the algorithm: a common predictor must choose it from public information, not from the hidden source. All assertions are for fixed deterministic horizons and burns, not data-selected stopping times.

For the explicit uniform-mixing consequence, define `D_K(q,beta)` to be the class of `(theta,mu)` for which some stationary pi satisfies

    P^q(s,t) >= beta pi(t)   for EVERY s,t in A²,           (D)

where the public parameters obey integer `q>=1`, `0<beta<=1`; mu remains arbitrary. Pointwise upper statements are meaningful whenever a source satisfies (D); class-risk statements below are restricted to `q>=2`, since the all-pairs q=1 class is empty as proved below. Define the envelope, without using an ambiguous `0^0`, by

    h_{q,beta}(b)=(1-beta)^floor(b/q),       beta<1;
    h_{q,1}(b)=1 if b<q, and 0 if b>=q.                    (S004.4)

Then `eta_b<=h_{q,beta}(b)`, and both (S004.1) and (S004.2) hold uniformly on `D_K(q,beta)` with eta_b replaced by this envelope. The stronger bound retaining `TV(mu,pi)` is proved below.

Let `a(K,M)=min{1,sqrt(K³/(M+1))}`. For `q>=2`, under the explicit sufficient burn condition

    b=floor(M/2),        h_{q,beta}(b)<=1/(M+1),            (B)

the two uniform bounds give, respectively,

    sup_{D_K(q,beta)} E TV(p_{Y_M}^{+, [b]},theta_{Y_M}) <= 69 a(K,M),
    sup_{D_K(q,beta)} E TV(p^+_{Y_M},theta_{Y_M})         <= 81 a(K,M),       (S004.5)

and each risk is also at most one. These are sufficient bounds, not sharp dependence on a growing mixing time or on beta approaching one.

For every `q>=2`, `0<beta<1`, the class has the lower bound

    inf_A sup_{D_K(q,beta)} E TV(A(H,U),theta_{Y_M})
       >= (tau_beta/18) a(K,M),
    tau_beta=min{1/10,1-sqrt(beta)} > 0.                  (S004.6)

The estimator in the infimum may use the public q,beta and all observed history, together with an independent seed, but no hidden source parameters. For `q=2,beta=.81`, (S004.6) is exactly the accepted S002 constant `1/180`. Thus fixed `q>=2,beta<1` permits matching stationary-order mean-TV bounds once (B) holds; the constants are explicitly nonuniform as `beta` tends to one. The endpoint `beta=1` is NOT covered by (S004.6).

Two structural boundaries are proved below:

1. With the all-pairs quantifier in (D), `D_K(1,beta)` is empty for every `K>=2,beta>0`, even if pi does not have full support.
2. For `q=2,beta=1`, (D) is equivalent to an IID symbol-transition table `theta_ab(c)=p(c)` with `pi=p tensor p`. This assertion is NOT extended to `q>2`. The optimal IID endpoint rates and an original-add-one versus pooled-algorithm comparison are left to a separate successor unit.

## 2. Assumptions, dependencies, and local lemma map

### Allowed assumptions and checked dependency interfaces

The primitive assumptions are only the finite legal pair-shift experiment, homogeneity, arbitrary mu, stationary pi, and the displayed deterministic-index conditions. The minorization (D) is an additional local hypothesis used only for the mixing-class corollaries. It is not assumed for the source-specific theorem.



The accepted interfaces used here, with assumptions discharged, are:

1. **Stationary occupancy and risk (S001, Sections 3 and 7).** For the same theta started at pi and any length `L>=1`, its actual terminal count satisfies `P(J_L<w)<=min{1,K²w/(L+1)}` for every integer w>=1, and its length-L add-one risk is at most `u_stat(K,L)`. The suffix started from pi is precisely this experiment; no irreducibility or mixing assumption is needed.
2. **Deterministic-stack maximum (S001, Sections 4 and 5, inherited there from L1MAX).** With independent 2M-symbol stacks of row laws theta_s and centered partial sums `S_{s,j}`, for deterministic `1<=v<=M`,

       Z_v=max_s max_{0<=j<=2v} ||S_{s,j}||_1,
       ||Z_v||_4 <= (25/4) sqrt(Kv),
       D(x)=sum_{ell>=0}2^(-ell/2) min{1,x2^ell}^(3/4) <= 10 sqrt(x), x>0.

   These deterministic-stack inequalities contain no initial-law assumption. The exact arbitrary-mu path coupling is given again below, so using this interface does not silently transfer stationary independence.
3. **Stationary hard family (S002, Sections 1–6).** The legal uniform-stationary hypercube has row probabilities in `[(1-alpha)/K,(1+alpha)/K]`. For any `0<alpha<=a(K,M)/10`, its full-history endpoint-conditional testing distance is below 1/2, and every common estimator has prior-average actual-endpoint TV risk at least `alpha/18`. Its two-step kernel satisfies `P²>= (1-alpha)² Pi`, where Pi has every row pi. S002 writes its final choice as `alpha=a/10`; the inequalities preceding that choice are monotone in alpha. The scaling check required for (S004.6) is supplied explicitly in Proposition 7 below.


No external theorem or web source is newly invoked. No MM5 nonstationary witness, reversible spectral-gap theorem, independent-query result, or suffix-averaged KL result is a premise.

| Local unit | Named result and label | Contribution |
|---|---|---|
| unit_001 | Lemma 1, Suffix path-law transfer (`lem:s004-path`) | Exact eta_b path distance; suffix risk and original-count floor |
| unit_002 | Lemma 2, Arbitrary-start finite stacks (`lem:s004-stacks`) | Original full-history count identity and initialization-free L4 maximum |
| unit_003 | Lemma 3, Floor-occupancy empirical bound (`lem:s004-empirical`) | Unconditional dyadic Holder with additive eta_b floor |
| unit_004 | Proposition 4, Smoothing and original-rule bound (`prop:s004-full`) | Real thresholds, zero counts, constants 48 and 13 |
| unit_005 | Lemma 5, Minorization contraction (`lem:s004-doeblin`) | Correct q,beta envelope, including beta=1 |
| unit_006 | Corollary 6, Sufficient burn and stationary-order upper (`cor:s004-burn`) | Explicit finite parameter absorption |
| unit_007 | Proposition 7, Fast-mixing hard subclass (`prop:s004-lower`) | Accepted S002 family and beta-dependent scaled lower |
| unit_008 | Proposition 8, One-step obstruction and exact two-step reset (`prop:s004-boundary`) | Structural zeros and beta=1 IID collapse |
| unit_009 | Proposition 9, Sufficiency is not necessity (`prop:s004-scope`) | Nonmixing stationary example and lack of uniformity from bare positivity |

## 3. Local derivation

### unit_001: lemma — Suffix path-law transfer (`lem:s004-path`)

**Statement.** Under the source-specific setting in Section 1, the law of `(Y_b,...,Y_M)` from mu and the law of a length-L path from pi have TV distance exactly eta_b. Consequently (S004.1) and (S004.3) hold.

**Proof.** Let Q_L be the Markov kernel taking a starting pair s to a pair path `(z_0,...,z_L)` with `z_0=s`, then L transitions of the SAME P. The suffix law from mu is `(mu P^b)Q_L`; its stationary comparison law is `pi Q_L`. For any two finite laws nu,rho and a Markov kernel Q,

    sum_z |sum_s (nu(s)-rho(s))Q(s,z)|
      <= sum_s |nu(s)-rho(s)| sum_z Q(s,z)
      =sum_s |nu(s)-rho(s)|.

Dividing by two proves TV contraction and hence distance at most eta_b. Conversely, projecting the suffix path to its first pair gives the two starting laws, so contraction for that projection proves distance at least eta_b. Equality follows. This equality uses the observed first pair of the suffix; it does not say that the FULL path distance has contracted after b steps.

For any finite laws nu,rho and any fixed function `0<=g<=1`,

    E_nu g-E_rho g <= sum_{x:nu(x)>rho(x)}(nu(x)-rho(x)) = TV(nu,rho).

Apply this to suffix add-one loss, a bounded function of the suffix with the same fixed theta under both laws. Under pi, S001 at length L applies, giving (S004.1) after the cap one. The algorithm need not know theta for theta to occur in its risk function.

Put `J=n_{Y_M}` and `J_b=n_{Y_M}^[b]`. Since the first sum includes every term of the suffix sum, `J>=J_b` PATHWISE. Therefore, for every integer w>=1,

    P_mu(J<w) <= P_mu(J_b<w)
       <= P_pi(length-L terminal count <w)+eta_b
       <= min{1,K²w/(L+1)}+eta_b.

Taking the additional probability cap one gives precisely `min{1,K²w/(L+1)+eta_b}`: if `K²w/(L+1)>=1` both capped expressions equal one, and otherwise they coincide. This proves (S004.3). All state and endpoint/count dependence remains in the event. ∎

### unit_002: lemma — Arbitrary-start finite stacks (`lem:s004-stacks`)

**Statement.** Under the setting in Section 1, including arbitrary mu, the ORIGINAL M-departure path has a finite row-stack realization with

    C_s-n_s theta_s=S_{s,n_s}

pathwise and `||Z_v||_4 <= (25/4)sqrt(Kv)` for every deterministic integer `1<=v<=M`.

**Proof.** Draw `Y_0~mu`, independently of mutually independent row variables `xi_{s,l}~theta_s`, `s in S,1<=l<=2M`. At each departure from s consume its next unused row symbol and make the legal pair shift. No row consumes more than M entries during the observed path. A prescribed symbol prefix `x_1,...,x_{i+2}` fixes the initial pair and exactly the consumed prefix in every stack, so its probability is

    mu(x_1,x_2) product_{r=0}^{i-1} theta_{x_{r+1},x_{r+2}}(x_{r+3}),

the original path probability. Zero-probability paths cause no conditioning on null events. Defining `S_{s,j}=sum_{l=1}^j(e_{xi_{s,l}}-theta_s)` gives the claimed count identity on every constructed path.

The maximum Z_v depends only on deterministic finite stack prefixes, whose product distribution is the same as in the accepted S001 maximal analysis, irrespective of mu. For transparency, the relevant bounds there are

    E max_{j<=2v}||S_{s,j}||_1 <= sqrt(8Kv),
    P(max_{j<=2v}||S_{s,j}||_1 - its mean >t) <= exp(-t²/(4v)).

The first follows from the finite L2 submartingale maximum inequality and `E||S_{s,2v}||_2²<=2v`; the second follows because changing one stack symbol changes the entire L1 prefix maximum by at most two. A union over K² rows and tail integration, as explicitly proved and reviewed in S001, yield

    ||Z_v||_4 <= sqrt(8Kv)+sqrt(8v log K)+32^(1/4)sqrt(v)
              <= (25/4)sqrt(Kv),

using `K>=2`. Every hypothesis of that accepted deterministic-prefix result is thus unchanged. The selected row, selected count and stack deviations may be dependent; no conditional iid assertion is made. ∎

### unit_003: lemma — Floor-occupancy empirical bound (`lem:s004-empirical`)

**Statement.** Under the source-specific setting, set `c=K²/(L+1)` and `eta=eta_b`. On `{J>=1}` define the ORIGINAL empirical terminal row `p_hat=C_{Y_M}/J`, and define its loss times `1{J>=1}` to be zero at J=0. Then

    E[TV(p_hat,theta_{Y_M})1{J>=1}]
       <= (125 sqrt(2)/4)sqrt(Kc)
             +(25/8)(2+sqrt(2))sqrt(K) eta^(3/4).       (3.1)

**Proof.** For deterministic dyadic `v=2^ell<=M`, put `E_v={v<=J<2v}`. On this event the count identity and the original-stack maximum of Lemma 2 give

    TV(p_hat,theta_{Y_M}) = ||S_{Y_M,J}||_1/(2J) <= Z_v/(2v).

Apply Holder with exponents 4 and 4/3 UNCONDITIONALLY, then use the integer threshold `w=2v` in Lemma 1:

    E[TV(p_hat,theta_{Y_M})1{E_v}]
       <= (25/8)sqrt(K) v^(-1/2) min{1,2cv+eta}^(3/4). (3.2)

For `x,y>=0`,

    min{1,x+y}^(3/4) <= min{1,x}^(3/4)+y^(3/4).       (3.3)

If x>=1 the right side is at least one; if x<1, use `(x+y)^r<=x^r+y^r` for `r=3/4`. One direct verification of this last inequality fixes x>0, differentiates `(x+y)^r-y^r` in y>0 to see it is nonincreasing, and takes y down to zero; x=0 is equality.

The events `E_{2^ell}`, `0<=ell<=floor(log_2 M)`, partition `{1<=J<=M}`, including J=M. Sum (3.2), use (3.3), and extend ONLY the nonnegative numerical series, not the stacks, beyond this finite range. The accepted S001 dyadic estimate gives

    sum_{ell>=0} 2^(-ell/2) min{1,2c 2^ell}^(3/4)
      <=10 sqrt(2c),

and the other geometric series equals

    sum_{ell>=0}2^(-ell/2)=2+sqrt(2).

Multiplication by `(25/8)sqrt(K)` proves (3.1). Even the last used stack maximum exists because `2v<=2M`. Neither the endpoint nor the occupancy layer is conditioned away. ∎

### unit_004: proposition — Smoothing and the original rule (`prop:s004-full`)

**Statement.** Under the source-specific setting, the full-history add-one rule satisfies (S004.2), with constants 48 and 13 uniform in all exposed parameters and sources.

**Proof.** Keep `c=K²/(L+1)`, `eta=eta_b`. The floor-occupancy bound at w=1 gives

    P(J=0)<=min{1,c+eta}<=min{1,c}+eta<=sqrt(c)+eta.    (4.1)

For any real `A_0>=0`, define

    Psi(0)=0;
    Psi(z)=z(1+log(1/z)) for 0<z<1;
    Psi(z)=1 for z>=1.

We claim

    E min{1,A_0/(J+K)} <= Psi(c A_0)+eta
                       <=2 sqrt(c A_0)+eta.           (4.2)

When `A_0=0` this is immediate. For `A_0>0`, `0<t<1`, put `x=A_0/t-K`. The tail event is `{J<x}`, empty if x<=0. If x>0, integer J gives `{J<x}={J<ceil(x)}`, and

    1<=ceil(x)<=x+1=A_0/t-K+1<=A_0/t.

Thus Lemma 1 bounds the tail probability by

    min{1,c A_0/t+eta} <= min{1,c A_0/t}+eta.

Integrating over t in (0,1) proves the first inequality of (4.2). Direct integration gives Psi, while `min{1,z/t}<=sqrt(z/t)` gives its upper bound `2sqrt(z)`. This treats exact integer x, noninteger thresholds and J=0 correctly.

On J>=1, with u the uniform distribution on A,

    p^+_{Y_M}=[J/(J+K)]p_hat+[K/(J+K)]u.

Hence its TV loss is at most the empirical loss plus `K/(J+K)`. At J=0 its loss is at most one. Enlarging the nonnegative smoothing term to all paths is conservative and yields

    E TV(p^+_{Y_M},theta_{Y_M})
       <=P(J=0)+E[TV(p_hat,theta_{Y_M})1{J>=1}]
                       +E min{1,K/(J+K)}.

Apply (4.1), Lemma 3, and (4.2) with `A_0=K`. Since `sqrt(c)<=sqrt(Kc)`, this is at most

    [125 sqrt(2)/4+3]sqrt(Kc)
       +(25/8)(2+sqrt(2))sqrt(K) eta^(3/4)+2eta.

For `0<=eta<=1`, `eta<=eta^(3/4)` (including eta=0); since `sqrt(K)>=1`, the last term is at most `2sqrt(K)eta^(3/4)`. The exact coefficient checks are

    125 sqrt(2)/4+3 < 48,
    (25/8)(2+sqrt(2))+2 < 13.

For the first use `sqrt(2)<36/25`; for the second use `sqrt(2)<38/25`, giving an upper bound `(25/8)(88/25)+2=13`. Therefore the total is at most `48sqrt(Kc)+13sqrt(K)eta^(3/4)`. Substitute `sqrt(Kc)=K^(3/2)/sqrt(L+1)` and cap by one to get (S004.2). No KL or squared-TV target has replaced the mean-TV loss. ∎

### unit_005: lemma — Minorization contraction (`lem:s004-doeblin`)

**Statement.** Under the setting and additional hypothesis (D), for `b=kq+r`, integers `k>=0`, `0<=r<q`,

    TV(mu P^b,pi) <= (1-beta)^k TV(mu,pi)   if beta<1;

if beta=1 this distance is at most `TV(mu,pi)` when k=0 and is zero when k>=1. In particular (S004.4) is a valid uniform envelope.

**Proof.** Let Pi be the kernel with every row equal to pi. If beta<1,

    R=(P^q-beta Pi)/(1-beta)

has nonnegative entries and row sums one. Stationarity gives `pi R=pi`. Consequently, for every law nu,

    nu P^q-pi=(1-beta)(nu R-pi R),

and finite-kernel TV contraction, proved in Lemma 1, gives a factor `(1-beta)` for each q-block. Iterating k times and then applying the remaining r transitions, which also contract TV and preserve pi, proves the claim. The k=0 case has factor one without any burn.

If beta=1, (D) and equality of row sums force `P^q=Pi` entrywise. Thus `mu P^b=pi` whenever b>=q; for b<q apply only TV contraction. This proves the stated boundary convention without interpreting `0^0`. The proof requires no reversibility. ∎

### unit_006: corollary — Sufficient burn and stationary-order upper (`cor:s004-burn`)

**Statement.** Under (D), for any admissible deterministic b the source-specific bounds hold with eta_b replaced by `h_{q,beta}(b)`. Under (B), (S004.5) holds. A fully explicit sufficient test for (B), for beta<1, is

    floor(M/(2q)) >= log(M+1)/[-log(1-beta)].           (6.1)

For beta=1, `M>=2q` suffices. For every fixed q and beta>0 the corresponding sufficient condition holds for all sufficiently large M.

**Proof.** Substitute Lemma 5 into the nondecreasing right sides of (S004.1) and (S004.2). When `b=floor(M/2)`, `L=ceil(M/2)>=1` and

    L+1 >= (M+1)/2,
    K^(3/2)/sqrt(L+1) <= sqrt(2) T,
    T=K^(3/2)/sqrt(M+1).

Under (B), `eta_b<=1/(M+1)`. In particular `eta_b<=T`, since `1/(M+1)<=K^(3/2)/sqrt(M+1)`. Also

    sqrt(K) eta_b^(3/4)
       <=sqrt(K)/(M+1)^(3/4)
       <=K^(3/2)/sqrt(M+1)=T,

where the last ratio is `1/[K(M+1)^(1/4)]<=1`. Therefore the suffix bound is at most `(48sqrt(2)+1)T<69T`, and the original-rule bound is at most `(48sqrt(2)+13)T<81T`. Taking the cap one and using `min{1,C T}<=C min{1,T}` proves (S004.5).

For integer M,q,

    floor(floor(M/2)/q)=floor(M/(2q)).

For beta<1 the logarithm of condition (B) is exactly (6.1). For beta=1 and M>=2q, the burn is at least q, so the envelope is zero. For fixed `q,beta<1`, the left side of (6.1) grows linearly with M whereas the right side grows logarithmically, proving the eventual claim; beta=1 was explicit. No sufficient condition is asserted at a small M where this test fails: the unconditional finite bounds and cap one remain available there.

Equivalently, for beta<1 one may choose the PUBLIC burn `b=q ceil(log(M+1)/[-log(1-beta)])`, provided this b is at most `floor(M/2)`; for beta=1 take b=q under the same half-window condition. These are admissible common suffix algorithms. The original algorithm does not need to make either choice. ∎

### unit_007: proposition — Fast-mixing hard subclass (`prop:s004-lower`)

**Statement.** For every `K>=2,M>=1,q>=2,0<beta<1`, the lower bound (S004.6) holds on the same full-history actual-endpoint mean-TV target. In particular constant fast mixing does not generally remove the K³ sample-size factor.

**Proof.** Use the accepted S002 legal hypercube, but choose

    alpha=tau_beta a(K,M),      tau_beta=min{1/10,1-sqrt(beta)}.

This is positive, at most 1/10, and at most `a/10`. The unchanged S002 conditional full-history information bound for each bit flip is

    D(P_sigma^s || P_{sigma^ell}^s)
       <=16 alpha²/K+36 alpha² M/K³.

Here the P's are full-history laws conditioned on the same actual endpoint s, not predictive distributions. Since `alpha²<=1/100`, `alpha² M/K³<=1/100`, and K>=2, this is at most `.44`. Hence S002's conditional testing distance bound below 1/2 still holds. Its pointwise target-row loss and conditional averaging yield Bayes risk at least `alpha/18` for EVERY common estimator, including one using public q,beta. No observation is discarded in this argument.

The family is started at its common uniform stationary pair law. Its two-step minorization obeys

    P_sigma²(s,t) >= (1-alpha)² pi(t) >= beta pi(t),

because `alpha<=tau_beta<=1-sqrt(beta)`. For q>=2, multiply on the right by `P_sigma^(q-2)` and use stationarity:

    P_sigma^q >= beta Pi P_sigma^(q-2)=beta Pi.

Thus this stationary-initialized hard subclass lies inside the arbitrary-mu class `D_K(q,beta)`. Supremum is at least the finite prior average for each estimator, and taking the infimum proves (S004.6). At `beta=.81`, `tau_beta=.1`, recovering `1/180`; the same holds for smaller beta. As beta approaches one the displayed lower constant tends to zero, and nothing here asserts a beta-uniform lower or a result at beta=1. Under (B) the lower and upper bounds give matching a(K,M) order for each FIXED q>=2,beta<1, not optimal joint dependence on the mixing parameters. ∎

### unit_008: proposition — One-step obstruction and exact two-step reset (`prop:s004-boundary`)

**Statement.** With all starting pairs in (D), q=1 is impossible for K>=2 and beta>0. With q=2,beta=1, (D) holds exactly for IID symbol-transition tables with their product stationary pair law.

**Proof of the one-step assertion.** Any probability pi gives positive mass to some pair `t=(c,d)`. Choose a pair `s=(a,b)` with b different from c; this is possible because K>=2. Structural shift zeros give `P(s,t)=0`, contrary to `P(s,t)>=beta pi(t)>0`. Thus pi need not have full support for the obstruction. A different condition quantified only over some restricted starting support would be a different class and would not justify the current arbitrary-mu statement.

**Proof of the exact two-step assertion.** At beta=1, row sums give `P²(s,t)=pi(t)` for every s,t. The unique legal two-step route from `(a,b)` to `(c,d)` goes through `(b,c)`, so

    P²((a,b),(c,d))=theta_ab(c) theta_bc(d).

Summing over d gives

    theta_ab(c)=sum_d pi(c,d)=:p(c)

for every a,b,c. Hence every row equals the same probability law p. Substitution into the two-step identity then gives `pi(c,d)=p(c)p(d)`. Conversely, if every theta row equals p, then the same product calculation gives `P²(s,(c,d))=p(c)p(d)` independently of s, and this product law is stationary; hence (D) holds with q=2,beta=1. Zero p coordinates are permitted. This is a statement about the transition table; the first pair may still have arbitrary law mu. No conclusion that `P^q=Pi` forces IID is asserted for q>2. ∎

### unit_009: proposition — Sufficiency is not necessity (`prop:s004-scope`)

**Statement.** Mixing is not necessary for the accepted stationary-rate guarantee. Conversely, positivity of every legal symbol-transition probability, without a quantitative lower bound, gives no source-uniform finite burn envelope tending to zero, even at a fixed K>=2.

**Proof.** For the first assertion take K=2 and the deterministic legal cycle

    00 -> 01 -> 11 -> 10 -> 00.

Its uniform law on the four pairs is stationary, and S001 applies to that stationary initialization. The chain from a fixed pair never converges to its uniform stationary law: its time-b marginal is a point mass for every b, whose TV distance to the uniform law is 3/4. Thus a uniform mixing assumption is not necessary for the stationary upper theorem. Periodicity was not silently excluded.

There is a second, logically different consistency point. The inherited arbitrary-initialization L1+ upper is `min{1,48K^(5/2)/sqrt(M+1)}`, which tends to zero as M tends to infinity for every FIXED K, without any mixing assumption. Mixing is therefore not necessary even for that form of general consistency. What the present theorem adds is an explicit sufficient condition for recovering the faster stationary ORDER in joint K,M from arbitrary mu, after a controlled burn scale; it is not a theorem that prediction is impossible without mixing.

For the second assertion, fix K>=2 and `0<epsilon<1` and define the strictly positive legal table

    theta_ab(c)=(1-epsilon)1{c=b}+epsilon/K.

Let `T(b,c)` denote this first-order symbol kernel. Its stationary symbol law is the uniform law u, and the pair law `pi(a,b)=u(a)T(a,b)` is stationary because

    sum_a pi(a,b) theta_ab(c)
      = [sum_a u(a)T(a,b)]T(b,c)=u(b)T(b,c).

Start at the fixed pair `(0,0)`. The second-coordinate marginal of Y_b is

    (1-epsilon)^b delta_0 + [1-(1-epsilon)^b]u,

by either induction or `T=(1-epsilon)I+epsilon U`, with U having every row u. The stationary second-coordinate marginal is u. Projection contracts TV, so

    TV(mu P^b,pi) >= (1-1/K)(1-epsilon)^b.             (9.1)

For every fixed finite b the right side tends to `1-1/K` as epsilon decreases to zero. Therefore positivity alone cannot give a single, source-independent burn that makes eta_b smaller than an arbitrary fixed tolerance below `1-1/K`; in particular there is no uniform envelope decaying to zero over all such positive tables.

This does not deny source-specific mixing from positivity. For a fixed positive finite table let `m=min_{a,b,c}theta_ab(c)>0`. Every two-step pair entry is at least m². For any stationary pi, `P²(s,t)>=m²>=m² pi(t)`, so a source-specific minorization exists with beta=m². The point is precisely that this beta may approach zero across the class. ∎

## 4. Target-step assembly and boundaries

Lemma 1 proves the suffix bound directly and transfers a stationary suffix occupancy bound to a FLOOR for the original count. Lemma 2 retains the original full-history stack identity under arbitrary initialization. Lemma 3 applies unconditional Holder to that original count and original error; Proposition 4 adds zero-count and smoothing terms. This yields the original-rule bound independently of the suffix risk bound. It is not valid to attribute (S004.1) to the original rule merely because both use the same endpoint, and this proof does not do so.

Lemma 5 supplies the exact uniform-mixing envelope, and Corollary 6 checks every burn and term absorption needed to recover stationary order. Proposition 7 supplies the matching all-common-algorithm lower for fixed beta<1 from the accepted stationary family, not a single-source add-one risk. Proposition 8 isolates the structural q=1 obstruction and the beta=1 two-step endpoint, so no false uniform K³ lower crosses that boundary. Proposition 9 separates sufficiency from necessity and qualitative positivity from a uniform parameter.

Boundary audit:

- **Small M:** the theorem permits M=1 only with b=0,L=1. The dyadic layer v=1 exists, and all risk caps remain valid. No burn condition is claimed automatically at small M.
- **Zero counts:** no empirical row is formed at J=0. The add-one denominator is always positive, and zero-count loss is separately bounded.
- **Large thresholds:** (S004.3) holds for every integer w>=1, including w>M; hence all `w=2v` layers are legal.
- **Zero probabilities / zero pi mass:** the path coupling uses finite products, not division by pi or conditional laws at null endpoints. States absent from pi can be reached under mu; their probability contribution is covered by eta_b and no absolute-continuity assumption is needed.
- **Reducibility and periodicity:** allowed in the source-specific theorem. The optional (D) imposes additional contraction, but is never retroactively imposed on S001.
- **eta_b=0 and b=0:** the floor disappears. At b=0 and mu=pi, (S004.2) is exactly the accepted S001 `min{1,48K^(3/2)/sqrt(M+1)}` upper. A later b with eta_b=0 gives a possibly conservative L-based bound without pretending the full initial law was stationary.
- **beta=1, zero q-blocks:** the envelope is one for b<q and zero for b>=q, as separately proved. There is no unqualified `0^0` expression.
- **Public versus hidden quantities:** pi and eta_b are analytical source descriptors, never estimator inputs. Public q,beta may determine the suffix burn. The full-history rule does not require a burn or knowledge of q,beta.
- **Loss distinctions:** every exported risk here is `E[TV]`. It does not prove an optimal `E[TV²]` or predictive-KL rate. If `E[TV]<=u`, the elementary consequence is only `E[TV²]<=u` from `TV²<=TV`, not `E[TV²]<=u²`. Jensen has the opposite direction. The conditional-history KL appearing in the lower proof is an information tool, not a prediction-loss theorem. A TV path-law perturbation gives an additive eta_b only for [0,1]-valued losses; it cannot silently be reused for an arbitrary unbounded KL loss.

## 5. Explicit rate, provenance, and scope audit

- Exposed variables: K,M,b,L,eta_b; optional q,beta, with exactly the domains in Section 1. Source theta and laws mu,pi are fixed within a trajectory and may vary in a supremum.
- Probability and horizon mode: finite-horizon expected actual-terminal TV and unconditional terminal-count tails, not a high-probability or simultaneous-horizon theorem.
- Constants: `25/4` and numerical dyadic constant 10 are accepted S001 interfaces; `2+sqrt(2)` is a geometric sum; 48 and 13 are proved in Proposition 4; 69 and 81 are conservative burn-absorption constants; `tau_beta/18` is the explicit accepted-hypercube scaling checked in Proposition 7.
- Assumption provenance: no occupancy, row-selection independence, or path-law mixing is assumed as a generated invariant. The path transfer and count floor are proved in Lemma 1; the full-history stack law in Lemma 2; contraction follows only after assuming (D).
- Optimality scope: under (B), fixed q>=2,beta<1 gives a matching mean-TV order `a(K,M)` for the mixing class, with constants allowed to depend on beta as displayed. The additive `sqrt(K)eta_b^(3/4)` term is a sufficient consequence of the L4 floor mechanism; it is NOT claimed optimal in eta_b. The burn or q,beta dependence is NOT asserted sharp when those parameters vary with K,M. No exact-beta-one minimax rate is inferred.
- Literature scope: path-law TV contraction, minorization splitting and bounded-loss transfer are elementary standard tools proved here for the exact objects. The original-count-floor plus original-stack argument is the explicit additional bridge required for this estimator. No claim of novelty relative to unsearched literature is made.
- Notation surface: theta,P,mu,pi,K,M,Y,C,n and the actual target come from the frozen setting. The public-facing new objects are the deterministic suffix rule, eta_b, D_K(q,beta), its envelope, and the displayed risk statements. `c,eta,J,J_b,Z_v,E_v,Psi,Pi,R,T,tau_beta` are proof-local quantities defined by formulas; every bound on them is proved or supplied by a stated accepted dependency. The symbol T in Proposition 9 is explicitly local to that first-order kernel, distinct from the scalar rate T in Corollary 6.
