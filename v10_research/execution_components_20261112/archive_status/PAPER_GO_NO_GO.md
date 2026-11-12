# Paper-level go/no-go decision: one main claim, not a collection of components

2026-11-12. Research decision memo. Current decision: NO-GO for claiming submission readiness; conditional GO for one focused source-average decision-limit program. This is not an originality certification. Primary HTML theorem statements were freshly read for the comparisons below, rather than inferred from titles.

## 1. Freeze the single proposed main claim

Under stationary fixed-c binary spin sources with unknown theta, a source-independent finite-prefix causal full positive-epsilon PreLN stack, public heterogeneous positions, common actual/reference domain, complete bounded scores and explicit Lipschitz gains admits a common endpoint-tag template g_N with

    sup_theta ||Q_N-g_N(T)||_2 <= Lout E_D/sqrt(N+1),
    E_(ell+1)=(a_ell+2b_ell)E_ell+2f_ell.

For a common +/-h prior this gives absolute risk >=max(0,h/2-delta_N) and squared probability risk >=max(0,h/2-delta_N)^2, whereas unrestricted statistical estimation has root-N risk. The theorem concerns accessible bounded-gain decisions, not loss of exact-real information: the explicit output encoding preserves word-law TV/KL while remaining O(1/N) from1/2. Neither half alone is enough to claim a strong new paper.

Freeze which input/readout model is used. Do not swap public sentinel, raw last row and free endpoint pair mid-proof. Do not replace whole effective-score/gain bounds with learned-parameter norms without a verified conversion. No global key-energy bound is needed for this proposed headline; the newer key-energy bridges are ancillary, not stronger substitutes.

## 2. Closest primary statements, compared on the same axes

### Duerinckx–Geshkovski–Rossi, Theorem1.1(ii)
Source: https://arxiv.org/html/2605.09213v1 ; equations1.11–1.12 and discussion immediately following.

Their quantitative claim is RMS empirical-measure test-function error <=constant N^(-min(delta,1/2)) exp(Ct) ||phi||, for independent initial circle-valued tokens whose characteristic-function profiles approach a continuous position profile at rate N^-delta. The dynamics are continuous-time causal particles with the paper's simplified circle interaction/normalization. Smooth test-function norms are charged. Independence is INITIAL only: no evolved-layer mixing is assumed. At delta>=1/2 the exponent in N is already exactly the root-N scale we use, and exponential time growth corresponds qualitatively to our exponential gain/depth constant. Therefore neither root-N nor absence of layerwise mixing is new by itself.

Non-identical contracts: an empirical-measure smooth-test bound is not automatically a pointwise terminal-state error, t is not discrete depth D, and independent initial samples are not our correlated source. The paper itself says mean-field convergence alone does not control retrieval accuracy and develops next-order correlations in Theorem1.2. We must not portray this prior as merely a qualitative limit or as ignoring retrieval.

Required decisive result: prove a finite discrete full-PreLN terminal decision bound under dependent source input without inserting an independence, discretization or endpoint-extraction error into a hidden constant. Then show the decision-risk separation uses information not covered by their stated smooth empirical observable. Different vocabulary labels or a different normalization notation do not constitute this proof.

### Xu–Fang, Assumptions3.5/5.1 and Theorem5.2
Source: https://arxiv.org/html/2605.10466v1 ; equations6–7.

Their bound is E||h_t^L-F^L(x_t)||^2 <= C_L T_L/t, T_L=sum_{ell<L} tau_alpha^(ell) tr(Sigma_ell). Assumption3.5 requires strictly stationary ergodic elliptical sub-Gaussian marginals, positive-definite covariance, and tau_alpha=1+2sum sqrt(alpha(k))<infinity. Assumption5.1 imposes that contract separately on EVERY evolved hidden process. A query quadratic-form constraint is additional. Residual maps are Lipschitz and explicitly cover pre-norm updates. It would be wrong to say this prior has no multilayer/residual treatment. Their RMS rate is already root-N; our advantage cannot be advertised as a faster N exponent.

Our prospective separation: derive all approximation errors from the initial finite-state mixing law and actual finite-prefix network, without stationary/elliptical evolved-state assumptions or unknown T_L. Position-specific deterministic embeddings and finite-prefix transients are allowed. Crucially their F^L depends on population covariances, so it need not be common across source parameters. The new risk step requires a genuinely common template, not merely a pointwise context-free approximation under each parameter.

Required decisive result: an explicit audited architecture/source witness admitted by our assumptions but not their positive-definite elliptical/evolved-stationarity regime, plus the theorem yielding source-uniform common-template risk separation for that witness. Explain honestly that our bounded-score/common-domain contract also restricts the class; neither theorem is a universal superset of the other.

### Xiang, Theorem1 and Corollary1
Source: https://arxiv.org/html/2610.24133v1 ; Section4.3, equation3.

Their actual PreLN prompt-offset bound is delta_L(t)<=C_L P(L+ln t)^(L-1)/t, C_L<=K3 sum_{m<L}(K1+2K2)^m. It compares different prompts of length at most P followed by the SAME continuation, under normalization nondegeneracy and bounded logits. It is pathwise, not a source-independence theorem. Its final output TV corollary is also already present. The paper explicitly warns that trained-model score spreads may make the constants noninformative in accessible windows.

Our source histories at +h and -h generally differ throughout; no same-continuation coupling is given. Replacing P by N removes the smallness that supports their result. We cannot claim an improved exponent by comparing 1/sqrt(N) to1/t: they measure different experiments. Conversely, if an existing coupling plus their bound already gives our full source-risk conclusion with the same constants, our proposed novelty collapses.

Required decisive result: explicitly attempt that reduction on the same stationary source and free-endpoint model, account for mismatch positions, and state exactly where it cannot supply the common-template conclusion. Mere citation of different tasks is insufficient.

### Castin et al., Theorem6
Source: https://arxiv.org/html/2501.18322v2 . This is well-posedness/stability for a masked normalized-softmax PDE with integrable time-varying Q,K,V, compact support, common position marginal and a positive position-zero atom. Its conditional Wasserstein framework preserves position when transporting states. An empirical single token at each position and a two-point position-conditional reference do not automatically approach each other in that metric; a single sentinel has mass1/N, not a uniform positive atom. No pointwise-terminal root-N error follows by simply naming the stability theorem. Do not claim a sharper exponent against a theorem that is not asserting that sample-rate contract.

## 3. Necessary gates, with pass/fail outputs

Gate A, correctness and uniformity: one immutable statement must expose all source, position, state, score, LN, readout, depth and precision assumptions; independent reviewers verify common-template construction and its same-trajectory risk comparison. Existing audits support this gate, not novelty.

Gate B, substantive non-subsumption: complete the three reduction attempts above. Deliver explicit admissible witnesses and a quantified missing term/assumption, not a table of architectural names. If the result follows from one prior plus standard covariance substitution and Lipschitz continuity with no meaningful strengthening, NO-GO as the main new theorem.

Gate C, paper-strength result: obtain at least one defensible major strengthening beyond bookkeeping: a broader matched-marginal dependent-source class with a uniform terminal decision theorem; or a sharp decision-access/precision tradeoff under ONE declared observation model; or a quantitatively improved growing-depth/resource regime. These are alternative targets, not results already proved. A new factor2, a small compiler, or restated standard minimax rate does not pass this gate.

Gate D, evidence: choose regimes where the claimed bound is actually below the target risk gap, or label the numerical checks strictly as theorem consistency. Report true effective scores/gains and sensitivity to LN epsilon rather than nominal weight norms. For claims about trained predictors, compare unseen-source performance against the count/innovation oracle and include a bounded-gain intervention; no current component test supplies this evidence. Experiments cannot repair a missing theorem and are optional if a strong purely theoretical claim survives Gates B–C.

Gate E, scope consistency: retain the exact-information counterexample so that no title/abstract claims TV-information destruction. Treat the statistical benchmark as known and the public-source alignment as support. Preserve all counterexample assumptions and avoid converting worst-word retrieval failures into average-risk necessity.

Decision rule: draft a focused technical paper only if A and B pass and at least one concrete Gate C result survives adversarial review; then judge whether D is needed for its stated claims. Otherwise consolidate a technical report and stop adding peripheral components. This memo does not certify readiness or predict acceptance.
