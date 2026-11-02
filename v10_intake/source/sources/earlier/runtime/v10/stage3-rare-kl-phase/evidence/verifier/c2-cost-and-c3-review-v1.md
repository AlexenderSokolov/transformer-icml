# Independent fixed C2 cost-repair and C3 realization review v1

Verifier，2026-10-25。[Non-scientific operational metadata omitted.]
`[redacted routing identifier]`，团队注册模型/effort 为
`[redacted model routing]`。这是首次实际执行的本项独立文件审查；不是恢复旧队列、
重复 C1/C2 统计审查，或运行原请求33163ae3。本报告没有 native admission 效力。

**A / C2 v2 局部成本修补：PASS。** 对义务
`8b179af3ef2fe36eca7503ff37e9baca6ba118d546cf884db6ad7e4da0d0b6f8`，
新 §2a 补齐本次原生拒绝指出的 D3–D4 编码、字长和有限转换成本。
没有必须修改的数学项。旧统计/表示段落按已核对的版本一致性及本会话原审查范围复用。

**B / C3 v1 完整确定性实现：PASS，限于明确声明的名义有限算术和分别列出的成本模型。**
对应义务
`c82d400c69019a551db29a66e99faec5bfbf281097c5c8ae57075ea5789772fb`。
主证明全部1,150行、嵌入 A–K、完整指令表、代码与资源函数均已审查；
未发现必须修补的承重错误。这个判断依赖全宽度构造、路径代数和误差证明，
不由有限诊断实例代替。

**原生边界：C2/C3 仍 OPEN，未新增 Fact/Evidence；不认证 C4 或阶段 root。**
C1 已接纳，无需重证。C3 的确定性等输出证明不依赖 C1/C2 风险定理；
后续接纳风险结论必须保留其真实 native 前提，不能凭本报告先行转移接纳状态。

## 1. 固定文件、原生状态与本次动作范围

除 PROBLEM.md 外，下表路径相对 `outputs/001-conditional-grid/`。

| 固定输入 | SHA256 |
|---|---|
| 当前 PROBLEM.md | `efc51898a4a702040f9048e2f53121ec59020586b12221fd57e1015940ec5751` |
| prover/c2-proof-v2.md | `b8de1c83444044357790ab8062caa443a701f260b7d631dbae35f85c308f667c` |
| prover/admissions-v1/c2-response.raw.json | `302eafcaf12cc877e93648096ca6a878ef334e11390cc14e1e321c0008020d8b` |
| prover/admissions-v1/c2-v1-to-v2.diff | `c33d01c2f5a02714b17080d4cbe275a4a578c2fb4d313a5e7f073864c0746bbc` |
| counter/c2-cost-repair-review-v1.md | `3b133d6493154f73556d31722be2b99cd5549e50f0d4a044ab2177259a8f643d` |
| lead/c2-cost-repair-review-v1.md | `4fd1e1c562755ab957e5ca0fe057823521d668fdb6e2a92db54e6fb71d1eedc3` |
| prover/c3-proof-v1.md | `68dcb797dfe0e2103d2f35034311efa97d9ae496dedf4eafc67c600b34a8679c` |
| prover/c3-resource-ledger-v1.md | `c00336780dfb8e7cfcdad1ffc2542d8319508b1fdf40f278dcf1960c0105076c` |
| prover/c3-resource-certificate-v1.json | `2a5aa300d24cebebc8006f2f4ced9ad4fa00f07f562e5d9eb697c534c5765125` |
| prover/c3_word_program_v1.py | `187f81b8da04a20412c07dc2fdfbe7387836484e2bc57e873a0dd8045b785a56` |
| prover/c3-word-operations-v1.json | `9f143a95c8d6b8bcc9ff93e3b49a4230f34a4118f3e06344f4c992aa60e869f1` |
| prover/c3-code-audit-v1.md | `5648f1bc74b43d44f7597ae055190e41d21413d207049ec59601210211334ee6` |
| lead/integer_predictor_v1.py | `5eae6f7c009cd5e612c74274117109099b249a54dbdd62a6ee15e3da093662d6` |
| counter/c3-adversarial-review-v1.md | `f1db7ce9110bdc782e6b15df291154535bf808567d9629711320d850a829c768` |
| counter/c3-review-manifest-v1.json | `e735da588c341208bc6be8bd4c4b45ed259c187a153ac9b1e89736a2e961ac0d` |
| lead/c3-review-v1.md | `e8665348447fb61abac0f263d820d79c50aaf967bbef0972af392c83d50202a0` |
| verifier/stats-grid-review-v1.md（原讨论审查，仅复用未变范围） | `9a7ec137568f5494d260a23a6bfdf6e945a11edc1fce9cb0a033717127fb2161` |

两份 Counter manifests 的 inputs/outputs 合并恰为34个不同 pin，SHA256/字节数全部
实查匹配。再固定8个补充输入，共42个；完整逐文件哈希在本次
`c2-cost-and-c3-checks-v1.json` 与 `c2-cost-and-c3-manifest-v1.json`。
历史来源文件仅检查 hash，不把来源或讨论 PASS 当已接纳前提，也没有执行旧诊断入口。
Counter/Lead 的新报告已读取，其肯定结论未被当作本次判断的替代品。

开始及结束前的 Euler research_state 一致：C1 DISCHARGED；C2、C3、C4、root OPEN；
acceptance=null；本次前后 frontier_hash 相同。C1 的真实已接纳前提为：

- Fact：`e418ec34b7dbc4a6`。
- Evidence：`4857f1b1b5d10ab74a979362e3d0c3068c9634016e4ce6b6a0609ed577eb2eea`。
- 接纳内容 hash：`7f0315c5a0a002ce4e9cb0ad9199e91309fe2cf4976d8082573087b53469fb27`。

这些由实际 C1 gateway 响应、evidence readback 与当前状态交叉核实；未重读或重证已接纳
C1 推导。只调用了只读 research_state/members/messages；未调用 ask、submit、continue、
final_audit、route/status/obligation 更新或调度工具。[Non-scientific operational metadata omitted.]
保护计数3及旧消息均无写入动作；本报告不是解除保护或重置计数的依据。
Lead/Counter 文件里较早的“四条/五个 OPEN”等是历史写作记录，没有被执行为新指令。

## 2. A：真实 C2 拒绝、版本差异及局部端口

原始响应确为 accepted=false、transport_status=ok、verdict=wrong，原 failure
`b97ba0738f1848747bd400c3e74405482a403fe463232e79f62fa7068938d708`
保留。它明确要求局部输出/converter 成本，不要求改变风险论证，也不要求在 C2 提前
证明完整 C3。我此前的讨论审查漏查了这项 D3 局部成本合同要求；旧 PASS 不推翻该真实拒绝。

实际 v1→v2 unified diff 与归档字节完全一致。新增数学内容是 §2a，其余改动是接纳/依赖
文字；§3–§8 整段字节一致。因此复用原本已审的统计和表示内容是有版本依据的，
不是再次提交/重证 C1，也没有悄改下界见证、随机比较器或 actual-terminal 风险。

§2a 明确是 selected exact counts 与实际末两位到输出的子程序成本。它不免费获取这些
输入，constant branches 也不请求 counts。完整获取过程仍由 C3 独立给出。

公开 b,Q 的主端口按 canonical (next0,next1) 次序解释，输出 **恰 b 位 next1 numerator
j1**，有前导零。因1<=j1<=Q-1，位宽足够；另坐标由 Q-j1 解码。
Q 和 b 是公开固定接口参数，不发 denominator 或自描述 header。
用 b+1 位中间借位减法恢复互补 numerator 的 <=16(b+1) elementary 界可实现。
若发两 numerator，为2b位；再发 literal denominator，则为3b+1位；这些可选写出与减法
都收费。没有把第二坐标、可变长协议或一个实数标量输出当作免费接口。

## 3. A：K 字长、72项库存和位操作界

ell=ceil(log2(N+1))，K=b+ell+6>=9。active 分支 D<=M、d<=m、Z<=4m，故：

    nearest dividend <16mQ<=8NQ<2^(b+ell+3),
    ceiling dividends <4mQ,
    shifted division remainder <2*divisor.

normalization 的 V=4(C+1)、3d、全部单调部分和/积、Q 的 b+1 位表示和 residual
均在 K guard 内，residual 减法非负。泛用完整乘积确实由两个 K 位字构成的2K accumulator
保留；首段“A second K-bit scratch word”与后文明确实现一致，不要求为这句文字改固定版。
该 nominal D<=M 的局部引理没有冒充 C3 任意 closed-grid masters 下的 D<=2M guard。

两 normalization 库存10/9，nearest6，ceil/residual11，controller12，routing8，
loads16，总数72，计入了互斥分支容量。DIV 扫描 K 位并维持
scanned-prefix=divisor*partial-quotient+remainder、0<=remainder<divisor；
因此 exact divisibility、半格 tie 与 residual1 不需要实数 floor。

schoolbook MUL 的80K²及 DIV 的128K² elementary 上界足够。
每 elementary operation 另给128K地址/控制余量后，32768K³/word 是有效保守界。
72*32768=2359296；初始化/擦除、最大可选端口及减法额外 elementary 数
可用275K+17覆盖。计入相同地址余量后，其成本小于4000K³（K>=9），
故总量严格小于3000000K³。

128个 K 位 data/scratch 字占128K位；2K 位地址足以寻址，常数、乘积/商余和控制有限银行
可置于256K live bits 内。固定有界循环程序不是免费 K 相关展开指令带。
因此 §2a 的 T_convert<=3000000K³、S_convert<=256K 在其明确顺序位操作模型成立。
它们不是完整预测器成本，也不是神经网络深度/宽度的界。

N=3,4,5、b=1、01/11 行直接写 Q/2 的 b 位串；不执行无效除法。
active 零 counts 时 Z=8，clipped endpoints、Q=4、half-up ties 与 residual1
均适用同一有限算法。**C2 局部强制修补列表为空。**

## 4. B：实际因果绑定、许可信息和四头路径恒等式

物理 query 在 N+1，输入 X_1..X_N 完整观测后。第一层四个 singleton heads 的 query
keys 分别是 m,m-1,N,N-1，给出两个独立绑定：E_m 与实际 S_N。历史行取前驱/前前驱，
不足时自取；所有边因果。N<6 跳过该统计过程，不使用 m-1=0 的无效 query key。
crop/routing 发生在绑定之后，不把 query 的物理时间改成 m+1。

第二层 query eligible keys **恰3..m**。合成 query 和尾部均不是样本；值只用观测 one-hot、
局部 lag 和公开初始 flag。恢复器接口限定为19个 masters、端点位和公开 metadata。
读取实际末对的成本已在 adapter，之后没有 raw-history、精确 count table 或未来符号的旁路。
四 singleton 掩码为4n²，四统计掩码为4n_m²；两者都存储、扫描并收费。

四个理想 heads 的代数逐项成立：U 给 alpha、nu、初始 symbol flag f 和 rho；
T 的权重1+1{lag2=b} 给出 source-pair 质量和初始 pair flag。
source/successor pair 列表相消只留下初始 pair 与 **E_m**：

    g_c=dT*h_c-nu_c+rho*1{E_m=(b,c)}-(dT*h0_c-f_c).

两 product heads 的权重分别为
(1+1{lag2=a})(1+lambda*1{lag1=b})，lambda=1,2。
d_k=(1+lambda*nu_b)/(1-U_k/2)，分母在[1/2,1]。
展开后消去共同 successor marginal 与 lag2-successor 项，得到

    c_(ab,c)=d2*q_(2,c)-d1*q_(1,c)-g_c.

这是包括 M=1、缺失行与零 counts 的有限路径恒等式，不借 stationarity、源参数或旧 Fact。

## 5. B：有限 log/exp、signed 恢复和严格 snap

| 承重步骤 | 独立核验 |
|---|---|
| Log 生成 | geometric-series 积分给 log2/log3 的 rational partial sums；共同分母使逐项 DIV 精确，末次 floor 后各误差<2δ。log3 numerator 用 p+1 位。离线生成不是 log oracle。 |
| Score/weight | 有限 score 在[0,log6]，相对理想误差<=4δ。8p 次 exp recurrence 先保留完整积再 DIV；每次截断向所有后续项的贡献<=8δ。含尾项与 score 误差后，每 weight 误差<=100pδ。 |
| Aggregation | 累加 numerator/denominator 精确，非空行 scaled denominator 至少 eligible-key 数。ratio 误差<=200pδ，末次 quotient 再损失<1/Q_A。p 的公开选择给每 master 误差<=eta=2/Q_A。闭端点0、1均包括。 |
| Normalizer | 整数式(14)分母在[Q_A,2Q_A]；d1/d2误差分别<=6eta+zeta、10eta+zeta，zeta=1/Q_A。 |
| Signed recovery | dT products 与初始/末端边界按 triangle inequality 得 g误差<=9eta+2zeta；两 product 项误差<=10eta+2zeta、16eta+2zeta；总误差<=35eta+6zeta=76/Q_A。无独立误差假设。 |
| 全域 guard | 任意 closed-grid masters 下 g∈[-3,4]、H∈[-8,9]（scaled units），[-16Q_A,16Q_A] 足够。全部 SUB 保留符号至 clip，不先做 unsigned 截断。 |
| Closed-grid expansion | ReLU 差在整数 grid 上精确取 bit；从 bit h 开始，故包括 H=2^h。没有对 nongrid 实数声称 floor。 |
| Count snap | clip 后用(2M*A+Q_A) div (2Q_A)。76M/Q_A<=76/256<1/2，严格小于半计数半径，所以逐路径恢复两个精确 counts。没有重用旧 count-snap Fact。 |

非名义 closed-grid 输入仅保证各 snapped count 在[0,M]，不能断言两项和<=M；
C3 正确据 D<=2M、d<=2M+2、Z<=8m-8 分配读出 guard。
nearest dividend<16mQ；ceil dividends<8mQ；完整2v积、v+1 shifted remainder
及符号银行在 O=32v 内。前端 B=128p 覆盖 score、exp 完整实际积、aggregation、
normalizer、signed recovery 和 snap；b 相关 literals 在输出阶段加载，未被塞进独立于 b 的前端字。

## 6. B：63/41 compiler 与不同输出端口

63 recovery 指令恰为19共享项加每坐标22项，与式(14)–(18)和 expanded JSON 一致。
所有 result 名唯一、无 use-before-definition。边界选择匹配 e0==b 且 e1==c，使用 E_m。
41 output 指令计算两候选再 mux；a 选择00/10，末位 b 或公开 small/Q2 flag 强制 uniform。
Z、2Z 在全部候选上都正。Q=2 的未选 nearest 候选可有零坐标，最终输出仍严格正 uniform。
N<6 以零 counts 进入合法常数读出，绝不执行 M<=0 recovery。

附录 A 的 primitive 由明确 ripple、schoolbook 和 quotient/remainder 递推实现。
对 w>=2，各列原始多项式<=512w²，双倍 sign/scratch 余量给 g(w)=1024w²。
2w product/quotient、w+1 remainder 及其余 scratch 银行受32w+32覆盖。
AND/NOT/XOR/OR 的 exact ReLU 恒等式有效；factor16 序列化留足更新空间，
所有其他 live channels 的 identity 逐层计入，而非免费保持。

保留所有 named input/result、双轨、scratch、metadata 与 grid extraction 后仍小于
512B/512O channels；W_F=1024B、W_O=1024O 足够。每 channel 用整 B/O 位存储
属于过收，所以 working bits 另外乘字长是正确的。

**端口不能混同。**本次 C3 存在性见证可选用已明确的 guarded literal-Q 固定端口：
两个 b+1 位 numerator words，加一个 b+1 位 literal denominator，共3(b+1)位；
Q 公开只发两项时为2(b+1)位。G_O 的1024O余量支付写出、copy/erase 和可选 affine
dyadic decoding。C2 的主端口只发紧凑 j1 的 b 位，另两种为2b或3b+1位。
这些 emitted lengths **不相等**，但编码同一概率向量。经证明高 guard bit 为零后，
付费复制可得到 C2 的 b 位 j1；不能把跨端口比较称作原始传输串逐比特相同。
指数/header 替代接口若采用还须固定相应协议；本 verdict 采用已完整声明的 literal-Q
接口，不依靠任意未定 header 免费。C3 与自身强基线采用同一端口时，numerator words
确实逐路径逐比特相同。

## 7. B：完整成本域审查

采用 proof(3) 与 A1–A21 的公开 N,b 函数；没有以有限 certificate 的四个实例外推全称证明。

| 成本域 | 已核验的完整账目及不能互换之处 |
|---|---|
| Hybrid dense token/query | P0=128、L_H=P0+L_F+L_O，前段保留 n 个 token，恢复/输出可付费抽取 query。I 按各阶段实际 width/token 数付 identities；P_D 按 phase-shaped dense matrices 收全部零系数。32层余量覆盖跨宽过渡。W 是 per-token/query width，不是全数组储存。 |
| Finite attention evaluator | E=(256p+512)n²+1024n 覆盖 adapter/masks、QKV、每 edge 的8p recurrence、exact aggregation 和初末 writes；T_A=E*g(B)。K0、scratch 与所有重复执行单列。Hybrid 少量 attention 层不等于这些 bit steps 的神经层数。 |
| Sparse neural | P_S 包含 arithmetic、identity、参数与地址；在线式也付 I 项 identity。不能使用 shared register model 的不变寄存器免费驻留规则。 |
| Shared addressed word program | A13 支付 word/address 长度和 arithmetic；S_shared 包含 B/O 两套 library、63/41 lists、dispatch、loop/routing、mask/metadata。是明确 register-memory 模型，不宣称 indexed memory 自动成为同成本神经电路。 |
| Tokenwise padded batch | A14 全 n token、全 phase 取最大 W/word，holds=L_H*n*W；8n² masks，全部 retained/unused banks、dense zeros、work/stored/peak 均另计。 |
| Global dense batch | A15 总 width=nW，literal full-batch matrix 按其平方收费；包括 cross-token routing 和 block zeros，不再使用 per-token width 作为 global width。 |
| Fully flattened Boolean/ReLU | A16–A17 将 T_A、G_F、G_O、adapter/array loops 全部展开。T_F 包含全部 exp/DIV bit steps；S_F 保留整个数组及 scratch。T_F*S_F holds、dense slots/parameter bits、sparse code/address、rolling 和 peak 分列。没有借 hybrid depth。 |
| Offline generation | A18 的共同分母生成<=32p+64 word ops，B_log=8p²+32覆盖完整中间积，T_log/W_log显式。A19 对所选完整 stored bits U 和 depth Dlen 枚举每个 coefficient/zero/identity/mask/position/address；generation peak=U+W_gen，与 inference peak 分开。 |
| Sequential baseline | A20 付全部 N 次输入读取、8 counter 更新、范围/位置/末 pair、row mux；另加完整41项输出、32 boundary layers、b相关存储与成本。输入顺序 arrival 是显式接口。 |
| One-shot baseline | A21 用 W_CB=W_C+2N+2ell，在 count 每层保留2N输入银行；全部 holds/dense slots/work/online 式换该 width，再接 output phase。不是只加2N静态位后仍称完整网络 width O(log N)。 |

上述 neural coefficient/activation 成本还包括 scalar extraction thresholds 与 output coefficients。
Hybrid 的 S_dense=P_D+K0+M0+Z0、S_sparse=P_S+K0+M0+Z0、W_work，
以及 stored+work 的 peak 均与代码函数对应；shared word、padded、flattened 和两种
baseline 同样各自相加。
Dense execution 另收 projections/pointwise multiply-accumulate，必要时过收未用行；
这种过收有效，不会把未声明输入交给 decoder。

离线生成每个 term 的 denominator 整除 D_q；log2 D_q<2p²，scaled numerator/full
products 被 B_log 宽松覆盖。生成式也收费模型指定的 dense zeros、全部 holds/addresses
和最终程序，不宣称这些巨大 dense graphs 已物化或测量。各模型预算独立代入，
不拼接不同列的最小值。全套函数是明确构造的充分上界，不是优化后逐项最优值。

## 8. B：强基线等价及反例保留

按 arrival position 归纳，8 counters 始终等于到当前时刻为止、仅3..m的 triple counts；
j>m 停止计数但继续更新末 pair，所以最后 query 是实际 S_N。头部恢复的两个 counts
由上述有限路径代数和 strict snap 得到同一整数，随后使用同一41项输出和同一端口。
因此等输出是全路径证明，不是样本诊断；它不证明神经实现对优化强基线的预算优势。

| 保留失败 | 本次核验及正确限制 |
|---|---|
| 偷换 E_m 为 S_N | 10001110 的正确 counts(1,0)，wrong endpoint 为(2,0)，本次重新调用固定函数复现。实际 query 绑定不许可更换 prefix flow endpoint。 |
| 省略 closed-grid 顶 bit | H=2^h 必须有 h+1 位；ReLU expansion 从 h 开始。log3 的 p+1 numerator 位也保留。 |
| 非严格 half-count 半径 | M=1,Q_A=16,A=8 对 C=0 的误差恰1/2，snap却为1；不能把 strict 改成 <=。 |
| 不收费的重新存储 | 7*(1/16+1/10000)<1/2 并不担保先 perturb 再 truncate 的恢复；该反例排除错误噪声模型，不反驳当前 nominal 声明。 |
| 只按 nominal sum 分配 guard | 两个任意 clipped masters可各 snap成M，故 D可为2M。N16,m8,Q4,C0=C1=6 得 nearest dividend280>旧8mQ=256；16mQ=512覆盖。本次重现。 |
| 坐标/quantizer扩张 | J是 next1，不能交换坐标；最近 grid 不等于逐 target KL 最优，row10 不加固定正下截断。原量化与统计反例保留，无新必要性/噪声结论。 |

## 9. 新诊断、强制修补与后续接纳边界

新脚本仅向 verifier 写新文件，不执行任何旧 diagnostic main，也不重跑旧统计套件。
其检查结果如下，均通过：

- 34个原清单 pin、42个总输入 pin；实际 diff/归档一致；嵌入 appendix 与 ledger 字节一致。
- 63/41 IR 与 expanded JSON 一致、无重复定义/未定义使用；四个 archived certificate 实例重新精确求值一致。
- 所有长度3..7二元前缀及四个 query 共992组：新四头 evaluator、exact rational flow、finite master error、signed recovery/snap 与直接 comparison counts 一致；618组实际出现负 intermediate，符号未被抹去。
- 4,704组读出分支，包括非名义 count sum；其中1,920组同时核验 nominal local K guard；另24组大参数 fixture 覆盖 b=4096 和 N=2^80+3。
- 对若干 K/w 边界值核对本次局部成本余量及 primitive 多项式；三个新/负例路径与 pinned Lead finite frontend 对照，保留 wrong-endpoint 与旧8mQ反例。

这些是补充诊断，不是全 N,b 证明、完整电路物化或 native Evidence。重现命令：

    python3 outputs/001-conditional-grid/verifier/check_c2_cost_and_c3_v1.py

| 本次新 artifact | SHA256 |
|---|---|
| verifier/check_c2_cost_and_c3_v1.py | `dceb2dfa8d65f3336a2655bc6c0c2c0fee55d47cdbc91f0020316ffb11e29395` |
| verifier/c2-cost-and-c3-checks-v1.json | `b6be1d61bc2c8b7310b18f4b0b5c67fde286a563aca9f4a4dc02e118dc6df902` |
| verifier/c2-cost-and-c3-native-state-v1.json | `bf4a1538079b4a9c8e036b10864d9b8f1b57e5c5870064b662f3e6cbacfd8037` |

**C2 mandatory repairs=[]。C3 mandatory repairs=[]。**本次没有发现必须登记的新科学障碍，
所以不造 failure、节点或 Evidence 来改变前沿/保护。C2 的旧 wrong 原样保留，只有后续
正常 gateway 能决定 v2 是否补齐；C1 的现有 Fact/Evidence 原样保留。

责任会话/Prover 应先读本报告实际固定字节，再分别办理对应提交。C2 使用真实 predecessor
`e418ec34b7dbc4a6`；C3 的确定性实现部分自包含，不可附带无 C1/C2 native 前提的风险接纳。
本审查不触发调度、不关闭图、不给 C4/root 或 final_audit 结论；本轮前沿未变化也不据此
请求重置 Lead 计数。[Non-scientific operational metadata omitted.]

本次新 Fact IDs=[]，新 Evidence IDs=[]，submit_proof=0，final_audit=0，调度/保护/旧消息
修改=0。[Non-scientific operational metadata omitted.][Non-scientific operational metadata omitted.]
仍保留。无外部检索、独立模型 CLI、替代 agent 或原 campaign 访问。C3 nominal 充分实现
不意味着内部精度/深度必要性、优化神经优势、噪声可靠性、可训练性、实用常数或发表新颖性。
本阶段的后续接纳也不等于 v10 母问题或 T1→T2→T3 完成。
