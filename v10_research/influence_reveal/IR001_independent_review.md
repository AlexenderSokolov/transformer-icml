# IR001 fresh independent mathematical/model review

2026-11-02. Reviewer: independent LLM reviewer, distinct from author. **PASS within the explicitly stated model.** This is an independent mathematical review, not root acceptance, formal verification, emitted-network certification, or novelty certification.

Reviewed theorem SHA-256: `963e3f743c474f3f4c29fcb2f4aa9dfe1283ac82e0821b18df6a99223b09fffe`.

## Scope read

Read the entire IR001 theorem; checked CA001 v3 Sections 1–3 and 7's primitive recurrence, actual matrix-entry majorants, and formal frozen-branch domain; GD001 lower Section 1's corrected terminal input and bounded-primitive scope; UI001's posterior-reveal and finite-label argument; FG001's statement, finite evaluator/error certificate and statistical/capacity interpretation. I did not rely on author diagnostics or inherit the author's conclusion as evidence.

## Adversarial checks and disposition

1. **Reveal can be large or duplicate.** Every pair selects m distinct indices when N>=m. Their union remains at least m even if all selections coincide; adding boundary positions only increases it. The upper bound Fm+b remains valid even when it exceeds N. If N=m, all data are revealed and the subsequent zero-variance argument remains valid. No nonexistent index or M/N substitution is used.
2. **Heavy indices may depend on branch/seed.** The union is over every formal branch and coordinate before sampling. Therefore it is independent of p and observations conditional on a public seed. Boundary bits belong to the union, so actual S is fixed after reveal. Revealed values do not invalidate any formal-history bounded-difference inequality. No conditioning on a data-selected event is smuggled into the product measure.
3. **Remaining influences and dependence.** Removing the top m of each pair gives max remaining c_i<=B/m. Conditional on p and Y, unrevealed coins remain independent. Efron–Stein gives the claimed loose coefficient 1/2; the sharper Bernoulli coefficient is unnecessary. Conditional variance <=B²/(2m) and simultaneous failure <=1/200 hold uniformly for all p,y. The conditional mean is a finite polynomial; differentiating product factors gives exactly the flip identity and slope bound B.
4. **Posterior is not uniform.** The proof properly uses the truncated beta posterior. Hoeffding bounds the joint parameter-outside-window probability; Markov supplies a set of revealed histories with high posterior mass. Boundary modes are covered: the derivative bound is 3sqrt(n)/(3/16)=16sqrt(n), the second derivative magnitude is <=16n, and the inward segment of length 1/(64sqrt(n)) loses at most 1/4+1/512 in log density. This proves the normalization and 128sqrt(n) density bound without an asymptotic approximation. The segment exists even at endpoints.
5. **Good event need not be observable.** This is harmless. Its conditional joint mass is >=.985, relaxed to .98. Its labels lie in a fixed finite set depending only on revealed y and seed, not on p. Covering decoder outputs under the marginal parameter posterior bounds the probability of their neighborhoods whether or not the sample-good event is correlated with p or labels. Hence the subtraction of 1/4 is valid.
6. **Finite arithmetic could encode hidden details.** Contract (2) can allow arbitrary discontinuous error inside its E/Q band. The final floor nevertheless leaves only a constant number of labels within each mesh box; no extra smoothness of the finite implementation is needed. Real Q, negative offsets, endpoint labels, and noninteger E do not invalidate the integer count ceil(2E+6)+1.
7. **Randomization.** For each fixed seed the same uniform prior works in the large-history branch; the small-history prior depends only on deterministic N. The branch selection uses a common deterministic B, not a seed-varying realized sensitivity. Decoder randomness can be fixed independently and averaged. Therefore no illegal interchange of supremum over p and expectation over seed occurs.
8. **Small history constants.** The exact Bernoulli gap yields one-bit chi-square <=1/(12N), product chi-square <=exp(1/12)-1<=1/11, TV<1/4, and Bayes absolute risk >=3/(64sqrt(N)). The deliberately weaker 1/(128sqrt(N)) suffices. Since m<= (C+1)Q²B², the displayed constant follows.
9. **Depth application.** The row-stochastic A has Hmat row sum a+b_att. Summing actual matrix-entry majorants through historical local windows gives <=rGDelta(a+b_att)^l, including early positions, without integrating a logarithmic envelope or invoking factorial square sums. The initial terminal state is unchanged within a frozen branch; this is essential and explicitly assumed. A dense-mask model uses its enlarged fixed recurrence constants; its masks are public and branch-independent. The added scope clarification correctly distinguishes enlarged frozen-branch historical dependence from the genuinely causal subclass with future-boundary dependence restricted to terminal/decoder. The claim does not extend to arbitrary internally rounded networks absent contract (2).
10. **Depth frontier statement.** At M comparable to Q^(2J), fixed J>=2, target O(M^-1/2) forces C_depth^l>=constant Q^(J-1), hence Omega(log Q). FG001's separately reviewed dyadic upper, fixed J and fixed primitive bounds, with E=1, has matching O(log Q) order in the common admitted family. This does not establish a sharp exponential base, an all-Q frontier, or a Markov upper bound. IR001 explicitly retains those limitations.

## Independent executable checks

`IR001_independent_checks.py` was written independently for this review and run successfully. It produces `IR001_independent_checks.json`:

- 608 exact-rational conditional cases for arbitrary nonlinear hypercube tables: top-influence remainder, conditional Efron–Stein bound, exact product-score versus flip derivative identity, and summed derivative bound.
- 31,336 truncated-posterior mode/segment checks across n=1,...,256 and selected n up to 1,000,000, including boundary modes and near-extreme empirical proportions. Largest observed log-density loss 0.250646, below 1/4+1/512 and log 2.
- 936 exact-rational causal matrix-power/local-window tests, including zero diagonal coefficient and a+b_att below one.
- 10,000 real-grid/noninteger-error tube checks, including negative translated coordinates.
- All explicit scalar inequalities in the final reduction checked.

These are finite corroborations, not proofs of the universal assertions; the mathematical checks above supply the review rationale.

## Residual qualifications

As standard for a statistical encoder, f, actual a, influence bounds, and all public choices are fixed independently of the unknown source p; IR001's source-independent encoder setup and explicit prohibition on p as metadata must not be relaxed. A common deterministic B and fixed D,b,E are indispensable to its uniform constant. The bounded-output hypothesis is unnecessary for IR but required for the separate Q^-J global alphabet statement. No defect requiring revision was found.
