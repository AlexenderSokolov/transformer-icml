# 末端 KL：任意起点对数率与平稳尖锐对数

本次公开两份完整科学材料及其直接前序证明。它们研究同一未知齐次二阶源的完整历史、实际末尾上下文和下一符号正向 KL 风险，不能与训练实验或一般 Transformer 优化保证混为一谈。

## 两项上界

1. [任意初始二元组](../../v10_research/fixed_alphabet_kl_sharpening_20261103_2346/sharp_kl_output_corollaries.v1.md)：对 A≥2、n≥1，full-history add-one 风险不超过 min{log(n+A), A^4[log A+1536A(1+floor(log_2 n))]/(n+1)}。固定 A 时为 O_A(log n/n)。HJW 平稳下界给出固定 A 最坏情形的匹配阶，也适用于包含平稳初态的任意初态大类；它不是每个预先指定初态的下界。
2. [平稳源](../../v10_research/stationary_logarithm_20261104_0032/stationary_sharp_output_corollaries.v1.md)：add-one 风险不超过 min{log(n+A), 14000 A^3/(n+1)[1+log_+((n+1)/A^3)]}。归一化对数与 alphabet 因子一起保留，不能把平稳假设去掉。

两者分别继承五块 exact-real 输出与指定整数/dyadic 求值器的额外风险项；后者支付随 A,n 增长的分数位、符号/幅值、累加及乘法字宽。它不是通用 IEEE 或固定总字长的软件正确性证书。n=0 和不同 alphabet/order 例外见原文。

## 证明、审查与文献边界

- [平稳候选证明](../../v10_research/stationary_logarithm_20261104_0032/stationary_addone_sharp_log.candidate.v1.md)、[独立审查](../../v10_research/stationary_logarithm_20261104_0032/stationary_addone_sharp_log.independent_review.v1.md)、[对抗审查](../../v10_research/stationary_logarithm_20261104_0032/stationary_addone_sharp_log.redteam_review.v1.md)均保留。
- [任意起点证明](../../v10_research/fixed_alphabet_kl_sharpening_20261103_2346/tilted_occupation_terminal_kl.candidate.v1.md)及两份完整审查与更早 log-squared 版本同时保存，不回写历史候选措辞。
- [文献状态审计](../../v10_research/stationary_logarithm_20261104_0032/stationary_addone_literature_status.20261104.md)只代表其声明的有限检索范围。现有内部独立 LLM 分析不等于外部同行评议，不能据此宣布解决开放问题、文献优先权或投稿级新颖性。
- [先前平稳证明](../../v10_research/stationary_row_tilt_20261104_0023/stationary_terminal_kl.candidate.v1.md)及两份审查作为前序保存。中间 row-tilt 矩界的障碍不是 KL 风险下界。

## 本次公开过程

先核验原文件封存身份，再制作公开科学副本。只移除非数学准备路径和运行细节，保留原始/公开双重哈希和逐行对应；不改数学陈述，不用公开哈希覆盖历史审查绑定。完整范围、脚本使用限制与缺失记录说明见 [PUBLIC_EXPORT.md](PUBLIC_EXPORT.md)。

本批没有新采样、数值数学实验、训练或缺失原始训练记录的“恢复”。已有 CI 仅检查仓库公开字节清单，不重证定理。
