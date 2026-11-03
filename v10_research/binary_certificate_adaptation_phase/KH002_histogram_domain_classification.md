# KH002 — Exact certificate-domain criterion for histogram budget adaptation (candidate)

2026-11-02. New author candidate, conditional on accepted KH001; fresh full independent review and root acceptance required. No accepted proof is modified. Observation means **exact triple histogram plus initial/final PAIRS**, not full history or larger boundary windows.

## 1. Experiment and exact statement

Use the binary protected-terminal-pair source-corruption experiment and known-k benchmark H_2 from SC003/BT002. The predictor knows M and the supplied valid all-state certificate beta, not the actual edit budget k. It sees the triple histogram and initial/final pairs, may randomize, and has no computational restriction. Loss is unconditional TV at the true protected terminal pair. Corruption is by a source-independent offline stochastic kernel with a strict pointwise budget. All integers 0<=k<=M are included.

Let E be ANY public subset of (M,beta), integer M>=64, beta in [0,1]. An adaptive family on E means one finite constant C and maps A_(M,beta), independent of actual k, whose worst risk is at most C H_2(M,k,beta) at every pair in E and every k. The maps and constant may depend on E. Empty domains are vacuous.

Define

    G(M,0)=0,
    G(M,beta)=min{M^2 beta, 1/[beta sqrt(M)]} (beta>0).

**Domain classification.** Such a histogram-plus-pairs family exists if and only if

    sup_((M,beta) in E) G(M,beta)<infinity.          (KH2)

When (KH2) holds, one ordinary-add-one rule, independent even of beta and E, suffices for every initial law. When it fails, stationary sources already rule out the guarantee. The equivalence therefore holds for either stationary-only or all-initial-laws guarantees.

Equivalently, E must lie in a fixed union of beta<=B/M^2 and beta>=1/[B sqrt(M)], for some finite B>=1. This includes oscillating or sparse public domains. It is relative to the beta-dependent known-k benchmark, not a claim that weaker mixing intrinsically makes estimation easier.

## 2. Sufficiency from accepted KA001

If G<=B on E, B>=1, then each beta>0 obeys M^2 beta<=B or 1/[beta sqrt(M)]<=B. At beta=0 the weak branch holds. Accepted KA001 proves that the SAME ordinary-add-one predictor attains H_2 on the weak band with a constant depending only on B and on the strong band with a constant depending only on1/B. Take their maximum. The algorithm need not decide which band applies; it is identical in both results. Both bounds hold for arbitrary starts.

For example its constants permit

    C_E=max{2^16+96[1+(1/2)log B],
            2^16+2^12+2^12 B}.

The cap in H_2 is already included. Only KA001's positive bands, not its lower, are used here.

## 3. Finite nesting lemma: the actual public beta stays fixed

Fix actual beta in (0,1/16]. Put

    beta_w=max{beta,1/M}, delta_w=sqrt(beta_w),
    T=floor(1/[8 beta_w]), c=2^-12.

Suppose integer k meets KH001's conditions at beta_w:

    32<=k<=T, k^2>=4M, k delta_w>=6/c,
    delta_w^5 k^3>=2^20, delta_w^3 k^2>=2^21.       (3.1)

Take its exact clean family, asymmetric null and strict kernel, built at beta_w. Fix the ACTUAL estimator map A=A_(M,beta). All these sources satisfy beta_w>=beta, hence belong to D_2(beta). KH001's universal finite inequality applied to this fixed map gives

    R_actual_beta >=[(c k/(64M)-S)log((T+1)/k)]_+,  (3.2)

where S is the same map's supremum clean risk over that family, evaluated with the same actual public beta.

This does NOT change the predictor's metadata or assume any guarantee at beta_w. KH001 is universal over maps on the statistic; it does not inspect their labels. The clean guarantee used below is at actual beta and is licensed by source-class inclusion.

The source laws also do not change when relabeling their valid lower certificate. In particular the asymmetric null's true symbol1 target at00 is **beta_w**, not beta. Its clean comparison gap and full-word probabilities remain those of KH001. Only the benchmark and public predictor input are evaluated at actual beta. A supplied certificate need not equal a transition probability or maximal coefficient.

The adversary is the KH001 map with its auxiliary table hardcoded at beta_w for this fixed public problem. It is common across the clean/null family, preserves the endpoint, and checks every output's Hamming distance. It has no hidden source-table, stationary-law, unseen-clean-interior or estimator-seed input. We do not require one attacker simultaneously uniform over all beta. General real probabilities are permitted by the unrestricted finite stochastic-kernel model.

If also k sqrt(beta)>=1, then sqrt(beta)>=1/k>=1/M, so the binary cutoff is sqrt(beta). Since log(1+u)<=u and k>=2sqrt(M),

    F_2<=k/M+1/[M sqrt(beta)]<=2k/M,
    H_2(M,k,beta)<=2k/M.                            (3.3)

This finite nesting lemma is the sole extension of KH001 needed.

## 4. Every intermediate sequence is obstructed

Consider any sequence with M->infinity and

    M^2 beta->infinity, beta sqrt(M)->0.            (4.1)

It may be irregular and cross1/M repeatedly; beta is positive eventually. Define

    beta_w=max{beta,1/M}, U=1/beta_w,
    L=max{sqrt(M),beta_w^(-5/6),beta^(-1/2)},
    k=floor(sqrt(U L)).                             (4.2)

The three terms of L/U are beta_w sqrt(M), beta_w^(1/6), beta_w/sqrt(beta). They all tend to zero: the first is max{beta sqrt(M),1/sqrt(M)}; beta_w->0 gives the second; the third is

    max{sqrt(beta),1/[M sqrt(beta)]}->0

by (4.1). Hence L/U->0, while U,L->infinity. Integer floors do not affect

    k/U->0, k/L->infinity.                         (4.3)

Thus k/sqrt(M)->infinity, k sqrt(beta)->infinity, and

    delta_w^5 k^3=(k beta_w^(5/6))^3->infinity,
    delta_w^3 k^2=(k beta_w^(5/6))^2 beta_w^(-1/6)->infinity.

Since beta_w>=1/M, k delta_w>=k/sqrt(M)->infinity. Eventually beta_w<=1/16, T/U->1/8, k/T->0. All (3.1), plus k sqrt(beta)>=1, hold eventually. These are legal integer budgets <=M, and

    log((T+1)/k)->infinity.                         (4.4)

If an adaptive family has one finite constant C on this sequence, its k=0 guarantee at the SAME actual beta gives S<=C/sqrt(M). The ratio of this to c k/(64M) is at most (64C/c)sqrt(M)/k->0. Therefore (3.2) eventually gives

    R_actual_beta >=[c k/(128M)]log((T+1)/k).

By (3.3), its ratio to the actual-beta benchmark is at least (c/256)log((T+1)/k), diverging. This contradicts any finite C. Stationary witnesses suffice. This is simultaneous clean-and-all-budget nonadaptivity, not pointwise failure at every separate k.

## 5. Necessity and arbitrary domains

If sup_E G is infinite, select (M_n,beta_n) in E with G>=n. Then beta_n>0, M_n^2 beta_n>=n and beta_n sqrt(M_n)<=1/n. Also M_n->infinity: G<=M_n^2 because beta<=1. Bounded horizons cannot have unbounded G. This sequence satisfies (4.1), so §4 contradicts any one-constant guarantee on E.

No monotonicity or regularity of E, beta_n or the predictor maps is used. On a prescribed curve, boundedness of G is the exact criterion; an unbounded subsequence already rules out adaptation. Finite exceptional horizons cause no additional issue. Alternation between the weak and strong bands can remain adaptive; a subsequence entering the intervening region with both ratios diverging suffices to fail.

For beta=M^-gamma, gamma>=0, the criterion yields adaptation at gamma<=1/2 or gamma>=2 and nonadaptation at1/2<gamma<2. In particular beta of order1/M is negative for this exact histogram interface, not thereby for full history.

## 6. Dependencies and scope

KH001 supplies the finite histogram constrained-risk inequality, asymmetric full-word null, all-state certificate, reversed concentration and strict canonicalization. Its independent review and root acceptance must be completed and bound before promoting this candidate. KA001's accepted positive bands give sufficiency. SC003/BT002 give the benchmark. The universal-map nesting discussion in KA001/BK002 is consistent with §3, but their full-history lower is not needed here.

This classifies only the stated observation interface and public certificate domains. It does not establish full-history adaptation in the remaining critical/stronger-side gap, a robust-sufficiency theorem, richer-boundary adaptation, causal/efficient attacks, visible masks, edited targets, neural/training consequences, external novelty, formal verification or external peer review.
