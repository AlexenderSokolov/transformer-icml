# Next problem after AB001–AB003

## Exact unresolved question

For each **supplied** beta, does there exist an estimator A_(M,beta), independent of the actual corruption budget k, attaining the accepted binary H_2(M,k,beta) uniformly for all k=0,...,M? The input remains the whole corrupted binary word; the original terminal pair is protected. The desired scope is arbitrary initialization, with stationary initialization a separately meaningful restriction. The true k is an analyst's bound, not a value secretly passed to the estimator.

AB001 cannot answer this question: its same estimator is compared across beta=0 clean alternatives and a beta=1/M corrupted null. A beta-informed family may legitimately use different maps on those two advertised classes. AB002 eliminates ordinary selected-row add-one, not all beta-informed rules. AB003 gives a joint-blind construction only over square-root-sized admissible ranges, and its range-envelope necessity also compares beta values.

## Evidence now available

- The accepted known-k estimator removes all potentially false designated exits via a soft lower envelope; it is beta-blind but uses k.
- Ordinary add-one produces a harmonic fake-exit loss on rare one-flip words of a sticky stationary first-order source.
- Hard thresholding the designated exit count instead of soft subtraction avoids a logarithm in clean threshold bias: sum over fixed states q_u P(Y_M=u,J_u<=cB/q_u), then use occupation. This yields the small-budget theorem in AB003.
- For larger k, false exits can cross that fixed threshold. The class certificate may detect patterns that look clean only in a weaker beta class.

## Genuine failure that must not be recycled

The zero-like active suffix with b=0 violates positive all-state minorization because P^2(01,10)=b*t=0 while stationary crossing mass is positive. The stationary alternatives in AB001 repair stationarity but have

    P_a^2(01,10)/Pi_a(10)=2r^2(1-a)/a^2.

At the null's beta=2r=1/M this requires a^2<=r(1-a). Thus the large-a portion producing the joint-blind obstruction is not a same-beta family. Changing the prior does not repair a violated class membership condition.

## Possible route, not a theorem or specified estimator

A beta-constrained full-history fit or a continuous certificate-consistency test might distinguish fake exits using other rows. In designated coordinates stationarity gives Pi=(e/a,1,1,b/t)*x on full support, and the all-state certificate includes b*t>=beta*x and e*a>=beta*x. Empirical counts can violate these constraints even when a row-only estimator sees many apparent exits. But plug-in consistency, unknown initialization, finite-sample fluctuations and adversarially altered other rows all require proof. No tested fit, risk bound, selected budget, or generic projection theorem is claimed here.

An attractive proof target would extend the AB003 pathwise comparison so that positive fake-exit bias above the fixed threshold is controlled by a certificate-aware discrepancy with expected cost O(k/M), while the legitimate-exit term retains the accepted weighted occupation bound. This is only a precise route to investigate, not evidence that the desired all-budget estimator exists.

## Established endpoint regimes

Generic ordinary add-one is k-blind optimal in the weak-certificate range beta<=M^-2, and pooling is k-blind optimal at beta=1 (as recorded and source-reviewed in AB002). For a fixed beta bounded below by an absolute constant, the generic beta-cutoff upper is also within a constant of max(M^-1/2,k/M); constants for a merely fixed small beta are not uniform as beta moves. The genuinely unresolved issue is uniform supplied-beta adaptation through intermediate/moving beta and large budgets.
