# Outer archive helper: scoped implementation and tests

The helper verifies the selected stage manifest against a required trusted SHA-256, then verifies every listed byte count, SHA-256 and Git blob identity. The trust anchor must come from an external release receipt or independently trusted commit/inventory, never merely from hashing an untrusted manifest.

The exact source-map schema binds 134 declared original/export identities, 83 exact sources, 51 mapped sources, and the fixed original/export byte totals. Public identities must match the stage manifest. Original-byte claims are declarations bound by the trusted manifest, not recomputation of absent private source bytes.

New-directory scopes must match source parents, excluding the partly inherited strong_mixing_precision directory and including the stage provenance directory. Unlisted files and symlinks are rejected only inside those scopes. The global provenance/PUBLIC_INVENTORY.json is explicitly excluded from the stage manifest. Up to 20 explicitly listed inherited files are checked by exact identity without recursively validating historical research.

The fixed-hash newly authored retained-record validator is compiled and executed only after complete stage hash reconciliation. No archived research program is executed or imported. All stage/inherited files and scoped directory contents are checked again after the numeric pass. This does not claim a globally atomic filesystem snapshot or proof certification.

The helper requires Python -I -B before loading non-builtin modules, uses bounded no-follow descriptor reads, explicit exception-based checks, strict duplicate/nonfinite/float-rejecting JSON, and no write/network/process operations. Only stdout receives the result.

All 12 deterministic outer-helper unit groups pass with normal and optimized Python. They cover typed exact schemas, totals and changed flags, duplicate IDs/paths, digest formats, byte/Git hashes, symlinks, FIFOs, path traversal, oversized files, extra files within bounded scopes, inherited-list uniqueness/disjointness, missing trust anchors and optimized failure behavior. Fixtures use synthetic metadata or benign byte strings, not generated scientific experiments. An earlier test-harness run reached a 10-second subprocess timeout; the harness allowance was increased to 120 seconds, and both complete runs then passed. No production validation was relaxed. A newly added test first reproduced the global-inventory-name omission before it was corrected.

The earlier wrapper source is retained locally as historical preparation, not a public deliverable. The original 22 retained-validator deliverables remain unchanged. Exact assembled-candidate verification is a separate final step and is not claimed by these unit/static results.
