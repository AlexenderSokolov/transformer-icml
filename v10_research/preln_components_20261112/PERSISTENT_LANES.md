# Persistent signed lanes in the full-PreLN amplifier

2026-11-12. Independent algebraic extension of preln-contrast-amplifier/AMPLIFIER.md. This is a clean-state invariant and a source comparison, not a completed predictor or noisy-state invariant.

## Primary source: what Li et al. actually supply

Zhiyuan Li, Hong Liu, Denny Zhou and Tengyu Ma, Chain of Thought Empowers Transformers to Solve Inherently Serial Problems, ICLR 2024, Appendix F.1. Primary text: https://arxiv.org/html/2402.12875v4.

They replace a ternary coordinate by four balanced sign coordinates: 0 maps to (1,-1,1,-1), +1 to (1,1,-1,-1), and -1 to (-1,-1,1,1). Constant mean zero and variance one make their asserted LayerNorm identity hold in the epsilon-zero, unit-gain convention. A decoder for these codes is the average of the FIRST TWO coordinates; averaging all four would give zero. Their wording 'average of the new representation' should not be copied without specifying this projection.

Independent positive-epsilon correction: LN_epsilon(h)=h/sqrt(1+epsilon) on such a code. A gain sqrt(1+epsilon), if allowed, restores exact identity. Under prescribed unit gain, absorb the fixed factor sqrt(1+epsilon) into the branch's input projections. This concerns an already balanced constant-energy discrete code, not arbitrary continuously varying amplifier lanes. With fixed width these codes have bounded raw norm; a logarithmically growing number of bits does not give a fixed raw Euclidean-norm budget.

## Direct extension, avoiding a false identity argument

Let r>=1 be a fixed number of persistent signed pairs (s_j,-s_j), s_j in {-1,+1}. Include two variable pairs (x,-x),(y,-y), and optionally z fixed zero pairs. Put k=r+2+z, W=2k. Attention and FFN outputs during amplification are zero in every persistent/zero coordinate. Hence the residual keeps their raw values exactly fixed on clean trajectories.

For full LN with epsilon=1, unit gain and zero shift,

    d²=A+(x²+y²)/k,  A=1+r/k.

Use the SAME two-coordinate residual update x'=x+phi(x/d), y'=y+phi(y/d), where phi(t)=t-2ReLU(t-a)+2ReLU(-t-a), a=1/10. The other pairs remain unchanged. This uses only a fixed number of ReLU units and fixed weights.

On [0,1]² of target-signed magnitudes u,v, 1<=sqrt(A)<=d<=sqrt(1+(r+2)/k)<=sqrt(2). Oddness reduces arbitrary target signs to this positive square. The coordinate derivative of u/d is 1/d-u²/(k d³), lying in [0,1]. Therefore u+phi(u/d) is nondecreasing in u with v fixed. It is nonnegative because phi(t)>=-t and d>=1; at u=1 its drift is 2a-1/d<0. This proves square invariance.

For u<a, the update grows by at least factor 1+1/sqrt(2). The same boundary monotonicity keeps u>=a once attained. On a<=u<=ell=a sqrt(2), the drift is at least min(a/sqrt(2),2a-ell)>ell-a. Thus one extra step enters [ell,1], which is invariant. Each coordinate follows this argument independently of the other's current value. A polynomially small initial margin still requires only O(log N) blocks.

Inside [ell,1]², both normalized coordinates are >=a and

    F(w)=w+2a(1,1)-w/d,  w=(u,v).
    DF=I-I/d+ww^T/(k d³).

Tangential and radial eigenvalues are 1-1/d and 1-A/d³, respectively, both nonnegative. Hence F is a Euclidean contraction on this convex square, with q<=1-A/(sqrt(2))³<1. Its symmetric fixed point has

    d_*²=A/(1-8a²/k),  b=2a d_*.

It lies in the invariant square. The amplified normalized coordinates converge to +/-2a; every persistent signed coordinate converges to s_j/d_*. All rows have the SAME d_* because r,k and every persistent magnitude are common, even though their signs vary. Raw state norm is bounded by sqrt(2(r+2)), independently of N and depth. The extra zero pairs do not contribute to that norm.

## Marker semantics and scope

Encode a binary marker m by s=2m-1, not an unpaired 0/1 coordinate. This keeps both mean and persistent squared energy identical across raw rows and allows a finite codebook lookup later. Several fixed markers or a fixed finite-alphabet token code can be carried this way. This does NOT supply arbitrary position labels at fixed width, nor a moving positional selector.

Appending unpaired marker coordinates generally shifts the mean and invalidates the displayed map. Paired 0/1 markers preserve mean but introduce row-dependent energy; the amplifier can still be analyzed per energy class, but common raw normalization and equalized value aggregation no longer follow without another argument. Signed pairs avoid this issue.

The initial contrast/readout/tie-insertion coefficients must be recomputed at the enlarged width: the initial raw normalized scale is c0=1/sqrt(A), not the W6 value sqrt(3)/2. At N-independent r,z this is still a fixed constant. Existing W6 initialization margins cannot simply be copied verbatim without checking them. Noise can perturb mean, raw bits and zero lanes; use the earlier positive-epsilon Lipschitz tube argument, not exact signed-pair invariance under arbitrary errors. Terminal gating, parity write, and later accumulator lanes remain separate stages to audit.
