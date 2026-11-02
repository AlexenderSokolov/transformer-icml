# S006 平稳近 IID 与两步 minorization 过渡

科学正文摘录。以下保留已接纳版本的数学文字与原有编号，不重写证明；仅省略提交身份、流程元数据和历史状态。来源与依赖见 `../SOURCES.md`，逐字节映射见 `../COPY_MAP.json`。本次编排不是新的独立数学审查。

## 1. Fixed experiment and the two precise classes

Fix integers `K>=2`, `M>=1`, alphabet `A={0,...,K-1}`, and a homogeneous second-order probability table `theta_ab(c)`. Its legal pair-shift kernel has

    P((a,b),(b,c))=theta_ab(c),

and zero entries on non-shift transitions. A source in the main two classes below includes a stationary pair law `pi`, with `pi P=pi`, and is initialized with `(X_1,X_2)~pi`. Observe the FULL history `H=(X_1,...,X_{M+2})`; put `Y_i=(X_{i+1},X_{i+2})`, `0<=i<=M`. The target is the actual endpoint row `theta_{Y_M}` for the unobserved `X_{M+3}`. The loss is `TV(q,p)=(1/2)sum_c |q(c)-p(c)|`, and the risk is its expectation, not squared TV or predictive KL.

Algorithms output a probability vector, may read the entire history, public `K,M` and the specified public class parameter, and may use an independent seed. They do not read hidden `theta,pi`, a hidden common row center, or any future observation. They must be common to the whole specified class.

For a public radius `rho in [0,1]`, define

    C_K(rho) = {(theta,pi): pi P=pi and there exists p in Delta_K
                             with max_{s in A^2} TV(theta_s,p)<=rho},
    R_near(K,M,rho)
       =inf_B sup_{(theta,pi) in C_K(rho)}
                    E_{theta,pi} TV(B(H,U),theta_{Y_M}).             (1.1)

The witness `p` is unknown and need not be unique. The condition is over EVERY row, not only occupied rows and not an occupation-weighted average. The radius is a public upper bound, not a requirement that the minimal possible radius equal `rho`. Every class is nonempty because it contains all IID transition tables with their stationary initialization.

For a public `beta in [0,1]`, define the stationary TWO-step Doeblin class

    D_K^stat(2,beta)
       = {(theta,pi): pi P=pi and P^2(s,t)>=beta pi(t)
                                      for EVERY s,t in A^2},
    R_D2stat(K,M,beta)
       =inf_B sup_{(theta,pi) in D_K^stat(2,beta)}
                    E_{theta,pi} TV(B(H,U),theta_{Y_M}).             (1.2)

Here too the condition is an inequality with a public lower bound, not equality with the maximal minorization coefficient. The initial law is exactly the displayed stationary `pi`. This is not the arbitrary-initialization class of S004. At `beta=0` the condition is vacuous; every `beta<=1` admits IID tables, so no empty-class convention is needed.

Use the following public rate expressions:

    a=a_stat(K,M)=min{1,sqrt(K^3/(M+1))},
    b=b_iid(K,M) =min{1,sqrt(K/(M+1))},
    F(K,M,z)=max{b,min{z,a}},                  0<=z<=1.              (1.3)

In particular `0<b<=a<=1` for every allowed `K,M`.

### Theorem S006-A: stationary near-IID transition

For all `K>=2,M>=1,rho in [0,1]`,

    (1/180) F(K,M,rho)
       <= R_near(K,M,rho)
       <= sup_{C_K(rho)} E TV(B_rho,theta_{Y_M})
       <= min{1,48 F(K,M,rho)},                                  (1.4)

where `B_rho` is the explicit public-parameter selector defined below. Thus the optimal expected actual-endpoint TV rate is, with universal constants,

    max{b_iid,min{rho,a_stat}}
       ~ min{a_stat,b_iid+rho}.                                  (1.5)

### Theorem S006-B: sharp stationary q=2 minorization interpolation

For all `K>=2,M>=1,beta in [0,1]`,

    (1/180) F(K,M,1-beta)
       <= R_D2stat(K,M,beta)
       <= sup_{D_K^stat(2,beta)} E TV(B_{1-beta},theta_{Y_M})
       <= min{1,48 F(K,M,1-beta)}.                               (1.6)

The constants do not depend on `beta`, including as `beta` tends to one. This proves a joint parameter result for stationary initialization, rather than a fixed-`beta<1` result with a vanishing lower constant. No extension to `q>2` or to arbitrary initial `mu` is asserted.

## 2. The actual algorithms and accepted dependency interfaces

The POOLED EMPIRICAL rule uses the `M` observed transition-output symbols:

    E_pool(c)=(1/M) sum_{i=0}^{M-1} 1{X_{i+3}=c}.                 (2.1)

It is a probability vector since `M>=1`; no smoothing is needed for expected TV. It pools across all contexts and is not the original rowwise rule. Retain separately the ORIGINAL rule

    C_s(c)=sum_{i=0}^{M-1} 1{Y_i=s,X_{i+3}=c},
    n_s=sum_c C_s(c),
    p_s^+(c)=(C_s(c)+1)/(n_s+K).                                 (2.2)

For any public `z in [0,1]`, compute only from public quantities

    U_stat=min{1,48 sqrt(K^3/(M+1))},
    U_pool(z)=min{1,(1/2)sqrt(K/M)+2z}.                           (2.3)

Define the deterministic common selector

    B_z(H) = E_pool(H)      if U_pool(z)<=U_stat,
             p^+_{Y_M}(H)  otherwise.                           (2.4)

In particular it does not estimate `p`, use the unknown true risk to choose a rule, or read a source-specific radius. The cap-one tie has a fixed pooled choice. Permitting the algorithm to use the full history does not require it to use every coordinate in every branch.

The following dependencies are used with exactly their original full-history actual-endpoint targets:

1. **Accepted S001 stationary original-rule bound.** For every legal `theta`, stationary `pi`, and `K>=2,M>=1`, the risk of (2.2) is at most `U_stat`. This applies to every source in both present classes; neither irreducibility nor positive stationary mass is required. Proof SHA-256: `6d00dc0b99ff0d6932b171bdd3e243ee923ca5d8a864cdac407c815e37f26f6d`.
2. **Accepted S002 hard-family calculations.** Its checkerboard family at an arbitrary amplitude `0<alpha<=1/2` has uniform stationary pair law; its endpoint-conditional FULL-history single-bit KL is at most `16alpha^2/K+36alpha^2 M/K^3`. If `alpha<=a/10`, the conditional testing distance is below `1/2` and the prior-average actual-endpoint TV risk is at least `alpha/18` for every common algorithm. Its two-step kernel satisfies `P^2>= (1-alpha)^2 Pi`. The reduced-amplitude inference is proved again in Lemma 2 below, rather than relying only on S002's final amplitude choice. Proof SHA-256: `ac5e20d249704e298454f1b3633eedcf4026847801922a584a9043304cbdbdf4`.
3. **Accepted S005 stationary IID lower witness.** S005 Section 4 proves that, for all estimators using the full `N=M+2` symbols, the unknown IID-table subclass initialized at `p tensor p` has risk at least `c_iid b`, where `c_iid=1/(32 sqrt(6))`. This statement is stronger than merely quoting the arbitrary-initialization class minimax lower: the actual witnesses there are stationary. Its exact source, full-data and public-parameter applicability are restated in Lemma 3. Frozen proof SHA-256: `389d743cebf89f7afeb4855ceb712bfec8b3b216b10ae077b23dd980b03c7eba`; accepted review SHA-256: `836fd40704d2d32a064f0efda7fc812d80855137c2aac4bd71ac2175f4c85bde`.


4. **Accepted S004 structure, rederived locally rather than needed as a black box.** Section 3, Proposition 8 identifies all-pairs `q=2,beta=1` with IID tables. Lemma 5 below derives the entire `beta in [0,1]` near-IID containment and the exact endpoint directly. S004 proof SHA-256: `a0f4f3cb2daf8f3191281d5e0fcdbb3f645d4118f7373f5fb1b8427006a1959a`.


## 3. Local lemma map and notation/assumption discipline

| Unit | Named mathematical result | Contribution |
|---|---|---|
| unit_001 | Lemma 1, pooled martingale bound (`lem:s006-pool`) | A dependent-path pooled bound, without assuming IID or stationarity |
| unit_002 | Lemma 2, scaled stationary checkerboard family (`lem:s006-cube`) | Uniformly controlled full-history testing, row radius, and minorization |
| unit_003 | Lemma 3, stationary IID floor (`lem:s006-iid`) | Full `M+2`-observation lower floor in both classes |
| unit_004 | Proposition 4, near-IID minimax transition (`prop:s006-near`) | Explicit common algorithm and lower/upper assembly with universal constants |
| unit_005 | Lemma 5, two-step minorization structure (`lem:s006-d2`) | All-row closeness to a hidden common probability vector; exact endpoints |
| unit_006 | Proposition 6, beta-uniform stationary interpolation (`prop:s006-beta`) | Matching lower at every beta, including both endpoints |
| unit_007 | Corollary 7, rate regimes and algorithm distinction (`cor:s006-regimes`) | Condition boundary and inherited same-target algorithm separation |

Primitive conditions are exactly the experiment, homogeneity, stationary initialization, the stated class hypothesis, and the public parameter domains. The temporary arbitrary initialization in Lemma 1 is an explicitly stronger local setting; it does not remove stationarity from Theorems S006-A/B. All row centers, martingale objects, checkerboard signs, and testing laws are proof-local and never supplied to an algorithm. Their probability, boundedness, or invariance properties are proved below or supplied by the audited dependency interface. The class definitions, risks, `a,b,F`, and selector are the minimal public-facing objects; all numerical constants are explicit or inherited from the stated dependencies.

## 4. Local derivation

### unit_001: Lemma 1 — Pooled martingale bound (`lem:s006-pool`)

**Statement.** In the fixed experiment with ANY initial pair law `mu`, if some probability vector `p` satisfies `max_s TV(theta_s,p)<=z`, then

    E_{theta,mu} TV(E_pool,theta_{Y_M})
       <= min{1,(1/2)sqrt(K/M)+2z}.                             (4.1)

**Proof.** Put `F_i=sigma(X_1,...,X_{i+2})`, `0<=i<=M`, and, for `0<=i<M`, set

    D_i=e_{X_{i+3}}-theta_{Y_i}.

This vector is `F_{i+1}`-measurable and has `E[D_i|F_i]=0`, by the defining conditional law of the homogeneous source. This assertion uses no stationarity and no independence of the observed outputs. Directly,

    E[||D_i||_2^2 |F_i]=1-||theta_{Y_i}||_2^2<=1.

For `i<j`, the vector `D_i` is `F_j`-measurable, so

    E <D_i,D_j> = E <D_i,E[D_j|F_j]> =0.

All variables are bounded on finite spaces. Expanding the square and using the vanishing cross terms gives

    E ||sum_{i=0}^{M-1} D_i||_2^2
       =sum_{i=0}^{M-1} E||D_i||_2^2 <= M.                     (4.2)

Let `q_bar=(1/M)sum_{i=0}^{M-1}theta_{Y_i}`, a random probability vector used only in the proof. By `||v||_1<=sqrt(K)||v||_2` and Cauchy-Schwarz for expectation,

    E TV(E_pool,q_bar)
       <= [sqrt(K)/(2M)] sqrt(E||sum_i D_i||_2^2)
       <= (1/2)sqrt(K/M).                                      (4.3)

The row-radius hypothesis gives PATHWISE

    TV(q_bar,p) <= (1/M)sum_i TV(theta_{Y_i},p)<=z,
    TV(theta_{Y_M},p)<=z.

The triangle inequality bounds the actual-endpoint loss by
`TV(E_pool,q_bar)+2z` on every path. Take expectations and the cap one to prove (4.1). The unknown center may be fixed arbitrarily among the existing witnesses for a source; no measurable selection across sources is required, since the bound is uniform for each source and the algorithm never uses the witness. This is a martingale argument for dependent samples, not an IID assertion. ∎

### unit_002: Lemma 2 — Scaled stationary checkerboard family (`lem:s006-cube`)

**Statement.** Fix `K>=2,M>=1` and `0<alpha<=a/10`. There is a finite family of legal stationary sources with common uniform pair law `pi(s)=K^-2` such that:

    max_s TV(theta_s,u)<=alpha/2,       u(c)=1/K;                 (4.4)
    P^2(s,t)>=(1-alpha)^2 pi(t)         for every s,t;            (4.5)

and every admissible full-history estimator has finite-prior average actual-endpoint risk at least `alpha/18`. The estimator may additionally read any class parameters shared by the whole family.

**Proof.** Let `r=floor(K/2)`, pair symbols into `B_i={2i,2i+1}`, `0<=i<r`, and put `epsilon(2i)=1`, `epsilon(2i+1)=-1`. For each middle symbol `b` and pair indices `i,j`, independently index a sign `sigma_bij in {-1,1}`. If `a in B_i,c in B_j`, use the accepted S002 construction

    theta_ab^sigma(c)=[1+alpha sigma_bij epsilon(a)epsilon(c)]/K;

if either `a` or `c` is the one unpaired symbol, use `1/K`. (Here the row's symbol `a` is not the rate `a_stat`; its local role is clear in the subscript.) Cancellation over each output pair makes every row stochastic; cancellation over each first-symbol pair makes `sum_a theta_ab^sigma(c)=1`. Hence uniform pair mass is stationary for the legal shift kernel. Initialize each family member at this exact common law, not at a horizon-selected phase.

If the first row symbol is paired, exactly `2r` coordinates have absolute perturbation `alpha/K`, so its distance from `u` is `r alpha/K<=alpha/2`. Unpaired first-symbol rows have distance zero. This proves (4.4) for odd as well as even `K`.

The unique two-step route from `(a,b)` to `(c,d)` passes through `(b,c)`, and every legal symbol probability is at least `(1-alpha)/K`. Consequently

    P_sigma^2((a,b),(c,d))
       =theta_ab^sigma(c) theta_bc^sigma(d)
       >=(1-alpha)^2/K^2,

which proves (4.5).

For completeness the scaled information interface is checked rather than assumed. Under uniform stationary initialization, the entire history conditioned on `Y_M=s` is the length-`M` reversed pair chain started at `s`. Its reverse probabilities are `Q_sigma((b,c),(a,b))=theta_ab^sigma(c)`. The initial uniform pair factor and the endpoint conditioning factor cancel; the symbol history and legal pair history determine one another. Thus all `M+2` observed symbols, including the initial pair, remain in this conditional experiment. A single sign flip changes only two reversed departure rows; the accepted S002 finite-chain calculation gives

    KL(P_sigma^s || P_sigma^s_flip)
       <= 16alpha^2/K+36alpha^2 M/K^3.                          (4.6)

Here `P_sigma^s` denotes the full conditional DATA law. Because `alpha<=a/10`,

    alpha^2<=1/100,
    alpha^2 M/K^3 <= [1/100]min{1,K^3/(M+1)}M/K^3<=1/100.

Together with `K>=2`, (4.6) is at most `.08+.36=.44`. The elementary finite Pinsker bound proved in S002 gives conditional data TV at most `sqrt(.22)<1/2`, uniformly in the endpoint and every other sign. For each paired endpoint and output pair, decoding the hidden sign from the estimator's signed coordinate difference makes a wrong sign cost at least `alpha/K` of TV. The two-hypothesis testing inequality then gives prior-average conditional bit-error probability at least `1/4`, also for randomized estimators. Every sign vector has the same uniform endpoint law, so the sign prior remains uniform after conditioning on `Y_M=s`.

There are `2rK` paired endpoints of probability `1/K^2`, and `r` tested output pairs at each. Their total prior-average loss is therefore at least

    (1/K^2)(2rK)(alpha/K)(r/4)
       =alpha r^2/(2K^2)>=alpha/18,                            (4.7)

using `r/K>=1/3` for all `K>=2`. This is precisely S002's endpoint-conditional testing assembly, and its hypotheses remain valid at the smaller amplitude. Shared public parameters only change the common estimator/test; they do not reveal signs or invalidate testing. No conditional IID row sampling or independent test query is used. ∎

### unit_003: Lemma 3 — Stationary IID floor (`lem:s006-iid`)

**Statement.** For every public `rho,beta in [0,1]`, the risks in (1.1) and (1.2) are each at least `c_iid b`, where `c_iid=1/(32 sqrt(6))`, using the accepted S005 stationary witnesses.

**Proof.** For every unknown probability vector `p`, take all transition rows equal to `p` and initial `pi=p tensor p`. Then every observed symbol, including the first two, is IID with law `p`, and the target is `theta_{Y_M}=p` on every history. This source belongs to every `C_K(rho)` by center `p` and radius zero. Moreover `P^2(s,(c,d))=p(c)p(d)=pi(c,d)`, so it belongs to every `D_K^stat(2,beta)`.

The required S005 bound is not obtained by restricting an arbitrary-initialization minimax inequality. Its actual stationary witnesses are as follows. Set `N=M+2`, `d=floor(K/2)`, `epsilon=(1/4)min{1,sqrt(d/N)}` and, for `sigma in {-1,1}^d`, set

    p_sigma(2j)=(1+epsilon sigma_j)/(2d),
    p_sigma(2j+1)=(1-epsilon sigma_j)/(2d),       0<=j<d,

with an odd leftover coordinate zero. The FULL data law is `p_sigma^(tensor N)`. Neighboring signs have full-data TV below `1/2` by the affinity calculation in S005 Section 4. A wrong decoded sign costs `epsilon/(2d)` in TV. Averaging binary tests gives error at least `1/4` per bit, hence average loss at least

    epsilon/8=(1/32)min{1,sqrt(d/N)}
       >= [1/(32 sqrt(6))]min{1,sqrt(K/(M+1))}.                 (4.8)

The last inequality uses `d>=K/3`, `N<=2(M+1)`, and the elementary capped-square-root comparison, so it includes odd `K` and `M=1`. Every hypothesis has the same public `rho` or `beta`, and the tested estimator retains all data and any independent seed. Thus revealing these public class parameters does not weaken the testing bound. Supremum dominates the finite prior average for each estimator, and then infimum preserves (4.8) in each class. ∎

### unit_004: Proposition 4 — Near-IID minimax transition (`prop:s006-near`)

**Statement.** Under the stationary near-IID setting (1.1), Theorem S006-A holds with the algorithm (2.4) and the constants in (1.4). Also the two expressions in (1.5) differ by a factor at most two.

**Proof: upper and admissibility.** Lemma 1 gives the risk bound `U_pool(rho)` for (2.1), and accepted S001 gives `U_stat` for (2.2). The choice in (2.4) is deterministic from public parameters and common to the class. Its supremum risk is therefore at most

    min{U_stat,U_pool(rho)}.                                    (4.9)

To simplify while preserving all caps, first note `U_stat<=48a`. Also

    U_pool(z)<=b+2z.                                            (4.10)

Indeed, if `K/(M+1)>=1`, then `b=1` and the cap one proves (4.10). Otherwise `b=sqrt(K/(M+1))`, and

    [(1/2)sqrt(K/M)]/b=(1/2)sqrt((M+1)/M)<=sqrt(2)/2<=1.

If `rho>=a`, then `F(K,M,rho)=a` and (4.9) is at most `48F`. If `rho<a`, then `F=max{b,rho}` and the pooled bound is at most `b+2rho<=3F<=48F`. The risk is also at most one. This proves the upper part of (1.4) without requiring any regime assumption on `K,M,rho`.

**Proof: lower.** Lemma 3 yields the IID floor `c_iid b`. If `rho=0`, the additional desired term `min{rho,a}` is zero. If `rho>0`, take Lemma 2 with

    alpha=min{a/10,2rho}>0.                                    (4.11)

Every such source belongs to `C_K(rho)` by (4.4), with the common uniform center. Its prior-average risk is at least `alpha/18`. Since each argument of the minimum in (4.11) is at least `(1/10)min{a,rho}`,

    R_near(K,M,rho)>= (1/180)min{a,rho}.                        (4.12)

This also holds trivially at `rho=0`. Further `c_iid>=1/180` (for example `32sqrt(6)<96<180`). Both lower bounds hold for EVERY estimator with the same public parameters; taking the infimum thus gives

    R_near>=max{c_iid b,(1/180)min{a,rho}}
            >=(1/180)F(K,M,rho).

The two hard subclasses need not be the same. Their bounds are combined by a maximum, not by adding risks of different sources.

For the asserted equivalence, let `G=min{a,b+rho}`. If `rho>=a`, then `F=G=a`. If `rho<a`, both `a` and `b+rho` are at least `max{b,rho}=F`, while `G<=b+rho<=2F`. Thus

    F<=G<=2F                                                    (4.13)

for every allowed parameter. ∎

### unit_005: Lemma 5 — Two-step minorization structure (`lem:s006-d2`)

**Statement.** If `(theta,pi) in D_K^stat(2,beta)`, then for the probability vector

    p(c)=sum_d pi(c,d)

every row obeys `theta_ab(c)>=beta p(c)` and `TV(theta_ab,p)<=1-beta`. Consequently

    D_K^stat(2,beta) subset C_K(1-beta).                         (4.14)

At `beta=1` this class consists exactly of all-row IID tables with stationary pair law `p tensor p`. At `beta=0` it is the entire stationary source class.

**Proof.** Nonnegativity and total mass one of `pi` make `p` a probability vector, even if some coordinates vanish. The unique legal two-step route gives

    theta_ab(c) theta_bc(d)=P^2((a,b),(c,d))>=beta pi(c,d).

Sum over `d`. Since `sum_d theta_bc(d)=1`, this yields

    theta_ab(c)>=beta sum_d pi(c,d)=beta p(c)                    (4.15)

for EVERY `a,b,c`, including zero-mass or unreachable starting pairs. If `beta<1`,

    r_ab(c)=[theta_ab(c)-beta p(c)]/(1-beta)

is a probability vector by (4.15) and the row sums. Therefore

    TV(theta_ab,p)=(1-beta)TV(r_ab,p)<=1-beta.

At `beta=1`, (4.15) and the equal row sums imply `theta_ab=p` exactly, with no division by a zero probability. In that case the two-step kernel is the constant-row matrix with row `p tensor p`; stationary `pi` obeys `pi=pi P^2=p tensor p`. Conversely an all-row IID table with this product stationary law satisfies `P^2=Pi`, including when `p` has zeros. For `beta=0` minorization asserts only nonnegativity, hence imposes no restriction beyond stationarity. This proves all claims. ∎

### unit_006: Proposition 6 — Beta-uniform stationary interpolation (`prop:s006-beta`)

**Statement.** Theorem S006-B holds for all `beta in [0,1]`, with exactly the constants and the public algorithm in (1.6).

**Proof.** Lemma 5 and Proposition 4 prove the upper bound, with `z=1-beta` in (2.4). This selector uses only public `beta`; it is not given the derived center `p` or stationary law `pi`.

For the lower, put `delta=1-beta`. The IID floor in Lemma 3 holds at every beta. At `beta=1`, `delta=0` and that floor is the only necessary term, so the lower is already proved. For `beta<1`, take the family in Lemma 2 with

    alpha=min{a/10,1-sqrt(beta)}>0.                              (4.16)

Its two-step kernel satisfies `P^2>=(1-alpha)^2 Pi>=beta Pi`, by (4.5) and (4.16). Each member is initialized at its actual uniform stationary pair law, so the family lies in the precise stationary class (1.2). The elementary identity

    1-sqrt(beta)=(1-beta)/(1+sqrt(beta))

implies, including the endpoints as scalar inequalities,

    delta/2<=1-sqrt(beta)<=delta.                               (4.17)

Both entries of the minimum in (4.16) are therefore at least `(1/10)min{a,delta}`. Lemma 2 supplies

    R_D2stat(K,M,beta)>=alpha/18
                      >=(1/180)min{a,1-beta}.                  (4.18)

This is also true with right side zero at `beta=1`; no positive-amplitude testing lemma is invoked at alpha zero. Combining (4.18) with `c_iid b>=b/180` yields the lower in (1.6), by the same maximum argument as in Proposition 4. At `beta=0`, (4.16) gives `alpha=a/10` and recovers the accepted stationary lower. At `beta=1`, Lemma 5 gives the exact IID class and the IID lower/pooled upper. Thus neither endpoint is obtained by an unjustified limit of a fixed-beta constant. ∎

### unit_007: Corollary 7 — Rate regimes and algorithm distinction (`cor:s006-regimes`)

**Statement.** For either theorem, put `z=rho` or `z=1-beta` respectively. Its optimal expected-TV rate has the following three regimes:

    F=b       if 0<=z<=b;
    F=z       if b<=z<=a;
    F=a       if a<=z<=1.                                      (4.19)

At `rho=0` and `beta=1`, the original rowwise add-one is not uniformly minimax-order optimal in `K,M`, although the pooled/public-selector rule attains the displayed rate. At `rho=1` and `beta=0`, the statements recover the full stationary class and rate. The original-rule separation uses S005's accepted stationary counterexample.

**Proof.** Equation (4.19) is direct from `b<=a` and the definition of `F`. In the regime `z>=a`, the original rule itself has the correct order because its bound `48a` matches the minimax lower `a/180`. In the two smaller-radius regimes the pooled bound `b+2z` is at most `3F`; this does not imply that the original rule also improves.

At `rho=0`, every row must equal its common center `p`. Any stationary pair law then equals `p tensor p` because `P^2` has every row `p tensor p`. Thus the near-IID endpoint is precisely the same stationary IID class as `beta=1` in Lemma 5. At `rho=1`, any fixed probability center witnesses the row condition because TV is at most one; hence this is the entire stationary class. Lemma 5 gives the `beta=0` endpoint.

For the stated algorithm distinction, the S005 countersequence already has stationary initialization: even `K>=10`, `M=floor(K^2/100)`, half the symbol probabilities `3/(2K)` and half `1/(2K)`, every row equal to that vector `p`, and initial pair `p tensor p`. It belongs to both exact endpoints. S005 proves actual-endpoint original-rule risk at least `391/1600`, while the pooled mean-TV upper tends to zero. The present empirical pooled bound also gives

    E TV(E_pool,p)<=(1/2)sqrt(K/M) ->0

on that same sequence. This is a same-source/same-target comparison, not a single-source minimax lower. Since the class minimax rate at either exact endpoint is `b ->0`, no universal multiplicative optimality factor for original rowwise add-one is possible on the whole family of these classes. No exact all-`K,M` formula for original-rule risk is inferred. ∎

## 5. Target-step assembly, caps, and explicit-rate audit

Lemma 1 supplies a pooled upper for the actual dependent-history endpoint without any IID declaration. Accepted S001 supplies a genuinely separate original-rule upper under stationarity. Proposition 4 combines them by a public, source-independent decision and proves the capped bound for every `K,M,rho`. Lemma 2 puts a scaled lower family inside the exact all-row radius class, while Lemma 3 supplies the nonzero IID floor even when the radius vanishes. Their maximum gives the entire near-IID lower, not a sum of unrelated witnesses.

Lemma 5 is the new structural bridge from TWO-step minorization to an all-row common center with radius `1-beta`. Proposition 6 combines that upper bridge with a minorization-compliant checkerboard amplitude and the IID floor, obtaining uniform constants as beta varies. The lower amplitude is the MINIMUM in (4.16), not S004's product `a min{1/10,1-sqrt(beta)}`; this change and (4.17) prevent an artificial product loss when both `a` and `1-beta` are small.

- **Exposed variables:** all integers `K>=2,M>=1`, all `rho,beta in [0,1]`. No hidden constants depend on any of them or on the source, stationary law, row center, or estimator.
- **Probability/norm/horizon mode:** expected TV at a deterministic finite actual endpoint, exactly `M` observed departures and the complete `M+2`-symbol history; no stopping-time or simultaneous-horizon upgrade.
- **All caps:** `a,b` are capped at one; algorithmic bound selection uses the two capped public bounds; the final risk is capped by one. The `M` versus `M+1` comparison uses `M>=1` explicitly in (4.10).
- **Zero and small cases:** `M=1`, `K=2`, odd `K`, zero probabilities, zero stationary masses, unvisited endpoint rows, periodic and reducible chains require no extra assumption. The pooled empirical denominator is always the deterministic positive `M`; the original rule has positive denominator `n_s+K`.
- **Positive-amplitude use:** Lemma 2 is used only for `rho>0` or `beta<1`. At `rho=0` or `beta=1` its additional lower term is zero and the stationary IID floor handles the endpoint. No testing argument with an indistinguishable zero-amplitude family is claimed.
- **Public parameters and existence:** the common center is existential and unknown. Public rho/beta are bound parameters. Every subclass used in a lower bound shares those public values, even though its true radius may be smaller or its true minorization stronger. Sources may depend on fixed `K,M` inside a supremum but remain unchanged throughout each trajectory.
- **Baseline reduction:** `rho=1` and `beta=0` give `F=a`, retaining the accepted stationary `1/180` lower and original `U_stat` upper. At `rho=0` and `beta=1`, `F=b`; the sharper displayed selector bound (4.9) retains the pooled IID upper, rather than merely the coarser universal `48b` summary. Exact reset is not treated as a limit of a strictly-subunit-beta lower constant.
- **Class distinction:** the near-IID condition is not claimed equivalent to Doeblin minorization; only the containment (4.14) is used for the upper, and a separate compliant subclass proves the Doeblin lower. The q=2 identity used in (4.15) does not extend to q>2 by summing the same coordinates.
- **Initialization distinction:** Lemma 1 alone holds for arbitrary initialization. The combined `min{a_stat,b_iid+radius}` upper and both matched theorems rely on stationarity through S001. They are not asserted for arbitrary `mu` merely because the pooled half does not need stationarity.
- **Statistical interpretation:** along any parameter sequence, the respective class minimax risk tends to zero exactly when both `b_iid` and `min{z,a_stat}` tend to zero, by the two universal inequalities. This is a consequence of the matched rate, not a new hypothesis or a claim about predictive KL.

