# T1/T2 retained-record validator

## Scope and result

This is a deterministic, read-only consistency validator for the selected saved numeric records. It is not a formal proof, scientific replay, new experiment, or certification of the research conclusions. Archived research programs are never imported or executed. No new binary words or parameter cases are generated, no RNG is used, and no model or transition matrix is initialized.

The public entry point is `verify_records(root)` in `verify_retained_records.py`. It reads 14 fixed public numeric paths. They contain 58,048 top-level file records, counting separately the retained author/reviewer provenance copies and the two identical family files. Each family file additionally contains 624 stored path entries. The spline archive retains 992 deliberate duplicate-input pairs: the separate exact case and its separately indexed zero-shift grid case. No original duplicate is removed.

The new addenda contribute 24,804 records: author collision 972, refined-port 20,088, independent collision 1,620, independent positionwise 1,620, and terminal-port paths 504. The older nine paths contribute 33,244 records. The discarded buggy Route-B files each retain nine rows explicitly labeled `discarded_history: true`; their scientific predicate is not required to be correct.

## What is checked

- Strict JSON rejects repeated object keys, floating-point/nonfinite tokens, oversized integers, deep structures, excessive arrays/objects, and overlong lines. TSV headers and row widths are exact.
- Schemas are exact at all declared nested record levels. Booleans cannot substitute for integers. Rational strings have bounded canonical reduced form, positive denominators, and no alternate spelling.
- Input files are descriptor-relative bounded regular-file reads. Absolute/traversing/internal empty paths, every symlink component, directories as data files, FIFOs, and oversized files are rejected. The root is opened component by component without following symlinks. Inputs are checked for descriptor metadata changes during reading.
- Every retained record key is unique within its file; counts and ordered-key SHA-256 fingerprints are fixed from the frozen saved records. This checks the exact saved key sequence without regenerating an entire mathematical case space. Indexed deliberate duplicates and separate provenance paths remain distinct.
- Transition counts are derived only from words already present in each record. Stored terminals, successor counts, margins, and previous-seen references are cross-checked where present.
- Elementary relationships between saved fields are checked: canonical probability ranges/sums, sums of recorded path probabilities, saved factor products, recorded ratios/midpoints, stored error/bound comparisons, saved pass flags, and applicable saved coefficient/count equalities. No spline/network output, perturbation experiment, transition-matrix product, or full path-probability model is recomputed.
- Terminal feasibility lists are compared with the groups of already-retained words. There is no graph search, Euler feasibility recomputation, or generation of an unrecorded word.

The refined-port files contain no null `bound9` values; the retained schema therefore requires a rational bound. Broader possibilities in the archived generation script are not treated as retained observations.

## Verification performed

The full new unit suite has 17 deterministic test groups, using copied retained examples and local corruption fixtures. Tests cover positive records, schema/type corruption, malformed/noncanonical fractions, duplicate/nonfinite JSON, nested keys, count/error/bound corruption, incomplete coverage, duplicate rows, blank/missing-newline JSONL, bad UTF-8, header corruption, path traversal, root/intermediate/final symlinks, FIFOs, oversized files, and optimized Python behavior. Fresh temporary fixtures are used; no source artifact is edited. Both ordinary and `-O` unit runs pass.

The complete 14-file validation passes in both ordinary and optimized isolated Python; their JSON reports are byte-identical. A separate full run under a Python audit hook rejects file mutations, network operations, and process launches. No such operation was attempted, and all 14 input SHA-256 values were unchanged. Runtime checks use explicit exceptions rather than removable Python assertions.

Tests were written and observed failing before the corresponding validator behavior was implemented or tightened. Private red-run logs and preparation scripts are excluded from the publication deliverables because their diagnostic context includes local preparation paths. The published success logs, fixture sources, result reports, and source hashes are sufficient to rerun the tests.

## Running

Use a POSIX Python 3.10+ environment with safe descriptor-relative open support:

`python -I -B verify_retained_records.py PUBLIC_REPOSITORY_ROOT`

Optional optimized check:

`python -I -B -O verify_retained_records.py PUBLIC_REPOSITORY_ROOT`

The script prints a JSON report to stdout and returns 0 on success, 1 on validation failure, or 2 for invalid CLI usage. It writes no files. `-I` avoids current-directory/module-path shadowing; `-B` prevents Python bytecode-cache creation. An outer helper importing the module should set `sys.dont_write_bytecode = True` before import. Keep the test file and `fixtures/` beside the module to run the standalone unit suite. The test harness creates fresh temporary files; it is not the read-only production entry point.

## Integration boundary and limitations

The outer archival helper must independently reconcile the complete public allowlist, file sizes, and content SHA-256, including byte-identical provenance copies. This module binds the selected numeric schemas and retained input-key coverage, not every numeric payload byte. A structurally valid edit to an unchecked scientific quantity can be rejected by the outer full-byte reconciliation even when this module alone cannot detect it. The module does not audit unlisted files, publication rights, privacy, mathematical antecedents, or remote repository state.

A checksum or consistency pass does not recover overwritten source versions, recreate missing contemporaneous search logs, elevate an AI diagnostic to proof, or validate the discarded buggy conclusion. These limitations remain part of the publication package.
