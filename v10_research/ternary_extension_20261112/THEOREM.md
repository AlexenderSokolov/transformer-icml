# Ternary source-average theorem for full causal evolving-K/V attention

2026-11-12. Complete proposed proof, awaiting independent review. No novelty certification, formal verification, matching upper bound, or unrestricted Transformer lower bound is claimed. This supersedes the architecture placeholder in NONSPIN_COMMON_MARGINAL_EXTENSION.md; its literature discussion remains applicable.

## 1. Source and theorem contract

Let m=3, A={0,1,2}, f=(1,-1/2,-1/2), 0<h<1 fixed. For theta in [-h,h], use the stationary order-two source

    P_theta(z|x,y)=(1+theta f(x)f(y)f(z))/3.

Its stationary pair distribution is uniform. Its pair-state chain has two-step minorization alpha=(1-h)^2 against the uniform distribution on A^2. Write rho=1-alpha and kappa=sqrt(1+16/alpha).

There are N>=2 source rows and terminal T=N+1. The terminal is freely given tau=(X_(N-1),X_N). For each of the nine possible tags t, consider the artificial execution with terminal initialized at that fixed t, irrespective of source word. Raw initial states depend only on their local token, public position and N. Architecture parameters, embeddings and positional biases can depend on N, but not on theta. The terminal is a separate row and never affects raw rows because attention is causal.

Single-head blocks suffice to state constants. At layer ell, scores s_ij(x_i,x_j) include the full positive-epsilon PreLN, Q/K projections and any bounded positional bias. Values v_j(x_j) include PreLN and V projections. On the entire radius-H Euclidean ball for each argument, assume

    |s_ij| <= S,
    |s_ij(x_i,x_j)-s_ij(y_i,y_j)| <= Ls(||x_i-y_i||+||x_j-y_j||),
    ||v_j|| <= V,  ||v_j(x)-v_j(y)|| <= Lv||x-y||.

Attention is softmax over every j<=i, including self, with no selected masks. The output projection has operator norm <=Lo. Following the attention residual, the row-local map G_ell (including FFN residual and any prescribed local normalization) has Lipschitz constant F=1+Lf on a convex bounded domain containing every pre-G vector produced from radius-H states and attention outputs of norm <=V. Constants may vary by layer; indices below are suppressed.

Every actual block state on every consistent-tag execution lies in radius H. For proof purposes, project each artificial block output onto that ball. This leaves every consistent-tag execution unchanged by induction, even if inconsistent-tag executions would leave the ball. Projection is not an extra operation granted to the actual network. Initial states of all artificial tags lie in the ball. All constants must cover these projected artificial executions and the reference domains, not only typical trajectories.

Decoder q maps the final ball into the probability simplex on A and is Lipschitz from Euclidean state distance to total variation with constant Lout. Thus ordinary Euclidean-softmax decoder bounds require the corresponding TV conversion, not a silently reused scalar constant. This envelope is a conditional bounded-resource hypothesis; the theorem does not assert arbitrary parameters satisfy N-uniform constants.

Define layer constants

    a=F[1+2 Lo V exp(2S)Ls],
    b=F Lo exp(2S)(Lv+2V Ls),
    u=F Lo sqrt(3) kappa exp(2S)(1+V^2),
    E_0=0, E_(ell+1)=(a_ell+2b_ell)E_ell+u_ell.

Then there are nine deterministic theta-independent predictions qbar_N(t) such that, for every theta in [-h,h],

    E_theta TV(Q_N(X),qbar_N(tau)) <= 3 Lout E_D/sqrt(N+1).       (A)

Consequently, defining risk against the true conditional next-token distribution,

    max(R_h(Q),R_-h(Q)) >= (R_h+R_-h)/2
        >= 4h/27 - 3 Lout E_D/sqrt(N+1).                         (B)

If a_ell+2b_ell<=B>1 and u_ell<=U uniformly, E_D<=U(B^D-1)/(B-1). This yields only a logarithmic-depth constant-risk obstruction within that envelope.

## 2. Input concentration, with all constants

Let g_j:A -> Hilbert space be arbitrary deterministic position-dependent functions with ||g_j||<=R. For pair state Y_i=(X_i,X_(i+1)), the two-step minorization gives

    sup_y TV(P^k(y,.),pi) <= rho^floor(k/2).

The conditional law of X_j given Y_i is obtained from P^(j-i) followed by the first-coordinate map. For j>i, centering g_j and using the TV bound gives conditional mean norm <=2R rho^floor((j-i)/2). Since the centered g_i has norm <=2R,

    |E <g_i-Eg_i,g_j-Eg_j>| <=4R^2 rho^floor((j-i)/2).

The diagonal variance is at most R^2. The lag sum is

    sum_(k>=1) rho^floor(k/2)=1+2rho/(1-rho)=2/alpha-1.

Thus the variance of the average of n terms is at most

    R^2/n [1+8(2/alpha-1)] <= kappa^2 R^2/n.                    (C)

This is dimension-free and applies to arbitrary deterministic positional heterogeneity. For a prefix of length i containing n<=i random source rows and deterministic terminal contributions, normalization by i gives variance <=kappa^2 R^2 n/i^2<=kappa^2 R^2/i. No evolved hidden-state mixing assumption is used.

## 3. All reference domains and averaging rule

For each fixed artificial tag t construct three deterministic reference branches bar_h_i^ell(r), r in A, at every raw row, and one deterministic reference bar_h_T^ell(t) at the terminal. Raw references are actually independent of t by causality. Initialize with the exact corresponding local-token or fixed-tag initial state.

At raw query branch r, or the single terminal query branch for fixed t, form contributions for each source row j<=i:

    F_ij^r(s)=(exp(s_ij(bar_h_i(r),bar_h_j(s))) v_j(bar_h_j(s)),
               exp(s_ij(bar_h_i(r),bar_h_j(s)))).

Average F_ij^r(s) uniformly over the THREE raw symbols s. At the terminal self row use its single fixed reference contribution, with no token average. Sum the numerator and denominator contributions, normalize each by i, then divide numerator by denominator. Apply the actual attention output projection, residual and G_ell, and finally the radius-H metric projection. This gives the next reference branch.

Every reference state is in the declared ball. Its intermediate attention value has norm <=V, so its pre-G state is in the stipulated domain. Each denominator is at least exp(-S). References are deterministic and theta-independent by induction, because all source one-token marginals are uniform and the weights and tag are fixed.

This is not the mean of the actual network. In particular no claim E[n/d]=E[n]/E[d] is made.

## 4. sqrt(3) raw-branch selection and normalized ratio

For fixed i and query branch r, the vector F has norm at most R=exp(S)sqrt(1+V^2). Subtract its reference mean, and denote its normalized empirical sketch error by Z_r. Equation (C) gives

    ||Z_r||_(L2) <= kappa R/sqrt(i).

For the realized raw query branch r=X_i, no independence or conditional concentration is needed:

    E||Z_(X_i)||^2
       =sum_r E[1{X_i=r}||Z_r||^2]
       <=sum_r E||Z_r||^2 <=3 kappa^2 R^2/i.                  (D)

Hence the factor is sqrt(3), not 3, when carrying L2 errors throughout. The terminal has only ONE query branch in each fixed-tag artificial execution and thus factor 1; using sqrt(3) there is a conservative common bound.

For empirical and mean sketches (n,d),(n',d'), d,d'>=exp(-S), and ||n'/d'||<=V. Therefore

    ||n/d-n'/d'|| <= exp(S)(||n-n'||+V|d-d'|)
                  <=exp(S)sqrt(1+V^2)||(n,d)-(n',d')||.

Combining with (D) yields reference-bank empirical-to-mean attention L2 error <=sqrt(3) kappa exp(2S)(1+V^2)/sqrt(i).

## 5. Pointwise stability and the L2 evolving-K/V induction

For two state banks x,y in the ball write d_j=||x_j-y_j||. Softmax interpolation along the straight segment between score vectors stays in [-S,S]. Its weights satisfy p_j<=exp(2S)/i. The identity derivative of the weighted average in a score direction is p_j(v_j-A), with norm <=2V p_j. Comparing values first and scores second gives

    ||Att_i(x)-Att_i(y)||
       <=2V exp(2S)Ls d_i
         +exp(2S)(Lv+2V Ls)(1/i)sum_(j<=i)d_j.              (E)

This includes evolving query, key, and value states. All mixed-bank value/score comparisons remain in the assumed bounds. Residual, output projection, G and the common metric projection give coefficients a,b above.

For each fixed tag t let

    e_i^ell(t)=||h_i^ell,t-bar_h_i^ell(X_i)||_(L2)

at raw rows; at terminal compare against its fixed-tag reference. Artificial h is the projected execution. Using pointwise (E), Minkowski's inequality, and section 4 gives

    e_i^(ell+1)(t) <=a e_i^ell(t)+(b/i)sum_(j<=i)e_j^ell(t)+u/sqrt(i).

Initial errors are zero. The elementary bound sum_(j<=i)j^(-1/2)<=2sqrt(i) proves by induction e_i^ell(t)<=E_ell/sqrt(i), simultaneously for all tags. No conditioning on t=tau is performed in this induction. Multiple heads are allowed by summing their projection-weighted stability and fluctuation constants using Minkowski; the single-head formulas must not simply be reused unchanged.

## 6. sqrt(9) actual endpoint-tag selection

For each fixed tag t, let Z_t(X)=TV(q(h_T^D,t(X)),qbar_N(t)). Its L2 norm is <=delta=Lout E_D/sqrt(N+1). The actual consistent-tag network equals the corresponding artificial network at t=tau. Therefore

    E Z_tau <=sqrt(E Z_tau^2)
             <=sqrt(sum_(t in A^2) E Z_t^2)
             <=sqrt(9) delta=3 delta.

This pays exactly the nine-tag L2 selection bound, not the older binary conditional factor 4. Uniform pair probabilities are not required for this selection step; they are required for the following risk comparison. One must not combine an L1 fixed-tag estimate with this L2 factor.

## 7. Risk separation

For fixed tau=(x,y),

    TV(P_h(.|tau),P_-h(.|tau))=(2h/3)|f(x)f(y)|.

The common pair law is uniform, so the average separation is (2h/3)(2/3)^2=8h/27. For every deterministic template qbar_N(tau), triangle inequality gives equal-prior template risk >=4h/27. Under each source, actual risk differs from template risk by at most the expected TV approximation error in (A). Averaging these two inequalities proves (B). This is a deterministic-template argument, not an assertion that random count laws agree or that endpoint-conditioned observations are independent.

## 8. Scope and provenance

The concentration, Lipschitz stability and mean-field propagation ingredients are standard. This proof supplies a ternary specialization and explicit branch/tag constants; it is not a claim of new source parameterization or a first mean-field theory. The family retains a binary latent partition. It does not provide a bounded-score predecessor-copy compiler, a sharp depth tradeoff, a finite-precision simulation theorem, or a matching statistical upper bound. All-row evolving K/V are included only under the displayed uniform score/value/state/local-map envelope.
