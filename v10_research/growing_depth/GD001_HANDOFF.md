# GD001 handoff — 2026-11-02

Status: author proofs plus fresh independent LLM mathematical/interface PASS; root acceptance remains root's decision. Prior accepted/frozen files unchanged. No external publication/upload.

## Result

For fixed K>=3, bounded-score fixed-width causal attention/affine-ReLU families with fixed per-stage primitive budgets, and Q asymptotic sqrt(M), the least necessary/sufficient primitive depth order for O_K(M^-1/2) worst-case prediction risk at β=0 is Θ(loglog M). Sufficiency holds for all β and arbitrary starts, and K>=2. Necessity already holds on stationary K>=3 sources. A sufficiently large fixed target risk multiplier is understood; feasibility for every arbitrarily small multiplier is not claimed.

Upper uses one uniform full triple histogram, coordinatewise concave g_L, terminal grid, then paid inverse/block normalization. All scores zero. Depth L=ceil(log2 bitlength(M+1)) suffices. One-sided finite arithmetic yields inverse-coordinate loss <=(6sqrt(x)+3/2^L)/Q; exact zero purity is preserved. The suggested Q^-2 occupation term is unnecessary. Full risk is U1 in the upper note.

Lower rescales effective grid z=γ_d Q, with γ_d<=C^d, shrinks suffix window, and keeps concentration tube cross-section depth-independent. It proves c/z log(1+min{z/(Mβ0),M/z}/8), with fixed c. At β=0,Q~sqrt(M), statistical risk forces γ_d≳log M, hence d=Ω(loglog M). No factorial global square-sum constant is used.

Uniform FA extension explicitly derives depth-independent per-stage error constants and uses P=4h+c(d+2), proving <=1/Q pre-cut error for every growing-depth network in the fixed primitive family. The SAME FA evaluator includes this upper with one-sided purity; no silent fixed-C_arch reuse. All parameter bits, depth, masks, arithmetic and decoder work are paid. The bespoke minimal-precision upper uses P=h+L+4 as a separate option.

## Evidence files

- GD001_upper_derivation.md
- GD001_lower_derivation.md
- GD001_uniform_FA_extension.md
- GD001_independent_review.md
- GD001_independent_checks.py / .json: 18,132 passing independent exact/finite cases, hashes all three proofs.
- GD001_diagnostics.py / .json: 10,244 coordinate, 3,000 normalization, 10,000 uniform precision-bootstrap passing author checks.
- GD001_lower_diagnostic.json: 32,868 harmonic sanity cases.
- GD001_source_bindings.json: hashes upstream proofs/acceptance receipts.

Independent reviewer requested two fixes, both completed before final hash binding: dummy attention heads require an n²(L+1) budget rather than n² if actually evaluated; generalized FA stage count d>=1 is explicit. No outstanding review blocker.

## Boundaries and natural successor

Depth is actual bounded-primitive attention/positionwise composition depth, NOT bit-PURE compiled depth; total precision/memory are not fixed. No full all-Q depth frontier is claimed. Binary lower and mixing-dependent optimal depth are not yet included. A focused next question is the mixing-dependent depth threshold at Q~sqrt(M), using occupation mixing refinements and the rescaled late-suffix lower; it requires a new argument, not relabeling this β=0 order result.

## Root terminal-initialization clarification

After full root read, the lower's contract was made explicit: synthetic terminal initialization depends only on frozen finite S/public data, S contains every query-used terminal symbol, and historical local-table perturbations affect only positions strictly below T. Any extra granted terminal window increases b0 before H_b is defined. This excludes an otherwise invalid direct diagonal a^depth input contribution. The intended CA-style family and all rates are unchanged. Preclarification proofs/reviews/manifests are preserved in `preclarification_20261102T065250Z/`; see the independent delta review for final lower binding.
