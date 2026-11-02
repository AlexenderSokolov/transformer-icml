# PE1 frozen-v2 reviewer report

## Identity, evidence and immutable target

- Review date: 2026-11-02.
- Reviewer agent: `independent LLM reviewer`.
- Author agent: `LLM author`.
- The reviewer is a separate LLM review with the research history supplied, including the proposal and prior discussion. It is a **same-model review by inherited configuration**, not a blind/cold review, cross-model replication, formal proof check, human peer review or server-attested model-provenance audit.
- Frozen file: `v10_research/protected_encoding/protected_encoding_proof_v2.md`.
- SHA-256, read directly before reviewing:

  `098dda50f64264a6d62f70bc9a71946ba8155f284a1f54bb947d2701df0febd5`

- This report does not alter that file. A later version requires its own hash and resolution record.

## Verdict

**The main PE1-H theorem, finite capacity theorem, sharp half-amplitude actual-risk obstruction and stated SRC-envelope inclusion are supported by the supplied arguments. One auxiliary general-amplitude conversion-work bound in §4 is incorrect as written and should be corrected or restricted before claiming the entire v2 conjunction is verified.**

The error does not affect the main amplitude-one binary construction, its constant-noise threshold, its risk bounds, or the direct-count comparator. It is nevertheless an actual quantified cost omission, not merely stylistic.

## Scopes inspected

Read the complete frozen v2 file, §§1–11. For the underlying implementation, directly inspected SRC Fact `fef8372728290b45`, proof §§3, 8 and 9.1: finite bit extraction, grid endpoints, retained-side-input list, erasure/access schedule, arithmetic widths and uniform-format dense accounting. The imported 016/MM5 statistical theorems are used in their stated accepted domains; this review did not newly re-prove them. Likewise it did not reopen the old 032–035 lower bounds.

The main checks covered:

1. Correct distinction between unchanged nominal information and the changed encoded storage boundary.
2. Correct binary numerator length, including master value one.
3. Exact cleaners in both radius regimes, including boundary points and sequences approaching one half.
4. All-coordinate, arbitrarily correlated canonical corruption and exact suffix restoration.
5. Statistical lower-bound composition and minimax quantifier order.
6. Exact finite-grid packing theorem, boundary clipping, side-information fibers and nonclaims about the actual reachable master image.
7. Uniform `p`-word costs, all-token work, coexistence, original input/masks and offline charges.
8. The actual-risk erasure converse using all original exact side inputs.
9. V-port repetition, the strict global-L1 budget and basic implementation charges.
10. The direct-count comparator's statistical and sequential-bit ledger, with the explicit batch/late-query distinction.

## Main proof checks and resolved first-review points

### Exact cleaning and finite arithmetic

For `delta<=1/4`, `g` is exactly zero/one on the two allowed closed intervals. The dyadic thresholds and factor two cause no finite-grid rounding. The first cleaner paragraph in §3 should be read as this subcase; the following paragraph explicitly handles the remaining range, so the organization does not create a missing case.

For `delta<1/2`, canonical numerator `j` of a corrupted zero bit is at most `Q/2-1`, while that of a corrupted one bit is at least `Q/2+1`. The integer-grid ReLU difference `g_Q` therefore returns the original bit exactly. Its slope/threshold size is `O(Q)` and its bit representation is `O(h)`; v2 now explicitly charges these. It does not claim an arbitrary-real exact threshold operation.

The source master numerator requires `h+1` bits. Each exposed rail is still an `h+1`-bit canonical physical payload after corruption, rather than a Boolean-only corruption alphabet. Clean H and forbidden scratch do not survive as auxiliary inputs. The decoded original master therefore produces exactly the clean finite suffix output, including rounding.

For the minimax lower side, identity corruption plus encoder/prefix/decoder composition is an admissible full-history predictor. Applying MM5 before taking the decoder infimum is the correct direction. The `T -> 0` equivalence follows under the specified `delta<1/2` domain; no necessary `K^5 delta -> 0` condition is imported from the different raw-cut experiment.

### Exact capacity theorem

The ball-intersection criterion remains true at the truncated alphabet boundary. Product partition cells have diameter `2e`, and the product-separated alphabet has minimum coordinate separation `2e+1`, proving the exact `s^m` capacity. Independent decoder randomization cannot permit exact recovery of two messages at a shared received point.

The proof correctly restricts its lower channel count to universal exact-message recovery, not low-risk learning or the unproven cardinality of the reachable SRC image. Side-information fibers are explicitly handled. V2 correctly confines the half-amplitude real threshold to even `L=Q=2^h`.

### Dense costs and the original representation

The earlier uniform-format issue has been fixed. With depth `O(h)` and width `O(dh)`, padded dense parameter bits are `O(d^2 h^3 p)` and all-`n` school-arithmetic work is `O(n d^2 h^3 p^2)`. The local `h`-word alternative is clearly separated and is not silently substituted for the unchanged uniform `p` format.

Scalar extraction residuals/gains of size `Q` are expressly charged and fit the inherited SRC allocation. The port itself retains amplitude one. Noisy rails cost `O(dh^2)` payload bits or `O(dhp)` under padded physical words. The phase description includes old H plus encoded rails during construction, damaged plus cleaned rails during decoding, and the original programs/input/masks/scratch. All-token execution and full-format offline writes are retained. Since `d=O(K)` and `h<=p`, the displayed extra costs fit the original broad SRC asymptotic envelopes. This is not numerical cost equality or optimality, as v2 explicitly states.

### Actual-risk obstruction at and above one half

The all-`1/2` kernel is canonical and lies within radius `1/2` of every amplitude-one coordinate. It reads no hidden source parameter. The original exact side inputs in actual mode contain no more than the terminal two symbols and possibly `X_2` through `F_3`; the remainder are public or functions of these values.

For iid Bernoulli parameters `1/4` and `3/4`, the full target distributions have separation `1/2`, and the three-symbol observation overlap is `5/16`. Any duplicated/omitted symbol or deterministic side projection only increases overlap. The pointwise triangle inequality yields sum risk at least `5/32`, hence maximum risk at least `5/64`. This works with outputs anywhere in the K-simplex and with independent decoder randomization. The original no-extra-exact-information condition is indispensable and appears in v2.

## Additional modules audited

### V-port module (§6)

The algebra is correct. For each bit, the sum of offsets from the positive baseline one is at most `D` when the bit is zero and at least `rQ-D` when it is one. Thus `rQ>2D` gives strict separation, and `r=floor(2D/Q)+1` handles ties. Every written coordinate `1+Qb` lies in the original positive payload range. The same argument uses one budget over the entire encoded bank, not one budget per replica or bit.

The bank dimension, per-slot payload width, accumulator width, moves and conservative summed arithmetic work are charged. The claimed absorption into SRC envelopes is limited to constant `r`. The text expressly makes no growing-`r` absorption claim. This review does **not** certify a separately optimized dense-neural implementation for growing `r`; no such precise optimized claim is used in the main theorem. The metric distinction from per-coordinate l-infinity noise is maintained.

### Direct-count comparator (§7)

The batch comparator has legitimate access to the already-observed complete history and actual endpoint before its boundary. Its fixed scan can maintain the queried row's K exact counters with one-hot matching and K gated increments per departure, using `O(MK(b+1))` bitwork without free random access. Working historical lags, current symbol and query one-hots contribute only the stated `O(K)` term. Counter width `b=ceil(log2(M+1))` handles all counts, including M=1. The protected counter bits use the same canonical noisy rails and cleaners.

The normalizer has positive denominator `J+K`, ordered flooring yields a legal probability vector, and its TV discrepancy is at most `(K-1)/Q`. The inherited add-one bound therefore gives `min(1,49T)` with legal h. The `w` allowance covers counts, output precision, denominator, full products and division scratch; normalization work `O(Kw^2)` is a valid conservative bound. No online all-row table or late-query-without-reread requirement is silently dropped: v2 expressly distinguishes this batch comparator from those models and disclaims its small neural-depth realization. Full input allocation is retained in the stated phase peak.

This is a checked constructive upper ledger, not a profile or a proof of optimal counter complexity. It does not establish that the direct counter and SRC have identical clean information at the cut; v2 accurately calls the counter a separate same-raw-history prefix comparator.

## The unresolved v2 error and precise repair

Section 4's constructive general-amplitude radix bullet states bitwork

`O((dh + m log(s+1))^3)`

for arbitrary physical alphabet `{0,...,L}`, while separately allocating `m log(L+1)` working bits. The work bound omits the length of the physical alphabet and therefore cannot include full output writes when `L` is arbitrarily large.

For a concrete family, fix `d=1`, `h=4`, `Q=16`, let `L` grow arbitrarily, and choose `e` near `L/2` so that `s=2`. Seventeen source messages require only a fixed number `m=5` of binary-level coordinates. The displayed work expression is then bounded independently of `L`, but writing the physical m-coordinate word costs `Omega(m log(L+1))` bit operations. Reading the public large integer `L` also costs its bit length under the stated bit model. The missing factor is not absorbable by the stated expression.

Either valid repair suffices:

1. Restrict that optional implementation-cost sentence to `L=Q` (the main amplitude-one setting), where `log(L+1)=O(h)`; or
2. Include physical/public input lengths explicitly, for example a loose cubic bound in `dh + m log(s+1) + m log(L+1) + log(Q+1)`, together with whatever finite integer budget index the implementation actually accepts. A source-independent integer index `e` can be accepted directly; no arbitrary-real delta oracle should be introduced.

The capacity **equality** itself is unaffected. The parent author separately noticed the same issue while this frozen review was underway; that agreement does not erase it from v2. No other bearing mathematical error was identified in this bounded pass.

## Diagnostics and limitations

The prior review actually ran 268 exact bounded-gain cleaner cases, 1,020 full-threshold grid-cleaner cases, 28 exact small capacity instances, and the exact three-sample overlap calculation. This pass re-read the frozen integrated proof and checked its file hash; it did not represent those prior runs as newly executed integrated SRC tests. No full SRC compiler, network profile, GPU run, training experiment or physical fault injector was run.

This is a bounded same-model mathematical review. Imported accepted facts were scope-checked, not independently recertified, and finite diagnostics are not a substitute for the supplied general arguments. There was no public action or external contact.
