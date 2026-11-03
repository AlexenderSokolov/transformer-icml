# Independent review of fixed-half tail geometry

3 November 2026. Scope: ANALYSIS.md, verify.py, analyze.py, SOURCE_BINDINGS.json and retained calibration data/checkpoints. I did not alter author artifacts or publish. No substantive mathematical or numerical error was found in the scoped analysis.

## Mathematical review

- At M=64, integer counts satisfy 0≤D≤J≤64. If D≥1 then J>0 and 512D≥512≥J; if D=0, the original gate J>0 and 512D≥J cannot hold. Thus the gate is exactly D≥1, including J=0. The feature rails determine J=a0+a1+b0+b1, C=a1+b1 and D=a0+a1; the endpoint gives F. Hence all valid words with identical features have identical Q. This is an exact all-word argument, not just an empirical collision check.
- Each half-count pair has C(34,2)=561 nonnegative integer possibilities. Four endpoint-bit choices yield at most 4×561²=1,258,884 feature vectors; consistency constraints can only decrease the number. Base-33 encoding of the four count digits followed by two binary endpoint digits is injective and can be formed as an affine function of normalized or count-scaled input rails.
- For sorted distinct encoded scores t1<⋯<tN and midpoints, each tanh(K(t−mi)) tends to −1 on rows at or below i and +1 above. Subtracting each original row from the next transforms the limiting evaluation matrix to a block triangular form with lower block 2I, determinant 2^(N−1). Its determinant is therefore nonzero for all sufficiently large finite K. Solving for output weights interpolates any desired finite logits, using at most N−1 hidden units. This proves only real-arithmetic existence at arbitrarily large width; it gives no bound on weights, precision, conditioning, width-32 capacity or learning.
- Every Q lies in [1/8,7/8], strictly inside (epsilon,1−epsilon) for epsilon=1/66²≈0.0002295684. Therefore log((Q−epsilon)/(1−epsilon−Q)) is finite; at the endpoints it is approximately −1.947486 and +1.947486. The floor-plus-sigmoid output is exactly Q in real arithmetic. The hard feature decoder is not claimed to be the learned width-32 network.

## Independent numerical checks

- Independently reconstructed first/second-half counts and targets directly from saved binary words. All 4,104 targets agree exactly; 3,530 distinct feature vectors have no conflicting Q. Exhaustive enumeration of all integer pairs 0≤D≤J≤64 confirms the gate equivalence.
- The supplied verify.py runs successfully and reconstructs all saved final scaled predictions. I reran analyze.py with only its script-relative base path and output destination changed in a separate review copy, so it could not overwrite author results. Its regenerated RESULTS.json equals the retained JSON. All 31 file hashes in SOURCE_BINDINGS.json match local files. Such local hashes bind bytes, not an independent timestamp.
- Independently confirmed the common worst validation case, index 1242: (J,C,D,U)=(2,1,1,2), Q=0.5, no matching training statistic or feature, and final predictions 0.9339221, 0.9012888, 0.9231806. The nearest same-endpoint training rows in six-rail L1 distance are exactly indices 797 and 1885, both at distance 2.
- The three final error tails contain 14, 13 and 14 validation trajectories over 0.1 absolute error. In every seed, 10 lack a matching (J,C,D,U) statistic in both prior training and collision words; respectively 3, 3 and 4 have an identical full feature vector in prior training. These are descriptive counts, not independent replication or a causal decomposition.
- Training has 15, 12 and 15 trajectories over 0.1 error, with maxima 0.615896, 0.578985 and 0.613527. The shared worst training case is index 1699, with Q=0.875 and 52 index draws; training row 797 has Q=0.375 and 63 draws. The checkpoint predictions and stated nearest-example values match.
- Worst-validation individual KLs are 0.699495, 0.516596, 0.629967; the >0.1-error tail accounts for 66.824%, 72.957% and 72.134% of each validation KL sum. A single prior-training index has objective mass 1/4096 and a collision index mass 1/8, ratio 512, with the author's qualification about repeated/identical features.

## Reproduction and interpretation cautions

The author reproduction command for analyze.py writes RESULTS.json in place and redirects over run.log. To preserve the sealed analysis, run a copy that redirects both the JSON output path and logs to a separate review directory, as done here. verify.py itself is read-only apart from redirected output. The separately reproduced checks reuse the same frozen examples; they do not create a new confirmation sample.

The coverage/tail observations coexist with observed training underfit, and do not identify which counterfactual intervention would fix either. Counts and tails are post-hoc on a single training/validation sample, shared across the three initialization seeds. No conclusion follows about population-tail probability, source-risk guarantees, effective width-32 capacity, a general optimization theorem, or the original natural next-token/edit objective.

Supporting files in this review directory: independent_check.py, independent_output.txt, a separately directed replay_analysis.py with REPLAY_RESULTS.json and analysis_output.txt, and verify_output.txt.
