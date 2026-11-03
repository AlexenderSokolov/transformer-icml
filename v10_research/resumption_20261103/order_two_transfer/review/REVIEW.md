# O2T001 independent source-bound review

2026-11-03. Verdict: **PASS for the stated transfer scope, no blocking correction required.** This is an independent LLM analytic review of the bound candidate, not root acceptance, formal verification, external peer review, or a novelty certificate. Candidate and TRANSFER bytes were not edited.

## Material actually read

Complete O2T001 candidate; complete original positional finite manuscript main.tex; complete original proofs_positive.tex (including occupation, stacks, weighted hitting, return transform, reflected unsupported-start argument, gate reduction, half reciprocal bound and oracle); complete proofs_finite_horizon.tex; complete BCC001 candidate; complete current BSC001 likelihood note; complete WMC001 candidate; BCC/BSC/WMC root receipts. The original positional receipt's source bindings were checked by script. I did not independently rederive/review the entire original negative manuscript or underlying FOT001 excursion combinatorics in this turn: they are explicitly imported accepted dependencies, not newly certified here. Their source files/receipt bindings are preserved. This distinction is consistent with candidate §2's own import boundary.

## Substantive checks

1. **Actual model, not a renamed first-order result.** M counts pair departures 0,...,M−1, and θ_ab governs the next symbol after each pair. The original first pair is arbitrary; no homogeneous initial edge is required. O2T uses the original four-row half-window gate, not pooled first-order departures or a discarded initial coordinate. Protected terminal pair fixes the selected row for every edit outcome.

2. **Upper theorem and constants.** The genuine `prop:finite-upper` states all-start risk ≤min{1,65536/√M+65536/(M√β)+2^23 k/M}. Substitution β=1/M gives 2^17 and 2^23, hence C2=8519680. I independently checked gate perturbation coefficients, the half reciprocal calculation 4·2·16368=130944, and 48·130944+16(6156+3078)=6433056<2^23. The same map works for every k. No ratio is evaluated at a zero denominator.

3. **Where the certificate is used.** Occupation, clean stack deviation and half reciprocal bounds are generic all-start facts; the weighted imbalance is the certificate-dependent step. Full support uses Π=(y,x,x,w), ya=xe,wτ=xb and the specified certificate entries to bound weighted hitting scales. Positive all-state minorization excludes multiple absorbing supported diagonals and nonfull off-diagonal support. For singleton 00, the reflected three-state chain dominates each original active path, preserving terminal row and all counts; this is NOT conditioning on survival. Original B=10 is paid by its first absorption point mass. Degenerate reflected parameters use finite-path continuity only. Symbol exchange treats singleton 11. This closes the unsupported-initial-state issue rather than assuming it away.

4. **Baseline and lower inclusion.** At r=2 the finite theorem upper needs only counts and final pair while the lower grants both pairs. Flow conservation reconstructs initial pair from triple counts and final pair regardless of probabilistic source, so optional initial pair is harmless. For first-order embedding, P²((a,b),(s,z))=T(b,s)T(s,z), Π(s,z)=π(s)T(s,z); the BSC witness ratios in O2T are correct, including null ratios 3(1−β),3β/2,3β/2,3(1−β/2)/2. The embedded stationary experiments and legal kernels are a subclass, so their same-map lower transfers to the enlarged source class. The imported BSC finite conclusion has already paid N=M+1 conversion; it is not silently applied before that conversion. IID witnesses also have exact P² rows Π and constant next-symbol target.

5. **Four channel classes.** The product common submeasure bound holds conditionally on every independent shared seed and arbitrary encoder mixture; it transports nonnegative risk and gives a max with the full-history floor. Equal rows can be simulated by the baseline. Disjoint supports transmit one exact gate. A one-sided exclusive event suffices for the balanced two-use erasure simulation: the failure flag alone is independent of the pre-channel experiment, and only its coarsened output is asserted BEC. Finiteness and common support give the all-codeword likelihood ratio κ^R needed by BSC001's signed-loss step after nonnegative transport. Repetition's two conditional testing errors are each ≤h^R. All source-specific upper inputs have been replaced by O2 rather than assumed inherited from FOU.

6. **Whole payload is exactly sufficient for this target.** Both terminal symbols are needed at the encoder to select row u. Once its J,C are selected, only d=1−Z_M is needed to interpret the designated-successor probability as a symbol probability. On rejection qhat=0 means complement d, not universal zero. Thus `(J,C,d,G)` uses exactly the claimed sufficient fixed width and reproduces the original prediction. This assertion would not by itself encode a next-pair distribution, whose support uses terminal second symbol; candidate correctly excludes that altered target. B is sufficient, not proven minimal. The coding result depends only on B and maximal conditional decoding error, so no source-order-specific assumption remains. The clean IID cardinality lower is valid because no baseline/query information is free; independent decoder counterfactual outputs are independent of p even though encoder selection is sample dependent.

7. **Costs and scope.** One scan with eight triple/four half-row counters gives O(log M) auxiliary bits but not total resident input storage. Whole-message counts are paid; supplemental counts are free by model declaration. Large explicit codebook and preprocessing are charged; exact computation for rational W is separated from statistical existence for arbitrary real W. No result is claimed for unrestricted no-mixing order-two sources, all β, adaptive length, unknown or M-dependent W, or learned/neural implementation. Efficient-code transfer is conditional on separately accepted maximal-error interface, not an acceptance by association.

## Reproducible finite diagnostics

`checks.py` completed with PASS and wrote `checks.json` and `bindings.json`:

- 33,260 binary-word payload cases (all lengths 3–14, plus 500 deterministic-seed words at M=64,65,127,512,1024).
- 133,040 per-state flow/initial-pair reconstruction identities.
- Included 1,396 zero-denominator cases and 5,356 rejected gates; exact arithmetic serialization matches direct symbol distributions.
- 19,683 length-six active paths for all 27 reflected-parameter triples in {0,1/3,1}³: original active-path probability ≤ reflected probability, including boundaries.
- 192 exact rational all-state minorization entries for embedded null/IID examples.
- Gate-threshold equality and displayed constants checked.
- Seven actual imported theorem/source files match the acceptance receipt hashes; candidate and TRANSFER are byte-identical.

Short-word checks verify algebra/combinatorics outside the theorem's M≥64 range, not a statistical risk theorem there. The 500 longer examples do not estimate risk. No finite check substitutes for the asymptotic analytic lower or imported mixture lemma. Source bindings include the specific candidate and all read primary dependencies/receipts; root can rerun the script without network access.
