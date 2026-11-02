# Independent diagnostic history

The first fresh audit run reached its final check and failed the audit script's `lower_and_upper_constant_slack` assertion. This was an audit-harness transcription error, not a candidate proof defect: the script tested `8*8193^2*32 < 2^34`, which is not the manuscript inequality.

The target is `2*8193*sqrt(32)+4 < 2^17`. Subtracting 4 and squaring positive sides gives exactly `4*8193^2*32 < (2^17-4)^2`. The revised diagnostic uses this exact equivalent assertion. The first script is retained as `independent_exact_checks.v1.py`. No author or frozen source was modified. All earlier checks in that run had passed; the complete corrected run is recorded separately.
