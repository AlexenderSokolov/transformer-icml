# Finite Precision Prediction from Bounded Causal Attention

A 19-page, single-column English mathematical research synthesis. The manuscript has no assigned author or institution and makes no journal-submission, novelty-certification, training, or external-peer-review claim.

## Reading and editing

- `finite_precision_prediction.pdf` is the rendered article.
- `finite_precision_prediction.tex` is the editable LaTeX source.
- `references.bib` is the editable bibliography. The bibliography is also available in the generated `.bbl` for archival portability.
- `SOURCE_MANIFEST.json` binds every directly used modular proof and comparison note to its SHA-256 hash.

The scientific scope is frozen at 2026-11-02 04:45 UTC. The article depends on the accompanying complete proof dossier, in particular the inherited R011 full-history statistical bounds and event-radius interfaces. It is not a substitute for that dossier or a formally verified standalone proof. Section 10 maps manuscript claims to exact proof versions and states the dependence boundaries.

## Build

A standard TeX Live installation with pdfLaTeX, BibTeX, Latin Modern, AMS mathematics, natbib, hyperref, microtype, fancyhdr, enumitem and booktabs is sufficient:

```sh
pdflatex finite_precision_prediction.tex
bibtex finite_precision_prediction
pdflatex finite_precision_prediction.tex
pdflatex finite_precision_prediction.tex
```

The included `build.sh` performs these passes and checks the log. It also supports a Debian TeX installation whose system format/font-map cache is absent, generating the necessary cache only inside `build/`. Run `./build.sh --render` to produce page PNGs with Poppler. Compilation caches, logs and QA images are intermediates; the PDF, `.tex`, `.bib`, `.bbl`, source manifest and this README are the useful reading/source package.

## Editorial corrections incorporated

The final manuscript explicitly requires fixed strictly positive local weight bounds and a finite causal mask-density budget permitting `c <= 1/3`. It distinguishes the public mixing-class parameter from the hidden stationary certificate. It separates final cut resolution from full arithmetic widths, fixed ideal depth from expanded circuit depth, and the ordinary full-histogram baseline from the compressed bank. The uniform-histogram corollary is labeled as a synthesis rather than an additional accepted proof unit.
