# SC002 author handoff

The full-history source-symbol-corruption frontier is proved in `SC002_theorem.md` for fixed K>=3, all beta in [0,1], M>=64, and 0<=k<=M, both stationary and arbitrary initialization:

    Theta_K(min(1,max(M^-1/2,(k/M)[1+ln(1+1/(max(beta,1/M)k))])))

with the k=0 corruption term defined as zero. Explicit lower constant is 2^-15; the upper constant is displayed in the theorem. The upper estimator is direct corrupted-selected-row add-one, independent of beta and k. The logarithmic lower uses a stationary recurrent three-symbol witness and one common offline randomized marker kernel; IID rounding supplies the linear corruption floor at every beta. Both preserve the terminal pair, account for the full corrupted word and retain the actual future return mass.

Artifacts:
- `SC002_theorem.md`: complete finite-domain proof; SHA256 `40a8950861b486f532ac625fa479cb49cd79241dbb4b08efce6296ae9b6a1f0e`.
- `SC002_source_bindings.json`: load-bearing source and author diagnostic identities.
- `SC002_diagnostics.py/json`: author finite tests; all pass.
- `SC002_review_checks.py/json`: separately written reviewer tests; all pass, also rerun by author without result changes.
- `SC002_independent_review.md`: finalized independent PASS at the exact theorem hash; no revisions required. `SC002_review_bindings.json` binds its evidence.

Only this new directory was authored. SC001, accepted IU/AU/IP/R011 sources and all delivery-stage7 material remain unchanged. Exact erasure avoids the abandoned concentration cutoff; residual suffix occupation avoids a loose additive mixing burn charge. No mathematical counterexample or unresolved diagnostic failure was encountered. Review is independent LLM checking, not formal verification, peer review or novelty certification. Root acceptance is separate and not asserted here.
