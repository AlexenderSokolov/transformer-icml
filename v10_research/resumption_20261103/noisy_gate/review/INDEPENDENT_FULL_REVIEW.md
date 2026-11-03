# Independent mathematical review: noisy-message reduction

Status: PASS for the abstract mathematics in the hash-bound source below. Independent derivation and source-specific review complete. Concrete v10 instantiation remains conditional and unaudited here. No repository publication performed.

## Scope and conclusion

The abstract common-minorization theorem, BSC specialization, repetition overlap, arbitrary fixed-length BSC-message lower bound, and stated necessary/sufficient length gap are mathematically correct under the conditions made explicit below. This review does **not** certify any Markov construction, claimed baseline logarithmic lower bound, exact-bit algorithm, or benchmark scaling: those are conditional inputs requiring separate load-bearing proof audits. Numerical checks only corroborate finite channel identities.

## 1. Precise experiment and quantifiers

Let i=(k,theta,K) range over the same fixed collection of admissible instances for all comparisons; g_k>0. One baseline rule A is chosen independently of i. Let T collect every risk-relevant latent variable, including the target and any corruption randomness, and let Z be the baseline observation. An encoder produces H (possibly randomized and even dependent on theta). Conditional on the full pre-channel tuple (T,Z,H), the new output has law W(dy|H). No extra decoder side information may silently be added: shared seeds available to the decoder must already belong to Z or be baseline-available independent randomization. The loss L(T,a) is measurable and lies in [0,1]. The rule class must allow independent randomization and ignoring Y.

Assume one probability law nu and one number 0<=lambda<=1, independent of **all** i and channel inputs, satisfy W(B|h)>=lambda nu(B) for every measurable B and h. Pointwise pmf/density inequalities imply this measure inequality in the usual discrete/dominated settings. Define

Gamma_0 = inf_A sup_i E_i L(T,A(Z))/g_k,
Gamma_W = inf_D sup_i E_i L(T,D(Z,Y))/g_k.

The conditional channel property is stronger than merely asserting an unconditional BSC marginal. A corruption kernel can depend on H or pre-channel information if allowed by the underlying model, but cannot use the channel noise to change Z or risk-relevant T while retaining this hypothesis in general. The two minimaxes must retain identical instance/adversary classes; changing the adversary's legal knowledge changes the question.

## 2. Independent proof and minimax ordering

Fix any augmented rule D. Define the **single universal baseline rule** A_D(z) by drawing Y_0~nu independently and running D(z,Y_0), including D's ordinary private coins. It is the same function for every k,theta,K. Nonnegativity of loss and minorization give, instance by instance,

R_i(D) >= lambda R_i(A_D).

Consequently sup_i R_i(D)/g_k >= lambda sup_i R_i(A_D)/g_k >= lambda Gamma_0. Taking infimum over D proves Gamma_W >= lambda Gamma_0. Conversely ignoring Y proves Gamma_W<=Gamma_0. No exchange of infimum and supremum, instance-specific simulator, or minimax interchange theorem is used. If lambda=0, state the lower bound simply as Gamma_W>=0 rather than multiplying 0 by an infinite Gamma_0. For positive lambda, the extended-real statement remains valid. Boundedness of loss is unnecessary for this lower bound; nonnegativity is essential.

The encoder's dependence on theta does not harm this proof because nu is input-independent. It may, however, render the purported exact-bit encoder operationally illegal in a separate statistical application; that is an application-level issue, not a flaw in the reduction.

## 3. BSC bit and robust upper bound

For 0<=eta<=1/2, the two BSC output pmfs each dominate eta at both outputs. With nu uniform, lambda=2eta. For eta>1/2, output relabeling reduces to min(eta,1-eta); formulas using eta itself must not be extended unchanged.

Suppose an admissible exact-bit procedure has normalized worst-case risk at most C (or an approximating sequence has limit at most C). Couple the noisy-bit and exact-bit experiments using identical pre-channel tuple and decoder coins. They agree when the bit is not flipped. Since losses are in [0,1], R_i(noisy)<=R_i(exact)+eta. Thus when g_min=inf_k g_k>0,

Gamma_eta <= min{Gamma_0, C+eta/g_min}.

The infimum need not be attained; epsilon-approximating rules suffice. If g_min=0 this displayed bound is vacuous and cannot justify a finite uniform estimate. A common C and a uniform admissible exact-bit procedure over all k,theta,K are required, not an instance-wise existence statement.

If Gamma_0(M)=Theta(log M) and eta is fixed strictly positive (eta<=1/2), then 2eta Gamma_0<=Gamma_eta<=Gamma_0 implies Gamma_eta=Theta_eta(log M). A bounded exact-bit advantage disappears in this multiplicative minimax sense, conditional on the baseline and exact-bit premises. This does not assert impossibility of any absolute-risk improvement or exact equality of noisy and baseline risks.

## 4. Repetition channel: exact overlap and endpoints

For a single bit repeated R times through independent BSC_eta, let W_0,W_1 be the joint output distributions. The maximal common subprobability mass is

lambda_R = sum_y min{W_0(y),W_1(y)}
         = 2 Pr[Bin(R,eta)>R/2] + Pr[Bin(R,eta)=R/2],

for 0<=eta<=1/2, with the tie term zero for odd R. The minorizing law is min(W_0,W_1)/lambda_R when lambda_R>0, and is independent of i. Therefore Gamma_R>=lambda_R Gamma_0. This is an intrinsic channel overlap, not an assumption that the downstream estimator discards Z. The decoder may use Z and all R noisy outputs jointly. Majority with randomized ties achieves isolated-bit minimax decoding error delta_R=lambda_R/2; it need not be the optimal downstream decision rule for a general loss and informative Z.

Endpoints: R=0 means one empty output, lambda_0=1, and isolated-bit minimax error 1/2. R=1 gives lambda_1=2eta. At eta=0, lambda_R=0 for R>=1 and exact recovery is possible. At eta=1/2, lambda_R=1 for every R, so repetition never helps, and a vanishing-error claim is false.

For fixed 0<eta<1/2 and R->infinity,

lambda_R = Theta_eta(R^(-1/2) a^R),  a=2 sqrt(eta(1-eta))<1.

Reason: the first term of each upper binomial tail is of order R^(-1/2)a^R by the central binomial coefficient estimate; successive terms have ratio at most eta/(1-eta)<1, giving a geometric upper bound. Even-R ties have the same order; odd/even constants differ but remain positive and finite. This asymptotic is neither uniform as eta approaches 0 or 1/2 nor meaningful at R=0.

## 5. Arbitrary R-bit messages, necessary length, and sufficiency gap

For every x,y in {0,1}^R, W(y|x)>=eta^R. Hence the entire R-bit channel has the common minorizer lambda=(2eta)^R with uniform nu on {0,1}^R. This covers arbitrary (even randomized, theta-dependent) fixed-length encoders because mixtures preserve the inequality. It is sharp as a universal common mass across the full input alphabet: every y has an antipodal x attaining eta^R. Adaptive/variable-length communication or noise-dependent encoders are different models and are not covered merely by counting transmitted bits.

For fixed 0<eta<1/2, Gamma_0(M)>=c log M and target Gamma_R<=B independent of M imply

R >= [log log M + log(c/B)] / log(1/(2eta)),

whenever the numerator is positive. Thus R=Omega_eta(log log M) is necessary. At eta=1/2, no finite R can beat the baseline; at eta=0, there is no such necessary-length lower bound. For a repetition-only scheme one may use its stronger lambda_R, but it still does not establish an O(log log M) sufficient construction.

If an admissible exact bit achieves C uniformly, majority decoding gives Gamma_R<=C+delta_R/g_min. The elementary bound lambda_R<=sum_y sqrt(W_0(y)W_1(y))=a^R gives delta_R<=a^R/2. For fixed 0<eta<1/2 and g_min(M) of order M^(-1/2), taking R=O_eta(log M) makes delta_R/g_min bounded (or smaller as desired), hence yields constant normalized risk. This sufficiency presupposes the exact-bit rule and admissibility of transmitting the same bit R times. It does not match the general Omega(log log M) necessity. No sharp coding threshold has been proved.

## 6. Failure modes and explicit counterexample

Without fresh conditional channel noise the lower bound can fail completely. Take theta in {0,1}, independent N~Bernoulli(eta), H=theta, Z=N, and Y=theta xor N. Under 0-1 estimation loss and g=1, Z alone gives minimax risk 1/2, while (Z,Y) recovers theta exactly, so Gamma_W=0 despite lambda=2eta>0. Marginally Y|theta is BSC_eta, but conditionally on (theta,Z) it is deterministic, violating the needed channel property. This models a noise-aware mechanism exposing its noise through the baseline observation; it is not a counterexample under the theorem's hypothesis.

Also excluded: adversarial bit flips, public-count corruption, different kernel classes between baseline/noisy experiments, privately correlated decoder/encoder randomness unavailable in the baseline, parameter-dependent nu, and clairvoyant per-instance selection of A_D. None should be silently identified with independent channel noise.

## 7. Exact finite corroboration

`exact_channel_check.py` checks eta in {0,1/10,1/4,1/3,1/2}, R=0,...,12 using exact rational arithmetic. It checks repetition overlap, the binomial tail/tie formula, twice majority error, and domination of the all-input minorizer. For R<=6 it additionally enumerates every pair of input/output words to verify the maximal all-input common mass. All 65 parameter pairs pass. No floating-point approximations, empirical sampling, or numerical minimax solver is used.

Script SHA-256: `145e3a3a4787807100fe092841fb3daabb9249ae215a2216ea6ca647cc28fc0e`.
Results SHA-256: `4a5f0bb159733947039bb3ec3c5c8f50595cd4836ecd3ebff40c9102dd84ea4b`.

## 8. Source-bound assessment

Reviewed source: `../NOISY_MESSAGE_REDUCTION.md`.

Source SHA-256: `b94a940fb5a83c93057c19ac8b2b661c0a42105c410f679c6d4bc27ec34c4db7`.

The independent derivation above was written before reading the source. The source was then read in full and checked against it. Source Sections 1–2 correctly impose a single estimator, identical instance classes, fresh conditional channel law, and randomization closure, and correctly preserve inf/sup ordering. Section 3 additionally proves the valid information-ordering inequality Gamma_exact<=Gamma_eta. Sections 4–5 correctly derive the exact overlap, parity-sensitive tail representation, two-sided fixed-interior asymptotics, coarse length necessity, sharper implicit necessity and its log-log-log rearrangement, and the conditional generic sufficiency. Sections 6–7 explicitly cover the noise/attack ordering and all requested endpoints. Section 8 validly extends the universal minorizer to arbitrary randomized and Z-dependent fixed-length encoders, and explicitly excludes encoder-dependent instance classes without separate argument. Its fair-noise counterexample is valid.

No substantive mathematical defect or mandatory correction was found. The abbreviated Main Findings should be read with the explicit eta range and extra normalizer/exact-rule assumptions in Sections 3 and 5, not as unconditional v10 claims. The source's label “awaiting separate review” describes the pre-review state; this separate hash-bound review now supplies that review without modifying the source.

**Release boundary:** PASS is limited to this exact source's abstract channel reduction. Any later source edit invalidates this binding until checked. A statement that v10 has Gamma_0=Theta(log M), Gamma_exact=O(1), or g_min comparable to M^(-1/2) still requires independent proof restoration and audit. This review neither imports a public-count damage model nor licenses adversarial-noise claims.
