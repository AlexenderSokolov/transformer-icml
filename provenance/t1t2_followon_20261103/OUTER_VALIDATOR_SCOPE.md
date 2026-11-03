# Follow-on archive verifier: scope and safety boundary

This stdlib-only helper verifies a selected public archive, not the scientific claims in it. It does not import or execute archived research scripts, generate scientific cases, construct networks or chains, or recreate missing execution traces. It executes only the separately authored retained-record checker whose exact SHA-256 is pinned in the wrapper.

## Invocation and trust

Use a trusted copy of `verify_public_archive.py` with Python 3.10+ on POSIX:

`python -I -B verify_public_archive.py PUBLIC_ROOT --manifest-sha256 TRUSTED_SHA256`

The same check supports `-O`; no validation relies on Python assertions. The helper refuses to start without isolated mode and disabled bytecode writing. Obtain the manifest SHA-256 from an independently trusted release receipt or commit, not by merely hashing a manifest from an untrusted download. The helper cannot authenticate itself; its own identity also belongs in a trusted release receipt.

## What the wrapper verifies

The stage prefix is `provenance/t1t2_followon_20261103`. It reads `STAGE_FILE_MANIFEST.json`, requires its bytes to match the external SHA-256 anchor, and checks strict JSON and exact metadata schemas. The canonical source-map schema does not include `base_commit` or `hash_semantics`; those documentary fields are carried in reconciliation instead. The source entries themselves are unchanged by that metadata canonicalization.

The manifest excludes itself and `provenance/PUBLIC_INVENTORY.json`. Each listed stage entry is checked for byte length, SHA-256, and Git blob SHA-1. The source map must declare 46 source records, 709,330 original bytes, 709,304 exported bytes, 31 byte-exact sources, and 15 mapped sources. Source IDs and paths must be unique, every public identity must match the stage manifest, and changed flags must agree with original/public identity differences. Original identities are historical declarations bound by the trusted manifest; the public checker cannot rederive private pre-export bytes that are not included.

All six newly selected research directories and the provenance stage are exhaustively scanned for unexpected files. There is no mixed-parent exception. Entries outside the selected sources and provenance stage are forbidden in the stage manifest. Up to 30 inherited public files may be listed explicitly in reconciliation and are checked by their exact bytes and hashes; overlapping entries and global-inventory recursion are rejected. This does not certify the entirety of the preexisting repository or complete historical closure of every citation.

The numeric module is pinned to SHA-256 `95f7da4de8376330c19605fb2c5b715fd18089960b17b1e8286d3141eae2cca4`. Its returned three file paths, 90/8/1,008 row counts, byte lengths, observed SHA-256 values, and saved ordered-input hashes are explicitly bound to the same outer manifest. This prevents a numeric pass over a different reopened root from being silently combined with the outer file checks. Stage and inherited bytes, manifest bytes, and scoped directory listings are checked again after the numeric pass.

The selected records remain population, reverse-moment, and no-BOS saved-case consistency checks. In particular, the 1,008 no-BOS records are not full internal traces and do not certify generic exponential evaluation or ordinary fixed-word floating-point softmax. See `RETAINED_RECORD_SCOPE.md` and the archived trace-preservation clarification.

## Safe input handling and limitations

Descriptor-relative file reads use `O_NOFOLLOW` for every path component, `O_DIRECTORY` for traversed directories, and `O_NONBLOCK` plus regular-file checks for files. Root parent traversal, symlinks, path traversal, special files and malformed paths are rejected. Read sizes, total bytes, JSON structure, directory widths/depths and file counts are bounded. Duplicate JSON keys, nonfinite/floating JSON numbers, malformed UTF-8/JSON, incorrect types, unexpected fields and inconsistent identities are rejected. Read metadata is compared before and after each file read.

Checks do not claim a globally atomic filesystem snapshot, resistance to a hostile operating system, source-rights clearance, a full dependency proof, external peer review, or novelty. Use an immutable checkout or snapshot for reproducible archival verification. All original research programs remain inert bytes. The explicit, hash-pinned new checker is the only evaluated program loaded from the archive.

## Test entrypoints

- `python -I -B test_verify_public_archive.py`: 16 unit tests, including strict metadata, identity relations, numeric-result/manifest binding, inherited boundaries, trusted-anchor failure, unsafe paths, special files, symlinks, scope extras, and isolated-mode requirements. These tests passed in both ordinary and optimized modes. Synthetic metadata used in unit tests is not scientific data or an experimental result.
- `python -I -B audit_public_archive.py PUBLIC_ROOT TRUSTED_SHA256`: runs the exact pinned wrapper with an audit hook rejecting mutation, network/process operations, or compilation/execution other than the pinned new numeric module. The wrapper pin is embedded in this harness. The harness reports observations to stdout, not into the archive.
- `python -I -B test_archive_tampering.py PUBLIC_ROOT TRUSTED_SHA256`: first requires a valid baseline, then checks deterministic corruptions in new temporary copies. It covers a wrong external anchor, altered bytes, extra source/provenance files, source symlinks, duplicate manifest keys, a changed numeric module with a recomputed test manifest, inconsistent source-map totals/flags, inherited global inventory, and inherited-byte corruption when inherited files exist. It never alters the input archive or runs archived research scripts.

The exact final candidate's validation, optimized validation, audit and tamper outputs are separate release receipts. Keeping those receipts outside the self-excluding stage manifest avoids a hash cycle from embedding the manifest's own hash in a file that it hashes. The reported receipts must identify the exact final wrapper and manifest; unit tests alone are not a claim that an arbitrary assembled archive passes.
