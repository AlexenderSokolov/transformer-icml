# Fixed-D realized-QK checkpoint

This analytical extension continues [the two-read checkpoint](../two_read_qk_bridge_20261112/RESULT.md) and [single-read bridge](../qk_risk_bridge_20261112/BRIDGE.md). The theorem and independent review were completed on 2026-11-12. Public source provenance is the immutable parent commit c868c4be852b976e816ffffd8b1c9c0a9aac689e and its referenced earlier checkpoints.

The induction assumes homogeneous token-only raw maps, complete-score realized global QK budgets at every row and stage, common comparison domains, and no history bypass. Gains and depth dependence remain explicit. It does not establish a general positional-value Transformer lower bound, a super-logarithmic frontier, or a matching construction. Risk is expected absolute probability error against (1+theta X_{N-1}X_N)/2 under the stationary source; the free-pair result compares the equal prior theta=+h,-h.

This publication contains no new experiment. Earlier two-read numerical bounds were vacuous and do not certify the induction. No CI or full-repository verifier was run. Historical inventory entries and the previously identified 293 undeclared historical files are left unchanged. The independent review is mathematical scrutiny, not formal verification or external peer review.
