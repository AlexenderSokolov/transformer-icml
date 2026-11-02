# BF001 v3 — independent revision review

**Verdict: PASS.** The exact v2-to-v3 diff resolves the augmented-address-width qualification in the prior review. No new blocking issue found. This is a scoped revision review, incorporating rather than overwriting `BF001_review_v2.md` and its bindings.

Reviewed candidate SHA256: `31138a756cc5e9cdc6a5cc8c55d11e265672c7048c1acb34266cdfd67411af7a`.

## Checks

1. All eleven v3 manifest entries match their actual SHA256 and byte length. Sections 1–3 are byte-for-byte unchanged from reviewed v2: family quantifiers, constants, domain-completion lower, finite SRC inclusion and upper therefore inherit the full prior independent review.
2. The only substantive revision is in §4 resource accounting. The original SRC/NB002 portion retains its original p and <=128p coefficient/product/guard bound. Added boundary heads, padding and their addresses instead use `p_aug=p+ceil(log2(D+r+K+2))`, with conservative <=128p_aug augmented words. This explicitly pays architecture-index widths rather than concealing them in fixed-parameter constants.
3. Original p already controls history indices and arithmetic precision. The added logarithm controls head/coordinate indices; addresses for the polynomial-size added buffers/projection/mask records consequently have O(p_aug) bits. The revised historical-copy, projection, attention, control/output and public-boundary-address charges all use p_aug. Boolean mask bits still require O(r n²), correctly independent of arithmetic word width; generation, indexing and writes remain paid separately.
4. The PURE compilation now expressly uses augmented actual work and live-memory totals. It cannot silently reuse the six-head memory/work inputs. The exact head bound remains at most 6+2r when the full S port is emitted, not six.
5. Extra copies remain acquisition of the permitted boundary S only. The causal construction and cut-release conditions in the v2 review remain applicable. No new interior statistic, historical reread, nonlocal statistical key feature or clean evaluator port is introduced.

The mathematical claim remains fixed K,D,r,a,b, one global dense bounded-ratio block over local windows, arbitrary decoder after the quantized cut. No growing-architecture risk-uniformity, equal numerical resource constants, formal verification or executed-network benchmark is certified. The revised accounting removes the specific address-width shorthand without changing that scope.

No frozen source or prior review was edited. Full revision/source bindings are in `BF001_review_v3.json`.
