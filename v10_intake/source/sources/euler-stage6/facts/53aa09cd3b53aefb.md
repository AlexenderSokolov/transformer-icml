---
fact_id: 53aa09cd3b53aefb
problem_id: icml-general-prediction
author: prover
predecessors: [a53804d650803060, 946d42d5bf502eb4, fef8372728290b45]
glossary_introduces: {}
external_refs: []
statement_chars: 4336
---

## statement
# DOT-STATIONARY-INITIALIZATION-PI（031）：Dot条件层及同一SRC-Pi平稳综合

这是独立nonroot来源接纳义务，尚未接纳。来源文本中的 ACCEPTED 标记和有限复核不自动构成独立科学接纳。采用inputs/source-dot-conditions-20261029-v2/的S001/S002/S003完整科学正文与真实闭包；原ZIP SHA256 cc8b3cf77d799e65d5cafd51d4738262c76a8c58756ffcf5b968d6a65ff1a188，SOURCE_MANIFEST.json绑定复制。此合取吸收完成成果及同一网络的标准组合，不重新发现条件统计支线；未来该支线仍归Dot。

## 1. 共同实验、源类和算法量词

所有整数K>=2、M>=1，N=M+2，Y_i=(X_(i+1),X_(i+2))。只观察完整X_1^(M+2)，departure i=0,...,M-1；目标为同轨迹theta_(Y_M)，TV=L1/2。每次实验theta为固定齐次二阶概率表，可含零边，pair链P_theta按(a,b)->(b,c)合法shift。sup可依公开参数选源；共同全历史概率预测器可用与源独立的种子，不读theta、mu、pi、隐藏混合标签、未来或辅助样本。

C_s,c=sum_(i=0)^(M-1)1{Y_i=s,X_(i+3)=c}，n_s=sum_c C_s,c，J=n_(Y_M)，p_s,c^+=(C_s,c+1)/(n_s+K)。设
s=K^(3/2)/sqrt(M+1)，t=K^(5/2)/sqrt(M+1)，
a=min(1,s)，g=min(1,t)，u_s=min(1,48s)，u_g=min(1,48t)。
此处a、g仅为031统计缩写，与028–030的clock字母组大小或内部精度无关。

平稳类为所有(theta,pi)满足pi P_theta=pi，初始化mu=pi；允许可约、周期、非唯一pi及pi零质量状态。R_stat=inf_A sup_(theta,pi:pi P_theta=pi) E_(theta,pi) TV(A(X),theta_(Y_M))；R_stat^+用固定p^+替代A。sup必须同时量化theta与pi，pi不交给算法。

对每个公开eta∈[0,1]，C_eta={(theta,mu):存在pi，pi P_theta=pi且TV(mu,pi)<=eta}。定义R_eta=inf_A sup_((theta,mu)∈C_eta) E TV(A(X),theta_(Y_M))；算法可依公开eta，R_eta^+用同一不依eta的p^+。先固定eta和共同算法再取源sup，不固定隐藏theta后允许算法知道其参数。

## 2. 平稳占用、截断及匹配（Dot-S001/S002）

全部平稳源、每个pair z及整数v>=1：
P(Y_M=z,n_z<v)<=min(pi(z),v/(M+1))，
P(J<v)<=min(1,K^2 v/(M+1))。
对所有实A>=0，
E min(1,A/(J+K))<=Psi(K^2 A/(M+1))<=2sqrt(K^2 A/(M+1))，
Psi(0)=0，Psi(x)=x(1+ln(1/x))于0<x<1，Psi(x)=1于x>=1。

完整有限参数结论为
a/180 <= R_stat <= R_stat^+ <= u_s。                 (STAT)

须给有限窗口charging及平稳块移位证明，含M=1、零质量行及v>M。平稳占用K^2不能由一般UC中错误交换sum/max得到。确定行/前缀L1最大估计可使用016；与随机末行通过无条件Holder和有限dyadic层连接，不条件于J或末行宣称样本iid。截断保留实阈值取整、A=0及J=0。

下界复用Dot完整checkerboard源及测试证明并自足写入本地正文：r=floor(K/2)，r对符号，sigma_(b,i,j)独立符号；x,c分别在第i,j对时theta_(x,b)(c)=(1+alpha sigma_(b,i,j) epsilon_x epsilon_c)/K，其余1/K；alpha=(1/10)min(1,s)。核行/列抵消、uniform pair平稳、全K包括2、3。给定actual末对的完整观察路径律必须用真实反向shift链Q((b,c),(a,b))=theta_(a,b)(c)核对，支付前两步及后续访问概率；不能丢历史或另加独立测试query。处理输出ties、随机种子及先验/末对条件概率，再取sup/inf。仅证明绝对常数因子内匹配，不称常数最优。

## 3. 初始TV邻域的有限插值（Dot-S003）

对全部K,M,eta：
max(a/180,2^-16 eta g) <= R_eta <= R_eta^+
 <= min(u_g,u_s+eta u_g)。                           (INIT)
特别令r_eta=max(a,eta g)，有
2^-16 r_eta <= R_eta <= R_eta^+ <= min(1,96r_eta)。

上界须以delta=(mu-pi)_+及mu<=pi+delta证明；一般TV近邻不被错误写成mu=(1-eta)pi+eta nu。下界仅选择合法污染子类mu=(1-eta)pi_theta+eta nu，利用损失对初始律线性、非负性及MM5，保持隐藏标签不可见；与STAT下界取max，不能把两个不同源的风险相加成同一见证。给有限链平稳律存在性，保留eta=0、1与可约/周期情形。

样本结论的cap属于本合取的标准推论，不另拆常数节点。对0<epsilon<1：
r_eta<=epsilon 当且仅当 M+1>=K^3/epsilon^2 且
[eta<=epsilon 或 M+1>=eta^2 K^5/epsilon^2]。
以epsilon=tau/96给p^+充分配置。若任意共同算法类风险<=tau且0<tau<1/180，则M+1>=K^3/(180^2 tau^2)；另仅在eta>0且tau<eta/65536时推出M+1>=eta^2 K^5/(65536^2 tau^2)。不能删除第二必要性阈值。

## 4. 同一个实际SRC-Pi的平稳组合及完整费用

严格使用SRC Fact fef8372728290b45的同一Pi_(K,N,h)，全部整数h>=h0=max(4,ceil(log2 M)+1)，Q=2^h，原全路径接口
TV(Pi(x;z),p_z^+(x))<=78KM/[Q(n_z+K)]+(K-1)/Q。
必须从已证平稳截断和真实J推出
R_Pi,stat(K,M,h)
 :=sup_(theta,pi:pi P_theta=pi) E_(theta,pi) TV(Pi(X;Y_M),theta_(Y_M))
 <=min(1,48s+(K-1)/Q+Psi(78K^3 M/[Q(M+1)]))
 <=min(1,64s)。                                     (PI-STAT)

Q>=2M，A=78KM/Q<=39K，平稳实现项<=2sqrt(39)s，最终输出项<=s，48+2sqrt(39)+1<64须明确核算。含所有合法h、零计数和M=1；不由高精度或一般源结果直接替换K指数。对0<tau<1，M+1>=(64K^(3/2)/tau)^2、h=h0给同一Pi平稳风险<=tau的充分配置。

统计分母M+1与实际n_tok=M+3位置严格区分。真实字长p=4h+4ell+64，ell=ceil(log2(M+K+4))。沿SRC的同一dense/uncached batch hybrid：六头、全部n_tok位置、QKV/mask/input/query/endpoint、full products/remainders/guards、holds/copy/clear、输出、offline完整格式及逐phase总peak均收费。保留SRC原完整构造上界，不创造新decoder、suffix或pooling端口、免费count table、cache或历史重读。此为同源标准统计组合，不推出同数值cap优势、最优work/width、所有Transformer资源下界或故障结论。未运行compiler、literal ledger或batch测量；[Non-scientific operational metadata omitted.]

## 5. 真实依赖、后续及接纳门槛

预计直接Fact前驱：016 a53804d650803060（确定前缀L1MAX及一般源u_g）、MM5 946d42d5bf502eb4（INIT一般源下界）、SRC fef8372728290b45（真实Pi/I及完整费用）。已有证明不重审；若实质另用Fact须如实登记。Dot-S001/S002/S003不以外部ACCEPTED作为前提，新增平稳占用、条件末对反向测试、初始化比较均自足入正文；源作者及复用位置明确。独立审查的科学对象是整个 STAT/INIT/PI-STAT 及上述有限辅助结论，不能只审查局部常数或编号。源包及已有复核仅作证明来源和诊断材料。

此处记录作者候选时的 OPEN/PROPOSED 状态。完整来源综合及准确范围仍需独立审查；后续状态以有日期的接纳证据为准。

S018原规则再生式与S019有限strip另待科学需要及真正来源闭包。其M<=K^4、beta<=1/2限制、S007非IID三步构造K>=6以及小K使用IID边界保留，不并入031。未来条件统计续研归原Dot，本地只接收完成结果与网络/资源/可靠性桥。[Non-scientific operational metadata omitted.]完成031亦不宣告v10母题解决。


## proof
Original contract and explicit scope for this proof:
{"contract_id":"e6b7592e781948d00eb2a2effb80d8e3ef77e480f8d70f960286bc33faf730af","definitions":"## A. 共同源、观察、算法及风险定义\n\n对每个整数 K>=2，A={0,...,K-1}，S=A²，D=K²。一个实验固定一个时间齐次二阶表 theta∈(Delta(A))^S，允许零坐标；初始对分布 mu∈Delta(S) 任意。令\n\n    Y_j=(X_(j+1),X_(j+2)),\n    P_theta((a,b),(b,c))=theta_(a,b)(c),\n    N>=3, M=N-2, E_N=Y_M,\n    n_s(M)=sum_(j=0)^(M-1)1{Y_j=s},\n    C_s,c(M)=sum_(j=0)^(M-1)1{Y_j=s,X_(j+3)=c},\n    p_s^+=(C_s+1)/(n_s+K).\n\n每次预测完整观察 X_1^N。最后一个计数后继是 X_N；Y_M 不是额外 departure。actual query 从已观察最后两符号取得；fixed-query 任务另有明确的公开 s。X_(N+1)、theta、mu、支持、闭类、平稳律、未来行栈及隐藏源标签不可见。外部 query 是同一历史下调用的查询参数，不额外赠送干净端点或统计量。获得和复制实际端点在实现中收费。\n\n共同算法族的程序和公开精度可以依赖 K,N,h，不能依赖未知 theta,mu 或其隐藏标签。统计根中的理想 p^+ 是分析变量；给定实现的计数、头输出等实际可见代码由来源实现义务确定，不能据理想表达式新增 readout 端口。比较中的任意全历史预测器可以用全部 X_1^N 和源独立随机种子，输出任意概率向量。具体 Pi 则遵守自己已声明的内部信息切口。\n\nTV(p,q)=1/2 sum_c|p_c-q_c|。对给定 family F，令 Z_N(s)=TV(F_(K,N,h)(X_1^N;s),theta_s)。严格区分：\n\n| 名称 | 定义 | 量词 |\n|---|---|---|\n| fixed row | E Z_N(s) | 固定公开 s |\n| all contexts | E max_(s∈S) Z_N(s)；另可问其 a.s. 极限 | 全 K² 行，不改成访问行 |\n| actual terminal | R_act=E Z_N(E_N) | 同一历史的末尾 query |\n| conditional terminal | E[Z_N(E_N)\\|E_N=s] | 仅当 p_N(s)=mu P^M(s)>0；零概率时未定义 |\n| empirical weighted | E sum_s(n_s/M)Z_N(s) | 同历史频率权重 |\n| other history weighted | E sum_s w_s(X_1^N)Z_N(s) | w 为观察历史可测 simplex；不自动有一致性 |\n\n逐源极限固定 K,theta,mu 后令 N→∞。统一均值是每个 N 的 sup_(theta,mu) R_act；取 supremum 时源可随 N 改选，但一个样本路径内部的核必须齐次。固定 K 的统一结论不是 K 随 N 变化的无条件结论，也不是 changing-source 的统一几乎处处结论。输出允许零坐标，损失仅 TV，本 contract 不把它解释为 positive-output KL。\n\n\n## 共同研究范围的约定\n\n接口I是一个程序性质的定义，不能作为所有算法已经满足的全局假设。条件统计根对任意满足I的共同有限族F证明蕴含式；具体Pi满足I及其完整成本须由SRC-Pi的正常独立来源义务支持，不能在证明SRC-Pi时先假定它。原第二阶段固定证明是可查来源，旧Fact编号不是新项目前驱。\n\n后继真实资源/可靠性命题可以在同一contract内建立独立义务，不必谎称它们是统计根的前提。数据观察及TV实验保持上述定义。每项具体实现须声明自己的内部代码、允许回读、输出格式、参数/字长、batch或streaming等执行方式；比较只在所声明的共同条件下成立。原Pi的finite-attention加pointwise batch hybrid、literal bit/ReLU模块的packed/scalar、sparse/dense选项分别核算，不将一项格式的便宜坐标拼入另一项。\n\n完整费用包括实际head和局部绑定、输入/query/端点取得、参数/零系数、物理字、复制/跨层保持/清除、mask/position、所有活动bank与metadata、online/offline工作和同时峰值。不能免费引入计数、normalizer、译码或生成器。新算术/扰动参数由各精确义务局部量化；改变共同数据律、可见信息或风险须建立新的明确数学范围。\n\n给定接口的条件定理、具体实现定理、训练可达性、必要资源及新颖性是不同主张。数学根只包含数学命题。行政完成程序不是数学前提；独立后续结论不改变已有定理的证明依赖。\n","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]},"statement":"# DOT-STATIONARY-INITIALIZATION-PI（031）：Dot条件层及同一SRC-Pi平稳综合\n\n这是独立nonroot来源接纳义务，尚未接纳。来源文本中的 ACCEPTED 标记和有限复核不自动构成独立科学接纳。采用inputs/source-dot-conditions-20261029-v2/的S001/S002/S003完整科学正文与真实闭包；原ZIP SHA256 cc8b3cf77d799e65d5cafd51d4738262c76a8c58756ffcf5b968d6a65ff1a188，SOURCE_MANIFEST.json绑定复制。此合取吸收完成成果及同一网络的标准组合，不重新发现条件统计支线；未来该支线仍归Dot。\n\n## 1. 共同实验、源类和算法量词\n\n所有整数K>=2、M>=1，N=M+2，Y_i=(X_(i+1),X_(i+2))。只观察完整X_1^(M+2)，departure i=0,...,M-1；目标为同轨迹theta_(Y_M)，TV=L1/2。每次实验theta为固定齐次二阶概率表，可含零边，pair链P_theta按(a,b)->(b,c)合法shift。sup可依公开参数选源；共同全历史概率预测器可用与源独立的种子，不读theta、mu、pi、隐藏混合标签、未来或辅助样本。\n\nC_s,c=sum_(i=0)^(M-1)1{Y_i=s,X_(i+3)=c}，n_s=sum_c C_s,c，J=n_(Y_M)，p_s,c^+=(C_s,c+1)/(n_s+K)。设\ns=K^(3/2)/sqrt(M+1)，t=K^(5/2)/sqrt(M+1)，\na=min(1,s)，g=min(1,t)，u_s=min(1,48s)，u_g=min(1,48t)。\n此处a、g仅为031统计缩写，与028–030的clock字母组大小或内部精度无关。\n\n平稳类为所有(theta,pi)满足pi P_theta=pi，初始化mu=pi；允许可约、周期、非唯一pi及pi零质量状态。R_stat=inf_A sup_(theta,pi:pi P_theta=pi) E_(theta,pi) TV(A(X),theta_(Y_M))；R_stat^+用固定p^+替代A。sup必须同时量化theta与pi，pi不交给算法。\n\n对每个公开eta∈[0,1]，C_eta={(theta,mu):存在pi，pi P_theta=pi且TV(mu,pi)<=eta}。定义R_eta=inf_A sup_((theta,mu)∈C_eta) E TV(A(X),theta_(Y_M))；算法可依公开eta，R_eta^+用同一不依eta的p^+。先固定eta和共同算法再取源sup，不固定隐藏theta后允许算法知道其参数。\n\n## 2. 平稳占用、截断及匹配（Dot-S001/S002）\n\n全部平稳源、每个pair z及整数v>=1：\nP(Y_M=z,n_z<v)<=min(pi(z),v/(M+1))，\nP(J<v)<=min(1,K^2 v/(M+1))。\n对所有实A>=0，\nE min(1,A/(J+K))<=Psi(K^2 A/(M+1))<=2sqrt(K^2 A/(M+1))，\nPsi(0)=0，Psi(x)=x(1+ln(1/x))于0<x<1，Psi(x)=1于x>=1。\n\n完整有限参数结论为\na/180 <= R_stat <= R_stat^+ <= u_s。                 (STAT)\n\n须给有限窗口charging及平稳块移位证明，含M=1、零质量行及v>M。平稳占用K^2不能由一般UC中错误交换sum/max得到。确定行/前缀L1最大估计可使用016；与随机末行通过无条件Holder和有限dyadic层连接，不条件于J或末行宣称样本iid。截断保留实阈值取整、A=0及J=0。\n\n下界复用Dot完整checkerboard源及测试证明并自足写入本地正文：r=floor(K/2)，r对符号，sigma_(b,i,j)独立符号；x,c分别在第i,j对时theta_(x,b)(c)=(1+alpha sigma_(b,i,j) epsilon_x epsilon_c)/K，其余1/K；alpha=(1/10)min(1,s)。核行/列抵消、uniform pair平稳、全K包括2、3。给定actual末对的完整观察路径律必须用真实反向shift链Q((b,c),(a,b))=theta_(a,b)(c)核对，支付前两步及后续访问概率；不能丢历史或另加独立测试query。处理输出ties、随机种子及先验/末对条件概率，再取sup/inf。仅证明绝对常数因子内匹配，不称常数最优。\n\n## 3. 初始TV邻域的有限插值（Dot-S003）\n\n对全部K,M,eta：\nmax(a/180,2^-16 eta g) <= R_eta <= R_eta^+\n <= min(u_g,u_s+eta u_g)。                           (INIT)\n特别令r_eta=max(a,eta g)，有\n2^-16 r_eta <= R_eta <= R_eta^+ <= min(1,96r_eta)。\n\n上界须以delta=(mu-pi)_+及mu<=pi+delta证明；一般TV近邻不被错误写成mu=(1-eta)pi+eta nu。下界仅选择合法污染子类mu=(1-eta)pi_theta+eta nu，利用损失对初始律线性、非负性及MM5，保持隐藏标签不可见；与STAT下界取max，不能把两个不同源的风险相加成同一见证。给有限链平稳律存在性，保留eta=0、1与可约/周期情形。\n\n样本结论的cap属于本合取的标准推论，不另拆常数节点。对0<epsilon<1：\nr_eta<=epsilon 当且仅当 M+1>=K^3/epsilon^2 且\n[eta<=epsilon 或 M+1>=eta^2 K^5/epsilon^2]。\n以epsilon=tau/96给p^+充分配置。若任意共同算法类风险<=tau且0<tau<1/180，则M+1>=K^3/(180^2 tau^2)；另仅在eta>0且tau<eta/65536时推出M+1>=eta^2 K^5/(65536^2 tau^2)。不能删除第二必要性阈值。\n\n## 4. 同一个实际SRC-Pi的平稳组合及完整费用\n\n严格使用SRC Fact fef8372728290b45的同一Pi_(K,N,h)，全部整数h>=h0=max(4,ceil(log2 M)+1)，Q=2^h，原全路径接口\nTV(Pi(x;z),p_z^+(x))<=78KM/[Q(n_z+K)]+(K-1)/Q。\n必须从已证平稳截断和真实J推出\nR_Pi,stat(K,M,h)\n :=sup_(theta,pi:pi P_theta=pi) E_(theta,pi) TV(Pi(X;Y_M),theta_(Y_M))\n <=min(1,48s+(K-1)/Q+Psi(78K^3 M/[Q(M+1)]))\n <=min(1,64s)。                                     (PI-STAT)\n\nQ>=2M，A=78KM/Q<=39K，平稳实现项<=2sqrt(39)s，最终输出项<=s，48+2sqrt(39)+1<64须明确核算。含所有合法h、零计数和M=1；不由高精度或一般源结果直接替换K指数。对0<tau<1，M+1>=(64K^(3/2)/tau)^2、h=h0给同一Pi平稳风险<=tau的充分配置。\n\n统计分母M+1与实际n_tok=M+3位置严格区分。真实字长p=4h+4ell+64，ell=ceil(log2(M+K+4))。沿SRC的同一dense/uncached batch hybrid：六头、全部n_tok位置、QKV/mask/input/query/endpoint、full products/remainders/guards、holds/copy/clear、输出、offline完整格式及逐phase总peak均收费。保留SRC原完整构造上界，不创造新decoder、suffix或pooling端口、免费count table、cache或历史重读。此为同源标准统计组合，不推出同数值cap优势、最优work/width、所有Transformer资源下界或故障结论。未运行compiler、literal ledger或batch测量；[Non-scientific operational metadata omitted.]\n\n## 5. 真实依赖、后续及接纳门槛\n\n预计直接Fact前驱：016 a53804d650803060（确定前缀L1MAX及一般源u_g）、MM5 946d42d5bf502eb4（INIT一般源下界）、SRC fef8372728290b45（真实Pi/I及完整费用）。已有证明不重审；若实质另用Fact须如实登记。Dot-S001/S002/S003不以外部ACCEPTED作为前提，新增平稳占用、条件末对反向测试、初始化比较均自足入正文；源作者及复用位置明确。独立审查的科学对象是整个 STAT/INIT/PI-STAT 及上述有限辅助结论，不能只审查局部常数或编号。源包及已有复核仅作证明来源和诊断材料。\n\n此处记录作者候选时的 OPEN/PROPOSED 状态。完整来源综合及准确范围仍需独立审查；后续状态以有日期的接纳证据为准。\n\nS018原规则再生式与S019有限strip另待科学需要及真正来源闭包。其M<=K^4、beta<=1/2限制、S007非IID三步构造K>=6以及小K使用IID边界保留，不并入031。未来条件统计续研归原Dot，本地只接收完成结果与网络/资源/可靠性桥。[Non-scientific operational metadata omitted.]完成031亦不宣告v10母题解决。\n"}

Admitted prerequisite interfaces (use only within the recorded scopes):
[{"exact_statement":"# RATE-L1-MAX：去除剩余 sqrt(log K) 的共同 actual TV 率候选及同风险配置\n\n本项是015完整接收后的独立科学后继。014、015及旧root的准确声明、接纳和依赖保持；本候选不是由它们的接纳自动得到，也不是任何旧结果的逆向前提。直接对前缀L1范数作有界差分是本次待核查的改动，不以相邻高矩参数优化替代。完成本项亦不宣告v10的资源与机制母题完成。\n\n## 1. 原完整实验与准确目标\n\n全部整数K>=2、M>=1，N=M+2，字母表{0,...,K-1}。theta为任意允许零边的齐次二阶转移表，mu为任意初始对律。每次实验内theta固定；sup可随K,M选源。观察完整X_1^(M+2)，Y_i=(X_(i+1),X_(i+2))，0<=i<=M。\n\n    C_s,a=sum_(i=0)^(M-1)1{Y_i=s,X_(i+3)=a},\n    n_s=sum_a C_s,a, J=n_(Y_M), p_s,a^+=(C_s,a+1)/(n_s+K),\n    T(K,M)=K^(5/2)/sqrt(M+1),\n    R_K^+(M)=sup_(theta,mu) E TV(p^+_(Y_M),theta_(Y_M)).\n\n待证结论：\n\n    R_K^+(M)<=min{1,48 T(K,M)}.                       (L1+)\n\n仍为同完整轨迹actual E[TV]，不是TV平方、fixed/all/conditional、独立测试查询或删尾平均。算法只获历史及公开参数，不获辅助行栈、隐藏theta/mu、访问参数或未来符号。所有退化行、周期/可约/暂态、J=0、小M及任意初始化均需覆盖。\n\n## 2. 直接L1最大集中的具体候选（全部需证明）\n\n有限辅助耦合为每个K²行提供2M个独立theta_s符号并顺序复现原M次departure。令S_s,j=sum_(l<=j)(e_(xi_s,l)-theta_s)。对确定整数1<=v<=M定义\n\n    F_s,v=max_(0<=j<=2v)||S_s,j||_1,\n    Z_v=max_s F_s,v.\n\n只对确定行/确定前缀使用iid。目标链：\n\n    E F_s,v <= sqrt(8Kv),\n    改变一个栈符号使F_s,v至多改变2,\n    P(F_s,v-E F_s,v>t)<=exp(-t²/(4v)), t>=0,\n    ||Z_v||_4 <= sqrt(8Kv)+sqrt(8v ln K)+32^(1/4)sqrt(v)\n              <= (25/4)sqrt(Kv).                    (L1MAX)\n\n均值可用L1/L2比较及有限Doob L2；集中直接作用于整个L1前缀最大值，其坐标敏感度2与K无关。请给有界差分的条件区间推导及尾积分。K²行union后以a=sqrt(8v lnK)平移，剩余正部四次矩应<=32v²；行最大值之间不要求独立。不得将sqrt(K)再次乘在全部集中误差上。\n\n最后常数可用lnK/K<=1/e<3/8、K>=2，从而系数至多sqrt(8)+sqrt(3)+2^(3/4)<25/4；所有常数比较须明确可审。该吸收利用的是sqrt(K)均值和sqrt(logK)偏差的相加，不声称偏差本身没有logK。\n\n在E_v={v<=J<2v}上逐路径TV(phat_(Y_M),theta_(Y_M))<=Z_v/(2v)。然后仅用无条件Holder及G/U整数UC：\n\n    c=K^4/(M+1), P(J<w)<=min(1,cw), 整数w>=1,\n    E[TV(phat,theta)1_Ev]\n       <=(25/8)sqrt(K) v^(-1/2) min(1,2cv)^(3/4).\n\n重述有限分层和数值几何和\n\n    sum_(l>=0)2^(-l/2)min(1,a 2^l)^(3/4)<=10sqrt(a), a>0.\n\n于是经验项候选<= (125sqrt(2)/4)T；零计数项<=T、平滑项<=2T，总系数<48。无限延拓只用于数值和，不为随机栈增加免费信息。phat不在J=0定义。\n\n平滑及下述实现误差保持截断：对每个实数A>=0，\n\n    E min{1,A/(J+K)}<=Psi(cA)<=2sqrt(cA),             (TRUNC)\n    Psi(0)=0; Psi(x)=x(1+ln(1/x)) (0<x<1); Psi(x)=1 (x>=1).\n\n需保留A=0及实阈值x=A/t-K，x>0时{J<x}={J<ceil(x)}且ceil(x)<=A/t，x<=0为空事件，不直接向非整数阈值套整数UC。A=K用于平滑。\n\n## 3. 全合法精度与原Pi\n\n对输出为概率向量且全路径全query满足原接口I的共同有限F：\n\n    h>=h0(M)=max(4,ceil(log2M)+1), Q=2^h,\n    TV(F_h(x;s),p_s^+(x))<=78KM/[Q(n_s(x)+K)]+(K-1)/Q,\n    A_h=78KM/Q, g_h=(K-1)/Q,\n\n证明\n\n    sup E TV(F_h(Y_M),p^+_(Y_M))<=min(1,g_h+Psi(cA_h)),\n    sup E TV(F_h(Y_M),theta_(Y_M))\n      <=min(1,48T+g_h+Psi(cA_h))<=min(1,64T).        (L1-I)\n\n由SRC Fact fef8372728290b45，这适用于同一个实际Pi，直接包括最低合法h0。不得由高精度结果自动推到h0，也不声称各h输出或真实风险相同。以原h_N=ceil(log2(128(K+1)(M+3)^3))、e_N=(M+3)^(-2)，另有原Pi风险<=min(1,48T+e_N)。全部须给有限参数推导。\n\n## 4. 已接纳MM5的同目标比较\n\n令R_min(K,M)=inf_A sup_(theta,mu)E TV(A(X_1^(M+2)),theta_(Y_M))，A为所有共同随机全历史概率预测器，种子与源独立，不读隐藏参数或未来。仅使用MM5 Fact946d42d5bf502eb4已接纳范围得到下界，并结合本项新上界，目标合取为\n\n    2^-16 min(1,T)<=R_min(K,M)<=R_K^+(M)<=min(1,48T). (MATCH)\n\n只有本项正常接纳后才能称K,M联合统计率在绝对常数因子内匹配，或原add-one达到该minimax阶。不能称数值常数最优、存在同一源对所有算法/所有horizon同时困难、内部资源下界或所有Transformer资源最优。旧MM5构造不重证，保留其唯一原前驱a125供小K。\n\n0<tau<2^-16时任何共同全历史算法的统一风险<=tau，必要样本为M+1>=2^-32 K^5/tau²。原Pi无故障取M+1>=(64K^(5/2)/tau)²、h=h0即为充分配置。必要与充分为不同量词方向，不能相加或当作同一见证。\n\n## 5. 联合故障与完整费用的标准后续推论\n\n在SRC原master/V切口，使用015相同的准确故障实验：master为9K+1个canonical G_h字，最终银行W在{1,...,2Q}^K；D为相对当前post-master银行V^delta的总绝对整数编辑预算。核只读已观察历史/当前银行/公开量和独立种子，不读隐藏源或未来。好事件G可与历史/J及编辑相关，P(G^c)<=gamma；G上master逐坐标误差<=delta、||W-V^delta||_1<=D；G外仍合法canonical/正银行。令\n\n    A=M[K(78/Q+36delta)+D/Q].\n\n重述短的正向量归一化与无条件截断推导，证明原Pi\n\n    R_fault<=min(1,48T+g_h+Psi(cA)+gamma)\n           <=min(1,62T+12K^(5/2)sqrt(delta)+2K²sqrt(D/Q)+gamma).\n\n因此对0<tau<1，M+1>=(248K^(5/2)/tau)²、h=h0、delta<=tau²/(2304K^5)、整数D<=floor(Q tau²/(64K^4))、gamma<=tau/4为充分配置。J0、M1、零预算和只能零编辑的网格均保留。这是新统计率代入既有接口的标准综合，不另造常数节点，不扩展015二元切口下界。\n\n取M_tau=max(1,ceil((aK^(5/2)/tau)²)-1)，a=64或248，N=M_tau+2、n=N+1、ell=ceil(log2(N+K+2))、p=4h0+4ell+64。明确S_tau=K^5/tau²、Lambda_tau=1+lnK+ln(1/tau)，n=O(S_tau)、p=O(Lambda_tau)。同一个uncached/dense SRC配置保留depth O(Kp²)、width O(Kp)、word<=128p、dense参数bits O(K³p^5)、全部n个token点运算/QKV O(nK³p^6)、attention O(n²(K+p)p²)，以及完整input/query/endpoint、metadata/masks、holds/copy/clear、输出、offline generation/全格式写出和逐phase总peak。rolling内存不替代总peak；缓存、sparse、PURE须另用完整收费配置。物理注入器、历史重读或新纠错桥不免费。\n\n该标准成本代入只消去充分样本证书中的logK，不改变Pi程序或宣称同精确预算优势。strong direct及真正同神经预算比较仍需独立科学工作。\n\n## 6. 实际依赖与正常证据门槛\n\n上界预计只必需G/U a12539a93d9f1ee3的UC与SRC fef8372728290b45的实际接口/费用；MATCH实际使用MM5 946d42d5bf502eb4。有限耦合、Doob、区间矩母函数、有界差分、Holder、dyadic及截断推导均重述自足时，不新增014/015/RATE/K3前驱。它们可作写作来源；若实质依赖其引理则如实加入前驱，禁止隐藏依赖。所有旧Fact保持原scope。\n\n先做有界逆向核查，尤其L1最大函数的单符号振幅、均值与偏差相加、25/4常数和随机末行相关性。若失败则登记精确障碍，保持OPEN，不将辅助估计失败宣称为目标反例。完整证明需要独立审查；补充检查不替代接纳。所有标准方法不作新工具或首创主张。[Non-scientific operational metadata omitted.]\n","fact_id":"a53804d650803060","scope_bindings":[{"evidence_id":"fef1785395851e47b5ca0b719640449061718f4c670bfcd74c24cf0aec696c88","obligation_id":"e5eac888f467f9e19522d9755a04c518aea63e80192c0532f59b4d9dfecbde33","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]}}],"source_hash":"bc24d183f5299df636e67f0b439aadbcd4d79671b69c327ed7083ddfab857c6f"},{"exact_statement":"# RATE-K5-MINIMAX：周期稀疏观测下的共同算法 actual TV 下界候选\n\n这是独立的新候选，不是已接纳结果，也不从原始add-one的确定后继反例直接推出。原G/U、SRC、RATE、K3、K-LOW及RATE-K-MINIMAX的接纳与依赖不变；RATE-K-SHARP-ADDONE的REFUTE+证明及网关独立继续。本义务失败不影响上述事项，完成亦不宣告v10结束。\n\n对每个整数K>=2、M>=1，N=M+2，字母表{0,...,K-1}。theta为任意允许零边的齐次二阶转移表，mu为任意初始对律；每个实验内theta固定。令Y_i=(X_(i+1),X_(i+2))，观察完整X_1^(M+2)，实际目标为theta_(Y_M)。共同全历史概率预测器A可依公开K,M选取，可使用与源独立的随机种子，不可读取隐藏theta、mu或未来符号。定义\n\n    R_min(K,M)=inf_A sup_(theta,mu) E TV(A(X_1^(M+2)),theta_(Y_M)).\n\n待证明的完整有限参数结论为\n\n    R_min(K,M)>=2^(-16) min{1,sqrt(K^5/(M+1))}.       (MM5)\n\n这里是原同轨迹actual的E[TV]，不是E[TV²]、KL、fixed/all/conditional风险或另加独立测试实验。sup可随K,M及算法选择源；不声称同一源对全部算法或全部horizon同时达到下界。\n\n## 候选合法源族\n\nK>=12时取m=floor(K/4)>=3、L=m²、b=floor(m/2)。取四个互不相交的字母组C,U,V,W，各有m个字母，C含字母0；其余字母不被访问。\n\n取C上的循环字c_0,...,c_(L-1)，使p_t=(c_t,c_(t+1))枚举全部C² pair且各出现一次，按模L延拓，旋转令c_5=0。需给出这种循环字的有限存在性证明。\n\n对每个(u,v)∈U×V、j=1,...,b引入未知sigma_(u,v,j)∈{-1,+1}。公开0<alpha<=1/2，设\n\n    theta_(u,v)(w_(2j-1))=(1+alpha sigma_(u,v,j))/m,\n    theta_(u,v)(w_(2j))  =(1-alpha sigma_(u,v,j))/m.\n\n奇数m时剩余W字母概率1/m，W外为0。其余行定义为\n\n    theta_p0=Unif(U),\n    theta_(c_1,u)=Unif(V)                      (u∈U),\n    theta_(v,w)=delta_0                       (v∈V,w∈W),\n    theta_(w,0)=delta_(c_6)                   (w∈W),\n    theta_p_t=delta_(c_(t+2))                 (5<=t<L),\n    其余未指定行=delta_0。\n\n需检查所有赋值无冲突、概率归一化和合法shift。预期每圈以五步等长拼接\n\n    p0 -> (c_1,A) -> (A,B) -> (B,Z) -> (Z,0) -> p5=(0,c_6)\n\n替代clock前五步，A∼Unif(U)、B∼Unif(V)，Z条件律为theta_(A,B)，之后沿clock返回p0。圈长L不依任何随机选择或sigma；完整轨迹除观测到的Z外不应泄露额外sigma信息。这一点必须从实际路径律证明，不能把额外clock状态视为免费删除的数据。\n\n## 全余数初始化及完整观察实验\n\n写M=nL+d，0<=d<L，取起始相位k=(2-d) mod L，使实际末对位于UV查询相位2。以下初始化均不得依sigma：\n\n- k=0：mu=delta_p0；\n- k=1：mu=delta_(c_1)⊗Unif(U)；\n- k=2：mu=Unif(U)⊗Unif(V)；\n- k=3：mu=delta_(v_*)⊗delta_(w_*)；\n- k=4：mu=delta_(w_*)⊗delta_0；\n- 5<=k<L：mu=delta_p_k。\n\nv_*∈V、w_*∈W固定公开。初始pair本身不要求由更早未观测历史生成。不同M可选择不同mu，实验内仍使用同一个齐次theta。\n\n需严格证明：完整已观察历史与n=floor(M/L)个iid训练block(A_i,B_i,Z_i)，加上一个与全部训练block独立的均匀actual末对(A_(n+1),B_(n+1))，以及无sigma信息的公开前缀/clock填充等价。k=1,2中的初始随机字母应计入首个训练block或最终末对，不能遗漏信息；k=3,4中的固定前缀不能包含未计的标签样本。覆盖所有余数、n=0及全部departure索引，不把一般源的条件样本称为iid。\n\n## 测试下界、常数与输出范围\n\n候选alpha=min{1/2,(1/8)sqrt(m³/(n+1))}。相邻sigma仅翻转一个UV行的一个标签对，预期完整观察KL至多8n alpha²/m³<=1/8。实际末对和clock前缀必须纳入路径律验证。对任意随机预测器用该标签对的坐标顺序作测试，处理ties、种子、实际末对条件律及均匀row权重；目标先得\n\n    R_min(K,M)>=(1/64) min{1,sqrt(m³/(floor(M/m²)+1))}.\n\n须证明完整实验而非丢失信息后的实验满足此式。随后以m>=K/8及有限参数分情况比较，推出保守的(MM5)。2<=K<=11可使用当前项目G/U Fact a12539a93d9f1ee3的共同算法iid actual下界1/(16sqrt(M+2))，必须明确有限常数比较。高K源族及测试论证应自足；唯一预期必需Fact前驱为a12539a93d9f1ee3。既有RATE-K-MINIMAX的证明可作为写作来源，不能未经说明扩张其已接纳scope。\n\n若(MM5)成立，统一actual均值风险tau满足0<tau<2^-16的任何共同算法必须有\n\n    M+1>=2^-32 K^5/tau²。\n\n这仅为样本必要性；不推出内部位数、深宽、算术工作、资源最优性。与已接纳K³/sqrt(M+1) upper比较仍有K指数差距，不称sharp匹配。未知标签族是新增的研究内容，原确定delta_0族并未自动提供此结论。\n\n首先做有界反向核查；若发现相位、信息或常数缺口，登记精确障碍并保持OPEN。只有完整自足证明和正常独立网关才能接纳。不重复提交原SHARP+否定构造，不重新审查已完成root。周期稀疏访问构造、条件L1估计及两点测试不作新工具或首创宣称。","fact_id":"946d42d5bf502eb4","scope_bindings":[{"evidence_id":"aa23c442ca1006c6ac0b12379f64a0fa500fbbd6a2e41c798b7a4de3952baa82","obligation_id":"3883ea68e83601751cd4e4ff1500d552ac6e412c158b39a9912f6e1de55283dd","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]}}],"source_hash":"fe18f4a413fef5da14c5f361aef47a8c5addceac1a3a58d73366ad20f16d8e93"},{"exact_statement":"# SRC-Pi：原有限因果程序的全路径实现、银行接口与完整费用\n\n对每个整数 K>=2、N>=3，令 M=N-2、n=N+1。对每个整数 h>=max(4,ceil(log2 M)+1)，令 Q=2^h、ell=ceil(log2(N+K+2))、p=4h+4ell+64。字母表 A={0,...,K-1}。对任意完整已观察历史 x_1^N 和 query s=(a,b)，定义\n\n    C_s,c=sum_(t=3)^N 1{(x_(t-2),x_(t-1),x_t)=(a,b,c)},\n    n_s=sum_c C_s,c, p_s,c^+=(C_s,c+1)/(n_s+K).\n\n存在下述同一个共同确定有限程序族 Pi_(K,N,h)，参数、固定循环、布局、掩码和常数仅依赖公开 K,N,h；其固定构造由本项目 inputs/source-v10/inputs/general-assumptions-20261027/stage2/ 下 C1-proof-v1.md §§1–7、finiteN-reliability-proof-v1.md §§4–6 和 root-proof-v1.md §5 指定。以下断言需由确定性构造证明支持，I 是待证结论。旧来源的正性、平稳初始化和旧 Fact 身份均不作前提。\n\n## S1. 实际因果前端与有限求值\n\n主实现为有限整数求值的因果 attention 加逐 token Boolean/ReLU 点运算的 batch hybrid。输入仅为已观察历史、声明 query/mode 和公开 metadata；合成位置 q=N+1 的 token 为零，不含未来符号。两个已付费 singleton copying heads 产生前两步符号，并在 q 保留实际端点 (x_(N-1),x_N)，供外部 query 与 actual query 两种模式使用。外部 s 不替换实际端点修正。\n\n另有四个统计 heads P1、P2、T、0。理想比较对象的 Q/K/V 为：P1 的 Q=((ln2)A,(ln2)B)、K=(lag2,lag1)、V=(token,lag2)；P2 将第二段 ln2 换为 ln3；T 的 Q=(ln2)B、K=lag2、V=(lag1,F)；0 的 Q=K=0、V=(lag2,lag1,F,z)。A,B 为 query one-hot，z_t=1{t=3}，F_t=z_t lag1_t；q 的有效 keys 为 3,...,N，其余行使用声明的因果 prefix/fallback。理想输出依次为 (q1,v1)、(q2,v2)、(hvec,h0)、(alpha,nu,f,rho)，共 9K+1 标量。值为 query 无关的局部 bits。\n\n实际程序以有限有理 log 生成、定长整数指数求值、精确累加和正整数除法产生闭 h-grid G_h={j/Q:0<=j<=Q} 上的标量；不调用实数 log/exp/floor oracle。每一返回 head 标量与其上述理想值相差至多 2/Q。包含 1 的 G_h 用 h+1 位无符号分子。连续 ReLU 不被声称在实区间上实现 floor；其 bit extraction 只作用于声明有限网格。\n\n四个统计 head 后不再有读取原始历史的 decoder 端口或免费 count table；计数 C 仅为数学比较对象。源参数 theta、mu、支持、平稳律和访问控制参数均不进入程序。\n\n## S2. 正确逐路径读出、guards 与接口 I\n\n记 c_s,c=C_s,c/M、rho=1/M、u_ij=n_ij/M，alpha_i=sum_j u_ij、nu_j=sum_i u_ij，J_c=1{实际端点=(b,c)}。理想读出为\n\n    dT=1+alpha_b,\n    initial_bc=dT h0_c-f_c,\n    g_bc=dT hvec_c-nu_c+rho J_c-initial_bc,\n    U_k=v_k,a, lambda_1=1,lambda_2=2,\n    d_k=(1+lambda_k nu_b)/(1-U_k/2),\n    c_s,c=d2 q2_c-d1 q1_c-g_bc.\n\n这些恒等式对每条有限路径成立，包含 M=1、n_s=0，以及任何特定源下零概率的历史。实际点运算保留完整整数乘积、除法余数和 guard fractional bit；加减和声明的除二精确，所需乘除截断绝对误差至多 1/Q。head clipping 后 1-U_k/2∈[1/2,1]，d1∈[1,4]、d2∈[1,6]、dT∈[1,2]，有符号中间量容纳于来源指定的 [-16,16] 安全盒。\n\n令 a_c 为恢复 c_s,c 后截入 [0,1] 的 h-grid 值，令\n\n    r0=2^(-ceil(log2 M)-1), r=max(hat rho,r0),\n    x_c=a_c+r, V_c=Q x_c, T=sum_c V_c.\n\n则 x_c∈(0,2]，V_c∈{1,...,2Q}，T>0，并且\n\n    |a_c-C_s,c/M|<=76/Q,\n    |x_c-(C_s,c+1)/M|<=78/Q.\n\n最终输出按原有序 simplex 格式：c=0,...,K-2 的分子 m_c=floor(Q V_c/T)，m_(K-1)=Q-sum_(c<K-1)m_c，随后已付费 dyadic decode。其坐标非负且和为一，允许非末坐标为零，且所有路径、所有 query 同时满足\n\n    TV(Pi_(K,N,h)(x_1^N;s),p_s^+(x_1^N))\n      <=78KM/[Q(n_s+K)]+(K-1)/Q.                 (I)\n\n程序在上述全域合法；不同源规律只改变路径概率，不改变给定输入的程序及其费用。\n\n## S3. 后继确实使用的 master 与正权重银行接口\n\n9K+1 个 head 坐标各有一个 post-quantization master word，在任何 readout fanout/residual 复制之前定位切口。所有后继副本都来自该 master；query、端点及 flag BITs 在此实验中精确，统计标量 h0、f、rho 包含在可替换银行内。有限 evaluator 的干净 numerator、denominator、指数、余数及不用的历史投影在切口开放前按声明生命周期擦除或释放；历史存储及其处理仍收费。这里声明的是指定访问规则下的实际程序接口，不是对任意能重读历史算法的信息论限制。\n\n若每个 master 被任意相关的 G_h 标量替换，坐标偏差至多 delta>=0，原 downstream 运算仍合法，并有\n\n    |a_c-C_s,c/M|<=76/Q+35delta,\n    |x_c-(C_s,c+1)/M|<=78/Q+36delta,\n    TV(Pi^delta_s,p_s^+)<=KM(78/Q+36delta)/(n_s+K)+(K-1)/Q.\n\n这些是有限路径上的确定性接口，不要求误差独立，不涵盖改变 query/endpoint bits 或额外算术故障。\n\n最后正整数 V 银行的切口在全部 V_c 生成后、任何最终求和与 quotient 前。可将 V 替换为 W∈{1,...,2Q}^K；原 decoder 只从替换后的 W 重算 U=sum W 和上述 ordered floor/residual 输出，不保留干净 T 或 quotient。比较向量 V*_c=Q(C_s,c+1)/M 不是程序输入，且无需为整数；上述坐标界等价于 |V_c-V*_c|<=78+36Q delta。该定位与生命周期可在原声明成本上界内实现；若另外实现物理注入器、快照设备或新 normalizer 的 bridge，其硬件和程序费用单列，不在 nominal Pi 的免费能力中。\n\n## S4. 完整构造费用及表示约定\n\n以下是固定构造的统一上界，常数与 K,N,h 无关；采用来源最终修正后的 batch hybrid 计费。全部 n 个 token 的点运算计费，数学上所有 query 的正确性不意味着一次运行免费输出全部 K² 行。\n\n| 坐标 | 上界或精确结构 |\n|---|---|\n| neural depth / width | O(Kp²) / O(Kp) |\n| total heads / max layer heads；max QK dimension；score cap | 6 / 4；2K；2 |\n| 单 coefficient 与 arithmetic word | 至多 128p bits，含完整乘积、余数与 guards |\n| dense coefficient slots / parameter bits | O(K³p⁴) / O(K³p⁵)，零项和 bias 收费 |\n| active gates/projections；identity holds | O(Kp²+K²)；O(K²p³) |\n| sparse program / coefficients / addresses / holds | 共 O(K²p⁴) bits |\n| masks / positions | O(n²+n log(n+1)) bits |\n| observed input | O(NK) one-hot bits，或另付 binary acquisition/转换 |\n| rolling working arrays | O(nKp²) bits，不含已存参数、input、masks |\n| uncached finite attention bitwork | O(n²(K+p)p²) |\n| equally cached attention bitwork | O(n²Kp²)，cache 生成、存储、selector 另付 |\n| dense pointwise / QKV bitwork | O(nK³p⁶) |\n| finite rational log generation / scratch | O(p³ log²(p+1)) / O(p log(p+1)) |\n| finite arithmetic evaluator code | 保守 O(p⁴) bits |\n\n五个 full-score caches 对应 0,L2,2L2,L3,L2+L3，分别有限求值；最后一项不是两个已舍入 exp 的乘积。使用 cache 时其非零生成需 O(p³) bitwork，另加 log 生成；与比较器一致付费。dense 与 sparse 为不同表示选择，不混合其优势；packed registers 与 scalar neural bit-channel 存储分别说明。\n\n完整 offline 包括 K,N,h layout、masks/positions、微码、cache/selector、全部 gate/term/hold 生成整理与实际格式输出。令 G,T_rec,I_hold 为实际生成的 gate、term、hold 记录数，其整理生成费用为 O((G+T_rec+I_hold)p²) bitwork 和 O((G+T_rec+I_hold)p) 工作 bits；dense 文件还支付真实 coefficient bits 的写出，包括零项。input/query/endpoint acquisition、residual copy、保持、擦除和最终 decode 均计费。\n\n总峰值按同一 phase 同时存活的程序/参数、input、mask/metadata、QKV、residual、银行、controller/address、临时工作区及输出求和，再取各 phase 最大值。上表 rolling working bits 不能冒充总峰值。这里不声称已在本 workspace 运行未提供的旧 emitter，也不以其他程序的精确 ledger 冒充 Pi 的实测 profile。\n\n另有保守 PURE neural 展开实现：令 T_bit 为上述固定循环的全部 online bitops（含 copy/clear），S_bit 为相应 live work、input/mask/public data；若用 interpreter，存储程序位作为常数 rails 加入。逐指令展开并保持其余 live bits，得到 depth O(T_bit+p)、width O(S_bit+p)、sparse gates/holds O((T_bit+p)(S_bit+p))、dense coefficient bits O(p(T_bit+p)(S_bit+p)²)、generic dense bitwork O(p²(T_bit+p)(S_bit+p)²)。该展开的完整成本单列，不能报告成较小的 hybrid L,W。\n\n## S5. 准确结论边界\n\nS1–S4 是本独立来源义务的合取，只针对上述固定 Pi 构造及定位接口。不从抽象 I 推导实现或费用，不泛化到所有训练 Transformer；不包含强 direct 基线上的逐坐标资源优势、整网主导成本下降或资源最优性。资源 NORM 模块与 weighted-direct 的新前端/bridge 若被使用，须有其自身明确实现和费用来源。\n\n证明可复用来源的固定确定性推导，但需在本项目正常提交为可独立检查的完整正文。G/U 统计根不作此纯确定性义务的必要前提；其独立完成不倒置为已完成统计根的前提。上述 statement 未把任何旧 discussion PASS 或旧 Fact 编号当作本项目 admission。\n","fact_id":"fef8372728290b45","scope_bindings":[{"evidence_id":"e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505","obligation_id":"6010cac30ffe4aea77e6d7a9e4e3f5686e4f44b2bf31c1674d33dfdf7dc46f84","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]}}],"source_hash":"33ea4cbe839a4ad72453cb20f8f74263a1d330e766027f7e65638c494da4c025"}]

Proof:
# 031 DOT-STATIONARY-INITIALIZATION-PI — complete finite proof

Obligation: 365961b8b82c621f77a34a41eb8013b2c5dee6134018aa8fb66baa47b9cae3fa.
Prepared by the native Prover, 2026-10-29. This is one submission of the entire
STAT/INIT/PI-STAT conjunction, including its auxiliary finite conclusions and
unchanged implementation costs. Acceptance is determined only by the normal
independent Euler gateway.

## 0. Authorship, exact target and actual premises

The stationary and initialization arguments are due to **Dot**. This proof
adopts S001 §§3–7 (stationary window charging, selected-row upper and truncation),
S002 §§1–5,7 (checkerboard family, reverse complete-history testing), and S003
§§3–7 (stationary existence, positive-part domination, contamination lower and
capped sample implications), from
inputs/source-dot-conditions-20261029-v2/sources/stage02/proofs/.
These arguments are written out below, not invoked as externally accepted Facts.
The same-Pi combination is the standard combination stated in the Lead's
031 frozen statement and source intake, proved in §8 below.
The source ZIP SHA256 is
cc8b3cf77d799e65d5cafd51d4738262c76a8c58756ffcf5b968d6a65ff1a188.
SOURCE_MANIFEST.json binds all 61 copied files, whose byte hashes were checked.
Source reviews, enumeration and external ACCEPTED labels are not premises.

The frozen file SHA256 is
399bb30c037d917827b7b575e53bb6f057f0766a23e792ea0557ac2c17ca3cb0.
The native exact statement SHA256 is
47b612212a7588ed6966c26aae7aadf4bfdabe8fc0222396f9bb2f6afa01ac65.
The frozen file is exactly the native statement plus one trailing LF; neither
was edited. All mathematical text and quantifiers agree.

Exactly three admitted direct Fact predecessors are used:

1. 016, Fact a53804d650803060; Evidence
   fef1785395851e47b5ca0b719640449061718f4c670bfcd74c24cf0aec696c88.
   Its deterministic-prefix bound is stated precisely in §3; its arbitrary
   initialization add-one upper is L_+(theta,nu)<=min(1,48t) for every theta,nu.
2. MM5, Fact 946d42d5bf502eb4; Evidence
   aa23c442ca1006c6ac0b12379f64a0fa500fbbd6a2e41c798b7a4de3952baa82.
   For every common full-history randomized probability predictor A,
   sup_(theta,nu) L_A(theta,nu)>=2^-16 min(1,t).
3. SRC, Fact fef8372728290b45; Evidence
   e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505.
   It supplies the actual common Pi, its all-path interface I, and its complete
   construction/cost certificate, used in §§8–9.

All three Evidence records are native PASS/VALID; the actual Fact bytes match
their content_hash. Their original proofs and predecessor lists are unchanged.
There is no direct use of 030, 028, 023, general UC, or any other Fact. In
particular general UC is not used to infer the stationary occupancy constant.

## 1. Common experiment, quantifiers and conclusions

Fix integers K>=2 and M>=1; N=M+2. Write mathcal A={0,...,K-1},
mathcal S=mathcal A^2. A source theta consists of K^2 probability rows theta_z.
Its pair kernel has only legal transitions
P_theta((x,b),(b,c))=theta_(x,b)(c). Within each experiment theta is fixed;
zero entries, reducibility and periodicity are allowed. Let
Y_i=(X_(i+1),X_(i+2)), 0<=i<=M. Only the complete history
H=(X_1,...,X_(M+2)) is observed. Its counted departures are i=0,...,M-1.
The target is theta_(Y_M); departure M and X_(M+3) are unobserved.

For z in mathcal S and c in mathcal A define
C_z,c=sum_(i=0)^(M-1) 1{Y_i=z,X_(i+3)=c},
n_z=sum_c C_z,c, J=n_(Y_M), p_z,c^+=(C_z,c+1)/(n_z+K).
Every denominator is positive, including at zero counts.
For a common algorithm A define
L_A(theta,mu)=E_(theta,mu,U) TV(A(H,U),theta_(Y_M)),
where TV(q,p)=||q-p||_1/2 and U is an independent seed.
A is a fixed probability kernel from the entire history to the simplex,
allowed public K,M and, for the initialization problem, public eta.
It receives neither theta,mu,pi, a mixture label, future data nor auxiliary
samples. The source supremum is taken after fixing this kernel.

Set s=K^(3/2)/sqrt(M+1), t=K^(5/2)/sqrt(M+1),
a=min(1,s), g=min(1,t), u_s=min(1,48s), u_g=min(1,48t).
Here s is a scalar rate; pair states are denoted z. These a,g have no
connection to clock sizes or internal precision in other obligations.

The stationary class consists of all PAIRS (theta,pi) with pi P_theta=pi,
and initialization mu=pi. The supremum is jointly over theta and pi, not
over pi at a fixed known theta. Pi may be nonunique or have zero coordinates;
it is hidden. Define
R_stat=inf_A sup_(theta,pi:pi P_theta=pi) L_A(theta,pi);
R_stat^+ is the same supremum for the fixed p^+.

For fixed public eta in [0,1] define
C_eta={(theta,mu): there exists pi with pi P_theta=pi, TV(mu,pi)<=eta}.
Define R_eta=inf_A sup_C_eta L_A and R_eta^+=sup_C_eta L_+.
The witnessing pi can vary with the source. The add-one algorithm is the
same eta-independent algorithm throughout.

We prove for every stated finite parameter
    a/180 <= R_stat <= R_stat^+ <= u_s;                         (STAT)
    max(a/180,2^-16 eta g) <= R_eta <= R_eta^+
      <= min(u_g,u_s+eta u_g);                                 (INIT)
and, with r_eta=max(a,eta g),
    2^-16 r_eta <= R_eta <= R_eta^+ <= min(1,96r_eta).
We also prove the frozen per-state occupancy, real-threshold truncation,
capped sample equivalence/necessities, and the same-SRC-Pi bound
    R_Pi,stat(K,M,h)
      <=min(1,48s+(K-1)/Q+Psi(78K^3 M/[Q(M+1)]))
      <=min(1,64s)                                            (PI-STAT)
for every legal h, with the exact unchanged cost certificate.

## 2. Stationary finite-window occupancy and real truncation

For any deterministic sequence y_0,...,y_(2M), any state z and integer v>=1,
flag times t=M,...,2M when y_t=z and fewer than v occurrences of z lie in
[t-M,t-1]. There are at most v flags. Indeed, if v+1 flags occurred at
t_1<...<t_(v+1), all earlier v times lie in the last flag's preceding
M-window: t_(v+1)-M<=M<=t_i<t_(v+1). This contradicts that flag.
For v>M this proof is still valid (or the desired bound is trivial).

Extend the source chain from time M to 2M purely on the proof probability
space. Starting at pi gives, for every offset b>=0 and every legal finite block,
    P(Y_b=z_0,...,Y_(b+M)=z_M)
      =pi(z_0) product_(i=0)^(M-1) P_theta(z_i,z_(i+1)).
This follows from pi P_theta=pi and the homogeneous Markov product.
Consequently all M+1 candidate flags have the same probability.
Taking expectations of the deterministic bound gives
    P(Y_M=z,n_z<v)<=v/(M+1).
It is also at most P(Y_M=z)=pi(z). Summing the disjoint terminal events over
K^2 states and capping at one gives
    P(Y_M=z,n_z<v)<=min(pi(z),v/(M+1)),
    P(J<v)<=min(1,c_0 v),   c_0=K^2/(M+1).                    (OCC-stat)

This uses only stationary finite blocks. It includes M=1, v>M,
zero-mass states (whose events have probability zero), deterministic periodic
chains and arbitrary stationary mixtures of closed classes. The extension
to 2M is not provided to the algorithm. There is no interchange of sum/max.

Define Psi(0)=0, Psi(x)=x(1+ln(1/x)) for 0<x<1, and Psi(x)=1 for x>=1.
For any real A_0>=0 we claim
    E min(1,A_0/(J+K))<=Psi(c_0 A_0)<=2sqrt(c_0 A_0).          (TRUNC-stat)
A_0=0 is immediate. Otherwise, for 0<q<1 put x=A_0/q-K.
The event {min(1,A_0/(J+K))>q} is {J<x}; it is empty for x<=0.
For x>0, integer J gives {J<x}={J<ceil(x)}, and
    1<=ceil(x)<=x+1=A_0/q-K+1<=A_0/q.
This is valid at exact integer x as well. Apply OCC-stat at that integer,
then integrate over q in (0,1):
    E min(1,A_0/(J+K))
      <= integral_0^1 min(1,c_0 A_0/q)dq = Psi(c_0 A_0).
Finally min(1,z/q)<=sqrt(z/q), so this integral is at most 2sqrt(z),
including z=0 and z>=1. No noninteger threshold was inserted into OCC-stat.

## 3. Stationary add-one upper using only deterministic-prefix L1MAX

Use independent row stacks xi_(z,l) with law theta_z, z in mathcal S,
1<=l<=2M, independent of Y_0~pi. At the (j+1)-st departure from z consume
xi_(z,j+1). For every full symbol prefix, exactly the consumed row-prefix
constraints are imposed; unused entries are unrestricted. Its probability
is pi(x_1,x_2) product_i theta_(Y_i)(x_(i+3)), so this finite coupling
reproduces the original complete path law, including zero-probability paths.
On every realized path, putting
S_(z,j)=sum_(l=1)^j(e_(xi_(z,l))-theta_z), S_(z,0)=0, gives
    C_z-n_z theta_z=S_(z,n_z).
No conditional iid assertion is made about J, Y_M or the selected stack.

The deterministic-prefix part of 016 applies for each deterministic 1<=v<=M:
    Z_v=max_z max_(0<=j<=2v) ||S_(z,j)||_1,
    ||Z_v||_4 <=sqrt(8Kv)+sqrt(8v ln K)+32^(1/4)sqrt(v)
              <=(25/4)sqrt(Kv).                             (L1MAX-016)
This premise concerns auxiliary iid stacks at fixed prefix lengths only;
it is independent of the initialization and remains valid for zero rows.

For clarity the numerical dyadic bound needed below is elementary:
    D(b)=sum_(l>=0) 2^(-l/2) min(1,b2^l)^(3/4)<=10sqrt(b)
for b>0. If b>=1, the sum is 2+sqrt(2)<7/2.
If b<1 choose H>=0 with b2^H<=1<b2^(H+1).
The first part is at most sqrt(b)/(1-2^(-1/4)); the second is less than
sqrt(b)/(1-2^(-1/2)). Since 2^(-1/4)<27/32 and
2+sqrt(2)<7/2, their sum is less than (32/5+7/2)sqrt(b)<10sqrt(b).
Only this deterministic numerical series is infinite.

Define the empirical row C_(Y_M)/J only on J>=1. On E_v={v<=J<2v},
for deterministic dyadic v=2^l<=M, the stack identity gives pathwise
    TV(C_(Y_M)/J,theta_(Y_M))<=Z_v/(2v).
Unconditional Holder with exponents 4 and 4/3, L1MAX-016 and OCC-stat
at integer 2v therefore give
    E[TV(C_(Y_M)/J,theta_(Y_M)) 1_(E_v)]
      <=(25/8)sqrt(K) v^(-1/2) min(1,2c_0 v)^(3/4).
This is an unconditional expectation of correlated random variables.
A null E_v contributes zero. Summing l=0,...,floor(log2 M), which
partitions 1<=J<=M, and extending only the numerical upper sum yields
    E[TV(C_(Y_M)/J,theta_(Y_M)) 1_(J>=1)]
      <=(25/8)sqrt(K)D(2c_0)
      <=(125sqrt(2)/4)sqrt(Kc_0)
      =(125sqrt(2)/4)s.
For M a power of two the last layer begins at v=M; the auxiliary
prefix 2M already exists. No extra data or random-length iid estimate enters.

On J>=1, with u the uniform alphabet vector,
    p^+_(Y_M)=[J/(J+K)] C_(Y_M)/J + [K/(J+K)]u.
The add-one loss is bounded by the empirical loss plus K/(J+K).
On J=0 it is at most one. Thus
    L_+(theta,pi)
      <=P(J=0)+E[empirical loss 1_(J>=1)]
                    +E min(1,K/(J+K)).
Here OCC-stat at v=1 gives P(J=0)<=min(1,c_0)<=sqrt(c_0)<=s;
TRUNC-stat at A_0=K gives the smoothing term <=2s.
Consequently
    L_+(theta,pi)<=[125sqrt(2)/4+3]s<48s,
because sqrt(2)<36/25 and (125/4)(36/25)+3=48.
Probability-vector TV is at most one. Taking the joint stationary
supremum proves R_stat^+<=u_s. Since p^+ is admissible, R_stat<=R_stat^+.
This proves the upper part of STAT without assuming mixing.

## 4. Dot's checkerboard sources and the complete reverse experiment

Put r=floor(K/2) and pair the first 2r symbols as B_i={2i,2i+1},
0<=i<r. Let epsilon_(2i)=+1, epsilon_(2i+1)=-1.
An odd leftover symbol is unpaired. Choose d_0=Kr^2 signs
sigma_(b,i,j) independently in {-1,+1} under a uniform proof prior.
Set alpha=a/10, so 0<alpha<=1/10. For x in B_i and c in B_j define
    theta^sigma_(x,b)(c)
      =(1+alpha sigma_(b,i,j) epsilon_x epsilon_c)/K,
and set theta^sigma_(x,b)(c)=1/K if x or c is unpaired.

All entries lie in [(1-alpha)/K,(1+alpha)/K].
For each fixed x,b, perturbations cancel in every output pair B_j;
for each fixed b,c, they cancel in every first-coordinate pair B_i.
Hence every row sums to one and sum_x theta^sigma_(x,b)(c)=1.
Use the legal shift pair kernel, with structural zeros elsewhere.
The uniform pair law pi(z)=K^-2 is stationary since
    sum_x K^-2 theta^sigma_(x,b)(c)=K^-2.
Initialize with exactly this pi. For every sigma and every M the
actual terminal law is uniform, independent of sigma.
The construction is valid also for K=2 and K=3.

Fix ANY actual endpoint z. Write P_sigma^z for the law of the entire
observed symbol history conditional on Y_M=z. All endpoints have
positive probability K^-2. Define the reverse kernel
    Q_sigma((b,c),(x,b))=theta^sigma_(x,b)(c),
with zero on other reverse shifts. Column cancellation proves its rows
sum to one. For every legal complete pair path ending at z,
    P_sigma^z(Y_0=y_0,...,Y_M=z)
      =[K^-2 product_(i=0)^(M-1) P_sigma(y_i,y_(i+1))]/K^-2
      =product_(i=0)^(M-1) Q_sigma(y_(i+1),y_i).              (PATH)
The pair path and complete symbol history determine each other bijectively.
Thus Z_l=Y_(M-l), 0<=l<=M, is the reverse chain started at z under
this conditional law. The initial observed pair and every observed symbol
remain in PATH. No terminal query is replaced by an independent query.

For reverse start (u,v) and destination (x,b), the unique two-step
reverse path goes through (b,u). Therefore
    Q_sigma^2((u,v),(x,b))
      =theta^sigma_(b,u)(v) theta^sigma_(x,b)(u)
      <=(1+alpha)^2/K^2.
For every reverse time l>=2 and every pair w, summing this bound over
Z_(l-2) gives P_sigma^z(Z_l=w)<=(1+alpha)^2/K^2.

Flip one bit ell=(b,i,j) of sigma. Only two reverse departure rows change:
D_ell={(b,2j),(b,2j+1)}. Each exchanges two outgoing probabilities
(1+alpha)/K and (1-alpha)/K. Its relative entropy is exactly
    (2alpha/K) ln((1+alpha)/(1-alpha))<=8alpha^2/K.
Indeed the logarithm is at most 2alpha/(1-alpha)<=4alpha, as alpha<=1/2.
All other reverse rows have relative entropy zero. The expected number
of departures from D_ell in the M reverse transitions is at most
    min(M,2)+(M-2)_+ 2(1+alpha)^2/K^2
      <=2+9M/(2K^2).
In particular the first two steps are explicitly paid even for M=1 or 2.

Expanding the logarithm of the two finite products PATH and then
taking expectation proves the chain rule here directly:
    D(P_sigma^z || P_(sigma^ell)^z)
      =sum_(l=0)^(M-1) E_sigma^z
          D(Q_sigma(Z_l,.) || Q_(sigma^ell)(Z_l,.))
      <=16alpha^2/K+36alpha^2 M/K^3.                        (KL)
All legal paths have positive probability in both hypotheses, and
illegal paths have zero in both. Since alpha^2<=1/100 and
alpha^2 M/K^3 <=1/100, K>=2 makes KL<=44/100<1/2.

Here is the finite Pinsker justification so that no additional Fact is used.
For probability vectors p,q on a common finite support with q>0, let
B={p>=q}, u=p(B), v=q(B); then u-v=TV(p,q).
When TV>0, 0<v<1. Log-sum (Jensen for x ln x, separately on B and its
complement) gives
    D(p||q)>=u ln(u/v)+(1-u)ln((1-u)/(1-v)).
For fixed v the expression and its first derivative vanish at u=v;
its second derivative is 1/[u(1-u)]>=4. Integrating twice and taking
endpoint limits gives D(p||q)>=2(u-v)^2. TV=0 is immediate.
It follows from KL that for EVERY actual endpoint z and bit ell,
    TV(P_sigma^z,P_(sigma^ell)^z)<=sqrt(22/100)<1/2.          (TEST-TV)

## 5. Actual-target loss, ties, seeds and the stationary lower

Fix an arbitrary common algorithm A, including its source-independent
randomization. For a paired endpoint z=(x,b), x in B_i, and each j<r,
decode +1 if epsilon_x(A_(2j)-A_(2j+1))>=0, and -1 otherwise.
The rule for a tie is fixed independently of sigma. The true signed
difference is (2alpha/K) sigma_(b,i,j).
If decoding is wrong, the sum of the absolute errors of these two
output coordinates is at least 2alpha/K, also in the tie case.
The pairs of coordinates are disjoint, so pointwise
    TV(A,theta_z^sigma)
      >=(alpha/K) sum_(j<r) 1{decoded bit != sigma_(b,i,j)}. (LOSS)

Under the uniform sign prior, conditioning on Y_M=z leaves the prior
uniform, because each source has the same terminal mass K^-2.
For any randomized binary test between P and Q, the sum of its two
error probabilities is >=1-TV(P,Q): if phi(h) in [0,1] is the
conditional probability of choosing the first hypothesis, the error sum
equals 1-integral phi d(P-Q), bounded below by 1-TV(P,Q).
This formula integrates the independent seed; no finite-seed assumption
or source-dependent randomization is introduced.

Fix z=(x,b), x in B_i, and j. Pair all sign vectors with their
ell=(b,i,j) flips. By TEST-TV their sum of conditional error probabilities
is >=1/2, hence the uniform prior average error probability is >=1/4.
Apply LOSS, sum over the 2rK paired endpoints with their true weights
1/K^2, and discard only the nonnegative losses at unpaired endpoints:
    2^(-d_0) sum_sigma L_A(theta^sigma,pi)
      >=K^-2 (2rK) (alpha/K) r/4
      =alpha r^2/(2K^2).
For all K>=2, r/K>=1/3: the even ratio is 1/2, and for odd K>=3
it is (K-1)/(2K)>=1/3. Thus the average is at least
alpha/18=a/180. The worst source risk is at least this finite average
for EACH fixed common A. Taking inf_A proves R_stat>=a/180.

The source table may depend on K,M through alpha but stays homogeneous
on the entire trajectory. The proof uses the complete actual history
conditional on its own endpoint, not a statistic with information removed.
The larger stationary class may have zero edges or multiple stationary
laws; a valid subclass suffices for its lower bound. This establishes
all of STAT, with absolute constants, not optimal numerical constants.

## 6. Initialization neighborhood: domination and contamination

Every finite stochastic matrix admits a stationary probability law,
without irreducibility. To see this, start from any row probability rho
and average pi_T=T^-1 sum_(i=0)^(T-1) rho P_theta^i.
The finite simplex is compact, so some subsequence converges to pi.
The identity
    pi_T P_theta-pi_T=(rho P_theta^T-rho)/T
has L1 norm at most 2/T. Continuity gives pi P_theta=pi.
This proof is unaffected by legal-shift zeros or periodicity.

Fix public eta and a common algorithm A BEFORE choosing a source.
For fixed theta define, for every deterministic starting pair y,
    f_(A,theta)(y)
      =sum_H P_theta^y(H) E_U TV(A(H,U),theta_(Y_M(H))) in [0,1].
This is defined even at a pi-zero-mass initial pair. The complete-path
product law implies the finite identity
    L_A(theta,mu)=sum_y mu(y) f_(A,theta)(y).                 (LIN)
It proves linearity in initialization for fixed theta and A. It does
not assert linearity of TV in its target, and it retains the entire
observed initial pair and every subsequent symbol.

For the upper, let (theta,mu) in C_eta, and choose a witnessing stationary pi.
Put delta=(mu-pi)_+, e=sum delta=TV(mu,pi)<=eta.
Pointwise mu<=pi+delta. If e=0, mu=pi and STAT applies.
If e>0, nu=delta/e is a probability law, and LIN with nonnegative f gives
    L_+(theta,mu)
      <=L_+(theta,pi)+e L_+(theta,nu)
      <=u_s+e u_g<=u_s+eta u_g.
The second term uses the already admitted 016 arbitrary-initialization
upper, valid for each theta and every nu. Independently 016 gives
L_+(theta,mu)<=u_g. Hence
    R_eta<=R_eta^+<=min(u_g,u_s+eta u_g).
This covers the WHOLE TV-neighborhood. We have not represented every
TV-close law as a fixed-weight contamination; that representation is
not generally valid.

For the lower, stationary initializations are a subclass of C_eta, so
for each fixed A,
    sup_C_eta L_A >= sup_(theta,pi:pi P_theta=pi) L_A >=a/180.
Separately, for EVERY fixed theta and arbitrary nu choose one stationary
law pi_theta supplied by the existence argument and define
    mu=(1-eta)pi_theta+eta nu.
This chosen subclass satisfies TV(mu,pi_theta)=eta TV(nu,pi_theta)<=eta.
At fixed theta and A, LIN and nonnegativity imply
    L_A(theta,mu)
      =(1-eta)L_A(theta,pi_theta)+eta L_A(theta,nu)
      >=eta L_A(theta,nu).
Taking the source supremum and applying the admitted MM5 lower gives
    sup_C_eta L_A >= eta sup_(theta,nu) L_A(theta,nu)
                  >=eta 2^-16 g.
For eta=0 the assertion is just nonnegativity; there is no division by eta.
No measurable global selection theta->pi_theta is needed for this
pointwise source comparison, nor is a supremum assumed attained.
The same kernel A acts on the full history in both experiments.
The hidden mixture label and pi_theta are not provided; any label
information inferred from the visible initial pair is already available
to the common full-history algorithm covered by MM5.

Taking inf_A only AFTER these comparisons yields
    R_eta>=max(a/180,eta g/65536)>=2^-16 max(a,eta g).
This combines different possible source witnesses by a maximum, not by
addition at a claimed common hard source. Fixing public eta leaves A
within the universal common-algorithm classes used in STAT and MM5.

Since min(1,48x)<=48min(1,x), the upper is at most
min(1,48(a+eta g))<=min(1,96max(a,eta g)).
This proves INIT and its capped simplification. At eta=0 the class is
exactly stationary initialization; at eta=1 stationary existence and
TV<=1 make it the entire arbitrary-initialization class.
All comparisons allow nonunique pi, reducible and periodic sources.

## 7. Finite sample implications and cap thresholds

For 0<epsilon<1, a<=epsilon is equivalent to
s<=epsilon, hence to M+1>=K^3/epsilon^2: the cap cannot be active.
For eta g<=epsilon, if eta<=epsilon the condition holds automatically.
If eta>epsilon, it is equivalent to g<=epsilon/eta<1, then to
M+1>=eta^2 K^5/epsilon^2. Thus exactly
    r_eta<=epsilon iff M+1>=K^3/epsilon^2 AND
       [eta<=epsilon OR M+1>=eta^2 K^5/epsilon^2].             (CAP)
This includes eta=0 without dividing by zero.

For 0<tau<1, use epsilon=tau/96. Therefore the SAME eta-blind p^+
has class risk <=tau whenever
    M+1>=96^2 K^3/tau^2,
    eta<=tau/96 OR M+1>=96^2 eta^2 K^5/tau^2.
These are sufficient, not exact numerical minimax thresholds.

If ANY common algorithm has uniform class risk <=tau and
0<tau<1/180, the lower a/180 forces a<=180tau<1 and hence
    M+1>=K^3/(180^2 tau^2).
For the other lower, ONLY when eta>0 and tau<eta/65536 may one infer
g<=65536tau/eta<1, and thus
    M+1>=eta^2 K^5/(65536^2 tau^2).
If the strict threshold does not hold, this lower permits its cap g=1
and does not imply that uncapped sample necessity. Both claims are
finite-parameter consequences of INIT with the source sup/algorithm inf
in their original order.

## 8. Same actual SRC-Pi: all-precision stationary combination

Let h be ANY integer at least h0=max(4,ceil(log2 M)+1), Q=2^h.
Use exactly the admitted SRC program Pi_(K,N,h); no decoder or port is
changed. SRC gives probability-vector output and, for every complete
history and every query z simultaneously,
    TV(Pi(H;z),p_z^+(H))
      <=78KM/[Q(n_z+K)]+(K-1)/Q.                            (I-SRC)
Therefore one may substitute the actual observed z=Y_M, with its true
count J, without an independence assumption.

Set A_h=78KM/Q and b_h=(K-1)/Q.
Probability-vector TV and I-SRC give pointwise
    TV(Pi(H;Y_M),p^+_(Y_M))
      <=min(1,A_h/(J+K)+b_h)
      <=min(1,A_h/(J+K))+b_h.
On every stationary source, TRUNC-stat at the REAL number A_h and
the true J gives
    E TV(Pi,p^+_(Y_M))<=Psi(K^2 A_h/(M+1))+b_h.
Combining with the proved STAT upper, then applying TV<=1 and taking
the joint stationary supremum, yields
    R_Pi,stat(K,M,h)
      <=min(1,48s+b_h+Psi(78K^3 M/[Q(M+1)])).
This is the first asserted PI-STAT bound.

For all these h, including M=1 and h=h0, Q>=2M.
Hence A_h<=39K, and
    Psi(K^2 A_h/(M+1))<=2sqrt(39) K^(3/2)/sqrt(M+1)
                              =2sqrt(39)s.
Also M+1<=4M^2 for M>=1, so
    b_h<=(K-1)/(2M)<=K^(3/2)/sqrt(M+1)=s.
Since 39<49, we have sqrt(39)<7 and
    48+2sqrt(39)+1<63<64.
Thus the SAME network satisfies R_Pi,stat<=min(1,64s) for EVERY legal h.
All steps include J=0 and pi-zero rows; the interface is all-path,
including histories incompatible with some source.

For 0<tau<1, if
    M+1>=(64K^(3/2)/tau)^2, h=h0,
then 64s<=tau and this Pi has stationary class risk <=tau.
No statement here transfers all of INIT to Pi without paying its
implementation error; INIT above concerns p^+ and minimax algorithms,
whereas the Pi conclusion proved here is exactly stationary PI-STAT.

## 9. Actual implementation and full cost preservation

The statistical denominator M+1 is distinct from the actual position
count n_tok=N+1=M+3. The genuine SRC word parameter is
    ell=ceil(log2(M+K+4)), p=4h+4ell+64.
Neither the row-stack construction nor checkerboard nor the analysis
counts become program inputs. Stationary pi, theta and eta remain hidden
to Pi. Changing the path distribution does not change the bitwise
program, its layout, masks or complete cost on a fixed input.

We retain SRC's dense/uncached batch hybrid. Two paid singleton-copy
heads and four statistical heads are evaluated at ALL n_tok positions.
The original finite rational logs, separately evaluated full scores,
head floors, guards, readout, positive normalization and ordered
simplex floor/residual output are unchanged; the backend does not
reread history. In particular this is SRC-Pi, not the later anchor
program. The following are the SAME SRC construction upper bounds,
with absolute constants, not new measurements:

| Resource | Preserved SRC bound/structure |
|---|---|
| neural depth / width | O(Kp^2) / O(Kp) |
| heads total / maximum per layer; maximum QK dimension; score cap | 6 / 4; 2K; 2 |
| each online coefficient and full arithmetic word | at most 128p bits, including products, remainders, guards |
| dense coefficient slots / parameter bits | O(K^3 p^4) / O(K^3 p^5), including zeros and bias |
| active gates/projections / identity holds | O(Kp^2+K^2) / O(K^2 p^3) |
| alternate sparse program, coefficient, address, holds format | O(K^2 p^4) bits, not substituted for dense storage/work |
| masks / position metadata | O(n_tok^2+n_tok log(n_tok+1)) bits |
| observed input | O(NK) one-hot bits, or paid binary acquisition/conversion |
| rolling work arrays only | O(n_tok Kp^2) bits |
| uncached finite attention bitwork | O(n_tok^2 (K+p)p^2) |
| dense pointwise and QKV bitwork | O(n_tok K^3 p^6) |
| rational log generation / scratch | O(p^3 log^2(p+1)) / O(p log(p+1)) |
| finite arithmetic evaluator code | O(p^4) bits |

All input/query/actual-endpoint acquisition, projection, causal masks,
residual copy, hold, clear, full arithmetic intermediates and final
decode are charged as in SRC. The alternative cached bound in SRC
does not replace the uncached work here; no cache advantage is claimed.
The dense and sparse representations and scalar bit channels versus
packed registers are not combined by selecting only their cheaper entries.

The full offline package includes K,N,h layout, masks/positions,
microcode and every gate/term/hold record and actual format output.
For actual record counts G_rec,T_rec,I_hold, the original assembly
bound O((G_rec+T_rec+I_hold)p^2) bitwork and
O((G_rec+T_rec+I_hold)p) working bits is retained; dense coefficient
bits, including zero entries, must be physically written.
Any cache/selector representation, if separately used, has its SRC
generation and storage costs; none is silently added to this program.
At every phase sum all simultaneously live program/parameter, input,
mask/metadata, QKV, residual, bank, controller/address, temporary and
output bits; total peak is the maximum of these phase totals.
The rolling-work line alone is not a total peak.
The separate conservative PURE neural expansion in SRC retains its
own costs and is not identified with these smaller hybrid dimensions.

This is a standard statistical combination for one previously realized
network. It establishes neither equal-numerical-cap advantage over a
direct comparator, optimal work/width, a resource lower bound for all
Transformers, nor a fault conclusion. No compiler, literal ledger,
batch measurement or profile was run for this task. GPU usage and
[Non-scientific operational metadata omitted.]

## 10. Closure, remaining boundaries and submission claim

Sections 2–5 prove stationary occupancy, all real truncation thresholds
and STAT for every K>=2,M>=1. Sections 6–7 prove INIT, its endpoint
cases and all capped sample conclusions. Sections 8–9 combine these
with the actual SRC all-path interface and full costs to prove PI-STAT.
These sections together prove the entire frozen 031 conjunction.
The only imported mathematical premises are exactly 016, MM5 and SRC
as declared in §0. Dot's own sources and the local reviews are attributed
writing sources, not independent admissions or additional Facts.

S018/S019, their restricted M<=K^4,beta<=1/2 domains, and the S007
non-IID K>=6 three-step construction are not used or extended.
Future conditional-statistics continuation remains Dot's.
Nothing changes old roots, accepted Fact dependencies, the two 027
method obstacles, 029 OPEN/PARKED, 021 closure, 022 OPEN/PARKED,
[Non-scientific operational metadata omitted.]
There is no claim of a single difficult source for every algorithm,
horizon or eta, no fixed/all/conditional-risk upgrade, and no independent
terminal query. Constants are conservative absolute constants.
Normal independent gateway acceptance of 031 is still required;
the v10 research objective is not declared solved.
