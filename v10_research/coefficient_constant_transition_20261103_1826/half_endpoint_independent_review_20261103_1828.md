# Independent analytic review: the c=1/2 endpoint

Reviewed `half_endpoint_safe_addendum_v1.html`, SHA-256 `3f246d6b28a1e7c778405558b36354bedc473a5fcf05f9ebf51b1e95cba95486`, and its fixed-c companion `constant_scale_transition_v1.html`, SHA-256 `2d8d6b8c668d1726cd16673b161f8c4a779f3889ea9f13dc0ccc1381ae0d27d0`. The architectural dependency audit is inherited from the reviewed two-sided safe-window graph. No tests, enumeration, simulations, source overwrite or external writes were performed.

## Result

I found no error in the exact-real, all-word equality for every N≥2 at η_N=1/[2(N+2)]. This extends the positive safe fixed-c range through c=1/2; it does not establish c=3/2, an N-dependent boundary layer, simultaneous coefficient errors, or finite-precision execution.

## Gap calculation

Let L=N+2≥4, η=1/(2L), r=i−1 and 4≤i≤L. The left-neighbor gap is f(i)=i[1−(2i−3)/(2L)], a concave quadratic. Its endpoint values are f(4)=4−10/L≥3/2 and f(L)=3/2, so f(i)≥3/2. The right-neighbor gap i[1+η(2r+1)] is at least i≥4. For any other causal key, put d=j−r. Since j,r≤L, its gap is at least i[d²−2Lη|d|]=i|d|(|d|−1). With |d|≥2, bounding d(d−1)≥2(d−1) and adding both signs gives relative wrong-key weight

S≤e^(−3/2)+e^(−4)+2e^(−8)/(1−e^(−8))<1/3.

The draft's elementary estimates e^(3/2)>4, e^4>32 and e^8>1024 indeed imply S<1/4+1/32+1/256=73/256<1/3. Actual off-target probability is S/(1+S)<1/4, not merely S. All token values including BOS lie in [0,1], so the output lies within 1/4 of the correct data bit and the fixed hinge snap gives it exactly.

## Boundaries and complete path

At i=4 the correct key r=3 contains X₁, even when N=2, L=4; its left neighbor is a BOS value, already covered by the convex-value estimate. At valid historical i≥5 both the corrected lag-one bit and unchanged lag-two bit equal their unperturbed values. For i≤4 all candidate g gates vanish irrespective of early snap changes. The actual terminal onehot, all anchor keys and values, BOS contributions, position-only reciprocal marker, selected p, fourth-block terminal queries and unchanged positional keys/values, final logits and vocabulary softmax therefore coincide wordwise. Raw copy coordinates, irrelevant earlier query/selected slots, and complete residual vectors need not coincide. In particular, the N=2 assertion is equality of the two model outputs, not a claim that their common output is exactly 1/2.

This is an independent analytic review, not formal verification or a numerical implementation result.
