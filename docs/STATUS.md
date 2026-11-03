# 当前状态：位置计数与未知预算适应

## 2026-11-03：固定半程信息充分，但有限拟合仍有尾部失败

新增[固定半程几何分析](../v10_research/fixed_half_tail_geometry_20261103/ANALYSIS.md)。M=64 时，已有计数特征可精确确定目标；至多 1,258,883 个隐单元的有限集合实数插值仅是存在性说明，不是当前宽度 32 的可学性、不可表达性或可行精度保证。

同一冻结数据上既有验证覆盖不足，也有重复抽样训练点的欠拟合。没有新训练、选种子或新确认样本；不能从平均误差、饱和或近邻关系推出唯一原因或成功的干预方法。此前 55 页稿件、实验原始档案与历史失败不变。

## 2026-11-03：两项有限经验研究

新增阶段包含[学习位置池化冒烟测试](../v10_research/learned_position_pilot_20261103/REPORT.md)及[解释修正](../v10_research/learned_position_pilot_20261103/REPORT_REVIEW_AMENDMENT.md)，然后是[固定半程读出校准](../v10_research/readout_conditioning_calibration_20261103/REPORT.md)及[审计补充](../v10_research/readout_conditioning_calibration_20261103/REPORT_AUDIT_ADDENDUM.md)。前者没有展示有用的学习位置保护；后者只支持特定 Q 监督、碰撞词加权和固定优化预算下的参数化差别。

校准的有限平均筛选通过不代表一致拟合：仍有个体误差超过 0.4。三个初始化共享数据/批次，四个碰撞词也是训练词；独立抽样的先验训练/验证集包含 9 个共同字符串，占 25 条验证轨迹。原始报告与补充均保留，不将结果改写成最坏情形学习保证、一般 SGD 结论或新理论单元。原设计的较大预算与随后缩小的实际冒烟测试预算保持各自历史身份。

## 2026-11-03：干净目标、单偏置动态与约束窗口

本次阶段包含三个已接纳数学单元 CTO001、PGT001、PBF001，以及一个已审阅的固定规模合成诊断。见[中文总结](../v10_research/learning_objective_stage_20261103/RESEARCH_SUMMARY.zh.md)。精确总体干净目标可以选中计数型 Bayes 规则；给定特征后的单偏置精确下降最终趋向该规则；适当投影则在这个明确模型内保留鲁棒性。

证据只覆盖已给定特征和精确总体梯度模型。不是一般网络训练结论，模拟也不证明最坏情形鲁棒性。所有旧稿件字节不变；候选文件中的待审或尚未公开标签保留为当时记录，最终接纳身份由同目录凭据与阶段冻结表说明。

## 2026-11-03：55 页完整论文整合稿

当前完整读物为[英文整合稿](../v10_research/positional_manuscript_consolidated_20261103/main.pdf)，包含主文、全部证明附录和文献。数学来源、完整证明整合、独立 LLM 审阅、清洁重建与页面核对均有明确凭据；发布只交付该固定版本及选定来源审计。

这次是已接纳工作的整理，不增加新定理。BCJ 的先前有限库结果、ACG/PBP 的改变接口重推与 FPA 的明确实现各自区分。证书自由结论按已有结果的推论说明，不重复计为新发现。尚未完成的学习目标研究未进入本稿。

## 2026-11-03：从统计接口到有限注意力

本次新增 CCH001、ACG001、FPA001、PBP001，详见[阶段综述](../v10_research/positional_attention_stage_20261103/RESEARCH_SUMMARY.zh.md)。二阶结果保留指定全状态证书；有限构造使用允许的 singleton 结构掩码；精度必要性只约束固定分别舍入的十二坐标库。CCH001 澄清完整预状态与历史条件下的信道保真要求，不把单次边缘错误率当作充分条件。

以下未知信道阶段的范围说明保留其当时含义；本次条件信道扩展有独立证明与接纳凭据。新的中心文献研究不在本次冻结内。

## 2026-11-03：未知信道阶段

新增四个接纳单元 UMC001、UWC001、CAF001、CMF001。结论和统一量词见[本阶段综述](../v10_research/channel_uncertainty_stage_20261103/RESEARCH_SUMMARY.zh.md)。固定名义信道下，模型误差的可辨识边界、精度过渡及余量趋零成本分别取证。含历史依赖的信道扩展仍在本阶段范围之外。

## 2026-11-03 状态补充

最新结果、适用模型和文献边界见[本阶段中文综述](../v10_research/resumption_20261103/RESEARCH_SUMMARY.zh.md)。六个接纳目录是 noisy_gate、bsc_sharp、channel_classification、whole_message_cost、efficient_message_code、order_two_transfer；对应接纳范围由各自 ROOT_ACCEPTANCE.json 固定。补充消息与全消息不同，一阶无混合条件与二阶给定临界全状态条件不同。下面的 2026-11-02 记录保持历史含义。

本稿按当前已接纳的十个单元整理：KH001、KH002、CB003、KH003、CB004、BP001、CB005、KH004、AF001、BCJ001。它们不改写阶段八冻结，也不改写已公开的历史证明与旧开放问题。十个单元的精确证明与审查字节已接纳；本次不加入更晚的研究单元。公开综述与资料清单已完成发布前来源与隐私核验。

## 核心区别：保存哪些统计量，比“是否看到完整历史”这个标签更精确

- **KH001／KH002：八个全局三元计数加首末符号对。** KH001 完成强于临界证书的一段否定结果；KH002 给出任意公开证书域的完整分类：对所有未知预算同时达到已知预算风险阶，当且仅当域内 `G(M, beta)` 有界，其中 `G(M, 0) = 0`，正 beta 时 `G = min(M² beta, 1/(beta sqrt(M)))`。正向适用于任意初始化；反例已可取平稳源。
- **KH003／KH004：上述计数加真正的首尾窗口。** KH003 在 `beta = 1/M` 排除所有预先指定 `r = o(M^(1/6))` 的全预算适应；KH004 用不同的常数交叉转移构造把这一充分否定范围扩大为 `r = o(M^(1/3))`。KH003 仍是独立有效的历史基线，不是错误版本。不能据此声称立方根是尖锐阈值，也不能把边界窗口换成全部内部长模式计数、任意局部编码器或完整历史。
- **CB004／CB005：全局三元计数，再加四个前半段行占用计数及受保护终点对。** 同一个确定性平衡门控估计器，不读取实际预算 k，也不读取 beta。CB004 在平稳初始化下成立，依赖 BP001 的平稳加权不平衡引理；CB005 用目标首达、回返和倾斜联合占用论证补齐任意初始化，包括平稳支撑之外的起点。它们不需要保存全部排列细节，也不证明“任意位置摘要”都足够。

因此，临界证书曲线上“全局直方图加短边界窗口不适应”和“只增加四个前半段计数即可适应”可以同时成立。否定结果与正向构造的观测接口不同，不能相互替换。

## 正向风险及与已有结果的关系

CB005 的已接纳上界为

    R_all <= min(1, 2^16 / sqrt(M) + 2^16 / (M sqrt(beta)) + 2^23 k / M).

同一估计器在每个固定 `c > 0` 的区域 `beta >= c/M` 内，对所有预算同时达到已知预算风险阶；常数可以依赖 c。这包括 `beta = 1/M`，并覆盖任意起始分布。CB004 的平稳项常数更小，但不能把它的平稳证明直接宣传为原本已经覆盖任意起点。

这不与 BK002 的“对全部 beta 一致”的全历史适应不可能性冲突：CB005 只证明上述强侧区域。也不消除 KA001 已证明的弱侧／中间曲线差异。AF001 现已接纳，补齐了下述任意公开证书域分类；原来的候选与开放措辞作为历史保留。

## 必须保留的失败、修订和归属

- CB003 是具体规则 `W(AB003)` 的反例：固定近前缀否决可以被合法污染绕过。它不是完整历史的不可能性证明；CB004／CB005 换用了前半段与全局占用的平衡门控。
- KH001 保存真实的预冻结编辑副本，及对旧对称零假设“长前缀免费”设想的失败分析；后者不是虚构的旧证明文件。
- KH002 保存诊断程序对可选收据字段处理不当的真实 KeyError 和一行修复。KH003 保存边界窗口测试必要性措辞的真实澄清，以及审查诊断中精确根号取整的真实修正。
- CB004 保存初版诊断的真实 SyntaxError 文件，不把它当作当前可运行程序，也不擦除它。CB005 的审查记录保存了冻结依赖诊断的独立重跑输出与原输出恢复证据；本次发布准备本身没有重跑这些科学程序。
- Norris、Peres、Zhai 的一手文献已建立一般有限状态首达概率的维度／时间尺度。项目中的自含推导与索引变体不能当作该尺度的新发现。相关文献笔记明确限定实际阅读范围，不提供全文，也不声称完成新颖性检索。

当前材料的独立 LLM 审查、有限精确诊断和来源审计均不是形式验证、外部同行评审、新颖性认证或神经架构实现证明。

## AF001：完整历史的精确证书域分类

对任意公开域 E，给定实际 beta、未知实际 k 的完整历史预测器能够统一覆盖全部预算，当且仅当

    sup_E G_full(M, beta) < infinity,
    G_full(M, 0) = 0,
    G_full(M, beta) = min(M² beta, 1 / (M beta))  （beta > 0）。

这等价于 E 被某个固定 B 对应的两段区域覆盖：`beta <= B/M²` 或 `beta >= 1/(B M)`。它包含稀疏、振荡等非幂律公开域；常数与估计器可以依赖整个公开域。平稳与任意初始化的分类相同，负向见证已经平稳。

正向选择器根据实际提供的 beta，在弱侧 add-one 与强侧平衡门控之间选择。因此整个并集上的选择器**不一般是 beta 盲的**，尽管各自单独的规则可以是。它与 KH002 的直方图判据差在第二项：`1/(M beta)` 对比 `1/(sqrt(M) beta)`。四个前半段计数是足够的构造，不是数量最小性的证明。

## BCJ001：十二坐标、已计费的有限噪声接口

固定编码器输出八个三元频率和四个前半段行占用子频率，十二项全部除以 M。源端先受严格 k 次符号编辑，再经过一次十二坐标向量的 l-infinity 噪声 delta，随后裁剪与 Q 网格向下取整。最终仅这十二个标签、受保护终点对及与数据无关的公开格式跨越切口。

同一个不读取 k、delta、beta 的有限有理门控解码器，在每个固定 `beta >= c/M` 区域达到

    Theta_c(min(1, max(M^(-1/2), k/M, delta, 1/Q)))。

该匹配阶对平稳与任意初始化均成立；在该区域以下，只有原文明确给出的上下界夹层，不能宣布全域匹配。一次向量攻击不是只改一个标量。新增四个端口需要新的完整十二坐标精度下界，不能直接沿用八坐标接口的结论。

局部表、公开位置指示、掩码、完整工作位宽、执行与隔离成本均按原证明计费。h 是小数精度参数而不是全部工作字长。本结果针对固定前缀，不是优化所有编码器后的下界，也不是固定神经深度或训练结论。

## 阅读入口与精确证据

- [英文阶段综述](../v10_research/adaptation_stage_synthesis/positional_counts_adaptation.md)
- [中文阶段总结](../v10_research/adaptation_stage_synthesis/research_summary_zh.md)
- [阶段综述来源表](../v10_research/adaptation_stage_synthesis/SOURCE_MAP.json)
- [初次完整发布的历史状态](STATUS_INITIAL_20261102_115746.md)与[第二次增量的历史状态](STATUS_SECOND_20261102_1337.md)：旧开放措辞只代表相应时点。

| 单元 | 证明 | 完整审查 | 接纳记录 |
|---|---|---|---|
| KH001 | [证明](../v10_research/binary_certificate_adaptation_phase/KH001_histogram_strong_side_obstruction.md) | [审查](../v10_research/reviews/KH001_independent_full_review.md) | [2026-11-02T13:37:01.035403+00:00](../v10_research/intake/KH001_acceptance.json) |
| KH002 | [证明](../v10_research/binary_certificate_adaptation_phase/KH002_histogram_domain_classification.md) | [审查](../v10_research/reviews/KH002_independent_full_review.md) | [2026-11-02T13:49:27.429240+00:00](../v10_research/intake/KH002_acceptance.json) |
| CB003 | [证明](../v10_research/critical_beta_adaptation/CB003_fixed_veto_bypass.md) | [审查](../v10_research/critical_beta_adaptation/CB003_independent_full_review.md) | [2026-11-02T13:40:32.637398+00:00](../v10_research/intake/CB003_acceptance.json) |
| KH003 | [证明](../v10_research/binary_certificate_adaptation_phase/KH003_boundary_window_obstruction.md) | [审查](../v10_research/reviews/KH003_independent_full_review.md) | [2026-11-02T14:19:42.998497+00:00](../v10_research/intake/KH003_root_acceptance.json) |
| CB004 | [证明](../v10_research/critical_beta_adaptation/CB004_stationary_critical_adaptation.md) | [审查](../v10_research/critical_beta_adaptation/CB004_BP001_independent_full_review.md) | [2026-11-02T14:19:42.998810+00:00](../v10_research/intake/CB004_root_acceptance.json) |
| BP001 | [证明](../v10_research/critical_beta_adaptation/balance_probe/BP001_stationary_weighted_balance.md) | [审查](../v10_research/critical_beta_adaptation/CB004_BP001_independent_full_review.md) | [2026-11-02T14:19:42.998943+00:00](../v10_research/intake/BP001_root_acceptance.json) |
| CB005 | [证明](../v10_research/critical_beta_adaptation/CB005_all_start_critical_adaptation.md) | [审查](../v10_research/critical_beta_adaptation/CB005_independent_full_review.md) | [2026-11-02T14:25:29.077559+00:00](../v10_research/intake/CB005_root_acceptance.json) |
| KH004 | [证明](../v10_research/binary_certificate_adaptation_phase/KH004_constant_crossing_window_obstruction.md) | [审查](../v10_research/reviews/KH004_independent_full_review.md) | [2026-11-02T14:26:19.438693+00:00](../v10_research/intake/KH004_root_acceptance.json) |
| AF001 | [证明](../v10_research/binary_full_history_domain/AF001_full_history_domain_classification.md) | [审查](../v10_research/reviews/AF001_independent_full_review.md) | [2026-11-02T14:31:00.361602+00:00](../v10_research/intake/AF001_root_acceptance.json) |
| BCJ001 | [证明](../v10_research/balanced_joint_finite_cut/BCJ001_theorem.md) | [审查](../v10_research/balanced_joint_finite_cut/BCJ001_independent_full_review.md) | [2026-11-02T14:31:28.560722+00:00](../v10_research/intake/BCJ001_root_acceptance.json) |

阶段八六单元冻结保持不变；BT001 的强输运前提仍未证明，BT002 仍走独立熵路线；EP001 仍以原始隐藏终点为目标。以上新增适应结果均须保持二元限定，不能移植成 K ≥ 3 的适应障碍。
