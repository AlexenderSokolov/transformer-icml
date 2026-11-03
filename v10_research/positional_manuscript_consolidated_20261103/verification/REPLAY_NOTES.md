# Replay scope and correction

The first consolidated replay copied the ACG diagnostic into a directory too shallow for its unused `BASE.parents[2]` root expression, producing an IndexError before any diagnostic ran. The harness was corrected to preserve repository-relative directory depth; the diagnostic source itself was not changed. The first PBP replay completed and the first FPA six-test suite passed. All three are rerun with the corrected common harness, and only the final exact reports support the aggregate result.

Each replay uses temporary source copies. The original accepted files remain unchanged. Finite diagnostics test indexing, rational inequalities, and implementation contracts; they do not establish all-horizon probability theorems.
