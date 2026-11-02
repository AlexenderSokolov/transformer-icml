# RE001 handoff — source edits + robust deep encoding

## Useful result

The complete candidate covers **all fixed K>=2, every beta, stationary and arbitrary starts**. A paid compander/no-plateau packed encoder of the **corrupted word only**, with a genuine noisy quantized information cut, satisfies

    risk <= C_K min(1, s + epsilon
                          + f_e(k/M + epsilon^2 + epsilon/chi)).

Here s=M^-1/2, e=max(beta,1/M) for K>=3, e=max(sqrt(beta),1/M) for K=2, and f_e(v)=v[1+ln(1+1/(Mev))], f_e(0)=0. A minimum outside/inside the fixed C_K is equivalent up to constants; the theorem gives min{1,C_K[...]} exactly.

At epsilon=O(s), chi≈log M, this reaches the full-corrupted-history source-edit profile. **Deep re-encoding can remove the fixed-uniform-bank precision penalty, but cannot undo source erasure.** Optimality is only the statistical/source term at the sufficient schedule; no global encoder/noise/capacity/depth minimax frontier is claimed.

## New proof steps

1. The edited histogram and clean histogram differ in l1 by at most 6k/M. Symmetric compander inversion plus Cauchy--Schwarz gives the selected-row error

       Delta <=4epsilon sqrt(Kr)+12k/M+8Kepsilon²+2Kepsilon/chi.

   The cross term epsilon sqrt(k/M) is absorbed, not left as a spurious statistical floor.
2. K>=3: ordinary reconstructed-frequency add-one is k- and beta-blind. JP001's accepted continuous-real-budget occupation bound, not just the integer-k headline, gives the mixing-aware f_e term.
3. K=2: observed-row radius Bhat=12epsilon·Sroot(rhat)+68tau, tau=k/M+epsilon²+epsilon/chi, satisfies Delta<=Bhat<=18epsilon sqrt(r)+132tau. A fixed-orientation subtract/inflate rule preserves true-q weighted occupation. The O(epsilon) square-root occupation term is split off before applying the binary sqrt(beta) lemma. Public k is used; beta is not.
4. General finite scale: u=rho+2/Q with delta<=rho<=2(delta+1/Q). Scalar epsilon=2u or no-plateau N with 4R uN<=1 and epsilon=8R u/N^(R-1). For rational target t0, u^R<=t0/(8R)^(R-1) is sufficient, with depth O_R(1+L+log_+(u/t0)).
5. Exact PRE-FAULT lattice clipping is mandatory and counted before P>=4h+c_FA(d+2). Full rational certificates, root computation, bank conversion/coexistence, dense slots, decoder enumeration, clearing and PURE-vs-primitive depth are paid separately.

## Evidence

- `RE001_theorem.md`: full proof, exact model, finite scales, paid ledger and limitations.
- `RESC_binary_lemma.md`: independently authored subtask lemma (not an independent review), with explicit binary constants 2^18,2^10,2^24.
- `RE001_diagnostics.py/json`: exact rational author tests: 10,657 all-word edit pairs; 420 actual finite compander/snake frequency evaluations; 6,951 noisy reconstructions; 192 corrupted-word pipeline row tests including six clean-empty/false-mass instances; 14,565 scale certificates; 28 explicit pre-fault clips. Radicals are checked by exact squaring. This is a finite terminal arithmetic slice, not an emitted full dense-network/resource audit or proof.
- `check_resc_binary_lemma.py` / `RESC_binary_lemma_diagnostics.json`: auxiliary 27,252 binary reconstructions across 1,204 clean/edited word pairs. Core rational confidence/envelope checks are exact; some auxiliary radical checks use floating tolerance. Do not describe this entire auxiliary script as exact. The main diagnostic supplies exact radical checks.
- `RE001_source_bindings.json` / `RE001_dependency_receipt_check.json`: 37 bound dependency/companion files and 11 accepted proof components exactly match their receipts.
- Fresh full independent review: **PASS** after charging arbitrary full target-description length b_t0. `RE001_independent_review.md` audits the entire proof/implementation; `RE001_independent_checks.py/json` independently passes 10,737 reconstructed-row checks, 10,575 binary pathwise checks, 3,160 noisy geometry checks, 30,716 finite-scale schedules, 5,048 exact clips and dependency hashes. `RE001_independent_review_bindings.json` binds final theorem `0cbe7c7a45b2efe6d73ba1a8e55b96d0a6d9f6bc8aa9b74a122960272944ce73`. Root acceptance remains separate.

## Scientific boundaries

The final pair remains protected and the target is the true actual terminal row. The encoder never sees clean symbols. No edit/noise seed or mask survives. No historical array, initial boundary, count, exact row mass, hidden rail or timing port reaches decoding. Rational outputs are not silently rounded back to Q. Public rho uses full numerator/denominator bitlength, not compact exponent coding. The binary rule is not unknown-budget adaptive. The general source lower transfers through zero noise; JP001's representation-specific precision lower does not transfer to a redesigned encoder. Fixed R-fold cut width expansion and paid decoding accompany depth, so this is not a depth-only equal-coordinate-count comparison.

Nothing frozen was edited. No publication or external contact occurred.
