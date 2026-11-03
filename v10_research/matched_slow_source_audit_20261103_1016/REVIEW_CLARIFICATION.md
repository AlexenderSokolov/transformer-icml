# Independent-review clarification

The term “accepted half gate” in §4 of PAIRED_SOURCE_SCOPE_AUDIT.md refers to A, the empirical-ratio gate in CTO001 and PGT001, not literally B_G. A and B_G agree on rejection; on acceptance A uses C/J whereas B_G uses the add-one B. PGT001 §3 shows that under protected k-edits their expected absolute difference is ≤16 M^-1/2+192k/M. Combining with A's bound gives

  R(B_G) ≤ (2^17+16)M^-1/2 + (2^23+192)k/M,
  R(q_1) ≤ (2^17+17)M^-1/2 + (2^23+192)k/M.

These are full critical-class bounds, independent of k and source, with the same fixed predictor. In §3, “output words need O(log M) bits” means the output probability's fixed-point representation, not the M+2-bit observed input word. This clarification does not alter or overwrite the original note.
