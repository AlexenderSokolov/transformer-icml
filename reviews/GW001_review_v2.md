# GW001 v2 — independent hostile review

2026-11-02. **Verdict: ACCEPT within the expressly changed integer-weight attention model and stated conservative resource conventions.** No blocking mathematical, interface, or asymptotic accounting defect found. This is independent LLM review, not external peer review, formal verification, or execution of a complete emitted network.

Reviewed candidate: `v10_research/growing_weight/GW001_growing_integer_weight_escape_v2.md`, SHA-256 `d55d4684ada185482c25479da36f4141b83c536d3cc16b1b87c8fa3268cfd19a`. Frozen source files were not edited. The v1-to-v2 correction correctly separates primary ratio M² from optional ratio M²Q².

## 1. Exact result accepted

For arbitrary K>=2, M>=1, h>=4, the stated causal local-copy/statistical-summary/residual program is a deterministic finite predictor at the actual terminal pair. It obeys GW1 and GW2, using accepted R011 ORIGINAL as its statistical black-box dependency. For fixed K, the displayed integer half-log precision schedule attains O_K(M^-1/2) risk for all beta and arbitrary initial pair laws. Its actual positive weights range from 1 to M², and its natural-softmax-equivalent logit range is 2 ln M. No bounded-natural-logit theorem follows from the score code being in {0,1,2}.

The implementation existence bounds (5.1)–(5.4) and separate PURE bounds are accepted as conservative constructive asymptotic bounds, not measured hardware profiles, supplied emitter artifacts, or the old SRC batch-hybrid depth/width. Constants are absolute; K dependence is retained in displayed formulas. The full source-dependent input is the one-hot history. Cache and layouts depend only on public inputs.

## 2. Source/interface audit

Read the complete GW001 v2 candidate; R011 theorem and proof with its root acceptance; SRC §§1–4 and §§9–10; GU §11.1; BA001's exact family and claims; BF001 v2 contextual inclusion and scope. Inspected author diagnostics but did not execute its source-writing script. All eight candidate manifest hashes verified independently. R011 acceptance is the declared inherited statistical interface, not a claim to have independently re-proved every underlying historical dependency in this review.

R011 uses exactly M observed departures from Y_0 through Y_(M-1), target theta_(Y_M), arbitrary initial distribution, and all-state D2(beta). Its ORIGINAL upper is min(1,2^13 H), with H exactly GW001's Hstat. No use of R011's stronger adaptive ALG or common-minimax scale is smuggled into GW001. The beta=0 and beta=1 endpoints have positive exponents and no 0^0 ambiguity.

SRC's actual old weight is a separately evaluated truncated exponential recurrence at each full finite score, uniformly in [1,6], with a distinct log-generation cost. GW001 does not use that recurrence or assert identical outputs. Cache (1,M,M²) is a genuinely changed code-to-weight map, computed by integer copy/multiplication. The real-softmax identity is a mathematical comparison only. BA001's positive fixed interval hypothesis fails uniformly in M here; the construction retains bounded local values, one dense terminal summary, local windows r=3, and no historical decoder reread. It therefore is not a counterexample to BA001 or BF001.

## 3. Causality, exact ratio and cut

The two singleton masks select only predecessors or self. At t=n=M+3 their returned pair is (X_(N-1),X_N), with no next symbol input. Singleton normalization is exact even when the value coordinate is one: the grid includes Q/Q and has h+1 numerator bits. Residual x copies and both lag arrays are paid. At t>=3 statistical keys are 3 through min(t,N), and at t=1,2 self fallback has observed one-hot value. All rows are nonempty, including M=1. The terminal synthetic zero token is never an allowed statistical value.

Each score is the sum of two one-hot equalities, hence 0,1,2; its cache selector is a three-way finite mux. Exact integer sums followed by floor(QA/D) produce the asserted coordinatewise down-rounded ratio. Shared denominators cause no problem. Replacing only the final coordinate by the residual yields a nonnegative simplex grid vector. It is not independent rounding of a probability vector followed by an uncharged normalization oracle.

The decoder's only source-dependent terminal inputs are the K returned grid scalars. D, A, codes, other rows, and historical arrays remain internal workspace; a physical allocation retained until other rows finish is not a functional decoder edge. The no-reread contract is therefore consistent with the paid batch arrays. No exact empirical-count port is hidden in the interface.

## 4. Deterministic discrepancy and endpoints

For J>=1, matched mass is JM² and unmatched mass at most M²; normalized contamination is at most 1/J. This gives TV(B,C/J)<=1/J, not an unjustified exact recovery. Add-one shrinkage is at most K/(J+K), and 1/J<=(K+1)/(J+K). The triangle bound (2K+1)/(J+K), capped by the independent simplex bound one, is valid. At J=0 the latter bound is still >=1 before capping; no runtime J test or probabilistic empty-row exception is needed. If unmatched mass is zero, the proof correctly avoids dividing by it. M=1 makes every cache entry one, and all inequalities still hold; a vanishing effective logit range at this endpoint is explicitly acknowledged.

For the first K-1 coordinates, downward errors e_c are nonnegative and <1/Q. The residual last-coordinate error is their sum with the opposite sign. Thus half-L1 error is exactly sum e_c, establishing the (K-1)/Q term. No K-fold head-error amplification beyond that named term appears.

For W=MQ, the sharper nonempty leakage is <=1/Q; when J=0, K/(J+K)=1 handles the entire simplex loss. The optional K/Q total grid-plus-leakage term follows. For general positive integer A, W=MA gives leakage <=1/(AJ) and discrepancy coefficient K+(K+1)/A. General A does require enlarged words; the manuscript explicitly says so. It is not covered at the original b for arbitrarily large A.

## 5. Actual-terminal occupation and risk

The occupation proof is valid for any finite homogeneous chain: the suffix starting state is conditioned on, not the terminal state. For fixed kernel, maximal-start bad-event probability B_m is nonincreasing by suffix domination. The pathwise first-w-occurrences bound is dw for each initial state; summing over d starting states before taking the maximum gives d²w. There is no illicit interchange that would replace d² by d. Applying d=K² gives exactly K^4 w/(M+1), at the random terminal pair, with no stationarity assumption.

For t in (0,1), the strict tail event of V=min(1,A/(J+K)) is J<A/t-K. Its integer threshold is ceil(A/t-K), with empty event when nonpositive, and threshold <=A/t because K>=1. Tail integration gives Psi(cA). This threshold detail covers exact integral boundaries. Triangle inequality with R011 then yields GW1; adding the independent loss cap is valid. Hstat<=g and Psi(x)<=2sqrt(x) give GW2. The schedule h=max(4,ceil(bitlength(M+1)/2)) has 2^(2h)>=M+1 and h=half log2(M+1)+O(1). This is output-grid precision, not fixed total arithmetic precision or fixed effective logits.

## 6. Full cost audit

### Numeric ranges and elementary operations

Primary denominators/numerators are <=M³, including fallback rows. Dividends are <=M³2^h. Optional W=MQ changes this to M³2^(3h), still within a constant multiple of h+ell. Sum-of-grid-word bounds <=KQ and dense small-value dot/projection guards fit the generously chosen b=64(h+ell+1). All loop/address lengths are O(b): log n, log K, and log b are O(b), including addresses into polynomial-in-n,K,b files. Restoring division has a positive divisor and uses fixed public loops. Three-way cache lookup needs O(b), not arbitrary table access.

Full products must retain double-length bit storage before any discard. The manuscript's full-product statement should be understood in its standard O(b)-width sense: multiplying two allocated b-bit containers may temporarily use 2b physical bits (with leading zeros on the proved reachable values), or payload operand widths can be chosen below b/2 so full products fit the common b allowance. This is a harmless representation choice already covered by every O(b) scratch and O(b²) work entry, not permission to truncate a product. No numerical overflow or missing asymptotic factor results. The claim is not a literal theorem that arbitrary unrestricted b-bit integer products fit b bits.

### Packed known-address circuit and tape evaluator

The schedule pays all n-token dense projection entries including zeros: O(nK²b²). Each of three heads scans all n² candidates, including masked ones; dense statistical edges pay dot product, cache selection, denominator and every numerator update. Singleton heads also pay scans/normalization, not free indexed access. Normalization and residual decoding execute at all n rows. Cache generation costs an actual square and writes, with optional shift for MQ. Input acquisition, synthetic zeros, residual/local copies, clearing, counters, output serialization, and masks/positions are within the enlarged T0=O(n²K²b²).

S=O(n²+nKb+K²b+b²) includes packed input, masks/positions, front matrices including zero slots, projected/history/lag/output arrays, row bank, cache, controller and arithmetic scratch. The n ell position term is absorbed since ell=O(n+Kb); there is no concealed n² numerical weight array. Even counting obsolete and new token arrays simultaneously is within nKb up to fixed constants. The local bank is not misreported as total memory.

Storing O(T0) explicit O(b)-bit instructions costs O(T0 b). Scanning the whole S-bit data tape for each fixed-arity access, with O(b) address comparison, gives O(T0 S b) serial bitwork. Sequential instruction fetch is not random access; reads and writes require the named scans. Fixed finite multi-tape/controller implementation and O(b²) scratch fit the ledger. The faster known-address gate count is explicitly an alternative wired circuit, not the runtime of this scan evaluator.

Offline emission in public nested-loop order needs no sorting or data-dependent layout. O(b²) arithmetic per instruction/data record safely covers address generation and writes; the stored program and all previously generated data coexist in the stated O(T0 b+S+b²) phase peak. Forward stored program plus full S, not just rolling arithmetic scratch, determines its peak. Binary symbol conversion, if selected, is additive and absorbed, not assumed free. No all-K²-query output claim is made.

### PURE expansion

Every Boolean update has a constant-size bounded-fan-in ReLU bit gadget; all other live bits have explicit holds. Therefore O(T) depth, O(S') width and O(TS') sparse gate/hold records are conservative. Wiring/coefficients require O(b)-bit addresses/values, giving O(bTS') sparse bits. Dense slots, including zero weights and biases, give O(bT(S')²) stored bits and O(b²T(S')²) generic dense bitwork. The two scalar-neural rolling layers cost O(bS'), distinct from packed-bit storage. Final dyadic decode fits the O(b) extra depth/width allowance and uses finite coefficients. Offline parameter writes and generation scratch are included in phase peak, along with separately retained public/input constants when applicable. The flattened network has no attention oracle and is not represented as a three-standard-softmax-head architecture. Tape and PURE implementation coordinates are not mixed.

## 7. Independent diagnostics and limitations

`reviews/GW001_independent_checks_v2.py` is independently written, with exact rational arithmetic and symbol-level lag construction rather than copying the author's projection implementation. It passed:

- 2,096 histories over K=2, M<=7 and K=3, M<=4;
- 65,096 all-token ratio/simplex/discrepancy checks, including primary A=1, optional A=Q and general A=3;
- 3,608 empty and 4,776 nonempty terminal cases;
- 3,564 exact finite-chain UC cases, plus maximal-start monotonicity and sum bounds;
- 2,370 restoring-division primitive cases;
- 2,496 public half-log schedule cases, including large powers-of-two boundaries;
- all eight source-manifest hashes.

These checks are diagnostic support only. Small-M risk bounds often cap at one; no vacuous numerical risk check is presented as validation of the asymptotic theorem. The complete large circuit/emitter, serial machine and dense PURE network were not generated or executed. Their acceptance here is proof/algorithmic-ledger review. No literature search or priority certification was needed or performed: the manuscript makes no novelty claim.

## 8. Final scope lock

Accept an explicit sufficient changed-model operating point, not an optimal or necessary logit tradeoff, advantage over another algorithm, architectural universality statement, training result, original finite exponential-evaluator implementation, or near-IID K-sharp minimax theorem. The result leaves total resources growing and pays logarithmic effective logit range to escape a fixed-weight information obstruction. No revision is required for the theorem or asymptotic ledgers; the product-container clarification above is nonblocking implementation hygiene.
