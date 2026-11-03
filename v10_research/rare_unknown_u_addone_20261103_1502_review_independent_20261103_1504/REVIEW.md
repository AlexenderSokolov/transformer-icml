# Independent analytic review: unknown-u add-one rate and network

Reviewed artifact: `v10_research/rare_unknown_u_addone_20261103_1502/unknown_u_addone_matched_rate_v1.html`  
SHA-256: `37a1b01e27f315097c5c910005605b877ba9b6d0de160940c7acc375b6af849b`  
Review type: mathematical and declared-model audit, without RNG, numerical tests, enumeration, external writes, or alteration of the reviewed artifact. The hash was independently read with `sha256sum` and matches the requested binding.

## Verdict

The conditional statistical proof, exact-real network identity, and selected-port error bound are sound under their stated setup. One correction is required to the statement about fixed-point rounding: “b-bit fixed-point” by itself does not guarantee the claimed quantization error. Define the quantization grid explicitly, for example as spacing 2^(-b) with the entire interval [0,1], including 1, representable; equivalently use b fractional bits with enough range/encoding to include 1. Nearest rounding then has error at most 2^(-b-1). A general format whose total word length is b bits may have sign/integer bits or a different step, so the displayed error need not hold. The separate 3ε/2 port result does not depend on this wording and remains valid.

## Statistical argument

For the conditioned stationary process, reverse time starts at Z_0=00 and has exactly the stated reverse kernel. R²(s,11)≥1/8 for every s, since its last column is (t/2, (1-h)/2, 1/4, 1/4) and h=ut/w<3/4. Therefore the two-step contraction factor ρ=7/8 applies. The geometric sums are Σ_(j≥0)ρ^⌊j/2⌋=16 and Σ_(h≥1)ρ^⌊h/2⌋=15, giving |EJ−Mu|≤16. For i<j, covariance is at most 2 E I_i ρ^⌊(j−i)/2⌋ in absolute value, yielding Var J≤61 EJ≤61(Mu+16).

In the conditioned reverse filtration, each 1{Z_j=00}(1{Z_(j+1)=10}−t) is a martingale difference. Thus E D²=t(1−t) EJ≤(Mu+16)/4; no independence between J and D or post-conditioning of a forward martingale is used.

The occupation counts differ by δ=1−1{S_2=00}; arrivals into 00 from 10 minus departures 00→01 equal the same endpoint difference. Hence J=J_00+δ and K=C_00+δ, including M=0. The additive numerator correction is 1−2t when δ=0 and −t when δ=1, both of absolute value at most 1. For x=Mu≥64, EJ≥3x/4 and Chebyshev gives P(J<x/2)≤16·61(x+16)/x²≤1220/x. On the good event Cauchy–Schwarz gives risk at most (√5/2)/√x+2/x, and the bad event contributes at most 1220/x. The report's bound 80015/512<157 is correct; for x<64 loss≤1 gives the advertised min bound. At M=0, S_2=S_N=00, δ=0, all counts are zero and B_00=1/2.

For every fixed u, the cited two-point lower bound applies to a single common prediction rule across the two t values, even with u and full history supplied. The same parameter-independent add-one rule attains the upper bound for all u and t; the oracle-u lower and u-blind upper have the correct direction. This yields a fixed-u terminal-conditioned minimax rate and simultaneous adaptation, not an unconditional-risk rate, nor a computational or architecture lower bound. The underlying cited audit is `v10_research/rare_fast_mixing_family_audit_20261103_1211/family_audit_report_v3.html`; adding this exact source as a link in a future revision would make the lower-bound dependency easier to trace.

## Network and numerical interface

At a history row i, the two paid singleton-copy heads provide X_(i−2), X_(i−1) while X_i is retained. Constant-width tokenwise Boolean/ReLU circuitry may form each context onehot e_i, f_i=e_i X_i, and the separate actual terminal-state query q. Such feature creation and subsequent multiplication by bits can require multiple nonlinear FFN stages, as the report acknowledges. At the terminal row the matching head has finite allowed scores 0 and β=log(1+M/2), with query/key dimension four and value dimension eight. Its normalization is D=M+(M/2)J_s=(M/2)(J_s+2). The selected coordinates are Q_C=(M+2)C_s/[M(J_s+2)] and Q_J=(M+2)J_s/[M(J_s+2)]. Therefore 1/2+[M/(M+2)](Q_C−Q_J/2)=(C_s+1)/(J_s+2). This is pathwise and holds for each actual terminal state and J_s=0. M=0 requires and receives its separate constant-output bypass. Off-query coordinates are not erroneously claimed to decode all four states simultaneously.

With q exact, clip all incoming head coordinates to [0,1] and use ReLU(v+b−1) for a onehot gate. Unselected coordinates are identically suppressed regardless of their errors, while clipping cannot increase the selected-coordinate errors. Exact subsequent operations then yield scalar—and Bernoulli total-variation—error ≤[M/(M+2)](ε+ε/2)≤3ε/2. The bound is conditional on only the two selected coordinate errors; it does not establish a complete finite-word implementation or bound scores, softmax, masks, copying, feature/query creation, coefficient, accumulator, projection or complement errors. With the quantizer clarified above, the sufficient inequality in §6 correctly gives extra risk at most 1/√(1+Mu), since u<1/4.

## Scope and cost

The exact construction is a length-indexed parameter family using N/M, with parameters independent of u and t; it is not one fixed length-independent network. It uses two copy heads plus one match head, explicit structural masks, a causal terminal self-edge, paid tokenwise feature/selection stages, and the specified values, residuals and arithmetic. It is not a free dense-causal implementation or a finite-precision end-to-end guarantee. Same-history streaming counts with add-one division are an exact statistical comparator, so this proof alone gives no statistical advantage over streaming. No claim of novelty, training success, optimal head/depth/bit count, or matched-resource separation follows.
