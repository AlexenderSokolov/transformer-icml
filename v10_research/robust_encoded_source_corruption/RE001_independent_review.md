# RE001 — fresh independent full review

2026-11-02. **PASS after one finite-input resource clarification.** This is independent LLM mathematical review, not author self-review, root acceptance, external peer review, novelty certification, formal verification, or a complete emitted-network audit.

Reviewed final theorem SHA-256:

`0cbe7c7a45b2efe6d73ba1a8e55b96d0a6d9f6bc8aa9b74a122960272944ce73`.

I read the entire RE001 theorem and full stated direct proof dependencies: MG001, MG002, GD001 upper and uniform growing-depth FA extension, GN001, JP001, SC002, SC003, BT002 main proof and scalar completion; also the mandatory MG pre-fault-clip clarification and its independent review, the eight corresponding acceptance receipts, and the stage8 companion's experiment/principal-results/provenance scope. The lower and occupation interfaces are treated as accepted dependencies at their verified versions, not claimed to have been newly re-proved from all foundational R011/IU/AU/BIF/BAI documents. I inspected the author diagnostics and wrote a separate exact diagnostic implementation without importing the author code or predecessor test code. No frozen source or theorem was edited by this reviewer.

## Finding and correction

The initial complete candidate accepted an arbitrary rational target scale `t0` for automatic selection of `N`, but its finite resource ledger charged `b_rho` and not the full target-description length. This matters: a rational target with enormous numerator/denominator can still select scalar fallback or a tiny `N`. Its input acquisition and exact cross-product comparisons cannot be charged solely by the selected output scale.

I reported this before a passing verdict. The corrected theorem defines `b_t0` using FULL binary numerator/denominator lengths, charges target acquisition and automatic scale comparisons, and adds it to `Bp` and decoder word bounds, hence to `w` and the displayed work/storage ledger. It permits `b_t0=0` only when `N` is directly supplied and the target-selection procedure is not executed. The statistical target has `O(log M)` full bits, but the arbitrary-target theorem no longer assumes that. The issue and resolution are retained in `RE001_issues_and_resolution.md`. No risk bound, geometric estimate, interface or statistical claim needed alteration.

No remaining blocking defect was found.

## Complete proof and implementation audit

### 1. Experiment, order of corruption and information access

The source class and target match SC002/SC003/BT002: all-pair-state two-step minorization, arbitrary or qualifying stationary initialization, unconditional TV at the actual terminal pair, edits restricted to the first `M` positions, hidden edit seed/mask, and no parameter supplied to the corruption kernel. The upper permits cooperative offline edits and coordinatewise vector port attacks because its error analysis is pathwise. The encoder really begins with the CORRUPTED word. Clean counts and clean terminal occupation enter only the proof. Protecting the final two positions makes selected clean and corrupted row labels identical. The cut exports only `RK^3` labels, the fixed-position protected pair and public source-independent metadata; the explicit isolation rule excludes history rereads and hidden arrays. This does not assume the corrupted word itself remains Markov.

The main output is a finite rational simplex vector, not silently restricted to the coarse cut grid. The separately priced `K/Q_out` rounding term is necessary; a return to the internal `Q` grid would generally lose the construction's benefit. One-shot noise means one vector channel use, not one-coordinate sparsity.

### 2. Complete finite encoder and exact pre-fault cube membership

The paid radius-three local table and uniform statistical pool are the MG dense-family front end, not an uncharged singleton-copy primitive. Historical tokens use their own prefix histograms. The synthetic terminal contributes no triple. The GD compander and GN shifted snake use bounded actual primitive compositions, with saturated doubling charged instead of an unbounded `N` coefficient.

The uniform GD recurrence is applied to the ENTIRE composition, including frequency pooling, rational coefficient conversion, companding and packing. GN's rational-description extension supplies precisely the coefficient error needed by the same recurrence. The prescribed `P>=4h+c_FA(d+2)` closes the stage-error bootstrap; it is not an unjustified fixed-architecture constant at growing depth. All ideal bounds are uniform on formal histories, so symbol editing does not invalidate the certificate.

The final working-lattice operation `ReLU(z)-ReLU(z-1)` is explicitly BEFORE the fault. Its integer-coefficient operations and lattice-exact subtractions give an actual bank in `[0,1]^D`; interval projection preserves the `1/Q` tube around the ideal cube-valued output. These stages are counted before choosing `P`. The older post-fault clip alone would not suffice, and RE001 correctly imports and uses the clarification rather than concealing the omission in the predecessor.

### 3. General certified port radius and geometric recovery

The certificate is finite and source independent, with full rational descriptions. Taking `u=rho+2/Q` correctly covers the complete finite error, port perturbation and final floor. No real noise sample is passed to reliable decoder arithmetic. In the packed branch, `4R u N<=1` implies the nearest-segment projection lies strictly within the GN local-inverse radius: `2 sqrt(R)u<=1/(2 sqrt(R)N)<1/N`. Thus the doubled compander-space error is at most `4sqrt(2R)u/N^(R-1)`, dominated by the rational `epsilon=8R u/N^(R-1)`. Only GN's uniform pointwise geometry is imported, never its IID statistical upper. The scalar fallback has error `2u` and covers budgets for which no separated snake exists.

The curve is the shifted no-plateau construction; the proof does not delete an additive plateau error from the old RG curve. Clipping the recovered compander value before inverse evaluation covers endpoints and gives `y in [0,1]`. Rational nearest-segment search, tie breaking and inversion are genuine finite operations on paid tables.

### 4. Symmetric inverse estimate composed with source edits

The inverse slope argument gives the stated symmetric bound, including an upward reconstruction at a zero frequency. The `epsilon^2` and `epsilon/chi` terms are correctly retained. Changing one symbol affects at most three triples and has full-histogram l1 cost at most six; telescoping applies also to adjacent replacements.

For the selected row, `r'<=r+6k/M` and Cauchy--Schwarz give the mixed term `4epsilon sqrt(K alpha)`. The inequality `4epsilon sqrt(K alpha)<=alpha+4Kepsilon^2` is valid and yields exactly

`Delta <=4epsilon sqrt(Kr)+12k/M+8Kepsilon^2+2Kepsilon/chi`.

The last bound by `4sqrt(K)epsilon sqrt(r)+8K tau` is valid for every `K>=2`. This removes the cross term without claiming any zero purity, support preservation, or exact decoded row mass.

### 5. Larger alphabets: normalization and continuous occupation

The nonnegative-vector normalization bound is correctly applied against clean add-one mass, including `J=0` and false positive reconstruction. The square-root-mass term becomes at most `4sqrt(K)epsilon sqrt(M)/sqrt(J+K)`, whose expected value is bounded by `8K^(5/2)epsilon` using the universal actual-terminal occupation interface. No conditional IID row assertion is used.

JP001's continuous real-`A` occupation completion has exactly the needed domain; it is not an interpolation of an integer edit-budget headline. It covers arbitrary initial law, unsupported starts, every beta, and large `A/M`. With `A=M B_K`, monotonicity and concavity scaling yield the explicit bound (9). The clean comparator and all constants agree with the accepted interfaces. The larger-alphabet decoder itself uses neither `k` nor `beta`.

### 6. Binary local data radius and preservation of true-q weighting

The binary extension is mathematically substantive and valid. Starting from `drow<=6epsilon sqrt(r)+16tau`, the radius computed ONLY from decoded mass,

`Bhat=12epsilon Sroot+68tau`,

satisfies both `drow<=Bhat` and `Bhat<=18epsilon sqrt(r)+132tau` by the displayed Young inequalities. The finite upper-square-root method uses squared integers and never reads a clean row statistic. The limiting `epsilon=0` case is explicit; actual finite-cut epsilons are positive.

The fixed orientation is precisely the complement of the first terminal bit, so its true probabilities are SC003/BIF/JP's `(a,b,e,t)`. Subtracting `M Bhat` from the designated pseudo-count and inflating the denominator gives the clean empirical lower envelope. Its proof works for rational pseudo-counts and a random data-dependent radius: the Lipschitz minimum inequality is pointwise, so no independence of the radius is required. At `J=0`, the numerator is zero and the smoothing `+2` pays the target through the weighted minimum.

The crucial split in (15) is correct: the `sqrt(r)` part is handled by universal square-root occupation, whereas ONLY `528M tau+2` enters the deterministic true-q weighted occupation functional. Thus the square-root-beta cutoff is not obtained by replacing `q` with one. The full-support, singleton-support, symbol-exchange and weak-beta cases inherited through JP001 exhaust the stated all-start/all-beta domain. The `2/M` smoothing term is absorbed by `f_e(2/M)<=8s`. The three numerical coefficients are below `2^18`, `2^10` and `2^24`, respectively. Public `k`/budget awareness is stated, and no unknown-k adaptation is inferred.

### 7. Finite-scale certificate and source-statistical operating point

For `u>t0`, minimal dyadic `N` satisfies `N<2(u/t0)^(1/(R-1))`; condition `u^R<=t0/(8R)^(R-1)` therefore implies geometric separation and `epsilon<=8R t0`. Its selection uses finite integer comparisons. Scalar fallback requires no separation. The bitlength-based statistical target satisfies exactly `s<=t0<2s`, and `m<=chi<2m`. The depth expression follows from the counted `log N` stages.

The function `f_e` is increasing and subadditive, and `e>=1/M` supplies the universal upper `v[1+ln(1+1/v)]`. Both extra terms at `epsilon=O(s)`, `chi>=bitlength(M+1)` are `O(s)`, including finite small `M` after enlarging fixed constants. Thus the resulting capped risk is of order `H_edit`. No noncomputable square root or logarithm is used by the executable setup or decoder merely because such functions appear in the analytic bound.

The source lower transfers in the correct information direction: full corrupted history can simulate this finite observation under zero port noise, and zero noise is admissible. SC002 and BT002 already allow arbitrary full-word decoders, hidden masks/seeds and fixed public budgets. Their stationary lower therefore applies to both initialization minimax models. The theorem properly limits the matching conclusion to the surviving statistical/source profile at a sufficient schedule. It does not claim a matching lower for scalar exponent `R`, total work or the global optimized-encoder noise/precision/depth frontier. The comparison with JP001 explicitly acknowledges the fixed `R`-fold cut-width expansion and architecture-specific uniform-bank lower.

### 8. Full paid resource ledger and limitations

The ledger distinguishes cut label length `h+1`, uniform fractional precision `P`, encoder guard width `w`, and rational decoder width `b`. It pays coefficient descriptions and exact conversion, dense zero/unused slots, public masks, local acquisition, all-token stages, final clips, segment/breakpoint generation and storage, exact rational projection/comparison/inversion, normalization, binary square-root comparisons and their `n b^3+b^4` additions. Handoff includes wide-word reading, label representation conversion and simultaneous old/new banks; cut isolation does not allow those old arrays to become side information.

The corrected arbitrary-target input cost is now included, and the full binary rational encoding prevents compact-exponent denominator blowup. Fixed `K,R` make bounded-count common-denominator products fit the stated words; no growing-K arithmetic claim is made. The explicit tape-scan alternative avoids free random access or exact-real unit cost. PURE compilation has separately paid large depth/width, not the primitive neural depth. The external noise channel is not represented as an implemented reliable real-noise generator. No practical or optimal arithmetic complexity is claimed.

## Independent diagnostic evidence

`RE001_independent_checks.py` is a separate implementation, using exact `Fraction` and integer-square comparisons throughout. Final run passes:

- 7,585 exhaustive small binary/ternary protected-word pairs, including all adjacent edit patterns;
- 350 additional random word pairs with `M>=64`;
- 10,737 symmetric-inverse, edit-composition and normalization cases;
- 10,575 binary lower-envelope/pathwise split cases;
- 5,040 empty-clean-row cases, of which 3,200 have positive reconstructed mass;
- 3,160 dyadic-Q noisy packed-geometry cases from an independently built recursive edge table;
- 5,048 exact pre-fault projection/nonexpansiveness checks;
- 30,716 exact finite-scale schedules, including 14,689 scalar and 16,027 packed cases;
- three arbitrarily long full target descriptions with scalar fallback, illustrating the corrected input-cost requirement;
- eight accepted receipts and their main/component proof hashes, plus the separate clipping clarification/review hashes.

The first geometry diagnostic draft used some integer non-dyadic Q values; it passed, but I narrowed its Q selection to powers of two before the final bound run to match the theorem exactly. This was a diagnostic-domain refinement, not a failed mathematical case. No failed diagnostic or mathematical counterexample was suppressed.

The author diagnostics additionally execute finite signed compander/GN arithmetic on edited-word frequency banks; I inspected their script and result. Those tests expressly do not audit every dense attention/mask slot or prove the all-history FA certificate. The auxiliary binary test includes floating radical comparisons; its mixed scope is candidly preserved, while the independent and main RE001 checks use exact squaring. All finite checks are corroboration only; the full symbolic argument and verified dependency contracts are indispensable.
