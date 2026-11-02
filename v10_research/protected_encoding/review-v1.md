# Independent bounded review of protected master encoding

Date: 2026-11-02. Reviewer: `review_protection`, separate child context of the protection author. This is an LLM mathematical review, not formal verification or external peer review.

## Verdict

**The proposed coding mechanism is correct, with explicit scope and accounting qualifications below.** Its useful conclusion is that the old scalar-port lower bound does not extend to arbitrary finite encodings within the same asymptotic SRC resource class. It is not a correction procedure applied after damage at the old scalar port, nor a same-numerical-budget comparison.

The review inspected the actual SRC proof, Fact `fef8372728290b45`, §§3, 8 and 9.1. These supply the finite scalar-to-bit gadget, exact original side inputs/lifetimes, all-token convention and uniform `p`-bit representation. The review did not re-prove the old statistical theorem or old lower-bound construction.

## 1. Exact protection and a full noise-threshold extension

Let `Q=2^h`, `h>=2`, `G_h={0,...,Q}/Q`, `d=9K+1`, and `B=d(h+1)`. Encode each integer numerator of the clean master `H` using its `h+1` binary bits, represented as `0` or `1` in **separate coordinates of the same grid `G_h`**. Every coordinate is corruptible; no encoded coordinate is treated as an exact exception.

For `0<=delta<=1/4`, the proposed cleaner

`f(y)=2 ReLU(y-1/4)-2 ReLU(y-3/4)`

returns `0` on `[0,1/4]` and `1` on `[3/4,1]`. Every operation is exact finite dyadic arithmetic when `y in G_h`. The endpoints are safe. The stored noisy rail still requires `h+1` payload bits, even though its nominal value has only one bit of entropy.

There is also a useful stronger finite-grid version. For **every real `0<=delta<1/2`**, including sequences approaching `1/2`, set

`f_Q(y)=ReLU(Qy-(Q/2-1))-ReLU(Qy-Q/2)`.

If the true bit is zero, a legal canonical replacement has integer numerator `j<=Q/2-1`; if the true bit is one, it has `j>=Q/2+1`. The integer-grid step therefore returns the exact bit. It has constant depth and coefficients/thresholds of magnitude at most `Q`, hence `O(h)` coefficient bits; its intermediate magnitudes are `O(Q)`. The SRC word allowance already covers such magnitudes and complete products. This extension is finite-grid-specific: its continuous extension does not exactly correct arbitrary real values arbitrarily close to `1/2`.

The bounded-gain `delta<=1/4` version should remain separately visible because its coefficients are bounded independently of `h`. The full-threshold version spends the already allowed `O(h)` coefficient precision/gain.

Once the clean scalar and clean scratch are erased before the attack, the decoder receives exactly a reversible encoding of the old master information, plus precisely the old exact side inputs. Decoding and using the original suffix gives the exact clean output, pathwise. Correlation between coordinates, data and the fault kernel is irrelevant to this deterministic statement. Independent decoder randomization is unnecessary.

## 2. Exact capacity converse: checked and correctly scoped

For integer coordinates `{0,...,L}` and coordinatewise edit radius `r=floor(Q delta)`, two codewords have intersecting admissible received sets iff their `l_infinity` distance is at most `2r`. This holds at the boundary of the alphabet as well: the coordinate intervals have an integer intersection whenever their centers differ by at most `2r`.

For a deterministic zero-error codec with `m` coordinates, the exact maximal message count is

`s^m`, where `s=ceil((L+1)/(2r+1))=floor(L/(2r+1))+1`.

Partition each coordinate into consecutive intervals of length `2r+1` (the last may be shorter). Two codewords in the same product cell would have intersecting noise balls, so there is at most one codeword per cell. The product code on centers `0,2r+1,2(2r+1),...` meets the upper bound. Independent decoder randomness cannot make two messages both recover with probability one at the same received word.

This is a **message-cardinality theorem**, not a risk lower bound for the actual reachable SRC image unless that image's cardinality or a suitable statistical packing has been established. In particular, do not silently replace the reachable image by the full `(Q+1)^d` cube. If exact side information is present, the bound applies separately within each fixed side-information fiber.

For general odd `L`, the zero-capacity condition is `r>=ceil(L/2)`, not literally `delta>=L/(2Q)`; grid parity matters. For the intended `L=Q=2^h`, the threshold is exactly `delta>=1/2`.

## 3. Additional actual-risk converse at delta >= 1/2

Under the original audited exact-side-input contract, any number of encoded coordinates in `G_h` can be erased to `1/2` when `delta>=1/2`. This kernel is common, source-independent and legal for every encoded state. It applies to arbitrary bounded-amplitude encoders, not just the binary scheme.

The exact retained data in actual-query mode are functions of the terminal pair and, if retained, the initial flag `F_3`, whose only data value is `X_2`; all other metadata are public. Thus after erasure an iid source exposes at most three iid symbols. Choose two legal second-order iid sources supported on symbols `0,1`, with every row Bernoulli parameter `1/4` or `3/4` and matching iid initial pair law. The target row is the same Bernoulli law in every context. Its two values have TV separation `1/2`.

The overlap of the laws of three iid Bernoulli observations is

`sum_{x in {0,1}^3} min(P_{1/4}(x),P_{3/4}(x)) = (1+9+9+1)/64 = 5/16`.

Fewer or repeated observed symbols can only make the testing problem harder. For every output distribution `q`, its TV loss dominates `|q(1)-p|`. The pointwise two-point triangle inequality and overlap therefore imply

`max_{p in {1/4,3/4}} E_p TV(q,theta_p) >= (1/2)*(5/16)/2 = 5/64`.

This holds for all `K>=2` and horizons in the common experiment, provided **no extra exact history-dependent side information has been added**. It gives an actual-risk phase boundary to accompany the `delta<1/2` construction. If the contract changes its exact-bit exception, re-audit this converse rather than importing it unchanged.

## 4. Resource correction

Parallel SRC extraction has depth `O(h)`, width `O(Kh)`, `O(Kh)` active arithmetic gates and `O(Kh^2)` hold records when all emitted bits are retained across the extraction stages. Cleaning and reconstruction add at most these orders. The original endpoint/query bits are included; no evaluator scratch needs to survive the encoded cut.

The noisy port needs `B(h+1)=O(Kh^2)` payload bits. Program/layout, original input, masks and other simultaneously live original objects remain charged. A capacity/entropy count of `B` is **not** the physical noisy-port allocation.

Under the **unchanged uniform `p`-bit dense format**, the conservative wrapper costs are

* coefficient slots `O(K^2 h^3)`;
* coefficient bits `O(K^2 h^3 p)`;
* all-`n` dense bitwork `O(n K^2 h^3 p^2)`.

The proposed shorter bounds `O(K^2h^4)` and `O(nK^2h^5)` require a separately declared local `O(h)`-word format. They should not replace the uniform-format bounds without stating that representation choice. Both versions are absorbed by the SRC envelopes because `h<=p`:

`L=O(Kp^2), W=O(Kp), parameter bits=O(K^3p^5), dense bitwork=O(nK^3p^6)`.

Offline generation, dense zero writes, copy/clear and phasewise simultaneous peak must be retained. Being absorbed in a big-O envelope does not mean zero cost, unchanged numerical constants, measured superiority or optimality.

## 5. Crucial fairness and interpretation limits

1. The vulnerable boundary has changed from an unencoded scalar storage interface to an encoded storage interface. This is allowed in an encoder-change problem, but it is not literally the 035 experiment.
2. The clean encoder runs before the declared fault event. If an adversary can choose to corrupt the original scalar before encoding, the old information loss can recur. The new result does not repair such upstream damage.
3. Cleaner, suffix, parameters and declared exact bits remain fault-free, just as arithmetic/exact bits were excluded in the original one-shot model. This is not an all-gates-noisy computer theorem.
4. Amplitude of exposed coordinates remains one and the per-coordinate radius is unchanged, while their number increases. This is not a mere amplitude rescaling, but it does spend width/storage and clean encoder work.
5. An ordinary direct counter can use the same digital storage construction. Its pre-cut history permissions, acquisition, late-query handling, storage, normalization and execution model must be costed. Nothing here establishes Transformer-specific resource advantage or trainability.
6. The old 034/035 lower bounds remain valid for their original encodings and cuts. No old result is refuted.

## 6. Bounded diagnostics actually run

The reviewer ran exact `fractions.Fraction` cleaner checks for all legal single-rail replacements at `delta=1/4`, `h=2,...,8`: **268 cases passed**. A separate exact maximum-clique computation checked the finite capacity formula for `L=1,...,4`, every radius `0,...,L`, and dimensions `m=1,2`: **28 cases passed**. The full-threshold grid cleaner was checked on all single-rail replacements of distance strictly below `1/2`, `h=2,...,9`: **1,020 cases passed**. Exact rational summation over the eight three-sample binary outcomes returned overlap `5/16`. These finite checks corroborate the elementary proofs; they are not universal verification, an SRC execution or a compiler/profile run.

No public action, model training, GPU run or external contact occurred.
