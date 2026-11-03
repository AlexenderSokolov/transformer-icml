# FOC001: Markov order and full-history joint adaptation

Root-authored interface corollary, pending independent review. This does not replace either accepted proof or manuscript.

## A common experiment and comparison profile

Use the original word length M+2, M>=64, final pair protected, strict budget k on the first M coordinates, 0<=k<=M. The predictor receives the FULL corrupted word and neither k nor beta. The target is unconditional unsquared TV at the actual protected final pair. For first-order sources the next-symbol distribution depends only on its last symbol, so the first-order and pair-state targets agree exactly.

For sources possessing a stationary pair law Pi and all-state certificate P²(u,v)>=beta Pi(v), beta in[0,1], retain the established profile

H2(M,k,beta)=min(1,max(M^-1/2,F2)),
F2=0 at k=0,
F2=(k/M)[1+ln(1+1/(k max(sqrt(beta),1/M)))] at k>=1.

This is the same comparison family used by the accepted joint-blindness theorem. It is not a new claim that H2 is an exact source-specific minimax risk. A uniform guarantee quantifies over every qualifying source and supplied-certificate value, while the predictor is not given that value.

## Candidate order comparison

1. If the source is known to be binary FIRST-order, a single predictor ignorant of k and beta has all-start risk <=2^21 H2 simultaneously for all M,k,beta and all such qualifying tables. It may use the full word, or the natural four pair counts, actual last symbol and one exact half-visit gate bit computed from that word.
2. For binary SECOND-order sources, no such jointly blind family exists with any finite universal constant, even with full corrupted history, unlimited computation and stationary initialization.

Thus Markov order affects this joint-adaptation question independently of the boundary-window restriction. This is not an unknown-order learning claim or a result for a predictor supplied beta.

## Positive derivation with the horizon shift paid

Apply the accepted FOU001 exact half-gate bound to N=M+1 ordinary transitions on the very same M+2 raw symbols:

R<=min(1,1024/sqrt(N)+2^20 k/N).

That theorem permits every first-order table and arbitrary starts, with no certificate assumption and no k/beta input. It permits edits to the first N symbols while protecting only the last. Every original legal attack is a subset of that class: it additionally protects the penultimate symbol and edits only the first M<N coordinates. Hence the bound applies unchanged. The full word permits computing the four ordinary pair counts and the half count on indices0,...,floor(N/2)-1; no inaccessible information is being supplied.

For g_M=max(M^-1/2,k/M), N=M+1 gives 1/sqrt(N)<=1/sqrt(M) and k/N<=k/M. Therefore

R<=(1024+2^20)g_M<=2^21 g_M.

For k>=1, F2>=k/M; for k=0 it is defined as zero. Because g_M<=1 on the exact budget domain, the cap in H2 preserves g_M<=H2 for every beta. Thus R<=2^21H2. The estimator's ordinary first-order flip orientation is merely another representation of its next-symbol distribution; binary TV at the last symbol equals TV at the actual pair for a first-order table.

No all-state certificate is used to construct the predictor. Reducible/periodic sources are covered by FOU001; this remains true for those with only beta=0. At positive beta, restrict the source class as usual without changing the map.

## Negative derivation and exact non-transfer boundary

Use accepted AB001, binary_budget_adaptation/AB001_joint_blindness_obstruction.md and its root receipt intake/AB001_acceptance.json. Root has reread the full proof and its complete independent review. It explicitly gives a stationary second-order clean family Q_a in the beta=0 class and a first-order null with beta=1/M, under one common strict source-independent protected-pair kernel. Its full-history constrained-risk inequality contradicts a constant H2 guarantee for the SAME k,beta-blind map by selecting k=floor(M^(3/4)). Its estimator may randomize and use the entire corrupted word.

The clean alternatives are not generally first order: they have theta00(1)=theta10(1)=a, but theta01(1)=r(1-a)/a differs from theta11(1)=1-r. This matters. Their use does not contradict the first-order positive theorem. Nor does AB001 refute beta-informed estimators: its clean and attacked cases use different certificate values and need not share a positive certificate.

## Scientific use and limitations

This corollary distinguishes two sources of difficulty:

- At fixed critical supplied certificate, restricted local counts may lose unknown-budget adaptation even for first-order dynamics; positional gates address that observation limitation.
- With full history but both k and beta hidden, the first-order class still permits universal adaptation, while the larger second-order class does not.

It does not establish a phase diagram for every beta, arbitrary alphabet, source-order estimation, a noisy-bit implementation, a neural advantage, or novelty. The negative proof is an already accepted theorem; the only new work here is the common-experiment/horizon/normalization interface check. Independent review of that interface remains required before acceptance.
