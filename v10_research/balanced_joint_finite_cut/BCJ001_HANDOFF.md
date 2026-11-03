# BCJ001 accepted handoff

2026-11-02. Status: **ROOT_ACCEPTED_AFTER_INDEPENDENT_LLM_REVIEW**, receipt `../intake/BCJ001_root_acceptance.json`, accepted 2026-11-02T14:31:28.560722+00:00. The frozen theorem's original candidate-status wording is retained as historical provenance; this receipt controls current acceptance. No theorem edit was made for acceptance.

## Exact frozen artifacts

- Theorem: `BCJ001_theorem.md`, SHA256 `95d5aac1ee2504955e55c1e82241c8a07d219661e2620c6e083acf5c8701554d`.
- Complete fresh review: `BCJ001_independent_full_review.md`, SHA256 `9cce8092070916078baa9b1cb82dcc9a9d6872b0013568996e4310a9f4c413ef`.
- Author source bindings: `BCJ001_source_bindings.json` (historical candidate freeze; preserved).
- Reviewer bindings: `BCJ001_independent_review_bindings.json`.
- Current accepted handoff bindings: `BCJ001_accepted_bindings.json`.

## Accepted result and interface

The fixed encoder exports eight global triple frequencies and four first-half row **subfrequencies normalized by M**, plus the exact protected terminal pair. All twelve scalar ports use one zero-score uniform head. Paid positional local tables implement the first-half indicator. The actual finite bank is exactly floor(D A/M)/D, P>=h, Q=2^h, D=2^P.

An attacker makes at most k first-M symbol replacements, preserving the terminal pair, then adds one vector l-infinity perturbation of radius delta before clipping and Q-flooring. The single rational decoder is blind to k, delta and beta. Its stationary upper is

    min(1,2^16/sqrt(M)+4096/(M sqrt(beta))+2^23(k/M+delta+1/Q)).

Accepted CB005 gives the same all-start claim with 2^16 replacing 4096 in the bias term, including unsupported starts. This extension is no longer conditional on a pending CB005 receipt. The independently perturbed pseudo-counts need only 0<=C'<=J'; no J1'<=J' or realizable-word/cross-bank consistency is imposed.

A fresh complete-twelve-port IID lower, exact vector coarsening, and BT002 full-corrupted-history simulation give the fixed-prefix lower. On every fixed beta>=c/M band the matching rate for both initialization conventions is

    Theta_c(min(1,max(M^-1/2,k/M,delta,1/Q))).

This matching statement is for THIS fixed encoder, not an optimized-encoder or arbitrary deep-architecture lower. Below the band, only the stated upper/lower bracket is established. Full positional, mask, finite-arithmetic, storage, handoff and isolation costs are included; h/P count fractional precision, not total accumulator width.

## Actual diagnostic history

The original author run completed successfully without a reported failed attempt or theorem repair: `BCJ001_author_checks.py` produced `BCJ001_author_checks.json`, PASS on 20,000 real pseudo-count gate cases, 16,440 floor/coarsening cases and 500 source-edit cases. Eight dependency receipt/proof hashes were separately checked at the author freeze.

The separate independent reviewer produced `BCJ001_independent_checks.json`, PASS on 8,800 boundary-enriched rational gate cases (including 1,006 where the half pseudo-count exceeds the total), 37,980 exact evaluator/nested-floor/coarsening cases, and eight fractional ceiling cases; eight dependency receipts were checked. These are the actually recorded outputs, not new reruns asserted by this handoff. No failed-run history is manufactured. The independent full proof review was read by root before acceptance.

Finite diagnostics and independent LLM review are not formal verification, external peer review or novelty certification. No fixed neural-depth, resource-optimality, training or physical-reliability claim is made. This handoff changes no accepted proof.
