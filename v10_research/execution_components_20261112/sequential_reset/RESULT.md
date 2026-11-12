# Sequential reuse: a proved reset component, not a complete statistical predictor

2026-11-12. This bounded attempt isolates a genuine missing composition step. It does not establish the proposed O(N log N) end-to-end baseline, let alone the O(log N) target.

## Actual PreLN scratch reset

Let width be 2m, epsilon=1, gain=1 and shift=0. All clean states consist of opposite coordinate pairs. Select k pairs as scratch, with scalar vector w; hold all other physical coordinates fixed. Their energy gives C=1+sum(nonscratch scalar squares)/m >=1. Full LayerNorm has divisor d=sqrt(C+||w||^2/m). A zero-attention residual block whose FFN writes minus each selected normalized coordinate into that coordinate (and its opposite into the paired coordinate) implements

    T_C(w)=(1-1/d)w.

This is a genuine fixed-width ReLU FFN: represent the linear map using positive and negative ReLUs. Its per-layer Frobenius bounds depend only on k. Both block normalizations retain positive epsilon; attention output is zero. No unknown inverse or comparison is evaluated.

Assume a common full-state norm bound H. Then d<=D=sqrt(1+H^2/(2m)). T preserves signs, decreases scratch norm, preserves exact pairing and the clean mean zero, and leaves every nonscratch coordinate exactly unchanged. On the fixed-C scratch ball, its Jacobian has tangential eigenvalue 1-1/d and radial eigenvalue 1-C/d^3. These lie in [0,1-D^-3]. Therefore

    ||w_L|| <= q^L ||w_0||, q=1-D^-3<1.

The full paired scratch norm is sqrt(2)||w||. Starting full scratch norm at most H, L>=ceil(log(H/epsilon)/(-log q)) suffices for full-state reset error epsilon. If H=0 the scratch is already zero and no logarithmic formula is needed. Different rows may have different C: the same depth and same weights work uniformly. C need not be known or constant across rows, only fixed during the reset blocks. This is linear-rate approximate reset, not the stronger cubic damping requiring known C, and not exact reset on an open continuum.

## Robustness, persistent registers, and mean

If paired scratch-only additive errors per block have full norm at most delta, the reset error is at most q^L H+delta/(1-q), PROVIDED the common H bound covers every actual perturbed state before and after each update (or a separate invariant-ball proof supplies that bound). An initial clean-state bound alone does not supply this noisy-trajectory hypothesis. Errors in held nonscratch coordinates are not removed; if held fixed during a reset their altered energy is allowed by the same common bound. Arbitrary full-vector errors need not preserve pairing. A common-mode error is invisible to LayerNorm and cannot be reset by this operation. Thus the clean lemma does NOT imply a contraction of full physical state under arbitrary errors. Any claim that it protects a continuously evolving accumulator against arbitrary errors needs a separate argument.

## What sequentially computing innovations would additionally require

For each t=3,...,N, one could schedule public source indices t-2,t-1,t, broadcast three bits to the terminal, form their product, add product/(N-2) to a persistent statistic, and reset temporary registers. Publicly varying layer coefficients are permitted only if the original model allows N-dependent, layer-dependent bounded parameters. Scheduling all t costs Theta(N) calls, not a logarithmic-depth statistic algorithm.

The audited width14 single-source module cannot be dropped unchanged into this schedule: retained bits and the accumulator change its normalization, gate margins and fixed points. A wider common architecture requires a new all-row proof. The terminal product gate, bounded accumulator increments and final normalized probability/logit readout must also be compiled; none is free. A large fixed anchor could narrow the normalization interval and separate a finite bit codebook, but this note does not claim that suggestion is a completed compiler.

Conditional bookkeeping: if those additional modules are proved uniformly on a fixed common state ball, each call costs O(log N+log(1/epsilon)) layers. If the actual composed system admits at most linear accumulated perturbation K N epsilon, choosing epsilon=eta/(K N) gives D_total=O(N log(N/eta)). Per-layer norms can remain fixed while the sum of squared parameter norms is O(D_total), and the concatenated Frobenius norm is O(sqrt(D_total)). There is no fixed global total-parameter-energy conclusion.

Crucially linear error accumulation is NOT yet established. With only generic per-layer Lipschitz bound B>1, the safe numerical error bound is delta times sum_{s<D_total} B^s. Writing delta=2^(-p), a sufficient error-radius exponent is p=O(D_total log B+log(D_total/eta)), with coefficient margins charged separately. This is not a storage-bit theorem. Only under a specified bounded-range arithmetic scheme with certified per-site errors can this exponent be interpreted as a sufficient fractional-bit budget; range bits must then also be charged. It does not justify p=O(log N). At D_total=O(N log N), this generic sufficient error-radius exponent is O(N log N), not a proved polylogarithmic arithmetic budget. Structural stability of retained bits and accumulator would be needed to improve it.

## Statistical interface only

For the stationary spin source, innovations Z_t=X_{t-2}X_{t-1}X_t are iid signs of mean theta, and m=N-2 observations give E|mean Z-theta|<=1/sqrt(m). If a future compiler outputs an estimate with expected absolute discrepancy at most eta from this mean, clipping to [-a,a] is nonexpansive. Given the true terminal product T, the ideal probability (1+clip(estimate)T)/2 then has risk <=1/(2sqrt(m))+eta/2. An approximate endpoint or probability head needs its own charged errors. This is a conditional statistical consequence, not an established actual-transformer predictor.

## Diagnostic

check.py checks the actual paired-state LayerNorm reset, unchanged persistent lanes, full paired error and a deliberately unreset common-mode perturbation. It does not execute the unfinished sequential statistic construction. No training or asymptotic empirical risk claim is made.
