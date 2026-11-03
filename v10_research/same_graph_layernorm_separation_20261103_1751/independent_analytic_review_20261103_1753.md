# 独立解析审查：同图 pre-LN 结构分离及补充

## 结论与四件组绑定

主稿在其明确的 exact-real、same-input、same-non-LN-weights、正 ε pre-LN 与同一固定源范围内成立。坐标与 N=2 澄清正确；Yang 引文补充必须与 Lemma 7 精确范围更正合读。结论是插入 8 个 LayerNorm 运算的结构比较，不是相同 FLOPs、动态范围、误差或精度预算，也不是训练、post-LN 或一般 normalized Transformer 下界。

- `same_graph_structural_separation_v1.html` SHA-256 `047c4cb1b18b8f351ab382629902ab7f7fecef13a11eaddcd1c499267089722f`。
- `input_padding_boundary_clarification_v1.html`：`73cc7606cee34df051c4c5fbabcb744221c6579a5d7e46fad0993ef8b8c6f44b`。
- `yang_prior_art_addendum_v1.html`：`0eafa7de0a76300abd142ef798ebd0fd511ad6aea8b7bdd20bf9cfe3c9d9fb4a`。
- `yang_lemma7_scope_correction_v1.html`：`5b7874a4c1d97f89fd72e9ef82fa442c683c4c3ee3a38515b6bb1ec83169fc63`。

关键源：三块图 `4141725b160d74288570dd2d02181cb7d14c22d691ac7cf53b38c93f6bb409b8`；四块正向图 `bf7f6c3ab19472d83658a3dc5cf24b90514df96e145b578706504526045c14c8`；高斯速率附录 `d21062d3d1bf660a955bba10df9c466cf0eabaa61e57251236b8a870e15f9ad7`；pre-LN 全网负向稿 `037a0f737d8afc86ec65ebdd3321b9d324781dbf91c0c92229b7f593a6b030a7` 及其输入/score 澄清分别为 `b0e60b8b20d9224c0701f8e4f2e76b81f7d40e43c7366422d324037850e9ecbf`、`adc985442cc6c377caf0609d1ca96c5fba977507dbf226f0979ff42a9f0f089c`。

本次只读源与哈希、解析推导和公开原文核对；未做实验、测试、枚举、仿真、科学代码执行或源覆盖。该审查非形式验证、外部同行评审或新颖性认证。

## 相同嵌入、图形和参数

原三块图保留 (1,i,i²,x) 及内部 copy、gate、anchor 槽；四块图把 ln i 写到另一个未用槽，扩大到宽 128 而不与现有槽冲突。主稿所示五坐标可作为抽象排列；若与旧槽次序不同，取一次固定坐标置换 P，所有残差输入/输出共同应用它：Q/K/V 及 FFN 第一矩阵右乘 Pᵀ，attention/FFN 写回矩阵左乘 P，相应写回偏置亦左乘 P，终端读出右乘 Pᵀ。残差 identity 保持；LN 使用全 1 gain、全 0 offset 时满足 LN(Px)=P LN(x)。因此一次共同共轭只是统一重标记，既不依 token、源、N，也不引入 token×position 预处理；两图使用完全相同的置换后非 LN 参数 W。

两 BOS 都用 x=1/2、i=1,2，数据用 x∈{0,1}；两个 BOS/有效标记由原 FFN 计算，不是额外预处理。第一块的两个 copy T 门共 4 个 ReLU、BOS 和有效位置各 2 个，再增加首 BOS 标记 1 个，共 9；第二块各 4 个历史/实际情境指示共 8；第三块 4 个选择 ReLU；第四块 FFN 为零。均可补零到隐藏宽 9。四块每块配置 8 头、head-dimension 16；活跃 head 实例依次 2、0、5、2，共 9；未使用头及隐藏坐标补零，两个图相同。两个残差子层、q·k/4、全 causal j≤i、同一线性词表读出及普通二类 softmax 完全相同。G₁ 在每块 attention/FFN 前各插入完整 128 维 LN，故共 8 个，冻结 γ=1、offset=0、ε=10^(−5)，无需相同框架总参数槽数的错误声明。

## 共同源与两侧风险

θ₀₀(1)=3/4、θ₁₀(1)=1/4、θ₀₁(1)=θ₁₁(1)=1/2。对每个中间符号 b 和后继 c，Σ_a θ_ab(c)=1，因此 uniform pair 概率 1/4 平稳。单符号两种概率都≥1/4，pair 两步任意状态概率≥1/16，即 P²≥(1/4)uniform；有限链不可约非周期，当前位为 0 的下一步概率仍随前驱变化，故严格二阶。

G₀ 是零延拓/重排后的原图。其逐历史 `|P₀−B_N|≤(N/2)e^(−N)+min{1,168/sqrt(N+2)}` 直接来自原计数和高斯速率附录。对本固定平稳不可约源，各有限 pair 的历史访问频率趋正、行经验转移趋真实值，故 B_N 对随机真实末行的误差几乎处处趋 0；有界收敛得 R₀(N)→0。R011 可提供更强但此处非必需的均匀 O(N^(−1/2)) 率。N=2 无有效历史三元组、B_N=1/2、末位 lag-1 query 仍合法；只宣称误差界，不把输出断言为 1/2。

G₁ 完全属于所审 pre-LN 族：固定深宽、参数、正 ε，所有 Q/K/V 与 FFN 仅读 LN，位置源/token 无关，score 无额外偏置，末位 affine softmax 固定，前缀全 causal。末两词仅改变倒数第二 token 时影响≤C_W/N。对任意 N≥4 固定前缀，末续 00 和 10 各概率≥1/16，对应真实 Bernoulli 目标 3/4 和 1/4，故 R₁(N)≥max{0,1/32−C_W/(16N)}，liminf≥1/32。该全网负向适用于任意一个固定权重的此类图；不能交换成未受预算限制、逐 N 重新选择参数的 infimum。

## Yang 先例的精确边界

直接查看 [Yang 等 Lemma 7、Theorem 13(b)、Theorem 26](https://aclanthology.org/2026.tacl-1.8.pdf)。Theorem 13(b) 用 future mask、固定 τ(i)=1、位置特征包含 (−1)^i 和 i² 模拟 previous 逻辑，§4.1 确有 n-gram 语境；Theorem 26 用依赖长度与 score-gap 的温度调度给一般 hard-attention 模拟。Lemma 7 的具体式是在 γ≥1、整数 1≤t≤n、s_j=γ(2tj−j²) 下，`|t−Σ_j softmax(s)_j j|≤(3/2)e^(−γ)`，即**位置值期望误差**。原 addendum 的“localization error”若理解为任意 value 或 softmax TV 不够精确；必须和单独更正合读。该文是十分接近的二次位置与 attention/threshold 先例，但这些段落并未宣称本稿同非 LN 权重插入 pre-LN 后的固定随机二阶源真实末态 TV 分离。

保留所有 paid 位置、arithmetical precision 和模型范围：G₀ 既有专用长度增长精度整数后端不意味着 G₁ 与之在固定字长、动态范围、操作数或实际硬件上相同。结论不主张有限精度、FLOPs、训练或一般性先例优先权。
