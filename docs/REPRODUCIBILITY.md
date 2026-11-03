# 公开版本的来源、校验与复现

## 未知信道阶段的核验范围

本阶段冻结 45 个源文件，包括四个接纳目录、中文综述、方法来源与 freeze 清单。数学正文、诊断代码、已有输出和真实修订记录保持原字节。仅一行审查署名作非数学规范化，原始与公开哈希见[精确协调表](../provenance/channel_uncertainty_20261103/PUBLIC_EXPORT_RECONCILIATION.json)。历史接纳记录继续绑定原始身份，新 inventory 绑定公开字节。

五个有限诊断脚本应在隔离副本中运行，避免覆盖冻结输出；本次发布准备只作身份检查和语法解析，没有重跑数学诊断。此前历史文件缺失及新重建 PDF 的边界继续有效，详见[本阶段核验说明](../provenance/channel_uncertainty_20261103/PUBLICATION_SCOPE_AND_CHECKS.json)。

## 2026-11-03 恢复与公开校验边界

本次恢复了可读的科学文本和完整集成证明，但并未恢复全部旧历史闭包。31 页稿和 6 页稿是新构建 PDF，不是原 PDF 字节恢复。新审计位于 [RECOVERY_AND_SOURCE_RESOLUTION.json](../provenance/resumption_20261103/RECOVERY_AND_SOURCE_RESOLUTION.json)，不冒充未恢复的旧来源审计。

数学正文、LaTeX、诊断代码及其已有输出保持原字节；少量审查和元数据去除了内部路由称谓、临时目录及私有操作细节，确切原始/导出哈希对应见 [PUBLIC_EXPORT_RECONCILIATION.json](../provenance/resumption_20261103/PUBLIC_EXPORT_RECONCILIATION.json)。要求原审查哈希的历史校验器，不被宣称能对改写后的公开副本原样通过。新的 active inventory 校验公开字节和成员身份，不是数学重证明。历史有限重跑按各自 receipt 的实际记录理解。

## 本次发布的边界

本仓库不是原始运行环境的镜像。原阶段包的科学闭包已展开为普通文件，原始用户委托、私人运行记录、路由标识、凭据、递归压缩包和可再生成的排版缓存不公开。必要的科学证明、完整审查、诊断、真实数学失败及留存修订继续可读。

`provenance/PUBLIC_SOURCE_MAP.json` 给出每个导入文件的输入字节哈希、原阶段源记录、公开字节哈希及逐行非数学编辑。编辑记录只给原行哈希与公开行，不泄露删除的私人值。`provenance/PUBLIC_EXCLUSIONS.json` 列出被排除文件的身份与原因。路径变化，尤其早期统计来源从递归归档展开到 `inherited_statistics/`，有明确映射。

## 严格检查公开文件

需要 Python 3，无需网络或凭据。在仓库根运行：

```bash
python tools/public_verify.py
python -m unittest discover -s tests -v
```

校验器检查完整成员集合、字节数和 SHA-256，拒绝缺失、未声明新增、符号链接、路径越界和字节篡改。仅 Git 自身目录及 Python 缓存被忽略；清单不包含自己的哈希，避免自引用。七项回归测试覆盖正常情况与六种拒绝条件。该校验不是数学证明，也不是对所有旧诊断脚本的重跑。

## 科学诊断与旧绑定

各主题目录保留原诊断脚本及当时输出。脚本常会写出新 JSON；请在独立副本内运行，不要覆盖历史证据。例如：

```bash
python v10_research/joint_corruption_precision/JP001_diagnostics.py
python v10_research/robust_encoded_source_corruption/RE001_diagnostics.py
python v10_research/binary_budget_adaptation/check_ab001.py
```

具体依赖以脚本为准；部分较早诊断需要 NumPy 或 SciPy。这些有限检查仅支持其明示实例，不代替普遍论证。RE001 的主诊断使用精确有理比较，辅助二元根式脚本包含浮点容差，不应把所有辅助检查都称为精确认证。

历史绑定中的哈希指当时实际读取的源文件，不应自动改成当前公开字节。若某个旧绑定校验器引用已排除的私人行政文件，或要求原审查元数据，它在公开目录里可能拒绝运行；这不表示科学定理失败，也不能用全局哈希忽略或虚构缺失文件解决。请通过公开来源映射检查已公开对象；原包的精确逐指针协调记录作为历史证据保留。

`provenance/stage8/` 中的包校验器、重放器和构建器属于原归档结构的历史来源，**不能直接当作当前展开仓库的入口**。原嵌套 ZIP 与私人委托没有公开，因此本仓库不声称可从公开文件逐字节重建完整原始归档。原始归档的身份是 SHA-256 `89d434c7b0d9fe81d6e3b2f47cb64ac6c019b8a3abdd8678910f2a814e451e38`，27,369,241 字节。

## 文稿

英文稿保留 LaTeX、BibTeX 与 `build.sh`，需要 `pdflatex` 和 `bibtex`。中文稿保留 Markdown 数学源、Pandoc／python-docx 构建器及原生 OMML DOCX；转 PDF 需要 LibreOffice 与相应字体。旧环境专用的渲染辅助程序不是科学前提，请使用可用的本地 DOCX 渲染工具。历史文稿验证器也可能读取原始行政绑定，运行前须区分数学排版构建与旧归档身份验证。

## 历史证据与本次实际检查

第八阶段历史记录中的 91 个当前脚本、1 个预期历史失败、913,221 个精确／认证有理案例和 36 页重建一致性，只归属于那些记录的实际运行。初次发布的检查范围见 `provenance/PUBLICATION_RECEIPT.json`；2026-11-03 的当前检查边界见[新审计](../provenance/resumption_20261103/PRIVACY_AND_CHECKS.json)。不把继承的历史结果冒充一次新运行。独立 LLM 审查不等于形式验证、外部同行评审或新颖性认证。

## 第二次增量的精确边界

第二次增量有独立[来源映射](../provenance/increment2/SOURCE_MAP.json)、[来源闭合审计](../provenance/increment2/SOURCE_CLOSURE_AUDIT.json)与[严格哈希协调表](../provenance/increment2/BINDING_RECONCILIATION.json)。原始期望哈希没有被全局改写；只有在准确路径的当前公开字节先通过其公开哈希后，才可承认表内原始身份。未列出的差异必须失败。历史脚本可能写诊断或绑定记录，应在一次性副本中运行。本次增量没有重跑这些科学程序；当前 CI 仅核验文件字节、集合和校验器回归测试。

## 第三次增量与历史路径恢复

第三次增量的[精确来源映射](../provenance/increment3/SOURCE_MAP.json)和[严格协调表](../provenance/increment3/BINDING_RECONCILIATION.json)已恢复。原闭合审计文件未恢复，当前边界与可读来源见[新的恢复审计](../provenance/resumption_20261103/RECOVERY_AND_SOURCE_RESOLUTION.json)；不能把新审计称作旧文件的逐字节恢复。三个旧绑定只在精确的记录所有者、原路径与原哈希同时匹配时，解析到真实保留的旧文件；不是跳过哈希或任意寻找近似内容。公开字节必须先匹配其声明哈希，才能识别相应原始身份。

历史 SyntaxError 文件和失败诊断必须保留，但不属于当前通过的程序清单。只读 CI 仍然仅执行 `tools/public_verify.py` 与七个回归测试；它不执行历史科学脚本、不形式化证明定理，也不声称重建文稿。
