# Fresh scientific audit — revision 5 and Chinese stage-7 guide

## Result

**PASS after the explicitly documented scope repairs and pre-fault cube-clipping clarification.** The new integrated arguments agree with the accepted proof scope, with the three presentation/interface items below resolved. No remaining rate, constant, statistical-target, or geometric counterexample has been found. This is a separately executed same-model LLM review, not blind external review, formal verification, or execution of an emitted network.

The audit reads the complete newly integrated English arguments, the Chinese mathematical guide, the thirteen new component proof bodies (eleven accepted units), their full review records, the freeze and acceptance bindings, the inherited uniform finite-evaluator derivation and relevant signed-arithmetic semantics. Earlier v4 proofs are reused on the strength of exact preservation and their existing audit, not represented as freshly re-proved here. The inherited statistical add-one/event-radius chain remains an explicit dependency.

## Issues found and dispositions

1. **All-sample IID domain.** The earlier global convention was M>=64 and Q>=16. The IID opening reset Q but omitted an explicit M>=1 reset. The author now explicitly overrides both defaults for the IID sections and repeats M>=1 in the independent-amplitude section. This restores the accepted FG/IC/GN/NP scope rather than extending the frozen theorem. Genuine pre-change TeX and a three-hunk diff are preserved in `authoring-scratch/pre_scope_clarification.tex` and `scope_clarification.diff`.
2. **Real-resolution influence theorem.** The manuscript initially omitted the accepted IR theorem's explicit real Q>=1 domain. The noise oracle later requires Q'=1/delta, generally non-dyadic. The theorem now explicitly permits every real Q>=1. Its proof uses real Q throughout and does not use dyadic divisibility. The same preserved diff records this repair. Both domain repairs have been independently reviewed and pass.
3. **Actual bank inside the cube before the fault.** The general-Markov construction declares a bank in [0,1]^D but a symmetric generic arithmetic certificate alone gives only proximity to that cube. The post-fault channel clip is not a proof of pre-fault membership. A final exact working-lattice clip before the fault, with corresponding ideal identity stages counted and paid, resolves this interface omission without changing any risk bound. The author/root were asked to preserve original bytes and record an explicit clarification, not silently rewrite a frozen proof. The final explicit ReLU clip, precision-selection order and all-token charges were reviewed and pass; see the separately bound clarification review.

## Proof-level checks

### Mixing-sensitive depth

The binary cutoff is max(sqrt(beta),1/M), not a claim of global square-root mixing; larger alphabets use max(beta,1/M). Upper and lower have the same fixed square-root grid band, and only sufficiently large fixed risk multipliers are promised feasible. The binary upper uses the *same* downward monotone finite scalar compander, positive-bank largest-coordinate comparison, the 32p purity bound, 33-fold empirical error, and a separately charged all-zero-bank event. Full support at beta M^2>=1, singleton stationary support with arbitrary transient starts, beta<M^-2, and equality are all handled. The larger-alphabet residual mixture is applied to occupation, not substituted as another predictor.

The binary lower uses a common stationary source prior, pointwise active-path domination, actual-terminal informative-state probability, Markov continuation coupling and differentiation of ideal finite-path probabilities. It does not replace active suffixes by IID samples or presume a conditional uniform prior. Late-symbol influence already includes local preprocessing. The tube cross-section constants do not grow with depth. All inversion branches (large beta, gain Q>M/4, bounded f, gain>=f, remaining logarithmic branches) are present.

### Clean capacity, partial folds and influence reveal

The complete alphabet is H(Q+1)^J, including endpoint label Q; arbitrary-real decoder outputs were already allowed by the old lower bounds. The fixed-initial-pair statistical witness and stationary-product influence witness are distinct legitimate witnesses inside arbitrary-initialization minimax, combined by maximum.

Partial-fold times include r=0 and multiples of h without duplicate rails. Each gap is at most h, so a Q-bin lies in one closed next branch. Negative slopes are sorted; Q labels impose a singleton rather than a fictitious branch. Closed-cell enlargement is harmless at turning points. The exact integer tent evaluator reconstructs its initial fine scalar; no false one-sided tent-output inequality is used. Every historical token computes its own prefix.

The reveal union is chosen using fixed public influences over all branches, before sampling. It includes all exact positional boundary bits. The remaining maximum influence is B/m and conditional product structure gives the stated variance and polynomial derivative identity. The posterior is explicitly truncated beta, not uniform. Mode, inward segment and density calculations handle boundary modes. The good message set can be unobservable; its posterior mass subtraction is still valid. Source-independent seeds share the prior and deterministic small/large-history branch. Matrix *row sums* give C^d, not a depth-dependent factorial square-sum envelope. An arbitrary nonlocal finite history statistic is not admitted as a positional boundary.

### Fault location and protected terminal pair

The reflection attack applies only to the specified clean folded encoder and its exact dyadic mean. A common reset map, not parameter-specific attacks, erases its orientation. Pinning the terminal pattern 01 under both laws retains the complete side port and pays its common subprobability mass; blindly complementing the terminal pair would fail. Fine-grid pre-cut, real pre-cut, canonical grid-to-grid post-cut, and repeated internal faults remain distinct experiments. No robustness impossibility for all redesigned encoders is inferred from this one collision.

### Robust dyadic and rational paths

The recursive path has a final connector but no copy in plane 1. Even N gives the stated endpoints. Grid-vertex geometry, perpendicular incidence and nonincident separation prove the local inverse, not a heuristic picture. Dyadic plateau fibers contribute their explicit additive term; the strict distance scale prevents extra far endpoint fibers.

For the dyadic evaluator, the input is deliberately coarsened inside one common lattice using scaled values and paid doublings. The guard sum G=(J-1)(J-2)k/2 pays recursive denominator growth. A naive full-P input would not justify exactness. Full signed affine products are retained before the output floor. The two-coordinate case has its own exact P=2h proof and weaker separation requirement.

The shifted no-pause curve uses an extended *first* tent at the final endpoint, then ordinary tents. Child and connector intervals tile [0,1] with positive duration; there is no initial pause and no additive inverse term. Its parameters are generally rational. Signed quotient conversion is an explicitly enlarged finite-description class, charged by actual input length, followed by the same bounded-stage recurrence and bootstrap. It is not declared lattice exact. Squared rational nearest-segment comparisons and inverse interpolation avoid any real projection or square-root oracle. Decoder enumeration is polynomial and paid. Scalar fallback and small Q are explicitly covered; robust sufficiency needs a sufficiently large capacity constant, unlike clean IC's every-positive-constant statement.

### Actual-terminal general Markov prediction

All K^3 triple frequencies are computed before selecting the actual terminal row. The front end is a paid radius-three local table, not a sparse head mislabeled as dense. Composition is certified as a whole; the special raw-mean dyadic lattice argument is not reapplied after companding. The local inverse is pointwise in its scalar input, so borrowing it from the IID construction does not borrow an invalid IID statistical upper.

The symmetric inverse retains 4 epsilon^2+2 epsilon/chi leakage, including zero coordinates, upward errors, L=0 and breakpoints. Public add-one smoothing gives a positive denominator even for an empty row. The true count J is used only in the analysis. The normalization inequality, square-root sum and integer-threshold unconditional occupation bounds yield the stated 8 K^(5/2) epsilon plus capped-Psi contribution. No conditional IID successors or independent terminal query is presumed. The bitlength gain absorbs the linear-leakage logarithm. Partial capacity uses the no-pause inverse and exact squared selection comparisons, including the scalar fallback.

The new finite rational output avoids the old *concrete upper program's* coarse output rounding. It is not a relaxation of older information lower bounds, which already permit arbitrary real decoders. The universal lower counts the whole D=RK^3 bank, not merely R. The R-versus-D capacity gap and additive compander-depth gap away from the named minimal-Q scale remain explicit.

### Independent-amplitude effective precision

The coarse attack a -> delta floor(a/delta) is a single legal source-independent real attack. Its indices determine final Q-labels. The lower grants those indices and applies IR to the original bank at real resolution 1/delta with the same E, not to a discontinuous new ideal map. Zero attack handles delta<=1/Q and the separate statistical witness. Fixed E, positional boundary and seed contracts are preserved.

Upper error delta+2/Q<=3 tau is rederived uniformly rather than hiding Q delta inside a fixed-c constant. The finite public integer certificate tau<=2^-m<2tau is required; arbitrary real delta is not a free input oracle. Full packing, exact dyadic endpoints, no-fit scalar fallback and statistical selection are covered. Fixed positive delta gives a fixed-dimensional floor; growing dimension is not claimed sufficient. The upper remains IID-only.

## Resource and provenance audit

All-token masks and excluded edges, dense zero slots, original parameter descriptions, full products, counters, compact generators, rational tables, decoder work, isolation and clearing remain paid. Generic encoder word w is distinct from decoder word b; reading/writing the handoff and coexisting banks are explicit, even when P is oversized. Offline scratch and stored programs remain separate phase charges. Primitive depth is not PURE/Boolean depth, arithmetic work, or total memory.

Fresh provenance checks verify all 142 English manifest source hashes, all 155 Chinese source bindings, and all eleven frozen receipts. All 67 labeled v4 equations are byte-identical. All 1,388 inline/display mathematical fragments in the inherited technical core are identical; its remaining diff is editorial attribution replacement, preserved as `audit_science_fresh/v4_core_editorial.diff`. Prior TeX and PDF hashes match their immutable release bindings. No post-freeze source-symbol-corruption theorem or unrelated alternative note is integrated.

The Chinese guide was read in full, not inferred from its title or source list. It correctly states the actual-terminal unconditional target, fixed-K/R constants, rational outputs, original real-decoder scope, integer occupation threshold, D/R gap, IID-only NP upper, noise timing, finite certificate, MD band and complete costs. It is an explanatory guide, not a replacement full proof. Its primary-source links are attribution links; this audit does not claim a new exhaustive literature review.

## Fresh executable evidence

Two independently written exact-Fraction scripts (no author diagnostic code imported) pass:

- `check_interfaces.py`: 28,874 assertions on independent recursive curve/time tables, formulas and endpoints; no-pause tiling and speed; nonincident separation; adversarial rational nearest-edge decodes; partial-fold orientation/closed endpoints; symmetric inverse leakage; public finite scale certificates and coarse-attack oracle simulation.
- `check_markov_interfaces.py`: 37,191 assertions on generic-final-half-floor scalar compander monotonicity/zero purity and largest-positive-bank inequalities; exact full-observation overlap with terminal pair retained; nontrivial finite actual-terminal occupation contributions for stochastic/absorbing homogeneous chains.
- `check_provenance.py`: exact manifest/freeze and preserved-core checks above.

An additional exact working-lattice clipping script checks 6,152 integer/nonexpansive cases. These 72,217 finite mathematical checks support selected interfaces. They do not prove universal claims, certify all arithmetic stages, or substitute for the symbolic review. Their source and results are retained under `audit_science_fresh/`.

## Final delta and exact artifact binding

The final explicit clipping addendum and both preserved manuscript clipping deltas pass. The clarification review binds its exact text, and the original scientific freeze and accepted proof/review bytes remain intact. The Chinese guide's corresponding pre-fault clip/provenance paragraphs and unchanged Psi-definition display relocation also pass. Its last substitution of “total depth” for the symbol d has identical meaning.

`AUDIT_SCIENCE_FRESH_BINDINGS.json` identifies the exact final English TeX, Chinese source, source/review/receipt dependencies, diagnostics, preserved corrections and author-confirmed rendered artifacts. Rendered hashes identify the audited-source release; full visual QA was performed by the authors/root, not newly claimed as this mathematical reviewer's all-page inspection. Any subsequent substantive source change requires another delta review.

Final reviewed source hashes:

- English TeX: `bc174b64e00fb704085c3c090323160469f5350afe06c0ac7c674615554e7351`.
- Chinese Markdown: `2305105433b0477da09bb5f1ae9a57903234cd0f34a569c947d3fa7c9caae934`.

Both authors confirmed stop-edit and final rendering QA. The exact rendered hashes and full dependency inventory are in the binding JSON.
