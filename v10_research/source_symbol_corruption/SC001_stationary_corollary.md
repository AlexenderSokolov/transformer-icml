# SC001 stationary strengthening — separate author corollary

2026-11-02. POST-STAGE7, pending independent review. This does not alter the main theorem's arbitrary-start contract or assert a positive-beta frontier.

For the same full-corrupted-history experiment restricted to stationary initialization, K>=3, M>=2 and 1<=k<=M, the corruption-specific lower is

 R_cor,stat(K,M,k)>=Psi(k/M)/2048.                     (S1)

Use exactly the same common rounding kernel and uniform prior as SC001, but choose the recurrent first-order witness with a=e=1/M:

 T(W,W)=1-a, T(W,Ci)=a p_i,
 T(Ci,W)=e, T(Ci,Cj)=(1-e)p_j.

Set pi(W)=1/2, pi(Ci)=p_i/2 and unused-symbol rows equal pi. Direct substitution gives pi T=pi. Set theta_(u,v)(x)=T(v,x) and initialize at the stationary pair law Pi(u,v)=pi(u)T(u,v). The supported three-symbol chain is recurrent and aperiodic for M>=2 and p in [1/4,3/4]. D2(0) membership is automatic. No positive-beta frontier conclusion is inferred from this construction.

For E_j={W^(M+2-j), followed by j active symbols}, j=2,...,M,

 P_p(E_j)=Pi(W,W)(1-a)^(M-j)a(1-e)^(j-1)
         =(1-1/M)^M/(2M)>=1/(8M).                   (S2)

The probability is independent of both p and j. The final inequality follows because f(x)=x ln(1-1/x) has derivative ln(1-1/x)+1/(x-1)>=0 for x>=2 (use ln(1-t)>=-t/(1-t)); its value at x=2 gives (1-1/M)^M>=1/4.

Conditional on E_j, all j active symbols are IID Bernoulli(p). The stationary initialization's relevant factor Pi(W,W)=(1-a)/2 is p-independent; there is no concealed initial-law information on these events. At every possible protected terminal pair the true future law is

 e delta_W+(1-e)[(1-p)delta_C0+p delta_C1].            (S3)

In particular the future return probability e is retained, despite no past return in E_j. The same corruption kernel recognizes precisely these observed marker words, rounds the first j-2 active bits, preserves all markers and the final pair, and is identity on every other word, including paths with prior active segments or returns.

For any output q, TV(q,theta)>=|q(C1)-(1-e)p|. Apply the finite-message lemma to the scalar estimator q(C1)/(1-e), retaining all four protected terminal-bit labels. Since 1-e>=1/2, conditional Bayes risk is at least

 1/[64(1+(j-2)/(k+1))].

Multiply by (S2), sum the disjoint events, and use exactly SC001 (7)–(8). The coefficient before harmonic integral is now 1/(512M) rather than 1/(128M), proving (S1).

This is still a full-observation lower against a SINGLE source-independent kernel, and even grants knowledge of that kernel and family. Histories outside the events are not censored; their nonnegative risks are simply discarded. The protected terminal pair is delivered exactly and is fully counted in the message alphabet. Thus arbitrary-initialization transience is not essential to the logarithmic corruption obstruction.

At fixed K, a stationary IID two-point Bernoulli family gives the usual clean Omega(M^-1/2) lower under identity corruption; combined with (S1) and the already proved arbitrary-start upper, this also gives the same fixed-K order at stationary initialization. For an explicit elementary constant, use p_±=1/2±1/(16sqrt(M+2)). The KL between the (M+2)-symbol IID laws is <=32(M+2)/(256(M+2))=1/8, hence TV<=1/4 by Pinsker. Their one-step law distance is 1/(8sqrt(M+2)). The two-point absolute-error bound is distance*(1-TV)/4, at least 3/(128sqrt(M+2)). (The conservative factor 1/4 follows by nearest-target testing and triangle inequality.) Constants are not K-sharp.
