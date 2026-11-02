# 离线恢复与复现

在解压后的包根目录执行：

```bash
python verify_package.py --restore /新的空目录
python run_diagnostics.py /包外目录/PACKAGE_DIAGNOSTIC_RERUN.json
python rebuild_documents.py /包外目录/PACKAGE_REBUILD.json
```

不要将新输出写入已校验的包根目录。恢复检查涵盖完整载荷、继承ZIP、来源与导出哈希、接纳回执及组成证明。每个科学脚本均从独立原始恢复副本运行；只对该脚本实际使用的、已声明的元数据哈希指针做精确协调，并逐项记录。不会全局覆写、递归豁免哈希或改动数学脚本。

文档单独从源文件清洁重建，比较所有27+9页的光栅和版式文本，检查93个原生OMML公式及未改变的构建输入。PDF元数据可能不同。需本地Python及numpy、scipy、lxml、python-docx、pypdf，TeX/pdflatex/bibtex、pandoc、LibreOffice、Poppler及文档渲染辅助脚本；不联网安装。

保留的原始输入历史运维脚本不新执行；时间相关的make_manifest.py只保留来源，不冒称数学诊断。历史行政缓存与丢失的旧稿不冒称可复现。科学证明、LLM审查、有限诊断、视觉检查和压缩包审计的证据身份分别保留。
