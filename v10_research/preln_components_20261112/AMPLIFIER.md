# Explicit bounded full-PreLN amplification and lane equalization

2026-11-12. This supplies the missing local amplifier interface, not the entire prediction architecture. It assumes the separately stated public predecessor-indicator score bias. It does not realize that bias from fixed-width positional dot products.

## Physical representation and tie insertion

Use width W=6, full LN with epsilon=1, gain=1, shift=0, and paired coordinates

    h_i=(s_i,-s_i,x_i,-x_i,y_i,-y_i),  s_i=X_i in {+1,-1}.

The mean is zero. Its normalization divisor is

    d(x,y)=sqrt(1+(1+x²+y²)/3).

Two contrast reads recover desired causal targets i-1 and i-2, using the previously proved biased-minus-uniform construction. Multiple simultaneous heads output both paired contrast lanes and preserve the raw pair. Raw LN values have common scale c0=sqrt(3)/2, so each initial contrast is c0(X_target-mu_i)/(i+1). Treat invalid predecessor indices at the first two rows as any causal target; those rows are excluded from the innovation statistic.

Let epsilon=1/[N(N+1)], N>=2. A legal pointwise PreLN FFN adds epsilon times the normalized first coordinate into each contrast lane, with the opposite amount into its paired coordinate. This is a linear map of LN(h), realized by ReLU(t)-ReLU(-t). It does NOT add a free unnormalized raw bit. The inserted amount is epsilon s_i/d_i.

Before insertion all contrast coordinates have magnitude <=c0*2/(i+1) for i>=2 and vanish for i=1; hence d_i<=sqrt(2). If a prefix is constant, the contrast is zero and the tie breaker has the correct sign and magnitude >=epsilon/sqrt(2). Otherwise its signed contrast is at least 2c0 epsilon, and the adverse tie breaker has magnitude at most epsilon. Thus after the actual normalized insertion each lane has the target sign and margin at least

    delta0=epsilon/2.

Both magnitudes are <1. This operation is the FFN residual immediately following the attention block; subsequent amplification blocks have zero attention.

## Actual residual FFN map

Fix a=1/10. Define the piecewise-linear scalar function

    phi(t)=t-2 ReLU(t-a)+2 ReLU(-t-a).

At every amplifier block set attention output to zero and let the FFN residual output be

    (0,0,phi(x/d),-phi(x/d),phi(y/d),-phi(y/d)).

This is an actual finite-width two-layer ReLU FFN: write t=ReLU(t)-ReLU(-t) if no linear skip inside the FFN is available. Four hidden units per amplified lane suffice, using fixed coefficients in {0,+/-1,+/-2} and biases {0,-a}. All matrix and bias norms are fixed finite constants independent of N and depth; any prescribed norm cap smaller than these constants needs an additional explicit factorization, which is not claimed here. The physical residual update is exactly

    x'=x+phi(x/d), y'=y+phi(y/d), s'=s.

No sign oracle, clip oracle, inverse normalization, or hard mask is used.

## Invariant bounded state and sign preservation

By oddness, replace x,y by their target-signed magnitudes u,v>=0. Their dynamics are the same because d depends on squares. On the square [0,1]², sqrt(4/3)<=d<=sqrt(2). For t>=0, phi(t)>=-t, so u'>=u(1-1/d)>=0. Also the coordinate map u->u+phi(u/d) is nondecreasing for fixed v: its derivative is 1+phi'(u/d)*(1/d-u²/(3d³))>=0, since |phi'|=1 and d>=1. At u=1, u/d>=1/sqrt(2)>2a, hence phi=2a-u/d<0, proving u'<=1 throughout. The same argument applies to v. Thus signs never cross and the entire physical state norm stays <=sqrt(6).

For u<a, its normalized value u/d<a, so u'>=u(1+1/sqrt(2)). Once u>=a it never drops below a: at the boundary u=a the drift is nonnegative, and the coordinate map is monotone. Let ell=a sqrt(2). For a<=u<=ell,

    phi(u/d)>=min(a/sqrt(2),2a-ell)>ell-a.

Therefore one additional step reaches ell. The region [ell,1]² is invariant by the same boundary argument. Starting from delta0 in each coordinate, after at most

    L0=ceil(log(a/delta0)/log(1+1/sqrt(2)))_+ + 2

steps both coordinates lie in this region. This bound is O(log N).

## Contraction to equalized constant-amplitude lanes

On [ell,1]², each normalized coordinate is at least a, so the map becomes

    F(u,v)=(u,v)+2a(1,1)-(u,v)/d(u,v).

Its unique fixed point in that square is (b,b), where

    d_*²=(4/3)/(1-8a²/3),  b=2a d_*.

In particular b is a constant independent of i, the word, and the signs. Its normalized amplified coordinates are exactly +/-2a and its normalized raw coordinate is s_i/d_*.

The Jacobian is

    DF=I-I/d + (1/3)ww^T/d³,  w=(u,v).

Its eigenvalues are 1-1/d and 1-(4/3)/d³, both nonnegative on the square. Therefore its Euclidean operator norm is at most

    q=1-(4/3)/(sqrt(2))³ <0.529.

Because the invariant square is convex, the mean-value theorem gives global q-contraction there. After an additional L1 steps,

    ||(u,v)-(b,b)||_2 <=sqrt(2) q^L1.

Thus normalized lane error <=C q^L1 with a fixed C, and eta accuracy requires O(log(1/eta)) further blocks. At eta=N^-1/2 or N^-1 this is still O(log N). Equal amplitudes are obtained by the actual common full-LN dynamics, not assumed after taking signs.

## Interface delivered and remaining work

At every raw row after O(log N+log(1/eta)) physical blocks,

    h_i=(X_i,-X_i,b X_target1,-b X_target1,b X_target2,-b X_target2)+O(eta)

in Euclidean norm, uniformly over all histories, with fixed state/weight budgets. The normalized coordinates likewise approach a fixed eight-point codebook. A subsequent fixed-size local ReLU lookup can in principle write the triple parity, but its physical lane allocation, constant-amplitude normalization after the write, exclusion of the first two rows, final attention, and probability output must be provided separately. Width six is used only for this amplifier; adding lanes changes d and requires adjusting the displayed constants. Do not silently transfer these numbers to a larger width.

An appended free-pair terminal can bypass the amplifier or be handled by separate token/tag gating; a legal fixed-size implementation of that gating is not supplied here. The uniform raw-row amplifier is the completed component. Public predecessor score biases remain substantive extra positional structure.

## Residual execution errors and precision

Clean physical norms are bounded as above. For arbitrary per-row full-vector errors <=2^-p at each attention and FFN residual, use a radius-r tube in maximum-row Euclidean norm and the actual global positive-epsilon LN/finite-ReLU maps to obtain finite constants Lambda>=1 and G>=1 on that tube. Lambda covers a complete physical residual site, including every normalization, projection and nonlinearity; G covers the final interface map on that same tube. With L residual sites, the clean/noisy state discrepancy is at most 2^-p sum_{j<L}Lambda^j. This statement does not pretend that noisy raw lanes remain exactly +/-1 or that errors are independent. Sufficient integer precision is

    p>=max(0,ceil(log2(S_L/r)),ceil(log2(G S_L/eta))),
    S_L=sum_{j<L}Lambda^j.

Since L=O(log N+log(1/eta)), p=O(log N+log(1/eta)) suffices for this component under fixed constants. This is a sufficient transfer, not a necessary or optimal precision theorem. Exact initial coefficients including the small epsilon are distinct from residual execution error. Errors in initialization or coefficients require separate budgets and are not included here.
