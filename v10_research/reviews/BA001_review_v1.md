# BA001 independent hostile mathematical review v1

Date: 2026-11-02. Reviewer: independent LLM reviewer [routing identity omitted].

## Verdict and binding

**PASS within the exact stated family; no blocking mathematical defect found.** Reviewed frozen manuscript SHA256 `fb589a775220737124a42e96a115eb3471ccbb84933edc2fd488e0d5986f1569`, including its independent IID §8, not merely its synthesis. This recommendation is an independent LLM audit, not formal verification, external peer review, novelty certification, or original emitted-network execution. Root acceptance remains the root's decision.

The accepted scope is one dense M-key, trailing-r-local weighted-ratio summary bank, D **scalar** coordinates, weights in [a,b] with a>0, values in [-1,1], fixed downward Q-grid quantization, and exact first/last-r boundary side information. Arbitrary source-independent position/K/M/Q/beta-dependent real tables and unlimited real randomized decoding are covered. Repeated weights/shared denominators are allowed. There is no general deep-Transformer lower bound here, no automatically matching upper, and no independently verified original-SRC inclusion in this review.

I read the actual BA001 manuscript, scalar-coordinate note, source manifest, handoff and author diagnostic code, and relevant complete IP002 and SM002 manuscripts and their acceptance records. Their statements are used for provenance comparison, not as permission to generalize a fixed-prefix theorem. BA001 supplies its family proof explicitly.

## 1. Source and stationary rare-suffix experiment

The symbol witness is legal for beta=0, beta=1/16 and the beta0=1/M transition. With alpha=1/(2M) and eta=beta0-alpha, eta>0 and eta<1/16. The stated pi is stationary, and every row—including unused source symbols—satisfies T(x,y)>=beta0 pi(y). Multiplying by T(x,y) in the two-step pair expression proves all-state minorization even for unsupported initial pairs and zero-mass targets. Starting at Pi is genuine stationary initialization, not a disguised deterministic WW start.

For E_j, the exponent M-j counts the WW transitions after the stationary initial pair and before entry. The initial factor Pi(W,W), entry mass, and no-exit mass are all p-independent after summing active words. Thus the conditional j bits are IID Bernoulli(p), and one uniform prior remains uniform on every E_j. The event probability lower follows from Pi(WW)>=1/4, alpha=1/(2M), the waiting factor >=1/2 and survival >=3/4; the result 3/(64M) is stronger than 1/(32M). The E_j are disjoint. Retaining eta in the next-symbol target is necessary and correctly done; past survival cannot remove the next exit probability.

The cutoff U has both arguments >=4 when M>=64, Q<=M/4, beta<=1/16. Consequently J>=4, J>=U/2, J<=M/4, beta0 J<=1/4 and Q sqrt(J)/M<=1/2. No dyadic/integer-Q assumption is used.

## 2. Query freezing and arbitrary positional tables

The attack that changing one bit changes the exact endpoint query, hence potentially every summand, does not invalidate this proof. It would invalidate bounded differences for the actual query-dependent bank. Instead the manuscript freezes each possible s first, proves bounds on the IID suffix experiment for that frozen query, and unions over all s. At the actual s the frozen bank equals the actual bank pathwise. It never asserts endpoint-conditioned IID.

There are at most H=3^(2r) s-values on this witness regardless of K. If r exceeds n or the first/last windows overlap, the duplicate consistency restriction only reduces their number. Even when S contains the full history, H is large enough to pay for it. Bounds remain mathematically valid but extraordinarily small; no fixed-family asymptotic inference should be extracted from a growing-r setting.

For fixed s, a changed coin appears in at most r displayed trailing windows. A weighted value is in [-b,b], and a weight is in [a,b], so 2br bounds each sum's change. Arbitrary real, nonuniform positional tables do not affect this argument. Efron–Stein yields variance <=2b^2r^2 j. With 2DH sums, Chebyshev gives failure <=4DH b^2r^2/T^2=1/10. It is harmless that many candidate queries are impossible, and no independence between the various sums is required.

## 3. Ratio comparison and differentiability

Both random and mean denominators are >=aM. The exact ratio subtraction is

`A/D - EA/ED = [(A-EA)-h(D-ED)]/D`, with `h=EA/ED` and |h|<=1.

It proves (4) without identifying E[A/D] with EA/ED. The product-Bernoulli expectation is a finite polynomial in p for each fixed table, even when the table contains arbitrary real constants. Differentiating by individual coin replacement gives derivatives <=2brj. Quotient differentiation then gives |h'|<=4brj/(aM). Thus the proposed curve is uniformly Lipschitz even if the position tables depend discontinuously or noncomputably on public M,Q,beta. No table-type count, monotonicity, finite precision assumption, or empirical-count reduction is needed.

## 4. Mesh, cell count and Bayes step

A mesh of length-1/2 interval with gap <=M/(LQj) exists with ceil(LQj/(2M))+1 <=2+LQj/(2M) points. The phrase 'choose a mesh' should be read as this constructed economical mesh, not as an assertion that every finer mesh has this size. This is not a mathematical gap.

The maximum-norm curve approximation contributes <=1/Q; fluctuation contributes at most a parameter-independent constant/Q; downward rounding contributes <1/Q, including at negative values and nonintegral Q. N=ceil(2C+4)+1 safely bounds the number of integers in each coordinate interval. A product of N^D counts the joint bank even when coordinates share denominators, because no independence is asserted. The union over meshes and s gives a fixed p-independent complete good-message set of cardinality <=A(1+Qj/M). Public metadata and exact real queries add no additional labels once s and public parameters are fixed.

The good-event lemma is valid for a parameter-dependent event and a noisy channel. For a fixed decoder seed, the union of radius ell/(8R) neighborhoods around its <=R good-message outputs occupies prior mass <=1/4. Good probability >=0.9 leaves >=0.65 joint probability outside these neighborhoods. The obtained 13ell/(160R) exceeds ell/(16R). Outputs need not lie in the prior interval. No posterior uniformity after G is required.

For a simplex output, TV dominates the error in its C1 mass, so dividing that coordinate by 1-eta gives the precise target p and loses at most a factor two. Combining the common prior, event probabilities and finite-message bound yields 1/(2048 AM) times the harmonic sum. The integral comparison supplies 1/(4u) ln(1+uJ); J>=U/2 supplies the stated log argument. Thus the constant 1/(8192A) is valid.

## 5. Full-history completion and the separate IID theorem

The IID pair source defines every row, including unsupported pairs, as Bernoulli(p), making P^2(s,t)=Pi(t). It works for all beta in [0,1]. For n=M+2 and delta=1/(16sqrt(n)), the KL upper <=1/8 and Pinsker TV<=1/4 are correct. Thresholding any real simplex estimate yields average error >=3delta/8, stronger than 1/(128sqrt(n)). Source-independent randomization does not improve that two-point limit.

For Q>M/4, the BA1 RHS is <=cM/(8Q^2)<2c/M, below this full-history lower. This does not import original-SRC c/Q and does not extend the narrow tube outside its valid range.

Section 8 separately proves BA2 for the enlarged family: now n independent coins produce variance <=2b^2r^2 n, curve derivative <=Ln/M<=2L, and Q<=sqrt(M) makes the scaled deviation <=2sqrt(2)T/a<C. The mesh requires <=2+LQ <=(2+2L)Q points; including S gives <=A_I Q labels and risk >=1/(32A_I Q), stronger than the claimed 1/(256A_I Q). When Q>sqrt(M), 1/(128sqrt(M+2))>=1/(256Q), so the full-history bound covers the remainder. The equality Q=sqrt(M) belongs to the first branch; no uncovered boundary exists. Different IID priors in different parameter regimes are allowed. BA1/BA2 combine by maximum, not by summing risks of unrelated witnesses.

## 6. Optimized and randomized encoders; scope boundaries

A fixed admissible encoder receives the same p-prior across j. All constants are uniform in its table contents. For an encoder with independent random seed, condition on that seed and grant it to the decoder: for each seed the **same** prior and constants give the lower, although its mesh/message set can depend on the seed. Integrating over the seed before taking the source supremum is valid. This establishes the claimed lower after optimization over admissible deterministic or randomized encoders; it does not silently choose a different worst source for each seed. Correlated encoder/decoder randomness can be absorbed into a common independent seed. As usual, expectations presuppose measurable randomized procedures.

The ratio form and source-independent-table contract are essential. Actual finite arithmetic must satisfy them exactly, not merely approximate an ideal attention map. Hard/query-selected masks, historical rereads, extra exact interior statistics, unbounded value ranges, and recursively nonlocal features are outside scope. D counts scalar outputs rather than physical heads. The scalar clarification accurately permits shared denominators. The generic IID proof would also work for K=2, but the common manuscript theorem scope K>=3 is conservative.

The two precision-threshold implications in §7 check out without importing BA2: monotonicity of log(1+cQ)/Q first rules out the lower-Q ranges; the remaining controlled ranges give logarithms of the asserted order; even larger Q already exceeds the necessary order. The implicit constants depend on fixed D,r,a,b and cannot be called architecture-universal or uniform under growth of those parameters.

## Independent diagnostics and limitations

`BA001_independent_checks_v1.py` was written independently of the author script. It passed **33,867 assertions**, including exact rational moment/derivative/influence computations on exhaustive five-bit suffixes with r=1,3,70 (M=64, n=66), all attainable boundary queries, negative values and shared denominators. It additionally checks all-state stationary pair minorization with an unused symbol, real nonintegral Q, cutoff endpoints, event and harmonic bounds, and high-Q comparisons. Observed maximal ratios to the theoretical bounds: variance 0.2, expectation derivative 0.2, ratio derivative about 0.033685, influence 0.9. Minimum event-probability ratio to the claimed bound was about 4.8427; minimum harmonic ratio about 2.5075.

These finite tests corroborate but cannot prove the arbitrary-table theorem. Universal validity is the analytic argument audited above. No source or frozen proof was modified. No original network execution, literature-priority search or formal proof assistant was used. No blocker or required correction remains from this review.
