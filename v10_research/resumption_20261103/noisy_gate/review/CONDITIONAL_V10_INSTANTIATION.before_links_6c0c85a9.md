# Conditional v10 instantiation: fixed supplemental-channel noise

2026-11-03. **Conditional on the recovered baseline/exact-gate results and their later acceptance/dependency checks.** This note does not independently validate those historical proofs or upgrade their status. Do not modify restored historical document headers based on this note.

## Inputs reported from recovered science

Model: M>=64, raw path X_0,...,X_(M-1), exact eight triple counts and a protected final pair in the base observation; initial pair recoverable by flow. First-order TABLE family with arbitrary initial pair; corruption budgets k=0,...,M; normalization

g_k=max{M^(-1/2), k/M},   g_min=M^(-1/2).

Let ell_M=1+ln((M+2)/2). The reported matched baseline bounds are

2^(-33) ell_M <= Gamma_0(M) <= 2^17 ell_M.

The reported exact supplemental one-bit gate estimator has risk bounded by

1024 M^(-1/2)+2^20 k/M,

and therefore Gamma_exact(M)<=C_exact:=1024+2^20. The additive 1024 term must not be silently dropped.

Recovered sources supplied by root (dependency review pending):
- `../recovered_science/first_order_positional_probe/UPPER_CANDIDATE.md`
- `../recovered_science/first_order_positional_probe/triple_access/FOT001_candidate.md`
- `../recovered_science/first_order_positional_probe/FOT002_matched_original_experiment.md`
- `../recovered_science/first_order_positional_probe/BOUNDARY_RECONSTRUCTION_NOTE.md`

The FOT003/log-upper and later acceptance receipts must be reconciled by root; the list is not an independent provenance audit. In particular WPC and other substantive dependencies are not discharged by the channel reduction.

## 1. One noisy supplemental bit

Apply an independent BSC_eta to the supplemental gate *after corruption/encoding*. The base counts and protected pair remain exact. Noise is fresh and unavailable to corruption/encoding. Assume the concrete loss is bounded in [0,1] for the additive upper bound.

Then, for 0<eta<=1/2,

2^(-32) eta ell_M <= Gamma_eta(M)
  <= min{2^17 ell_M, C_exact+eta sqrt(M)}.

For every fixed eta>0 this yields Gamma_eta(M)=Theta_eta(log M): a fixed nonzero crossover probability destroys the exact gate's constant competitive-ratio advantage asymptotically. This conclusion is conditional only on the baseline logarithmic bounds and common-channel model; the exact-gate result supplies the contrast, not the logarithmic lower bound.

At eta=0, Gamma_eta=Gamma_exact<=C_exact. At eta=1/2, Gamma_eta=Gamma_0. If eta depends on M, the displayed bounds remain valid pointwise, but they are not a sharp characterization of all vanishing-noise regimes.

## 2. R repetitions of the exact gate

Let lambda_R be the repeated-BSC overlap from NOISY_MESSAGE_REDUCTION.md and e_R=lambda_R/2, with fair majority tie-breaking. For 0<eta<1/2,

2^(-33) lambda_R ell_M <= Gamma_R(M)
  <= min{2^17 ell_M, C_exact+e_R sqrt(M)}.

For every fixed positive integer R and fixed eta>0, Gamma_R(M)=Theta_eta,R(log M). R=0 also gives the baseline exactly. For fixed 0<eta<1/2, rho=2sqrt(eta(1-eta))<1 and e_R<=rho^R/2. Taking

R=ceil((log M)/(2[-log rho]))

gives Gamma_R(M)<=C_exact+1/2. Thus O_eta(log M) independent repetitions suffice. This is a construction, not a sharp lower bound on necessary repetitions.

The repeated-code common-overlap lower bound requires R=Omega_eta(log log M) for any target competitive ratio independent of M. There remains a gap between this necessary bound and the O(log M) sufficient count; optimal joint use of the base observation could potentially improve upon decode-then-estimate.

## 3. Any R-bit encoded supplemental message

For any clean R-bit supplemental message (including randomized, full-path-dependent, or Z-dependent encoding), send each coordinate through an independent BSC_eta after encoding. For each fixed encoder/joint estimator pair, a common independent-uniform output component of weight (2eta)^R exists. Consequently the optimal competitive ratio over all such procedures obeys

Gamma_any-code,R(M) >= 2^(-33)(2eta)^R ell_M,

and is at most 2^17 ell_M by ignoring the message. Hence fixed eta>0 and fixed R cannot yield constant adaptation, even with a more expressive clean message than the historical exact bit. For 0<eta<1/2, any target constant C demands

R >= [log(2^(-33) ell_M/C)]/log(1/(2eta)),

when its numerator is positive. This establishes an Omega_eta(log log M) necessary noisy message length for arbitrary encoding. It does not identify the optimal code or eliminate the necessity/sufficiency gap.

At eta=1/2 all encoded supplemental messages are independent uniform, regardless of R, so no improvement is possible under this model. None of these claims extend automatically to correlated noise, adversarial channel errors, noise-aware attacks, or a model in which the base triple counts/final pair are themselves noisy.

## Research status

The abstract statistical-experiment reduction is proved locally in the companion note and is awaiting independent review. The concrete v10 conclusions here are conditional on recovery and verification of the precise historical lower/upper hypotheses, estimator randomization convention, matched attack families, and bounded concrete loss. No material has been published or pushed.
