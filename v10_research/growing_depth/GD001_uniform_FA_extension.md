# GD001 uniform growing-depth FA extension

2026-11-02. New explicit extension; it does not change accepted FA001 v3.

## Uniform family and approximation theorem

Fix all per-layer FA001 affine/ReLU dimensions, fan-ins, head counts, primitive DAG sizes, coefficient/operator bounds, ideal reachable-state bound, local radius, boundary-branch count and mask-density constant. Only the integer number d>=1 of these bounded stages may grow. Public finite dyadic descriptions are paid and can vary by layer/position. Output dimension and readout primitive budget remain fixed. Every frozen branch obeys the ideal range contract on every formal history. Attention-free bounded affine/ReLU stages are allowed, or represented using paid zero-output attention heads.

FA001 §§2–5 give, from these FIXED PER-LAYER bounds alone, computable rational constants α,β>=0 independent of d,M,h, such that its very same signed integer Taylor/affine evaluator satisfies

 δ_(i+1)<=α δ_i+β(P+1)2^-P, whenever δ_i<=1,
 δ_0<=2^-P.

The logit neighborhood integer shift and Taylor constant j0 are uniform because all per-layer primitive bounds and state ranges are uniform. No constant is computed by treating the entire d-layer DAG as one fixed architecture. Increase α,β to cover the fixed readout as one extra stage. Choose an integer A>=max(2,α+β+1). Induction on the scalar recurrence C_0=1, C_(i+1)=αC_i+β gives C_i<=A^i, so every intermediate discrepancy and readout error are bounded by A^(d+2)(P+1)2^-P, provided the neighborhood bootstrap holds.

Choose a single integer c>=4, by finite search from A, such that

 A(c+5)2^(1-c)<=1.

Put t=d+2 and P=4h+ct. Then

 A^t(P+1)2^(-P+h)
 <= A^t(ct+5)2^-ct
 <= (c+5)[A2^(1-c)]^t <=1.

The first inequality uses (4h+ct+1)2^-3h<=ct+5; the second uses ct+5<=(c+5)t<=(c+5)2^t for integer t>=1. Hence every error <=2^-h<=1, which closes the neighborhood induction rather than assuming it. The final pre-cut error is <=1/Q, uniformly over d and all formal histories. Consequently the lower note's E=1 tube applies to the actual finite FA evaluator with growing d. Output floor-label equality is neither needed nor claimed.

This is an explicit sufficient P=4h+O(d+1), not a minimal precision theorem. Parameter conversion still pays its true supplied description length. For the compander d=O(L+1), P>=L+2 and all powers 2^-j and quarter biases are represented exactly. Increasing P to max of this formula and h+L+4 preserves the theorem (the function (P+1)2^-P decreases for integer P>=1).

## Inclusion of the compander in this finite family

Use exact local one-hot triple tables and uniform zero logits. FA's Taylor routine gives identical positive weights at all allowed edges. Exact accumulated ratios therefore return exactly the downward fine histogram floor(D_f A/m)/D_f; the common integer weight cancels, including short rows. Preserve u,v on positive rails. Implement ReLU(u-.25), multiplication by 2^-j with downward output floor, addition of v, and integer T=min(1,4u) by its affine/ReLU expression, retaining old u until updates finish. All affine operations defining T are exact on the fine lattice; dyadic products in v and final 2^-L u are the only new rounding losses. Paid unused heads have zero values, hence exactly zero outputs regardless of their identical positive Taylor weights.

The final /2, if evaluated by FA's separate affine floor rather than exact rational cut formation, introduces at most 1/D_f additional error in g_L/2-space. Therefore in g_L-space

 0<=g_L(x)-2F_fin(x)<=(κ+L+3)/D_f<=5κ/D_f.

With P>=h+L+4, subsequent Q-floor gives total loss <(2+5/16)/Q<3/Q. Thus the sharper one-sided deterministic U5, zero purity, and risk U1 hold for this SAME generic FA evaluator, not only the bespoke minimal-P arithmetic schedule. No fresh positive offset enters zero-valued rails. All coefficients are finite dyadic and ideal/rounded zero coordinates remain exactly zero. The upper is therefore included in the growing-depth finite comparison family after its declared extra work precision and stage counts are paid.

## Fully paid generalized FA ledger

Let U be the total supplied scalar-record count across ALL d stages/branches/local tables/edge biases; F the total public mask/metadata bits across all stages; Bp the maximum supplied description bitlength. Neither U nor F is treated as depth-independent. Use the explicitly ordered sequential public-data layout of FA001 §6.1; its rewinds and reads occur at every stage and are paid. The online guarded word length can be taken

 w=O_fixed(P+log(n+1)+log(d+1)+log(P+1)+log(U+F+2)),

with fixed constants determined only by the uniform per-layer bounds. Original-description conversion scratch uses O(Bp+P) separately. The extra log(d+1) covers layer counters and parameter addresses; no L-dependent constant is suppressed.

Supplied-data acquisition costs UBp+F actual bits, conversion costs O(U(Bp+P)^2), converted compact records use O(UP) bits, and fixed arithmetic microcode uses a conservative O(w^4) bits/work as in FA001. A known explicit table generator, if used, must have its own actual time, program and peak scratch added; arbitrary tables are not generated for free.

Online sequential bitwork is

 O_fixed(d n²(P+1)w² + (U+F)w + w^4).

The first term pays every head/edge/Taylor step, all affine/ReLU stages, row division, copy/zero, local input acquisition and tape rewinds; the second safely covers sequential reads and conversion-to-working-slot copies for the total supplied layout. One can roll hidden arrays in O_fixed(nw) numerical bits, since d stage outputs are not all retained. A safe phase-sum peak is

 O_fixed(UBp+UP+F+n+nw+w^4+Bp+P).

This includes the actual total parameter/mask storage, not merely rolling activations. Offline known-generator work and phase scratch are added when present. Terminal isolation disables all noncut source-dependent arrays and charges zeroing if chosen. The compander's extra decoder inverse/normalization and local preprocessor costs are the upper note's ledger and must be ADDED, not replaced by this encoder-only ledger. Its explicit breakpoint generator is polynomial in L and fully paid there.

A separate PURE Boolean/ReLU compilation of the actual bit operations has depth O(T), width O(S) and O(TS) held/live gate records, or O(TS²) dense slots, with all coefficient/address bits and phase sums charged. It is NOT a fixed-width O(loglog M)-depth PURE theorem. The meaningful optimal depth-order assertion compares bounded-primitive attention/affine stages, with growing precision and paid finite evaluation, not bit-gadget depth.
