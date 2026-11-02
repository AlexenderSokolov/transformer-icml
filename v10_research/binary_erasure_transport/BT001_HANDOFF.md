# BT001 handoff — exploratory unit, 2026-11-02

## Established, reviewed
- All-count O(Δl) transport fails: from U_(s,2) to U_(s+3,0), optimal expected Hamming cost is 2s/3+3=t/3+1.
- Cheap adjacent-long merge has cost 3+2s/(l+1) but target density proportional to Σ binom(h_i−1,2), not uniform.
- New stationary binary witness θ(1)=(a,p,1−e,e), Π∝(e/a,1,1,p/(1−e)), satisfies all-state P²≥βΠ with e=max(√β,1/M); deterministic renewal reference is dominated through j≤1/(4e).
- Interior one-step expected-cost transport (T), IF proved, is enough for the complete common-kernel/common-prior logarithmic corruption lower. Strict budget follows by truncation; fixed bad mass is handled before small-ball integration. No source-specific oracle or pair-per-horizon substitution.

## Not established
- Interior transport theorem (T).
- Matching binary logarithmic corruption lower.
- Exact asymptotic inference from the finite LPs.
- External novelty, formal verification, or root acceptance.

## Evidence
- BT001_obstruction_and_reduction.md: full statement/proofs/conditional reduction.
- BT001_independent_review.md: independent LLM review PASS for the precise limited conclusions.
- check_bt001.py, BT001_exact_diagnostic.json: 5,282 exact finite checks.
- BT001_review_checks.json: independent 4,960 boundary-word and 45 rational certificate checks.
- transport_lp.py, transport_lp.log, transport_lp_results.json: 38 finite floating-point transportation solves; balanced examples about3.39–4 expected edits per count step.

## Next scientific decision
Prove interior T or refute it with a diverging interior sequence. The obstacle is exact marginal correction of the cheap local merge, not the existence of a nearby long-cycle pair. General Markov-chain parameter coupling does not automatically imply count-conditioned transport. A weak all-count conjecture is already false. No requirement to force a positive conclusion.

No process remains running. No frozen/accepted source or SC003 author file changed. No external contact, upload, restart or publication.
