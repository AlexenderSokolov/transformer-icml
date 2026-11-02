# 导读重建与完整性检查

可编辑中文导读使用 XeLaTeX、Noto Serif CJK SC / Noto Sans CJK SC 及标准 TeX Live 包。保持源文件名后，在具备相同字体环境的临时工作目录执行：

```sh
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error guide_中文.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error guide_中文.tex
```

生成 PDF 后需逐页渲染检查字体、溢出、页码及公式；成功编译并不等于版面已检查。最终 PDF 为六页。PDF 时间戳和不同 TeX 字体环境可改变二进制哈希；SHA256SUMS 对交付的固定字节负责，不承诺跨环境位级可复现。

```sh
python3 verify_package.py
python3 verify_package.py --source-dir /path/to/frozen/resume_inputs
```

默认检查全部文件清单、公开复制的区间与哈希、每个区间覆盖、诊断与唯一继承档案的精确复制、索引中的嵌套来源。可选 `--source-dir` 对本次十个冻结原输入验证复制/省略区间及源身份。原输入不在科学载荷内，省略内容的原字节不能仅从公开包反推；不把默认检查称为已验证未提供源。

SHA256SUMS 覆盖除其自身外的全部公开文件。清单不自哈希；外层 ZIP 哈希在独立交付记录给出。此工具只做内容完整性检查，不是数学证明器或独立科学审查。
