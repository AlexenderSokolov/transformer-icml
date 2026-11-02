# 当前状态：第二次研究增量的七个已接纳单元

本增量只包含 AB003、JB001、BK001、BK002、KA001、CB001、CB002，以及另行采纳的 BK002 十六个矩阵位置枚举说明。它们均为阶段八冻结之后的研究更新，不加入原阶段八的六单元冻结集合。候选标题与旧开放问题按原写作时点保留；后续状态以带时间和精确哈希的接纳记录为准。

| 单元 | 已建立的结论 | 不可扩张的边界 |
|---|---|---|
| AB003 | 二元全历史实验中，一个不知道 k 和 beta 的硬阈值估计器，在 k 不超过平方根量级的公开预算范围内达到已知 k 的风险阶；上界适用于任意初始分布。 | 不是每个更大 k 上的逐点不可能性。 |
| JB001 | 固定二元八坐标均匀直方图有限切口中，不知道 k、delta、beta 的阈值解码器，在 k/M + delta + 1/Q ≤ M^(-1/2) 时达到相应已知预算阶。 | 固定编码器、向量端口噪声、小总扰动域；不是全预算或任意重新设计编码器的结果。 |
| BK001 | 在给定 beta = 1/M 时，只看八个三元计数以及首末符号对的预测器，不能同时对所有未知实际 k 达到已知 k 的风险阶。 | 这是受限统计量的结论，不是完整有序历史的不可能性。 |
| BK002 | 即使提供 beta 和完整污染历史，也不存在对所有 beta、所有未知实际预算统一达到已知 k 风险阶的规则。结合 AB003，公开预算区间 0 ≤ k ≤ b_M 上的统一适应可行，当且仅当 b_M = O(sqrt(M))。 | 下界已在平稳初始分布成立，上界适用于所有初始分布；常数可依赖固定的公开区间包络。不是每个较大 k 的逐点不可能性，不排除固定正 beta 下依赖 beta 的常数，也不解决预先指定 beta = 1/M 曲线上的全历史问题。 |
| KA001 | 给定 beta 的全历史未知预算适应具有部分相图：beta ≤ C/M² 可行；M beta → 0 且 M² beta → ∞ 的指定中间曲线不可行；beta ≥ c/sqrt(M) 可行。 | C、c 固定，正向常数可依赖它们。beta 约为 1/M 及其至 M^(-1/2) 之间的剩余区间未由本单元解决。 |
| CB001 | 精确长游程否决规则在任意初始分布下具有受控的干净风险增量，并可阻断明确列出的 BK001/BK002 攻击支持。 | 仅为部分引理，不控制任意污染风险，也不证明完整适应。 |
| CB002 | 对任意基线加入近前缀否决，在任意严格 Hamming-k 污染下只增加受控风险；beta = 1/M 时增量不超过 min(1, 2^11/sqrt(M) + 2^9 k/M)。 | 基线本身的风险仍然存在；这是风险增量定理，不是全预算适应定理。 |

## BK002 枚举说明

原证明与原独立审查中的矩阵、参数、证书不等式、常数和风险结论保持原字节。另行采纳的说明补充明确列出位置 (00,10)，其矩阵元素 a e 与已处理的 e a 相同，目标同为 delta² x；正确的位置数是 2+1+3+1+2+3+4 = 16。旧审查写出的和实际等于 15。旧诊断程序本已遍历全部十六个位置。该说明纠正文字枚举和加法，不是新的定理、矩阵变更、参数域扩大或风险阶修正。

## 真实历史与仍未解决的问题

- BK001 的端点界改写保留准确差分。旧版本并非当时备份，而是由有记录的单段替换反向重建；不能把它说成同时保存的历史快照。
- BK002 的参考采样器证明没有在审查中改写。可选的真实干净续接采样器、同 beta 路线障碍和宏循环探索仍明确标注为未独立接纳的历史研究，不作已接纳前提。
- CB001 保留一般 L 界及 L = floor(M/2) 特化的真实澄清差分。CB002 没有证明基线在否决区域以外的风险。
- 仅就本次固定增量，预先指定 beta 约为 1/M 曲线上的全历史未知 k 适应仍未解决。KH001、KH002、CB003 等后续单元不在本次发布范围，不能用它们改写本次结论。

独立 LLM 审查和有限精确诊断不等于形式化验证、外部同行评审或新颖性认证。本次隐私与来源审计没有重新运行全部科学诊断。

## 证明、完整审查和接纳记录

| 单元 | 证明 | 完整审查 | 接纳时间（UTC）与记录 |
|---|---|---|---|
| AB003 | [证明](../v10_research/binary_budget_adaptation/AB003_small_budget_hard_threshold.md) | [审查](../v10_research/binary_budget_adaptation/review_ab003_full.md) | [2026-11-02T12:11:01.832759+00:00](../v10_research/intake/AB003_acceptance.json) |
| JB001 | [证明](../v10_research/joint_blind_finite_cut/JB001_theorem.md) | [审查](../v10_research/joint_blind_finite_cut/JB001_independent_review.md) | [2026-11-02T12:23:28.851337+00:00](../v10_research/intake/JB001_acceptance.json) |
| BK001 | [证明](../v10_research/binary_beta_known_adaptation/BK001_histogram_adaptation_obstruction.md) | [审查](../v10_research/binary_beta_known_adaptation/BK001_independent_full_review.md) | [2026-11-02T12:32:29.954083+00:00](../v10_research/intake/BK001_acceptance.json) |
| BK002 | [证明](../v10_research/binary_beta_known_adaptation/BK002_full_history_supplied_beta_obstruction.md) | [审查](../v10_research/reviews/BK002_independent_full_review.md) | [2026-11-02T12:56:33.419419+00:00](../v10_research/intake/BK002_acceptance.json) |
| KA001 | [证明](../v10_research/binary_certificate_adaptation_phase/KA001_certificate_phase_partial.md) | [审查](../v10_research/reviews/KA001_independent_full_review.md) | [2026-11-02T13:20:27.137673+00:00](../v10_research/intake/KA001_acceptance.json) |
| CB001 | [证明](../v10_research/critical_beta_adaptation/CB001_long_run_veto_partial.md) | [审查](../v10_research/critical_beta_adaptation/CB001_independent_full_review.md) | [2026-11-02T13:22:25.063063+00:00](../v10_research/intake/CB001_acceptance.json) |
| CB002 | [证明](../v10_research/critical_beta_adaptation/CB002_near_prefix_veto_partial.md) | [审查](../v10_research/critical_beta_adaptation/CB002_independent_full_review.md) | [2026-11-02T13:32:31.964358+00:00](../v10_research/intake/CB002_acceptance.json) |

BK002 的[枚举说明](../v10_research/binary_beta_known_adaptation/BK002_ALL16_ENUMERATION_CLARIFICATION.md)与[另行采纳记录](../v10_research/intake/BK002_all16_clarification_adoption.json)须与原证明、原审查同时阅读。

## 原有主线与历史状态

[初次完整发布的科学状态](STATUS_INITIAL_20261102_115746.md)保留阶段八六个冻结单元和 JP001、RE001、AB001、AB002 的原始时点摘要。其旧开放问题不代表本次新增结果之后的状态。阶段八冻结本身、BT001 的开放强输运前提、BT002 的独立熵路线、EP001 的真实隐藏终点目标均不改变。70 页 v5 精度／深度稿仍见[资料导航](NAVIGATION.md)。

这些适应结论涉及二元模型；不能推广为 K ≥ 3 的预算盲适应障碍。文献阅读范围见[限定的一手文献记录](../v10_research/prior_art/adaptation_and_constrained_risk_screen.md)，不是新颖性认证。
