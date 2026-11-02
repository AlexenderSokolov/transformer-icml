# BS001 diagnostic notes

The author scalar suite is derived from TR001's accepted synthesis diagnostics, with the binary scale `t=M max(sqrt(beta),1/M)`, the correct lower cutoff beta<=1/256, extra beta=M^-2 boundary points, and direct real-envelope/integer-construction checks. It is not an independent audit. All old files are preserved.

Run: `python v10_research/binary_stationary_frontier/BS001_diagnostics_v1.py`.

Result: PASS, 1,326,099 assertions across 81 M values through log2(M)=496, with lower-completion branch counts A=12,342, B=39,265, C=14,883, D=60,487. Checks include monotonicity, log truncation completion, both product-threshold directions, legal dyadic allocation, fixed-factor threshold sufficiency, ceil(f_Q) upper, real-envelope lower, elementary statistical KL, and ten source/receipt hashes.

The separate independent script/review is authored by a fresh reviewer. Neither suite verifies a universal minimax theorem, implements an original network, or substitutes for the written proof and accepted dependency arguments. Floating-point tolerances are explicit in scripts; extreme finite checks remain numerical evidence, not exact arithmetic certification.

An initially duplicated closing parenthesis in the author Z_star display was corrected before freezing the candidate for review; no mathematical statement changed. There were no author diagnostic failures.
