# Transformer 预测：统计、资源、精度与源轨迹扰动

## 2026-11-04：自然标签可学习性实验完整归档

[完整研究报告与可复现原始数据](v10_research/natural_label_accessibility_20261104_0200/README.md)：4 个独立重复、4 个条件、全部 24,000 个优化步骤、参数/梯度/Adam 状态、输入与逐样本预测均保留。联合预设描述性假设未达到：学习池化通过，固定均匀池化漏过差距阈值；KT 计数基线更好。该实验使用提供的局部特征，不是完整 Transformer 训练，也没有恢复旧 20:35 试验。原始 22 个捕获包约 639 MB，另有早期实现快照；公开副本仅清理非科学隐私元数据，逐成员哈希映射和离线逐步审计齐全。

## 2026-11-04：任意初始化 A⁵ 下界的补充纠正

[完整更正与两份独立分析](provenance/arbitrary_initial_kl_lower_20261104/PUBLIC_EXPORT.md)：继承 MM5 的实际末端 TV 下界经 Pinsker 与 Jensen 推出 2⁻³¹ min{1,A⁵/(n+1)} 的 forward-KL minimax 下界。任意初始化的 A⁵ 多项式因子因此是必要的，与已有 add-one 上界至多差对数因子；精细对数、饱和区及完整联合参数速率仍未解决。平稳 A³ 源类须单独区分。旧科学文件不覆盖，哈希差异及原始记录缺口继续保留。

## 2026-11-04：末端 KL 的两个新上界

[本批中文总览](provenance/terminal_kl_20261104/RESEARCH_SUMMARY.zh.md)公开任意初始二元组的固定 alphabet 对数率，以及平稳源的 A³[1+log₊((n+1)/A³)]/(n+1) 上界，并保留独立 LLM 分析、完整前序证明及 exact-real/指定 finite-bit 输出区别。

[公开导出与核验范围](provenance/terminal_kl_20261104/PUBLIC_EXPORT.md)：数学陈述不改，非数学准备信息另作逐行映射。内部分析不是外部同行评议、文献优先权、训练成功或通用 IEEE 证书。旧 build/check 脚本仅作历史准备记录，不构成本次公开副本的独立重建方法。

## 完整同源训练轨迹：经典计数比较基线（2026-11-03）

[新阶段导读](provenance/full_shared_source_training_20261103/RESEARCH_SUMMARY.zh.md)：N 条独立平稳干净轨迹共享同一个未知二阶源，汇集 NM 次转移，测试仅使用受保护末尾对。在 β≥1/M、N≥M 时可达到 Θ((NM)^−1/2)，包括允许比较者读取完整测试词的未知源下界。

这不是注意力优势、新学习原理或换源训练保证。训练输入需 N(M+2) 字符，N=Θ(M) 时为 Θ(M²)。三份完整现存原件与实际措辞纠正均保留，当前没有训练/数值实验；[默认检查](provenance/full_shared_source_training_20261103/PUBLIC_REPLAY.md)只核验来源与依赖身份。

## 同源训练、换源先验与固定门：适用边界（2026-11-03）

[本阶段中文总览](provenance/source_matched_learning_20261103/RESEARCH_SUMMARY.zh.md)保留三项完成研究及真实纠正：iid 子类的固定门拒绝上界、跨源下界推理的撤回、同一个未知源的训练基线和每个 episode 重新抽源的条件推论。

**没有得到一般训练困难性或新学习算法。** 同源四行估计有 3/√(N+1) 风险界，但完整输入要读取 N(M+3) 字符；换源推论直接来自既有 B.3，先验依赖 k，结论条件于干净风险 ε。两种实验不能混用。

全部 25 项现存脚本、日志、逐例数据和审阅按原字节归档。原 iid 精确尾中间值及失败 wrapper 输出仍缺失；后来完整记录另列，不冒充恢复。见[无采样公开核验](provenance/source_matched_learning_20261103/PUBLIC_REPLAY.md)。

## 浮点、攻击 DP 与期望风险：边界和完整现存证据（2026-11-03）

[本阶段中文总览](provenance/float_and_attack_boundaries_20261103/RESEARCH_SUMMARY.zh.md)串联 15 个完成目录：特定后端下的浮点同计数差异、条件误差/区间证书、固定维 dyadic DP、增长维度与位置权重困难性，以及逐点、期望 TV、常数因子和常数加性逼近。

**这些不是训练成功、通用 Transformer 或未知源预测困难性的证明。** 期望风险构造允许重写所有公式位，主要嵌入经典 Max3SAT；常数加性 TV 结果放弃消失误差。文献审计的宽泛 7/8 匹配基线已[纠正](v10_research/expected_risk_prior_art_audit_20261103_0957/CORRECTION_CONDITIONAL_EXPECTATION.md)：一般情形为 1/2，7/8 需额外条件。

258 项现存文件、全部原脚本和数值档案一并保存。初次浮点失败输出、被覆盖的训练检查首版、部分原确定性逐项记录和原区间端点并未恢复。请读[无采样公共核验及缺口](provenance/float_and_attack_boundaries_20261103/PUBLIC_REPLAY.md)，不要把后补独立记录或历史综合稿当作原始证据/最新全局结论。

## 四计数 DP 与固定门函数试验：完整现存记录及缺失说明（2026-11-03）

[四计数证明](v10_research/four_counter_dp_20261103/RESEARCH_NOTE.md)给出固定半程输入的 O(M^5) 扫描、O(M^4) 滚动状态；但[补充纠正](v10_research/four_counter_dp_20261103/ADDITIVE_CORRECTION.md)明确，现有程序先转浮点，并非通用精确有理或逐位等同神经输入的优化器。[45 次固定门函数评估](v10_research/exact_dp_pilot_20261103/REPORT.md)不是神经训练，CE 最大值采用浮点比较，时间口径另有[纠正](v10_research/exact_dp_pilot_20261103/TIMING_AND_NUMERIC_CORRECTION.md)。

全部 54 项现存非缓存文件公开，包括原二进制、脚本、参数、候选、见证、时间和重构档案。**这不等于原始采样全保存**：原始随机轨迹、完整 DP 状态，以及后续 700,000 个诊断词和重复模型参数未全部留存。请先读[保留缺口审计](v10_research/exact_dp_pilot_20261103/review_independent/ADDITIONAL_PRESERVATION_AUDIT.md)及[不采样的公共核验](provenance/four_counter_and_gate_pilot_20261103/PUBLIC_REPLAY.md)。历史脚本若直接执行可能采样或覆盖输出，不能把后补重放冒充原始记录。

## 固定计数读出的精确离线攻击（2026-11-03）

[完整证明与诊断](v10_research/exact_attacker_dp_20261103/RESEARCH_NOTE.md)给出严格保护末尾二元组、至多 k 次编辑的最小代价动态规划。对选定 J,C,D 三计数读出，扫描 O(M^4)、滚动状态 O(M^3)；完整前后半段转移直方图为 O(M^9)/O(M^8)。位运算、精确读出/比较和见证重建成本另计，不能据此宣称实际高效。

它只适用于声明的计数与端点接口，不是任意 Transformer 攻击算法或学习保证。对同一条件估计和相同合法读出，它可原样替换上一阶段的内层枚举；不会自己估计 p(h)。[全部代码、真实修正与原始输出](v10_research/exact_attacker_dp_20261103)、[独立 LLM 审阅](v10_research/exact_attacker_dp_20261103/review_independent/REVIEW.md)及[公共隔离复现](provenance/exact_attacker_dp_20261103/PUBLIC_REPLAY.md)均保留。

## 合法对抗监督目标与离线有限类界（2026-11-03）

[完整分析](v10_research/legal_conditional_training_20261103/RESEARCH_NOTE.md)区分只看历史的合法攻击与看见未来标签的训练攻击：平方损失下，前者与真实来源风险的预测器排序一致；一个精确反例显示后者可以反转排序。对固定二阶 Markov 混合总体，初末状态与转移计数给出至多 16(M+1)^4 个条件预测组，继而得到保守的有限类离线学习界。

这是已知充分性和集中工具的具体组合，不是新的通用统计原理、SGD 收敛、学得注意力、最坏来源或未知预算保证。枚举攻击的成本可能指数增长，界也可能无效。[独立 LLM 审阅](v10_research/legal_conditional_training_20261103/review_independent/REVIEW.md)、全部修正历史、精确有理检查与[公共隔离复现](provenance/legal_conditional_training_20261103/PUBLIC_REPLAY.md)均保留；原 55 页稿件和训练档案不变。

## 稀有样本加权：均值收益、尾部代价与完整记录（2026-11-03）

[初次加权实验](v10_research/rare_weight_ablation_20261103/COMPLETED_RUN_REPORT.md)与[保留缺口更正](v10_research/rare_weight_ablation_20261103/COMPLETED_RUN_REPORT_CORRECTION.md)、[新数据后续实验](v10_research/rare_weight_confirmation_20261103/RESULTS_REPORT.md)及[完整轨迹独立审计](v10_research/rare_weight_confirmation_20261103/independent_completion_audit/REVIEW.md)均已整理。两次有限筛选均通过，但自然先验平均绝对误差变差，条件尾部最大误差仍很大；三个初始化共享数据/批次，后续不是盲确认，也不是学得鲁棒性或一致逼近保证。

全部实际保留的脚本、参数、原始候选/潜变量/均匀随机数、逐步更新、检查点、指标和失败历史均入档。第一次未保留的 128,000 个拒绝/截断候选及潜变量不能冒称已恢复；第二次完整留存不修复这个历史缺口。71,171,358 字节全更新日志以 17 个无压缩字节块保存，可[逐字节重建并安全复核](provenance/rare_weight_20261103/PUBLIC_REPLAY.md)。

## 固定半程特征与稀有大误差（2026-11-03）

[完整分析](v10_research/fixed_half_tail_geometry_20261103/ANALYSIS.md)证明：在 M=64，已提供的半程计数特征足以确定 Q；有限集合上也存在极大宽度、精确实数的 tanh 插值构造。这不是宽度 32 的容量结论、有限精度方案或学习保证。

对已有数据和检查点的[尾部诊断](v10_research/fixed_half_tail_geometry_20261103/RESULTS.json)同时发现未覆盖的验证特征，以及被反复抽到仍明显欠拟合的训练例。平均目标允许稀有大误差，但这些事后观察没有隔离因果机制，也未展示学得鲁棒性。完整失败记录、脚本、原始输出和[独立 LLM 审阅](v10_research/fixed_half_tail_geometry_20261103/review_independent/REVIEW.md)均保留。[安全复现与身份说明](provenance/fixed_half_tail_geometry_20261103/PUBLIC_REPLAY.md)。

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
