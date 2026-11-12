# A failed parallel-context route under ordinary per-row/parameter bounds

2026-11-12. Candidate obstruction for a specified tied positional-code/scalar-sign interface. This is NOT a lower bound for arbitrary fixed-width PreLN, arbitrary QK, nonlinear multiple sketches, or terminal prediction risk. It investigates simultaneous local-context extraction rather than repeating a single public-source broadcast.

## 1. Proposed parallel route and exact scalar interface

Choose unit positional codes u_j in R^d, any deterministic choice depending on N. At raw row i>=2 let query q_i=sqrt(gamma)u_(i-1), keys k_j=sqrt(gamma)u_j, gamma>0 fixed. Scores are gamma<u_(i-1),u_j>, bounded by gamma. This gives the query the desired predecessor POSITION code, not its token. Keys have per-row norm sqrt(gamma), but whole-key Frobenius norm sqrt(gamma N). This is compatible with fixed per-row and learned-matrix bounds at fixed d; it is not a global-key-energy budget.

Read raw values X_j with this full-prefix softmax head H_i and a uniform head U_i. Let D_i=sum_(j<=i)exp(gamma<u_(i-1),u_j>) be its public denominator. Grant the decoder exact correction of both uniform mass and its known current token:

    C_i=(D_i/i)H_i-U_i
         -[exp(gamma<u_(i-1),u_i>)-1]X_i/i
       =(1/i)sum_(j<=i-1) w_(i-1,j)X_j,
    w_(t,j)=exp(gamma<u_t,u_j>)-1.

The intended digital predecessor estimate is sign(C_i); any tie rule may be used. The target coefficient is A=exp(gamma)-1>0. Taking two consecutive recovered predecessors would aim to form local innovations in parallel.

The position-dependent coefficients D_i/i and the self subtraction are granted as a favorable exact scalar interface, NOT claimed to be implemented by a shared ordinary FFN. Demonstrating failure even with this correction isolates a genuine problem with this proposed route; it does not prove other decoders fail.

## 2. Average local-recovery obstruction, no execution noise

Test on theta=0 in the fixed-c spin family: raw X_j are iid fair signs, an admissible source for every c<1/2. At target t=i-1, write i C_i=A X_t+Z_t with Z_t=sum_(j<t)w_(t,j)X_j. Target and nuisance are independent.

A unit sphere has a radius-1/2 Euclidean net of at most5^d centers (maximal separated-set volume argument). Assign every code to one covering cell. Points in the same cell are at distance at most1 and so have inner product at least1/2. Put

    B=exp(gamma/2)-1,
    K=ceil(2 A²/B²)=ceil(2[exp(gamma/2)+1]²).

Except for the first K targets in each cell, every target has at least K earlier same-cell keys. Thus, among t=1,...,N-1, at most K5^d targets fail this property. For every other target,

    sigma_t²=E Z_t²=sum_(j<t)w_(t,j)²>=K B²>=2A².

For independent Rademacher signs, E Z_t^4<=3 sigma_t^4. Paley-Zygmund applied to Z_t² gives

    P(|Z_t|>A)>= (1-A²/sigma_t²)²/3>=1/12.

Whenever |Z_t|>A, the independent fair target has the opposite sign with probability1/2, forcing the scalar-sign decoder to err. Therefore

    P(sign(C_(t+1)) !=X_t)>=1/24,
    average_(i=2..N) predecessor error
       >=(1/24) max(0,1-K5^d/(N-1)).

This is an AVERAGE predecessor reconstruction bound under an actual allowed source, not merely a rare worst-word example. It holds with exact real arithmetic and no noise. At fixed d,gamma, it remains a positive constant as N grows. In this interface, achieving average error tending to zero necessarily requires d growing at least logarithmically with N according to this conservative bound. The constants are very loose; the statement does not claim logarithmic width suffices.

For gamma=0 the contrast is identically zero and fair-target error is1/2, separately. The proof neither requires nor bounds correlations among different rows' reconstruction errors.

## 3. Why increasing amplification depth or precision does not repair this route

The obstruction is that the exact noiseless contrast often has the WRONG sign. Amplifying that scalar through any sign-preserving saturation map, for O(log N) or more stages, preserves the wrong sign. Greater execution precision cannot fix systematic crosstalk. This is different from a tiny but correctly signed public-source signal.

An arbitrary nonlinear decoder of several sketches, a different choice of untied Q/K, contextual value processing, or a statistical estimator not reconstructing predecessor bits is outside this statement. In particular theta=0 has trivial next-token predictor1/2, so the reconstruction lower bound is NOT a terminal-risk lower bound. That distinction is central, not a technical caveat.

## 4. Position and norm ledger

The raw Q/K score mechanism alone admits actual initial positive-epsilon full LN with a favorable explicit public feature supply. Use paired coordinates for X_i, all coordinates of u_(i-1), all coordinates of u_i, a constant anchor, and an empty output pair. Residual width is W=4d+6. The nonempty paired input has squared norm8, independent of i,X_i. Full LN with epsilon1 and gain1 divides by sigma=sqrt(1+8/W). Shared Q and K project the query/key code lanes with factor sigma sqrt(gamma), and V selects X with factor sigma. Thus

    ||W_Q||F=||W_K||F=sigma sqrt(gamma d), ||W_V||F=sigma.

Scores and raw values are exactly those above; no external pairwise bias or near-hard mask is needed. At fixed d these are fixed ordinary parameter norms, while whole-key energy is sqrt(gamma N). Public u_(i-1),u_i features and their numerical representation are charged inputs; generation from a lone normalized-position scalar is not supplied. Growing d also grows full LN gain norm sqrt(W) and Q/K Frobenius norms, so it is not a free escape under a frozen full-norm contract.

This is only the initial score/value realization. It does not supply the shared decoder implementing the granted correction or the multi-layer physical full-PreLN circuit. The negative result already applies to the simpler ideal scalar-sign interface.

## 5. Comparison and retained failure paths

(1) Replicating a single-public-source gate for all N targets is not a fixed-width parallel construction: it introduces source-indexed channels/parameters, changes full LN and grows their complete norm ledger. The earlier source-specific proof cannot simply be reused N times for free.

(2) Exact diffuse predecessor-score bias gamma*1{j=i-1} has a separate rank obstacle. Restrict rows i=2,...,N and columns j=1,...,N-1. Every causal entry below the main diagonal is zero and the diagonal is gamma, while unused future entries may be arbitrary. This square matrix is upper triangular with nonzero diagonal, so rank at least N-1. If row-constant shifts are permitted by softmax invariance, a factorization can lower this rank by at most1, leaving rank at least N-2. This exact-score statement is not an approximate-retrieval or statistical-risk theorem.

(3) Bounded low-dimensional unit codes approximate equality in many contexts, but this specific parallel decoder fails because many earlier keys share a geometric neighborhood. Unlike the global-Frobenius small-signal examples, all code norms here remain order one. Tiny score approximation error cannot simply be translated to task error without a gain/probability analysis.

Open: a same-contract, bounded-width/logarithmic-depth parallel local-context compiler using permitted scalar positions, or a direct prediction construction that avoids predecessor reconstruction. Neither is delivered here. The useful output is an independently checkable obstruction to one plausible route, with its precise assumptions and costs.

## Diagnostic coverage

`check.py` checks24 selected code/row cases by exhaustive fair-sign enumeration;19 are in the variance regime of the Paley-Zygmund bound. It also checks all-row average error for identical codes at N=64,128,256 using exact rational binomial probabilities, and80 independent direct two-head correction/self-subtraction identities. These do not prove the covering argument, which is supplied analytically. Causal counting refers to the firstK occurrences of each cell in increasing target index; all remaining neighbors have indexj<t and are therefore already present when rowi=t+1 reads. Every nuisance sign in a given row appears once with deterministic positional coefficient and is independent of the target at theta0; dependence across different rows is irrelevant to averaging expectations.
