# BC001 independent mathematical/interface review v1

2026-11-02. Reviewer: separately spawned `independent LLM reviewer` agent. Reviewed current `BC001_binary_stationary_causal_frontier_v1.md`, including the notation clarification `3/exp(1)` and final §§1,5 capacity clarification (supplied-table row-sum-one projections, optional explicit AND requiring row-sum three, and identically zero synthetic state with width 16). Verdict: **PASS within the explicitly stationary, fixed-budget, finite-evaluator scope; no blocking defect found.** This is independent LLM review, not formal verification, external peer review or root acceptance. No proof/source/delivery file was edited by this reviewer.

## Load-bearing checks

### 1. Nonlinear Markov lower

The extension does not illegitimately use BI001's local-sum variance lemma on a nonlinear global output. Instead it first imports CA001's late-coordinate replacement bound Γ/M, then telescopes arbitrary pairs of formal source histories. The BI001 active kernel has a common 1/8 atom in its two-step B column. A blockwise maximal/shared-atom coupling, with conditional bridges, bounds expected differing states by 16, including the initial differing state. Symbol disagreements are bounded by state disagreements. The common revealed prefix is identical, all remaining random indices lie in the late suffix, and local-window propagation has already been paid inside Γ. Thus continuation-expectation differences <=16Γ/M are valid; the chosen 34Γ/M is conservative.

The Doob conditional ranges and orthogonal variance sum consequently yield BC2. The single-transition derivative formula is legitimate for the finite path polynomial. Only row A varies, and each signed B/C continuation difference has the same bound, giving BC3. This is not differentiation of finite rounded activations and not IID concentration. Formal-history branch uniformity is essential for the telescoping paths and is explicitly retained in the family.

The source prior is shared across all j and independent seeds. Source pathwise domination is used rather than claiming event probabilities or conditional suffix laws are parameter independent. Terminal A has probability >=1/8, so subtracting the <=1/32 bad event leaves >=3/32. Removing the decoder-value neighborhoods costs <=1/32 of prior measure regardless of terminal dependence. The resulting radius times probability is exactly 1/(2048 R_j). Domination and the harmonic integral produce the displayed 1/(524288 A_B) constant. The lower is never extended outside β<=1/256,Q<=M/4 without a separate scalar argument.

### 2. Complete-message tube and all regimes

The Chebyshev union bound uses D H_b coordinates and τ_B²=32 D H_b L_c², correctly leaving failure <=1/32. The curve speed is L_c j/M and interval length is 1/2, so the stated mesh-count upper is sufficient. After scaling by Q, concentration is at most τ_B/2, mesh error at most one, certified finite error at most one, and floor error less than one. The radius τ_B+3 and integer count N_B=ceil(2τ_B+6)+1 are safe. Actual S is counted as one of H_b branches and j is granted before the fixed-j argument; neither leaks an extra infinite-valued statistic.

CA001's binary IID floor remains applicable with FA's enlarged tube; no growing-weight uniformity argument is required in this fixed-architecture family. The full-history testing floor is also valid. The β>1/256 branch uses W<=1/Q+2/sqrt(M), the two large-Q branches use W<=5/sqrt(M), and the residual branch uses W<=1/Q+24L. Their combination supports exactly c_arch=min(c_S/5,c_I/2,c_B/48). The notation `exp(1)` now prevents confusion with the cutoff e. No missing small-M or large-Q case was found in the declared M>=64,Q>=16 domain.

### 3. Exact finite upper and causality

The prototype is genuinely a member of the finite-data affine/ReLU subclass: paid radius-three finite input tables can contain the eight one-hot triple bits; equivalently the local AND is ReLU(u+v+w-2) on exact local one-hot inputs. Singleton copy heads are not treated as dense attention. The masks are nonempty, independent of S, causal, and have density >=1/3, including early rows and the terminal synthetic row. Zero Q/K and exact bit values satisfy all bounded primitive hypotheses. Historical states never consume terminal S; S is used at most at the appended query and downstream block selection. Identity padding ignores extra head outputs and preserves the histogram coordinates.

The crucial exactness claim is stronger than FA's generic approximation guarantee and is proved correctly. FA's shifted Taylor routine produces one identical positive integer W_* at every zero-logit edge. Exact accumulations give N=W_* d_f C and Z=M W_*, so the output integer is floor(d_f C/M). There is no extra d_f division. Integer coefficients, projection, concatenation, and identity padding cause no further loss on already represented grid values. Since d_f/Q is integral, the final coarse label is floor(Q C/M). Thus every zero count remains exactly zero, every pure coordinate remains pure, and the exact SB001 κ=1 histogram input is obtained. Approximate error alone would not suffice; the proof does not make that mistake.

BU001 v2's stationary application therefore inherits the complete binary minority-floor and zero-bank arguments with identical labels and decoder, not merely close averages. The post-cut selection uses only S and grid coordinates. True counts, row masses and weighted denominators remain proof variables. No arbitrary-start improved cutoff is inferred.

### 4. Costs and model boundary

FA001's compact sequential multi-tape layout is preserved, including public numerical records at P_f+O_arch(1) bits, separate w-bit scratch, explicit masks, generated tables, full edge scans, full products/guards, Taylor divisions, rewinds, copying, and microcode. The wider word pays log n in addition to fine fractional precision. The supplied/generation cost is not silently omitted. A fixed prototype may have fewer than n² parameters, but the stated n² upper is harmless.

The decoder suffix has a completely finite implementation already contained in SB001's paid program. Charging the entire SB001 addressed resource envelope while executing only its pointwise suffix is a conservative overcharge, not inclusion of its singleton heads in the causal architecture. Conversion/copying of the new encoder bank is additionally paid. All-token work and full banks remain charged, and historical outputs are isolated from the terminal decoder. Composed resource sums are used rather than mixed minima. PURE expansion is expressly a separate larger circuit and is not advertised as a fixed-depth bit-level realization. These qualifications prevent the usual architecture-versus-evaluator conflation.

The final revision explicitly separates the supplied-table prototype (row-sum-one projections, admitted under the declared bound two and the original CF001 budget) from the optional explicit AND implementation (separately enlarged row-sum-three budget). Its synthetic initial state is zero, so width 16 holds eight triple and eight output slots without extra query storage. This resolves the capacity ambiguity in the earlier wording; no further capacity obstruction was found.

## Independent evidence

`BC001_independent_checks_v1.py` was written and run independently of author diagnostics. Its JSON records:

- 60 exact rational stationary-law/all-state minorization tests;
- 55,260 exact shifted-Taylor normalization and nested-floor cases, including W_* unequal to d_f;
- 1,269 exact mask-density/causality rows;
- 2,040 exhaustive short binary histories checking one-hot ReLU triple features and eight histogram labels;
- 1,656 floating scalar-completion cases (only this group uses floating arithmetic);
- verification that CA001, FA001, CF001, BI001, BU001, BS001 and SB001 accepted source hashes match their receipts.

These finite checks corroborate local identities and boundary cases; universal conclusions rest on the written proof and scoped accepted dependencies. Review source hashes are in `BC001_review_source_bindings_v1.json`. The reviewer recommends root consideration of BC001 as a new standalone post-stage-5 unit. Stage-5 and paper_v3 must remain immutable. No new external literature/novelty claim is made.

## Pre-acceptance revision-note acknowledgment

Read `BC001_revision_note_v1.md`. It accurately records the notation change, the root-identified capacity wording correction separating the supplied-table and optional explicit-AND implementations, and the zero synthetic state/width-16 clarification. These are reflected in the final proof reviewed above. The note transparently states that no pre-change filesystem snapshot was retained; this review does not manufacture one or claim a bytewise comparison to such a snapshot. Final proof SHA-256 remains `38712b68da30e08d14f41567e84f53b4073b7e2d46280313adc8b69859fc850e`. PASS remains unchanged.
