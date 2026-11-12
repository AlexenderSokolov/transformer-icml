# Worst-word scalar-sign failure need not imply average prediction failure

2026-11-12. A rank-one positional-score/statistical-interface counterexample. This is NOT a complete PreLN compiler or a low-precision algorithm. It extends the existing block-exponential interface in a different direction: deliberately permit rare sign errors instead of insisting on worst-word recovery.

## Rank-one interface and deterministic failure

For public N choose rho=1/2+epsilon, 0<epsilon<=1/16, delta=rho^N, q_i=rho^i, k_j=rho^(N-j). These nonzero rank-one factors have whole-array squared Frobenius norms at most rho²/(1-rho²) and1/(1-rho²), bounded uniformly in N. Scores s_ij=q_i k_j=delta rho^(i-j) on causal entries j<=i are bounded; no key is masked.

Let w_k=expm1(delta rho^k). From a uniform head U_i and the rank-one head H_i with public denominator D_i, the same exact corrected contrast as the earlier interface is

    C_i=(D_i/i)H_i-U_i-(w_0/i)X_i
       =(1/i) sum_(k=1)^(i-1) w_k X_(i-k).

Recover the previous sign by sign(C_i), then subtract (w_1/i) times that recovered sign and recover the second predecessor. This correction, sign amplification and subtraction are an explicit SCALAR INTERFACE, not free legal Transformer operations.

For every k>=1, convexity gives w_(k+1)<=rho w_k. Also w_(k+j)/w_k>=exp(-delta rho^k)rho^j>=exp(-1)rho^j. Unlike rho<1/2, here the infinite geometric tail can exceed the leading coefficient. In particular, with first predecessor +1 and all older signs -1, the first decoder fails whenever

    exp(-delta rho) rho (1-rho^(i-2))/(1-rho)>1.

This sufficient condition follows by lower-bounding the tail/head ratio. It holds at i=N for all sufficiently large N when epsilon=N^(-kappa)/16 for any fixed kappa>0. Therefore there are genuinely misdecoded words; this is not merely an absent proof of diagonal dominance. Their probabilities under the fixed-c source are positive.

## Why failures are rare under the source

Put m=floor(log2(1/(16epsilon))) and assume m>=1. For either decoding stage, let the true target sign be +1 by sign symmetry and normalize its coefficient to one. The sum of all older absolute coefficients is at most

    rho/(1-rho) <=1+8epsilon.

If any of the first m older signs agrees with the target, its relative coefficient is at least exp(-1)rho^m>=exp(-1)2^(-m)>=16epsilon/exp(1). Replacing a maximally negative tail sign by this positive sign increases the total by at least32epsilon/exp(1)>8epsilon, preventing an error or tie. If only t<m older signs exist, their total relative weight is at most the truncated GEOMETRIC upper bound rho(1-rho^t)/(1-rho). Its deficit from the infinite geometric upper bound is rho^(t+1)/(1-rho)>=rho^m/(1-rho)>=16epsilon, again preventing an error. This deficit refers to the geometric bound, not an unjustified lower bound on actual expm1 weights. Thus failure requires that at least m older signs exist and ALL first m are opposite to the target. This is a sufficient necessary-event bound, not an equality of failure events.

For P_theta(z|xy)=(1+theta xyz)/2 with |theta|<=1-2c and uniform stationary pair, the reversed second-order transition is also (1+theta xyz)/2: it follows by dividing the symmetric stationary triple mass (1+theta xyz)/8 by pair mass1/4. Every reverse transition is <=1-c. Conditional on the target spin, its immediately older spin is fair; the remaining reverse transitions are each <=1-c. Hence the required run event has probability at most (1-c)^(m-1), uniformly in theta and position. No independence of spins is assumed.

The first-stage error probability is at most r_m=(1-c)^(m-1). On first-stage success the second stage equals the ideal second contrast; its error probability is bounded by the same run event at the second target. Union bound gives probability of either predecessor error at most2r_m, without conditioning the source on successful decoding.

## Direct average prediction-risk bound

For i=3,...,N form the decoded innovation X_i times the two decoded predecessor signs, and average to estimate theta; clip to [-a,a], a=1-2c. A wrong predecessor pair can change an innovation by at most2. Thus expected absolute deviation from the true innovation empirical mean is <=4r_m. Clipping is nonexpansive. The actual free terminal pair multiplies the parameter estimate to produce next-plus probability and contributes a factor1/2 to absolute risk. Since true innovations are iid signs with mean theta,

    sup_theta risk <=1/(2sqrt(N-2)) +2(1-c)^(m-1).

Endpoint/estimator independence is NOT required: multiplication by the true endpoint parity preserves absolute parameter error pathwise.

Choose epsilon_N=N^(-kappa)/16 and beta=-log2(1-c)>0. Then m=floor(kappa log2 N) and

    (1-c)^(m-1) <=(1-c)^(-2) N^(-kappa beta).

Taking kappa>=1/(2beta) gives an O(N^-1/2) average-risk interface despite actual worst-word predecessor-sign failures for all sufficiently large N. This explicitly invalidates promoting a worst-word scalar-sign failure into a statistical risk obstruction without controlling how often the bad words occur.

## Costs and limits

The contrast scale is still delta/N, with delta=(1/2+N^(-kappa)/16)^N=2^(-N+O(N^(1-kappa)))=2^(-N+o(N)). It is not necessarily a constant multiple of 2^(-N) when kappa<1. Exact retrieval may require very high precision; rare permitted sign errors do not make the cancelled contrast large. The risk bound assumes exact-real interface arithmetic and sign decisions and does not certify adversarial residual errors, coefficient rounding, or bounded-gain PreLN amplification. The public correction factors D_i/i and w_k/i and their shared implementation remain charged unresolved steps. Conventional final prediction is only a statistical-interface formula here, not a compiled full-LN affine-softmax head.

Whole-array factor norms bounded in N do NOT imply modest decoding gain. This example is therefore consistent with the single-read globally bounded-QK gain-to-risk obstruction and the existing exponential precision/amplification costs. It does not show that worst-word recovery is necessary for statistical success; rather, it gives an explicit case where it is not.
