# Exact low-count feature enumeration and split

3 November 2026. This is a deterministic, finite state-space construction. No model was fitted or sampled, and no optimizer was run. At M=64, it enumerates exactly every feature vector realized by a valid binary word with J≤3. It does not establish any representability or optimization result for a neural architecture.

There are **128 feasible feature vectors in 108 statistic groups**. The specified SHA-256 split yields **117 vectors in 99 train groups** and **11 vectors in 9 holdout groups**. The four collision groups are forced to train. The holdout is small and was not blinded to the prior analysis: the already-inspected worst validation group (J,C,D,U)=(2,1,1,2) is in holdout. Interpret subsequent evaluation as exploratory, not as an untouched independent confirmation.

## Data contract

`rare_states.json` is canonical UTF-8 JSON. The top-level object has `M`, `max_J`, `hash_input`, `hash_rule`, `collision_groups`, and `rows`. Each row represents a unique attainable tuple `(a0,a1,b0,b1,U)`, sorted lexicographically by this tuple, and contains those five integers; `J,C,D`; exact target fields `Q_numerator,Q_denominator`; one 66-character `word` bit string witnessing the feature tuple; and `split`, either `train` or `holdout`. Here `a0,a1` are first-half counts and `b0,b1` are second-half counts of the *terminal pair* followed by zero or one. `U` is the terminal pair coded as 2F+G, and `J=a0+a1+b0+b1`, `C=a1+b1`, `D=a0+a1`.

The existing model expects normalized inputs `[(a0+b0)/64, (a1+b1)/64, a0/32, a1/32, b0/32, b1/32, U//2, U%2, 1/64]`. The count-scaled condition applies its own scaling internally. Each exact target is the quotient of its integer numerator and denominator.

Each statistic group hashes the ASCII text `v10-rare-split-20261103:` followed by decimal J,C,D,U separated by commas and no spaces. A group is holdout if the SHA-256 digest, interpreted as a big-endian unsigned integer, is divisible by 5, except these four groups are forced train: `(1,0,0,2)`, `(1,0,1,2)`, `(1,1,0,1)`, `(1,1,1,1)`. The assignment is group-level, so no `(J,C,D,U)` group crosses the split. Data constructed from the original prior must be filtered according to the same group rule if it is used in training; in particular, never train on a word in a held-out group. The supplied collision examples must be checked under this same rule.

## Proof of completeness and soundness

Fix a target terminal pair `U`. A state after processing `i` transitions comprises the current pair `(w_i,w_{i+1})` and four nonnegative half-counts. At `i=0` every one of the four initial pairs is allowed, with all counts zero. Each legal next bit `b` deterministically changes the current pair to `(w_{i+1},b)`; it increments exactly the selected count if and only if the current pair equals `U`, choosing its first/second half by `i<32` and its zero/one successor by `b`. The algorithm applies both values of `b` to every currently reachable state, retaining a witness for each resulting state.

By induction on `i`, the maintained states are exactly those reachable by some prefix whose selected-pair total is at most three. Pruning states with total exceeding three cannot remove any prefix of a final J≤3 word: counts never decrease. At `i=64`, retain only states whose current pair is `U`. Every retained path is a valid 66-bit word ending in U, and every valid word ending in U with J≤3 follows a retained path. Projecting away the path and current pair produces exactly its `(a0,a1,b0,b1,U)` feature vector. Union over U=0,1,2,3 proves both inclusions. Retaining one arbitrary representative path when a state is reached more than once is sound because future transitions depend only on the stored state, not its history.

The recurrence proves the enumeration scope independently of model behavior. `verify_independent.py` supplies additional computational checks: an independently written backward recurrence produces the identical 128-vector set; the retained calibration's independent literal word-count oracle and feature function verify all 128 actual witnesses, counts, terminal bits and targets; all four collision groups and all hash assignments are checked; and a fresh run reproduces the JSON byte for byte. `test_enumeration.py` exhaustively compares the forward algorithm to brute force at even M=2,4,6,8 and checks all M=64 witnesses. It also confirms no group crosses the split. These checks complement, rather than replace, the proof.

## Reproduction

From this directory:

    python -m unittest -v test_enumeration
    python enumerate_rare.py > rare_states.replay.json
    cmp rare_states.json rare_states.replay.json
    OPENBLAS_NUM_THREADS=1 python verify_independent.py

`tests.log` and `VERIFICATION.json` retain test and independent-verifier outputs. `red.log` records the test-first missing-enumerator check. `SOURCE_BINDINGS.json` hashes source inputs and delivered artifacts. Scripts never modify the upstream calibration. Run from a separate output filename to avoid overwriting the retained result.
