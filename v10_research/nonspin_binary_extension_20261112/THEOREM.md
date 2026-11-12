# Non-spin extension: the full balanced binary second-order source class

2026-11-12. Candidate source-class extension of the independently reviewed tag-aware L2 mean-field theorem. The finite binary Fourier/moment parameterization and Markov-chain tools are standard; no novelty is claimed for them. The new result to review is the extension of the existing architecture argument and its explicit L1/squared-risk separation beyond the one-parameter spin family.

## 1. Exact finite parameter domain and source construction

Fix0<c<1/2 and a=1-2c. Define F_c to consist of all triples(r,s,t) with -1<r<1 and

    |r+s|+|t| <=a(1+r),
    |r-s|+|t| <=a(1-r).                                  (1)

For x,y,z in{-1,+1}, set

    pi_r(x,y)=(1+rxy)/4,
    p_rst(x,y,z)=[1+rxy+ryz+s xz+t xyz]/8,
    P_rst(z|xy)=(1/2)[1+z(ry+s x+t xy)/(1+rxy)].           (2)

Use initial pair pi_r and this homogeneous second-order kernel. The denominator is positive. Conditions(1) are EXACTLY equivalent to each P(+|xy) belonging to[c,1-c]: on xy=+1 the maximum absolute numerator is |r+s|+|t|; on xy=-1 it is |r-s|+|t|. Thus both outcomes have probability at least c. The triple probabilities equal pi_r(x,y)P(z|xy), sum to1, and their left and right pair marginals are both pi_r. This proves compatibility and stationarity, not merely normalization of a proposed triple table.

All one-token marginals are fair. Their pair and triple moments are

    E X_i X_(i+1)=r, E X_i X_(i+2)=s,
    E X_i X_(i+1)X_(i+2)=t.

Conversely, every stationary binary second-order source with fair one-token marginal has a triple law of exactly this form: expand its distribution in the eight Walsh monomials. All three first moments vanish, stationarity identifies the two adjacent second moments, leaving exactly r,s,t. If its transition probabilities are in[c,1-c], its parameters satisfy(1). Thus this is the WHOLE balanced binary stationary second-order class under that positivity bound, not just another isolated algebraic witness.

Genuine second-order dependence is also explicit. For fixed y,

    P(+|+1,y)-P(+|-1,y)=(s-r²+t y)/(1-r²).

The kernel is first-order precisely when s=r² and t=0. The original spin family is the special slice r=s=0. Taking r nonzero gives a different pair distribution and cannot be identified with that slice by relabeling the two symbols.

## 2. Uniform mixing and the correct minorization measure

Let K be the four-state pair-chain transition matrix, (x,y)->(y,z). For ANY starting and target pair, K² has an entry at least c² because the two prescribed next symbols each have conditional probability at least c. Thus

    K²(u,v)>=c²=4c² nu(v), nu(v)=1/4,
    ||K^k(u,.)-pi_r||TV <=rho^floor(k/2), rho=1-4c².      (3)

The reset measure nu is UNIFORM, while the invariant pair law pi_r need not be. One must not rewrite the minorization as4c² pi_r(v). A common reset measure, not its stationarity, is sufficient for the contraction. Positivity also gives pi_r(v)>=c² directly from stationarity. All chains are irreducible, aperiodic, uniquely stationary and have a common fixed mixing bound.

## 3. Exactly which mean-field steps extend

Reviewed source: `Tag-aware L2 mean-field refinement for heterogeneous public positions`, Library libfile_ca2a2b27f1fc81919f6d5de34d65dc51 (parent identifies published commit9efcda3). This candidate was checked against its complete theorem text, not just the older L1 argument.

Keep its ENTIRE architecture contract: token-local raw initialization with public heterogeneous positions; full self-inclusive causal masks; an optional finite terminal tag that cannot flow backward to raw rows; source-independent parameters; a common bounded state/reference/artificial-tag domain; charged complete score bounds, positive-epsilon PreLN/projection and row-map Lipschitz constants; and a final Lipschitz probability head with no further history access. No assumption on whole-key-array energy is added. Public positional data must not encode hidden raw symbols.

The two deterministic raw reference branches still average their unnormalized contributions equally over the fair token marginal. The reference is therefore independent of r,s,t when model parameters/public inputs are shared over F_c. If r,s are public but t unknown, it need only be common over the chosen t fiber. Actual evolved states are NOT asserted to remain token-local; only the reference states do.

For position-dependent vectors f_j(X_j) with norm<=R, put g_j=f_j-Ef_j. By(3), conditioning on the pair state and applying total-variation contraction bounds

    |E<g_j,g_k>| <=4R² rho^floor((k-j)/2), j<k.

The diagonal bound is4R². Summing the geometric series gives the same conservative L2 constant as the reviewed theorem,

    ||i^-1 sum_(j<=i)g_j||L2 <=kappa_c R/sqrt(i),
    kappa_c=sqrt(4+8/c²).                                (4)

No spin-specific covariance identity or iid innovations is used. The pair minorization correction above is the only change needed at this source-concentration step.

The reviewed finite-branch selection identity

    ||Z_R||L2²<=sum_r ||Z_r||L2²

holds for arbitrary tag dependence and arbitrary tag probabilities. It therefore still pays sqrt2 for a raw token and2 for a free pair, even though pi_r is NOT uniform. There is no division by the smallest endpoint probability. In particular, one must not condition on an endpoint and then pretend raw spins remain independent or fair under that conditioning.

All quotient, stability, Minkowski and nonexpansive-reference-projection steps are unchanged. With the reviewed per-layer constants

    a_l=L_l[1+2Lo_l V_l exp(2S_l)Ls_l],
    b_l=L_l Lo_l exp(2S_l)(Lv_l+2V_l Ls_l),
    f_l=L_l Lo_l kappa_c exp(2S_l)(1+V_l²),

one may use E_0=0 and E_(l+1)=(a_l+2b_l)E_l+2f_l. For terminal n=N+1 and actual free pair T,

    ||Q-barQ_N(T)||L2 <=delta_N=Lout E_D/sqrt(n),          (5)

uniformly over F_c. The sharper separated raw/terminal recurrence from the reviewed theorem is also unchanged because branch counts and prefix geometry are unchanged. The same Chebyshev tail bound delta_N²/u² follows. This is conditional on all reviewed architecture/domain hypotheses, not a new automatic assertion about every Transformer.

## 4. Same-pair two-source fibers and exact risk separation

Fix r,s and define

    tmax=min{a(1+r)-|r+s|, a(1-r)-|r-s|}.

When tmax>0, choose t0 and h>0 with |t0|+h<=tmax, and take t_-=t0-h, t_+=t0+h. Both sources have the SAME one-token AND pair marginals. Their pair-tag next-plus probabilities differ by

    Delta_xy=|q_+(xy)-q_-(xy)|=h/(1+rxy).                (6)

For any deterministic common pair template g(x,y), exact equal-prior optimal risks over such templates are

    inf_g (R_abs,-(g)+R_abs,+(g))/2 = h/2,
    inf_g (R_sq,-(g)+R_sq,+(g))/2 = h²/[4(1-r²)].         (7)

For L1, the per-tag optimum is Delta_xy/2; weighting pi_r cancels the denominator and sums to h/2. For squared loss, the midpoint is optimal and its per-tag risk is Delta_xy²/4; summing pi_r gives the displayed1/(1-r²). The midpoint template is q_(r,s,t0), so both bounds are attained within[c,1-c]. These are risks for a COMMON template, not claims that a predictor knowing the true t has unavoidable error.

If actual network approximation errors under the two sources are epsilon_-,epsilon_+ in L2, let epsilon_pool=sqrt((epsilon_-²+epsilon_+²)/2). L1 triangle/Cauchy-Schwarz and pooled L2 triangle yield

    R_abs,equal_prior(Q)>=max(0,h/2-(epsilon_-+epsilon_+)/2),
    R_sq,equal_prior(Q)>=max(0,h/[2sqrt(1-r²)]-epsilon_pool)². (8)

With uniform bound(5), substitute delta_N for both errors. Maximum risk over the two sources is at least the corresponding equal-prior risk. The model/template may depend on the supplied endpoint pair but may NOT be selected using the unknown true t.

## 5. Concrete non-spin, non-relabeling example

Take c=1/4,r=1/10,s=1/20,t0=1/10,h=1/5. Then t_-=-1/10 and t_+=3/10; tmax=2/5, so both are legal with slack. Pair masses are11/40 on equal signs and9/40 on opposite signs. The two sources are genuinely second order and have nonzero adjacent correlation. They are not the original spin slice. A global symbol flip sends t to -t while retaining r,s; it does NOT map -1/10 to3/10, so the chosen comparison is not merely that relabeling.

The exact common-template L1 floor is1/10; squared floor is1/99. Both depend on estimating a real transition difference after endpoint access has already been granted. Numerical/finite-rational checks below verify these values.

## 6. Readout contracts, boundaries and statistical interpretation

A public synthetic-terminal template (one branch) or a token-local raw-last-row template (two branches) is a special case of a pair template. Thus the same two-source common-template lower bounds apply, with the corresponding reviewed approximation bound and denominator. This does not blindly extend the old fixed-theta |theta|/2 endpoint-access formula: that formula used special spin conditional symmetries. Here the robust conclusion is the explicitly proved cross-source same-pair comparison.

If r varies between the two sources, endpoint distributions differ and(7) cannot be reused without reweighting. If tmax=0 there is no nontrivial t fiber. At r=+/-1 pair support degenerates and the model is excluded. If c tends to0 with N, the fixed mixing constant and architecture conclusion must be recalculated. If parameters or public features know true t, the common-template reduction fails. If D/gain makes delta_N large, the risk bound becomes vacuous, as in the original theorem.

Unlike the spin slice, triple products need not be iid here. One may use the independently reviewed general row-frequency statistical benchmark to obtain unrestricted O_c(N^-1/2) risk; do not transplant the iid innovation estimator proof. The standard statistical target remains vanishing risk, whereas(8) constrains the shallow bounded-gain architecture regime. No logarithmic-depth sufficient construction, new minimax rate, or publication-ready optimal frontier is claimed.

## 7. Verification status

`check.py` uses exact Fraction arithmetic for a finite feasible parameter grid, triple/pair compatibility, Fourier moments, stationary pair-chain matrices and K² minorization. It checks the concrete example by full path enumeration and exact L1/squared template risks. Finite checks do not certify the architecture theorem; its extension is the step-by-step analytical argument in Section3. Independent review is requested on this frozen document and outputs.

### Prior-work attribution

The finite binary moment/Fourier expansion is standard. A published reference discussing the Bahadur binary representation is Ekdahl and Koski, *Bounds for the Loss in Probability of Correct Classification Under Model Based Approximation*, JMLR7 (2006),2449–2480, Section4 Example1: https://jmlr.org/papers/volume7/ekdahl06a/ekdahl06a.pdf . This citation supports the standard expansion, not a claim that this exact stationary three-parameter class or the present architecture extension is novel or previously proved there. Stationary compatibility and the finite positivity domain are derived explicitly above. The earlier spin witness is recovered by r=s=0 and is not redescribed as a new source.
