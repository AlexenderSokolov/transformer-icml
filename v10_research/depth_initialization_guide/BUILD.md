# 第六阶段指南构建

科学冻结 2026-11-02 06:56 UTC（北京时间14:56）。本目录是新指南，不改写旧指南或第五阶段。

最终交付为 Chinese-stage6-guide.docx 与 Chinese-stage6-guide.pdf。DOCX 公式是原生 OMML，可在 Word 中编辑，不是图片。

使用提供的 Codex 主运行时、Pandoc 和文档技能渲染器：

```bash
"$CODEX_PRIMARY_RUNTIME_PYTHON" v10_research/depth_initialization_guide/build_guide.py
"$CODEX_PRIMARY_RUNTIME_PYTHON" $DOCUMENT_RENDER_HELPER v10_research/depth_initialization_guide/Chinese-stage6-guide.docx --output_dir v10_research/depth_initialization_guide/qa_release4 --emit_pdf
cp v10_research/depth_initialization_guide/qa_release4/Chinese-stage6-guide.pdf v10_research/depth_initialization_guide/Chinese-stage6-guide.pdf
"$CODEX_PRIMARY_RUNTIME_PYTHON" v10_research/depth_initialization_guide/verify_guide.py
```

渲染后必须逐页打开 PNG 检查；脚本不会自动把人工视觉审核置为通过。重新构建会重置视觉审核状态。SOURCE_BINDINGS.json 记录直接科学来源及接受记录的内容哈希；QA_RECEIPT.json 记录最终交付哈希、公式结构、页数及视觉审核。qa_* 为检查中间产物，不是额外交付件。
