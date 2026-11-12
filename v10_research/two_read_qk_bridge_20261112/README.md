# Restricted two-read checkpoint

This adds a source-average correction to the single-read bridge in ../qk_risk_bridge_20261112/. A second uniform read of contextual values is not exactly count-sufficient, even for width-six full-PreLN. The corrected bridge pays the first-layer covariance and contextualization error; these do not disappear at zero QK.

Only the restricted two-read theorem and explicit example are included. No fixed-D extension, trained experiment, general evolving-KV lower, or sharp resource frontier is asserted. Constants are total gains and realized global key-array norms, not merely projection norms.

For the risk formulas, R_theta means E_theta|Q-(1+theta X_{N-1}X_N)/2|, with stationary source, N>=3, 0<h<=1-2c, and uniform constants at theta=±h. The current proof is clean deterministic.

Run `python check.py`. The finite inequality checks are deliberately loose and vacuous; the nonzero summary counterexample is the substantive diagnostic. No CI or full-repository verifier was run. The inherited 293 undeclared historical files were not repaired or modified.
