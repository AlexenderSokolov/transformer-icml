# Exact fixed-bank attack DP: public replay

All 18 scientific files are exported byte-for-byte: the final proof, two real before versions and their two diffs, author programs and results, and independent review/programs/outputs/input identities. No privacy normalization, mathematical edit, source resealing or selective removal was needed. Historical candidate/unreviewed headers remain as chronology; the separate later LLM review binds the exact final note.

## Reproduce the saved finite checks

From a trusted pinned checkout, with ordinary Python 3 and its standard library:

    python3 provenance/exact_attacker_dp_20261103/verify_public_replay.py

The helper checks its own bytes, the two current maps, all 18 sources and six already-public scientific context references against the active inventory. All 14 original SHA256SUMS and independent INPUT_BINDINGS occurrences match directly; there is no new public/original discrepancy or resealing. The context references pin the prior legal-objective theorem/review and the exact ACG/FPA candidate/acceptance records. They are source interpretation references, not imports required by the diagnostic programs. Existing project-wide original/public mapping and missing-history boundaries remain unchanged.

The helper runs these unchanged commands in an automatically cleaned temporary copy and compares stdout byte-for-byte with all six saved logs:

    python3 -I verify.py --max-m 6
    python3 -I verify_histogram.py 6
    python3 -I review_independent/check_independent.py
    python3 -I review_independent/check_bank_semantics.py

The independent bank-semantic checker imports only the included author verify.py; no private workspace file or network is needed. Symlinked inputs or inventory paths, missing or altered source identities, and optimized Python are rejected. No checkout result is overwritten, and scientific assertions remain enabled. Integrity assumes a trusted pinned checkout; the inventory is not a cryptographic signature against a coordinated rewrite of the entire checkout.

## What was checked

- The author selected/all-row J,C,D check makes 6,144 complete reachable-bank/minimum-cost-map comparisons through M=6 and checks a nontrivial exact readout maximum. Its brute force shares the author's bank-update helper.
- The separate author histogram program checks 3,072 complete maps and four-counter segment reconstruction through M=6.
- The independent histogram DP uses a literal independently counted brute-force oracle, checks the same 3,072 maps, and validates an attaining maximum-utility witness in every case.
- A separate independent recount validates all-row and selected-row bank semantics on all 2,040 words for M=1 through 8, without reusing the author's update helper for its oracle.

The actual correction chain is before_clarification → CLARIFICATION.diff → before_class_scope → CLASS_SCOPE.diff → final note. Each diff's output header names the then-current RESEARCH_NOTE.md, not a license to apply it to the final file repeatedly. These real successor bytes are preserved. Finite checks support but do not replace the general recurrence/dominance/flow proof.

## Boundaries

Edits are at most k, restricted to positions below M; the final pair is protected, including the M=1 initialization. Minimum-edit dominance is not automatically a theorem for exactly k edits. The selected three-count bank takes O(M^4) transitions and O(M^3) rolling states. Complete first/second-segment histograms take O(M^9)/O(M^8); utility evaluation, exact comparison, bit/encoding and witness reconstruction are additional. These loose upper bounds are not a practical runtime claim.

A DP substitution preserves the earlier offline empirical objective only for predictors using exactly the retained count bank and declared endpoint interface, with the same conditional estimate and exact readout/comparison. It does not estimate p(h), cover arbitrary Transformer/whole-word readouts, learn a predictor, prove SGD efficiency or provide a new robustness/novelty guarantee. Independent review is LLM scientific audit, not external peer review or formal proof.
