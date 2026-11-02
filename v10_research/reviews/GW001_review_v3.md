# GW001 v3 — independent narrow revision review

2026-11-02. **Verdict: ACCEPT.** The v3 revision resolves the nonblocking product-container ambiguity identified in my v2 review, without changing the theorem, finite attention rule, statistical proof, or asymptotic resource coordinates. Its newly supplied canonical-source identities are correct. No new blocking issue was found.

Candidate: `v10_research/growing_weight/GW001_growing_integer_weight_escape_v3.md`, SHA-256 `44f32cd431c4a304602537b19ab3e9752cd9fcd1a1cfece391e718db47e0da62`.

## Review scope and comparison

This is a narrow revision review building on my complete v2 review, now copied byte-identically to `v10_research/reviews/GW001_review_v2.md` (SHA-256 `5a96423961c7bc6ddc36471dec9a2b5439db11b57758966a4d2bf3cfdeebee02`). I inspected the complete v2-to-v3 unified diff and independently checked the v3 source manifest, source reconciliation receipt and canonical/historical byte comparisons. No frozen candidate, historical source, original review, or copied v2 artifact was edited.

The diff contains exactly: (i) version/status text; (ii) three paragraphs in §5 specifying actual allocated multiplication/temporary widths; and (iii) the appended revision/provenance account. Sections 1–4, the execution-ledger formulas, §6 PURE expansion, and the fixed-versus-growing weight scope are unchanged. Therefore the deterministic and statistical diagnostics recorded in the v2 review still concern the identical mathematical algorithm. I did not rerun or relabel them as execution of a new emitted implementation.

## Product/temporary widths

V3 now explicitly uses b-bit persistent payloads, retains the full 2b-bit product of arbitrary b-bit operands, and permits guarded constant-multiple-b temporary words with a safe 4b+4-bit allocation. Wider arithmetic runs at its actual allocated width; fixed public loops have O(b), rather than literally b, steps. No product truncation is authorized.

This removes the earlier literal tension between b-bit allocated operands and a claimed b-bit full product. The actual construction does not multiply two unrestricted 4b+4-bit temporaries recursively: products are formed from the specified payloads, then manipulated within the proved guard ranges. A sum of O(K) b-by-b products needs at most 2b+O(log K) bits, and log K<=ell<=b/64. Division shifts need only a constant number of additional remainder bits. The stated guarded allocation is adequate for the declared operations, including the optional W=MQ ranges. General arbitrary A still requires its separately declared enlargement of b.

Replacing b by a fixed multiple in these arithmetic operations changes only absolute constants: ripple operations remain O(b), school products/divisions O(b²), and their recycled scratch O(b). The packed S, stored program, addressed-tape scan cost, offline writes, simultaneous phase peaks, and distinct PURE layer/parameter/forward-work bounds retain their claimed asymptotic orders. The revision makes no cheaper runtime, narrower product, or new equivalence to the original exponential evaluator claim.

## Independently verified provenance

All 13 entries of `GW001_source_bindings_v3.json` match their actual SHA-256 values, including unchanged v1/v2 and the exact assigned v3 candidate.

1. **R011:** Removing exactly the first two newline-terminated lines of the canonical proof leaves bytes identical to the historical bound proof. The removed editorial preamble is exactly 561 bytes. This is not merely similar theorem text or whitespace-normalized equivalence. The canonical independent-review header states ACCEPT and explains that pending references in the frozen author proof are historical. Existing historical root acceptance remains retained; canonical editorial material does not independently re-prove the theorem or reset its status.
2. **SRC:** The historical English proof with its final whitespace removed occurs at byte offset 24,715 in the canonical fact. The historical suffix is two newlines and the canonical suffix after this exact body is one newline. Thus the scientific English body matches exactly, with only one trailing blank line removed. The containing canonical fact additionally has its statement/contract wrapper; no equality of whole fact to standalone proof is asserted.
3. **GU:** The entire historical proof bytes, without normalization or omission, occur at byte offset 25,501 of the canonical fact. In particular the actual-terminal occupation argument is unchanged. This is a containment assertion, not whole-file equality.
4. **Copied review artifacts:** The original review, review bindings, independent-check script and check report are each byte-identical to their four canonical copies named in `GW001_source_reconciliation.json`. The receipt's hashes and 561-byte preamble identity agree with independent checks.

The byte-identical relocated check script is a provenance copy, not a location-independent new executable: it computes its workspace root from `__file__`, so its original `reviews/` location remains the execution entrypoint unless a later separately versioned script adapts that path. This does not affect any source identity or existing check result, and no change to originals is requested.

## Scope retained

Acceptance remains for GW1/GW2 and the declared fully paid changed cached-integer-weight construction, with separate conservative serial and PURE realizations. The primary effective logit range is 2 ln M and the optional range 2 ln(MQ); code value 2 is not a bounded natural-logit claim. No arbitrary-architecture, computational-advantage, training, optimal-logit-budget, original finite-exp evaluator equivalence, or near-IID K-sharp minimax conclusion is accepted or implied.

This is independent LLM proof/provenance review, not external peer review, formal verification, literature-priority certification, or execution of a complete emitted circuit. No further revision is required within this narrow review scope.
