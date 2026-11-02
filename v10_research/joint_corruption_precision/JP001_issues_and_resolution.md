# JP001 issues and resolutions

Post-stage8; accepted and frozen sources untouched.

1. **Noise ambiguity.** The theorem requires one-shot vector l-infinity noise (every coordinate may shift), not a single sparse scalar fault. Complete-bank coarsening needs the former. The latter problem remains outside this result.
2. **Different historical cuts.** FR001's original 9K+1 bank is not this complete K^3 histogram. Lower transfer uses BF001/BS001 family inclusions; K=3 needs mathematical zero-padding from 27 to 28 coordinates in BF's family. No physical extra output is executed.
3. **Binary zero purity under noise.** Direct clean quantized-histogram purity fails when positive false counts can be injected. SC003's pessimistic subtraction by the certified total row error restores a pathwise downward envelope, valid for rational pseudo-counts. This is not a claim that arbitrary noisy counts remain pure.
4. **Resource-review correction.** A compact denominator-exponent encoding of rho could hide enormous output denominators. Reviewer identified this; final ledger explicitly counts FULL numerator and denominator binary lengths. The useful dyadic certificate has ordinary finite denominator length; no real oracle is needed.
5. **Fine-grid-noise refinement.** Initial author draft only showed coarsening via D-grid shifts and left Q-grid shifts unresolved. This was genuinely improved: eta=floor(Qc a)/Qc−floor(Qa)/Q is a Q-grid shift whose final fine floor equals the desired coarse value. Reviewer independently confirmed it and exact diagnostics were extended. The initial conservative limitation was not a counterexample.
6. **No arbitrary scalar-noise surrogate for arithmetic.** Finite internal evaluation is specified, not replaced by a worst-case error oracle. Its zero-score exact common-weight cancellation is essential to all lower transfers.

Finite diagnostics corroborate tested instances only. Full review and root acceptance remain distinct evidence events.
