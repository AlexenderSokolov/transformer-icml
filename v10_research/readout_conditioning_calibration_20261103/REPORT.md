# Fixed-half readout calibration: count scaling changes finite optimization

3 November 2026. The nine approved fits are complete and stopped. This is an explicitly supervised finite calibration, not natural discovery of a robust predictor, not a minimax experiment, and not a uniform approximation theorem. Original proposal and smoke materials remain unchanged.

## Result and important limit

All three **count-scaled fixed-half** runs pass the declared finite screen; all three **normalized fixed-half** runs miss it. The two parameterizations have the same representable function class at M=64 and exactly matched initial predictions, but Adam is not invariant to this coordinate change. This supports a parameterization/optimization explanation for this particular calibration, not inability of the normalized readout.

Passing the screen means small *average* held-out KL and accurate predictions on four supplied collision words. It does **not** mean that Q was uniformly approximated: the count-scaled runs still have maximum held-out absolute errors **0.401–0.434**, with **13–14 of 2,048** validation words exceeding error 0.1. These tail checks were requested during independent review and were not used to select models, checkpoints or hyperparameters.

All three initializations share the same frozen training set, validation set and minibatch sequence. They are three initialization runs, not three independent data replications.

## Exact task performed

At M=64, keep the uniform/first-half/second-half pooling fixed and train only the 353-parameter, width-32 tanh readout. Its inputs contain counts but not the gate, ratio or teacher prediction. The target is explicitly **Q(w)=0.75 A(w)+0.125**, computed by an independent literal word-count oracle.

Training uses 2,048 CTO-prior words and four deterministic collision words. Each minibatch contains 64 examples sampled with replacement from each stratum, matching the equal-weight objective. An independent 2,048-word prior sample is used for validation. Three fixed initialization seeds, 2,000 Adam steps each, and three conditions give nine fits. There is no attack selection in this experiment.

The collision words are w(8), w(54) and their complements, with w(r)=0, then r ones, then 00, then 62−r ones, then 0. Each early/late pair has identical full triple counts and terminal pair, but D differs. Their Q targets are (1/8,7/8,7/8,1/8). Additional w(31)/w(32) words check boundary indexing only; they duplicate the four feature classes and are not independent feature generalization.

Count scaling multiplies the first six coordinates by (64,64,32,32,32,32). Correspondingly dividing the initial W rows makes the initial functions identical. Both conditions retain identical architecture, information and representable functions at this single fixed horizon. The raw Adam step is nevertheless taken in different coordinates. It is not a comparison with matched function-space step sizes or an optimizer-invariant reparameterization.

## Final declared-screen results

The fixed final checkpoint at step 2,000 is used throughout. A pass requires prior-validation mean KL<=0.01 and maximum error<=0.05 on every supplied collision word, together with passing checks.

| Condition | Initialization | Prior validation KL | Collision KL | Collision max error | Pass |
|---|---|---:|---:|---:|---|
| Half normalized | 20261103201 | 0.0248003 | 0.0264665 | 0.122184 | No |
| Half count-scaled | 20261103201 | 0.00140869 | 0.000001322 | 0.000880 | Yes |
| Uniform count-only | 20261103201 | 0.00689373 | 0.317572 | 0.408006 | No |
| Half normalized | 20261103202 | 0.0238118 | 0.0188402 | 0.089044 | No |
| Half count-scaled | 20261103202 | 0.00164018 | 0.000000534 | 0.000502 | Yes |
| Uniform count-only | 20261103202 | 0.00674876 | 0.317630 | 0.408175 | No |
| Half normalized | 20261103203 | 0.0263742 | 0.0359008 | 0.138782 | No |
| Half count-scaled | 20261103203 | 0.00135190 | 0.000002709 | 0.000930 | Yes |
| Uniform count-only | 20261103203 | 0.00724876 | 0.317384 | 0.405570 | No |

The count-only control respects its exact four-point information floor, log(2)−H_2(1/8)=0.3163770193 nats of collision KL. This is a property of these balanced identical-input/different-target pairs, not a general statistical risk theorem.

## Held-out tails prevent a uniform claim

| Count-scaled initialization | Maximum absolute error | Number with error>0.1 |
|---|---:|---:|
| 20261103201 | 0.433922 | 14/2,048 |
| 20261103202 | 0.401289 | 13/2,048 |
| 20261103203 | 0.423181 | 14/2,048 |

All three largest errors occur at the same validation word, index 1242 in the saved array: terminal pair 10, J=2, C=1, D=1, hence Q=0.5. The three models predict approximately 0.933922, 0.901289 and 0.923181. Thus successful fitting of the supplied J=1 collision cases did not resolve nearby rare-row configurations.

Mean-error calibration cannot be substituted into the accepted all-word/statistic perturbation interface. These observations already rule out claiming small uniform teacher approximation for the retained fitted models. No asymptotic learning rate, general-source protection or natural next-token feature discovery is inferred.

## Verification and cost

The source/configuration seal preceded calibration sampling. Six tests passed before sampling or fitting: literal collision counts and boundaries; independent feature decoder; matched initialization/function-class mapping; every readout gradient in all three conditions; count-only collision floor; and fixed pooling/Adam non-invariance. Maximum analytical/finite-difference gradient discrepancy was 4.72e−9. Before fitting, the independent feature decoder, literal teacher versus original word-statistic implementation, and matched initial predictions each had maximum discrepancy exactly zero over all 4,104 frozen words.

Author verification checked seven sealed inputs and 53 output hashes, recomputed all nine final result rows from retained predictions with zero discrepancy, and checked all 18,000 update rows and 36 checkpoint metric rows. Three initial effective-W matrix pairs are identical. Independent audit/replay was also started by root; its retained checks report identical frozen data/final predictions and independently reconstructed checkpoint metrics to floating tolerance. Final scientific acceptance remains with root's review, not this author's report.

Total runtime was 15.17 seconds with one BLAS thread. Individual fits took approximately 1.04–2.40 seconds. Saved run outputs occupy about 13.04 MB. No dependency installation, additional resource purchase, external write or publication occurred.

## Reproduce and inspect

From this directory:

    OPENBLAS_NUM_THREADS=1 python test_calibration.py
    python run.py run --output independent_replay

The runner verifies PRE_RUN_HASHES.json and refuses to overwrite an existing output directory. A failed correctness check writes FAILURE.json and stops. Do not edit or reseal inputs to replay. Numerical arrays/CSV metrics should reproduce; wall-clock metadata can differ.

- protocol.json, PRE_RUN_HASHES.json and seal.log: fixed choices and input bindings.
- calibration.py, test_calibration.py, run.py: implementation, tests and runner.
- calibration_v1/frozen_data.npz: all words, teacher targets and 2,000 paired minibatch-index arrays.
- calibration_v1/checkpoints/: 36 parameter/scale/effective-W checkpoints.
- calibration_v1/updates.csv: all 18,000 updates, gradient row norms and saturation diagnostics.
- calibration_v1/checkpoint_metrics.csv and final_metrics.csv: complete stratum results.
- calibration_v1/final_predictions.npz: full final predictions, including tails.
- calibration_v1/pre_fit_checks.json, results.json, ARTIFACT_HASHES.json.
- AUTHOR_VERIFICATION.json, tests_final.log and calibration_v1_console.log.

## Scope and stopping

The narrow positive result is that one explicitly Q-supervised fixed-half readout parameterization meets a declared finite average/four-point fit criterion, while an equivalent normalized parameterization under the same raw Adam settings does not within the budget. It does not prove why the original next-token/edit smoke failed, that normalized inputs cannot eventually fit, or that a learned temporal mechanism has acquired robustness. Q supervision, oversampled supplied collisions and fixed positional features are substantive changes from the original task.

Stop here for root review. No new seeds, widths, steps, objectives, horizons, attacks or models have been added after seeing these results.
