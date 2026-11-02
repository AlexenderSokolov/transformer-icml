# BF001 v2 — independent family synthesis and finite-interface review

**Verdict: PASS within the stated fixed-parameter, one-global-summary-block scope.** No blocking mathematical or finite-interface defect found. This is independent LLM review, not formal verification or an executed original-network benchmark. The v1 omission of boundary-port acquisition costs is materially corrected, not waived.

Reviewed candidate: `bounded_attention/BF001_encoder_family_frontier_v2.md`, SHA256 `bc97fc6fd402a84b2cd2b5e100ae1c905915629aa8c9d5b71e40cdeaf6e05925`. All ten entries in its v2 source manifest match both SHA256 and byte length. Source bodies read include BA001 throughout, FR001 throughout, NB002 §§1–2, SM002 §§1–2, and actual SRC proof §§2,4,8,9.2–9.3. Acceptance receipts establish prior scope, not substitute for these body checks.

## 1. Generic lower and minimax quantifiers

BA001 actually states a uniform lower over scalar ratios with all M keys, bounded local influence, positive lower weights, bounded values, and exact finite boundary side information. Shared denominators are legal. Its seedwise argument uses an encoder-independent prior; source-independent common randomization cannot choose a different favorable witness after observing the seed. The IID floor in BA001 §8 is a family theorem, not the original-SRC SM002 theorem imported into a larger architecture class.

The three simultaneous bounds used by BF001 are valid: the full-history stationary floor is at least `s/256`; the IID bound is `c_I/Q`; and the rare-suffix logarithmic bound has the stated minimum and constant `c_B`. Taking their maximum, rather than adding witness risks, justifies the ensuing comparisons.

Checked domain completion algebra:

* If beta>1/16, `W<=1/Q+16/M<=1/Q+2s` for M>=64, giving the displayed coefficient `1/c_I+512`.
* Outside Q<=min(M/4,M^(3/4)), `W<=5 Q^(-3/4)`. When Q>M/4, `4^(3/4) M^(-3/4)<=M^(-1/2)` exactly requires M>=64; when Q>M^(3/4), the exponent is -9/16. Both imply `W<=5s` and the coefficient 1280.
* Inside that domain, x>y implies x<=Q<=y^3. Thus `ln(1+x)<=3 ln(1+y)`. Bernoulli gives `ln(1+t)<=8 ln(1+t/8)`. The factor 24 and `1/c_I+24/c_B` follow. The case x<=y needs no factor 3 but is safely included.

Hence c_F H is correct. Allowing tables to know beta does not affect the uniform lower. The stationary source set is a subset of the arbitrary-initialization set with the same observation contract, so the middle minimax inequality has the correct direction. An admissible single beta-blind upper suffices after encoder optimization; no assertion that every encoder is good is needed.

## 2. Actual SRC, not ideal softmax

The actual SRC proof establishes downward finite log approximants, so every realized score is nonnegative and at most its ideal score, at most ln 6. Its exact recurrence gives `0<=T_j/R<=z^j/j!`, including `T_0/R=1`, hence `1<=W(z)/R<=6`. The full scores 0,L2,2L2,L3,L2+L3 are evaluated separately; the combined score is not implemented by multiplying rounded cache entries. Exact integer numerator/denominator sums followed by the final floor yield exactly the BA ratio representation after common R cancellation. No approximation claim is being mistaken for exact membership.

At the synthetic terminal position the four statistical heads scan precisely 3,...,M+2. Predecessor-copy heads produce local lag1/lag2 bits; they do not make statistical keys nonlocal. F_i is `1{i=3} e_(X_2)`, a triple-local feature at i=3 and zero otherwise. Values are bits. Query, endpoint correction, mode and surviving flags are functions of boundary symbols and public metadata. Statistical h0,f,rho remain inside the quantized bank, not exact side ports.

The coordinate count is `2K+2K+2K+(3K+1)=9K+1`, not the physical-head count. The original implementation has four statistical heads plus two singleton-copy heads. Constant-zero padded scalar coordinates with weight one are legal and disclose no information. The original NB002 suffix can ignore all surplus S entries and padding. NB002 §2 specifically extends only the retained prefix to h>=4 and avoids the old positive-r0 suffix; thus the legal grid domain matches BF001 and FR001.

## 3. Boundary realization, costs and lifetimes

The original six heads do **not** produce arbitrary first/last r windows. BF001 v2 no longer claims they do. A concrete completion of its proposed construction is: for each distinct requested boundary index j, add a zero-score singleton head that selects j in rows where j is causally available and selects self otherwise. At the final synthetic row all requested indices are available. For r exceeding history length use the min(r,M+2) convention inherited from BA001, and duplicate overlaps consistently. At most 2r heads suffice. A singleton bit output remains exact on every Q-grid.

These heads are acquisition for the explicitly permitted S side information, not hard-masked statistical summaries masquerading as the dense ratio block. They must not feed new nonlocal features into statistical key tables. Their only surviving data-dependent outputs are the designated boundary symbols. Finish/pay all historical rows, retain q's boundary bank, and release other copy outputs, original history/QKV, clean weights, numerator/denominator/remainders before exposing the augmented master cut. This realizes precisely (Z,S), not a historical reread port. SRC §8 supplies the original release schedule; the added boundary heads can be run before that release.

The added conservative charges are adequate in the declared fixed-K,D,r comparison: 2r public masks cost O(r n²), full historical scalar copies O(r n K p), separate head projections O(r K² p), and even scanning/evaluating every candidate edge fits O(r n²(K+p)p²). Boundary-index generation, output movement, controller/address state, zero padding, offline writes and simultaneously live buffers are explicitly charged rather than called free. Projection and copy buffers can be allocated per head/streamed; no requirement to form a gratuitously dense cross-head rK-by-rK transformation is imposed. Retaining S through the decoder is real live storage, included in the stated extra buffers and phase-sum rule.

This acceptance is **not** a uniform sharp resource theorem in growing D or r. Literal large-architecture address widths would require accounting for log D/log r if they exceed the retained public word capacity; one can cap boundary acquisitions at the actual history length. The candidate explicitly restricts the conclusion to fixed parameters and disclaims identical numerical resource constants and equal exact head count. An at-most-D implementation needs no padded bank; an exactly-D implementation must pay its actual padded output/representation. No lower bound on physical head count follows from D scalar coordinates. PURE expansion must use the augmented actual live memory/work, not reuse an unaugmented numerical ledger.

## 4. Interpretation and remaining limitations

The result is a valid family-minimax strengthening over a single SRC encoder, but only for a fixed number of bounded dense scalar ratios over fixed-radius local windows, plus bounded boundary information. Exact global preprocessing, source-dependent hidden tables, query-dependent selected interior domains, growing effective score range, unrestricted historical ports, or multiple recursive global-summary stages are not covered. Arbitrary downstream computation after the cut is covered. No training-convergence, joint-K optimality, novelty certification, or measured resource advantage is established.

No frozen source was edited. Machine-readable review bindings are in `BF001_review_v2.json`.
