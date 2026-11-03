# 独立解析审查：pre-LN 全网风险与 copy 接口

## 摘要与哈希

对指定的标准点积、全因果、固定深宽和正 ε pre-LN 架构，完整末位 O(1/N) 敏感性及固定源 liminf TV≥1/32 的证明成立。单 copy 路径的 pre-LN 衰减、原始坐标布局的 post-LN 局部 O(i⁻²) 和 LayerNorm 模块界也成立。建议把 score 明确写为标准 q·k/√d，或只允许额外固定、与 token 无关且有界的偏置：若“只排除无界 score bias”被宽泛理解为允许依赖全段 token 的任意有界外部偏置，则它可能形成未计的侧信道。该建议是定义澄清；按标准点积及文中禁止旁路的自然解释没有发现数学错误。

- `preln_actual_risk_obstruction_v1.html` SHA-256 `037a0f737d8afc86ec65ebdd3321b9d324781dbf91c0c92229b7f593a6b030a7`。
- `layernorm_copy_scope_v1.html` SHA-256 `ca27f7a3a1e3baa2a38280b3bedddd9de846b765ea76a34f2310a89781e2664d`。

方法：对冻结源、哈希和所引原文的只读核查及解析推导；无实验、枚举、仿真、科学代码执行或源覆盖。结论不涵盖局部窗口、额外绕过、零 ε、长度增长的参数或其他文中排除的架构。

## 全网 pre-LN 敏感性

设 LN_ε(x)=γ⊙Px/sqrt(||Px||²/d+ε)+β，P 为去均值正交投影。其输出范数≤sqrt(d)||γ||∞+||β||₂，且 ε>0 时全局 Lipschitz 常数≤||γ||∞/sqrt ε。因而无论残差中的 token 无关位置向量多大，固定 affine Q,K,V 的范数以及点积 logits 均由独立于 N 的常数控制；每行 i 的每个权重≤exp(2C)/i。与 token embedding 相加的位置向量在相同长度的两输入中相同，初始末位差 δ₀=0，且因果性使更改位置 N−1 后所有更早位置在每层完全相同。

比较末位一个 head 时，先仅改变末位 query 和自身 key/value：LN 的 Lipschitz 界保证三者变化 O(δ_l)，对所有旧 key 的得分变化统一 O(δ_l)，故 softmax 权重的 TV 变化 O(δ_l)，值向量统一有界，输出差 O(δ_l)。再改变倒数第二位置的 key 和 value：它们虽可变化 O(1)，但该位置改变前后在两个有界-score softmax 下的权重均≤C/N，故额外输出差 O(1/N)。有限 head、固定输出矩阵、末位残差和仅接收 LN 的固定 Lipschitz FFN 导出 δ_(l+1)≤a_lδ_l+b_l/N。固定有限层数给 δ_L≤C/N。最后的固定 affine logits 加二类 softmax 对输入差全局 Lipschitz，即使共同 logits 含无界位置残差，仍有 |q₀−q₁|≤C′/N；若末尾另有正 ε LN，其全局 Lipschitz 界同样适用。

这一步不要求倒数第二位置自身残差有界，只需其 normalized K,V 统一有界。固定特殊符号数保持有效 key 数 N+O(1)。证明依赖 score 没有未计的 token-dependent 全局计算、全因果 support、固定位置顺序和固定网络；逐层同词长度比较允许位置向量随 N 变化但不允许它依赖被翻转的 token。

## 固定源的真实末态风险

令 θ_ab 表示下一位为 1 的概率，取 θ₀₀=3/4、θ₁₀=1/4、θ₀₁=θ₁₁=1/2。所有符号转移概率均在 [1/4,3/4]。固定任何长度 N−2≥2 的前缀，后续 00 和 10 各以至少 (1/4)²=1/16 的条件概率发生。这两条同前缀词只在倒数第二位不同，真实终端目标分别为 Bernoulli(3/4) 与 Bernoulli(1/4)，且最终 token 相同。因而条件预期 TV ≥(1/16)(|q₀−3/4|+|q₁−1/4|)≥(1/16)(1/2−C′/N)。对所有前缀与任意初始对律平均，得到每个固定网络 liminf 风险≥1/32。该链两步每个 pair 概率≥1/16，故 P²≥(1/4)Unif({0,1}²)，不可约、非周期，且可取其平稳初态；两个前驱为 0 和 1 的当前 0 行不同，确实严格二阶。

## Copy 路径和 post-LN

在第一层仅 Q/K 经 LN 的 full-causal 指定 head，比较仅目标 lag 的 token 改变的两词。该行 query 和其他 keys/values 一样，除目标项以外的归一化平均 μ 不变；目标项在两词中的权重 p,p′≤exp(2C)/i。若值范数≤V̄，则输出差≤2V̄(p+p′)≤4V̄exp(2C)/i；原 0/1 标量值下更紧为≤p+p′。因此一个固定阈值后的精确 bit 拷贝不能对两词都保持常数 margin。该局部结论单独不控制其他头或全网风险。

对于原始候选的 post-LN 第一块，原第一层注意力先看到未归一化位置，因此上述 bounded-score 论证不适用于这一 attention。其后的独立 i² 坐标保持原值，其他保留坐标最多 O(i) 且两个 copy 输出有界；u_i=i²e_sq+O(i) 有 ||Pu_i||≥i²||Pe_sq||−O(i)=Ω(i²)。两历史只在两个 copy 输出槽变化，每槽至多 1，故连接它们的线段上仍有 ||Pu||=Ω(i²)。该线段上的 LN Jacobian 范数 O(i⁻²)，从而首次归一化结果差 O(i⁻²)。之后若仅由该规范化状态输入固定 Lipschitz FFN 并保持其残差，再经过正 ε LN，O(i⁻²) 保持；不允许把此局部衰减扩大成所有 post-LN 网络的完整风险定理。

## 文献核对

[Hahn 2020, Lemma 5](https://aclanthology.org/2020.tacl-1.11.pdf) 原文已有单一非末位输入改变导致输出激活 O(1/N) 的影响机制，其证明使用固定网络及有界/Lipschitz 控制。冻结稿的区别是按指定 pre-LN 明确处理无界但 token 无关残差位置及给出具体同轨迹二阶源的 TV 损失；不应称一般机制原创。

[Chiang–Cholak 2022, Propositions 2–3](https://arxiv.org/pdf/2202.12172) 分别展示 ε=0 的 layernorm 可放大边界信号，以及 log N score scaling 的 FIRST 例子，后者亦讨论 ε>0；这些改变不属于本定理假设。[Veličković 等 Lemma 2.1 与 Theorem 2.2](https://arxiv.org/html/2410.01104) 分别涉及有界 logits 的稀释和其有限输入集架构，不能直接把后者的输入条件当成无界原位置的条件。较早 copy-only 文件保留了其时尚未由该文件自身解决的全网端点；新 pre-LN 文件仅在明示模型类内解决了该端点，不覆盖一般 post-LN。
