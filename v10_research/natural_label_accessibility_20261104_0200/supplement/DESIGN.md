# Natural-label accessibility of the v10 clean predictor

Design version 1, 2026-11-04. This is a bounded, exploratory implementation study, not a preregistered external study or a new Markov-ICL result. No training or experimental sampling has run for this design. The initial source package is subject to independent scientific and capture review before execution.

## What it adds

The v10 add-one/finite-network results establish statistical performance and representability, not that a small optimizer learns the desired map from ordinary next-token labels. Existing public learned-position experiments supervised the clean posterior B or the robust gate Q; later rare-weight experiments also explicitly supplied Q. The new question is narrowly different: **on a fixed fresh-source task, how much of the finite optimization gap comes from natural label noise, and how much from learning a query-dependent pooling map rather than receiving uniform sufficient statistics?**

Population conditional expectation makes the natural-label and B-target gradients equal at any fixed model, but finite datasets and trajectories differ. A positive experiment adds finite evidence of accessibility for this exact model/optimizer/budget. A negative experiment locates a finite obstruction, not a learning lower bound. It does not establish a Transformer theorem, robustness, uniform risk, the new A^5/A^3 rates, or novelty.

## Alternatives and choice

1. Repeat Q-teacher/rare-reweighting fits: rejected because already archived, including explicit failure tails and retention corrections.
2. Build a full raw-token Transformer now: deferred because no existing tensor-autodiff framework is installed and this would mix local-feature construction, content selection, normalization, optimization and objective issues.
3. **Chosen:** a matched 2×2 conditional-label study in NumPy, with supplied local triple indicators and terminal pair. This is a small query-conditioned attention readout, not an end-to-end Transformer. Both models use the same 21-dimensional readout and the same raw history information. Pooling changes trainable parameter count, so any advantage is not claimed to be equal-parameter superiority.

## Data, targets, model and controls

An independent episode draws four Uniform(0,1) transition-row probabilities, a uniform initial binary pair independent of those probabilities, and M+1 Markov transitions. W contains the initial pair and first M transitions; y is the final withheld successor. The final label is excluded from all counts and input features. Each episode has its own independent source. This is not the same-source multi-episode experiment; pooled training-row estimation of one common source is not a valid comparator.

Training uses 4,096 episodes at M=32 and 4,096 at M=64 per replicate. Four independent replicate bundles vary dataset, minibatch and initialization seeds together. These are four independent complete experiments, not four seeds on one dataset; the design does not separate data and initialization variance. Every condition within a replicate shares the exact words, labels, initialization and minibatch indices. No sample is rejected.

Let H_t be the eight triple counts and U the terminal pair. Two heads each pool one-hot triple values, with head h and query U having eight trainable scores S[h,U,t]. Their output is H_t exp(S[h,U,t])/sum_j H_j exp(S[h,U,j]). This equals a tokenwise softmax over the supplied local triples in real arithmetic. No positional feature is present. The uniform control fixes all scores at zero, yielding duplicate H/M heads. Thus the uniform control already has the sufficient statistics for B; the learned model cannot claim a new information channel. The efficient count-based implementation is not a bitwise implementation of a full tokenwise Transformer.

Concatenate the two eight-dimensional head outputs, four terminal-pair one-hot coordinates, and 1/M. A 32-unit tanh layer plus scalar logit/sigmoid produces q=eta+(1-2eta)sigmoid(z), eta=(M+2)^(-2). Readout has 737 trainable parameters; learned pooling adds 64. All scores start at zero; the paired conditions have identical initial predictions. Readout weights use independent normal draws with the stated Xavier-like scales in protocol.json, biases zero.

Conditions: uniform_y, uniform_B, learned_y, learned_B. y conditions see only the sampled next token; B conditions explicitly see B=(C+1)/(J+2), where J,C select the terminal row. B supervision is a diagnostic control, never relabeled natural learning.

Untrained baselines: exact B, KT row predictor (C+1/2)/(J+1), whole-word add-one unigram, constant 1/2. A learned classical baseline pools all training horizons into an add-one empirical label table indexed by (J,C); unseen cells use 1/2. Its counts and predictions are retained. B is the correct prior-Bayes comparator; it is not the true hidden source row p_U. All predictors have access only to W at evaluation, except that true p is used solely for scoring.

## Optimization, evaluation and decisions

Each of the 16 fixed fits has 1,500 Adam updates, batch 128, alternating the two horizons. Adam uses lr .003, beta1 .9, beta2 .999, epsilon 1e-8, no decay, no clipping, no schedule, no early selection. Every initialization, batch index, gradient, parameter vector and first/second moment is saved. There is no seed/hyperparameter search. Test predictions are computed only at the final fixed step.

Each replicate has 8,192 fresh heldout episodes at each of M=32,64,128, generated independently before fitting. M=128 is an explicitly out-of-training-length diagnostic. Duplicate words or (J,C) groups are expected under iid sampling and will be counted, not silently excluded. Test data is not used to change training or select checkpoints.

Primary quantity is heldout mean KL(B||q), averaged equally over M=32,64. Record each replicate separately and all 16 paired fits. The primary descriptive hypothesis is natural-label accessibility: uniform_y and learned_y each attain mean <=0.02 nats in at least 3 of 4 replicates, and median paired natural-minus-teacher excess <=0.01 nats separately within each architecture (four paired differences per median). These are screening thresholds, not power-justified significance cutoffs. Pooling benefit is separately descriptive: report learned-minus-uniform pairs without claiming superiority merely because one crosses a threshold.

Secondary quantities are actual-source forward KL(p_U||q), |q-p_U|, |q-B|, realized next-token CE, and conditional metrics for rare terminal rows J<=3. Record rare counts and all per-example values. A source-KL difference on a finite sample need not equal a B-KL difference, although their prior expectations agree. Do not replace either target with the other. No asymptotic rate or minimax claim comes from these three small horizons.

Report per-test-cell Monte Carlo SE and paired per-example SE conditional on each trained model, plus the four replicate means and paired differences. With only four independent replicas, there is no well-powered general training-effect inference. Ordinary t summaries, if supplied, are labeled exploratory and do not turn multiple cells into simultaneous significance. For planning, bounded absolute error at n=8192 has worst-case SE <=0.00553; rare cells can be much less precise. KL is bounded by log(1/eta), so its distribution-free bound is too loose for a 0.01-nat claim; use observed variance transparently and retain raw data. No post-hoc enlargement is permitted in this design.

## Resource and stopping plan

NumPy only, float64, one BLAS thread; existing environment checked: Python/NumPy present, Torch/JAX absent. Training comprises 32,768 distinct episodes across four replicas and 3,072,000 example presentations across sixteen fits. Raw training input generation uses 1,671,168 symbols including labels (4×4096×[(32+3)+(64+3)]). Evaluation additionally consumes 4×8192×[(32+3)+(64+3)+(128+3)]=7,634,944 symbols. Same data is reused fairly across four conditions; count preprocessing cost is charged separately. Runtime is measured, not promised. The per-fit full trajectory is about 38.5 MB before compression; all sixteen about 616 MB. Allow 2 GiB total local space for inputs, results and verified roundtrip copies. Stop before any new fit if free space is below 1 GiB, any correctness check fails, nonfinite values occur, or any required capture is unverified. Stop the run after 1,500 fixed updates regardless of outcome. Retain partial/failed records, do not silently retry or overwrite them.

## Durable capture, no additional human-approval gate

1. Freeze code, parameters, this design, tests, source map and execution plan in SOURCE_MANIFEST.json. Save the source ZIP to Space immediately. An independent checker must verify downloaded bytes, file hashes and the deterministic correctness tests and create a source-capture receipt. No experimental sampling or fitting before that check.
2. Generate one replicate's entire raw input bundle. Save latent sources, initial pairs, every uniform random variate, all words, future labels, count arrays, B values, initial weights, minibatch indices and RNG states. Zip and immediately save it to Space. Require independently verified roundtrip receipt before fitting.
3. Execute one fixed fit. Flush per-step metrics and full gradient/parameter/moment state to disk. Preserve console and exception tracebacks. Save all final per-example predictions/metrics, baseline table, source/input bindings, timing and environment. Seal its complete output. Immediately save it to Space and verify roundtrip before starting any further fit.
4. Any interruption preserves an INCOMPLETE status and all bytes already flushed. The current script does not resume or rerun a partial fit. A new versioned recovery action would have to describe exactly what is retained and missing.

The capture receipts are evidence from actual uploads and readbacks, not manufactured flags. They are a machine-checkable workflow barrier, not a security boundary. Review and capture do not require a new user confirmation. The lost 20:35 tiny-pilot originals remain lost; none of the new data or source files are a recovery of them. No GitHub writes are performed by this package.

## Scientific sources and scope

- Public v10 snapshot 109ac29309af3fe508dafef493fd891421dfb0fa: clean objective CTO001, learned-position smoke and interpretation amendment, calibration protocol, rare-weight confirmation protocol/report, source-matched and full-shared-source summaries. Exact links and content bindings are in SOURCES.json. These explain why repeated Q supervision would add little and why source identity matters.
- Edelman et al., *The Evolution of Statistical Induction Heads: In-Context Learning Markov Chains*, NeurIPS 2024: https://arxiv.org/abs/2402.11004 . Its primary abstract explicitly studies fresh random Markov sources, learned statistical induction heads and n-grams. It already establishes the broad empirical phenomenon we must not claim as new. Only the abstract was inspected here, not a full-paper reproduction.
- Lepage, Mary and Picard, *Markov Chain Estimation with In-Context Learning*, GRETSI 2025: https://arxiv.org/abs/2508.03934 . The primary abstract reports next-token learning across unseen transition matrices and size/data thresholds. Our smaller supplied-feature diagnostic is not a replication or extension of those results.
- Garg et al., *What Can Transformers Learn In-Context?*, NeurIPS 2022: https://arxiv.org/abs/2208.01066 . Controlled task distributions and strong task-specific algorithms are relevant methodology, not evidence for this Markov experiment.
- von Oswald et al., *Transformers Learn In-Context by Gradient Descent*, ICML 2023: https://proceedings.mlr.press/v202/von-oswald23a.html . It separates explicit constructions from experimentally learned mechanisms in regression; no inference that its dynamics apply here.

The saved T1/T2 research plan was also read in Space. It already warns that Markov-ICL, n-gram normalization and training mechanisms have substantial prior art. Its newer citations are not independently audited here and no novelty conclusion is drawn from them. The current Space synthesis/A5 correction archive was inspected with its recorded roundtrip hash; this experiment does not test its worst-case growing-alphabet results.
