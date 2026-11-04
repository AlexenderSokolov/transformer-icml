# Fixed alphabet terminal KL at logarithmic rate

Composition note, 4 November 2026. This note combines the frozen, analytically reviewed row-tilting theorem with the separately reviewed five-block exact-real construction and its specialized integer/dyadic evaluator. It does not change any of those source files. The proof statements and complete analytical reviews are reproduced in the accompanying offline HTML.

## Scope and main conclusion

Fix a publicly known alphabet size A>=2. Observe X_1,...,X_{n+2} from an arbitrary homogeneous second-order source on [A]. Its transition rows and initial pair distribution are arbitrary and unknown. Zeros, deterministic rows, reducibility and periodicity are permitted. The target is the true next-symbol row at the actual terminal context Y_n=(X_{n+1},X_{n+2}); there is no fresh independently sampled context. All logarithms in KL and risk bounds are natural.

Let B be ordinary full-history add-one at that terminal context, let L=n+2+A, and for n>=1 define

    K_n = 1+floor(log_2 n),
    V_{A,n} = min{log(n+A),
                  A^4[log A+1536 A K_n]/(n+1)}.

The frozen row-tilting proof gives

    E D_KL(p_{Y_n}||B) <= V_{A,n}.

For every fixed A, this is O_A(log(n+2)/(n+1)), uniformly over the stated kernels and initial pair distributions. Its leading alphabet factor is A^5. It is not a claim of sharp growing-alphabet dependence or of an optimal constant. The proof evaluates the actual full-history estimator; it does not replace it by a minimax-existence or suffix-averaged estimator.

## Exact real five block corollary

Use the unchanged five-block causal attention/ReLU model in the complete exact-real prerequisite. For each fixed A, its learned coefficients are fixed independently of history length and source. Inputs and resource assumptions remain exactly those specified there, including the positional features (1,i,i^2,log i), full causal attention, A smoothing BOS tokens, and ordinary final A-way vocabulary softmax. Let R be its exact-real terminal output.

The prerequisite proves, for every word including n=0,

    TV(R,B) <= min{1,(44A+1)/L},
    R_b >= 1/[1+(A-1)L] >= 1/(AL).

Hence for n>=1,

    E D_KL(p_{Y_n}||R)
      <= min{log[1+(A-1)L],
             2V_{A,n}+2A(44A+1)^2/L}.

The only substitution in the statistical transfer is the new upper bound for E D_KL(p_{Y_n}||B). Its pathwise approximation and support bounds do not depend on which statistical proof is used. For fixed A, the statistical rate is O_A(log(n+2)/(n+1)), with a separate O_A(1/(n+1)) output-approximation penalty. This is an exact-real theorem, not a finite-bit assertion.

## Specialized finite bit corollary

Separately use the exact integer/dyadic evaluator specified in the complete precision prerequisite. It is an explicit numerical evaluation scheme for the same five-block model, with max-shifted exponential approximation, constructed log positions, exact dyadic gates, and mass-preserving normalization. Let Q be its numerical terminal output, and choose

    s = ceil(log_2(AL)),
    b = 32s,  H = 2^b,  F = H^2.

The prerequisite proves, for every word including n=0,

    Q is an exact nonnegative H-grid simplex,
    TV(Q,B) <= min{1,(46A+2)/L},
    Q_b >= 1/(4AL),
    D_KL(p_{Y_n}||Q)
      <= 2D_KL(p_{Y_n}||B)+8A(46A+2)^2/L.

Consequently, for n>=1,

    E D_KL(p_{Y_n}||Q)
      <= min{log(4AL),
             2V_{A,n}+8A(46A+2)^2/L}.

This follows by substituting the same add-one statistical theorem into a pointwise finite-evaluator inequality. It does not infer forward KL from TV alone; the explicit positive support floor is essential. For fixed A the rate remains O_A(log(n+2)/(n+1)).

The value b counts fractional bits, not the entire signed word. Integer positions, score magnitude, accumulation and constant-factor wider products are charged separately, with total working integer lengths O(log(AL)). The exact-real model's learned parameters remain fixed; arithmetic precision is a length-dependent resource. The inherited conservative complete causal evaluation cost is

    O(((A^2+2A+3)L^2+L)b^3
       +(A^3 L^2+A^6 L)b^2) bit operations,

with row-streamed storage

    O(A^3 L b+b^2+A^6 log(A+2)) bits.

This corollary is not a guarantee for generic IEEE, fixed word length, fixed exponent range, GPU kernels, or automatic mixed precision. It is not a matching lower bound on all numerical representations, an optimal compute theorem, a training claim, or an executed implementation certificate.

## The zero transition case

For n=0, B is uniform and D_KL(p_{Y_0}||B)<=log A pointwise. Do not evaluate K_n or V_{A,n} at zero. The two output bounds above instead use

    E D_KL(p_{Y_0}||R)
      <= min{log[1+(A-1)L],
             2log A+2A(44A+1)^2/L},
    E D_KL(p_{Y_0}||Q)
      <= min{log(4AL),
             2log A+8A(46A+2)^2/L},
    L=A+2.

These boundary formulas use the unchanged all-history pathwise guarantees.

## What the sharpening does and does not establish

The decisive joint tail applies a kernel-uniform occupation estimate under an explicitly altered transition law. It is not a multiplication of two unrelated marginal bounds and does not condition selected row counts to be binomial. The initial pair law is retained under the alternative kernel; stationarity under that kernel is neither assumed nor needed.

The arbitrary-start occupation constant must be used after tilting. This argument therefore does not inherit the better stationary alphabet factor from the older log-squared proof. The older proofs and their rate statements remain preserved as historical source text; this composition note supersedes only the statistical upper bound used in these two corollaries.

For fixed A and order two, these three upper bounds match a primary-source stationary minimax lower bound in their dependence on sample length. The precise implication is stated separately below. It does not establish sharp A dependence or resolve every parameter regime of the ordinary full-history add-one question. The binary first-order minimax rate is different, so the displayed O(log n/n) rate is not asserted to be optimal there.

The attached prior-art audit is a bounded search record dated 3 November 2026, not a novelty certificate or exhaustive exclusion of earlier results. Classical occupation, Chernoff, random-count and Markov change-of-measure tools are explicitly distinguished from this particular combination. No new literature search is represented by the act of packaging this document.

## Matching fixed alphabet minimax lower bound

The separate primary-source audit checks the actual-terminal forward-KL loss in Han, Jana and Wu's published Section V-A, Eq. (103), and the second-order lower bound in Theorems 22 and 24. Their observed-symbol length is N=n+2, so the terminal pair and next-symbol target coincide exactly with those used here. Theorem 22 gives

    R_A^stat(n)
      >= A^3/[C_2(n+2)] log[(n+2)/A^3],
    provided n+2 >= (C_2 A)^3,

where C_2 is an absolute constant supplied by that theorem, not assigned a numerical value here. For every fixed A this is Omega_A(log n/n) as n tends to infinity. Theorem 24 explicitly covers binary second-order sources. Binary first-order behavior is not substituted for that result.

The stationary source class is a subset of the class allowing arbitrary initial-pair laws. Its minimax lower bound therefore also lower-bounds minimax risk over that larger class. Every history-dependent probability-vector output, including B, R and Q, is covered by the minimax infimum. Combining that lower bound with the corresponding uniform upper bounds above shows that each of B, R and Q is minimax-rate optimal in n for each fixed A>=2, both over the stationary class and over the unrestricted-initial-pair class:

    worst-case expected forward KL = Theta_A(log n/n),
    as n tends to infinity for fixed A.

This is a worst-case, fixed-alphabet asymptotic result. It is not a lower bound at each individual source, for each prescribed initial distribution, or at every sample length. It does not close the gap between the A^5 upper factor here and the A^3 stationary minimax factor. For Q it still applies only to the specialized evaluator and its paid precision schedule.

Primary reference: Han, Jana and Wu, "Optimal prediction of Markov chains with and without spectral gap," IEEE Transactions on Information Theory 69(6), 2023, 3920-3959, [published DOI](https://doi.org/10.1109/TIT.2023.3239508), [author preprint Section 5](https://arxiv.org/html/2106.13947v2#S5). The complete source-bound applicability audit is embedded after the bounded prior-art audit.

## Review and source status

The frozen row-tilting source has SHA-256 c42b6f1d86c9c91aa6ba8257a86c613150e6fb477deb549cd70d1e7b79548281. Two analytical reports pass its new statistical proof. The first report discloses its preceding discussion of the candidate and is not blind external peer review. The second report treats the output transfer conditionally on the inherited architecture premises and excludes architecture and literature verification; it also gives a separate stronger-constant derivation. This composition deliberately retains the frozen theorem's constant 1536 rather than silently adopting that derivation.

The exact-real architecture and the integer/dyadic evaluator have their own source-bound reviews, included in full. The original candidate-status paragraphs are preserved as historical authoring text, with later review status identified separately. Source-level reviews are not formal verification, external peer review, or a review of arbitrary generated files. The accompanying final-file receipt separately identifies the HTML bytes it reviewed.

No numerical experiment, simulation, training, mathematical sample enumeration, external upload, or public repository mutation is part of this package. Document conversion, hashing, source-equality checks and presentation inspection are integrity work, not numerical evidence for the mathematics.
