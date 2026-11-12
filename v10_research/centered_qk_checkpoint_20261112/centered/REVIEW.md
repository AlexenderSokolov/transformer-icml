# Independent centered-key D-stage bridge review

2026-11-12. Reviewed THEOREM.md. No gap found under its retained computational/value/domain assumptions. This is analytical review, not a new risk experiment.

The row-gauge identity softmax(Kq)=softmax(PKq) is pathwise and permits data-dependent query/key means. The softmax Jacobian annihilates constants and has operator norm at most max probability <=e^Omega/i throughout interpolation. Hence the stated attention error V e^Omega ||Ps||/sqrt(i) is correct, including the optional explicit centered additive bias term. Only constant row offsets vanish; arbitrary external biases cannot be omitted.

The full-array centered SSE controls each prefix-centered SSE because the prefix mean minimizes its own least-squares objective, and using the full mean gives a prefix sum bounded by the full sum. This remains true when the terminal depends on the free endpoint pair. It does not require prefix/full means to coincide and is not a probabilistic claim.

The key-array condition is needed only on ACTUAL realized states: the proof first removes actual attention weights, then compares values. No key-energy or query-state Lipschitz bound on artificial references is needed. However reference states must still lie in the common value/local-map domain, and all value bounds, local Lipschitz constants, projection invariance and final-readout Lipschitz assumptions remain essential.

Replacing the previous forcing by V e^Omega(Q Fc+Bc) leaves the fixed-D recurrence and risk proof intact. Terminal self-value cancellation continues to remove any conditional-endpoint factor. The count-retaining variant is valid only with the retained homogeneous raw maps/no-bypass restrictions; centering does not relax these.

The nonuniform prefix recursion is correct. For alpha=1/2-beta in (0,1/2], the power-sum inequality sum j^-alpha /i <=i^-alpha/(1-alpha) gives the stated coefficient. At beta=1/2 no decay follows. Global Fc(N) must remain inside E_D(N); a growing score oscillation contributes exponentially and cannot be absorbed into an N-independent constant.

Identical nonzero keys demonstrate genuine strict improvement over the raw-array norm premise. Conversely bounded parameters/per-row activations need not yield small centered key energy, as the separate positional and content-key examples show. No low-rank-only or unrestricted multi-layer risk result follows.
