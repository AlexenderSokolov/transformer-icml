# Transformer 预测：统计、资源、精度与源轨迹扰动

## 有限学习实验：失败的冒烟测试与受监督读出校准（2026-11-03）

[位置池化冒烟报告](v10_research/learned_position_pilot_20261103/REPORT.md)与[独立审阅后的解释修正](v10_research/learned_position_pilot_20261103/REPORT_REVIEW_AMENDMENT.md)：一个初始化、每种条件 200 次更新没有显示有用的位置保护。有限 CE 攻击合法但不是整个编辑球的最坏攻击；不同模型可能选择不同污染词，近均匀随机对照和消融也不能支持孤立因果结论。

[固定半程读出校准](v10_research/readout_conditioning_calibration_20261103/REPORT.md)与[审计补充](v10_research/readout_conditioning_calibration_20261103/REPORT_AUDIT_ADDENDUM.md)：明确提供 Q 教师和位置特征后，计数缩放版本通过有限平均/四个训练碰撞词的拟合筛选，等价的归一化参数化在相同 Adam 预算下没有通过。但验证集仍有 0.401–0.434 的最大个体误差；三次初始化共用数据和批次，训练/验证样本也存在相同词重合。

这两项是有完整失败记录、逐样本数据与独立 LLM 审计的探索实验，不是新定理、自然学得鲁棒性或一致逼近保证。此前的 55 页稿件与理论阶段不变。[公开范围](provenance/empirical_position_20261103/PUBLICATION_SCOPE_AND_CHECKS.json) · [隔离复现步骤](provenance/empirical_position_20261103/PUBLIC_REPLAY.md) · [仅省略重复重跑与缓存](provenance/empirical_position_20261103/OMISSIONS_AND_REPLAY.json)。

## 后续研究：干净目标与位置鲁棒性（2026-11-03）

[中文阶段总结](v10_research/learning_objective_stage_20261103/RESEARCH_SUMMARY.zh.md)：CTO001 区分精确干净总体最优与近似最优的鲁棒行为；PGT001 分析给定位置特征后的单偏置精确总体下降；PBF001 给出保留鲁棒性的偏置窗口与投影更新。另有 [14 万条轨迹的固定先验诊断](v10_research/clean_objective_experiment_20261103/REPORT.md)及[科学图](v10_research/clean_objective_experiment_20261103/synthetic_clean_objective.png)。

这不是学习注意力、一般 SGD、有限精度训练或最坏情形实验验证，也不是新的一般统计原理。它是独立于下方固定 55 页稿件的后续研究，未改动该 PDF。完整证明、审阅、代码、CSV、真实修订与失败记录均按[精确来源清单](provenance/learning_objective_20261103/SOURCE_EXPORT_MAP.json)公开。

## 完整整合稿：55 页正文、证明与文献（2026-11-03）

[阅读完整英文 PDF](v10_research/positional_manuscript_consolidated_20261103/main.pdf)：12 页主文、41 页完整证明附录和 2 页参考文献。它把位置观察的未知预算适应代价、近似门控、有限注意力实现及固定统计库精度界整合为一篇匿名研究草稿，不是投稿或新颖性认证。此前 BCJ 的有限统计库结果明确署明来源；同信息流式计数器仍是更强的计算基线。

- [可编辑 TeX、Bib 与复现说明](v10_research/positional_manuscript_consolidated_20261103/README.md) · [逐项结论来源](v10_research/positional_manuscript_consolidated_20261103/CLAIM_TO_SOURCE.md)
- [已有结果的时间顺序与接口协调](v10_research/central_prior_art_20261103/INTERNAL_ANTECEDENT_RECONCILIATION.md) · [中心文献核查及边界](v10_research/central_prior_art_20261103/ATTENTION_PRECISION_AUDIT.md)
- [本次公开文件与核验范围](provenance/consolidated_manuscript_20261103/PUBLICATION_SCOPE_AND_CHECKS.json)

## 新阶段：有限位置注意力与统计库精度（2026-11-03）

已接纳 CCH001、ACG001、FPA001 和 PBP001：近似位置统计不必精确恢复门控位；明确计费的有限注意力程序实现该接口；固定十二坐标舍入统计库的干净风险为 Θ(max{M⁻¹ᐟ²,2⁻ʰ})。这不是所有编码器、整网精度或训练性能的下界，也不宣称优于拥有同样信息的流式计数器。

- [中文综述与四项证明](v10_research/positional_attention_stage_20261103/RESEARCH_SUMMARY.zh.md)
- [最终六项测试版本的复现入口](v10_research/finite_positional_attention_20261103/ROOT_REPRODUCTION_NOTES.md)
- [冻结清单](v10_research/positional_attention_stage_20261103/STAGE_SCIENCE_FREEZE.json) · [公开身份与核验边界](provenance/positional_attention_20261103/PUBLICATION_SCOPE_AND_CHECKS.json)

## 新阶段：信道模型不确定性（2026-11-03）

已接纳 UMC001、UWC001、CAF001 和 CMF001，研究真实信道未知时的可辨识边界、完整消息编码、模型误差精度与通信长度，以及接近不可辨识边界的成本。名义信道固定，补充消息与全消息实验分别计费；二阶结论保留指定临界全状态条件。

- [本阶段中文综述及四个证明入口](v10_research/channel_uncertainty_stage_20261103/RESEARCH_SUMMARY.zh.md)
- [方法来源与实际阅读范围](v10_research/channel_uncertainty_stage_20261103/METHOD_ANTECEDENTS.md)
- [冻结清单](v10_research/channel_uncertainty_stage_20261103/STAGE_SCIENCE_FREEZE.json) · [公开导出与核验边界](provenance/channel_uncertainty_20261103/PUBLICATION_SCOPE_AND_CHECKS.json)

## 最新进展：2026-11-03

新增阶段区分“免费精确计数下的补充消息”与“全部信息均须付费的完整预测消息”。六个已接纳研究目录给出固定信道的长度分类、全消息通信成本、明确计费的编码构造，并在给定临界全状态条件下迁回二阶预测；不声称一般无混合二阶结论、新纠错码、训练可达性或新颖性认证。

- [最新中文综述、完整证明与审查入口](v10_research/resumption_20261103/RESEARCH_SUMMARY.zh.md)
- [完整有限时域稿：新重建 31 页 PDF](v10_research/resumption_20261103/rebuilt_documents/positional_manuscript_finite_20261102/main.pdf) · [恢复的 LaTeX 源码](v10_research/resumption_20261103/recovered_science/positional_manuscript_finite_20261102/main.tex)
- [综合稿：新重建 6 页 PDF](v10_research/resumption_20261103/rebuilt_documents/richer_count_consolidation_20261102/main.pdf)
- [有限文献核查与新颖性边界](v10_research/resumption_20261103/reliability_prior_art/AUDIT.md)
- [恢复范围与来源缺口](provenance/resumption_20261103/RECOVERY_AND_SOURCE_RESOLUTION.json) · [公开导出编辑映射](provenance/resumption_20261103/PUBLIC_EXPORT_RECONCILIATION.json)

两份 PDF 是从恢复源码新编译的输出，不是找回的旧 PDF 二进制。完整集成证明可读，不等于旧独立笔记、历史诊断和原来源审计已全部恢复。下文保留此前各阶段的原有条件与历史记录。

这项研究讨论未知二阶随机过程的下一符号概率预测：历史长度、可见信息、网络结构、内部精度、计算成本与扰动，分别怎样限制可达风险。仓库保留完整证明、审查、诊断、真实失败与修订记录；不同模型的结论不互相替代。

**科学状态截至 2026-11-02。** 第八阶段有六个冻结单元，之后另有二十一项已审查接纳的研究更新（首次四项，第二次七项，第三次十项）。这里的“接纳”是项目内证据状态，不是期刊录用、形式证明或外部同行评审。

第三次增量截至 2026-11-02 14:39 UTC：二元完整历史的给定 beta、未知 k 适应已有精确公开域分类；在 beta ≥ c/M，同一个不读取 k 或 beta 的平衡门控规则覆盖任意初始化及全部预算。全局直方图加短首尾窗口仍可能不足，四个前半段行计数则提供一个充分构造。没有声称这些计数数量最少或首尾窗口阈值尖锐。

## 从这里开始

| 阅读目的 | 入口 |
|---|---|
| 最新适应阶段综述 | [English](v10_research/adaptation_stage_synthesis/positional_counts_adaptation.md) · [中文](v10_research/adaptation_stage_synthesis/research_summary_zh.md) |
| 先了解结论、条件和未解项 | [当前状态与分析](docs/STATUS.md) |
| 看方法、失败、修订及阶段决定 | [按日期整理的研究日志](docs/RESEARCH_LOG.md) |
| 找证明、完整审查、诊断和历版文稿 | [资料导航](docs/NAVIGATION.md) |
| 第八阶段源轨迹扰动：英文 27 页 | [PDF](v10_research/source_corruption_manuscript/corrupted_trajectories.pdf) · [LaTeX](v10_research/source_corruption_manuscript/corrupted_trajectories.tex) |
| 第八阶段中文说明：9 页，93 个原生可编辑公式 | [DOCX](v10_research/source_corruption_guide/Chinese-stage8-guide.docx) · [PDF](v10_research/source_corruption_guide/Chinese-stage8-guide.pdf) |
| 内部信息切口、精度、深度与可靠性：英文 v5，70 页 | [PDF](v10_research/manuscript_v5/finite_precision_prediction.pdf) · [LaTeX](v10_research/manuscript_v5/finite_precision_prediction.tex) |
| 前期精度与可靠性中文说明 | [第七阶段 DOCX](v10_research/precision_robustness_guide/Chinese-stage7-guide.docx) · [PDF](v10_research/precision_robustness_guide/Chinese-stage7-guide.pdf) |
| 核对原始文件、公开导出与路径对应 | [初次来源映射](provenance/PUBLIC_SOURCE_MAP.json) · [第二次来源映射](provenance/increment2/SOURCE_MAP.json) · [第三次来源映射](provenance/increment3/SOURCE_MAP.json) · [公开校验工具](tools/public_verify.py) · [复现边界与操作](docs/REPRODUCIBILITY.md) |

## 三条主线

1. **统计基准与固定表示。** 全历史预测、固定有限信息接口、正混合与任意初始化分别取证。内部网格、完整计算字长、输出精度以及计算时间不能合并成一个“精度”指标。
2. **深度、编码与可靠性。** 研究固定结构的必要条件，也研究付出全部成本的重新编码构造。IID、一般 Markov 源、固定编码器和可重新设计的编码器有不同结论。
3. **源轨迹扰动及后续联合问题。** 第八阶段研究编码前的符号替换；后续 JP001 与 RE001 把源扰动接到不同的内部噪声接口，后续适应研究区分联合盲、给定 beta、完整历史与固定统计量，并保留尚未闭合的参数域。

## 必须保留的边界

- **BT001 的强内部常数步输运前提仍未证明。** BT002 通过独立的较弱熵输运路线证明二元下界，不依赖那个开放前提。
- **EP001 改变终点编辑权限，不改变预测目标。** 目标仍是原始隐藏轨迹的真实终点条件分布。
- **AB001 排除的是同一个估计器同时不知道 `k` 和 `beta` 的统一适应。** BK002 进一步排除二元模型中给定 `beta` 但对所有 `beta` 一致的全历史未知 `k` 适应；CB005 已解决 `beta ≥ c/M` 的任意初始化正向适应，AF001 给出给定 beta 的完整公开域分类，但不能把其并集选择器说成 beta 盲。AB002 只证明普通 add-one 估计器的对数级失配。
- 独立 LLM 审查、有限诊断与构建复现各有证据范围，均不等于形式验证、外部同行评审、新颖性认证、训练可达性或真实网络运行证明。

原始科学版本不被事后改成“当时已经完成”。历史文件中的候选、待批准或尚未发布措辞，按其写作时点理解；后续状态见带时间与哈希的接纳记录及公开来源映射。原始用户指令、私人运行记录、凭据与无关文件不属于公开研究材料。
