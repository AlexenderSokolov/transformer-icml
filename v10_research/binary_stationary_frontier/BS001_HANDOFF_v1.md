# BS001 handoff

**Result:** exact stationary K=2 one-block two-resource frontier

`R_stat = Theta_(D,r) max{M^-1/2, 1/Q, [1+ln(1+kappa Q/(M e0))]/(kappa Q)}`, `e0=max(sqrt(beta),1/M)`.

Domain: D>=8,r>=3,M>=64,integer kappa>=1,dyadic Q>=16,beta in [0,1]. Full model, all-regime proof, explicit constants, joint thresholds and unchanged full paid ledger are in `BS001_binary_stationary_frontier_v1.md`.

Fresh independent synthesis review: PASS recommendation in `BS001_independent_review_v1.md`, bound to proof SHA-256 `ca116bd9c9a8ee88c62be85d5f0352c2d4f7b3d7df84df6406036c94ac86cb2b`. NOT root accepted yet. Author diagnostic: 1,326,099 assertions PASS. Fresh independent diagnostic: 27,646 parameter cases PASS, also rerun successfully by author. Both suites verify source/receipt hashes and remain finite numerical corroborations, not formal proof.

At Q≈sqrt(M), least feasible integer kappa has order `1+ln(1+Q/(M e0))` for sufficiently large fixed target multiplier. Lower works for real envelopes; upper uses ceil(f_Q). At beta=1/M binary requires only constant kappa, whereas every fixed K>=3 requires Theta(log M), using the same stationary all-state certificate and common fixed dimensions when D>=K^3. Constants are architecture-dependent.

All prior files and stage-4 freeze preserved. No external contact/publication/upload. Improved arbitrary-start binary surface remains OPEN; BU001's stationary mechanism cannot be silently transferred. Natural successor: prove or disprove an arbitrary-start extension with a rigorously controlled complete-suffix mixture and binary weighted-return term.
