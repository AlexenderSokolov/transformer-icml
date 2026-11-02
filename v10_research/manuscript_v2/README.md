# Finite Precision Prediction from Bounded Causal Attention
## Research synthesis revision 2

This versioned 21-page English mathematical manuscript incorporates the accepted rescaled rare-window lower bound SH001 v1. It leaves the original bounded-causal risk frontier and signed finite-arithmetic bridge unchanged.

The new result identifies the least feasible weight ratio, up to constants, in the fixed-dimensional one-summary-block family at square-root grid resolution. Its precise statement includes the real-budget infimum, stationary and arbitrary-start comparison, fixed grid band, sufficiently large target-risk multiplier and unchanged integer triple-bank upper. It does not assert a matching all-resolution two-resource law, an arbitrary-depth lower bound, training convergence or computational superiority.

The scientific scope is frozen at 2026-11-02 05:15 UTC. The earlier approved manuscript and stage-three archive are preserved; this is a separate revision, not an overwrite. No author or institution is assigned. The manuscript is an AI-assisted modular research synthesis, not externally peer reviewed or formally verified, and depends explicitly on the accompanying full proof dossier.

## Reading and editing

- `finite_precision_prediction.pdf` is the rendered article.
- `finite_precision_prediction.tex` is the editable, figure-independent LaTeX source.
- `references.bib` is the unchanged editable bibliography.
- `finite_precision_prediction.bbl` preserves the generated bibliography for portability.
- `SOURCE_MANIFEST.json` binds directly used proof versions and comparison notes to exact SHA-256 hashes.

Section 10 maps each manuscript result to its source proof. The full R011 statistical and event-radius dependency chains remain inherited from the accompanying dossier; this manuscript does not claim to reprove them as new standalone results.

## Build

A standard TeX Live installation with pdfLaTeX, BibTeX, Latin Modern, AMS mathematics, natbib, hyperref, microtype, fancyhdr, enumitem and booktabs is sufficient:

```sh
pdflatex finite_precision_prediction.tex
bibtex finite_precision_prediction
pdflatex finite_precision_prediction.tex
pdflatex finite_precision_prediction.tex
```

The included `build.sh` performs these passes and checks the log. It also supports a Debian TeX installation whose system format/font-map cache is absent, generating the necessary cache only inside this revision's `build/` directory. Run `./build.sh --render` to produce page PNGs with Poppler. Compilation caches, audit logs and page images are verification intermediates, not part of the reading/source package.

## Scientific changes from revision 1

The new proof sets `z = kappa Q` and shortens the admissible rare-window cutoff accordingly. This keeps the tube's grid-cell cross-section independent of the weight ratio. It sharpens the earlier valid `kappa^(-(D+1))` lower rather than refuting it. The unchanged SB001 upper then gives `kappa_min = Theta(f)` uniformly across mixing promises in the stated grid band. In weak mixing this is `Theta(log M)`, with effective score range `ln ln M + O(1)`.

The uniform full-histogram corollary remains explicitly labeled as a synthesis. The original compressed `9K+1` bank and the full `K^3` bank still have different alphabet-dependent costs. No bibliography change or new novelty claim is made.
