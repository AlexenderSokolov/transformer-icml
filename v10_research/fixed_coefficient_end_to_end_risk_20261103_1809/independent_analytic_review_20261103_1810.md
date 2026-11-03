# 独立解析审查：固定系数偏差的端到端风险

## 结论和绑定

对每个固定整数 q≥1，冻结稿的单权重变更、索引漂移、非平稳索引计数、原 anchor/最终词表 softmax 以及固定源真实末态期望 TV 极限 3/16，均通过解析核查。该结论针对指定的精确实数四块图和 η=1/(2q) 序列，不自动推广至所有 η、所有架构或 IEEE 浮点。无新颖性认证。

- `drift_risk_counterexample_v1.html` SHA-256 `7e41058add6b41818414502fd83bc4959da6f30ae57c1be3c4af6fc3f8689821`。
- 四块源 `../fixed_parameter_vocab_softmax_20261103_1639/gaussian_log_position_candidate_v1.html`：`bf7f6c3ab19472d83658a3dc5cf24b90514df96e145b578706504526045c14c8`。
- 全 p 高斯速率附录 `../fixed_parameter_vocab_softmax_20261103_1639/rate_improvement_addendum_v1.html`：`d21062d3d1bf660a955bba10df9c466cf0eabaa61e57251236b8a870e15f9ad7`。
- 三块边界说明 `../fixed_parameter_position_decoder_20261103_1632/boundary_and_prior_addendum_v2.html`：`25dd4ff06226867aa79578766ac7eeaf41cd4a5fef59dd9c77d896120d908ee4`。

本次只读源、SHA-256、解析推导及来源比对；未进行测试、枚举、仿真、科学代码执行或源覆盖。LLM 审查非形式验证或外部同行评审。

## 单参数、圆整与门

第一 copy 头第二 query 坐标原为 −4i、相应 key 为 j²、score 除以 4；将这一权重乘以 1+η 后恰得到 `2i(i−1)j−(1+η)ij²`，绝对变化为 4η=2/q，其余 W 和 h=2 头保持。设 λ=2q/(2q+1)，配方平方后中心为 λ(i−1)。该中心分母为奇数，距任何半整数至少 1/[2(2q+1)]；因此最近整数唯一，次近整数的平方距离差≥1/(2q+1)，乘 (1+η)i 后 gap≥i/(2q)。其他任何整数距离不更优，每个错误指数权重最多 exp[−i/(2q)]，总泄漏≤i exp[−i/(2q)]→0。对足够大 i 最近键是合法数据位置，误差小于 1/4，固定 T 门确切返回其二值。

数据 X_k 在位置 k+2，故实际漂移 `f(k)=round(λ(k+1))−2`。它满足 f(k)=λk+O_q(1)，且 k−2−f(k)→∞ 线性增长。未改 lag2 在所有有效候选 k≥3 返回 X_(k−2)。晚历史的 context gate 恰为 `(X_(k−2), X_f(k))`，实际终端 query 恰为 `(X_f(N), X_N)`。较早有限个位置不要求门整值，但所有 gate∈[0,1]；两个 BOS 仍不受影响且固定 b=1，故早期异常最多造成 O_q(1) 个相对权重，而不被误当成零。

## 非独立两块统计

固定源的 pair 平稳律均匀，P²≥(1/4)π，故各段间 TV mixing 可用 d(t)≤(3/4)^floor(t/2)。固定 k，X_f(k) 与区间 X_(k−2):k 的距离趋于无穷，前者趋于独立的均匀 bit，后者保持平稳。又 pair 平稳均匀，所以在给定 X_(k−2)=0 或 1 后，中间 X_(k−1) 均匀，得到 r₀=(3/4+1/2)/2=5/8、r₁=(1/4+1/2)/2=3/8。于是 J 单项期望趋 1/4，C 单项期望趋 r_a/4，Cesàro 平均同极限。

对两个统计项把其参与的时间块写为早单点 f(k)、晚区间 [k−2,k] 和相应 ℓ 两块。取 R 后去掉前 O_q(R) 个自身早晚距离不足 R+2 的 k。若跨项四类中心距离 `|k−ℓ|, |f(k)−f(ℓ)|, |f(k)−ℓ|, |k−f(ℓ)|` 任一≤R+3，记 bad。f 单调、斜率 λ>0 且值域纤维大小统一有界（本族至多 2），所以每个 k 的 bad ℓ 为 O_q(R+1)，总 O_q(NR)。其余两项各自内部及彼此块按时间排序都相距至少 R 减固定长度；最多四次有限块由均匀 pair-chain mixing 逐次解耦，协方差为 O(d(R−O(1)))。因此归一化方差为 O_q(R/N)+O(d(R−O(1)))；取 R=floor(sqrt N) 后趋零。此为依概率收敛，可对有限四行及两类计数取并，不需声称这些采样项独立或其比率几乎处处收敛。

## 原 anchor、最终 softmax 和风险

晚期正确 anchor match 与两 BOS 的块 3 score 都为 N，非匹配晚期 score 为 0。有限早期 gates∈[0,1]，除以 e^N 后每个权重≤1，合计 O_q(1)；其余不匹配总权重≤Ne^(−N)，values∈[0,1]。由 J_ab/N→1/4，有限早项、BOS 和非匹配均使经验比率仅变 o_P(1)，故四个 anchor 联合趋于 r_a。末端 query 是 `(X_f(N),X_N)` 的 onehot，ReLU 选择所得 p_N 满足 p_N−r_(X_f(N))→0 in probability，且 p_N∈[0,1]。

原第四块的长度标记与 ln 位置值不受所改头影响，高斯 lemma 对每个 p∈[0,1] 逐词统一给 `|P̃_N−p_N|≤min{1,168/sqrt(N+2)}`，包括随机 p_N。因此 P̃_N−r_(X_f(N))→0 in probability，并由 [0,1] 有界而在 L1 收敛。由 N−f(N)→∞，均匀 mixing 使 `(X_f(N),(X_(N−1),X_N))` 趋于独立均匀 bit 与均匀 pair。最终期望 TV 的极限为

`(1/8) Σ_(a,u,v) |r_a−θ_uv(1)| = (1/8)(6/8+6/8)=3/16`。

这是真实末状态的无条件平均，不是把局部 snap 出错直接当作最终风险。任取 q 再令 N→∞，而非让 η 随 N 改变；q 可先任意大以使非零单权重误差 2/q 任意小。一般 η 的中心可能逼近半整数，当前证明没有覆盖。

## 先例范围

[Liu 等 Proposition 4 和 C.3](https://arxiv.org/abs/2306.00946) 讨论不同 flip-flop 任务中线性位置系数导致错误注意力位置，并没有在本稿范围下自动推出最终 TV 风险。[Chen 等 Theorem 3.6 和 C.5](https://arxiv.org/html/2409.10559#S3) 分析其训练阶段和 GIH 整体近似误差；[Castin 等](https://arxiv.org/html/2312.14820#S4.SS2) 的 attention 光滑性在其有界输入等条件下成立。差异是问题、网络、输入范围和风险接口；未作穷尽检索或原创性判断。
