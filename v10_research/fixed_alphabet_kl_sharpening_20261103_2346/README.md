> Public-export notice: this is a historical package README. Original build/check instructions and hashes refer to the pre-export preparation. Read ../../provenance/terminal_kl_20261104/PUBLIC_EXPORT.md before running scripts.

# Fixed alphabet terminal KL at logarithmic rate

Local research package, 4 November 2026.

## Read first

Open `fixed_alphabet_sharp_terminal_kl.v1.html`. It is self-contained and needs no script, equation service, external font or network resource. The main composition and complete sharpened statistical proof are shown directly. Expand the appendices for all prerequisite proofs, reviews, the bounded prior-art audit, and the primary-source matching-lower-bound audit.

The frozen source `tilted_occupation_terminal_kl.candidate.v1.md` is unchanged and has SHA-256 `c42b6f1d86c9c91aa6ba8257a86c613150e6fb477deb549cd70d1e7b79548281`. Two source-bound analytical reports pass its new statistical proof. The candidate-status paragraphs remain historical text and are not silently rewritten. The composition identifies the later review status and the scope of each review.

## Main conclusions

- Actual-terminal full-history add-one has uniform forward-KL risk at most `min{log(n+A), A^4[log A+1536 A(1+floor(log_2 n))]/(n+1)}` for every finite A>=2 and n>=1, allowing arbitrary homogeneous second-order rows and arbitrary initial-pair distributions.
- The unchanged five-block exact-real output R inherits a separate `2A(44A+1)^2/(n+2+A)` penalty.
- The separately reviewed integer/dyadic evaluator Q inherits a separate `8A(46A+2)^2/(n+2+A)` penalty and positive output support, at fractional precision `b=32 ceil(log_2(A(n+2+A)))`. Signed magnitude and accumulation/product widths are additional paid resources.
- For each fixed A, the risk order is `log n/n`. The independently checked HJW stationary lower bound establishes matching worst-case minimax order for B, R and Q over stationary and unrestricted-initial-pair classes. This is not a per-source or every-prescribed-start lower bound.
- The leading A^5 upper factor is not the sharp A^3 stationary minimax alphabet dependence. No optimal growing-A theorem, generic IEEE certificate, constant-word-length result, training result, executed evaluator certificate, or novelty certification is claimed.

The n=0 case is stated separately in the composition. The final-file review checks the composition and its exact HTML bytes; it does not turn source reviews into formal verification or external peer review.

## File guide

- `sharp_kl_output_corollaries.v1.md`: new composition, separate output corollaries, fixed-A minimax implication, and all scope qualifications.
- `tilted_occupation_terminal_kl.candidate.v1.md`: frozen statistical proof, retaining constant 1536.
- `tilted_occupation_analytical_review.v1.md` and `tilted_occupation_independent_review.v1.md`: complete statistical reviews. The second also supplies an alternative stronger-constant derivation, which the main statement does not adopt.
- `sources/` and `reviews/`: unchanged copies of the exact-real and precision prerequisites and their reviews, plus the bounded prior-art audit.
- `primary_source_matching_lower_audit.v1.md`: the HJW theorem applicability, exact N=n+2 indexing, domain, and reductions.
- `log_squared_terminal_kl.v1.md` and `analytical_review.v1.md`: preserved predecessor proof and review.
- `SOURCE_BINDINGS.json`: exact embedded-source hashes and copy provenance.
- `HTML_VERIFICATION.json`: source-fidelity and HTML-structure checks, with rendering status.
- `final_file_review.v1.md`: independent review binding the final composition and HTML hashes.
- `FINAL_ARTIFACT.json`, `MANIFEST.json`, and `MANIFEST.sha256`: final identity and sealed file ledger.

## Reproducibility and limits of verification

`python build_html.py` regenerates the HTML with installed Pandoc, preserving the frozen source bytes. `python check_html.py` checks every embedded conversion, normalized displayed text, source hashes, internal anchors, and absence of external resources. These are document-integrity checks, not mathematical numerical experiments. The checker never evaluates the source process or the theorem's inequalities numerically.

The optional visual rendering check was not completed. No browser-rendered visual PASS is claimed. Plain mathematical notation, source fidelity, offline structure, and anchor validity are checked independently of rendering.

No mathematical numerical experiments, simulation, model training, external upload, or public repository mutation were performed for this package. The package does not include the copyrighted published PDF; its primary-source audit records the verified reference and source identity.
