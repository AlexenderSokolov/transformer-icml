# 研究者中文综合备忘 v2：独立解析审查

## 审查结论和字节绑定

备忘 v2 在所声明的内部研究、独立 LLM 审查及待发布范围内，与已核查的承重源、统计量词和先例一致；未发现尚未修复的承重数学错误。v2 对照 v1 的变化限于版本标记、注明合并两项更正，以及纳入快混合硬源包含条件与 pre-LN 偏置独立条件。原 v1 和两份更正均保留。以下不是形式验证、人类同行评审或穷尽文献搜索。

- `research_memo_v2.html`：SHA-256 `f65db2fed6d691fd8f7bfd785e58f03c8e6e5e2711be6128e470e7e7e617c0eb`。
- `research_memo_v1.html`：`b7f4a68d1282bf7d7e7acb7e15617a8eec679ea4e7aab78007d002d923c7e3b8`。
- `fast_mixing_scope_correction_v1.html`：`dd09754e7f1443ddbf22dcac33afe964edb49ac4606300dc09d2ddeb56584ea0`。
- `preln_bias_scope_correction_v1.html`：`d528283457211ca21533cf6a399e6c196d3a1043f4be7d78872926794fe6e164`。

本次只读源、查哈希、解析比较及核对所引文献；未测试、枚举、仿真、执行科学代码或覆盖源文件。

## 四块、精度与统计

二元 exact-real 图的 4 层、宽 128、每层 8 头、2 BOS、(1,i,i²,ln i) 输入、真实末态和逐词误差 `(N/2)e^(−N)+min{1,168/sqrt(N+2)}` 与候选及改进率文件一致。N=2 的 add-one 目标为 1/2，但无需把实际数值输出当成严格 1/2。有限 A 采用 A 个 onehot BOS、A² 情境头、A 个第四块头、每层 A²+1 个分配头和 O(A³) 宽，逐词误差 `Ne^(−N)/A+min{1,84A/sqrt(N+A)}`；每个固定 A 的权重不随 N 变，跨 A 不声称单网络。

整数后端精度 `b=32 ceil(log₂(N+2))`、支付 ln i 和 exp/归一化、二元 bit-work `O(N²log³N)` 与 streaming bits `O(Nlog N+log²N)` 均与指定后端一致。它是随长度增加精度的专用精确整数方案，不是固定字长 IEEE、GPU 实测或训练保证。一般 A 的详细资源另在候选文件中计数；备忘没有把该 A 因子声称为常数。

平稳有界逆混合类的 add-one 上界与包含对应硬族的类的 A³ minimax 下界匹配；不能对任意严格子类推出下界，v2 已吸收该必要条件。任意初态的 MM5 clock 和 R011 给 A⁵ 级别，且其风险是对整个同轨迹 actual-terminal 的均值；初态和难源可按问题规模选。转移正化仍无跨规模统一混合常数。A⁵/N→0 是 A 增长时该已证整体上界的充分条件，不是必要或最优阈值。

稀有 u 行对应 `rare_unknown_u_addone_20261103_1502/unknown_u_addone_matched_rate_v1.html`，SHA `37a1b01e27f315097c5c910005605b877ba9b6d0de160940c7acc375b6af849b`：同一个 add-one 规则不读取 u,t，在该特定平稳二元族、条件 S_N=00 的风险≤157/sqrt(1+(N−2)u)；相应两点下界甚至允许已知 u。故备忘中的 N 级简写与范围正确，不应误用至所有源或无条件平均。

## Pre-LN、先例和已知来源缺口

固定正 ε、固定网络、full causal、token/源无关位置和统一有界 token/源无关 score bias 的风险陈述符合主稿及 score 接口澄清；每一固定网络在同一固定源上的 liminf≥1/32，不能交换成无限制的逐 N 网络 infimum。有限 N 的 `max{0,1/32−C_model/(16N)}` 及必要条件 `C_model≥N(1/2−16r)` 与已审资源账本一致。no-LN 构造是结构对比，不是相同 score、计算或精度预算的分离；post-LN 的局部复制信号衰减也没有被转述为全网风险定理。

直接核验 D’Angelo Corollary 4.1 是 BOS 引出的 β→∞ 对称 add-α 形式；Ekbote、Rajaraman 的链接对应其 conditional k-gram / 层数构造；He 等所链的 BiPE 论文 Appendix A.1 确实含 q=(1,i²,i)、k_j=(−j²,−1,2j)，给 −(i−j)² 的位置复制机制。Han–Jana–Wu 先例是平稳同轨迹 KL，不可反向用 Pinsker 得 TV 下界。Hahn、Barbero、Chiang–Cholak 和 Makkuva v2 先例范围与既有独立审查一致；列示不是穷尽搜寻或原创性证明。

D’Angelo 最早 AUDIT 完整字节未保留、Route B 两次原始搜索无同期逐路径完整记录、MM5 旧审查请求哈希与当前可读证明哈希不一致，备忘均未声称恢复；BT002 旧标量草稿与诊断改写可由 `binary_erasure_transport/BT_STAGE8_PROVENANCE.md` 的记录支持。已保存的后来重放或独立解析不是旧原始记录，LLM 审查亦非正式验证。内部文件的短哈希仅为提示；正式外发前仍需建立含依赖、澄清、可访问性的完整版本化包。本文无权证明外部发布已发生或证明所有潜在现有文献均已查全。
