# Independent finite-horizon manuscript integration review

## Disposition and scope

**PASS for mathematical transcription and integration on the final bytes bound alongside this report.** No mathematical correction is needed. This is a fresh independent LLM integration audit, not formal verification, external peer review, novelty certification, build/visual certification, root acceptance, or publication approval. No external action was performed. Only this review directory was written; accepted v1 and new manuscript sources were not edited by this reviewer.

I read the complete new main text, complete new finite proof, exact v1-to-v2 main diff, accepted FHW001 candidate, its full independent review and acceptance receipt, and the accepted v1 statements/interfaces used by the new derivation. In particular I inspected the finite suffix proposition and proof, finite critical lower statement and its source/certificate and kernel/risk-transfer application, clean oracle-floor proof, and the original width/fixed-fraction consequence proof. This is not a new full re-review of every unchanged internal lemma of v1: their accepted bytes are preserved and verified, and the present task is their exact use in the new finite derivation.

## Provenance and unchanged material

The fresh checker compares bytes, not just rendered similarity: `sections/proofs_positive.tex`, `sections/proofs_negative.tex`, and `references.bib` are identical to accepted v1. The v1 receipt's current artifacts and all historical `verified_at` bindings match. FHW001 receipt artifact hashes all match. Copied candidate, independent review, review bindings, and both acceptance receipts are exact. Both source-binding maps validate. The retained v1-to-v2 diff exactly equals an independently regenerated unified diff. Thus no silent change to the stronger old constants, proof assumptions, prior-work attribution, or bibliography is hidden by the integration.

## Quantifiers, interfaces, and information model

The definition of Γ at fixed `(M,r)` is a supremum over budgets and qualifying experiments for one k-blind map, followed by an infimum over maps. The map may know M, r, and supplied `1/M`, but not hidden source quantities or k. Γ is not sequence C, and the manuscript explicitly distinguishes them. Bounded TV and `g>=M^-1/2` imply every such map has finite factor at most `sqrt(M)`; the contradiction proof does not manipulate an infinite factor. The stationary class is a subclass of all-start experiments for each same map, so the infimum inequality is valid. Neither optimum nor worst-case source is assumed attained.

The same-map clean guarantee is used at k=0 before the attacked comparison. All clean alternatives qualify at exactly the supplied certificate, not necessarily their maximal certificate. The attacked budget in fact depends only on `(M,r)`. No claim that all budgets have logarithmic risk is introduced; the abstract, result discussion, fixed-fraction discussion, appendix, and limitations expressly avoid that mistake.

The loss remains unconditional unsquared TV at the actual protected final pair. There is no independent query replacement. The legal kernel remains a common source-independent map with pointwise edits only in the first M coordinates, endpoint protection on every outcome, identity rejection, and independent predictor randomness. Counts and both boundary windows remain exact; the positive map only needs counts and suffix. Full/overlapping windows are included in the upper, while the chosen lower-domain budgets imply nonoverlap where that proof needs it. The computed-bit corollary retains its distinct full-word-scan access model and fault-free supplemental message; no raw-coordinate/bit equivalence is asserted.

## Full transcription and arithmetic audit

The new appendix reproduces the entire FHW001 proof, rather than citing a receipt as proof. Renaming finite C to Γ avoids colliding with the original sequence definition; renaming the numerical constant to A₀ avoids colliding with the estimator A. No substantive premise is lost.

1. **Upper endpoints:** `m+1=min(r-1,floor(M/2)+1)`. The inequalities `r-1>=r/2` and `floor(M/2)+1>=M/2` yield `M/(m+1)<=max(2M/r,2)<=2(M+2)/r`. Thus `L<=ell+ln 2<=2ell`. The inherited all-start bound `287264 L g<2^19 L g` gives `2^20 ell g` using one map for all k. At r=2 the suffix has zero departures, not one; at r=M+2 the logarithm is one and the upper remains valid.
2. **Small log:** every fixed map has worst stationary clean risk at least `1/(96 sqrt(M))` by the full-history clean oracle floor, hence G≥1/96. This exceeds `2^-30 ell` for ell<64. The endpoint ell=64 goes into the next branch without a gap.
3. **Large log and integer budget:** ell≥64 implies `ln M>=ell-1>=63` using r≥2, so M>2^80. Set `k=ceil(max(128r,M^(3/4)))`. This explicitly guarantees integrality, r≤k/128, and k≥M^(3/4).
4. **Every finite-domain condition:** `M/k²<=M^-1/2<2^-40=A₀c²/2^20`; `ck>2^44>=1024`. The identity `r/M=(1+2/M)e^(1-ell)` bounds r/M by `2e^-63<2^-79`. Since `k<=128r+M^(3/4)+1`, k/M is less than `2^-72+2^-20+2^-80<2^-19<1/8`. Thus k is legal, k≤M/8, A₀t=k/(16M)<1/128<1/4, and the old proposition's entire finite domain holds. In particular r≤M/1024 ensures nonoverlap. No asymptotic invocation is hidden here.
5. **Floor/prefactor:** ck≥1024 gives `floor(ck/4)>=ck/8`, even though ck need not be integral. With Mt=ck, `rho=u₀/(8Mt)>=1/64`.
6. **Same map's clean risk:** S is the supremum over the old proposition's stationary alternatives. Each is covered by this map's factor at k=0, so S≤G/sqrt(M). Under G<2^-30 ell and `(1+x)e^-x/4<=4` for x≥0, `S<2^-28 M^-1/4<=2^-21 M^-1/4<=t/32`. The derivative maximum is correctly at x=3; the final inequality uses c/32=2^-21 and k≥M^(3/4). This is a finite estimate, not S=o(t).
7. **Logarithm and ceiling:** 4A₀c=1/4 gives `L_-=ln(4M/k)`. For x=max(128r,M^(3/4))≥1, ceil(x)≤2x, so `L_->=min(ln(M/(64r)),ln(2M^(1/4)))`. The first equals `ell-1-ln(1+2/M)-ln64>=ell-8>=ell/8`; the second is at least `(ell-1)/4>=ell/8`. Both bounds apply simultaneously, including at the budget branch crossing.
8. **Nonnegative bracket and normalization:** the inherited common-kernel lower is `R_null>=rho[(t/16-S)L_-]_+`. S<t/32 and the positive logarithm justify removing the positive part in the indicated direction. Since k≥sqrt(M), g(k)=k/M. The final coefficient is `c/(64·32·8)=2^-30`. This contradicts the hypothesized factor for each map separately. Taking the infimum therefore needs no attained optimum.

## Sequence consequences and stronger fixed-fraction bound

Positive liminf of r_M/M bounds ell_M eventually; the explicit suffix maps furnish one family, and any finite prefix of horizons costs only a finite constant. Zero liminf gives a subsequence with ell_M→∞, and the per-horizon lower rules out every uniform-factor family. No unjustified interchange of infimum, supremum, and limit is needed.

For fixed alpha, the finite theorem supplies logarithmic order, not the stronger original lower constant by itself. The original `2^-26 ln(1/(32alpha))` statement, `alpha<=1/4096`, and `2^19(1+ln(2/alpha))` upper are preserved exactly. Its original proof still sends M to infinity with alpha and a proposed factor fixed. The new appendix explicitly attributes the stronger constant to that separate argument. The finite result, by contrast, requires no limit in either parameter.

The interpretations for linear widths, r=2, and `max(2,ceil(M^gamma))` with fixed 0<gamma<1 follow at order level within the legal integer range. No sharp constants, practically meaningful threshold, new certificate regime, architectural advantage, or novelty certification is asserted.

## Independent diagnostic evidence and limits

`checks.py` is fresh for this integration review. It checks the upper comparison with exact rationals for all 129,761 legal pairs with 64≤M≤512. It checks 84 large-log cases near powers of two through exponent 2048, near the budget branch and ell=64 threshold. Ceil(M^(3/4)) is computed as an exact integer fourth root of M³; domain and prefactor inequalities are exact rational comparisons. Transcendental checks use 100-digit Decimal arithmetic. All pass. These are diagnostics, not interval-certified exhaustive proof; the universal analytic audit above is the basis of the disposition.

Build success, resolved references, pagination, and page-by-page visual review are explicitly outside this mathematical acceptance. The manuscript should retain a separate build/visual record and receive a root decision on the exact final bytes. There is no blocker or denied action within this local review scope.

## Final editorial rebind

After the initial reading, I read both exact editorial diffs and changed contexts. The main date now neutrally identifies a local research draft; the fixed-fraction discussion now correctly states that the finite characterization requires no limit in either parameter. These are the only main-text changes since the initial reading. The separate proof changed only six `\paragraph` heading commands to `\noindent\textbf`, for the author's reported amsthm run-in build conflict. A mechanical whole-file replacement check confirms no mathematical content changed. Both saved editorial diffs independently regenerate exactly, and the full v1-to-final diff also regenerates exactly. I reran all fresh diagnostics against these final bytes.

Final main SHA-256: `e53c4a93a09fb9629157072b77d87d373f8f3aba8929c9fce81c9d8f0f974b06`. Final finite-proof SHA-256: `5ce65ec56017f2581e06681bb90848afc0a8987c44022663b4866667f84e3639`. Any later substantive source change requires a new review/rebind; build artifacts are not included in this mathematical disposition.
