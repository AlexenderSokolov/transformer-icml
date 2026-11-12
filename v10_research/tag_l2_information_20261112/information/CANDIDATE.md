# Candidate: exact information retention with a shrinking full-PreLN output

2026-11-12. Not a new injectivity principle. Candidate contribution is only an explicit positive-epsilon full-PreLN realization and resource ledger of the familiar distinction between exact-real information and usable bounded-gain prediction. Independent analytical review is included as REVIEW.md; no formal verification or novelty certification is claimed.

## Inputs, actual Q/K/V and sentinel

Fix alpha=1/2 and lambda=1, independent of N and the unknown source parameter. Put T=N+1 and

    k_j=log(1+alpha 2^(-j)), j=1,...,N,
    D=T+alpha(1-2^(-N)), sigma=sqrt(3/2).

Width12 raw input at row j is

    h_j=(X_j,-X_j,k_j,-k_j,sqrt(1-k_j²),-sqrt(1-k_j²),1,-1,0,0,0,0).

The public sentinel is

    h_T=(0,0,0,0,sqrt(2),-sqrt(2),1,-1,0,0,0,0).

Every input has mean zero and squared norm6. Full-feature LN with epsilon1, unit gain and zero shift divides each row by sigma. All positional features, including logarithms and padding, are explicitly supplied exact public features. This is NOT an implementation from a restricted single normalized-position scalar or a finite-precision embedding table.

Use two scalar heads with dot-product dimension1. Head1 has Q=sigma e_6, K=sigma e_2, V=sigma e_0, with coordinates zero-based. Head2 has Q=K=0 and V=sigma e_0. Thus all queries of head1 equal1, raw keys equal k_j, sentinel key zero, raw values equal X_j, sentinel value zero. There are no pairwise additive positional biases. Full self-inclusive causal attention applies at every row. At the sentinel,

    H=[sum_j (1+alpha2^(-j))X_j]/D,
    U=[sum_j X_j]/T.

A shared output projection writes C_i,-C_i into previously empty coordinates8,9, where

    C_i=(D/(alpha T))H_i-(1/alpha)U_i.

The coefficients D/T are public length-dependent parameters of bounded magnitude, not an oracle statistic. Only at the terminal do they cancel to the desired code:

    C_T=(1/T)sum_(j=1)^N 2^(-j) X_j.

Other rows execute exactly the same projection; they need not decode their own prefix. The FFN is zero. Final full LN also has epsilon1, unit gain, zero shift. Terminal state has squared norm6+2C_T² and mean zero, so final two-class affine logits are

    (lambda C_T/sqrt(3/2+C_T²/6), 0).

The resulting next-plus output Phi(C_T) is an ordinary two-class softmax and is strictly increasing in C_T. No alternative/no-final-LN head is used.

## Bounded magnitudes versus representation costs

All scores lie in[0,log(1+alpha/2)]. Input row norm is sqrt6. Both scalar attention averages are in[-1,1], so every post-attention row obeys |C_i|<=(2+alpha)/alpha and

    ||h_i^+|| <=sqrt(6+2[(2+alpha)/alpha]²).

Matrix Frobenius squares: head1 Q,K,V contribute3 sigma²; head2 V contributes sigma²; total6. Output projection contributes exactly

    2[(D/(alpha T))²+alpha^(-2)],

bounded independently of N. Zero biases/FFN contribute zero. If both block pre-LNs and final LN are counted, unit gain vectors contribute squared norm36. Head contributes lambda². These are fixed-depth occurrence totals, not an uncharged shared-storage trick. Raw-input/public-feature coefficients and exact feature generation remain separately declared.

The realized full key-array norm satisfies ||K||F²<=alpha² sum_j4^(-j)<=alpha²/3; centering only decreases it. Each query is1 but the WHOLE query-array norm is sqrt(T), not constant. Thus the construction is compatible with the single-terminal-query global-key energy bridge: the represented signal is tiny and it is not amplified to a useful probability.

Finite magnitudes do not imply short coefficient descriptions. Public k_j and padding require ideal real arithmetic; the N-dependent output coefficient includes2^(-N). No constant-bit or hardware implementation is asserted. A bounded-gain preprocessing from a narrower position representation is not supplied.

## Exact injectivity and smallest spacing

Writing X_j=2b_j-1 gives

    C_T=[2 sum_j b_j2^(-j)-(1-2^(-N))]/T.

For fixed N, the binary integers sum_j b_j2^(N-j) range once over0,...,2^N-1. Hence all word codes are distinct, adjacent code spacing is exactly

    Delta_C=2^(1-N)/T,

and |C_T|<1/T. Final LN and softmax preserve injectivity. For g(C)=lambda C/sqrt(3/2+C²/6),

    g'(C)=lambda(3/2)/(3/2+C²/6)^(3/2)>0,
    Phi'(C)=sigmoid(g(C))(1-sigmoid(g(C)))g'(C).

On |C|<=1/3 (N>=2), Phi' has fixed positive lower and upper bounds. Therefore the minimum output spacing is Theta(2^(-N)/T), not an O(1) digital margin. Robust worst-word code recovery from scalar-output adversarial error requires an error smaller than half the closest spacing; an error at least half that spacing makes two words indistinguishable. The necessary/sufficient order for this scalar-output contract is p=N+log2 T+O(1) bits. This is not automatically the per-sublayer rounding budget of a physical implementation.

A decoder that recovers a last bit on all words must send two adjacent codes (same first N-1 bits, opposite last bit) to outputs separated by2; its Lipschitz constant is at least T2^N in C coordinates, and of the same exponential order in final-probability coordinates. No such decoder appears in the fixed-depth network above.

## What is retained, and what the actual predictor does

For the stationary spin source P_theta(z|xy)=(1+theta xyz)/2, the exact output random variable is in bijection with the entire input word. Therefore its pushforward experiment preserves total variation between any two source laws, and preserves KL exactly:

    KL(Law_theta(output)||Law_theta'(output))
      =(N-2) KL(Bernoulli((1+theta)/2)||Bernoulli((1+theta')/2)).

This means no loss of source STATISTICAL INFORMATION under ideal observation of arbitrarily precise reals. It does NOT mean theta itself is encoded exactly from finitely many samples. Nor does it imply an admissible bounded-gain predictor can extract that information. An arbitrary external inverse lookup could reconstruct all innovations and use their standard estimator; its resolution/gain is excluded from the evaluated architecture.

All outputs lie in a shrinking O(1/N) interval about1/2. In particular, pairwise Wasserstein-1 distance of output laws is O(1/N), even though for distinct fixed theta,theta' their total variation tends to1. The latter follows from consistent testing using the iid innovations and the exact bijection. Weak proximity, total-variation proximity and accessible task information are different statements.

The ordinary output head is itself a poor predictor: for any fixed theta, target is (1+theta X_(N-1)X_N)/2, so pathwise

    abs( abs(Phi(C_T)-target)-abs(theta)/2 ) <=abs(Phi(C_T)-1/2)=O(1/N).

Its actual risk therefore tends to abs(theta)/2 (and to0 at theta0). This explicitly agrees with a fixed-depth mean-field RISK obstruction. Free endpoint disclosure can be ignored; no result here says it must be ignored by other architectures.

## Evidence status

`check.py` evaluates actual all-row Q/K/V, attention, residual output and final full LN for all words at several small N, compares exact rational code spacing and finite-source pushforward KL. Float64 checks are diagnostic only. Exact injectivity and information statements rest on the displayed algebra; binary64 will eventually collide when N grows, which is the declared precision cost rather than a contradiction.
