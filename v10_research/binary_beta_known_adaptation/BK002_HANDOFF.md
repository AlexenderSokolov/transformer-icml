# BK002 accepted full-history adaptation handoff

Root accepted BK002 at 2026-11-02 12:56:33.419419 UTC after reading the entire frozen reference-sampler proof and the complete fresh independent review. Acceptance is recorded in `intake/BK002_acceptance.json`; historical candidate wording is preserved in the proof.

## Main result

**Supplying beta and the entire corrupted word does not permit uniform known-k-rate adaptation to an unknown actual edit budget.** The obstruction is already stationary and uses a single source-independent strict-budget kernel with the final pair protected.

For k^2>=4M and k<=T=floor(M/8), at the common supplied beta=1/k^2, the finite theorem gives

    R_null >= [(3k/(2048M)) log((T+1)/k)
                         -32 S_clean log(2T/k)]_+.

Here S_clean is the same estimator map's worst clean risk over the displayed stationary source family. All ordered output-word probabilities are compared; no histogram restriction or hidden clean input is used. If S_clean=O(M^-1/2), k/sqrt(M) tends to infinity and M/k tends to infinity, the corrupted risk exceeds the known-k profile by an unbounded logarithmic factor.

Combining accepted AB003's hard-threshold upper with this new lower yields the sharp statement: a family supplied beta can attain the known-k profile uniformly over all beta and every actual 0<=k<=b_M if and only if b_M=O(sqrt(M)). Constants may depend on a fixed public envelope bound. Sufficiency holds for all initializations; necessity already holds for stationary initialization.

This CLOSES the general uniform-in-beta supplied-beta all-budget question negatively. It does not settle full-history adaptation on a prescribed moving-beta curve such as beta=1/M, does not prohibit beta-dependent constants for fixed positive beta, and is not a pointwise impossibility for each individual large k. A known-k rule may have clean risk of order k/M when invoked with a large advertised maximum; that differs from adapting to the clean actual budget zero.

## Exact accepted evidence

- Proof `BK002_full_history_supplied_beta_obstruction.md`: `e50381632af4825923138c086c34e7b3b082af381d4b9ec8f641825455c50e12`.
- Fresh full review `reviews/BK002_independent_full_review.md`: `41f6a35a5224271a6f8cc70a8b84e4099526257b47aef19eb6f64779ca41c3a4`.
- Root receipt `intake/BK002_acceptance.json` binds both versions and the exact unrestricted-full-history scope.

The author saved `revisions/BK002_initial_candidate.md` before review. The independent reviewer separately saved `reviews/BK002_audit_snapshots/BK002_reference_sampler_received.md`. Both are byte-identical to the accepted proof. The reviewer's `received_to_reviewed.diff` is an actual empty diff. No BK002 proof revision occurred.

## Fresh exact diagnostics

Author: 126 stationary/all-sixteen-entry certificate cases; 63 exact prefix ratios; 45 reference acceptance DPs; 12,319 accepted ordered-path likelihood/strict-budget/endpoint checks; 511 one-quarter bounds. Minimum tested acceptance is about0.885714, versus the proof's1/2.

Independent reviewer: 235 stationary alternatives /3,760 all-state certificate entries; 752 null certificate entries; 312 prefix/interval/density cases; 18 legal-theorem continuation DPs; 108 nonnegative-functional/loss checks including order-sensitive and randomized decoders; 1,932 exhaustive accepted ordered paths; 298 one-quarter inequalities; exact final coefficients. All PASS on the stated instances. Small structural tests outside the joint theorem domain are explicitly labeled rather than misrepresented as full theorem instances.

These diagnostics corroborate the independently reconstructed proof, not formally verify the universal integration or asymptotics. No external peer review or novelty certification is claimed.

## Provenance, actual alternatives and remaining work

`BK002_ACCEPTED_BINDINGS.json` records the accepted proof, author evidence, independent review/checks/snapshots/bindings, exact source versions and root receipt. Accepted AB003 supplies the small-budget upper; SC003 and BT002 supply the known-k comparison profile. `BK002_FIXED_POSITIVE_BETA_PROVENANCE.md` separately identifies SC002 §§1–2 as the generic-upper source for the ancillary fixed-positive-beta remark; no accepted proof byte was changed for this nonblocking clarification.

`BK002_exploration_and_optional_simplification_unreviewed.md` preserves the actual growing-L exploration and root's optional actual-clean-sampler alternative. Neither was substituted into the accepted reference-sampler theorem. Contributor same-beta likelihood and macrocycle notes remain UNREVIEWED, are not proof dependencies, and do not extend the accepted claims.

BK001 remains an independently accepted histogram-plus-initial/final-PAIR obstruction at beta=1/M; it is not relabeled as BK002. Its actual single-paragraph revision and reconstructed-prior-snapshot disclosure remain in its own handoff.

The next focused problem is certificate-dependent adaptation, especially unrestricted full history on beta≈1/M versus the already adaptive weak range beta=O(M^-2). It is isolated in the sibling `binary_certificate_adaptation_phase` directory, not folded into these accepted files.
