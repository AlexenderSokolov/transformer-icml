# AB002 — Ordinary add-one fails; supplied-beta adaptation remains open

2026-11-02. Author candidate; fresh independent full review required.

## 1. Explicit stationary counterexample to ordinary add-one

Take the stationary symmetric first-order flip-r source from AB001, r=1/(2M). Its binary pair chain satisfies the all-state certificate beta=1/M. At terminal pair 00 the true probability of symbol 1 is r. Each one-flip word x^(t)=1^(M+1-t)0^(t+1), 1<=t<=M-1, has probability v=(r/2)(1-r)^M>=1/(8M).

For 1<=k<=(M-1)/4, define a deterministic kernel as follows. On x^(t) with 4k<=t<=M-1, enumerate its final zero run by offsets 0,...,t, and flip the k zeros at offsets 3j-1, j=1,...,k, to ones. Else output the input unchanged. This is a map on all words, independent of the source. The inserted ones are isolated with two zeros between them, and the last inserted one has offset 3k-1<=t-2, so the terminal two zeros remain protected. Exactly k legal positions are changed.

The original number of terminal-row 00 departures is t-1. Each isolated inserted one removes exactly two distinct 00 departures and creates one designated 001 triple. Therefore the corrupted counts are

    J'=t-1-2k, C'=k,

and ordinary selected-row add-one predicts

    qhat=(k+1)/(t+1-2k)>=k/(t+1).

Since r=1/(2M)<=k/[2(t+1)], its TV loss is at least k/[2(t+1)]. Summing the disjoint words gives the exact finite lower

    R_addone >= (k/(16M)) sum_(t=4k)^(M-1) 1/(t+1)
              >= (k/(16M)) log((M+1)/(4k+1)).         (AB2)

At k=floor(M^(3/4)), this is order (k/M)log(M/k), whereas the known-k binary minimax profile at beta=1/M is order k/M. Thus ordinary add-one does not attain the all-beta binary frontier, even under stationary initialization. This refutes that estimator, not every k-blind estimator. It remains a counterexample even if beta is supplied, because the ordinary add-one rule does not use it.

## 2. Honest failed route toward a supplied-beta obstruction

An initial tempting alternative used theta_00(1)=a, theta_01(1)=0, theta_10(0)=1-a, theta_11(0)≈1/M, with a long initial 11 wait followed by a zero-like active suffix. At beta=0 this is legitimate for arbitrary initialization, but it cannot satisfy a positive all-state certificate with positive stationary crossing mass: P^2(01,10)=b*t=0 while Pi_10>0. That candidate is not a same-beta adaptation obstruction.

The stationary Q_a family in AB001 repairs stationarity but deliberately uses beta=0 for its clean guarantee. Its two-step ratio at (01,10) is

    P_a^2(01,10)/Pi_a(10)=2r^2(1-a)/a^2.

To meet beta=1/M=2r this necessary condition requires a^2<=r(1-a), hence a=O(M^-1/2). The putative high-exit alternatives a≈k/t with k≫sqrt(M) are excluded. The obstruction is structural, not a missing constant.

## 3. Remaining problem, precisely

Open in this note: for each supplied beta, is there one estimator A_(M,beta), independent of k, that attains H_2(M,k,beta) simultaneously for all k, uniformly in beta, under stationary and/or arbitrary initialization?

A class-constrained full-history fit could in principle reject fake exit patterns through the certificate's cross-row constraints; ordinary row-wise add-one ignores them. No risk theorem for such a fit has been proved here. Guessing an edit budget, silently using clean counts, or transplanting AB001 across different advertised beta values would not answer the supplied-beta question.

Two immediate valid regimes: (i) beta=0 (indeed the weak range beta<=M^-2) admits the generic ordinary-add-one corruption upper of order min{1,M^-1/2+(k/M)[1+log(1+M/k)]}, so it is k-blind rate-optimal there; (ii) the class beta=1 is IID in its next-symbol law, and pooled symbol frequencies give a k-blind order max{M^-1/2,k/M} rule. These statements use accepted predecessor interfaces for (i) and the endpoint manuscript's beta=1 structure/pooling argument for (ii); they are not newly proved by this counterexample. No claim is made here for an unknown positive beta or an intermediate supplied beta.
