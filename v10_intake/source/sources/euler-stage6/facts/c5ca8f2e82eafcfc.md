---
fact_id: c5ca8f2e82eafcfc
problem_id: icml-general-prediction
author: prover
predecessors: [8a4d1b9aef15dae8, a53804d650803060, fef8372728290b45]
glossary_introduces: {}
external_refs: []
statement_chars: 6141
---

## statement
# ANCHOR-PRECISION-RISK：固定锚定读出的精度—实际风险及一个粗精度失败配置

这是020之后的独立nonroot科学义务。020 Fact8a4d1b9aef15dae8及其Evidence3ff58057b04b6befec3ddaa73e01d996e10fdb69caf7719520f48d5f4d315692保持原scope；本项不扩写其精确恢复参数域。021精确旧cap核查本轮收束，022保持OPEN/PARKED，不是本项前提。已恢复core及尚未解决的接线/alias/地址/微码/phase问题原样保留。不新做旧cap、compiler枚举或调度修复。

来源设计资料 inputs/anchor-precision-risk-seed-20261029.md 和 anchor-precision-risk-precheck-20261029.md 当时尚未接纳，不能将来源材料标记当作独立科学证据。下述上界是标准有限误差与截断推论；新增可判别部分是指定粗配置在真实四头联合输出上的实际风险。整个合取经正常网关才可接纳，不拆常数节点，以首引理替代完整目标。

## 1. 全域、量词与新程序

所有整数K>=2、M>=1，N=M+2、n=q=N+1，字母表{0,...,K-1}。每次实验内theta固定为任意允许零边的齐次二阶表，mu为任意初始对律。只观察完整X_1^N，Y_i=(X_(i+1),X_(i+2))，departure为i=0,...,M-1，actual目标为theta_(Y_M)。风险始终为同轨迹E[TV]，TV=L1/2；sup可随公开参数选源。程序不读theta、mu、未来或辅助行栈。

定义h0=max(4,ceil(log2 M)+1)，整数h>=h0，Q=2^h，b=ceil(log2(M+1))，ell=ceil(log2(N+K+2))，D_*=4M+1，p=4h+4ell+64，并独立选择整数g：

    g_min=max(h,ceil(log2(8D_*))),
    g_min<=g<=g_0=max(h,2b+12),
    G=2^g, u=4g+4ell+64.                            (DOMAIN)

需证明区间非空、g>=h>=b、u<=2p。所有整数配置有有限位长/移位构造。

F_(K,M,h,g)保留020的同一六头共享因果batch hybrid前端、局部query、q外部/actual模式选择与half-up/clip decoder，仅重生成内部精度相关常数、有限求值和网格。两singleton复制头取得历史lag2/lag1及q已观察末对。q的token为零；f_t=1{t=q}；统计key为((1-f_t)lag2_t,(1-f_t)lag1_t)，value为(x_t,f_t)。四头(alpha,beta)∈{0,1}²的query为(alpha L2 A,beta L2 B)，A,B是该token合法局部query的one-hot。q选择最终query，过去位置不提前获得它。

q的统计mask为{3,...,N,q}；其他行是{3,...,t}，空集self fallback。mask为有限bits。所有n位置完整执行、收费，每次只暴露q一个query输出。后端只访问四头返回、公开量及声明精确bits，不回读历史。

精确冻结有限求值如下。R=2^u，先有理生成

    V=2 sum_(j=0)^(u-1) 1/[3^(2j+1)(2j+1)],
    L2=floor(R V)/R.

对每个完整score s=S/R∈{0,L2,2L2}分别计算

    T_0=R, T_j=floor(T_(j-1) S/(jR)), 1<=j<=8u,
    W(S)=sum_(j=0)^(8u)T_j.

保留full product和余数。对每个非空mask精确累加D_int=sum W、A_int=sum W v，返回网格分子floor(G A_int/D_int)。cached实现只缓存三个完整score的各自递推结果，不能把exp(L2)的舍入结果平方代替2L2求值。zero score的W=R准确。

每个位置的四头label/anchor分子记Y_(ab),c、Z_(ab)。执行：

    Z_safe=max(1,Z),
    U_(ab),c=clip_[0,4M](floor((2Y_(ab),c+Z_safe)/(2Z_safe))),
    C'_c=clip_[0,M](U_11,c-U_10,c-U_01,c+U_00,c),
    B_c=C'_c+1, B_sum=sum_c B_c,
    m_c=floor(Q B_c/B_sum) (c<K-1),
    m_(K-1)=Q-sum_(c<K-1)m_c, F_c=m_c/Q.             (PROGRAM)

不得改变舍入/clip顺序。非q的Z可能为0，sum C'可达KM，必须容纳；所有路径、query、两模式均合法，含M=1、无访问行、网格端点及源支持不相容历史。

## 2. 全路径误差、统一actual上界和风险配置

理想四头沿020的乘积展开定义D_ab=1+sum w_ab、S_ab,c=sum w_ab 1{x_t=c}，w_ab∈{1,2,4}。则S+1<=D<=D_*，C_c=S_11,c-S_10,c-S_01,c+S_00,c是真实完整triple count，J=sum C，p_c^+=(C_c+1)/(J+K)。需要为新g重述：有限log误差<2·2^-u，单weight误差<=100u2^-u，网格化前每坐标比值误差<=200u2^-u，网格化后HEAD误差<=2/G；score∈[0,2]。前一更强误差界亦用于第三节，不能只用独立的HEAD区间替代实际输出。

待证在q，Z>=1，且

    |Y/Z-S|<=4D_*²/G,
    |C'_c-C_c|<=e, e=16D_*²/G+2,
    TV(F_(h,g)(x;s),p_s^+(x))
      <=min(1,K e/(J_s+K))+(K-1)/Q.                 (PATH)

最后归一化必须以真实正向量C+1及其总和J+K证明；两次clip是向含真实值的区间投影，half-up每项另付1/2。非q概率合法性独立证明。

令T=K^(5/2)/sqrt(M+1)，Psi(0)=0，Psi(x)=x(1+ln(1/x))于0<x<1，Psi(x)=1于x>=1。定义

    R(K,M,h,g)=sup_(theta,mu) E TV(F_(h,g)(X;Y_M),theta_(Y_M)).

使用016 Fact a53804d650803060的实际48T及TRUNC，证明

    R(K,M,h,g)<=min(1,48T+(K-1)/Q+Psi(x)),
    x=K^5[16D_*²/G+2]/(M+1)
      <=256K^5 M/G+2K^5/(M+1).                      (RISK)

TRUNC的实阈值取整、J=0、小M和零参数保持。对每个固定K，任何合法公开序列h_M,g_M，若G_M/M→∞，则R(K,M,h_M,g_M)→0。特别h=h0且G按M^(1+epsilon)向上取二次幂，固定0<epsilon<1，在充分大M进入DOMAIN，给M<<G<<M²的充分配置。此结论不声称必要性。

给定0<tau<1，保留48T+(K-1)/Q+Psi(x)<=tau这个有限充分证书，并给出可检查的显式选择：

    M+1 >= (144 K^(5/2)/tau)^2,
    h=max(h0,ceil(log2(3(K-1)/tau))),
    H=16K^5 D_*² / [(M+1)tau²/36-2K^5],
    g=max(g_min,ceil(log2 H)).                      (TAU)

需证明分母正、此g<=g_0、R<=tau；如上述表达式有真缺口须登记修复，不默许超出DOMAIN。此处使用Psi(x)<=2sqrt(x)只是显式充分配置的松弛。平方根界也足以推出G/M→∞时一致，不能说其一致性需要M²；只有要求保持M^-1/2实现误差阶时，它才给粗的M²充分尺度。TAU不声称最优精度或新的样本下界。

## 3. 一个完全指定的coarse配置：真实联合四头的失败见证

令K=2，对所有M取公开h_c(M)=h0(M)、g_c(M)=g_min(M,h0)。G_c=2^g_c满足G_c=Theta(M)。待证该特定配置不uniform actual一致，具体用以下同一个固定合法源，不引入任何新观察实验：

    theta_00=delta_1, theta_01=delta_1,
    theta_11=delta_0, theta_10=delta_0, mu=delta_00.

真实pair路径是00→01→11→10→00的确定周期。沿公开子序列M_r=3·2^r，整数r>=2，真实末对Y_M=00，真实下一符号律delta_1；每个triple 001、011、110、100恰出现M_r/4次。待证实际有限程序给

    lim_(r→∞) E TV(F_(2,M_r,h_c,g_c)(X;Y_M),theta_(Y_M))=1/12,
    limsup_(M→∞) R(2,M,h_c(M),g_c(M))>=1/12.         (COARSE-FAIL)

必须从同一路径产生全部四头。可核候选计算链为：在M_r上h_c=r+3，g_c=r+7，u=8r+100，G/M=128/3。按头顺序00、10、01、11，D/M趋于(1,3/2,3/2,9/4)，label0的S/M=(1/2,1/2,3/4,3/4)，label1的S/M=(1/2,1,3/4,3/2)。量化前误差乘G趋于0，理想G/D的极限(128/3,256/9,256/9,512/27)均非整数；应推出真实Z最终为(42,28,28,18)。须再逐项验证half-up、两次clip、add-one及ordered final floor，从而

    (C'_0/M,C'_1/M)→(16/567,176/567),
    F→(1/12,11/12).

该计算链及有限诊断是待独立验证的证明候选，不是Fact。若失败，保持义务OPEN并登记精确失败点；不能以独立选择HEAD误差、理想实数输出或其他decoder替代。

这是一个指定coarse配置、固定decoder的反例；不证明每个G=Theta(M)配置都失败，不证明G/M→∞对全配置必要，不推广为任意decoder、所有attention或一般Transformer资源下界。[Non-scientific operational metadata omitted.]

## 4. 实际u的完整收费资源及范围

从020已接纳构件核实新DOMAIN中的同一收费实现，精度字长为实际u，不自动以p或原p_a替换。要求沿其完整batch hybrid模型保持下列统一构造上界：L=O(Ku²)、per-token W=O(Ku)，6总heads/最多同层4、max QK=2K、统计value维K+1、score<=2；在线coefficient/arithmetic完整word<=128u；dense slots O(K³u⁴)、dense参数bits O(K³u⁵)、active gates/projections O(Ku²+K²)、holds O(K²u³)。

主配置固定dense/uncached：全部n点运算/QKV O(nK³u⁶)，attention O(n²(K+u)u²)，mask/position O(n²+n log(n+1))，input/query/mode/endpoint/flag取得、转换、保存及residual/copy/hold/clear/decode全部收费。有限log work O(u³log²(u+1))、scratch O(u log(u+1))，code O(u⁴)。

令P_u=K³u⁵+n²+nKu²+u⁴+u log(u+1)。复核program/参数/code、已存input、masks、QKV、rolling层、四头银行、controller/address、完整算术scratch和output逐phase共存求和，online/offline总peak O(P_u)。完整offline生成/整理及包括dense零项的真实格式写出work为O(K³u⁶+n²u²+u³log²(u+1))。这些是同源构件的解析上界核实，不要求旧十进制cap、literal ledger或compiler。须明说未运行这些测量。

若讨论cached或sparse，独立列出其完整cache/selector/代码/格式费用，不与主配置混合。u<=2p仅给共同常数倍包络，不给原128p的逐数值word结论、020对Pi支配、最优work/width或资源必要性。COARSE-FAIL证明亦不扩展SRC的master故障接口。

## 5. 依赖与执行门槛

实际预期前驱为020 Fact8a4d1b9aef15dae8（固定前端/decoder及收费构件）、016 Facta53804d650803060（48T/TRUNC）、SRC Factfef8372728290b45（实际有限运算构件，若正文实质直接使用即登记）。若自足重述使某前驱不实际必需，提交时如实报告，不隐藏真正依赖。G/U已由016支持所需统计引理，不为此重审旧root。022及021均无数学前驱关系。

完整 PATH/RISK/TAU/COARSE-FAIL/新参数资源合取需要独立审查；补充检查重点是四头联合可达性、Z 的 floor 稳定、两次 clip、最终归一化抵消和量词。[Private task allocation omitted from the public export.][Non-scientific operational metadata omitted.]新输入和上述具体数学见证是选择性接续的依据。旧接纳及依赖保持，不为新义务添加任何逆向前提。完成本合取仍不宣称v10母题解决。


## proof
Original contract and explicit scope for this proof:
{"contract_id":"e6b7592e781948d00eb2a2effb80d8e3ef77e480f8d70f960286bc33faf730af","definitions":"## A. 共同源、观察、算法及风险定义\n\n对每个整数 K>=2，A={0,...,K-1}，S=A²，D=K²。一个实验固定一个时间齐次二阶表 theta∈(Delta(A))^S，允许零坐标；初始对分布 mu∈Delta(S) 任意。令\n\n    Y_j=(X_(j+1),X_(j+2)),\n    P_theta((a,b),(b,c))=theta_(a,b)(c),\n    N>=3, M=N-2, E_N=Y_M,\n    n_s(M)=sum_(j=0)^(M-1)1{Y_j=s},\n    C_s,c(M)=sum_(j=0)^(M-1)1{Y_j=s,X_(j+3)=c},\n    p_s^+=(C_s+1)/(n_s+K).\n\n每次预测完整观察 X_1^N。最后一个计数后继是 X_N；Y_M 不是额外 departure。actual query 从已观察最后两符号取得；fixed-query 任务另有明确的公开 s。X_(N+1)、theta、mu、支持、闭类、平稳律、未来行栈及隐藏源标签不可见。外部 query 是同一历史下调用的查询参数，不额外赠送干净端点或统计量。获得和复制实际端点在实现中收费。\n\n共同算法族的程序和公开精度可以依赖 K,N,h，不能依赖未知 theta,mu 或其隐藏标签。统计根中的理想 p^+ 是分析变量；给定实现的计数、头输出等实际可见代码由来源实现义务确定，不能据理想表达式新增 readout 端口。比较中的任意全历史预测器可以用全部 X_1^N 和源独立随机种子，输出任意概率向量。具体 Pi 则遵守自己已声明的内部信息切口。\n\nTV(p,q)=1/2 sum_c|p_c-q_c|。对给定 family F，令 Z_N(s)=TV(F_(K,N,h)(X_1^N;s),theta_s)。严格区分：\n\n| 名称 | 定义 | 量词 |\n|---|---|---|\n| fixed row | E Z_N(s) | 固定公开 s |\n| all contexts | E max_(s∈S) Z_N(s)；另可问其 a.s. 极限 | 全 K² 行，不改成访问行 |\n| actual terminal | R_act=E Z_N(E_N) | 同一历史的末尾 query |\n| conditional terminal | E[Z_N(E_N)\\|E_N=s] | 仅当 p_N(s)=mu P^M(s)>0；零概率时未定义 |\n| empirical weighted | E sum_s(n_s/M)Z_N(s) | 同历史频率权重 |\n| other history weighted | E sum_s w_s(X_1^N)Z_N(s) | w 为观察历史可测 simplex；不自动有一致性 |\n\n逐源极限固定 K,theta,mu 后令 N→∞。统一均值是每个 N 的 sup_(theta,mu) R_act；取 supremum 时源可随 N 改选，但一个样本路径内部的核必须齐次。固定 K 的统一结论不是 K 随 N 变化的无条件结论，也不是 changing-source 的统一几乎处处结论。输出允许零坐标，损失仅 TV，本 contract 不把它解释为 positive-output KL。\n\n\n## 共同研究范围的约定\n\n接口I是一个程序性质的定义，不能作为所有算法已经满足的全局假设。条件统计根对任意满足I的共同有限族F证明蕴含式；具体Pi满足I及其完整成本须由SRC-Pi的正常独立来源义务支持，不能在证明SRC-Pi时先假定它。原第二阶段固定证明是可查来源，旧Fact编号不是新项目前驱。\n\n后继真实资源/可靠性命题可以在同一contract内建立独立义务，不必谎称它们是统计根的前提。数据观察及TV实验保持上述定义。每项具体实现须声明自己的内部代码、允许回读、输出格式、参数/字长、batch或streaming等执行方式；比较只在所声明的共同条件下成立。原Pi的finite-attention加pointwise batch hybrid、literal bit/ReLU模块的packed/scalar、sparse/dense选项分别核算，不将一项格式的便宜坐标拼入另一项。\n\n完整费用包括实际head和局部绑定、输入/query/端点取得、参数/零系数、物理字、复制/跨层保持/清除、mask/position、所有活动bank与metadata、online/offline工作和同时峰值。不能免费引入计数、normalizer、译码或生成器。新算术/扰动参数由各精确义务局部量化；改变共同数据律、可见信息或风险须建立新的明确数学范围。\n\n给定接口的条件定理、具体实现定理、训练可达性、必要资源及新颖性是不同主张。数学根只包含数学命题。行政完成程序不是数学前提；独立后续结论不改变已有定理的证明依赖。\n","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]},"statement":"# ANCHOR-PRECISION-RISK：固定锚定读出的精度—实际风险及一个粗精度失败配置\n\n这是020之后的独立nonroot科学义务。020 Fact8a4d1b9aef15dae8及其Evidence3ff58057b04b6befec3ddaa73e01d996e10fdb69caf7719520f48d5f4d315692保持原scope；本项不扩写其精确恢复参数域。021精确旧cap核查本轮收束，022保持OPEN/PARKED，不是本项前提。已恢复core及尚未解决的接线/alias/地址/微码/phase问题原样保留。不新做旧cap、compiler枚举或调度修复。\n\n来源设计资料 inputs/anchor-precision-risk-seed-20261029.md 和 anchor-precision-risk-precheck-20261029.md 当时尚未接纳，不能将来源材料标记当作独立科学证据。下述上界是标准有限误差与截断推论；新增可判别部分是指定粗配置在真实四头联合输出上的实际风险。整个合取经正常网关才可接纳，不拆常数节点，以首引理替代完整目标。\n\n## 1. 全域、量词与新程序\n\n所有整数K>=2、M>=1，N=M+2、n=q=N+1，字母表{0,...,K-1}。每次实验内theta固定为任意允许零边的齐次二阶表，mu为任意初始对律。只观察完整X_1^N，Y_i=(X_(i+1),X_(i+2))，departure为i=0,...,M-1，actual目标为theta_(Y_M)。风险始终为同轨迹E[TV]，TV=L1/2；sup可随公开参数选源。程序不读theta、mu、未来或辅助行栈。\n\n定义h0=max(4,ceil(log2 M)+1)，整数h>=h0，Q=2^h，b=ceil(log2(M+1))，ell=ceil(log2(N+K+2))，D_*=4M+1，p=4h+4ell+64，并独立选择整数g：\n\n    g_min=max(h,ceil(log2(8D_*))),\n    g_min<=g<=g_0=max(h,2b+12),\n    G=2^g, u=4g+4ell+64.                            (DOMAIN)\n\n需证明区间非空、g>=h>=b、u<=2p。所有整数配置有有限位长/移位构造。\n\nF_(K,M,h,g)保留020的同一六头共享因果batch hybrid前端、局部query、q外部/actual模式选择与half-up/clip decoder，仅重生成内部精度相关常数、有限求值和网格。两singleton复制头取得历史lag2/lag1及q已观察末对。q的token为零；f_t=1{t=q}；统计key为((1-f_t)lag2_t,(1-f_t)lag1_t)，value为(x_t,f_t)。四头(alpha,beta)∈{0,1}²的query为(alpha L2 A,beta L2 B)，A,B是该token合法局部query的one-hot。q选择最终query，过去位置不提前获得它。\n\nq的统计mask为{3,...,N,q}；其他行是{3,...,t}，空集self fallback。mask为有限bits。所有n位置完整执行、收费，每次只暴露q一个query输出。后端只访问四头返回、公开量及声明精确bits，不回读历史。\n\n精确冻结有限求值如下。R=2^u，先有理生成\n\n    V=2 sum_(j=0)^(u-1) 1/[3^(2j+1)(2j+1)],\n    L2=floor(R V)/R.\n\n对每个完整score s=S/R∈{0,L2,2L2}分别计算\n\n    T_0=R, T_j=floor(T_(j-1) S/(jR)), 1<=j<=8u,\n    W(S)=sum_(j=0)^(8u)T_j.\n\n保留full product和余数。对每个非空mask精确累加D_int=sum W、A_int=sum W v，返回网格分子floor(G A_int/D_int)。cached实现只缓存三个完整score的各自递推结果，不能把exp(L2)的舍入结果平方代替2L2求值。zero score的W=R准确。\n\n每个位置的四头label/anchor分子记Y_(ab),c、Z_(ab)。执行：\n\n    Z_safe=max(1,Z),\n    U_(ab),c=clip_[0,4M](floor((2Y_(ab),c+Z_safe)/(2Z_safe))),\n    C'_c=clip_[0,M](U_11,c-U_10,c-U_01,c+U_00,c),\n    B_c=C'_c+1, B_sum=sum_c B_c,\n    m_c=floor(Q B_c/B_sum) (c<K-1),\n    m_(K-1)=Q-sum_(c<K-1)m_c, F_c=m_c/Q.             (PROGRAM)\n\n不得改变舍入/clip顺序。非q的Z可能为0，sum C'可达KM，必须容纳；所有路径、query、两模式均合法，含M=1、无访问行、网格端点及源支持不相容历史。\n\n## 2. 全路径误差、统一actual上界和风险配置\n\n理想四头沿020的乘积展开定义D_ab=1+sum w_ab、S_ab,c=sum w_ab 1{x_t=c}，w_ab∈{1,2,4}。则S+1<=D<=D_*，C_c=S_11,c-S_10,c-S_01,c+S_00,c是真实完整triple count，J=sum C，p_c^+=(C_c+1)/(J+K)。需要为新g重述：有限log误差<2·2^-u，单weight误差<=100u2^-u，网格化前每坐标比值误差<=200u2^-u，网格化后HEAD误差<=2/G；score∈[0,2]。前一更强误差界亦用于第三节，不能只用独立的HEAD区间替代实际输出。\n\n待证在q，Z>=1，且\n\n    |Y/Z-S|<=4D_*²/G,\n    |C'_c-C_c|<=e, e=16D_*²/G+2,\n    TV(F_(h,g)(x;s),p_s^+(x))\n      <=min(1,K e/(J_s+K))+(K-1)/Q.                 (PATH)\n\n最后归一化必须以真实正向量C+1及其总和J+K证明；两次clip是向含真实值的区间投影，half-up每项另付1/2。非q概率合法性独立证明。\n\n令T=K^(5/2)/sqrt(M+1)，Psi(0)=0，Psi(x)=x(1+ln(1/x))于0<x<1，Psi(x)=1于x>=1。定义\n\n    R(K,M,h,g)=sup_(theta,mu) E TV(F_(h,g)(X;Y_M),theta_(Y_M)).\n\n使用016 Fact a53804d650803060的实际48T及TRUNC，证明\n\n    R(K,M,h,g)<=min(1,48T+(K-1)/Q+Psi(x)),\n    x=K^5[16D_*²/G+2]/(M+1)\n      <=256K^5 M/G+2K^5/(M+1).                      (RISK)\n\nTRUNC的实阈值取整、J=0、小M和零参数保持。对每个固定K，任何合法公开序列h_M,g_M，若G_M/M→∞，则R(K,M,h_M,g_M)→0。特别h=h0且G按M^(1+epsilon)向上取二次幂，固定0<epsilon<1，在充分大M进入DOMAIN，给M<<G<<M²的充分配置。此结论不声称必要性。\n\n给定0<tau<1，保留48T+(K-1)/Q+Psi(x)<=tau这个有限充分证书，并给出可检查的显式选择：\n\n    M+1 >= (144 K^(5/2)/tau)^2,\n    h=max(h0,ceil(log2(3(K-1)/tau))),\n    H=16K^5 D_*² / [(M+1)tau²/36-2K^5],\n    g=max(g_min,ceil(log2 H)).                      (TAU)\n\n需证明分母正、此g<=g_0、R<=tau；如上述表达式有真缺口须登记修复，不默许超出DOMAIN。此处使用Psi(x)<=2sqrt(x)只是显式充分配置的松弛。平方根界也足以推出G/M→∞时一致，不能说其一致性需要M²；只有要求保持M^-1/2实现误差阶时，它才给粗的M²充分尺度。TAU不声称最优精度或新的样本下界。\n\n## 3. 一个完全指定的coarse配置：真实联合四头的失败见证\n\n令K=2，对所有M取公开h_c(M)=h0(M)、g_c(M)=g_min(M,h0)。G_c=2^g_c满足G_c=Theta(M)。待证该特定配置不uniform actual一致，具体用以下同一个固定合法源，不引入任何新观察实验：\n\n    theta_00=delta_1, theta_01=delta_1,\n    theta_11=delta_0, theta_10=delta_0, mu=delta_00.\n\n真实pair路径是00→01→11→10→00的确定周期。沿公开子序列M_r=3·2^r，整数r>=2，真实末对Y_M=00，真实下一符号律delta_1；每个triple 001、011、110、100恰出现M_r/4次。待证实际有限程序给\n\n    lim_(r→∞) E TV(F_(2,M_r,h_c,g_c)(X;Y_M),theta_(Y_M))=1/12,\n    limsup_(M→∞) R(2,M,h_c(M),g_c(M))>=1/12.         (COARSE-FAIL)\n\n必须从同一路径产生全部四头。可核候选计算链为：在M_r上h_c=r+3，g_c=r+7，u=8r+100，G/M=128/3。按头顺序00、10、01、11，D/M趋于(1,3/2,3/2,9/4)，label0的S/M=(1/2,1/2,3/4,3/4)，label1的S/M=(1/2,1,3/4,3/2)。量化前误差乘G趋于0，理想G/D的极限(128/3,256/9,256/9,512/27)均非整数；应推出真实Z最终为(42,28,28,18)。须再逐项验证half-up、两次clip、add-one及ordered final floor，从而\n\n    (C'_0/M,C'_1/M)→(16/567,176/567),\n    F→(1/12,11/12).\n\n该计算链及有限诊断是待独立验证的证明候选，不是Fact。若失败，保持义务OPEN并登记精确失败点；不能以独立选择HEAD误差、理想实数输出或其他decoder替代。\n\n这是一个指定coarse配置、固定decoder的反例；不证明每个G=Theta(M)配置都失败，不证明G/M→∞对全配置必要，不推广为任意decoder、所有attention或一般Transformer资源下界。[Non-scientific operational metadata omitted.]\n\n## 4. 实际u的完整收费资源及范围\n\n从020已接纳构件核实新DOMAIN中的同一收费实现，精度字长为实际u，不自动以p或原p_a替换。要求沿其完整batch hybrid模型保持下列统一构造上界：L=O(Ku²)、per-token W=O(Ku)，6总heads/最多同层4、max QK=2K、统计value维K+1、score<=2；在线coefficient/arithmetic完整word<=128u；dense slots O(K³u⁴)、dense参数bits O(K³u⁵)、active gates/projections O(Ku²+K²)、holds O(K²u³)。\n\n主配置固定dense/uncached：全部n点运算/QKV O(nK³u⁶)，attention O(n²(K+u)u²)，mask/position O(n²+n log(n+1))，input/query/mode/endpoint/flag取得、转换、保存及residual/copy/hold/clear/decode全部收费。有限log work O(u³log²(u+1))、scratch O(u log(u+1))，code O(u⁴)。\n\n令P_u=K³u⁵+n²+nKu²+u⁴+u log(u+1)。复核program/参数/code、已存input、masks、QKV、rolling层、四头银行、controller/address、完整算术scratch和output逐phase共存求和，online/offline总peak O(P_u)。完整offline生成/整理及包括dense零项的真实格式写出work为O(K³u⁶+n²u²+u³log²(u+1))。这些是同源构件的解析上界核实，不要求旧十进制cap、literal ledger或compiler。须明说未运行这些测量。\n\n若讨论cached或sparse，独立列出其完整cache/selector/代码/格式费用，不与主配置混合。u<=2p仅给共同常数倍包络，不给原128p的逐数值word结论、020对Pi支配、最优work/width或资源必要性。COARSE-FAIL证明亦不扩展SRC的master故障接口。\n\n## 5. 依赖与执行门槛\n\n实际预期前驱为020 Fact8a4d1b9aef15dae8（固定前端/decoder及收费构件）、016 Facta53804d650803060（48T/TRUNC）、SRC Factfef8372728290b45（实际有限运算构件，若正文实质直接使用即登记）。若自足重述使某前驱不实际必需，提交时如实报告，不隐藏真正依赖。G/U已由016支持所需统计引理，不为此重审旧root。022及021均无数学前驱关系。\n\n完整 PATH/RISK/TAU/COARSE-FAIL/新参数资源合取需要独立审查；补充检查重点是四头联合可达性、Z 的 floor 稳定、两次 clip、最终归一化抵消和量词。[Private task allocation omitted from the public export.][Non-scientific operational metadata omitted.]新输入和上述具体数学见证是选择性接续的依据。旧接纳及依赖保持，不为新义务添加任何逆向前提。完成本合取仍不宣称v10母题解决。\n"}

Admitted prerequisite interfaces (use only within the recorded scopes):
[{"exact_statement":"# T2-ANCHORED-CAUSAL-DIRECT：有限锚点归一化的低维强 direct 因果 batch 候选\n\n019已正常接纳Fact5110203ec700e7e1 / Evidence41b852ff8a4fe4bf8aa948707c6bce8c1e7ca0a3ef48107c0ed2cdd5b401b12d，其完整streaming物理peak与017/018切口结论保持。本项不再把该顺序机展开成通用逐指令网络，而直接研究原SRC的共享逐token、因果batch hybrid执行模型中的强direct前端。旧B-C三元表及B-J联合特征已有来源，不将它们重包为新结果。本候选尚未证明，019不是本项数学前提，完成也不宣告同精确预算最优或v10完成。\n\n## 1. 原实验、全路径对象及有限配置\n\n全部整数K>=2、M>=1，N=M+2，n=N+1，q=N+1。每条实验内固定任意允许零边的齐次二阶theta及任意初始对律mu。观察完整X_1^N，Y_i=(X_(i+1),X_(i+2))，M次departure只计i=0,...,M-1。目标仍为同轨迹actual E TV(output,theta_(Y_M))，TV=L1/2，sup可逐K,M与算法选源。程序不读theta、mu、未来符号或辅助行栈。\n\n对每条历史及声明query s=(a,b)，C_s,c为完整原triple counts，J_s=sum_c C_s,c，p_s,c^+=(C_s,c+1)/(J_s+K)，T=K^(5/2)/sqrt(M+1)。精度为整数\n\n    h>=h0(M)=max(4,ceil(log2 M)+1), Q=2^h,\n    b=ceil(log2(M+1)), ell=ceil(log2(N+K+2)),\n    g=max(h,2b+12), G=2^g,\n    p=4h+4ell+64, p_a=4g+4ell+64.                 (CONFIG)\n\n待核h>=b、g<=2h+12及p_a<=2p。g是本新程序内部head精度，h仍是最终输出格式。公开整数由有限移位/位长/整数循环构造，不使用实数oracle。\n\n输入为同一one-hot历史和一个不含新观测的synthetic零token q。q的public flag可作锚点；不能另添来自源的样本。外部query和actual两种模式均可，实际末对来自已观察端点。每次运行只输出一个query；全query正确性不等于免费同时输出K²行。\n\n## 2. 具体共享因果前端及四个锚定heads\n\n沿SRC已付费的两个singleton copying heads，在历史key t>=3取得l2_t=e_(X_(t-2)), l1_t=e_(X_(t-1))；q取得e_(X_(N-1)),e_(X_N)。fallback、query/mode选择、端点保存及两头全batch执行收费。各token共享同一有限点运算；任何历史token不需提前知道末query。\n\n令f_t=1{t=q}为公开flag。历史key的标签value为x_t，q的x_q=0。所有统计key使用\n\n    k_t=((1-f_t)l2_t,(1-f_t)l1_t),\n    v_t=(x_t,f_t).\n\nkey和value在历史位置都不依赖最终query，q的key为零、value仅最后一个flag为1。位门控的构造、公开flag和位置均收费。q的四个统计heads由(alpha,beta)∈{0,1}²标记，其理想query/score为\n\n    Q_alpha,beta=((alpha ln2)A,(beta ln2)B),\n    score(q,t)=ln2[alpha 1{X_(t-2)=a}+beta 1{X_(t-1)=b}]\n\n对历史key t=3,...,N成立；anchor q的score=0。每head的value维数K+1，QK维数至多2K，四头共4K+4个返回坐标。q允许keys为{3,...,N,q}，包括因果self；其它行使用{3,...,t}的因果prefix，空集时self fallback。所有mask是明确有限bits，没有数值负无穷。不能省略非q行的求值费用。\n\n设i_t=1{X_(t-2)=a}, j_t=1{X_(t-1)=b}。理想权重\n\n    w_alpha,beta(t)=(1+i_t)^alpha (1+j_t)^beta ∈{1,2,4},\n    D_alpha,beta=1+sum_(t=3)^N w_alpha,beta(t),\n    S_alpha,beta,c=sum_(t=3)^N w_alpha,beta(t)1{X_t=c}.\n\n返回理想label坐标y_alpha,beta,c=S_alpha,beta,c/D_alpha,beta及anchor坐标z_alpha,beta=1/D_alpha,beta。待证全部历史/query下\n\n    1<=D_alpha,beta<=4M+1,\n    0<=S_alpha,beta,c<=4M,\n    C_s,c=S_11,c-S_10,c-S_01,c+S_00,c.            (IDEAL)\n\n这只是标准乘积展开/容斥与锚点去归一化，不能称新工具或首创。与旧B-J单个joint kernel的K²维表示不同，不能把旧单kernel秩下界误用于这个多头构造。\n\n## 3. 实际有限heads与精确整数恢复\n\n不能把exp(ln2)=2当实际实数运算。实际query系数采用SRC有限有理log生成得到的L2，保留完整p_a小数位、乘积/guard。使用同一声明的有限指数递推、正整数累加和返回G-grid的商余数。必须对这里的新key/value、self anchor及全部prefix/fallback重新核验适用性，给出足够自足的误差推导；SRC固定旧四头的结论不能未经解释直接覆盖新头。\n\n待证全部实际score在[0,2]内，每head、每返回坐标有\n\n    hat y=Y/G, hat z=Z/G, Y,Z∈{0,...,G},\n    |hat y-y|<=2/G, |hat z-z|<=2/G.              (HEAD)\n\n可重述SRC的有限log误差、8p_a项指数递推、单weight误差<=100p_a 2^(-p_a)，以每行至少一个正weight给归一化误差<=200p_a 2^(-p_a)，最后一次head floor另付1/G。锚点的有限score为0，weight确为该递推的单位weight。\n\n置D_*=4M+1。CONFIG须保证G>=64D_*²。对q处各头证明Z>=1且\n\n    |Y/Z-S_alpha,beta,c|<=4D_*²/G<=1/16.         (SNAP-MARGIN)\n\n用完整整数除法实现half-up\n\n    S_hat_alpha,beta,c=floor((2Y+Z)/(2Z)).\n\n因此q处S_hat精确等于整数S，并由IDEAL恢复完整C_s,c。必须保留M=1、无访问行、全零/确定路径、任意特定theta下零概率的历史、S=0与S=4M以及head网格端点。\n\n为了共享点运算在非q位置也全程合法，可统一将anchor numerator替换为Z_safe=max(1,Z)，将各half-up结果clip到[0,4M]，将容斥结果clip到[0,M]后再输出。q处这些guards不改变结果；其他行不声称恢复最终query计数，但每次division必须正分母、每个字宽合法，最终输出亦为概率向量。所有guards、比较、signed差、copy和holds收费。禁止免费广播最终query到过去或仅运行q的解码以省去全token费用。\n\n最终对恢复的C执行完整ordered add-one输出：前K-1坐标floor(Q(C_c+1)/(sum C+K))/Q，末坐标补残差。待证同一新程序F_anc在全历史/全query上\n\n    F_anc(x;s)=Gamma_Q(C_s),\n    TV(F_anc(x;s),p_s^+(x))<=(K-1)/Q.             (EXACT-READOUT)\n\n不声称F_anc逐位等于原Pi；Pi的master/V故障接口与36delta常数也不自动转移到新4K+4坐标银行。注意锚点概率约1/M，解码的精度放大已通过g实际付费，不把内部g与最终h混同。\n\n## 4. 同actual风险及完整共享batch资源候选\n\n仅引用016已接纳48T与Q>=2M的有限比较，证明\n\n    sup_(theta,mu) E TV(F_anc(X;Y_M),theta_(Y_M))\n      <=min(1,48T+(K-1)/Q)<=min(1,49T).          (RISK)\n\nM+1>=(64K^(5/2)/tau)²、h=h0、0<tau<1为充分配置。[Non-scientific operational metadata omitted.]\n\n模型严格沿SRC：共享逐token Boolean/ReLU点运算加收费有限因果attention的batch hybrid。固定参数/布局只依K,N,h，源无关。点运算在全部n位置执行并收费；head值的grid-to-bits、完整整数乘除/余数、归位、residual复制、所有live位逐层hold、输出decode均收费。不存在packed RAM的免费neural persistence或外加count table。历史输入及QKV是明确收费的attention输入，随后decoder只能访问四头返回、公开量及声明精确bits；它不再回读历史。它不满足017–019的最后两符号前不可回读cut限制，不将这些lower外推至该batch前端。\n\n待证一个具体有限电路实现具备下列保守上界，常数独立于K,M,h。p_a为本实现真实字长参数：\n\n|项目|候选完整上界|\n|---|---|\n|neural depth / per-token width|O(K p_a²) / O(K p_a)|\n|总heads / 同层最多heads；max QK dimension；score cap|6 / 4；2K；2|\n|online coefficient/arithmetic word，含完整乘积/余数/guards|<=128 p_a bits|\n|dense coefficient slots / parameter bits|O(K³p_a⁴) / O(K³p_a⁵)，包括零项/bias|\n|active gates/projections；identity holds|O(Kp_a²+K²)；O(K²p_a³)|\n|sparse program/coefficient/address/hold格式|共O(K²p_a⁴) bits|\n|完整masks/positions|O(n²+n log(n+1)) bits|\n|observed input、query/endpoint、public flags|NK及其完整取得/转换/保存另列|\n|rolling工作数组|O(nKp_a²) bits，仅作为总peak的分项|\n|uncached有限attention online bitwork|O(n²(K+p_a)p_a²)|\n|同样允许full-score cache的attention online bitwork|O(n²Kp_a²)，cache生成/存储/selector另付|\n|dense pointwise/QKV全n位置online bitwork|O(nK³p_a⁶)|\n|有限有理log生成work / scratch|O(p_a³ log²(p_a+1)) / O(p_a log(p_a+1))|\n|compact有限attention/arithmetic evaluator code|O(p_a⁴) bits|\n\n前两复制头、四统计头的所有有效边均按选定方案计费。缓存只允许固定完整score菜单0,L2,2L2，2L2须由有限指数递推单独生成，不能用舍入后的exp(L2)平方替代；cache生成O(p_a³)与log生成另列。比较原Pi时同样允许其已声明五项菜单，不通过仅给一方缓存制造差距。dense/sparse是独立格式，不能混取优势。\n\n给出完整phase同时活跃项求和。dense格式下令\n\n    P_dense=K³p_a⁵+n²+nKp_a²+p_a⁴+p_a log(p_a+1).\n\n待证含program/参数、input、masks/positions、QKV、residual、四银行、controller、完整算术scratch及输出的phase-total物理peak为O(P_dense)。如用sparse格式，单独以K²p_a⁴替换dense参数项并仍完整列账；不自动导出sparse在线加速。不得只报rolling数组或query-token容量。\n\n完整offline还包括布局、mask/位置、微码、每个gate/term/hold记录及真实全格式写出。以实际记录数G_rec,T_rec,I_hold列出生成O((G_rec+T_rec+I_hold)p_a²)和相应O((G_rec+T_rec+I_hold)p_a) scratch，加log/cache与所有dense零项写出；须证明保守总offline work\n\n    O(K³p_a⁶+n²p_a²+p_a³ log²(p_a+1)),\n\n及phase-total offline peak O(P_dense)。公开循环/索引和格式地址位长均核入p_a的常数倍；若任何费用承诺不成立，登记准确缺口，保持OPEN，不静默改成更弱界。\n\n这是实际batch hybrid构造和解析费用；generic逐指令PURE展开不是以上较小L/W的证明。无需新增compiler、大规模枚举或literal ledger，未执行则明确说明。若讨论PURE，另写其完整膨胀账，不并入本候选比较。\n\n## 5. 比较的准确结论与未决量\n\n只有完整IDEAL/HEAD/SNAP/EXACT-READOUT/RISK及上表全部成本经正常独立网关后，方可声称：一般K也有一个强direct，在6heads、4同层heads、2K QK维、score cap2的共同因果batch模型中，恢复完整query counts，且与原Pi具有同阶的上述完整资源上界。由p_a<=2p可把这些上界用原p表示，代价为独立于参数的常数倍；最小上述充分M、h0下p_a=O(1+logK+log(1/tau))。\n\n“共同常数倍上界包络”不是“逐坐标装入原Pi的同一个数值cap”。若双方只有upper，不推导实际费用优势、支配或一般算法lower。特别不凭p_a<=2p把新128p_a word说成原128p；不把旧K=2 allocation外推一般K，不把多头与单joint-kernel的表示区别说成神经最优。数值cap、完整资源tradeoff/优势、最优work/width、一般K故障预算与物理纠错仍需独立后续。\n\n乘积展开、容斥、已知锚点去归一化、整数rounding以及Boolean/ReLU运算均按标准方法分类。旧来源已列出的lag-matching、subset-count inversion与count recovery文献必须保留，有限本地检索无命中不等于新颖性证明。若完整前端已被既有来源覆盖，说明准确重合与必要实现增量，不为纯重述另立首创结论。\n\n## 6. 依赖、预检和提交边界\n\n预期实际Fact前驱只有SRC fef8372728290b45（真实有限求值、复制/运算构件与比较费用）和016 a53804d650803060（原actual48T）。新四头、anchor/self-mask、全路径精确恢复、guard与生命周期/成本需自足；实质另用Fact则如实登记。019只说明研究进度，不是前驱；不得让020成为任何旧结果的逆向前提。\n\n[Private administrative workflow omitted from the public export.]若有真实缺口登记准确障碍/修复方向，保持原目标OPEN；团队讨论不是Fact。\n\n[Non-scientific operational metadata omitted.][Non-scientific operational metadata omitted.]\n","fact_id":"8a4d1b9aef15dae8","scope_bindings":[{"evidence_id":"3ff58057b04b6befec3ddaa73e01d996e10fdb69caf7719520f48d5f4d315692","obligation_id":"69f5064f1811226c999d4c360b455fd23b8ba59fedf8e5c638f2a307e716854e","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]}}],"source_hash":"7b646cf36163843cd4f1608313429226f55283c57dd5b23770a7d6ad3083e2da"},{"exact_statement":"# RATE-L1-MAX：去除剩余 sqrt(log K) 的共同 actual TV 率候选及同风险配置\n\n本项是015完整接收后的独立科学后继。014、015及旧root的准确声明、接纳和依赖保持；本候选不是由它们的接纳自动得到，也不是任何旧结果的逆向前提。直接对前缀L1范数作有界差分是本次待核查的改动，不以相邻高矩参数优化替代。完成本项亦不宣告v10的资源与机制母题完成。\n\n## 1. 原完整实验与准确目标\n\n全部整数K>=2、M>=1，N=M+2，字母表{0,...,K-1}。theta为任意允许零边的齐次二阶转移表，mu为任意初始对律。每次实验内theta固定；sup可随K,M选源。观察完整X_1^(M+2)，Y_i=(X_(i+1),X_(i+2))，0<=i<=M。\n\n    C_s,a=sum_(i=0)^(M-1)1{Y_i=s,X_(i+3)=a},\n    n_s=sum_a C_s,a, J=n_(Y_M), p_s,a^+=(C_s,a+1)/(n_s+K),\n    T(K,M)=K^(5/2)/sqrt(M+1),\n    R_K^+(M)=sup_(theta,mu) E TV(p^+_(Y_M),theta_(Y_M)).\n\n待证结论：\n\n    R_K^+(M)<=min{1,48 T(K,M)}.                       (L1+)\n\n仍为同完整轨迹actual E[TV]，不是TV平方、fixed/all/conditional、独立测试查询或删尾平均。算法只获历史及公开参数，不获辅助行栈、隐藏theta/mu、访问参数或未来符号。所有退化行、周期/可约/暂态、J=0、小M及任意初始化均需覆盖。\n\n## 2. 直接L1最大集中的具体候选（全部需证明）\n\n有限辅助耦合为每个K²行提供2M个独立theta_s符号并顺序复现原M次departure。令S_s,j=sum_(l<=j)(e_(xi_s,l)-theta_s)。对确定整数1<=v<=M定义\n\n    F_s,v=max_(0<=j<=2v)||S_s,j||_1,\n    Z_v=max_s F_s,v.\n\n只对确定行/确定前缀使用iid。目标链：\n\n    E F_s,v <= sqrt(8Kv),\n    改变一个栈符号使F_s,v至多改变2,\n    P(F_s,v-E F_s,v>t)<=exp(-t²/(4v)), t>=0,\n    ||Z_v||_4 <= sqrt(8Kv)+sqrt(8v ln K)+32^(1/4)sqrt(v)\n              <= (25/4)sqrt(Kv).                    (L1MAX)\n\n均值可用L1/L2比较及有限Doob L2；集中直接作用于整个L1前缀最大值，其坐标敏感度2与K无关。请给有界差分的条件区间推导及尾积分。K²行union后以a=sqrt(8v lnK)平移，剩余正部四次矩应<=32v²；行最大值之间不要求独立。不得将sqrt(K)再次乘在全部集中误差上。\n\n最后常数可用lnK/K<=1/e<3/8、K>=2，从而系数至多sqrt(8)+sqrt(3)+2^(3/4)<25/4；所有常数比较须明确可审。该吸收利用的是sqrt(K)均值和sqrt(logK)偏差的相加，不声称偏差本身没有logK。\n\n在E_v={v<=J<2v}上逐路径TV(phat_(Y_M),theta_(Y_M))<=Z_v/(2v)。然后仅用无条件Holder及G/U整数UC：\n\n    c=K^4/(M+1), P(J<w)<=min(1,cw), 整数w>=1,\n    E[TV(phat,theta)1_Ev]\n       <=(25/8)sqrt(K) v^(-1/2) min(1,2cv)^(3/4).\n\n重述有限分层和数值几何和\n\n    sum_(l>=0)2^(-l/2)min(1,a 2^l)^(3/4)<=10sqrt(a), a>0.\n\n于是经验项候选<= (125sqrt(2)/4)T；零计数项<=T、平滑项<=2T，总系数<48。无限延拓只用于数值和，不为随机栈增加免费信息。phat不在J=0定义。\n\n平滑及下述实现误差保持截断：对每个实数A>=0，\n\n    E min{1,A/(J+K)}<=Psi(cA)<=2sqrt(cA),             (TRUNC)\n    Psi(0)=0; Psi(x)=x(1+ln(1/x)) (0<x<1); Psi(x)=1 (x>=1).\n\n需保留A=0及实阈值x=A/t-K，x>0时{J<x}={J<ceil(x)}且ceil(x)<=A/t，x<=0为空事件，不直接向非整数阈值套整数UC。A=K用于平滑。\n\n## 3. 全合法精度与原Pi\n\n对输出为概率向量且全路径全query满足原接口I的共同有限F：\n\n    h>=h0(M)=max(4,ceil(log2M)+1), Q=2^h,\n    TV(F_h(x;s),p_s^+(x))<=78KM/[Q(n_s(x)+K)]+(K-1)/Q,\n    A_h=78KM/Q, g_h=(K-1)/Q,\n\n证明\n\n    sup E TV(F_h(Y_M),p^+_(Y_M))<=min(1,g_h+Psi(cA_h)),\n    sup E TV(F_h(Y_M),theta_(Y_M))\n      <=min(1,48T+g_h+Psi(cA_h))<=min(1,64T).        (L1-I)\n\n由SRC Fact fef8372728290b45，这适用于同一个实际Pi，直接包括最低合法h0。不得由高精度结果自动推到h0，也不声称各h输出或真实风险相同。以原h_N=ceil(log2(128(K+1)(M+3)^3))、e_N=(M+3)^(-2)，另有原Pi风险<=min(1,48T+e_N)。全部须给有限参数推导。\n\n## 4. 已接纳MM5的同目标比较\n\n令R_min(K,M)=inf_A sup_(theta,mu)E TV(A(X_1^(M+2)),theta_(Y_M))，A为所有共同随机全历史概率预测器，种子与源独立，不读隐藏参数或未来。仅使用MM5 Fact946d42d5bf502eb4已接纳范围得到下界，并结合本项新上界，目标合取为\n\n    2^-16 min(1,T)<=R_min(K,M)<=R_K^+(M)<=min(1,48T). (MATCH)\n\n只有本项正常接纳后才能称K,M联合统计率在绝对常数因子内匹配，或原add-one达到该minimax阶。不能称数值常数最优、存在同一源对所有算法/所有horizon同时困难、内部资源下界或所有Transformer资源最优。旧MM5构造不重证，保留其唯一原前驱a125供小K。\n\n0<tau<2^-16时任何共同全历史算法的统一风险<=tau，必要样本为M+1>=2^-32 K^5/tau²。原Pi无故障取M+1>=(64K^(5/2)/tau)²、h=h0即为充分配置。必要与充分为不同量词方向，不能相加或当作同一见证。\n\n## 5. 联合故障与完整费用的标准后续推论\n\n在SRC原master/V切口，使用015相同的准确故障实验：master为9K+1个canonical G_h字，最终银行W在{1,...,2Q}^K；D为相对当前post-master银行V^delta的总绝对整数编辑预算。核只读已观察历史/当前银行/公开量和独立种子，不读隐藏源或未来。好事件G可与历史/J及编辑相关，P(G^c)<=gamma；G上master逐坐标误差<=delta、||W-V^delta||_1<=D；G外仍合法canonical/正银行。令\n\n    A=M[K(78/Q+36delta)+D/Q].\n\n重述短的正向量归一化与无条件截断推导，证明原Pi\n\n    R_fault<=min(1,48T+g_h+Psi(cA)+gamma)\n           <=min(1,62T+12K^(5/2)sqrt(delta)+2K²sqrt(D/Q)+gamma).\n\n因此对0<tau<1，M+1>=(248K^(5/2)/tau)²、h=h0、delta<=tau²/(2304K^5)、整数D<=floor(Q tau²/(64K^4))、gamma<=tau/4为充分配置。J0、M1、零预算和只能零编辑的网格均保留。这是新统计率代入既有接口的标准综合，不另造常数节点，不扩展015二元切口下界。\n\n取M_tau=max(1,ceil((aK^(5/2)/tau)²)-1)，a=64或248，N=M_tau+2、n=N+1、ell=ceil(log2(N+K+2))、p=4h0+4ell+64。明确S_tau=K^5/tau²、Lambda_tau=1+lnK+ln(1/tau)，n=O(S_tau)、p=O(Lambda_tau)。同一个uncached/dense SRC配置保留depth O(Kp²)、width O(Kp)、word<=128p、dense参数bits O(K³p^5)、全部n个token点运算/QKV O(nK³p^6)、attention O(n²(K+p)p²)，以及完整input/query/endpoint、metadata/masks、holds/copy/clear、输出、offline generation/全格式写出和逐phase总peak。rolling内存不替代总peak；缓存、sparse、PURE须另用完整收费配置。物理注入器、历史重读或新纠错桥不免费。\n\n该标准成本代入只消去充分样本证书中的logK，不改变Pi程序或宣称同精确预算优势。strong direct及真正同神经预算比较仍需独立科学工作。\n\n## 6. 实际依赖与正常证据门槛\n\n上界预计只必需G/U a12539a93d9f1ee3的UC与SRC fef8372728290b45的实际接口/费用；MATCH实际使用MM5 946d42d5bf502eb4。有限耦合、Doob、区间矩母函数、有界差分、Holder、dyadic及截断推导均重述自足时，不新增014/015/RATE/K3前驱。它们可作写作来源；若实质依赖其引理则如实加入前驱，禁止隐藏依赖。所有旧Fact保持原scope。\n\n先做有界逆向核查，尤其L1最大函数的单符号振幅、均值与偏差相加、25/4常数和随机末行相关性。若失败则登记精确障碍，保持OPEN，不将辅助估计失败宣称为目标反例。完整证明需要独立审查；补充检查不替代接纳。所有标准方法不作新工具或首创主张。[Non-scientific operational metadata omitted.]\n","fact_id":"a53804d650803060","scope_bindings":[{"evidence_id":"fef1785395851e47b5ca0b719640449061718f4c670bfcd74c24cf0aec696c88","obligation_id":"e5eac888f467f9e19522d9755a04c518aea63e80192c0532f59b4d9dfecbde33","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]}}],"source_hash":"bc24d183f5299df636e67f0b439aadbcd4d79671b69c327ed7083ddfab857c6f"},{"exact_statement":"# SRC-Pi：原有限因果程序的全路径实现、银行接口与完整费用\n\n对每个整数 K>=2、N>=3，令 M=N-2、n=N+1。对每个整数 h>=max(4,ceil(log2 M)+1)，令 Q=2^h、ell=ceil(log2(N+K+2))、p=4h+4ell+64。字母表 A={0,...,K-1}。对任意完整已观察历史 x_1^N 和 query s=(a,b)，定义\n\n    C_s,c=sum_(t=3)^N 1{(x_(t-2),x_(t-1),x_t)=(a,b,c)},\n    n_s=sum_c C_s,c, p_s,c^+=(C_s,c+1)/(n_s+K).\n\n存在下述同一个共同确定有限程序族 Pi_(K,N,h)，参数、固定循环、布局、掩码和常数仅依赖公开 K,N,h；其固定构造由本项目 inputs/source-v10/inputs/general-assumptions-20261027/stage2/ 下 C1-proof-v1.md §§1–7、finiteN-reliability-proof-v1.md §§4–6 和 root-proof-v1.md §5 指定。以下断言需由确定性构造证明支持，I 是待证结论。旧来源的正性、平稳初始化和旧 Fact 身份均不作前提。\n\n## S1. 实际因果前端与有限求值\n\n主实现为有限整数求值的因果 attention 加逐 token Boolean/ReLU 点运算的 batch hybrid。输入仅为已观察历史、声明 query/mode 和公开 metadata；合成位置 q=N+1 的 token 为零，不含未来符号。两个已付费 singleton copying heads 产生前两步符号，并在 q 保留实际端点 (x_(N-1),x_N)，供外部 query 与 actual query 两种模式使用。外部 s 不替换实际端点修正。\n\n另有四个统计 heads P1、P2、T、0。理想比较对象的 Q/K/V 为：P1 的 Q=((ln2)A,(ln2)B)、K=(lag2,lag1)、V=(token,lag2)；P2 将第二段 ln2 换为 ln3；T 的 Q=(ln2)B、K=lag2、V=(lag1,F)；0 的 Q=K=0、V=(lag2,lag1,F,z)。A,B 为 query one-hot，z_t=1{t=3}，F_t=z_t lag1_t；q 的有效 keys 为 3,...,N，其余行使用声明的因果 prefix/fallback。理想输出依次为 (q1,v1)、(q2,v2)、(hvec,h0)、(alpha,nu,f,rho)，共 9K+1 标量。值为 query 无关的局部 bits。\n\n实际程序以有限有理 log 生成、定长整数指数求值、精确累加和正整数除法产生闭 h-grid G_h={j/Q:0<=j<=Q} 上的标量；不调用实数 log/exp/floor oracle。每一返回 head 标量与其上述理想值相差至多 2/Q。包含 1 的 G_h 用 h+1 位无符号分子。连续 ReLU 不被声称在实区间上实现 floor；其 bit extraction 只作用于声明有限网格。\n\n四个统计 head 后不再有读取原始历史的 decoder 端口或免费 count table；计数 C 仅为数学比较对象。源参数 theta、mu、支持、平稳律和访问控制参数均不进入程序。\n\n## S2. 正确逐路径读出、guards 与接口 I\n\n记 c_s,c=C_s,c/M、rho=1/M、u_ij=n_ij/M，alpha_i=sum_j u_ij、nu_j=sum_i u_ij，J_c=1{实际端点=(b,c)}。理想读出为\n\n    dT=1+alpha_b,\n    initial_bc=dT h0_c-f_c,\n    g_bc=dT hvec_c-nu_c+rho J_c-initial_bc,\n    U_k=v_k,a, lambda_1=1,lambda_2=2,\n    d_k=(1+lambda_k nu_b)/(1-U_k/2),\n    c_s,c=d2 q2_c-d1 q1_c-g_bc.\n\n这些恒等式对每条有限路径成立，包含 M=1、n_s=0，以及任何特定源下零概率的历史。实际点运算保留完整整数乘积、除法余数和 guard fractional bit；加减和声明的除二精确，所需乘除截断绝对误差至多 1/Q。head clipping 后 1-U_k/2∈[1/2,1]，d1∈[1,4]、d2∈[1,6]、dT∈[1,2]，有符号中间量容纳于来源指定的 [-16,16] 安全盒。\n\n令 a_c 为恢复 c_s,c 后截入 [0,1] 的 h-grid 值，令\n\n    r0=2^(-ceil(log2 M)-1), r=max(hat rho,r0),\n    x_c=a_c+r, V_c=Q x_c, T=sum_c V_c.\n\n则 x_c∈(0,2]，V_c∈{1,...,2Q}，T>0，并且\n\n    |a_c-C_s,c/M|<=76/Q,\n    |x_c-(C_s,c+1)/M|<=78/Q.\n\n最终输出按原有序 simplex 格式：c=0,...,K-2 的分子 m_c=floor(Q V_c/T)，m_(K-1)=Q-sum_(c<K-1)m_c，随后已付费 dyadic decode。其坐标非负且和为一，允许非末坐标为零，且所有路径、所有 query 同时满足\n\n    TV(Pi_(K,N,h)(x_1^N;s),p_s^+(x_1^N))\n      <=78KM/[Q(n_s+K)]+(K-1)/Q.                 (I)\n\n程序在上述全域合法；不同源规律只改变路径概率，不改变给定输入的程序及其费用。\n\n## S3. 后继确实使用的 master 与正权重银行接口\n\n9K+1 个 head 坐标各有一个 post-quantization master word，在任何 readout fanout/residual 复制之前定位切口。所有后继副本都来自该 master；query、端点及 flag BITs 在此实验中精确，统计标量 h0、f、rho 包含在可替换银行内。有限 evaluator 的干净 numerator、denominator、指数、余数及不用的历史投影在切口开放前按声明生命周期擦除或释放；历史存储及其处理仍收费。这里声明的是指定访问规则下的实际程序接口，不是对任意能重读历史算法的信息论限制。\n\n若每个 master 被任意相关的 G_h 标量替换，坐标偏差至多 delta>=0，原 downstream 运算仍合法，并有\n\n    |a_c-C_s,c/M|<=76/Q+35delta,\n    |x_c-(C_s,c+1)/M|<=78/Q+36delta,\n    TV(Pi^delta_s,p_s^+)<=KM(78/Q+36delta)/(n_s+K)+(K-1)/Q.\n\n这些是有限路径上的确定性接口，不要求误差独立，不涵盖改变 query/endpoint bits 或额外算术故障。\n\n最后正整数 V 银行的切口在全部 V_c 生成后、任何最终求和与 quotient 前。可将 V 替换为 W∈{1,...,2Q}^K；原 decoder 只从替换后的 W 重算 U=sum W 和上述 ordered floor/residual 输出，不保留干净 T 或 quotient。比较向量 V*_c=Q(C_s,c+1)/M 不是程序输入，且无需为整数；上述坐标界等价于 |V_c-V*_c|<=78+36Q delta。该定位与生命周期可在原声明成本上界内实现；若另外实现物理注入器、快照设备或新 normalizer 的 bridge，其硬件和程序费用单列，不在 nominal Pi 的免费能力中。\n\n## S4. 完整构造费用及表示约定\n\n以下是固定构造的统一上界，常数与 K,N,h 无关；采用来源最终修正后的 batch hybrid 计费。全部 n 个 token 的点运算计费，数学上所有 query 的正确性不意味着一次运行免费输出全部 K² 行。\n\n| 坐标 | 上界或精确结构 |\n|---|---|\n| neural depth / width | O(Kp²) / O(Kp) |\n| total heads / max layer heads；max QK dimension；score cap | 6 / 4；2K；2 |\n| 单 coefficient 与 arithmetic word | 至多 128p bits，含完整乘积、余数与 guards |\n| dense coefficient slots / parameter bits | O(K³p⁴) / O(K³p⁵)，零项和 bias 收费 |\n| active gates/projections；identity holds | O(Kp²+K²)；O(K²p³) |\n| sparse program / coefficients / addresses / holds | 共 O(K²p⁴) bits |\n| masks / positions | O(n²+n log(n+1)) bits |\n| observed input | O(NK) one-hot bits，或另付 binary acquisition/转换 |\n| rolling working arrays | O(nKp²) bits，不含已存参数、input、masks |\n| uncached finite attention bitwork | O(n²(K+p)p²) |\n| equally cached attention bitwork | O(n²Kp²)，cache 生成、存储、selector 另付 |\n| dense pointwise / QKV bitwork | O(nK³p⁶) |\n| finite rational log generation / scratch | O(p³ log²(p+1)) / O(p log(p+1)) |\n| finite arithmetic evaluator code | 保守 O(p⁴) bits |\n\n五个 full-score caches 对应 0,L2,2L2,L3,L2+L3，分别有限求值；最后一项不是两个已舍入 exp 的乘积。使用 cache 时其非零生成需 O(p³) bitwork，另加 log 生成；与比较器一致付费。dense 与 sparse 为不同表示选择，不混合其优势；packed registers 与 scalar neural bit-channel 存储分别说明。\n\n完整 offline 包括 K,N,h layout、masks/positions、微码、cache/selector、全部 gate/term/hold 生成整理与实际格式输出。令 G,T_rec,I_hold 为实际生成的 gate、term、hold 记录数，其整理生成费用为 O((G+T_rec+I_hold)p²) bitwork 和 O((G+T_rec+I_hold)p) 工作 bits；dense 文件还支付真实 coefficient bits 的写出，包括零项。input/query/endpoint acquisition、residual copy、保持、擦除和最终 decode 均计费。\n\n总峰值按同一 phase 同时存活的程序/参数、input、mask/metadata、QKV、residual、银行、controller/address、临时工作区及输出求和，再取各 phase 最大值。上表 rolling working bits 不能冒充总峰值。这里不声称已在本 workspace 运行未提供的旧 emitter，也不以其他程序的精确 ledger 冒充 Pi 的实测 profile。\n\n另有保守 PURE neural 展开实现：令 T_bit 为上述固定循环的全部 online bitops（含 copy/clear），S_bit 为相应 live work、input/mask/public data；若用 interpreter，存储程序位作为常数 rails 加入。逐指令展开并保持其余 live bits，得到 depth O(T_bit+p)、width O(S_bit+p)、sparse gates/holds O((T_bit+p)(S_bit+p))、dense coefficient bits O(p(T_bit+p)(S_bit+p)²)、generic dense bitwork O(p²(T_bit+p)(S_bit+p)²)。该展开的完整成本单列，不能报告成较小的 hybrid L,W。\n\n## S5. 准确结论边界\n\nS1–S4 是本独立来源义务的合取，只针对上述固定 Pi 构造及定位接口。不从抽象 I 推导实现或费用，不泛化到所有训练 Transformer；不包含强 direct 基线上的逐坐标资源优势、整网主导成本下降或资源最优性。资源 NORM 模块与 weighted-direct 的新前端/bridge 若被使用，须有其自身明确实现和费用来源。\n\n证明可复用来源的固定确定性推导，但需在本项目正常提交为可独立检查的完整正文。G/U 统计根不作此纯确定性义务的必要前提；其独立完成不倒置为已完成统计根的前提。上述 statement 未把任何旧 discussion PASS 或旧 Fact 编号当作本项目 admission。\n","fact_id":"fef8372728290b45","scope_bindings":[{"evidence_id":"e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505","obligation_id":"6010cac30ffe4aea77e6d7a9e4e3f5686e4f44b2bf31c1674d33dfdf7dc46f84","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]}}],"source_hash":"33ea4cbe839a4ad72453cb20f8f74263a1d330e766027f7e65638c494da4c025"}]

Proof:
# ANCHOR-PRECISION-RISK: complete finite-program, risk and cost proof

Obligation: 8b01f4916991a27070c6a469b8efe13a421c0ffc8d68065bd6b643838dce114c.
Author: native Prover. This proves the complete 023 conjunction, subject to the independent gateway; it is not an admitted Fact before that gateway accepts it.

## 1. Scope, sources, and the disclosed finite-prefix correction

The direct Fact predecessors used here are:

* 020, Fact 8a4d1b9aef15dae8, Evidence 3ff58057b04b6befec3ddaa73e01d996e10fdb69caf7719520f48d5f4d315692: the six-head anchored causal batch front end, guarded decoder architecture and its charged Boolean/ReLU/arithmetic construction.
* 016, Fact a53804d650803060, Evidence fef1785395851e47b5ca0b719640449061718f4c670bfcd74c24cf0aec696c88: the original same-trajectory actual add-one risk at most min(1,48T), and TRUNC for that trajectory's actual visit count J.
* SRC, Fact fef8372728290b45, Evidence e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505: the paid finite copying/arithmetic and batch-hybrid execution model, including full products and offline rational generation.

Their native evidence is PASS/VALID; their Fact-file hashes equal the native evidence content hashes, as recorded in source-check-v1.json. No 021/022 statement, old campaign Fact, source diagnostic, stationary/mixing theorem, or discussion is a mathematical predecessor. In particular, we do not apply 020's exact snap theorem below its admitted precision.

The frozen 023 statement has SHA256
372829802f4c71386c6e7ffca964ef012ad6c673d03024276b29afe1c661c0e2.
Its PROGRAM/DOMAIN are used without changing any rounding or clip. Its Section 3 candidate calculation chain contains a finite-prefix slip, already disclosed by the Lead's scope note and native event
8c560af8abb32c565a39acbd1a34f0ced44126bfc98ffb8917552a3c8b573daa.
For K=2,M=3*2^r, the shortcut u=8r+100 holds for r>=3, not r=2. At r=2 the actual values are (M,h,g,ell,u)=(12,5,9,5,120). We explicitly prove and use the correct values in Section 7. This corrects an auxiliary candidate identity; it does not redefine the program or weaken its asserted asymptotic COARSE-FAIL conclusion.

Fix integers K>=2,M>=1, N=M+2, n=q=N+1. A history x_1^N is arbitrary, including any path of probability zero under a particular source. One run exposes one declared query s=(a,beta_symbol), or the actual query (x_(N-1),x_N). The source theta and initial pair law mu never enter the program. In the statistical statements they range over all homogeneous second-order tables, including zeros, and all initial pair laws, with a single fixed source within each experiment. The actual row is Y_M in the original trajectory Y_i=(X_(i+1),X_(i+2)), with exactly M departures i=0,...,M-1. TV is half the L1 norm.

The input seed and precheck, and the Lead's four finite diagnostic instances, are design/checking sources only. The proof below does not infer an infinite-parameter assertion from their diagnostic output.

## 2. DOMAIN, exact dataflow and program legality

Set
h0=max(4,ceil(log2 M)+1), h>=h0, Q=2^h,
b=ceil(log2(M+1)), ell=ceil(log2(N+K+2)), D_*=4M+1,
p=4h+4ell+64,
g_min=max(h,ceil(log2(8D_*))),
g0=max(h,2b+12), g_min<=g<=g0,
G=2^g, u=4g+4ell+64.

First Q>=2M>=M+1, so h>=b. Since
8D_*=32M+8<=32(M+1)<=2^(b+5)<=2^(2b+12),
g_min<=g0 and the interval contains an integer. Also g>=h, g<=2h+12, and

    u<=8h+4ell+112<=8h+8ell+128=2p.                (2.1)

We shall use G>=8D_* and u>=4g+64. Integer ceil-log2(v) is computed by the bit length of v-1, with the v=1 case zero; powers of two are shifts. All public layout integers and loop bounds have finite representations. Mathematical real logarithms used for bounds are not program oracles.

For completeness, the shared dataflow is the following concrete 020 front end, regenerated at the actual u,g. Two singleton heads with zero scores and values x_t copy positions t-2 and t-1 when present. At t=1 both missing lags use self; at t=2 the missing lag2 uses self. At q they copy the observed last two symbols. Thus all lag vectors are one-hot. Retain x_t and the public bit f_t=1{t=q} by charged residual copies. The synthetic token x_q is the zero vector, with no new observation.

External A_ext,B_ext fields are supplied only at q, with zero placeholders in the past. A mode bit and f_t implement a shared bit-mux: at q use the external pair or the copied actual endpoints; at history t use A_t=lag2_t and B_t=lag1_t. Every chosen A_t,B_t is one-hot. No earlier token receives the final query.

For each statistical key use
k_t=((1-f_t)lag2_t,(1-f_t)lag1_t), v_t=(x_t,f_t).
At q the key is zero and value is a unit anchor in the final coordinate. At history keys neither depends on the eventual query. The head queries for (alpha,beta) in {0,1}² are ((alpha L2)A_t,(beta L2)B_t). The masks at q are {3,...,N,q}; at history t>=3 they are {3,...,t}, and t=1,2 use self fallback. Masks are explicit finite bits. There are two copying heads in one stage and four statistical heads in the next, at most four simultaneously, maximum QK dimension 2K, and K+1 value coordinates for every statistical head.

Use exactly the rational log and integer exponential rules of the frozen statement, as detailed and bounded in Section 3. Each nonempty mask has positive integer denominator. Return every label and anchor coordinate by floor(G A_int/D_int). Hence Y,Z are integers in [0,G], including the endpoint G.

At every token, in this order, compute

    Z_safe=max(1,Z),
    U_(alpha,beta),c=
      clip_[0,4M]( floor((2Y_(alpha,beta),c+Z_safe)/(2Z_safe)) ),
    C'_c=clip_[0,M](U_11,c-U_10,c-U_01,c+U_00,c),
    B_c=C'_c+1, B_sum=sum_c B_c,
    m_c=floor(Q B_c/B_sum), c=0,...,K-2,
    m_(K-1)=Q-sum_(c<K-1)m_c, F_c=m_c/Q.             (2.2)

All divisions use full integer numerator, quotient and remainder. Intermediate differences are signed. At non-q positions Z is in fact zero because no anchor key is visible; the guard still makes 2Z_safe positive. U is in [0,4M], C' in [0,M], and

    K<=B_sum<=K(M+1).                                (2.3)

In particular we never bound the non-q sum C' by M. All B_c are positive. The first K-1 nonnegative quotients sum to less than Q: their real-valued sum before flooring is Q(1-B_(K-1)/B_sum)<Q. The residual is therefore an integer in [1,Q], and all n outputs are probability vectors. This proves legality independently of count recovery, including M=1, no visits, deterministic/all-zero histories, both modes, and grid endpoints.

The decoder only has the four returned banks, public quantities and the declared exact bits. Attention weight, numerator, denominator and remainder scratch, and unused historical projections are cleared/released at a charged cost before decoding; no historical readout port or count table is supplied. All n token computations occur even though only q's answer is exposed. This is the causal batch hybrid, not a late-query streaming cut or a PURE instruction-by-instruction expansion.

## 3. New finite HEAD and the stronger pre-grid error

Write R=2^u, eps=1/R. Construct the exact rational

    V=2 sum_(j=0)^(u-1) 1/[3^(2j+1)(2j+1)],
    L2=floor(RV)/R.                                  (3.1)

Integrating the finite geometric series on [0,1/3], with its positive remainder, gives the standard series for ln2. Its tail after u terms is at most

    2*3^(-(2u+1))/[(2u+1)(1-1/9)]<=2^(-2u).

Consequently 0<=ln2-L2<2eps and 0<=L2<=ln2<1. Every actual score s is 0,L2 or 2L2, exactly, because the gated key blocks and the chosen query blocks are bits with the stated one-hot structure. For the ideal score s* formed with ln2,

    0<=s<=s*<=2ln2<2,  0<=s*-s<4eps.                (3.2)

This applies to every prefix and fallback row as well as q. There is no premature rounding of a dyadic score multiplication by a bit.

For the integer score numerator S=Rs, execute

    T_0=R,
    T_j=floor(T_(j-1) S/(jR)), j=1,...,8u,
    W(S)=sum_(j=0)^(8u)T_j.                           (3.3)

The full product and remainder are retained. Induction gives
0<=T_j/R<=s^j/j!, and hence 1<=W/R<=exp(s)<=4. At s=0 every T_j after T_0 is zero and W=R exactly.

Here is a uniform finite error estimate. Let e_j=s^j/j!-T_j/R. Then
e_0=0 and 0<=e_j<=s e_(j-1)/j+eps.
An error eps inserted at one step contributes to all subsequent term errors at most eps sum_(a>=0)2^a/a!<8eps, since the successive factorial denominators are at least a!. The inequality exp(2)<8 follows by a geometric bound on the tail after its fourth term. Summing the 8u insertions costs at most 64u eps.
For j>=9, 2^j/j!<=2^(-j): check j=9, then use the successive ratio 2/(j+1)<=1/2. Since u>=32, the omitted tail after 8u is at most 2^(-8u)<=eps. Finally (3.2) and the bound exp(t)<8 on [0,2] cost less than 32eps. Thus

    |W(S)/R-exp(s*)|<=(64u+33)eps<=100u eps.          (3.4)

On any row let m>=1 be its number of allowed keys and let v_t in {0,1} be one fixed value coordinate. Define the exact integer sums
D_int=sum W_t, A_int=sum W_t v_t,
and their ideal real analogues D*,A*. The normalized finite denominator D_int/R is at least m. Both sum errors are at most m eta with eta=100u eps. Because the ideal ratio lies in [0,1], adding/subtracting A*/(D_int/R) gives

    |A_int/D_int-A*/D*|<=2eta=200u2^-u.              (3.5)

There is no factor m left and no independence assumption. Bit-valued coordinates, positive masks, bounded scores and exact sums are all that this argument uses.

Flooring G times the finite ratio and dividing back by G adds less than 1/G. For integer u>=32, 200u<=2^(u/2) (true at 32 and preserved by the next integer step). Since u>=4g+64,

    200u2^-u<=2^(-u/2)<=1/G.

Therefore every returned scalar is on the closed G-grid and differs from its ideal normalized coordinate by at most 2/G. At q this says

    |Y/G-S_c/D|<=2/G, |Z/G-1/D|<=2/G.                (HEAD)

At past rows the ideal comparison is their own local-query prefix/fallback ratio. Their anchor coordinate is exactly zero. Singleton heads copy bits exactly, since their coordinate numerator is zero or equals their denominator. The stronger pre-grid estimate (3.5), not an arbitrary selection of errors inside HEAD, will be essential to the failure witness.

No exact-snap margin or lower bound of order D_*² was used in this proof. It therefore establishes HEAD for the new DOMAIN, without extending the admitted domain of 020's exact count result.

The rational arithmetic in (3.1) is finite: a common denominator is
3^(2u-1) product_(j=0)^(u-1)(2j+1).
It has O(u log(u+1)) bits. Construct it, each term numerator and their sum serially, and then compute the final integer quotient. School arithmetic, including every division, takes O(u³ log²(u+1)) bitwork and O(u log(u+1)) simultaneous scratch. Long offline integers are multiword arrays. Only the u-fractional-bit L2 is stored online.

## 4. Ideal algebra, ratio amplification, clipping and PATH

Fix a history and query at q. For t=3,...,N let
i_t=1{x_(t-2)=a}, j_t=1{x_(t-1)=beta_symbol}.
The ideal historical weight is
w_(alpha,beta)(t)=(1+i_t)^alpha(1+j_t)^beta in {1,2,4}.
There are exactly M historical keys, one per original departure, and one unit anchor. Thus

    D_(alpha,beta)=1+sum_t w_(alpha,beta)(t),
    S_(alpha,beta),c=sum_t w_(alpha,beta)(t)1{x_t=c},
    S_c+1<=D<=D_*, 0<=S_c<=4M.                      (4.1)

For each key, (1+i)(1+j)-(1+i)-(1+j)+1=ij, so

    C_c=S_11,c-S_10,c-S_01,c+S_00,c                 (4.2)

is exactly the original full triple count; J=sum C_c. These are mathematical identities, not free program inputs.

Put delta=2/G and abbreviate one ideal head/label by D,S. Since G>=8D_*,
delta D<=1/4 and Z/G>=1/D-delta>0. Integer Z>=1, so the q guard leaves it unchanged. Subtracting the ideal ratio and using S+1<=D yields

    |Y/Z-S|
      <=delta(1+S)/(1/D-delta)
      <=(2D²/G)/(1-2D/G)
      <=(8/3)D²/G<=4D_*²/G.                         (4.3)

For any nonnegative real t, |floor(t+1/2)-t|<=1/2, including ties. Projection onto an interval containing the target cannot increase distance from that target. Therefore the first clip in (2.2), whose interval contains S, gives
|U_c-S_c|<=4D_*²/G+1/2.
By (4.2), the four error magnitudes add to at most
e=16D_*²/G+2. The second clip interval [0,M] contains the true C_c and cannot increase that error. Hence

    |C'_c-C_c|<=e.                                  (4.4)

No claim of exact count recovery at this smaller G is made.

For clarity prove the positive-vector normalization inequality with the required denominator. If a,b have strictly positive sums A,B, let d=||a-b||_1. Then

    ||a/A-b/B||_1
      <=||a/A-a/B||_1+||a/B-b/B||_1
      =|B-A|/B+d/B<=2d/B.

Thus TV(a/A,b/B)<=min(1,d/B). Apply it with a=C'+1 and b=C+1, for which B=J+K and d<=Ke. This does not assume the two sums agree.

Finally for any positive normalized vector v, the first K-1 ordered Q-rounding errors e_c=v_c-floor(Qv_c)/Q belong to [0,1/Q). The residual coordinate has error minus their sum, so the TV rounding error is exactly sum_(c<K-1)e_c<=(K-1)/Q. Using (4.4) and the preceding normalization inequality proves

    TV(F_(h,g)(x;s),p_s^+(x))
      <=min(1,Ke/(J_s+K))+(K-1)/Q.                  (PATH)

This is all-path/all-query and covers zero counts, M1 and support-incompatible paths. Program legality at non-q was proved separately in Section 2, using the larger bound KM.

## 5. Uniform actual RISK and sufficient consistency scales

The imported 016 conclusion for the original full trajectory is

    sup_(theta,mu) E TV(p^+_(Y_M),theta_(Y_M))
       <=min(1,48T), T=K^(5/2)/sqrt(M+1).

It also supplies TRUNC for J, the actual terminal-row departure count:
with c=K⁴/(M+1), for every deterministic real A>=0,

    E min(1,A/(J+K))<=Psi(cA)<=2sqrt(cA).            (5.1)

Here Psi(0)=0, Psi(x)=x(1+ln(1/x)) for 0<x<1, and Psi(x)=1 for x>=1. To make its threshold scope explicit, the integer UC estimate in 016's derivation is P(J<w)<=min(1,cw), for integer w>=1. If A=0 there is nothing to prove. For A>0 and 0<t<1, write v=A/t-K. When v<=0, the event {J<v} is empty. When v>0, J integer gives {J<v}={J<ceil v}, with 1<=ceil v<=v+1<=A/t. Integrating min(1,cA/t) over t in (0,1) yields Psi(cA). Bounding this integrand by sqrt(cA/t) gives 2sqrt(cA). Thus neither a real threshold substituted into integer UC nor division by J at J=0 is used. We import this already admitted 016 result, not a new direct G/U predecessor.

Apply (5.1) to A=Ke, a nonrandom quantity fixed by K,M,g, in PATH at s=Y_M. The expectation is unconditional and no iid claim conditional on J or the actual row is involved. The triangle inequality gives

    R(K,M,h,g)
      <=min(1,48T+(K-1)/Q+Psi(x)),
    x=K⁵[16D_*²/G+2]/(M+1).                         (5.2)

The estimate is uniform over the stated class, so taking the supremum separately at each parameter tuple is valid. Since
(4M+1)²=16M²+8M+1<=16M(M+1) for M>=1,

    x<=256K⁵ M/G+2K⁵/(M+1).                         (5.3)

This proves the specified RISK, including small M and J=0.

Fix K and any public legal sequence h_M,g_M in DOMAIN. If G_M/M tends to infinity, the right side of (5.3) tends to zero; Psi is continuous at zero since x ln(1/x) tends to zero. Also T tends to zero and Q>=2M makes (K-1)/Q tend to zero. Hence R tends to zero uniformly over theta,mu. This is an E[TV] assertion, not a simultaneous almost-sure assertion or a fixed/all/conditional risk claim.

For a concrete intermediate scale, fix 0<epsilon<1, choose h=h0 and
G=2^ceil(log2(M^(1+epsilon))).
For sufficiently large M this is at least 8D_* and at least Q. Indeed Q(h0)<=max(16,4M)<=16M, while M^epsilon tends to infinity and 8D_*<=40M. The chosen G is less than 2M^(1+epsilon), whereas 2^g0>=4096(M+1)²; hence it is below 2^g0 eventually. It belongs to DOMAIN and satisfies M<<G<<M². The rounding operation here describes a public parameter sequence; it is not a hidden source oracle or a real arithmetic operation inside F.

Both Psi(x) and its weaker upper bound 2sqrt(x) suffice for the consistency conclusion G/M -> infinity. If instead one asks that this square-root upper bound on implementation error be O(M^(-1/2)) for fixed K, (5.3) gives an M² sufficient scale for G. That statement concerns one coarse upper certificate, not necessity, not sharp precision, and not a claim that consistency itself needs M². It also does not contradict 020's exact result in its finer precision domain.

## 6. TAU: positive denominator, DOMAIN membership and risk

Let 0<tau<1 and choose an integer M satisfying

    M+1>=(144 K^(5/2)/tau)².

Put
h=max(h0,ceil(log2(3(K-1)/tau))),
Delta=(M+1)tau²/36-2K⁵,
H=16K⁵D_*²/Delta,
g=max(g_min,ceil(log2 H)).

The sample condition gives (M+1)tau²/36>=576K⁵, so

    Delta>=574K⁵>0,  H<=16D_*²/574.                 (6.1)

Thus H is positive and finite. By Section 2, g_min<=g0. Moreover
2^g0>=4096(M+1)²>D_*²>H.
Since g0 is an integer, ceil(log2 H)<=g0. Therefore the prescribed g lies in the original DOMAIN without any enlarged upper endpoint.

Because G>=H, rearranging its definition gives

    16K⁵D_*²/G
      <=(M+1)tau²/36-2K⁵,
    x<=tau²/36.

So Psi(x)<=2sqrt(x)<=tau/3. The sample bound gives 48T<=tau/3, and the chosen h gives (K-1)/Q<=tau/3. Formula (5.2) proves R<=tau. This also proves the more precise finite sufficient certificate
48T+(K-1)/Q+Psi(x)<=tau whenever it holds, without requiring use of the square-root relaxation.

These are sufficient, not optimal configurations or lower bounds. For a positive rational tau, the displayed conditions and integer choices can be computed by rational/integer comparisons and shifts: compare (M+1)tau² with 144²K⁵ and compare powers of two against positive rationals 3(K-1)/tau and H. Any requested configuration work on an encoded tau is additional public preprocessing; F itself receives only its finite integer parameters. No real sqrt/log oracle is required by the program. For arbitrary real tau the displayed choices are mathematical existence/configuration formulas.

## 7. COARSE-FAIL from one fixed reachable trajectory and its actual joint heads

Take K=2 and the fixed homogeneous source

    theta_00=delta_1, theta_01=delta_1,
    theta_11=delta_0, theta_10=delta_0, mu=delta_00.

Starting at pair 00, the only path is 00 -> 01 -> 11 -> 10 -> 00, repeating, with observations 00110011.... Each experiment therefore has probability one on a single valid trajectory. No additional samples, test experiment or random initialization are introduced.

For all M use h_c=h0(M), g_c=g_min(M,h_c), G_c=2^g_c. These are legal by Section 2. In fact Q(h0)<=max(16,4M)<=16M<8D_* for M>=1. Hence g_c=ceil(log2(8D_*)), and

    32M<8D_*<=G_c<16D_*<=80M.                       (7.1)

So G_c=Theta(M) on the entire public sequence.

Now restrict to M=M_r=3*2^r, integer r>=2. M is divisible by four. At the terminal pair Y_M=00 the true next-symbol law is delta_1; the M observed departures contain exactly M/4 copies of each triple 001,011,110,100. A direct enumeration of these four kinds gives the following weights in the SAME trajectory, at query 00:

|triple|label|w_00|w_10|w_01|w_11|
|---|---|---:|---:|---:|---:|
|001|1|1|2|2|4|
|011|1|1|2|1|2|
|110|0|1|1|1|1|
|100|0|1|1|2|2|

The anchor contributes one only to D. Thus all four ideal head sums are simultaneously

|head|D|S_0|S_1|
|---|---|---|---|
|00|1+M|M/2|M/2|
|10|1+3M/2|M/2|M|
|01|1+3M/2|3M/4|3M/4|
|11|1+9M/4|3M/4|3M/2|

Call this joint table (7.2).

These are not independently chosen estimates or error values.

The exact precision identities on this subsequence are
h_c=r+3, g_c=r+7, G/M=lambda=128/3.
For h, ceil(log2(3*2^r))=r+2. For g, 8D_*=96*2^r+8 lies strictly between 2^(r+6) and 2^(r+7); this exponent dominates h.
The actual ell=ceil(log2(M+6)) satisfies
ell=5 at r=2, and ell=r+2 for r>=3, because
2^(r+1)<3*2^r+6<=2^(r+2) holds for r>=3.
Accordingly u=120 at r=2 and u=8r+100 for r>=3. In particular u>=8r+100 for all r>=2. All finite evaluations use this actual u; the shortcut at r=2 in the original candidate chain is not used.

Let z_tilde be an actual normalized anchor coordinate BEFORE the final G-grid floor. By the stronger estimate (3.5), not merely HEAD,

    |G z_tilde-G/D|<=200G u2^-u.

For integer u>=2 the quantity u2^-u decreases. Therefore, on this subsequence,

    200G u2^-u
      <=200(8r+100)2^(-7r-93) -> 0.                  (7.3)

From (7.2), with head order 00,10,01,11,

    G/D -> (128/3,256/9,256/9,512/27).               (7.4)

The respective open integer intervals containing these limits are
(42,43), (28,29), (28,29), (18,19).
Each has a positive distance from its endpoints. By (7.3)-(7.4), for all sufficiently large r, the actual G z_tilde lies inside the same open interval. The actual floor is therefore exactly

    (Z_00,Z_10,Z_01,Z_11)=(42,28,28,18) eventually. (7.5)

For example, a common distance smaller than 1/54 suffices once the convergence errors are smaller than it; the smallest upper-end distance is 19-512/27=1/27. No assertion that (7.5) already holds at r=2 is needed or made. Using an arbitrary error of size 2/G after flooring would not prove (7.5); that is why (3.5) was retained.

For each label, denote its actual pre-grid coordinate by y_tilde. Formula (3.5) gives y_tilde-S_c/D ->0, and the final floor changes Y/G by less than 1/G. Thus Y/G tends to the corresponding ideal normalized limit. Since G/M=lambda, Y/M tends to lambda times that limit. With Z eventually the fixed positive integer in (7.5), the raw half-up integer
H_c=floor(Y_c/Z+1/2) satisfies |H_c-Y_c/Z|<=1/2, so H_c/M has the limits:

|head|lim H_0/M|lim H_1/M|
|---|---:|---:|
|00|32/63|32/63|
|10|32/63|64/63|
|01|16/21|16/21|
|11|64/81|128/81|

Call this limit table (7.6).

For instance the 11 label0 limit is
(lambda*( (3/4)/(9/4) ))/18=(128/9)/18=64/81.
Every number in (7.6) lies strictly between 0 and 4. Therefore, for sufficiently large r the raw half-up integers lie in [0,4M], and the first clip is inactive; Z_safe=Z also then. This proves these are the limits of the actual U, not of a substituted decoder.

Inclusion-exclusion of these ACTUAL U gives the limits

    (U_11,0-U_10,0-U_01,0+U_00,0)/M
        ->64/81-16/21=16/567,
    (U_11,1-U_10,1-U_01,1+U_00,1)/M
        ->128/81-64/63-16/21+32/63=176/567.          (7.7)

Both numbers are strictly between 0 and 1. The second clip is therefore also inactive eventually. We have proved for the actual finite program

    (C'_0/M,C'_1/M)->(16/567,176/567).               (7.8)

Adding one to each coordinate contributes 1/M and hence vanishes. Their positive total divided by M tends to 192/567. Consequently
B_0/B_sum ->16/192=1/12.
The final ordered Q-floor changes the first normalized coordinate by less than 1/Q; Q=2^(r+3) tends to infinity. The second coordinate is exactly the residual. Thus

    F_(2,M_r,h_c,g_c)(x;Y_M)->(1/12,11/12).         (7.9)

Since the true actual row is delta_1 and the path has probability one, its actual TV is precisely F_0, both before taking an expectation and after. This proves

    lim_(r->infinity) E TV(F_(2,M_r,h_c,g_c),theta_(Y_M))=1/12.

For each M the class supremum is at least the risk at this SAME fixed theta,mu. Taking a limsup along all M, which dominates that subsequence limit, gives
limsup_M R(2,M,h_c(M),g_c(M))>=1/12.

The error does not disappear under normalization: (7.8) has a strictly positive erroneous-label coordinate. Mechanistically the 11 denominator scaling differs from the other three; this is derived from the actual jointly attainable floors, not assigned adversarial HEAD errors. This is one public coarse configuration and one fixed decoder. It neither rules out every other G=Theta(M) configuration, proves G/M->infinity necessary in general, nor gives an information-theoretic or Transformer-wide resource lower bound. The deterministic periodic source is used solely as this precision witness, with no stationary/mixing-rate assertion.

## 8. The same charged finite construction at the actual precision u

This section proves the new-domain implementation bounds; it does not merely rename 020's g0. The construction reused from 020/SRC consists of constant-size Boolean/ReLU bit gadgets, fixed-loop school arithmetic, the causal front end in Section 2, and the guarded decoder (2.2). Its cost arguments require g>=h, b<=h, ell in u, and finite bounded scores, all established here. The finer exact-snap inequality G>=64D_*² is used only for 020's count correctness, not for the construction or any bound below. All constants in the following O bounds are independent of K,M,h,g, source, history and query.

Use AND(a,b)=ReLU(a+b-1), NOT(a)=ReLU(1-a), and XOR as the sum of ReLU(a-b) and ReLU(b-a); OR and mux are fixed compositions. Ripple add/subtract and comparison have O(w) active bit gates/depth. School multiplication of w-bit words retains the full 2w-bit product, has O(w²) gates/depth and O(w) scratch. Restoring division scans a fixed number of numerator bits high-to-low, shifts the remainder, compares, subtracts by a mux and emits a quotient bit. The divisor is positive; the post-step remainder is below the divisor and the trial remainder below twice it. Numerator/divisor lengths a fixed multiple of w still give O(w²) active gates/depth and O(w) scratch. No input-dependent early exit is used. Signed values use sign/magnitude or two nonnegative rails with explicit comparisons and clipping.

A scalar H on the closed G-grid is extracted finitely: start A=GH, then for j=g,g-1,...,0 set
b_j=ReLU(A-(2^j-1))-ReLU(A-2^j), A:=A-2^j b_j.
The integer residual gives the exact next bit, including H=1 via its top bit. This uses O(g) gates/depth per scalar with charged residuals/thresholds. It is not a real-interval floor representation. Final dyadic decoding is the charged linear sum of numerator bits with weights 2^(j-h). Score-integer extraction, if represented as a scalar, similarly uses the finite u-grid.

Expand the 4K+4 statistical outputs in parallel. Compute the four Z_safe guards. Serially for each of K labels perform its four full half-up divisions, four clips, signed inclusion-exclusion and second clip, and keep C'_c. Only after all C' are available form B_sum, compute the K-1 final full quotient/remainder operations, partial quotient sum and final residual/decode. All unfinished banks, exact fields and results crossing layers have paid identity/copy holds. The two lag heads, mode/gating bit stages and QKV/output projections are also stages of this same shared circuit. This is a direct tokenwise arithmetic construction, not a generic unfolding of an n-token sequential algorithm.

### 8.1 Complete online word ranges

For (3.3), 0<=S<=2R, and every T_j and W is at most 8R (the stronger 4R bound is available). Hence a full T_(j-1)S product uses at most 2u+6 bits; jR for j<=8u uses at most u+ceil(log2(8u))+1 bits. A head denominator is at most 8nR and needs at most u+ell+4 bits. A full head dividend G A_int needs at most u+g+ell+4 bits. Remainders and trial shifts add only a fixed number of bits. These ranges apply to every nonempty prefix/fallback and singleton row.

Y,Z lie in [0,G]; Z_safe in [1,G]; 2Y+Z_safe<=3G and 2Z_safe<=2G. The raw half-up quotient is at most 2G, so even when non-q has Z=0 it has O(g) bits before being clipped. Clipped U lies in [0,4M]; pairwise signed differences and their inclusion-exclusion sum lie in [-8M,8M]. After clipping, C' lies in [0,M], B in [1,M+1], and B_sum<=K(M+1) by (2.3), requiring at most ceil(log2 K)+b+1 bits. The complete final dividend Q B_c requires at most h+b+1 bits. Trial remainders are below twice B_sum, and the output sum and residual fit h+1 bits. All these payloads are O(u) because h,b<=g and g,ell<=u/4.

For the scalar convention already used by the charged 020 construction, reserve sign plus 16u integer and 16u fractional positions per scalar/coefficient. Each full product is formed in a separate approximately 64u-bit temporary before any declared truncation; this is not multiplication of arbitrary 128u-bit operands with a discarded double-width result. Actual payloads, dyadic thresholds and coefficients fit within these fields. Select fixed bit templates and the serial schedule with per-layer channel/term bound 2^16 K u and depth bound 2^16 K u², the conservative construction constants supplied by 020. Thus at most 2^16 K u products are accumulated in any dense neuron. Sign plus accumulation guard length can be bounded by
16+ceil(log2 K)+ceil(log2 u)+2.
Together with the complete product this is strictly below 128u for u>=64, using log2 K<=ell<=u/4 and log2 u<u. The integer attention/decoder payloads just bounded are smaller.

Loop, layer, slot, token, mask and layout addresses are also finite charged words. With these constant-size templates the dense file and its record/working arrays have sizes bounded by fixed products of K³u^5, n², nKu² and u^4. Choosing the usual sequential segment offsets needs at most a fixed constant plus 3 log2 K+2 log2 n+O(log2 u) address bits. More explicitly the loose construction constants above permit a 64+4ell+8ceil(log2(u+1)) envelope for the needed segment/index counters; this is less than 16u for u>=64 (ceil(log2(u+1))<=u/4 there). Scalar product/guard bounds, not this address envelope, dominate. The compact controller and addresses therefore also fit 128u. Long offline rational integers are arrays, not single online words.

### 8.2 Neural, parameter and hold bounds

There are O(K) arithmetic tasks of O(u²) gates/depth, O(Ku) head-extraction/decoding terms and O(K²) conservative projection terms. At a time O(Ku) bit/scalar channels, including all retained banks and scratch, suffice. Consequently

    L=O(Ku²), W_per_token=O(Ku),
    active gates/projections=O(Ku²+K²),
    identity holds=O((Ku²)(Ku))=O(K²u³).             (8.1)

The holds are real identity nodes/connections; packed evaluator memory is not substituted for neural persistence. Exact query/endpoint/flag bits, extraction residuals, carries and outputs are included while live. Six total heads, at most four per stage, max QK=2K, statistical value dimension K+1 and score<=2 follow from Sections 2-3, independently of the precision-recovery outcome.

Fix the main representation as dense, with every actual coefficient slot and bias, including zero, written and executed. Pointwise/QKV/final projections fit the common padded width above, so slots are O(L W²)=O(K³u⁴) and parameter bits O(K³u⁵), using O(u)-bit coefficient fields. Arithmetic record, term and hold counts are from this same circuit. No sparse-storage savings are imported into its time or peak estimates.

### 8.3 All-token dense/uncached online work

For the main uncached variant, scan the explicitly stored finite masks for all rows and all six heads. Per effective edge compute the exact score from its O(K) projected coordinates, using charged integer/scalar operations; run all 8u recurrence steps (3.3), and update its denominator and K+1 value numerators. Full fixed-length school multiplication/division costs O(u²), so score/value work is O(Ku²) and exponential work O(u³) per edge. Stream a row into denominator/numerator buffers; do not allocate an n² numerical weight array. Compute every row coordinate by a full integer division; then clear its temporary arithmetic at a charged cost. Keep the required QKV arrays while the relevant stage runs.

All O(n²) candidate pairs and allowed edges, the singleton heads and non-q/fallback rows are accounted for. For reference, each statistical head has exactly
e_anchor=2+M(M+1)/2+(M+1)
effective edges and the copying heads have n each. A full six-mask pair scan uses 6n² Boolean entries if stored separately; it is permissible to share identical bit masks, with their writes/reads still charged. The distinction between scanning and doing a positive-weight update is retained. All index increments, mask reads, score extraction, row copies/resets and output divisions fit

    uncached attention bitwork=O(n²(K+u)u²).         (8.2)

Every dense coefficient slot, including zeros, is processed at all n tokens. O(u²) word work per coefficient/addition yields

    all-token dense pointwise/QKV bitwork
      =O(n L W² u²)=O(nK³u⁶).                       (8.3)

This includes the guards/divisions/holds at past tokens, not only q.

Observed-history acquisition writes NK one-hot bits. Query/mode, endpoint placeholders, public flags and positions require O(nK+n log(n+1)) initial writes; actual endpoint copies are made by the paid heads. Under the stipulated one-hot input no binary conversion is omitted; if a binary interface is introduced it must pay its own conversion and is outside this chosen input representation. Full residual/copy/hold/clear costs, grid extraction and all K(h+1)-bit numerators with final decode are included in (8.1)-(8.3), with acquisition separately named. Releasing or erasing histories/QKV after attention is counted, not a free storage port change.

For completeness the independently specified cached variant gives exactly the same outputs: evaluate (3.3) once for each complete score 0,L2,2L2, store W, then select its full integer by comparisons/muxes on every edge. In particular W(2L2) is not a square of a rounded exp(L2). This adds O(u³) offline generation, O(u) cache storage plus charged selector/code/clear terms, and replaces (8.2) by O(n²Ku²). All other dense costs and the phase rules below remain, including the cache when live. These costs are not mixed into the main uncached bound. No sparse variant or sparse acceleration is needed for this proof.

## 9. Offline full writes and simultaneous physical peak

Six finite mask bit arrays and positions occupy O(n²+n log(n+1)) bits. They are generated by public nested row/key integer loops with the stated self/fallback rules; allowing O(u²) bitwork per tested pair gives O(n²u²) generation including actual writes. Positions, flags, layouts and known public integer fields have finite index/shift generation, no numerical minus infinity or position oracle.

Let G_rec,T_rec,I_hold denote the actual gate, connection/term and identity records of the Section 8 circuit. Fixed-arity arithmetic, extraction/decode and projections give

    G_rec+T_rec=O(Ku²+K²), I_hold=O(K²u³).           (9.1)

Explicit loops over coordinates, arithmetic bit stages and every live channel at each intervening layer generate all records, including copies/holds. Record fields contain O(u)-bit coefficients and addresses. Assigning/sorting/arranging them costs
O((G_rec+T_rec+I_hold)u²) bitwork and
O((G_rec+T_rec+I_hold)u) scratch bits.
For example finite merge sort on O(u)-bit keys uses O(log(record count))=O(u) comparisons per record, and this gives the displayed bound. No sorting workspace is omitted.

Sweep every dense slot and bias in fixed lexicographic order, merging the sorted active records with the sweep, and write the actual O(u)-bit coefficient even when zero. O(u²) allowance per slot covers addressing, selection and complete writes; no per-slot scan of the full record list is used. This costs O(K³u⁶). The finite attention/arithmetic/mask/copy controller can use a compact O(u⁴)-bit evaluator code: constant Boolean primitives, O(u²) school templates with O(u)-bit indices, and recurrence metadata suffice, while K,n loop bounds are binary fields. This code is stored and executed, not free. Generating and writing it costs at most O(u⁵), absorbed by K³u⁶. Pointwise neural parameters remain separate from that code and are executed at every token.

Add the exact log generation from Section 3,
O(u³ log²(u+1)) work and O(u log(u+1)) scratch.
For the optional cached variant add its O(u³) generation and all cache/selector records/writes; for main uncached only L2 and recurrence code are offline. Include input/public initialization, layout, output-buffer writes and masks. From (9.1) the complete offline work is

    O(K³u⁶+n²u²+u³ log²(u+1)).                      (9.2)

No unknown exact-decimal cap, emitter or compiler profile is asserted.

Here is a simultaneous-memory accounting. Define the sizes of the live object groups, with a fixed constant allowance for simultaneous old/new copies:

|Object group|Physical bits|
|---|---:|
|Stored dense matrices including zeros/biases, layout and parameter fields|O(K³u⁵)|
|Finite masks and positions|O(n²+n log(n+1))|
|Stored observed one-hot input|NK|
|Query/mode/flags/endpoint acquisition and exact input placeholders|O(nK+n log(n+1))|
|Two rolling neural layers, retained exact fields and live residuals|O(nKu²)|
|Current attention-stage QKV arrays and all returned head banks|O(nKu²)|
|Row old/new accumulators, full arithmetic scratch, controller and addresses|O(Ku²+u²), absorbed by O(nKu²)|
|Decoded-count/output banks and unfinished output/residual arrays|O(nKu²)|
|Compact evaluator code|O(u⁴)|
|Exact rational-log arrays while being generated|O(u log(u+1))|
|Record/layout generation and sorting arrays while live|O(K²u⁴)|
|Cache, only in its separately declared variant|O(u), plus charged selector terms|

Call this live-object table (9.3).

The O(u) physical storage per logical bit/scalar neural channel is conservative and preserves the distinction between neural width and packed registers. A returned bank may be a segment of a rolling array or separately allocated; in (9.3) both possible allocations are allowed simultaneously, which is an upper bound, not reliance on free aliasing. No object is subtracted merely because it represents the same mathematical value. In a copy the two physical versions are both counted until the old one is released.

To spell out lifetimes by phase:
(a) During log generation, rational numerator/denominator/term arrays, already written program/code/public/input data, controller and output constant fields coexist.
(b) During circuit/layout/mask generation and full dense writes, generated parameters/code/masks, the complete active/hold record and sorting buffers, writer/controller and any retained log/input arrays coexist. We allow the log buffer to remain, so no ordering trick is needed.
(c) During acquisition and the copy/mode stage, program/code/masks/positions, stored input/public fields, both rolling layers, local QKV, copy residuals and local arithmetic coexist.
(d) During statistical attention, the same stored items, both rolling layers, statistical QKV, row accumulators/scratch, and already returned four-head banks coexist; previous-stage buffers can be cleared at the paid cost, or a constant duplicate can be accommodated.
(e) During decoding, program/code/public metadata, returned raw/expanded banks, count/output arrays, both rolling layers, exact retained bits and current full multiplication/division scratch coexist. The old historical/QKV/evaluator intermediates have been charged and cleared; no decoder port to them is available.
(f) Output writing includes the scalar decode and numerator buffers together until the final exposed q answer is copied. Offline buffers are released after their actual last uses; allowing them longer only gives the conservative bound already listed.

For each phase sum all its simultaneous groups first. Even the sum of all rows in (9.3) is bounded by

    O(P_u), P_u=K³u⁵+n²+nKu²+u⁴+u log(u+1),          (9.4)

because K²u⁴ is absorbed by K³u⁵, NK<=nK, and n log(n+1)=O(n²). Thus both offline and online phase-total physical peaks obey (9.4), including program, input, masks, QKV, controller, output and generation scratch. The rolling term alone is never reported as total peak.

The complete cost argument uses actual u=4g+4ell+64 throughout. The comparison u<=2p gives at most a common constant-factor envelope in p; it does not turn 128u into an original numerical 128p certificate, prove 020 fits Pi's cap, or give resource dominance/optimality. The result is within the shared causal batch-hybrid execution model; fully flattening attention as a PURE network is not used to justify its L/W bounds.

## 10. Closure and evidence boundary

Sections 2-4 prove DOMAIN, all-token legality, the new finite HEAD/pre-grid estimates and PATH; Sections 5-6 prove RISK, fixed-K consistency and the entire TAU certificate inside DOMAIN; Section 7 proves COARSE-FAIL on the actual jointly produced four heads of one fixed homogeneous source, with the disclosed r=2 precision correction; Sections 8-9 prove the complete actual-u resource conjunction including offline full writes and both phase-total peaks. These implications use exactly the three Fact predecessors listed in Section 1.

The scalar numerical exp/log oracles sometimes used as ideal notation are never implementation primitives. The argument was developed analytically; the Lead's r=5,8,12,20 exact-integer diagnostics were read only, not promoted to a proof. No new compiler, trajectory enumeration, literal ledger, recovered-emitter execution, network measurement or GPU task was run for this submission. [Non-scientific operational metadata omitted.]

[Non-scientific operational metadata omitted.] It neither resumes 021/022 nor addresses the separate stationary/mixing line. Standard inclusion-exclusion, finite perturbation, rounding, normalization and truncation are not claimed as novel tools. The new failure conclusion is scoped to the specified public coarse configuration and fixed decoder; general coarse necessity and resource optimality remain outside the claim. Acceptance of this nonroot conjunction does not settle the v10 mother problem.
