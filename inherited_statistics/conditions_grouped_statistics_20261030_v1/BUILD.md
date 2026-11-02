# 构建与校验

导读沿用既有项目的 A4、21 mm 页边距、11 pt、Noto Serif/Sans CJK SC 和 XeLaTeX 样式，不改用 DOCX。

```sh
xelatex -interaction=nonstopmode -halt-on-error guide_中文.tex
xelatex -interaction=nonstopmode -halt-on-error guide_中文.tex
python3 verify_package.py
```

需要 XeLaTeX、相应 Noto CJK 字体；校验脚本仅使用 Python 3 标准库。PDF 已逐页渲染并检查全部五页。校验可确认包中身份、公开复制区间和嵌套来源可定位；没有原始冻结输入时，不声称重新验证被省略区间的内容。SHA256SUMS 不包含自身，以免循环自引用；最终 ZIP 身份在包外报告。
