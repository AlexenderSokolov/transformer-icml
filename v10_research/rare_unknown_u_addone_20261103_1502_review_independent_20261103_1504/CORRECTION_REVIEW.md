# Review of precision-format correction

Candidate: `v10_research/rare_unknown_u_addone_20261103_1502/unknown_u_addone_matched_rate_v1.html`  
Candidate SHA-256: `37a1b01e27f315097c5c910005605b877ba9b6d0de160940c7acc375b6af849b`

Correction: `v10_research/rare_unknown_u_addone_20261103_1502/fractional_grid_precision_correction_v1.html`  
Correction SHA-256: `97ebbf5d680f5d0e8dfcd30b86924bdfcaa751082ca6f5cd6723f5b43c09c384`

The candidate and correction hashes were independently checked and match these bindings. The correction resolves the format issue identified in `REVIEW.md`: the grid {k·2^(-b): k=0,...,2^b} includes both 0 and 1 and has spacing 2^(-b), so nearest-grid rounding of a clipped value incurs error at most 2^(-b-1). The caveat that this may require an additional endpoint/integer bit or a different encoding is necessary and stated. In particular, b denotes the number of fractional bits in this specified grid, not necessarily total storage bits.

Read together, the candidate and correction support the stated selected-head-output port condition and ≤3ε/2 extra TV error, assuming exact selected head-coordinate values before rounding and the otherwise exact operations enumerated in the candidate. The correction does not imply that errors from earlier computation disappear: any such error must be added to or otherwise incorporated in the ε port budget. Nor does it establish a complete finite-word implementation or a bit lower bound. The statistical-rate and architectural scope limitations in `REVIEW.md` remain in force.

This was a read-only analytic audit of both bound source files, with no randomness, numerical tests, enumeration, external writes, or source overwrite.
