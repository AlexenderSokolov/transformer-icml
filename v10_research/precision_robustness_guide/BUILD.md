# 第七阶段指南构建

科学冻结为 2026-11-02T08:09:06.390192Z。只使用冻结清单的十一项新接纳单元及不变的第六阶段前驱闭包。早先指南及完整旧稿没有改写。

最终格式为 Chinese-stage7-guide.docx 与 Chinese-stage7-guide.pdf。guide_math_zh.md 是数学源，guide_final_math_zh.md 是规范化构建输入。全部公式为原生可编辑 OMML，无公式图片。正文 11pt，11 页。无外发或上传步骤。

使用提供的 Codex 主运行时、Pandoc 和共享文档渲染器：

```bash
"$CODEX_PRIMARY_RUNTIME_PYTHON" v10_research/precision_robustness_guide/build_guide.py
"$CODEX_PRIMARY_RUNTIME_PYTHON" $DOCUMENT_RENDER_HELPER v10_research/precision_robustness_guide/Chinese-stage7-guide.docx --output_dir v10_research/precision_robustness_guide/qa_release_final --emit_pdf
cp v10_research/precision_robustness_guide/qa_release_final/Chinese-stage7-guide.pdf v10_research/precision_robustness_guide/Chinese-stage7-guide.pdf
"$CODEX_PRIMARY_RUNTIME_PYTHON" v10_research/precision_robustness_guide/verify_guide.py
```

每次重新构建或修改后须重新渲染并逐页打开 PNG 检查，脚本不会把视觉审核自动标记通过。SOURCE_BINDINGS.json 绑定精确接受记录、证明、组件证明和审查，不用历史候选标题推断接受状态。QA_RECEIPT.json 记录最终哈希、公式结构、页数和审核状态。

precorrection_v1 至 precorrection_v4 保留实际审读版本及差异。qa_* 是视觉核查中间件。构建器将非圆动态 OMML 定界符规范化为原生固定字符，避免 LibreOffice 的非圆动态定界符导入问题，公式本身保持可编辑。

冻结后实现澄清单独绑定 MG_final_clip_clarification.md、其独立 PASS 审查及审查哈希记录。它显式补齐攻击前工作网格裁剪，不作为第十二项新定理，不覆盖原十一项接受记录。实际改前版本与差异保存在 precorrection_v3。
