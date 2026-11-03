# 独立解析审查：有限资源 pre-LN 风险界

## 结论与绑定

在冻结稿所列 full-causal、输入/score 无侧信道、正 ε、固定有限参数且数学运算精确的模型内，逐 head 扰动、残差差值、逐层递推、输出概率和风险常数、统一预算及最后的对数 score 上限必要条件均成立；界非常保守，不等于充分条件、实际硬件下界或同架构同预算分离。

- 审查稿 `finite_resource_risk_bound_v1.html`：SHA-256 `48fca04c400e61e49af8e9deb2dfbb5a1fb97466c69469c4593de7bef6664d2d`。
- pre-LN 主稿 `../layernorm_position_interface_20261103_1726/preln_actual_risk_obstruction_v1.html`：`037a0f737d8afc86ec65ebdd3321b9d324781dbf91c0c92229b7f593a6b030a7`。
- 输入量词澄清 `../layernorm_position_interface_20261103_1726/input_and_quantifiers_clarification_v1.html`：`b0e60b8b20d9224c0701f8e4f2e76b81f7d40e43c7366422d324037850e9ecbf`。
- score 接口澄清 `../layernorm_position_interface_20261103_1726/score_interface_clarification_v1.html`：`adc985442cc6c377caf0609d1ca96c5fba977507dbf226f0979ff42a9f0f089c`。
- 比较的 no-LN 源 `../fixed_parameter_position_decoder_20261103_1632/fixed_parameter_causal_candidate_v1.html`：`4141725b160d74288570dd2d02181cb7d14c22d691ac7cf53b38c93f6bb409b8`。

只读源、哈希和解析计算；未做测试、枚举、仿真、科学代码执行或源覆盖。B_l 表示步骤系数，不与 LN 偏置混淆。

## LN、残差和单层 head

正 ε 的 LN 输出 Euclidean 范数≤B^a 或 B^f，Lipschitz 常数≤G^a 或 G^f，故经固定 affine 映射的 Q,K,V 及 aQ,aK,aV 取值与变化界均正确，|score|≤S，每个 causal 权重≤e^(2S)/N。head 输出是 V 范数球内的凸组合，其固定输出映射和偏置使 attention 分支范数≤G_l；FFN 的 ReLU 与 affine 范数使其分支范数≤U_l。比较相同位置的两条历史，位置残差抵消、初始差为 D₀；每个分支差至多其各自绝对范数之和，因此改动位置在第 l 层前差≤D_l=D₀+2Σ_(r<l)(G_r+U_r)，无需假设位置残差有界。

先更换末位 query 和其自己的 key、value。用 q'k'−qk=(q'−q)k+q'(k'−k)，并在任一词使用 ||q||≤Q, ||k||≤K，全部得分差≤(K aQ+Q aK)δ_l/√d_h。沿 softmax 线段，Jacobian 满足 ||Jv||₁=Σ_i p_i|v_i−Σ_jp_jv_j|≤2||v||∞，故权重 L1 变化≤两倍最大得分变化。值输出范数≤V，而末位 value 自身变化≤aV δ_l（权重至多 1），得到 c_lh δ_l。

再只更换倒数第二 key/value。该 key 的得分差≤min{2QK/√d_h, Q aK D_l/√d_h}；value 差≤min{2V,aV D_l}。其他项与 query 固定，单 score 在两端都属于 [−S,S]，其线性插值亦如此。该项 softmax 概率导数 p(1−p)≤p≤e^(2S)/N，故其质量变化≤(e^(2S)/N)|Δscore|。把输出写为 (1−p)μ+pv，μ 不变且 ||μ||,||v||≤V，得输出变化≤(e^(2S)/N)[2V|Δscore|+||Δv||]，即 t_lh/N。确定性 source/token 无关偏置在两历史完全相同，不在 Δscore 中。

有限 heads 经相应 output operator 后求和；注意力残差加一，再经 FFN 加残差的 Lipschitz 因子 F_l=1+||W₂||||W₁||G^f，得到 A_l 和 B_l 及 δ_(l+1)≤A_lδ_l+B_l/N。δ₀=0 逐层展开得到 Σ_l B_l∏_(k>l)A_k /N。对于每个有限 N 的网络可以单独计算这些常数；当网络随 N 改变时，不能把它们当成同一有界常数。

## 输出、风险和统一预算

二类 softmax 的输出 1 概率为 sigmoid((w₁−w₀)·x+b)，其导数≤1/4，故 R_out≤||w₁−w₀||/4；末尾正 ε LN 若存在再乘其全局 Lipschitz 常数。固定二阶源给定任意长度 N−2 前缀，00 与 10 各概率≥1/16，真实末态概率为 3/4 与 1/4。三角不等式得到风险≥max{0,1/32−C_model/(16N)}。因此若风险≤r<1/32，则必有 C_model≥N(1/2−16r)；对每个按同一个显式 C_budget(N) 限制的模型统一成立，可在该有限 N 的预算类内取 infimum。

在 §5 的统一 caps 下，Q,K,V≤R=W(B+1)，aQ,aK,aV≤WG，S_head≤S=R²+T。去掉 √d_h≥1 的分母并对单 key 差用饱和上界，c_lh≤WG(4R²+1)，t_lh≤e^(2S)(4R³+2R)，F_l≤F。加上 H 个 output operator≤W，逐层 A_l≤A、B_l≤B_step。若输出 logits 组成的矩阵谱范数≤W，||w₁−w₀||≤sqrt(2)W，因此 R_out≤W/(2sqrt 2)≤W/2。由于 A≥1，Σ_l B_l∏_(k>l)A_k≤L B_step A^(L−1)，得到冻结稿必要不等式。

固定其他资源 cap 与 r<1/32，仅允许 token/source 无关偏置 cap T 增长时，右边为与 N 无关正系数乘 exp(2S)；若风险条件可满足，则 S≥(1/2)ln N−O(1)。若其他预算随 N 改变必须重新代入，且这只约束保守上限 S，不断言某个实际得分、温度或其它资源各自必须以此速度增长；必要条件也不代表足够。

## 比较和范围

no-LN 源直接将 (1,i,i²) 送到 Q/K，使原始 first-block 项 O(N³)、实际相对 lag gap 随 i 增长；四块扩展另支付 ln i。它不属于 LN 强制约束，所以冻结稿把比较称为结构模型分离而非同架构、相同 score 范围或同计算预算下界，是准确的。该报告亦不覆盖 post-LN 首注意力、局部窗口、源依赖或 token×position 侧通道、零 ε、训练或常规 IEEE 实现。
