# Additive interpretation amendment after independent review

3 November 2026. Read alongside REPORT.md and review_independent/REVIEW.md. The original report, sealed implementation/protocol and smoke outputs remain unchanged. This amendment narrows interpretation, not numerical results.

The independent reviewer reproduced the saved paths/metrics and confirmed the reported values and legal edit contract. Its check shares the author's forward/proposal/statistic implementation, so this is independent replay/audit, not independent mathematical implementation or formal verification.

## Corrections that govern use of the original report

1. **The random control is nearly uniform.** Its frozen logits had SD 0.01. At M=128 the first-half masses are 0.50393 and 0.49960; the greatest pointwise relative departure from uniform is about 2.72% (review output: 0.027116). This tests only that small-random initialization. It is not a strong comparison against arbitrary or deliberately diverse frozen positional representations.

2. **Models are paired by clean history, not necessarily attacked history.** Each model, baseline and ablation chooses its own finite CE-maximizing proposal. Thus the same clean word can yield different corrupted inputs for different predictors. Uniform-profile ablation changes the predictor's features, can induce feature distribution shift, and also changes attack selection. Its improved descriptive scores are not an isolated causal demonstration that learned positions caused worse protection. The original report's phrase “uniform-profile ablation improves” describes the measured combined intervention only.

3. **A has infinite-CE ties, with substantial practical consequences.** B(w) is strictly interior while A can return 0 or 1. Among 15,360 nonzero-budget A candidate sets, the review found 4,009 infinite maxima, 3,440 sets with multiple infinite candidates, and 3,226 cases in which first-index tie-breaking selected identity as the first infinite-loss candidate. The attack is still a legal history-derived CE attack. It is not a maximizer of true-source TV. The review found 5,855 sets where its selected candidate did not maximize true-source TV within the proposals, with maximum individual gap 0.9375. This latter computation is a post-hoc oracle diagnostic; using it to choose per-history attacks would violate the declared source-independent procedure. More generally, even finite CE maximization need not maximize source-TV for any model. Do not use A's panel score as evidence it faced the strongest available TV attack.

4. **No fixed-half incapability conclusion is supported.** Fixed-half features contain the required counts: at these even horizons their selected-row sum is 2D/M, while the uniform head gives J/M. The short tanh-readout training run did not show a clear fixed-half benefit over count-only training under the tested objective and attacks. It was not directly trained to reproduce the gate, and no approximation or expressivity impossibility was established. “Readout/optimization/objective calibration remains open” is the correct conclusion.

5. **The retained negative statement is only about this smoke.** One seed, 200 updates, a small finite source panel and restricted attack proposals did not demonstrate useful learned positional protection. Selected sample maxima and pointwise SEs do not establish a significant improvement, general-source risk bound, or impossibility. Local hashes are reproducibility bindings, not preregistration or a trusted external timestamp.

## Next action boundary

A targeted calibration has been proposed separately at ../readout_conditioning_calibration_design_20261103/PROPOSAL.md. It directly supervises the known smoothed gate using fixed positional features and contrasts two equivalent feature parameterizations. It is not feature discovery or another robustness sweep. No calibration code, training or new sampling has been executed. Await root review before running it.
