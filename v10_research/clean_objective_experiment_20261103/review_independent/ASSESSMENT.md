# Independent review of bounded CTO001 synthetic diagnostic

Verdict: ACCEPT as a reproducible finite-horizon clean-prior Monte Carlo diagnostic, with the scope and uncertainty caveats below. No substantive implementation or reporting error found. This does not validate neural training, adversarial simulations, worst-case constants, or an asymptotic empirical rate.

## Frozen sources and replay

BINDINGS.json records independently verified SHA-256 bindings for every file in PRE_RUN_HASHES.json and ARTIFACT_HASHES.json, including accepted CTO001 statement and root acceptance/replay records. No original author artifact was modified. Original config creation time is 2026-11-03 04:25:28 UTC; filesystem modification times agree, and result/run records follow at 04:25:37 UTC. Run checks every pre-run hash before generating samples. The protocol supplied by the parent before this review matches the frozen config: seven horizons 64 through 4096, 20,000 trajectories each, fixed seed list, 100 consecutive batches of 200.

The isolated replay copies the original simulator/config/tests/report and the three theory bindings. Four author test methods pass freshly (tests_replay.log), the complete original run succeeds (run_replay.log), and chart regeneration succeeds (report_replay.log). Both CSV files and the PNG are byte-identical to the originals. Runtime/environment metadata is naturally not required to be identical. check_independent.py and CHECKS.json preserve independent verification work.

These are retrospective artifact and transcript-consistency checks, not an externally timestamped preregistration or proof that no unrecorded earlier experiments ever occurred. No evidence of tuning, seed selection, omitted declared horizons, or cherry-picking occurs in reviewed files. Every declared horizon and metric appears. Do not strengthen this to an independently provable absence of all prior trials.

## Simulator and statistical target

- Each horizon uses a distinct fixed PCG64 seed. Within a horizon four row probabilities per trajectory are drawn independently, then an independent uniform pair, then one fresh random number per trajectory per observed transition. Trajectories do not share a latent source. This implements intended independence under the pseudorandom model, not mathematical independence of deterministic PRNG output. Continuous uniforms are represented in float64 [0,1), as disclosed.
- Exactly M transitions are observed. Counts are incremented for the old state before the next state is formed. Terminal probability p is selected from the actual same source at the final pair. No next-label draw enters counts or loss. There is no conditioning on any robustness certificate or rejection-based sampling.
- Row index is 2*first+second. The designated successor is 1-first; A is complemented exactly when first=1. Rejection therefore yields probability-of-one zero for first=0 and one for first=1. This correctly preserves the accepted orientation, including J=0.
- The first-half window uses t<floor(M/2), not a rounded or terminal-inclusive window. The accepted tie is 512D>=J, provided J>0. B=(H[U,1]+1)/(J+2) uses all M observed departures. Q=(1-2/sqrt(M))*A+1/sqrt(M).
- There is no epsilon clipping. B is strictly interior; Q is bounded by s and 1-s. At maximum declared horizon these ranges are safely away from numerical underflow. Complement logs use log1p(-p). KL is evaluated using float64 log operations; the tiny negative tolerance is an assertion tolerance, not clipping. A may be an endpoint and its logloss is deliberately omitted.
- TV values compare each rule with actual source p. Excess KL uses the posterior Bernoulli B and Q, exactly the conditional expected excess formula rather than noisy sampled-label losses. Conditional entropy and cross-entropy are evaluated analytically in floating point and then averaged over sampled words. The population averages are Monte Carlo estimates, not exact population values.

## Independent checks beyond original tests

check_independent.py reconstructs literal scalar trajectories for 285 cases over M=0,1,2,3,5,17,63,64,65,128,256,512,1024,2048,4096, using separately generated fixed uniforms. It identifies selected departures by literal pair comparison and checks J,C,D,B,A,acceptance,terminal row and actual p against the reviewed vector simulator. For M>=64 it also checks direct conditional cross-entropy and a distinct algebraic KL expression. These checks do not call the author's path/count oracle.

A separate rational likelihood enumerator checks 2,044 words for M=0..8, exact word-mass normalization, and exact rational predictive extension ratio. The original fresh suite additionally exhausts 8,188 words for M=0..10 and tests the exact acceptance tie, one-count rejection, both orientations, J=0, invalid probabilities and identical-uniform scalar/vector equivalence. Exact Fraction identities concern finite small-word algebra only. Neither the large simulation nor its logarithms are exact rational computations.

Every one of 70 aggregate rows was independently recomputed from all 7,000 saved batch means using math.fsum and the declared sample-variance formula. Maximum mean/SE/interval discrepancy is 1.11e-16. CSV numeric values agree with results.json. The 100 batches are fixed equal-size independent trajectory groups, so averaging batch means equals trajectory averaging. MC SE is batch SD with ddof=1 divided by 10. Intervals are mean +/-1.96 MC SE, approximate pointwise normal intervals, not simultaneous or certified coverage. The report appropriately flags zero-event zero-SE and possibly negative rare-event lower limits. Gate rejection absence at the two largest horizons is not proof of zero rejection probability.

Weak-tail probabilities use the actual four source rows and min(p,1-p)<M^-1/2. The analytic prior probability 1-(1-2/sqrt(M))^4 is correctly matched; standardized deviations range from -1.636 to 1.331. This is a limited randomization sanity check, not a goodness-of-fit proof.

## Figure and scientific claims

The original PNG was opened and visually inspected. Titles, labels, legends and ticks are legible and unclipped. The two panels show conditional excess and the three true-source TVs at exactly the seven CSV horizons. report.py reads results.json; those values were checked against CSV, and regeneration produced a byte-identical PNG. Error bars are the declared 1.96 MC SE. Log2 horizon axis and linear response axes are clearly labeled. Joining observed points is not presented as a fit. No fitted exponent, rate inference, extrapolation, neural optimization outcome, learned representation result, or worst-case robust-risk measurement is claimed.

The report's wording “exact conditional quantity” refers to the exact analytical conditional formula evaluated in float64, not exact arithmetic. Its explicit float64 limitation and distinction between conditional quantities and population Monte Carlo estimates make the meaning adequately clear. Future reuse should preserve that distinction and the finite-horizon scope.

Review did not install software, change manuscript content, make external writes, or alter frozen results. Acceptance is limited to this diagnostic and these pinned artifacts.
