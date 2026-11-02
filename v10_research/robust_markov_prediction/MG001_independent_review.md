# MG001 independent mathematical review

2026-11-02. Verdict: **PASS for the stated fixed-K,R general-Markov robust upper and named precision-schedule depth comparison**, subject to root acceptance/source binding. This is an independent LLM mathematical review with finite exact diagnostics, not formal verification, emitted-network testing, external peer review, or novelty certification.

Reviewed theorem SHA-256: `c4f114bb7510f3dd5ead7461d9ebead092e2abe103fc92f96e3af9fbd4ac6623`.

The reviewer did not edit the theorem. Read the full theorem, GD001 upper/compander and uniform-FA extension, FA001 finite arithmetic definitions and bootstrap, RG001 explicit formula/geometry/decoder, their acceptance receipts, GW001 unconditional occupation derivation and R011 original-risk interface. GD001 receipt binds its upper to `5959d2c6f60c1374f9c2702fcf58a9bd5cc1245313e59c0fe95ad635e9e8e50a` and FA extension to `505be0ffc2f7499581cac5ba9da7c018b6f04cb10dc21bce9d3ab7cdba3f5c7e`; RG001 receipt binds its theorem to `fc563812489ea4deba9bbc00e072119f2e26d23f3b6bcab56c40cb5dabd74949`. Historical candidate headers do not override those later root receipts.

## Audit findings

1. **The statistical object is genuinely general Markov.** Each selected triple frequency is the count of a departure before the actual random terminal pair, divided by M. The terminal pair is not replaced by a predetermined row. Arbitrary initialization is retained, and no stationary law or conditional successor independence is used. The full K^3 bank contains every row before selection. Local radius-three features and causal prefix pooling are enough; no final counts are copied backward in time. Sparse singleton preprocessing is distinguished from positive-density statistical attention.

2. **The ideal composition is in the uniform finite family.** The compander and RG snake use bounded affine/ReLU primitives with paid dyadic descriptions. RG's inverse connector lengths are rational decoder data, not unbounded network coefficients. Saturated repeated doubling replaces large amplification coefficients. Concatenating the two bounded-stage families keeps all per-stage bounds fixed in M,Q,L. GD001's growing-depth FA recurrence therefore applies to the whole composition with one global P, rather than incorrectly applying RG's exact-mean lattice certificate after a different nonlinear preprocessing. Increasing P to cover coefficient exponents is harmless. The full-product/single-floor semantics, neighborhood bootstrap, dense zero slots and conversion descriptions are explicitly inherited and paid.

3. **The noise constants are correct.** Complete finite encoder error contributes 1/Q, attack contributes c/Q, and final downward flooring contributes less than 1/Q. Clipping is nonexpansive relative to the ideal [0,1] curve. Thus the Euclidean distance is bounded by sqrt(R)(c+2)/Q. RG's local inverse is a geometric fact for arbitrary scalar inputs and arbitrary nearby observed points, not merely for means on a special lattice. The theorem correctly invokes that fact with effective noise c+1. Its strict locality hypothesis follows from the chosen a. Multiplication by 2 after decoding gives epsilon=2B/Q^R; subsequent clipping cannot increase the g-space error.

4. **Symmetric inversion repairs the crucial one-sided gap.** For upward error e, the compander inverse inequality gives e <=2sqrt(x)epsilon+2sqrt(e)epsilon+epsilon/chi. Young's inequality with e/2+2epsilon^2 gives the claimed bound. Downward error has an even smaller bound. Endpoints, x=0 and L=0 are included. In particular the proof neither preserves nor assumes zero purity after robust decoding, and retains both leakage terms.

5. **Reconstructed add-one is a legitimate labels-only decoder.** For positive masses A,B, splitting through v/A yields TV(u/A,v/B)<=(||u-v||_1+|A-B|)/(2A)<=||u-v||_1/A. Adding public 1/M to reconstructed nonnegative frequencies makes the denominator positive even if J=0. The true denominator r+K/M is used only in analysis, never supplied to the decoder. Cauchy–Schwarz gives 4epsilon sqrt(Kr)+K delta. The passage sqrt(J)/(J+K)<=1/sqrt(J+K) and min(1,A+B)<=A+min(1,B) proves (III) with the stated constants.

6. **Occupation and risk assembly are valid without mixing.** The d_state^2 occupation argument correctly combines suffix domination, maximal starting-state probabilities, and the pathwise first-w-visit count. Integer threshold rounding is valid because K>=1. The layer-cake integral gives 2K^2/sqrt(M+1), hence the leading approximation term 8K^(5/2)epsilon. The residual argument is K^5 M delta/(M+1), safely enlarged to K^5 delta. R011's ORIGINAL upper then adds by triangle inequality. The operating-point Psi estimates are correct: concavity with zero origin yields subadditivity, and chi>=bitlength(M+1) absorbs the logarithm in the linear-leakage contribution. No IID-only upper has been transferred by source-class inclusion.

7. **The interface change is essential and explicit.** The final vector is exact rational, not forced to the coarse Q simplex. All component denominators, their finite products at fixed K,R, normalization and output serialization are charged. The decoder is finite and receives no work arrays/counts. The segment search is polynomial in Q, not falsely logarithmic. Rational bit lengths are O_(K,R)(h+L+log M), with the K dependence honestly inside the constant. A separate fine output rounding could be added with a separate error term but is not needed here.

8. **Resource and lower scopes do not overclaim.** Generic work word w, original description length Bp, and decoder word b are distinct. Mask/parameter storage is total across depth, not only rolling activations; all-token decoding is conservatively paid. Full products, dense zeros, input copies, setup/generation, boundary data and cut isolation are included. The tape and PURE alternatives do not assert the small primitive depth as bit-machine depth. The universal alphabet lower uses D=RK^3, not R. The stronger sufficient Q^R threshold is not called necessary. IR001 is invoked only within the common bounded influence/finite approximation/fixed-position boundary family and only establishes the stated Omega(log M) at Q=Theta(M^(1/(2R))). Its IID stationary initial law is a valid witness inside arbitrary-initialization minimax.

## Exact executable diagnostics

`MG001_independent_checks.py` and its JSON output use Python Fraction arithmetic. All passed:

- 19,305 symmetric inverse cases, with square-rational true x so every occurrence of sqrt(x) is exact, L=0,...,8, both error signs, endpoints and many breakpoint values; exact inverse round trips also checked.
- 2,106 normalization cases for K=2,3 and M=1,7,64, including empty true rows and positive false reconstructed mass.
- 20,480 occupation inequalities. Short histories are exhaustively enumerated for all deterministic binary second-order tables and three genuinely row-dependent stochastic tables, all four deterministic initial pairs. Since short-history UC bounds can be vacuous, separate exact dynamic programming checks stochastic tables at M=17,32,64 and deterministic paths through M=129 in the nontrivial domain. These count departures before time M separately for each possible terminal state.

These are finite support checks of local claims, not a verification of the full generic finite evaluator or an asymptotic proof. The analytic arguments above remain necessary.

## Nonblocking clarity note and acceptance boundary

The author added the explicit beta-dependent Hstat formula and beta=0 fallback during review. This clarification was reread and agrees with R011; the current hash above binds the clarified theorem. No scientific change was needed.

No blocking gap was found. Acceptance does not extend to pending/independent GN partial-capacity results, a sharp K-dependent rate, a universal Q/depth frontier, coarse-Q final probability outputs, internal faults, training reachability, efficient decoding, or unbounded-family Transformer lower bounds.

## Delta review: dense-family local preprocessing and word-bank handoff

The prior reviewed theorem and report are preserved in `preclarification/`. Root requested explicit selection of the paid radius-three local TABLE as the actual dense-family front end, with singleton-head copying relegated to a separate alternative. The amended §2 makes that choice and obtains boundary symbols by a paid fixed-position scan. This matches FA001/CA/IR local-input assumptions without claiming a sparse head has dense-mask membership. The terminal statistical histogram still pools only observed triple positions.

The amended §6 separately pays every old O(w)-bit word read and new O(b)-bit label write, including O(nK^3 R(w+b)) in T0. Both old and new banks coexist in the nK^3w+nK^3b storage terms, with R fixed, until paid clearing/isolation. Thus taking P larger than necessary cannot leave an uncharged wide-to-narrow conversion. These are scope/accounting clarifications; the mathematical risk proof is unchanged. Exact diagnostics were rerun and rebound to the new theorem hash printed above. **Delta verdict: PASS; no remaining condition.**
