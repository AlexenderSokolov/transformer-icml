# 第五阶段指南构建

科学冻结：2026-11-02 06:05 UTC。正文源为 guide_math_zh.md；build_guide.py 通过 Pandoc 转为原生可编辑 OMML，再由 python-docx 统一排版。需要 Pandoc、Noto Serif CJK SC、Latin Modern Math 及项目使用的 Codex 主运行时。

```bash
"$CODEX_PRIMARY_RUNTIME_PYTHON" build_guide.py
"$CODEX_PRIMARY_RUNTIME_PYTHON" $DOCUMENT_RENDER_HELPER Chinese-stage5-guide.docx --output_dir qa_rebuild --emit_pdf
cp qa_rebuild/Chinese-stage5-guide.pdf Chinese-stage5-guide.pdf
"$CODEX_PRIMARY_RUNTIME_PYTHON" verify_guide.py
```

实际使用的文档渲染器路径由安装环境提供；移植时可替换为同版本脚本的位置。每次重建后须查看全部六页图像，不能以文本提取替代视觉检查。SOURCE_BINDINGS.json 逐项绑定研究根目录中的完整科学源、对应接收与审查；摘要不替代这些全文。guide_final_math_zh.md 为确定性公式规范化源。原阶段指南与历史交付均不修改。

首次创建已单独执行文档技能的操作标记。最终交付是同目录 DOCX 与 PDF；qa_* 中图像仅供质量检查。
