# Stage3 有界对抗审查 v1

Counter，2026-10-25。对象是当前 PROBLEM.md D1–D7 以及 C2 义务
`8b179af3ef2fe36eca7503ff37e9baca6ba118d546cf884db6ad7e4da0d0b6f8`。
本文是固定文件的研究讨论审查，不是独立 Verifier 的接纳，不产生 Fact 或 Evidence。

**结论：所审 C1/C2 v1 未发现承重数学错误；C2 的网格桥及全部边界可保留。
C2 仍须先取得当前项目 C1 的真实 native Fact。C3 本次只能通过强基线/输入域的
限定审查，不能把 implementation checkpoint 当完整实现证明。
C4 须纳入已找到的直接概率量化先例，不能由 HJW/Paulin 的未覆盖推断新颖性。**

固定版本如下；完整读入清单、原始 PDF 来源和本报告 hash 见 manifest-v1.json
及 SHA256SUMS-v1.txt。后续修补应另存新版本，不静默替换本文所审字节。

| 文件 | SHA256 |
|---|---|
| 当前 PROBLEM.md | efc51898a4a702040f9048e2f53121ec59020586b12221fd57e1015940ec5751 |
| Lead checkpoint-v1.md | 7c19965199c6cd92dc578c3a3f4d91009fbefc2948754b5de6e21b292dce8b4a |
| Prover c1-proof-v1.md | 5884ffc213a0aaa950b48f881abd4519440800737485b5c3aae9d293c38fb38d |
| Prover c2-proof-v1.md | a008ec575571973d7df08ece2468c901744a6c3680df08b15a008c38ff1d7105 |
| Lead implementation-checkpoint-v1.md | ff29424bef9a5225e3d79c6790804514980ccf6f3f047d55a6d229f9640c6ce8 |
| Lead integer_predictor_v1.py | 5eae6f7c009cd5e612c74274117109099b249a54dbdd62a6ee15e3da093662d6 |

本次目录快照中没有独立的完整 C3/C4 proof 文件。没有审查尚未出现的未来版本。

## 1. 实验、量词及证据边界

模型是二元 stationary rare 族：0<u<1/4，1/4<=t<=3/4，
w=(1-u)/3，r=ut/w；pair law 按 (00,01,10,11) 为 (u,w,w,w)，
next1 概率为 (t,1/2,1-r,1/2)。只允许 ab->bc。输入 X_1^N，
实际查询 S_N=(X_(N-1),X_N)，不另抽独立 context。算法只知模型结构、N、Q。
Q=2^b，b>=1；输出每次实现都须为 canonical (next0,next1) 次序的正 Q-grid。

目标是同一个未知参数程序对所有 N,Q,u,t 的同时上界：

    R_N <= 6000000/N + 3/Q,
    R_N,00 <= 1000000/(1+Nu) + 3/Q^2.

下界的比较器可以使用全历史和 source-independent 随机化，固定 u 的条件实验还可
告知 u。不是仅与 prefix 估计器比较。所有风险均为 natural-log expected KL。
期望收敛、逐 law、uniform、triangular、conditional 和平均结论不能互换。

本次 research_state 读得五个 obligation 均 OPEN，两条现有 route ACTIVE，
all_evidence=[]，acceptance=null。C1 的当前义务为
`1dd6b3b9191952ba424db347dab176cd3336d5399831f867f595a13a40e5ce25`。
C1/C2 的 v1 明确没有继承任何旧 Fact；C2 只把该待接纳 C1 作为统计前提。
source009 的实现 C1 名称和本阶段 statistical C1 名称不同，不能因同名而继承。
文件 hash、旧讨论 PASS 和 obligation ID 都不是 native predecessor Fact。

## 2. C2 的 KL 到 MSE 桥：合法

令 a 为 row00 未量化的 clipped next1，q 为新量化 next1。它们和 t 都在
[1/4,3/4]。对每个历史，Bernoulli Pinsker 与 chi-square 上界给出

    (t-a)^2 <= kl(t,a)/2,
    kl(t,q) <= (16/3)(t-q)^2,
    |a-q| <= 1/(2Q).

所以

    kl(t,q) <= (16/3) kl(t,a) + 8/(3Q^2).

这是同一历史上的确定不等式；之后才对真实 S_N=00 条件期望。
没有把 TV 平方，也没有把 query 与 prefix 当独立。C1 先以未量化 cap 比较
prefix 条件 law，因而不会无故产生 log Q 乘 mixing 误差。

若 C1 的统计界 R_N(a)<=10^6/N、R_N,00(a)<=160000/(1+Nu) 接纳，则
条件统计系数为 (16/3)*160000=2560000/3<10^6，表示项系数
8/3<3，正好推出所需条件上界。

平均风险用 stationarity 的实际质量 u,w；另两行损失为零。row10 的旧 positive
ceil/residual 满足 q_c >=(1-1/Q) a_c，故 KL 增量至多
delta_Q=-log(1-1/Q)<=2/Q。于是

    R_N(q) <= (16/3)u R_old,00 + w R_old,10
                 + w delta_Q + 8u/(3Q^2)
            <= (16/3)*10^6/N + delta_Q + 2/(3Q^2)
            <= 6000000/N + 3/Q.

只用了非负行损失，不要求分别以同一常数控制每个条件行。

## 3. 一个程序及其整数边界：通过

先处理 N=3,4,5 或 Q=2，直接返回 uniform。其余 N>=6、Q>=4 时，
m=floor(N/2)，只数 positions3..m 的完整 triples，以实际 S_N 选行。
01/11 仍输出 uniform。选中行 C0,C1>=0，D=C0+C1，d=D+2>=2，采用

    row00: z1=min(3d,max(d,4(C1+1))), z0=4d-z1;
    row10: z0=min(3d,4(C0+1)),       z1=4d-z0;
    Z=z0+z1=4d.

row00 的 a=z1/Z 在闭区间 [1/4,3/4]；row10 的 z0/Z 是 next0，不能
误用 next1，也不能加固定正数下截断。所有 z 都严格为正。

row00 对正整数 2Qz1+Z 除以 2Z，取 Euclidean quotient J。
J=floor(Qa+1/2)，输出为 **(Q-J,J)/Q**。J 是 next1 numerator。
Q/4、3Q/4 是整数，所以 Q/4<=J<=3Q/4；端点固定，严格正且精确和为一。
Qa=k+1/2 时 J=k+1，半整数向上。Q=4 的三个区间依次为
[1/4,3/8)、[3/8,5/8)、[5/8,3/4]，对应 next1 的 1/4、1/2、3/4。
商余算法是有限整数运算，不是实数 floor oracle。

row10 令 A=Q-1，k_c=(A z_c+Z-1) div Z，e=Q-k0-k1，输出
(k0,k1+e)/Q。两项正数之和为整数 A，故 ceil 和只能为 A 或 A+1，
e∈{0,1}。两输出在1..Q-1，且逐坐标满足上一节的乘性下界。
residual 永远给 canonical coordinate1，不能随“当前估计哪一项”改变。
该代数也覆盖 Q=4；例如 C0=0,C1=1，Q=4 时输出 (1,3)/4，e=1。

D=0 时两行都是 (z0,z1)=(4,4)，Q 偶数，所以两种 converter 都输出
uniform。一个 successor count 为零、clip 的两端及零 visits 均无未定义分支。
Q=2 是正网格的唯一 uniform 点：平均 loss<=log2<3/Q；row00 loss
<=4(t-1/2)^2<=1/4<3/Q^2。N<6 的 uniform 分支由粗统计常数直接覆盖，
未误用 M>=1 的 count 引理。所有输出至少1/Q，故另有 pointwise log Q cap。

## 4. 同族表示下界、随机化和 max：通过

对每个固定 u∈(0,1/4)，Q>=4 取 t_Q=1/4+1/(2Q)，Q=2 取 t_Q=1/4。
这是合法 D1 law；每个 grid next1 与 t_Q 的距离至少1/(2Q)。因此对每个
历史及几乎每个 seed，kl(t_Q,q1)>=1/(2Q^2)。S_N=00 有质量 u>0，
条件化保留该下界；允许比较器知 u 也不改变它。这不是某个特殊 u 的论证。
随机选择邻近 grid 点不能绕过逐 seed 下界；若先平均概率再输出，则平均结果本身
仍须满足本题的 grid 要求。

平均格式见证另取 t=1/2、u↓0。row10 的 p=(r,1-r)，每次输出
q1<=1-1/Q，所以

    KL((r,1-r)||q) >= (1-r)delta_Q-h2(r),
    R_N(u,1/2;q) >= w[(1-r)delta_Q-h2(r)] -> delta_Q/3.

右侧与 q 无关，故没有交换 predictor-dependent 极限与期望。u=0 不属于模型；
这里只对允许的正 u 取 supremum。seed 不影响这个逐路径界。

统计见证来自 C1 的完整历史 testing，故对 grid 子类同样有效，得到

    max{3/[16384(N+6)], delta_Q/3} <= M_N,Q,
    max{3/[16384(1+(N-2)u)], 1/(2Q^2)} <= C_N,Q(u).

max 可用 >=(x+y)/2 化为常数因子的 sum-order；不同见证不是同一 law 上的
additive lower bound。C2 v1 的显式 order 常数 1/32768、3/32768 均成立。
所有这些 lower 只限制发出的正概率网格，不限制内部 count 精度、深度或架构。

一阶曲线是 t=(1-u)/(1+2u)>1/2，且仅在1/10<=u<1/4 时落在 t 域。
条件 midpoint 的 t_Q<=3/8；统计两点 t∈[5/16,7/16]；平均格式 t=1/2。
因此三类下界见证都避开该曲线，上界仍含该曲线。

## 5. C1 前提及 source009 的范围审计

本次逐节阅读了当前 c1-proof-v1 的完整推导，同时核对 source009 proof/review/handoff
的实际范围。没有将 009 讨论审查转成新证据。当前 v1 已重写以下承重环节：

1. 直接证明 pi P=pi，R=σPσ（σ交换01/10），以及 R³ 的共同质量至少1/32。
   从 S_N 反向走 N-m 步至 S_m，再由同一 reverse kernel 生成整个 prefix，
   得 TV<= (31/32)^floor((N-m)/3)，不除以 pi_s。
2. 固定 horizon 下 Z=C-pD 的正交 martingale 增量给 E Z²=p(1-p)ED。
   间隔 visits 使用条件 MGF；row-stack 仅对确定 d 使用
   {D>=d,C<pd/2}⊆{B(d)<pd/2}，没有声称 C|D 是二项。
3. stationary-prefix row00 risk <=50000/(1+Mu)，row10 <=400000/(M+1)。
   row10 的 G/H/J 三块分别保留 rare p 的平方或 p log 系数；H 块用
   [y log_+(256y)+2y+4]e^(-y/8)<=108，而不是裸 log M 的界。
   再加未量化 mixing cap，足以达到当前 C1 的有限 N 常数，N<6 单独处理。
4. 完整历史条件实验等价于从00出发的反向链。其 drift 保留
   t U00=1-Pr(Y_n=00)+alpha*t U01，不能删除第一项。
   得 path KL<=40(1+(N-2)u)Delta²；选 Delta=1/[32sqrt(1+(N-2)u)]，
   Pinsker/testing 给所述 lower，包含任意 source-independent 随机核。
5. 平均 lower 在相同 u 的两点条件实验完成后才乘 u；u=1/8 给1/N。
   u_N=1/(N+1) 的条件非消失见证是 triangular，不否定固定正 u 的收敛。

数值常数的关键比较也已核算：row10 三块合为342528/M，
M>=64 时 <=400000/(M+1)；M+1>=N/4；reverse mixing项 <=73728/N；
条件 row00 的 (1+Nu)/(1+Mu)<=3。未发现须修补的承重步。

source009 明确只给指定 rare 二元族的 expected actual-terminal 率及旧 all-row
ceil converter 的条件 O(1/Q) 上界。它没有给本阶段 conditional 网格 sharp
分类，没有普通 pair-chain reversibility，没有 all-stationary-order2 C/N，
没有 almost-sure 或 full-history Laplace/KT 最优性，也没有新 native KL Fact。
其原实现 C1/count-snap Fact 只属于旧项目原范围；本阶段 C3 必须重新证明。

## 6. C3 强比较器及输入成本域：限定通过，完整实现仍待固定

最强合法基线可从同一完整观测按顺序消费符号，保持8个 T_abc 计数器和最近两位。
只在 j=3..m 增加一项；j>m 继续消费输入、更新末 pair，但停止计数。
最终以实际 S_N 选 T_s0,T_s1，执行本报告第3节的同一 clipping、half-up 和
固定 coordinate1 residual。N<6、Q=2、01/11 分支相同。它不知 u,t，也不用未来值。
因此只要 attention frontend 的名义计数恢复正确，最终输出逐路径逐比特相同，
平均和条件风险也相同。这里比较完整输入的同一信息，而不是把强基线排除出类。

该基线须收费：N 次输入访问、context shift、公开位置/停止控制、8个 triple match、
有条件 ripple increment、row mux、整数 readout、程序/地址/metadata、输出 b 位。
ell=ceil log2(N+2)，v=b+ell+8。顺序 counting block 的 live O(ell)、
active work O(N ell) 及 loop/address-safe O(N ell²) 可以保留，再加 readout
O(v²) active gates/O(v) scratch 和所选代码表示。8个计数器不是免费输入。

**成本域不能混用。** 若输入只在时刻0一次性全部给出，一次前馈 batch 网络必须保留
尚未消费的 O(N) 个符号/bit 及每层 holds；不能只加2N静态输入存储后仍称完整网络
width O(ell)。若选择外部顺序 arrivals，则输入调度/读取属于明确接口，两边都收费。
hybrid attention 的少层计数不含内部 softmax bit steps；flattened 电路必须另计。
相位分离时 p 通道应按生命周期释放，不应将 sparse、dense、streaming 各列的最小值
拼成一个不存在的共同预算。Big-O 共同上限和 identical bits 都不证明优化资源逐项支配。

Lead 当前 checkpoint 已写明这些域，并修正 row00 新 dividend 为 <16mQ，
不再重用旧 <8mQ；闭网格1需 h_A+1 位、signed recovery 和 Q_A 与 Q 分开。
但它自己注明：完整 word-op list、gate certificate、有限 frontend 全证明仍需出现。
本次不把“<64 word operations”或现有 O 资源表自动认证成完整 C3 接纳。
所审代码是在任意精度 Python 上解释所声明定宽算法，也不是机器整数 unit-cost 证据。

E_m 与 S_N 的区别是实际正确性条件，不只是成本记号。历史10001110、N=8、m=4
有 E_m=00、S_N=10。正确 selected counts=[1,0]；flow boundary 偷换 S_N 后是
[2,0]。本次在新代码中重现，旧失败保留。query/copy token 从未列为样本，eligible
keys 必须始终恰为3..m；任何完整 C3 版本必须据真实路径代数证明这三项。

## 7. 固定 primary 对照：假设—风险—量词—估计器—资源

只读取了下列两篇 pinned 本地 PDF。唯一新增定向检索是一条 Geiger/Böcherer
概率量化查询，并下载了同一作品的 published PDF；未继续追引文或泛搜。
一次 web PDF 镜像请求429，随后从 publisher PDF 链接获取成功；没有新增第二篇。
PDF 页码均为一基。来源 hash 与最小位置释义在 sources/primary-map-v1.md。

| Primary 固定版本 | 实际页/命题及适用性 | 本阶段不能偷换的量词/估计器/资源 |
|---|---|---|
| [Han–Jana–Wu，arXiv:2106.13947v2](https://arxiv.org/pdf/2106.13947v2)，修订记录2022-05-03、PDF日期2022-05-05，66页。SHA256 0b7b2e83fd0e405507eccb02b954129e4a0dc5f7926e1cc6d3a71f45e3e40cf7 | pp4–5 (8)–(9)、Theorem3/Corollary4；pp27–28 (65)/Lemma16：ordinary reversible irreducible first-order chains 的 actual-terminal KL；固定正 gap 下有 parametric rate，并不额外要求统一 min-pi。 | D1整体不能视为一阶类；四状态 pair chain 又不是 ordinary reversible。全轨迹 add-one 或相关构造不是本 prefix+gap predictor 的现成保证；没有当前 finite attention/输出 grid bit 资源。 |
| 同一 HJW v2 | p22 Theorem13 是 binary first-order gap-class rate。pp38–40 Lemma20、(94)–(96)、Theorems22/24：高阶 symbolic reversal 及全 stationary order-m 类；binary order2 minimax 为 log n/n。 | 后者的全类 upper 可给子类一个粗 upper；全类 lower 不能移入 D1。不是本 fixed-u conditional00 的现成 sharp theorem。高阶 upper 的概率赋值/add-one及stationary reduction亦不等同单 prefix 程序。 |
| 同一 HJW v2 | pp48–50 Lemmas30/31、(118)–(122)：特制高阶模型的 Frobenius estimation，uniform context stationary law、uniform positive transition bounds；借 nonreversible block-chain pseudo gap。 | D1 的 pi00=u→0、r→0 破坏这些 uniform 假设；该 Frobenius 结论不直接给 terminal KL 或本文条件表示率。按 Lemma31 明确假设及其证明核对，不把 Lemma30 文本抽取中显示的异常当可用新假设。 |
| [Paulin，arXiv:1212.2015v5](https://arxiv.org/pdf/1212.2015v5)，修订2018-11-13，42页。SHA256 7a54a70c47954687e87800c5e7dcc9df37a47568ed13f35c5c170a5728d92a82 | pp13–14 (3.2)–(3.4)、Proposition3.4/(3.9)–(3.10)：reverse/pseudo gap；point initial N_q=1/pi(s)。p16 Theorem3.7/(3.18)、p17 Theorem3.11/(3.25)：stationary nonreversible variance/Bernstein。 | 标准 count/mixing 工具，不提供本 unknown-(u,t) predictor 的 risk theorem。直接用 point initial 的 L2 prefactor 会引入1/u，不能宣称 uniform conditional00；不能替换 HJW 的 ordinary reversibility。 |
| 同一 Paulin v5 | p18 Proposition3.15/(3.29)、3.16/(3.32)：burn-in 后任意 path event 的 additive TV 比较；uniform ergodicity 的无 min-pi TV 衰减。 | 与本 reverse-prefix bridge 直接相关，但还要本地证明 reverse conditional experiment、loss cap、随机 row count 与 rare-successor KL。没有输出量化器或 finite resource ledger。v5编号不能照搬 HJW 引 Pau15 的旧编号。 |
| [Geiger–Böcherer，Greedy Algorithms for Optimal Distribution Approximation](https://doi.org/10.3390/e18070262)，Entropy18(7):262，published 2016-07-18，10页。SHA256 cae05b607164d7ff44315b3cd5ab1f9b00f5514bd799b3984f561cb72f4e6e84 | pp1–4 (1c)、Algorithm1/Proposition1、Table1、Lemma1：已给定有限正 target t，M>=support size，最小化 D(t||p) 的 M-type 分布，正支持及 greedy allocation；p5 Proposition2/(8)，p5–6 (10) 还有 Markov rows 的相同方向 divergence-rate 映射。 | 这是直接概率量化先例，不能忽略。target 已知；无未知-source、依赖 history、conditional terminal 或统计1/N项。其 greedy marginal-cost 比较也不是本文用整数商余实现的 bit-cost theorem；本文不声称 exact KL optimizer。 |

HJW 的两种 reversal 必须分清：D1 有 pi00*t=pi10*r、pi01/2=pi11/2，故符号
三元组满足其 Lemma20 的反序判据；但 pi00 P(00,01)=ut>0，
pi01 P(01,00)=0，已经否定普通 pair detailed balance。R=σPσ 也不等于 R=P。

新增 primary 的 p5、(9) 前一句印成 M>t_i 就声称 t∈P_M，这个条件显然不足：
例如 t=(.999,.001)、M=2。应依 p4 对 P_M={p:p_i>=1/M} 的定义核对，
采用每项 t_i>=1/M（其 p4 对(5) 使用 M>1/t_i 的充分条件），不能照抄该句。
这项条件纠正不影响本文自己的二元 grid 证明。对 source PDF 的 Lemma30 文本抽取中
异常的常数顺序，也只按后续明确 Lemma31 的假设使用，不从异常文字推出额外定理。

本次只能说：HJW/Paulin 不是 D1 上本完整共同程序的现成 theorem；直接概率量化
早有同方向 KL/正支持先例。不能据三篇的未覆盖声称发表级新颖，更不能宣称所有
nonreversible literature 都缺 parametric KL。未新增数学路线，未重开 parked 候选。

## 8. 明确反例及相应修复语句

这些反例限制错误扩张；除已保留的 endpoint 错误外，不表示 v1 正在使用错误论证。

| 被否定的简化/扩张 | 具体反例或反检查 | 必须保留的修复 |
|---|---|---|
| “C given random D 是 Binomial(D,t)” | M=2、row00、u=1/8,t=3/8：Pr(C=1|D=1)=11/16，不是3/8。 | 固定 horizon martingale 与确定长度 stack 分开。 |
| “交换输出坐标不影响二元预测” | t=a=1/4,Q=4：正确(3,1)/4 loss0；错为(1,3)/4，loss=(log3)/2。 | J明确是 next1；输出(Q-J,J)/Q。 |
| “最近网格就是精确 KL 最小点” | t=37/100,Q=4，欧氏最近 q1=1/4，KL≈.03521294；q1=1/2 的 KL≈.03419150 更小。 | 只称本 converter 达到 uniform minimax orders，不称逐 target 精确 KL 最优。 |
| “row10 也可固定正下截断” | 任意固定 lower clip tau>0，t=1/2,u↓0，row10 p0=r↓0；该行的极限 loss至少 -log(1-tau)>0，质量趋1/3。 | row10 仅上截，允许其估计向0；不能据这种错误 converter 维持 uniform C/N。 |
| “E_m 可改成实际 query” | 历史10001110，正确counts[1,0]，错误[2,0]。 | flow correction用 E_m，选行用 S_N，分别付费绑定。 |
| “任意历史上零输出都令条件00风险无限” | 只在 terminal10 输出(0,1)，其他行uniform：平均risk无限，conditional00却有限。 | 条件零输出论证只用于终止00的正质量历史；v1已作正确限定。 |
| “symbolic reversal 足以套普通可逆定理” | P(00,01)>0而P(01,00)=0，pi均正。 | 保留普通 detailed-balance 失败及 reverse-conjugacy 的不同作用。 |
| “minimax lower 是每个 fixed law 的量化误差” | 取u=1/8,t=1/4,Q=4，row00真值在网格上，其表示误差可为0。 | 条件下界是sup_t midpoint witness，不是每个 t 的pointwise floor。 |

不同统计/格式见证只经 minimax max 合并，不需要把下界变成每源之和。

用普通中文解释两种精度：00 情境虽然少见，但它内部两种结果的真实概率都离0和1
有固定距离；就这一情境看，把概率舍入半格只造成平方级 KL 损失，即1/Q²。
10 情境本身却有接近1/3的质量，而其中一种结果可以任意稀少。严格正网格仍须给
稀少结果至少1/Q的概率，这会从常见结果挪走约1/Q质量，产生一阶损失。
因此平均风险受1/Q瓶颈约束，条件00可达到1/Q²；这两者完全可以由同一程序实现，
也不表示内部计算位数已经达到任何必要下界。

## 9. 可复现诊断、待交付与 Euler 记录

独立新脚本 check_adversarial_v1.py 仅写本目录。35组有理距离 oracle 检查（含两个
half ties、clipped endpoints、zero和off-nominal D<=2M guard）、row10 residual、
Q2/Q4、b=1024 uniform 分支；6条whole-history reference，其中2条实际 finite-head
检查；4个 grid midpoint；16个长度4路径的精确有理 conditional-count 反例，均 PASS。
重现 wrong endpoint 和上述 nearest≠KL optimizer 的反例。没有运行旧 diagnostic，
没有 statistical simulation。有限检查不是全 N/Q 证明或 native evidence。

Lead 下一步应固定 C3/C4 全包和 primary 映射，先读本报告，再送独立 Verifier。
C1 可按当前 v1 进入后续独立审查；C2 数学稿无需因本报告改式，但须等待 C1 native
接纳并以真实 C1 Fact ID 为 predecessor。完整 C3 的 gate/word counts 仍需证明，
不能用本次 comparator 审查代替。其后才是 root admission 与 final_audit。

Euler 已记录 C4 的证据/综合缺口，诊断 failure ID：
`0def94abb5dd20e9fc11024c4f656ce7f0d77ef78740e17ef61155836d95a99d`，
event ID：`cfa92b3aa233276487bba8e5ca2e68f2cb9605e2705f47282edf5e02ca287ab6`。
该记录不是 C2 反证，不更改已有 routes 或合同。本成员尝试通过 euler_team_ask
咨询 Prover/Lead，但工具只允许 Lead 调度，明确返回
“only the lead may schedule team consultations”；没有虚构任何成员答复。

新 Fact IDs=[]；新 Evidence IDs=[]；submit_proof calls=0。
[Non-scientific operational metadata omitted.]
没有 continued-research 开关，没有原 campaign 访问、模型 CLI、替代 agent、旧源改写、
旧图手工编辑或旧根操作。所有旧失败和 queues 保留，007/014/018/019/020 未重开。
阶段 C1–C4 即使日后接纳，也不表示 v10 母问题/T1→T2→T3 的全部研究完成。
