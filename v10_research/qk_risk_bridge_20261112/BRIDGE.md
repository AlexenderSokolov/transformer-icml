# A task-risk bridge for globally bounded positional QK factors

2026-11-12. New bounded-gain transfer lemma using the already established count-plus-endpoint Bayes obstruction. This is NOT a new proof of that obstruction and NOT a rank-only Transformer lower bound.

## Contract

A single retrieval stage at terminal T reads raw binary tokens through H full-prefix softmax heads. Let n be the number of keys, possibly including the terminal. Values have norm <=V_h and depend on each raw token through the same position-independent map; public additive constants may be separated out if their weighted contribution is explicitly controlled. A terminal value and terminal residual can depend on the freely supplied actual endpoint pair and public N. There is no other history-dependent bypass. Positional QK score factors may be nonzero and have arbitrary rank/dimension. For head h, the actual terminal query q_h and full key array K_h satisfy

    ||q_h||_2 <=Q_h, ||K_h||_F <=F_h, s_h=K_h q_h,
    ||s_h||_infinity <=S_h.

Any conventional 1/sqrt(d_k) scaling is included in q_h. The F_h bound is a GLOBAL array norm over all keys, not the norm of the learned key-projection matrix, and not a per-row key bound. Standard per-row bounds only imply F_h=O(sqrt(n)), which makes the result below vacuous for fixed-gain asymptotic separation.

After this retrieval, a decoder maps the concatenated head outputs and terminal residual to the probability of the next plus-spin. It is G-Lipschitz in the concatenated head-output Euclidean norm, uniformly in the public/free-endpoint inputs and along the comparison segments. This decoder may be nonlinear. Its total Lipschitz gain, including all downstream PreLN, final LN and softmax, must be charged. No additional retrieval of evolved/raw historical rows is allowed in this single-stage theorem.

## Deterministic softmax-to-summary estimate

For any score vector s with ||s||infinity<=S, let a(t)=softmax(ts), t in[0,1]. Its derivative is a_j(t)(s_j-E_a(t)s). Consequently

    ||a'(t)||_1 <=2 sum_j a_j(t)|s_j|
                  <=(2 exp(2S)/n)||s||_1
                  <=2 exp(2S)||s||_2/sqrt(n).

Integrate t from0 to1. The attention read v differs from its uniform-score counterpart v0 by

    ||v-v0||_2 <=2V exp(2S)||s||_2/sqrt(n)
                <=2V exp(2S)QF/sqrt(n).

This inequality holds pathwise, not merely on average. For H heads define

    C=2 sqrt(sum_h [V_h exp(2S_h)Q_h F_h]^2).

Their concatenated reads differ by <=C/sqrt(n). A fixed output projection can either be included in G or charged by its operator norm. The probability difference is <=min(1,GC/sqrt(n)). Thus score approximation alone is NOT the argument: a quantitative bound on downstream gain is the indispensable bridge.

## Direct prediction-risk consequence

Use P_theta(z|xy)=(1+theta xyz)/2 with uniform stationary pair, and equal prior theta=+h,-h for fixed0<h<=1-2c. Let B_N be the Bayes-optimal expected absolute next-plus-probability error among all predictors measurable in (S_N,X_(N-1),X_N). The existing count obstruction establishes

    B_N=(h/2)(1-TV(Law_h(S_N,pair),Law_-h(S_N,pair))) -> h/2.

The uniform-reference retrieval is a function of this summary, because the raw binary value map is identical across positions. Its downstream prediction therefore has equal-prior risk at least B_N. The pathwise triangle inequality now gives the NEW transfer statement

    R_equal_prior(actual QK predictor) >= B_N - GC/sqrt(n),
    sup_(theta=+/-h) R_theta >= max(0,B_N-GC/sqrt(n)).

For fixed Q,F,V,S,H and G=o(sqrt(n)), risk remains asymptotically at least h/2. A constant Lipschitz envelope per downstream block Lambda>1 implies G<=G0 Lambda^D; achieving risk below h/2-epsilon consequently needs G=Omega(sqrt(n)) and, under this bound, D>=log(n)/(2log Lambda)-O(1). This only concerns post-retrieval processing under the contract, not general evolving-KV depth.

Finite example h=1/2,N=10: the previously established exact B_10 is5347/32768=0.163177490234375. The lower bound subtracts the displayed gain-sensitive term; if that term exceeds B_10 the finite statement correctly says nothing.

## Relation to low-rank positional interfaces

This covers arbitrary nonzero rank-r QK satisfying global factor bounds, including rank growing with n; no rank lower bound is asserted. It addresses globally-Frobenius-bounded low-rank constructions directly: their tiny perturbations from a uniform read cannot produce small prediction risk through an insufficient-gain decoder. Exponentially small score constructions may demand much more than the sqrt(n) gain lower bound; the lemma does not optimize that cost. Exact-real injectivity plus an arbitrarily steep/discontinuous decoder is not excluded and does not violate this statement.

The present proof does not apply to general position-dependent value encodings, multiple interleaved contextualization/retrieval stages, hidden history bypasses, or mere bounds on projection matrices/per-row keys. A rank-only impossibility or a strict standard-PreLN realization is not obtained.

## Evidence

`check.py` independently checks the softmax norm inequalities for deterministic globally normalized nonzero QK factors and checks the risk triangle inequality by exhaustive stationary-word enumeration for a concrete smooth decoder. Binary64 diagnostics are not a universal certificate. The universal transfer proof is the elementary differentiation and triangle argument above. The imported count lower bound is an existing separately reviewed result, not claimed as new work here.
