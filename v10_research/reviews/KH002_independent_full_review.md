# KH002 — fresh independent full mathematical review

**Verdict: no substantive mathematical defect found in the frozen candidate.** The exact arbitrary-public-domain criterion is supported for the **exact triple histogram plus initial/final pairs**. It holds both for stationary-only and arbitrary-initial-law guarantees. The negative direction is not a full-history or richer-boundary-window classification. Root acceptance is a separate decision.

This is independent LLM mathematical corroboration, not formal verification, external peer review, or an external novelty assessment. No author proof or accepted source was changed by this reviewer.

Reviewed candidate: `binary_certificate_adaptation_phase/KH002_histogram_domain_classification.md`.

SHA256: `970bfefb6041cdb989148819eb526c789d86591992375b84b05de2dd72bf9702`.

Date: 2026-11-02 UTC. The author confirmed these bytes frozen during this audit. The independent snapshot `reviews/KH002_audit_snapshots/KH002_received.md` is byte-identical. No proof revision was requested or made. Later changed proof bytes are not covered by this verdict.

## 1. Complete reading, accepted dependencies, and exact experiment

I read the complete KH002 candidate and complete KH001 and KA001 proofs, their full independent reviews, and their current root acceptance receipts. I also read SC003's full proof/review, BT002's main and scalar proofs and full review, and BK001's full proof to inspect the observation and canonicalization interfaces. Their current accepted proof hashes and, where receipt-specified, review hashes were checked. The separate KH001 review bindings were inspected as provenance. Candidate-era headings and pending-review wording in immutable proof files do not override the later exact acceptance receipts.

The word has N=M+2 bits and M overlapping departure triples. A homogeneous binary second-order source has a qualifying stationary pair law Pi satisfying P²(u,v)>=beta Pi(v) on **all** four starting and target pair states. Beta is a supplied valid lower certificate; it need not be the maximal such coefficient or equal a transition probability. The stationary-only version starts each source at its own stationary law; the arbitrary-start version allows every initial pair distribution.

The offline adversary sees the original whole word, has no unknown-source-table or qualifying-Pi input, and changes at most k of its first M positions on every outcome. The original final pair is protected. Loss is unconditional TV at that actual pair, which for a binary next-symbol law is absolute error of its symbol-1 probability. The attack seed and edit mask are not revealed.

The predictor sees precisely the eight exact overlapping-triple counts and the initial and final pairs. It knows M and the actual supplied beta, may know the entire public domain E, may randomize independently, and has unrestricted computation. It does not know the actual budget. The same map A_(M,beta) must satisfy all integer budgets 0,...,M at that public pair. The attacker is not histogram-restricted.

The known-k benchmark is

    s=M^(-1/2), e_beta=max(sqrt(beta),1/M),
    F2=(k/M)[1+log(1+1/(k e_beta))] for k>=1,
    F2=0 for k=0,
    H2=min(1,max(s,F2)).

SC003's known-k upper uses only the triple counts and final pair, although its statement allows the whole word. BT002's full-history lower also applies to predictors restricted to this statistic. Therefore H2 is the same known-k benchmark for this restricted experiment; KH002 is not importing a full-history upper that secretly requires ordering. SC003's historical missing-lower caveat was subsequently resolved by accepted BT002, not by KH002.

## 2. The domain condition and positive union use exactly one estimator

For beta>0, G<=B means

    M² beta<=B OR beta sqrt(M)>=1/B.

This is the elementary equivalence min(x,y)<=B iff x<=B or y<=B, with both terms positive. At beta=0 the separately defined G=0 agrees with the weak branch. If sup_E G is finite, choose one finite B>=1 dominating it. This gives a fixed weak/strong union containing E, even if E switches branches irregularly or contains multiple certificate values at one horizon. Conversely, containment in such a fixed union immediately bounds G by B.

Accepted KA001's two positive bounds concern the **same ordinary corrupted-terminal-row add-one predictor**. Its output at terminal pair u has coordinates (N'_(u,b)+1)/(J'_u+2). Neither its program nor its output depends on beta, the band constant, E, or the actual k. It is available from the stated histogram interface; even the initial pair is unnecessary for this upper.

For the weak branch use KA001 with band parameter C=B. Since B>=1, its D=max(1,sqrt(B)) is sqrt(B), giving

    2^16+96[1+(1/2)log B].

For the strong branch use its c=1/B, giving

    2^16+2^12+2^12 B.

Their maximum is exactly the candidate's permissible C_E. There is no need to select between two procedures, infer which branch holds, estimate beta, or know k. Both imported bounds include the unit cap and hold uniformly for arbitrary starts, all finite M>=64 and all budgets including zero. Only KA001's positive results are needed for this part; its full-history negative region is not being extrapolated.

## 3. Finite nesting keeps the actual predictor metadata fixed

Fix the actual beta in (0,1/16] and write beta_w=max(beta,1/M). Because M>=64, beta_w is in [1/M,1/16], exactly KH001's witness-certificate range. Use its source family and null at beta_w, its delta_w=sqrt(beta_w), and its T=floor(1/(8 beta_w)). The listed k conditions are precisely KH001's finite conditions, with no dropped constant or unlicensed extension to smaller beta_w.

Every witness satisfies P²>=beta_w Pi>=beta Pi, so it belongs to D2(beta). Now fix the actual map

    A=A_(M,beta).

KH001's finite constrained-risk inequality is universal over maps on the statistic. It may therefore be applied to this fixed map, regardless of the name assigned to its certificate argument. The clean supremum S and the attacked null risk both use this same actual A, supplied actual beta. No guarantee at A_(M,beta_w) is assumed or used. In particular this is not an exchange of distinct metadata values within one risk guarantee.

This yields exactly

    R_null,actual-beta >=[(c k/(64M)-S)log((T+1)/k)]_+,
    c=1/4096.

The k=0 adaptation guarantee at actual beta will later control S solely because of source-class inclusion. Clean alternatives may depend on the attacked k: the clean guarantee is uniform over the entire actual source class, and hence over every selected subfamily. The estimator map cannot change with that selection.

## 4. The null's true target is beta_w, not the supplied beta

KH001's null has symbol transition probabilities

    T_*(0,1)=beta_w, T_*(1,0)=r=1/(2M),
    pi_*(1)=beta_w/(beta_w+r).

Its actual next-symbol-1 target at terminal pair 00 is therefore **beta_w**. Retagging the valid certificate does not change its transition probabilities, stationary law, full-word law, target, or attack kernel. For the full null word 1^(M+2-j)0^j the exact probability remains

    v_j=pi_*(1)(1-r)^(M+1-j)r(1-beta_w)^(j-1).

These probabilities depend on j and retain the long-prefix factor. Their KH001 bounds 1/(8M)<=v_j<=1/(2M) and the clean target separation a_j>=2 beta_w remain unchanged. It would be invalid to substitute actual beta for beta_w in either the null target or these full-word probabilities. The candidate explicitly avoids that error.

For completeness, the null's pair-kernel ratios are

    P_*²((u,v),(s,t))/Pi_*(s,t)=T_*(v,s)/pi_*(s).

Their minimum is at least beta_w+r>=beta_w>=beta. Thus the nesting concerns the all-state certificate, not just entry into a supported row. The independent diagnostics separately check both witness-beta and actual-beta certificates and explicitly test 57 cases in which the target beta_w is strictly different from supplied beta.

## 5. The attacker remains legal and the observation restriction remains essential

For each fixed public (M,beta,k), the KH001 auxiliary tables can be constructed using beta_w and fixed in one finite stochastic map before source sampling. The map is common across the clean/null source family. Its runtime behavior depends on the observed full word and private randomness, not the unknown true transition table, hidden stationary law, unseen clean interior, or predictor seed. Different public beta values may have different fixed maps; the theorem does not require one beta-blind attacker across all experiments.

On a designated null word the map samples an auxiliary stationary clean word conditional on initial pair 11/final pair 00, canonicalizes that word, and outputs it only after checking its Hamming distance from the **actual observed null word** against k. Rejection is identity. Both endpoint pairs are preserved, so the actual terminal pair is protected and every edit is among the first M bits. The auxiliary canonicalization is not an uncharged permutation privilege.

General real beta_w can produce irrational auxiliary probabilities. A stochastic kernel on a finite set can have real probabilities under the unrestricted model. Neither rational implementation nor effective sampling is required or asserted. This would need re-examination under computational restrictions, which are outside the statement.

Canonicalization preserves exactly the triple histogram and both endpoint pairs. Therefore the actual predictor has the same input statistic on the sampled clean word and its canonicalization. Its independent randomization can be averaged without exposing its seed to the attacker. This equality need not hold for a full-history predictor or a predictor seeing longer boundary windows. The restriction cannot be removed from the lower theorem or its resulting classification.

## 6. Benchmark comparison is at actual beta

The extra condition k sqrt(beta)>=1 is essential when actual beta is below 1/M. It gives sqrt(beta)>=1/k>=1/M, since k<=T<=M/8<M. Therefore the binary cutoff e_beta equals sqrt(beta), not sqrt(beta_w). Applying log(1+u)<=u yields

    F2(M,k,beta)<=k/M+1/(M sqrt(beta))<=2k/M.

The second inequality uses k sqrt(beta)>=1. Separately k²>=4M implies s<=k/(2M), so taking max(s,F2) and then the cap gives

    H2(M,k,beta)<=2k/M.

Every quantity on the left is evaluated at the actual public certificate. The source construction is at beta_w, but the desired benchmark is not silently replaced by the potentially smaller H2(M,k,beta_w). The candidate's added beta^(-1/2) term in L is exactly what ensures this finite comparison below the witness floor.

## 7. The geometric budget works on every intermediate sequence

Consider any sequence of public pairs with M tending to infinity, M² beta tending to infinity, and beta sqrt(M) tending to zero. No monotonicity, power law, or unique beta at a repeated horizon is required. Beta is eventually positive. Define

    beta_w=max(beta,1/M), U=1/beta_w,
    L=max(sqrt(M),beta_w^(-5/6),beta^(-1/2)),
    k=floor(sqrt(U L)).

The exact three ratios making up L/U are

    beta_w sqrt(M)=max(beta sqrt(M),1/sqrt(M)),
    beta_w^(1/6),
    beta_w/sqrt(beta)=max(sqrt(beta),1/(M sqrt(beta))).

Each tends to zero. For the second, beta_w tends to zero. For the third, sqrt(beta) tends to zero and M sqrt(beta)=sqrt(M² beta) tends to infinity. Thus L/U tends to zero while U and L tend to infinity.

If x=sqrt(U L), then k/x tends to one because x tends to infinity and x-1<k<=x. Consequently

    k/U=(k/x)sqrt(L/U) ->0,
    k/L=(k/x)sqrt(U/L) ->infinity.

Floors do not require any uniform rate or regularity assumption. Because L dominates all three displayed scales,

    k/sqrt(M) ->infinity,
    k beta_w^(5/6) ->infinity,
    k sqrt(beta) ->infinity.

The KH001 concentration terms are exactly

    delta_w^5 k³=(k beta_w^(5/6))³ ->infinity,
    delta_w^3 k²=(k beta_w^(5/6))² beta_w^(-1/6) ->infinity.

Also k delta_w>=k/sqrt(M) tends to infinity. These implications prove every fixed finite lower threshold in (3.1) eventually, including 32, 4M, 6/c, 2^20, and 2^21. They also prove the actual-beta benchmark condition k sqrt(beta)>=1 eventually.

Since U tends to infinity, T/U=floor(U/8)/U tends to 1/8. Together with k/U tending to zero this gives k/T tending to zero, hence k<=T eventually and log((T+1)/k) tending to infinity. Since beta_w>=1/M, U<=M and T<=M/8; the selected k is a legal integer budget. No asymptotic budget outside the permitted horizon is used.

## 8. Clean-risk subtraction and the all-budget contradiction

Suppose one adaptive family with finite constant C works on this sequence. At k=0, F2=0 and H2=s, exactly. The same-map clean guarantee gives S<=C/sqrt(M) on the KH001 subfamily. Dividing by the positive coefficient in its finite lower yields

    S/[c k/(64M)] <=(64C/c)sqrt(M)/k ->0.

Thus eventually S<=c k/(128M), and the positive-part lower is at least

    [c k/(128M)]log((T+1)/k).

Divide by the **actual-beta** H2<=2k/M to obtain a risk/profile ratio at least

    (c/256)log((T+1)/k) ->infinity.

This contradicts that same finite C. Constants and the eventual horizon may depend on the whole chosen public domain or sequence; the divergence defeats each such fixed constant. The sequence does not have to provide a uniform quantitative rate over all possible domains.

Stationary nulls and stationary clean alternatives suffice, so the contradiction applies to stationary-only guarantees and therefore also to arbitrary-start guarantees. It requires simultaneous clean accuracy and robustness over all budgets; it does not assert pointwise failure at every separate positive k or a known-k lower stronger than the accepted benchmark.

## 9. Arbitrary domains, subsequences, and all edge cases

If sup_E G is infinite, choose a pair (M_n,beta_n) in E with G>=n. Then beta_n>0 and both defining terms of the minimum are at least n. Hence

    M_n² beta_n>=n,
    beta_n sqrt(M_n)<=1/n.

Also G<=M_n² beta_n<=M_n² because beta_n<=1. Therefore M_n>=sqrt(n), and in particular M_n tends to infinity. This proves all three assumptions of the preceding sequence argument. The sequence need not have increasing M at every index; repeated horizons cannot prevent the limit because the bound is valid at each index. Nor need E contain every horizon, have a graph representation, be closed, or satisfy any regularity.

An assumed guarantee at every pair in E would hold on this selected sequence with the **same** C and actual maps, so it is contradicted. This is the correct direction from unbounded supremum to an obstructed subsequence; it does not require G itself to diverge along every ordering of E.

Edge cases are correctly handled:

- **beta=0:** G is expressly defined as zero, and ordinary add-one is covered by KA001's weak band, including arbitrary starts. No reciprocal-beta formula is evaluated there.
- **Empty E:** the guarantee is vacuous and there exists a finite band union containing E. Equivalently the boundedness assertion has no counterexample; the usual extended-real empty supremum convention causes no problem.
- **Bounded horizons:** even if there are infinitely many beta values at these horizons, G<=M_max² is bounded. Independently, risk<=1 and H2>=M_max^(-1/2) permit a finite constant.
- **Finite exceptional horizons:** they can be absorbed into one finite B or risk constant. An exceptional bounded set of horizons cannot create an unbounded G.
- **Oscillating positive domains:** a domain may alternate between fixed weak and strong bands and remain adaptive, because the algorithm is identical on both.
- **Sparse or irregular negative domains:** one sequence with both ratios escaping is sufficient to preclude a uniform constant. The proof does not assume the domain has a limiting exponent.

For beta=M^(-gamma), gamma>=0, the two terms are M^(2-gamma) and M^(gamma-1/2). Their minimum remains bounded exactly for gamma<=1/2 or gamma>=2, giving the stated power-law corollary including both boundary exponents. Fixed multiplicative constants in valid certificates can be absorbed into the positive bands; beta=0 is separately covered. This nonmonotone adaptation pattern is relative to a beta-dependent benchmark, not evidence that weaker mixing intrinsically improves estimation.

## 10. Independent exact diagnostics, limitations, and disposition

I wrote `reviews/KH002_independent_exact_checks.py` without reading or importing the author's checker. The run passed **31,408 assertions**, all using exact integers or rational arithmetic. Integer root calculations are certified by checking both adjacent powers; no floating-point decision or Monte Carlo estimate is used.

The diagnostics include:

- 2,569 exact bounded-G/fixed-union equivalences, including weak and strong boundary equalities at square horizons, 350 beta-zero cases, and finite-horizon bounds;
- 108 complete geometric-budget cases with actual beta equal to or below beta_w, plus 15 slow-boundary/sparse/crossing cases, including every finite KH001 condition and the actual-beta benchmark conditions;
- 369 certified radical floors realizing k=floor(sqrt(U L)) through exact fourth and twelfth roots, with examples controlled by **each of the three** terms in L;
- 375 rational stationary clean witnesses with 6,000 all-state entries at beta_w and another 6,000 at actual beta;
- 75 asymmetric nulls with 1,200 all-state entries at each certificate, exact pair-kernel ratio identities, and 57 checks explicitly distinguishing true target beta_w from supplied beta;
- exact positive-part/clean-penalty/benchmark-ratio scalar implications, current accepted proof/component/review hashes as specified by their receipts, and unchanged candidate/snapshot/input hashes at the end of the run.

The finite instances corroborate their stated arithmetic only. They do not formally verify arbitrary real certificates, universal maps and source-independent kernels, asymptotic limits, or arbitrary-public-domain quantifiers; those are mathematical arguments reconstructed in Sections 2–9. The accepted analytic and canonicalization dependencies retain their own review scope.

No further correction is requested for the frozen candidate. The separate manifest binds this review, the independent checker/output and snapshot, the exact candidate, and accepted dependencies. Any root acceptance or summary should keep **histogram plus initial/final pairs only** prominent. This does not settle full-history adaptation in the remaining range, classify richer boundary windows, prove robust sufficiency of ordering, establish an efficient/causal attack, expose masks or seeds, edit the target, or support neural/training, publication, external novelty, or formal-verification claims.
