# TR001 diagnostic scope and execution notes

Author command: `python v10_research/two_resource_frontier/TR001_diagnostics_v1.py`.

PASS: 1,228,235 floating-point scalar assertions, 81 M values through 2^496, every branch A/B/C/D exercised, all 13 bound source hashes verified. Checks include beta=0, beta=1/M, beta=1/16 and its next float, beta=1, legal dyadic grids and integer weights, next-float cutoff boundaries, statistical KL, and necessary/sufficient product-budget conditions. These checks corroborate the analytic proof; they do not establish universal quantifiers or execute the predictor.

One initial diagnostic execution failed with Python `OverflowError` from evaluating y**3 at huge y, not a violated inequality. The check was equivalently rewritten as log(z)<=3log(y); all inputs there are positive and y>=4. No theorem formula or constant changed. The script was rerun successfully. This is the only author diagnostic failure; no failed mathematical sample was discarded.
