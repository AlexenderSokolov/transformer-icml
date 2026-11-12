# Independent general second-order statistical benchmark review

2026-11-12. Reviewed the complete draft text supplied by the author, including exact count indexing, filtration, estimator, source class, bounds and minimax comparison. Analytical review only; no independent numerical rerun or new-rate claim.

Verdict: PASS, no mandatory mathematical correction. N>=3 and n=N−2 counts exactly the observed transitions: Y_i=(X_i,X_(i+1)), i=1,...,N−2, with next labels X_(i+2). The actual terminal pair is (X_(N−1),X_N), which is not an additional departure count. It is selected from the same path; the proof correctly does not assume independence.

For each pair u, d_i=1{Y_i=u}(1{X_(i+2)=+1}−q_u) is measurable at F_(i+2), has conditional mean zero given F_(i+1), and is orthogonal to every earlier d_j, including the adjacent one. Thus M=A−qJ has second moment <=n pi_u/4 without conditioning on occupation counts or treating selected transitions as conditionally iid.

The unique two-step pair path has transition probability at least c². Stationarity yields pi_u>=c²; Doeblin minorization gives rho=1−4c² and the stated covariance bound. The geometric series is exactly 1+2sum_(k>=1)rho^floor(k/2)=1/c²−1, so VarJ<=n pi_u/c² is conservative and valid.

On J>=n pi_u/2, the smoothed estimator error is bounded by 2(|M|+1/2)/(n pi_u), giving 1/sqrt(n pi_u)+1/(n pi_u). Chebyshev bounds the complementary event by4/(n pi_u c²). Summing the four unconditional row errors safely dominates the terminal-selected error and yields the displayed U_n=4/(c sqrt(n))+4/(nc²)+16/(nc⁴). The row-independent fallback decision based only on known n,c correctly gives min(U_n,(1−2c)/2); unknown pi is used only in analysis.

For the spin subfamily, triple innovations are iid and endpoint multiplication preserves absolute parameter error pathwise. The clipped innovation mean, exact binomial risk expression and stated upper bound are correct. For h=min(a,1/(4sqrt(n))), the full-history KL is n h log((1+h)/(1−h))<=2/15. Pinsker and the common-mass Bayes argument give risk at least h/2(1−1/sqrt15)>=h/3. The same-history target difference is h; no independent test query is substituted. This supports the claimed spin minimax order and a lower bound for the larger class, not a new statistical rate.

The architectural comparison requires one common theta-independent endpoint template and separately charged approximation errors under both sources. It is invalid if the template is allowed to depend on theta. The draft states this restriction and does not conflate finite-sample statistical uncertainty with a constant label-noise floor.

Optional implementation clarification: O(N) running time uses the usual streaming word-RAM convention for O(log N)-bit counters; it is not an O(N) bit-operation statement or a neural/finite-execution-precision construction. Existing innovation/binomial benchmarks are acknowledged, so this should be published as consolidation with explicit constants rather than a new rate.
