# Independent analytic review: fixed-c coefficient transition

Reviewed `constant_scale_transition_v1.html`, SHA-256 `2d8d6b8c668d1726cd16673b161f8c4a779f3889ea9f13dc0ccc1381ae0d27d0`. The source graph and the c=2 companion, together with its moving-target correction, are inherited as cited. This is an analytic review of the declared exact-real graph and source, not a formal verification, numerical test, or general Transformer theorem.

## Conclusion

I found no error in the two open-interval claims, the deterministic gaps, four anchor ratios, or the fixed-source actual-terminal risk. The result fixes c before taking N→∞ and leaves c=1/2, c=3/2 and N-dependent c unresolved. It establishes the stated one-parameter positive-side transition in this specific graph, not general robustness or an optimal finite-N threshold.

## Safe interval

For 0<c<1/2, r=i−1 and nonzero d=j−r, the exact score difference is i[d²+(c/L)(j²−r²)]. Because j,r≤i, it is at least i d²[1−2ci/L]. The concave function i−2ci²/L is at least the smaller endpoint value on [4,L]; the displayed L conditions make both at least 3. Thus off-target softmax mass is ≤2/(e³−1)<1/4 at every needed row, uniformly over words. The copied data bit is snapped exactly. Invalid g gates remain zero, lag-two and all input values are unchanged, and the terminal onehot, block-3 anchor and length outputs, and final Gaussian vocabulary logits agree. Raw first-head values and irrelevant earlier slots need not agree; no other route from them reaches the terminal output. Hence the two final distributions are exactly equal under the stated conditions.

## Drift interval and anchor counts

For fixed 1/2<c<3/2, with D=L+c and ζ=cr/D, the thresholds ζ=1/2,3/2 occur at D/(2c),3D/(2c). The first lies within the sequence and the second exceeds L by Θ_c(L), so for large L it is more than H=ceil(100 ln L)+10 beyond the terminal row. Discarding i<H and the H-neighborhood of the first threshold removes O(log L) rows and all ties. When i<D/(4c), ζ<1/4 and gap≥i/2≥H/2. Otherwise i≥D/(4c), both relevant threshold distances exceed H and the runner-up score gap is ≥2ciH/D≥H/2. The outside lower half-integer cannot be closer, and the upper threshold is covered by r₂−L>H. The wrong-key mass is ≤Le^(−H/2)≤L^-49<1/4. The exact snapped lag-one bit is X_(k−1) in a segment of relative length α=1/(2c) and X_(k−2) in the remaining segment. The lag-two bit is X_(k−2). At terminal, ζ→c strictly between 1/2 and 3/2, so the gap grows linearly and the actual query is (X_(N−2),X_N).

The stationary pair law is uniform and r0=5/8, r1=3/8. Fixed-window stationary ergodic prefix sums and their deterministic interval differences yield the displayed limits for J_ab/N and C_ab/N. Each denominator is positive since α>0. Exceptional keys contribute O(log N) scaled mass, BOS O(1), and nonmatches ≤Ne^(−N), so the four anchors converge almost surely to the displayed p00=(5−2α)/[4(2−α)], p01=1/2, p10=1/4 and p11=(3−α)/[4(2−α)]. Uniform final-block error and bounded convergence give E|P_N−p_(X_(N−2),X_N)|→0, without claiming the moving comparator converges.

## Actual terminal risk

For a=X_(N−2), b=X_(N−1), z=X_N, P(a,b)=1/4 and P(z=1|a,b)=θ_ab; the true next probability is θ_bz. Grouping the finite joint law by a,z, the z=0 contribution for a=0 is p00/16+1/64, and for a=1 it is 3/32. For z=1, a=0 contributes zero and a=1 contributes 3(1/2−p11)/16. This gives (11−6α)/[32(2−α)]=(11c−3)/[16(4c−1)]. It equals 1/6 at c=1 and tends to 5/32 as c decreases to 1/2 from above. The expectation is over the real dependent terminal window, whose law is stationary; reverse triangle inequality transfers the L1 approximation to the risk.

Only source reads and SHA checks were used; no experiments, enumeration, code execution, source overwrite, or external writes were performed.
