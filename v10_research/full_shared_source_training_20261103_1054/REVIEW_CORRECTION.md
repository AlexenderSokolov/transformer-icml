# Source-blind lower-bound wording

In the minimax paragraph of FULL_TRAJECTORY_BASELINE.md, replace “any randomized or source-independent predictor” with “any possibly randomized predictor that is not given θ.” The Le Cam lower is over one prediction procedure whose only source information comes from the disclosed training/test data. A θ-informed oracle can predict exactly and is not subject to this lower. The upper bounds, in contrast, remain valid against even a source-aware attacker. The original note remains unchanged.
