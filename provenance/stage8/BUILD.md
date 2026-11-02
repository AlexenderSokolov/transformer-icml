# Offline restoration and reproducibility

From the extracted package root:

```bash
python verify_package.py --restore /new/empty/restore
python run_diagnostics.py /outside/package/PACKAGE_DIAGNOSTIC_RERUN.json
python rebuild_documents.py /outside/package/PACKAGE_REBUILD.json
```

Do not put reports inside the checksummed package directory. `verify_package.py` checks every payload/hash, predecessor ZIP, declared source binding and accepted component, then restores export bytes from recursive ZIP chains. The restore target must be empty. No network is needed.

`run_diagnostics.py` executes each byte-distinct retained scientific/audit Python script in its own fresh package-only restoration. Original author/reviewer output files are never edited. Identical script aliases are listed. The genuinely retained first fresh-audit harness has one known transcription error; its unchanged bytes are deliberately rerun and must reproduce the exact historical assertion failure. The report separates that expected failure from current passing diagnostics; it is never relabelled a scientific pass. Only exact original-to-export SHA pointers (and the byte-count consequences where checked) for bindings consumed by that script may be reconciled in that disposable run; every pointer and basis are logged. There is no global or transitive hash override. Historical original-input operational scripts are preserved but not newly rerun; document builders/verifiers run in the separate document audit. `make_manifest.py` is a provenance-authoring generator, not a mathematical diagnostic; its exact source is retained but its time-dependent administrative output is not represented as a replay check.

Dependencies: Python 3 with numpy, scipy, lxml, python-docx, pypdf; a TeX installation supporting pdflatex and bibtex; pandoc with OMML support; LibreOffice; Poppler (`pdfinfo`, `pdftotext`, `pdftoppm`). The document rebuild helper uses the installed documents-skill rendering utility; see its `--render-helper` option for an explicit path. It does not download or install dependencies.

Clean document reproduction deletes copied generated outputs, rebuilds the English source, rebuilds and renders the Chinese native-math DOCX, then compares every delivered/rebuilt PDF page raster and layout text. PDF metadata may differ. Native DOCX equations and unchanged build-input hashes are checked separately. This is a reproducibility audit, not a substitute for direct visual review or mathematical proof.

Full scientific closure is restored; old administrative preservation baselines and unavailable overwritten draft outputs are not falsely presented as reproducible history. See START_HERE.md and DEPENDENCY_SOURCE_MAP.json.
