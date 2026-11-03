# Public verification and replay boundaries

This is a bounded archive of all 258 extant artifacts in the 15 listed directories, including true prior versions, correction diffs, empty interrupted-run logs, all retained numeric arrays, distinct independent checks and their original logs. No missing artifact is represented as recovered. It supplements the existing public research history; it does not replace the frozen manuscript or earlier inventories.

## Default: read-only verification of retained evidence

In a trusted checkout pinned to the publication commit, run from the repository root:

    python provenance/float_and_attack_boundaries_20261103/verify_public_archive.py .

Use ordinary Python, without -O or PYTHONOPTIMIZE. The wrapper checks the public inventory, all selected source identities, every required inherited public dependency, original/public mappings, and declared historical-binding resolutions. It then runs only the newly reviewed stdlib retained-arithmetic module. That module reads saved arrays and exact rational values; it does not execute archived author/reviewer scripts, initialize a model, import NumPy, call a random generator, run native programs, contact a service or write into the checkout. Numeric records and compressed originals are not rewritten. The printed report names the checked counters and explicit unchecked scope.

Inventory and mapping files are trust roots from the pinned checkout, not signatures from an external authority. The verifier is not a sandbox for malicious code. Original private metadata cannot be independently checked from the public repository, and source-bound LLM reviews are not formal verification or external peer review.

## Source reconciliation is explicit

`SOURCE_EXPORT_MAP.json` gives original and public byte length, SHA-256 and Git blob identity for every selected source. The only public-copy changes remove host/runtime locations, internal coordination attribution, or private preparation/publication paths in nonmathematical logs and metadata. Original mathematical text, Python programs, scientific numbers, arrays, gzip bytes and actual correction bodies remain unchanged. A changed checksum manifest is not called the original manifest; its own original/public identity is mapped.

`PUBLIC_EXPORT_RECONCILIATION.json` records all 486 parsed historical bindings. Expected historical hashes are not silently replaced. Twenty-one occurrences name files normalized in this export; one occurrence uses the existing published central antecedent mapping. Naive original SHA checks of the public copies therefore need not pass. The wrapper verifies the public bytes and the declared pair rather than claiming those bytes are the original.

Five historical independent-replay checkpoint paths resolve to already-public, byte-identical smoke checkpoints at steps 0, 50, 100, 150 and 200. This is an explicit path alias, not a claim that the smoke file restores provenance of an independent run. The historical local replay note likewise maps to its exact published `provenance/rare_weight_20261103/PUBLIC_REPLAY.md` path. Eight historical local preparation/publication records are intentionally not public: only neutral identifiers, original hashes, sizes and unavailable status are supplied. They are not mathematical proofs or runtime inputs. Thus scientific retained-source verification is available, but the private operational metadata graph is not fully public.

## Historical replay requires a separate fresh output workspace

Do not run archived programs in this immutable evidence checkout. Some write fixed filenames or call code that can initialize models. Others make new deterministic candidate records or have backend-dependent outputs. If a separate replay is wanted, first inspect its complete import/call/output closure, create a new destination that does not already exist, copy verified sources and necessary dependencies there, and explicitly materialize any listed byte aliases. Leave generated output names absent. Use exclusive creation for each new output and record fresh identities separately. Never replace the preserved log, JSON or compressed data, and never label a regenerated record as contemporaneous evidence.

No such historical script replay was performed for this publication. The default checker neither evolves saved RNG states nor reconstructs missing random values. It does not establish a new safe pre-run capture guard for scripts that could sample or initialize a model. Existing source validation is not disabled, and original binding files are not patched to make normalized prose appear exact.

## What remains conditional or unavailable

- The deterministic same-bank float collision depends on its stated batch/slot/dtype/backend protocol. The amplified separating readout is untrained; the actual trained A/B diagnostic has equal saved probabilities and CE. This checker is not a BLAS, libm, mpmath, GPU or bitwise model replay.
- Uniform actual-backend error premises remain unproved. The rational interval example and its post-hoc endpoint reconstruction do not certify a concrete NumPy implementation. The general signed readout interval evaluator and bank multiplicity program were proposed, not implemented by this stage.
- Original broad deterministic searches and several author diagnostics saved aggregate logs rather than every candidate/intermediate. Their separate independent archives do not recover original run records.
- The trained-check first script, complete log and full JSON were overwritten. Final files and six recorded summaries cannot recover unprinted first-run values or original artifact identities.
- Initial float serialization/int8 failures, the first interrupted interval demo and the failed endpoint append retain only the actual surviving evidence and disclosure. Original interval endpoints were not contemporaneously recorded.
- The growing-feature author's original diagnostic and its later unmodified-script replay both lack their per-case intermediates. The independent complete archive is distinct from both.
- Older missing random probes, benchmark traces and initial ablation data remain missing as previously disclosed. Deterministic reconstruction is not contemporaneous capture.
- Finite retained arithmetic checks do not prove an imported PCP theorem, a worst-case asymptotic statement, full-source closure of external literature, training success or broad novelty. The strongest TV reductions use a known source and an attack able to overwrite every formula-bearing bit. The prior-art audit's broad 7/8 matching-policy assertion was retracted; the explicit correction governs.

The existing push/manual CI remains a read-only public-file integrity check. It neither runs these old scientific scripts nor certifies the mathematics.
