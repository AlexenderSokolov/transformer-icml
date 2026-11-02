# FG001 fresh independent review

2026-11-02. Reviewer is separate from theorem author. Review scope: mathematical theorem, exact floor-cell decoder, finite arithmetic admission, IID lower bounds, causal/resource scope. No prior frozen file was edited. No private proof was uploaded. This is a research review, not a formal proof-system validation or emitted-network audit.

## Verdict

**PASS for the stated IID-only, arbitrary-initialization interface theorem.** The author has explicitly clarified that the boundary label is computed from history and independent randomness, never an oracle for the unknown parameter. No substantive mathematical blocker found. The theorem appropriately does not claim full Markov minimax optimality, minimum necessary depth, or novelty.

## Independent reasoning

1. **Fold cells.** For Q=2^h, the h-fold tent has alternating slopes ±Q and breakpoints k/Q. Before label j is used, the previous labels have fixed a single affine branch of F^j, with slope magnitude Q^j. Pulling back a coarse interval of length 1/Q therefore yields length at most Q^(-j-1), even after intersection with prior constraints. Closed endpoints are harmless: adjacent affine formulas agree there. Label Q imposes the single equation F^j(x)=1 on that fixed affine branch and therefore yields a singleton. It is not an extra positive-length branch. The decoder's lower endpoint is on the Q^J grid; the true scalar lies within Q^-J above it.

2. **Finite evaluator.** Direct reading of FA001 v3 Section 2 confirms a full-product affine sum followed by one signed floor. With integer tent weights, an exact half-bias, and lattice inputs, that floor is exact. Its Section 4 computes integer weighted sums and one normalized quotient. At zero logits all positive shifted-Taylor weights agree, hence cancel and give exactly floor(D_f A/m). This is the declared finite program, not substitution of an ideal exponential. Nonmonotonic folding causes no problem because the decoder reconstructs the initial fine scalar; the proof does not claim each later rail rounds one-sidedly relative to its ideal value.

3. **Uniform approximation.** The maximum retained fold count is (J-1)h. Its Lipschitz constant is Q^(J-1), so initial error <2^-P with P>=Jh gives strict pre-cut error <1/Q. Intermediate folds obey the same bound. Thus growing depth is admitted with a direct E=1 certificate, without treating a depth-dependent FA constant as fixed. The optional larger generic precision is consistent with GD001's uniform-family prescription.

4. **IID risk.** Common Bernoulli transition rows make the M generated symbols independent of the initial pair, and the terminal target remains p on every history. The sample-mean standard-deviation bound is 1/(2 sqrt(M)). The deterministic reconstruction error is at most Q^-J+2^-P, proving the asserted upper.

5. **Interface lower.** Exactly J bounded coarse coordinates have at most (Q+1)^J label vectors, including endpoint Q. Multiplying by H pays the full boundary side channel. Fixing an independent random seed gives at most R output values. Their intervals of radius ell/(4R) cover at most half a uniform prior interval of length ell. The outside-prior error gives ell/(8R)=1/(16R). This is valid for stochastic sample-to-message maps; no posterior-uniformity assumption enters. Random seeds may be integrated afterward.

6. **Statistical lower constants.** With initial pair fixed to (0,0), there are exactly M informative IID observations. At p_±=1/2±1/(16 sqrt(M)), the gap is 1/(8 sqrt(M)); p_-(1-p_-)>=3/16 and one-step chi-squared <=1/(12M). Product chi-squared <=1/11 and TV<1/4. The minimum-density triangle inequality yields at least 3/(64 sqrt(M)), as claimed. The max combination needs no common worst-case witness.

7. **Architecture and ledger.** The mean at a historical row uses only its prefix; mask density is at least 1/4 globally, including M=1 at terminal. Historical initial states/parameters do not receive terminal boundary data. Two primitive stages per tent and O(J) rails prevent hidden growing width or a free large per-layer DAG. The ledger pays work precision, log M count guards, all-token evaluation, dense masks, parameter zeros, decoder arithmetic and isolation; it explicitly distinguishes primitive depth from bit-machine/PURE depth. Bounds are deliberately loose existence bounds rather than an optimal complexity result.

## Nonblocking wording cautions

- Resolved during review: Section 1 now explicitly restricts the H-valued boundary label to observed history and independent randomness. An arbitrary parameter oracle would invalidate the full-history statistical data-processing step, although not the alphabet bound.
- Resolved during delta review: Section 5 now calls h the precision exponent and explicitly pays h+1 raw fixed-length bits per coordinate, J(h+1) total, including endpoint label Q. The total information interpretation is unchanged.
- If stationary initialization were imposed on the lower experiment, fixing the initial pair to (0,0) would not be allowed. The current theorem is explicitly arbitrary-initialization. A stationary-only corollary would instead use all M+2 IID observations and adjust constants.

## Executable evidence

`FG001_independent_checks.py` is an independent Fraction/integer implementation of the affine-constraint decoder and exact finite folds. It tests every finest-cell boundary and midpoint for a finite parameter grid, and count fractions A/m at minimal and increased fine precision. Tests include singleton endpoint labels, inverse orientation, denominator divisibility, finite-vs-ideal pre-cut certificates, and the final deterministic error. The JSON records counts and the exact theorem hash. These checks supplement, not replace, the reasoning above.

## Final source binding

Reviewed theorem SHA256: `085e94826be642b71acbbeefe5bdc44cc0774da2eae0e1445e4c7f3a8e93d442`. The author deltas during review clarify the history-derived boundary-label restriction and exact h+1 fixed-length label-bit accounting. Both are correct, resolve the wording cautions, and preserve all tested arithmetic. The stationary-only lower remains excluded from the theorem. Resource review is loose existence accounting, not verification of an emitted network or measured implementation.

Final status-only header delta acknowledges this independent PASS and explicitly disclaims formal proof-system/emitted-network validation. No mathematical content changed.
