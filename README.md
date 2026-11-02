# Transformer 预测：统计、资源、精度与源轨迹扰动

这项研究讨论未知二阶随机过程的下一符号概率预测：历史长度、可见信息、网络结构、内部精度、计算成本与扰动，分别怎样限制可达风险。仓库保留完整证明、审查、诊断、真实失败与修订记录；不同模型的结论不互相替代。

**科学状态截至 2026-11-02。** 第八阶段有六个冻结单元，之后另有四个已审查接纳的研究更新。这里的“接纳”是项目内证据状态，不是期刊录用、形式证明或外部同行评审。

## 从这里开始

| 阅读目的 | 入口 |
|---|---|
| 先了解结论、条件和未解项 | [当前状态与分析](docs/STATUS.md) |
| 看方法、失败、修订及阶段决定 | [按日期整理的研究日志](docs/RESEARCH_LOG.md) |
| 找证明、完整审查、诊断和历版文稿 | [资料导航](docs/NAVIGATION.md) |
| 第八阶段源轨迹扰动：英文 27 页 | [PDF](v10_research/source_corruption_manuscript/corrupted_trajectories.pdf) · [LaTeX](v10_research/source_corruption_manuscript/corrupted_trajectories.tex) |
| 第八阶段中文说明：9 页，93 个原生可编辑公式 | [DOCX](v10_research/source_corruption_guide/Chinese-stage8-guide.docx) · [PDF](v10_research/source_corruption_guide/Chinese-stage8-guide.pdf) |
| 内部信息切口、精度、深度与可靠性：英文 v5，70 页 | [PDF](v10_research/manuscript_v5/finite_precision_prediction.pdf) · [LaTeX](v10_research/manuscript_v5/finite_precision_prediction.tex) |
| 前期精度与可靠性中文说明 | [第七阶段 DOCX](v10_research/precision_robustness_guide/Chinese-stage7-guide.docx) · [PDF](v10_research/precision_robustness_guide/Chinese-stage7-guide.pdf) |
| 核对原始文件、公开导出与路径对应 | [公开来源映射](provenance/PUBLIC_SOURCE_MAP.json) · [公开校验工具](tools/public_verify.py) · [复现边界与操作](docs/REPRODUCIBILITY.md) |

## 三条主线

1. **统计基准与固定表示。** 全历史预测、固定有限信息接口、正混合与任意初始化分别取证。内部网格、完整计算字长、输出精度以及计算时间不能合并成一个“精度”指标。
2. **深度、编码与可靠性。** 研究固定结构的必要条件，也研究付出全部成本的重新编码构造。IID、一般 Markov 源、固定编码器和可重新设计的编码器有不同结论。
3. **源轨迹扰动及后续联合问题。** 第八阶段研究编码前的符号替换；后续 JP001 与 RE001 把源扰动接到不同的内部噪声接口，AB001 与 AB002 划清未知预算适应的已知边界。

## 必须保留的边界

- **BT001 的强内部常数步输运前提仍未证明。** BT002 通过独立的较弱熵输运路线证明二元下界，不依赖那个开放前提。
- **EP001 改变终点编辑权限，不改变预测目标。** 目标仍是原始隐藏轨迹的真实终点条件分布。
- **AB001 排除的是同一个估计器同时不知道 `k` 和 `beta` 的统一适应。** 已知 `beta`、未知 `k` 的中间混合区间仍开放；AB002 只证明普通 add-one 估计器的对数级失配。
- 独立 LLM 审查、有限诊断与构建复现各有证据范围，均不等于形式验证、外部同行评审、新颖性认证、训练可达性或真实网络运行证明。

原始科学版本不被事后改成“当时已经完成”。历史文件中的候选、待批准或尚未发布措辞，按其写作时点理解；后续状态见带时间与哈希的接纳记录及公开来源映射。原始用户指令、私人运行记录、凭据与无关文件不属于公开研究材料。
