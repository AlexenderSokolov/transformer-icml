# Finite Precision Prediction from Bounded Causal Attention
## Research synthesis revision 3

This separate 30-page English mathematical manuscript incorporates the accepted uniform IID grid floor, full one-block weight/grid frontier, and stationary binary refinement. It preserves all earlier manuscript versions and frozen dossiers.

The scientific scope is frozen at **2026-11-02 06:05 UTC**. No post-cutoff candidate result is included. The complete modular proof dossier accompanies this synthesis; in particular, the R011 full-history statistical and event-radius inputs remain inherited, not newly reproved standalone theorems. The work is AI-assisted, independently LLM-audited, not externally peer reviewed or formally verified. No authorship or institution is assigned.

## Main scope

- The fixed-depth bounded causal finite-evaluator risk theorem remains unchanged and retains its K >= 3 scope.
- In the fixed-dimensional one-summary-block local positive-weight family, K >= 3 has the complete joint risk frontier for both stationary and arbitrary initialization. A separate grid floor remains uniform over every finite weight envelope.
- K = 2 has a matching **stationary-only** frontier with a square-root mixing cutoff, using a binary active Markov window and weighted return analysis of the unchanged paid decoder.
- At beta = 1/M and square-root grid resolution, the stationary weight-ratio threshold is constant for binary sources and logarithmic for each fixed K >= 3. This is not an unrestricted Transformer theorem or a uniform-in-alphabet/dimension claim.
- The improved positive-beta arbitrary-start binary frontier remains open here. Partial successor work is excluded.
- Cut resolution, weight range, full arithmetic word length, total memory, forward/offline work and expanded circuit depth remain distinct. The existing SB001 finite program and cost ledger are unchanged.

## Files

- **finite_precision_prediction.pdf**: rendered article.
- **finite_precision_prediction.tex**: self-contained editable LaTeX source; no external figure or partial-source files are required.
- **references.bib**: editable bibliography, byte-identical to revision 2.
- **finite_precision_prediction.bbl**: generated bibliography for portability.
- **SOURCE_MANIFEST.json**: exact SHA-256 bindings to directly used proof versions, full/delta reviews, acceptance receipts and bounded literature notes.
- **build.sh**: local build and verification helper.

Section 12 maps manuscript results to their complete source proofs. The targeted adjacent-literature screen does not license claims about unread theorems or research priority; no new bibliography item or novelty certification is introduced.

## Rebuild

A standard TeX Live installation with pdfLaTeX, BibTeX, Latin Modern, AMS mathematics, mathtools, natbib, hyperref, microtype, fancyhdr, enumitem, array, longtable and booktabs suffices:

~~~sh
pdflatex finite_precision_prediction.tex
bibtex finite_precision_prediction
pdflatex finite_precision_prediction.tex
pdflatex finite_precision_prediction.tex
~~~

Alternatively run ./build.sh. It also handles an absent Debian TeX format/font-map cache by generating local files under build/, without changing the system installation. ./build.sh --render produces page PNGs with Poppler.

The article is a modular scientific synthesis, not a submission-ready standalone replacement for its inherited proof dossier. QA records, audit logs, rendered page images, partial authoring scratch files, auxiliary files and build caches are verification intermediates, not part of the reading/source payload.
