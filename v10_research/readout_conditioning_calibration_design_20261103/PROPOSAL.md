# Proposed calibration: can the fixed-half readout fit rare-row gate decisions?

3 November 2026. **Design only. Do not run until root review.** This is one bounded supervised-readout calibration, not a broad sweep, feature-discovery experiment, robustness guarantee or new theorem unit. Preserve learned_position_pilot_20261103 and its smoke_v1 unchanged.

## Question and reason

Can the existing width-32 tanh readout fit the explicit smoothed robust rule Q when the correct full/half statistics are already present? If optimization is poor, does an invertible count rescaling help while preserving the representable function class and initial predictions?

The smoke only showed that fixed-half inputs did not help after one short run under a different target and finite CE-selected attacks. Its first-half count differences can be as small as 2/M in normalized input coordinates. A low-visit gate switch can nevertheless change Q by order one. This suggests a concrete conditioning issue to test, without presuming it is the cause.

## Data and target

Fix **M=64 only**, so all statements concern one finite input domain and the rescaling below is a constant invertible transformation. No source-risk or length-generalization claim is tested.

Create 2,048 training words and 2,048 independent validation words from the unchanged CTO prior, with separate fixed seeds. Freeze these words before training. Add a balanced four-word collision stratum to both training and evaluation. Define

    w(r) = 0 followed by r ones, then 00, then (62−r) ones, then 0.

Use r=8 and r=54 and their bit complements. Each word has 66 symbols. For r and 62−r at least two, its complete triple histogram is

    (0,1,0,2,1,0,2,58),

its terminal pair is 10, its selected-row counts are J=1, C(probability-of-1)=0, and its first-half count is D=1 if r<32, otherwise 0. The complementary pair has corresponding complemented counts/endpoint. Therefore each early/late pair has identical count-only inputs but different hard-gate decisions. At M=64, Q equals 1/8 or 7/8 on these words. These are valid deterministic words, not samples from a claimed source distribution.

Use teacher target **Q(w)=(1−2/√M)A(w)+1/√M**, computed from each word, solely as the supervised target. Train the loss

    (1/2) mean_prior KL(Bern(Q(w)) || Bern(q(w)))
      + (1/2) mean_collision KL(Bern(Q(w)) || Bern(q(w))).

Equivalently minimize the corresponding weighted cross-entropy; teacher entropy is parameter-independent. This deliberately changes the smoke's target from B to Q and makes gate disagreements visible. It tests finite supervised fit, not whether next-token training discovers Q. There are **no attacks** and no hidden-source targets in this calibration.

For indexing validation only, also evaluate w(31), w(32) and their complements. Their fixed-half feature vectors duplicate the four gate/orientation classes already present; do not advertise them as independent feature generalization. The fresh ordinary-prior validation words provide the nontrivial held-out feature variation.

## Three conditions, one fixed architecture

Freeze all pooling profiles. Use exactly the smoke's 9-input, width-32 tanh readout and output floor. No extra layer, hard gate, ratio or teacher output is supplied to the trainable readout.

1. **Half-normalized:** the original uniform/half/suffix features x, plus two endpoint bits and 1/M.
2. **Half-count-scaled:** x_scaled=x S, where

       S=diag(M,M,M/2,M/2,M/2,M/2,1,1,1).

   These are the same features in count units. Initialize W_scaled=S^(-1)W_normalized, with every other readout parameter identical. Hence x_scaled W_scaled=x W, so initial predictions coincide on every word. At this fixed M the two parameterizations have exactly the same representable function class; only the parameterization/optimizer trajectory changes. Verify initial agreement to 1e−14 before training.
3. **Uniform count-only control:** replace both half/suffix profiles with uniform pooling and use the original normalized readout. It cannot distinguish either early/late collision pair. Do not include the near-uniform random control: it does not address this particular question.

Also evaluate a nontrainable exact decoder of the fixed-half feature vector. Recover J/M, C/M and D/M from the known normalization; apply the stated hard gate, ratio and smoothing. This oracle is an explicit feature/target consistency check, not a learned baseline. It must reproduce Q to numerical tolerance.

## Fixed optimization budget

Proposed seed values, to be written into the eventual protocol before sampling:

- Initializations: 20261103201, 20261103202, 20261103203.
- Prior training words: 20261103204; independent prior validation words: 20261103205.
- Shared minibatch-index stream: 20261103206, reset for each condition/initialization.

Use the existing symmetric initialization and Adam (lr=0.003, beta=(0.9,0.999), epsilon=1e−8, no weight decay) for the readout only. Run **2,000 updates**, batch size 128: 64 ordinary-prior examples drawn with replacement from the frozen training set and 64 collision examples drawn uniformly with replacement from the four-word stratum. Use the same minibatch stream across conditions and seeds. Checkpoints at 0,200,1000,2000. Three conditions times three initializations is nine small fits, with no hyperparameter search. The already known exact decoder is not trained.

Record full training and validation losses by stratum, collision prediction probabilities, gradient norms by input row, effective first-layer matrices in the original x coordinates, saturation fractions |tanh activation|>0.99, wall time, weights and reproducible indices. The scaling is deliberately not neutral for Adam's effective function-space step. That is the conditioning intervention under study, not a hidden architecture upgrade.

## Checks and finite pass/fail rules

Before any fit:

- Independently enumerate the literal triple counts/half counts of all collision words; verify paired full-count equality and the changed gate.
- Verify the exact feature decoder equals Q and matched initial predictions agree.
- Check gradients for the scaled-input readout as well as the unchanged normalized branch.
- Assert pooling weights never change; attacks and transition tables never enter model inputs or targets.

Count-only information control: on the balanced collision stratum every predictor using the same count-only input for each early/late pair has average KL at least

    log 2 − H_2(1/8), approximately 0.316377 nats.

This follows by minimizing the pair's average cross-entropy at q=1/2. Its contribution to the balanced overall objective is half that number. If the control violates this floor beyond floating tolerance, stop and diagnose leakage, weighting or target errors. This is a four-point diagnostic calculation, not a general statistical lower-bound claim.

A positive *finite fit* screen requires, at the fixed final checkpoint in all three initializations:

- absolute prediction error <=0.05 on every collision word;
- mean KL <=0.01 on fresh ordinary-prior validation words;
- correct oracle, gradient and frozen-profile checks.

Report the actual metrics even if thresholds are missed. Do not choose an earlier checkpoint because it looks better; earlier checkpoints only diagnose dynamics. No attacks or robustness scores are needed to answer this calibration question.

## Interpretation and stopping

- If both half parameterizations fit, the readout can learn this explicit finite supervised target; the original smoke did not test that question adequately. This does not establish learning from next-label/edit objectives or uniform risk.
- If only count-scaled fitting succeeds, with matched initial functions and the same function class, this supports a parameterization/optimization-conditioning explanation **for this calibration**. It does not prove the normalized model is incapable.
- If neither fits, retain the failure. Finite unsuccessful optimization does not distinguish expressivity from optimization impossibility. Do not automatically increase width, tune rates or add seeds.
- If only ordinary prior loss fits but collision predictions do not, the rare-row gate decision remains unresolved and the positive criterion fails.

Stop after the nine declared fits and a source-bound report, or immediately on a violated correctness check. Any next optimizer, feature, objective or width change needs a new reviewed question and protocol. Do not execute this proposed calibration before root review.
