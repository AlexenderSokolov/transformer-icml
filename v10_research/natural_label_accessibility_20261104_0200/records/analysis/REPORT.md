# Natural-label accessibility: bounded exploratory results

All sixteen fixed fits are retained. Primary values are KL(B || q), equal-weighted over M=32,64. Each column is one independent dataset, initialization and minibatch replicate.

| Condition | Replicate 0 | Replicate 1 | Replicate 2 | Replicate 3 |
|---|---:|---:|---:|---:|
| uniform_y | 0.02313405 | 0.01686241 | 0.01561924 | 0.01994519 |
| uniform_B | 0.00982678 | 0.00800445 | 0.00836146 | 0.00770551 |
| learned_y | 0.01297102 | 0.00722922 | 0.00670023 | 0.00986792 |
| learned_B | 0.00337940 | 0.00266802 | 0.00313036 | 0.00335515 |

## Predeclared descriptive screens
- uniform: 3/4 at or below 0.02 nats; median natural-minus-teacher 0.01054882; screen does not pass.
- learned: 4/4 at or below 0.02 nats; median natural-minus-teacher 0.00553699; screen passes.

## Paired primary differences
- uniform_y_minus_uniform_B: 0.01330727, 0.00885796, 0.00725779, 0.01223968
- learned_y_minus_learned_B: 0.00959162, 0.00456120, 0.00356987, 0.00651277
- learned_y_minus_uniform_y: -0.01016303, -0.00963318, -0.00891901, -0.01007726
- learned_B_minus_uniform_B: -0.00644738, -0.00533643, -0.00523110, -0.00435036

## Scope and limitations
- Supplied local triple features and terminal query; this is not an end-to-end Transformer. Uniform pooling already supplies sufficient statistics.
- Bayes-target fits use explicit B supervision; natural-label fits use sampled y only. Both are kept distinct.
- M=128 is out of training length. Full per-cell, rare-row, baseline and paired errors and conditional Monte Carlo SE are in all_results.json; per-example records are in each captured output.
- Four independent replicas do not support strong general training-effect inference. Thresholds are screening rules, not power-justified tests. No hyperparameter or seed selection was performed.
- Neither these outcomes nor failures recover the missing original 20:35 pilot.
- Broad Markov in-context learning is prior art (Edelman et al. 2024; Lepage et al. 2025). No novelty claim is made.
