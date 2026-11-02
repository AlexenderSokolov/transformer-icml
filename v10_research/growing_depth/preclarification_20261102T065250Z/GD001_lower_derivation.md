# GD001 auxiliary lower derivation — growing depth, fixed primitive budget

2026-11-02. Mathematical derivation, not an independent acceptance receipt. This note reads and extends CA001 v3 §§1–7 and BA001 v1 §5. It does not use CA001's depth-dependent global square-sum constant.

## 1. Precisely uniform architecture contract

Fix K>=3, output dimension d>=1, maximum heads H, local preprocessing radius r, and number b0 of exact boundary symbols, independently of M and network depth l. Source observations number N=M+2; synthetic terminal index T=M+3. Initial local-table diameter is at most Δ. Each layer has the same fixed bounds B,V,S,V_L,F_L from CA001 v3: logits in [-B,B], values bounded V, score Lipschitz S, value Lipschitz V_L, and row update Lipschitz F_L for its sum norm. Terminal projection has Lipschitz constant G. Constants need not be equal layerwise, only uniformly upper-bounded by these numbers. Dense public causal masks of density c_mask>0 are permitted by replacing exp(2B) below by exp(2B)/c_mask. Attention-free positionwise layers are permitted by increasing the diagonal recurrence constant to cover their Lipschitz bound.

Every exact boundary branch must satisfy these contracts on all formal source histories with the branch frozen, not only boundary-consistent histories. The decoder sees only d coordinatewise downward Q-grid outputs, this fixed finite boundary label, and public metadata. It has no unquantized historical side port. A fixed uniform pre-cut approximation error E/Q can be allowed, with E independent of l,M,Q; otherwise E=0 here.

The relevant depth is actual bounded-primitive composition depth. A row update cannot hide an l-dependent ReLU circuit inside one declared layer. Fixed width, bounded coefficients, a fixed number of affine/ReLU operations per layer, and fixed fan-in give a fixed F_L. Width or bounded scores alone do not impose this condition. This note is not a lower bound for arbitrary discontinuous internally rounded programs.

Set C_att=exp(2B) (or its dense-mask variant),

    a=F_L(1+2HVC_att S),
    b=F_L H C_att(V_L+2VS),
    w=1+ln 2,
    gamma_l=max{1,rGΔ[(a+b)^l-a^l]w^(l-1)}, l>=1.

Increase a if needed for attention-free layers. CA001's nonnegative matrix recurrence and local-window counting give, for every source coin i>=T/2,

    ||F(X)-F(X with coin i replaced)||_infinity <= gamma_l/M.       (L1)

Here F is the terminal ideal real vector, and all constants are uniform over frozen branches. Coin i affects at most r local-table states; all such affected states have index >=i and hence are late. This justifies the r factor, including windows overlapping the terminal observation.

There is an explicit fixed C>=2 such that gamma_l<=C^l:

    C=max{2, max(1,rGΔ) max(1,(a+b)w)}.                            (L2)

Indeed w^(l-1)<=w^l, the subtracted a^l is nonnegative, and max(1,rGΔ) <= max(1,rGΔ)^l. This C has no hidden l-dependent factors. For different conventions for primitive depth, a constant number of primitive layers per attention block changes C but not the order conclusion.

## 2. Depth-independent suffix tube

Write gamma=gamma_l, z=gamma Q, H_b=3^b0, and tau=sqrt(5dH_b). For a suffix of j independent Bernoulli(p) source symbols wholly in the late half, (L1), the product derivative identity, and Efron–Stein give for each frozen branch and output coordinate

    |(E_p F_d)'| <= gamma j/M,
    Var_p F_d <= gamma² j/(2M²).

A union bound over all dH_b coordinate/branch pairs implies simultaneous deviations <=tau gamma sqrt(j)/M with probability >=9/10. This samples the unconditional product suffix while freezing branches, then selects the actual boundary label; it does not condition independent coins on that label.

Suppose z sqrt(j)/M<=1/2. Cover p in [1/4,3/4] at spacing M/(zj), allowing at most 2+zj/(2M)<=2(1+zj/M) mesh points per branch. The mean vector moves at most 1/Q to its closest mesh representative. Concentration contributes at most tau/(2Q), approximation error contributes E/Q, and floor contributes less than 1/Q. Therefore every good integer grid label is within tau/2+E+2 of its mesh point, coordinatewise. The deliberately larger constant

    N_box=ceil(2tau+2E+4)+1,
    A=2H_b N_box^d

bounds complete good-message cardinality by

    A(1+zj/M).                                                   (L3)

In particular A is independent of l, gamma, M, Q. The former CA001 constant involving sqrt(I_(2l-2)) is entirely absent because only late suffixes are used. Approximation E must be certified separately for any actual arithmetic implementation.

## 3. Stationary source and all-z bound

For 0<=beta<=1/16 let beta0=max(beta,1/M), alpha=1/(2M), eta=beta0-alpha. On symbols W,C0,C1 put

    Tsrc(W,W)=1-alpha; Tsrc(W,Ci)=alpha p_i;
    Tsrc(Ci,W)=eta; Tsrc(Ci,Ck)=(1-eta)p_k;
    pi(W)=eta/beta0; pi(Ci)=alpha p_i/beta0,

where p_1=p, p_0=1-p. Extend unused-symbol rows by pi. The stationary second-order chain has theta_(u,v)(x)=Tsrc(v,x), pair law Pi(u,v)=pi(u)Tsrc(u,v), and all-state two-step minorization P²>=beta Pi. This is the same explicit witness as CA001, with Pi(W,W)>=1/4 independently of p.

First suppose 1<=z<=M/4. Let

    U=min{1/(4beta0),M²/(4z²)}, J=floor U.

Then U>=4, J>=4, J<=M/4, J>=U/2. For 2<=j<=J, event E_j consists of W^(N-j) followed by j active symbols. Its p-independent probability is

    Pi(W,W) alpha(1-alpha)^(M-j)(1-eta)^(j-1) >=1/(32M).

The active suffix lies in the late half, is conditionally IID Bernoulli(p), and meets z sqrt(j)/M<=1/2. These events are disjoint. Grant event index j to the decoder (only making its task easier) and use the single common uniform prior p in [1/4,3/4]. The next law is eta delta_W+(1-eta)[(1-p)delta_C0+p delta_C1], with 1-eta>=1/2.

For completeness the finite-message lemma says: a uniform parameter over length ell, with joint good-event probability >=9/10 and at most R good labels, has expected absolute estimation error >=ell/(16R). Fix decoder randomness; radius ell/(8R) intervals about its R scalar outputs cover at most ell/4 of parameter space. Goodness outside these intervals has probability >=9/10-1/4. Multiply by radius, then average decoder randomness. Outputs may be arbitrary real numbers. Here ell=1/2 and TV is at least (1-eta) times scalar p-error, so conditional prior risk is >=1/[64A(1+zj/M)]. Consequently

    R >= (1/(2048AM)) sum_(j=2)^J 1/(1+zj/M).

For u=z/M<=1/4, write j=k+2 and use 1+u(k+2)<=(1+2u)(1+uk), (1+2u)^(-1)>=1/2. Integrating the decreasing function over [0,J-1], J-1>=J/2, and ln(1+x/2)>=ln(1+x)/2 prove

    sum_(j=2)^J 1/(1+uj) >=(1/(4u))ln(1+uJ).

Since uJ>= (1/8)min{z/(Mbeta0),M/z},

    R >= c/z ln(1+(1/8)min{z/(Mbeta0),M/z}),
    c=1/(8192A).                                                (L4)

For z>M/4, the right side is at most cM/(8z²)<2c/M, using ln(1+x)<=x. Full-history stationary IID two-point testing gives risk >=1/[128sqrt(M+2)] (the CA001 explicit Bernoulli pair). Since c<=1/8192 and M>=64 this dominates 2c/M. Thus (L4) holds for every z=gamma_l Q>=1. The large-z extension does not rely on nonexistent suffix windows.

All source laws used belong to the stationary subclass, so the lower applies as well to minimax risk over arbitrary initialization. Constants are uniform in the allowed encoder family, including source-independent randomized seeds whose contracts hold seedwise.

## 4. Necessary log-log primitive depth at the statistical grid

Let beta=0, c_-sqrt(M)<=Q<=c_+sqrt(M) with fixed positive c_-,c_+, and suppose the family attains R<=C_risk/sqrt(M) for all sufficiently large M. The risk constant C_risk is fixed independently of M and l.

If gamma_l>=M^(1/4), it already exceeds a positive multiple of ln M eventually. Otherwise

    z>=c_-sqrt(M), M/z>=M^(1/4)/c_+.

At beta0=1/M, the logarithm in (L4) is therefore >=(1/8)ln M for all sufficiently large M (threshold depends only on c_±). As z<=gamma_l c_+sqrt(M), (L4) and the target risk imply

    gamma_l >= [c/(8c_+ C_risk)] ln M.

Together the cases imply gamma_l>=c_*ln M eventually, for fixed positive c_*. By (L2),

    l >= [ln ln M + ln c_*]/ln C = Omega(ln ln M).               (L5)

This is a necessary order for bounded primitive budgets, not an exact coefficient or a claim that gamma_l is the actual sensitivity. A separate explicit fixed-width upper construction is needed for sufficiency. This proof does not make constants depth-independent by pretending CA001's old A_s was fixed: it replaces that tube entirely by the z-rescaled late-suffix tube.
