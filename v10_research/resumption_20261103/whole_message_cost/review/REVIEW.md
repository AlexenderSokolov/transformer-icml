# Independent audit: entire prediction-message communication cost

Reviewer: `independent LLM reviewer`; local, unpublished. **PASS for the byte-bound actual `CANDIDATE.md`.** Read the full actual candidate after the independent derivation; no blocking discrepancy remains. This is a new no-free-information model, not a correction of the one supplemental gate-bit result.

## Independent analytic derivation

### Interface and payload

The accepted FOT002 interface discards X0, then applies FOU001 to X1,...,X(M+1), exactly M homogeneous first-order transitions. This removal is essential with arbitrary initial PAIR laws. Conditional on clean X0=b, prepend that fixed b to define the full attack and retain its suffix. That induced kernel is law-independent, edits at most k suffix symbols, and protects the terminal symbol (indeed the last two). The same predictor is used for every b, so averaging is legitimate without communicating b.

Read full current FOT002 and FOU001 candidate proofs, their root receipts, and the complete independent FOU upper review. Both candidates' hashes match their root receipts. FOU's exact gate estimate has risk at most 1024/sqrt(M)+2^20 k/M for all permitted starts, tables, and strict kernels. This review takes that accepted theorem as an imported lemma; it does not purport to independently re-prove all earlier generic stochastic lemmas.

A full-word scan computes both rows' total departures J, flips C, and first-half departures H on suffix indices 1,...,M, with H using indices 1,...,floor(M/2). Retain both rows until the terminal symbol u arrives; then select u. Sending u, J_u, C_u and 1{512H_u>=J_u} needs B=2ceil(log2(M+1))+2 bits. The receiver separately tests J>0, predicts flip C/J only if the gate is on, and converts to symbol-1 probability as q if u=0 and 1-q if u=1. The terminal bit is charged, not provided freely. Each invalid payload must map to a valid distribution, for example Bernoulli(0), to preserve loss at most one. No initial symbol, count, denominator, selected row, or gate is received for free.

### Coding upper

Write h=sum_y sqrt(W(y|0)W(y|1)). Normalization and Cauchy-Schwarz give h<=1, with equality iff the channel rows coincide. For 0<h<1, let d=ceil(R/4). A greedy maximal distance-d binary code deletes at most V=sum_{j=0}^{d-1} binom(R,j) strings at each insertion, hence has at least 2^R/V words. Since d-1<R/4, V<=2^{R H2(1/4)}. For completeness the entropy bound follows by weighting each summand by p^j(1-p)^(R-j), p=1/4: for j<=pR the weight is at least p^(pR)(1-p)^((1-p)R)=2^{-RH2(p)}, and the full binomial probability is one. Thus R(1-H2(1/4))>=B guarantees at least 2^B codewords, with no rounding gap.

For each pair x,x', the probability under x that the competing likelihood is at least the true likelihood is at most sum_y sqrt(P_x(y)P_x'(y))=h^{dist(x,x')}; zero likelihoods cause no issue. ML ties are included by the weak inequality, so any fixed tie-breaking rule works. Union bounding over 2^B-1 competitors gives maximal (not merely average) error at most (2^B-1)h^{R/4}. Therefore the proposed ceiling of the maximum of the GV length and 4(B ln2+0.5 ln M)/(-ln h) ensures error at most M^-1/2.

The error bound is uniform conditional on every full corrupted word and its payload because channel randomness is fresh after the attack. Correct decoding gives the exact gate predictor; incorrect decoding can increase TV by at most one. Hence risk <=(1024+1)/sqrt(M)+2^20 k/M <=(1024+2^20+1)g_M(k). The same encoder/decoder is used for every unknown k. For h=0, row supports are disjoint and each raw channel input bit is recovered perfectly, so R=B suffices. None of these arguments assumes the receiver knows the terminal state separately.

### Cardinality lower, including randomized protocols

Use stationary IID Bernoulli(p), p uniform on [1/4,3/4], and identity corruption k=0. The source belongs to the first-order class and to the optional beta=1/M pair-certificate subclass because P^2=Pi. The actual-terminal next-symbol probability is p at either terminal state, so loss is precisely |prediction-p|, not a surrogate transition parameter.

There are D=2^R possible fixed binary input strings. Realize the complete channel as a random function of that string, by pre-drawing one independent channel-output realization for every input string. Freeze that function and the decoder's random seed; also freeze any common seed independent of the law. There are then at most D real predictions. The encoder can still select a distribution of labels using the observed sample and private randomness; nothing requires its label to be deterministic. Regardless of that selection, an error smaller than v requires p to lie within v of one of those D predictions. The uniform prior assigns the union mass at most 2Dv/(1/2)=4Dv. Integrating the complementary probability from 0 to 1/(4D) gives Bayes absolute risk at least 1/(8D). Averaging the frozen law-independent seeds retains this lower bound. An output alphabet larger than two is irrelevant: after freezing its channel map, the bottleneck remains D input labels.

Consequently a single protocol with uniform risk <=C g_M(k) must satisfy 2^R>=sqrt(M)/(8C), i.e. R>=0.5log2M-log2(8C). This is a lower for every finite fixed C; the upper establishes existence of one universal C, not attainability of every prescribed smaller C. This proves order log M for fixed informative W in the constant-factor regime, not matching leading constants.

### Uninformative channel

If the rows coincide, W^R has the same output law for every input string. With no side channels and law-independent shared randomness, the receiver observation is independent of p. A random prediction independent of a uniform p in [1/4,3/4] has Bayes absolute risk at least the median risk 1/8. Thus for every R there is a source with risk at least 1/8, and a uniform C g_M rate is impossible as M grows. Sending longer blocks does not repair a rank-one channel.

### Resources and scope

O(log M) bits describes the payload, the fixed channel-input block length for fixed W, and scan counters separately; it is not a logarithmic-memory claim for the entire coding pipeline. Keeping an explicit 2^B-word codebook costs O(2^B R)=O_W(M^2 log M) bits, and brute-force greedy construction can cost O(2^R 2^B R) bit comparisons. Brute-force ML visits 2^B codewords. For fixed finite rational W, likelihood products can be compared by exact integer/rational arithmetic with polynomial bit complexity in R and the fixed channel description length. For arbitrary real W the mathematical existence theorem alone does not establish computable exact ML, computable length selection, or a finite exact representation of W. No neural efficiency, uniform efficient code construction, optimized leading constant, or novelty claim follows.

## Finite diagnostics

The executed `checks.py` (output `checks.json`) enumerates 8,184 binary words for M=1,...,10, checking suffix counts, selected-row payload roundtrips, and bounded predictions; checks GV ball entropy bounds through R=512; constructs maximal greedy codes through R=12; verifies 30 length/error choices over six horizons and five affinities; checks 502 exact-rational BSC pairwise likelihood-error cases through R=8; and verifies the optimal uniform-quantizer Bayes integral for D=1,...,100. All passed. Small M cases test interface identities, not the M>=64 stochastic risk theorem. These diagnostics supplement, not replace, the proofs.

No external publication, repository mutation, accepted-source edit, or licensing change was performed.

## Actual-candidate comparison and acceptance recommendation

Read the complete actual candidate, including its finite-code proof, randomized-kernel lower, identical-row argument, and resource ledger. All principal claims agree with the independent derivation above. The candidate explicitly excludes feedback, variable length, path-dependent free seeds and other ancillary observations; includes malformed-payload fallback; separates fixed-rational computational claims from arbitrary-real statistical existence; and states the correct quantifier over achievable constants. Its conservative rational-ML bound O(K R^3 log^2(Q_W+1)) covers sequential grade-school products. Its a_lower=1/8 certificate is correct since H2(1/4)=2−(3/4)log2(3)<7/8 iff 9>8. The optional FOT003 in-degree identity was read directly and verified by telescoping; it is not needed for direct scan encoding.

Recommend root acceptance of the informative-W total-length order and identical-row impossibility, with the new model and explicit resource limitations intact. This does not accept a pending supplemental-channel lower, any neural efficiency theorem, or publication. Final source/check/review hashes are recorded in `bindings.json`; any later candidate edits require re-review/rebinding.

### Final input-storage clarification

Read the actual `input_storage_clarification.diff` against the preserved before-file. The only change distinguishes O(log M) auxiliary scan memory from any resident M+2-bit input storage; it explicitly charges one pass of M+2 symbols. This is correct and improves the resource ledger without changing the theorem. Final accepted candidate SHA-256: `502b3a7e37c8adda33722ca324bade02efeab1c9d140c59abb3d812bba3eca62`.
