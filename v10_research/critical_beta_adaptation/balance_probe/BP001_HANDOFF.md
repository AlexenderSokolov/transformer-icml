# BP001 stationary balance handoff

Candidate proof: `BP001_stationary_weighted_balance.md`, SHA256 `22b60eedf31f1e990e990a8b64ad733a1a3acc9723a421fdc6d677866c771271`.

For a stationary binary second-order source with all-state positive-beta certificate, first-half/full terminal-row occupation imbalance at fixed fraction <=1/256 has designated weighted probability at most min(1,4096/(M sqrt(beta))). This is O(M^-1/2) on beta>=c/M. The stronger crossing-unit caps gamma=(a,1,1,tau) are proved, so binary reversal is handled correctly.

Proof ingredients: generic fixed-target return/hit moment induction and two-sided occupation concentration; accepted BU001 v2's target-weighted hitting scale; exact binary stationary reversal and shifted windows. No global sqrt(beta) mixing theorem or terminal-conditioned IID claim. Stationary singleton supports contribute zero.

Author diagnostics pass, preserving frozen proof bytes: 36 all16 source tables,144 hitting-moment/weighted-scale checks,24,384 exact reverse-window identities,6,096 exact word-reversal probabilities;576 explicitly numerical exponential-tail comparisons. Exact BU001/SC003 proof receipts checked. Full independent review should be supplied with the assembled stationary estimator theorem; this handoff is not acceptance or external/formal review.

Arbitrary-start extension is still open in this note. The concentration bounds are uniform-start, but the final stationary Pi(s) multiplier is essential and cannot be dropped. Existing WM001 residual obstructions do not directly refute a critical-curve O(1/(M sqrt(beta))) weighted residual bound, but no such coupling theorem was proved here. A first-target-hit plus return-loop-count treatment appears more faithful than discarding path occupation information.
