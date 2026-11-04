# Stationary row tilting with a one-count correction

Analytical candidate, 4 November 2026 (UTC). This is a new proof file, not a replacement of the prior arbitrary-start theorem. It requires independent exact-file review. No numerical experiment, simulation, training, external upload, public repository mutation, or literature-priority claim is made.

## 1. Main theorem

Let A >= 2 and n >= 1. Observe X_1,...,X_{n+2} from a homogeneous second-order source on [A], with arbitrary transition rows, and a **stationary initial pair distribution**. Zero transition probabilities, reducibility, periodicity, and multiple closed classes are allowed. Put D=A^2, Y_i=(X_{i+1},X_{i+2}), 0<=i<=n, and

    J_s = sum_{i=0}^{n-1} 1{Y_i=s},
    C_{s,b} = sum_{i=0}^{n-1} 1{Y_i=s,X_{i+3}=b},
    B_s(b) = (C_{s,b}+1)/(J_s+A),
    K_n = 1+floor(log_2 n).

Write p_s(b) for the true next-symbol row. All logarithms are natural, except the displayed log_2. Then the usual full-history add-one predictor satisfies

    E D_KL(p_{Y_n} || B_{Y_n})
      <= min{ log(n+A),
              A^2 [log A + 4608 A K_n]/(n+1) }.          (1)

For n=0 its risk is at most log A. In particular, this is a uniform O(A^3 log(n+2)/(n+1)) bound in the stationary model, with an absolute constant. It keeps the actual terminal context and the unmodified full-history estimator.

For arbitrary initial pair laws, the separate reviewed row-tilting theorem remains O(A^5 log(n+2)/(n+1)). Equation (1) does not extend the improved A^3 factor to arbitrary starts.

The new step is not to pretend the original stationary law remains stationary under a row change. Instead, initialize the changed kernel in its own stationary law, control the initial density ratio, and cancel that ratio using one extra count in a one-sided deviation event.

## 2. Stationary fixed-target occupation

For any stationary finite-state Markov chain with stationary law rho, any target state s, and integer w>=1,

    P_rho(Y_n=s, J_s<w) <= w/(n+1).                     (2)

Proof. Let b_m=P_rho(Y_m=s,sum_{i=0}^{m-1}1{Y_i=s}<w). For m>=ell, the event at time m implies fewer than w visits in the last ell departure positions. By stationarity the probability of the latter terminal event is b_ell, so b_m<=b_ell. On every infinite path at most the first w occurrences of s are counted by the flags defining b_0,...,b_n. Hence sum_{m=0}^n b_m<=w and (n+1)b_n<=w. No reversibility, mixing, or irreducibility is required.

Consequently, with r=1/(n+1) and E_m={Y_n=s,m<=J_s<2m},

    P_rho(E_m) <= 2rm.                                  (3)

## 3. Stationary-law comparison for changing one row

Let P be a finite-state transition matrix and pi a stationary distribution. Fix a state s with pi(s)>0. Split the destinations of row s into two groups of total masses p and 1-p, with 0<p<1. For 0<q<1 define Q by scaling the first group by q/p and the second by (1-q)/(1-p), leaving every other row unchanged. Define

    r_min=min{q/p,(1-q)/(1-p)},
    r_max=max{q/p,(1-q)/(1-p)},
    lambda=log[q(1-p)/(p(1-q))].

Then Q has a stationary distribution nu, supported on the same closed classes as pi and giving them the same weights, for which

    pi(z)/nu(z) <= r_max/r_min = exp(|lambda|)           (4)

at every z with pi(z)>0.

Proof within the closed irreducible class containing s. The support graph is unchanged because both scaling factors are positive. Let tau_s^+ be the first positive return to s, and define the excursion occupation vectors

    v_i(P)=E_s^P sum_{t=0}^{tau_s^+-1}1{Y_t=i},
    v_i(Q)=E_s^Q sum_{t=0}^{tau_s^+-1}1{Y_t=i}.

Their entries and total masses are finite because the class is finite and irreducible. In particular v_s(P)=v_s(Q)=1. For i!=s put

    g_i(y)=E_y sum_{t=0}^{tau_s-1}1{Y_t=i}, y!=s,
    g_i(s)=0,

where tau_s is the first hitting time of s. Until that hitting time no transition out of s is used, so g_i is the same under P and Q. Conditioning on the first departure gives

    v_i(P)=sum_y P(s,y)g_i(y),
    v_i(Q)=sum_y Q(s,y)g_i(y).

All terms are nonnegative. Therefore r_min v_i(P)<=v_i(Q)<=r_max v_i(P). The same bounds also hold for i=s since r_min<=1<=r_max. Normalized excursion occupation is stationary: v(P)P=v(P), because shifting the occupation sum by one step replaces the initial s by the terminal s. Thus the class-stationary probabilities are v_i(P)/sum_j v_j(P), and analogously for Q. Dividing these formulas proves (4).

For a reducible P, any stationary pi puts mass only on closed irreducible classes. Changing one row with positive support factors preserves all classes. Choose the Q-stationary law within the class of s as above, leave the stationary laws in the other classes unchanged, and retain all original class weights. On other classes pi/nu=1. This proves the assertion. If pi(s)=0, terminal events at s have probability zero under the original stationary law and need not be tilted.

The proof allows a one-state closed class. Such a class cannot have a nontrivial split into distinct destinations, but the comparison itself remains true for any valid grouped transition representation. Periodicity never enters the argument.

## 4. One-count cancellation in the path likelihood

Apply Section 3 to the pair chain, with the first group consisting of next symbol b. Fix s,b with p=p_s(b) in (0,1), and let q in (0,1). The changed row is

    q_s(b)=q,
    q_s(a)=p_s(a)(1-q)/(1-p), a!=b.                     (5)

This remains a legal homogeneous second-order source. It has the same transition support. Initialize P in pi and Q in the nu constructed above. On any path of positive original probability, with j=J_s and k=C_{s,b},

    P_pi(path)/Q_nu(path)
      = [pi(Y_0)/nu(Y_0)]
        (p/q)^k [(1-p)/(1-q)]^(j-k),

    log[P_pi(path)/Q_nu(path)]
      <= |lambda| - j d(q||p) - (k-jq)lambda,          (6)

where d is binary forward KL.

If q>p and k>=jq+1, then lambda>0 and the last term cancels |lambda|. If q<p and k<=jq-1, the same cancellation holds with lambda<0. Hence

    P_pi(E_m, k>=J_s q+1)
      <=2rm exp[-m d(q||p)], q>p,
    P_pi(E_m, k<=J_s q-1)
      <=2rm exp[-m d(q||p)], q<p.                      (7)

Here (3) is used under the genuinely stationary law Q_nu. The alternative stationary distribution is an analytical device, not something estimated by the predictor. Each deterministic threshold may use its own q and nu.

## 5. Joint Bernstein bound with one extra count

For t>=1 set

    delta=sqrt(2pt/m)+2t/(3m).

For q=p+delta or p-delta in (0,1),

    d(q||p)>=delta^2/[2(p+delta/3)]>=t/m.               (8)

For completeness, if Z is a centered Bernoulli(p), then |Z|<=1 and E Z^2<=p. Expansion of the exponential gives log E exp(+-aZ)<=p a^2/[2(1-a/3)] for 0<=a<3. In the variational formula for binary KL choose a=delta/(p+delta/3); this proves the first inequality. Substitution of delta proves the second. This is valid for either direction.

On m<=j<2m,

    j delta <=sqrt(4jpt)+4t/3.

Thus (7)-(8) imply

    P_pi(E_m, |C_{s,b}-J_s p|
           > sqrt(4J_s p t)+4t/3+1)
      <=4rm exp(-t), t>=1.                            (9)

If p+delta>=1 or p-delta<=0, the corresponding strict event is impossible, so an endpoint tilt is unnecessary. If p=0 or p=1, C_{s,b}=J_s p pathwise and the deviation event is empty. Strict inequalities in (9) imply the weak inequalities required in (7).

No conditional binomial statement is used. In particular, terminal selection and the row visit count are not conditioned away.

## 6. Scalar forward-KL estimate

For x>=0,a>0 put h(x,a)=x log(x/a)-x+a, with 0 log 0=0. The following deterministic estimate is inherited from the prior all-start proof and reproduced here:

    If j>=0, p in [0,1], 0<=k<=j, u>=1, and
    |k-jp|<=sqrt(2jp u)+2u/3, then
    h((j+1)p,k+1)<=48u(1+log u).                       (10)

To verify it, write z=jp, a=k+1, x=z+p. Since sqrt(2zu)<=z/2+u,

    z<=2k+10u/3,
    (k-z)^2<=4zu+8u^2/9<=8ku+128u^2/9,
    (x-a)^2<=16ku+31u^2,
    x<=2a+10u/3.

The inequality h(x,a)<=(x-a)^2/a gives h<=47u if a>=u. If a<u, then x<6u and a>=1, so h<=x log_+x+a<=6u log(6u)+u<=48u(1+log u). This proves (10).

For an A-symbol row q_b=(k_b+1)/(j+A), the exact identity is

    sum_b h((j+1)p_b,k_b+1)
      =(j+1)D_KL(p||q)+(A-1)
        -(j+1)log[1+(A-1)/(j+1)]
      >=(j+1)D_KL(p||q).                              (11)

## 7. Integrate, then sum

Fix s,b,m and let Z=h((J_s+1)p_s(b),C_{s,b}+1)/(J_s+1). Outside the event in (9), and for t>=1,

    |C_{s,b}-J_s p|
      <=sqrt(4J_s p t)+4t/3+1
      <=sqrt(8J_s p t)+8t/3.

Thus (10), with u=4t, implies on E_m

    Z<=192t[1+log(4t)]/m
      <=576t(1+log t)/m=:f_m(t).                       (12)

The latter inequality uses 1+log 4<=3. Therefore P_pi(E_m,Z>f_m(t))<=4rm e^(-t). Since f_m is increasing, layer-cake integration and (3) under P_pi give

    E_pi[1{E_m}Z]
      <=f_m(1)P_pi(E_m)
        + integral_1^infty f_m'(t)P_pi(E_m,Z>f_m(t))dt
      <=1152r+2304r integral_1^infty(2+log t)e^(-t)dt
      <=1152r+6912r/e
      <4608r.                                        (13)

Use log t<=t-1 to bound the integral by 3/e; the final inequality uses e>2.

The K_n disjoint bands m=1,2,4,...,2^floor(log_2 n) cover J_s=1,...,n. Summing (13), followed by (11), over D contexts, A symbols, and K_n bands gives

    E_pi[1{J_{Y_n}>=1}D_KL(p_{Y_n}||B_{Y_n})]
      <=4608 D A K_n/(n+1).                           (14)

For zero visits, B is uniform and the loss is at most log A. Equation (2), summed over s with w=1, gives P_pi(J_{Y_n}=0)<=D/(n+1). Therefore

    E_pi[1{J_{Y_n}=0}D_KL(p_{Y_n}||B_{Y_n})]
      <=D log A/(n+1).                                (15)

Equations (14)-(15) prove the second term in (1). The pathwise bound B_s(b)>=1/(n+A) yields D_KL(p_s||B_s)<=log(n+A), proving its first term.

## 8. What is and is not gained

1. Stationarity improves the leading alphabet dependence from A^5 to A^3 in this log(n) upper bound, without changing the estimator or the terminal query. The all-start theorem is unchanged.
2. If A=A_n varies, (1) guarantees consistency whenever A_n^3 log(n+2)/(n+1) tends to zero, equivalently as a sufficient condition A_n=o((n/log n)^(1/3)). This is a sufficient condition from this bound, not a necessary condition for add-one consistency.
3. Han, Jana and Wu, Theorem 22, give the stationary second-order minimax order A^3/N * log(N/A^3), in the stated domain 2<=A<=N^(1/3)/C_2. Here their observed-symbol length is N=n+2. Equation (1) retains log n rather than log[(n+2)/A^3]. Thus it does not establish uniform growing-alphabet minimax optimality or the entire add-one question stated in their Remark 1.
4. In subregimes A^3 <= (n+2)^(1-eta), for any fixed eta>0, the two logarithms are comparable, with constants depending on eta. Together with the cited lower bound, and within its domain, this gives matching order for the full-history predictor in those subregimes. Near the boundary A^3 comparable to n, no such conclusion follows from (1).
5. No reversibility assumption is needed. Reversibility of an order-two symbol process should not be confused with ordinary reversibility of its overlapping-pair chain. This proof uses neither notion.
6. For a stationary ordinary D-state Markov chain with D possible next states, the same proof gives O(D^2 log n/n). Its stationary binary first-order instance does not match the distinct log log n/n minimax rate.
7. This document asserts an analytical bound pending exact-file review, not literature priority or resolution of all growing-alphabet regimes.

## 9. Why retaining the original initial law loses the dimension

This limitation does not contradict the proof above, which changes the alternative initial law and pays the one-count correction.

For every A>=2 there is a legal pair-chain ring through all L=A^2-1 contexts other than s=(a,a). One construction is an Euler circuit through the directed symbol graph with all A^2 directed edges except (a,a); consecutive graph edges are the ring's pair states. This graph is balanced and strongly connected. Choose consecutive ring states g=(b,a), h=(a,c) with b,c!=a.

At s let the chain self-loop with probability 1-p and go to h with p. All ring steps are deterministic except at gateway g: go to s with probability epsilon and to h with 1-epsilon. This is irreducible and aperiodic for 0<p,epsilon<1. With p=epsilon/L its stationary law is

    pi(s)=1/2,
    pi(z)=1/(2L), every ring state z.                   (16)

Tilt only the row s, replacing p by q, and retain pi as the initial law under Q. For any integer K>=2 choose epsilon=1/K and n=1+LK, so p=1/(n-1). Let F be the event that the path starts at s, immediately enters the ring, bypasses the gateway K-1 times, and returns to s at its Kth gateway encounter. On F,

    Y_n=s, J_s=1, C_{s,c}=1,

    P_pi(F)=[1/(2LK^2)](1-1/K)^(K-1)
             >=L/[2e(n-1)^2],
    Q_pi(F)=[q/(2K)](1-1/K)^(K-1)
             >=qL/[2e(n-1)].                          (17)

Consequently any proposed bound Q_pi(Y_n=s,J_s<w)<=Cw/(n+1) holding for all such original-stationary row tilts needs C>=qL/(4e), by taking w=2. This is Omega(A^2) for fixed q>0, even as K and n/A^3 become arbitrarily large.

A related general envelope proof uses

    M_pi(Q)=sum_z sup_{t>=0}(pi Q^t)(z),

and gives (n+1)Q_pi(Y_n=s,J_s<w)<=w M_pi(Q): apply the suffix argument for each suffix length ell, dominate its initial distribution by sup_t(pi Q^t)(z), sum over ell, and use the pathwise first-w-visits count for each starting state. In the ring example every ring vertex receives at least q/2 mass at its first-lap time from the initial s mass. Thus M_pi(Q)>=qL/2. This potential cannot uniformly replace the dimension by an absolute constant.

Even an unshifted stationary-P occupation-times-full-Chernoff bound fails with a dimension-free coefficient. Set q=1-p. For p<=1/4,

    exp[-d(1-p||p)]<=4p.

Indeed the ratio of its left side to p equals p^(-2p)(1-p)^(-1+2p), at most (4/3)exp(2/e)<4. On F, k/j=1>=q. Thus a bound

    P_pi(E_1,C_{s,c}/J_s>=q)
      <=[2C/(n+1)] exp[-d(q||p)]

would require C>=L/(16e), using (17). This is a barrier to that particular unshifted factorization, not a lower bound on add-one risk or on every loss-sensitive argument. In fact F does not satisfy the shifted event k>=jq+1, so it is fully consistent with (7). The +1 correction is essential to this repair.

## Sources and proof provenance

- Prior all-start theorem and deterministic scalar estimate: ../fixed_alphabet_kl_sharpening_20261103_2346/tilted_occupation_terminal_kl.candidate.v1.md, Sections 4-7. This file reproduces the needed scalar argument and changes the probability comparison explicitly.
- Prior independent source audit for model, indexing and lower theorem: ../fixed_alphabet_kl_sharpening_20261103_2346/primary_source_matching_lower_audit.v1.md.
- Yanjun Han, Soham Jana and Yihong Wu, "Optimal prediction of Markov chains with and without spectral gap," IEEE Transactions on Information Theory 69(6), 2023, pp. 3920-3959. DOI: https://doi.org/10.1109/TIT.2023.3239508 . Author preprint: https://arxiv.org/abs/2106.13947v2 . Primary HTML inspected for Theorem 22, definition (95), and Remark 1: https://arxiv.org/html/2106.13947v2 . Published theorem and indexing were independently checked in the prior source audit; this proof does not claim to survey subsequent literature.
- Sections 2-7 and 9 contain self-contained analytical derivations. The normalized excursion-occupation identity is proved where used; no unverified stationary-perturbation formula is assumed.
