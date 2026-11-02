# 固定版本独立审查 v1（review-only）

目标为原根 `4f974bc0673ee0456e1ba3acbe18fd194e9f8f8fa0a29e4d2ed8c2296f52c140`，contract `3aa0ff5ddc4dd7295ab94404797636c9f50fa30cd6e7249cc5f98467b5f1179a`。本稿是一次有界审查，不是根接纳、完整优先权证明、重新提交既有 Fact 或新 Fact。冻结根和 D1–D8 不改。

**结论：v2 的三篇指定原文比较及三个 primitive 计算，在其限定范围内成立；精度 Fact 的指定关键环节未发现具体反例。中心贡献的新颖性尚未确立。若中心定理声称“同一扩展实现同时具有 general-D1 定位误差保证和规范 floor 精度分类”，九个冻结 Fact 之间仍需要一个实际的 floor 移植/组合命题。兼容 Fact 已经接好了扩展后端的 adversarial-center 路线，不能把这个缺口说成该 Fact 未完成其自身义务。**

## 1. 固定输入、原生证据及本轮边界

首先对实际 `../lead/fixed-review-manifest-v2.json` 计算 SHA256，等于用户给定的 `351e1a25691f28ce006232a3457276fb4e5565abcfd3a6c6752acf7a24bf4add`。清单固定的九个 Fact、十个其他文件和七个 source 文件共 26 项，实际哈希全部匹配。逐文件 expected/actual 记录见 [input-hash-audit.json](input-hash-audit.json)，本稿附录也逐项列出。活动比较稿为 `checkpoint-v2.md`，SHA256 `68c9f271889faf2e48e95618f0373f5f67434b5cdf4a40e1548c60fbc35cb640`；没有用 v1 覆盖 v2 的修正。

原生 `research_state` 核实根为 OPEN、acceptance=null，九条既有证据均为 `LLM_CHECKED_PROOF/PASS/VALID`。特别是：

| Fact | 原生 evidence ID | 本轮判断的含义 |
|---|---|---|
| `54c3088eb3c35a36` | `7064d5bc355688b040e8065a1e9246656739701d730b4deb0ea3ccdbee37666f` | 已接纳；本轮抽查关键证明，未找到撤销依据 |
| `199c7b2000c58e6b` | `15f24ebaff4309f7972c662c27a39e0fa9a89854d3d154847e4e0207f383b9fc` | 已接纳；本轮只审查其与旧 floor 结果的接口，不重复派出其全文审核 |

九条 evidence ID、对应实际内容哈希和预算另存 [native-evidence-audit.json](native-evidence-audit.json)。精度 source proof 确为 421 行，SHA256 `6f82fa1923608b564575e0fe2cd4f14d8e66d90874f7657c28ec8b131fab7423`，且其完整正文逐字包含在对应 Fact 中；Fact 文件因包含原生上下文有 447 行。本稿以下 `L` 行号均指实际 Fact 文件，避免把两种行号混用。

这是固定版本的独立 LLM 科学审查，不是形式化验证；未在本报告中产生新的数学接纳或最终审计。私人模型路由与运行预算不属于公开证据。

本轮没有重新完整证明九个 Fact：主要阅读精度证明的实现、相位、风险、分辨率和缩放各段，以及兼容 Fact 的编码、切点、cap、中心下界和比较接口；其他依赖以原生接纳和必要接口为准。文献只核查下述指定原文，不把未读的全文/附录默认为通过。

## 2. 三篇指定 primary 文献与数学替换

### 2.1 Rajaraman：比较正确，须同时保留两个有限精度 remark

核对官方 NeurIPS 2024 PDF 的 Definition 1（印刷 p.3）、Theorem 2/Remark 1（pp.5–6）、Theorem 4/Remark 2（p.7）、Theorem 5（p.9）和 Appendix A/A.1 的相关构造。Definition 1 正是按最后 k 个符号条件化的经验分布，**分母非零时才定义**。Theorem 2 给两层、k 头，宽度 `(k+2)|V|+k+1`；Theorem 4 给三层、每层一头、相对位置和 LayerNorm，宽度 `O(|V|)`。这些已经排除“浅层能表示条件频数”作为独立新贡献。[官方 PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/f8a2070082ad05b4deeff4ffb4312a6f-Paper-Conference.pdf)

Remark 1 对 Theorems 1–3 明确陈述 `O(log T)` 位和 `O(1/T)` 加性误差；不能写成这篇完全没有精度论述。Remark 2 对 Theorem 4 明确说证明没有界定有限 bit precision 导致的误差，其后“应足够”的讨论不能升级为完整位级实现定理。Appendix A/A.1 用 attention scale 趋向无穷。Theorem 5 是一层、有 LN/FF、三元输入、逐串逼近 conditional 3-gram 的确定性限制：误差 `1/(3T)` 下 `2pH+dp+2 >= T/3`。它不是 D5 的固定正概率过程/实际末查询 TV 风险下界。核对到 theorem statement 和相关 reduction/limit 段落，未独立重做整个通信复杂度归约。[同一原文](https://proceedings.neurips.cc/paper_files/paper/2024/file/f8a2070082ad05b4deeff4ffb4312a6f-Paper-Conference.pdf)

### 2.2 D'Angelo：v2 的 lag 置换与实际末查询公式正确

直接读取并交叉核对冻结快照和原文 Definition 3.1/Proposition 3.1/Eq.(8)：

`M_j^(T)={r∈[k]: x_(T-r+1)=x_(j-r)}`。

无 BOS 时 `k'=k+1`，故 `k=2,T=N` 的候选恰是 `j=3,...,N`，包括最后一个历史例子；query 是 `(x_(N-1),x_N)`。`r=1` 比较最近项 `b=d`，`r=2` 比较较早项 `a=c`。为避免与本地 β 混淆，记 paper 参数为 α，则确为

`α1=2β2, α2=2β1`，

`α2·1{a=c}+α1·1{b=d}=β1 ac+β2 bd+(β1+β2)`。

公共指数因子抵消，Eq.(8) 无 BOS 的分子/分母按四种 mask 分组，严格等于

`Σ_z exp(β1 ac+β2 bd) A_N(z,y) / Σ_z exp(β1 ac+β2 bd) μ_N(z)`。

这与本地 Fact `33e7d01a130b6858` L38–89 的 nominal finite-history B 一致，所有历史成立，零 context count 不妨碍正分母。这里比较的是**实际末查询的统计算子**；不顺带授予论文一个任意外插 query 的完整电路，不把它的 copying、残差或数值码等同于本地付费实现。Eq.(8) 的逐串表示结论也须与论文的 task-prior/均匀初始 context 实验分开；本地 stationary、每 fixed θ 的风险量词不能由 prior 平均最优性直接推出。[Definition 3.1/Eq.(8)](https://arxiv.org/html/2607.02800v1#S3.SS1)

原文 §3.2.1 的复制明确采用 positional gap 趋向无穷；Appendix D.3 对 ratio/population 替代使用近似和额外假设。因此不能用该附录的均值近似代替本地有限随机路径或 endpoint 风险证明。文献 overlap 是确定的，新的有限码保证并不由公式相同自动获得。[原文 §3.2.1 与 Appendix D.3](https://arxiv.org/html/2607.02800v1)

### 2.3 Zhou：计数恢复确为明写先例

读取冻结 v3 HTML 的 §4.4 Theorems 3–5，并核对 G.2.2 的公式 (37)–(38)。第一层复制过去符号，第二层收集 forward/backward normalized statistics；原文显式恢复

`n_(i,s_(i,l))(a) = i · g_(i,s_(i,l))(a) · Π_(j=0)^(l-1) g^←_(i-1,s_(i,j))(x_(i-j))`。

式子是计数比的 telescoping product，`i` 由位置提供。后续 D 个递归层形成 CTW Bayesian 混合，总计 D+2 层，FF 需要足够表示能力。故“从归一化 attention 配辅助量恢复 count”已有明确原文，不构成新增贡献。[§4.4](https://arxiv.org/html/2410.05493v3#S4.SS4)

其对象是给定 CTW prior 的 variable-order Bayesian predictor；本文是 fixed unknown D1 的 TV 分类。该差别不能推出本文资源或风险优于 CTW。G.2.2 亦采用 attention scale 极限，本文没有审出其有限码端到端 cap；也未重做整个 G.1/G.2 或所有零计数情形。本地显式编译不能简单称为推翻/改进 CTW 定理。[同一版本](https://arxiv.org/html/2410.05493v3)

## 3. 两个 kernel/复制检查的精确范围

**四 mask 乘积关系正确。** 用 `(m1,m2)` 表示两个精确匹配位，A 的权重为 `(1,1,1,e^β)`；单个 additive-score head 的权重（除去公共正因子）为 `(1,e^α1,e^α2,e^(α1+α2))`。后一组必有 `w11 w00=w10 w01`，前一组在 β>0 不满足。所有四种 context mask 在 K>=2 的符号空间存在。这仅排除“一个逐项 additive kernel 在四 mask 上直接换参数成为 A”；不排除 K² 联合特征、更多 head、另一个 readout、不同可见历史约束下的等价实现。

**有限 gap 复制误差公式正确。** 精确 primitive 是 m>=2 个实际允许位置、目标 score g>0、其余 score 0、identity one-hot values、没有后处理校正。目标值为一个符号、其余全部为另一个符号时，TV 恰为

`(m−1)/(e^g+m−1)`，

对 `0<ε<1`，误差<=ε 等价于 `g>=log((m−1)(1−ε)/ε)`。不能将其提升为有 FF/硬掩码/其他值编码的所有网络障碍。每个这样的有限符号串在严格正 D1 下具有正概率，**这不提供随 N 统一的正随机风险下界**。本地 singleton mask 是另一个已付费 primitive，唯一允许位置给精确权重 1。

v2 的 direct-A contamination 公式也正确：有 `m>0` 个匹配例子时，`Bmass=(M−m)/(e^β m+M−m)`，head 为 `(1−Bmass)P_emp+Bmass R_nonmatch`，TV 等于 `Bmass·TV(R_nonmatch,P_emp)`。`m=M` 时误差为零且无需定义 R_nonmatch；`m=0` 时 P_emp 未定义，不能使用此式。无 worst-history 两端分布分离条件时，`Bmass<=ε` 是充分准则，不是每个历史的必要准则。这些边界与 v2 的限定相容。

## 4. 精度 Fact 54c3088eb3c35a36 的重点抽查

以下结论以其已接纳状态和指定接口为前提；没有无证据撤销。

| 审查点与实际位置 | 结论与精确依据 |
|---|---|
| 完整规范码和擦除，L63–88、143–192 | Q_b 作用于 q 两坐标、r 两坐标、全部 μ 及所有可读 aggregate copies；不是只保留 plus 坐标。输出固定 `b+1` 位分子、公共分母，旧分母/码长/标志/padding/scratch 都须清掉。真 N、query、末两项仍在。式 (6) 的整数长除法对 `0<=A<D` 由 `2^i A=nD+r,0<=r<D` 归纳；`A=D` 单独输出 endpoint。不能把不连续 real floor 当作一个免费 ReLU。已给出位门/擦除 cap。本轮未物化其极大的完整电路，但未发现该构造的具体算术断点。 |
| 非空 phase，L194–228 | `v=(m+1/2)δ`、`(2^b−m) mod 3∈{0,1}` 保证 w 的小数部分为 1/6 或 5/6，r*=2w 为 1/3 或 2/3；j=2 被合理排除。序列 (18) 的奇偶选择确保任意稀有尺度都有可行 b。`δ<=v/[512(c+1)]` 蕴含 `δ<=a_v/16`，其中 `a_v=v/(c+v)`。不是任意 grid phase 定理。 |
| 两点确为合法规律，L218–228 | 先把 q*(1/2) 移到所在格的中点，再取 `Δ=δ/(4a_v)`，两端 q* 距中点 δ/8。`|t0−1/2|<=1/32`、`Δ/2<=1/128`，两 t 均严格位于 D5 区间。两个 q 坐标同时处在相同格，补数不是遗漏的额外信息。 |
| 真随机历史和 endpoint，L230–280 | 唯一事件 G_h 是八个合法 edge count 的联合事件，非 iid 自由统计量。取 `h=δ/(48Cγ), ζ<=δ/48` 后，q、μ、r 各自有严格 cell margin。`p_h<=αv` 给每一 endpoint 的条件失败概率<=α；因此给定 query=00、保留 endpoint=e 的整份码为同一 atom。对随机 decoder 用同一 atom 上的三角不等式成立。 |
| 固定 b 的量词，L282 | 固定 β,b,v,t±，令前端 J_N 增大，可得 `liminf_N max_± R_± >= Δ/2`（actual 则为 vΔ/2）；至少一个固定 sign 的 `limsup` 达此阈值。允许 decoder 随 N 交替，不能换成某个固定 sign 的 liminf。这里写法正确。 |
| 条件与实际加权风险，L266–280、307–316 | fixed/conditional 下界是 `(1−α)(c+v)δ/(8v)`；actual 下界是 `(1−α)(c+v)δ/8`。实际风险严格为 `Σ_s π_s R_cond(s)`，先将两 sign 的加权风险相加再 max；不逐 context 选择不同最坏 sign。没有假设 query/history 独立，也没有拿 `Σπ_s R_fix(s)` 当 actual 恒等式。只使用 00 的贡献，未擅加 q10。 |
| 同族上界和 sample 区域，L284–341 | 式 (30) 直接减去同历史 reference，避免二次放大 sampling error。由 `[4(c+1)ζ+8(c+1)δ+4d0]/π_s` 加 projection/compile/smoothing 得式 (33)。actual bad event 只付 p_h 一次。式 (34) 给非空、保守的 `δ^−2 log(1/δ)` sample 区域；不是最优 rare-count rate。 |
| summary 与 output 分别必要，L343–383 | output-grid midpoint 选择对 b_out=0,1,>=2 都合法；对每次实际 emitted vector 的 TV，随机化不能绕开 `d_out/2`。summary 两点与 output 最坏 t 可不同；在同一 t-class 上可取 lower 的 max，不能相加。actual output lower 仅 `v d_out/2`。因此 (39)–(42) 的区分正确；b 不等于总 B_arith 或 B_param。 |
| growing schedule，L385–415 | 对所有二元 histories、包括零计数，(43) 以 λ=1/M 控制分母；(44) 的 J_N,b_N,b_out,N 不依赖 θ。与既有 reference 强律组合得到 max-context、actual 及 conditional 期望结论。后者需除以固定 `πθ(s)>0`，不是跨 θ 的统一条件风险速率。此 floor theorem 的实现/一致性分支仍是二元范围。 |
| S 缩放和共同总字长，L417–435 | 对真实有理 z∈[0,1]、非负整数 k、S=2^k，Q_b 在完整 [0,S] 上运行且不饱和，有 `S^−1 Q_b(Sz)=Q_(b+k)(z)`，包括 endpoints/ties。必须重新规范为 `(n;2^(b+k))` 并清掉旧 scaled codes。需要 `b+k+1<=T_bits`，公共分母、系数、scratch 和 range 均收费；固定 b 的改善购买了 k 个范围位。按同一总字长是位分配相同，非新核的信息收益。 |

两个需要在综合稿继续保留的条件，不是已发现的 Fact 反例：

1. L427 的“整份 observation 相同”同时要求**公共字段约定也相同**。若两个独立编译的 family 在 padding、family-index 或公开 b/k constants 上有不同确定性标签，aggregate canonical blocks 相等仍成立，整串通常只通过已知 public-field relabeling 等价。要比较任意 decoder 的信息可用这种可逆转换；要说“同一 decoder 字面输出相同”，必须先统一字段。不能让任意 decoder 读取不同公开标签后还断言输出逐字相等。Fact 的 side-information-identical 前提不能省略。
2. 该 quantizer 的原始输入域是非负 [0,1]。若把 general-D1 的物理注入放在 floor **之前**，可能出现负数或 >1；必须扩展 signed/off-event floor 或明确先 clip 的新顺序，不能直接复用非负长除法。单独已接纳的干净 floor 实验不受此问题反驳。

精度、scale 与合法输出的结论只针对上述已付费接口。output grid 可输出零，TV 收敛/正值 grid 之前的 smoothing 均不自动给出统一期望 log-loss 结论。

## 5. “single compatible chain”实际还缺什么

**已有可直接组合的部分。** Fact `0bf422aeee139e59` 的 general-D1 joint-count/located-error upper，和 Fact `199c7b2000c58e6b` 明确固定的新后端、切点、全码 transport、非循环 input cap，是同一条扩展机制。199 的 L29–41 使用 `E_R(ell)=Σ_(j<n)(ell+R)^j/j!`；54 的 L54–61 使用不同的 `ell+1` 多项式。199 的 L53–79 证明每个 endpoint 下的完整观察因子化 `O_f=F_f(B',D_f(s,e))`，L219–271 给新的 adversarial-center lower/upper，L307–330 对其 S 扩展和共轭编码作独立限定。因此**扩展机制上的 adversarial-center T1–T3 接法已有实质证明**，不能将它误报为仅行政交接。

**不能直接组合的部分。** `|q_old−q_exact|<=ζ_old` 和 `|q_new−q_exact|<=ζ_new` 不蕴含 `Q_b(q_old)=Q_b(q_new)`。例：参考值 1/2，两个有理近似 `1/2±e`，`0<e<2^−b`，误差同样小但 floor 分属不同格。这是对“仅凭误差界即可逐码认同”的逻辑反例，**不是声称某个已核实真实历史已反驳其中一个 Fact**。199 的 center-map 可把不同码强制覆盖成同一码；固定 floor 没有此自由。

若中心 statement 包含扩展后端的 floor 精度分类，最短的下一数学单元是下面的 **移植命题**，而非重新证明两份原 Fact：

> 对每个 K,β,N,J,b（和合法 S=2^k<=M），固定 199 的 before-copy cut。把其 q_new、r、μ 全部替换为同一个 Q_b 的完整规范码，保留 D_f(s,e)、清掉全部旧 aggregate/denominator/length/padding/scratch，不再读历史。给出实际有限 rational-word floor 编译与非循环放大的共同资源 cap；声明与 0bf 的每一定位误差的先后顺序。证明所有 history/context 的 reference error 和一个 θ-independent growing schedule。二元 D5 上使用 54 的显式 phase pair、1c 的同一个联合事件、**q_new 自己的** `Cγ h+ζ_new` 严格格内界及 199 的全码因子化，重新推出全 decoder、含随机化和 endpoint 的 floor lower，并在这同一 family 上推出 upper、output-grid 和付费 range 比较。

这个命题的概率核心可以复用，不必证明旧码等于新码：在 54 的相位下，两 population q*(00) 距 cell midpoint δ/8；只需 `Cγ h+ζ_new<=δ/24`，即可有和原证明相同的严格 cell margin。μ/r 的 margin 来自原 joint event，不涉及 exp backend。条件 sample bound `p_h<=αv` 与所有 endpoint atom 的论证原样适用。于是仍得 rare conditional `(1−α)(c+v)δ/(8v)`、actual `(1−α)(c+v)δ/8` 的下界；不能因为 199 的 adversarial 版本还抹掉了 q10 信息，就给新 floor 版本额外加 q10 下界。

同族上界的干净量化分支应有 `d_q<=ζ_new+δ,d_r<=δ,d_μ<=δ,d_u<=δ`，所以 0bf 的 shared-statistic identity 给 `E<=(c+1)ζ_new+2(c+1)δ+d_new`，再加**新 readout 自己的** compile/smoothing 误差。对 general K，在 `δ<=λ/2` 且 query 精确时，确定性的参考误差可按 `K M E+Eout` 控制；这说明 growing b_N/J_N 的路径可行，但不是完整的 cap/编译证明。若额外误差先发生，再 floor，逆缩放后的新增误差是 `(physical_error+floor_error)/S`；nominal ζ_new 不除以 S。若 floor 后再加误差，则需要另写该顺序，不能混同。

这里的**实现缺口确实有数学内容**：signed floor/离域输入，public fields，selected-u 是否在切点之前，所有旧 denominator 是否擦除，有限输入码 cap 与新 bit circuit cap 如何非循环地共同容纳。把两套 R 分量取最大值，只给了预算同时装得下的条件，没有给出正确的 observation 或下界。源码相位和有限算术误差也不能省略。

另两种路线的范围如下：

- 可以保留“旧 binary floor 分支”与“新 general-D1/adversarial 分支”，用不依赖 θ 的公开 implementation index 和共同 cap 定义一个组合 family；但是只能报告**分支条件化**结论。`∃F_old P(F_old)` 与 `∃F_new Q(F_new)` 不蕴含一个成员同时有 P,Q。若要求二元 floor 分支也覆盖扩展后端的全部定位错误，仍须证明上面的桥或等价适配器。
- 不能直接拼接两份可见码流来继承任何 lower。对 augmented observation 的任意 decoder 可读取新增信息，原 marginal 的 common atom 不保证 joint common atom。若两份都被同一相位/严格 margin 的 floor 规范化并共同擦除，可以另证 joint event 上共同码；若保留任一未降级 sufficient stream，低精度 lower 可以完全消失。这是可检验的额外命题，不是预算声明。

本轮开始的 live frontier 已有 OPEN obligation `dd580c59b90ab239b37bd6085cecc930fa5abb090476bb0d8cd34ed20d5dfcfe`，范围正是这个桥。本轮没有读取其新 seed 来替代冻结证据，也没有另派任务或宣称它已完成。所需先决是 admitted `199c7b2000c58e6b`、`0bf422aeee139e59`、`54c3088eb3c35a36`、`1c8686b995accf27`，并通过 `608003f641535f2c` 的 reference strong law 承接一致性。

## 6. 候选中心贡献的严肃判断

指定三篇原文足以确认若干 overlap；它们不足以证明全球优先权，也不足以排除更接近的量化估计论先例。当前可区分的内容和价值判断如下。

| 维度 | 冻结结果实际增加/保留的东西 | 不能据此作的推广；创新判断 |
|---|---|---|
| 对象 | 固定未知严格正二阶 θ；D5 是特定 stationarily initialized rare family | “Markov next-token prediction”本身不是新对象；只限定二阶也不是贡献 |
| 信息 | 明确可见整份有限码、endpoint/query/length，针对指定 aggregate cut 降级并完整擦除 | 完整编码封住了真实漏洞，是 lower 的必要条件；一般 common-atom/数据处理原理仍是标准估计论 |
| 架构 | singleton masks、K² conjunction、q/r/μ、有限 PWL 纠正和 simplex 输出均收费 | 与 sharp matching、两层频数或 CTW 的能力没有普遍优劣结论；极大 cap 不能证明计算效率 |
| 量词 | 每 fixed θ 的 growing family 一致性；指定 phase/sample 内 every decoder 的 stochastic floor obstruction | 不是一个固定有限网络对一切 N 的一致性；不是任意 phase/所有预算网络 lower |
| 资源 | fractional summary b、output b_out、内部大 rational words、range 和 parameter bits 分开 | `log(1/(vε))` 是指定摘要分辨率，不是总 word complexity lower；S 的 fixed-total-word equality 是标准位分配恒等式 |
| 风险 | 一条真实路径、全 endpoint 分层、conditional 与真正加权 actual TV 同时计量 | actual/conditional 的区分重要但不是新统计原理；没有 optimal finite-N sampling、expected KL 或 learned-parameter theorem |

**数学成熟度判断。** “衰减后摘要的误差被约 1/v 逆放大；floor 把相邻参数压入同格；三角不等式给两点下界；sample concentration 将 population 格搬到有限历史；权重 v 抵消 rare conditional 的 1/v”是一套标准可识别性/量化估计论推导。仅把这些率或 S 恒等式列成中心新定理，没有足够依据。完整有限码与真实末查询在此机制上的组合，尚可能是具体的、可审查的技术增量；三篇原文没有逐项替代本地显式编译/擦除/endpoint/located-error 联合命题。但**“未见于这三段原文”不等于“非标准直接推论”，也不等于“达到中心贡献门槛”**。

更精确的中心候选应写成：对一个完整声明且真正兼容的有限码机制，给出 nominal sufficiency、指定位置降级后的 finite-path recovery/failure、以及付费 range 与 fractional precision 的等价分类。其新增性需要通过最近统计/量化先例的 theorem-level comparison 证明；floor 移植只修复兼容性，不会自动增加新颖性。

同预算比较目前最强的已证结论是：扩展实现里的 literal A 与 direct correction C 在同样 clipped inputs 上理想算子相等，C 少一个逐坐标 product bank，二者适配同 cap；付费 dyadic scale 与更细 fractional grid 在共同范围/码规范下等价。这些等式/负结论有研究价值，但不支撑 Transformer、深度或 A/B 的普遍统计优势。已有 lower 允许任意 decoder，仍只针对**被指定 cut 删去信息后的 representation**。若 baseline 可在同巨大 R 内改变摘要、留下未量化 joint counts 或原始历史，不能借此 lower 排除它；要声称全 architecture precision necessity，需要另一个真正统一的可见信息限制和证明。

最关键的两个下一 primary 核验对象如下，均只完成身份/摘要级定位，**未读完整定理证明，不在本轮宣称覆盖关系**：

1. Han–Jana–Wu，*Optimal prediction of Markov chains with and without spectral gap*，arXiv `2106.13947v2`。它直接研究 stationary trajectory 的下一状态 conditional predictor，并有 higher-order 扩展。应核查其实际 terminal、结构零/非可逆 pair chain、mixing 量词和 risk；不要只看 KL/TV 标题不同。已知 KL upper 可经 Pinsker/Jensen给 TV upper，而 KL lower 不能直接变成本地 TV lower；本地不是 optimal statistical rate 的证明。[primary 元数据与摘要](https://arxiv.org/abs/2106.13947v2)
2. Han–Özgür–Weissman，*Geometric Lower Bounds for Distributed Parameter Estimation under Communication Constraints*，arXiv `1802.08417v4`（COLT 2018 工作的修订版本）。应检查其 arbitrary randomized quantized experiment 和各 loss 下的 lower 是否已使本地“两点同码”成为直接特例；同时核对 iid/每 sensor k-bit 与本地一条 dependent path 的固定 aggregate floor、全码/side information、growing total cap 的差异。不能把分布式 communication bits 直接当本地 fractional b。[primary 元数据与摘要](https://arxiv.org/abs/1802.08417v4)

## 7. 未读边界、辅助计算和原生交回

未完成：九 Fact 的重新完整证明；兼容 Fact 的又一次全 cap/gate 独立复验；三篇论文所有 appendix、其他版本和全部引用链；上述两篇统计/量化先例的完整 theorem comparison；expanded signed floor 的实际编译、共同 cap 和全部定位误差组合证明；C1–C4 最终精确总 statement/proof、真实 gateway 和 final_audit。本稿不推断这些已通过。

辅助脚本 [check_review.py](check_review.py) 使用标准库有理数，核对 20 个 `c=1` 非空 phase 实例、850 个含 endpoint 的非负长除法 floor、3400 个 dyadic-scale 恒等式、16 个 lag exponent 换元，均通过，见 [check-results.json](check-results.json)。另给出“相同近似误差不蕴含相同 floor”的精确有理逻辑见证。未训练、未模拟整台巨大后端、未用数值枚举代替普遍证明。

已通过 Euler `record_obstacle` 记录一个窄范围 proof-gap diagnostic：`9ba6fedaa6b7562e4ef6bcba21553e9c7e2a2bf6e55d10d5b6f20852acc8cc64`，事件 `a74ee2894e8b4d0e43c21570dda06b34787d64c5ebfc12c04f53a9a30d2a52d8`，evidence_level=`diagnostic`。工具将此类记录放在 failure/MISSING_PREMISE 类中；它的内容只指本稿第5节的统一 floor 命题，**不是根反证、旧 Fact 撤销或新的 admitted evidence**。没有编辑图存储。沿现有 bridge obligation 接续即可，不需要重复审核兼容 Fact 或再派本轮 review。

## 普通中文

B 的软匹配公式确实可以从已有论文直接换参数得到；恢复条件频数和恢复计数也都有明确先例。现在比较可信的新增部分，是把中间每一份码、分母和残差都说清楚，再证明两种真的随机规律何时会被舍入成同一份观察，最后一个查询又该怎样正确算平均风险。这需要严谨，但其中很多统计步骤是标准方法，暂时不能包装成已确立的新中心理论。

旧舍入证明本身没有发现具体错误。问题是新后端虽然也很准确，却可能给出不同分数和不同码；舍入在格子边界是不连续的，不能只凭“同样准确”就把两个结论拼成同一个实现。最关键的一步，是把同一个规范舍入器真的装到新后端上，清掉全部旧码，并重新证明严格格内事件、末查询风险与实际资源都对得上。把 value 放大也不是免费精度：多出的范围位付费后，它等于把相同位数用作小数位。这个桥补齐以后，仍需核验最近先例并经过原生接纳，才能讨论 C4 或根是否完成。

## 附录：全部固定输入 SHA256

清单自身 SHA256：`351e1a25691f28ce006232a3457276fb4e5565abcfd3a6c6752acf7a24bf4add`。

| 实际文件（相对项目根） | SHA256（expected=actual） |
|---|---|
| `fact_graph/facts/3a69c2fa3d459b1d.md` | `899e13e3de35de82397926f56e26587a062e7789c726ea676465f2a1151b8132` |
| `fact_graph/facts/338012727e3d5f81.md` | `82170d7734472d615c25a172a95fd8a04624154a1d6c0a4b19f53d47dab7b363` |
| `fact_graph/facts/608003f641535f2c.md` | `6a231cbc6dc9fd88e1291234d295b38652a12f4f33199a96d2ac85c6f9db7fe4` |
| `fact_graph/facts/17afd9045ade0c3d.md` | `70fecafd40d3c3228ad123491a32a910d45173db852765034c44ead7d0df1c9c` |
| `fact_graph/facts/1c8686b995accf27.md` | `96fe8b12c8d596ba78b97c567c9427cdbeb20106189bcd33130adcb5861d54a9` |
| `fact_graph/facts/33e7d01a130b6858.md` | `02bdf0189b40f6ec385d950b0e3b95036d06801afbfa849ef548892dd724037c` |
| `fact_graph/facts/0bf422aeee139e59.md` | `b7cfd43f5e8c2bd7a5e3ed3fe716bfea9e4dd3395b6be963f9a4ca48eb20a240` |
| `fact_graph/facts/54c3088eb3c35a36.md` | `6b80628d65aa79ef8c6b0c8dd855077e817faff870f0c411802c738f453d6916` |
| `fact_graph/facts/199c7b2000c58e6b.md` | `619d25095eb8ddf9b9237bbe003c2b52cb30d8b1f5a4d947ae3d8cc698060996` |
| `PROBLEM.md` | `05ec43313e6680af547bf6e11628c2c04345301e1c2d0b223f33bbdbff8167d9` |
| `inputs/AUTONOMOUS_RESEARCH.md` | `e21e211cfda567f2f5bdca8b5bc7bd42fd59527938bc1ec77d5e50ff22003424` |
| `inputs/materials/plan/ICML_研究总计划.md` | `cd42fa71a891284832291451b00a9d36da27426ef37540fa5c29c76354f654a2` |
| `inputs/PROBLEM.md` | `413243ac3bf9d2c1103ece084af0f2af564931e81893c2404185b9146152b66f` |
| `inputs/materials/docs/research-reset-20261024/novelty-map.md` | `5865d90d1fcc74631756a8ebfc1c679a8d8b6b4f024efd95e1c6c2d12b74ea8b` |
| `outputs/C4-literature-008/lead/checkpoint-v0.md` | `cff0e489c6201fa908291bcbeecd2b88c556c28819d73fb7b71839ad545460a7` |
| `outputs/C4-literature-008/lead/checkpoint-v1.md` | `27957b80f6aea409831b98d4dfde23ae0c0f87d26c9d261c63b54208fe736940` |
| `outputs/A-precision-006/prover/exact-proof.md` | `6f82fa1923608b564575e0fe2cd4f14d8e66d90874f7657c28ec8b131fab7423` |
| `outputs/A-compatibility-007/counter/exact-proof.md` | `54e09e64663f9398e705ca7e71c83129336cc8366488a8a6bb1ec46b8c2d0bf0` |
| `outputs/C4-literature-008/lead/checkpoint-v2.md` | `68c9f271889faf2e48e95618f0373f5f67434b5cdf4a40e1548c60fbc35cb640` |
| `outputs/C4-literature-008/lead/sources/zhou-2410.05493v3.html` | `cefc70d6e3f5a8567d87b2564b26e47e04514a8d630f0fc2a0755ed60d57f06c` |
| `outputs/C4-literature-008/lead/sources/rajaraman-neurips2024.pdf` | `d927b5e99e57bc677c01f3c065962d3023673a264c592cac97e5517b4c825a2f` |
| `outputs/C4-literature-008/lead/sources/primary-search-return.json` | `e1e013bea338775214c9737629a0456084e448fd949178fec879adc7c750ceeb` |
| `outputs/C4-literature-008/lead/sources/dangelo-proposition-snapshot.json` | `2e0111925e6462e6b968422dc322790b47dc6f5fb05c79d1080959e49bde0c5b` |
| `outputs/C4-literature-008/lead/sources/primary-details-return.json` | `c02c5d9cf1d989650f83436e67e9453d076e969d6c60b8f7a2659b04e7bb24ba` |
| `outputs/C4-literature-008/lead/sources/manifest.json` | `a76c4485711769dc46818d7240078cc94a64953588a5666358b2a771a1eebf8a` |
| `outputs/C4-literature-008/lead/sources/primary-open-return.json` | `5efc5135d9dbf46601ba8ad55bbd9cd341fa9506335682ffa35a84ccaed00bb2` |
