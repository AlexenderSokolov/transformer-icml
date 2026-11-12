# Independent scope, indexing and numerical audit of the two-read bridge

Date: 2026-11-12. Reviewed `RESULT.md` and `check.py`. This complements, rather than duplicates, the step-by-step mathematical review. It is not formal verification or novelty certification.

## Verdict

The actual two-read example correctly disproves exact count-plus-endpoint sufficiency. The proposed source-average replacement is consistent with the example and its indexing and statistical risk reduction are sound under the stated identical raw embedding/value/local-map restrictions, with one important score-contract clarification below. No general evolving-KV or finite-precision lower follows.

## Required explicit score convention

The complete scores in each attention softmax must be the controlled dot products (with any conventional scale absorbed into Q or K), up to a common row offset. Public positional information may enter those controlled factors; an arbitrary additive pairwise positional bias is NOT covered merely by a bound on complete scores. For example Q=K=0, two values +1,-1, and additional scores (+b,-b) give attention tanh(b) instead of uniform zero, whereas the claimed QF bound is zero. This is a concrete failure of the intermediate inequality if the phrase “public position information may affect QK SCORES” is interpreted to permit independent additive bias. Explicitly disallow such bias or charge its centered score norm separately. This is a contract ambiguity, not a disproof under the intended pure-dot-product reading.

## Positions and endpoints

N is the number of raw spins, terminal index is n=N+1, and the target next-spin probability is (1+theta X_{N-1} X_N)/2. The public terminal is a separate sentinel, not an additional source sample. Its own initial value belongs in both self-inclusive terminal averages. Raw row i has exactly i raw values and no sentinel.

In the displayed example, the words +++--- and ++-+-- have identical count and final pair. Although raw row-3 and row-4 token signs differ, the first-state full-LN denominator depends on their square, so second values depend only on the prefix means. Those means differ only at row 3. The terminal first state is zero, hence its second value is zero; division by 7 is correct. Final full LN maps the terminal state (0,0,0,0,z,-z) to a monotone normalized coordinate z/sqrt(1+z^2/3), so the probability difference survives the mandatory final LN. This is a genuine full-PreLN construction with zero FFNs, not a missing-normalization artifact.

Identical token-only reference maps are essential. They may depend on N, but within a fixed N they must not depend on raw position. Position-dependent residual embeddings or exposed position features invalidate the count measurability conclusion even if attention QK norms remain small.

## Concentration and risk quantifiers

The first-layer raw fluctuation is the unconditioned stationary sum of a single two-valued map. At the terminal, the tag-dependent initial value cancels pathwise in the comparison. With uniform Lipschitz constants over all endpoint tags, taking unconditional expectation requires no four-tag union factor. Conditioning that sum on a terminal pair and reusing the unconditional bound would instead be unjustified, but the draft does not do that.

The second layer uses a triangle bound on the average first-state deviations; it does not assert independence of evolving values or concentration after conditioning on a query. The terminal deviation is the n-th summand, making the bound sum_{i=1}^n i^{-1/2} <= 2 sqrt(n) valid. References and actual states must remain in the specified common comparison domains; projection does not magically extend undefined local maps.

For clarity, define R_theta = E_theta |Q-(1+theta X_{N-1}X_N)/2|, choose 0<h<=1-2c and N>=3, and use identical constants for theta=±h. The same parameter-independent count-plus-pair reference predictor is used at both sources. This is what permits its equal-prior risk to be bounded below by B_N, and max risk then exceeds equal-prior risk. The result is not a lower bound for each theta individually and does not assert useful risk for the counterexample. The presented result is clean deterministic; randomized architectures require conditioning on public theta-independent randomness and uniform constants. No finite-p claim is tested here.

## Re-execution and diagnostic strength

Copied the script into a separate review directory and reran it without changing author outputs. The resulting JSON is byte-identical to the author's recorded results.

- q_x = 0.5891837558334733; q_y = 0.5746977577182404.
- Difference = 0.014485998115232879.
- Second-read scalar difference = 0.06297305313699836.
- Maximum observed all-row physical norm = 2.108878474699913.

The reported 34 checks are FOUR counterexample assertions plus FIFTEEN probability-normalization checks plus FIFTEEN expected-error inequalities. They are not 34 independent architectures or 34 separate examples. The 15 cases exhaustively enumerate words at N in {3,4,6,8,10} and theta in {-0.5,0,0.5}; no random seed is needed. Their conservative bridge bounds range from 5.51135 to 9.13954, whereas probability discrepancies are at most one, so these particular numerical bridge tests are vacuous as inequality evidence. They do exercise source weights and actual full-PreLN computation. The exact counterexample and analytic source-average argument carry the substantive conclusions.

The script does not currently reject optimized Python, which strips assertions. Add an explicit `if not __debug__: raise RuntimeError(...)` guard before advertising assertion-based verification. No CI was run. This audit did not test generic nonzero QK arrays or arbitrary terminal maps.

## Revision verification

The revised result explicitly excludes uncharged additive pairwise bias and identifies the finite bridge comparisons as vacuous. The revised script rejects optimized Python; this rejection was tested. A fresh normal replay still matches results.json byte-for-byte. The earlier corrective recommendations above are resolved for those three points.
