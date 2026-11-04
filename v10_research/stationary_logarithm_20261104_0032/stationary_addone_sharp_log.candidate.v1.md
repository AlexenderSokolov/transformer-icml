# A stationary-mass and loss-sensitive bound for full-history add-one prediction

Analytical candidate, 4 November 2026 (UTC). Status: awaiting independent exact-file review. No numerical experiments or external uploads were performed. This document makes no literature-priority claim.

## 1. The result and precise observation model

Let A >= 2 and n >= 1. Observe X_1,...,X_{n+2} from a homogeneous second-order source on [A], with arbitrary transition rows and a stationary initial pair distribution. Zero transition probabilities, reducibility, periodicity, and multiple closed classes are allowed. Write D=A^2 and

    Y_i=(X_{i+1},X_{i+2}),                 0 <= i <= n,
    J_s=sum_{i=0}^{n-1} 1{Y_i=s},
    C_{s,b}=sum_{i=0}^{n-1} 1{Y_i=s,X_{i+3}=b},
    B_s(b)=(C_{s,b}+1)/(J_s+A).

Let p_s denote the true next-symbol row and pi the stationary pair distribution. All logarithms are natural, and log_+(x)=max{log x,0} for x>0. The proposed bound is

    E D_KL(p_{Y_n} || B_{Y_n})
      <= min{ log(n+A),
              14000 A^3/(n+1) [1+log_+((n+1)/A^3)] }.       (1)

For n=0 the risk is at most log A. The estimator and its actual terminal query are not modified, randomized, conditioned away, or replaced by an independent test context. No mixing assumption is used.

The argument refines the previously reviewed stationary row-tilt proof in two places: retain the target's stationary mass in the deviation coefficient, and use a loss-sensitive positive-log estimate at small row counts. The first removes the unnecessary high-count bands; the second avoids paying A/m at counts m<A.

## 2. Stationary fixed-target occupation

For a stationary finite-state Markov chain with law rho, a target s, and integer w>=1,

    P_rho(Y_n=s, J_s<w) <= w/(n+1).                         (2)

Here J_s counts the n departure positions 0,...,n-1. To prove (2), put

    b_l=P_rho(Y_l=s, sum_{i=0}^{l-1}1{Y_i=s}<w).

Stationarity and restriction to a suffix imply b_l>=b_n for every l<=n. On every infinite path, only the first w occurrences of s can satisfy the corresponding condition, so sum_{l=0}^n b_l<=w. This proves (2).

For dyadic m in {1,2,4,...}, define

    E_{s,m}={Y_n=s, m<=J_s<2m},
    beta_{s,m}=min{2m/(n+1), pi(s)}.

Consequently

    P_pi(E_{s,m})<=beta_{s,m},
    sum_s beta_{s,m} <= min{2Dm/(n+1),1}.                  (3)

Both bounds retain the actual terminal selection.

## 3. The stationary-mass refinement of the row tilt

Fix a target s with pi(s)>0 and split its outgoing row into a group of probability p and its complement of probability 1-p, where 0<p<1. For 0<q<1 replace these two masses by q and 1-q while retaining their within-group proportions. Call the resulting kernel Q. Put

    r_min=min{q/p,(1-q)/(1-p)},
    r_max=max{q/p,(1-q)/(1-p)},
    lambda=log[q(1-p)/(p(1-q))].

The positive scaling preserves the transition support, hence all closed irreducible classes. Choose a Q-stationary distribution nu with the same weights on those classes as pi. On every unchanged class keep its original stationary distribution. On the class containing s use its Q-stationary distribution.

Let v_P(z) and v_Q(z) be expected visits to z from time 0 through the departure before the first positive return to s, when starting from s under P and Q respectively. These vectors are finite, satisfy v_P(s)=v_Q(s)=1, and obey

    r_min v_P(z) <= v_Q(z) <= r_max v_P(z).                (4)

For z!=s, (4) follows by conditioning on the first departure: until the next hit of s, the transition kernels coincide, and the first-departure distribution was scaled between r_min and r_max. For z=s, it follows from r_min<=1<=r_max. Write L_P=sum_z v_P(z) and L_Q=sum_z v_Q(z). The normalized excursion vector is stationary: shifting the visit sum by one time step replaces its initial s by its terminal s. Therefore, within the class containing s,

    pi(z)/nu(z)=(L_Q/L_P) v_P(z)/v_Q(z),
    pi(s)/nu(s)=L_Q/L_P in [r_min,r_max].

It follows that on the entire support of pi,

    pi(z)/nu(z) <= r_max/r_min=exp(|lambda|),              (5)
    pi(z)/nu(z) <= [pi(s)/nu(s)]/r_min.                    (6)

For (6) outside s's class the left side is 1, while the right side is at least 1 because L_Q/L_P>=r_min. This deals explicitly with mixtures of closed classes.

On any original-positive path having j departures from s and k departures in the first group,

    log [P_pi(path)/Q_nu(path)]
      =log[pi(Y_0)/nu(Y_0)] - j d(q||p) - (k-jq)lambda,   (7)

where d is binary forward KL. On either shifted one-sided event

    k>=jq+1 if q>p;       k<=jq-1 if q<p,                 (8)

the final term in (7) is at most -|lambda|. By (5), the initial ratio is canceled. By (6), it is canceled up to pi(s)/nu(s), because 1/r_min<=exp(|lambda|). Apply the two resulting likelihood bounds separately. Using stationary occupation under Q in the first, and Q_nu(Y_n=s)=nu(s) in the second, gives

    P_pi(E_{s,m}, event (8))
      <= min{2m/(n+1),pi(s)} exp[-m d(q||p)]
      = beta_{s,m} exp[-m d(q||p)].                       (9)

This is a statement about the intersection event, not a binomial law conditional on a count or on the terminal state. A different deterministic q and nu may be used for each application. Targets with pi(s)=0 have zero terminal contribution.

For a second-order source, the first group can be the next symbol b and its complement. This changes exactly one legal second-order row, not an arbitrary pair-chain transition.

## 4. Joint Bernstein bound and the large-count loss estimate

For t>=1 set delta=sqrt(2pt/m)+2t/(3m). For q=p+delta or p-delta in (0,1),

    d(q||p) >= delta^2/[2(p+delta/3)] >= t/m.              (10)

For completeness, if Z is a centered Bernoulli(p), then |Z|<=1 and E Z^2<=p. The exponential series gives

    log E exp(+-aZ) <= p a^2/[2(1-a/3)],  0<=a<3.

The variational formula for binary KL at a=delta/(p+delta/3) gives the first inequality in (10); substitution gives the second. On m<=j<2m,

    j delta <= sqrt(4jpt)+4t/3.

Thus the two sides of (9) imply

    P_pi(E_{s,m}, |C_{s,b}-J_s p_s(b)|
          >sqrt(4J_s p_s(b)t)+4t/3+1)
      <=2 beta_{s,m} e^{-t}.                             (11)

If a tilt would reach or cross 0 or 1, its corresponding strict deviation event is impossible. If p_s(b) is 0 or 1, the deviation is identically zero.

For x>=0 and a>0 let h(x,a)=x log(x/a)-x+a, with 0 log 0=0. The following deterministic implication is useful:

    |k-jp|<=sqrt(2jpu)+2u/3, u>=1
      implies h((j+1)p,k+1)<=48u(1+log u).                (12)

Here j>=0, p in [0,1], and 0<=k<=j. To verify it put z=jp and a=k+1. The premise and sqrt(2zu)<=z/2+u imply

    z<=2k+10u/3,
    (k-z)^2<=4zu+8u^2/9<=8ku+128u^2/9,
    ((j+1)p-a)^2<=16ku+31u^2,
    (j+1)p<=2a+10u/3.

The inequality h(x,a)<=(x-a)^2/a gives h<=47u when a>=u. If a<u then x<6u and a>=1, so h<=x log_+x+a<=6u log(6u)+u<=48u(1+log u). This proves (12).

The exact row identity, for sum_b k_b=j, is

    sum_b h((j+1)p_b,k_b+1)
      =(j+1)D_KL(p || (k+1)/(j+A))+(A-1)
        -(j+1)log[1+(A-1)/(j+1)]
      >=(j+1)D_KL(p || (k+1)/(j+A)).                     (13)

Fix s,b,m and put Z=h((J_s+1)p_s(b),C_{s,b}+1)/(J_s+1). Off the event in (11), the deviation is bounded by sqrt(8J_s p_s(b)t)+8t/3, so (12) with u=4t yields on E_{s,m}

    Z<=576t(1+log t)/m=:f_m(t).

Together with (3) and (11), layer-cake integration gives

    E[1_{E_{s,m}} Z]
      <=f_m(1) beta_{s,m}
          + integral_1^infty f_m'(t) 2 beta_{s,m}e^{-t}dt
      <=[576+3456/e] beta_{s,m}/m
      <2304 beta_{s,m}/m.                               (14)

The integral uses log t<=t-1, so integral_1^infty(2+log t)e^{-t}dt<=3/e, and e>2 suffices for the final strict inequality. Summing (14) over b and using (13) proves

    E[1_{E_{s,m}} D_KL(p_s||B_s)]
      <=2304 A beta_{s,m}/m.                             (15)

## 5. A low-count estimate that does not pay A/m

The exact alternative KL decomposition is

    D_KL(p || (k+1)/(j+A))
      =log[(j+A)/(j+1)]
          +sum_b p_b log[(j+1)p_b/(k_b+1)].               (16)

Terms with p_b=0 are defined to be zero. For j in [m,2m), the first term is at most log(1+A/m). Define

    ell_b=log_+[(j+1)p_b/(k_b+1)].

If 0<p_b<1, then

    ell_b>log 4
      implies k_b+1<(j+1)p_b/4<=jp_b/2,
      implies k_b<j(p_b/2)-1.                            (17)

The second inequality uses j>=1. Apply (9) with q=p_b/2. Binary KL satisfies

    d(p_b/2||p_b)>=p_b/8.                                (18)

Indeed, its second derivative with respect to its first argument is 1/[t(1-t)]. On [p_b/2,p_b] this is at least 1/p_b; Taylor's integral formula at p_b gives (18).

Also, j<2m and integrality give j+1<=2m, so ell_b<=log_+(2mp_b). Combining this pathwise bound, (17), (18), and (3),

    E[1_{E_{s,m}} ell_b]
      <= beta_{s,m} [log 4 + log_+(2mp_b)e^{-mp_b/8}]
      <10 beta_{s,m}.                                   (19)

Here log_+(2z)<=2z and sup_{z>=0} 2z e^{-z/8}=16/e<8, while log 4<2. If p_b=1 then k_b=j and ell_b=0, so (19) remains valid; p_b=0 contributes no weighted term. Multiplying by p_b and summing, sum_b p_b=1 gives from (16)

    E[1_{E_{s,m}} D_KL(p_s||B_s)]
      <=beta_{s,m} [10+log(1+A/m)].                       (20)

This estimate is for the full row loss. It does not sum an unweighted constant over all A output symbols.

## 6. Sum count bands and stationary masses

Let

    H=DA/(n+1),       T=(n+1)/(2D),       A/T=2H.

Summing (15) or (20) over s and using (3), the contribution of a dyadic band m is at most

    min{m/T,1} min{10+log(1+A/m), 2304 A/m}.              (21)

We may bound the finite collection of m<=n by the corresponding infinite positive series.

Low bands m<A: use (20) and min{m/T,1}<=m/T. Let M be the largest power of 2 below A. Then M<A, A/M<=2, and each band is M/2^k for a nonnegative integer k, possibly truncated at 1. Consequently

    sum_{m dyadic, m<A} m[10+log(1+A/m)]
      <=M sum_{k>=0} 2^{-k}[10+(k+2)log 2]
      =M(20+6 log 2)<26A.

Thus the total low-band risk is at most 26A/T=52H.

Middle bands A<=m<=T: if T<A there are none. Otherwise there are at most 1+log(T/A)/log 2 such bands, each costing at most 2304 A/T. Their total is bounded by

    4608H [1+log_+(T/A)/log 2].                           (22)

High bands m>=A and m>T: let m_0 be their first dyadic value. Then sum_{m>=m_0,dyadic}1/m=2/m_0<2/T, so their total from (15) is at most

    4608 A/T=9216H.                                     (23)

For J_{Y_n}=0, the row estimate is uniform and the loss is at most log A. By (2), summed over s, the contribution is at most

    D log A/(n+1)<=H.                                   (24)

Combining the low, middle, high, and zero-count bounds yields

    Risk <= H [13877 + (4608/log 2)log_+(T/A)]
         <=14000 H [1+log_+((n+1)/(DA))].                 (25)

For the last inequality use log 2>=1/2, T/A=(n+1)/(2DA), and 13877<14000. Finally B_s(b)>=1/(n+A), so the pathwise KL is at most log(n+A). This completes the proof of (1).

## 7. Relation to HJW and limitations

Han, Jana and Wu, Theorem 22, use N observed symbols and state the stationary second-order minimax order

    (A^3/N) log(N/A^3),  2<=A<=N^{1/3}/C_2.

The exact substitution here is N=n+2. Their constant C_2 can be enlarged to at least 2 without invalidating their theorem. On that domain, N/A^3>=8, so 1+log_+((n+1)/A^3) is bounded by an absolute multiple of log(N/A^3), and (n+1)^{-1} is bounded by 2/N. Therefore (1), together with their lower bound, would establish growing-alphabet minimax order for the unmodified full-history add-one predictor throughout the stated HJW second-order domain (with such a harmless enlargement of the unspecified constant). This conclusion is conditional on independent review of this new proof, not on numerical evidence.

The same analytical proof actually works with D context states and A outcomes whenever each single-row probability-group tilt is a legal kernel in the model. In particular, homogeneous order-r sources give D=A^r and the upper bound O(A^{r+1}/n [1+log_+(n/A^{r+1})]). This is an upper-bound extension, not a claim that every order/alphabet pair has this minimax rate. In particular, binary first-order stationary prediction has a smaller log log n/n minimax order, which this argument does not attain.

The proof is stationary. It does not improve the arbitrary-initial-law theorem or justify applying the sharper expression when the initial law is not stationary. The constant 14000 is deliberately loose.

## 8. Source and derivation bindings

- Starting proof: ../stationary_row_tilt_20261104_0023/stationary_terminal_kl.candidate.v1.md. Its Section 3 gives the excursion comparison, Section 4 the shifted likelihood cancellation, and Sections 5-7 the scalar Bernstein/KL integration. These ingredients are reproduced above.
- New refinements: the stationary target-mass comparison (6)-(9), the weighted positive-log bound (16)-(20), and the three-range summation (21)-(25).
- Primary theorem: Yanjun Han, Soham Jana and Yihong Wu, "Optimal prediction of Markov chains with and without spectral gap," IEEE Transactions on Information Theory 69(6), 2023, pp. 3920-3959, DOI https://doi.org/10.1109/TIT.2023.3239508; author preprint https://arxiv.org/abs/2106.13947v2; primary HTML https://arxiv.org/html/2106.13947v2.
- Published Theorem 22 and observation indexing were read in the local primary PDF at [preparation path omitted; see the DOI and source identity]; see also ../stationary_row_tilt_20261104_0023/sources/primary_source_matching_lower_audit.v1.md. The theorem's minimax estimator is not presumed to be the full-history add-one estimator.
