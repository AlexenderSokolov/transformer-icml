# SB001 v2 — independent hostile review

**Verdict: PASS within the stated model and dependency contract.** No blocking mathematical, scope, or resource-accounting defect found. SB1–SB4 and the optional §7 order theorem are supported, not merely conjectured, conditional on the explicitly inherited accepted statistical lemmas. This is an independent LLM review, not formal verification, external peer review, a novelty determination, or execution of an emitted network.

Reviewed immutable target: `v10_research/score_precision/SB001_loglog_effective_score_budget_v2.md`, SHA-256 `d10086be4d358e322872daffad4dd10572588d6dcffaecbffefc409df6a217b7`.

## Evidence and independence

Read the entire target, BA001 v1, AU001 v1, GW001 v3, and the canonical R011 scientific proof, rather than relying on the author's earlier algebra audit. Also checked current BA001/AU001/GW001 acceptance records against actual file hashes. R011's ORIGINAL statement is precisely `R^+ <= min(1,2^13 H)` with horizon M+1, arbitrary initialization, and the actual terminal pair. It is not the common-minimax L or adaptive ALG bound. GW001's Hstat agrees exactly. AU001's general occupation lemma permits every positive numerator A, so substituting the new A is legitimate; importing AU001's predictor-specific final risk instead would not be legitimate and is not done here.

Bindings and independently authored reproducible checks accompany this review. Neither author diagnostics nor prior review verdicts were used as a replacement for checking the new algebra.

## 1. Changed encoder and deterministic error

The terminal key set contains exactly M triples. The terminal pair is `(X_(N-1),X_N)`, obtained from two paid local shifts at the synthetic token. Dotting pair one-hots distinguishes a complete pair match, not two independent partial-match scores. Every statistical weight is the actual positive integer 1 or κ. Values are query-independent triple indicators. Nonmatching triples occupy other coordinates: they dilute the selected pair block but do not change its normalized conditional successor distribution. This is the essential valid change from GW001's successor-only values.

The selected exact block is `κ C/[M+(κ-1)J]`, hence mass `r=κJ/[M+(κ-1)J]`. If the floors retain positive mass, the two triangle-inequality terms for normalization have total half-L1 error at most e/r. If every floor vanishes, r<K/Q and the capped bound becomes one. Thus no positive surviving-mass assumption is hidden. For J>=1, `J+K <= (K+1)J` gives (3.1). Comparing to the add-one law costs at most K/(J+K); for J=0 this equals one and independently covers any fallback. Ordered simplex rounding costs (K-1)/Q and produces a genuine simplex. Consequently (3.2) is correct on every history, with no conditioning that falsely makes successor samples independent.

The full K³ bank is retained before the cut. The decoder sees only that bank, its exact pair, and public metadata, not denominators, exact counts, unquantized mass, historical features, or earlier outputs. Normalization is post-grid; the test s=0 is not an exact J=0 side channel. The pair has only K² possibilities and is contained in BA001's stronger exact boundary grant. First two rows have nonempty self fallbacks; the terminal synthetic zero triple is not among terminal keys. All-token execution is consistent with causality.

## 2. Universal integration and SB2

The occupation proof in GW001 is valid for arbitrary starts: terminal suffix domination makes the maximum initial-state probability nonincreasing, and pathwise first-w charging followed by summation over initial states gives the K⁴ bound. The layer-cake integer threshold `ceil(a/t-K) <= a/t` is valid because K>=1; no real-versus-integer threshold gap appears. Applying it to a=K yields Ψ(K⁵/(M+1)); applying it to `a=K(K+1)M/(κQ)` yields the stated Ψ(D_K/(κQ)). Combining with R011 ORIGINAL proves SB1.

For M>=64, L=bitlength(M+1)>=7, so max(4,ceil(L/2)) equals ceil(L/2). The squared inequalities `M+1 <= Q² <= 4(M+1)` hold also at bitlength jumps and the first permitted M. The scalar envelope `Ψ(D/z) <= D[1+ln(1+z)]/z` is valid in both capped and uncapped cases. With z=LQ, `1+ln(1+LQ) <= 3L` follows from the displayed elementary bounds. Together with Ψ(x)<=2sqrt(x), this proves the explicit SB2 multiplier. Natural effective range ln L is ln ln(M+1)+O(1); it is not arithmetic-word precision, which remains O(log M).

## 3. Lower constants, finite domain and comparison family

BA001 is genuinely uniform over table contents and its displayed finite constants allow a new weight interval [1,κ(M)] at each M. Its proof does not require κ independent of M to obtain that finite inequality; only its old fixed-family asymptotic interpretation did. Substitution gives T=κu, L_B=4κr, C_B=4κu. The ceiling bound `ceil(8κu+4)+1 <= κ(8u+6)` is valid for all κ>=1. The product therefore deteriorates by at most κ^(D+1), not κ^D and not an omitted κ-dependent constant. Equation (5.2) follows.

At β=0 the floor β0=max(β,1/M) is essential: t=1, and the truncated minimum is min(Q,M/Q). Under the grid band it is at least min(c_-,1/c_+)sqrt(M). Its logarithm eventually dominates (1/4)ln M; the threshold can depend on c_-,c_+. The prefactor uses 1/Q>=1/(c_+sqrt M). The manuscript expressly limits SB3's simplified logarithmic form to the eventual regime, so it does not falsely assert that comparison for every M>=64. Taking logarithms yields SB4 for every fixed target multiplier C.

The at-most-D revision is sound. A smaller bank can be embedded statistically in the exact-D class using deterministic zero coordinates with admissible weights; these convey no extra information. BA001's lower then bounds the smaller physical implementation. This is not a physical-storage claim for a padded network. The upper fits r=3 and D>=K³; for greater r the triple tables simply ignore extra window entries. A growing-D claim would not follow from these constants. K>=3 is needed for the lower witness; the manuscript correctly asserts only the upper for K=2. Lower initialization is stationary, a subclass of the arbitrary-start upper experiment.

Thus the matched quantity is the **order of natural effective logit range**, not κ itself or its exponent. No arbitrary-depth/global-feature architecture lower follows or is claimed. The equivalent real-softmax ratio is explanatory only: the old finite exponential evaluator is not being certified.

## 4. Mixing-dependent refinement

For β>=1/M, use the exact AU001 suffix mixture with m=ceil(M/2). The general stationary bound applied to this new A gives coefficient `2K³(K+1)/z` and logarithm `ln(1+480z/[K(K+1)t])`; no predictor-specific AU001 constants are transplanted. Since `ln(1+ax)<=ln(max(1,a))+ln(1+x)` and ln480<7, twice the bracket is at most 48G. The residual universal occupation cost is at most εΨ(2D_K/z). The two branches z<2D_K and z>=2D_K, together with ε<=min(1,e exp(-t/4)), bound it by 10D_K G/z. β=1 has zero residual, and β<1/M uses t=1 and the universal envelope directly. These cover all endpoints and prove (7.1).

Choosing κ=ceil(f) is a public **known-β-promise** selection, not learning β. Because `1+κQ/t<=κ(1+Q/t)` and lnκ<=κ-1, the asserted ratio bound <=2 holds for every f>=1. This optional transcendental description is not represented as a free runtime primitive: the manuscript explicitly excludes its input-dependent selection cost from the core ledger and discusses a separately charged rational/bitlength alternative.

For necessity, `min(Q/t,M/Q) >= (Q/t)/max(1,c_+²)` uses t>=1 and Q²/M<=c_+². BA1 controls ln(1+Q/t); BA2 supplies the missing constant-one floor with the same κ^(D+1) exponent. Taking their maximum, not their sum on a common witness, gives a constant times f. Combining with the target risk and Q<=c_+sqrt M yields (7.2). For β>1/16, f is bounded; κ>=1 gives the trivial lower for 1+range. Additive constants in (7.2) plus this baseline produce the uniform order statement, not a pointwise positive lower on range when f is bounded.

The least-feasible-budget interpretation requires a sufficiently large fixed target multiplier. V2 correctly includes c_- in sufficiency: (7.1) gives `[(2^13+2)K^(5/2)+(2C_K+2K-1)/c_-]/sqrt M`. Necessity can be stated for any fixed C, but an arbitrary tiny C is not promised attainable. The v2 quantifiers now make this distinction explicit.

## 5. Full implementation ledger

The ledger consistently pays for local feature gates, dense maps including zero slots, K² dot products, K³ updates, all n² candidate edges per head, full nK³ storage, all-token division/decoding, masks, cache creation, loops, serialization, copies/clears and addresses. Common feature width O(K³) gives O(K⁶) dense maps; using K⁶ in T0 is conservative relative to the K³ attention loop. No n² numeric weight matrix is required when edges are streamed, but n² masks remain charged.

The integer bounds include Mκ denominators/numerators, Q times numerators, KQ block sums and Q² decoder dividends. The chosen b includes bitlength κ as well as h and log(n+K), and full 2b products/guarded O(b) temporaries are separate from persistent b-bit payloads. Safe selected denominators exclude inactive division by zero. Exact one-hot Boolean arithmetic and finite dyadic output need no transcendental oracle.

The serial evaluator pays O(T0 b) program records and O(T0 S b) tape scanning, rather than treating indexed access as free. The PURE alternative explicitly holds live bits and pays sparse/dense wiring, zeros, coefficients, rolling numeric layers, offline generation, and phase-wise coexistence. These are alternative implementations, not mixed coordinatewise minima. The flattened PURE realization is correctly not called a three-ordinary-softmax-head network. The ledger proves conservative constructive asymptotic existence; it is not a measured implementation or an emitted-network verification.

## Independent checks and limits

`reviews/SB001_independent_checks_v2.py` independently rebuilds the complete triple bank with exact rational decoding, checks (3.1)/(3.2), simplex validity and empty/vanishing blocks, checks bitlength schedules near powers of two, and probes scalar envelopes, mixing selection/logarithm comparisons and BA constants. Result: **PASS**, 38,547 exact-history configurations (29,482 all-zero selected blocks, 19,134 zero-match cases), 14,866 schedule cases, 4,375 envelope cases, 1,605 mixing/log cases, and 60 lower-constant cases. Small histories and Q<16 deliberately test the deterministic lemma outside the statistical theorem's domain; they are not claimed statistical evidence in that domain. Numeric probes corroborate the independently checked symbolic arguments, not replace them.

No source edits made. No blocking action or external authorization needed. Recommended disposition: accept the stated SB001 v2 theorem and conservative implementation ledger with the explicit inherited-dependency and independent-LLM-review limitations above. Do not extrapolate to joint-K sharpness, optimal κ exponent, arbitrary deep families, original-evaluator equivalence, unknown-β budget learning, or novelty.
