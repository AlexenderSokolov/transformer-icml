# NP001 independent adversarial review

2026-11-02. **PASS — no outstanding mathematical or interface blocker found.** Independent LLM review and exact finite diagnostics, not external peer review, formal verification, emitted-network validation or novelty certification.

## Reviewed material

Read the entire NP001 theorem, the complete IR001 theorem, GN001 theorem and GN001 independent review. Inspected root acceptance receipts for GN001, IR001, IC001, RG001 and RP001. The substantive new proof obligations here are the independent-amplitude common attack, its IR oracle, uniform constants, public scale selection, and compatibility with the inherited finite implementation. The accepted GN geometry and rational FA/GD extension remain dependencies rather than newly certified foundational results.

## Adversarial checks and findings

1. **The noise channel is explicitly the one needed.** Real perturbations occur after the finite precut computation and before clipping/Q-flooring. The coarse map Aδ(a)=δ floor(a/δ) stays in [0,1] and moves down by strictly less than δ for every a, including endpoints. It is source-parameter-independent and shared by all histories; the proof does not exploit illegal p-dependent channels. Non-dyadic δ need not map to the evaluator's fine grid, but real attack values are explicitly permitted. No old post-grid or fine-grid-restricted lower is claimed.

2. **Capacity lower is valid.** Zero attack gives H(Q+1)^J possible observations conditional on public seeds. Coarse attack gives at most H(floor(1/δ)+1)^J; final flooring can only merge labels. The uniform-prior interval-covering argument fixes independent encoder/decoder seeds and then averages, so an uncountable public seed does not become a hidden source port. Since Q>=2 and δ<=1/4, the common constant 1/[16H(3/2)^J] safely yields c_cap max(Q^-J,δ^J)=c_cap τ^J. δ=0 is treated without division by zero.

3. **The depth lower applies IR to the correct bank.** When δ>=1/Q, granting k=floor(a/δ) is more informative than the actually attacked label, which is a deterministic function floor(Qδk)/Q. With Q'=1/δ>=4, IR001 expressly allows real Q'>=1. Its original ideal f and actual a satisfy the fixed-error tube E/Q<=E/Q', and their influence/branch contracts are unchanged. This proves γδ/C^d. There is no attempt to make the discontinuous attacked map itself an ideal Lipschitz network. At δ<=1/Q, zero attack gives γ/(QC^d); equality is harmless. The oracle's exact real simulation is legitimate in a lower-bound comparison, not an uncharged finite upper algorithm.

4. **Statistical witnesses and boundary scope are correctly separated.** Fixed (0,0) initialization supplies the M-bit statistical test; stationary Bernoulli(p) product initialization supplies the M+2 IID history required literally by IR. Both lie inside the arbitrary-initialization minimax class, so the maximum of the bounds is legitimate despite different witnesses. Only public-position source bits are retained as side information, not arbitrary nonlocal statistics. Frozen-branch formal histories and source-independent synthetic initialization are retained.

5. **Uniform upper constants are rederived, not hidden in c.** The GN curve's coefficient/state/width bounds have no noise parameter. Its fixed-stage evaluator continues to give error 1/Q. Coordinate error is at most δ+2/Q<=3τ, and the nearest projected curve point is within 6sqrt(J)τ of the true curve point. D>=12sqrt(J) and N<=1/(Dt) make this <=1/(2N), strictly inside GN's inverse scale. Consequently the stated K=6sqrt(2J) is safe. The no-plateau inverse is essential and correctly imported; no old N^-J additive term has been silently discarded. Pointwise recovery handles arbitrary histories and randomized/adaptive attacks before expectation is taken.

6. **Scale promise is a finite input, not a real oracle.** τ<=2^-m<2τ exists with 1<=m<=h, including τ=1/2 and exact dyadic τ. The construction only reads m and h. For arbitrary real δ the theorem honestly requires this public certificate; rational δ may instead be read with its description length and compared exactly. Such metadata depends on the budget, not p/history. Public δ can separately be granted for the lower oracle without enlarging constructive access.

7. **Selectors and endpoint cases are sound.** Full packing takes the largest dyadic N<=1/(Dt) when Dt<=1/2; if no N>=2 exists, scalar fallback plus τ>1/(4D) proves the same O_J(τ^J) risk with a larger J-only constant. Statistical sufficiency uses κ_J=2^J(2D)^(J-1), hence t^-J>(2D)^(J-1)sqrt(M). The least dyadic N above (t sqrt(M))^(1/(J-1)) is then admissible. Scalar selection handles t sqrt(M)<=1. Squared exact comparisons avoid a numerical square-root assumption. The necessary inequalities follow directly from the lower; no same-constant iff or matching exponential base is asserted.

8. **Finite implementation and resource ledger remain coherent.** Coefficients of the shifted snake are rational; signed quotient conversion is explicitly paid and the accepted GN rational extension is used rather than declaring lattice exactness. Stage constants and c_FA do not depend on δ,Q,N. The error includes initial causal mean computation and all subsequent rounding, so no second mean-rounding term is missing. Rational decoder output is allowed off the transmitted Q-grid. Edge enumeration, rational projection/comparison/inverse and O_J(N^(J-1)) storage/work are charged. The new Lnoise term and w^4 slack cover reading the scale/rational budget and exact selection; h<=w and log M<=w make the conservative comparison count fit. Compact streaming records avoid an uncharged padded generator array. Primitive depth is explicitly distinguished from much larger paid bit-machine/PURE depth. This review does not claim a freshly emitted end-to-end FA implementation was executed.

9. **Consistency interpretation is appropriately narrow.** For fixed δ>0 and fixed J, the positive δ^J floor forbids consistency even as Q,d increase. Necessity of δ->0 and Q->infinity at fixed J follows. Growing exposed dimension is only identified as a possible escape outside the uniform fixed-J theorem, not proved sufficient. The upper remains IID-only; no Markov sufficiency or novelty claim is inferred.

## Independent executed diagnostics

`NP001_independent_checks.py` was written independently during review with Python Fraction arithmetic and without importing author diagnostic routines. It passed:

- 21,450 common coarse-attack legality and coarse-oracle/Q-floor simulation checks, including non-dyadic rational δ and endpoints;
- 5,532 scale/selector resource cases, including 866 admitted statistical snake selections and 2,464 statistical scalar selections, using exact squared inequalities;
- 16,640 noisy rational nearest-edge decodes for independent recursive edge/time tables, with coordinate tube error ±1/Q, attack extrema, clipping, Q-flooring, endpoint/vertex samples and squared recovery-bound checks.

These finite checks corroborate selected claims but do not prove arbitrary-real universality, audit the full FA evaluator or replace the symbolic proof.

Final reviewed theorem SHA-256: `79cae4ebb56694452d63ccb2f6ac1f2d89516e9812c68bba700341ea600e9f54`. The attribution-only addition was reinspected; it makes no mathematical-dependency or novelty claim and does not change the verdict. Independent diagnostics were rerun against this final hash. Any later substantive amendment requires reinspection.
