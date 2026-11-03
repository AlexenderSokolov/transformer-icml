# Learned positional pooling smoke pilot

Goal: implement and test the proposed small NumPy model, then run one fixed exploratory smoke experiment and stop for root review. This is not preregistered research, a training guarantee, or a minimax experiment.

Spec: ../learned_position_direction_20261103/RECOMMENDATION.md. This plan specifies the smaller exploratory smoke run below.

Files: protocol.json fixes samples/seeds/optimizer/evaluation before sampling; pilot.py owns simulator/model/attacks/training/evaluation; test_pilot.py owns independent literal and finite-difference checks; run.py is the sealed entrypoint; results and logs remain local.

1. Write fixed protocol and unit tests before implementation. Observe expected missing-module failure.
2. Implement word simulator, posterior/count controls and legal block attacks. Check exhaustive small words, source/label-independent API, endpoints/budget/ties and simulator oracle.
3. Implement learned pools, readout/backprop and Adam. Check every analytical parameter gradient by central finite differences; frozen-control invariance and clean objective/posterior identity.
4. Seal code/config/test hashes; execute all tests and the fixed small smoke pilot with single-thread BLAS. Save initial/final parameters, full per-step logs, test aggregates and timing. Do not expand automatically.
5. Verify generated artifacts and report actual metrics, weak calibration, inconclusive cells and next decision. Root independently reviews/replays.

Scientific constraints: no hidden theta/label access by attack functions, no data-selected hyperparameter changes, no finite tests described as minimax proof.
