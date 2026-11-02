# MD001 independent hostile mathematical/interface review

2026-11-02. Fresh independent LLM review, not formal verification or external peer review. Reviewer authored neither upper, lower nor synthesis and did not edit those files. Exact reviewed contents and dependency/receipt hashes are in `MD001_review_source_bindings.json`; numerical corroboration is independently implemented in `MD001_independent_checks.py` and its JSON.

## Verdict: PASS in the precisely stated scope

No outstanding mathematical blocker. The three MD001 proof files establish the uniform fixed-square-root-grid mixing-dependent order **Theta(1+ln f_K)** for the infimum feasible **1+bounded-primitive depth**, with e_K=max(beta,1/M) for K>=3 and e_2=max(sqrt(beta),1/M), for stationary and arbitrary initialization. Necessity is for every fixed positive target multiplier; sufficiency and the least-feasible statement require a sufficiently large fixed multiplier and capacity containing the explicit compander. Root acceptance remains separate. This unit is new post-stage6 research, excluded from the 06:56 stage6 freeze.

Two clarification requests were resolved before final hashing:

* Monotonicity is of the composed scalar T update and the positive accumulator updates, not of every individual affine primitive (the expression for T includes a subtraction).
* Generic encoder precision P cannot be covered by the bespoke fixed coefficient 128 word formula when the architecture-dependent c or chosen P is larger. Final text separates w_enc(P,U,F,...) from bespoke/decoder b_d, retains original-description conversion scratch, and charges conversion writes and simultaneous phase sums.

Neither changes the stochastic or deterministic rates. No author acceptance receipt was written by this reviewer.

## 1. Upper: new binary argument checked independently

The sequential compander recurrence yields the stated piecewise formula. On a geometric segment, put x=t4^-j. The intercept lies between 1/4 and 1/2, and t+1/4>=sqrt(t), t+1/2<=1.5sqrt(t) for t in [1/4,1]. On the bottom segment g=gamma x. Thus u<=g<=1.5u for u=min(gamma x,sqrt x), including L=0 and breakpoints. Moreover u(cy)>=sqrt(c)u(y) follows by applying the inequality to both candidates in the minimum.

The actual generic finite realization has identical coordinatewise code and precision, exact fine-grid T, downward dyadic accumulator floors and downward final /2. Consequently each complete scalar coordinate map is monotone, downward, and exactly zero at zero. Uniform attention's common positive Taylor weight cancels in its exact ratio before histogram flooring; no ideal/finite coarse-label equality is assumed. GD's final g-space error is strictly below 3/Q even including the /2 floor.

If a selected binary bank is positive, the largest true coordinate has largest integer Z and Z>=1. Hence g(y0)=2Z0/Q>=2/Q and g(x0)<g(y0)+3/Q<=2.5g(y0)<=3.75u(y0). Scaling u gives x0/y0<(3.75)^2<16. For empirical exit fraction p<=1/2 this yields v<=16p/(1-p)<=32p; absolute error is bounded by 32p as well. For p>1/2 unit loss suffices. The argument is valid for either choice of successor called exit; zero exits never acquire fake mass. No assertion that nonlinear companding preserves the old sharper minority-floor inequality is used.

Intersecting this purity bound with GD normalization gives min(32p,A_J+B_J)<=A_J+min(32p,B_J). The truncation map is 1-Lipschitz, so adding the true empirical-to-source error gives exactly coefficient 33 on |p-q| and A0=18M/(32z). The true q are (a,b,e,t_exit), not unit crossing caps. The empirical statistical term is the arbitrary-start add-one comparison plus its empirical correction on J>0. The chosen q are proof labels, not program inputs.

For an all-zero bank, u(x_i)<3/Q implies x_i<max(3/z,9/Q^2)<=3/z+9/Q^2. Thus J/M<6/z+18/Q^2. The universal actual-terminal occupation inequality with a positive integer ceiling includes J=0 and gives U4; it does not require an exact J=0 detector. Positive and all-zero banks are treated separately without a division by zero.

BIF's full-support actual-q occupation holds at arbitrary initial law for every A0>0 in the strong domain beta M^2>=1. Its substitution gives 300096/z before absorbing the factor 16/9 inside the logarithm, hence 600192G/z. Singleton support uses BAI003 v2 (6.2); 32*256*A0/M=4608/z and the remaining 8192/M+512/(M+2)<=8704/M. This covers transient initial states and zero transition parameters. Positive-beta support classification is exhaustive. Below beta=M^-2 no such classification is required: the universal K=2 upper gives t=1. Equality belongs to the strong branch. The conservative C_2=2^23 dominates all displayed statistical, reciprocal and grid coefficients.

## 2. Larger-alphabet upper and schedule

AU's stationary/residual decomposition applies to the occupation functional, not its old predictor. For a=3K(K+1)M/z, m>=M/2 produces the displayed factor 6K^3(K+1)/z and argument 160z/[K(K+1)M beta]. Bounding the bracket by 24G gives 144K^3(K+1)G/z. The residual uses Psi(6K^5(K+1)/z) and AU's factor-five envelope; beta=1 has zero residual, and beta<1/M uses universal occupation. These substitutions require no lower stationary-mass bound and cover all supports/starts. Statistical and square-root-count costs are the accepted actual-terminal bounds, not independent-query analogues.

With f=1+ln(1+Q/t), choose public dyadic gamma in [f,2f). Since 1+gamma Q/t<=gamma(1+Q/t), G(gamma Q,t)/gamma<=2. The 1/Q term is O(M^-1/2) only because the theorem fixes c_-sqrt M<=Q. L=O(1+ln f) counts actual repeated primitive operations. This is a promise-indexed existence construction; no free real logarithm/square root or adaptive learning of beta enters runtime. Supplied rational promise descriptions and selection work remain separately paid.

## 3. Binary lower: full nonlinear coupling/tube argument

I checked BI001's stationary law and all-state two-step certificate, not just its scalar lower. With e>=1/M and e<=1/16, the witness has Pi_W>=1/4, e^2>=beta and all rows minorize beta Pi. The initial distribution is its own p-dependent stationary Pi. The reference path mass is pointwise dominated below by 1/(32M), uniformly p; no posterior uniformity after selecting E_j is claimed. The same prior is used throughout the disjoint j events. J>=4, J<=M/4 and every random suffix symbol is late in the domain beta<=1/256, 1<=z<=M/4.

R_p^2 has B-column (p/2,1-p,1/4), all >=1/8. Coupling through this common atom and conditional bridges costs at most 16 differing states in expectation. Emitted symbols disagree no more often. Telescoping the ideal output over those symbols uses GD's late influence, already including historical local radius, and works on formal hybrid histories because frozen-branch contracts are universal. No extra r is needed. The safe 34Gamma/M continuation range gives the Doob variance 34^2Gamma^2 j/M^2; finite-path differentiation inserts R'_p at one transition and gives 34Gamma j/M. These facts hold for nonlinear ideal outputs, not just local sums. They never differentiate finite floors.

With z=Gamma Q the chosen cutoff makes the scaled concentration radius at most tau/2. Mean-curve mesh spacing M/(34zj), finite discrepancy E, floor loss <1 and frozen branch union give a p-independent good-message alphabet <=A_B(1+zj/M). Crucially tau and A_B have no depth/Gamma dependence. Boundary consistency is not conditioned upon; simultaneous good control over frozen branches precedes actual S selection. Source-independent seeds are fixed then averaged with the same prior.

R_p^3 has A-column bounded below by 1/8. Thus good-and-informative-endpoint probability is at least 3/32 for every p. Decoder intervals of radius |I|/(64R_j) cover prior mass at most 1/32. Integrating leaves mass at least 1/16 and reference error at least 1/(2048R_j). Combining pathwise domination and disjoint events gives the displayed harmonic sum. The shifted decreasing-integral estimate holds even at J=4, and J>=U/2 gives the minimum divided by eight. This proves BL1 with the stated 524288 denominator. Real Gamma is allowed; no integrality of z was used.

## 4. Uniform fixed-band necessity, both alphabets

GD's larger-alphabet source/tube supplies the same truncated minimum with e=max(beta,1/M), constants independent of depth. Its three-symbol witness embeds in each fixed K>=3 with unused rows extended as specified. The binary tube gives e=max(sqrt beta,1/M). The synthesis's complete inversion is correct: large beta bounds f; z>M/4 directly forces Gamma>=sqrt M/(4c_+) and dominates f; bounded f uses Gamma>=1. Otherwise 1<=Gamma<f, and x=exp(f-1)-1 with Q^2/M<=c_+^2 makes both logarithm branches >=f/2 once a fixed F is chosen. Exponential domination establishes such F uniformly, not just along a subsequence. This yields Gamma>=c_*f for every legal finite-domain case, including extreme small beta and real Gamma.

Gamma<=C^d follows from GD's actual nonnegative causal influence recurrence with fixed per-stage primitive budgets, local radius, projection and dense-mask constants. It is not CA's old global square-sum constant reused at growing depth. Taking logarithms plus the base bound 1+d>=1 handles bounded f without a spurious positive lower on ln f. The stage-zero convention is benign: with frozen terminal initialization and no global stage the late influence is zero, dominated by Gamma_0=1. Stationary inclusion transfers necessity to all-start guarantees; the same all-start upper implies stationary sufficiency. Neither a growing-depth uniform 1/Q floor nor an all-Q depth surface is invoked.

## 5. Architecture, cut and complete cost scope

Capacity must include the full K^3 bank and rolling scalar-compander rails; output count alone does not suffice. All statistical logits are zero (attention ratio one); gamma is nonlinear gain. Initial terminal state uses only counted finite S/public data; historical local tables stay below T. This excludes an uncharged direct terminal history contribution in the lower. All formal frozen branches obey the contracts.

GD uniform FA uses common per-layer alpha,beta and a depth-independent finite-search c; its recurrence and bootstrap give E=1 at P=4h+c(d+2), increased for purity when needed. The same evaluator includes the upper, with downward exact-zero rails; a generic symmetric approximation certificate alone would not prove the new clipping lemma. All layers, masks, dense zeros, supplied descriptions, conversion, all-token causal work, buffers, inverse breakpoint generation, normalization, final grid rounding, terminal isolation and phase sums remain paid. The revised w_enc/b_d separation prevents precision from silently overflowing an inherited decoder bound. Compiled Boolean/PURE depth is not the optimized primitive depth. No total-bit or minimal-work claim is reviewed.

## Independent executed corroboration

31,383 checks PASS: 4,800 exact rational finite two-coordinate banks (generic final /2 floor included), 6,168 exact monotonicity/downward-error grid cases, 408 exact stationary/minorization witness cases, 408 exact active-chain atom checks, 9,599 harmonic/cutoff cases with real Gamma, and 10,000 dyadic selection cases. These independently support but do not establish the universal claims; the proof review above supplies their mathematical scrutiny. No external publication, upload or contact occurred.
