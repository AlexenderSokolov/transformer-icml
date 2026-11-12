# Tag-aware L2 mean-field refinement for heterogeneous public positions

2026-11-12. This is a refinement of the already reviewed bounded-score evolving-K/V mean-field argument, NOT a new general architecture lower bound. The prior theorem already allowed heterogeneous bounded public positions without a global key-activation energy budget. The new content is a direct finite-tag L2 reference construction, a sharper free-endpoint comparison, and explicit RMS/tail/squared-risk consequences.

## 1. Contract and what is NOT assumed

Use the stationary binary spin source P_theta(z|xy)=(1+theta xyz)/2, fixed c in (0,1/2), |theta|<=1-2c, uniform initial pair. All raw marginals are fair. There are N raw rows and an appended terminal n=N+1, with actual endpoint tag T=(X_(N-1),X_N) in four values optionally supplied at terminal initialization.

Raw initialization may be h_i^0(X_i,p_i,N), with arbitrary PUBLIC position representations p_i. Different positions need not use the same embedding or token-only map. Public parameters/positions may depend on N but not theta or hidden raw symbols. Raw rows never receive the terminal tag or any other global data at initialization. The mask is the full self-inclusive causal prefix, so the terminal tag cannot flow backward into raw rows. Initial values and all true/reference states lie in a common radius-H domain.

At layer ell, the actual residual block is F_ell,i(h_i+O_ell,i A_i). Heterogeneous public row maps are allowed, with common Lipschitz bounds ||O||<=Lo_ell and Lip(F)<=L_ell. Every head value has norm<=V_ell and is Lv_ell-Lipschitz in its source state. COMPLETE scores, including any public positional biases, lie in [-S_ell,S_ell], and for any two banks in the common domain,

    |score_ij(x)-score_ij(y)|<=Ls_ell(||x_i-y_i||+||x_j-y_j||).

These constants include actual full positive-epsilon PreLN and every projection. Public additive score biases cancel in the score DIFFERENCE but still count in S_ell. Parameters are shared across the source family. No global/raw/centered key-array Frobenius bound is assumed. A fixed per-parameter norm budget is sufficient only if it actually implies these uniform score, state and Lipschitz constants; depthwise amplification and normalization epsilon must be charged.

The common domain must also cover reference queries at fixed artificial tags paired with arbitrary raw reference words, including inconsistent endpoint tags. This is a bounded-domain condition for intermediate attention evaluation, not permission to disclose extra data. Reference states can be projected onto the H ball, nonexpansively fixing true states; the FFN Lipschitz domain must include their residual inputs. The final probability map has uniform Lout Lipschitz constant on this domain and may depend on public information/free tag, but has no further historical-row access.

Displayed constants are single-head; multiple heads require summing or otherwise explicitly bounding the actual projection-weighted contributions. Arbitrary hard selected masks, uncharged global features, unbounded gain or nonpublic positional encodings are excluded.

## 2. Reference model with positions retained

At each raw row i maintain two deterministic reference states bar_h_i^ell(+),bar_h_i^ell(-), which CAN vary with position. Crucially the realized raw reference is ONLY bar_h_i^ell(X_i), not a function of its neighbors or the endpoint tag. At terminal maintain four deterministic states bar_h_n^ell(t), one per possible pair t. Initialize them from the actual public/token/tag embeddings.

For a receiving row i and fixed receiving branch r, use its reference state as query. At each raw source row j<=i, average the unnormalized numerator/denominator vector

    f_ij^r(s)=(exp(score_ij(bar_h_i(r),bar_h_j(s)))*v_j(bar_h_j(s)),
               exp(score_ij(bar_h_i(r),bar_h_j(s))))

over s=+/- with equal weights. At terminal, the source j=n contributes its single deterministic self vector for the SAME fixed tag r. Divide the averaged numerator sum by the averaged denominator sum, then use the actual residual/local row map and project into the H ball.

This is a ratio of averaged sketches, not an assertion that an expectation of a ratio equals the ratio of expectations. Every reference is deterministic and theta-independent by induction. Raw references remain tag-free by causality. Terminal reference states depend only on t and the public positional/architectural data.

For fixed r, the functions f_ij^r(X_j) are token-local functions of raw spins, even though the actual network states are contextual. The query tag is held fixed when applying the source concentration bound. It is NOT treated as independent of the source when selecting the realized branch later.

## 3. Exact finite-branch selection lemma

Let R be any random tag with m possible values, and let Z_r be arbitrary jointly distributed random vectors, possibly maximally dependent on R. Then pointwise

    ||Z_R||²=sum_r 1{R=r}||Z_r||²<=sum_r ||Z_r||²,

so

    ||Z_R||L2 <=(sum_r ||Z_r||L2²)^(1/2).               (1)

Thus a common bound ||Z_r||L2<=sigma gives sqrt(m)*sigma, WITHOUT conditioning, independence or any assumption on tag probabilities. The raw query tag R=X_i has m=2, while the actual terminal pair has m=4. The respective factors are sqrt2 and 2, not 2 and 4 from summing first moments. The self-row coincidence R=X_i is covered by the same identity.

This generic sqrt(m) factor is sharp: on a uniform m-tag probability space, take scalar Z_r=1{R=r}; each has L2 norm1/sqrt(m), but Z_R=1. These artificial vectors establish sharpness of the selection lemma, not a lower bound for all attention sketches.

## 4. Fixed-branch concentration and quotient cost

The known fixed-c covariance estimate gives, for arbitrary public position-dependent token-local vectors f_j(X_j) with ||f_j||<=R0,

    ||i^-1 sum_{j<=i}(f_j(X_j)-E f_j(X_j))||L2
       <=kappa_c R0/sqrt(i), kappa_c=sqrt(4+8/c²).

For a fixed query reference branch, R0=exp(S_ell)sqrt(1+V_ell²). At the terminal, its deterministic self contribution cancels exactly; N raw terms divided by n have bound kappa_c R0 sqrt(N)/n<=kappa_c R0/sqrt(n). The fixed-tag source distribution is NOT conditioned on the event T=t. It remains the original unconditional source law.

The empirical and reference normalized denominators are both >=exp(-S_ell), and their ratio vectors have value norm<=V_ell. Hence the quotient map obeys

    ||a/d-a'/d'||<=exp(S_ell)sqrt(1+V_ell²)||(a,d)-(a',d')||.

Applying (1) before this pathwise quotient bound yields an L2 reference-bank attention fluctuation cost at most

    sqrt(m_i) kappa_c exp(2S_ell)(1+V_ell²)/sqrt(i),

where m_i=2 at raw rows and m_n=4 for the free-pair terminal. This is a direct actual-tag comparison. There is no later conditioning penalty, no division by P(T=t), and no hidden assumption that raw observations are independent given T.

## 5. L2 layer recursion with fully evolving Q/K/V

Let e_i^ell=||h_i^ell-bar_h_i^ell(X_i)||L2 for raw rows and e_n^ell=||h_n^ell-bar_h_n^ell(T)||L2. First compare actual attention with the empirical reference bank at the SAME realized raw signs and terminal tag. Bounded-score stability gives a pathwise query/row discrepancy bound. Then compare that bank to the deterministic averaged-sketch reference as above. Minkowski's inequality for L2 gives

    e_i^(ell+1)<=a_ell e_i^ell+b_ell i^-1 sum_{j<=i}e_j^ell
                   +sqrt(m_i) f_ell/sqrt(i),            (2)

where

    a_ell=L_ell[1+2Lo_ell V_ell exp(2S_ell)Ls_ell],
    b_ell=L_ell Lo_ell exp(2S_ell)(Lv_ell+2V_ell Ls_ell),
    f_ell=L_ell Lo_ell kappa_c exp(2S_ell)(1+V_ell²).

This comparison fully charges evolving queries, keys and values. No actual later row is assumed token-local. The raw references alone have that property. Pointwise-only layers have their actual local a, with b=f=0.

A simple common envelope is E_0=0,

    E_(ell+1)=(a_ell+2b_ell)E_ell+2 f_ell,
    e_i^ell<=E_ell/sqrt(i),                             (3)

including the free-pair terminal. It follows from i^-1 sum_{j<=i}j^-1/2<=2/sqrt(i). All expectations and L2 norms are unconditional under the chosen theta, uniformly over the source family.

A slightly sharper separated recursion keeps R_0=T_0=0 and

    R_(ell+1)=(a_ell+2b_ell)R_ell+sqrt2 f_ell,
    T_(ell+1)=(a_ell+b_ell/n)T_ell+b_ell alpha_N R_ell+2f_ell,
    alpha_N=n^-1/2 sum_{j=1}^N j^-1/2<2.

Then raw e_i<=R_ell/sqrt(i) and terminal e_n<=T_ell/sqrt(n). The b/n terminal self contribution is kept explicitly. Either recursion is valid; (3) is simpler and independent of N apart from the final denominator.

## 6. Output approximation, tails and risk

Let qbar_N(t) be the actual final probability readout applied to bar_h_n^D(t), and delta_N=Lout E_D/sqrt(n) (or use T_D). Then

    ||Q-qbar_N(T)||L2<=delta_N,
    P_theta(|Q-qbar_N(T)|>u)<=min(1,delta_N²/u²), u>0.    (4)

For equal prior theta=+h,-h with fixed0<h<=1-2c, the endpoint pair is uniform under BOTH parameters. At each pair, the two target probabilities differ by h. Every common template qbar_N(T) therefore has equal-prior absolute risk at least h/2 and mean squared risk at least h²/4. Triangle inequalities in L1 and L2 yield

    R_abs,equal_prior(Q)>=max(0,h/2-delta_N),
    R_squared,equal_prior(Q)>=max(0,h/2-delta_N)².        (5)

The maximum risk over the two parameters is at least the corresponding equal-prior risk. These are squared probability errors, not log loss or classification error. For comparison of theta=0 and theta=h, replace h/2 in (5) by h/4. This improves the previous artificial-tag/conditioning bound h/4-4delta to a DIRECT h/4-delta bound under the explicitly stated common-domain assumptions.

For public sentinel or raw-last-row output, the known fixed-theta versions follow using the constant or own-token reference and stationary uniform pair. They do not require a new architectural conclusion.

## 7. Novelty boundary and usefulness

The pre-existing heterogeneous-position bounded-score theorem already required no global key activation energy. This note does not rebrand that as new. Its refinement is the unconditional finite-tag L2 comparison, direct free-pair reference recursion, RMS/tail control and charged squared-risk consequence. It replaces a loose first-moment/conditioning step, not the underlying Lipschitz depth scale.

With fixed per-layer bounds, E_D can grow exponentially in D. Thus the approximation is useful when Lout E_D=o(sqrt N), in particular fixed D, and may give the same logarithmic-depth necessary scale. It is not a sharp frontier, a theorem that logarithmic depth suffices, or a claim of good prediction by the deterministic reference. Strong positional localization requiring S to grow, growing FFN gains, tiny LN epsilon, nonpublic position features or hard masks must be charged and can make the bound vacuous.

No numerical risk certification is asserted. The selection lemma and induction are analytical; finite unit checks only verify their bookkeeping on small exact probability spaces.
