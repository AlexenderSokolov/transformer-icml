# 浮点实现、结构化攻击与期望风险的计算边界

2026-11-03。本阶段保存 15 个已完成研究目录的全部现存证明、脚本、参数、数值记录、失败说明、真实修改和来源绑定审阅。历史正文中的“尚未审阅”保留原时间状态，请同时阅读后来的独立 LLM 审阅；它们不是外部同行评议、形式化证明或新颖性认证。既有 55 页论文和训练档案不改。

## 1. 理想计数相同，不保证实际浮点路径相同

[确定性浮点调查](../../v10_research/float_bank_deterministic_20261103/REPORT.md)给出特定 NumPy/BLAS、布局和固定批形状下同计数银行的差异。早期跨不同批大小的观察不能当作固定形状反例。换后端、批大小、候选顺序或槽位，结果可能不同；这既不是所有 BLAS 的定理，也不是训练模型鲁棒性失败的普遍结论。

[已训练半程读出诊断](../../v10_research/trained_half_float_check_20261103/REPORT.md)中，测试的 A/B 最终概率和 CE 相同，不能把输入轨的一 ULP 差异夸大成预测损害。[读出误差界](../../v10_research/float_readout_bound_20261103/REPORT.md)及[批上下文补充](../../v10_research/float_readout_bound_20261103/ADDITIVE_BATCH_CONTEXT.md)依赖明确的统一后端误差假设，未证明实际 NumPy/BLAS 满足这些假设。

[区间证书](../../v10_research/conditional_bank_interval_certificate_20261103_0854/RESEARCH_NOTE.md)是精确有理计算与假设误差半径下的条件结论，不是实际后端、保存检查点或观察攻击的证书。[事后端点](../../v10_research/bank_certificate_posthoc_endpoints_20261103_0857/PRESERVATION_AND_PROVENANCE.md)和[范围/重数补充](../../v10_research/bank_certificate_scope_addendum_20261103_0857/SCOPE_AND_MULTIPLICITY.md)一起阅读。

## 2. 精度、维度与允许接口决定可解性

[位置加权攻击](../../v10_research/position_weighted_attack_hardness_20261103_0903/RESEARCH_NOTE.citation_corrected.md)给出指定混合模型及二进制编码参数下的弱 NP 困难性；不能推出固定精度、近似攻击、SGD 或学习权重的困难性。原引用描述已[纠正并保留差分](../../v10_research/position_weighted_attack_hardness_20261103_0903/CITATION_CORRECTION.diff)。

[固定维 dyadic DP](../../v10_research/dyadic_feature_dp_20261103_0915/RESEARCH_NOTE.dominance_corrected.md)利用有界、精确对齐的可加特征和有限状态。多项式界要求维度、状态、幅值、读出与位成本满足所列条件。最小编辑数支配适用于“至多 k”，不能直接换成“恰好 k”。[稀疏预算补充](../../v10_research/dyadic_feature_dp_20261103_0915/SPARSE_BUDGET_ADDENDUM.restrictions_corrected.md)明确附加限制前后的前缀计数差异。

[增长维度构造](../../v10_research/growing_features_hardness_20261103_0922/RESEARCH_NOTE.md)把 3SAT 放入可变宽度、精确 dyadic、ReLU/均匀注意力模型，所有表示和精度成本必须计入。其逆多项式间隙本身不是常数加性间隙，也不是任意标准 Transformer 的结论。

## 3. 从单历史到期望 TV，再到两种逼近尺度

- [逐点 TV](../../v10_research/fixed_source_pointwise_tv_hardness_20261103_0934/RESEARCH_NOTE.md)对应指定公共 iid 源下有正概率的全零历史，必须遵守[初始分布澄清](../../v10_research/fixed_source_pointwise_tv_hardness_20261103_0934/INITIALIZATION_CLARIFICATION.md)。
- [期望 TV](../../v10_research/fixed_source_expected_tv_hardness_20261103_0939/RESEARCH_NOTE.md)及[精确 MaxSAT 关系](../../v10_research/fixed_source_expected_tv_hardness_20261103_0939/EXACT_MAXSAT_REDUCTION.md)针对构造出的预测器和合法、只看历史的攻击，不需要把未来标签交给攻击者。最优赋值作为存在性见证，并不免费提供寻找它的算法。
- [常数因子期望 TV](../../v10_research/constant_factor_expected_tv_hardness_20261103_0945/RESEARCH_NOTE.scope_corrected.md)引入经典 Håstad 间隙；原模型的绝对 TV 为 O(1/M)，所以不是常数绝对误差困难性。
- [常数加性期望 TV](../../v10_research/constant_additive_expected_tv_hardness_20261103_0954/RESEARCH_NOTE.md)改用 q=p+S/(2P)，得到指定模型族的 1/128 加性值估计困难性，但有意放弃消失误差，风险可为常数。独立的确定性、全局合法、可多项式求值策略输出结论另需平稳初始化。
- [归一化消失风险](../../v10_research/constant_additive_expected_tv_hardness_20261103_0954/NORMALIZED_VANISHING_RISK.md)对原小风险模型考察 M·R；常数归一化误差等于原 TV 中 O(1/M) 精度，不能偷换成常数绝对 TV 间隙。

这些期望风险构造中 k=n 足以重写所有携带公式的位，每个干净历史都可到达同一赋值最优问题。因此它们主要是经典 Max3SAT 的明确模型嵌入，并非新的随机困难性机制。知道同一个公共源参数 p 的常数预测器可以输出 p，取得零 TV；这些结果不是未知源预测或 minimax 学习困难性，不证明神经优势、训练可达性或一般架构困难性。

## 4. 文献和基线：保留真正的纠正

[定向文献审计](../../v10_research/expected_risk_prior_art_audit_20261103_0957/AUDIT.md)对顶会级新颖性作谨慎评价，不声称完整检索。**先读[条件期望法纠正](../../v10_research/expected_risk_prior_art_audit_20261103_0957/CORRECTION_CONDITIONAL_EXPECTATION.md)**：原审计把所有长度至多三的标准化子句都算成 7/8，是错误的。一般非空标准化子句证明的是 1/2 因子；7/8 需要每个非重言子句含三个不同变量，或实际 E0≥7m/8。重复子句的重数仍保留。该纠正针对拟议匹配算法，不改变此前归约的逐子句真值保持。检查器枚举小例，不能把它的指数枚举当作所述多项式条件期望算法。

[额外核验比较](../../v10_research/expected_risk_prior_art_audit_20261103_0957/ADDITIONAL_VERIFICATION_PRIOR_ART.md)区分离散反事实、编码器可满足性、候选计数概率与干净历史上最优损失的期望。只链接原论文；没有转发版权全文。阅读范围和无法直接访问的来源均明示，不声称通用形式验证困难性首次出现。

## 5. 历史记录与可重放范围

- 原浮点确定性搜索、位置加权困难性作者检查和 dyadic 作者诊断只保留汇总日志，未保存每个原候选/中间量；独立检查器的逐项档案不是这些原运行的恢复。浮点初次 JSON 序列化错误和 int8 溢出输出也没有独立保存。最终修正版不能恢复那些原输出。
- [第二项已训练诊断保留纠正](../../v10_research/trained_half_float_check_20261103/PRESERVATION_CORRECTION.md)：首次脚本、日志和完整 JSON 在重跑时被覆盖。只有已记录的打印摘要；没有完整原件和原哈希，不能把当前 JSON 当作原件。
- 区间初次程序被中断且日志为空；成功版本未同时记录精确端点，后来端点是确定性重构。一次追加失败也没有独立终端日志。
- [增长维度保留披露](../../v10_research/growing_features_hardness_20261103_0922/PRESERVATION_DISCLOSURE.md)：原作者的逐公式/赋值/中间量以及后来独立执行原脚本的逐项记录均未保存。独立检查器自己的完整档案是不同记录，不能补回这两次原件。
- [旧综合稿](../../v10_research/integrated_boundary_20261103_EQRJKR/SYNTHESIS.readout_corrected.md)及[经验补充](../../v10_research/integrated_boundary_20261103_EQRJKR/EMPIRICAL_SCOPE_ADDENDUM.md)是早于逐点和期望 TV 新结果的历史快照，不充当本阶段最新总论。它还保留更早训练/诊断的缺口，不因本次上传而消失。

本次公开核验只读已保留数值并做确定性算术，不运行旧采样脚本、不初始化模型、不重跑 BLAS/计时、也不生成随机数据。完整范围见[公共核验说明](PUBLIC_REPLAY.md)。路径/主机元数据的非数学公开编辑都有原始与公开身份映射；数学、程序和数值数组保持不变。五个检查点旧路径可由相同字节的公开文件作别名，不代表恢复独立运行来源。八份历史本地准备/发布元数据不公开，不能声称整个私人操作历史已闭合。
