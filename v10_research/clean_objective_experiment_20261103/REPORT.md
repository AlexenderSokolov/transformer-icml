# Synthetic clean-objective diagnostic (CTO001)

## Result and scope

This is a fixed-prior Monte Carlo diagnostic of explicit statistical maps, not neural training and not a worst-case robustness experiment. It uses the accepted CTO001 prior without conditioning on any test certificate. Exactly 20,000 independent simulated trajectories were generated for each of seven predeclared horizons, 140,000 total.

At M=64 the estimated clean excess of Q over B is 0.0176684 nats (MC SE 0.0004007). At M=4096 it is 0.000820469 nats (MC SE 0.00001119). These are finite-horizon prior averages. We do not fit an asymptotic rate, extrapolate, or infer worst-case behavior from these points.

| M | TV B | TV A | TV Q | excess KL(B||Q) | MC SE excess | gate rejection | weak tail (exact) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 64 | 0.06919654 | 0.07652156 | 0.09210038 | 0.01766835 | 0.00040074 | 0.018750 | 0.681150 (0.683594) |
| 128 | 0.04993802 | 0.05248450 | 0.06754919 | 0.01077866 | 0.00025045 | 0.006000 | 0.542900 (0.540727) |
| 256 | 0.03579095 | 0.03655612 | 0.04874752 | 0.00634514 | 0.00015291 | 0.001850 | 0.413550 (0.413818) |
| 512 | 0.02549439 | 0.02584674 | 0.03527272 | 0.00422236 | 0.00012196 | 0.000700 | 0.309500 (0.309379) |
| 1024 | 0.01816236 | 0.01823742 | 0.02556006 | 0.00247212 | 0.00003474 | 0.000300 | 0.231800 (0.227524) |
| 2048 | 0.01280313 | 0.01283445 | 0.01803941 | 0.00143130 | 0.00001934 | 0.000000 | 0.161150 (0.165399) |
| 4096 | 0.00906091 | 0.00906999 | 0.01288315 | 0.00082047 | 0.00001119 | 0.000000 | 0.117900 (0.119262) |

## Protocol and uncertainty

config.json and PRE_RUN_HASHES.json were written before the run. They specify horizons, seeds, PCG64 RNG, draw order, and 100 fixed consecutive batches of 200 trajectories. No seeds, horizons, or sample sizes were tuned based on results. Each row parameter is independently uniform and the initial pair independently uniform. The simulator observes M transitions and does not draw the next label. It computes every row count H, first-half row count, and terminal J,C,D, then the true terminal source probability p, Bayes B, oriented half-gate A, and Q.

The exact conditional quantity KL(B||Q) is averaged, avoiding extra next-label noise. H(B) is the conditional optimal expected logloss. Q conditional expected logloss is H(B)+KL(B||Q). Their population quantities remain Monte Carlo estimates. Logs are natural and complementary logs use log1p. Probability bounds, finiteness, total count, and half-count identities are checked. A logloss is not reported: A can be 0 or 1 while B is strictly interior, so population A logloss is infinite; no arbitrary epsilon is substituted.

MC SE is the sample standard deviation (ddof=1) of the 100 independent batch means divided by sqrt(100). CSV intervals are mean ±1.96 MC SE, approximate pointwise normal intervals, not finite-sample coverage guarantees or simultaneous confidence bands. Rare-event normal intervals can extend below zero, and zero observed events give a zero estimated SE without implying zero true probability. In particular, gate rejection was not observed in 20,000 draws at M=2048 or 4096; this is not evidence of an identically inactive gate. No paired significance comparison is claimed from marginal intervals.

The weak-tail fraction is compared with exact 1−(1−2/sqrt(M))^4. All seven deviations are below 1.64 estimated MC SE in magnitude; this is a sanity check, not proof of the simulator. The continuous prior is represented by float64 pseudorandom uniforms in [0,1); endpoint discretization and finite RNG precision are limitations.

## Validation and reproduction

test_experiment.py is an independent literal list-path/count oracle. It exhausts all 8,188 binary words for M=0..10, verifies count and gate outputs and exact rational posterior extension identities and word-mass normalization. Identical pre-generated transition uniforms are also used to compare the vector simulator against independent literal path simulation at M=0,1,2,3,17,64. Separate cases cover both orientations, J=0, the 512D=J acceptance tie, and a one-count rejection. Metrics are checked against direct conditional cross-entropy, and invalid source probabilities are rejected. tests_red.log records feature-missing NotImplementedError errors before implementation; tests_green.log records the four passing test methods. This is not a full repository suite; no repository-level test configuration was found in the inspected root/top levels.

Reproduce the sealed run without preparing a new protocol:

    cd v10_research/clean_objective_experiment_20261103
    python test_experiment.py
    python experiment.py run
    python report.py

Do not run prepare to replay the original protocol: it replaces the timestamp/config hash. run verifies sealed hashes before drawing trajectories. Aggregates and batch means are fully retained; full paths and trajectory-level arrays are not retained, but are reproducible from the declared seeds and code. results.json records Python, NumPy, platform, total runtime and per-horizon runtimes.

Total simulation/aggregation runtime: 8.169 seconds. No external writes, installations, or consolidated manuscript changes were made. The scientific plot uses a logarithmic horizon axis with linear response axes, no fitted line or scaling exponent. Review acceptance is left to the root's independent replay.
