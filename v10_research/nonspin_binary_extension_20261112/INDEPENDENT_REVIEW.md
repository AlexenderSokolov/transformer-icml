# Independent review: balanced binary second-order common-pair extension

2026-11-12. Verdict: PASS for the complete source parameterization and the stated extension of the existing tag-aware L2 architecture theorem. This broadens the source class; it does not prove logarithmic-depth sufficiency or a sharp frontier.

## Frozen evidence

THEOREM.md SHA256 712b59ef7e5cde24e2a7d5b13a4d78eef688d1aec9f151816b3f6ef7b5074065

check.py SHA256 2869bdbf9d09721ed68b96f095e5b25929815033832fcf5d0f48e206c7cd25ae

results.json SHA256 bcdda2d093132ac63c0ae66c317fa591496dcf0ac7c1e50ce0426119ea7d6b2f

RECEIPT.json SHA256 e5ecf1b3b06525a651d11229e5026861c1b2292b9e1e14bbf5461532f56d9b8d

I read the full candidate, including its final attribution addition, and independently reread the entire inherited theorem at GitHub ref 9efcda3, v10_research/tag_l2_information_20261112/l2/THEOREM.md, Git blob 71af149bb22bd7ad2ef0c7ce442032053fdc3f98. This was not a review based only on the author's abstract.

## 1. Parameter domain and stationary construction

For xy=1 the conditional-mean numerator takes the two values +(r+s)+t and -(r+s)+t, whose maximum absolute value is |r+s|+|t|. For xy=-1 the analogous maximum is |r-s|+|t|. Since 1+rxy>0, the two displayed inequalities are exactly equivalent to both next-symbol probabilities belonging to [c,1-c]. Multiplication by pi_r yields the displayed triple law. Summing over z gives the left pair marginal, and summing over x gives the identical right pair marginal. Thus a valid homogeneous Markov kernel with stationary initial pair is actually constructed.

The completeness claim is correct: binary Fourier expansion of a triple with fair one-token marginals has no degree-one coefficients; stationarity identifies the two adjacent pair moments. Only r,s,t remain. Conversely, the constructed positive kernel has exactly those moments. The argument is specific to stationary balanced binary second-order sources, not arbitrary nonstationary initial laws. Positivity excludes degenerate pair support.

The first-order test also checks algebraically: the difference between predecessor choices for fixed y is (s-r^2+t y)/(1-r^2). It vanishes for both y iff s=r^2 and t=0. The example with nonzero r is genuinely outside the original spin slice.

## 2. Mixing and source concentration

Every pair-to-pair two-step path has exactly the prescribed two next symbols, each with probability at least c. Therefore K^2(u,v)>=c^2=4c^2 nu(v), with uniform nu, is correct. The invariant distribution is nonuniform pi_r; replacing nu by pi_r without changing constants would be invalid. The candidate explicitly avoids that error. The Dobrushin contraction yields TV distance to pi_r at most (1-4c^2)^floor(k/2); stationarity also gives pi_r(v)>=c^2.

For deterministic position-indexed vector observables bounded by R, condition on Y_j=(X_j,X_(j+1)). The future X_k is the first component of Y_k. Total-variation contraction bounds its conditional centered mean by 2R rho^floor((k-j)/2). Multiplying by the norm of the earlier centered observable, at most 2R, gives the displayed 4R^2 covariance bound with no dimension factor. Summing diagonal and both off-diagonal terms is dominated by the inherited kappa_c^2=4+8/c^2. This constant is conservative but valid uniformly on the full feasible domain. No iid innovation or spin-specific covariance formula is used.

## 3. Architecture linkage and all tag probabilities

Fair token marginals permit the exact same equal-weight unnormalized-sketch reference averaging. Raw references remain functions of their own raw sign and public position only, by causality; actual hidden states need not be token-local. If one model is shared over the full class, the reference is independent of r,s,t. If known r,s are allowed as public parameters, the same construction remains common along the unknown t fiber, which is sufficient for the two-source lower bound.

The complete score, value, FFN residual-domain, artificial-tag, projection and final-readout assumptions from the inherited theorem are expressly retained. They cannot be replaced by bounds only on realized trajectories or selected matrix entries. Public score biases count in the complete score envelope; no centered-key shortcut or whole-key-energy restriction is introduced.

The selection inequality ||Z_R||_L2^2<=sum_r ||Z_r||_L2^2 is unconditional and requires no tag probability lower bound. Hence the raw factor sqrt(2) and free-pair factor 2 stay valid with nonuniform pi_r. Terminal self-sketch cancellation and the actual/reference same-tag stability comparison also remain valid. Minkowski and the prefix-weight inequality yield the unchanged common recursion E_next=(a+2b)E+2f. Thus Lout E_D/sqrt(N+1) is a valid RMS error under the stated free-pair contract. The sharper separated recursion retains the terminal self term as in the parent theorem. There is no hidden conditioning penalty or independence-given-terminal assertion.

## 4. Exact common-template risks

For fixed r,s and t=t0±h, the feasible-fiber condition |t0|+h<=tmax is exact. The two stationary pair laws coincide. The conditional probability difference is h/(1+rxy). Equal-prior L1 template risk at each tag is half that gap; multiplying by pi_r cancels the denominator and gives h/2. Squared template risk is one quarter of its square, giving h^2/[4(1-r^2)]. The midpoint q_(r,s,t0) is feasible and achieves both values. These floors apply to a single common template, not a parameter-aware oracle.

The L1 network correction by (epsilon_-+epsilon_+)/2 follows from L2-to-L1 and triangle inequalities. For squared loss, apply the norm triangle inequality on the equal-prior mixture probability space; the pooled approximation norm is sqrt((epsilon_-^2+epsilon_+^2)/2). This proves the stated squared lower bound with a positive part. Maximum two-source risk is at least this Bayes risk.

A constant public-sentinel template and a raw-last-token template are subsets of pair templates. The same cross-source risk floors therefore apply using their respective already justified approximation errors and denominators. This does not extend the old spin-specific fixed-theta lower formula; the manuscript correctly declines that extrapolation. Varying r across the compared sources would change pair weights and requires a different calculation.

## 5. Concrete example and independent replay

For c=1/4, r=1/10, s=1/20, t0=1/10, h=1/5, tmax=2/5 and both selected t values are legal. Pair masses are 11/40 or 9/40, the common-template risks are exactly 1/10 and 1/99, and a global symbol flip cannot map t=-1/10 to 3/10 while preserving r,s.

I ran the frozen exact-Fraction diagnostic and compared parsed JSON with saved results. Every field matched: 831 feasible grid models, 3162 rejected grid models and 688 enumerated paths. The computed adjacent-triple-product covariances are 59/6600 and 193/19800 in the example, explicitly nonzero. Thus transplanting the spin iid-innovation estimator would be unjustified. These finite checks support the algebra; the general architecture extension rests on the preceding proof, not enumeration.

## Scope

The general row-frequency benchmark supplies unrestricted fixed-c root-N estimation without an iid innovation claim. The new architecture lower remains informative only where its charged E_D/sqrt(N) error is small. It does not settle the logarithmic-depth regime, construct a valid probability predictor, prove a new minimax rate, or establish novelty. The binary Fourier/Bahadur attribution in the draft is appropriately limited; I did not independently re-audit that external citation in this mathematical review. No formal verification or external peer review is claimed.
