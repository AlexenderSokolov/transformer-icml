# Independent analytic review of deterministic vocabulary backend

**Disposition:** No mathematical defect found in the stated fixed-point error and bit-complexity bounds, subject to the explicit inherited assumptions and scope limitations below. This is not a proof of the inherited statistical theorem, a trained-model result, an implementation verification, or a novelty review.

## Immutable source bindings

- Backend reviewed: `deterministic_vocab_backend_v1.html`, SHA-256 `e532e78809c4edf7d4e47ec39ad548c06ad339c55e9f56b8d75a85ea86a7143b`.
- Four-block exact-real candidate: `../fixed_parameter_vocab_softmax_20261103_1639/gaussian_log_position_candidate_v1.html`, SHA-256 `bf7f6c3ab19472d83658a3dc5cf24b90514df96e145b578706504526045c14c8`.
- Gaussian rate addendum: `../fixed_parameter_vocab_softmax_20261103_1639/rate_improvement_addendum_v1.html`, SHA-256 `d21062d3d1bf660a955bba10df9c466cf0eabaa61e57251236b8a870e15f9ad7`.
- Three-block graph: `../fixed_parameter_position_decoder_20261103_1632/fixed_parameter_causal_candidate_v1.html`, SHA-256 `4141725b160d74288570dd2d02181cb7d14c22d691ac7cf53b38c93f6bb409b8`.
- Prior deterministic integer backend: `../fixed_parameter_integer_backend_20261103_1637/deterministic_integer_backend_v1.html`, SHA-256 `962ca335827e4366855a4229798b92ae910c0b3a1996a7b990193757befa98cc`.
- Boundary/prior addendum v2: `../fixed_parameter_position_decoder_20261103_1632/boundary_and_prior_addendum_v2.html`, SHA-256 `25dd4ff06226867aa79578766ac7eeaf41cd4a5fef59dd9c77d896120d908ee4`.

Method: source comparison and algebraic inequalities only, plus SHA-256 checks. No random, numerical, enumerative, simulation, or paper-code execution was performed. No reviewed source was modified.

## Calculations checked

1. **Exponential.** For 0≤d≤b, put a=1−d/H. Since H≥2b, 0≤d/H≤1/2 and −d−d²/(H−d)≤H ln a≤−d. Thus the ideal base-power error is at most 2b²/H. Each downward F-grid squaring contributes less than 1/F with error amplified by at most 2 per remaining squaring, totaling less than (H−1)/F<1/H. Conversion to the H grid costs less than 1/H. For d>b, e^(−d)<e^(−b)<1/H. X=0 is exactly preserved. The stated uniform bound ε_w=(2b²+2)/H follows.

2. **Log positions.** The recurrence Q_n=⌊Q_(n−1)T/F⌋ with T=⌊Ft⌋ gives |Q_n/F−t^n|≤2n/F by induction; division floors add at most 2/F per retained summand after the leading factor 2. Consequently the K-term error is at most 6K/F; for t≤1/3, a geometric bound gives tail ≤3·9^(−K). Since k≤s, the total pre-round error is at most (s+1)(6K/F+3·9^(−K)). The displayed sufficient inequalities follow from K=b+2≤33s, H=2^(32s), and 9^(−K)<H^(−3): 24(s+1)K<H and 12(s+1)<H² for s≥2. Rounding then gives |λ_j−ln j|<1/H. In particular λ_1=0; nonnegativity and λ_j≤s+1 hold.

3. **Normalized first-stage softmax.** A maximum-shifted exact weight of 1 corresponds to E(0)=H, so the approximate denominator is nonzero. The sum of absolute unnormalized weight errors is at most Lε_w and the exact denominator is at least 1. A standard numerator/denominator comparison gives an l1 normalized-weight difference at most 2Lε_w. For values in [0,1], this is a safe expectation bound; the output flooring adds <1/H. Since 2b²+2≤2^(16s) and L≤2^s, the claimed 2Lε_w+1/H≤3L^(−7) is conservative. The exact copy leakage 2/(e⁴−1)<2/15 and this numerical error <1/15 together remain below 1/5<1/4, preserving the ReLU snap. The original graph's BOS and valid-context gates are exact H-grid arithmetic. The terminal selector is one-hot, and the selected anchor incurs at most the same numerical attention error on top of (N/2)e^(−N).

4. **Length marker and Gaussian scores.** The block-1 marker is exactly 1 at j=1 and 0 at all other integer positions; the zero-score block-3 head produces z̃=⌊H/L⌋/H. Its error is <1/H. The two score maps match the exact-real candidate with p replaced by p̃; the score discrepancy at the same p̃ is j²|z̃−1/L|≤L²/H. This choice is important: the uniform Gaussian estimate is applied at p̃, not at the ideal p, avoiding an unproved Lipschitz bound in p.

5. **Softmax perturbation and logit budget.** For two score vectors whose entries differ by at most δ, the Hilbert distance of their exact softmax laws is at most 2δ. Cohen–Fausti Theorem 5.1 uses full l1 as its TV norm; dividing by two gives conventional TV≤tanh(δ/2)≤δ/2. For λ_j∈[0,s+1], this contributes at most (s+1)L²/(2H). Replacing ideal weights by the numerical normalized weights costs at most (s+1)2Lε_w. The λ approximation and output flooring each cost <1/H. This is exactly the stated E_h bound. The final binary softmax has l-infinity-to-output Lipschitz constant at most 1/2 because the l1 norm of its two-logit gradient is at most 1/2. Its numerical evaluation introduces at most 2ε_w+1/H by the same normalization argument and a final floor.

6. **Rate addendum.** The L-point discrete-Gaussian normalization bound, the 17√L first-moment estimate, and the split log-deficit estimate yield |G−μ|≤42√L for μ∈[0,L], including both endpoints. With the two means Lp̃ and L(1−p̃), the denominator argument gives the stated conservative min{1,168/√L} uniformly in p̃. Combining with the anchor and numerical terms yields the stated pathwise bound. For N=2, B_N=1/2 because there are no valid triples; the real or rounded selected head need not be exactly 1/2, and the bound correctly permits that. The risk conclusion additionally depends on the inherited R011 actual-terminal theorem, which was not independently reproved in this review.

7. **Resources and interpretation.** With b=Θ(log L), input i and i², all dyadic scores and residuals, and each F-grid intermediate have O(log L) bits up to constant factors; schoolbook operations cost O(b²). O(b) squarings per gap and O(L²) dense row/key visits give O(L²b³), while O(Lb³) log generation is included. Streaming attention rows and retaining O(L) constant-width residuals and positions costs O(Lb+b²) bits. The constant model weights do not depend on the horizon, but the implementation explicitly changes precision b=32⌈log₂L⌉ and the range/table size with L. This is a family of length-budgeted integer evaluations of one graph, not fixed-word, IEEE, bounded-logit, or fixed-precision execution.

## Residual qualifications

- This review checks the analytical backend and its linkage to the candidate graph. It does not verify a running implementation, a hardware benchmark, training, prior-art novelty, or formal proof-assistant output.
- The O(N^(−1/2)) uniform statistical risk claim is conditional on the actual inherited R011 theorem with its stated source and initial-law quantifiers; a distributable package needs that theorem and review, not just a fingerprint.
- The numerical softmax analysis presumes exact integer arithmetic, exact causal masking/max-shift, exact affine/gate arithmetic as specified, unbounded word range, and a supplied horizon L to choose precision. These are substantive assumptions, not generic floating-point guarantees.
- The Gaussian-rate source and graph are analytically checked here to the extent used above; the final result is still subject to independent editorial/architecture and primary-prior-art review.
