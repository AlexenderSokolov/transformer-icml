---
fact_id: ca2de64e8dbb95d4
problem_id: icml-general-prediction
author: prover
predecessors: [a12539a93d9f1ee3]
glossary_introduces: {}
external_refs: []
statement_chars: 2726
---

## statement
# RATE-K-MINIMAX：合法二阶源族上的一般 K actual TV 下界

这是 RATE-K-LOW 接纳之后的独立算法量词扩展候选，目标是全部共同全历史预测器，不把指定 add-one 的已知源损失冒充 minimax。旧 G/U、SRC、RATE-TV、K3 与 K-LOW 均保持接纳及原有依赖，不增加逆向前提。Lead 候选和 Counter 报告不是 Fact；本合取需完整证明与正常独立网关。

对每个整数 K>=2、M>=1，N=M+2，字母表为 {0,...,K-1}。theta 是任意齐次二阶转移表，允许零边；mu 为任意初始对律。令 Y_i=(X_(i+1),X_(i+2))，0<=i<=M；观察完整 X_1^(M+2)，actual target 是 theta_(Y_M)。一条实验内 theta 固定，sup 可随 (K,M) 改选源。

令 A_(K,M) 遍历所有共同、可能随机的全历史概率预测器：其输入只有已观察历史和公开 K,M，可计算 actual query，但不得读隐藏 theta,mu 或未来符号。算法的随机种子与源独立；算法可依 K,M 选择，且输出在 K-simplex 上。定义

    R_min(K,M)=inf_A sup_(theta,mu)
        E_(theta,mu,A) TV(A(X_1^(M+2)),theta_(Y_M)).

拟证明全部有限参数上的

    R_min(K,M)>=2^(-12) min{1,sqrt(K^3/(M+1))}.        (MM)

这是同轨迹 actual 的均值风险，非 fixed row、最大行、时间平均或额外独立测试实验。证明中允许在一个具体合法源族内导出末对的独立性，但必须从原二阶路径律严格证明，不能为一般源额外假设独立 query 或条件 iid。

## 1. 拟用的合法有限源族及全余数初始化

K>=6 时，置 q=floor(K/3)>=2、r=floor(q/2)。取三个互不相交的字母组 U,V,W，各有 q 个字母；余下字母的质量可为零。对每个 (u,v)∈U×V、j=1,...,r，取未知符号 sigma_(u,v,j)∈{-1,+1}。将 W 中前 2r 个字母分为 r 对，取公开 0<alpha<=1/2，定义

    theta_(u,v)(w_(2j-1))=(1+alpha sigma_(u,v,j))/q,
    theta_(u,v)(w_(2j))  =(1-alpha sigma_(u,v,j))/q.

若 q 为奇数，剩下的一个 W 字母概率为 1/q；组外概率为零。对所有 (v,w)∈V×W，theta_(v,w)=Unif(U)；对所有 (w,u)∈W×U，theta_(w,u)=Unif(V)。其余未到达 pair 给任一固定合法概率行。完整证明须检查归一化、shift 约束、未到达行及同一齐次表。

写 M=3n+d，d∈{0,1,2}。初始化不依 sigma：d=0 时 mu=Unif(U)⊗Unif(V)；d=1 时 mu=delta_(w_*)⊗Unif(U)；d=2 时 mu=delta_(v_*)⊗delta_(w_*)，其中公开 v_*∈V,w_*∈W。应严格证明已观察历史等价于 n=floor(M/3) 个独立 block (U_i,V_i,W_i)，其中 (U_i,V_i) 独立 uniform 于 U×V，W_i 条件律为 theta_(U_i,V_i)，加上一个与全部训练 block 独立的 uniform 末对 (U_(n+1),V_(n+1))。d=1,2 的初始固定前缀不携带 sigma 信息；n=0 也必须覆盖。这个等价是原始完整轨迹的精确表示，没有删除信息或更换风险实验。

## 2. 未知符号测试与常数

可取 alpha=min{1/2,(1/8)sqrt(q^3/(n+1))}。相邻符号向量仅翻转一个 (u,v,j) 时，完整训练 block 的 KL 必须从实际路径律计算；候选给不超过 8n alpha^2/q^3。实际末对和固定前缀不能引入未计的信息。

对实际末对为 (u,v) 的每个符号对，预测器两个 W 坐标的顺序可用作 sigma_(u,v,j) 的测试；错误顺序使该对的 TV 贡献至少 alpha/q。需要严格处理任意随机预测器、ties、实际末对条件下的观察律、符号平均与所有 q² 行的权重，不能把不同源风险直接相加后声称同一见证。标准两点测试不等式及所用 KL-TV 控制须明确证明或给准确可核版本。

预期由此先得 q>=2 时的保守下界

    R_min(K,M)>=(1/64) min{1,sqrt(q^3/(n+1))}.

再由 q>=K/6 与 n+1<=M+1推出 (MM)。对于 2<=K<=5，可只用本项目 G/U Fact a12539a93d9f1ee3 已接纳的任意共同算法 iid actual 下界 1/(16sqrt(M+2))，明确比较有限常数以补齐 (MM)。该 Fact 是此候选唯一必需的当前项目 Fact 前驱；高 K 源族和测试论证须自足，不能依赖 K-LOW 的指定估计器 lower。

## 3. 准确推论和范围

(MM) 若成立，则任何共同算法在该完整源类上达到统一 actual 均值风险 tau，0<tau<2^(-12)，必须有

    M+1>=2^(-24) K^3/tau^2.                          (sample necessity)

这只是统计样本量必要条件，不是内部 bit 数、层数、宽度、算术工作或资源最优性的下界。它覆盖实际 Pi 和 strong direct 作为全历史算法的子类，但不额外声称它们的实现费用，也不需要 SRC 作统计 lower 前提。

与已有 K3 upper 比较仍留下 K^(3/2) 与 K^3 的差距，不宣称 sharp K 或 minimax 完整匹配。未知源可依算法/参数选择，不能称一个固定源同时使所有算法失败。初始化依 M 的余数是合法的每 horizon supremum，不称同一 mu 在全部 M 同时实现该界。分组嵌入、两点测试、KL/TV 工具不作首创声称；直接 primary 的同范围先例仍需核对。本义务不重做 count-snap、二元故障或模块费用，也不宣告 v10 完成。

## proof
Original contract and explicit scope for this proof:
{"contract_id":"e6b7592e781948d00eb2a2effb80d8e3ef77e480f8d70f960286bc33faf730af","definitions":"## A. 共同源、观察、算法及风险定义\n\n对每个整数 K>=2，A={0,...,K-1}，S=A²，D=K²。一个实验固定一个时间齐次二阶表 theta∈(Delta(A))^S，允许零坐标；初始对分布 mu∈Delta(S) 任意。令\n\n    Y_j=(X_(j+1),X_(j+2)),\n    P_theta((a,b),(b,c))=theta_(a,b)(c),\n    N>=3, M=N-2, E_N=Y_M,\n    n_s(M)=sum_(j=0)^(M-1)1{Y_j=s},\n    C_s,c(M)=sum_(j=0)^(M-1)1{Y_j=s,X_(j+3)=c},\n    p_s^+=(C_s+1)/(n_s+K).\n\n每次预测完整观察 X_1^N。最后一个计数后继是 X_N；Y_M 不是额外 departure。actual query 从已观察最后两符号取得；fixed-query 任务另有明确的公开 s。X_(N+1)、theta、mu、支持、闭类、平稳律、未来行栈及隐藏源标签不可见。外部 query 是同一历史下调用的查询参数，不额外赠送干净端点或统计量。获得和复制实际端点在实现中收费。\n\n共同算法族的程序和公开精度可以依赖 K,N,h，不能依赖未知 theta,mu 或其隐藏标签。统计根中的理想 p^+ 是分析变量；给定实现的计数、头输出等实际可见代码由来源实现义务确定，不能据理想表达式新增 readout 端口。比较中的任意全历史预测器可以用全部 X_1^N 和源独立随机种子，输出任意概率向量。具体 Pi 则遵守自己已声明的内部信息切口。\n\nTV(p,q)=1/2 sum_c|p_c-q_c|。对给定 family F，令 Z_N(s)=TV(F_(K,N,h)(X_1^N;s),theta_s)。严格区分：\n\n| 名称 | 定义 | 量词 |\n|---|---|---|\n| fixed row | E Z_N(s) | 固定公开 s |\n| all contexts | E max_(s∈S) Z_N(s)；另可问其 a.s. 极限 | 全 K² 行，不改成访问行 |\n| actual terminal | R_act=E Z_N(E_N) | 同一历史的末尾 query |\n| conditional terminal | E[Z_N(E_N)\\|E_N=s] | 仅当 p_N(s)=mu P^M(s)>0；零概率时未定义 |\n| empirical weighted | E sum_s(n_s/M)Z_N(s) | 同历史频率权重 |\n| other history weighted | E sum_s w_s(X_1^N)Z_N(s) | w 为观察历史可测 simplex；不自动有一致性 |\n\n逐源极限固定 K,theta,mu 后令 N→∞。统一均值是每个 N 的 sup_(theta,mu) R_act；取 supremum 时源可随 N 改选，但一个样本路径内部的核必须齐次。固定 K 的统一结论不是 K 随 N 变化的无条件结论，也不是 changing-source 的统一几乎处处结论。输出允许零坐标，损失仅 TV，本 contract 不把它解释为 positive-output KL。\n\n\n## 共同研究范围的约定\n\n接口I是一个程序性质的定义，不能作为所有算法已经满足的全局假设。条件统计根对任意满足I的共同有限族F证明蕴含式；具体Pi满足I及其完整成本须由SRC-Pi的正常独立来源义务支持，不能在证明SRC-Pi时先假定它。原第二阶段固定证明是可查来源，旧Fact编号不是新项目前驱。\n\n后继真实资源/可靠性命题可以在同一contract内建立独立义务，不必谎称它们是统计根的前提。数据观察及TV实验保持上述定义。每项具体实现须声明自己的内部代码、允许回读、输出格式、参数/字长、batch或streaming等执行方式；比较只在所声明的共同条件下成立。原Pi的finite-attention加pointwise batch hybrid、literal bit/ReLU模块的packed/scalar、sparse/dense选项分别核算，不将一项格式的便宜坐标拼入另一项。\n\n完整费用包括实际head和局部绑定、输入/query/端点取得、参数/零系数、物理字、复制/跨层保持/清除、mask/position、所有活动bank与metadata、online/offline工作和同时峰值。不能免费引入计数、normalizer、译码或生成器。新算术/扰动参数由各精确义务局部量化；改变共同数据律、可见信息或风险须建立新的明确数学范围。\n\n给定接口的条件定理、具体实现定理、训练可达性、必要资源及新颖性是不同主张。数学根只包含数学命题。行政完成程序不是数学前提；独立后续结论不改变已有定理的证明依赖。\n","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]},"statement":"# RATE-K-MINIMAX：合法二阶源族上的一般 K actual TV 下界\n\n这是 RATE-K-LOW 接纳之后的独立算法量词扩展候选，目标是全部共同全历史预测器，不把指定 add-one 的已知源损失冒充 minimax。旧 G/U、SRC、RATE-TV、K3 与 K-LOW 均保持接纳及原有依赖，不增加逆向前提。Lead 候选和 Counter 报告不是 Fact；本合取需完整证明与正常独立网关。\n\n对每个整数 K>=2、M>=1，N=M+2，字母表为 {0,...,K-1}。theta 是任意齐次二阶转移表，允许零边；mu 为任意初始对律。令 Y_i=(X_(i+1),X_(i+2))，0<=i<=M；观察完整 X_1^(M+2)，actual target 是 theta_(Y_M)。一条实验内 theta 固定，sup 可随 (K,M) 改选源。\n\n令 A_(K,M) 遍历所有共同、可能随机的全历史概率预测器：其输入只有已观察历史和公开 K,M，可计算 actual query，但不得读隐藏 theta,mu 或未来符号。算法的随机种子与源独立；算法可依 K,M 选择，且输出在 K-simplex 上。定义\n\n    R_min(K,M)=inf_A sup_(theta,mu)\n        E_(theta,mu,A) TV(A(X_1^(M+2)),theta_(Y_M)).\n\n拟证明全部有限参数上的\n\n    R_min(K,M)>=2^(-12) min{1,sqrt(K^3/(M+1))}.        (MM)\n\n这是同轨迹 actual 的均值风险，非 fixed row、最大行、时间平均或额外独立测试实验。证明中允许在一个具体合法源族内导出末对的独立性，但必须从原二阶路径律严格证明，不能为一般源额外假设独立 query 或条件 iid。\n\n## 1. 拟用的合法有限源族及全余数初始化\n\nK>=6 时，置 q=floor(K/3)>=2、r=floor(q/2)。取三个互不相交的字母组 U,V,W，各有 q 个字母；余下字母的质量可为零。对每个 (u,v)∈U×V、j=1,...,r，取未知符号 sigma_(u,v,j)∈{-1,+1}。将 W 中前 2r 个字母分为 r 对，取公开 0<alpha<=1/2，定义\n\n    theta_(u,v)(w_(2j-1))=(1+alpha sigma_(u,v,j))/q,\n    theta_(u,v)(w_(2j))  =(1-alpha sigma_(u,v,j))/q.\n\n若 q 为奇数，剩下的一个 W 字母概率为 1/q；组外概率为零。对所有 (v,w)∈V×W，theta_(v,w)=Unif(U)；对所有 (w,u)∈W×U，theta_(w,u)=Unif(V)。其余未到达 pair 给任一固定合法概率行。完整证明须检查归一化、shift 约束、未到达行及同一齐次表。\n\n写 M=3n+d，d∈{0,1,2}。初始化不依 sigma：d=0 时 mu=Unif(U)⊗Unif(V)；d=1 时 mu=delta_(w_*)⊗Unif(U)；d=2 时 mu=delta_(v_*)⊗delta_(w_*)，其中公开 v_*∈V,w_*∈W。应严格证明已观察历史等价于 n=floor(M/3) 个独立 block (U_i,V_i,W_i)，其中 (U_i,V_i) 独立 uniform 于 U×V，W_i 条件律为 theta_(U_i,V_i)，加上一个与全部训练 block 独立的 uniform 末对 (U_(n+1),V_(n+1))。d=1,2 的初始固定前缀不携带 sigma 信息；n=0 也必须覆盖。这个等价是原始完整轨迹的精确表示，没有删除信息或更换风险实验。\n\n## 2. 未知符号测试与常数\n\n可取 alpha=min{1/2,(1/8)sqrt(q^3/(n+1))}。相邻符号向量仅翻转一个 (u,v,j) 时，完整训练 block 的 KL 必须从实际路径律计算；候选给不超过 8n alpha^2/q^3。实际末对和固定前缀不能引入未计的信息。\n\n对实际末对为 (u,v) 的每个符号对，预测器两个 W 坐标的顺序可用作 sigma_(u,v,j) 的测试；错误顺序使该对的 TV 贡献至少 alpha/q。需要严格处理任意随机预测器、ties、实际末对条件下的观察律、符号平均与所有 q² 行的权重，不能把不同源风险直接相加后声称同一见证。标准两点测试不等式及所用 KL-TV 控制须明确证明或给准确可核版本。\n\n预期由此先得 q>=2 时的保守下界\n\n    R_min(K,M)>=(1/64) min{1,sqrt(q^3/(n+1))}.\n\n再由 q>=K/6 与 n+1<=M+1推出 (MM)。对于 2<=K<=5，可只用本项目 G/U Fact a12539a93d9f1ee3 已接纳的任意共同算法 iid actual 下界 1/(16sqrt(M+2))，明确比较有限常数以补齐 (MM)。该 Fact 是此候选唯一必需的当前项目 Fact 前驱；高 K 源族和测试论证须自足，不能依赖 K-LOW 的指定估计器 lower。\n\n## 3. 准确推论和范围\n\n(MM) 若成立，则任何共同算法在该完整源类上达到统一 actual 均值风险 tau，0<tau<2^(-12)，必须有\n\n    M+1>=2^(-24) K^3/tau^2.                          (sample necessity)\n\n这只是统计样本量必要条件，不是内部 bit 数、层数、宽度、算术工作或资源最优性的下界。它覆盖实际 Pi 和 strong direct 作为全历史算法的子类，但不额外声称它们的实现费用，也不需要 SRC 作统计 lower 前提。\n\n与已有 K3 upper 比较仍留下 K^(3/2) 与 K^3 的差距，不宣称 sharp K 或 minimax 完整匹配。未知源可依算法/参数选择，不能称一个固定源同时使所有算法失败。初始化依 M 的余数是合法的每 horizon supremum，不称同一 mu 在全部 M 同时实现该界。分组嵌入、两点测试、KL/TV 工具不作首创声称；直接 primary 的同范围先例仍需核对。本义务不重做 count-snap、二元故障或模块费用，也不宣告 v10 完成。"}

Admitted prerequisite interfaces (use only within the recorded scopes):
[{"exact_statement":"## B. 条件接口 I 与精确根声明\n\n给定任意共同确定有限预测器族 F，合法精度为整数\n\n    h>=h_0(M):=max(4,ceil(log2 M)+1), Q=2^h.\n\n假定每条有限历史 x_1^N∈A^N、每个 s∈S、每个合法 h，输出均为概率向量，并满足以下**确定性程序接口**：\n\n    TV(F_(K,N,h)(x_1^N;s),p_s^+(x_1^N))\n       <=78KM/[Q(n_s(x_1^N)+K)]+(K-1)/Q.             (I)\n\nI 包括零计数以及与某一 theta 的支持不相容的历史；不是对数据分布增加正性、混合或可访问性的假设。该条件统计命题不声称任何满足 I 的族都具有 Pi 的成本。实际 Pi 满足 I 及其完整实现成本应由独立正常来源义务证明，见 `inputs/source-v10/outputs/005-native-general-handoff/lead/source-dependencies-v1.md`。\n\n精确数学根命题为：**对上述每个 K 和每个满足 I 的共同有限族 F，下面 G1–G6、G7 的统计转移部分及 U1/UC/U2 全部成立。** 对渐近 G1–G6（注明有限 N 部分除外）使用同一个公开序列\n\n    h_N=ceil(log2(128(K+1)(N+1)^3)), e_N=(N+1)^(-2).\n\n由 I，全路径、全 query 的 F 与 p^+ 的 TV 差至多 e_N。G7 中原 Pi 的实际构造存在性和完整成本不从 I 推出，明确移交 SRC-Pi 来源义务；原 G7 未变文件仍完整保留。这是用户允许的条件统计根，不是把原 G7 的成本结论暗中删除后宣称整个实际网络已被接纳。\n\n### G1：同一观察事件上的有限 N 风险界\n\n对每个合法 h、0<alpha<1，写自然对数\n\n    A_alpha=K ln2+ln(2K²M/alpha),\n    g(0)=1,\n    g(j)=min(1,sqrt(A_alpha/(2j))+(K-1)/(j+K)\n                 +78KM/[Q(j+K)]+(K-1)/Q), j>=1.\n\n存在观察历史可测事件，概率至少 1-alpha，在其上全部 s 同时有 Z_N(s)<=g(n_s)。所以 fixed、all、actual、任意观察历史权重的期望分别由 E g(n_s)、E max_s g(n_s)、E g(n_(E_N))、E sum_s w_s g(n_s)，各加 alpha 后与 1 取小控制。对 p_N(s)>0、整数 v>=1，\n\n    E[Z_N(E_N)|E_N=s]\n      <=min(1,g(v)+(alpha+P(E_N=s,n_s<v))/p_N(s)).     (G1-C)\n\n行栈证明只对确定栈长度使用 iid 界，再取联合事件；不能条件于随机 n_s 或 E_N 后称样本 iid。\n\n### G2：逐源 actual 一致性及有限访问行精确极限\n\n对每个固定 theta,mu，有限对链 a.s. 在有限时间 tau 进入一个随机闭不可约类 C_infty。所有行同时有 Z_N(s)→ell_s a.s.，其中\n\n    ell_s=0                                  if s∈C_infty;\n    ell_s=TV((C_s(infinity)+1)/(n_s(infinity)+K),theta_s)\n                                             if s∉C_infty.\n\n第二行计数 a.s. 有限。任意固定非空 S0⊆S 的最大误差 a.s./L1 趋向 max_(s∈S0)ell_s。因此在给定 theta,mu 上，该集合一致当且仅当其所有有限访问行的最终 add-one 向量 a.s. 恰等于真实行。尤其\n\n    max_(s∈C_infty)Z_N(s)→0 a.s./L1,\n    Z_N(E_N)→0 a.s., R_act→0,\n    E sum_s(n_s/M)Z_N(s)→0.\n\n随机进入的类不等于所有可能进入类的并。实际末尾一致性不要求正性、平稳初始化、全链不可约、非周期或唯一平稳分布。\n\n### G3：actual conditional 风险的正确范围\n\n固定 theta,mu，若常返 s 所在闭类从 mu 可达，则存在 c_s>0、M_s，使 M>=M_s 且 p_(M+2)(s)>0 时 p_(M+2)(s)>=c_s。沿所有充分大的可条件化时刻，E[Z_N(E_N)|E_N=s]→0。证明覆盖周期类的全部正质量入口余数；不只挑单一相位。暂态 s 不在此结论内：其条件风险可以失败，也可以因有限访问 add-one 恰好正确而成功。均值趋零不能自动除以趋零条件概率。\n\n### G4：任意初始下有限 N 访问控制\n\n令 eta_mu(b)=P(tau>b)。若每个闭类内从任意起点，在 L 个连续状态（含起点）内命中任意指定类内 s 的概率至少 a>0，则对于 0<=b<M，\n\n    B=floor((M-b)/L), v=floor(aB/2)>=1:\n    R_act<=min(1,g(v)+alpha+eta_mu(b)+K² exp(-aB/8)).  (G4-F)\n\n固定源的一组保守参数为 D=K²、p_* 为正边最小值、L=D、a=p_*^(D-1)，eta_mu(b)<=(1-p_*^D)^floor(b/D)。它们仅用于证明，不交给算法。不可约时取 b=0，亦得全 query maximum 同类界。\n\n闭不可约类内 Poisson 方程 (Id-P_C)f_s=1_s-pi_s^C 可解；H_s=osc(f_s)。任意类内初始 nu、m>=1，\n\n    E_nu n_s(m)-m pi_s^C=nu f_s-nu P_C^m f_s,\n    P_nu(|n_s(m)-m pi_s^C|>H_s+x)\n        <=2 exp(-2x²/(m H_s²)), H_s>0,x>0.\n\nH_s=0 用确定性情形；去掉初始 b 段后比较整段 M pi_s 另付 b 边界与 eta_mu(b)。不假设非周期或可逆。\n\n### G5：全 K² 一致性的结构分类\n\n对固定 theta，满足 I 并使用 h_N 的族对**所有初始 mu**都有全 K² a.s./L1 一致性，当且仅当对链不可约。对指定 mu 不作这个必要性结论。\n\n若有至少两个闭类，每条合法历史至少有一个闭类从未访问；该真闭类存在某行一个后继概率为零，所以对每个 N，max_s Z_N(s)>=1/K-e_N。唯一全链平稳律因而是本 add-one 近似族全行一致性的必要但非充分条件；它不是 actual 风险一致性的必要条件。若只有一个真闭类，类外非均匀行可从类内初始化使之失败；若类外全均匀，可从类外沿正概率简单路径一次访问后进入闭类，仍产生错误的有限 add-one 极限。\n\n### G6：边界证据及精确不可能性\n\n1. K=2、从吸收 00 开始的两个源可有相同全零历史而 11 行分别 delta_0、delta_1。任意共同随机算法的两源 fixed-11 风险之和>=1；至少一固定源的 limsup>=1/2。这不否定 actual 一致性。\n2. 00=(p,1-p)，01→11，11 吸收，初始 00，0<p<1；在 E_N=00 上概率 p^M，全部已见 00 后继为 0，条件风险趋 1-p。此时 actual 均值仍趋零。合法周期 00→01→11→10→00 给非周期非必要，并保留零概率条件时刻未定义。未访问行刚好均匀的正例保留。\n3. 对每个 M 取 epsilon=1/(16M)，00=(1-epsilon,epsilon)，01=10=(1/2,1/2)，11=(a,1-a)，a=1/4 或 3/4；分别以 pi∝(1,2epsilon,2epsilon,epsilon/a) 初始化。两源全零历史质量各至少 5/8，故任意共同随机算法的两源最大 fixed-11 风险至少 5/32。这是每 N 的类 supremum 下界，源随 N 变化；该同族 F 的 actual 风险却至多 59/(16M)+e_N。\n4. 所有其他已审暂态成功/失败、多入口周期、随机闭类反例按原 Counter 的完整表保留，不能合并不同示例的行。K 随 N 增长的例子仅为 K 无关速率的边界证据。\n\n### G7 的统计转移与实现义务的边界\n\n改变合法历史的概率律不改变给定历史对应的程序输出或费用。只要另行正常证明具体 Pi 全路径满足 I，上述 G 及以下 U 可直接实例化到同一个 Pi。直接 add-one 的统计证明也成立；它的有限前端和输出运算另行收费。**实际 Pi 存在、SRC-Pi 完整成本、与强 direct 基线的成本比较，均不是 I 单独的逻辑后果，不属于本条件根已经完成的内容。**\n\n### U1/UC：统一实际末尾占用与可计算模\n\n对整数 v>=1、m>=0，定义\n\n    B_(m,v)(P)=max_y P_y(n_(Y_m)(m)<v),\n    beta_(K,v)(m)=sup_theta B_(m,v)(P_theta).\n\nB 随 m 非增；个别初始态的概率未必非增。确定路径的 first-v charging 与 max_y<=sum_y 给\n\n    beta_(K,v)(m)<=min(1,K^4 v/(m+1)).               (UC)\n\n不以错误的 sum max<=max sum 把 K^4 降成 K²。另有含退化表的紧性证明给固定 K,v 的 beta→0。对 0<epsilon<1，\n\n    A_K(v,epsilon)=min(1,2^(K+1)K² exp(-2v epsilon²)\n                                /(1-exp(-2epsilon²))),\n    rho_K(M)=min(1,inf_(1<=v<=M,0<epsilon<1)\n       [epsilon+(K-1)/(v+K)+A_K(v,epsilon)+beta_(K,v)(M)]).\n\nrho_K 非增且趋零，并可计算到任意给定正有理绝对误差：分母 L 的有限转移表格最大值 b_grid 满足 b_grid<=beta<=min(1,b_grid+m(K-1)/L)，再在远离 epsilon=0 的公开紧区间作有限区间计算。这里只断言有限可计算性，不给免费或实用计算成本。对 h_N，sup_(theta,mu)R_act<=min(1,rho_K(M)+e_N)。从而对固定 K 有统一均值及统一依概率一致性，不推出统一 a.s.，不扩为 fixed/all/conditional 统一一致性。\n\n### U2：显式粗率及同目标下界\n\n令 J=n_(Y_M)(M)，c=K^4/(M+1)，H(c)=1（c>=1），H(c)=c(1+ln(1/c))（0<c<1）。则对全 theta,mu，\n\n    P(J=0)<=min(1,c), E[1/(J+K)]<=H(c),\n    E[1{J>=1}/sqrt(J)]<=2sqrt(2c).\n\n置 A=K ln2+ln(2K²M(M+1))，\n\n    S_K(M)=min(1,min(1,c)+2sqrt(Ac)+(K-1)H(c)+1/(M+1)),\n    sup_(theta,mu) E TV(p^+_(Y_M),theta_(Y_M))<=S_K(M),\n    U_K(M,Q)=min(1,S_K(M)+(78KM H(c)+K-1)/Q),\n    sup_(theta,mu)R_act(F_h)<=U_K(M,Q).              (UQ)\n\nh_N 下可用 min(1,S_K(M)+e_N)。最低合法 h_0 下 Q>=2M，有 min(1,S_K(M)+39K H(c)+(K-1)/(2M)) 的上界；固定 K 均为 O_K(sqrt(log(M+1)/(M+1)))。h_0 不声称与 h_N 逐位相同，也不自动继承有限访问外部行的精确极限分类。\n\n任意 N>=3、K>=2、任意共同随机全历史预测器，某个合法 iid 源的 actual 均值风险至少 1/(16sqrt(N))。可取所有行相同的 Bernoulli 参数 1/2±1/(8sqrt(N))，初始对为 iid；K>2 时其余符号零质量。每 N 选择一个见证，不称存在同一源在全部 N 同时达到下界。\n\n若每次最终输出在分母 R=2^b、b>=1 的 simplex 网格，另有某 iid 源逐输出 TV>=1/(2R)。这是输出格式界，不是内部精度/层数/宽度界；不能与统计下界相加并声称同一见证。前 K-1 坐标 floor、末坐标补残差的 F_R 满足 TV(F_R(q),q)<=(K-1)/R，实际模块需付完整实现成本。\n\n**保留的数学缺口：** sqrt(log N) 是否可去、sharp K 依赖、最优资源—风险关系均未决。不能把固定 K 上下界指数相近称为已匹配的 sharp rate，不能由特殊 iid、稀有 row 或有限 code 下界推出整个 Transformer 类的最优性。\n\n","fact_id":"a12539a93d9f1ee3","scope_bindings":[{"evidence_id":"7cea58dd50e9a72f962471a58a902c35fa2a5eb09d1c3e903e50b9417b08a9f0","obligation_id":"a92235561a82e3ac845de304718b82c944869ccc236c5d248be1f24b25cdac3b","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]}}],"source_hash":"94f8cb48a2a96dba050584d9c200c8b8eb7c59335c77ae1c8d9fefc6b1240cba"}]

Proof:
# RATE-K-MINIMAX：合法齐次二阶源族上的 actual TV 下界完整证明

义务：b6e7db977d423f7b01c0b85da8246c76747f0a49c2b8de136bc623efcf586a91。

冻结声明：outputs/011-k-minimax/lead/minimax-statement-v1.md，文件 SHA256 为 d0741b690cd6155bc54f77f2a0ed019a5a49528963463e3a6ab10bff3874dcb9。已与原生 exact_statement 逐字核对，文件仅多末尾换行；原生声明 SHA256 为 e0d712e1027d7bce378dc6c38c4cf28f9b904b224699761bdd043fd5e1fe6c5d。

唯一当前项目 Fact 前驱为 **a12539a93d9f1ee3**，其正常接纳 Evidence 为 7cea58dd50e9a72f962471a58a902c35fa2a5eb09d1c3e903e50b9417b08a9f0。只在第 7 节使用该 Fact 的 U2：每个 K>=2、N>=3 和每个共同随机全历史预测器，都有一个合法 iid 源使 actual 均值 TV 至少为 1/(16 sqrt(N))。高 K 的源族、完整路径分解、随机测试及 KL–TV 控制全部在下文证明。Lead 候选、Counter 报告和有界计算不作为前提；K-LOW、SRC、RATE-TV、K3 均不是本证明的项目 Fact 前驱。合同中的接口 I 不是对任意共同算法的额外假设，本证明不使用它。

## 1. 定理、实验及量词

固定任意整数 K>=2、M>=1，N=M+2，字母表 A={0,...,K-1}。源为齐次二阶表 theta 和初始对律 mu；允许零边和任意 mu。观察 H=(X_1,...,X_(M+2))，Y_i=(X_(i+1),X_(i+2))，实际待预测分布为 theta_(Y_M)。已观察的 M 次 departure 为 i=0,...,M-1，尚未观察 X_(M+3)。

一个共同预测器 A 可依公开 K,M 选择，使用全部 H 并输出 K-simplex 中的概率向量。其私有随机化与源实验独立；等价地，每个给定历史的输出概率核在所有源下相同。没有 theta、mu 或未来符号输入。设

    R(A;theta,mu)=E_(theta,mu,A) TV(A(H),theta_(Y_M)),
    TV(p,q)=(1/2) sum_c |p_c-q_c|,
    R_min(K,M)=inf_A sup_(theta,mu) R(A;theta,mu).

我们证明原声明的

    R_min(K,M) >= 2^(-12) min{1,sqrt(K^3/(M+1))}.       (MM)

对 K>=6，还证明声明中的中间界：q=floor(K/3)、n=floor(M/3) 时，

    R_min(K,M) >= (1/64) min{1,sqrt(q^3/(n+1))}.       (Q)

证明对每个给定算法先取合法源族的风险平均，再以类 supremum 控制这个平均。因此无需交换 infimum 与 supremum，也不需要一个源同时使所有算法失败。整个证明始终使用同轨迹 actual 风险。

## 2. 三组源族是合法的同一齐次二阶表

现在令 K>=6，q=floor(K/3)>=2，r=floor(q/2)，取互不相交的 U,V,W，各有 q 个字母；W 标为 w_1,...,w_q。所有组和标号均公开。将其余 K-3q 个字母保留在字母表中，但不赋予可达输出质量。

令索引集

    I=(U×V)×{1,...,r},  B=|I|=q²r,
    sigma=(sigma_(u,v,j))_(I) in {-1,+1}^B.

暂取任意公开 0<alpha<=1/2。对 (u,v) in U×V，定义

    theta^sigma_(u,v)(w_(2j-1))=(1+alpha sigma_(u,v,j))/q,
    theta^sigma_(u,v)(w_(2j))  =(1-alpha sigma_(u,v,j))/q,
                                         j=1,...,r.       (2.1)

若 q 为奇数，再令 theta^sigma_(u,v)(w_q)=1/q；W 外概率为零。每对坐标总质量是 2/q，余下的质量在奇数 q 情形恰为 1/q。因此每行归一化为 1，且 W 上全部坐标至少为 1/(2q)>0。

对 (v,w) in V×W，令 theta^sigma_(v,w)=Unif(U)；对 (w,u) in W×U，令 theta^sigma_(w,u)=Unif(V)。其他 pair 一律给固定的 delta_(u_* )，其中 u_* in U 公开且不依 sigma。三类已指定 pair 互不相交，所以转移表没有冲突，全部 K² 行都有定义。

pair 链按原二阶规则

    (a,b) -> (b,c), 概率为 theta^sigma_(a,b)(c).

由上述支持，三类 pair 依次循环：

    U×V -> V×W -> W×U -> U×V.                       (2.2)

这严格符合 shift 约束；它是一个时间齐次表。未知 sigma 固定在整个实验中，时间相位由当前 pair 类型决定，未使用随时间改变的转移规则。下述初始 pair 均在这三类内，所以其他 pair 和多余字母不可达。零边、可能的周期性和这些初始律都属于原声明允许的源类。

## 3. 三种余数下完整观察的精确路径分解

写 M=3n+d，d in {0,1,2}。公开固定 v_* in V、w_* in W。取不依 sigma 的初始化

    d=0: mu_0=Unif(U) tensor Unif(V);
    d=1: mu_1=delta_(w_*) tensor Unif(U);
    d=2: mu_2=delta_(v_*) tensor delta_(w_*).

令 D=(B_1,...,B_n)，B_i=(U_i,V_i,W_i)，并记 S=(U_(n+1),V_(n+1))。完整历史有以下唯一格式：

    d=0: (U_1,V_1,W_1,...,U_n,V_n,W_n,U_(n+1),V_(n+1));
    d=1: (w_*,U_1,V_1,W_1,...,U_n,V_n,W_n,U_(n+1),V_(n+1));
    d=2: (v_*,w_*,U_1,V_1,W_1,...,U_n,V_n,W_n,U_(n+1),V_(n+1)).
                                                               (3.1)

更精确地，第 i 个完整 block 的位置为

    (X_(d+3i-2),X_(d+3i-1),X_(d+3i)), 1<=i<=n,

而 S 占位置 3n+d+1=M+1 和 M+2。故 S **就是原 actual pair Y_M**。每个完整 block 中的 W_i 由 UV 行产生；这些 departure 的编号为 d+3(i-1)，都在 0,...,M-1 中。S 所对应的下一次 UV 输出尚未观察。

对任意指定 b_i=(u_i,v_i,w_i) 和 s=(u_(n+1),v_(n+1))，用初始律乘全部 M 次转移概率，得到

    P_sigma(D=(b_1,...,b_n), S=s)
      = q^(-2(n+1)) product_(i=1)^n theta^sigma_(u_i,v_i)(w_i)
      = [product_(i=1)^n b_sigma(b_i)] q^(-2),        (3.2)

其中

    b_sigma(u,v,w)=q^(-2) theta^sigma_(u,v)(w).

现逐项核对初始的 q^(-2) 因子和末尾，而不假设独立性：

- d=0 时，初始 U_1,V_1 已独立均匀，给出 q^(-2)。
- d=1 时，初始 U_1 给出 1/q，从 (w_*,U_1) 出发的第一步产生均匀 V_1，再给出 1/q。开头固定的 w_* 没有未知信息，随机 U_1 已计入 (3.1)，没有删去。
- d=2 时，初始 (v_*,w_*) 固定；前两步依次产生均匀 U_1,V_1，仍给出 q^(-2)。
- 每次由 (U_i,V_i) 产生 W_i，付 theta^sigma_(U_i,V_i)(W_i)。随后两次 reset 分别产生 U_(i+1)、V_(i+1)，每次概率 1/q，不依已出现的 W_i 或更早历史。最后两次 reset 正好给出实际末对 S。

因此每个固定 sigma 下，D 中的 n 个 block 相互独立、同律为 b_sigma；S 在 U×V 上均匀，且独立于全部 D。这个独立性是 (3.2) 的结论，不是对一般二阶源增加的假设。对 sigma 取混合后，不需要、也不声称训练 block 仍独立。

令 H_d(D,s) 为 (3.1) 的拼接。所有 b_i in U×V×W 和 s in U×V 的组合在每个 sigma 下概率都正。H_d 在这些组合与原源族全部正概率历史之间是双射：去掉已知的 d 个固定前缀字母，按位置读出全部 n 个 block 和最后两个字母即可逆转。所有其他历史在全部 sigma 下概率为零。因此 D,S 连同公开固定前缀精确表示原算法获得的**全部**观察，既没有删除信息，也没有新增独立测试实验。

n=0 时，M>=1 只可能有 M=1,d=1 或 M=2,d=2。(3.1) 分别变成 (w_*,U_1,V_1) 或 (v_*,w_*,U_1,V_1)；D 是唯一的空序列，S 均匀且不含 sigma 信息，(3.2) 按空积 1 仍成立。

## 4. 有限分布的测试与 KL–TV 工具

以下给出所用工具的短证明。对同一有限集合上的分布 P,Q，记

    KL(P||Q)=sum_x P(x) ln(P(x)/Q(x)),

按通常的零概率约定；若 P 对 Q 不绝对连续则 KL=+infinity。所有对数为自然对数。

### 4.1 任意随机测试

设测试在观察 x 后以概率 t(x) in [0,1] 输出 +，其余概率输出 -；这个 t 在两种源下是同一个函数。则

    P(test=-)+Q(test=+)
      =1-sum_x (P(x)-Q(x)) t(x)
      >=1-TV(P,Q),                                  (4.1)

因为最后的带权和至多 sum_(P>Q)(P-Q)=TV(P,Q)。此式直接涵盖任意私有随机化。把共同算法的随机种子积分掉即可得到 t；无需让算法确定性化，也无需对随机种子引入任何 source-dependent 律。

### 4.2 Pinsker 控制的短证明

先证明 log-sum：若 a_i,b_i>=0，A=sum_i a_i>0、B=sum_i b_i>0，则

    sum_i a_i ln(a_i/b_i) >= A ln(A/B).               (4.2)

在有限左端的情形，令 p_i=a_i/A、q_i=b_i/B。由 -ln x>=1-x，对 p_i>0 的项求和得

    sum_i p_i ln(p_i/q_i)
      >=sum_(p_i>0)(p_i-q_i)>=0,

故得 (4.2)；无限值及零总和的边界按连续性或定义处理。

令 E={x:P(x)>=Q(x)}，a=P(E)、b=Q(E)，则 a-b=TV(P,Q)。把 E 及其补集分别应用 (4.2)，得到

    KL(P||Q)>=a ln(a/b)+(1-a) ln((1-a)/(1-b))=:g_b(a).

当 0<b<1 时，g_b(b)=g_b'(b)=0，且

    g_b''(a)=1/[a(1-a)]>=4,  0<a<1.

对二阶导数积分（或带积分余项的 Taylor 公式）即得 g_b(a)>=2(a-b)²；a=0,1 时用连续性。b=0,1 时，有限 KL 要求对应 a=b，其他情形 KL 无穷，结论同样成立。因此

    TV(P,Q)<=sqrt(KL(P||Q)/2).                       (4.3)

这两个工具只在下文的有限训练数据空间上使用，无额外集中或条件 iid 前提。

## 5. 邻点的完整路径 KL 与实际末对条件律

设 sigma、sigma' 只在 t=(u,v,j) 这一个符号上相反。两种单 block 分布仅在 (u,v,w_(2j-1)) 和 (u,v,w_(2j)) 两点上不同。无论翻转方向如何，直接计算得到

    KL(b_sigma||b_sigma')
      = (2 alpha/q³) ln((1+alpha)/(1-alpha))
      <= 8 alpha²/q³.                               (5.1)

确实，两个概率是 (1+alpha)/q³ 和 (1-alpha)/q³ 的交换；相应 KL 为其差乘对数比。又

    ln((1+alpha)/(1-alpha))
      = integral_(-alpha)^alpha 1/(1+t) dt
      <= 2alpha/(1-alpha)<=4alpha

适用于 0<alpha<=1/2。奇数 q 未配对的坐标完全相同，没有遗漏。

记 P_sigma=b_sigma^(tensor n) 为训练数据 D 的律（n=0 时是点质量）。对 n 个 block 的对数似然比按 i 相加，再取期望，由 (3.2) 得

    KL(P_sigma||P_sigma')=n KL(b_sigma||b_sigma')
                         <=8n alpha²/q³.            (5.2)

原完整历史 H 的 KL 也恰等于此值：在 (3.2) 的概率比中，S 的 q^(-2) 因子抵消；双射 H_d 不改变求和；固定前缀没有随机似然贡献。该计算包括全部观察，不是数据处理产生的一个方向的近似。

特别，对于每个实际末对 s in U×V，

    P_sigma(S=s)=1/q²,
    Law_sigma(D | S=s)=P_sigma.                      (5.3)

同一个 s 在所有 sigma 下均有正质量。条件化只使用已经证明的源族因子分解 (3.2)，没有把一般随机访问数或一般实际末行条件化成 iid。完整算法仍可使用 S 和全部前缀。

现在取声明指定的

    alpha=min{1/2, (1/8)sqrt(q³/(n+1))}.             (5.4)

alpha 始终正，且 alpha²<=q³/[64(n+1)]，包括 alpha=1/2 的分支。于是

    KL(P_sigma||P_sigma')<= n/[8(n+1)]<=1/8,
    TV(P_sigma,P_sigma')<=1/4.                       (5.5)

n=0 时 KL、TV 均为零。这里没有要求 n 或某行的样本数大于零；各行出现次数全部保留在完整训练律中。

## 6. 从随机预测器得到每个未知符号的测试

固定任意共同预测器 A。对给定 D、s，令

    a=A(H_d(D,s))

为其随机输出向量。对 s=(u,v) 和每个 j=1,...,r，定义测试

    T_(s,j)=+1 当 a_(w_(2j-1))>=a_(w_(2j));
    T_(s,j)=-1 当 a_(w_(2j-1))< a_(w_(2j)).          (6.1)

ties 统一判作 +1。这是依赖完整观察和算法私有随机化的共同测试，不读取 sigma。真实两个坐标的差是 2alpha sigma_(s,j)/q。若 T_(s,j)≠sigma_(s,j)，则预测差与真实差的次序相反或在错误的 tie 情形等于零。因此

    |a_(w_(2j-1))-theta^sigma_s(w_(2j-1))|
      +|a_(w_(2j))-theta^sigma_s(w_(2j))|
       >= |[a_(w_(2j-1))-a_(w_(2j))]
               -2alpha sigma_(s,j)/q|
       >= 2alpha/q.                                 (6.2)

具体地，sigma=+1 的错误要求预测差严格为负；sigma=-1 的错误允许预测差为零，此时 (6.2) 仍成立。sigma=+1 的 tie 判对，只是不计入错误项，并不会破坏下界。

各 j 使用互不相交的 W 坐标，故可在同一个源、同一个输出上相加：

    TV(a,theta^sigma_s)
       >= (alpha/q) sum_(j=1)^r 1{T_(s,j)≠sigma_(s,j)}.    (6.3)

输出可以在 W 外分配质量或为零，均不影响此不等式；其他坐标的 TV 贡献只是非负量。

令

    e_(s,j)(sigma)=P_(D~P_sigma,A)(T_(s,j)≠sigma_(s,j)).

这是将 actual pair 固定为 s 后，用 (5.3) 给出的训练律及原算法随机化计算的错误概率。对固定 (s,j)，先固定所有其他 B-1 个符号，令 P_+、P_- 为该符号分别取 +1、-1 的训练律。在相同 D,s 上，算法的输出核和 (6.1) 的判决规则相同，因而 (4.1)、(5.5) 给出

    e_(s,j)(sigma_+) + e_(s,j)(sigma_-)
       >=1-TV(P_+,P_-)>=3/4.                        (6.4)

对全部 2^B 个 sigma 等权平均，配对这两个相邻端点，即得

    2^(-B) sum_sigma e_(s,j)(sigma) >=3/8            (6.5)

对所有 s,j 成立。随机算法的 t(D) 是在固定 s 后对私有随机化积分得到的；这里不需要、也未假设算法在各行的输出或各个测试彼此独立。

令 R_sigma(A)=R(A;theta^sigma,mu_d)。由精确 actual 末行权重 (5.3) 和 (6.3)，

    R_sigma(A)
      = (1/q²) sum_(s in U×V)
            E_(P_sigma,A) TV(A(H_d(D,s)),theta^sigma_s)
      >= (alpha/q³) sum_s sum_(j=1)^r e_(s,j)(sigma).

再对 sigma 等权平均，使用 (6.5) 及 |U×V|=q²，得到

    2^(-B) sum_sigma R_sigma(A)
      >= (alpha/q³) q² r (3/8)
       = 3alpha r/(8q)
      >= alpha/8.                                   (6.6)

最后一步因为 r/q>=1/3：偶数 q 时为 1/2，奇数 q>=3 时 (q-1)/(2q)>=1/3。这同时覆盖 q=2 与最小奇数 q=3。

任意有限集合的风险平均不超过其中最大风险。因此对每个 A，

    sup_(theta,mu) R(A;theta,mu)
       >=max_sigma R_sigma(A)
       >=2^(-B) sum_sigma R_sigma(A)
       >=alpha/8.                                   (6.7)

这是有限先验平均给出的最坏源下界，不是把不同源的风险相加后声称一个源承担其总和。至少一个 sigma 可依赖 A,K,M；同一个 sigma 仍在该实验整条轨迹中保持不变。

设 x=sqrt(q³/(n+1))。由 (5.4)，

    alpha=min{1/2,x/8}>=(1/8)min{1,x}.

在 (6.7) 对全部共同随机预测器取 infimum，就证明 (Q)：

    R_min(K,M)>=(1/64)min{1,sqrt(q³/(n+1))}.

## 7. 全部 K,M 的有限常数

对 K>=6，K/3>=2，故 floor(K/3)>=K/6；同时 n+1<=M+1。于是，记 y=sqrt(K³/(M+1))，

    sqrt(q³/(n+1)) >= y/sqrt(216).

对任意 y>=0 和 0<b<=1，有 min{1,by}>=b min{1,y}，分 y<=1、y>1 两种情形即可核对。结合 (Q)，

    R_min(K,M)
       >=1/[64 sqrt(216)] min{1,y}
       >=2^(-12) min{1,y},                           (7.1)

因为 sqrt(216)<64，故 64 sqrt(216)<4096。这里留有明确的常数余量，并不以渐近符号替代有限比较。

对 2<=K<=5，使用唯一前驱 a12539a93d9f1ee3 的已接纳 U2 iid actual 下界。它的量词是任意共同随机全历史预测器，适用于这里的算法类；N=M+2，合法 iid 源可嵌入 K 字母表，其他符号质量为零。因此

    R_min(K,M)>=1/[16 sqrt(M+2)].                    (7.2)

下面的比较对全部 M>=1 成立：

    1/[16 sqrt(M+2)]
       >=(1/4096) sqrt(K³/(M+1)).

两边平方并整理后，所需条件为

    K³ <= 65536 (M+1)/(M+2).

而 K³<=125，(M+1)/(M+2)>=2/3，且 125<65536·(2/3)，故条件成立。右端再与 1/4096 取小只会降低所需下界。由 (7.1)、(7.2)，原 (MM) 对全部整数 K>=2、M>=1 得证。

这个拼接仅在小 K 区间使用已接纳 iid lower。高 K 下界不依赖指定 add-one 的风险，也不依赖任何程序接口、上界或资源结论。

## 8. 样本必要条件及结论的准确范围

若一个共同算法在完整源类上满足

    sup_(theta,mu) R(A;theta,mu)<=tau,
    0<tau<2^(-12),

由 R_min<=sup R(A) 和 (MM)，有

    2^(-12) min{1,sqrt(K³/(M+1))}<=tau<2^(-12).

因此饱和分支不可能，必有 sqrt(K³/(M+1))<1，并且

    2^(-12) sqrt(K³/(M+1))<=tau.

平方、整理得到原声明的有限必要条件

    M+1 >= 2^(-24) K³/tau².                         (sample necessity)

此处只有统计样本量的必要性，没有内部 bit 数、层数、宽度、算术工作、完整实现费用或资源最优性的推论。实际 Pi 和 strong direct 若视为共同全历史算法的子类，自然也受该统计下界限制；这不需要 SRC 作本 lower 的前提，也不另行赋予它们任何实现费用结论。

所得风险是原完整历史的 actual 均值 TV。源族中 S 与 D 的独立性已经由齐次二阶路径律证明，仅用于该具体族；对一般源没有独立 query、条件 iid 或随机样本数重置假设。初始化按 M mod 3 选择属于每个 horizon 的 supremum，未声称同一个 mu 在所有 M 同时实现下界。n=0、奇数 q、多余零质量字母、周期 pair 链、随机预测器与 ties 都已在证明内覆盖。

本下界扩展到任意共同算法，依赖的是未知 sigma 源族及其不可辨识性，不是 uniform 已知源或已知确定性 cycle 上某个指定估计器的误差。与既有 K3 上界比较，K 的 3/2 与 3 指数仍留有差距；不据此声称 sharp K 或完整 minimax 匹配。分组源嵌入、有限两点测试和 KL–TV 工具不作首创宣称；直接 primary 的同范围先例核对不作为本数学证明的已完成结论。旧根和已接纳各项保持原依赖，本义务的完成也不宣告 v10 整体完成。证毕。
