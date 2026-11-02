# BK001 accepted handoff

Root accepted BK001 on 2026-11-02 at 12:32:29.954083 UTC after reading the complete initial proof, its sole exact endpoint-bound delta, and the complete fresh independent review. The proof's candidate header is preserved; acceptance authority is `../intake/BK001_acceptance.json`.

## Result and information boundary

At supplied beta=1/M, an estimator restricted to the exact eight triple counts plus the initial/final PAIRS cannot attain the binary known-k rate simultaneously at clean budget zero and every unknown corruption budget. The stationary construction gives the exact constrained-risk inequality (BK1). It uses a parameter-independent strict-k kernel with the final pair protected. Canonicalization preserves the stated statistic and explicitly charges the mismatch from the fixed pre-sampling null suffix length.

This theorem is **not** a full-history impossibility, does not include richer first/last-r boundary windows, and does not strengthen the known-k minimax lower. Continued full-history work is kept in separate BK002 candidate files; no later result changes this unit's scope or bytes.

## Exact versions

- Proof `BK001_histogram_adaptation_obstruction.md`: `edbfc9cd372df7497ff7462eded0e6c85a3ee4f99f21bd7310f460bd1f0fcb5a`.
- Full independent review `BK001_independent_full_review.md`: `ec654b57d3a82c66fb70e9801febc517f83a4fa1e3f6a06fa93b5b66f186628b`.
- Receipt `intake/BK001_acceptance.json` binds both versions and the restricted observation model.

Author diagnostics: 32,767 exact small-word canonicalizations, 458,753 fixed-null-distance comparisons, 37 exact family/certificate/atom cases, and exact conditioned-failure constants. Independent diagnostics: 131,071 complete words, 2,097,153 fixed-suffix comparisons, 30 exact large-parameter cases, 480 alternative certificate inequalities, 96 null inequalities, and symbolic/rational probability-flow identities. All PASS on their stated instances, not formal verification of the infinite theorem.

## Actual revision history

The ONLY proof revision changed §4's endpoint-mixing paragraph (line101 in the initial/final candidates): a valid exponential contraction estimate was replaced by a valid elementary reciprocal Bernoulli estimate. Its auxiliary sufficient n threshold changed 32 to64; the actual theorem domain n>=4096, family, kernel, constants and conclusions did not change.

The previous file hash was `f51f7b0ce139389d117ce05a8ac74889fb82bbc010c3908a62442b6f447eabeb`. `revisions/BK001_endpoint_bound_true.diff` is the exact single-paragraph delta.

**Preservation disclosure:** the previous bytes were NOT backed up contemporaneously. They were reconstructed losslessly by reversing the exact documented one-paragraph replacement from the execution record. `revisions/BK001_endpoint_bound_revision_record.json` states this explicitly, and `BK001_pre_elementary_endpoint_bound.md` contains those exact prior bytes. It is not misrepresented as a saved-at-the-time snapshot.

## Evidence and limits

`BK001_ACCEPTED_BINDINGS.json` records the exact accepted artifact/revision/receipt hashes and imports the independently checked source bindings. Accepted proof files were not edited after acceptance. Contributor route-barrier and macrocycle notes in this directory remain explicitly UNREVIEWED and are not dependencies of BK001. Independent LLM review and finite diagnostics are corroboration, not external peer review, formal verification or a novelty certification.
