# Independent adversarial re-audit of the original bounded-score mean-field theorem

Date: 2026-11-12. Scope: the original evolving-K/V bounded-score theorem, not the newer global/centered-key bridge. Analytical review only; no new numerical experiment, formal verification, or novelty certification.

## Frozen provenance and verdict

Repository: AlexenderSokolov/transformer-icml. Path: v10_research/fixed_c_checkpoint_20261112/MEAN_FIELD_THEOREM.md. The current research/fixed-c-checkpoint-20261112-7b142ee branch file was fetched through the GitHub connector and compared byte-for-byte in memory with commit 03f91a4d0a4408dd1e520b8a0151e9ba38452176. They are identical. Git blob: ab9f745a18ca74ad364be1b4a070097f26d42927.

Verdict: no mathematical gap found under the stated common-domain, token-local initialization, full-causal-mask and source-independent architecture hypotheses. No mandatory correction. The conclusion remains a constant-risk/logarithmic-depth obstruction, not a matching frontier theorem.

## Lines 5–35: architecture, public positions and domains

Public pairwise positional biases may vary arbitrarily with i,j,N and layer, but not with theta or hidden full-history information. They are included in the COMPLETE score bound S. A public additive bias cancels from the score-difference comparison, but its magnitude still changes softmax concentration and the exp(2S) constants. Setting learned Q,K to zero does not remove an external bias from S.

The pair-local score stability inequality is sufficient for the reference construction: fixing receiving/source states while varying other rows forces the score to remain unchanged. The value inequality likewise enforces row-local value dependence. Keys/queries must be the same state-based computational rules across the source family, not maps secretly indexed by the observed full word. This is consistent with the actual architecture specification.

The H-ball and all derivative/Lipschitz envelopes must be common to theta, actual and reference states. Bounds solely along true trajectories would not justify the proof. The text explicitly includes references, FFN residual inputs with convex averages, and final-readout comparison states. Four artificial terminal tags require their declared common envelope or the stated projected artificial executions; projection is a proof device, not a free model operation.

## Lines 66–76: mixing and vector concentration

The stationary pair chain has K²(y,y')>=c² and uniform stationary pi, giving minorization K²>=4c² pi. Its Doeblin contraction is rho=1−4c². Centering a norm-R vector function costs at most2R; conditional-mean comparison costs at most2R times total variation. Thus the stated 4R² rho^floor((lag−1)/2) covariance estimate is valid and dimension-free. The one-step offset is conservative, including adjacent spins.

Summing both off-diagonals and the diagonal gives (4+4/c²)R² i, which is below the declared kappa_c²=(4+8/c²). Position-dependent deterministic functions f_i are permitted. Their expectations are fair-sign averages independent of theta because THIS source is stationary with uniform pairs. This would not automatically hold for arbitrary initial distributions or arbitrary Markov families sharing only transition bounds.

## Lines 78–100: theta-independent nonlinear references

Inductively each raw reference branch is a deterministic function of its own sign and public position/layer information. For fixed query branch r, every reference weighted numerator/denominator contribution is therefore a deterministic token-local function of source sign. All coefficients, public biases and projections are theta-independent. Averaging these sketches over fair signs preserves theta independence.

The construction correctly takes the ratio of expected UNNORMALIZED numerator/denominator sketches, not the expectation of a softmax ratio. It never assumes actual evolved means equal these references.

The receiving raw query tag equals X_i and is correlated with the prefix, including its self row. The proof handles this by bounding the selected error by the sum of the two fixed-branch error norms, then taking unconditional expectation. No conditional independence is used. This is why the factor two in u is legitimate.

Each denominator is >=exp(−S). The quotient bound exp(S)sqrt(1+V²), combined with sketch radius exp(S)sqrt(1+V²), gives exactly the stated forcing 2 kappa_c exp(2S)(1+V²)/sqrt(i).

## Lines 102–116: actual evolving-state recursion

Interpolate the actual and reference SCORE VECTORS while holding one value bank fixed. The convex score interpolation remains in [−S,S], so weights are <=exp(2S)/i. The weighted-average derivative contributes at most2V times the weighted absolute score change. Then separately change values. This gives the displayed query-error coefficient and prefix-average source-error coefficient without requiring differentiability of scores or FFNs.

Residual addition, output projection, row-local Lipschitz map and nonexpansive reference projection give the stated a,b,u. Prefix averaging maps i^−1/2 to at most2i^−1/2, proving E_(ell+1)=(a+2b)E_ell+u. Actual evolved states are never assumed token-local. All growth with depth and normalization gain remains charged.

## Lines 118–130: terminal pair and risk

Public-sentinel and raw-last-row risk reductions use uniform stationary pair law. For the raw last row, the template depends on X_N, not a constant; its predecessor remains fair conditional on X_N.

For the free-pair case, fix each artificial tag tau BEFORE sampling an unconditional source word. This yields a theta-independent q(tau) with unconditional error <=delta_A. On the event actual T=tau, artificial and real computations agree. Since P_theta(T=tau)=1/4 for every theta, the conditional error is at most4delta_A. Averaging over tags preserves4delta_A, not16delta_A.

Comparing theta=0 and theta=h gives target gap h/2 for every tag. The sum of template risks is at least h/2; subtracting both approximation errors and dividing by two yields max(R_0,R_h)>=h/4−4delta_A. The factor four cannot simply be deleted using the newer centered-QK proof: that proof has a different comparison order and terminal self-value cancellation. Any improved tag-aware bound requires a separate derivation.

## Noise and exclusion boundaries

An exogenous random seed is safe only when independent of the source and theta and every fixed-seed network obeys the same uniform contract. Adaptive input-aware residual errors are not such a seed; they require the explicit charged comparison errors. The original noise section states this correctly.

No counterexample arises merely from bounded public positional heterogeneity. Counterexamples would have to violate a relevant condition: uncharged global initialization, a history-dependent side channel, an unbounded/localizing complete score, a selected mask, nonuniform gain/domain constants, or nonstationary marginals. Exact-real information retention is not a counterexample to output-Lipschitz approximation.

The risk threshold and depth statements are explicitly source-uniform or apply to the specified nonzero parameters. Risk at theta=0 alone gives no depth lower. There is no sharp resource frontier, arbitrary-depth impossibility, or novelty conclusion in this audit.
