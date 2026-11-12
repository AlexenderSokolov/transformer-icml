# Conditional two-row sensitivity lemma

The complete statement, derivation and independent review are in REVIEW.md. The hypothesis is a declared pathwise prefix-stability recurrence; this checkpoint does not verify it for generic PreLN networks. Initial readout state must not reveal the changed predecessor or a free endpoint pair.

The special a<=1 assumption first forces a total cross-row budget sum b=Omega(N); bounded b per layer is additionally required for a linear depth lower bound. These statements concern worst-word bit recovery, not average prediction risk or necessary local recovery for statistical estimation.

A separate replay of the independent diagnostic matched results.json byte-for-byte: 1050 variable-coefficient cases. Matrix products and full-prefix recurrences use exact Fraction arithmetic; exponential bound comparisons use binary64. These matrices commute, and no noncommuting test claim is made. Run `python check.py`. No CI or full-repository verifier was run.

This is separate from ../uniform_linear_alignment_20261112/ and excludes the scalar-position construction, whose correction/review is still pending. Existing historical inventory records are preserved.
