# Verified primary references: evolving K/V without layerwise mixing

Verified on 2026-11-12 by reading the linked primary HTML theorem statements. This is a contract comparison, not independent verification of every source proof or a novelty certification.

## Duerinckx, Geshkovski, Rossi

Exact title: Kinetic theory for Transformers and the lost-in-the-middle phenomenon.
URL: https://arxiv.org/html/2605.09213v1
Theorem 1.1(ii): independent initial tokens, initial characteristic-function profile converging at rate N^-delta with controlled frequency growth; smooth test functions. The evolving empirical measure has RMS test-function error O(N^-min(delta,1/2) exp(Ct)). No independence or mixing is imposed anew at each evolved layer/time.

This is a genuine source-average propagation predecessor. The main model is continuous-time causal interacting particles on the circle with simplified normalization. Section 1.2.2 discusses general self-attention separately. Neither initial independence nor this simplified continuous-time model directly covers our correlated binary Markov input and discrete full-PreLN architecture. Time t must not silently be identified with a discrete layer count without a discretization argument.

## Castin, Ablin, Carrillo, Peyre

Exact title: A Unified Perspective on the Dynamics of Deep Transformers.
URL: https://arxiv.org/html/2501.18322v2
Theorem 6: integrable time-varying Q,K,V, compactly supported initial measure, common position marginal theta with theta({0})>0. It establishes global well-posedness and stability for masked Transformer PDEs, including normalized softmax, in conditional Wasserstein distance. Stability constants depend on time, support radius, parameters, and theta({0}). No layerwise mixing is required.

Our applicability assessment: per-position single empirical samples versus a two-point reference do not approach one another in this conditional metric. A single sentinel's mass 1/N gives no automatic uniformity in the atom-dependent constant. This theorem therefore is not a turnkey N^-1/2 terminal approximation. It is also a continuous-time attention PDE rather than the full discrete PreLN/MLP stack.

## Shuyang Xiang

Exact title: A Conditional No-Hair Theorem for Transformers: How Language Models Forget Their Prompt.
URL: https://arxiv.org/html/2610.24133v1
Theorem 1 and Section 4: under the paper's normalization non-degeneracy and bounded-logit assumptions, finite-depth PreLN stacks with evolving K/V satisfy delta_L(t) <= C_L P (L+ln t)^(L-1)/t, C_L <= K3 sum_{m=0}^{L-1}(K1+2K2)^m. The comparison uses different initial prompts followed by the same continuation; the argument is pathwise and assumes no source mixing.

Our applicability assessment: this is a direct architectural influence-propagation predecessor. Two full histories drawn under different Markov parameters generally do not have a shared continuation, so its theorem cannot be substituted directly into that source-average risk comparison. Positive-epsilon normalization can provide a Lipschitz bound, but the precise normalization and constants must still be translated rather than asserted identical.

## Positioning conclusion

Do not claim that evolving-K/V propagation without layerwise mixing is itself new. A defensible narrower candidate is a finite-prefix, correlated discrete-source approximation for full normalized discrete PreLN, with explicit depth/gain constants and a terminal statistical risk transfer. The verified theorems above do not directly establish that combined contract; this finding does not certify originality. Xu-Fang's separate equilibrium-layer theorem remains an additional necessary comparator, and is not resolved by this comparison.
