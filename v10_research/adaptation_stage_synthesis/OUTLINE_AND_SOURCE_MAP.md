# Positional counts and unknown-budget robust prediction — synthesis outline

**Preparation status, 2 November 2026:** the critical/strong-band all-start theorem and the histogram/boundary-window obstructions are accepted. The exact full-history domain classification and the paid twelve-coordinate finite-cut extension are separate candidates. This outline does not promote those pending units. Their eventual acceptance receipts must be checked before drafting the corresponding conclusions as established results.

## Scientific narrative

### 1. The question is adaptation, not merely estimation

Fix binary homogeneous second-order sources, the all-state certificate `P² >= beta Pi`, strict edits of at most `k` of the first `M` symbols, and a protected final pair. The predictor is judged by unconditional TV at that pair's true next-symbol law. Source parameters, original interior, mask, seed and `k` are hidden. State explicitly whether `beta` is supplied; distinguish arbitrary actual starts from stationary witness laws.

The known-budget profile is `H₂ = min{1, max{M^(-1/2), F₂}}`, where

    F₂ = (k/M) [1 + log(1 + 1/(k max{sqrt(beta), 1/M}))]

for `k >= 1`, and `F₂ = 0` at `k = 0`. Uniform adaptation over all certificates and budgets is impossible even with the full corrupted word. This leaves prescribed certificate domains, not another attempt to overturn that lower bound.

### 2. Compression can remove exactly the information needed for adaptation

At `beta = 1/M`, global triple counts plus the initial/final pairs cannot support all-budget adaptation, although those counts capture the clean homogeneous path likelihood. Even adding the genuine first and last `r` symbols fails when `r = o(M^(1/3))`. The last statement concerns exactly those endpoint windows, not all interior pattern counts or arbitrary local-feature encoders.

The contrast to develop is not “more computation beats a lower bound”: positional information changes the statistical observation. Four first-half row counters, in addition to the global triple histogram and protected pair, suffice. No assertion of counter minimality follows.

### 3. A simple positional gate restores the critical rate

Describe the same budget/certificate-blind estimator explicitly. For terminal row `u`, use its full departure count `J'`, designated-success count `C'`, and first-half departure count `J1'`. Output `C'/J'` if `J' > 0` and `512 J1' >= J'`; otherwise output designated probability zero. The designated symbol is the complement of the first bit of `u`.

The accepted all-start upper is

    min{1, 2^16 M^(-1/2) + 2^16/(M sqrt(beta)) + 2^23 k/M}.

At `beta >= c/M`, this is the known-budget order `min{1, max{M^(-1/2), k/M}}`, simultaneously for every budget, with constants depending only on fixed `c > 0`. Arbitrary unsupported initial states are included. The earlier stationary proof remains a separate valid result, not a purported all-start reversal argument.

### 4. Why the gate works

Give a proof roadmap rather than duplicate the accepted derivation: Hamming perturbations change each relevant count by `O(k)`; wrong gate decisions force small clean terminal rows; balanced rows admit an `O(1/M)` terminal-weighted inverse-occupation bound; the rejected clean histories cost a weighted imbalance term `O(1/(M sqrt(beta)))`.

The all-start proof retains the target stationary mass inside a JOINT terminal/upper-occupation tail, using a hitting potential, a loop identity and an auxiliary exponential tilt. Singleton stationary supports require a separate transient argument. Neither global square-root-beta mixing nor IID row samples conditional on the terminal state are used. Established first-hit pointmass background is attributed explicitly; no novelty certification is made.

### 5. The exact certificate-domain comparison — await the full-history receipt

Accepted histogram classification: adaptation on a public domain `E` is possible exactly when

    sup_E min{M² beta, 1/(sqrt(M) beta)} < infinity,

with value zero at `beta = 0`. The pending full-history synthesis replaces the second term by `1/(M beta)`. If accepted, display the two criteria side by side, including arbitrary sparse/oscillating domains, not only power laws. Explain the weak-certificate branch relative to the beta-dependent oracle benchmark: this is not nonmonotonic absolute estimation difficulty.

For the prospective full-history sufficiency, distinguish the beta-blind balance rule on the strong band from the supplied-beta selector between weak-band add-one and strong-band balance. Do not call the selector beta-blind.

### 6. Finite communication without a free positional side channel — await its receipt

The pending fixed encoder exports eight global triple frequencies and four first-half subfrequencies, all normalized by `M`, through a twelve-coordinate noisy quantized cut. The protected pair is the only additional data-dependent endpoint input. The half indicator is a public positional feature that is explicitly generated/read and paid, not an uncharged history statistic.

If accepted, state the fixed-encoder rate on `beta >= c/M` as

    min{1, max{M^(-1/2), k/M, delta, 1/Q}},

for one decoder ignoring `k`, `delta` and `beta`. Explain why adding four ports requires a fresh complete-message precision lower rather than importing an eight-port lower. State the sequential finite arithmetic, storage and information-isolation accounting; no fixed neural depth, training result or architecture-family lower follows.

### 7. What the failed routes taught, and what remains open

Retain the earlier exact-run and near-prefix vetoes as valid partial risk-increment results. A concrete attack bypasses the fixed near-prefix wrapper around the small-budget threshold estimator; it does not disprove all full-history estimators. The balance rule changes the observable geometry rather than merely enlarging that veto.

Limitations: no sharp endpoint-window threshold at `M^(1/3)`; no minimal number of positional summaries; no uniform all-certificate adaptation; no matching finite-cut surface below the stated band; no free resource transfer from a statistical estimator; no comprehensive novelty search or formal/external peer review.

## Exact source map

`SOURCE_MAP.json` binds the relevant acceptance receipts, proof/review hashes, actual reading scopes, and the two pending candidate hashes. In the eventual manuscript, use descriptive scientific references linked directly to these files, with unit IDs confined to reference/provenance entries rather than the main exposition. Accepted proof bytes and historical status headers are not to be rewritten.
