# Accepted all-start balance-gate handoff

The authoritative status is `../intake/CB005_root_acceptance.json`. The historical candidate header in the frozen proof is intentionally unchanged.

- Proof: `CB005_all_start_critical_adaptation.md`, SHA-256 `5e514451e88672533b5a376e43265b8a382ac0b59e816e3ef06212ea5be6db52`.
- Fresh complete review: `CB005_independent_full_review.md`, SHA-256 `b8976cae54be86f6b9c110f207256c38ec5c81913cc1156af0bd913cba47c57a`.
- The review independently reconstructed the frozen gate reduction and reports 16,736 new exact checks plus a separate rerun of 752,062 existing exact checks. These are corroboration, not formal verification or external peer review.

## Accepted conclusion

For the binary homogeneous second-order experiment with an ALL-STATE certificate `P² >= beta Pi`, `M >= 64`, and every strict first-`M` Hamming budget `0 <= k <= M`, the same deterministic estimator satisfies

    R_all <= min{1, 2^16 / sqrt(M) + 2^16 / (M sqrt(beta)) + 2^23 k / M}.

The actual initial pair law is arbitrary, including unsupported states. The last pair is protected, loss is unconditional TV at its true actual next law, and the mask, attack seed, clean interior, source and stationary law are not observed. The estimator itself uses neither `k` nor `beta`.

At `beta = 1/M`, its risk is at most `min{1, 2^17 / sqrt(M) + 2^23 k/M}`. More generally it attains the known-budget minimax order simultaneously for all budgets on every band `beta >= c/M`, with constants depending on fixed `c > 0`.

## Observable map and proof mechanism

Only the global eight triple counts, four first-half pair-departure counts, and the protected terminal pair are used. In the terminal row, write these counts as `C'`, `J'`, and `J1'`. Output the designated empirical probability `C'/J'` if `J' > 0` and `512 J1' >= J'`; otherwise output zero. The designated symbols are `00 -> 1`, `01 -> 1`, `10 -> 0`, `11 -> 0`.

The new all-start step is a terminal-weighted occupation-imbalance bound. A target-specific transition bound and a tilted JOINT terminal/upper-occupation tail retain the stationary target mass without assuming that the actual start is stationary. An auxiliary reflected chain and an absorbing-entry first-hit bound handle singleton stationary support and unsupported starts. The deterministic edit reduction was already all-start valid in the separately preserved stationary proof.

## Boundaries and provenance

The stationary proofs and failed exact/near-prefix vetoes remain immutable historical units. The result does not prove global square-root-beta mixing, a subcritical all-budget guarantee, minimality of four counters, or any architecture/resource claim by itself. The companion domain and finite-cut manuscripts require their own review and receipts.

`CB005_first_hit_prior_art_note.md` records the established Norris–Peres–Zhai first-hit pointmass scale and exact limited reading scope. The self-contained reset-row derivation is not advertised as a new generic first-hit theorem. No external novelty certification is made.

`CB005_ACCEPTED_BINDINGS.json` binds the receipt, exact proof/review bytes, diagnostic evidence, inherited sources, and this handoff. No accepted proof was edited while preparing the handoff.
