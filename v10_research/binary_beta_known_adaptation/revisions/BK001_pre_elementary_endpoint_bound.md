# BK001 — Supplied-beta adaptation requires more than a triple histogram (candidate)

2026-11-02. New author candidate, not reviewed or accepted. Accepted AB001–AB003 remain unchanged. This is a **histogram-restricted** obstruction, not a resolution of the full-history supplied-beta question.

## 1. Exact result

Use the binary source-corruption experiment with the actual final pair protected, but restrict the predictor's observation to

    T(X)=(X_1,X_2, X_(M+1),X_(M+2), (N_abc(X))_(a,b,c in {0,1})),

where N_abc counts all M overlapping triples. Counts are exact and unquantized. The predictor may know M and beta, randomize, and use unlimited computation, but it does not see the ordering beyond this statistic. The adversary still sees and edits the full original word.

Fix c=2^-12 and an integer n>=4096. Put

    M=n^10, k=n^9, beta=1/M, delta=n^-5, r=1/(2M),
    T0=floor(M/8), x=c k/M, e=1-delta.

For each integer j in [k,T0], define a stationary source Q_j by

    y_j=j/M, w_j=1-y_j-2x,
    a_j=x e/y_j=c k e/j,
    b_j=delta, e_j=e,
    t_j=x delta/w_j=c k delta/(M-j-2ck),
    theta(1)=(a_j,b_j,1-e_j,1-t_j),
    Pi_j=(y_j,x,x,w_j).

Every Q_j satisfies the SAME all-state certificate P_j^2>=beta Pi_j. Let S be the supremum of a histogram estimator A_(M,beta)'s clean identity-corruption risk over these Q_j. Let Q_* be the stationary binary symmetric first-order flip-r source; it also satisfies the same certificate beta=1/M.

There is one source-independent strict-k protected kernel C_(M,k) on full binary words such that

    R_*(A,C_(M,k))
       >= [ (c k/(64M)-S/2) log((T0+1)/k) ]_+.       (BK1)

The same map A_(M,beta) occurs in S and in the corrupted null risk. In particular **no histogram-only estimator family independent of k, even when beta is supplied, attains the binary known-k profile uniformly for all k and beta**, already under stationary initialization. This is a constrained-risk conclusion; it is not a known-k minimax lower beyond the accepted profile.

No implication of impossibility is made for a predictor receiving the full corrupted word. The proof deliberately changes word order while preserving T, which such a predictor could detect.

## 2. Stationarity and every all-state certificate entry

All parameters are legal. In the stated domain,

    0<delta<=1/4, 0<a_j<=c<=1/4, a_j>=delta,
    0<x<=c, 0<y_j<=1/8, w_j>=3/4, 0<t_j<=1/4.

For example a_j>=8ck e/M>=4c/n>=n^-5=delta, since 4c n^4>=1. The stationarity identities are

    y_j a_j=x e,  w_j t_j=x delta,

and the crossing masses are equal, proving Pi_j P_j=Pi_j.

Suppress j and write a=a_j,t=t_j,y=y_j,w=w_j. The complete P^2 matrix, with state order 00,01,10,11, is

    [ (1-a)^2, (1-a)a, a e,        a delta       ]
    [ e^2,      e delta, delta t,  delta(1-t)    ]
    [ e(1-a),   e a,     delta e,  delta^2       ]
    [ t e,      t delta, (1-t)t,   (1-t)^2       ].

Compare to beta Pi=delta^2(y,x,x,w). The entries delta*t=t*delta=delta^2*x/w are >=delta^2*x. Also

    t e=delta*y*a/w >=delta^2*y,
    a delta>=delta^2*w,
    (1-t)t=x delta(1-t)/w>=delta^2*x,

using a>=delta>=delta*w and 1-t>=3/4>=delta*w. The entry delta^2 dominates delta^2*w. Entries e delta and delta e dominate delta^2*x since e>=3/4>=delta*x. The entries (1-a)a and e*a dominate delta^2*x: x=y*a/e<=a/e, while 1-a,e>=3/4 and delta^2/e<=1/12. The remaining diagonal/00-column entries are at least 9/16 and dominate the respective delta^2*y or delta^2*w (at most 1/16). Likewise delta(1-t)>=delta^2*w. This checks all sixteen entries, not merely the stationary flows or a subset of rows.

For Q_*, with one-step kernel T_r, Pi_*(u,v)=T_r(u,v)/2 and

    P_*^2((u,v),(s,t))=T_r(v,s)T_r(s,t)>=2r Pi_*(s,t).

Thus Q_* has the same beta=2r=1/M on every pair state. Its true symbol-1 probability at terminal 00 is r.

## 3. A uniform three-step atom and occupation variance

For Q_j, from 00 the path 00->00->01->11 has probability (1-a)a delta; from 01 the path to 11 followed by two 11 self-loops has probability delta(1-t)^2; from 10 the path 10->00->01->11 has probability e a delta; and from 11 three self-loops have probability (1-t)^3. Therefore

    P_j^3(u,11)>=(a delta)/2>=lambda,
    lambda=c k/(4 M^(3/2)),                         (3.1)

for every u and every j in the stated range. The final lower uses a>=ck/(2M). This is a common-atom minorization for this explicit family, not a claimed improvement for arbitrary binary chains.

Splitting each three-step kernel into lambda*delta_11+(1-lambda)R gives TV contraction. In particular, for every initial state u,

    TV(P_j^h(u,.),Pi_j)<=(1-lambda)^floor(h/3)=alpha_h.

Also sum_(h>=1)alpha_h<=3/lambda. Under stationary initialization, for any state subset D and its departure occupation J_D=sum_(m=0)^(M-1)1{Y_m in D},

    |Cov(1{Y_0 in D},1{Y_h in D})|<=Pi_j(D)alpha_h,

because the conditional probability differs from Pi_j(D) by at most alpha_h. Consequently

    Var(J_D)<=7M Pi_j(D)/lambda.                    (3.2)

This includes D={00} and D={01,10}; no independence of visits is asserted.

## 4. Endpoint conditioning is charged, not treated as constant probability

Let F_j={Y_0=11,Y_M=00}. With y=j/M and w>=1/2,

    P_j(F_j)=w P_j^M(11,00)>=y/4.                   (4.1)

Indeed alpha_M<=exp(-lambda floor(M/3))<=exp(-c k/(16sqrt(M)))=exp(-c n^4/16). For n>=32 this is <=1/(2n)<=y/2: at n=32 the exponent is 16>log(64), and c n^4/16-log(2n) is increasing thereafter. Our n>=4096 domain is more than sufficient.

Consider a full stationary Q_j word conditional on F_j. Its clean target at the endpoint is a_j. Since the contribution of F_j is part of its unconditional clean risk,

    E[ |A_(M,beta)(T(X))(1)-a_j| | F_j ]
       <= S/P_j(F_j)<=4SM/j.                        (4.2)

The factor M/j is essential. No conditional stationary law or conditional-IID assertion is made.

## 5. Canonicalization preserves the full triple histogram exactly

For any word starting in pair 11 and ending in pair 00, view its M triples as directed edges in the four-state pair graph. Remove all 111 and 000 self-loops from its path; removing a self-loop preserves the current vertex, so the remaining edge sequence is still a legal path from 11 to 00. Let L_1=N_111,L_0=N_000 and E=M-L_0-L_1. Prepend all L_1 loops at vertex 11, traverse the remaining path in its original order, and append all L_0 loops at vertex 00. Call the resulting word z=Can(X).

This operation preserves every triple count and both endpoint pairs exactly. The resulting word has the form

    1^(L_1+2) [E emitted skeleton bits] 0^(L_0).

Let x^(j)=1^(N-j)0^j be the null one-flip word with exactly j terminal zeros. Its terminal pair is 00 since j>=k>=2. Compare z first with the monotone word having L_0 terminal zeros. They differ only within the E skeleton positions. The two monotone words differ in exactly |L_0-j| positions. Hence

    d_H(z,x^(j))<=E+|L_0-j|.                        (5.1)

Write U=N_001,V=N_110 and J_cross=J_01+J_10. Exact flow identities for initial11/terminal00 give N_100=U+1 and N_011=V-1. Thus U<=J_10-1 and V<=J_01+1, so U+V<=J_cross. Since E=U+V+J_cross and L_0=J_00-U, (5.1) implies

    d_H(Can(X),x^(j))
       <=3 J_cross+|J_00-j|.                        (5.2)

This explicitly charges the random occupancy mismatch from the fixed, pre-sampling null suffix length j. It is not assumed that a sampled clean word has exactly j zero-row departures.

## 6. At least half of conditioned samples fit the strict budget

The stationary occupation means are E J_00=j and E J_cross=2ck. Set

    G_j={|J_00-j|<=k/4, J_cross<=k/16}.

On F_j intersect G_j, (5.2) gives distance <=7k/16<k. By (3.2), Chebyshev and (4.1),

    P(|J_00-j|>k/4 | F_j)
       <=1792 M^(5/2)/(c k^3).                      (6.1)

For J_cross, its mean 2ck<=k/32, so J_cross>k/16 implies a deviation greater than k/32. The same variance bound and j>=k give

    P(J_cross>k/16 | F_j)
       <=229376 M^(5/2)/k^3.                        (6.2)

For clarity, the numerator before conditioning in (6.2) is at most 14336 Mx/(lambda k^2); division by P(F_j)>=j/(4M), then x=ck/M and j>=k, yields the stated constant. In (6.1) the factor y cancels exactly against the lower conditioning probability.

Since M^(5/2)/k^3=n^-2 and c=1/4096, the sum of these bounds is at most

    (1792/c+229376)/n^2 <=231/512 <1/2

for n>=4096. Therefore

    P_j(G_j | F_j)>=1/2.                            (6.3)

The choice k=M^(9/10) is not asserted sharp. The variance route explains the sufficient power condition k>>M^(5/6).

## 7. One full-word, source-independent, protected strict-k kernel

Define the map on every binary word. It is identity unless the input is x^(j) for some k<=j<=T0. On such an input:

1. Construct the public table Q_j above from M,k,j,c.
2. Sample a complete Q_j stationary word conditional on F_j (which has positive probability).
3. Form z=Can(X). Output z only if d_H(z,x^(j))<=k; otherwise output the original input.

The actual unknown source is not an input. The family Q_j is a public auxiliary construction, not an oracle read of the null's parameter or a hidden clean history. The same stochastic map is defined for every source and every input. All its probabilities are finite rational numbers; conditional sampling can be specified by a finite table, with no efficient-sampling claim.

Every accepted output has the same initial11 and terminal00 pairs as the input, and the final two positions are protected. The explicit distance test ensures at most k edits on every realization; rejection is identity. Equation (6.3) proves acceptance probability at least one half on each attacked input.

Since T(Can(X))=T(X), a histogram-only estimator has exactly the same prediction distribution on the canonicalized output as on the corresponding clean sample. This is the only point where the restricted observation model is used. It would be false for an unrestricted full-history estimator.

## 8. Constrained-risk calculation and logarithmic separation

Under Q_*, each x^(j) has probability

    v=(r/2)(1-r)^M>=1/(8M),                         (8.1)

independent of j. These events are disjoint. On an accepted sample, the null target is r while the clean target on F_j is a_j. Since a_j>=delta>=2r and acceptance has mass at least 1/2,

    E[null loss after attack | x^(j)]
       >=a_j/4 - E[clean |A(T(X))(1)-a_j| | F_j]
       >=(c e k/4-4SM)/j.                          (8.2)

Only nonnegative rejected losses are discarded. Independent estimator randomness can be averaged throughout. Summing (8.2), using e>=1/2, nonnegativity, and the fact that v is the SAME for all j, gives

    R_* >= [ (c k/(64M)-S/2) sum_(j=k)^T0 1/j ]_+
         >= [ (c k/(64M)-S/2) log((T0+1)/k) ]_+.

When the common coefficient is negative the final right side is zero; when it is nonnegative the harmonic integral is valid in the displayed direction. This proves (BK1). The per-j clean error has been paid with its correct conditional factor M/j; the proof does not subtract one clean risk from unrelated models without weighting it.

If a supplied-beta histogram family attained C H_2 for all k, its clean guarantee at this SAME beta=1/M would give S<=C/sqrt(M). Here k/sqrt(M)=n^4 tends to infinity, so eventually the coefficient in (BK1) is at least c k/(128M). Meanwhile

    H_2(M,k,1/M)<=2k/M,
    log((T0+1)/k)~log(n/8)->infinity.

Thus the ratio of the actual corrupted risk to H_2 diverges, contradicting a finite uniform C. All sources in both clean and corrupted comparisons have stationary initialization and the same advertised beta.

## 9. Scope and successor question

This proves, if accepted, that any successful supplied-beta, all-budget adaptive procedure must exploit information not contained in the exact triple histogram plus initial/final pairs. In particular, merely projecting empirical transition counts onto the advertised source class cannot solve the problem. This does not show that full-history ordering suffices; its use by an adaptive estimator remains to be established or obstructed.

The strict-budget kernel uses full word rearrangement only as an analytical canonicalization of an auxiliary clean sample, then performs a checked Hamming edit of the observed null word. No unrestricted permutation operation is granted to the adversary without being charged. The original target, terminal pair, common parameter-independent map and conditioning costs remain explicit. No quantized encoder, causal attacker, revealed mask/seed, efficient computation, neural architecture, external novelty or formal-verification claim is made.
