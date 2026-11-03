# Positional Information for Budget-Adaptive Markov Prediction

This directory is a coherent manuscript consolidation of the v10 positional-prediction results. The article is anonymous and is not labeled as a conference submission.

The central result is the finite-horizon, same-map competitive price of exact triple counts plus prescribed boundary windows: order 1+log((M+2)/r) at supplied all-state certificate 1/M. A whole-word scan can supply the needed gate as one exact bit beyond counts and the protected endpoint. The finite attention section is a fully costed realization of positional statistics, with a stronger same-information classical counter comparison.

## Read and reproduce

- `main.pdf`: the complete article, proofs, and bibliography.
- `main.tex`, `references.bib`, and `sections/`: editable source.
- `CLAIM_TO_SOURCE.md` and `.json`: claim-level provenance and limits.
- `SOURCE_BINDINGS.json`: exact source hashes and source locations.
- `PROVENANCE_RECONCILIATION.json`: verified original/export differences.
- `COMPANION_CONTEXT.md`: already settled certificate questions and separately scoped reliability links.
- `CONSOLIDATION_LOG.md`: actual editorial changes and validation process.
- `verification/`: build, diagnostic replay, structural, and visual review evidence.

Run `bash build_local.sh` to compile and render the article. A working pdfTeX/LaTeXmk/BibTeX installation, Latin Modern fonts, AMS packages, natbib, hyperref, microtype, and Poppler are required. The script uses a writable local TeX cache and writes intermediate artifacts into `build/` and `qa/`.

Run `python3 replay_sources.py` from a checkout containing the source theorem directories to rerun the exact ACG/PBP diagnostics and the complete six-test FPA evaluator suite in isolated temporary copies. Accepted source files are not overwritten. These tests diagnose finite arithmetic and indexing; they are not substitutes for mathematical proofs.

## Contribution and chronology

The 2 November finite-bank analysis already established approximate-gate robustness and matching precision/noise/edit rates for eight floored triple frequencies plus four floored half-prefix frequencies. The present additions translate the changed direct J/C/D approximation interface, calibrate its nearest-rounded fixed bank, and give explicit copying, Boolean/ReLU, scalar-grid extraction, finite comparator/division, and resource accounting. The manuscript does not claim a new precision phenomenon, a learned predictor, neural advantage, or a half-log precision law for an entire network.

All three original statistical appendix files are preserved byte-for-byte. Full new interface and realization proofs are included. The fixed-bank lower allows arbitrary randomized decoders but concerns only its prescribed observation; its clean lower is not silently promoted to a joint lower for a different numeric fault port.

## Publication boundary

`PUBLICATION_MANIFEST.json` lists the proposed public files after validation. Build caches, raw host-specific logs, page PNGs, temporary harnesses, and source-paper downloads are excluded. Source-unit acceptance and manuscript integration review are distinct. The directory itself performs no repository upload or release.
