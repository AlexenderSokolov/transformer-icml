# Independent analytic review: fixed-parameter perturbations

**Disposition.** No mathematical error found in the stated exact-real perturbation bounds and counterexample, under the specified choice of model realization, fixed dimensions and exact softmax. The bounds are intentionally very conservative. This is not an IEEE numerical analysis, an end-to-end lower bound, a training result or a formal verification.

## Hash-bound inputs and method

- Report `perturbation_bounds_v1.html`: SHA-256 `d92ec0a43232dbaa9c20e9eef65e24d4d4623d2ae822d5d488c31effbf20d802`.
- Four-block candidate `../fixed_parameter_vocab_softmax_20261103_1639/gaussian_log_position_candidate_v1.html`: SHA-256 `bf7f6c3ab19472d83658a3dc5cf24b90514df96e145b578706504526045c14c8`.
- Gaussian rate addendum `../fixed_parameter_vocab_softmax_20261103_1639/rate_improvement_addendum_v1.html`: SHA-256 `d21062d3d1bf660a955bba10df9c466cf0eabaa61e57251236b8a870e15f9ad7`.
- Three-block graph `../fixed_parameter_position_decoder_20261103_1632/fixed_parameter_causal_candidate_v1.html`: SHA-256 `4141725b160d74288570dd2d02181cb7d14c22d691ac7cf53b38c93f6bb409b8`.
- Integer backend `../four_block_integer_backend_20261103_1645/deterministic_vocab_backend_v1.html`: SHA-256 `e532e78809c4edf7d4e47ec39ad548c06ad339c55e9f56b8d75a85ea86a7143b`.

Method: analytic inequalities, direct source comparison and SHA-256 checks only. No random or numerical experiments, enumeration, simulation or scientific-code execution; no source overwrite.

## Oscillation and snap guarantee

For exact softmax distributions whose score vectors differ by Δ, the Hilbert distance is osc(Δ). The standard sharp bound therefore gives conventional half-l1 TV at most tanh(osc(Δ)/4). The ideal values range in [0,1], so the change in their expectation is bounded by that TV; replacing values by perturbations of absolute size ≤ν costs at most ν, and a separate weighted-output error costs τ. At i≥4 the ideal lag-copy leakage is ≤2/(e⁴−1)<2/15, giving the stated 2/15+tanh(ω/4)+ν+τ. If this is below 1/4, an ideal bit 0 has copy value <1/4 and an ideal bit 1 has copy value >3/4, so the exact fixed T gate returns it exactly. The available conservative margin is 1/4−2/15=7/60. These conclusions require the stated support and exact gate parameters; the separate global theorem covers perturbed gates only through output error, not preservation of an exact snap.

## Positive-coefficient perturbation and BOS values

With r=i−h, direct subtraction yields s_(h,η)(i,r)−s_(h,η)(i,r−1)=i[1−η(2r−1)]. If η(2r−1)>1, the neighbor alone has more softmax weight than the target and the target mass α<1/2. Choose target data bit 1 and all other data bits 0, while retaining the two actual BOS values 1/2. The copied value is α+(1/2)P(BOS)≤α+(1/2)(1−α)=1/2+α/2<3/4, so T is not 1. For all-word copy preservation through length L, this implies η≤1/(2r−1) for the relevant last valid positions, hence the necessary O(1/L) coefficient scale. The selected term corresponds to perturbing the fixed coefficient multiplying i in the second query coordinate; this is an actual matrix-entry perturbation up to the fixed score-scaling factor. It is not an end-to-end risk lower bound or a statement about other architectures.

## Explicit positional score error

The score is 2(i²−hi)j−ij², where i, i², j and j² are separately supplied coordinates. If each has an independent additive error of absolute size at most δ≤1, expansion and the triangle inequality for h≤2, i,j≤L give

|Δs|≤[2(1+h)L+2L²+2(1+h)+L²+L+1]δ
       ≤(3L²+7L+7)δ≤10L²δ   (L≥4).

This is a raw per-entry bound; a row-common part cancels and may reduce oscillation. The Gaussian score change from p,z alone is bounded by 2L|Δp|+L²|Δz| when positions are fixed.

## Activation bound and block recurrence

The source graph admits the claimed realization with entries/biases ≤16, including the lag-two coefficient 16; perturbation by ε≤1 makes them ≤17. R=129·17=2193 accounts for at most 128 incoming coordinates plus a bias. For any scalar activation bound B≥1, an affine map is bounded by RB. Convex averaging preserves the V bound RB, and output projection plus residual is ≤2R²B. Two FFN affine maps, ReLU and their residual give a block bound ≤4R⁴B<2⁵⁰B. Starting from inputs ≤2L², four blocks and all internal affine outputs are safely ≤B_L=2²¹⁰L². This is a bound on affine activations, not on raw Q·K logits.

If incoming coordinate error is E, one affine error is at most T=R(E+B_L ε), using the B_L bound for the unperturbed input and perturbed-entry bound 17. Each head has 16 coordinates and score scaling 1/4; the bilinear telescoping inequality gives score sup error ≤(16/4)·2B_LT=8B_LT. The corresponding softmax TV is ≤4B_LT. Since values lie in [−B_L,B_L], weight change costs ≤8B_L²T and V change costs ≤T. Thus each head coordinate differs by ≤9B_L²T. The output projection plus residual is bounded by 11R²B_L²(E+B_Lε), safely absorbing direct entry and residual errors. Two further affine perturbation bounds, ReLU 1-Lipschitzness and FFN residual give E_next≤24R⁴B_L²(E+B_Lε)=K_L(E+B_Lε), with K_L<2⁵³B_L².

Because K_L≥1 and E_0≤δ, iteration gives E_4≤K_L⁴(δ+4B_Lε). The final affine map costs ≤R(E_4+B_Lε). Final vocabulary softmax in conventional TV is ≤half the score l-infinity difference. Substituting B_L=2²¹⁰L² and K_L<2⁵³B_L² gives coefficients bounded by 2¹⁹⁰³ for L¹⁶δ and by 2²¹¹⁶ for L¹⁸ε; the report's common factor 2²¹²⁰ safely covers both. The cap at one is valid for all distributions, and δ,ε≤2^(-2124)L^(-19) indeed make the additional error O(1/L).

## Scope of risk and numerics

For each word, TV(output perturbed, target)≤TV(output perturbed, ideal output)+TV(ideal output, target). The perturbation bound is uniform in words, so averaging and then taking a source supremum preserves it. The underlying O(N^(-1/2)) risk rate remains conditional on the linked exact-real Gaussian argument and inherited R011 actual-terminal theorem; this review does not reprove that theorem. Uniform vanishing perturbations give vanishing additional risk, while the displayed O(1/L) example preserves the baseline rate.

The unbounded-length integer backend stores the specified integer coefficients exactly, computes paid integer positions exactly, and charges growing fixed-point precision and logarithm/exponential approximations. It is not subject to the nonzero coefficient perturbation in the counterexample. Conversely the exact-real ε,δ model does not account for roundoff, underflow, overflow, non-exact matrix multiplication or any particular IEEE softmax implementation. A fixed η can invalidate the copy-gate proof without proving that the overall predictor's risk is inconsistent.
