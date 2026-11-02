# 本地编译与完整性检查

摘要可编辑源为 summary_中文.tex，目标为 6 页 A4 PDF；完整证明另以 Markdown 给出，不把所有证明压缩到 6 页内。

## 常规编译

需要 XeLaTeX、Noto Serif CJK SC 与 Noto Sans CJK SC 字体，以及 geometry、fontspec、amsmath、amssymb、booktabs、tabularx、enumitem、fancyhdr、hyperref 等常见包。源码使用 XeTeX 中文换行，不依赖 xeCJK。

在本目录执行两遍：

```sh
mkdir -p build-local
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build-local summary_中文.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build-local summary_中文.tex
```

得到 build-local/summary_中文.pdf。编辑后的 PDF 应重新渲染并逐页检查，不能仅因命令退出成功就断言排版正确。字体版本变化可能改变换行；成稿应不超过 6 页，公式、页眉页脚与中文必须可读。编译辅助文件不是交付正文。

## 已有 TeX 工具但缺少预生成格式的环境

若系统没有可用的 xelatex 格式、默认用户缓存又不可写，不需扩大权限或修改系统。可以在自己的可写工作目录建立格式和缓存，显式设置 TEXMFVAR、TEXMFCONFIG、TEXMFCACHE、TEXMFHOME、XDG_CACHE_HOME、TEXFORMATS，并让 TeX／字体检索指向已有系统安装。典型 TeX Live 安装可先在本地格式目录运行：

```sh
xetex -ini -etex -no-shell-escape -interaction=nonstopmode -halt-on-error -jobname=xelatex /usr/share/texlive/texmf-dist/tex/latex/tex-ini-files/xelatex.ini
```

这不是独立安装步骤；具体只读系统路径取决于现有发行版。本次 PDF 即用已有依赖与独立可写缓存编译，未修改系统或扩大权限。格式／缓存不随本科学包交付。

## 完整性与精确复制

```sh
sha256sum -c SHA256SUMS.txt
python3 verify_copies.py
python3 verify_copies.py --sources /path/to/provided-originals
```

第一条核对当前公开文件。第二条检查新科学副本及其映射的内部一致性、Stage02 原 ZIP 及其全部嵌套清单条目；未提供原件时不声称原件比较。第三条才进一步核对精确原件的全部字节区间、全文身份与 inclusive touched-line 注释。脚本只读、不联网，不验证数学。

Stage02 ZIP 是先前交付且本次逐字节不变的归档；不要为了更新旧说明而改写或重压缩。解压其中的 DOT_conditions_stage02/ 可阅读继承证明、原审查科学正文、来源与构建说明。它的旧摘要页数不是本增补 6 页限制的对象。

## 公开集合

公开交付严格限定为 SHA256SUMS.txt 列出的文件加清单自身。隐藏构建目录、独立审计目录、原始管理文件、未接纳诊断、原始容器、运行记录及失败快照均不属于交付。只按这个清单制作外层归档，不要递归加入整个工作目录。

对任何公开文件的后续修改都会改变冻结身份，必须更新相应映射／清单并重新核查；数学改动不能沿用旧原版本的独立审查作为新版本接纳。
