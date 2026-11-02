# S005 两步重置 IID 最优率与算法分离

科学正文摘录。以下保留已接纳版本的数学文字与原有编号，不重写证明；仅省略提交身份、流程元数据和历史状态。来源与依赖见 `../SOURCES.md`，逐字节映射见 `../COPY_MAP.json`。本次编排不是新的独立数学审查。

## 1. Fixed experiment, admissible algorithms, and exported statements

Fix integers `K>=2`, `M>=1`; write `N=M+2` and `A={0,...,K-1}`. A legal homogeneous second-order source has transition table `theta_ab(c)`, with nonnegative rows summing to one, and pair kernel

    P((a,b),(b,c))=theta_ab(c),

with zero entries elsewhere. The initial pair `(X_1,X_2)` has an arbitrary law `mu`. The observation is the ENTIRE history `H=(X_1,...,X_N)`. Put

    Y_i=(X_{i+1},X_{i+2}),   0<=i<=M.

The target remains the next-symbol law at the ACTUAL endpoint, `theta_{Y_M}` for `X_{M+3}`. No independent query is introduced. Throughout, `TV(q,p)=(1/2)sum_c |q(c)-p(c)|`, and `Delta_L` denotes the probability simplex on an `L`-element set.

Let `E_K` be the exact two-step-reset source class: there exists a stationary pair law `pi` such that

    P^2(s,t)=pi(t) for EVERY s,t in A^2.              (E)

Equivalently this is the all-pairs minorization class with `q=2,beta=1`, since row sums turn `P^2(s,t)>=pi(t)` into equality. Initial `mu` remains arbitrary. The equivalence proved in Section 2 identifies (E) with

    theta_ab(c)=p(c) for all a,b,c,   pi=p tensor p,    (I)

for some unknown probability vector `p` on `A`. Zero coordinates of `p` are allowed. Knowledge of the class (I) is public; the vector `p`, `theta`, `mu`, and `pi` are not given to the algorithm.

An admissible common algorithm `B(H,U)` outputs a probability vector on `A`; its optional seed `U` is independent of the source and sample. Its program and parameters may use public `K,M` and the class definition, but not hidden source parameters. Define

    R_IID(K,M)
      =inf_B sup_{p in Delta_K, mu in Delta_(K^2)}
           E_{p,mu} TV(B(H,U),p),
    r(K,M)=min{1,sqrt(K/(M+1))}.

The target in this formula equals `theta_{Y_M}` identically by (I), rather than by replacing the endpoint with another query.

Define the POOLED add-one rule, distinct from the original context-specific rule, by

    T_c=sum_{j=3}^{M+2} 1{X_j=c},
    B_pool(c)=(T_c+1)/(M+K).                           (P)

It uses all `M` transition-output symbols and does not require `p` or a mixing parameter. It ignores the arbitrary initial pair. It pools across contexts; it is not the S004 rowwise suffix rule.

**Theorem S005-A (all-algorithm optimal mean-TV rate).** For every `K>=2,M>=1`,

    [1/(32 sqrt(6))] r(K,M)
      <= R_IID(K,M)
      <= sup_{p,mu} E TV(B_pool,p)
      <= min{1,(3/2)sqrt(K/(M+1))}
      <= (3/2)r(K,M).                                (S005.1)

Thus the exact two-step-reset class has optimal rate

    R_IID(K,M) = Theta(min{1,sqrt(K/(M+1))}),

with absolute constants uniform in all displayed parameters and initial laws. The lower bound retains the full observed `N=M+2` symbols, by choosing the legal stationary initialization `mu=p tensor p`.

For comparison retain the ORIGINAL frozen rule

    C_{s,c}=sum_{i=0}^{M-1} 1{Y_i=s,X_{i+3}=c},
    n_s=sum_c C_{s,c},
    p_s^+(c)=(C_{s,c}+1)/(n_s+K),
    R_orig,IID^+(K,M)=sup_{p,mu} E TV(p^+_{Y_M},p).

**Theorem S005-B (original-rule separation).** For every even `K>=10`, take

    p(c)=3/(2K),   0<=c<K/2;
    p(c)=1/(2K),   K/2<=c<K;
    theta_ab(c)=p(c),   mu=p tensor p,
    M=floor(K^2/100).

This is a legal stationary-initialized member of the same class, and

    E TV(p^+_{Y_M},p) >= 391/1600 > .24,              (S005.2)
    R_IID(K,M) <= sup_{p',mu'} E TV(B_pool,p')
                    <= min{1,(3/2)sqrt(K/(M+1))}
                    <= min{1,15/sqrt(K)}.             (S005.3)

Consequently no absolute `C` can satisfy

    R_orig,IID^+(K,M) <= C R_IID(K,M)

for all `K,M`. The exact original-rule rate over all `K,M` is not asserted.

## 2. Exact reset is exactly the IID transition-table class

**Lemma 1.** Condition (E) holds if and only if (I) holds. Under (I), for every initial law `mu`,

    P_{p,mu}(X_1=x_1,...,X_N=x_N)
      =mu(x_1,x_2) product_{j=3}^N p(x_j).             (2.1)

In particular `X_3,...,X_N` are `M` IID `p` observations, independent of the initial pair, and `theta_{Y_M}=p` for every possible observed history.

**Proof.** There is exactly one structurally legal two-step pair path from `(a,b)` to `(c,d)`, namely through `(b,c)`. Thus

    P^2((a,b),(c,d))=theta_ab(c) theta_bc(d).

Under (E), summing over `d` yields

    theta_ab(c)=sum_d pi(c,d)=:p(c)

for every `a,b,c`. The right side is a probability vector and does not depend on the starting pair. Substituting this into the two-step formula gives `pi(c,d)=p(c)p(d)`.

Conversely, if every row is `p`, the same product formula gives `P^2((a,b),(c,d))=p(c)p(d)`, independent of `(a,b)`. The product pair law is stationary, since

    sum_a [p(a)p(b)] theta_ab(c)=p(b)p(c).

This proves (E). Formula (2.1) follows by multiplying the initial pair probability and the successive conditional transition probabilities. It is valid when some factors vanish. It proves the IID and independence statements without assuming anything about `mu`. The target equality follows directly from the all-row equality `theta_ab=p`. ∎

The all-starting-pairs quantifier matters. A condition only on a stationary support need not control arbitrary initial pairs. Nothing in this lemma asserts that `P^q=Pi` for an arbitrary `q>2` forces an IID table.

## 3. Uniform upper bound for the pooled rule

**Lemma 2.** For every `p,mu,K,M` in the stated domains,

    E TV(B_pool,p)
      <= min{1, sqrt(M(K-1))/(2(M+K))+(K-1)/(M+K)}
      <= min{1,(3/2)sqrt(K/(M+1))}.                   (3.1)

**Proof.** By Lemma 1, `T_c` has mean `M p(c)` and variance `M p(c)(1-p(c))`. For the empirical vector `p_hat(c)=T_c/M`, Cauchy-Schwarz gives

    E TV(p_hat,p)
      <= (1/(2 sqrt(M))) sum_c sqrt(p(c)(1-p(c)))
      <= (1/2) sqrt((K-1)/M).                        (3.2)

For the last step, the square of the sum is at most

    K sum_c p(c)(1-p(c))
      =K(1-sum_c p(c)^2) <= K-1,

using `sum_c p(c)^2>=1/K`. This remains true when some probabilities are zero.

Let `u(c)=1/K`. Exactly,

    B_pool=[M/(M+K)] p_hat+[K/(M+K)]u.

Convexity of the absolute value and `TV(u,p)<=1-1/K` imply the first bound in (3.1), also capped by one. For completeness, `TV(u,p)=1-sum_c min{1/K,p(c)}` and this overlap sum is at least `1/K`: each summand is at least `p(c)/K`, so their sum is at least `1/K`.

Write `x=K/(M+1)`. The empirical term satisfies

    sqrt(M(K-1))/(2(M+K)) <= (1/2)sqrt(x),            (3.3)

because `K-1<=K` and `M(M+1)<=(M+K)^2`. The smoothing term satisfies

    (K-1)/(M+K) <= K/(M+1)=x.                        (3.4)

If `x<=1`, (3.3)-(3.4) give risk at most `(1/2)sqrt(x)+x <=(3/2)sqrt(x)`. If `x>=1`, risk at most one already proves the second bound in (3.1). This proves the uniform upper bound. No initial-pair parameter is read by the algorithm or used in the bound. ∎

## 4. A full-data, all-algorithm finite hypercube lower bound

The proof uses an elementary affinity/testing inequality, proved next. It is an information bound on distributions of the observed DATA, not a prediction-loss change from TV to another loss.

**Lemma 3 (finite testing bound).** For probability vectors `Q,R` on a finite set, put

    aff(Q,R)=sum_h sqrt(Q(h)R(h)).

Then

    TV(Q,R) <= sqrt(1-aff(Q,R)^2).                    (4.1)

For an arbitrary randomized test with probability `f(h) in [0,1]` of choosing the first hypothesis,

    E_Q[1-f(H)]+E_R[f(H)] >= 1-TV(Q,R).               (4.2)

Product distributions satisfy `aff(Q^N,R^N)=aff(Q,R)^N`.

**Proof.** Cauchy-Schwarz gives

    TV(Q,R)
      =(1/2)sum_h |sqrt(Q(h))-sqrt(R(h))|
                          (sqrt(Q(h))+sqrt(R(h)))
      <=(1/2)sqrt((2-2 aff(Q,R))(2+2 aff(Q,R))),

which is (4.1). Since `0<=f<=1`,

    E_Q f-E_R f <= sum_{h:Q(h)>R(h)}(Q(h)-R(h))
                =TV(Q,R),

and rearrangement proves (4.2). The product affinity identity follows by expanding the finite sum over all coordinates. ∎

**Lemma 4.** Let `N=M+2`. Every admissible estimator based on the full `N` observations satisfies

    sup_{p,mu} E TV(B(H,U),p)
      >= (1/32) min{1,sqrt(floor(K/2)/N)}.            (4.3)

**Proof.** Write `d=floor(K/2)>=1` and choose

    epsilon=(1/4)min{1,sqrt(d/N)}.                    (4.4)

For each sign vector `sigma in {-1,+1}^d`, define

    p_sigma(2j-2)=(1+epsilon sigma_j)/(2d),
    p_sigma(2j-1)=(1-epsilon sigma_j)/(2d),
                       j=1,...,d.                  (4.5)

If `K` is odd set the one remaining probability to zero. Each vector in (4.5) is a valid probability vector. Take the legal source with every transition row `p_sigma`, and its stationary initial law `mu_sigma=p_sigma tensor p_sigma`. By Lemma 1 the FULL history law is

    Q_sigma=p_sigma^(tensor N).                     (4.6)

Thus the initial two symbols are retained as informative observations. The lower bound does not discard them or condition on a selected endpoint.

For any output probability vector `q`, decode a sign for coordinate `j` by

    sigma_hat_j(q)=+1 if q(2j-2)>=q(2j-1),
                  -1 otherwise.

If this sign is wrong, the true coordinate difference is `epsilon sigma_j/d`, while the decoded difference has the opposite sign or is zero. The triangle inequality therefore gives

    |q(2j-2)-p_sigma(2j-2)|
       +|q(2j-1)-p_sigma(2j-1)| >= epsilon/d.

The pairs are disjoint, so pointwise

    TV(q,p_sigma)
      >= [epsilon/(2d)] sum_{j=1}^d
                         1{sigma_hat_j(q)!=sigma_j}. (4.7)

Let `sigma^(j)` denote a sign flip in coordinate `j`. A direct one-symbol affinity computation gives

    rho=aff(p_sigma,p_sigma^(j))
       =(d-1)/d+sqrt(1-epsilon^2)/d,
    1-rho=[1-sqrt(1-epsilon^2)]/d <=epsilon^2/d.       (4.8)

The last inequality follows from `sqrt(1-z)>=1-z` for `0<=z<=1`. Lemma 3 and `1-t^n <= n(1-t)` for `0<=t<=1` yield

    TV(Q_sigma,Q_sigma^(j))
      <=sqrt(1-rho^(2N))
      <=sqrt(2N(1-rho))
      <=sqrt(2N epsilon^2/d)
      <=1/sqrt(8)<1/2.                              (4.9)

The last inequality follows from (4.4), because `N epsilon^2/d <=1/16`. The elementary inequality about `t^n` is just `1-t^n=(1-t)(1+t+...+t^(n-1))<=n(1-t)`.

Fix an arbitrary admissible `B`. Its independent random seed induces for each bit a randomized decision function of the finite history, so Lemma 3 applies after integrating the seed. For fixed values of the other `d-1` signs, (4.2) and (4.9) show that the sum of the bit-error probabilities under the two possible values of `sigma_j` is at least `1/2`. Averaging uniformly over the `2^d` sign vectors gives

    2^(-d) sum_sigma
       P_sigma{sigma_hat_j(B(H,U))!=sigma_j} >=1/4.   (4.10)

Average (4.7), then use (4.10) and sum over `j`. The finite-prior average risk of `B` is at least

    [epsilon/(2d)] d/4
      =epsilon/8
      =(1/32)min{1,sqrt(d/N)}.

The supremum over all allowed sources is at least this finite average. This is true for every common algorithm, including every randomized one, and proves (4.3). The family depends on the public `K,M`, which is allowed inside a finite-horizon supremum; no source changes during a trajectory. ∎

**Proof of the lower inequality in Theorem S005-A.** For every `K>=2`, `d=floor(K/2)>=K/3`; for every `M>=1`, `N=M+2<=2(M+1)`. Consequently

    d/N >= K/[6(M+1)].

For `z>=0` and `0<a<=1`, `min{1,sqrt(a z)}>=sqrt(a)min{1,sqrt(z)}`: if `z<=1` it is equality, and if `z>=1` the left side is at least `sqrt(a)`. With `a=1/6`, Lemma 4 therefore gives

    sup_{p,mu} E TV(B,p) >=[1/(32 sqrt(6))]r(K,M)

for every admissible `B`. Take the infimum over `B`. Combine with Lemma 2 and the admissibility of `B_pool` to prove the entire chain (S005.1). ∎

## 5. The original context-specific rule can lose a constant

**Lemma 5 (endpoint collision count, including the overlap).** Suppose the whole observed sequence is IID with law `p`. Put

    J=n_{Y_M}=sum_{i=0}^{M-1}1{Y_i=Y_M}.

For every `M>=1`,

    E J=(M-1)(sum_c p(c)^2)^2+sum_c p(c)^3.          (5.1)

The first term is zero when `M=1`.

**Proof.** For each `0<=i<=M-2`, the pair `(X_{i+1},X_{i+2})` and the endpoint pair `(X_{M+1},X_{M+2})` involve four distinct IID coordinates. Their equality probability is

    sum_{a,b} p(a)^2p(b)^2=(sum_c p(c)^2)^2.

There are exactly `M-1` such indices when `M>=2`, and none when `M=1`. The last previous pair, `Y_{M-1}=(X_M,X_{M+1})`, overlaps `Y_M` in one symbol. Equality is precisely

    X_M=X_{M+1}=X_{M+2},

whose probability is `sum_c p(c)^3`. This formula also covers `M=1`, when the three symbols are `X_1,X_2,X_3`. Sum the indicator expectations; no independence between different collision indicators is needed. ∎

**Proof of Theorem S005-B.** For the stated even-`K` vector,

    TV(p,u)=1/4,
    sum_c p(c)^2=5/(4K),
    sum_c p(c)^3=7/(4K^2).

The chosen stationary initialization makes the entire history IID. Lemma 5 gives the exact expectation

    E J=(M-1)25/(16K^2)+7/(4K^2)
       =(25M+3)/(16K^2)
       <=9M/(4K^2),                                (5.2)

where the last inequality uses only `M>=1`. Equivalently the nonoverlap match probability `25/(16K^2)` and the overlap match probability `7/(4K^2)` are each at most `9/(4K^2)`.

Since `J` is a nonnegative integer, `P(J>=1)<=E J`, hence

    P(J=0)>=1-9M/(4K^2).                            (5.3)

On `J=0`, the ORIGINAL rule has `C_{Y_M,c}=0` for every `c`, and therefore outputs exactly `u`. Its target is still `p`. Nonnegativity of the loss on the remaining histories gives

    E TV(p^+_{Y_M},p)
      >=(1/4)P(J=0)
      >=(1/4)[1-9M/(4K^2)].                         (5.4)

For `M=floor(K^2/100)` and even `K>=10`, we have `M>=1` and `M/K^2<=1/100`. Therefore (5.4) is at least

    (1/4)(1-9/400)=391/1600,

which proves (S005.2). Meanwhile `M+1>K^2/100`, so Theorem S005-A gives

    R_IID(K,M)
      <=sup_{p',mu'} E TV(B_pool,p')
      <=min{1,(3/2)sqrt(K/(M+1))}
      <=min{1,15/sqrt(K)} ->0.                       (5.5)

For every such `K`, the original worst-case risk is at least the specific-source risk in (S005.2). Since `R_IID(K,M)>0` by the lower theorem and is at most `15/sqrt(K)`,

    R_orig,IID^+(K,M)/R_IID(K,M)
      >=(391/24000)sqrt(K) ->infinity.

This proves failure of uniform minimax-order optimality. It also compares the two algorithms on exactly the same source, history length, and actual-endpoint TV objective: the pooled rule's risk on the displayed source tends to zero, while the original rule's risk stays above `391/1600`. It is not a lower bound for every algorithm at that single source. ∎

## 6. Interpretation, boundaries, and explicit nonclaims

1. **What condition changes the rate.** The all-row exact TWO-step-reset condition forces shared transition probabilities across every context. This structural equality allows pooling and reduces the class minimax mean-TV rate to `min{1,sqrt(K/(M+1))}`. This is stronger than merely having a fixed, nonzero minorization parameter below one. No beta-uniform `K^3` lower should be extended across this endpoint on the basis of this proof.

2. **Same goal, different algorithms.** The original full-history rowwise add-one, a rowwise suffix/burn-in add-one, and the pooled rule (P) are distinct objects. The good bound in Section 3 belongs to (P); it is not assigned to the original rule. Section 5 separately establishes an actual original-rule obstruction. In this exact class the endpoint target is `p` on every path, which is why the estimation reduction is exact, not a fixed-query substitution.

3. **Arbitrary initialization versus full-data lower.** The upper bound uses only the `M` symbols whose IID law is guaranteed under every `mu`. The minimax lower uses the stationary-initialized subclass, in which ALL `N=M+2` observations are IID and informative. Both original initial symbols are present in every data law used in the lower proof. Different `mu` may depend on the source across the supremum, as permitted by the frozen experiment; each is fixed within its trajectory.

4. **Small and large parameters.** The proof covers `K=2` (`d=1`), all odd `K` (one unused symbol in the lower family), and `M=1` (`N=3`). The rate cap handles `K` larger than the number of observations. The countersequence requires only an infinite even-`K` subsequence; no odd-`K` extension is needed to refute a proposed uniform statement over all `K,M`.

5. **Zeros and support.** No full-support assumption is used. The lower family deliberately permits a zero coordinate for odd `K`; the upper proof and transition equivalence allow zeros. The explicit separation family itself has strictly positive symbol probabilities, so the separation is not caused by zero edges or nonstationary initialization.

6. **Public information and computation.** The pooled algorithm reads only `K,M,H`, and is deterministic. Its counts can be accumulated in `O(M+K)` elementary operations with `O(K)` storage; this is an implementation bound for the stated count rule, not a computational lower bound or neural-realizability theorem. Every estimator in the lower infimum has the same public class information; none receives `p` or its signs.

7. **Sample requirement for the proved loss.** Let `c=1/(32 sqrt(6))`. For a target `0<delta<c`, achieving worst-case mean TV at most `delta` necessarily requires

       M+1 >= c^2 K/delta^2 = K/(6144 delta^2),

   by the lower bound. Conversely, the pooled rule suffices whenever

       M+1 >= (9/4)K/delta^2.

   These are loose-constant necessary/sufficient inequalities for the exact-reset class and this expected-TV objective. Thus the sample scale is `K/delta^2`, not a sharp finite-sample threshold or a high-probability guarantee.

8. **TV, squared TV, and KL remain distinct.** Every exported rate is for `E[TV]`. The affinity in the testing proof concerns full-history laws and is only a proved testing tool. No minimax prediction-`KL` or `E[TV^2]` rate is established here. From an upper bound on `E[TV]` alone one can infer `E[TV^2]<=E[TV]` because `0<=TV<=1`, but cannot square the upper bound. Jensen instead gives `(E[TV])^2<=E[TV^2]`. No unbounded KL transfer is used.

9. **Unsettled objects are not silently completed.** There is no matching all-`K,M` characterization of `R_orig,IID^+` in this unit, no claimed optimal dependence on an approximate-reset parameter, and no assertion that exact reset at `q>2` forces IID. The countersequence suffices for the specific uniform-optimality negation and nothing stronger is required or asserted.

## 7. Assembly and review interface

The dependency chain is entirely local:

    Lemma 1 (exact-reset equivalence and likelihood factorization)
      -> Lemma 2 (uniform pooled upper)
      -> Theorem S005-A upper;

    Lemma 1 + Lemma 3 (finite affinity/testing identities)
      -> Lemma 4 (full-N hypercube lower)
      -> Theorem S005-A lower;

    Lemma 1 + Lemma 5 (overlap-aware endpoint collision identity)
      -> Theorem S005-B original-rule separation.

No accepted result from S001-S004 is required. All constants, horizons, tests, and source families are explicit above. Independent review should check especially: the all-row equivalence, preservation of the full `N` observations in (4.6), the seed-integrated testing step, the factor `1/2` in the pointwise TV loss, and the last overlapping context in Lemma 5.
