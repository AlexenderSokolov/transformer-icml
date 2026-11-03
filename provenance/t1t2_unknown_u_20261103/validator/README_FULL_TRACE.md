# Safe full-trace archive verification

This newly authored helper checks the exact preserved full-trace source and its saved data layout. It does **not** run a scientific experiment, prove the recorded assertions, reconstruct a network, or execute any archived checker or launcher.

## Read-only verification

Use Python 3.10 or newer on POSIX, with isolated imports and bytecode disabled:

```sh
python -I -B provenance/t1t2_unknown_u_20261103/validator/verify_full_trace.py PUBLIC_ROOT --manifest-sha256 TRUSTED_SHA256
```

`PUBLIC_ROOT` is the checked-out archive root. Obtain `TRUSTED_SHA256` from an independently trusted release receipt or commit/inventory. Computing the hash of an otherwise untrusted manifest and passing that value does not establish authenticity. The enclosing archive verifier must itself pin this helper's exact bytes before importing or executing it.

The default command only reads files and prints a JSON result. It does not create caches, modify records, contact a network, or invoke another program. `PASS_ARCHIVED_BYTES_AND_SAVED_SCHEMA_ONLY` is intentionally narrower than a scientific or theorem-verification result.

## What is checked

- The externally anchored manifest has exactly the supported schema, source identity, ordered chunk inventory and four source bindings.
- The logical full trace is exactly 79,712,544 bytes with SHA256 `b2559d1d28cf43d54a42f12adff27b65d1fbdb113a2fc1ed13b347b9cc0f34cf` and 1,008 newline-terminated records.
- Each chunk is at most 4 MiB. Ordered offsets, record ranges, per-chunk lengths/hashes and concatenated original length/hash all agree. Chunk boundaries retain original newline-aligned bytes; nothing is parsed and reserialized for reconstruction.
- Every row is strict UTF-8 JSON. Duplicate object keys, floating-point/nonfinite tokens, BOMs, unpaired surrogates, excessive nesting, large integers and excessive collection/string sizes fail closed.
- Every retained object has the declared exact field set. Integers and booleans are type-checked separately. All rational objects have integer numerator, positive denominator and greatest common divisor one. Sparse vectors have bounded matching dimensions and strictly increasing, unique, nonzero entries. Projection triples, attention edges, gates, candidate records and residual-state fields have the declared shapes.
- Saved record indices and input identities cover N = 3 through 8, eta = 1/4 then 1/32, and all saved bit strings in order, without duplicates or missing rows. This checks an archive inventory; it does not generate model outputs or evaluate those inputs.
- The saved completed statuses, null failure/partial-work fields, 1,008 recorded passes, 157,248 recorded true assertions, 16 N=3 rows and 236 recorded J=0 rows match the frozen census. These booleans are inspected and counted, not independently proved.
- Four historical source hashes in each row are original-byte identities. The helper checks their explicit map references, exact source-map SHA256 values, original and public identity entries, and the current public source file bytes. The report's original hash `79e81b718fbb89990d4a679fbd6fd5f1aec30a65e29ac8ddb9fb43cca5afec3a` may resolve through the inherited map to privacy-normalized public bytes. Row bytes and original hashes are never rewritten.

The helper does not apply projections, evaluate scores, exponentials or hinges, derive a Boolean-match oracle from input bits, recompute residual arithmetic, or establish an unknown-u, compact-causal, fixed-word, floating-softmax or theorem claim. It is distinct from the earlier abbreviated records and does not recover missing historical intermediate data.

## Optional exact reconstruction

Only an explicit option enables writes:

```sh
python -I -B provenance/t1t2_unknown_u_20261103/validator/verify_full_trace.py PUBLIC_ROOT --manifest-sha256 TRUSTED_SHA256 --reconstruct-to NEW_ROOT
```

The helper first completes all read-only checks. It then exclusively creates `NEW_ROOT`, which must not already exist, and writes exactly:

```text
NEW_ROOT/v10_research/route_a_bos_causal_compile_20261103_1411/full_trace_cases_v1.jsonl
```

Its existing parent must be an accessible non-symlink directory. The file is created exclusively with mode 0600 under new mode-0700 directories. No existing destination root, file or symlink is overwritten. Every copied chunk and the concatenation are hashed again. On an ordinary detected failure, the partial output file is removed; newly created empty directories may remain. An interrupted process or machine crash can leave a partial destination and is not a successful reconstruction. Select another new destination rather than reusing a failed root.

All source and destination components are accessed with descriptor-relative no-follow operations, and source files must be regular bounded files. FIFO/device/symlink inputs are rejected. Size and metadata are checked before and after each read. Operate on a stable checkout and a destination parent you control. This is not a sandbox against another process with the same account or an administrator concurrently replacing directories or modifying the helper itself.

Reconstruction does not launch the historical checker. In particular, a historical checker may require original pre-normalization source hashes and reject the privacy-normalized public report; do not change the frozen row hashes or run that checker as a substitute for this archive check.

## Separation from the whole-archive verifier

This helper verifies only the full-trace chunk manifest, all full-trace data, and its four explicitly referenced original/public source bindings. The outer verifier owns the exact whole-archive inventory, complete source-map schemas, inherited maps, auxiliary artifacts, and trust anchors. A successful full-trace result does not certify those unrelated files.

Public API for the pinned outer verifier: `verify(root, trusted_sha256, destination=None)`. Leave `destination` unset for the outer verifier. Lower-level functions exist for deterministic unit tests; invoking them alone is not an authenticated release verification.

## Software tests

```sh
python -I -B provenance/t1t2_unknown_u_20261103/validator/test_verify_full_trace.py
python -I -B -O provenance/t1t2_unknown_u_20261103/validator/test_verify_full_trace.py
```

The tests construct small deterministic synthetic fixtures, with no RNG, archived program execution or scientific recomputation. Synthetic rows intentionally use placeholder numeric fields: they demonstrate the narrow distinction between valid stored schema and independently verified scientific truth. Tests cover malformed JSON, noncanonical rationals, wrong types/status/shapes, missing/order/coverage errors, corrupt hashes/ranges, mutation during a read, path traversal, file/directory symlinks, FIFOs, exact reconstruction, refusal to overwrite and partial-file cleanup. Test workspace directories are exclusive and removed afterward. The tests require write access beside the new helper for these small temporary fixtures.
