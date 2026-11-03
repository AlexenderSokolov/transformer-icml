# Actual revision note — 2026-11-02

At the root's request after independent review, section 6 now explicitly fixes integer N≥64 and integer 1≤r≤N+1, restricts the single-map supremum to integer budgets k∈{0,...,N}, and defines Γ_stat(N,r)=inf_A Γ(A;N,r), stating that the every-map lower passes to that infimum.

This is a scope/notation clarification, not a change to the finite lower proof or constants. The actual before file and unified diff are preserved here. Original `MANIFEST.json` and original `HANDOFF.md` remain historical, unchanged. The updated binding is `MANIFEST_after_factor_domain_clarification.json`.

Correction to the author's earlier chat report: section 6 previously displayed `sup_{k, stationary P, strict common K}` without printing the bounded integer budget domain. The earlier report saying section 6 already used integer budgets overstated what its displayed definition explicitly said. The current edit makes that domain explicit rather than pretending it was already printed.
