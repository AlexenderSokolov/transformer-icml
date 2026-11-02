# 中文摘要的本地编译

可编辑正文为 `summary_中文.tex`，使用 XeLaTeX 编译。PDF 是摘要；完整证明以 Markdown 交付，未把数千行证明另行重排成 PDF。

## 依赖

- 正常安装且已生成 xelatex 格式的 TeX Live 或兼容发行版。
- Noto Serif CJK SC 与 Noto Sans CJK SC 字体。
- 常见 TeX 包：fontspec、amsmath、amssymb、booktabs、tabularx、enumitem、xcolor、fancyhdr、hyperref、geometry。

源码采用 XeTeX 自带中文换行，不依赖 xeCJK。中文强调使用粗体，避免缺失中文斜体字形。

## 编译

在本目录执行两遍：

```sh
xelatex -interaction=nonstopmode -halt-on-error summary_中文.tex
xelatex -interaction=nonstopmode -halt-on-error summary_中文.tex
```

标准发行版应输出 8 页 A4 摘要。不同字体版本可能略改换行；编辑后应重新渲染每页，检查公式、表格、页脚、溢出和缺字。辅助 `.aux`、`.log`、`.out` 文件不是交付正文。

## 完整性与复制映射

在支持 sha256sum 的系统中运行 `sha256sum -c SHA256SUMS.txt` 可核对全部公开文件。若已有原始提供资料，可按 `COPY_CERTIFICATE.md` 和 `COPY_MAP.json` 的 UTF-8 字节区间重新核对科学副本。目标哈希只证明复制和文件完整性，不提高数学证据等级；重新修改数学原文后不能沿用旧版本独立审查。

另可运行：

```sh
python3 verify_copies.py
python3 verify_copies.py --sources /path/to/provided-originals
```

第一条只校验交付片段及目标文件的内部哈希一致性；第二条递归查找原文件名及匹配全文哈希，另核每个原字节区间的精确相等。没有提供原件时，不会冒称已验证来源。脚本不联网、不改文件，也不进行数学审查。

包内不含私有运行日志、身份句柄、调度/控制文档或第三方论文全文。源文件名、哈希、原数学编号和必要的科学引用保留用于追溯。

交付文件范围仅为 `SHA256SUMS.txt` 所列文件及该清单自身；不包含隐藏构建目录、审计目录、原件、历史快照或内部报告。复核脚本只检查完整性，不会提高原数学结论的证据等级。
