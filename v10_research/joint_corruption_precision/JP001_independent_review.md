# JP001 independent full review

2026-11-02. Independent LLM review, not author self-review, formal verification, external peer review or root acceptance. Reviewed the entire JP001 theorem, exact experiment, proof, finite implementation ledger, and limitations. Final exact SHA-256 binding is in `JP001_independent_checks.json`; root acceptance must bind that version.

## Verdict

**PASS after one resource-encoding clarification.** The claimed fixed-prefix both-initialization minimax profile follows from the accepted ingredients and the new exact cut/coarsening arguments. No remaining mathematical or interface defect found. Constants are deliberately loose; no growing-K claim is warranted. The theorem uses one-shot coordinatewise vector noise (an l-infinity ball), not one-scalar sparsity.

## Resolved finding (preserved)

The original resource sentence used “full certificate bitlength” without fixing rational versus compact dyadic-exponent encoding. If rho=2^(-2^b) is given by a b-bit exponent, exact pseudo-count arithmetic can need exponentially longer denominators than the claimed word bound. I reported this to the author. The current text explicitly defines b_rho as full binary numerator AND denominator lengths, not compact exponent coding. Under that explicit encoding, the fixed-number cross products, common denominators and rational output fit O_K(P+h+ell+b_rho) bits and the stated school-arithmetic bound. This correction is necessary for the resource certificate, although it never threatened the information-theoretic risk result.

## Full proof audit

1. **Experiment/quantifiers.** Sources satisfy the same all-pair-state minorization as accepted SC002/SC003/BT002/BIF, including unsupported starts. Stationary certificates are hidden. Protected terminal pair makes row selection identical before/after corruption. Public budget/certificate/P metadata are source-independent constants across the priors and do not supply source information. General cooperating/history-adaptive kernels cause no problem for a pathwise upper. The lower uses separate source-independent kernels for separate witness inequalities, combined only by maximum.

2. **Finite uniform prefix.** BC001 §5 and FA001 §§2–4 provide the relevant exact arithmetic, not just an approximation theorem. Zero scores produce a common positive Taylor integer; exact bit values and full-width sums cancel it before the only quotient. Integer affine copies are exact. Therefore a=floor(D C'/M)/D for every integer P>=h, even below FA001's general approximation precision schedule. Radius-three local tables, public causal masks, terminal-only two-symbol port and nonuse of earlier boundary ports are legal. Count-M maps to one, count-zero to zero.

3. **Pathwise discrepancy.** One edited symbol affects at most three triples; changing one triple changes the full histogram l1 norm by at most two, so 6k is valid even for adjacent edits. Clipping is nonexpansive around the true corrupted frequency. Adding finite-floor, port-noise and final-floor deviations gives rho+2/Q per coordinate, hence B=6k+KM(rho+2/Q). The certificate implies B<=b_K M tau, with b_K=6+4K. This deliberately overcharges rather than loses dependence on a budget.

4. **K>=3 upper.** Normalization stability applies to nonnegative rational pseudo-counts, and clean add-one has the accepted all-start R011 bound inherited in SC002. I checked IU001 Lemma 4.1 permits every real A>0; AU001 §§2–4 permits the same A in the complete ordinary-P suffix mixture. JP001's continuous-A scalar completion gives its stated L_K without extrapolating an integer-k statement. x>=1 is handled by the unit cap, beta=0 by universal occupation, beta>=1/M by residual occupation rather than an additive burn term.

5. **Binary upper.** SC003's pessimistic orientation is the complement of the first pair bit, independent of theta. Its algebra extends to arbitrary nonnegative real pseudo-counts with l1 radius B. The J=0 branch is valid because n=0 and A>=2. I independently checked the envelope with rational data. The comparator coefficient 8193 sqrt32 agrees with SC003 §3, not BIF's looser B0 alternative. BIF §3 equation (3.4) holds for every real A>0 at full support and beta>=M^-2; the q_A=b,q_B=e orientation is preserved. BAI003 v2 §6 equation (6.2) gives the singleton-support term, bounded by 264A/M for A>=2. Universal occupation covers weak beta and arbitrary unsupported starts. No purity assumption is transferred through corruption. The additional 2/M contribution is absorbed in 8s; direct integration gives the claimed inequality. The explicit C_K comfortably dominates both coefficients.

6. **Source-edit lower.** Full corrupted history can simulate this finite bank when port noise is zero, so arbitrary-decoder lower bounds transfer in the correct information direction. BT002 gives its uncapped max directly. Although SC002's headline is capped, its §6 explicitly establishes the stronger uncapped 2^-15 max(s,F) used here; this is not an unjustified inversion of the headline. Public fixed budget metadata cannot defeat these arbitrary-decoder results.

7. **Noiseless precision lower.** This is NOT a direct FR001/SRC-bank identification. The author correctly uses the BF001 family lower for K>=3 and BS001 at kappa=1 for K=2. The exact uniform histogram is a member of those larger families. For K=3, the one required extra coordinate is constant zero. Exact first/last-three symbols granted by those families only strengthen the decoder relative to JP001's terminal pair. Thus family minimax lower <= each member's minimax <= the corresponding smaller-port risk, giving the required direction. Accepted lower constants are independent of P, k, delta and fixed certificate metadata.

8. **Noise lower / fine-grid refinement.** If delta>=1/Q, the chosen dyadic Q_c lies between 16 and Q and divides D and Q. Nested flooring is an exact integer identity. The simple coarsening attack is already legal for real and D-grid perturbations. The stronger fine-Q-grid version is also correct: with b=floor(Qa)/Q and c=floor(Q_c a)/Q_c, choose eta=c-b. Then eta is a multiple of 1/Q, |eta|<1/Q_c<=delta, and a+eta=c+(a-b), where 0<=a-b<1/Q. It stays in the cube (c=1 only at a=1), and the final floor returns c. The attack reads only a and public scales. Thus the same lower even holds with Q-grid-restricted shifts. For delta<=1/16 the coarsened scale loses at most factor two; for larger delta up to 1/4 it loses at most four. For delta<1/Q the quantization witness dominates. No precision/source asymptotic domain is omitted.

9. **Scalar assembly.** The given derivatives of f are correct. Increasing concavity with f(0)=0 gives subadditivity and f(cx)<=cf(x). Three separate floors thus dominate f(k/M+delta+1/Q) within factor three, without adding incompatible witness risks. Combining constants gives c_K as claimed; the final cap is harmless. Stationary subclass inclusion has the right direction under identical cut and attack contracts.

10. **Costs and exclusions.** The ledger pays all-token local features, dense zero Q/K slots, masks, Taylor arithmetic, accumulator guards, sequential tape movement, descriptions, parameter conversion and simultaneous storage. The exact reliable rational decoder is not allowed to reread hidden counts/history. The revised certificate encoding avoids a hidden real oracle or exponent blowup. The reliable computation cost does not claim to construct the physical perturbation/isolation device. Optional output rounding is explicitly separate and its K/Q loss is dominated. Fixed-depth attention is not conflated with its PURE bit expansion. No training, redesign-universal, single-coordinate-noise, edited-terminal or unknown-budget adaptation claim follows.

## Independent diagnostic evidence

`JP001_independent_checks.py` was written and run independently of the author's diagnostics. It checks:

- 155,176 exact finite nested-floor/coarsening configurations, including the fine-Q-grid-shift construction;
- 35,000 exact rational binary lower-envelope cases;
- 9,000 exact rational normalized add-one stability cases;
- all 16,384 pairs of length-eight binary words sharing the protected final pair (M=6) for histogram edit sensitivity; this is an algebra diagnostic only, not a risk-domain test;
- 30,000 floating scalar/profile cases as corroboration only;
- exact SHA-256 matches for nine accepted direct dependency proof files and their receipts.

All passed. Finite checks are not the universal proof; the analytic audit above supplies the proof-interface assessment. There were no suppressed failed numerical cases. The only reviewer-requested change was the rational-input encoding clarification preserved above.
