# Finite Information Cuts in Markov Prediction: Precision, Range, and Depth
## Research synthesis revision 4

This separate 45-page English mathematical manuscript consolidates the grid, attention-weight-range and actual bounded-primitive-depth results. All previous manuscript versions and frozen proof dossiers are preserved.

The scientific theorem scope is frozen at **2026-11-02 06:56 UTC**. The complete modular proof dossier accompanies the synthesis. In particular, the R011 full-history statistical and event-radius inputs remain inherited, not newly reproved standalone theorems. The work is AI-assisted, with independent LLM mathematical audits, and is not externally peer reviewed, formally verified or a submission-ready standalone proof. No authorship or institution is assigned.

## Main scope

- The fixed-dimensional, fixed-locality one-summary-block family has the complete joint grid/weight frontier for every fixed alphabet size K >= 2 and both stationary and arbitrary initialization.
- The binary cutoff is max(sqrt(beta), 1/M), compared with max(beta, 1/M) for K >= 3. The arbitrary-start extension uses actual terminal counts, first-hit densities and true exit weights; a weighted endpoint-mixing shortcut is disproved, not assumed.
- Separate fixed-depth bounded causal finite evaluators have the matching grid profile. Their upper membership and finite arithmetic are explicitly proved; they are not identified with the one-block real-table implementation.
- At beta = 1/M and square-root grid resolution, the weight-ratio threshold is constant for binary sources and logarithmic for each fixed larger alphabet, under either initialization and sufficiently large fixed risk multipliers.
- A fixed-width, zero-logit dyadic compander attains sampling-order risk at square-root grid resolution with O(log log M) actual primitive depth for all mixing promises and initializations. The matching necessary depth order is proved for K >= 3 and beta = 0 under fixed per-stage budgets and a uniform finite-evaluation certificate.
- The depth theorem is not an all-resolution three-resource frontier, a necessary-depth statement for every positive beta, or a Boolean/PURE circuit-depth theorem. Final cut precision, coefficient precision, full words, working memory and execution costs remain distinct and paid.
- The previously accepted SB001 programs/costs are unchanged. The growing-depth construction has its own explicit per-stage arithmetic certificate and complete additional ledger.

## Files

- **finite_precision_prediction.pdf**: rendered article.
- **finite_precision_prediction.tex**: self-contained editable LaTeX; no external figure or partial-source files are required.
- **references.bib**: editable bibliography. The original eight records are unchanged; two verified primary-source companding/depth-precision attributions are appended.
- **finite_precision_prediction.bbl**: generated bibliography for portability.
- **SOURCE_MANIFEST.json**: exact proof, review and acceptance bindings, with the scientific cutoff and separately dated attribution context.
- **build.sh**: local build and verification helper.

Section 15 maps the manuscript to its full proof sources. The narrow literature comparisons do not certify novelty or exhaustive prior-art coverage. The two new attribution checks occurred after the theorem freeze and introduce no new scientific claim.

## Rebuild

A standard TeX Live installation with pdfLaTeX, BibTeX, Latin Modern, AMS mathematics, mathtools, natbib, hyperref, microtype, fancyhdr, enumitem, array, longtable and booktabs suffices:

~~~sh
pdflatex finite_precision_prediction.tex
bibtex finite_precision_prediction
pdflatex finite_precision_prediction.tex
pdflatex finite_precision_prediction.tex
~~~

Alternatively run ./build.sh. It handles missing Debian TeX format/font-map caches by generating local files under build/, without changing the system installation. ./build.sh --render produces page PNGs with Poppler.

The PDF can be read by itself, but the full mathematical dependency chain requires the accompanying modular dossier. QA records, audit logs, rendered page images, partial authoring scratch, auxiliary files and build caches are verification intermediates, not part of the reading/source payload.
