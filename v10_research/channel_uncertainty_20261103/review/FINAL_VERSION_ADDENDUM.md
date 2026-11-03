# Final-version review addendum and preserved review history

2026-11-03. PASS retained for final candidate SHA256 `4051fa63b42f582efdbbba7f70f151b297d52f5ee449b22b570abbba4debb5e2`.

The reviewer previously completed and reported PASS for the mgf-completed candidate SHA256 `76ae32e6221cf0efb5e05d9597969ee2fcc6b8cb26366ac4f8dfd24861de50a6`, before receiving the author's final computational clarifications. That prior review is preserved here as a historical review fact, not represented as root acceptance. The live full_review.md and bindings.json were subsequently updated to the final version; no contemporaneous standalone snapshot of the prior reviewer binding was retained, and none is fabricated here.

Actually read the full final history/mgf_proof.diff, which compares the genuinely saved original candidate `3f5aeb2b8fde5adf6007be49bb5ece803fc5c0c0c0a3ebb6f53acef4bbdecd58` with the final candidate. It contains the already reviewed mgf proof and these two further computational changes:

1. Choose `R=ceil(ceil(log2 M)/(4γ²))`. For M≥64, `ceil(log2 M)≥log2 M≥ln M`, so this integer satisfies the original sufficient length inequality. For rational γ, it is exactly computable with integer bit-length (including the power-of-two boundary) and rational arithmetic. It remains O(log M) for fixed γ.
2. Separate `O(R)` output-symbol/word operations from `O(R log(R+1))` conservative naive bit operations. The decoding counter uses O(log(R+1)) bits. This is a valid conservative cost, and additional time remains polylogarithmic in M; it does not assert O(R) naive bit operations.

Neither change alters the statistical proof, feasible factors, minimax quantifiers, source classes, or sharp midpoint boundary. The final candidate hash was actually recomputed and checked; current bindings.json fixes the final candidate and final full review. This addendum is an additional preserved review record, not a retroactive acceptance or a claim of an unretained historical snapshot. No accepted source was rewritten, and root disposition remains separate.
