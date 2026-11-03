# CTO001 independent review

Verdict: PASS, conditional on the explicitly accepted statistical interfaces, for candidate SHA256 1405c661827773bba64c8d8ae91f8eb8a9b2bf17ffc6a66e3be69525f1674bb2. No author-file edits or external writes. Local independent LLM review, not formal verification, external peer review or novelty certification.

## Method and result

Derived the posterior, uniqueness transfer, augmented ratio, and prior-tail/entropy arguments before reading the author candidate; see INDEPENDENT_DERIVATION.md. Then read the complete actual CANDIDATE.md. No substantive correction required.

1. The independent uniform initial pair removes any parameter-dependent initial likelihood. Adaptive row selection does not change the finite-word product likelihood. The full word fixes its queried terminal row before posterior averaging. Exact integrated mass is strictly positive for every word. Proper-loss uniqueness is a statement about the prediction kernel, not uniqueness of model parameters. A finite union of null seed events proves equality on every corrupted word; independent seeds and attacks are explicitly required.
2. Clean accuracy is uniform over all sources and all initial laws, unlike training average loss. Complementing the designated row output correctly transfers the accepted empirical lemma to symbol-1 probability. The loose clean constant 560 is valid; the claimed reciprocal layer-cake bound correctly uses a ceiling threshold and no endpoint-conditioned independence.
3. The r=2 finite-window lower grants more observations than B uses. Its stationary witnesses are inside the exact critical supplied-certificate test class. It bounds a supremum over budgets, not each budget separately. Arbitrary-start factors dominate stationary factors. The accepted original known-budget proposition is g/96 <= R_stat <= R_all <=191488g for full histories and for counts plus protected pair, matching this interpretation.
4. For edited add-one estimates both denominators remain positive. The pathwise augmented ratio uses a'/b'<=1 and the original denominator b, yielding 12k/(J+2) even when the edited departure count is zero. Its occupation/layer-cake upper has correct 192 constant and k=0 separation.
5. The full-history gate is exactly the original order-two first-half gate, with correct designated-successor orientation, equality acceptance, and denominator-zero handling. The general-beta source interface and its all-state/arbitrary-start scope match. Smoothing adds at most s and keeps finite logloss. This is an unrestricted real-valued map, not an effective finite-bit realization claim.
6. The uniform prior is not uniformly in the critical class. Its weak-row tail costs at most 8s. On the complement, P²>=m² pointwise implies P²>=m² Pi, so the general-beta clean bound integrates to 131080s. Smoothing gives D=131081. No stationary initialization is needed.
7. The conditional KL decomposition compares true source p, posterior b and smoothed prediction q correctly. The entropy coupling proof works on the full binary domain; Jensen is used for concavity, then monotonicity only when Ds<=1/2. The all-horizon log(1/s) bound covers remaining M. Thus same-prior excess vanishes at O(log M/sqrt M).
8. Scope exclusions are appropriate: no SGD guarantee, finite-class representation assumption, universal robustness of near-minimizers, necessity of corrupted training, or architecture/priority claim. Root supplied synthesis route is not an independent new learning principle.

## Independent diagnostics

check.py exhaustively integrates 4,092 binary words for M=0,...,9 using rational factorial masses. Normalization, positive support, next-label posterior ratios and one-step marginalization all hold exactly. It checks 105,625 rational count-ratio cases exactly, 10,404 entropy grid cases at four smoothing values, and 16 layer-cake endpoint cases. The final entropy check uses 70-digit mpmath, tolerance 1e-60 and minimum slack -4.53e-72. An initial machine-float grid encountered endpoint cancellation, so the final check uses higher precision rather than a relaxed machine tolerance. The mathematical entropy proof was reviewed separately. These diagnostics do not prove imported stochastic lemmas.

## Source read scope

Read accepted O2T001 in full and its ROOT_ACCEPTANCE. Read original manuscript definitions, known-budget proposition, finite-window theorem and scope; read actual positive occupation/empirical lemmas with proofs, and actual general-beta first-half proposition with proof. Verified the original acceptance receipt binds the main and positive source bytes. This review imports rather than independently re-proves the finite-window lower and certificate-dependent imbalance machinery. Exact source and final artifacts are pinned in bindings.json.

## Final wording audit

Read the complete final real-s/comparator-scope candidate (0b299a4d), then the exact final SCOPE_WORDING.diff yielding 1405c661. Root-requested removal of “discontinuity” is valid: for fixed M, full finite support ensures vanishing excess controls each word, so the asymptotic separation is along growing horizons. The replacement accurately states this. The header now excludes optimization dynamics and architecture learnability rather than obscuring its global-minimizer characterization. No mathematical formulas changed. Final PASS applies to 1405c661, not an unbounded future edit.
