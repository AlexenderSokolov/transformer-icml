# 来源身份与完整科学闭包

## 新增科学原件与复制关系

S 编号均指本条件统计项目，不能与其他项目的同号义务混同。下表绑定完整原件，不是交付删略副本的哈希；每个输出自身哈希及精确区间见 COPY_MAP.json。原件只按名称和 SHA-256 标识，不公开执行目录。

| 原件 | 字节 | SHA-256 | 科学副本 |
|---|---:|---|---|
| `long_history_upper_diagnostic_v1.md` | 28656 | `4a49759bfd8eb75babf695e319b6aafea7ed7ae09085c3339db1684981d9a4e8` | `proofs/S020_complete_proof.md` |
| `S020_mathematical_review_v1.md` | 25661 | `9630c56b9f8bf0eb74695a4c8d48555893ff99a8d7640e6bc652a0aac0655864` | `reviews/S020_mathematical_review.md` |
| `long_history_lower_diagnostic_v2.md` | 27867 | `879532785c8a195ef84263ab90e327bb50fc8e9c20315f269274070b24625fa2` | `proofs/S021_complete_proof_v2.md` |
| `S021_mathematical_review_v1.md` | 23236 | `46b519432b13ba9e30f0164cb5e1c946515345bce45117c65833de803c65f0f4` | `reviews/S021_mathematical_review_v1_science.md` |
| `S021_mathematical_review_v2.md` | 10550 | `023a5e1d3ee2ac2552e68fd151e3eafc90e17bc4fba9ddca4934be571c734ee4` | `reviews/S021_mathematical_review_v2.md` |
| `beta_blind_endpoint_diagnostic_v1.md` | 23547 | `d11ee159300e8eae610570683d8c7bb38579020b28f48243805dba5c9120947d` | `proofs/S022_complete_proof.md` |
| `S022_mathematical_review_v1.md` | 19101 | `1beffd77ad9a0a5386e8f438fce4f9fd8d9c7731d111ce6ea45630d0da0c9ad5` | `reviews/S022_mathematical_review.md` |

只接纳 S020 v1、S021 v2、S022 v1；S021 v1 科学审查为未通过的历史判断，因其完整五单元推理构成 v2 复核的必要前件而保留。原 v1 证明身份为 `d0f410dab67d21e29aebdf65c4ac52454616fd0e1e59301ead0a309a9c6ebe21`；只附其合法反例及科学审查，不附原始失败档案。v2 未追认 v1。

## 一个逐字节不变的既有科学归档

上一阶段 v2 科学 ZIP 大小 1,460,410 字节，SHA-256 `cc8b3cf77d799e65d5cafd51d4738262c76a8c58756ffcf5b968d6a65ff1a188`。它不是全项目备份。三项新结果的直接依赖跨越多层，又通过 S018、S016、S011 和 S003 等回连早期接口；保留一个已有归档避免重组并重复认证这些来源。外层只加入本阶段科学内容，不为小改再次复制完整项目。

解包后逐层读取各自 SOURCES.md、COPY_MAP.json、COPY_CERTIFICATE.md、proofs/ 与 reviews/。箭头表示打开相应 ZIP，再在其内寻找后续路径，不表示某个实际电脑路径。

| 归档链 | 字节 | SHA-256 | 本层成员数 |
|---|---:|---|---:|
| `inherited/DOT_conditions_phase_review_20261028_v2.zip` | 1460410 | `cc8b3cf77d799e65d5cafd51d4738262c76a8c58756ffcf5b968d6a65ff1a188` | 19 |
| `inherited/DOT_conditions_phase_review_20261028_v2.zip → DOT_conditions_phase_review_20261028/inherited/DOT_conditions_stage04_20261028.zip` | 1069825 | `a5f96b4987dfdaccf0c2a98d89f575b81a5ef9267ad3f7a8f9fd27254de6a1a1` | 15 |
| `inherited/DOT_conditions_phase_review_20261028_v2.zip → DOT_conditions_phase_review_20261028/inherited/DOT_conditions_stage04_20261028.zip → DOT_conditions_stage04/inherited/DOT_conditions_stage03_20261028.zip` | 793953 | `d5c85ed930cb1711960993799a1a6fbecd84b96e041db23eae7411c2d608b2fd` | 19 |
| `inherited/DOT_conditions_phase_review_20261028_v2.zip → DOT_conditions_phase_review_20261028/inherited/DOT_conditions_stage04_20261028.zip → DOT_conditions_stage04/inherited/DOT_conditions_stage03_20261028.zip → DOT_conditions_stage03/inherited/DOT_conditions_stage02_20261028.zip` | 456828 | `3f6a415201271c30224c5bef8759d80dd8570168b8a20e555f500178e2ce8c50` | 34 |

## 必要直接科学接口的精确副本身份

这里 SHA-256 是已交付科学副本的身份，不与其上游完整原件／原包哈希混用。每层 COPY_MAP 继续提供上游原件身份和复制区间。相应历史独立审查位于同层 reviews/；本阶段审查不是重新认证全部前代材料。

| 直接科学正文 | 字节 | SHA-256 |
|---|---:|---|
| `DOT_conditions_stage02/inherited/L1MAX_statistical_proof.md` | 15130 | `b430fe3d176ecefc00ac575670ea13ffc5d5799f9e232a10375333a0547f44e4` |
| `DOT_conditions_stage02/inherited/GU_UC_and_IID_interfaces.md` | 5188 | `f4abb8e565d58c5af9f6f52ca1e83fc78989dfeb70554e4d22ad1fab8308d275` |
| `DOT_conditions_stage02/inherited/MM5_statistical_proof.md` | 21262 | `4d5e865ebe00846662cef1830be02bf52cc2b839eca8a0600f8baa501ada6078` |
| `DOT_conditions_stage02/proofs/S001_stationary_upper.md` | 16004 | `7fa8b2119f84d9f382da80516aa8b3c277ebd2c4587dffd58d24bf16b11a77d4` |
| `DOT_conditions_stage02/proofs/S003_initialization_transition.md` | 18715 | `5ab2b390ab2d40b238932d658cd1986381bafe9514ba5fa9d25f1d3f18507759` |
| `DOT_conditions_stage02/proofs/S005_iid_algorithm_separation.md` | 19549 | `54071248416106afcc8f51734bc8ed019135ec2502e02d6e49fd09a45e6065e6` |
| `DOT_conditions_stage02/proofs/S006_near_iid_and_two_step.md` | 28893 | `17644d47e3b899d141c61251858aebbc1b64848306d77b0a210179b1472a2b30` |
| `DOT_conditions_stage03/proofs/S011_complete_proof.md` | 30903 | `8286e13dabe19b4b7adc72ab11bc65a5a8594f70c507c6321bc398f46860c762` |
| `DOT_conditions_stage03/proofs/S012_complete_proof.md` | 43629 | `7021dea45b1a262cd6ff71caee4cd8a1f7a973828313100d3d6ad5acbfe09132` |
| `DOT_conditions_stage04/proofs/S015_complete_proof.md` | 48577 | `452f4274a9b47635a4d3d7995db09f222b10d024cef935b9b1f5370ebad9db69` |
| `DOT_conditions_phase_review_20261028/proofs/S016_complete_proof.md` | 23244 | `bfb6ab6e9bd403d4a8502da6474b51f8b31940189dad339cfa5dac1b5ecbf645` |
| `DOT_conditions_phase_review_20261028/proofs/S018_complete_proof.md` | 33339 | `0bd13ecdc9d33df0cd56a5367885fa6779ce6fcabf16caf59ecbf9ed8e7b4d46` |
| `DOT_conditions_phase_review_20261028/proofs/S019_complete_proof.md` | 15887 | `7cf5eb6a408109d534bc1537a7123b90201795d5b6450832b2649ccba739905b` |

定位：S016/S018/S019 在上一阶段 v2 外层；S015 在其中 Stage04；S011/S012 在 Stage03；S001/S003/S005/S006、L1MAX、GU、MM5 在 Stage02。所有层均在上述唯一归档内，不要求访问旧机器或私有目录。

## 新结果实际使用的范围

- S020 直接使用 L1MAX 的有限原行栈及精确最大尾界、GU 的 first-w 计数机制、S001 平稳末行占用、S018 完整两步分裂与无条件 good-event 桥。S011、S016、S019 用于准确旧证书／下包络比较及已明确重证的标量求和，不越域继承匹配定理。
- S021 的新模板 Lemmas A/B 和 Theorem C 自足陈述并证明；S015/S012 支撑精确固定源族、初始化、完整历史乘积实验和已有 lower；S016 只是全类窗口比较。MM5 是已有 lower 谱系而非模板定理新黑箱。
- S022 使用 L1MAX 一般原规则上界、S005 全状态 IID 等价与 pooling／IID lower、S003 经 MM5 的一般 lower 解释。S006 只保留 near-IID 与任意初始化边界，不能当任意初始化匹配上界；S020 不是端点定理的数学前提。

## 审查及来源口径

S020 与 S022 各有一次完整独立上下文 LLM 数学审查。S021 是完整 v1 五单元审查指出真实 R1，随后有界 v2 差异复核修复 R1/N1并继承其余逐字节未改材料。所有历史作者／审查的有限检查叙述保留其原证据性质，本次未重跑数学枚举。公开 verify_copies.py 只检查本地字节，不等于数学审查。

既有归档中的阶段终止措辞均属 2026-10-28 历史状态；本轮 2026-10-29 的 A/B 目标仍接续。原科学字节和源身份不改写。无外部论文作为本阶段新证明黑箱，无论文全文新增。
