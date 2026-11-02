# BAI004 — Square-root-beta occupation from a diagonal start to its successor crossing

2026-11-02. Author candidate v3, adding the opposite-crossing phase-convolution bound. Independent full/delta review required. v1, accepted BAI003, and delivered materials remain unchanged. This is a strong intermediate lemma, NOT the complete arbitrary-initialization theorem.

## 1. Main intermediate result

Use binary states W=00,A=01,B=10,C=11 and row parameters

    a=thetaW(1), b=thetaA(1), e=thetaB(0), t=thetaC(0).

Consider a full-support binary second-order source in D2(beta), with beta>=0. For positive beta full support forces a,b,e,t>0; the proof below treats positive values, and beta=0 uses the universal bound. Let M>=8, A0>0, and d0=max(sqrt(beta),1/M). Then

 E_W[1{Y_M=A} min(1,A0/(J_A+2))]
   <=min{1, (40A0/M)[1+ln(1+1/(d0 A0))]},             (BAI4.1)

where J_A=sum_(j=0)^(M-1)1{Y_j=A}. The symbol-swapped bound holds for initial C and terminal B, with the SAME constants. The cap can be replaced by any q<=1 by monotonicity; it need not be the true row exit probability.

Thus two genuinely arbitrary-start, actual-terminal unweighted occupation components have the same square-root-beta cutoff as the accepted stationary upper. In addition, section9 proves the initial-W/terminal-B and initial-C/terminal-A bounds with constant100 in place of40. Thus ALL crossing-terminal components from a diagonal initial state are controlled. Opposite-diagonal components remain open.

## 2. General initial-equals-target reciprocal identity

For ANY d-state homogeneous chain, any target s, and n>=1,

    E_s[1{Y_n=s}/J_s]<=d/n.                            (2.1)

On the event in question J_s>=1. Let F_s(z) be the pgf of the first positive return to s, allowing a defective law. In the state ordering s,rest,

 F_s(z)=zP_ss+z²P_s,rest(I-zP_rest)^(-1)P_rest,s.

Schur complementation gives

    1-F_s(z)=det(I-zP)/det(I-zP_rest).

All calculations are formal power series; both determinants have constant term one. Differentiating the determinant logarithm, expanding the formal inverse, and matching constant terms yields

 [z^n](-log(1-F_s(z)))
   =[tr(P^n)-tr(P_rest^n)]/n<=d/n.

The same coefficient equals sum_(k>=1)P_s(tau_k=n)/k, because -log(1-F)=sum F^k/k and the Markov property makes successive return lengths identically distributed and independent until a possibly infinite return. At the kth positive return J_s=k exactly: the initial visit is among earlier visits. This proves (2.1). Nonnegativity follows from the return expansion. Irreducibility, stationarity and aperiodicity are unnecessary.

## 3. A scalar consequence of the full all-state certificate

Write stationary masses y,x,x,w. Full-support stationarity gives ya=xe, wt=xb, and

    x=at/(et+2at+ab).

The actual two-step entries P²(B,A)=ea and P²(A,B)=bt imply

    ae>=beta x, bt>=beta x.

Also P²(W,C)=ab>=beta w=beta xb/t implies at>=beta x. This last deduction uses b>0, valid in the positive-beta full-support class. No off-support condition is discarded.

Define dimensionless variables

    alpha=Ma, E=Me, B=Mb, T=Mt,
    gamma=beta M², D=alpha B+2alpha T+ET.

The three certificate inequalities are exactly

    gamma<=D, gamma<=ED/T, gamma<=BD/alpha.             (3.1)

If gamma>=1, then

 min{1/e,(1+Mt)/b}<=12(1+Ma)/sqrt(beta).               (3.2)

### Proof of the scalar bridge

Set H=max{E,B/(1+T)} and X=(1+alpha)H.

* If T>=1, then B<=2HT, E<=H, and ED/T<=H(2alpha H+2alpha+H)<=3X²+2X.
* If T<1 and alpha>=1, then B<=2H, E<=H, and BD/alpha<=2H(3H+2)<=6X²+4X.
* If T<1 and alpha<1, then min(E/T,B/alpha)<=(E+B)/(alpha+T)<=3H/(alpha+T), while D<=2H(alpha+T)+2alpha T. Thus gamma<=6H²+6H alpha T/(alpha+T)<=6X²+3X, using alpha T/(alpha+T)<=1/2.

In every case gamma<=6X²+6X. If X>=1, gamma<=12X². If X<1, gamma<=12X, and gamma>=1 implies gamma>=sqrt(gamma). Both cases give X>=sqrt(gamma)/12. Finally

    min{1/e,(1+Mt)/b}=M/H
      <=12M(1+alpha)/sqrt(gamma),

which is (3.2).

## 4. Truncated active-excursion visit count

Consider a path starting A, stopped on its first hit of W, and count its A visits at times0,...,M before that hit. Call this number N. Then

    E N<=min{1/e,(1+Mt)/b}.                            (4.1)

For the first bound, between A visits the chain must reach B; any intermediate C holding period ends almost surely because t>0. At B it enters W with probability e. The COMPLETE number of A visits before W is therefore geometric(e), with mean1/e. Truncation lowers it.

For the second bound, extend each counted A visit by its outgoing transition, including the possible one at time M+1. The event that a given visit is counted is measurable before its outgoing transition, so the expected number of A→C entries from counted visits equals b E N. Before W is hit, the number of such C entries is at most one plus the number of C exits through time M. The latter expectation is at most Mt: the path starts A, so time0 cannot contribute a C exit, leaving at most M eligible times1,...,M. Hence b E N<=1+Mt. This argument covers the endpoint visit without an uncharged extra count.

Now run the full chain from A for M steps and let

    V=sum_(n=0)^M 1{Y_n=A}

be its TOTAL A visits, including both endpoints when applicable. There is one initial active excursion and at most Ma further W→A entrances in expectation. Strong Markov at each entrance, nonnegative truncated counts, and (4.1) give

    E_A V<=(1+Ma)min{1/e,(1+Mt)/b}.                    (4.2)

Indeed every excursion has remaining horizon at most M, and the bound (4.1) is uniform for that maximal horizon. For gamma>=1, (3.2) therefore yields

    E_A V<=12(1+Ma)²/sqrt(beta).                       (4.3)

## 5. Harmonic visit cost and the late initial hit

For N>=0 define

    Phi(N)=sum_(j=0)^(N-1) min(1,A0/(j+2)).

Integral comparison with min(1,A0/x), or a split at N=A0, gives

    Phi(N)<=A0[1+ln(1+N/A0)].                          (5.1)

This holds for all A0>0, including A0<1 and N=0. For N>A0 the comparison integral is A0[1+ln(N/A0)]; for N<=A0 the cost is at most N<=A0. Since logarithm is concave, Jensen's inequality gives

    E Phi(V)<=A0[1+ln(1+E V/A0)].                      (5.2)

Let f(n)=E_A[1{Y_n=A}min(1,A0/(J_A(n)+2))] with the same A0 at every horizon. Summing pathwise over n=0,...,M selects exactly the first V visits to A, indexed by their earlier counts j=0,...,V-1. Thus

    sum_(n=0)^M f(n)=E_A Phi(V).                        (5.3)

Starting W, the first hit of A is T_hit~geometric(a). There are no earlier A visits, so the required occupation expectation is exactly

    sum_(r=1)^M a(1-a)^(r-1) f(M-r).                   (5.4)

Split at r=floor(M/2). For the early part, n=M-r>=M/2; (2.1) gives f(n)<=4A0/n<=8A0/M. Its total contribution is at most8A0/M.

For the late part, r-1>=M/2-1>=M/4, since M>=8. Its point probability is therefore at most a exp(-aM/4). Equations(4.3),(5.2),(5.3) bound the late contribution by

 a exp(-aM/4) A0
   *[1+ln(1+12(1+Ma)²/(sqrt(beta) A0))].              (5.5)

Set x=Ma, s=sqrt(beta)A0 and G=1+ln(1+1/s). Since ln12<3,

 1+ln(1+12(1+x)²/s)
   <=G+ln12+2ln(1+x)<=4G+2x.

Also x exp(-x/4)<=2 and x² exp(-x/4)<=9. Thus (5.5) is at most

    (A0/M)(8G+18)<=(26A0/M)G.

Adding the early part proves a bound34A0G/M, and hence the stated constant40, when beta M²>=1.

If beta M²<1, use the accepted universal terminal-occupation lemma directly, even with the terminal-A indicator discarded:

 E min(1,A0/(J_(Y_M)+2))<=Psi(16A0/(M+1)).

Writing u=A0/M, one has Psi(16u)<=16u[1+ln(1+1/u)]: for16u>=1 use the cap; otherwise use the definition and discard the negative ln16 term. Here d0=1/M, so this is bounded by (BAI4.1). The endpoint beta M²=1 was already covered by the positive-beta argument. The unit probability cap completes the proof.

## 6. Crossing initial states reduce to diagonal initial states

This separate reduction may be useful after the remaining diagonal-start components are controlled. Let h=b+e-be, q=(a,b,e,t), and

    V_s=1{Y_M=s}min(q_s,A0/(J_s+2)).

Starting A or B, until the first diagonal hit the chain alternates A,B. In each two-step block it hits a diagonal with probability h, irrespective of which crossing state starts the block.

If h<=M^(-1/2), then for either crossing initial state

    E q_(Y_M)<=2(b+e)<=4/sqrt(M).                      (6.1)

Crossing endpoint contributions are at most b+e. For W endpoints, sum over the last B→W entrance: P(Y_M=W)<=e sum_(j>=0)(1-a)^j=e/a, so aP(Y_M=W)<=e. There is no initial W mass. Likewise tP(Y_M=C)<=b. Finally b+e<=2h. Thus (6.1) bounds E sum_s V_s independently of A0.

If h>M^(-1/2), let u=floor(M/2), and T_diag be the first diagonal hit. Then for M>=8,

    P(T_diag>u)<=(1-h)^floor(u/2)
                  <=exp(-sqrt(M)/8).                  (6.2)

On T_diag<=u the post-hit suffix has length n=M-T_diag>=ceil(M/2), starts at a diagonal, and has the same actual terminal query. Its prior terminal count is at most the full count. Strong Markov and count monotonicity give

 E_cross sum_s V_s
 <=exp(-sqrt(M)/8)
   +sup_{i in{W,C}, ceil(M/2)<=n<=M}
       E_i[sum_s 1{Y_n=s}min(q_s,A0/(J_s(n)+2))].      (6.3)

The first term is O(M^-1/2), by maximizing sqrt(M)exp(-sqrt(M)/8). This is an exact suffix/count reduction, not weighted marginal mixing.

## 7. What remains open

The complete arbitrary-start precision upper is NOT proved. Initial-equals-target contributions are controlled by section2. The initial-W/terminal-A and initial-C/terminal-B contributions now have the desired square-root-beta cutoff, even with unit clipping cap. Section6 reduces crossing initial states once uniform diagonal-start bounds are available.

Opposite-diagonal terminal queries still require proof. The opposite-crossing components are proved separately in section9. No rate for the opposite-diagonal terms or the full sum is inferred from these results. No global mixing improvement, stationary-mass lower bound, new runtime input, or new implementation is asserted.

## 8. Version and evidence notes

v1 recorded an e/b-cutoff excursion bound and the crossing-start reduction. v2 preserves v1 and proves the stronger square-root-beta cutoff using the root-derived scalar bridge, a checked truncated excursion-count identity, and Jensen applied to the GLOBAL cumulative count (not a reset-count surrogate). The cap is strengthened to one. The general Schur-return identity is independently proved here, rather than assumed accepted from a message.

The only inherited estimate in (BAI4.1) is the accepted universal finite-state terminal-occupation inequality, as recorded in SB001 v2. Every new scalar, count, hitting, and logarithmic comparison is proved explicitly above. A fresh independent reviewer, source bindings, and diagnostics are required before acceptance. No external publication or contact occurred.


## 9. Exact phase convolution controls the opposite crossing

For the same class and M>=8,

 E_W[1{Y_M=B}min(1,A0/(J_B+2))]
   <=min{1,(100A0/M)[1+ln(1+1/(d0 A0))]}.             (BAI4.2)

The swapped bound is initial C, terminal A. This is also a UNIT-cap bound; no minority/exit weight is needed.

### Exact count and phase identity

Starting W means the initial symbol is0. On terminal B=10, the telescoping pair-count identity gives

    J_A(M)-J_B(M)=1.

Indeed the difference of01 and10 occurrences among pair times0,...,M-1 is X_(M+1)-X_1, which is1 on that endpoint. Let k be the last A visit before terminal B. The A→B phase either takes one step, or goes A→C, stays in C, and exits to B. There are no intermediate A or B visits. Consequently

    J_A(M)=J_A(k)+1, and J_B(M)=J_A(k).

Let f_WA(k)=E_W[1{Y_k=A}min(1,A0/(J_A(k)+2))], with the same A0 at every horizon. The independent phase-length law, conditional on its starting A state, is

    U_C(1)=1-b,
    U_C(l)=bt(1-t)^(l-2), l>=2.

Every terminal-B path has exactly one such last-A decomposition. Therefore the desired expectation is EXACTLY

    g_WB(M)=sum_(k=0)^(M-1) f_WA(k) U_C(M-k).         (9.1)

This identity does not assume an independent query or condition a row-stack law on the endpoint.

### Early last-A contribution

Suppose first M>=16. For k>=M/2, one has k>=8, so (BAI4.1) applies at horizon k. Since max(sqrt(beta),1/k)>=d0,

    f_WA(k)<=(80A0/M)G,
    G=1+ln(1+1/(d0 A0)).

The phase probabilities sum to one, so this part of (9.1) contributes at most80A0G/M.

### Late C holding period

If k<M/2 then l=M-k>M/2. The one-step branch is absent, and l-2>=M/4 for M>=8. Hence

    U_C(l)<=bt exp(-tM/4).

For a path started W let V_A be its total A visits at times0,...,M. Count each such visit's outgoing transition, extending the final one if necessary. Expected A→C entries equal b E V_A. The number of C entries through M+1 is at most one plus the number of C exits through M. Because time0 is W, the exit expectation is at most Mt. Thus the GLOBAL count bound is

    b E_W V_A<=1+Mt.                                  (9.2)

This bound does not reset at W returns and is valid even if there are many W excursions. The same pathwise visit-cost identity and Jensen argument as section5 now give

    sum_(k=0)^M f_WA(k)
      <=A0[1+ln(1+(1+Mt)/(b A0))].                    (9.3)

Set x=Mt. Since beta<=1 and M>=8, d0<=1 and G>=1+ln(1+1/A0). Consequently

 1+ln(1+(1+x)/(b A0))
   <=G+ln(1+x)+ln(1/b),

where b<=1 and x>=0. Multiplying (9.3) by the phase-density bound yields a late contribution at most

 (A0/M)b x exp(-x/4)[G+ln(1+x)+ln(1/b)].

Use b<=1, x exp(-x/4)<=2, x² exp(-x/4)<=9, ln(1+x)<=x, and b ln(1/b)<=1/Euler_e. This is at most

    (A0/M)[2G+9+2/Euler_e] <= (12A0/M)G.

Adding early and late parts gives92A0G/M, covered by100. For8<=M<16, simply use min(1,A0/(J_B+2))<=A0/2<=100A0/M; this explicitly avoids applying (BAI4.1) below its minimum horizon. The unit cap and symbol symmetry finish (BAI4.2).

## 10. v2-to-v3 change and remaining scope

v2 is preserved. v3 adds the exact last-A phase convolution, the global C-entry count bound, and (BAI4.2). Sections1 and7 are updated to state that all crossing-terminal contributions from diagonal starts are now controlled. No earlier constant or proof is changed. Opposite-diagonal targets remain the only unproved diagonal-start occupation components. Independent review of the NEW section9 is required; approval of v2 alone is insufficient for v3.
