# Stage 8 Chinese source corruption guide

Final local deliverables: `Chinese-stage8-guide.docx`, `Chinese-stage8-guide.pdf`, and `guide_math_zh.md`.

Nine readable pages, 11 pt body, 93 native editable OMML math objects; no formula images. Scientific freeze: 2026-11-02T09:22:25.495805Z. The six new accepted units are SC001, SC002, SC003, BT001, BT002 and EP001; SC001 and BT002 each have two bound proof components. The guide preserves the distinction between accepted statistical-rate closure and BT001's still-open stronger transport premise.

Build and verify from repository root:

```bash
"$CODEX_PRIMARY_RUNTIME_PYTHON" v10_research/source_corruption_guide/build_guide.py
"$CODEX_PRIMARY_RUNTIME_PYTHON" $DOCUMENT_RENDER_HELPER v10_research/source_corruption_guide/Chinese-stage8-guide.docx --output_dir v10_research/source_corruption_guide/render --emit_pdf
cp v10_research/source_corruption_guide/render/Chinese-stage8-guide.pdf v10_research/source_corruption_guide/Chinese-stage8-guide.pdf
"$CODEX_PRIMARY_RUNTIME_PYTHON" v10_research/source_corruption_guide/verify_guide.py
```

`SOURCE_BINDINGS.json` pins proofs, full reviews, receipts, diagnostics, source records, the original mandate and the bounded literature screen. `VERIFICATION.json` records structural/hash/rebuild checks. Rendered page images are QA evidence, not formula assets. `revisions/` preserves the genuine draft delta adding explicit source-independent offline-kernel/minimax quantifier language. Earlier artifacts were not edited.

External citations are not reproduced in this explanatory guide; the bound source_corruption_screen.md preserves verified source links and precise reading scopes. No new novelty claim follows.
