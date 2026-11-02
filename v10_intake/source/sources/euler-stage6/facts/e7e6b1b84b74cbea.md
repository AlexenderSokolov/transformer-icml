---
fact_id: e7e6b1b84b74cbea
problem_id: icml-general-prediction
author: prover
predecessors: [946d42d5bf502eb4, a53804d650803060]
glossary_introduces: {}
external_refs: []
statement_chars: 5284
---

## statement
# T2-LATE-QUERY-MEMORY：实际末对揭示前不可回读切口的联合样本与信息存储候选

016已正常接纳Fact a53804d650803060，联合K,M统计率的sqrt(logK)差距关闭。本项转向T2的一个明确必要环节：在实际末对出现之前压缩全部旧观察，随后只许读这份状态及最后两符号，统一actual预测需要多少历史相关状态。不是重投016或重新包装010的packed扫描；既有root、SRC、各RATE/MM5、014/015/016原接纳及依赖保持。本项尚未接纳，完成也不宣告同神经预算或v10完成。

## 1. 原统计实验与准确的新算法子类

K>=2、M>=2整数，N=M+2。theta为任意含零边的齐次二阶表，mu为任意初始对律，每条实验内部固定。观察完整X_1^N，Y_i=(X_(i+1),X_(i+2))、0<=i<=M，departures只计i=0,...,M-1。风险仍是E TV(output,theta_(Y_M))，TV为L1的一半，sup可逐K,M及算法选源。

唯一新增限制是明确的因果信息切口。在观察X_1^M后、观察X_(M+1),X_(M+2)前，编码器把全部历史相关信息存为消息I，取值空间大小至多2^s，s>=0为整数。之后旧历史不可回读，decoder只获I、最后两个真实符号X_(M+1),X_(M+2)、公开K,M及源独立随机性，并返回任意概率向量。末对正好为这两个新符号；不是外加的独立测试query。允许编码器与decoder拥有共享随机种子U，其与源及数据独立；各自私人随机性也源独立，不给decoder私有编码随机性之外的隐蔽通道。算法对所有源共同，参数、程序和码本不依隐藏theta/mu。

所有穿过切口的历史相关register、地址、控制、停止时刻、prefix endpoint、residual、snapshot及缓存都须包含于I的2^s容量。不存在额外免费prefix endpoint；公开时间M、固定布局或源独立随机种子不携带历史信息。实际物理成本中这些公开对象仍须收费。decoder的计算不受限；证明不可把一种读出公式当成所有decoder。切口前encoder甚至可读完整prefix并任意计算，这是给其更强能力。读出可依预算s选择。

记R_cut(K,M,s)为本共同随机算法子类的inf，对原母源类(theta,mu)的sup actual E[TV]。无此切口限制的R_min保持016定义。仅讨论统一均值风险，不扩成fixed/all/conditional或统一a.s.。

## 2. 待证信息容量下界及联合必要性

对K>=12令m=floor(K/4)>=3、b=floor(m/2)、d=m^2 b。待证全有限参数结论：

    R_cut(K,M,s) >= (1/96) 2^(-s/d),
                 K>=12, M>=2, s>=0整数。          (MEM)

常数96可争取更好，但不能未经新准确声明把较弱界冒作本结论。对任意正风险目标tau<1/96，统一风险<=tau必须

    s >= d log2(1/(96tau)),
    d>=K^3/1536.                                  (BITS)

s为整数时取右端的上整。该下界只指全部历史相关状态通过当前切口的容量。若某接口另保留D个值的历史相关侧信息，需将容量替换为2^s D；不能只报告query-token宽度而漏掉其他token或RAM。

由于本类为共同完整历史预测器的子类，同时由已接纳MM5原scope有

    R_cut >= max{2^-16 min(1,K^(5/2)/sqrt(M+1)),
                 (1/96)2^(-s/d)}.                 (JOINT-NEC)

两项取max，不相加，也不声称同一见证同时达到它们。0<tau<2^-16时仍必要M+1>=2^-32 K^5/tau^2。统计样本必要性与当前受限存储必要性是不同坐标，均不推出depth/width/bitwork的普遍下界。

## 3. 可核查源族与prefix切口（候选，须自足证明）

以MM5的四组合法clock源为构造来源，不能把改参数后的声明当成该旧Fact已证明。K>=12取互不相交C,U,V,W各m个字母，C含0，L=m^2。C上的循环字使p_t=(c_t,c_(t+1))枚举C^2，旋转令c_5=0。需给有限存在性或准确引用已接纳构造的适用部分。

每个(u,v)及j=1,...,b赋连续参数z_(u,v,j)∈[-1/2,1/2]，全部d参数独立可选。设置

    theta_(u,v)(w_(2j-1))=(1+z_(u,v,j))/m,
    theta_(u,v)(w_(2j))  =(1-z_(u,v,j))/m.

奇数m剩余W字母概率1/m；其余行沿原五步拼接p0 -> (c1,A) -> (A,B) -> (B,Z) -> (Z,0) -> p5，然后clock返回p0；A,B各均匀，Z按该UV行。赋值为theta_p0=Unif(U)、theta_(c1,u)=Unif(V)、theta_(v,w)=delta0、theta_(w,0)=delta_c6、theta_p_t=delta_c_(t+2) (5<=t<L)，未指定行delta0。检查shift、无冲突、归一化及剩余字母。

M=nL+r、0<=r<L，k=(2-r) mod L，初始化不依z：k=0用p0；k=1用(c1,Unif(U))；k=2用Unif(U)×Unif(V)；k=3用固定(v*,w*)；k=4用固定(w*,0)；其他k用p_k。

关键新检查是全部M>=2下，切口所在Y_(M-2)确定为p0，且其后两个符号A=X_(M+1)、B=X_(M+2)是独立均匀UV对，与整个prefix及编码消息I（条件于源独立种子）独立。不能用错误的“末对条件后一般源仍iid”。对于M小、n=0、k=1/2初始随机字母及k=3/4固定prefix，须逐项解释相位；原完整prefix的其他标签、边界信息全部允许encoder读取，证明不删掉它们。lower不要求有限样本无法估计z：即使encoder知道z并择最佳消息，容量障碍仍应成立。

## 4. 编码体积候选证明（需包括随机性与量词）

对每个固定共享随机种子u及消息i，decoder在各UV query上的输出随机性可先取平均。以每对W标签的坐标差定义

    zhat_(i,u;v1,v2,j)
       =clip_[-1/2,1/2]{ (m/2)(q_(2j-1)-q_(2j)) }.

这得到至多2^s个d维中心。请严格证明：actual末对均匀且独立prefix，使对每个z的风险至少

    (1/m^3) E_U min_(i<=2^s)||z-zhat_(i,U)||_1.

不能在见到随机末对后允许encoder另选消息；若允许那样做，d维同时中心论证会失效。随机decoder通过Jensen及clip不增距离处理；源相关消息概率不妨由oracle最小值下界。共享种子固定后逐个有限码本做积分，最后再交换非负积分得到一个固定源z的下界，不能逐条样本更换源。

在单位体积cube[-1/2,1/2]^d上，对C0<=2^s个任意中心，L1球体积<=2^d r^d/d!。候选取r=(d/8)2^(-s/d)，利用d!>=(d/e)^d及e<3，使球并体积<=(3/4)^d<=3/4。于是平均最近中心L1距离>=r/4=(d/32)2^(-s/d)。再用b/m>=1/3得MEM的1/96。请给体积、阶乘估计、边界clip、任意随机码本及有界积分交换的完整短证明，不以有限枚举替代。

这些是标准编码/体积方法，不称新工具或首创。若相位或信息口有真实矛盾，则登记准确障碍并保持OPEN；辅助估计失败不是目标反例。

## 5. 可达方向：原始计数的有限因果存储基线

为不把lower误当任意精确预算最优，同时给本切口模型中的明确强计数基线。对全部K>=2、M>=2及合法h>=h0(M)，Q=2^h，令

    b_M=ceil(log2(M+1)), B_K=ceil(log2 K),
    s_count=K^3 b_M+2 B_K.

候选算法逐符号取得同一one-hot历史，转换/保留最后两个符号，维护全部K^3个triple整数counts。在X_1^M切口处只保留prefix的M-2次departure计数及最后两个符号，其他历史清除；计数各为b_M bits。再读最后两个真实符号，补足恰好M次departure，选择实际末对对应的K个counts并输出原ordered dyadic add-one：前K-1坐标floor(Q(C+1)/(J+K))/Q，最后补残差。求和/完整除法、余数、控制、copy/clear和输出均实际收费，不能免费给出counts。

证明其切口历史容量<=2^(s_count)，输出全路径合法且距p+的TV<=(K-1)/Q。由016已接纳上界，风险<=min(1,48T+(K-1)/Q)<=min(1,49T)<=min(1,64T)。这里T=K^(5/2)/sqrt(M+1)，不同程序仅共享风险证书，不声称真实风险或输出bits相同。

提供一个明确有限顺序位程序实现作为存在性及完整收费基线，无免费大整数oracle或随机寻址。可用逐departure顺序扫描全部K^3计数块的保守实现，每块比较公开triple索引并执行完整gated increment。设w=h+b_M+B_K+O(1)，核实或给更准确的：online active bitwork O(NK+MK^3(b_M+B_K)+K w^2)，同时存活物理bits O(K^3 b_M+K w+w)，有限控制/公开索引/布局、取得one-hot/转换、状态移动/copy/clear、输出及offline生成写出均列账。不得将packed persistence当成免费neural holds。

若输入约定要求一开始完整batch历史已同时存储，则那份NK buffer须单列峰值并在切口前擦除/断开；不能抹去其存在。该streaming/顺序位程序不是原SRC共享逐token网络的实现，不把其寄存器数冒称neural width；不得据此宣称同一neural cap的优势。无需新增compiler或大规模枚举，解析构造及证明足够；literal ledger未运行则如实说明。

取M+1>=(64K^(5/2)/tau)^2、h=h0给一个同目标样本/切口状态充分配置：样本O(K^5/tau^2)，s_count=O(K^3[1+logK+log(1/tau)])。与BITS比较保留logK及常数差距，不自动宣称全参数存储最优。任何进一步匹配的参数子域须明确单列。已存在010扫描可在末对已知后重读历史而只保留一行counts；它不满足本切口禁止回读约束，应明确保留为另一强基线，不能用MEM排除它。

## 6. 真实依赖、结论边界与正常网关

预期实际前驱为MM5 Fact946d42d5bf502eb4（JOINT-NEC及准确沿用的clock事实）与016 Facta53804d650803060（计数基线风险）。MEM新增连续参数族、prefix相位与体积论证必须自足；若另用旧Fact则如实登记。旧文件R-CAP或FILE-SCOPED PASS仅作来源，不自动接纳。

完整承诺为MEM、BITS、JOINT-NEC及明确计数可达基线/费用界。自足完整证明需要独立审查。Counter做一次有界互补攻击，[Private task allocation omitted from the public export.]若具体候选有缺口或费用式不成立，给精确原因及修复方向，保持OPEN，不静默修改定义或较弱替代后宣称原合取完成。

这个结果若成立，是同actual母实验内一个明确无回读、晚query子类的信息存储边界。它不覆盖保留raw history的模型，不给单个query-token宽度下界，不排除全历史strong direct，不证明原Pi同预算优势或内部资源最优。真正causal batch neural的完整预算allocation、一般K故障预算紧性、物理纠错实现及主文新颖性范围继续保留。[Non-scientific operational metadata omitted.]


## proof
Original contract and explicit scope for this proof:
{"contract_id":"e6b7592e781948d00eb2a2effb80d8e3ef77e480f8d70f960286bc33faf730af","definitions":"## A. 共同源、观察、算法及风险定义\n\n对每个整数 K>=2，A={0,...,K-1}，S=A²，D=K²。一个实验固定一个时间齐次二阶表 theta∈(Delta(A))^S，允许零坐标；初始对分布 mu∈Delta(S) 任意。令\n\n    Y_j=(X_(j+1),X_(j+2)),\n    P_theta((a,b),(b,c))=theta_(a,b)(c),\n    N>=3, M=N-2, E_N=Y_M,\n    n_s(M)=sum_(j=0)^(M-1)1{Y_j=s},\n    C_s,c(M)=sum_(j=0)^(M-1)1{Y_j=s,X_(j+3)=c},\n    p_s^+=(C_s+1)/(n_s+K).\n\n每次预测完整观察 X_1^N。最后一个计数后继是 X_N；Y_M 不是额外 departure。actual query 从已观察最后两符号取得；fixed-query 任务另有明确的公开 s。X_(N+1)、theta、mu、支持、闭类、平稳律、未来行栈及隐藏源标签不可见。外部 query 是同一历史下调用的查询参数，不额外赠送干净端点或统计量。获得和复制实际端点在实现中收费。\n\n共同算法族的程序和公开精度可以依赖 K,N,h，不能依赖未知 theta,mu 或其隐藏标签。统计根中的理想 p^+ 是分析变量；给定实现的计数、头输出等实际可见代码由来源实现义务确定，不能据理想表达式新增 readout 端口。比较中的任意全历史预测器可以用全部 X_1^N 和源独立随机种子，输出任意概率向量。具体 Pi 则遵守自己已声明的内部信息切口。\n\nTV(p,q)=1/2 sum_c|p_c-q_c|。对给定 family F，令 Z_N(s)=TV(F_(K,N,h)(X_1^N;s),theta_s)。严格区分：\n\n| 名称 | 定义 | 量词 |\n|---|---|---|\n| fixed row | E Z_N(s) | 固定公开 s |\n| all contexts | E max_(s∈S) Z_N(s)；另可问其 a.s. 极限 | 全 K² 行，不改成访问行 |\n| actual terminal | R_act=E Z_N(E_N) | 同一历史的末尾 query |\n| conditional terminal | E[Z_N(E_N)\\|E_N=s] | 仅当 p_N(s)=mu P^M(s)>0；零概率时未定义 |\n| empirical weighted | E sum_s(n_s/M)Z_N(s) | 同历史频率权重 |\n| other history weighted | E sum_s w_s(X_1^N)Z_N(s) | w 为观察历史可测 simplex；不自动有一致性 |\n\n逐源极限固定 K,theta,mu 后令 N→∞。统一均值是每个 N 的 sup_(theta,mu) R_act；取 supremum 时源可随 N 改选，但一个样本路径内部的核必须齐次。固定 K 的统一结论不是 K 随 N 变化的无条件结论，也不是 changing-source 的统一几乎处处结论。输出允许零坐标，损失仅 TV，本 contract 不把它解释为 positive-output KL。\n\n\n## 共同研究范围的约定\n\n接口I是一个程序性质的定义，不能作为所有算法已经满足的全局假设。条件统计根对任意满足I的共同有限族F证明蕴含式；具体Pi满足I及其完整成本须由SRC-Pi的正常独立来源义务支持，不能在证明SRC-Pi时先假定它。原第二阶段固定证明是可查来源，旧Fact编号不是新项目前驱。\n\n后继真实资源/可靠性命题可以在同一contract内建立独立义务，不必谎称它们是统计根的前提。数据观察及TV实验保持上述定义。每项具体实现须声明自己的内部代码、允许回读、输出格式、参数/字长、batch或streaming等执行方式；比较只在所声明的共同条件下成立。原Pi的finite-attention加pointwise batch hybrid、literal bit/ReLU模块的packed/scalar、sparse/dense选项分别核算，不将一项格式的便宜坐标拼入另一项。\n\n完整费用包括实际head和局部绑定、输入/query/端点取得、参数/零系数、物理字、复制/跨层保持/清除、mask/position、所有活动bank与metadata、online/offline工作和同时峰值。不能免费引入计数、normalizer、译码或生成器。新算术/扰动参数由各精确义务局部量化；改变共同数据律、可见信息或风险须建立新的明确数学范围。\n\n给定接口的条件定理、具体实现定理、训练可达性、必要资源及新颖性是不同主张。数学根只包含数学命题。行政完成程序不是数学前提；独立后续结论不改变已有定理的证明依赖。\n","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]},"statement":"# T2-LATE-QUERY-MEMORY：实际末对揭示前不可回读切口的联合样本与信息存储候选\n\n016已正常接纳Fact a53804d650803060，联合K,M统计率的sqrt(logK)差距关闭。本项转向T2的一个明确必要环节：在实际末对出现之前压缩全部旧观察，随后只许读这份状态及最后两符号，统一actual预测需要多少历史相关状态。不是重投016或重新包装010的packed扫描；既有root、SRC、各RATE/MM5、014/015/016原接纳及依赖保持。本项尚未接纳，完成也不宣告同神经预算或v10完成。\n\n## 1. 原统计实验与准确的新算法子类\n\nK>=2、M>=2整数，N=M+2。theta为任意含零边的齐次二阶表，mu为任意初始对律，每条实验内部固定。观察完整X_1^N，Y_i=(X_(i+1),X_(i+2))、0<=i<=M，departures只计i=0,...,M-1。风险仍是E TV(output,theta_(Y_M))，TV为L1的一半，sup可逐K,M及算法选源。\n\n唯一新增限制是明确的因果信息切口。在观察X_1^M后、观察X_(M+1),X_(M+2)前，编码器把全部历史相关信息存为消息I，取值空间大小至多2^s，s>=0为整数。之后旧历史不可回读，decoder只获I、最后两个真实符号X_(M+1),X_(M+2)、公开K,M及源独立随机性，并返回任意概率向量。末对正好为这两个新符号；不是外加的独立测试query。允许编码器与decoder拥有共享随机种子U，其与源及数据独立；各自私人随机性也源独立，不给decoder私有编码随机性之外的隐蔽通道。算法对所有源共同，参数、程序和码本不依隐藏theta/mu。\n\n所有穿过切口的历史相关register、地址、控制、停止时刻、prefix endpoint、residual、snapshot及缓存都须包含于I的2^s容量。不存在额外免费prefix endpoint；公开时间M、固定布局或源独立随机种子不携带历史信息。实际物理成本中这些公开对象仍须收费。decoder的计算不受限；证明不可把一种读出公式当成所有decoder。切口前encoder甚至可读完整prefix并任意计算，这是给其更强能力。读出可依预算s选择。\n\n记R_cut(K,M,s)为本共同随机算法子类的inf，对原母源类(theta,mu)的sup actual E[TV]。无此切口限制的R_min保持016定义。仅讨论统一均值风险，不扩成fixed/all/conditional或统一a.s.。\n\n## 2. 待证信息容量下界及联合必要性\n\n对K>=12令m=floor(K/4)>=3、b=floor(m/2)、d=m^2 b。待证全有限参数结论：\n\n    R_cut(K,M,s) >= (1/96) 2^(-s/d),\n                 K>=12, M>=2, s>=0整数。          (MEM)\n\n常数96可争取更好，但不能未经新准确声明把较弱界冒作本结论。对任意正风险目标tau<1/96，统一风险<=tau必须\n\n    s >= d log2(1/(96tau)),\n    d>=K^3/1536.                                  (BITS)\n\ns为整数时取右端的上整。该下界只指全部历史相关状态通过当前切口的容量。若某接口另保留D个值的历史相关侧信息，需将容量替换为2^s D；不能只报告query-token宽度而漏掉其他token或RAM。\n\n由于本类为共同完整历史预测器的子类，同时由已接纳MM5原scope有\n\n    R_cut >= max{2^-16 min(1,K^(5/2)/sqrt(M+1)),\n                 (1/96)2^(-s/d)}.                 (JOINT-NEC)\n\n两项取max，不相加，也不声称同一见证同时达到它们。0<tau<2^-16时仍必要M+1>=2^-32 K^5/tau^2。统计样本必要性与当前受限存储必要性是不同坐标，均不推出depth/width/bitwork的普遍下界。\n\n## 3. 可核查源族与prefix切口（候选，须自足证明）\n\n以MM5的四组合法clock源为构造来源，不能把改参数后的声明当成该旧Fact已证明。K>=12取互不相交C,U,V,W各m个字母，C含0，L=m^2。C上的循环字使p_t=(c_t,c_(t+1))枚举C^2，旋转令c_5=0。需给有限存在性或准确引用已接纳构造的适用部分。\n\n每个(u,v)及j=1,...,b赋连续参数z_(u,v,j)∈[-1/2,1/2]，全部d参数独立可选。设置\n\n    theta_(u,v)(w_(2j-1))=(1+z_(u,v,j))/m,\n    theta_(u,v)(w_(2j))  =(1-z_(u,v,j))/m.\n\n奇数m剩余W字母概率1/m；其余行沿原五步拼接p0 -> (c1,A) -> (A,B) -> (B,Z) -> (Z,0) -> p5，然后clock返回p0；A,B各均匀，Z按该UV行。赋值为theta_p0=Unif(U)、theta_(c1,u)=Unif(V)、theta_(v,w)=delta0、theta_(w,0)=delta_c6、theta_p_t=delta_c_(t+2) (5<=t<L)，未指定行delta0。检查shift、无冲突、归一化及剩余字母。\n\nM=nL+r、0<=r<L，k=(2-r) mod L，初始化不依z：k=0用p0；k=1用(c1,Unif(U))；k=2用Unif(U)×Unif(V)；k=3用固定(v*,w*)；k=4用固定(w*,0)；其他k用p_k。\n\n关键新检查是全部M>=2下，切口所在Y_(M-2)确定为p0，且其后两个符号A=X_(M+1)、B=X_(M+2)是独立均匀UV对，与整个prefix及编码消息I（条件于源独立种子）独立。不能用错误的“末对条件后一般源仍iid”。对于M小、n=0、k=1/2初始随机字母及k=3/4固定prefix，须逐项解释相位；原完整prefix的其他标签、边界信息全部允许encoder读取，证明不删掉它们。lower不要求有限样本无法估计z：即使encoder知道z并择最佳消息，容量障碍仍应成立。\n\n## 4. 编码体积候选证明（需包括随机性与量词）\n\n对每个固定共享随机种子u及消息i，decoder在各UV query上的输出随机性可先取平均。以每对W标签的坐标差定义\n\n    zhat_(i,u;v1,v2,j)\n       =clip_[-1/2,1/2]{ (m/2)(q_(2j-1)-q_(2j)) }.\n\n这得到至多2^s个d维中心。请严格证明：actual末对均匀且独立prefix，使对每个z的风险至少\n\n    (1/m^3) E_U min_(i<=2^s)||z-zhat_(i,U)||_1.\n\n不能在见到随机末对后允许encoder另选消息；若允许那样做，d维同时中心论证会失效。随机decoder通过Jensen及clip不增距离处理；源相关消息概率不妨由oracle最小值下界。共享种子固定后逐个有限码本做积分，最后再交换非负积分得到一个固定源z的下界，不能逐条样本更换源。\n\n在单位体积cube[-1/2,1/2]^d上，对C0<=2^s个任意中心，L1球体积<=2^d r^d/d!。候选取r=(d/8)2^(-s/d)，利用d!>=(d/e)^d及e<3，使球并体积<=(3/4)^d<=3/4。于是平均最近中心L1距离>=r/4=(d/32)2^(-s/d)。再用b/m>=1/3得MEM的1/96。请给体积、阶乘估计、边界clip、任意随机码本及有界积分交换的完整短证明，不以有限枚举替代。\n\n这些是标准编码/体积方法，不称新工具或首创。若相位或信息口有真实矛盾，则登记准确障碍并保持OPEN；辅助估计失败不是目标反例。\n\n## 5. 可达方向：原始计数的有限因果存储基线\n\n为不把lower误当任意精确预算最优，同时给本切口模型中的明确强计数基线。对全部K>=2、M>=2及合法h>=h0(M)，Q=2^h，令\n\n    b_M=ceil(log2(M+1)), B_K=ceil(log2 K),\n    s_count=K^3 b_M+2 B_K.\n\n候选算法逐符号取得同一one-hot历史，转换/保留最后两个符号，维护全部K^3个triple整数counts。在X_1^M切口处只保留prefix的M-2次departure计数及最后两个符号，其他历史清除；计数各为b_M bits。再读最后两个真实符号，补足恰好M次departure，选择实际末对对应的K个counts并输出原ordered dyadic add-one：前K-1坐标floor(Q(C+1)/(J+K))/Q，最后补残差。求和/完整除法、余数、控制、copy/clear和输出均实际收费，不能免费给出counts。\n\n证明其切口历史容量<=2^(s_count)，输出全路径合法且距p+的TV<=(K-1)/Q。由016已接纳上界，风险<=min(1,48T+(K-1)/Q)<=min(1,49T)<=min(1,64T)。这里T=K^(5/2)/sqrt(M+1)，不同程序仅共享风险证书，不声称真实风险或输出bits相同。\n\n提供一个明确有限顺序位程序实现作为存在性及完整收费基线，无免费大整数oracle或随机寻址。可用逐departure顺序扫描全部K^3计数块的保守实现，每块比较公开triple索引并执行完整gated increment。设w=h+b_M+B_K+O(1)，核实或给更准确的：online active bitwork O(NK+MK^3(b_M+B_K)+K w^2)，同时存活物理bits O(K^3 b_M+K w+w)，有限控制/公开索引/布局、取得one-hot/转换、状态移动/copy/clear、输出及offline生成写出均列账。不得将packed persistence当成免费neural holds。\n\n若输入约定要求一开始完整batch历史已同时存储，则那份NK buffer须单列峰值并在切口前擦除/断开；不能抹去其存在。该streaming/顺序位程序不是原SRC共享逐token网络的实现，不把其寄存器数冒称neural width；不得据此宣称同一neural cap的优势。无需新增compiler或大规模枚举，解析构造及证明足够；literal ledger未运行则如实说明。\n\n取M+1>=(64K^(5/2)/tau)^2、h=h0给一个同目标样本/切口状态充分配置：样本O(K^5/tau^2)，s_count=O(K^3[1+logK+log(1/tau)])。与BITS比较保留logK及常数差距，不自动宣称全参数存储最优。任何进一步匹配的参数子域须明确单列。已存在010扫描可在末对已知后重读历史而只保留一行counts；它不满足本切口禁止回读约束，应明确保留为另一强基线，不能用MEM排除它。\n\n## 6. 真实依赖、结论边界与正常网关\n\n预期实际前驱为MM5 Fact946d42d5bf502eb4（JOINT-NEC及准确沿用的clock事实）与016 Facta53804d650803060（计数基线风险）。MEM新增连续参数族、prefix相位与体积论证必须自足；若另用旧Fact则如实登记。旧文件R-CAP或FILE-SCOPED PASS仅作来源，不自动接纳。\n\n完整承诺为MEM、BITS、JOINT-NEC及明确计数可达基线/费用界。自足完整证明需要独立审查。Counter做一次有界互补攻击，[Private task allocation omitted from the public export.]若具体候选有缺口或费用式不成立，给精确原因及修复方向，保持OPEN，不静默修改定义或较弱替代后宣称原合取完成。\n\n这个结果若成立，是同actual母实验内一个明确无回读、晚query子类的信息存储边界。它不覆盖保留raw history的模型，不给单个query-token宽度下界，不排除全历史strong direct，不证明原Pi同预算优势或内部资源最优。真正causal batch neural的完整预算allocation、一般K故障预算紧性、物理纠错实现及主文新颖性范围继续保留。[Non-scientific operational metadata omitted.]\n"}

Admitted prerequisite interfaces (use only within the recorded scopes):
[{"exact_statement":"# RATE-K5-MINIMAX：周期稀疏观测下的共同算法 actual TV 下界候选\n\n这是独立的新候选，不是已接纳结果，也不从原始add-one的确定后继反例直接推出。原G/U、SRC、RATE、K3、K-LOW及RATE-K-MINIMAX的接纳与依赖不变；RATE-K-SHARP-ADDONE的REFUTE+证明及网关独立继续。本义务失败不影响上述事项，完成亦不宣告v10结束。\n\n对每个整数K>=2、M>=1，N=M+2，字母表{0,...,K-1}。theta为任意允许零边的齐次二阶转移表，mu为任意初始对律；每个实验内theta固定。令Y_i=(X_(i+1),X_(i+2))，观察完整X_1^(M+2)，实际目标为theta_(Y_M)。共同全历史概率预测器A可依公开K,M选取，可使用与源独立的随机种子，不可读取隐藏theta、mu或未来符号。定义\n\n    R_min(K,M)=inf_A sup_(theta,mu) E TV(A(X_1^(M+2)),theta_(Y_M)).\n\n待证明的完整有限参数结论为\n\n    R_min(K,M)>=2^(-16) min{1,sqrt(K^5/(M+1))}.       (MM5)\n\n这里是原同轨迹actual的E[TV]，不是E[TV²]、KL、fixed/all/conditional风险或另加独立测试实验。sup可随K,M及算法选择源；不声称同一源对全部算法或全部horizon同时达到下界。\n\n## 候选合法源族\n\nK>=12时取m=floor(K/4)>=3、L=m²、b=floor(m/2)。取四个互不相交的字母组C,U,V,W，各有m个字母，C含字母0；其余字母不被访问。\n\n取C上的循环字c_0,...,c_(L-1)，使p_t=(c_t,c_(t+1))枚举全部C² pair且各出现一次，按模L延拓，旋转令c_5=0。需给出这种循环字的有限存在性证明。\n\n对每个(u,v)∈U×V、j=1,...,b引入未知sigma_(u,v,j)∈{-1,+1}。公开0<alpha<=1/2，设\n\n    theta_(u,v)(w_(2j-1))=(1+alpha sigma_(u,v,j))/m,\n    theta_(u,v)(w_(2j))  =(1-alpha sigma_(u,v,j))/m.\n\n奇数m时剩余W字母概率1/m，W外为0。其余行定义为\n\n    theta_p0=Unif(U),\n    theta_(c_1,u)=Unif(V)                      (u∈U),\n    theta_(v,w)=delta_0                       (v∈V,w∈W),\n    theta_(w,0)=delta_(c_6)                   (w∈W),\n    theta_p_t=delta_(c_(t+2))                 (5<=t<L),\n    其余未指定行=delta_0。\n\n需检查所有赋值无冲突、概率归一化和合法shift。预期每圈以五步等长拼接\n\n    p0 -> (c_1,A) -> (A,B) -> (B,Z) -> (Z,0) -> p5=(0,c_6)\n\n替代clock前五步，A∼Unif(U)、B∼Unif(V)，Z条件律为theta_(A,B)，之后沿clock返回p0。圈长L不依任何随机选择或sigma；完整轨迹除观测到的Z外不应泄露额外sigma信息。这一点必须从实际路径律证明，不能把额外clock状态视为免费删除的数据。\n\n## 全余数初始化及完整观察实验\n\n写M=nL+d，0<=d<L，取起始相位k=(2-d) mod L，使实际末对位于UV查询相位2。以下初始化均不得依sigma：\n\n- k=0：mu=delta_p0；\n- k=1：mu=delta_(c_1)⊗Unif(U)；\n- k=2：mu=Unif(U)⊗Unif(V)；\n- k=3：mu=delta_(v_*)⊗delta_(w_*)；\n- k=4：mu=delta_(w_*)⊗delta_0；\n- 5<=k<L：mu=delta_p_k。\n\nv_*∈V、w_*∈W固定公开。初始pair本身不要求由更早未观测历史生成。不同M可选择不同mu，实验内仍使用同一个齐次theta。\n\n需严格证明：完整已观察历史与n=floor(M/L)个iid训练block(A_i,B_i,Z_i)，加上一个与全部训练block独立的均匀actual末对(A_(n+1),B_(n+1))，以及无sigma信息的公开前缀/clock填充等价。k=1,2中的初始随机字母应计入首个训练block或最终末对，不能遗漏信息；k=3,4中的固定前缀不能包含未计的标签样本。覆盖所有余数、n=0及全部departure索引，不把一般源的条件样本称为iid。\n\n## 测试下界、常数与输出范围\n\n候选alpha=min{1/2,(1/8)sqrt(m³/(n+1))}。相邻sigma仅翻转一个UV行的一个标签对，预期完整观察KL至多8n alpha²/m³<=1/8。实际末对和clock前缀必须纳入路径律验证。对任意随机预测器用该标签对的坐标顺序作测试，处理ties、种子、实际末对条件律及均匀row权重；目标先得\n\n    R_min(K,M)>=(1/64) min{1,sqrt(m³/(floor(M/m²)+1))}.\n\n须证明完整实验而非丢失信息后的实验满足此式。随后以m>=K/8及有限参数分情况比较，推出保守的(MM5)。2<=K<=11可使用当前项目G/U Fact a12539a93d9f1ee3的共同算法iid actual下界1/(16sqrt(M+2))，必须明确有限常数比较。高K源族及测试论证应自足；唯一预期必需Fact前驱为a12539a93d9f1ee3。既有RATE-K-MINIMAX的证明可作为写作来源，不能未经说明扩张其已接纳scope。\n\n若(MM5)成立，统一actual均值风险tau满足0<tau<2^-16的任何共同算法必须有\n\n    M+1>=2^-32 K^5/tau²。\n\n这仅为样本必要性；不推出内部位数、深宽、算术工作、资源最优性。与已接纳K³/sqrt(M+1) upper比较仍有K指数差距，不称sharp匹配。未知标签族是新增的研究内容，原确定delta_0族并未自动提供此结论。\n\n首先做有界反向核查；若发现相位、信息或常数缺口，登记精确障碍并保持OPEN。只有完整自足证明和正常独立网关才能接纳。不重复提交原SHARP+否定构造，不重新审查已完成root。周期稀疏访问构造、条件L1估计及两点测试不作新工具或首创宣称。","fact_id":"946d42d5bf502eb4","scope_bindings":[{"evidence_id":"aa23c442ca1006c6ac0b12379f64a0fa500fbbd6a2e41c798b7a4de3952baa82","obligation_id":"3883ea68e83601751cd4e4ff1500d552ac6e412c158b39a9912f6e1de55283dd","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]}}],"source_hash":"fe18f4a413fef5da14c5f361aef47a8c5addceac1a3a58d73366ad20f16d8e93"},{"exact_statement":"# RATE-L1-MAX：去除剩余 sqrt(log K) 的共同 actual TV 率候选及同风险配置\n\n本项是015完整接收后的独立科学后继。014、015及旧root的准确声明、接纳和依赖保持；本候选不是由它们的接纳自动得到，也不是任何旧结果的逆向前提。直接对前缀L1范数作有界差分是本次待核查的改动，不以相邻高矩参数优化替代。完成本项亦不宣告v10的资源与机制母题完成。\n\n## 1. 原完整实验与准确目标\n\n全部整数K>=2、M>=1，N=M+2，字母表{0,...,K-1}。theta为任意允许零边的齐次二阶转移表，mu为任意初始对律。每次实验内theta固定；sup可随K,M选源。观察完整X_1^(M+2)，Y_i=(X_(i+1),X_(i+2))，0<=i<=M。\n\n    C_s,a=sum_(i=0)^(M-1)1{Y_i=s,X_(i+3)=a},\n    n_s=sum_a C_s,a, J=n_(Y_M), p_s,a^+=(C_s,a+1)/(n_s+K),\n    T(K,M)=K^(5/2)/sqrt(M+1),\n    R_K^+(M)=sup_(theta,mu) E TV(p^+_(Y_M),theta_(Y_M)).\n\n待证结论：\n\n    R_K^+(M)<=min{1,48 T(K,M)}.                       (L1+)\n\n仍为同完整轨迹actual E[TV]，不是TV平方、fixed/all/conditional、独立测试查询或删尾平均。算法只获历史及公开参数，不获辅助行栈、隐藏theta/mu、访问参数或未来符号。所有退化行、周期/可约/暂态、J=0、小M及任意初始化均需覆盖。\n\n## 2. 直接L1最大集中的具体候选（全部需证明）\n\n有限辅助耦合为每个K²行提供2M个独立theta_s符号并顺序复现原M次departure。令S_s,j=sum_(l<=j)(e_(xi_s,l)-theta_s)。对确定整数1<=v<=M定义\n\n    F_s,v=max_(0<=j<=2v)||S_s,j||_1,\n    Z_v=max_s F_s,v.\n\n只对确定行/确定前缀使用iid。目标链：\n\n    E F_s,v <= sqrt(8Kv),\n    改变一个栈符号使F_s,v至多改变2,\n    P(F_s,v-E F_s,v>t)<=exp(-t²/(4v)), t>=0,\n    ||Z_v||_4 <= sqrt(8Kv)+sqrt(8v ln K)+32^(1/4)sqrt(v)\n              <= (25/4)sqrt(Kv).                    (L1MAX)\n\n均值可用L1/L2比较及有限Doob L2；集中直接作用于整个L1前缀最大值，其坐标敏感度2与K无关。请给有界差分的条件区间推导及尾积分。K²行union后以a=sqrt(8v lnK)平移，剩余正部四次矩应<=32v²；行最大值之间不要求独立。不得将sqrt(K)再次乘在全部集中误差上。\n\n最后常数可用lnK/K<=1/e<3/8、K>=2，从而系数至多sqrt(8)+sqrt(3)+2^(3/4)<25/4；所有常数比较须明确可审。该吸收利用的是sqrt(K)均值和sqrt(logK)偏差的相加，不声称偏差本身没有logK。\n\n在E_v={v<=J<2v}上逐路径TV(phat_(Y_M),theta_(Y_M))<=Z_v/(2v)。然后仅用无条件Holder及G/U整数UC：\n\n    c=K^4/(M+1), P(J<w)<=min(1,cw), 整数w>=1,\n    E[TV(phat,theta)1_Ev]\n       <=(25/8)sqrt(K) v^(-1/2) min(1,2cv)^(3/4).\n\n重述有限分层和数值几何和\n\n    sum_(l>=0)2^(-l/2)min(1,a 2^l)^(3/4)<=10sqrt(a), a>0.\n\n于是经验项候选<= (125sqrt(2)/4)T；零计数项<=T、平滑项<=2T，总系数<48。无限延拓只用于数值和，不为随机栈增加免费信息。phat不在J=0定义。\n\n平滑及下述实现误差保持截断：对每个实数A>=0，\n\n    E min{1,A/(J+K)}<=Psi(cA)<=2sqrt(cA),             (TRUNC)\n    Psi(0)=0; Psi(x)=x(1+ln(1/x)) (0<x<1); Psi(x)=1 (x>=1).\n\n需保留A=0及实阈值x=A/t-K，x>0时{J<x}={J<ceil(x)}且ceil(x)<=A/t，x<=0为空事件，不直接向非整数阈值套整数UC。A=K用于平滑。\n\n## 3. 全合法精度与原Pi\n\n对输出为概率向量且全路径全query满足原接口I的共同有限F：\n\n    h>=h0(M)=max(4,ceil(log2M)+1), Q=2^h,\n    TV(F_h(x;s),p_s^+(x))<=78KM/[Q(n_s(x)+K)]+(K-1)/Q,\n    A_h=78KM/Q, g_h=(K-1)/Q,\n\n证明\n\n    sup E TV(F_h(Y_M),p^+_(Y_M))<=min(1,g_h+Psi(cA_h)),\n    sup E TV(F_h(Y_M),theta_(Y_M))\n      <=min(1,48T+g_h+Psi(cA_h))<=min(1,64T).        (L1-I)\n\n由SRC Fact fef8372728290b45，这适用于同一个实际Pi，直接包括最低合法h0。不得由高精度结果自动推到h0，也不声称各h输出或真实风险相同。以原h_N=ceil(log2(128(K+1)(M+3)^3))、e_N=(M+3)^(-2)，另有原Pi风险<=min(1,48T+e_N)。全部须给有限参数推导。\n\n## 4. 已接纳MM5的同目标比较\n\n令R_min(K,M)=inf_A sup_(theta,mu)E TV(A(X_1^(M+2)),theta_(Y_M))，A为所有共同随机全历史概率预测器，种子与源独立，不读隐藏参数或未来。仅使用MM5 Fact946d42d5bf502eb4已接纳范围得到下界，并结合本项新上界，目标合取为\n\n    2^-16 min(1,T)<=R_min(K,M)<=R_K^+(M)<=min(1,48T). (MATCH)\n\n只有本项正常接纳后才能称K,M联合统计率在绝对常数因子内匹配，或原add-one达到该minimax阶。不能称数值常数最优、存在同一源对所有算法/所有horizon同时困难、内部资源下界或所有Transformer资源最优。旧MM5构造不重证，保留其唯一原前驱a125供小K。\n\n0<tau<2^-16时任何共同全历史算法的统一风险<=tau，必要样本为M+1>=2^-32 K^5/tau²。原Pi无故障取M+1>=(64K^(5/2)/tau)²、h=h0即为充分配置。必要与充分为不同量词方向，不能相加或当作同一见证。\n\n## 5. 联合故障与完整费用的标准后续推论\n\n在SRC原master/V切口，使用015相同的准确故障实验：master为9K+1个canonical G_h字，最终银行W在{1,...,2Q}^K；D为相对当前post-master银行V^delta的总绝对整数编辑预算。核只读已观察历史/当前银行/公开量和独立种子，不读隐藏源或未来。好事件G可与历史/J及编辑相关，P(G^c)<=gamma；G上master逐坐标误差<=delta、||W-V^delta||_1<=D；G外仍合法canonical/正银行。令\n\n    A=M[K(78/Q+36delta)+D/Q].\n\n重述短的正向量归一化与无条件截断推导，证明原Pi\n\n    R_fault<=min(1,48T+g_h+Psi(cA)+gamma)\n           <=min(1,62T+12K^(5/2)sqrt(delta)+2K²sqrt(D/Q)+gamma).\n\n因此对0<tau<1，M+1>=(248K^(5/2)/tau)²、h=h0、delta<=tau²/(2304K^5)、整数D<=floor(Q tau²/(64K^4))、gamma<=tau/4为充分配置。J0、M1、零预算和只能零编辑的网格均保留。这是新统计率代入既有接口的标准综合，不另造常数节点，不扩展015二元切口下界。\n\n取M_tau=max(1,ceil((aK^(5/2)/tau)²)-1)，a=64或248，N=M_tau+2、n=N+1、ell=ceil(log2(N+K+2))、p=4h0+4ell+64。明确S_tau=K^5/tau²、Lambda_tau=1+lnK+ln(1/tau)，n=O(S_tau)、p=O(Lambda_tau)。同一个uncached/dense SRC配置保留depth O(Kp²)、width O(Kp)、word<=128p、dense参数bits O(K³p^5)、全部n个token点运算/QKV O(nK³p^6)、attention O(n²(K+p)p²)，以及完整input/query/endpoint、metadata/masks、holds/copy/clear、输出、offline generation/全格式写出和逐phase总peak。rolling内存不替代总peak；缓存、sparse、PURE须另用完整收费配置。物理注入器、历史重读或新纠错桥不免费。\n\n该标准成本代入只消去充分样本证书中的logK，不改变Pi程序或宣称同精确预算优势。strong direct及真正同神经预算比较仍需独立科学工作。\n\n## 6. 实际依赖与正常证据门槛\n\n上界预计只必需G/U a12539a93d9f1ee3的UC与SRC fef8372728290b45的实际接口/费用；MATCH实际使用MM5 946d42d5bf502eb4。有限耦合、Doob、区间矩母函数、有界差分、Holder、dyadic及截断推导均重述自足时，不新增014/015/RATE/K3前驱。它们可作写作来源；若实质依赖其引理则如实加入前驱，禁止隐藏依赖。所有旧Fact保持原scope。\n\n先做有界逆向核查，尤其L1最大函数的单符号振幅、均值与偏差相加、25/4常数和随机末行相关性。若失败则登记精确障碍，保持OPEN，不将辅助估计失败宣称为目标反例。完整证明需要独立审查；补充检查不替代接纳。所有标准方法不作新工具或首创主张。[Non-scientific operational metadata omitted.]\n","fact_id":"a53804d650803060","scope_bindings":[{"evidence_id":"fef1785395851e47b5ca0b719640449061718f4c670bfcd74c24cf0aec696c88","obligation_id":"e5eac888f467f9e19522d9755a04c518aea63e80192c0532f59b4d9dfecbde33","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]}}],"source_hash":"bc24d183f5299df636e67f0b439aadbcd4d79671b69c327ed7083ddfab857c6f"}]

Proof:
# T2-LATE-QUERY-MEMORY — complete proof v1

Target obligation: f228ec91da7ce41d27fc032fc7fe47f8c87d318b97e55f3d765824fd20d115f8.
Frozen contract: e6b7592e781948d00eb2a2effb80d8e3ef77e480f8d70f960286bc33faf730af.
This is the complete conjunction for the frozen 017 statement, including the finite sequential-bit baseline. Before normal gateway acceptance this document is an author proof, not an admitted Fact.

## 1. Experiment, claims, and exact dependencies

Let K>=2, M>=2, N=M+2. All histories are the original X_1,...,X_N from a fixed-in-experiment homogeneous second-order table theta and initial pair law mu, including zero edges. Set Y_i=(X_(i+1),X_(i+2)). The observed departure indices are exactly i=0,...,M-1, with successor X_(i+3). TV is one half of L1. All risks below are the original same-path actual mean TV against theta_(Y_M).

A cut algorithm consists of an encoder of X_1^M into a message I in a fixed alphabet of at most 2^s values and a decoder using only I, X_(M+1), X_(M+2), public parameters, and source-independent randomness. All history-dependent side information crossing the cut is part of I, including addresses, head positions, control states, stopping times, prefix endpoints, or copies. The algorithm and codebook are common to all sources. Let R_cut be the infimum over these algorithms of their supremum source risk. We use the frozen definitions for shared and private seeds; the elementary lower-bound argument even permits revealing all source-independent random seeds to both parties, if necessary to handle correlations between their randomizations. Such extra source-independent randomness cannot weaken a lower bound proved for the larger class.

For K>=12 put m=floor(K/4), b=floor(m/2), d=m^2 b. We prove

    R_cut(K,M,s) >= (1/96) 2^(-s/d).                      (1)

We then prove BITS, JOINT-NEC, and the exact all-K finite count baseline and costs. For 2<=K<12 only the count baseline and the MM5 sample necessity are asserted; d and MEM are not extended there.

Actual project predecessors are precisely:

1. Fact 946d42d5bf502eb4: the already admitted MM5 bound
   R_min(K,M)>=2^-16 min(1,K^(5/2)/sqrt(M+1)) for common randomized full-history predictors.
2. Fact a53804d650803060: the admitted original add-one bound
   R_K^+(M)<=min(1,48 K^(5/2)/sqrt(M+1)).

Their statement scopes and native evidence hashes were checked in source-checks-v1.json. Neither old proof is re-adjudicated. The clock's continuous family, initialization, cut property, volume proof, and all count-program arguments are proved here. The binary-label MM5 claim is not silently extended. No other project Fact is invoked. In particular this proof does not use a file-scoped PASS, 010, SRC costs, 014, or 015 as a premise.

## 2. A finite cyclic word enumerating all pairs

Use the directed graph whose vertices are the m clock letters C and which has one directed edge a->b for every ordered pair (a,b) in C^2, including loops. Every vertex has in-degree and out-degree m, and the graph is strongly connected.

Here is a finite Euler-circuit proof. Start at any vertex and follow unused outgoing edges until no such edge remains. At a nonstarting endpoint the used incoming count exceeds its used outgoing count by one. Equality of the total incoming and outgoing counts would then leave an unused outgoing edge; hence stopping is possible only at the start. Thus the trail is closed. Remove its edges; at every vertex the unused in- and out-degrees remain equal. If unused edges remain, some vertex of the current trail has an unused outgoing edge: otherwise no unused edge could leave the visited set, whereas a directed path from that set to a vertex incident to an unused edge would have a first such unused edge. Equivalently, in this complete graph a vertex outside the visited set can be reached by an as-yet unused edge from a visited vertex. Start another closed unused-edge trail at that vertex and splice it into the old one. Each splice uses at least one new edge. After at most m^2 edges have been used, the process terminates with an Euler circuit using every edge exactly once.

Write its successive vertices as c_0,c_1,...,c_L=c_0, where L=m^2. Extend subscripts modulo L. Then p_t=(c_t,c_(t+1)), 0<=t<L, are the distinct elements of C^2. The circuit visits 0, so a cyclic rotation makes c_5=0. Since m>=3, L>=9, the indices 0,...,6 used below cause no exceptional small-length collision. In particular p_0 and p_5,...,p_(L-1) are distinct, even if some individual clock letters repeat. The word and its rotation are public and independent of all source parameters.

## 3. Continuous homogeneous source, legal shifts, and phase support

Take disjoint sets of m letters C,U,V,W inside {0,...,K-1}, with 0 in C. The remaining K-4m letters are unused on the constructed path. Enumerate W as w_1,...,w_m. For every (a,b') in U x V and j=1,...,b choose an independent coordinate z_(a,b',j) in [-1/2,1/2]. Here b' denotes a V letter; the unprimed b still denotes floor(m/2). The whole parameter vector ranges over the cube H=[-1/2,1/2]^d, with no restrictions coupling its coordinates.

For s=(a,b') in U x V define q_z(.|s) by

    q_z(w_(2j-1)|s)=(1+z_(s,j))/m,
    q_z(w_(2j)|s)  =(1-z_(s,j))/m,

and, if m is odd, q_z(w_m|s)=1/m. All other probabilities in that row are zero. Each paired sum is 2/m, the possible leftover is 1/m, and all nonzero probabilities lie in [1/(2m),3/(2m)]. Thus every such row is a probability vector.

Define the whole second-order table theta_z as follows:

    theta_(p_0)             = Unif(U);
    theta_(c_1,a)           = Unif(V),                 a in U;
    theta_(a,b')            = q_z(.|(a,b')),           a in U, b' in V;
    theta_(b',w)            = delta_0,                b' in V, w in W;
    theta_(w,0)             = delta_(c_6),            w in W;
    theta_(p_t)             = delta_(c_(t+2)),        5<=t<L;
    every unassigned row    = delta_0.

These assignments are consistent. The row types are, respectively, C x C, C x U, U x V, V x W, W x C, and C x C. Disjoint alphabet groups separate all mixed types. Within C x C, distinctness of the p_t separates p_0 and all assigned later clock rows. The remaining C x C rows, all other mixed pairs, and pairs using leftover alphabet letters receive the default row only once. The default rule supplies legal normalized rows even for states never reached.

For any row (a,b') and drawn letter c, the pair transition is exactly (a,b')->(b',c). The special segment is consequently

    p_0=(c_0,c_1)
      -> (c_1,A) -> (A,B) -> (B,Z) -> (Z,0)
      -> (0,c_6)=p_5,

where the first two choices are uniform on U and V and the third has law q_z(.|(A,B)). This uses five departures, exactly the number of departures replaced in the clock. From p_5 the chain takes p_6,...,p_(L-1),p_0. Every such lap has length L regardless of A,B,Z,z.

More explicitly define the phase sets

    H_0={p_0}, H_1={c_1} x U, H_2=U x V,
    H_3=V x W, H_4=W x {0}, H_t={p_t} for 5<=t<L.

They are pairwise disjoint. Each transition from H_t stays in H_(t+1 mod L). Thus their union is a closed support for all z. No transition from this support invokes a default row. In particular phase 0 always means the one actual pair p_0; it is not a hidden extra state attached to a pair. The construction is a genuine homogeneous pair-shift chain and not a scheduled general finite-state chain.

For any fixed finite history x_1^N its exact probability under this table is

    mu(x_1,x_2) product_(i=0)^(M-1)
        theta_z,(x_(i+1),x_(i+2))(x_(i+3)).          (2)

This follows successively from the defining second-order transition law. We will use (2), not an assumption of conditional iid row samples, to prove the cut property.

## 4. Every remainder, the prefix cut, and the two fresh actual symbols

Write M=nL+r, 0<=r<L, and choose k in {0,...,L-1} congruent to 2-r modulo L. Choose the z-independent initial pair as in the frozen statement:

|k|initial pair law|
|---|---|
|0|delta_(p_0)|
|1|first letter c_1, second uniform U|
|2|independent uniform U and V|
|3|delta_(v_*,w_*) for fixed public v_* in V, w_* in W|
|4|delta_(w_*,0)|
|5,...,L-1|delta_(p_k)|

The chosen law is supported on H_k. Initial pairs need not arise as the end of an unobserved previous path. Induction on the transitions of Section 3 gives

    Y_i in H_((k+i) mod L) for every 0<=i<=M.       (3)

Since k+M-2 is divisible by L and M-2>=0, (3) proves

    Y_(M-2)=(X_(M-1),X_M)=p_0, with probability one. (4)

This includes the actual boundary M=2: then n=0,r=2,k=0, the cut prefix is just the initial p_0. For additional explicit coverage of all remainders:

- r=2 gives k=0 and M-2=nL.
- r=1 gives k=1. M>=2 forces n>=1, so M-2=nL-1 is nonnegative; the initial random U letter is part of the prefix, and the path completes the missing part of that lap before the final phase 0.
- r=0 gives k=2. Again n>=1. The initial random UV pair belongs to the prefix; M-2=nL-2 reaches phase 0 after its lap.
- 3<=r<=L-1 gives k=L+2-r, ranging over 3,...,L-1. Before any full extra laps, exactly r-2=L-k transitions reach p_0. Thus n=0 is covered here as well.
- In particular k=3 is r=L-1: the fixed initial W label in (v_*,w_*) is part of the allowed prefix, not a draw from an unknown row. k=4 is r=L-2 and has the same interpretation for (w_*,0). The other initial phases are deterministic clock pairs.

We do not remove any labels, prefix endpoint information, or other observations available before the cut. All of X_1^M, including any initial random U/V symbols and every occurrence or deterministic copy of an earlier label, may be read by the encoder.

Let H denote this full prefix. For every positive-probability value h of H, (4) fixes its last pair to p_0. The next row is Unif(U), and, after choosing A=a, the next row is theta_(c_1,a)=Unif(V). Applying (2) to just these two further departures gives, for every a in U and b' in V,

    P_z(X_(M+1)=a, X_(M+2)=b' | H=h)=1/m^2.        (5)

The two departure indices are i=M-2 and i=M-1, with successors X_(M+1) and X_(M+2), respectively. The actual query is Y_M=(A,B). Its departure and its unknown label successor X_(M+3) are not observed. This last distinction is essential.

Equation (5) proves that the actual pair is uniform on U x V and independent of the entire prefix for each fixed z. It also proves independence of the prefix together with all source-independent seeds and any message computed from that prefix and encoder seeds. For instance, condition on a fixed shared seed and integrate encoder-private randomness; (5) is unchanged. These are properties of this specific source family, not of general second-order chains. They hold for all M>=2 and all z, without any mixing or stationary-initialization premise.

## 5. Random decoders give one finite d-dimensional codebook per shared seed

Fix an arbitrary admissible cut algorithm with at most C0=2^s message values. Unused values may be padded by a fixed output rule. Use R for its shared seed to avoid confusion with the letter set U. First take encoder and decoder private randomness independent conditional on R. If a model permits correlated source-independent seeds, grant their joint value as additional shared randomness and condition on it instead; the argument below is valid even for that stronger class.

For fixed seed value u, message i and actual row t=(a,b') in U x V, let q_(i,u)(.|t) be the mean decoder output over its private randomness. This is a probability vector. It is independent of the hidden z, because the decoder is common and has only the specified inputs. Convexity of absolute value, coordinate by coordinate, yields

    E_decoder TV(output,theta_z,t) >= TV(q_(i,u)(.|t),theta_z,t). (6)

The assertion is pointwise in i,u,t; the probability that the encoder chooses i may still depend arbitrarily on z. No posterior assumption about the encoder is needed.

For every t,j define

    a_(i,u;t,j)=(m/2)
       [q_(i,u)(w_(2j-1)|t)-q_(i,u)(w_(2j)|t)],
    zhat_(i,u;t,j)=clip_[-1/2,1/2](a_(i,u;t,j)).

For any real a and z0 in [-1/2,1/2], clipping a to this interval cannot increase |a-z0|: outside the interval it moves toward every z0 in the interval, and inside it does nothing. The two true coordinates have difference 2 z_(t,j)/m. Therefore the triangle inequality gives

    (1/2)(|q_(2j-1)-theta_(2j-1)|+|q_(2j)-theta_(2j)|)
       >= (1/2)|(q_(2j-1)-q_(2j))-2z_(t,j)/m|
       >= (1/m)|zhat_(i,u;t,j)-z_(t,j)|.           (7)

Summing over disjoint label pairs in that row is legitimate. All unpaired or outside-W coordinates contribute nonnegative additional loss. Thus q need not be supported on W, and the argument covers arbitrary probability readouts.

Let pi_i(z,u) be the conditional probability that the encoder chooses message i. By (5), this probability is the same for every future actual row t. Applying (6), (7), and averaging the actual row with its real weight 1/m^2 gives the following lower bound on the original, unconditioned actual risk r_A(z):

    r_A(z)
      >= (1/m^3) E_R sum_i pi_i(z,R)
            sum_(t,j)|z_(t,j)-zhat_(i,R;t,j)|
      >= (1/m^3) E_R min_(1<=i<=C0)
            ||z-zhat_(i,R)||_1.                   (8)

For each fixed seed this is a single codebook with at most 2^s centers in H. It is not a separate selection of a message for each t. In the first line the same chosen message must answer every possible late row. Moving the minimum inside the row sum would instead permit choosing a message after seeing the query; that is not done. The second line even grants an oracle encoder knowing z and choosing its best whole center, which only decreases the lower bound and is consequently valid for the real finite-sample encoder.

## 6. Elementary L1 volume estimate and the uniform constant

Lebesgue measure on H has total mass 1. We give the needed volume and factorial estimates explicitly.

The nonnegative simplex {x in R^d: x_l>=0, sum_l x_l<=r} has volume r^d/d!. For d=1 this is its length r. Integrating the last coordinate t from 0 to r and using the induction formula in dimension d-1 gives integral_0^r (r-t)^(d-1)/(d-1)! dt = r^d/d!. An L1 ball is the union of its 2^d orthants with disjoint interiors. Therefore its volume in R^d is 2^d r^d/d!; intersecting with H can only reduce the volume. Translation of the center does not affect the full-ball volume.

For integer d>=1, monotonicity of ln x gives

    ln(d!)=sum_(j=1)^d ln j
       >= integral_1^d ln x dx
       =d ln d-d+1 >= d ln d-d.

Hence d! >= (d/e)^d. Also e=sum_(j>=0)1/j!<3: for j>=2, j!>=2^(j-1), with strict inequality once j>=3, so the sum of the j>=2 terms is strictly less than 1. These two estimates require no asymptotic formula.

Fix any one codebook of at most 2^s centers, and set

    rho=(d/8) 2^(-s/d)>0.

The measure inside distance at most rho of some center is bounded by the sum of the ball volumes:

    2^s 2^d rho^d/d!
       <= 2^s (2e rho/d)^d
       =(e/4)^d
       <(3/4)^d <=3/4.                            (9)

Here d=m^2 b>=1, including m=3,b=1,d=9. Boundary intersections and repeated centers only reduce the union volume. Outside these balls the nearest-center distance is at least rho, on a set of measure at least 1/4. Consequently

    integral_H min_i ||z-zhat_i||_1 dz
       >= rho/4 = (d/32)2^(-s/d).                 (10)

The strict slack in (9) is not required for the claimed weak inequality.

The function in (8) is measurable and between 0 and d, because all centers and z lie in H. Integrating (8) over z and exchanging the two nonnegative integrals is valid: the exchange holds first for simple nonnegative functions by finite sums, then for increasing simple approximations by monotone convergence. Equivalently, bounded Tonelli applies on the two probability spaces. Apply (10) separately for every fixed shared seed, obtaining

    integral_H r_A(z) dz
       >= d/(32m^3) 2^(-s/d)
       = b/(32m) 2^(-s/d)
       >= (1/96)2^(-s/d),                         (11)

because floor(m/2)>=m/3 for m>=3 (even m is immediate, and for odd m, (m-1)/2>=m/3 exactly when m>=3).

The uniform cube measure is a proof device, not a random choice of the source during an experiment. For any fixed algorithm, the supremum over fixed z is at least its average in (11). A fixed-source witness can also be chosen attaining the maximum: for each complete history the algorithm's output distribution, after averaging its source-independent seeds, is fixed independently of z; the probability of that history is a finite product of affine row probabilities, and its expected loss is continuous in the target vector. There are finitely many histories, so r_A(z) is continuous on the compact cube. This proves attainment, though the supremum inequality alone suffices. Thus one source theta_z and the one z-independent initialization mu chosen in Section 4 serve for the whole experiment. The selected source may depend on the algorithm and on public K,M,s, but not on realized seeds, samples, or the realized late row.

Finally take the infimum over all admissible algorithms. This proves (1), exactly MEM, for every K>=12, M>=2, integer s>=0. It does not require the finite prefix to identify z: its oracle relaxation already allows that advantage.

## 7. BITS, side channels, and the two independent necessary coordinates

Suppose a cut algorithm has supremum actual risk at most tau, where 0<tau<1/96. Inequality (1) gives 2^(-s/d)<=96tau, hence

    s >= d log2(1/(96tau)),

with ceiling on the right when expressed as an integer bit requirement. For K>=12,

    m=floor(K/4)>=K/4-1>=K/8,
    d=m^2 floor(m/2)>=m^3/3>=K^3/1536.             (12)

The middle comparison is valid already for K>=8. If a proposed interface additionally leaves a history-dependent side variable with at most D_side>=1 values, its entire joint message has at most 2^s D_side possibilities. Replacing the codebook size in (9) yields the same bound with s replaced by s+log2 D_side. This explains why omitted prefix endpoints, token states, RAM, addresses, and caches cannot be treated as free. Source-independent public objects and random seeds are conditioned upon in the argument; they do not increase the number of history-dependent centers for a fixed seed.

Every admissible cut algorithm can be simulated by a common full-history predictor: apply its encoder to the first M symbols, then its decoder to the resulting message and the last two symbols, using the same source-independent random seeds. This is a subclass inclusion, not an extra experiment. MM5's admitted scope therefore gives, for all K>=2,M>=2,s,

    R_cut(K,M,s)>=R_min(K,M)
       >=2^-16 min(1,T), T=K^(5/2)/sqrt(M+1).

Together with (1), for K>=12 this is exactly

    R_cut >= max{2^-16 min(1,T),(1/96)2^(-s/d)}.    (13)

The two terms are separate uniform lower bounds. They are not added, and the argument does not identify their witnesses. When 0<tau<2^-16, risk at most tau forces T<1 and 2^-16 T<=tau, which gives

    M+1>=2^-32 K^5/tau^2.                         (14)

Equations (12) and (14) concern storage capacity and sample count respectively. No arbitrary-decoder depth, width, internal word, or bitwork lower bound is inferred.

## 8. Exact all-count algorithm at the same causal cut

Now let K>=2, M>=2 without the four-group restriction. Set

    b_M=ceil(log2(M+1)), B_K=ceil(log2 K),
    s_count=K^3 b_M+2B_K.

Use the binary labels 0,...,K-1. Keep one b_M-bit nonnegative integer D_(a,b',c) for every triple, initially zero, and two B_K-bit registers for the last two symbols. While reading symbols sequentially, after the first two symbols each newly read X_t (3<=t<=N) causes exactly one increment of D_(X_(t-2),X_(t-1),X_t), followed by shifting the two-symbol registers. The scan implementation of the increment is specified in Section 10; it is not a random-access oracle.

Inductively, immediately after reading t>=2 symbols,

    D_(a,b',c)
       =sum_(i=0)^(t-3)1{(X_(i+1),X_(i+2),X_(i+3))=(a,b',c)}, (15)

where the sum is empty for t=2. The registers contain (X_(t-1),X_t). The total of all counters is t-2. Since t<=M+2, every count is at most M, representable because 2^b_M>=M+1.

At the prescribed cut t=M, the counters cover exactly i=0,...,M-3, namely M-2 departures, and the last two symbols are X_(M-1),X_M. For M=2 the counts are all zero. Complete the current scan, return heads and public loop indices to fixed positions, and erase all data-dependent scratch, temporary incoming symbols, equality flags, carries, and copies. No input prefix remains accessible. The surviving history-dependent configuration is precisely these K^3 counters and the two B_K-bit labels. Thus it takes at most

    (2^b_M)^(K^3) (2^B_K)^2=2^s_count

values, including unused binary encodings. Any public metadata and fixed zero scratch have only one value for these public parameters. In particular the retained prefix endpoint is included in the 2B_K term.

Reading X_(M+1) increments the triple with departure i=M-2; reading X_(M+2) increments the triple with departure i=M-1. The resulting counts equal the frozen C_(s,c) on all histories and the final pair registers equal Y_M. The decoder thus completes the original M departures using only the cut message and the two allowed true symbols; it never rereads X_1^M.

## 9. Ordered dyadic output, zero counts, and the 49T risk certificate

For legal integer h>=h0(M), let Q=2^h. Select the K counts of the final pair, sum them to J, and let H=J+K>0. Compute exact integer quotients

    t_c=floor(Q(C_(Y_M,c)+1)/H), 0<=c<K-1,
    t_(K-1)=Q-sum_(c=0)^(K-2)t_c,
    output_c=t_c/Q.                                (16)

There is no zero denominator, including J=0. The first K-1 values are nonnegative and their sum divided by Q is at most the corresponding sum of add-one probabilities, which is at most 1. The residual is therefore an integer in [0,Q]. The output is a probability vector on every alphabet history.

For c<K-1 let epsilon_c=p_c^+-t_c/Q, so 0<=epsilon_c<1/Q. The final output coordinate differs from p_(K-1)^+ by exactly sum_(c<K-1)epsilon_c in the opposite direction. Its L1 error is twice that sum. Consequently

    TV(output,p^+_(Y_M))=sum_(c<K-1)epsilon_c
       <=(K-1)/Q.                                  (17)

This deterministic statement makes no assumption on the source support. Fact a53804d650803060 and the triangle inequality imply

    sup_(theta,mu) E TV(output,theta_(Y_M))
       <=min{1,48T+(K-1)/Q}.                        (18)

Legality gives Q>=2M. Since M>=2, sqrt(M+1)<=2M, and therefore

    (K-1)/Q <= K/(2M) <= K/sqrt(M+1)
             <= K^(5/2)/sqrt(M+1)=T.

Thus (18) is at most min(1,49T), hence at most min(1,64T). This uses the admitted risk of the original add-one, not an assertion that the sequential program's output bits or true risk equal SRC-Pi's at that precision. The program is valid for zero edges, arbitrary initial laws, transient/reducible/periodic sources, and J=0, since (15)--(17) hold for every history.

## 10. A finite sequential-bit implementation without random access

This section gives an explicit bit-program construction and a conservative ledger. It is an existence proof; no literal instruction ledger, compiler, or hardware execution is claimed to have been run.

Use the ordinary sequential bit-machine model with a fixed finite number of tapes, bounded-symbol cells, finite control, and sequential tape heads. One active step reads/writes a bounded number of bits and moves each used head by at most one cell. There is no unit-cost arithmetic on arbitrarily large words and no random-address access. A bit register of length l is a delimited tape segment; a forward or backward sweep, copying, clearing, adding, comparing, or gated updating such a segment is charged O(l) elementary steps. Head movements and the return sweeps are part of that cost. Loop ends can be recognized by public delimiters, so a logarithmic-cost loop-counter update is not silently charged as O(1) per bit.

A fixed lexicographic count tape has K^3 blocks of b_M bits and fixed delimiters. Triple labels are generated by three public B_K-bit indices rather than stored per block or selected by a data address. The machine also has the two persistent symbol registers, an incoming-symbol register, a K-word selected-row/output tape, and arithmetic scratch. Set, explicitly,

    w=h+b_M+B_K+8.                                  (19)

All arithmetic data below fit within O(w) bits. The statement's asymptotic w is therefore realized without a hidden precision parameter.

Input acquisition and conversion. Read the N one-hot K-vectors in their original order, charging NK bit acquisitions (and, if a vector is buffered, its K bits and their clearing). A concrete conservative binary conversion scans all K positions; at public index a, for each of its B_K binary bits OR the product of that bit and the current input indicator into the label accumulator. This uses O(K B_K) active steps per input vector, including public-index updates, sweeps/copies and clearing. Exactly one indicator is one, so the resulting B_K bits encode that symbol. There is no assumption of a free one-hot-to-integer primitive. The public scan schedule has a fixed length for valid inputs. One may stream the vector or buffer one current vector; either fits the physical bound below.

Updating one triple. Store the three symbol labels to be compared on short tapes. Sweep the full count tape in lexicographic order. At every block compare all 3B_K index bits with those labels, in O(B_K) work, forming a one-bit equality flag e. Execute a complete b_M-bit ripple increment with initial carry e. For each count bit x, write x XOR carry and set the next carry to x AND carry. This costs O(b_M) including its sweep. If e=0 it preserves the block; if e=1 it increments it. Execute the full pass even when the carry has become zero. Advance the public triple indices, clear the equality/carry scratch, and continue. Exactly one block has e=1. At that stage its count is at most M-1, so it cannot overflow the b_M-bit format. Head return to the start costs O(K^3 b_M), already within the same scan bound. One departure costs

    O(K^3(b_M+B_K)).

Shift/copy the last-symbol registers and clear the incoming-symbol and comparison tapes in O(B_K) additional work. These costs are absorbed in the scan. There are exactly M departures. Public symbol-time counters of O(b_M) bits, when needed, can be fully updated in O(b_M) per symbol, which is absorbed as well. Their values at the cut depend only on public time M. All data-dependent control/scratch is erased before the cut and heads are returned to fixed public positions. This provides the cut normalization specified in Section 8; it does not leave a data-dependent head position as a side channel.

Final row extraction. After both late updates, perform another full lexicographic scan, compare each block's first two indices with the final pair, and copy the matching K counters, in label order, onto a sequential K-word row tape. This uses O(K^3(b_M+B_K)+K b_M), including all scans and rewinds. It is absorbed by the M scan budget since M>=2. Sum those K counters by ripple addition, form H=J+K, and form each numerator by adding one then appending h zero bits. These use O(Kw) work. The sum of counts is at most M, H<=M+K, and a numerator is at most (M+1)2^h; each fits the width (19). Intermediate twice-remainders and carries fit there too.

Full quotient, remainder, and residual. For each of the first K-1 numerators, implement binary long division. Starting with remainder zero, scan all numerator bits from most significant to least significant. At each step replace remainder by twice itself plus the incoming bit; compare to H by a complete word scan; subtract H if needed using a full gated borrow scan; write the resulting quotient bit. Rewind the word heads as necessary. The invariant for the processed numerator prefix P is P=H q+rem, 0<=rem<H. The update preserves it, because the pre-subtraction new remainder is less than 2H. This proves that the final quotient and remainder are exact, with quotient floor(numerator/H). There are O(w) bit iterations and O(w) work per iteration, hence O(w^2) per division, with O(w) scratch. Compute the sum of quotients and subtract from Q to obtain the last coordinate in O(Kw). The numerator Q itself and any residual equal to Q are represented using h+1 bits, not an overflowing h-bit word. Serialize all K dyadic numerators in that format, with public exponent h (or, if demanded, the full h+1-bit denominator), charging every output bit and every copy/clear. The output work O(Kw) is already paid.

All loops are finite and bounded by K,M,h, with standard finite-state transitions for bitwise XOR, AND, OR, carries and borrows. Delimited sweeps implement the word operations just described; the count bank is never accessed by a hidden random-address primitive. In particular we have specified what must be done to obtain, update, select, normalize and output the counts.

## 11. Online, physical, offline, and batch ledgers

Write P=K^3 b_M+K w+w. Below constants are absolute, independent of K,M,h and the data.

A direct sum of the preceding active-step costs, including initialization/clearing, is

    O(NK + N K B_K
      + M K^3(b_M+B_K)
      + K^3(b_M+B_K) + K w^2 + P).

The acquisition NK and the conversion N K B_K are both displayed; conversion was not charged at unit word cost. Since N=M+2<=2M for M>=2, N K B_K<=2M K^3 B_K. Since M>=2, b_M>=1, B_K>=1, and w>=1, the remaining initialization, final scan, copies and row buffer clear costs are also absorbed. Thus the claimed online bound is exactly valid:

    active online bitwork
      =O(NK+M K^3(b_M+B_K)+K w^2).                 (20)

There is no use of amortized hidden random access in this reduction.

The simultaneously live storage of the streaming implementation consists of the count tape and fixed delimiters O(K^3 b_M), the K selected/output words O(Kw), two persistent and one temporary symbol labels O(B_K), input conversion workspace at most O(K+B_K), arithmetic scratch O(w), public indices/time/width parameters and head descriptors O(w), and a constant finite-control microprogram. Because K<=K^3 b_M and B_K<=w, the total is

    simultaneously live physical bits =O(P)
       =O(K^3 b_M+K w+w).                           (21)

Logarithmic head-location descriptors, if encoded explicitly rather than implicit in the tape model, are O(log P)=O(w), so they do not alter (21). Their cut values are public fixed positions. At intermediate times they may be data-dependent; their reset is charged. The public values and zeroed scratch contribute to physical space (21) even though they do not increase the information alphabet of the cut. At the cut the only variable bits are exactly the counters and the two endpoint labels. One can also serialize that message sequentially to a fresh tape and erase the old copy for O(s_count) work and a constant-factor physical peak; both are within (20)--(21). No serialization, copy, or erasure is assumed free.

A concrete program/output representation for the offline account is a fixed finite-state microprogram plus binary public K,M,h and widths, delimiters and the initial zero-filled tapes of the sizes just listed. The lexicographic layout rule is fixed; it has no stored data-address table. An offline generator writes this representation by nested public-index loops. Even charging O(w) bit work per emitted bit for index updates and checks gives

    offline generation and initial-layout/file writes =O((P+1)(w+1)),
    offline simultaneously live bits                  =O(P+w),
    serialized program/parameters/layout length       =O(P+w).   (22)

If zero-filled runtime storage is allocated later rather than written to the program file, its O(P) initialization is still present in (20); (22) is the conservative representation that writes it. The mathematical microprogram description can be expanded mechanically into a finite bit machine by the specified carry/comparison/sweep routines; no externally supplied large-integer oracle or uncharged compiler stage is used. If a different expanded instruction-file format is requested, its actual expanded length and generation work must additionally be paid; it is not silently identified with the compact loop-program representation (22). The present existence baseline uses that declared compact representation. No literal expansion or measured ledger is being reported.

Physical peak is a phase total: during setup include the generator scratch, descriptors and written layout; during streaming include the count bank, current input/conversion, public control and scratch; during final extraction/division include the still-live bank, selected row, arithmetic scratch and accumulating output. If an offline image is retained while runtime tapes are instantiated, both are counted, still O(P) for this chosen format. In every phase the components are summed before maximizing. Nothing is replaced by the size of just the final row or a query register.

If the external input convention instead supplies the entire batch at once, its NK-bit one-hot buffer is a separate physical component. Acquisition and eventual clearing cost O(NK), and total peak becomes

    O(NK+P),

not just (21). To realize the information cut, the consumed prefix portion must be erased or made physically inaccessible before the encoder commits I. Unseen last-two-symbol cells remain inaccessible until their observation times; the decoder may access just those two symbols, as permitted, and not the erased prefix. Early acquisition is not early semantic access by the encoder. If a proposed batch interface exposes the future cells to the encoder or retains readable prefix cells at the cut, it is outside this cut model and these information lower bounds are not applied to it.

The active-bit model charges reading, writes, movement, explicit copies/holds/clears and public control. Persistence of a stationary tape cell is ordinary stored memory in this declared sequential model; we do not convert it into a claim that a shared neural network can propagate that value through its layers without charged holds. Neither tape bits nor the count registers are being identified with neural width. No attention layer or physical error-correction/injection apparatus is part of this baseline, and no such apparatus is included at zero cost.

## 12. Same-risk sufficient parameters, comparison, and boundaries

For 0<tau<1 choose

    M_tau=max{2,ceil((64K^(5/2)/tau)^2)-1},
    h=h0(M_tau), N=M_tau+2.

This has M_tau+1>=(64K^(5/2)/tau)^2. By (18) the count baseline has uniform actual risk at most tau. With S=K^5/tau^2 and Lambda=1+log2 K+log2(1/tau),

    N=O(S), b_(M_tau)=O(Lambda),
    h0(M_tau)=O(Lambda), w=O(Lambda),
    s_count=O(K^3 Lambda).                          (23)

These estimates follow immediately by taking logarithms of M_tau+1=O(S), with the constants 64 and the ceiling/max retained. For example b_M<=1+log2(M+1), B_K<=1+log2K, and h0<=4+1+log2M. A reusable substitution into the declared sequential implementation gives

    online active bitwork O(S K^3 Lambda + K Lambda^2),
    streaming simultaneous physical bits O(K^3 Lambda),
    batch peak O(S K + K^3 Lambda),
    offline work O(K^3 Lambda^2),                   (24)

together with the full accounting (20)--(22), not as an alternative cheaper execution model. All public setup, input and final output remain charged. These are sufficient bounds for this one baseline, not lower bounds on the computation of every decoder.

For K>=12, BITS instead requires s>=d log2(1/(96tau)) when tau<1/96, with d>=K^3/1536. The necessary and sufficient storage statements retain their log K and constant gaps. No all-parameter optimal storage assertion follows from them. Sample necessity (14), storage necessity (12), and the sufficient algorithm (23) are different quantified statements, not one simultaneous hard-source construction.

The proof treats s=0 (one center), arbitrarily large finite s, all M>=2 including a prefix with no departures, odd or even m, zero-count final rows, all legal h including h0, and the residual numerator Q. Extra alphabet letters have legal default rows in the lower-bound family and are allowed freely in the count baseline. The lower bound uses no general-source conditional-iid assertion and no independent test experiment.

The result constrains the total history-related information through this precise pre-query no-reread cut. A full-history method that learns the final pair and then scans the old history for that one row, such as the previously discussed 010 scan, does not satisfy this cut restriction; the present argument does not exclude it or borrow a result about its cost. Full-history strong direct algorithms, genuinely shared causal-batch neural budgets, general-K fault tightness, physical correction implementations, and resource optimality require separate work. The result is not a universal Transformer lower bound, not a single-query-token width lower bound, and not a completion of v10. Standard volume/encoding and finite-bit arithmetic methods are used without a novelty claim.
