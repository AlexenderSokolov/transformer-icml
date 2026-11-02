# 精确科学复制说明

这是新增编排说明。四份科学副本来自两个已接纳工作单元。它们的完整数学定义、18 个局部证明及对应完整逐引理审查推理保留；旧原件未修改。原独立审查不是复制后新执行的审查，本证书与脚本只检查字节和来源。

## 区间与删略规则

COPY_MAP.json 使用 UTF-8 零起点左闭右开字节区间 [start,end)。所有非空源区间的辅助行号是一基 inclusive touched lines，最后一行由 end−1 字节计算，半行也计入。字节区间是主要依据。

每个原件由保留 spans 与 omitted_source_spans 完整无重叠分割；每个目标由保留 spans 与 editorial_output_spans 完整无重叠分割。删略区间只公开范围／哈希，不泄露私有删略文字。完整原件、目标、各片段、拼接复制正文及新增区间各有独立哈希。新标题、时序说明、符号说明及分隔符均诚实标为非原文。

删略包含身份、私有路径和控制来源、原提交时状态、重复结果摘要、已在正文完整陈述的管理性目标描述、原读／写范围记录及纯来源核对项；不删除承重数学、参数限制、量词、数值检查事实或科学依赖。必要原科学术语 Euler clock / star clock 保留。原检查命令／脚本不在本包，检查事实是历史结果而非本次重新运算。S014 的原历史开放语句由明确的新编排时序注解释，不静默改写成 S015 的新结论。

## 映射索引

| 目标副本 | 原文件名 | 非空复制片段数 |
|---|---|---|
| `proofs/S014_complete_proof.md` | `S014_proof_v1.md` | 7 |
| `reviews/S014_mathematical_review.md` | `S014_review_v1.md` | 5 |
| `proofs/S015_complete_proof.md` | `S015_proof_v1.md` | 10 |
| `reviews/S015_mathematical_review.md` | `S015_review_v1.md` | 4 |

共 4 份科学正文、26 个精确片段，另有 1 个 binary_copies 记录绑定完整 Stage03 历史 ZIP；其内层 Stage02 ZIP 不变。

## 可复核范围

`python3 verify_copies.py` 检查交付片段、新增区间、完整分割、公开清单，以及 Stage03 和嵌套 Stage02 的全部文件哈希、CRC 与集合。没有原件时只声称交付内部一致性。

`python3 verify_copies.py --sources /path/to/provided-originals` 按文件名与完整哈希找到持有的原件后，另核每个源片段／目标字节相等、全部 touched-line 注释与删略区间哈希。原管理性全文不随公开包另附；没有它们也能完整阅读科学证明和依赖闭包。

脚本使用 Python 标准库，只读本地、不联网、不写文件、不验证数学。公开范围严格是 SHA256SUMS.txt 的条目加清单自身；清单不自包含自己的哈希，冻结身份由后续审计／交付绑定。隐藏构建目录、原件、运行记录和历史失败快照不随包公开。
