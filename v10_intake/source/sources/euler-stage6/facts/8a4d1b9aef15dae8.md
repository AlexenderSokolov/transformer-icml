---
fact_id: 8a4d1b9aef15dae8
problem_id: icml-general-prediction
author: prover
predecessors: [fef8372728290b45, a53804d650803060]
glossary_introduces: {}
external_refs: []
statement_chars: 7120
---

## statement
# T2-ANCHORED-CAUSAL-DIRECT：有限锚点归一化的低维强 direct 因果 batch 候选

019已正常接纳Fact5110203ec700e7e1 / Evidence41b852ff8a4fe4bf8aa948707c6bce8c1e7ca0a3ef48107c0ed2cdd5b401b12d，其完整streaming物理peak与017/018切口结论保持。本项不再把该顺序机展开成通用逐指令网络，而直接研究原SRC的共享逐token、因果batch hybrid执行模型中的强direct前端。旧B-C三元表及B-J联合特征已有来源，不将它们重包为新结果。本候选尚未证明，019不是本项数学前提，完成也不宣告同精确预算最优或v10完成。

## 1. 原实验、全路径对象及有限配置

全部整数K>=2、M>=1，N=M+2，n=N+1，q=N+1。每条实验内固定任意允许零边的齐次二阶theta及任意初始对律mu。观察完整X_1^N，Y_i=(X_(i+1),X_(i+2))，M次departure只计i=0,...,M-1。目标仍为同轨迹actual E TV(output,theta_(Y_M))，TV=L1/2，sup可逐K,M与算法选源。程序不读theta、mu、未来符号或辅助行栈。

对每条历史及声明query s=(a,b)，C_s,c为完整原triple counts，J_s=sum_c C_s,c，p_s,c^+=(C_s,c+1)/(J_s+K)，T=K^(5/2)/sqrt(M+1)。精度为整数

    h>=h0(M)=max(4,ceil(log2 M)+1), Q=2^h,
    b=ceil(log2(M+1)), ell=ceil(log2(N+K+2)),
    g=max(h,2b+12), G=2^g,
    p=4h+4ell+64, p_a=4g+4ell+64.                 (CONFIG)

待核h>=b、g<=2h+12及p_a<=2p。g是本新程序内部head精度，h仍是最终输出格式。公开整数由有限移位/位长/整数循环构造，不使用实数oracle。

输入为同一one-hot历史和一个不含新观测的synthetic零token q。q的public flag可作锚点；不能另添来自源的样本。外部query和actual两种模式均可，实际末对来自已观察端点。每次运行只输出一个query；全query正确性不等于免费同时输出K²行。

## 2. 具体共享因果前端及四个锚定heads

沿SRC已付费的两个singleton copying heads，在历史key t>=3取得l2_t=e_(X_(t-2)), l1_t=e_(X_(t-1))；q取得e_(X_(N-1)),e_(X_N)。fallback、query/mode选择、端点保存及两头全batch执行收费。各token共享同一有限点运算；任何历史token不需提前知道末query。

令f_t=1{t=q}为公开flag。历史key的标签value为x_t，q的x_q=0。所有统计key使用

    k_t=((1-f_t)l2_t,(1-f_t)l1_t),
    v_t=(x_t,f_t).

key和value在历史位置都不依赖最终query，q的key为零、value仅最后一个flag为1。位门控的构造、公开flag和位置均收费。q的四个统计heads由(alpha,beta)∈{0,1}²标记，其理想query/score为

    Q_alpha,beta=((alpha ln2)A,(beta ln2)B),
    score(q,t)=ln2[alpha 1{X_(t-2)=a}+beta 1{X_(t-1)=b}]

对历史key t=3,...,N成立；anchor q的score=0。每head的value维数K+1，QK维数至多2K，四头共4K+4个返回坐标。q允许keys为{3,...,N,q}，包括因果self；其它行使用{3,...,t}的因果prefix，空集时self fallback。所有mask是明确有限bits，没有数值负无穷。不能省略非q行的求值费用。

设i_t=1{X_(t-2)=a}, j_t=1{X_(t-1)=b}。理想权重

    w_alpha,beta(t)=(1+i_t)^alpha (1+j_t)^beta ∈{1,2,4},
    D_alpha,beta=1+sum_(t=3)^N w_alpha,beta(t),
    S_alpha,beta,c=sum_(t=3)^N w_alpha,beta(t)1{X_t=c}.

返回理想label坐标y_alpha,beta,c=S_alpha,beta,c/D_alpha,beta及anchor坐标z_alpha,beta=1/D_alpha,beta。待证全部历史/query下

    1<=D_alpha,beta<=4M+1,
    0<=S_alpha,beta,c<=4M,
    C_s,c=S_11,c-S_10,c-S_01,c+S_00,c.            (IDEAL)

这只是标准乘积展开/容斥与锚点去归一化，不能称新工具或首创。与旧B-J单个joint kernel的K²维表示不同，不能把旧单kernel秩下界误用于这个多头构造。

## 3. 实际有限heads与精确整数恢复

不能把exp(ln2)=2当实际实数运算。实际query系数采用SRC有限有理log生成得到的L2，保留完整p_a小数位、乘积/guard。使用同一声明的有限指数递推、正整数累加和返回G-grid的商余数。必须对这里的新key/value、self anchor及全部prefix/fallback重新核验适用性，给出足够自足的误差推导；SRC固定旧四头的结论不能未经解释直接覆盖新头。

待证全部实际score在[0,2]内，每head、每返回坐标有

    hat y=Y/G, hat z=Z/G, Y,Z∈{0,...,G},
    |hat y-y|<=2/G, |hat z-z|<=2/G.              (HEAD)

可重述SRC的有限log误差、8p_a项指数递推、单weight误差<=100p_a 2^(-p_a)，以每行至少一个正weight给归一化误差<=200p_a 2^(-p_a)，最后一次head floor另付1/G。锚点的有限score为0，weight确为该递推的单位weight。

置D_*=4M+1。CONFIG须保证G>=64D_*²。对q处各头证明Z>=1且

    |Y/Z-S_alpha,beta,c|<=4D_*²/G<=1/16.         (SNAP-MARGIN)

用完整整数除法实现half-up

    S_hat_alpha,beta,c=floor((2Y+Z)/(2Z)).

因此q处S_hat精确等于整数S，并由IDEAL恢复完整C_s,c。必须保留M=1、无访问行、全零/确定路径、任意特定theta下零概率的历史、S=0与S=4M以及head网格端点。

为了共享点运算在非q位置也全程合法，可统一将anchor numerator替换为Z_safe=max(1,Z)，将各half-up结果clip到[0,4M]，将容斥结果clip到[0,M]后再输出。q处这些guards不改变结果；其他行不声称恢复最终query计数，但每次division必须正分母、每个字宽合法，最终输出亦为概率向量。所有guards、比较、signed差、copy和holds收费。禁止免费广播最终query到过去或仅运行q的解码以省去全token费用。

最终对恢复的C执行完整ordered add-one输出：前K-1坐标floor(Q(C_c+1)/(sum C+K))/Q，末坐标补残差。待证同一新程序F_anc在全历史/全query上

    F_anc(x;s)=Gamma_Q(C_s),
    TV(F_anc(x;s),p_s^+(x))<=(K-1)/Q.             (EXACT-READOUT)

不声称F_anc逐位等于原Pi；Pi的master/V故障接口与36delta常数也不自动转移到新4K+4坐标银行。注意锚点概率约1/M，解码的精度放大已通过g实际付费，不把内部g与最终h混同。

## 4. 同actual风险及完整共享batch资源候选

仅引用016已接纳48T与Q>=2M的有限比较，证明

    sup_(theta,mu) E TV(F_anc(X;Y_M),theta_(Y_M))
      <=min(1,48T+(K-1)/Q)<=min(1,49T).          (RISK)

M+1>=(64K^(5/2)/tau)²、h=h0、0<tau<1为充分配置。[Non-scientific operational metadata omitted.]

模型严格沿SRC：共享逐token Boolean/ReLU点运算加收费有限因果attention的batch hybrid。固定参数/布局只依K,N,h，源无关。点运算在全部n位置执行并收费；head值的grid-to-bits、完整整数乘除/余数、归位、residual复制、所有live位逐层hold、输出decode均收费。不存在packed RAM的免费neural persistence或外加count table。历史输入及QKV是明确收费的attention输入，随后decoder只能访问四头返回、公开量及声明精确bits；它不再回读历史。它不满足017–019的最后两符号前不可回读cut限制，不将这些lower外推至该batch前端。

待证一个具体有限电路实现具备下列保守上界，常数独立于K,M,h。p_a为本实现真实字长参数：

|项目|候选完整上界|
|---|---|
|neural depth / per-token width|O(K p_a²) / O(K p_a)|
|总heads / 同层最多heads；max QK dimension；score cap|6 / 4；2K；2|
|online coefficient/arithmetic word，含完整乘积/余数/guards|<=128 p_a bits|
|dense coefficient slots / parameter bits|O(K³p_a⁴) / O(K³p_a⁵)，包括零项/bias|
|active gates/projections；identity holds|O(Kp_a²+K²)；O(K²p_a³)|
|sparse program/coefficient/address/hold格式|共O(K²p_a⁴) bits|
|完整masks/positions|O(n²+n log(n+1)) bits|
|observed input、query/endpoint、public flags|NK及其完整取得/转换/保存另列|
|rolling工作数组|O(nKp_a²) bits，仅作为总peak的分项|
|uncached有限attention online bitwork|O(n²(K+p_a)p_a²)|
|同样允许full-score cache的attention online bitwork|O(n²Kp_a²)，cache生成/存储/selector另付|
|dense pointwise/QKV全n位置online bitwork|O(nK³p_a⁶)|
|有限有理log生成work / scratch|O(p_a³ log²(p_a+1)) / O(p_a log(p_a+1))|
|compact有限attention/arithmetic evaluator code|O(p_a⁴) bits|

前两复制头、四统计头的所有有效边均按选定方案计费。缓存只允许固定完整score菜单0,L2,2L2，2L2须由有限指数递推单独生成，不能用舍入后的exp(L2)平方替代；cache生成O(p_a³)与log生成另列。比较原Pi时同样允许其已声明五项菜单，不通过仅给一方缓存制造差距。dense/sparse是独立格式，不能混取优势。

给出完整phase同时活跃项求和。dense格式下令

    P_dense=K³p_a⁵+n²+nKp_a²+p_a⁴+p_a log(p_a+1).

待证含program/参数、input、masks/positions、QKV、residual、四银行、controller、完整算术scratch及输出的phase-total物理peak为O(P_dense)。如用sparse格式，单独以K²p_a⁴替换dense参数项并仍完整列账；不自动导出sparse在线加速。不得只报rolling数组或query-token容量。

完整offline还包括布局、mask/位置、微码、每个gate/term/hold记录及真实全格式写出。以实际记录数G_rec,T_rec,I_hold列出生成O((G_rec+T_rec+I_hold)p_a²)和相应O((G_rec+T_rec+I_hold)p_a) scratch，加log/cache与所有dense零项写出；须证明保守总offline work

    O(K³p_a⁶+n²p_a²+p_a³ log²(p_a+1)),

及phase-total offline peak O(P_dense)。公开循环/索引和格式地址位长均核入p_a的常数倍；若任何费用承诺不成立，登记准确缺口，保持OPEN，不静默改成更弱界。

这是实际batch hybrid构造和解析费用；generic逐指令PURE展开不是以上较小L/W的证明。无需新增compiler、大规模枚举或literal ledger，未执行则明确说明。若讨论PURE，另写其完整膨胀账，不并入本候选比较。

## 5. 比较的准确结论与未决量

只有完整IDEAL/HEAD/SNAP/EXACT-READOUT/RISK及上表全部成本经正常独立网关后，方可声称：一般K也有一个强direct，在6heads、4同层heads、2K QK维、score cap2的共同因果batch模型中，恢复完整query counts，且与原Pi具有同阶的上述完整资源上界。由p_a<=2p可把这些上界用原p表示，代价为独立于参数的常数倍；最小上述充分M、h0下p_a=O(1+logK+log(1/tau))。

“共同常数倍上界包络”不是“逐坐标装入原Pi的同一个数值cap”。若双方只有upper，不推导实际费用优势、支配或一般算法lower。特别不凭p_a<=2p把新128p_a word说成原128p；不把旧K=2 allocation外推一般K，不把多头与单joint-kernel的表示区别说成神经最优。数值cap、完整资源tradeoff/优势、最优work/width、一般K故障预算与物理纠错仍需独立后续。

乘积展开、容斥、已知锚点去归一化、整数rounding以及Boolean/ReLU运算均按标准方法分类。旧来源已列出的lag-matching、subset-count inversion与count recovery文献必须保留，有限本地检索无命中不等于新颖性证明。若完整前端已被既有来源覆盖，说明准确重合与必要实现增量，不为纯重述另立首创结论。

## 6. 依赖、预检和提交边界

预期实际Fact前驱只有SRC fef8372728290b45（真实有限求值、复制/运算构件与比较费用）和016 a53804d650803060（原actual48T）。新四头、anchor/self-mask、全路径精确恢复、guard与生命周期/成本需自足；实质另用Fact则如实登记。019只说明研究进度，不是前驱；不得让020成为任何旧结果的逆向前提。

[Private administrative workflow omitted from the public export.]若有真实缺口登记准确障碍/修复方向，保持原目标OPEN；团队讨论不是Fact。

[Non-scientific operational metadata omitted.][Non-scientific operational metadata omitted.]


## proof
Original contract and explicit scope for this proof:
{"contract_id":"e6b7592e781948d00eb2a2effb80d8e3ef77e480f8d70f960286bc33faf730af","definitions":"## A. 共同源、观察、算法及风险定义\n\n对每个整数 K>=2，A={0,...,K-1}，S=A²，D=K²。一个实验固定一个时间齐次二阶表 theta∈(Delta(A))^S，允许零坐标；初始对分布 mu∈Delta(S) 任意。令\n\n    Y_j=(X_(j+1),X_(j+2)),\n    P_theta((a,b),(b,c))=theta_(a,b)(c),\n    N>=3, M=N-2, E_N=Y_M,\n    n_s(M)=sum_(j=0)^(M-1)1{Y_j=s},\n    C_s,c(M)=sum_(j=0)^(M-1)1{Y_j=s,X_(j+3)=c},\n    p_s^+=(C_s+1)/(n_s+K).\n\n每次预测完整观察 X_1^N。最后一个计数后继是 X_N；Y_M 不是额外 departure。actual query 从已观察最后两符号取得；fixed-query 任务另有明确的公开 s。X_(N+1)、theta、mu、支持、闭类、平稳律、未来行栈及隐藏源标签不可见。外部 query 是同一历史下调用的查询参数，不额外赠送干净端点或统计量。获得和复制实际端点在实现中收费。\n\n共同算法族的程序和公开精度可以依赖 K,N,h，不能依赖未知 theta,mu 或其隐藏标签。统计根中的理想 p^+ 是分析变量；给定实现的计数、头输出等实际可见代码由来源实现义务确定，不能据理想表达式新增 readout 端口。比较中的任意全历史预测器可以用全部 X_1^N 和源独立随机种子，输出任意概率向量。具体 Pi 则遵守自己已声明的内部信息切口。\n\nTV(p,q)=1/2 sum_c|p_c-q_c|。对给定 family F，令 Z_N(s)=TV(F_(K,N,h)(X_1^N;s),theta_s)。严格区分：\n\n| 名称 | 定义 | 量词 |\n|---|---|---|\n| fixed row | E Z_N(s) | 固定公开 s |\n| all contexts | E max_(s∈S) Z_N(s)；另可问其 a.s. 极限 | 全 K² 行，不改成访问行 |\n| actual terminal | R_act=E Z_N(E_N) | 同一历史的末尾 query |\n| conditional terminal | E[Z_N(E_N)\\|E_N=s] | 仅当 p_N(s)=mu P^M(s)>0；零概率时未定义 |\n| empirical weighted | E sum_s(n_s/M)Z_N(s) | 同历史频率权重 |\n| other history weighted | E sum_s w_s(X_1^N)Z_N(s) | w 为观察历史可测 simplex；不自动有一致性 |\n\n逐源极限固定 K,theta,mu 后令 N→∞。统一均值是每个 N 的 sup_(theta,mu) R_act；取 supremum 时源可随 N 改选，但一个样本路径内部的核必须齐次。固定 K 的统一结论不是 K 随 N 变化的无条件结论，也不是 changing-source 的统一几乎处处结论。输出允许零坐标，损失仅 TV，本 contract 不把它解释为 positive-output KL。\n\n\n## 共同研究范围的约定\n\n接口I是一个程序性质的定义，不能作为所有算法已经满足的全局假设。条件统计根对任意满足I的共同有限族F证明蕴含式；具体Pi满足I及其完整成本须由SRC-Pi的正常独立来源义务支持，不能在证明SRC-Pi时先假定它。原第二阶段固定证明是可查来源，旧Fact编号不是新项目前驱。\n\n后继真实资源/可靠性命题可以在同一contract内建立独立义务，不必谎称它们是统计根的前提。数据观察及TV实验保持上述定义。每项具体实现须声明自己的内部代码、允许回读、输出格式、参数/字长、batch或streaming等执行方式；比较只在所声明的共同条件下成立。原Pi的finite-attention加pointwise batch hybrid、literal bit/ReLU模块的packed/scalar、sparse/dense选项分别核算，不将一项格式的便宜坐标拼入另一项。\n\n完整费用包括实际head和局部绑定、输入/query/端点取得、参数/零系数、物理字、复制/跨层保持/清除、mask/position、所有活动bank与metadata、online/offline工作和同时峰值。不能免费引入计数、normalizer、译码或生成器。新算术/扰动参数由各精确义务局部量化；改变共同数据律、可见信息或风险须建立新的明确数学范围。\n\n给定接口的条件定理、具体实现定理、训练可达性、必要资源及新颖性是不同主张。数学根只包含数学命题。行政完成程序不是数学前提；独立后续结论不改变已有定理的证明依赖。\n","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]},"statement":"# T2-ANCHORED-CAUSAL-DIRECT：有限锚点归一化的低维强 direct 因果 batch 候选\n\n019已正常接纳Fact5110203ec700e7e1 / Evidence41b852ff8a4fe4bf8aa948707c6bce8c1e7ca0a3ef48107c0ed2cdd5b401b12d，其完整streaming物理peak与017/018切口结论保持。本项不再把该顺序机展开成通用逐指令网络，而直接研究原SRC的共享逐token、因果batch hybrid执行模型中的强direct前端。旧B-C三元表及B-J联合特征已有来源，不将它们重包为新结果。本候选尚未证明，019不是本项数学前提，完成也不宣告同精确预算最优或v10完成。\n\n## 1. 原实验、全路径对象及有限配置\n\n全部整数K>=2、M>=1，N=M+2，n=N+1，q=N+1。每条实验内固定任意允许零边的齐次二阶theta及任意初始对律mu。观察完整X_1^N，Y_i=(X_(i+1),X_(i+2))，M次departure只计i=0,...,M-1。目标仍为同轨迹actual E TV(output,theta_(Y_M))，TV=L1/2，sup可逐K,M与算法选源。程序不读theta、mu、未来符号或辅助行栈。\n\n对每条历史及声明query s=(a,b)，C_s,c为完整原triple counts，J_s=sum_c C_s,c，p_s,c^+=(C_s,c+1)/(J_s+K)，T=K^(5/2)/sqrt(M+1)。精度为整数\n\n    h>=h0(M)=max(4,ceil(log2 M)+1), Q=2^h,\n    b=ceil(log2(M+1)), ell=ceil(log2(N+K+2)),\n    g=max(h,2b+12), G=2^g,\n    p=4h+4ell+64, p_a=4g+4ell+64.                 (CONFIG)\n\n待核h>=b、g<=2h+12及p_a<=2p。g是本新程序内部head精度，h仍是最终输出格式。公开整数由有限移位/位长/整数循环构造，不使用实数oracle。\n\n输入为同一one-hot历史和一个不含新观测的synthetic零token q。q的public flag可作锚点；不能另添来自源的样本。外部query和actual两种模式均可，实际末对来自已观察端点。每次运行只输出一个query；全query正确性不等于免费同时输出K²行。\n\n## 2. 具体共享因果前端及四个锚定heads\n\n沿SRC已付费的两个singleton copying heads，在历史key t>=3取得l2_t=e_(X_(t-2)), l1_t=e_(X_(t-1))；q取得e_(X_(N-1)),e_(X_N)。fallback、query/mode选择、端点保存及两头全batch执行收费。各token共享同一有限点运算；任何历史token不需提前知道末query。\n\n令f_t=1{t=q}为公开flag。历史key的标签value为x_t，q的x_q=0。所有统计key使用\n\n    k_t=((1-f_t)l2_t,(1-f_t)l1_t),\n    v_t=(x_t,f_t).\n\nkey和value在历史位置都不依赖最终query，q的key为零、value仅最后一个flag为1。位门控的构造、公开flag和位置均收费。q的四个统计heads由(alpha,beta)∈{0,1}²标记，其理想query/score为\n\n    Q_alpha,beta=((alpha ln2)A,(beta ln2)B),\n    score(q,t)=ln2[alpha 1{X_(t-2)=a}+beta 1{X_(t-1)=b}]\n\n对历史key t=3,...,N成立；anchor q的score=0。每head的value维数K+1，QK维数至多2K，四头共4K+4个返回坐标。q允许keys为{3,...,N,q}，包括因果self；其它行使用{3,...,t}的因果prefix，空集时self fallback。所有mask是明确有限bits，没有数值负无穷。不能省略非q行的求值费用。\n\n设i_t=1{X_(t-2)=a}, j_t=1{X_(t-1)=b}。理想权重\n\n    w_alpha,beta(t)=(1+i_t)^alpha (1+j_t)^beta ∈{1,2,4},\n    D_alpha,beta=1+sum_(t=3)^N w_alpha,beta(t),\n    S_alpha,beta,c=sum_(t=3)^N w_alpha,beta(t)1{X_t=c}.\n\n返回理想label坐标y_alpha,beta,c=S_alpha,beta,c/D_alpha,beta及anchor坐标z_alpha,beta=1/D_alpha,beta。待证全部历史/query下\n\n    1<=D_alpha,beta<=4M+1,\n    0<=S_alpha,beta,c<=4M,\n    C_s,c=S_11,c-S_10,c-S_01,c+S_00,c.            (IDEAL)\n\n这只是标准乘积展开/容斥与锚点去归一化，不能称新工具或首创。与旧B-J单个joint kernel的K²维表示不同，不能把旧单kernel秩下界误用于这个多头构造。\n\n## 3. 实际有限heads与精确整数恢复\n\n不能把exp(ln2)=2当实际实数运算。实际query系数采用SRC有限有理log生成得到的L2，保留完整p_a小数位、乘积/guard。使用同一声明的有限指数递推、正整数累加和返回G-grid的商余数。必须对这里的新key/value、self anchor及全部prefix/fallback重新核验适用性，给出足够自足的误差推导；SRC固定旧四头的结论不能未经解释直接覆盖新头。\n\n待证全部实际score在[0,2]内，每head、每返回坐标有\n\n    hat y=Y/G, hat z=Z/G, Y,Z∈{0,...,G},\n    |hat y-y|<=2/G, |hat z-z|<=2/G.              (HEAD)\n\n可重述SRC的有限log误差、8p_a项指数递推、单weight误差<=100p_a 2^(-p_a)，以每行至少一个正weight给归一化误差<=200p_a 2^(-p_a)，最后一次head floor另付1/G。锚点的有限score为0，weight确为该递推的单位weight。\n\n置D_*=4M+1。CONFIG须保证G>=64D_*²。对q处各头证明Z>=1且\n\n    |Y/Z-S_alpha,beta,c|<=4D_*²/G<=1/16.         (SNAP-MARGIN)\n\n用完整整数除法实现half-up\n\n    S_hat_alpha,beta,c=floor((2Y+Z)/(2Z)).\n\n因此q处S_hat精确等于整数S，并由IDEAL恢复完整C_s,c。必须保留M=1、无访问行、全零/确定路径、任意特定theta下零概率的历史、S=0与S=4M以及head网格端点。\n\n为了共享点运算在非q位置也全程合法，可统一将anchor numerator替换为Z_safe=max(1,Z)，将各half-up结果clip到[0,4M]，将容斥结果clip到[0,M]后再输出。q处这些guards不改变结果；其他行不声称恢复最终query计数，但每次division必须正分母、每个字宽合法，最终输出亦为概率向量。所有guards、比较、signed差、copy和holds收费。禁止免费广播最终query到过去或仅运行q的解码以省去全token费用。\n\n最终对恢复的C执行完整ordered add-one输出：前K-1坐标floor(Q(C_c+1)/(sum C+K))/Q，末坐标补残差。待证同一新程序F_anc在全历史/全query上\n\n    F_anc(x;s)=Gamma_Q(C_s),\n    TV(F_anc(x;s),p_s^+(x))<=(K-1)/Q.             (EXACT-READOUT)\n\n不声称F_anc逐位等于原Pi；Pi的master/V故障接口与36delta常数也不自动转移到新4K+4坐标银行。注意锚点概率约1/M，解码的精度放大已通过g实际付费，不把内部g与最终h混同。\n\n## 4. 同actual风险及完整共享batch资源候选\n\n仅引用016已接纳48T与Q>=2M的有限比较，证明\n\n    sup_(theta,mu) E TV(F_anc(X;Y_M),theta_(Y_M))\n      <=min(1,48T+(K-1)/Q)<=min(1,49T).          (RISK)\n\nM+1>=(64K^(5/2)/tau)²、h=h0、0<tau<1为充分配置。[Non-scientific operational metadata omitted.]\n\n模型严格沿SRC：共享逐token Boolean/ReLU点运算加收费有限因果attention的batch hybrid。固定参数/布局只依K,N,h，源无关。点运算在全部n位置执行并收费；head值的grid-to-bits、完整整数乘除/余数、归位、residual复制、所有live位逐层hold、输出decode均收费。不存在packed RAM的免费neural persistence或外加count table。历史输入及QKV是明确收费的attention输入，随后decoder只能访问四头返回、公开量及声明精确bits；它不再回读历史。它不满足017–019的最后两符号前不可回读cut限制，不将这些lower外推至该batch前端。\n\n待证一个具体有限电路实现具备下列保守上界，常数独立于K,M,h。p_a为本实现真实字长参数：\n\n|项目|候选完整上界|\n|---|---|\n|neural depth / per-token width|O(K p_a²) / O(K p_a)|\n|总heads / 同层最多heads；max QK dimension；score cap|6 / 4；2K；2|\n|online coefficient/arithmetic word，含完整乘积/余数/guards|<=128 p_a bits|\n|dense coefficient slots / parameter bits|O(K³p_a⁴) / O(K³p_a⁵)，包括零项/bias|\n|active gates/projections；identity holds|O(Kp_a²+K²)；O(K²p_a³)|\n|sparse program/coefficient/address/hold格式|共O(K²p_a⁴) bits|\n|完整masks/positions|O(n²+n log(n+1)) bits|\n|observed input、query/endpoint、public flags|NK及其完整取得/转换/保存另列|\n|rolling工作数组|O(nKp_a²) bits，仅作为总peak的分项|\n|uncached有限attention online bitwork|O(n²(K+p_a)p_a²)|\n|同样允许full-score cache的attention online bitwork|O(n²Kp_a²)，cache生成/存储/selector另付|\n|dense pointwise/QKV全n位置online bitwork|O(nK³p_a⁶)|\n|有限有理log生成work / scratch|O(p_a³ log²(p_a+1)) / O(p_a log(p_a+1))|\n|compact有限attention/arithmetic evaluator code|O(p_a⁴) bits|\n\n前两复制头、四统计头的所有有效边均按选定方案计费。缓存只允许固定完整score菜单0,L2,2L2，2L2须由有限指数递推单独生成，不能用舍入后的exp(L2)平方替代；cache生成O(p_a³)与log生成另列。比较原Pi时同样允许其已声明五项菜单，不通过仅给一方缓存制造差距。dense/sparse是独立格式，不能混取优势。\n\n给出完整phase同时活跃项求和。dense格式下令\n\n    P_dense=K³p_a⁵+n²+nKp_a²+p_a⁴+p_a log(p_a+1).\n\n待证含program/参数、input、masks/positions、QKV、residual、四银行、controller、完整算术scratch及输出的phase-total物理peak为O(P_dense)。如用sparse格式，单独以K²p_a⁴替换dense参数项并仍完整列账；不自动导出sparse在线加速。不得只报rolling数组或query-token容量。\n\n完整offline还包括布局、mask/位置、微码、每个gate/term/hold记录及真实全格式写出。以实际记录数G_rec,T_rec,I_hold列出生成O((G_rec+T_rec+I_hold)p_a²)和相应O((G_rec+T_rec+I_hold)p_a) scratch，加log/cache与所有dense零项写出；须证明保守总offline work\n\n    O(K³p_a⁶+n²p_a²+p_a³ log²(p_a+1)),\n\n及phase-total offline peak O(P_dense)。公开循环/索引和格式地址位长均核入p_a的常数倍；若任何费用承诺不成立，登记准确缺口，保持OPEN，不静默改成更弱界。\n\n这是实际batch hybrid构造和解析费用；generic逐指令PURE展开不是以上较小L/W的证明。无需新增compiler、大规模枚举或literal ledger，未执行则明确说明。若讨论PURE，另写其完整膨胀账，不并入本候选比较。\n\n## 5. 比较的准确结论与未决量\n\n只有完整IDEAL/HEAD/SNAP/EXACT-READOUT/RISK及上表全部成本经正常独立网关后，方可声称：一般K也有一个强direct，在6heads、4同层heads、2K QK维、score cap2的共同因果batch模型中，恢复完整query counts，且与原Pi具有同阶的上述完整资源上界。由p_a<=2p可把这些上界用原p表示，代价为独立于参数的常数倍；最小上述充分M、h0下p_a=O(1+logK+log(1/tau))。\n\n“共同常数倍上界包络”不是“逐坐标装入原Pi的同一个数值cap”。若双方只有upper，不推导实际费用优势、支配或一般算法lower。特别不凭p_a<=2p把新128p_a word说成原128p；不把旧K=2 allocation外推一般K，不把多头与单joint-kernel的表示区别说成神经最优。数值cap、完整资源tradeoff/优势、最优work/width、一般K故障预算与物理纠错仍需独立后续。\n\n乘积展开、容斥、已知锚点去归一化、整数rounding以及Boolean/ReLU运算均按标准方法分类。旧来源已列出的lag-matching、subset-count inversion与count recovery文献必须保留，有限本地检索无命中不等于新颖性证明。若完整前端已被既有来源覆盖，说明准确重合与必要实现增量，不为纯重述另立首创结论。\n\n## 6. 依赖、预检和提交边界\n\n预期实际Fact前驱只有SRC fef8372728290b45（真实有限求值、复制/运算构件与比较费用）和016 a53804d650803060（原actual48T）。新四头、anchor/self-mask、全路径精确恢复、guard与生命周期/成本需自足；实质另用Fact则如实登记。019只说明研究进度，不是前驱；不得让020成为任何旧结果的逆向前提。\n\n[Private administrative workflow omitted from the public export.]若有真实缺口登记准确障碍/修复方向，保持原目标OPEN；团队讨论不是Fact。\n\n[Non-scientific operational metadata omitted.][Non-scientific operational metadata omitted.]\n"}

Admitted prerequisite interfaces (use only within the recorded scopes):
[{"exact_statement":"# SRC-Pi：原有限因果程序的全路径实现、银行接口与完整费用\n\n对每个整数 K>=2、N>=3，令 M=N-2、n=N+1。对每个整数 h>=max(4,ceil(log2 M)+1)，令 Q=2^h、ell=ceil(log2(N+K+2))、p=4h+4ell+64。字母表 A={0,...,K-1}。对任意完整已观察历史 x_1^N 和 query s=(a,b)，定义\n\n    C_s,c=sum_(t=3)^N 1{(x_(t-2),x_(t-1),x_t)=(a,b,c)},\n    n_s=sum_c C_s,c, p_s,c^+=(C_s,c+1)/(n_s+K).\n\n存在下述同一个共同确定有限程序族 Pi_(K,N,h)，参数、固定循环、布局、掩码和常数仅依赖公开 K,N,h；其固定构造由本项目 inputs/source-v10/inputs/general-assumptions-20261027/stage2/ 下 C1-proof-v1.md §§1–7、finiteN-reliability-proof-v1.md §§4–6 和 root-proof-v1.md §5 指定。以下断言需由确定性构造证明支持，I 是待证结论。旧来源的正性、平稳初始化和旧 Fact 身份均不作前提。\n\n## S1. 实际因果前端与有限求值\n\n主实现为有限整数求值的因果 attention 加逐 token Boolean/ReLU 点运算的 batch hybrid。输入仅为已观察历史、声明 query/mode 和公开 metadata；合成位置 q=N+1 的 token 为零，不含未来符号。两个已付费 singleton copying heads 产生前两步符号，并在 q 保留实际端点 (x_(N-1),x_N)，供外部 query 与 actual query 两种模式使用。外部 s 不替换实际端点修正。\n\n另有四个统计 heads P1、P2、T、0。理想比较对象的 Q/K/V 为：P1 的 Q=((ln2)A,(ln2)B)、K=(lag2,lag1)、V=(token,lag2)；P2 将第二段 ln2 换为 ln3；T 的 Q=(ln2)B、K=lag2、V=(lag1,F)；0 的 Q=K=0、V=(lag2,lag1,F,z)。A,B 为 query one-hot，z_t=1{t=3}，F_t=z_t lag1_t；q 的有效 keys 为 3,...,N，其余行使用声明的因果 prefix/fallback。理想输出依次为 (q1,v1)、(q2,v2)、(hvec,h0)、(alpha,nu,f,rho)，共 9K+1 标量。值为 query 无关的局部 bits。\n\n实际程序以有限有理 log 生成、定长整数指数求值、精确累加和正整数除法产生闭 h-grid G_h={j/Q:0<=j<=Q} 上的标量；不调用实数 log/exp/floor oracle。每一返回 head 标量与其上述理想值相差至多 2/Q。包含 1 的 G_h 用 h+1 位无符号分子。连续 ReLU 不被声称在实区间上实现 floor；其 bit extraction 只作用于声明有限网格。\n\n四个统计 head 后不再有读取原始历史的 decoder 端口或免费 count table；计数 C 仅为数学比较对象。源参数 theta、mu、支持、平稳律和访问控制参数均不进入程序。\n\n## S2. 正确逐路径读出、guards 与接口 I\n\n记 c_s,c=C_s,c/M、rho=1/M、u_ij=n_ij/M，alpha_i=sum_j u_ij、nu_j=sum_i u_ij，J_c=1{实际端点=(b,c)}。理想读出为\n\n    dT=1+alpha_b,\n    initial_bc=dT h0_c-f_c,\n    g_bc=dT hvec_c-nu_c+rho J_c-initial_bc,\n    U_k=v_k,a, lambda_1=1,lambda_2=2,\n    d_k=(1+lambda_k nu_b)/(1-U_k/2),\n    c_s,c=d2 q2_c-d1 q1_c-g_bc.\n\n这些恒等式对每条有限路径成立，包含 M=1、n_s=0，以及任何特定源下零概率的历史。实际点运算保留完整整数乘积、除法余数和 guard fractional bit；加减和声明的除二精确，所需乘除截断绝对误差至多 1/Q。head clipping 后 1-U_k/2∈[1/2,1]，d1∈[1,4]、d2∈[1,6]、dT∈[1,2]，有符号中间量容纳于来源指定的 [-16,16] 安全盒。\n\n令 a_c 为恢复 c_s,c 后截入 [0,1] 的 h-grid 值，令\n\n    r0=2^(-ceil(log2 M)-1), r=max(hat rho,r0),\n    x_c=a_c+r, V_c=Q x_c, T=sum_c V_c.\n\n则 x_c∈(0,2]，V_c∈{1,...,2Q}，T>0，并且\n\n    |a_c-C_s,c/M|<=76/Q,\n    |x_c-(C_s,c+1)/M|<=78/Q.\n\n最终输出按原有序 simplex 格式：c=0,...,K-2 的分子 m_c=floor(Q V_c/T)，m_(K-1)=Q-sum_(c<K-1)m_c，随后已付费 dyadic decode。其坐标非负且和为一，允许非末坐标为零，且所有路径、所有 query 同时满足\n\n    TV(Pi_(K,N,h)(x_1^N;s),p_s^+(x_1^N))\n      <=78KM/[Q(n_s+K)]+(K-1)/Q.                 (I)\n\n程序在上述全域合法；不同源规律只改变路径概率，不改变给定输入的程序及其费用。\n\n## S3. 后继确实使用的 master 与正权重银行接口\n\n9K+1 个 head 坐标各有一个 post-quantization master word，在任何 readout fanout/residual 复制之前定位切口。所有后继副本都来自该 master；query、端点及 flag BITs 在此实验中精确，统计标量 h0、f、rho 包含在可替换银行内。有限 evaluator 的干净 numerator、denominator、指数、余数及不用的历史投影在切口开放前按声明生命周期擦除或释放；历史存储及其处理仍收费。这里声明的是指定访问规则下的实际程序接口，不是对任意能重读历史算法的信息论限制。\n\n若每个 master 被任意相关的 G_h 标量替换，坐标偏差至多 delta>=0，原 downstream 运算仍合法，并有\n\n    |a_c-C_s,c/M|<=76/Q+35delta,\n    |x_c-(C_s,c+1)/M|<=78/Q+36delta,\n    TV(Pi^delta_s,p_s^+)<=KM(78/Q+36delta)/(n_s+K)+(K-1)/Q.\n\n这些是有限路径上的确定性接口，不要求误差独立，不涵盖改变 query/endpoint bits 或额外算术故障。\n\n最后正整数 V 银行的切口在全部 V_c 生成后、任何最终求和与 quotient 前。可将 V 替换为 W∈{1,...,2Q}^K；原 decoder 只从替换后的 W 重算 U=sum W 和上述 ordered floor/residual 输出，不保留干净 T 或 quotient。比较向量 V*_c=Q(C_s,c+1)/M 不是程序输入，且无需为整数；上述坐标界等价于 |V_c-V*_c|<=78+36Q delta。该定位与生命周期可在原声明成本上界内实现；若另外实现物理注入器、快照设备或新 normalizer 的 bridge，其硬件和程序费用单列，不在 nominal Pi 的免费能力中。\n\n## S4. 完整构造费用及表示约定\n\n以下是固定构造的统一上界，常数与 K,N,h 无关；采用来源最终修正后的 batch hybrid 计费。全部 n 个 token 的点运算计费，数学上所有 query 的正确性不意味着一次运行免费输出全部 K² 行。\n\n| 坐标 | 上界或精确结构 |\n|---|---|\n| neural depth / width | O(Kp²) / O(Kp) |\n| total heads / max layer heads；max QK dimension；score cap | 6 / 4；2K；2 |\n| 单 coefficient 与 arithmetic word | 至多 128p bits，含完整乘积、余数与 guards |\n| dense coefficient slots / parameter bits | O(K³p⁴) / O(K³p⁵)，零项和 bias 收费 |\n| active gates/projections；identity holds | O(Kp²+K²)；O(K²p³) |\n| sparse program / coefficients / addresses / holds | 共 O(K²p⁴) bits |\n| masks / positions | O(n²+n log(n+1)) bits |\n| observed input | O(NK) one-hot bits，或另付 binary acquisition/转换 |\n| rolling working arrays | O(nKp²) bits，不含已存参数、input、masks |\n| uncached finite attention bitwork | O(n²(K+p)p²) |\n| equally cached attention bitwork | O(n²Kp²)，cache 生成、存储、selector 另付 |\n| dense pointwise / QKV bitwork | O(nK³p⁶) |\n| finite rational log generation / scratch | O(p³ log²(p+1)) / O(p log(p+1)) |\n| finite arithmetic evaluator code | 保守 O(p⁴) bits |\n\n五个 full-score caches 对应 0,L2,2L2,L3,L2+L3，分别有限求值；最后一项不是两个已舍入 exp 的乘积。使用 cache 时其非零生成需 O(p³) bitwork，另加 log 生成；与比较器一致付费。dense 与 sparse 为不同表示选择，不混合其优势；packed registers 与 scalar neural bit-channel 存储分别说明。\n\n完整 offline 包括 K,N,h layout、masks/positions、微码、cache/selector、全部 gate/term/hold 生成整理与实际格式输出。令 G,T_rec,I_hold 为实际生成的 gate、term、hold 记录数，其整理生成费用为 O((G+T_rec+I_hold)p²) bitwork 和 O((G+T_rec+I_hold)p) 工作 bits；dense 文件还支付真实 coefficient bits 的写出，包括零项。input/query/endpoint acquisition、residual copy、保持、擦除和最终 decode 均计费。\n\n总峰值按同一 phase 同时存活的程序/参数、input、mask/metadata、QKV、residual、银行、controller/address、临时工作区及输出求和，再取各 phase 最大值。上表 rolling working bits 不能冒充总峰值。这里不声称已在本 workspace 运行未提供的旧 emitter，也不以其他程序的精确 ledger 冒充 Pi 的实测 profile。\n\n另有保守 PURE neural 展开实现：令 T_bit 为上述固定循环的全部 online bitops（含 copy/clear），S_bit 为相应 live work、input/mask/public data；若用 interpreter，存储程序位作为常数 rails 加入。逐指令展开并保持其余 live bits，得到 depth O(T_bit+p)、width O(S_bit+p)、sparse gates/holds O((T_bit+p)(S_bit+p))、dense coefficient bits O(p(T_bit+p)(S_bit+p)²)、generic dense bitwork O(p²(T_bit+p)(S_bit+p)²)。该展开的完整成本单列，不能报告成较小的 hybrid L,W。\n\n## S5. 准确结论边界\n\nS1–S4 是本独立来源义务的合取，只针对上述固定 Pi 构造及定位接口。不从抽象 I 推导实现或费用，不泛化到所有训练 Transformer；不包含强 direct 基线上的逐坐标资源优势、整网主导成本下降或资源最优性。资源 NORM 模块与 weighted-direct 的新前端/bridge 若被使用，须有其自身明确实现和费用来源。\n\n证明可复用来源的固定确定性推导，但需在本项目正常提交为可独立检查的完整正文。G/U 统计根不作此纯确定性义务的必要前提；其独立完成不倒置为已完成统计根的前提。上述 statement 未把任何旧 discussion PASS 或旧 Fact 编号当作本项目 admission。\n","fact_id":"fef8372728290b45","scope_bindings":[{"evidence_id":"e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505","obligation_id":"6010cac30ffe4aea77e6d7a9e4e3f5686e4f44b2bf31c1674d33dfdf7dc46f84","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]}}],"source_hash":"33ea4cbe839a4ad72453cb20f8f74263a1d330e766027f7e65638c494da4c025"},{"exact_statement":"# RATE-L1-MAX：去除剩余 sqrt(log K) 的共同 actual TV 率候选及同风险配置\n\n本项是015完整接收后的独立科学后继。014、015及旧root的准确声明、接纳和依赖保持；本候选不是由它们的接纳自动得到，也不是任何旧结果的逆向前提。直接对前缀L1范数作有界差分是本次待核查的改动，不以相邻高矩参数优化替代。完成本项亦不宣告v10的资源与机制母题完成。\n\n## 1. 原完整实验与准确目标\n\n全部整数K>=2、M>=1，N=M+2，字母表{0,...,K-1}。theta为任意允许零边的齐次二阶转移表，mu为任意初始对律。每次实验内theta固定；sup可随K,M选源。观察完整X_1^(M+2)，Y_i=(X_(i+1),X_(i+2))，0<=i<=M。\n\n    C_s,a=sum_(i=0)^(M-1)1{Y_i=s,X_(i+3)=a},\n    n_s=sum_a C_s,a, J=n_(Y_M), p_s,a^+=(C_s,a+1)/(n_s+K),\n    T(K,M)=K^(5/2)/sqrt(M+1),\n    R_K^+(M)=sup_(theta,mu) E TV(p^+_(Y_M),theta_(Y_M)).\n\n待证结论：\n\n    R_K^+(M)<=min{1,48 T(K,M)}.                       (L1+)\n\n仍为同完整轨迹actual E[TV]，不是TV平方、fixed/all/conditional、独立测试查询或删尾平均。算法只获历史及公开参数，不获辅助行栈、隐藏theta/mu、访问参数或未来符号。所有退化行、周期/可约/暂态、J=0、小M及任意初始化均需覆盖。\n\n## 2. 直接L1最大集中的具体候选（全部需证明）\n\n有限辅助耦合为每个K²行提供2M个独立theta_s符号并顺序复现原M次departure。令S_s,j=sum_(l<=j)(e_(xi_s,l)-theta_s)。对确定整数1<=v<=M定义\n\n    F_s,v=max_(0<=j<=2v)||S_s,j||_1,\n    Z_v=max_s F_s,v.\n\n只对确定行/确定前缀使用iid。目标链：\n\n    E F_s,v <= sqrt(8Kv),\n    改变一个栈符号使F_s,v至多改变2,\n    P(F_s,v-E F_s,v>t)<=exp(-t²/(4v)), t>=0,\n    ||Z_v||_4 <= sqrt(8Kv)+sqrt(8v ln K)+32^(1/4)sqrt(v)\n              <= (25/4)sqrt(Kv).                    (L1MAX)\n\n均值可用L1/L2比较及有限Doob L2；集中直接作用于整个L1前缀最大值，其坐标敏感度2与K无关。请给有界差分的条件区间推导及尾积分。K²行union后以a=sqrt(8v lnK)平移，剩余正部四次矩应<=32v²；行最大值之间不要求独立。不得将sqrt(K)再次乘在全部集中误差上。\n\n最后常数可用lnK/K<=1/e<3/8、K>=2，从而系数至多sqrt(8)+sqrt(3)+2^(3/4)<25/4；所有常数比较须明确可审。该吸收利用的是sqrt(K)均值和sqrt(logK)偏差的相加，不声称偏差本身没有logK。\n\n在E_v={v<=J<2v}上逐路径TV(phat_(Y_M),theta_(Y_M))<=Z_v/(2v)。然后仅用无条件Holder及G/U整数UC：\n\n    c=K^4/(M+1), P(J<w)<=min(1,cw), 整数w>=1,\n    E[TV(phat,theta)1_Ev]\n       <=(25/8)sqrt(K) v^(-1/2) min(1,2cv)^(3/4).\n\n重述有限分层和数值几何和\n\n    sum_(l>=0)2^(-l/2)min(1,a 2^l)^(3/4)<=10sqrt(a), a>0.\n\n于是经验项候选<= (125sqrt(2)/4)T；零计数项<=T、平滑项<=2T，总系数<48。无限延拓只用于数值和，不为随机栈增加免费信息。phat不在J=0定义。\n\n平滑及下述实现误差保持截断：对每个实数A>=0，\n\n    E min{1,A/(J+K)}<=Psi(cA)<=2sqrt(cA),             (TRUNC)\n    Psi(0)=0; Psi(x)=x(1+ln(1/x)) (0<x<1); Psi(x)=1 (x>=1).\n\n需保留A=0及实阈值x=A/t-K，x>0时{J<x}={J<ceil(x)}且ceil(x)<=A/t，x<=0为空事件，不直接向非整数阈值套整数UC。A=K用于平滑。\n\n## 3. 全合法精度与原Pi\n\n对输出为概率向量且全路径全query满足原接口I的共同有限F：\n\n    h>=h0(M)=max(4,ceil(log2M)+1), Q=2^h,\n    TV(F_h(x;s),p_s^+(x))<=78KM/[Q(n_s(x)+K)]+(K-1)/Q,\n    A_h=78KM/Q, g_h=(K-1)/Q,\n\n证明\n\n    sup E TV(F_h(Y_M),p^+_(Y_M))<=min(1,g_h+Psi(cA_h)),\n    sup E TV(F_h(Y_M),theta_(Y_M))\n      <=min(1,48T+g_h+Psi(cA_h))<=min(1,64T).        (L1-I)\n\n由SRC Fact fef8372728290b45，这适用于同一个实际Pi，直接包括最低合法h0。不得由高精度结果自动推到h0，也不声称各h输出或真实风险相同。以原h_N=ceil(log2(128(K+1)(M+3)^3))、e_N=(M+3)^(-2)，另有原Pi风险<=min(1,48T+e_N)。全部须给有限参数推导。\n\n## 4. 已接纳MM5的同目标比较\n\n令R_min(K,M)=inf_A sup_(theta,mu)E TV(A(X_1^(M+2)),theta_(Y_M))，A为所有共同随机全历史概率预测器，种子与源独立，不读隐藏参数或未来。仅使用MM5 Fact946d42d5bf502eb4已接纳范围得到下界，并结合本项新上界，目标合取为\n\n    2^-16 min(1,T)<=R_min(K,M)<=R_K^+(M)<=min(1,48T). (MATCH)\n\n只有本项正常接纳后才能称K,M联合统计率在绝对常数因子内匹配，或原add-one达到该minimax阶。不能称数值常数最优、存在同一源对所有算法/所有horizon同时困难、内部资源下界或所有Transformer资源最优。旧MM5构造不重证，保留其唯一原前驱a125供小K。\n\n0<tau<2^-16时任何共同全历史算法的统一风险<=tau，必要样本为M+1>=2^-32 K^5/tau²。原Pi无故障取M+1>=(64K^(5/2)/tau)²、h=h0即为充分配置。必要与充分为不同量词方向，不能相加或当作同一见证。\n\n## 5. 联合故障与完整费用的标准后续推论\n\n在SRC原master/V切口，使用015相同的准确故障实验：master为9K+1个canonical G_h字，最终银行W在{1,...,2Q}^K；D为相对当前post-master银行V^delta的总绝对整数编辑预算。核只读已观察历史/当前银行/公开量和独立种子，不读隐藏源或未来。好事件G可与历史/J及编辑相关，P(G^c)<=gamma；G上master逐坐标误差<=delta、||W-V^delta||_1<=D；G外仍合法canonical/正银行。令\n\n    A=M[K(78/Q+36delta)+D/Q].\n\n重述短的正向量归一化与无条件截断推导，证明原Pi\n\n    R_fault<=min(1,48T+g_h+Psi(cA)+gamma)\n           <=min(1,62T+12K^(5/2)sqrt(delta)+2K²sqrt(D/Q)+gamma).\n\n因此对0<tau<1，M+1>=(248K^(5/2)/tau)²、h=h0、delta<=tau²/(2304K^5)、整数D<=floor(Q tau²/(64K^4))、gamma<=tau/4为充分配置。J0、M1、零预算和只能零编辑的网格均保留。这是新统计率代入既有接口的标准综合，不另造常数节点，不扩展015二元切口下界。\n\n取M_tau=max(1,ceil((aK^(5/2)/tau)²)-1)，a=64或248，N=M_tau+2、n=N+1、ell=ceil(log2(N+K+2))、p=4h0+4ell+64。明确S_tau=K^5/tau²、Lambda_tau=1+lnK+ln(1/tau)，n=O(S_tau)、p=O(Lambda_tau)。同一个uncached/dense SRC配置保留depth O(Kp²)、width O(Kp)、word<=128p、dense参数bits O(K³p^5)、全部n个token点运算/QKV O(nK³p^6)、attention O(n²(K+p)p²)，以及完整input/query/endpoint、metadata/masks、holds/copy/clear、输出、offline generation/全格式写出和逐phase总peak。rolling内存不替代总peak；缓存、sparse、PURE须另用完整收费配置。物理注入器、历史重读或新纠错桥不免费。\n\n该标准成本代入只消去充分样本证书中的logK，不改变Pi程序或宣称同精确预算优势。strong direct及真正同神经预算比较仍需独立科学工作。\n\n## 6. 实际依赖与正常证据门槛\n\n上界预计只必需G/U a12539a93d9f1ee3的UC与SRC fef8372728290b45的实际接口/费用；MATCH实际使用MM5 946d42d5bf502eb4。有限耦合、Doob、区间矩母函数、有界差分、Holder、dyadic及截断推导均重述自足时，不新增014/015/RATE/K3前驱。它们可作写作来源；若实质依赖其引理则如实加入前驱，禁止隐藏依赖。所有旧Fact保持原scope。\n\n先做有界逆向核查，尤其L1最大函数的单符号振幅、均值与偏差相加、25/4常数和随机末行相关性。若失败则登记精确障碍，保持OPEN，不将辅助估计失败宣称为目标反例。完整证明需要独立审查；补充检查不替代接纳。所有标准方法不作新工具或首创主张。[Non-scientific operational metadata omitted.]\n","fact_id":"a53804d650803060","scope_bindings":[{"evidence_id":"fef1785395851e47b5ca0b719640449061718f4c670bfcd74c24cf0aec696c88","obligation_id":"e5eac888f467f9e19522d9755a04c518aea63e80192c0532f59b4d9dfecbde33","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]}}],"source_hash":"bc24d183f5299df636e67f0b439aadbcd4d79671b69c327ed7083ddfab857c6f"}]

Proof:
# T2-ANCHORED-CAUSAL-DIRECT: complete finite construction and cost proof

Obligation: 69f5064f1811226c999d4c360b455fd23b8ba59fedf8e5c638f2a307e716854e.
Author: native Prover. This text proves the exact frozen 020 conjunction.
Before the normal independent gateway accepts it, this is a submitted proof,
not a new admitted Fact.

## 1. Imported facts, quantifiers and configuration

The only direct Fact predecessors are:

* SRC fef8372728290b45, Evidence
  e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505:
  the shared tokenwise Boolean/ReLU plus finite causal attention batch-hybrid
  model, its copying/arithmetic constructions, and its comparison costs.
* 016 a53804d650803060, Evidence
  fef1785395851e47b5ca0b719640449061718f4c670bfcd74c24cf0aec696c88:
  for the original full-trajectory add-one predictor,
  sup E TV(p^+_(Y_M),theta_(Y_M)) <= min(1,48T), for K>=2,M>=1.

Their native evidence is PASS/VALID and their Fact-file hashes match its
content hashes; source-check-v1.json records the check. We do not import
019, the cut lower bounds, any former file PASS, or any stationary/mixing
assumption. All new head algebra, finite error, integer recovery and costs
are proved below. Standard building blocks are restated to make their
applicability to these new heads explicit.

Fix integers K>=2, M>=1. Set N=M+2, n=q=N+1. The observed symbols are
x_1,...,x_N in {0,...,K-1}; x_q=0 is a zero vector, not a new observation.
For any declared s=(a,beta_symbol), write C_c for its triple count among
t=3,...,N, J=sum_c C_c and p_c^+=(C_c+1)/(J+K). These are mathematical
definitions, not a freely supplied count table. The actual mode uses
s=(x_(N-1),x_N). The source theta may have zeros and mu is arbitrary;
parameters and program never depend on either. All deterministic
statements quantify over every history and every declared query,
including histories of probability zero under a particular source.

Let h>=max(4,ceil(log2 M)+1) and set

    Q=2^h, b=ceil(log2(M+1)), ell=ceil(log2(N+K+2)),
    g=max(h,2b+12), G=2^g,
    p=4h+4ell+64, u=p_a=4g+4ell+64.

We use u in the proof to avoid confusing the two precision parameters.
For every M>=1, Q>=2M>=M+1, hence h>=b. Consequently g<=2h+12 and

    u<=8h+4ell+112<=8h+8ell+128=2p.

Put D_*=4M+1. Since 2^b>=M+1,

    G>=4096(M+1)^2>=64(4M+1)^2.                 (1)

In particular G>=64D_*^2>=4D_* and g>=h. All powers here have finite
binary representations. ceil(log2 v) for an integer v>=1 is obtained
by scanning the bits of v-1; no real logarithm is a program operation.
The mathematical logarithms in bounds or in ideal comparison heads do
not enter the actual finite evaluator.

## 2. Causal front end and dataflow at every token

Use two singleton copying heads with zero QK score and value x_t.
At positions t>=3 they attend respectively to t-2 and t-1; their values
are l2_t=e_(x_(t-2)) and l1_t=e_(x_(t-1)). At t=1 the missing lags use
self, and at t=2 only the missing second lag uses self. All selected
values there are still one-hot. At q these same offsets return the
observed endpoints e_(x_(N-1)),e_(x_N). Each singleton head has a
nonempty finite causal mask, weight exactly one, and exact copied
bits even under the finite evaluation in Section 4. Retain the input
value x_t and the public flag f_t=1{t=q} through this stage using paid
residual copies and holds.

An external query has two one-hot fields A_ext,B_ext only at q, with
zero placeholders at past positions. A mode bit specifies external
or actual at q. A shared bit-mux selects A_q,B_q from these fields or
the two copied endpoints. At a history position choose
A_t=l2_t,B_t=l1_t, independently of the final query or mode. This can
be implemented with f_t and bit muxes by the same map at every token.
Both choices are one-hot. External query acquisition, zero placeholders,
flag/mode fields and endpoint retention are charged. No broadcast from
q to any earlier position occurs.

All statistical heads share the tokenwise key and value

    k_t=((1-f_t)l2_t,(1-f_t)l1_t),  v_t=(x_t,f_t).          (2)

The products in (2) are Boolean gates. At every historical key they use
only its present and past symbols, never A_q,B_q. At q the key is zero
and the value is (0,...,0,1). This is a public unit anchor; it contains
no source symbol. The query at token t for head (alpha,beta) in {0,1}^2
is ((alpha L2)A_t,(beta L2)B_t), where L2 is constructed in Section 4.
For ideal comparisons alone replace L2 by ln 2.

For each of the four heads the allowed keys at q are
{3,...,N,q}. At historical t>=3 they are {3,...,t}; at t=1,2 use self
as the declared fallback for the empty set. These are nonempty
causal masks, including permitted self edges. All masks are stored
finite bits, never numeric minus infinity. The past rows may have
different local queries and no anchor, but are evaluated by exactly
the same finite loops and pointwise decoder as q.

There are two copying heads in the first attention stage and four
statistical heads in the second: six in total and at most four in
one layer. Maximal QK dimension is 2K. Each statistical value has K+1
coordinates, giving 4K+4 returned scalars at each token. The history
is consumed through these explicitly charged attention inputs. After
the statistical heads finish, downstream decoding has only these
returned banks, public parameters and the declared retained exact
bits. Exponentials, clean sums and division remainders from attention
are cleared/released; the decoder has no extra count table or raw
history port. Retaining input storage while computing the heads is
a paid batch resource. This is not the earlier late-query no-reread
cut before the final two observations.

## 3. Ideal integer identities

At q let i_t=1{x_(t-2)=a}, j_t=1{x_(t-1)=beta_symbol}, for t=3,...,N.
The ideal historical scores and weights are

    s^*_(alpha,beta)(q,t)=ln2(alpha i_t+beta j_t),
    w_(alpha,beta)(t)=(1+i_t)^alpha(1+j_t)^beta in {1,2,4}.

The anchor has score zero and weight one. There are exactly M
historical keys, one for each original departure. Define

    D_(alpha,beta)=1+sum_t w_(alpha,beta)(t),
    S_(alpha,beta),c=sum_t w_(alpha,beta)(t)1{x_t=c}.

Then 1<=D<=4M+1, 0<=S_c<=4M and, more precisely,

    S_c+1<=D.                                           (3)

The ideal returned coordinates are y_c=S_c/D and z=1/D. For each key,

    (1+i_t)(1+j_t)-(1+i_t)-(1+j_t)+1=i_t j_t.

Multiplying by its label indicator and summing proves

    C_c=S_11,c-S_10,c-S_01,c+S_00,c.                    (IDEAL)

No independence or probability argument is involved. The construction
is standard product expansion, inclusion-exclusion and normalization
by a known anchor. All query correctness concerns one run for one
query; it does not give K^2 simultaneous outputs for free.

## 4. Finite log, exponential and all-row HEAD error

Write R=2^u and epsilon=2^(-u). Generate exactly the rational

    V=2 sum_(j=0)^(u-1) (1/3)^(2j+1)/(2j+1),
    L2=R^(-1) floor(R V).                              (4)

The finite geometric-series identity integrated on [0,1/3] gives
ln2=2 sum_(j>=0)(1/3)^(2j+1)/(2j+1). Its positive tail after u terms
is at most 2(1/3)^(2u+1)/[(2u+1)(1-1/9)]<=2^(-2u).
Thus 0<=ln2-L2<2epsilon. Also 0<=L2<=ln2<1; for example
ln2=integral_1^2 dt/t<1. Each actual score is exactly one of
0,L2,2L2, since both query selectors are one-hot and the gated key
blocks are one-hot or zero. This includes the self fallbacks and
q's zero key. All actual and ideal scores lie in [0,2] and

    0<=s^*-s<4epsilon.                                (5)

There is no rounding of a score product before its declared sum.
Products with bits are exact; any dense zero terms are still charged.

For a score s=S/R, S a nonnegative integer, use the SRC finite
recurrence, now with parameter u:

    T_0=R,
    T_j=floor(T_(j-1) S/(jR)), 1<=j<=8u,
    W=sum_(j=0)^(8u) T_j,  w_tilde=W/R.                (6)

Each floor is exact long division of the full integer product with
its remainder; jR>0. Induction gives 0<=T_j/R<=s^j/j!, so
1<=w_tilde<=exp(s)<=4 (the bound 8 also suffices). At s=0 every
T_j for j>=1 is zero: the anchor and zero-score weights are exactly
one, not approximations to one.

If e_j=s^j/j!-T_j/R, then e_0=0 and
0<=e_j<=s e_(j-1)/j+epsilon. An error introduced at any step k
contributes at most epsilon sum_(a>=0)2^a/a!<8epsilon to the sum
of all later term errors. Indeed (k+1)...(k+a)>=a!, and
exp(2)<8 follows, for instance, by bounding its tail after a=4
with a geometric series of ratio at most 1/3.
Summing the 8u possible introduced errors gives 64u epsilon.
For j>=9, 2^j/j!<=2^(-j), by the case j=9 and the successive
ratio 2/(j+1)<=1/2. The omitted tail after 8u is at most
2^(-8u)<=epsilon. By (5) and the derivative exp(s)<8 on [0,2],

    |exp(s^*)-w_tilde|
       <=(64u+1+32)epsilon<=100u epsilon.              (7)

For any row with m>=1 allowed keys and any one value coordinate
v_t in {0,1}, keep exact integer sums
D_int=sum_t W_t and A_int=sum_t W_t v_t. Then
D_int>=mR, 0<=A_int<=D_int. If A^*,D^* denote the analogous ideal
real sums, both numerator and denominator perturbations are at most
m e_w, e_w=100u epsilon. Writing a ratio difference as a numerator
difference plus (A^*/D^*) times a denominator difference gives

    |(A_int/R)/(D_int/R)-A^*/D^*|<=2e_w.              (8)

The denominator D_int/R>=m and ideal ratio lies in [0,1]; hence
there is no factor m left in (8). This proof needs only bit-valued
values, bounded scores and a nonempty mask, which all new heads,
the added self anchor and the prefix/fallback rows have.

Return the G-grid coordinate

    H=G^(-1) floor(G A_int/D_int).                     (9)

It lies in {0,1/G,...,1}; its numerator is a (g+1)-bit unsigned
integer, including the endpoint G. Final division adds less than
1/G error. For integers u>=32, 200u<=2^(u/2), as checked at 32
and preserved since 1+1/u<=sqrt(2). Our u>=4g+64 implies

    200u 2^(-u)<=2^(-u/2)<=2^(-g).

Combining (8)-(9) proves every returned coordinate differs from
its corresponding ideal head coordinate by at most 2/G. In
particular at q write the label and anchor coordinates Y/G,Z/G:

    Y,Z in {0,...,G}, |Y/G-y|<=2/G, |Z/G-z|<=2/G.    (HEAD)

At other rows the ideal coordinates mean their own local-query
prefix/fallback normalized values, not q's S/D formulas. Their
anchor value is zero, so their finite anchor numerator is exactly
zero. Singleton copying values are copied exactly by (9), since
their coordinate numerator is zero or equals their denominator.
This establishes the new heads' applicability without importing
the old four heads' specific algebra.

Formula (4) is an actual finite computation. A common denominator
3^(2u-1) product_(j=0)^(u-1)(2j+1) suffices, with O(u log(u+1))
bits. Serial construction of its factors, the u term numerators,
their sum and the final quotient by school arithmetic costs
O(u^3 log^2(u+1)) bit operations and O(u log(u+1)) scratch bits.
The long exact offline integers are multiword arrays; online only
the u-fractional-bit dyadic L2 is stored. No real log or exp oracle
is involved.

## 5. Integer recovery with the prescribed margin and guards

Fix a head and label at q and abbreviate its ideal values by S,D.
Let delta=2/G. By (1), D<=D_* and delta D<=1/2. HEAD gives

    Z/G>=1/D-delta>0,

so the integer Z>=1. Subtract the ideal integer ratio, using (3):

    |Y/Z-S|
      <= (|Y/G-S/D|+S|Z/G-1/D|)/(1/D-delta)
      <= delta D(1+S)/(1-delta D)
      <= (2D^2/G)/(1-2D/G)
      <=4D^2/G<=4D_*^2/G<=1/16.                    (SNAP)

The strict positive denominator and the useful S+1<=D follow
from the unit anchor, including S=0 and S=4M. Half-up integer
division is therefore exact:

    floor((2Y+Z)/(2Z))=floor(Y/Z+1/2)=S.             (10)

The possible ratio lies in [S-1/16,S+1/16], entirely inside the
half-up rounding interval for S. No equality at a half-integer
is possible. Formula (10) uses a full integer numerator and
positive denominator, not a rounding oracle.

At every token execute instead the following common, safe decoder:

    Z_safe=max(1,Z),
    U_(alpha,beta),c=
        clip_[0,4M]( floor((2Y_(alpha,beta),c+Z_safe)/(2Z_safe)) ),
    C'_c=clip_[0,M](U_11,c-U_10,c-U_01,c+U_00,c).    (11)

All intermediate differences are signed. At q, SNAP makes Z_safe=Z,
each U equals the ideal S in its clip range, and IDEAL makes C'=C
in [0,M]. At non-q tokens Z may be zero; (11) still divides by
a positive integer. There 0<=C'_c<=M, but sum_c C'_c can be KM.
We retain this larger sum in both the arithmetic and cost bounds;
we do not assume those outputs are true query counts.

At every position form positive integers B_c=C'_c+1 and
D_out=sum_c B_c. Thus K<=D_out<=K(M+1). For c=0,...,K-2 calculate

    m_c=floor(Q B_c/D_out),
    m_(K-1)=Q-sum_(c<K-1)m_c,
    F_c=m_c/Q.                                       (12)

All quotients and remainders are computed in full. Each m_c>=0
and their partial sum is at most Q; indeed it is strictly below Q
because the omitted B_(K-1)>0. The residual lies in [1,Q].
Consequently (12) is a legal probability vector at every token.
There are K(h+1) numerator bits, preserving the case m_(K-1)=Q.

At q formula (12) is exactly the ordered dyadic map Gamma_Q(C_s).
For a positive normalized vector p and its ordered Q rounding,
put e_c=p_c-floor(Qp_c)/Q in [0,1/Q) for c<K-1. The last coordinate
error is minus sum e_c, hence TV equals sum e_c. Applied at q,

    F_anc(x;s)=Gamma_Q(C_s),
    TV(F_anc(x;s),p_s^+(x))<=(K-1)/Q.               (EXACT-READOUT)

This covers M=1, J=0, unvisited query rows, all-zero and deterministic
histories, all alphabet sizes, head grid endpoints and any
zero-probability history. No assumption about occurrence of the
declared query has been made. The other n-1 outputs are computed
and paid even though only q's vector is exposed as the answer.

## 6. Actual risk, precision and sufficient sample configuration

By EXACT-READOUT on each path, the triangle inequality and the
imported 016 actual add-one bound,

    sup_(theta,mu) E TV(F_anc(X;Y_M),theta_(Y_M))
       <=min(1,48T+(K-1)/Q).

For every M>=1, sqrt(M+1)<=2M and Q>=2M. Also K-1<=K^(5/2).
Thus (K-1)/Q<=K^(5/2)/sqrt(M+1)=T, including M=1.
This proves the requested min(1,49T) RISK bound. The argument is
pathwise transfer followed by an unconditional expectation,
not conditioning on the actual row and asserting iid data.

If 0<tau<1, M+1>=(64K^(5/2)/tau)^2 and h=h0(M),
then T<=tau/64 and risk<=49tau/64<tau.
At the smallest such integer M,
log2(M+1)=O(1+log2 K+log2(1/tau)); the same holds for h0,b,ell,g
and hence u. A positive rational tau can configure M using integer
comparisons of (M+1)tau^2 with 64^2 K^5; charge its input length
and arithmetic separately if configuration is requested. The program
itself only takes public integer K,N,h, and uses no square-root oracle.

The risk is that of this new finite program. We do not identify its
output bits or true risk with Pi, or import Pi's 9K+1 master bank,
V bank, or 36delta fault interface into the new 4K+4 bank.

## 7. Explicit Boolean/ReLU arithmetic and the shared circuit schedule

The following gives the actual finite pointwise circuit, not a
generic unrolling of a sequential machine. For bits a,b use

    AND(a,b)=ReLU(a+b-1), NOT(a)=ReLU(1-a),
    XOR(a,b)=ReLU(a-b)+ReLU(b-a), OR=a+b-AND.

Bit muxes use two ANDs and an OR. Unsigned identity is an identity
ReLU; every live channel crossing a layer has a charged identity
hold. Signed differences use sign/magnitude bits or two nonnegative
rails. Ripple addition computes the sum from two XORs and the carry
from OR(AND(a,b),AND(carry,XOR(a,b))). Borrow subtraction and
high-to-low comparison use the analogous constant-size bit stages.
On w-bit inputs these need O(w) active gates/depth. School
multiplication adds all shifted partial products, retaining the
full 2w-bit result, with O(w^2) active gates/depth and O(w) scratch.
Restoring division scans all numerator bits high-to-low, shifts the
remainder, compares it with the positive divisor, conditionally
subtracts and emits the quotient bit. The post-step remainder is
below the divisor and the trial remainder below twice the divisor.
This uses O(w^2) active gates/depth and O(w) scratch also for
numerators of a fixed multiple of w bits. There is no early exit;
all loop bounds are public and choices are muxes.

Head-grid extraction is a finite-grid ReLU construction. Given H
in the G-grid, start with A_g=GH. For j=g,...,0 set

    b_j=ReLU(A_j-(2^j-1))-ReLU(A_j-2^j),
    A_(j-1)=A_j-2^j b_j.

Inductively the integer A_j is in [0,2^(j+1)-1] after the first
step (initially [0,2^g]); b_j is its exact j-th bit and
0<=A_(j-1)<2^j. The case H=1 uses the top bit j=g. Each scalar
uses O(g) active gates and depth, with paid residuals and thresholds.
This is not a claim that continuous ReLU implements floor off grid.
Analogous extraction of a score numerator, if scalar storage is
used, has top index u+1. Final dyadic decoding is a paid linear
sum of output bits with coefficients 2^(j-h).

Expand the 4K+4 returned scalars in parallel into bit banks.
Retain them and the O(K) exact query/endpoint/flag fields where
needed. Compute four Z_safe values. For each of the K labels in
fixed order, perform the four full divisions and clipping in (11),
then signed inclusion-exclusion and its clip. Store its C'_c bits.
After all K labels, sum C'_c+1 by ripple addition and then perform
K-1 full quotient/remainder calculations (12), accumulate the
partial quotient sum, and write/decode the residual. The O(K)
full word arithmetic tasks can be serial; each uses O(u^2)
active gates/depth and O(u) scratch by the word bounds below.
All bank words and unfinished outputs are explicitly held over
the intervening layers. Front-end bit gates, two copying heads,
four statistical heads, QKV projections, all guards and final
decode are actual stages of this same shared circuit.

There are O(Ku) live logical bit/scalar channels. The depth is
O(Ku^2) and per-token width O(Ku). Active arithmetic and projection
records before holds total O(Ku^2+K^2); the K^2 term conservatively
covers tokenwise projection maps. A linear decode has O(h)
summands per output, included in the term count; it is not an
unbounded free summation gate. All live channels have identity
holds through every layer, at most

    O((Ku^2)(Ku))=O(K^2 u^3)                         (13)

hold records. This includes residual copies, extraction residuals,
carries, input fields retained between heads, all four banks and
unfinished outputs. Layer scheduling and wiring are public;
the same circuit is executed on all n positions. No packed-RAM
persistence or query-only decoder is used to obtain these figures.

## 8. Online word lengths, dense and sparse formats

Here and below all big-O constants are absolute and independent of
K,M,h, source, history and query. The symbol u always denotes the
actual p_a of this implementation, not the original Pi parameter p.

For the finite exponential, 0<=S<=2R, every T_j and W is <=8R,
a full T_(j-1)S product uses at most 2u+6 bits, and jR for j<=8u
uses at most u+ceil(log2(8u))+1 bits. A head denominator is at most
8nR and has at most u+ell+4 bits. A full head dividend G A_int
has at most u+g+ell+4 bits. Remainders and trial shifts need only
a constant number of additional bits. These bounds hold at every
prefix and fallback row.

The returned Y,Z lie in [0,G]. In (11), 1<=Z_safe<=G,
2Y+Z_safe<=3G and 2Z_safe<=2G. The un-clipped quotient is at
most 2G; its clipping is performed before any inclusion-exclusion.
Each clipped U is in [0,4M], so signed pairwise differences and
their sum lie in [-8M,8M]. Clipped C' lies in [0,M].
The final normalizer is at most K(M+1), requiring at most
ceil(log2 K)+b+1 bits; a full final dividend Q(C'_c+1)
requires at most h+b+1 bits. Its quotient is in [0,Q],
and trial remainders are below twice the normalizer. The
partial output sum stays at most Q. None of these ranges use
the true-q count identity to justify a non-q computation.

For an explicit safe scalar convention, use sign plus 16u integer
and 16u fractional positions for working scalar registers and
coefficients; retain each full double-width product in a separate
temporary, with sign and accumulation guards, before a declared
quotient/truncation. The largest actual payloads just listed,
extraction thresholds 2^g and 2^(u+1), score numerators and fixed
bit-gadget coefficients fit far inside these allocations.
All bit operations are exact. Offline long rational integers are
arrays with the separately counted total scratch, not one online word.

One may choose the constant-size bit gadgets and the serial schedule
above with per-layer channel/term counts bounded by 2^16 K u,
and depth bounded by 2^16 K u^2; these deliberately loose constants
cover four ratio divisions, one final division per coordinate,
banks, muxes, extraction and residuals. Hence a dense neuron has
at most 2^16 K u products. Its accumulation needs at most
16+ceil(log2 K)+ceil(log2 u)+2 additional integer guard bits.
Since log2 K<=ell<=u/4, log2 u<u, u>=64, these guards together
with a full 64u+O(1)-bit product remain below 128u bits.
The smaller attention and integer arithmetic bounds also fit.
Program indices and addresses have lengths O(u); e.g. layer,
slot, token and edge counters use sums of log2 K, log2 n and
O(log2 u), also within the same 128u allowance when represented
as online words. Thus the promised coefficient/arithmetic word
cap is <=128p_a bits, including complete products, remainders,
signs and guards. It is not a 128p bound merely because p_a<=2p.

Let L_neur=O(Ku^2), W_neur=O(Ku). Dense representation allocates
every coefficient slot and bias in every pointwise/QKV layer,
including zeros. The total slots are

    O(L_neur W_neur^2)=O(K^3 u^4),

and the stored coefficient bits are O(K^3 u^5). Initial/final
projections are included by the same padded width. Sparse format
instead stores every active gate/term and every identity hold,
with coefficient and source/destination addresses. Their counts
from Section 7 are respectively O(Ku^2+K^2) and O(K^2u^3);
each record needs O(u) bits because log(L_neur W_neur+1)=O(u).
The complete sparse format therefore has O(K^2u^4) bits.
No free fanout, residual edge or unlisted hold is omitted.
Dense and sparse are alternative representations, not a single
profile taking the smaller coordinate of each.

## 9. Charged finite attention and all-token online work

Fix either uncached or cached finite attention, and a representation
format. The main dense resource statement uses dense pointwise
evaluation; we do not infer a sparse runtime improvement from
sparse file size.

For each scanned/allowed edge, form the score from its projected
coordinates using O(K) word operations. Generic O(u)-bit school
arithmetic costs O(u^2) per multiplication/division; dense score
formation and the K+1 weighted value updates cost O(Ku^2) per
edge. With no cache, (6) uses 8u full multiplication/division
steps at O(u^2) each, hence O(u^3). Stream each row's positive
weights into one denominator and K+1 numerator accumulators;
do not store an n^2 numerical weight matrix. Return all its
coordinates by full (9) divisions, then clear its arithmetic
scratch before the next row. All projected token arrays are
retained and paid while needed. Score-to-integer extraction,
mask reading, control, row copies and resets fit these bounds.

There are O(n^2) candidate/effective edges for the fixed six
heads and O(n) rows per head, including the singleton heads,
the q self anchor and both fallback rows. Every non-q row is
actually evaluated. Consequently

    uncached attention online bitwork
       =O(n^2(K+u)u^2).                               (14)

A full-score cache variant evaluates exactly recurrence (6)
once at each of 0,L2,2L2, stores the resulting full integer W,
and selects by the finite score on each edge. In particular
W(2L2) is separately generated, never obtained by squaring a
rounded W(L2)/R. Weight at zero is exactly R, though the
constant can still be written and charged. A constant number
of 8u-step recurrences costs O(u^3) offline/cache generation,
in addition to (4). The cache has O(u) bits, its comparisons
and mux selectors are explicit and included in O(Ku^2) per
edge. The cached outputs are bitwise the same as the uncached
outputs for this new program. The resulting bound is

    cached attention online bitwork=O(n^2 K u^2).      (15)

In a comparison Pi is equally allowed its SRC full-score
cache 0,L2,2L2,L3,L2+L3 and pays its own generation/storage/
selectors. We do not get a comparative advantage by denying
one side caching.

For dense pointwise/QKV evaluation, process every matrix
coefficient, including zero slots, at every one of the n tokens.
Generic multiplication/addition on the stated words costs
O(u^2). Therefore

    dense pointwise/QKV online bitwork
       =O(n L_neur W_neur^2 u^2)
       =O(n K^3 u^6).                                (16)

This includes all-token (11)-(12) and their identity holds,
not merely q. Initial observed input acquisition writes NK
one-hot bits. Public flags and positions, query/mode fields,
their zero placeholders and all copied endpoints require
O(nK+n log(n+1)) additional acquisition/initialization bits
with the indicated finite arithmetic or copying cost.
Under the given one-hot interface no binary-to-one-hot
conversion is needed. If input is instead supplied in binary,
one must add its explicit conversion; that different interface
is not used to obtain these bounds. Reading/clearing input
and temporary arrays, residual copying, head extraction and
final K(h+1) bit output with dyadic decoding are paid operations,
covered by (14)/(15)/(16) as appropriate, with acquisition
listed separately. The two copying heads are not free
lookups or position oracles.

## 10. Layout, finite generation and total physical peak

Masks for six heads occupy O(n^2) actual bits, including the
self and fallback rules. Positions occupy O(n log(n+1)) bits.
Masks can be generated by nested row/key integer loops testing
the explicit rules in Section 2, with full index arithmetic
and O(u^2) work per pair; no numerical infinity is generated.
Their total generation/writes cost O(n^2u^2).
The observed history occupies NK one-hot bits. Query, endpoint,
public flag/mode placeholders and control/layout fields have
their complete allocations; none is counted as zero-cost input.

Use two rolling neural layers. Under the scalar-neural convention
each live bit channel may itself occupy O(u) physical bits.
Thus the O(Ku) per-token channels, QKV arrays, returned banks,
residuals, active word scratch and all unfinished output arrays
fit O(nK u^2) physical bits. This is a working-array bound,
not the total memory. If bits are packed in an evaluator the
bound remains conservative, but it does not identify packed
register counts with neural width. Across neural layers the
holds in (13) are still paid. Only two layers are retained,
not all training activations.

A compact finite evaluator for school arithmetic, full-score
weight generation, row summation, masks, copying, loops and
head outputs has a conservative O(u^4)-bit code allocation.
To see existence, fixed Boolean microcode plus the public
O(u^2) school-operation templates, their O(u)-bit indices/
addresses and O(u) recurrence-length metadata fit that allowance;
K and n loop counts are stored binary, not unrolled in this code.
The neural pointwise circuit is separately stored in its dense
or sparse format and is separately executed at all n positions.
The evaluator's code is not a free interpreter. Its scalar
runtime words and all counters are in the working-array bound.

Let G_rec,T_rec,I_hold be the actual generated arithmetic/
projection gate, summand/connection and hold record counts of
the serial circuit in Section 7. The fixed-arity bit gadgets,
O(Ku) extraction/decoding terms and O(K^2) projection terms give

    G_rec+T_rec=O(Ku^2+K^2), I_hold=O(K^2u^3).        (17)

Each record has O(u) coefficient/address bits and
log2(G_rec+T_rec+I_hold+1)=O(u). Explicit nested loops over
coordinates, arithmetic stages and live channels generate every
record, including holds for each live channel at each layer.
Arithmetic for a record, assigning its address and inserting it
in the ordered layout costs O(u^2) bitwork conservatively.
Even comparison sorting all records can be done by a finite
merge sort with O(log(number of records)) comparisons per
record on O(u)-bit keys. Thus generation/arrangement uses

    O((G_rec+T_rec+I_hold)u^2) work,
    O((G_rec+T_rec+I_hold)u) scratch.                 (18)

This explicitly pays circuit layout, rather than relying on
an existence theorem for arithmetic circuits.

Dense generation additionally sweeps every one of O(K^3u^4)
slots and all biases, writes its O(u)-bit coefficient including
zero, and performs the requisite address/selection work.
The sorted active-record list can be merged sequentially with
the lexicographic dense slot sweep; no per-slot scan of the
whole record list is needed. Allowing O(u^2) per slot is a
safe full generation and write cost O(K^3u^6). Sparse format
writes each addressed record including every hold instead.
The compact evaluator code and public fields are also
generated and fully written, at worst O(u^5) work, which
is absorbed by K^3u^6. All loops are finite, using finite
integer shifts/bit scans for the public lengths.

In addition to (18) and full-format writes, charge log
generation O(u^3 log^2(u+1)), with O(u log(u+1)) scratch
as proved in Section 4; optional cache generation O(u^3)
and O(u) cache storage; masks and positions O(n^2u^2);
all layout, selector, microcode, input initialization and
output-buffer allocation writes. From (17)-(18) and K>=2,

    total offline work
       =O(K^3u^6+n^2u^2+u^3 log^2(u+1)).             (19)

One-hot acquisition NK and metadata writes are no larger than
the displayed polynomial allowances, but are retained as
named items. Expensive rational log scratch coexists with
whatever program/input data has already been generated,
and is not subtracted from the phase total.

For clarity, the simultaneous live items can be bounded as follows;
constant multiple copies are included in each row.

|Live item|Physical bits|
|---|---:|
|Dense parameters, zero slots, biases and public layout records|O(K^3u^5)|
|Complete masks and positions|O(n^2+n log(n+1))|
|Observed one-hot history|NK|
|Query/mode, endpoint copies, flags and input placeholders|O(nK+n log(n+1)) or their scalar copies inside the rolling allowance|
|Rolling layers, live QKV, four returned banks, residuals, arithmetic scratch, controller and output|O(nKu^2)|
|Compact finite evaluator code|O(u^4)|
|Exact rational log generation arrays when live|O(u log(u+1))|
|Circuit-record generation/sorting arrays when live|O((G_rec+T_rec+I_hold)u)=O(K^2u^4)|
|Optional finite full-score cache and selectors|O(u) plus its charged circuit terms|

Since log(n+1)=O(n), NK<=nK and n>=4, the sum of ALL these
items is bounded by

    P_dense=K^3u^5+n^2+nKu^2+u^4+u log(u+1).          (20)

The bound also allows offline generation buffers and forward
buffers to coexist; alternatively releasing an offline buffer
only lowers the relevant phase sum. Thus both offline and
forward phase-total peak are O(P_dense), not just the rolling
term. After the heads, release/erase the unused input/QKV and
their arithmetic scratch at actual charged cost before the
decoder can access only its stated banks. No clean numerator
or residual side port is left available.

For a sparse parameter format replace K^3u^5 in (20) by its
actual O(K^2u^4) program/record term and retain every other
term and phase rule. The generation scratch in (18) then
still fits that term. This is a separate representation,
and does not assert a sparse online speedup or permit one
to mix sparse storage with an unrelated time/cap claim.
Keeping every layer's activations, constructing a new
physical fault injector, or expanding to PURE would be
different executions with additional costs; none is used
in (13)-(20).

## 11. Complete cost statement and comparison boundary

Collecting the construction, with u=p_a, gives all requested
coordinates for the same batch-hybrid program:

|Coordinate|Proved bound|
|---|---|
|Neural depth / per-token width|O(Kp_a^2) / O(Kp_a)|
|Total heads / max simultaneous; QK dimension; score cap|6 / 4; 2K; 2|
|Online coefficient and arithmetic word|<=128p_a bits including products, guards and remainders|
|Dense slots / parameter bits|O(K^3p_a^4) / O(K^3p_a^5), including zeros and biases|
|Active gates/projections / identity holds|O(Kp_a^2+K^2) / O(K^2p_a^3)|
|Full sparse program, coefficients, addresses and holds|O(K^2p_a^4) bits|
|Masks / positions|O(n^2+n log(n+1)) bits|
|Input and query acquisition|NK observed one-hot bits plus the complete query/endpoint/flag acquisition and copies described above|
|Rolling work only|O(nKp_a^2) bits|
|Uncached attention online work|O(n^2(K+p_a)p_a^2)|
|Fair full-score cached attention online work|O(n^2Kp_a^2), plus generation/storage/selectors|
|Dense pointwise/QKV, all n tokens|O(nK^3p_a^6) bitwork|
|Finite rational log generation work / scratch|O(p_a^3 log^2(p_a+1)) / O(p_a log(p_a+1))|
|Compact evaluator code|O(p_a^4) bits|
|Complete offline work|O(K^3p_a^6+n^2p_a^2+p_a^3 log^2(p_a+1))|
|Dense online/offline total phase peak|O(P_dense) as in (20)|

Each all-token and per-edge term is actually charged in this
construction. In particular exact recovery does not license
omitting non-q decoding, earlier-token QKV, or positive-
denominator guards. The neural depth does not include a
fictional constant-time log/exp operation: attention is the
separately charged finite evaluator of this hybrid model.
The smaller depth/width figures come from the explicit
pointwise bit circuit plus allowed attention stages,
not from an uncharged generic sequential-machine simulation.

The direct predecessor SRC already supplies the original Pi's
analogous full upper-bound package with p. Since p_a<=2p,
every polynomial bound here lies in a constant multiple
of that same asymptotic upper envelope, and
log(p_a+1)<=log(2(p+1)) handles the log factors. This states
common constructive upper bounds. It proves neither actual
cost dominance nor that the new program meets Pi's exact
numerical componentwise caps. Its real word bound remains
128p_a; its four banks and guards have their own dimensions.
No old K=2 exact allocation is generalized to arbitrary K.
No single-kernel rank lower bound is applied to these four
separate normalized heads and nonlinear integer decoding.

Under the smallest sufficient sample configuration in Section 6,
p_a=O(1+log K+log(1/tau)). This is a standard substitution into
complete proved bounds, not a new statistical rate or an
algorithmic resource lower bound.

## 12. Prior sources, scope and evidence limits

The local writing source
inputs/source-v10/stage2-count-snap-prior/strong-comparison-proof-r1.md
already discusses B-C triple features, B-J joint features, the
restriction of its single-joint-kernel rank argument and prior
count-recovery/inclusion-exclusion methods. Its Section 9 records
D'Angelo et al. 2607.02800v1 (lag matching and subset-count inversion),
Ye et al. 2410.05258v1 (differential normalized attention),
Zhou et al. 2410.05493v3 (count recovery), Rajaraman et al.
2407.17686v1 and Ekbote et al. 2508.07208v2 (shallow k-gram
constructions). Those prior-source references are preserved as
provenance, not new theorem dependencies or a new comprehensive
literature verification in this proof.

The retained primary-source pointers from that local record are:
D'Angelo et al., https://arxiv.org/html/2607.02800v1#S3.Thmproposition1
and its Appendix D.2; Ye et al.,
https://arxiv.org/html/2410.05258v1#S2.SS1; Zhou et al.,
https://arxiv.org/html/2410.05493v3#A7.SS2.SSS2; Rajaraman et al.,
https://arxiv.org/html/2407.17686v1#S5.Thmtheorem1; Ekbote et al.,
https://arxiv.org/html/2508.07208v2#S4. These links identify preserved
prior-source attribution; no result in this proof depends on a new
reading or an unproved extension of those papers.

The accurate overlap is product matching, cancellation of lower
order terms, and recovering counts from normalized statistics.
The implementation established here specifies this particular
synthetic self anchor, four 2K-dimensional heads, finite lower
log/8u-term evaluator, amplified precision g, exact half-up
recovery, non-q guards and the complete shared-batch resource
and lifetime accounting. We do not claim the algebra, anchor,
rounding, or Boolean/ReLU methods are new tools or first uses,
or that the entire front end is novel. The 010 whole-program
Counter assessment is only a model-boundary writing source:
a low-space sequential scanner is not this shared causal batch
network. Neither old source-file PASS nor a local search with
no match is an admission or a novelty proof.

All inequalities above preserve the original experiment and
same-trajectory actual mean risk. There is no independent
test query, no conditioning-iid shortcut, no extra source
observation, and no forecast of an unobserved target symbol.
The finite head identities hold even where a given theta
would assign the history probability zero. A query run is
not free simultaneous all-query evaluation. This construction
is outside the 017--019 late-query no-reread cut, so those
cut lower bounds are not applied here.

This is an analytic finite-circuit and cost proof. No new
compiler, emitter, large enumeration, literal instruction
ledger, GPU computation or exact cycle measurement was run.
The original root, SRC, 014--019, their dependencies and
[Non-scientific operational metadata omitted.] Stationary
initialization/mixing questions assigned to Dot/VALG are not
part of the proof. General resource tradeoffs, same numerical
caps, arbitrary Transformer optimality, physical fault correction
and general-K fault allocations remain outside the conclusion.
The conjunction CONFIG/IDEAL/HEAD/SNAP/EXACT-READOUT/RISK and
the entire stated COST package is what is submitted to the
normal independent gateway for this exact obligation.
