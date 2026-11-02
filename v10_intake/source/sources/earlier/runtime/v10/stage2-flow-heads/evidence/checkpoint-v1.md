# D3 因果电路与有限实现 checkpoint v1

日期：2026-10-25。项目 icml-flow-heads；contract
22e80d3d620c36cfc0bbd297101a5efabe634d7fd696b4cae200963af52af02a；root
2b80c631152f22bae0797d03b25703a6dc785dcec5fe5f9c8dd4078ed8243b38。

**状态：Lead 的待审推导，不是 Fact，不 discharge C1–C4。**
本文选择 D5 明许的固定局部掩码、无 LayerNorm、ReLU 点计算、有限字长评价模型。
§1–5 给出可直接核查的电路和误差推导；§6 的有限神经资源构造仍须由 Prover 完成逐门证明。
不调用旧阶段已接纳结论。已阅读本项目 PROBLEM、AUTONOMOUS_RESEARCH、总计划v10、
previous-stage/stage-synthesis-zh 与 previous-stage/IDENTITY；后者标识旧阶段来源，不是当前身份。

## 1. 位置、输入、复制与全部残差

固定 K≥2，N≥3，M=N−2。序列包含 N 个已观察符号位置和第 N+1 个**合成查询位置**；
后者没有 X_(N+1)。每个历史输入为 x_t=e_(X_t)。付费位置元数据给出 t、历史/查询类型、
z_t=1{t=3}、N；可以用 O(N log(N+2)) 位展开存储，或 O(log(N+2)) 位规则程序生成。
本稿按展开版本计费以免隐去成本。查询另含模式位及两个 K 维 one-hot 外部 s=(a,b)。

第一注意力层有**两个局部复制头**，Q=K=0、V=x_t，固定 singleton 因果掩码分别指向
t−1 和 t−2；在不存在前项的早期行用自身作无关 fallback。这两行从全局统计中排除。
softmax 在 singleton 上为1，故合法历史 t≥3 获得 l1_t=e_(X_(t−1))、l2_t=e_(X_(t−2))。
当前 x_t 经 residual 保留。在查询位置，这同样两个头获得 l1_q=e_(X_N)、l2_q=e_(X_(N−1))。
所以**无需额外端点头，但这两个头必须计入**，且 endpoint 两个 K 维槽不能丢。

复制输出写入最初为0的独立 residual 槽，无叠加污染。再用 ReLU(l1_t,c+z_t−1)
生成 F_t,c=z_t l1_t,c（K个门）。查询的模式门选定查询 one-hot A=e_a、B=e_b；
实际模式选 (l2_q,l1_q)，固定情境模式选外部 s。门对0/1输入精确，例如
ReLU(v+mode−1)+ReLU(w−mode)。**实际 E_N 始终另存 (l2_q,l1_q)，不能由外部 s 覆盖。**

第二注意力层在查询行只允许 keys t=3,…,N（显式因果历史掩码）；历史行只允许合法前缀，
无合法前缀的行允许自身且输出不用。位置掩码的存储、生成及扫描操作均计费。
后续读出只能作用于查询 residual；没有读取历史位置的额外 attention。

## 2. 四个统计头的 Q/K/V 和可见表示

采用 softmax(Q·K) 的未缩放点积约定；若库固定除以 sqrt(d)，需把其补偿及近似另记账。
此约定本身是标准缩放可选的 causal softmax attention，不把 sqrt(d) 当精确有限常数。

|头|查询 Q|历史 K_t|历史 V_t|输出|
|---|---|---|---|---|
|P1|((log2)A,(log2)B)|(l2_t,l1_t)|(x_t,l2_t)|(q1,v1)|
|P2|((log2)A,(log3)B)|(l2_t,l1_t)|(x_t,l2_t)|(q2,v2)|
|T| (log2)B | l2_t |(l1_t,F_t)|(h,h0)|
|0|0|0|(l2_t,l1_t,F_t,z_t)|(alpha,nu,f,rho)|

P1/P2 的 QK 维度各2K，T为K，uniform可用1；各自 value 维度为2K、2K、2K、3K+1。
故四头总输出 **9K+1** 个标量，无 K² pair 或 K³ triple 表。
这里只是 alphabetic interface。所有 QKV 的完整矩阵和后续算术神经宽度另计。

U_k=∑_i A_i v_(k,i) 用 K 个选择门、一次求和实现。对 v∈[0,1]，
ReLU(v+A_i−1)=A_i v，故这里无 query-dependent 历史 value。
同样选择 alpha_b、nu_b。末端向量 J_c=1{E_N=(b,c)} 由 query B 与
l2_q 的交集求出单 bit，再与 l1_q,c 作 AND；总 O(K) 门，保留整个 J 而不是换入 s。

在全局层后指定完整可见寄存器：9K+1 个头输出、A/B、实际 endpoint 两个 one-hot、
模式、N和位置常量、上述同查询 residual 的所有副本；读出中的每一复制/暂存也登记。
历史 x,l1,l2,F 仍是前向评价工作空间，**不是此后读出可读取的旁路**。
若 C3 把对手权限扩展到整个历史工作空间，不能使用本摘要切口的下界；必须重新证明。

二元映射为符号 ±1 时 1{i=a}=(1+ai)/2，logit 行常数去掉后成为
beta1 ai+beta2 bj，2beta1=log(1+gamma)、2beta2=log(1+lambda)。
这里 gamma=1、lambda∈{1,2}。K>2 完全由上表 categorical 电路定义，不引用均匀二元谱结论。

## 3. 边界与 normalizer：逐条历史的证明

以下均为理想头输出。令 c_(ab,c)=C_(ab,c)/M，u_ij=n_ij/M；
alpha_i=u_i.，nu_j=u_.j，rho=1/M，f_c=rho 1{X2=c}。
T的平均权重为 dT=1+alpha_b，因此

    dT h_c = nu_c+u_bc,
    dT h0_c = f_c+rho 1{(X1,X2)=(b,c)}.

这里第二式直接来自唯一 z_t=1 的 t=3，不能把 f 当初始 pair。
设 initial_bc=dT h0_c−f_c，令

    g_bc=(dT h_c−nu_c)+rho J_c−initial_bc.

历史中的相邻 pair 从 (X1,X2),…,(X_(N−2),X_(N−1)) 平移为
(X2,X3),…,(X_(N−1),X_N)，中间项抵消，所以 g_bc=G_bc/M。
N=3 也成立：相减的起点 pair 与留下的终点 pair 都不能忽略。

写 A_t=1{lag2=a}、B_t=1{lag1=b}。P_k 的未归一化权重为
(1+A_t)(1+lambda_k B_t)，平均权重

    d_k=1+alpha_a+lambda_k nu_b+lambda_k u_ab.
    d_k U_k=2(alpha_a+lambda_k u_ab).

两式消去括号得 d_k(1−U_k/2)=1+lambda_k nu_b，所以

    d_k=(1+lambda_k nu_b)/(1−U_k/2),  1−U_k/2∈[1/2,1].

d1∈[1,4]、d2∈[1,6]。本 normalizer 不需要小 u_ab 的 reciprocal。
再展开每个 next-symbol 分子，r_c=M^−1∑1{X_t=c}、
A_c=M^−1∑1{lag2=a,X_t=c}，得到

    d_k q_(k,c)=r_c+A_c+lambda_k g_bc+lambda_k c_(ab,c).

两头相减抵消 r_c+A_c，故

    c_(ab,c)=d2 q_(2,c)−d1 q_(1,c)−g_bc.
    u_ab=(d2 U2−d1 U1)/2.

也可从 d_k−1−alpha_a−lambda_k nu_b 再除 lambda_k 得 u_ab。
这些输出不需要显式形成全部 pair 表。主读出使用 ∑_c clip(c_tilde,c) 作分母，
而不以独立、可能不相容的 u_tilde 替代该和；u恢复式保留作核查和后继分析。

## 4. 定位误差账本（同一条路径，不假设独立）

先把所有原本属于[0,1]的头坐标 clip 到[0,1]。设这些坐标与理想值的逐坐标差≤eta，
one-hot 查询、位置位及复制端点本节精确；算术的每次乘法/除法绝对误差≤zeta。
加减和2的乘除通过保留足够整数位/小数位精确执行。恢复 d 的分母由剪裁后 U 构成，
仍≥1/2。以下公式没有把统计误差当独立坐标噪声。

令 d_tilde_k 为带一次除法误差的恢复。对 n=1+lambda nu、v=1−U/2，
|n_tilde/v_tilde−n/v|≤2lambda eta+4(1+lambda)eta/2，因而

|模块|逐坐标绝对误差上界|
|---|---|
|dT|eta|
|d1|6eta+zeta|
|d2|10eta+zeta|
|u_bc=dT h−nu|4eta+zeta|
|initial=dT h0−f|4eta+zeta|
|rho J|eta（bit选择精确）|
|g|9eta+2zeta|
|d1 q1|10eta+2zeta|
|d2 q2|16eta+2zeta|
|c恢复|**35eta+6zeta**|
|独立u恢复|13eta+2zeta|

例如 d_k q_k 的差≤d_k eta+|d_tilde_k−d_k|，因为 q_tilde∈[0,1]，再加乘法误差。
故上表对相关、同向或对抗误差均成立。把 c_tilde clip 到[0,1]不增大对真实 c 的误差。

前级 softmax 误差接口也明示：若各 logit 误差≤sigma，value误差≤v，
且有限评价/聚合后另有坐标误差 a，则可取 eta≤v+(exp(2sigma)−1)+a。
理由是归一化权重逐项比在[exp(−2sigma),exp(2sigma)]；对[0,1] values，
加权和差由权重的L1差界定。singleton binding 本构造无近似误差。
若端点本身受扰，则 rho J 项须额外加入 |rho_tilde|·error(J)，不能沿用表中 eta。
若 query被扰，选择门及 score同样须重算。以上不是所有层统一扰动定理。

## 5. 零计数、平滑和精确有限 simplex 码

设所有用于读出的数在2^−b网格上，b≥ceil(log2 M)+1。设
r0=2^(−ceil(log2 M)−1)，r=max(rho_tilde,r0)，把rho_tilde事先clip到[0,1]。
r0≤rho/2，故 r>0 且 |r−rho|≤eta。r0依赖已声明N，不依赖theta；其存储和比较计费。
令 a_c=clip(c_tilde,c,0,1)，x_c=a_c+r，S=∑x_c>0。理想 normalized readout为x/S。
这也处理 n_ab=0；理想无误差时为 add-one (C_(ab,c)+1)/(n_ab+K)，未出现情境输出uniform。

有限输出不是用一个近似 reciprocal 后直接宣称和为1。设Q=2^b，将x乘Q得到正整数V_c，
T=∑V_c，用**付费整数长除法**形成 m_c=floor(Q V_c/T)，c=0,…,K−2；
m_(K−1)=Q−∑_(c<K−1)m_c。输出 m/Q 为精确合法simplex。
TV(m/Q,x/S)≤(K−1)/Q。这个规则允许最后一坐标有不同量化误差，并须在C3完整码中保留。

对任何正向量x,y，TV(x/∑x,y/∑y)≤||x−y||_1/∑y。
取y_c=c_(ab,c)+rho，E=35eta+6zeta，得到

    TV(Pi_(N,b)(s), p_add1,N(s))
       ≤ K(E+eta)/(u_ab+K/M)+(K−1)2^−b
       ≤ M(36eta+6zeta)+(K−1)2^−b.                    (★)

这是逐路径统一实现界；实际终点查询可直接代入，无独立性假设。
稀有情境只在最后条件化进入1/(u_ab+K/M)，未凭空产生 u^−2。
给定 eta,zeta≤2^−b，一个充足的theta无关目标是

    b_N=ceil(log2(1024 K (N+1)^3))+ceil(log2 M)+2.

更紧日程可由Prover给出；此处只证明(★)一旦实现后趋零，不声称该日程最优。
对固定严格正theta，pair链两步可到所有pair、自环存在，有限链不可约且非周期；
遍历计数 u_ab→pi_ab>0、c_(ab,c)→pi_ab theta_(ab,c)，所以add-one最大情境误差趋零。
有限K可取最大值，实际末查询误差≤该最大值；TV≤1给出期望收敛。
进一步 E[err·1{E_N=s}]/P(E_N=s)≤E[max err]/pi_s→0（平稳初始化），
所以固定s的终点条件期望也收敛。上述为待核验证明骨架，不是已接纳T1。

## 6. 有限实现的具体构造和待封口成本

**不得把log2/log3或attention评价当有限精度精确oracle。** 一种待Prover逐门确认的保守实现如下。
为输出b位，内部取 p=4b+4ceil(log2(N+K+2))+32 位工作精度，另存O(log(N+K))整数位。
log2、log3 用log x=2∑ y^(2j+1)/(2j+1)，y=(x−1)/(x+1)，j到p项，
y≤1/2；尾项几何界，系数以p位dyadic编码。只计算两个常数并存入Q投影，无theta。
截断exp在[0,2]的Taylor到8p项，以p位运算评价；给出累计舍入后再次留guard bits。
分母≤8M，非零且≥M/2，长除法给b位head坐标。uniform/partial也按同评价规则收费。
此段的**明确剩余证明**是把尾项、O(p)次舍入和M次求和合成eta≤2^−b；
若此p不足，必须改p并保留修正，不能默认成立。

读出采用位电路，不借用旧通用编译器。b位整数比较、加法、乘法、带余数除法各有
逐位/学校算法，乘除 O(b²) Boolean门；AND(x,y)=ReLU(x+y−1)，NOT(x)=1−x，
XOR由有限个同类门构成。连续标量到位通道不能免费：对网格整数A，
最高位为ReLU(A−(2^(b−1)−1))−ReLU(A−2^(b−1))，减去该位贡献后递归。
该转换在声明的网格上精确，O(b)门/深度，系数需O(b)位，**不声称在连续实数上精确floor**。
各有理算术按上述门实现、截断到b位，乘除误差≤2^−b；除法中间整数足够长避免溢出。
中间寄存器可用带符号整数，恢复c保守范围[-16,16]，最后clip再平滑。

资源提案（是本具体宽松实现的上界目标，未作最优或全网络O(K)声称）：

|资源|计费与预计上界|
|---|---|
|统计alphabetic通道|QK最大2K，总value 9K+1；pre-readout残差≤32K+16槽|
|attention头|局部2 + 统计4 = 共6个头模块；单层最多4；后续读出层attention禁用|
|attention阶段|局部复制、flag/query门、全局统计，O(1)层，singleton与合法历史掩码显式|
|全神经宽度 W|位展开后O(Kp)，不等于O(K)标量接口|
|全深度 L|保守顺序安排读出 O(Kp²)，包含恒等残差保持；不主张需要这么深|
|QK维数 D_qk|最大2K；local可用1|
|参数字长 B_param|O(p+log(N+K))，包括log近似、位提取的2^p权重及位置常量|
|算术字长 B_arith|O(p+log(N+K))；整数累加和乘积用常数倍字长|
|稀疏非零程序/参数|O(K²+Kp²)个系数/门（含完整QKV矩阵的保守K²收费），门地址另O(log(Kp))位|
|标准逐层dense存储|O(L W²) = O(K³p⁴)个槽，即使为0也收费；每槽B_param位|
|工作bits|逐层滚动O((N+1)Kp²)加参数；若存全层激活则再乘L|
|固定mask/位置存储|O(Nlog(N+2))位索引；若实现dense布尔mask则O(N²)位|
|前向bit操作|dense保守O((N+1)²(K+p)p³ +(N+1)K³p⁵)；分开attention评价与点网络|
|score_range|理想统计范围≤log6；有限log编码扩展O(2^−p)，可统一声明上限2；local允许项全0|

这里value和端点操作按全K计；max_s陈述是对同一个query输入族逐一取最大，
**没有免费同时运行K²个query**。如果实验同时输出全部情境，时间/输出存储另乘K²。
工作空间只保留必要前向层时可以更省，但须明示执行计划后才缩减上述界。
同预算baseline也可以使用这些宽度、深度、精度、score上限2和局部掩码，并自由重分配。

## 7. 与种子检查的差别、真实障碍和下一单元

已人工核对 inputs/flow-seed/check_flow_seed.py。它检查二元所有N=3,…,9历史、全部query，
加100条三元随机历史/全部query，总4964个Fraction案例；包括flag、boundary、normalizer。
没有重跑以增加计数，没有将其当网络、风险或新颖性认证。其循环本身也不证明所有K,N。
本稿§3给出一般索引证明，§1–2给出实际QKV/局部复制，§4–6补充实现与误差对象。

当前最承重缺口按依赖为：

1. Prover封口有限softmax与读出逐门资源、theta无关日程及一般非均匀D1的C1固定版本。
   若数字化ReLU接口违反D5或字长范围不足，给具体反例/修正；不能把这个候选实现视作已成立。
2. 在同一个完整码上给C2联合有限N事件（计数鞅/占据次数），再接(★)；所有统计共用路径事件。
3. Counter检查完整可见码的旁路与强浅层/校正/joint-feature/同score预算尖化baseline；
   精确核rank只约束该核的表示。primary逐项对照应覆盖itemwise、差分/包含排除和count recovery。
4. C3不能由§4这条上界单独关闭：还缺具体定位误差的失败/反构造，以及真实有限N风险结果和相容上界。
5. 最终C1–C3接入同版本包、独立审查、原生submit，才进入C4；旧阶段SOLVED完全冻结。

[Non-scientific private operational paragraph omitted from the public export.]
本单元不使用GPU；为最终审计显式保留0 GPU毫秒（审计无需GPU），其余无限维度不虚构数值配额。
[Non-scientific private operational paragraph omitted from the public export.]
