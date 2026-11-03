# Supplemental replay note — two separate verification annotations

2026-11-02. Added after root isolated replay; accepted REVIEW.md, checks.py, checks_results.json and source_bindings.json are not rewritten.

## Distinction

The accepted checks_results.json contains the core results emitted by checks.py **plus two fields appended after separate verifications**:

- `direct_receipt_matches: 4`
- `actual_wording_diff_reconstructs_final: true`

Running checks.py alone reproduces the core metrics, but does not reproduce those two annotations or byte-identical checks_results.json. In particular, that script writes its output file, so replay it in an isolated copy if preserving accepted result bytes. The review's final-closure paragraph refers to the combined verification sequence, not a claim that checks.py alone performed all closure steps.

## Actual original provenance

After the final source freeze, the reviewer reran checks.py, which passed 42 source-map hashes and the reported finite checks. In a separate shell execution the reviewer copied `revisions/main.before_integration_wording.tex` to `reviews/integration/reconstructed_final.tex`, ran:

```
patch --batch --fuzz=0 <reconstructed_final.tex> <revisions/integration_wording.diff>
cmp <reconstructed_final.tex> <main.tex>
```

That tool execution returned exit code 0. The retained reconstructed file remains available. No historical log file was saved for that command; this note describes the actual tool execution, not a reconstructed log.

A later separate inline Python command loaded SOURCE_VALIDATION.json, read the four root receipts, computed actual proof SHA256 values and compared them to the receipts. The first attempt indexed a receipt using just a basename and raised KeyError for FOL001's path-qualified artifact key before modifying results. The corrected actual command selected the unique receipt artifact whose `Path(key).name` matched the proof basename, asserted all four digest matches, then appended both fields to checks_results.json. Thus the diff field recorded the preceding successful patch/cmp execution, while the receipt field was checked in that corrected inline command. The combined results were then hash-bound in source_bindings.json. This was not an output from checks.py and should not be represented as such.

## Reproducible independent replay now supplied

From repository root:

```sh
python3 v10_research/richer_count_consolidation_20261102/reviews/integration/supplemental_replay.py
```

The new standalone supplemental checker independently repeats both operations, prints exactly the two fields, and does not alter accepted artifacts. It resolves the repository root from its own path, checks all four actual proof/receipt identities by the same unique-basename rule, applies the actual retained diff with `patch --batch --fuzz=0` to a temporary copy, checks the process exit status, and compares reconstructed bytes with final main.tex. Temporary files are automatically deleted.

The reviewer executed this supplemental checker successfully (exit code 0) on 2026-11-02, obtaining 4 and true. This supplements provenance and replay precision only; no mathematical claim, original artifact or accepted hash history was changed. No nonexistent original log is supplied.
