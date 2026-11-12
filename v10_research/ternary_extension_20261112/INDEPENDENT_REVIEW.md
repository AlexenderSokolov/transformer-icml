# Independent review: ternary full causal evolving-K/V source-average theorem

2026-11-12. Verdict: PASS for the complete conditional architecture theorem, not a matching upper bound or unrestricted Transformer claim.

Reviewed TERNARY_FULL_ARCHITECTURE_THEOREM.md SHA256 cbb4270cbaea2a345f0290706d2d6d8053ba885a45afa5ec955803834c0b9bf7. I read all eight sections, not just the earlier source-family candidate. The earlier literature claims were not independently recertified in this mathematical review.

## Source and exact risk separation

For f=(1,-1/2,-1/2), sum f=0 and |f|<=1. Thus every row of P_theta is normalized and its entries are at least (1-h)/3. Starting from uniform pairs, summing over the earlier symbol gives the same uniform pair law after one transition. The two-step pair transition to any specified pair is a product of two conditional probabilities, at least (1-h)^2/9, so alpha=(1-h)^2 minorization against the uniform pair law is valid. The family is not a binary relabeling, although it has the explicitly acknowledged binary latent partition.

At a fixed pair (x,y), the TV gap between theta=±h is (2h/3)|f(x)f(y)|. Averaging over the common uniform pair law gives 8h/27. A deterministic common pair template consequently has equal-prior risk at least 4h/27, by pointwise triangle inequality. This is the correct probability-vector TV calculation, not a reused binary absolute-error constant.

## Hilbert concentration and indices

Set Y_i=(X_i,X_(i+1)). For j>i, the law of X_j conditional on Y_i is the first-coordinate image of the pair transition after j-i steps. The two-step Doeblin contraction gives the stated floor((j-i)/2) rate. For ||g_j||<=R, the conditional centered mean has norm at most 2R rho^floor((j-i)/2); the earlier centered observable has norm at most 2R. Hence covariance magnitude is bounded by 4R^2 times the decay factor, with no dimension multiplier. The diagonal variance is at most R^2, not merely 4R^2. The lag sum equals 2/alpha-1, so variance of the average is at most R^2[1+8(2/alpha-1)]/n, safely below (1+16/alpha)R^2/n. Arbitrary deterministic position heterogeneity is retained. Deterministic sentinel terms cancel from fluctuation; dividing n random terms by a prefix length i>=n gives the stated bound. No mixing property of actual evolved hidden states is assumed.

## References, artificial executions and domains

The references average unnormalized numerator/denominator vectors uniformly over three symbols and divide only afterward. They remain deterministic and theta-independent because source marginals are uniform and parameters/public positions are shared. Raw references remain independent of terminal tag by full causal masking; actual raw states may be contextual.

Every fixed artificial-tag execution is projected after each block, and references are projected as well. These proof projections stay in the common ball. On a word whose true endpoint equals the artificial tag, induction shows the artificial execution equals the true one: both previous states and block computations coincide, and projection fixes the bounded true output. Thus no projection is granted as a physical network operation. The theorem correctly requires bounds throughout the whole argument ball and a G-domain covering all pre-G residual inputs; bounds only on typical or consistent-tag paths would not suffice. Initial artificial tags are also in the ball.

## Branch factors, ratio and evolving-bank stability

For each fixed receiving tag, the sketch is a deterministic token-local function, so unconditional source concentration applies. Selecting the actual raw query among three tags gives the exact L2 union factor sqrt(3) without conditioning. For each fixed terminal artificial-tag execution there is only one query branch; using sqrt(3) there is conservative. Denominators are at least exp(-S), and the ratio Lipschitz bound exp(S)sqrt(1+V^2) is correct.

The score interpolation argument bounds every softmax weight by exp(2S)/i. Comparing values and complete scores gives the displayed query term 2V exp(2S)Ls d_i and prefix term exp(2S)(Lv+2V Ls) average(d_j). This charges evolving Q,K,V, including receiving-query changes and all public score biases in S. Residual/G/projection and Minkowski give exactly the a,b,u recursion. The prefix inequality sum j^-1/2<=2sqrt(i) closes E_next=(a+2b)E+u. Pointwise projected updates and all references remain within the stated domains. The single-head constants cannot be retained unchanged when adding heads; the draft says so.

## Actual endpoint and risk

Each of the nine fixed-tag output TV errors has an unconditional L2 bound delta=Lout E_D/sqrt(N+1). On the actual tag, Cauchy-Schwarz plus the finite-tag identity gives expected TV error at most sqrt(9)delta=3delta. This step needs no uniform tag probabilities and uses genuine L2, not an L1 bound relabeled as L2. Uniform pair probabilities enter only the subsequent source-risk comparison. Combining the common-template floor with the two approximation errors gives the stated equal-prior and maximum-risk lower 4h/27-3delta. Decoder Lipschitzness is explicitly into probability-vector TV; no scalar-to-vector norm conversion is omitted. The constants are conservative, but no missing factor was found.

## Independent finite diagnostics

I ran a new in-memory exact Fraction diagnostic, separate from the author's proof. It tested h=1/2,3/4, theta=-h,0,h and N=2,...,6. It checked transition normalization, uniform stationary pair law, every two-step minorization entry, exact average TV separation 8h/27, and a bounded heterogeneous two-dimensional centered token-observable variance bound. There were 656 assertions and 6534 enumerated paths; all passed. These tests do not prove the general architecture induction.

Reproducible diagnostic definition: for each h and theta, set P(x,y,z)=(1+theta f[x]f[y]f[z])/3 using Fraction and f=[1,-1/2,-1/2]. Check row sums, sum_x P(x,y,z)/9=1/9, and P(x,y,u)P(y,u,v)>=(1-h)^2/9. Enumerate all words of lengths 2 through 6 with probability 1/9 times their transition product. For word x define the two-vector average with components N^-1 sum_j (-1)^j f[x_j] and N^-1 sum_j f[(x_j+j) mod 3], indexing j from 0. Each summand has mean zero and squared norm at most 2. Verify total probability 1 and expected squared norm <=2(1+16/(1-h)^2)/N. Finally sum h|f[x]f[y]|(sum_z|f[z]|)/27 over all nine pairs and verify 8h/27. The diagnostic uses no floating-point approximate probability arithmetic or random seeds.

## Limitations

The result is a finite-alphabet specialization of the existing mean-field mechanism under a strong complete bounded-domain contract. It does not establish novelty, generic initialization mixing after every layer, matching logarithmic-depth sufficiency, finite-precision execution, or a predecessor compiler. Fixed h is essential to uniform mixing constants. If charged gains or depth make E_D comparable to sqrt(N), the bound can be vacuous. Reference determinism and common source-independent parameters are essential; sharing only count expectations would not replace them. No formal verification or external peer review is claimed.
