# 精确科学复制说明

这是新增编排说明。8 份科学副本的每个保留片段都是 UTF-8 原字节的逐字节复制；原件没有被修改。原独立 review 是原版本的数学审查，不是复制后新执行的审查。本证书和脚本仅检查完整性。

## 区间约定

COPY_MAP.json 使用零起点、左闭右开字节区间 [start,end)。每个非空源片段的辅助行号为一基、包含首尾的 touched lines：start 为 start 字节所在行，end 为 end−1 字节所在行。因此跨到半行也计入最后一行，单行片段不会出现 start>end。字节区间是复制的主证据。

每份源文件恰被 copied spans 与 omitted_source_spans 分割；每份目标恰被 copied spans 与 editorial_output_spans 分割。省略区间给出原范围和哈希，不把被省略的私有文本再次泄露到映射。新增区间有独立哈希且不伪装为原文。完整原件哈希、目标全文哈希、各片段哈希和拼接正文哈希分别列示。

省略范围仅含原身份／控制／路径来源、历史提交状态、重复管理性总结及不承载论证的运行记录。科学定义、全部局部证明、精确量词、有限数值和独立审查推理保留；有限检查命令／脚本不交付，并明确为历史结果。本包新中文索引／摘要也不是这些原件的逐字译本。

## 映射索引

| 目标科学副本 | 原文件名 | 精确片段数 |
|---|---|---|
| `proofs/S010_complete_proof.md` | `S010_proof_v1.md` | 10 |
| `proofs/S011_complete_proof.md` | `S011_proof_v1.md` | 5 |
| `proofs/S012_complete_proof.md` | `S012_proof_v1.md` | 9 |
| `proofs/S013_complete_proof.md` | `S013_proof_v1.md` | 4 |
| `reviews/S010_mathematical_review.md` | `S010_review_v1.md` | 9 |
| `reviews/S011_mathematical_review.md` | `S011_review_v1.md` | 3 |
| `reviews/S012_mathematical_review.md` | `S012_review_v1.md` | 3 |
| `reviews/S013_mathematical_review.md` | `S013_review_v1.md` | 4 |

共 8 份正文、47 个非空精确片段。另有 1 个 binary_copies 记录，绑定整个先前交付 Stage02 ZIP 的原／目标字节相等。

## 可复核范围

`python3 verify_copies.py` 只验证交付片段／新增区间的内部哈希、区间分割及完整继承 ZIP；不声称读到了原件。

`python3 verify_copies.py --sources /path/to/provided-originals` 递归按原文件名和完整哈希找到原件后，另核全部原字节、全部 touched-line 注释和省略区间哈希。原件未随此科学增补另附；原件模式仅适用于已经持有原始提供材料的读者。没有原件也可完整阅读科学证明及继承闭包。

脚本仅用 Python 标准库，只读本地文件、不联网、不修改文件、不验证数学正确性。清单自身不自包含哈希；其冻结身份由后续交付／审计另行绑定。
