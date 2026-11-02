# SH001 handoff

New successor candidate: `SH001_sharp_weight_ratio_threshold_v1.md`.

**Result:** rescale the rare-suffix cutoff by z=κQ; keep κ out of the tube-cell count, rather than paying the old κ^D cell-volume factor. This proves a lower c_(D,r)/z times ln(1+(1/8)min{z/(Mβ0),M/z}) on z<=M/4, β<=1/16. A complete regime split then proves the uniform necessary κ>=c f at Q~sqrt(M), f=1+ln(1+Q/(Mβ0)). The accepted SB001 v2 upper supplies κ<=2f for a sufficiently large fixed target-risk multiplier. Thus actual κ, not only its effective logarithmic range, is matched in this grid band.

Preserved: all BA001/SB001 originals, old open remarks, and frozen stage3 delivery. No implementation edits or all-Q matching formula. No arbitrary-deep or growing-D sharpness claim.

Evidence: `SH001_source_bindings_v1.json`; independently reproducible author `SH001_diagnostics_v1.py` and its JSON. Independent reviewer is `independent LLM reviewer`, with output under `v10_research/reviews/SH001_*`; independent review returned PASS and its executable checks were rerun successfully by the author; candidate acceptance remains the root's decision. Diagnostics are finite corroboration, not formal verification or external peer review.

Independent review: `reviews/SH001_review_v1.md`; bindings: `reviews/SH001_review_bindings_v1.json`. Target SHA256 `fa8e326047f2df8f01dd7b3112da655937ad7be1a3508ad00b80ccd51b64fd50`. Independent checks passed 1,120 cutoff cases, 2,430 necessity cases, 468 exact-rational local-moment cases and 19,968 influence checks. No blocking correction requested.
