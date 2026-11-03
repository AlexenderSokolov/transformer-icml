# KH001 — Histogram adaptation obstruction above the critical certificate (candidate)

2026-11-02. New author candidate; fresh full independent review and root acceptance required. This is a **triple-histogram-plus-initial/final-PAIR** result, not a full-history impossibility. All accepted proof files are unchanged. The full-history question is treated separately.

## 1. Finite statement and asymptotic consequence

Use the protected-endpoint binary source-corruption experiment, but restrict the predictor to the exact eight triple counts and the initial/final pairs, as in accepted BK001. It may know beta, randomize and use unlimited computation; the adversary acts on the full word with a strict pointwise Hamming budget.

Put c=2^-12. Fix M>=64, beta in [1/M,1/16], delta=sqrt(beta), T=floor(1/(8beta)), and an integer k satisfying

    32<=k<=T,  k^2>=4M,  k delta>=6/c,
    delta^5 k^3>=2^20,  delta^3 k^2>=2^21.           (1.1)

For each j=k,...,T, set

    x=c k/M, y_j=j/M, w_j=1-y_j-2x,
    a_j=c k(1-delta)/j, b=delta, e=1-delta,
    tau_j=x delta/w_j,
    Pi_j=(y_j,x,x,w_j), theta_j(1)=(a_j,delta,delta,1-tau_j).

These are stationary sources Q_j satisfying the all-state certificate with the SAME supplied beta. Let S be the estimator's supremum clean risk over this family. There is a stationary first-order null Q_* in the same beta class, and one common protected strict-k kernel, such that

    R_null >=[(c k/(64M)-S) log((T+1)/k)]_+.         (KH1)

Also H_2(M,k,beta)<=2k/M.

Consequently, on EVERY prescribed curve satisfying

    beta_M>=1/M eventually, beta_M sqrt(M)->0,       (1.2)

no histogram-plus-pairs estimator supplied beta_M and blind to k can attain the known-k profile with one finite constant over all budgets. Failure is stationary. This extends the histogram-only negative region above beta=1/M; it does not transfer to full-history predictors.

Together with separately accepted KA001 (receipt `intake/KA001_acceptance.json`), the resulting power-law interpretation is stated in §9, not silently used as a premise for the present lower bound.

## 2. Explicit asymmetric null — the long prefix is not free

Let r=1/(2M). The null is a stationary first-order binary source with

    T_*(1,0)=r, T_*(0,1)=beta,
    pi_*(1)=beta/(beta+r), pi_*(0)=r/(beta+r).

Its pair stationary law is Pi_*(u,v)=pi_*(u)T_*(u,v). For every starting pair and target pair,

    P_*^2((u,v),(s,t))/Pi_*(s,t)=T_*(v,s)/pi_*(s).

Since beta+r<=1, each ratio is at least beta+r>=beta. This checks the all-state pair certificate, not merely the one-state entry probability. Because beta>=1/M=2r, pi_*(1)>=2/3.

For j=k,...,T let x^(j)=1^(N-j)0^j. Its EXACT full-word probability is

    v_j=pi_*(1)(1-r)^(M+1-j) r(1-beta)^(j-1).

The prefix exponent is retained. Since j>=1 and beta*j<=1/8,

    (1-r)^(M+1-j)>=(1-r)^M>=1/2,
    (1-beta)^(j-1)>=7/8,
    1/(8M)<=v_j<=1/(2M).                           (2.1)

The lower follows from 7/(48M)>=1/(8M). These probabilities are not asserted identical across j. At the actual terminal pair 00 the null target probability of symbol1 is beta, NOT r.

## 3. Clean family, all-state certificate, and a common atom

As beta>=1/M, T<=M/8. The domain gives j>=k, so a_j<=c. Also w_j>=1-1/8-c/4>=3/4 and tau_j<=1/4. Since j<=1/(8delta^2) and e>=1/2,

    a_j>=4c k delta^2>=delta,

using k delta>=6/c. In particular a_j>=2beta because delta<=1/4. All probabilities and stationary masses are positive and legal.

The identities y_j a_j=x e and w_j tau_j=x delta establish stationarity. The pair-kernel square is exactly

    [ (1-a)^2, (1-a)a, a e,         a delta        ]
    [ e^2,      e delta, delta tau, delta(1-tau)   ]
    [ e(1-a),   e a,     delta e,   delta^2        ]
    [ tau e,    tau delta, (1-tau)tau, (1-tau)^2  ].

Compare to delta^2(y,x,x,w). The two small cross entries delta*tau=tau*delta=delta^2*x/w dominate delta^2*x. Further,

    tau e=delta*y*a/w>=delta^2*y,
    a delta>=delta^2*w,
    (1-tau)tau=x delta(1-tau)/w>=delta^2*x.

The delta(1-tau) and delta^2 entries dominate their target delta^2*w. The e delta and delta e entries dominate delta^2*x. Because x=y*a/e<=a/e, the three positions (00,01), (00,10), and (10,01), with entries (1-a)a, a*e, and e*a, also dominate delta^2*x. The remaining four entries are at least9/16 and their targets at most1/16. This covers all sixteen entries by the same exact partition as the accepted BK001 certificate, with the present parameters explicitly checked.

The four length-three paths into 11 used in BK001 give

    P_j^3(u,11)>=a_j delta/2>=lambda_j,
    lambda_j=c k delta/(4j).                        (3.1)

Thus TV contraction after h steps is at most alpha_h=(1-lambda_j)^floor(h/3). For a stationary copy W of this chain and any state subset D, the covariance argument gives

    Var[J_D(W)]<=7M Pi_j(D)/lambda_j.               (3.2)

Here J_D counts exactly the M departures. These are properties of this explicit family; no general binary square-root-beta mixing assertion is made.

## 4. Exact binary reversal identity and endpoint corrections

Let a stationary binary second-order source have designated exits (a,b,e,tau) and full-support stationary law (y,x,x,w). Stationarity gives ya=xe and w*tau=xb. Its reversed pair kernel is P^*=diag(Pi)^(-1)P^T diag(Pi). Let R swap the two bits of a state, so R exchanges01 and10 and fixes00,11. Direct substitution using those two flow identities gives

    R P^* R=P.

Equivalently, reversing the entire stationary bit word leaves its probability unchanged. This is an elementary identity for binary order2 chains, not an asserted literature novelty. It can also be checked from equality of stationary triple probabilities001=100 and011=110, the remaining binary triples being palindromes.

For the present Q_j, let F_j={Y_0=11,Y_M=00}. Under stationary Q_j conditioned on F_j, reversing the word produces the SAME kernel P_j started at00 and conditioned to finish at11. Thus

    P_j(F_j)=y_j P_j^M(00,11).                      (4.1)

The reversed departure counts are NOT identical to the original counts. If Z_m=R Y_(M-m), then on F_j,

    J_00(Z)=J_00(Y)+1,
    J_cross(Z)=J_cross(Y), J_cross=J_01+J_10.        (4.2)

This follows because reversal replaces departures0,...,M-1 by original indices1,...,M; the endpoints are11 and00. The +1 will be paid explicitly below.

By Bernoulli's reciprocal bound and floor(M/3)>=M/4,

    alpha_M<=1/(1+lambda_j M/4).

Since j<=1/(8beta), M beta>=1 and k delta>=6/c,

    lambda_j M/4=c k delta M/(16j)
                    >=(c/2)k delta M beta>=3.

Therefore P_j^M(00,11)>=w_j-1/4>=1/2, and

    P_j(F_j)>=y_j/2=j/(2M).                         (4.3)

The original rare terminal event still has probability of order j/M. Reversal is used only to analyze its CONDITIONAL concentration; it does not remove this factor from clean-risk accounting. In particular,

    E[|A(T(X))(1)-a_j| | F_j]<=2SM/j.               (4.4)

## 5. Reverse-start coupling avoids a rare-event concentration loss

Couple a P_j chain Z started at00 to a stationary copy W. At three-step block boundaries, use the common atom in (3.1): with probability lambda_j, both chains' next boundary state is11; fill each block by its appropriate conditional bridge. After that first common-atom success, use the same transitions forever. Let sigma be this meeting time. Both marginals have the correct P_j path laws, and

    E sigma<=3/lambda_j.

Counts before time sigma can differ at at most sigma departure indices. Hence, for any state subset D,

    |J_D(Z)-J_D(W)|<=sigma.                         (5.1)

No independence of sigma from W is required for the subsequent union bound. The stationary copy has E J_00(W)=j and E J_cross(W)=2ck.

Suppose

    sigma<=k/32,
    |J_00(W)-j|<=k/8,
    J_cross(W)<=k/32.                               (5.2)

On the event Z_M=11, reverse Z back to an original word Y with initial11/final00. Since k>=32, (4.2) and (5.1) give

    |J_00(Y)-j|<=k/8+k/32+1<=3k/16<k/4,
    J_cross(Y)<=k/32+k/32=k/16.                     (5.3)

The endpoint correction is explicitly included; it is not dropped by identifying forward and reversed departure counts.

The three unconditional failure bounds under this coupling are:

    P(sigma>k/32)<=384j/(c delta k^2),
    P(|J_00(W)-j|>k/8)<=1792j^2/(c delta k^3),
    P(J_cross(W)>k/32)<=229376j/(delta k^2).         (5.4)

The first is Markov's inequality using E sigma. The second is (3.2) with Pi(00)=j/M and Chebyshev threshold k/8. For the third, E J_cross(W)=2ck<=k/64; exceeding k/32 entails deviation greater than k/64. Apply (3.2) with Pi(cross)=2ck/M.

Conditioning the reverse-start chain on Z_M=11 costs at most a factor2 by §4, NOT a factor M/j. Union bound, j<=1/(8delta^2), and c=1/4096 yield

    P[ (5.3) fails | F_j ]
       <=229376/(delta^5 k^3)+450560/(delta^3 k^2)
       <=7/32+55/256=111/256<1/2.                  (5.5)

The last line uses the explicit finite conditions (1.1). Thus at least half of the correctly conditioned clean words obey (5.3).

## 6. Histogram-preserving canonicalization and strict kernel

Use the exact canonicalization from accepted BK001 §5: remove all111 and000 self-loops from the pair path, prepend the former at initial11, retain the other edges in their original order, and append the latter at terminal00. It preserves every triple count and both endpoint pairs. For any such word X, exact endpoint-flow identities give

    d_H(Can(X),1^(N-j)0^j)
       <=3J_cross(X)+|J_00(X)-j|.                  (6.1)

This identity holds for the fixed, pre-sampling integer j, not a random reselected suffix length. On (5.3), the right side is at most7k/16<k.

For each fixed public problem M,beta,k, define one stochastic map on full input words. It is identity except on x^(j), k<=j<=T. On such a word, sample a full stationary Q_j word conditioned on F_j, form Can(X), and output it only if its Hamming distance to the observed input is <=k; otherwise output the original input. The auxiliary family is a public construction fixed across sources, not an unknown table read from the true source. As a map on words, it has no source-law, stationary-law, hidden-parameter or clean-interior input. Its fixed auxiliary table entries may equivalently be hardcoded into that one map; no runtime oracle is needed.

Every outcome respects the strict budget. Both endpoint pairs remain11/00, so the actual final pair is protected and initial pair preservation is stronger than required. Acceptance probability is at least1/2 by (5.5). Auxiliary parameter probabilities may be real at a general beta; the model permits stochastic kernels on a finite set, and no rational-implementation or efficient-sampling assertion is made.

The histogram-plus-pairs predictor has exactly the same input statistic on Can(X) as on X. A full-history predictor need not do so. This is the sole observation restriction used in transferring clean prediction error.

## 7. Risk comparison with correct target and nonconstant null weights

On accepted samples, the null target is beta and the clean comparison target is a_j>=2beta. Triangle inequality and acceptance>=1/2 yield

    E[null loss | x^(j)]>=a_j/4-2SM/j,              (7.1)

using the clean conditional bound (4.4). Rejecting samples only discards nonnegative losses. Independent estimator randomization can be averaged throughout.

Now v_j is NOT constant across j. Bound the nonnegative positive and error terms separately using (2.1). Since a_j=ck e/j>=ck/(2j),

    R_null >=sum_j [ (1/(8M)) ck/(8j)
                            -(1/(2M)) 2SM/j ]
            =(ck/(64M)-S) sum_(j=k)^T 1/j.

If this coefficient is negative, unit nonnegativity gives the positive-part statement. If nonnegative, use the harmonic integral. This proves exactly (KH1) with no invalid replacement of a multiplier in front of a negative quantity.

For the known-k benchmark, delta>=1/sqrt(M) and k>=2sqrt(M), so

    F_2<=(k/M)+1/(M delta)<=(k/M)+s<=2k/M,
    H_2<=2k/M.                                     (7.2)

The cap does not create a problem. All clean/null sources are stationary members of the same supplied beta class.

## 8. Nonadaptivity on every stronger-side curve (1.2)

Let U_M=1/beta_M and L_M=max{sqrt(M),beta_M^(-5/6)}. Under (1.2), beta_M tends to zero and

    L_M/U_M=max{beta_M sqrt(M),beta_M^(1/6)}->0.

Choose k_M=floor(sqrt(U_M L_M)). Then k_M/U_M->0 while k_M/L_M->infinity. In particular,

    k_M/sqrt(M)->infinity,
    beta_M^(5/2)k_M^3->infinity,
    beta_M^(3/2)k_M^2->infinity,
    k_M sqrt(beta_M)->infinity,
    log((floor(1/(8beta_M))+1)/k_M)->infinity.

The fourth limit follows from beta_M>=1/M and the first. All finite conditions (1.1) therefore hold eventually. If an all-budget estimator had S<=C_curve/sqrt(M), the error S in (KH1) would be negligible relative to ck_M/(64M). The actual risk is then at least a positive multiple of (k_M/M)log(1/(beta_M k_M)), whereas (7.2) bounds H_2 by2k_M/M. Their ratio diverges.

This proves the claimed histogram-only failure for every fixed curve (1.2), even allowing the constant to depend on the curve and giving beta_M to the estimator. It does not prove that ordering is sufficient for adaptation.

## 9. Power-law implication and dependency boundary

For beta_M=M^(-gamma) with1/2<gamma<=1, condition (1.2) holds and this theorem gives histogram-plus-pairs nonadaptivity. For1<gamma<2, accepted KA001's intermediate full-history obstruction also rules out histogram procedures. For0<=gamma<=1/2 and gamma>=2, accepted KA001's ordinary-add-one uppers work for the histogram statistic as well.

Thus the combination gives a complete POWER-LAW classification for this exact statistic: adaptive at gamma<=1/2 or gamma>=2, nonadaptive at1/2<gamma<2. This is not a classification for unrestricted full-history estimators, arbitrary non-power-law curves, or richer boundary interfaces. KA001 is not required for the finite (KH1) theorem or the stronger-side negative result; its exact accepted bytes and receipt are separate inherited dependencies for the combined table.

The new probabilistic ingredients are the exact reversal/coupling composition and its corrected departure counts. BK001 supplies canonicalization; SC003/BT002 supply the known-k benchmark. All diagnostics and independent review are separate requirements. No external novelty, formal-verification, efficient/causal attacker, revealed mask/seed, edited-target, neural-resource or training claim is made.
