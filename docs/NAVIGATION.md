# 资料导航

## 阅读顺序

1. [当前状态](STATUS.md)：明确对象、量词、条件和剩余问题。
2. [研究日志](RESEARCH_LOG.md)：了解为何采用当前路线，以及哪些尝试失败。
3. 两条综合稿主线：内部信息切口的 [英文 v5](../v10_research/manuscript_v5/finite_precision_prediction.pdf) 与源轨迹扰动的 [英文伴随稿](../v10_research/source_corruption_manuscript/corrupted_trajectories.pdf)。
4. 根据下表进入完整证明和审查，最后核对 [接纳记录](../v10_research/intake/) 与 [公开来源映射](../provenance/PUBLIC_SOURCE_MAP.json)。

## 论文与中文说明

| 内容 | 可读成品 | 可编辑来源 |
|---|---|---|
| 精度、深度与可靠性 v5，70 页 | [英文 PDF](../v10_research/manuscript_v5/finite_precision_prediction.pdf) | [LaTeX](../v10_research/manuscript_v5/finite_precision_prediction.tex)、[构建说明](../v10_research/manuscript_v5/README.md) |
| 源轨迹扰动，27 页 | [英文 PDF](../v10_research/source_corruption_manuscript/corrupted_trajectories.pdf) | [主文](../v10_research/source_corruption_manuscript/corrupted_trajectories.tex)、[非二元与终点证明](../v10_research/source_corruption_manuscript/nonbinary_endpoint.tex)、[二元证明](../v10_research/source_corruption_manuscript/binary.tex) |
| 第八阶段中文说明，9 页 | [PDF](../v10_research/source_corruption_guide/Chinese-stage8-guide.pdf) | [DOCX](../v10_research/source_corruption_guide/Chinese-stage8-guide.docx)、[数学源文](../v10_research/source_corruption_guide/guide_math_zh.md) |
| 第七阶段精度与可靠性中文说明 | [PDF](../v10_research/precision_robustness_guide/Chinese-stage7-guide.pdf) | [DOCX](../v10_research/precision_robustness_guide/Chinese-stage7-guide.docx)、[构建说明](../v10_research/precision_robustness_guide/BUILD.md) |
| 深度与初始化中文说明 | [PDF](../v10_research/depth_initialization_guide/Chinese-stage6-guide.pdf) | [DOCX](../v10_research/depth_initialization_guide/Chinese-stage6-guide.docx) |
| 联合前沿中文说明 | [PDF](../v10_research/joint_frontier_guide/Chinese-stage5-guide.pdf) | [DOCX](../v10_research/joint_frontier_guide/Chinese-stage5-guide.docx) |

英文旧稿仍可访问：[v1](../v10_research/manuscript/)、[v2](../v10_research/manuscript_v2/)、[v3](../v10_research/manuscript_v3/)、[v4](../v10_research/manuscript_v4/)。旧稿是历史科学版本，不按新稿状态回写。

## 第八阶段六个冻结单元

| 单元 | 证明目录 | 审查与诊断 |
|---|---|---|
| SC001 | [源符号扰动](../v10_research/source_symbol_corruption/) | 同目录的完整审查、源绑定及诊断；须同时读取主证明和获接纳的平稳扩展 |
| SC002 | [混合依赖扰动](../v10_research/source_symbol_corruption_mixing/) | 同目录完整审查及诊断 |
| SC003 | [二元上界](../v10_research/binary_source_corruption/SC003_theorem.md) | [完整审查](../v10_research/binary_source_corruption/SC003_independent_full_review.md)；同目录精确检查与源绑定 |
| BT001 | [障碍与条件归约](../v10_research/binary_erasure_transport/BT001_obstruction_and_reduction.md) | [完整审查](../v10_research/binary_erasure_transport/BT001_independent_review.md) |
| BT002 | [熵输运下界](../v10_research/binary_erasure_transport/BT002_entropy_bridge_lower.md)、[标量补全](../v10_research/binary_erasure_transport/BT002_scalar_completion.md) | [完整审查](../v10_research/binary_erasure_transport/BT002_independent_review.md)、[真实保留边界](../v10_research/binary_erasure_transport/BT_STAGE8_PROVENANCE.md) |
| EP001 | [终点扰动](../v10_research/terminal_symbol_corruption/) | 同目录完整证明、审查与诊断 |

整体证据：[科学冻结](../v10_research/delivery_stage8/SCIENTIFIC_FREEZE.json)、[新鲜科学审计目录](../v10_research/stage8_science_audit/)、[阶段包审计](../provenance/stage8/PACKAGE_AUDIT.md)。历史包审计中的待批准措辞描述其当时时点；后续接纳／授权记录不把它改写成早已通过。

## 冻结后的更新

| 单元 | 完整材料 | 后续接纳 |
|---|---|---|
| JP001 | [固定直方图联合扰动](../v10_research/joint_corruption_precision/)：证明、完整审查、修订说明、诊断及绑定 | [收据](../v10_research/intake/JP001_acceptance.json) |
| RE001 | [鲁棒重新编码后的源扰动](../v10_research/robust_encoded_source_corruption/)：证明、辅助引理、完整审查、成本修正与诊断 | [收据](../v10_research/intake/RE001_acceptance.json) |
| AB001 | [联合未知 `k`／`beta` 障碍](../v10_research/binary_budget_adaptation/AB001_joint_blindness_obstruction.md) | [收据](../v10_research/intake/AB001_acceptance.json) |
| AB002 | [add-one 反例与给定 `beta` 的开放问题](../v10_research/binary_budget_adaptation/AB002_addone_failure_and_open_beta_known.md) | [收据](../v10_research/intake/AB002_acceptance.json) |

AB001／AB002 的 [共同审查](../v10_research/binary_budget_adaptation/review_joint_blindness_full.md)、独立检查及实际编号变更历史在同一目录。它们不属于第八阶段冻结快照。

## 前期证明的主题入口

- **固定接口和统计桥梁：** [网络桥梁](../v10_research/network_bridge/)、[精度下界](../v10_research/precision_lower/)、[完整前沿](../v10_research/precision_frontier/)、[强混合](../v10_research/strong_mixing_precision/)。
- **注意力与资源：** [有界注意力](../v10_research/bounded_attention/)、[因果有限求值器](../v10_research/causal_attention/)、[权重增长](../v10_research/growing_weight/)、[双资源前沿](../v10_research/two_resource_frontier/)。
- **二元特殊结构：** [平稳前沿](../v10_research/binary_stationary_frontier/)、[任意初始化](../v10_research/binary_arbitrary/)、[合并定理](../v10_research/binary_all_start/)、[方法反例](../v10_research/binary_weighted_coupling/)。
- **深度、容量与可靠性：** [混合依赖深度](../v10_research/mixing_depth/)、[影响揭示下界](../v10_research/influence_reveal/)、[IID 容量](../v10_research/iid_depth_capacity/)、[折叠脆弱性](../v10_research/folded_noise/)、[鲁棒深度](../v10_research/robust_depth_capacity/)、[一般 Markov 构造](../v10_research/robust_markov_prediction/)、[噪声精度前沿](../v10_research/noise_precision_frontier/)。
- **继承的较早科学来源：** [较早研究材料](../v10_intake/source/sources/earlier/)、[前驱事实与完整正文](../v10_intake/source/sources/euler-stage6/)、[返回科学材料](../v10_intake/source/sources/dot-return/) 与 [展开的 S001–S025／R001–R011 统计来源](../inherited_statistics/)。这里仅公开经检查的科学材料，不含原始用户委托或私人运行信息。
- **文献比较：** [定向文献笔记](../v10_research/prior_art/)。阅读范围逐项声明；文献检索不构成新颖性认证。

## 来源与复现

[公开来源映射](../provenance/PUBLIC_SOURCE_MAP.json) 区分原始字节、既有科学导出和本次公开导出，并声明真实路径变化及必要脱敏。科学正文、历史失败和审查结论不能靠重写哈希来“通过”。如某个旧脚本消费原始绑定，应使用明确限定的导出协调记录，而不是全局忽略完整性检查。

[公开校验工具](../tools/public_verify.py) 用于公开目录的完整性检查；具体执行范围和结果看发布记录。文稿各自的 `build.sh` 或构建说明给出依赖。原包的历史嵌套归档结构不等于当前仓库结构；仓库展开必要科学来源，避免递归 ZIP、渲染缓存与重复归档堆积。公开版不声称可从被排除的私人操作信息重建整个原始运行环境。

## 第二次已接纳研究增量

下列七项及 BK002 枚举说明独立于阶段八冻结；[当前条件、边界与完整入口](STATUS.md)。

- **AB003**：[证明](../v10_research/binary_budget_adaptation/AB003_small_budget_hard_threshold.md) · [完整审查](../v10_research/binary_budget_adaptation/review_ab003_full.md) · [接纳记录](../v10_research/intake/AB003_acceptance.json)。
- **JB001**：[证明](../v10_research/joint_blind_finite_cut/JB001_theorem.md) · [完整审查](../v10_research/joint_blind_finite_cut/JB001_independent_review.md) · [接纳记录](../v10_research/intake/JB001_acceptance.json)。
- **BK001**：[证明](../v10_research/binary_beta_known_adaptation/BK001_histogram_adaptation_obstruction.md) · [完整审查](../v10_research/binary_beta_known_adaptation/BK001_independent_full_review.md) · [接纳记录](../v10_research/intake/BK001_acceptance.json)。
- **BK002**：[证明](../v10_research/binary_beta_known_adaptation/BK002_full_history_supplied_beta_obstruction.md) · [完整审查](../v10_research/reviews/BK002_independent_full_review.md) · [接纳记录](../v10_research/intake/BK002_acceptance.json)。
- **KA001**：[证明](../v10_research/binary_certificate_adaptation_phase/KA001_certificate_phase_partial.md) · [完整审查](../v10_research/reviews/KA001_independent_full_review.md) · [接纳记录](../v10_research/intake/KA001_acceptance.json)。
- **CB001**：[证明](../v10_research/critical_beta_adaptation/CB001_long_run_veto_partial.md) · [完整审查](../v10_research/critical_beta_adaptation/CB001_independent_full_review.md) · [接纳记录](../v10_research/intake/CB001_acceptance.json)。
- **CB002**：[证明](../v10_research/critical_beta_adaptation/CB002_near_prefix_veto_partial.md) · [完整审查](../v10_research/critical_beta_adaptation/CB002_independent_full_review.md) · [接纳记录](../v10_research/intake/CB002_acceptance.json)。

精确来源与脱敏差异见[第二次来源映射](../provenance/increment2/SOURCE_MAP.json)，历史预期哈希与公开哈希的严格对照见[绑定协调表](../provenance/increment2/BINDING_RECONCILIATION.json)。
