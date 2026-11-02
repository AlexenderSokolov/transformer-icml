# 编辑 编译与只读核对

可编辑源是 `guide_中文.tex`。当前导读为九页 A4；完整证明与原审查另以 Markdown 提供，不压缩进这九页。

## 已有 TeX 环境

需要 XeLaTeX、Noto Serif CJK SC、Noto Sans CJK SC，以及 geometry、fontspec、amsmath、amssymb、booktabs、tabularx、enumitem、fancyhdr、hyperref。源码使用 XeTeX 的中文换行，不需 xeCJK。只调用已有工具，不安装或改系统。

```sh
mkdir -p ../conditions-guide-build
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=../conditions-guide-build guide_中文.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=../conditions-guide-build guide_中文.tex
```

若已有 TeX Live 但缺少 xelatex 预生成格式，可在自己的可写格式／缓存目录设置 TEXMFVAR、TEXMFCONFIG、TEXMFCACHE、TEXMFHOME、XDG_CACHE_HOME、TEXFORMATS，并用现有 `xetex -ini -etex -no-shell-escape ... xelatex.ini` 生成格式。不需扩大权限或安装软件。本次亦使用独立可写缓存与已有系统只读字体／TeX 文件。具体系统路径随发行版变化，不写进公开源。

每次编辑后重新编译两遍，检查完整日志、页数、字体和提取文本，再用 `pdftoppm -png` 渲染并逐页目视检查。退出成功不代表无排版错误。构建缓存、日志和 PNG 应放在公开包目录之外，不属于科学交付。

## 完整性

```sh
sha256sum -c SHA256SUMS.txt
python3 verify_copies.py
python3 verify_copies.py --sources /path/to/provided-originals
```

前两条检查当前交付内部字节／区间／清单及 Stage04→Stage03→Stage02 所有嵌套清单成员，含安全路径、无重复／symlink 与 CRC。其中 verifier 另要求外层实际普通文件集合恰等于清单条目加清单自身，并拒绝目录树中的所有 symlink，包括悬空链接及文件／目录链接。没有原件时不声称做过原件比较。第三条才对持有的完整原件按文件名和全文哈希定位，核对精确源／目标区间及 inclusive touched-line 注释。脚本仅 Python 标准库、只读本地、不联网，不验证数学。

公开集合严格为 SHA256SUMS.txt 条目加清单自身；只能依清单制作外层 ZIP。不要把原件、日志、构建目录、审计记录、失败快照或整个研究目录递归加入。修改后必须重做来源映射／清单和审查绑定；旧数学接纳不能自动认证改过的新数学。
