# Finite Information Cuts in Markov Prediction: Precision, Depth, and Robustness

## Comprehensive research draft revision 5

This English manuscript preserves the previous mathematical core and integrates the accepted depth, coordinate-capacity and robustness results. A main narrative distinguishes the experiments; technical appendices provide the proofs and complete resource accounts. Scientific scope is frozen at **2026-11-02 08:09:06 UTC**. A separately recorded post-freeze implementation clarification explicitly appends exact working-lattice clipping before the general-Markov fault, counting its stages before precision selection and charging its all-token costs. The original proof/review bytes remain unchanged; they are not represented as having already stated this omitted step. This clarification adds no new risk rate or source class.

### What is established

- Fixed-family grid/attention-range frontiers, binary versus larger-alphabet mixing dependence, and arbitrary-initialization prediction.
- Mixing-dependent bounded-primitive depth at the square-root grid.
- Clean and robust IID coordinate-capacity/depth sandwiches, with a complete influence-reveal lower.
- A specific folded encoder's pre-grid vulnerability, followed by redesigned robust dyadic and rational curve representations.
- A robust general-Markov upper at the actual terminal row, with paid rational outputs and explicit false-mass control.
- An IID effective-precision theorem for independent real pre-grid fault amplitude.

The general-Markov sufficient packing exponent R differs from the lower's whole-bank dimension D = R K³. That gap remains open. IID upper bounds do not transfer to general Markov sources. All dimensional constants are scoped as stated. Internal grid resolution, full working precision, output precision, primitive depth and bit-machine/PURE depth are different resources.

### Proof and evidence boundaries

Newly integrated proofs are developed in the manuscript. Earlier full-history add-one/selector, event-radius, compressed-interface identity and stationary operator inputs are explicitly identified as inherited; their full original proofs remain in the accompanying dossier. This is not a claim to have newly rederived that statistical chain.

The manuscript is AI-assisted. Independent LLM mathematical reviews and finite diagnostics are not formal verification, external peer review, emitted-network execution or a learnability result. The targeted primary-source comparison credits known companding, folding and geometric coding; it does not certify novelty. No publication or external submission is implied.

### Files and rebuild

- `finite_precision_prediction.tex`: editable self-contained LaTeX source (no external partial TeX or figures needed to compile).
- `references.bib` and `finite_precision_prediction.bbl`: editable and generated bibliography.
- `finite_precision_prediction.pdf`: rendered manuscript.
- `SOURCE_MANIFEST.json`: exact adopted proof/review/source SHA-256 bindings and scope.
- `PREVIOUS_VERSIONS_BINDINGS.json`: pre-edit preservation bindings for earlier manuscripts and deliveries.
- `build.sh`: reproducible local build helper.
- `QA_VERIFICATION.json`: author rendering, preservation and isolated clean-rebuild evidence after final verification.

Run `bash build.sh`; add `--render` to produce PNG pages with Poppler. The script uses pdfLaTeX, BibTeX and standard TeX Live packages and creates missing TeX caches locally. Equivalent commands are:

```sh
pdflatex finite_precision_prediction.tex
bibtex finite_precision_prediction
pdflatex finite_precision_prediction.tex
pdflatex finite_precision_prediction.tex
```

Build caches, PNG pages, audit files and logs are verification intermediates. Earlier versions and deliveries are not overwritten. A later independent manuscript-level science audit is separate from author QA and source-level reviews.
