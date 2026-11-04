# Exact-file review of the sharp stationary HTML package

Date: 4 November 2026 UTC.

**Verdict: PASS as an analytical output composition and source-preserving HTML package.** No mathematical substitution error, missing declared proof section, or source-conversion defect was found. No source changes are required. This verdict does not assert a browser-render pass, formal verification, external peer review, current literature priority, or an executed numerical implementation.

## Exact files reviewed

- `stationary_addone_sharp_log.v1.html`, 205793 bytes, SHA-256 `b2d96c03f14c35c83c084ca94c714257d295f4955e184f98bf0d73ea602b6e32`.
- `stationary_sharp_output_corollaries.v1.md`, 12606 bytes, SHA-256 `cd2379246d2ca2a3ce56ac9e32ea41c8c83b26327424f303d16d015668d587ef`.
- Statistical input: `stationary_addone_sharp_log.candidate.v1.md`, SHA-256 `90e949efc52cd8f3d57108ca334f9083a9858950183dd8e6f60d6664d92c6195`.
- Its two exact-file reviews have SHA-256 `02ef46cd71c27d218f72942e80484f36fc23253e16779ae49cb989d670335d23` and `05935d27057e2038dbb2033b97da78e845a7f13c966235bcbedd8cfc78d63df6`.

The new proof, both mathematical reviews, and the complete new composition were read. The previous stationary corollaries and their reviews, relevant inherited exact-real and precision statements, and the signed-range adversarial review were checked. HJW's first-order model, Theorem 1, Remark 1, and higher-order theorem were checked in the local published-text extraction; the associated published PDF hash is `375c730cb4c9f6dd2eaa4439e59800764faeddbebee73f220e22d6d2cf3116a3`.

## 1. Statistical input and unchanged output transfers

The new W(A,n) is copied exactly from the reviewed statistical source, including the cap, constant 14000, denominator n+1, and logarithm of (n+1)/A^3. Its stationarity requirement, actual terminal pair, n observed departures, and tolerance of zero probabilities, reducibility, and periodicity are retained. The complete new proof is embedded, including the separate likelihood integrations yielding the stationary-mass minimum, the probability-weighted positive-log estimate, and the three count ranges. There is no omitted proof replaced by a reference to either mathematical review.

The new composition supplies a valid pointwise KL-transfer proof. When a true coordinate is zero, omitting it in Jensen's inequality is legitimate; adding its nonnegative B_b^2/Q_b term only enlarges the upper bound. The zero-sum difference estimate gives squared Euclidean error at most twice the squared TV distance.

The unchanged exact-real floor 1/(AL) and TV constant 44A+1 yield precisely 2W+2A(44A+1)^2/L. The stronger floor gives the separate cap log[1+(A-1)L]. The specialized evaluator's floor 1/(4AL) and TV constant 46A+2 yield precisely 2W+8A(46A+2)^2/L and the separate cap log(4AL). No independence of the terminal state is required because both transfers hold for each observed word. TV alone is not used to infer support.

At n=0 the uniform add-one loss is at most log A. The two boundary formulas correctly use L=A+2 and the inherited all-word guarantees without invoking the n>=1 statistical theorem or introducing a transition.

## 2. Alphabet dependence and HJW comparison

Both output corrections are O(A^3/L) with absolute constants, and L>=n+1. They are absorbed by the new statistical order, since its bracket is at least one. If h=A^3/(n+1) tends to zero, h[1+log(1/h)] also tends to zero. Thus A^3/n -> 0 is a valid sufficient consistency condition; no necessity claim is made.

For second order, the exact HJW observation substitution is N=n+2. Enlarging its unspecified C_2 to at least 2 narrows the theorem's domain validly and gives N/A^3>=8. The candidate logarithm is then comparable to log(N/A^3), while n+1 and N differ by an absolute factor. The lower theorem applies to the stationary worst-case risk of each history-to-simplex predictor, including both network outputs. The claimed growing-alphabet rate and fixed-A Theta_A(log n/n) conclusion therefore follow within the explicitly stated HJW range. They are not pointwise lower bounds.

The arbitrary-initial-pair bound is explicitly preserved separately. Neither the new A^3 dependence nor the sharper logarithm is transferred to arbitrary initialization.

## 3. First-order implication and historical question

For an ordinary stationary k-state chain, one-row probability-group tilts are legal kernels. Substitution D=A=k and n=N-1 gives denominator N, logarithm N/k^2, and cap log(N-1+k), exactly as in equation (9). Its transition counts use positions 1 through N-1 and predict at Z_N. This is ordinary full-history add-one, not suffix averaging.

HJW Theorem 1 has 3<=k<=sqrt(N)/C. Enlarging C to at least 2 makes the logarithms comparable on that domain. The corollary states that domain and does not extend the five-block architecture claim to first-order chains. The binary first-order Theta(log log N/N) exception is correctly distinguished from binary second-order behavior.

Remark 1 in the published paper asks the stated full-history question. The potential-answer wording, conditional on independent external review, is appropriately cautious. The HTML and current corollaries distinguish internal analytical audits from external peer review and expressly decline current priority or first-answer claims.

The complete bounded literature audit is embedded with SHA-256 `79b16421ec826c6e0b80c4a987e1bd0a104706cc91db3341afe9553f30b995ee`. Its limitations and the distinction between a dated open-question statement and absence of a later located theorem are preserved. This final-file review did not independently repeat that current-literature search and is not a priority certification.

## 4. Architecture, precision, and range restrictions

The exact-real model retains its fixed-A architecture, positional features, smoothing BOS tokens, full causal support, no LayerNorm, and ordinary vocabulary softmax. The parameter, head-count, and width statements agree with the inherited source. A changing alphabet changes the architecture family.

The integer/dyadic statement retains the exact grid simplex, normalization rules, support floor, and s=ceil(log_2(AL)), b=32s, H=2^b, F=H^2 schedule. It correctly distinguishes fractional b from total signed width. Raw copy and narrow score magnitudes, the terminal-only broad O(L) statement, earlier A^2 coordinate allowance, signed maxima and differences, accumulation guards, and approximately 4b-bit temporary products are all retained. The stated working lengths, operation count, and streamed storage agree with the inherited precision source and its adversarial review. Generic IEEE, GPU, mixed-precision, extra rounding, fixed-exponent, training, and timing guarantees are not inferred.

This is a review of the composition and faithful inheritance of those prerequisites, not a fresh proof of every architecture or arithmetic lemma.

## 5. Independent HTML fidelity checks

The final HTML and corollary hashes and sizes were independently recomputed. For all 15 ledger entries, the source hash and byte count were checked, each complete Markdown source was independently converted with the declared Pandoc settings, and its HTML fragment was compared exactly after the documented section-ID prefixing. Decoded display-text sequences also agree. All 10 copied-source files were independently compared byte-for-byte with their original workspace sources.

The HTML has 156 unique IDs, no duplicate IDs, no missing internal-link targets, and no script, frame, stylesheet link, image, font, CSS import, or URL-based resource needed to load its content. External citation links do not supply proof text. Complete exact-real and precision proofs are present in the expandable appendices; historical source labels and older rates remain unchanged and are explained by the leading current text.

These are source-integrity and structural checks. `HTML_VERIFICATION.json` records blocked rendering: visual rendering was not verified and no browser page was rendered. Visual rendering is not an accepted check in this review, and no browser-render pass is asserted. No numerical experiment, simulation, training, external upload, or repository mutation was performed. Only this review file was added; the reviewed sources and HTML were not changed.
