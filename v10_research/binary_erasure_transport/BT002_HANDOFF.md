# BT002 handoff — candidate binary logarithmic corruption lower

2026-11-02. Fresh full independent LLM review PASS; consult BT002_independent_review.md for bound snapshot hashes and exact scope. No root acceptance is implied by this handoff.

## Claimed result
For M>=64,0<=k<=M,beta∈[0,1], e=max(sqrt(beta),1/M), F=(k/M)[1+ln(1+1/(e k))] (F=0 for k=0):

    R_stat >=2^-54 max{M^-1/2,F}.

This is stationary binary second-order, all-state P²>=beta Pi, complete corrupted-history observation, actual preserved terminal pair, hidden attack seed, offline source-independent at-most-k Hamming corruption. The same prior/kernel handles all rare suffix lengths. Combined with accepted SC003 upper, this closes the binary fixed-alphabet rate for stationary and arbitrary starts. Root must verify and accept the new lower before promoting that combination.

## New mechanism
Uniform fixed-count renewal paths have KL<=ln(t+1) from a canonical chain at empirical parameter. Uniform five-step coupling yields a finite Hamming transport bound O(sqrt(t log t)+tDelta) to a public coarse-parameter canonical bridge. This gives a common strict-budget attack after truncation on t<=2^-44 k²/ln(k+2). Finite-message small-ball reasoning tolerates fixed truncation-failure probability. The exact scalar completion F<=1830 max{clean,epsilon,truncated sum} removes that restricted range from the final minimax rate.

BT001's stronger neighboring-count O(1) transport remains OPEN and is not needed. Its boundary obstruction and failed merge are preserved unchanged.

## Files/evidence
- BT002_entropy_bridge_lower.md: full proof, explicit constants and semantics.
- BT002_scalar_completion.md: independent complete finite-domain algebra.
- check_bt002.py / BT002_exact_diagnostic.json: 762 structural checks pass.
- check_bt002_scalar.py / BT002_scalar_checks.json: 99,180 checks pass.
- BT002_source_bindings.json: SHA256 dependency bindings.
- BT002_independent_review.md: full-review PASS, no blocker.
- check_bt002_review.py / BT002_review_checks.json: 5,392 independent checks pass.

## Limits
No efficient transport algorithm, online attacker, visible mask/seed, modified terminal pair, learned predictor, K-sharp growth, external novelty or formal-verification claim. No frozen or accepted source changed; no external upload, contact or publication.
