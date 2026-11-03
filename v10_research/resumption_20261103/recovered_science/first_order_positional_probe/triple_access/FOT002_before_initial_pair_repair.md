# FOT002: matched first-order result in the original richer observation

Root-authored interface candidate, pending independent check. The accepted FOT001 lower and FOU001 upper use different horizon conventions; this note matches them without dropping constants.

## Exact common model

Let M>=64, N=M+1. Observe X_0,...,X_(M+1), i.e. N+1 raw symbols. The source is known to be first-order binary, but its table and initial law are hidden. There are M triple departures (eight exact counts H_abc at indices0,...,M−1) and N ordinary pair edges. Supply actual first/last r raw symbols, integer2<=r<=M+2. Protect X_M and X_(M+1); strict offline source-independent kernels change at most integerk∈{0,...,M} of the first M coordinates. Prediction is at the actual terminal pair; for first-order tables this is exactly prediction at its last symbol. Loss is unconditional unsquared TV.

For one k-blind map, take its supremum risk/g_M(k), g_M=max(M^-1/2,k/M), then infimize over maps. Denote the resulting stationary/all-start factors by Lambda_stat(M,r), Lambda_all(M,r). The source class may be either (i) all first-order tables, or (ii) those satisfying the original all-state pair certificate beta=1/M. Lower witnesses obey(ii), upper covers(i).

## Candidate matched theorem

For ell=1+ln((M+2)/r), under either source-class convention,

2^-33 ell <= Lambda_stat(M,r) <= Lambda_all(M,r) <=2^17 ell.

Known-budget same-information risks obey

g_M(k)/96 <= Rstat(M,k) <= Rall(M,k) <=2^16 g_M(k).

Thus the logarithmic cost already occurs for first-order dynamics even after supplying all eight triple counts and protecting both final symbols. The certificate is not needed for the first-order upper; the lower respects it when it is imposed. This does not change the class for the existing second-order upper theorem, which still uses its certificate assumption.

## Proof of the upper and oracle upper

The original observation recovers all four ordinary pair counts exactly:

N_ab = sum_c H_abc + 1{(X_M,X_(M+1))=(a,b)}.

The last pair is known because r>=2. This adds the single omitted final ordinary edge; it does not add another triple departure. The last r raw symbols are already available. Therefore the FOU001 natural first-order suffix predictor can be evaluated on this observation with N=M+1, and its same-map bound holds for everyk≤M<N.

Original attacks protect two symbols, a subset of FOU001's attacks that protect only the final symbol. They also edit a subset of its first N potential coordinates. Thus the stronger FOU001 bound applies. Its suffix uses m=min(r−1,floor(N/2)), which is appropriate for ordinary single-state departures, not the older pair-departure r−2 count. The richer histogram reconstruction has supplied the correct ordinary row counts.

FOU001 gives R<=2^17[1+ln((N+1)/r)]g_N(k) and, for knownk, R<=2^16g_N(k). Since N=M+1 gives g_N(k)<=g_M(k), these prove the asserted uppers with no extra factor. They include arbitrary starts and all first-order boundary/periodic tables. TV targets agree as distributions of the next raw symbol.

## Proof of the lower and oracle floor

For each fixed map, accepted FOT001 gives sup R/g_N >=2^-32ell over legal budgets0..N−1 and stationary first-order sources satisfying beta=1/(N−1). These are exactly the original budget and certificate values after M=N−1. Pointwise,

g_N<=g_M<=[N/(N−1)]g_N,

so R/g_M >=[(N−1)/N]R/g_N. Taking the supremum and then infimum preserves the universal lower, giving at least[M/(M+1)]2^-32ell >=2^-33ell. No optimizer or worst-case attainment is required. The lower for the larger all-table class follows by inclusion.

For the known-budget floor use the actual elementary IID proof in the accepted original manuscript (lem:oracle-floor), not an arbitrarysecondorder lower. It uses only stationary IID binary sources and one source-independent kernel on the first M editable symbols, preserving the last TWO symbols and counting all four protected labels. Hence that proof is already within the first-order subclass and yields g_M/96 even with full history. IID pair kernels have P²=Pi on every row, so the certificate-restricted convention also admits them. Information restriction and arbitrary-start inclusion give the stated oracle floor.

## Direct consequences and limits

Prescribed raw widths have a uniform finite factor iff their normalized liminf is positive. Counts plus initial/final pairs (r=2) cost orderlogM. A full-word encoder may instead send FOU001's exact half-visit bit after corruption; the recovered ordinary pair counts and last symbol suffice to decode it, with risk<=1024/sqrt(N)+2^20k/N. A one-symbol alphabet leaves at most the r=2 baseline and cannot achieve a uniform constant. Thus the minimum fixed supplemental alphabet is two in this richer-count model too; scanning and exact counters are not charged as message bits, and the message is fault-free.

These are same-map adaptation factors, not a logarithmic risk penalty at each individual budget. Exact-oracle normalization changes constants according to the displayed sandwich. No neural, causal-attack, noisy-message, source-order-learning, leading-constant or novelty claim is made. No accepted manuscript has been edited by this interface candidate.
