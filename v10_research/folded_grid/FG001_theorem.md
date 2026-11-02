# FG001 — IID capacity frontier through a folded scalar grid

2026-11-02. New research candidate. Frozen earlier stages are unchanged. No novelty claim. Fresh independent review PASS; see FG001_independent_review.md. This is not a formal proof-system or emitted-network validation.

## 1. Precise experiment and conclusion

Fix J>=2, h>=1, Q=2^h, M>=1. Binary second-order sources have EVERY transition row equal to Bernoulli(p), p in [0,1]. The initial pair is arbitrary; the M generated symbols X_3,...,X_(M+2) are IID Bernoulli(p), independent of the initial pair. The actual terminal next-symbol target is p. The pair-chain has P^2(s,.)=Bernoulli(p) tensor Bernoulli(p), for every s, so these sources satisfy every beta in the usual stationary-witness class, including beta=1.

The terminal interface consists of exactly J coordinates in [0,1], each downward quantized at Q, plus a fixed finite boundary label with at most H values and public source-independent metadata. The boundary label is a function of the observed history (and permitted independent seeds), never an oracle for the unknown source parameter. No other source-dependent port survives. Decoder outputs may be arbitrary real Bernoulli parameters; in particular they are NOT restricted to a Q-grid. Source-independent randomization is allowed. Width and H are fixed, while bounded-primitive depth and paid work precision may grow with h.

For all encoders with this interface, regardless of their internal computation or depth,

    minimax risk >= max{3/(64 sqrt(M)), 1/[16 H(Q+1)^J]}.

Here the statistical lower fixes the initial pair to (0,0). Conversely, one explicit end-to-end causal zero-logit attention/ReLU encoder of width O(J), primitive depth O(1+(J-1)h), coefficients bounded by 4, and bounded scalar states has a fully finite implementation with

    sup_(p,initialization) E |p_hat-p| <= 1/(2 sqrt(M)) + 2/Q^J.

Consequently the best IID-only risk over this interface class, once that depth and paid capacity are permitted, is Theta_(J,H)(max{M^(-1/2), Q^(-J)}). This is NOT a full second-order Markov minimax theorem and NOT a depth-necessity theorem. It refutes an unrestricted growing-depth extension of a universal 1/Q lower for fixed J. It does not refute fixed-architecture theorems whose constants depend on depth, nor a theorem about a particular fixed prefix.

## 2. Geometry: J coarse labels locate one fine cell

Let T(u)=2 min(u,1-u)=2u-4 ReLU(u-1/2), for 0<=u<=1, and F=T^h. On the Q intervals I_k=[k/Q,(k+1)/Q], 0<=k<Q,

    F(u)=Q u-k             if k is even,
    F(u)=k+1-Q u           if k is odd.

The endpoint formulas agree on shared endpoints. This is proved by induction on h from the two branches of T. Define y_j=F^j(x), 0<=j<J, and labels k_j=floor(Q y_j), including the possible endpoint label Q.

Given a valid label vector, start with feasible closed interval C=[0,1] and affine representation y_0=x. At step j, intersect C with the inverse of [k_j/Q,(k_j+1)/Q] under the current affine y_j=a_j x+b_j when k_j<Q. Its slope magnitude is Q^j. The remaining interval has length at most Q^(-(j+1)). For the next step substitute the appropriate branch formula above, so the new slope has magnitude Q^(j+1). Shared endpoints cause no ambiguity because both branch formulas agree there. The use of closed intervals only enlarges the true floor-label fiber by boundary points.

If k_j=Q, impose y_j=1. Since a_j is nonzero, C becomes a singleton and x is known exactly. Later labels can be checked by direct forward evaluation (or ignored for a valid-input decoder). Invalid inputs may return 0. This singleton rule includes x=1 and every turning point without assigning a fictitious branch k=Q.

Return the lower endpoint a of C. It is dyadic with denominator dividing Q^J, and for every valid x,

    a <= x <= a+Q^(-J).                              (G)

The interval algorithm uses O(J) affine updates/intersections on signed integers/rationals with O(Jh) bits; no enumeration of Q^J cells or arbitrary-real operation is needed. Orientation is essential: one cannot simply interpret the labels as ordinary base-Q digits.

## 3. Causal bounded-primitive architecture

There are N=M+2 source positions and one synthetic terminal position n=N+1. At each history row t>=3, a uniform zero-score head pools the bits X_i over 3<=i<=t; at terminal it pools 3<=i<=N. Rows 1,2 have public singleton self fallbacks. These masks have density at least 1/3 for history rows t>=3, and M/(M+3)>=1/4 at terminal (a common density 1/4 suffices). All allowed attention weights are positive. Input preprocessing has radius one and contains no future boundary dependence. The synthetic terminal may receive the permitted exact boundary label, but this construction ignores it.

At EVERY history row, the pooled scalar is that row's causal prefix mean, not the final mean copied backwards. At terminal it is x=(sum_(i=3)^N X_i)/M. Retain x, advance a working rail through h copies of T, retain F(x), and continue until F^(J-1)(x) is retained. Width O(J) stores only the J required output rails plus O(1) working rails. Each T uses r=ReLU(u-1/2) then u'=2u-4r, retaining old u until the affine update finishes. These are two bounded-size primitive stages, not a growing DAG concealed in one layer. All retained nonnegative rails are in [0,1]; signed preactivation u-1/2 lies in [-1/2,1/2]. Coefficients have magnitude <=4. Readout is the J-coordinate projection. Optional zero-value dummy attention heads must be charged if the syntax requires attention at each stage.

This deliberately uses global nonlinear features of the mean. A local-ratio 1/Q obstruction cannot be applied to this changed encoder. Stronger assumptions such as fixed depth, fixed total primitive budget, output Q-grid rounding, or finite work precision smaller than the following prescription would describe different experiments.

## 4. Exact finite evaluator, including generic FA admission

Choose P>=Jh and D_f=2^P. At each row with m valid bits and count A, compute U_0=floor(D_f A/m) by integer division. Rows 1,2 use their public fallback. All fine tent updates are EXACT integers:

    U <- 2 min(U,D_f-U).

Equivalently evaluate ReLU(U-D_f/2), then 2U-4ReLU(U-D_f/2). P>=1 ensures the half-bias is exact. The affine/ReLU integer evaluator has no intermediate rounding loss in this computation; negative half-preactivations and endpoints are exactly represented. Zero remains zero, D_f maps to zero, and D_f/2 maps to D_f.

At retained rails emit k_j=floor(Q U_j/D_f). These are the exact labels of x_hat=U_0/D_f under the folded map. Decode using Section 2. Since x_hat<=x<x_hat+2^-P,

    0 <= x-a <= Q^-J+2^-P <= 2 Q^-J.                (F)

Although T is not monotone, no one-sided tent-output claim is made or needed: the decoder recovers the initial fine scalar, not an inverse under a globally monotone map.

The SAME signed Taylor/affine finite family used by FA001 can realize this schedule: zero logits yield identical positive Taylor weights, which cancel exactly in the attention ratio; all affine tent coefficients and half-biases are exactly representable and all products are fine-grid integers. Identity rails and zero-value dummy heads remain exact. A larger sufficient generic-family prescription is P>=max{Jh,4h+c(d+2)}, where d is actual bounded-primitive depth and c is the fixed constant from GD001's uniform FA extension. This generic extra precision is paid, not hidden. It changes no label geometry or risk argument.

A direct stronger certificate here avoids any depth-dependent black-box constant: T^r is 2^r-Lipschitz, so at every folded rail the discrepancy from the ideal mean-based rail is at most 2^((J-1)h)2^-P <=1/Q. The same bound covers intermediate folds and all formal histories/rows. Thus this concrete family satisfies a uniform pre-cut E/Q contract with E=1 even at growing depth. Exact equality of ideal and finite final floor labels is neither needed nor asserted.

## 5. Risk and alphabet lower

The generated bits are IID, so E|x-p|<=sqrt(p(1-p)/M)<=1/(2 sqrt(M)). Add (F). For binary probability vectors this absolute error is precisely TV error.

For the interface lower let R=H(Q+1)^J. Fix all independent random seeds of encoder and decoder; the decoder has at most R scalar outputs z_1,...,z_R. Under a uniform prior on p in [1/4,3/4], write ell=1/2 and epsilon=ell/(4R). The union of their epsilon-neighborhoods covers prior mass at most 2R epsilon/ell=1/2. Outside that union EVERY possible decoded message has error >=epsilon, irrespective of how the stochastic sample chooses a message. Hence prior risk >=epsilon/2=ell/(8R)=1/(16R). The bound is uniform in the seed, so integrating it handles randomization. This argument neither assumes a noiseless parameter-to-message map nor conditions the prior on a good event.

For the separate full-history floor fix the initial pair to (0,0), let p_±=1/2±1/(16 sqrt(M)), and delta=p_+-p_-=1/(8 sqrt(M)). One-observation chi-squared is delta²/[p_-(1-p_-)]<=1/(12M), since p_-(1-p_-)>=3/16. For M observations chi-squared <=exp(1/12)-1<=1/11, so TV between sample laws <=1/(2 sqrt(11))<1/4. The standard minimum-density triangle inequality yields average absolute risk >=delta(1-TV)/2>=3/(64 sqrt(M)). This applies to any interface estimator by data processing. The two lower witnesses need not coincide; combine their risks by maximum.

At h=ceil(log2(M)/(2J)) (and at least 1), Q^J>=sqrt(M), so the construction attains statistical order with O(log M) primitive depth and h=(log2 M)/(2J)+O(1) as the grid precision exponent. Because endpoint Q is included, a raw fixed-length label uses h+1 bits (alphabet size Q+1), so the total label bit count is J(h+1), still approximately half log2 M: this is packing across J coordinates, not a free loss of information requirements. Internal work precision is larger and paid.

## 6. Fully paid finite-resource ledger

This is an existence ledger, not an efficiency-optimal claim. Let d=O(1+(J-1)h), n=M+3, and w=C_J(P+log2(n+1)+log2(d+1)+1), with an absolute sufficiently large integer factor. Count dividends, exact common attention weights, addresses and signed tent/decoder numerators fit these guarded words; multiplication uses 2w-bit products. Decoder affine coefficients have O(Jh) bits. With generic Taylor evaluation increase the fixed factor to cover FA001's bounds.

A conservative direct implementation, including dense masks and optional dummy heads at every stage, has elementary bit-operation budget

    T0=O_J(d n² (P+1) w² + (d+n)w²),
    S0=O_J(d n² + d J² w + n J w + w^4).

The (P+1) factor is unnecessary for bespoke exact uniform pooling but safely pays generic Taylor evaluation. These bounds pay all tokens, every dense-mask entry including excluded edges, dense affine/QKV zero slots, input acquisition, public positions and local tables, coefficient and mask generation, layer counters, rolling hidden arrays, exact counts/divisions, final quantization, O(J) interval decoder arithmetic, outputs and clearing/isolation. Public coefficient descriptions are only O(1) bits here except parameter/position records; masks have d n² bits if separately stored. The bound deliberately permits full mask storage rather than claiming free implicit masks. No history array, count, denominator, unquantized rail or discarded token output is accessible after the cut. They may be overwritten, with the zeroing work paid.

To avoid any random-access unit-cost assumption, compile the fixed-loop arithmetic into a bounded-arity addressed tape program. Storing O(T0 w) instruction/address bits and scanning an S0-bit data tape for each instruction gives safe forward bitwork O(T0 S0 w), peak O(T0 w+S0), and offline generation bitwork O((T0+S0)w²) with its scratch added. These loose bounds already include decoder work. A Boolean/ReLU PURE compilation is a separate larger-depth representation; no claim that it has O(log M) Boolean depth or fixed width is made. The O(log M) claim concerns the ideal attention/affine/ReLU primitive architecture with its paid finite evaluator.

## 7. Attribution and evidence boundaries

The tent-map/ReLU folding idea is established. Telgarsky, *Benefits of depth in neural networks*, COLT/PMLR 49 (2016), pp.1517–1539, Section 3.3, Lemmas 3.8, 3.10, 3.11 and Corollary 3.9 explicitly develop the same triangle function and repeated folds: https://proceedings.mlr.press/v49/telgarsky16.html and https://proceedings.mlr.press/v49/telgarsky16.pdf . This note supplies the present finite-label decoder and IID experiment analysis; it makes no originality claim for either these or the general depth/precision idea. Only generic bibliographic searches were sent externally; private proof material was not uploaded.

Inherited interfaces consulted: CA001 v3 plus its boundary-causality scope note; FA001 v3; GD001 uniform FA extension. The mathematical interval and alphabet arguments above are self-contained. Executable diagnostics test exact arithmetic on finite cases, not a replacement for proof or an emitted-network audit.
