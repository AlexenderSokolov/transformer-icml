# A depth-independent obstruction for a restricted one-read model

2026-11-12. New mathematical candidate with an explicit proof below. No novelty claim; independent review requested. This does not settle the unrestricted repeated evolving-K/V frontier.

## Statement and scope

Fix 0<c<1/2 and 0<h<1-2c. Use the stationary binary source
P_theta(z|xy)=(1+theta xyz)/2, theta in {h,-h}.
For N>=2, write S_N=sum_{i=1}^N X_i and T=(X_(N-1),X_N).

There is C_h<infinity such that

    TV(Law_h(S_N,T), Law_-h(S_N,T)) <= C_h N^(-1/3).

Consequently any estimator Q_N=q_N(S_N,T), including randomized estimators with a source-independent seed, satisfies

    max(R_h(Q_N), R_-h(Q_N)) >= h/2 (1-C_h N^(-1/3)).

This applies to an exact-real Transformer with one attention read at an appended terminal, free access to T, no position dependence in source embeddings/keys/values/scores, and arbitrary subsequent terminal-only pointwise computation. Any number of simultaneous heads is allowed. Row-local preprocessing must be identical across raw positions. Every head's numerator and denominator is a function of the two token counts and T; the terminal's own contribution is also a function of T. Thus the terminal state factors through (S_N,T). Neither greater post-read depth nor precision can remove this statistical obstruction.

It does NOT apply to a second attention read from evolved all-row states, position-dependent raw features, local masks, or global features at initialization. In particular, causal prefix representations after the first read need not be count-sufficient collectively. This is a restricted-model separation, not a super-logarithmic lower bound for the mother's architecture.

## Fourier proof of the statistical assertion

Use pair states (x,y) in {+1,-1}². Let K_theta be their four-state transition kernel and define the tilted matrix

    M_theta(t)[(x,y),(y,z)] = K_theta[(x,y),(y,z)] exp(it z).

Let b_theta(t)[(x,y)]=(1/4)exp(it(x+y)); this vector actually does not depend on theta. For N>=2, the joint characteristic function at endpoint tau is

    Phi_theta,tau,N(t)=b(t) M_theta(t)^(N-2) e_tau.

At t=0, K is irreducible, aperiodic and stationary with uniform pi. In particular K² has every entry positive. The eigenvalue 1 is simple and all others have modulus less than 1. Finite-dimensional analytic perturbation gives an analytic simple eigenvalue lambda_theta(t), analytic eigenprojection and a uniformly exponentially decaying remainder in a fixed neighborhood of zero. Therefore

    Phi_theta,tau,N(t)=A_theta,tau(t) lambda_theta(t)^(N-2)+O(r^N),
    A_theta,tau(0)=1/4.

The source has mean zero and covariance E[X_i X_(i+k)]=theta^(2k/3) for k divisible by three, zero otherwise. Hence the asymptotic variance is

    v_theta=(1+theta²)/(1-theta²)>0,
    log lambda_theta(t)=-v_theta t²/2+O(|t|³).

These coefficients can also be obtained by differentiating the displayed four-by-four matrix; the covariance formula follows directly from independent triple innovations. In particular v_h=v_-h. All local constants can be fixed jointly for the two parameters and four endpoints.

The difference between their leading characteristic functions is bounded by

    C (|t|+N|t|³) exp(-a N t²)+C r^N

on a sufficiently small fixed neighborhood of zero. Here the O(|t|) term comes from A_h-A_-h, whose constant term vanishes. For the exponential difference, interpolate the two complex logarithms; their real parts are both <=-a t² after shrinking the neighborhood. This avoids incorrectly controlling exp(N O(t³)) over a fixed interval.

There are no other unit-modulus spectral points on [-pi,pi] except 0 and pi (identified with -pi). To verify this, if M(t)v=lambda v with |lambda|=1, equality in the triangle inequality and irreducibility force all |v_y| equal and nonzero, and force exp(it z)v_(y,z)=lambda v_(x,y) on every positive edge. The (++ ) and (-- ) self-loops then give lambda=exp(it)=exp(-it), so t is a multiple of pi. Away from neighborhoods of these two points, compactness gives uniform exponential decay of matrix powers (a slightly larger radius absorbs possible Jordan factors). At pi, M(t+pi)=-M(t) and b(t+pi)=b(t), so Phi(t+pi)=(-1)^N Phi(t). The zero-neighborhood argument therefore also covers the parity point; it must not be omitted.

Fourier inversion and the triangle inequality now give the uniform local bound

    sup_{s,tau}|P_h(S_N=s,T=tau)-P_-h(S_N=s,T=tau)| <= C/N,

because integral |t| exp(-aNt²) dt=O(1/N) and integral N|t|³ exp(-aNt²) dt=O(1/N). No Gaussian approximation is assumed uniformly over impossible lattice points.

For |s|<=N^(2/3), there are O(N^(2/3)) candidate integers and four endpoint pairs, giving total difference O(N^(-1/3)). Outside this range, the exact covariance bound gives Var_theta(S_N)<=C_h N, so Chebyshev bounds each tail by C_h N^(-1/3). Combining the central and tail pieces proves the TV assertion. The rate is deliberately conservative; optimizing an Edgeworth or exponential-tail argument is unnecessary here.

## Risk reduction

For a fixed observed (s,tau), the two target probabilities are

    p_h(tau)=(1+h tau_1 tau_2)/2,
    p_-h(tau)=(1-h tau_1 tau_2)/2,

whose absolute difference is h. Integrate |q-p_h|+|q-p_-h|>=h against the common part of the two joint laws, of mass 1-TV. This yields R_h+R_-h>=h(1-TV), hence the displayed maximum-risk bound. Randomness independent of the source is handled by conditioning on its seed. For the architectural corollary, every fixed-seed architecture must remain position-identical on raw rows: row-specific random tags would invalidate count sufficiency. Enlarge C_h to cover the finitely many small values N=2,3. This proof does not assume the endpoint pair is independent of the total count.

For comparison, the full-history innovation mean theta_hat=(N-2)^(-1)sum X_i X_(i+1) X_(i+2) has E|theta_hat-theta|<=1/sqrt(N-2), so Q=(1+theta_hat T_1 T_2)/2 has risk at most 1/(2sqrt(N-2)). This comparison uses the actual terminal pair and independent innovations, not a random denominator.

## Reproduction and remaining questions

check_count.py computes joint laws by a forward count/pair recursion, checks against exact rational enumeration for small N, and reports TV for larger N using floating arithmetic. These finite diagnostics check implementation and behavior, not the spectral proof or an asymptotic rate certificate. The Fourier proof is self-contained up to standard analytic perturbation of a simple finite-matrix eigenvalue, whose hypotheses are supplied explicitly.

Next genuine frontier step would require a replacement for count sufficiency after a second evolving-K/V read or a legal positional construction of signed triple statistics. The present result gives neither. It does establish that arbitrary exact-real postprocessing of a single position-free read is insufficient, a stronger conclusion than bounded-gain mean-field for this restricted subclass.
