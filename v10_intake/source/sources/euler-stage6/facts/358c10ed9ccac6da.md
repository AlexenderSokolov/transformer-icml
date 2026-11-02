---
fact_id: 358c10ed9ccac6da
problem_id: icml-general-prediction
author: prover
predecessors: [e7e6b1b84b74cbea, a53804d650803060]
glossary_introduces: {}
external_refs: []
statement_chars: 6128
---

## statement
# T2-COMPRESSED-CUT：单纯形行表编码与截断访问数的晚 query 切口容量匹配候选

017的完整正常接纳已核：Fact e7e6b1b84b74cbea，Evidence 28049650420d2e560f81570f2afb3a30128c98f3b474a03a4cdcc346a77567fe；其MEM/BITS与全计数基线保持原scope和依赖。本项为独立后继，拟关闭017切口容量上下界中的log K差距。不是重新提交017，也不是把packed寄存器称为神经width。旧root、SRC及014–017等接纳保持；本候选尚未证明，完成亦不宣告v10完成。

## 1. 同一原实验与信息接口

整数K>=2、M>=2，N=M+2；任意允许零边的齐次二阶theta和任意初始对律mu，每条实验内固定。观察X_1^N，Y_i=(X_(i+1),X_(i+2))，departure i=0,...,M-1。完整计数C_(s,c)、J=n_(Y_M)及p^+_(s,c)=(C_(s,c)+1)/(n_s+K)沿016/017定义。T=K^(5/2)/sqrt(M+1)。目标仍为同轨迹actual E[TV(output,theta_(Y_M))]，TV是L1的一半。

算法类恰为017的晚query、禁止回读切口：在读完X_1^M后、读最后两个真实符号X_(M+1),X_(M+2)前，encoder只留下至多2^s值的消息I；此后decoder只获I、这两个实际符号、公开参数及源独立随机性。全部跨切口历史相关endpoint、地址、控制、停止时刻、缓存、residual和其他token状态均计入I。程序、码本、公开参数均不依隐藏theta/mu。prefix encoder计算不受限；允许017已定义的随机共同算法，以下上界给一个共同确定有限算法。切口容量不限制切口前工作峰值，也不允许把峰值漏报。末对不是新添的独立query，upper不假定它独立prefix。

R_cut(K,M,s)保持017定义。另定义s_req(K,M,tau)为存在该共同切口算法且sup actual风险<=tau的最小非负整数s；若不存在，取+infinity。此定义用存在算法，不假定某个风险infimum达到。

## 2. 具体有限编码及容量承诺

公开编码精度为整数r>=1，令

    eta=2^(-r), R=K*2^(r+4), H=2^(r+3),
    B=ceil(log2 K), b_M=ceil(log2(M+1)),
    L=ceil(log2 binom(R+K-1,K-1)),
    s_pack=K^2*(L+r+4)+2B.                         (PACK)

R是内部单纯形分母，可以不是2的幂；最终输出另用合法Q=2^h。h>=h0(M)=max(4,ceil(log2 M)+1)。所有参数由公开整数有限生成，不调用实数log/floor oracle；位长/二项系数可以用整数循环确定。

令D_(s,c)为prefix X_1^M的M-2次departure计数，v_s=sum_c D_(s,c)，p^0_(s,c)=(D_(s,c)+1)/(v_s+K)。encoder用017已收费全计数前端获得它们。对每行s，以前K-1坐标向下取整和末坐标补残差定义

    t_(s,c)=floor(R*p^0_(s,c)), c<K-1,
    t_(s,K-1)=R-sum_(c<K-1)t_(s,c), q_s=t_s/R,
    a_s=min(v_s,H).

每个t_s是K个非负整数和为R的weak composition。固定公开字典序，以其在全部binom(R+K-1,K-1)个compositions中的rank存为L bits。a_s在0,...,H中，用r+4 bits，包括a_s=H。按全部K^2行的固定顺序写出这些rank/count字段，再附prefix最后两个真实符号的2B bits。将原counts、q坐标临时数组、余数、搬运副本等全部擦除，控制/地址/读头重置到公开位置后才开放最后两个符号。不存在免费prefix endpoint或隐藏rank码表。

待证：该编码全路径合法，所有历史相关信息值数<=2^(s_pack)，并有

    L <= (K-1)(r+7), s_pack <= K^3(r+7).            (CAP)

须给stars-and-bars双射、rank/unrank有限算法及容量估计。可用binom(n,k)<=(en/k)^k、e<3和K/(K-1)<=2，给逐步有限常数比较。不能逐坐标固定宽存K个数后忽略其额外log K，也不能把存在码本当免费编码器。未使用的rank/endpoint二进制格式可约定输出固定合法概率向量；所有真实历史所产生的消息必须按原算法正确解码。

## 3. 最后两个真实符号的全路径修正

prefix最后两符号为(u,v)，新符号为(A,B')，实际query s_*=(A,B')。两个新triple恰为(u,v,A)、(v,A,B')。由这四个符号计算对每个row s的新增标签计数z_s及k_s=sum_c z_(s,c)<=2；只需取s_*对应部分。decoder通过消息的付费顺序扫描取得q=q_(s_*)和a=a_(s_*)。

在a<H分支，v_(s_*)=a精确已知，构造

    q' = ((a+K)*q+z_(s_*))/(a+K+k_(s_*)).

在a=H分支，取q'=q，忽略至多两次新departure。注意a=H包括v=H，不允许误作精确v。待证明每条完整历史上q'是概率向量且

    TV(q',p^+_(s_*)) <= (K-1)/R+2/H <= 5eta/16. (BRIDGE)

证明须保留M=2的空prefix计数、v=0、k=0/1/2、两次departure相同row、a=H边界、任意零概率历史。small-count分支用同权重凸组合控制量化误差；large-count分支须严格比较完整add-one与prefix add-one，不能直接把q当经验分布或删除真实数据后改变统计实验。upper为逐路径陈述，不使用随机末行条件iid或独立性。

最后按ordered floor/residual将q'转为分母Q=2^h的概率向量F_(K,M,h,r)，完整有理分子分母通过有限整数乘除求出。证明

    TV(F,p^+_(Y_M)) <= 5eta/16+(K-1)/Q,
    sup E TV(F,theta_(Y_M))
      <= min(1,48T+5eta/16+(K-1)/Q)
      <= min(1,49T+5eta/16).                       (RISK)

48T只引用016 Fact a53804d650803060已接纳的同actual上界；(K-1)/Q<=T须给全有限参数推导。F是新程序，不声称与原Pi或017全计数程序的逐位输出/真实风险相同。

## 4. 联合样本与切口容量结论

对0<tau<1取r=max(1,ceil(log2(1/tau)))、h=h0(M)。当

    M+1 >= (128K^(5/2)/tau)^2                     (SUFF)

时，待证RISK<=89tau/128<tau，且s_pack<=K^3(r+7)。公开tau只用于选择整数配置，算法实际只收K,M,h,r；若输入tau为正有理数，配置选择用有限整数比较实现，费用另计入公开配置生成，不用实数oracle。

特别对K>=12、0<tau<2^-16及满足SUFF的任意整数M，结合017的原MEM/BITS，证明

    (K^3/3072)*log2(1/tau)
       <= s_req(K,M,tau) <= 2K^3*log2(1/tau).      (CUT-MATCH)

整数容量须保留相应上整/下整含义，可优先给精确L、s_pack和d log2(1/(96tau))再作上述实数比较。下界只用017的d>=K^3/1536及log2 96<7；不重新证明或扩展其母源/随机算法scope。

同范围内任何共同切口算法risk<=tau仍必要M+1>=2^-32 K^5/tau^2（017的JOINT-NEC）。因此在这个精确算法类和小tau域，有一个同时达到样本O(K^5/tau^2)、切口容量O(K^3 log(1/tau))的算法；对应两个坐标各有常数因子必要性。必要性分别量化，不把两个lower相加、不声称同一个源同时实现两个障碍，也不把不同M的source supremum改成同源forall horizons。

只在本义务经正常独立网关接纳后，方称上述参数域的样本与切口容量阶匹配。数值常数、接近1的tau域、切口前在线内存以及神经资源最优均不由CUT-MATCH得到。

## 5. 有限实现与完整收费承诺

使用017已声明的固定有限条sequential bit tapes、逐bit读写/移动、完整delimited sweeps的顺序位程序模型。无随机寻址、无免费任意精度整数运算、无存储全部compositions的码本oracle。原counts可依017扫描法获得；编码与解码采用标准组合rank/unrank，须给出足以机械实现的有限过程。可用逐坐标的组合块计数及hockey-stick恒等式，unrank在公开范围内二分，二项系数以最多K次精确乘除生成。二分迭代数、乘除完整字宽和所有循环上界有限可审，不枚举R个候选或指数大小码表来冒充下面的费用。

令

    w = h+b_M+8K(r+B+8),
    P = K^3 b_M+s_pack+K w+w.

完整中间整数、完整乘积、余数与guards须有O(w)位界。待核如下保守上界，常数独立于K,M,h,r及数据：

    online bitwork, including compression/decompression
      O(NK+M K^3(b_M+B)+K^4(r+B+1)w^2),
    streaming phase-total physical peak O(P),
    compact program/parameters/layout full-format length O(P+w),
    offline generation and full writes O((P+1)(w+1)),
    offline phase-total physical peak O(P+w).        (COST)

这里compression是观察prefix后的真实在线运算，不挪到offline。给每row至多O(K(r+B+1))次组合计数查询、每次至多O(Kw^2)的乘除等明确账目；若采用更省rank算法可以，但必须支持同一保守上界。prefix完整扫描、行和、量化quotient/remainder、所有rank字段序列化、切口前擦除原counts/副本、decoder顺序扫描整份消息、prefix endpoint、两个新增triple、最终有理normalize、Q-grid输出均收费。数据相关停止时刻/地址不能成为切口侧信道；可用公开上界的固定循环和gated运算，末尾清理/控制归位，并交代padding费用。

完整one-hot取得NK及转换O(NKB)列出，允许用N<=2M吸收入扫描项。公开循环/参数/索引、layout和工作存储、输入缓冲、copied message与输出的同phase活跃项必须先相加再取peak。若输入一开始以完整batch存储，NK buffer另加使peak为O(NK+P)，其取得、擦除/断开均计费；未来两符号在其观察时刻前不可访问。物理存储与消息capacity不同：即使擦除后的空白tapes不再携带历史，也不能抹去它们在相应phase的费用。

取最小SUFF配置M_tau=max(2,ceil((128K^(5/2)/tau)^2)-1)，h=h0、r如上，S=K^5/tau^2、Lambda=1+log2K+log2(1/tau)，可作标准保守代入：w=O(K Lambda)、s_pack=O(K^3(1+log2(1/tau)))、P=O(K^3 Lambda)，online O(S K^3 Lambda+K^6 Lambda^3)，offline O(K^4 Lambda^2)，batch peak O(SK+K^3 Lambda)。所有真实费用仍以COST完整分项为准；不声称该计算工作最优，也不将新较小切口消息替代全程物理peak。

这是解析有限程序/费用证明，未运行literal ledger则明确说明；无需新增emitter/compiler或大规模枚举。packed persistence不当作免费神经hold，顺序机space不称共享batch网络width，绝不把SRC的128p word或较小神经L/W挪给本codec。

## 6. 真实依赖与证据门槛

预期实际Fact前驱为e7e6b1b84b74cbea（017切口lower与全计数有限前端）和a53804d650803060（016的48T）。MM5若只通过017的JOINT-NEC引用，不额外伪造直接依赖；如实直接用其证明则登记。组合编码、两次更新桥、截断访问数与费用需自足，标准方法不称新工具或首创。不得让018成为任何旧Fact的逆向前提。

完整承诺为PACK/CAP、BRIDGE/RISK、SUFF/CUT-MATCH及COST。先作有界反向核查，尤其截断count是否足够完成晚更新、组合码实际长度、所有历史相关状态和纯顺序实现费用。若有真实缺口，登记准确障碍及修复方向，保持OPEN，不静默改为较弱费用/容量界后宣布原合取完成。接纳需要自足完整证明与独立审查；补充检查不替代这一要求。

母问题仍包括真正causal batch neural的同预算allocation/强direct比较、一般K故障预算紧性、物理纠错/注入和新颖性范围。允许保留或重读raw history的算法不受本cut lower排除。旧root不重审；[Non-scientific operational metadata omitted.]


## proof
Original contract and explicit scope for this proof:
{"contract_id":"e6b7592e781948d00eb2a2effb80d8e3ef77e480f8d70f960286bc33faf730af","definitions":"## A. 共同源、观察、算法及风险定义\n\n对每个整数 K>=2，A={0,...,K-1}，S=A²，D=K²。一个实验固定一个时间齐次二阶表 theta∈(Delta(A))^S，允许零坐标；初始对分布 mu∈Delta(S) 任意。令\n\n    Y_j=(X_(j+1),X_(j+2)),\n    P_theta((a,b),(b,c))=theta_(a,b)(c),\n    N>=3, M=N-2, E_N=Y_M,\n    n_s(M)=sum_(j=0)^(M-1)1{Y_j=s},\n    C_s,c(M)=sum_(j=0)^(M-1)1{Y_j=s,X_(j+3)=c},\n    p_s^+=(C_s+1)/(n_s+K).\n\n每次预测完整观察 X_1^N。最后一个计数后继是 X_N；Y_M 不是额外 departure。actual query 从已观察最后两符号取得；fixed-query 任务另有明确的公开 s。X_(N+1)、theta、mu、支持、闭类、平稳律、未来行栈及隐藏源标签不可见。外部 query 是同一历史下调用的查询参数，不额外赠送干净端点或统计量。获得和复制实际端点在实现中收费。\n\n共同算法族的程序和公开精度可以依赖 K,N,h，不能依赖未知 theta,mu 或其隐藏标签。统计根中的理想 p^+ 是分析变量；给定实现的计数、头输出等实际可见代码由来源实现义务确定，不能据理想表达式新增 readout 端口。比较中的任意全历史预测器可以用全部 X_1^N 和源独立随机种子，输出任意概率向量。具体 Pi 则遵守自己已声明的内部信息切口。\n\nTV(p,q)=1/2 sum_c|p_c-q_c|。对给定 family F，令 Z_N(s)=TV(F_(K,N,h)(X_1^N;s),theta_s)。严格区分：\n\n| 名称 | 定义 | 量词 |\n|---|---|---|\n| fixed row | E Z_N(s) | 固定公开 s |\n| all contexts | E max_(s∈S) Z_N(s)；另可问其 a.s. 极限 | 全 K² 行，不改成访问行 |\n| actual terminal | R_act=E Z_N(E_N) | 同一历史的末尾 query |\n| conditional terminal | E[Z_N(E_N)\\|E_N=s] | 仅当 p_N(s)=mu P^M(s)>0；零概率时未定义 |\n| empirical weighted | E sum_s(n_s/M)Z_N(s) | 同历史频率权重 |\n| other history weighted | E sum_s w_s(X_1^N)Z_N(s) | w 为观察历史可测 simplex；不自动有一致性 |\n\n逐源极限固定 K,theta,mu 后令 N→∞。统一均值是每个 N 的 sup_(theta,mu) R_act；取 supremum 时源可随 N 改选，但一个样本路径内部的核必须齐次。固定 K 的统一结论不是 K 随 N 变化的无条件结论，也不是 changing-source 的统一几乎处处结论。输出允许零坐标，损失仅 TV，本 contract 不把它解释为 positive-output KL。\n\n\n## 共同研究范围的约定\n\n接口I是一个程序性质的定义，不能作为所有算法已经满足的全局假设。条件统计根对任意满足I的共同有限族F证明蕴含式；具体Pi满足I及其完整成本须由SRC-Pi的正常独立来源义务支持，不能在证明SRC-Pi时先假定它。原第二阶段固定证明是可查来源，旧Fact编号不是新项目前驱。\n\n后继真实资源/可靠性命题可以在同一contract内建立独立义务，不必谎称它们是统计根的前提。数据观察及TV实验保持上述定义。每项具体实现须声明自己的内部代码、允许回读、输出格式、参数/字长、batch或streaming等执行方式；比较只在所声明的共同条件下成立。原Pi的finite-attention加pointwise batch hybrid、literal bit/ReLU模块的packed/scalar、sparse/dense选项分别核算，不将一项格式的便宜坐标拼入另一项。\n\n完整费用包括实际head和局部绑定、输入/query/端点取得、参数/零系数、物理字、复制/跨层保持/清除、mask/position、所有活动bank与metadata、online/offline工作和同时峰值。不能免费引入计数、normalizer、译码或生成器。新算术/扰动参数由各精确义务局部量化；改变共同数据律、可见信息或风险须建立新的明确数学范围。\n\n给定接口的条件定理、具体实现定理、训练可达性、必要资源及新颖性是不同主张。数学根只包含数学命题。行政完成程序不是数学前提；独立后续结论不改变已有定理的证明依赖。\n","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]},"statement":"# T2-COMPRESSED-CUT：单纯形行表编码与截断访问数的晚 query 切口容量匹配候选\n\n017的完整正常接纳已核：Fact e7e6b1b84b74cbea，Evidence 28049650420d2e560f81570f2afb3a30128c98f3b474a03a4cdcc346a77567fe；其MEM/BITS与全计数基线保持原scope和依赖。本项为独立后继，拟关闭017切口容量上下界中的log K差距。不是重新提交017，也不是把packed寄存器称为神经width。旧root、SRC及014–017等接纳保持；本候选尚未证明，完成亦不宣告v10完成。\n\n## 1. 同一原实验与信息接口\n\n整数K>=2、M>=2，N=M+2；任意允许零边的齐次二阶theta和任意初始对律mu，每条实验内固定。观察X_1^N，Y_i=(X_(i+1),X_(i+2))，departure i=0,...,M-1。完整计数C_(s,c)、J=n_(Y_M)及p^+_(s,c)=(C_(s,c)+1)/(n_s+K)沿016/017定义。T=K^(5/2)/sqrt(M+1)。目标仍为同轨迹actual E[TV(output,theta_(Y_M))]，TV是L1的一半。\n\n算法类恰为017的晚query、禁止回读切口：在读完X_1^M后、读最后两个真实符号X_(M+1),X_(M+2)前，encoder只留下至多2^s值的消息I；此后decoder只获I、这两个实际符号、公开参数及源独立随机性。全部跨切口历史相关endpoint、地址、控制、停止时刻、缓存、residual和其他token状态均计入I。程序、码本、公开参数均不依隐藏theta/mu。prefix encoder计算不受限；允许017已定义的随机共同算法，以下上界给一个共同确定有限算法。切口容量不限制切口前工作峰值，也不允许把峰值漏报。末对不是新添的独立query，upper不假定它独立prefix。\n\nR_cut(K,M,s)保持017定义。另定义s_req(K,M,tau)为存在该共同切口算法且sup actual风险<=tau的最小非负整数s；若不存在，取+infinity。此定义用存在算法，不假定某个风险infimum达到。\n\n## 2. 具体有限编码及容量承诺\n\n公开编码精度为整数r>=1，令\n\n    eta=2^(-r), R=K*2^(r+4), H=2^(r+3),\n    B=ceil(log2 K), b_M=ceil(log2(M+1)),\n    L=ceil(log2 binom(R+K-1,K-1)),\n    s_pack=K^2*(L+r+4)+2B.                         (PACK)\n\nR是内部单纯形分母，可以不是2的幂；最终输出另用合法Q=2^h。h>=h0(M)=max(4,ceil(log2 M)+1)。所有参数由公开整数有限生成，不调用实数log/floor oracle；位长/二项系数可以用整数循环确定。\n\n令D_(s,c)为prefix X_1^M的M-2次departure计数，v_s=sum_c D_(s,c)，p^0_(s,c)=(D_(s,c)+1)/(v_s+K)。encoder用017已收费全计数前端获得它们。对每行s，以前K-1坐标向下取整和末坐标补残差定义\n\n    t_(s,c)=floor(R*p^0_(s,c)), c<K-1,\n    t_(s,K-1)=R-sum_(c<K-1)t_(s,c), q_s=t_s/R,\n    a_s=min(v_s,H).\n\n每个t_s是K个非负整数和为R的weak composition。固定公开字典序，以其在全部binom(R+K-1,K-1)个compositions中的rank存为L bits。a_s在0,...,H中，用r+4 bits，包括a_s=H。按全部K^2行的固定顺序写出这些rank/count字段，再附prefix最后两个真实符号的2B bits。将原counts、q坐标临时数组、余数、搬运副本等全部擦除，控制/地址/读头重置到公开位置后才开放最后两个符号。不存在免费prefix endpoint或隐藏rank码表。\n\n待证：该编码全路径合法，所有历史相关信息值数<=2^(s_pack)，并有\n\n    L <= (K-1)(r+7), s_pack <= K^3(r+7).            (CAP)\n\n须给stars-and-bars双射、rank/unrank有限算法及容量估计。可用binom(n,k)<=(en/k)^k、e<3和K/(K-1)<=2，给逐步有限常数比较。不能逐坐标固定宽存K个数后忽略其额外log K，也不能把存在码本当免费编码器。未使用的rank/endpoint二进制格式可约定输出固定合法概率向量；所有真实历史所产生的消息必须按原算法正确解码。\n\n## 3. 最后两个真实符号的全路径修正\n\nprefix最后两符号为(u,v)，新符号为(A,B')，实际query s_*=(A,B')。两个新triple恰为(u,v,A)、(v,A,B')。由这四个符号计算对每个row s的新增标签计数z_s及k_s=sum_c z_(s,c)<=2；只需取s_*对应部分。decoder通过消息的付费顺序扫描取得q=q_(s_*)和a=a_(s_*)。\n\n在a<H分支，v_(s_*)=a精确已知，构造\n\n    q' = ((a+K)*q+z_(s_*))/(a+K+k_(s_*)).\n\n在a=H分支，取q'=q，忽略至多两次新departure。注意a=H包括v=H，不允许误作精确v。待证明每条完整历史上q'是概率向量且\n\n    TV(q',p^+_(s_*)) <= (K-1)/R+2/H <= 5eta/16. (BRIDGE)\n\n证明须保留M=2的空prefix计数、v=0、k=0/1/2、两次departure相同row、a=H边界、任意零概率历史。small-count分支用同权重凸组合控制量化误差；large-count分支须严格比较完整add-one与prefix add-one，不能直接把q当经验分布或删除真实数据后改变统计实验。upper为逐路径陈述，不使用随机末行条件iid或独立性。\n\n最后按ordered floor/residual将q'转为分母Q=2^h的概率向量F_(K,M,h,r)，完整有理分子分母通过有限整数乘除求出。证明\n\n    TV(F,p^+_(Y_M)) <= 5eta/16+(K-1)/Q,\n    sup E TV(F,theta_(Y_M))\n      <= min(1,48T+5eta/16+(K-1)/Q)\n      <= min(1,49T+5eta/16).                       (RISK)\n\n48T只引用016 Fact a53804d650803060已接纳的同actual上界；(K-1)/Q<=T须给全有限参数推导。F是新程序，不声称与原Pi或017全计数程序的逐位输出/真实风险相同。\n\n## 4. 联合样本与切口容量结论\n\n对0<tau<1取r=max(1,ceil(log2(1/tau)))、h=h0(M)。当\n\n    M+1 >= (128K^(5/2)/tau)^2                     (SUFF)\n\n时，待证RISK<=89tau/128<tau，且s_pack<=K^3(r+7)。公开tau只用于选择整数配置，算法实际只收K,M,h,r；若输入tau为正有理数，配置选择用有限整数比较实现，费用另计入公开配置生成，不用实数oracle。\n\n特别对K>=12、0<tau<2^-16及满足SUFF的任意整数M，结合017的原MEM/BITS，证明\n\n    (K^3/3072)*log2(1/tau)\n       <= s_req(K,M,tau) <= 2K^3*log2(1/tau).      (CUT-MATCH)\n\n整数容量须保留相应上整/下整含义，可优先给精确L、s_pack和d log2(1/(96tau))再作上述实数比较。下界只用017的d>=K^3/1536及log2 96<7；不重新证明或扩展其母源/随机算法scope。\n\n同范围内任何共同切口算法risk<=tau仍必要M+1>=2^-32 K^5/tau^2（017的JOINT-NEC）。因此在这个精确算法类和小tau域，有一个同时达到样本O(K^5/tau^2)、切口容量O(K^3 log(1/tau))的算法；对应两个坐标各有常数因子必要性。必要性分别量化，不把两个lower相加、不声称同一个源同时实现两个障碍，也不把不同M的source supremum改成同源forall horizons。\n\n只在本义务经正常独立网关接纳后，方称上述参数域的样本与切口容量阶匹配。数值常数、接近1的tau域、切口前在线内存以及神经资源最优均不由CUT-MATCH得到。\n\n## 5. 有限实现与完整收费承诺\n\n使用017已声明的固定有限条sequential bit tapes、逐bit读写/移动、完整delimited sweeps的顺序位程序模型。无随机寻址、无免费任意精度整数运算、无存储全部compositions的码本oracle。原counts可依017扫描法获得；编码与解码采用标准组合rank/unrank，须给出足以机械实现的有限过程。可用逐坐标的组合块计数及hockey-stick恒等式，unrank在公开范围内二分，二项系数以最多K次精确乘除生成。二分迭代数、乘除完整字宽和所有循环上界有限可审，不枚举R个候选或指数大小码表来冒充下面的费用。\n\n令\n\n    w = h+b_M+8K(r+B+8),\n    P = K^3 b_M+s_pack+K w+w.\n\n完整中间整数、完整乘积、余数与guards须有O(w)位界。待核如下保守上界，常数独立于K,M,h,r及数据：\n\n    online bitwork, including compression/decompression\n      O(NK+M K^3(b_M+B)+K^4(r+B+1)w^2),\n    streaming phase-total physical peak O(P),\n    compact program/parameters/layout full-format length O(P+w),\n    offline generation and full writes O((P+1)(w+1)),\n    offline phase-total physical peak O(P+w).        (COST)\n\n这里compression是观察prefix后的真实在线运算，不挪到offline。给每row至多O(K(r+B+1))次组合计数查询、每次至多O(Kw^2)的乘除等明确账目；若采用更省rank算法可以，但必须支持同一保守上界。prefix完整扫描、行和、量化quotient/remainder、所有rank字段序列化、切口前擦除原counts/副本、decoder顺序扫描整份消息、prefix endpoint、两个新增triple、最终有理normalize、Q-grid输出均收费。数据相关停止时刻/地址不能成为切口侧信道；可用公开上界的固定循环和gated运算，末尾清理/控制归位，并交代padding费用。\n\n完整one-hot取得NK及转换O(NKB)列出，允许用N<=2M吸收入扫描项。公开循环/参数/索引、layout和工作存储、输入缓冲、copied message与输出的同phase活跃项必须先相加再取peak。若输入一开始以完整batch存储，NK buffer另加使peak为O(NK+P)，其取得、擦除/断开均计费；未来两符号在其观察时刻前不可访问。物理存储与消息capacity不同：即使擦除后的空白tapes不再携带历史，也不能抹去它们在相应phase的费用。\n\n取最小SUFF配置M_tau=max(2,ceil((128K^(5/2)/tau)^2)-1)，h=h0、r如上，S=K^5/tau^2、Lambda=1+log2K+log2(1/tau)，可作标准保守代入：w=O(K Lambda)、s_pack=O(K^3(1+log2(1/tau)))、P=O(K^3 Lambda)，online O(S K^3 Lambda+K^6 Lambda^3)，offline O(K^4 Lambda^2)，batch peak O(SK+K^3 Lambda)。所有真实费用仍以COST完整分项为准；不声称该计算工作最优，也不将新较小切口消息替代全程物理peak。\n\n这是解析有限程序/费用证明，未运行literal ledger则明确说明；无需新增emitter/compiler或大规模枚举。packed persistence不当作免费神经hold，顺序机space不称共享batch网络width，绝不把SRC的128p word或较小神经L/W挪给本codec。\n\n## 6. 真实依赖与证据门槛\n\n预期实际Fact前驱为e7e6b1b84b74cbea（017切口lower与全计数有限前端）和a53804d650803060（016的48T）。MM5若只通过017的JOINT-NEC引用，不额外伪造直接依赖；如实直接用其证明则登记。组合编码、两次更新桥、截断访问数与费用需自足，标准方法不称新工具或首创。不得让018成为任何旧Fact的逆向前提。\n\n完整承诺为PACK/CAP、BRIDGE/RISK、SUFF/CUT-MATCH及COST。先作有界反向核查，尤其截断count是否足够完成晚更新、组合码实际长度、所有历史相关状态和纯顺序实现费用。若有真实缺口，登记准确障碍及修复方向，保持OPEN，不静默改为较弱费用/容量界后宣布原合取完成。接纳需要自足完整证明与独立审查；补充检查不替代这一要求。\n\n母问题仍包括真正causal batch neural的同预算allocation/强direct比较、一般K故障预算紧性、物理纠错/注入和新颖性范围。允许保留或重读raw history的算法不受本cut lower排除。旧root不重审；[Non-scientific operational metadata omitted.]\n"}

Admitted prerequisite interfaces (use only within the recorded scopes):
[{"exact_statement":"# T2-LATE-QUERY-MEMORY：实际末对揭示前不可回读切口的联合样本与信息存储候选\n\n016已正常接纳Fact a53804d650803060，联合K,M统计率的sqrt(logK)差距关闭。本项转向T2的一个明确必要环节：在实际末对出现之前压缩全部旧观察，随后只许读这份状态及最后两符号，统一actual预测需要多少历史相关状态。不是重投016或重新包装010的packed扫描；既有root、SRC、各RATE/MM5、014/015/016原接纳及依赖保持。本项尚未接纳，完成也不宣告同神经预算或v10完成。\n\n## 1. 原统计实验与准确的新算法子类\n\nK>=2、M>=2整数，N=M+2。theta为任意含零边的齐次二阶表，mu为任意初始对律，每条实验内部固定。观察完整X_1^N，Y_i=(X_(i+1),X_(i+2))、0<=i<=M，departures只计i=0,...,M-1。风险仍是E TV(output,theta_(Y_M))，TV为L1的一半，sup可逐K,M及算法选源。\n\n唯一新增限制是明确的因果信息切口。在观察X_1^M后、观察X_(M+1),X_(M+2)前，编码器把全部历史相关信息存为消息I，取值空间大小至多2^s，s>=0为整数。之后旧历史不可回读，decoder只获I、最后两个真实符号X_(M+1),X_(M+2)、公开K,M及源独立随机性，并返回任意概率向量。末对正好为这两个新符号；不是外加的独立测试query。允许编码器与decoder拥有共享随机种子U，其与源及数据独立；各自私人随机性也源独立，不给decoder私有编码随机性之外的隐蔽通道。算法对所有源共同，参数、程序和码本不依隐藏theta/mu。\n\n所有穿过切口的历史相关register、地址、控制、停止时刻、prefix endpoint、residual、snapshot及缓存都须包含于I的2^s容量。不存在额外免费prefix endpoint；公开时间M、固定布局或源独立随机种子不携带历史信息。实际物理成本中这些公开对象仍须收费。decoder的计算不受限；证明不可把一种读出公式当成所有decoder。切口前encoder甚至可读完整prefix并任意计算，这是给其更强能力。读出可依预算s选择。\n\n记R_cut(K,M,s)为本共同随机算法子类的inf，对原母源类(theta,mu)的sup actual E[TV]。无此切口限制的R_min保持016定义。仅讨论统一均值风险，不扩成fixed/all/conditional或统一a.s.。\n\n## 2. 待证信息容量下界及联合必要性\n\n对K>=12令m=floor(K/4)>=3、b=floor(m/2)、d=m^2 b。待证全有限参数结论：\n\n    R_cut(K,M,s) >= (1/96) 2^(-s/d),\n                 K>=12, M>=2, s>=0整数。          (MEM)\n\n常数96可争取更好，但不能未经新准确声明把较弱界冒作本结论。对任意正风险目标tau<1/96，统一风险<=tau必须\n\n    s >= d log2(1/(96tau)),\n    d>=K^3/1536.                                  (BITS)\n\ns为整数时取右端的上整。该下界只指全部历史相关状态通过当前切口的容量。若某接口另保留D个值的历史相关侧信息，需将容量替换为2^s D；不能只报告query-token宽度而漏掉其他token或RAM。\n\n由于本类为共同完整历史预测器的子类，同时由已接纳MM5原scope有\n\n    R_cut >= max{2^-16 min(1,K^(5/2)/sqrt(M+1)),\n                 (1/96)2^(-s/d)}.                 (JOINT-NEC)\n\n两项取max，不相加，也不声称同一见证同时达到它们。0<tau<2^-16时仍必要M+1>=2^-32 K^5/tau^2。统计样本必要性与当前受限存储必要性是不同坐标，均不推出depth/width/bitwork的普遍下界。\n\n## 3. 可核查源族与prefix切口（候选，须自足证明）\n\n以MM5的四组合法clock源为构造来源，不能把改参数后的声明当成该旧Fact已证明。K>=12取互不相交C,U,V,W各m个字母，C含0，L=m^2。C上的循环字使p_t=(c_t,c_(t+1))枚举C^2，旋转令c_5=0。需给有限存在性或准确引用已接纳构造的适用部分。\n\n每个(u,v)及j=1,...,b赋连续参数z_(u,v,j)∈[-1/2,1/2]，全部d参数独立可选。设置\n\n    theta_(u,v)(w_(2j-1))=(1+z_(u,v,j))/m,\n    theta_(u,v)(w_(2j))  =(1-z_(u,v,j))/m.\n\n奇数m剩余W字母概率1/m；其余行沿原五步拼接p0 -> (c1,A) -> (A,B) -> (B,Z) -> (Z,0) -> p5，然后clock返回p0；A,B各均匀，Z按该UV行。赋值为theta_p0=Unif(U)、theta_(c1,u)=Unif(V)、theta_(v,w)=delta0、theta_(w,0)=delta_c6、theta_p_t=delta_c_(t+2) (5<=t<L)，未指定行delta0。检查shift、无冲突、归一化及剩余字母。\n\nM=nL+r、0<=r<L，k=(2-r) mod L，初始化不依z：k=0用p0；k=1用(c1,Unif(U))；k=2用Unif(U)×Unif(V)；k=3用固定(v*,w*)；k=4用固定(w*,0)；其他k用p_k。\n\n关键新检查是全部M>=2下，切口所在Y_(M-2)确定为p0，且其后两个符号A=X_(M+1)、B=X_(M+2)是独立均匀UV对，与整个prefix及编码消息I（条件于源独立种子）独立。不能用错误的“末对条件后一般源仍iid”。对于M小、n=0、k=1/2初始随机字母及k=3/4固定prefix，须逐项解释相位；原完整prefix的其他标签、边界信息全部允许encoder读取，证明不删掉它们。lower不要求有限样本无法估计z：即使encoder知道z并择最佳消息，容量障碍仍应成立。\n\n## 4. 编码体积候选证明（需包括随机性与量词）\n\n对每个固定共享随机种子u及消息i，decoder在各UV query上的输出随机性可先取平均。以每对W标签的坐标差定义\n\n    zhat_(i,u;v1,v2,j)\n       =clip_[-1/2,1/2]{ (m/2)(q_(2j-1)-q_(2j)) }.\n\n这得到至多2^s个d维中心。请严格证明：actual末对均匀且独立prefix，使对每个z的风险至少\n\n    (1/m^3) E_U min_(i<=2^s)||z-zhat_(i,U)||_1.\n\n不能在见到随机末对后允许encoder另选消息；若允许那样做，d维同时中心论证会失效。随机decoder通过Jensen及clip不增距离处理；源相关消息概率不妨由oracle最小值下界。共享种子固定后逐个有限码本做积分，最后再交换非负积分得到一个固定源z的下界，不能逐条样本更换源。\n\n在单位体积cube[-1/2,1/2]^d上，对C0<=2^s个任意中心，L1球体积<=2^d r^d/d!。候选取r=(d/8)2^(-s/d)，利用d!>=(d/e)^d及e<3，使球并体积<=(3/4)^d<=3/4。于是平均最近中心L1距离>=r/4=(d/32)2^(-s/d)。再用b/m>=1/3得MEM的1/96。请给体积、阶乘估计、边界clip、任意随机码本及有界积分交换的完整短证明，不以有限枚举替代。\n\n这些是标准编码/体积方法，不称新工具或首创。若相位或信息口有真实矛盾，则登记准确障碍并保持OPEN；辅助估计失败不是目标反例。\n\n## 5. 可达方向：原始计数的有限因果存储基线\n\n为不把lower误当任意精确预算最优，同时给本切口模型中的明确强计数基线。对全部K>=2、M>=2及合法h>=h0(M)，Q=2^h，令\n\n    b_M=ceil(log2(M+1)), B_K=ceil(log2 K),\n    s_count=K^3 b_M+2 B_K.\n\n候选算法逐符号取得同一one-hot历史，转换/保留最后两个符号，维护全部K^3个triple整数counts。在X_1^M切口处只保留prefix的M-2次departure计数及最后两个符号，其他历史清除；计数各为b_M bits。再读最后两个真实符号，补足恰好M次departure，选择实际末对对应的K个counts并输出原ordered dyadic add-one：前K-1坐标floor(Q(C+1)/(J+K))/Q，最后补残差。求和/完整除法、余数、控制、copy/clear和输出均实际收费，不能免费给出counts。\n\n证明其切口历史容量<=2^(s_count)，输出全路径合法且距p+的TV<=(K-1)/Q。由016已接纳上界，风险<=min(1,48T+(K-1)/Q)<=min(1,49T)<=min(1,64T)。这里T=K^(5/2)/sqrt(M+1)，不同程序仅共享风险证书，不声称真实风险或输出bits相同。\n\n提供一个明确有限顺序位程序实现作为存在性及完整收费基线，无免费大整数oracle或随机寻址。可用逐departure顺序扫描全部K^3计数块的保守实现，每块比较公开triple索引并执行完整gated increment。设w=h+b_M+B_K+O(1)，核实或给更准确的：online active bitwork O(NK+MK^3(b_M+B_K)+K w^2)，同时存活物理bits O(K^3 b_M+K w+w)，有限控制/公开索引/布局、取得one-hot/转换、状态移动/copy/clear、输出及offline生成写出均列账。不得将packed persistence当成免费neural holds。\n\n若输入约定要求一开始完整batch历史已同时存储，则那份NK buffer须单列峰值并在切口前擦除/断开；不能抹去其存在。该streaming/顺序位程序不是原SRC共享逐token网络的实现，不把其寄存器数冒称neural width；不得据此宣称同一neural cap的优势。无需新增compiler或大规模枚举，解析构造及证明足够；literal ledger未运行则如实说明。\n\n取M+1>=(64K^(5/2)/tau)^2、h=h0给一个同目标样本/切口状态充分配置：样本O(K^5/tau^2)，s_count=O(K^3[1+logK+log(1/tau)])。与BITS比较保留logK及常数差距，不自动宣称全参数存储最优。任何进一步匹配的参数子域须明确单列。已存在010扫描可在末对已知后重读历史而只保留一行counts；它不满足本切口禁止回读约束，应明确保留为另一强基线，不能用MEM排除它。\n\n## 6. 真实依赖、结论边界与正常网关\n\n预期实际前驱为MM5 Fact946d42d5bf502eb4（JOINT-NEC及准确沿用的clock事实）与016 Facta53804d650803060（计数基线风险）。MEM新增连续参数族、prefix相位与体积论证必须自足；若另用旧Fact则如实登记。旧文件R-CAP或FILE-SCOPED PASS仅作来源，不自动接纳。\n\n完整承诺为MEM、BITS、JOINT-NEC及明确计数可达基线/费用界。自足完整证明需要独立审查。Counter做一次有界互补攻击，[Private task allocation omitted from the public export.]若具体候选有缺口或费用式不成立，给精确原因及修复方向，保持OPEN，不静默修改定义或较弱替代后宣称原合取完成。\n\n这个结果若成立，是同actual母实验内一个明确无回读、晚query子类的信息存储边界。它不覆盖保留raw history的模型，不给单个query-token宽度下界，不排除全历史strong direct，不证明原Pi同预算优势或内部资源最优。真正causal batch neural的完整预算allocation、一般K故障预算紧性、物理纠错实现及主文新颖性范围继续保留。[Non-scientific operational metadata omitted.]\n","fact_id":"e7e6b1b84b74cbea","scope_bindings":[{"evidence_id":"28049650420d2e560f81570f2afb3a30128c98f3b474a03a4cdcc346a77567fe","obligation_id":"f228ec91da7ce41d27fc032fc7fe47f8c87d318b97e55f3d765824fd20d115f8","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]}}],"source_hash":"5c530be9cd4b9bd233649db3d6104f2698be86cfbb0735aa720a656c42dd432b"},{"exact_statement":"# RATE-L1-MAX：去除剩余 sqrt(log K) 的共同 actual TV 率候选及同风险配置\n\n本项是015完整接收后的独立科学后继。014、015及旧root的准确声明、接纳和依赖保持；本候选不是由它们的接纳自动得到，也不是任何旧结果的逆向前提。直接对前缀L1范数作有界差分是本次待核查的改动，不以相邻高矩参数优化替代。完成本项亦不宣告v10的资源与机制母题完成。\n\n## 1. 原完整实验与准确目标\n\n全部整数K>=2、M>=1，N=M+2，字母表{0,...,K-1}。theta为任意允许零边的齐次二阶转移表，mu为任意初始对律。每次实验内theta固定；sup可随K,M选源。观察完整X_1^(M+2)，Y_i=(X_(i+1),X_(i+2))，0<=i<=M。\n\n    C_s,a=sum_(i=0)^(M-1)1{Y_i=s,X_(i+3)=a},\n    n_s=sum_a C_s,a, J=n_(Y_M), p_s,a^+=(C_s,a+1)/(n_s+K),\n    T(K,M)=K^(5/2)/sqrt(M+1),\n    R_K^+(M)=sup_(theta,mu) E TV(p^+_(Y_M),theta_(Y_M)).\n\n待证结论：\n\n    R_K^+(M)<=min{1,48 T(K,M)}.                       (L1+)\n\n仍为同完整轨迹actual E[TV]，不是TV平方、fixed/all/conditional、独立测试查询或删尾平均。算法只获历史及公开参数，不获辅助行栈、隐藏theta/mu、访问参数或未来符号。所有退化行、周期/可约/暂态、J=0、小M及任意初始化均需覆盖。\n\n## 2. 直接L1最大集中的具体候选（全部需证明）\n\n有限辅助耦合为每个K²行提供2M个独立theta_s符号并顺序复现原M次departure。令S_s,j=sum_(l<=j)(e_(xi_s,l)-theta_s)。对确定整数1<=v<=M定义\n\n    F_s,v=max_(0<=j<=2v)||S_s,j||_1,\n    Z_v=max_s F_s,v.\n\n只对确定行/确定前缀使用iid。目标链：\n\n    E F_s,v <= sqrt(8Kv),\n    改变一个栈符号使F_s,v至多改变2,\n    P(F_s,v-E F_s,v>t)<=exp(-t²/(4v)), t>=0,\n    ||Z_v||_4 <= sqrt(8Kv)+sqrt(8v ln K)+32^(1/4)sqrt(v)\n              <= (25/4)sqrt(Kv).                    (L1MAX)\n\n均值可用L1/L2比较及有限Doob L2；集中直接作用于整个L1前缀最大值，其坐标敏感度2与K无关。请给有界差分的条件区间推导及尾积分。K²行union后以a=sqrt(8v lnK)平移，剩余正部四次矩应<=32v²；行最大值之间不要求独立。不得将sqrt(K)再次乘在全部集中误差上。\n\n最后常数可用lnK/K<=1/e<3/8、K>=2，从而系数至多sqrt(8)+sqrt(3)+2^(3/4)<25/4；所有常数比较须明确可审。该吸收利用的是sqrt(K)均值和sqrt(logK)偏差的相加，不声称偏差本身没有logK。\n\n在E_v={v<=J<2v}上逐路径TV(phat_(Y_M),theta_(Y_M))<=Z_v/(2v)。然后仅用无条件Holder及G/U整数UC：\n\n    c=K^4/(M+1), P(J<w)<=min(1,cw), 整数w>=1,\n    E[TV(phat,theta)1_Ev]\n       <=(25/8)sqrt(K) v^(-1/2) min(1,2cv)^(3/4).\n\n重述有限分层和数值几何和\n\n    sum_(l>=0)2^(-l/2)min(1,a 2^l)^(3/4)<=10sqrt(a), a>0.\n\n于是经验项候选<= (125sqrt(2)/4)T；零计数项<=T、平滑项<=2T，总系数<48。无限延拓只用于数值和，不为随机栈增加免费信息。phat不在J=0定义。\n\n平滑及下述实现误差保持截断：对每个实数A>=0，\n\n    E min{1,A/(J+K)}<=Psi(cA)<=2sqrt(cA),             (TRUNC)\n    Psi(0)=0; Psi(x)=x(1+ln(1/x)) (0<x<1); Psi(x)=1 (x>=1).\n\n需保留A=0及实阈值x=A/t-K，x>0时{J<x}={J<ceil(x)}且ceil(x)<=A/t，x<=0为空事件，不直接向非整数阈值套整数UC。A=K用于平滑。\n\n## 3. 全合法精度与原Pi\n\n对输出为概率向量且全路径全query满足原接口I的共同有限F：\n\n    h>=h0(M)=max(4,ceil(log2M)+1), Q=2^h,\n    TV(F_h(x;s),p_s^+(x))<=78KM/[Q(n_s(x)+K)]+(K-1)/Q,\n    A_h=78KM/Q, g_h=(K-1)/Q,\n\n证明\n\n    sup E TV(F_h(Y_M),p^+_(Y_M))<=min(1,g_h+Psi(cA_h)),\n    sup E TV(F_h(Y_M),theta_(Y_M))\n      <=min(1,48T+g_h+Psi(cA_h))<=min(1,64T).        (L1-I)\n\n由SRC Fact fef8372728290b45，这适用于同一个实际Pi，直接包括最低合法h0。不得由高精度结果自动推到h0，也不声称各h输出或真实风险相同。以原h_N=ceil(log2(128(K+1)(M+3)^3))、e_N=(M+3)^(-2)，另有原Pi风险<=min(1,48T+e_N)。全部须给有限参数推导。\n\n## 4. 已接纳MM5的同目标比较\n\n令R_min(K,M)=inf_A sup_(theta,mu)E TV(A(X_1^(M+2)),theta_(Y_M))，A为所有共同随机全历史概率预测器，种子与源独立，不读隐藏参数或未来。仅使用MM5 Fact946d42d5bf502eb4已接纳范围得到下界，并结合本项新上界，目标合取为\n\n    2^-16 min(1,T)<=R_min(K,M)<=R_K^+(M)<=min(1,48T). (MATCH)\n\n只有本项正常接纳后才能称K,M联合统计率在绝对常数因子内匹配，或原add-one达到该minimax阶。不能称数值常数最优、存在同一源对所有算法/所有horizon同时困难、内部资源下界或所有Transformer资源最优。旧MM5构造不重证，保留其唯一原前驱a125供小K。\n\n0<tau<2^-16时任何共同全历史算法的统一风险<=tau，必要样本为M+1>=2^-32 K^5/tau²。原Pi无故障取M+1>=(64K^(5/2)/tau)²、h=h0即为充分配置。必要与充分为不同量词方向，不能相加或当作同一见证。\n\n## 5. 联合故障与完整费用的标准后续推论\n\n在SRC原master/V切口，使用015相同的准确故障实验：master为9K+1个canonical G_h字，最终银行W在{1,...,2Q}^K；D为相对当前post-master银行V^delta的总绝对整数编辑预算。核只读已观察历史/当前银行/公开量和独立种子，不读隐藏源或未来。好事件G可与历史/J及编辑相关，P(G^c)<=gamma；G上master逐坐标误差<=delta、||W-V^delta||_1<=D；G外仍合法canonical/正银行。令\n\n    A=M[K(78/Q+36delta)+D/Q].\n\n重述短的正向量归一化与无条件截断推导，证明原Pi\n\n    R_fault<=min(1,48T+g_h+Psi(cA)+gamma)\n           <=min(1,62T+12K^(5/2)sqrt(delta)+2K²sqrt(D/Q)+gamma).\n\n因此对0<tau<1，M+1>=(248K^(5/2)/tau)²、h=h0、delta<=tau²/(2304K^5)、整数D<=floor(Q tau²/(64K^4))、gamma<=tau/4为充分配置。J0、M1、零预算和只能零编辑的网格均保留。这是新统计率代入既有接口的标准综合，不另造常数节点，不扩展015二元切口下界。\n\n取M_tau=max(1,ceil((aK^(5/2)/tau)²)-1)，a=64或248，N=M_tau+2、n=N+1、ell=ceil(log2(N+K+2))、p=4h0+4ell+64。明确S_tau=K^5/tau²、Lambda_tau=1+lnK+ln(1/tau)，n=O(S_tau)、p=O(Lambda_tau)。同一个uncached/dense SRC配置保留depth O(Kp²)、width O(Kp)、word<=128p、dense参数bits O(K³p^5)、全部n个token点运算/QKV O(nK³p^6)、attention O(n²(K+p)p²)，以及完整input/query/endpoint、metadata/masks、holds/copy/clear、输出、offline generation/全格式写出和逐phase总peak。rolling内存不替代总peak；缓存、sparse、PURE须另用完整收费配置。物理注入器、历史重读或新纠错桥不免费。\n\n该标准成本代入只消去充分样本证书中的logK，不改变Pi程序或宣称同精确预算优势。strong direct及真正同神经预算比较仍需独立科学工作。\n\n## 6. 实际依赖与正常证据门槛\n\n上界预计只必需G/U a12539a93d9f1ee3的UC与SRC fef8372728290b45的实际接口/费用；MATCH实际使用MM5 946d42d5bf502eb4。有限耦合、Doob、区间矩母函数、有界差分、Holder、dyadic及截断推导均重述自足时，不新增014/015/RATE/K3前驱。它们可作写作来源；若实质依赖其引理则如实加入前驱，禁止隐藏依赖。所有旧Fact保持原scope。\n\n先做有界逆向核查，尤其L1最大函数的单符号振幅、均值与偏差相加、25/4常数和随机末行相关性。若失败则登记精确障碍，保持OPEN，不将辅助估计失败宣称为目标反例。完整证明需要独立审查；补充检查不替代接纳。所有标准方法不作新工具或首创主张。[Non-scientific operational metadata omitted.]\n","fact_id":"a53804d650803060","scope_bindings":[{"evidence_id":"fef1785395851e47b5ca0b719640449061718f4c670bfcd74c24cf0aec696c88","obligation_id":"e5eac888f467f9e19522d9755a04c518aea63e80192c0532f59b4d9dfecbde33","scope":{"assumptions":["Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.","Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.","The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.","Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project."],"definitions_hash":"2e1530f79109eb12f5f9c38a09bfc33a11cb241c811b093a8c1e9cc305f1d3dc","objects":[],"parameter_domain":"K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.","quantifiers":[]}}],"source_hash":"bc24d183f5299df636e67f0b439aadbcd4d79671b69c327ed7083ddfab857c6f"}]

Proof:
# T2-COMPRESSED-CUT — complete proof v1

Exact target: b45f091c8b480719a5dbbfbce40c954456e3d8cc329a031f596d4a8d3d6c422d.
Contract: e6b7592e781948d00eb2a2effb80d8e3ef77e480f8d70f960286bc33faf730af.
This proves the full frozen conjunction PACK/CAP, BRIDGE/RISK, SUFF/CUT-MATCH and COST. Before a normal gateway acceptance it is an author submission, not an admitted Fact.

## 1. Scope and the two admitted premises

Fix integers K>=2, M>=2, N=M+2, r>=1, and h>=h0(M)=max(4,ceil(log2 M)+1). A history is the original X_1,...,X_N of an arbitrary fixed-in-experiment homogeneous second-order source, allowing zero edges and any initial pair law. Y_i=(X_(i+1),X_(i+2)), and the observed departures are precisely i=0,...,M-1. Let C_(s,c), n_s, J=n_(Y_M), and p^+ be the frozen complete-history counts and add-one vectors. Put T=K^(5/2)/sqrt(M+1). TV is half L1.

We retain the exact 017 causal cut: all history-dependent information remaining after X_1^M and before the last two symbols is encoded in the finite message. The decoder has only that message, the last two actual symbols, and public parameters/source-independent randomness. Our upper algorithm is deterministic and common to all sources. No step of its upper proof requires independence of the actual query and the prefix.

The actual project predecessors are exactly:

- e7e6b1b84b74cbea (017): the original cut MEM/BITS and JOINT-NEC scopes, and its finite all-count sequential-bit front end. In particular for K>=12, d=floor(K/4)^2 floor(floor(K/4)/2), its capacity necessity is s>=d log2(1/(96tau)) for tau<1/96, with d>=K^3/1536. Its separate sample necessity is M+1>=2^-32 K^5/tau^2 when tau<2^-16.
- a53804d650803060 (016): for this complete-history actual risk, R_K^+(M)<=min(1,48T).

Their native evidence and unchanged file hashes are in source-checks-v1.json. We use 017's already admitted scope, not a fresh extension of its clock or a reproof of its lower bounds. MM5 is used only through 017's JOINT-NEC, so no separate direct MM5 premise is introduced. The combinatorial codec, update bridge, and its new implementation costs are proved below. Neither SRC neural costs nor any file-scoped review is an additional premise.

Define the public integers and one auxiliary real notation

    eta=2^(-r), R=K 2^(r+4), H=2^(r+3),
    B=ceil(log2 K), b=ceil(log2(M+1)),
    C_tot=binom(R+K-1,K-1),
    L=ceil(log2 C_tot),
    s_pack=K^2(L+r+4)+2B,
    Q=2^h.

The real notation eta is not an arithmetic oracle. The implemented parameters, quotients, ranks, and output are computed by finite integer algorithms.

## 2. Row quantization is a finite simplex composition

Let D_(s,c) be the prefix's counts for departures i=0,...,M-3, with an empty range when M=2. There are M-2 departures. Set v_s=sum_c D_(s,c) and

    p^0_(s,c)=(D_(s,c)+1)/(v_s+K).

Every denominator is strictly positive, including a zero-visit row. The 017 front end supplies these exact counters and the two prefix endpoint labels; its charges are retained in Section 10.

For c=0,...,K-2 compute the exact integer quotients

    t_(s,c)=floor(R(D_(s,c)+1)/(v_s+K)),
    t_(s,K-1)=R-sum_(c=0)^(K-2)t_(s,c),
    q_s=t_s/R,
    a_s=min(v_s,H).                                 (1)

The first K-1 integers are nonnegative and their sum is at most R times the corresponding sum of probabilities, hence at most R. Therefore the residual is nonnegative and all K coordinates sum to R. In particular t_s is a weak composition of R into K parts. No special support or positive observed count is needed.

If epsilon_c=p^0_(s,c)-t_(s,c)/R for c<K-1, then 0<=epsilon_c<1/R, and the last coordinate's error has the opposite sign and magnitude sum epsilon_c. Thus, on every prefix,

    TV(q_s,p^0_s)=sum_(c<K-1)epsilon_c <=(K-1)/R.   (2)

The same calculation will be used later at the final Q denominator. The last coordinate can equal the entire denominator, so that integer representation always includes its leading bit.

## 3. Composition counting, exact rank length, and the total capacity

Represent a weak composition (t_0,...,t_(K-1)) by a string of R identical stars and K-1 bars: write t_0 stars, a bar, t_1 stars, a bar, and so on. Zero components produce consecutive or endpoint bars. Removing the bars and recording star-run lengths is the inverse map. Choosing the K-1 bar locations among R+K-1 positions proves that the number of compositions is exactly C_tot.

We use zero-based ascending lexicographic rank among these compositions; ranks are 0,...,C_tot-1. L bits suffice because 2^L>=C_tot. The construction of rank and its inverse without a stored table is in Section 4.

Here is the finite numerical bound needed for CAP. For positive integer k, monotonicity of ln x gives

    ln(k!)=sum_(j=1)^k ln j
       >= integral_1^k ln x dx
       = k ln k-k+1 >= k ln k-k,

so k!>=(k/e)^k. Also e<3, since sum_(j>=2)1/j!<sum_(j>=2)2^(-(j-1))=1. Therefore for n>=k>=1,

    binom(n,k) <= n^k/k! <= (en/k)^k.

For n=R+K-1 and k=K-1,

    n/k = (K/(K-1))2^(r+4)+1 <= 2^(r+5)+1,
    e n/k < 3(2^(r+5)+1) < 2^(r+7).               (3)

The last strict inequality holds because 3<2^(r+5), already for r>=1. Consequently C_tot<2^((K-1)(r+7)). Since the exponent is an integer, taking the ceiling of log2 proves

    L <= (K-1)(r+7).                                (4)

This argument pays only the logarithm of the composition set, not K separately padded coordinate widths.

The value a_s is an integer from 0 through H inclusive. Since H=2^(r+3), r+4 bits store it, including its endpoint value H. Write the rank and a_s for every one of the K^2 rows in a fixed public order, followed by the prefix's two B-bit labels. This gives exactly s_pack bits. Since 2^(K-1)>=K for K>=2 (by induction), B<=K-1. In particular 2B<=3K^2. Using (4),

    s_pack
       <= K^2[(K-1)(r+7)+r+4]+2B
       = K^3(r+7)-3K^2+2B
       <= K^3(r+7).                                (5)

Once all other history-dependent tapes have been cleared and all head/control states returned to public positions, there are at most 2^s_pack possible surviving history-dependent configurations. This includes the endpoint labels; they are not a free side channel. Public delimiters, fixed layout, constant parameters, and cleared cells have the same values on every history, though their physical allocation is charged later.

Unused binary ranks, a-fields larger than H, or endpoint labels outside the alphabet can be detected by bounded scans. Specify the decoder to output the point mass at symbol 0 on any such message. Every message actually generated by (1) is valid and uses the nonfallback decoder. Thus the program can be total on the entire binary message alphabet without changing the asserted behavior on actual histories.

## 4. Explicit finite lexicographic rank and unrank

For S>=0 and l>=1 let

    C(S,l)=binom(S+l-1,l-1).

This counts the compositions of remaining sum S into l parts. For l>=2 and a prospective next coordinate x in {0,...,S}, the block of compositions beginning with x has size C(S-x,l-1). Define the cumulative number before x, also including a sentinel x=S+1, by

    G(S,l,x)
      =sum_(y=0)^(x-1) C(S-y,l-1)
      =binom(S+l-1,l-1)-binom(S-x+l-1,l-1),
            0<=x<=S+1.                            (6)

Our convention is binom(n,k)=0 for 0<=n<k. At x=S+1 the second term is binom(l-2,l-1)=0, so G(S,l,S+1)=C(S,l). At x=0 it is zero. The identity follows by telescoping Pascal's identity: choosing a k-element subset according to whether it contains its last available position gives binom(n,k)-binom(n-1,k)=binom(n-1,k-1). Sum that identity over the consecutive n in (6). In particular

    G(S,l,x+1)-G(S,l,x)=C(S-x,l-1)>0
                    for 0<=x<=S.                 (7)

Ranking a given composition starts with S=R,l=K,rank=0. For each of its first K-1 coordinates x, add G(S,l,x) to rank, set S:=S-x and l:=l-1, and continue. The remaining coordinate equals S and adds nothing. Lexicographic blocks and (7) show by induction that this is a bijection onto 0,...,C_tot-1: rank is the number of earlier first-coordinate blocks plus the rank of the remaining suffix in its own block.

To unrank, start with a valid residual rank j in [0,C(S,l)-1], initially S=R,l=K. For l>=2 find the unique x satisfying

    G(S,l,x)<=j<G(S,l,x+1).                         (8)

Then output x and replace j by j-G(S,l,x), S by S-x, l by l-1. By (7) the new j lies in [0,C(S-x,l-1)-1]. At l=1 the unique final coordinate is S and the residual rank is zero. This proves correctness of the inverse even when S=0 or many coordinates vanish.

Finding x does not enumerate S+1 candidates. Binary search maintains lo=0, hi=S+1 with G(lo)<=j<G(hi). When hi-lo>1, use mid=floor((lo+hi)/2) and replace lo or hi according to the comparison with G(mid). When the gap is 1, freeze the bounds and use gated dummy iterations. Let

    t_search=B+r+6.

Since R<=2^(B+r+4), we have R+1<=2^(B+r+5); at most t_search iterations suffice to reduce every gap to 1. This public number of iterations is used at every coordinate, regardless of the residual rank. One final evaluation of G(S,l,lo) updates j. Thus each row's unrank uses O(K(r+B+1)) binomial queries, including the two terms of (6). Ranking uses only O(K) such queries, so it obeys the same conservative upper count. No procedure runs a loop of length R or stores a list of compositions.

Each binomial query binom(n,k), with 0<=k<=K-1 and n<=R+K-1, is computed from B_0=1 by

    B_j = B_(j-1)(n-j+1)/j, 1<=j<=k.               (9)

For n>=k all divisions in (9) are exact because the result is the integer number of j-element subsets, equivalently the product formula for binom(n,j). If n<k the result is zero; if k=0 it is one. Padding the routine to K iterations, with inactive factor and divisor both one and a final gated result selection for invalid n<k, makes its running time independent of the data. Divisors are never zero. Widths, arithmetic costs, and the inactive arithmetic are detailed in Sections 9–10.

Public C_tot and L are obtained by this same finite routine. L is the bit length of C_tot-1, and B is the bit length of K-1; b is the bit length of M. These are integer scans. R,H and Q are constructed by binary shifts. All operations described so far are finite integer loops, not calls to real logarithm or floor oracles.

## 5. Causal message formation and the actual two-departure correction

After reading the prefix, the count front end has processed exactly M-2 departures i=0,...,M-3 and retained its endpoints (u,v)=(X_(M-1),X_M). Compression computes (1), ranks each row, stores its a-field, and writes the two endpoint labels. Before the last two symbols are made accessible, it erases the raw prefix counts, temporary row coordinates, ranks outside the serialized message, division remainders, copied endpoints, and all other history-dependent scratch. It returns tape heads and control indices to fixed public positions using a fixed, padded schedule. Sections 10–11 account for this computation, padding, clearing, physical storage and movement.

Now let A=X_(M+1), B'=X_(M+2). The actual query is s_*=(A,B'). The two new triples, including their original indices, are

    i=M-2: (u,v,A),
    i=M-1: (v,A,B').

Hence for any row s and label c the true count increment is

    z_(s,c)=1{(u,v)=s}1{A=c}
              +1{(v,A)=s}1{B'=c},
    k_s=sum_c z_(s,c) in {0,1,2}.                  (10)

This allows both departures to have the same row and even the same label; no update is discarded by deduplicating. The decoder can compute just z_(s_*) and k_(s_*) from the two paid endpoint labels and the two new symbols. The final counts are exactly D+z, not counts of a shortened statistical experiment.

Scan the whole message in public row order, compare row indices with s_*, and copy out its rank and a-field; the endpoints at the end of the message are also read. No random-address selection is required. Unrank the selected composition to get q=t/R. Write v_*=v_(s_*), k=k_(s_*), z=z_(s_*), and p^0=p^0_(s_*).

If a<H, then a=min(v_*,H) entails v_*=a exactly. Define

    q'=((a+K)q+z)/(a+K+k).                          (11)

It is a probability vector: all coordinates are nonnegative, its numerator sum is a+K+k, and its denominator is positive. The actual complete-history add-one vector obeys

    p^+_(s_*)=((a+K)p^0+z)/(a+K+k).

Subtract these two equations. Their common z term cancels, so by (2)

    TV(q',p^+_(s_*))
      =[(a+K)/(a+K+k)] TV(q,p^0)
      <=(K-1)/R.                                  (12)

This also covers k=0 without forming an undefined z/k, and covers a=0 including the empty-count prefix M=2.

If a=H, the only used inference is v_*>=H; it includes the boundary v_*=H and does not claim to know v_* exactly. Set q'=q. If k=0, then p^+=p^0. If k>0, the exact complete add-one vector is the convex combination

    p^+=[(v_*+K)/(v_*+K+k)]p^0
                 +[k/(v_*+K+k)](z/k).

Since TV between probability vectors is at most one,

    TV(p^+,p^0)<=k/(v_*+K+k)<=2/H.                 (13)

The same final bound is zero or valid in the k=0 case. By the triangle inequality and (2), in every case

    TV(q',p^+_(s_*)) <=(K-1)/R+2/H
       <=eta/16+eta/4=5eta/16.                    (14)

This proves BRIDGE on every alphabet history, including histories that have probability zero under a selected source, all row coincidences, zero visits, and all small horizons. It uses no conditional iid or actual-query independence.

## 6. Final finite rational output and the risk certificate

The decoder can implement (11) without approximate real arithmetic. In the small-count branch put

    U_c=(a+K)t_c+R z_c,
    V=R(a+K+k),

and in the large-count branch put U_c=t_c, V=R. Then V is a positive integer, U_c>=0, sum_c U_c=V, and q'_c=U_c/V. The inactive branch may be evaluated with safe public dummy inputs, with a final gated choice, to keep fixed running-time bounds.

Compute exact integer quotients for c<K-1,

    f_c=floor(Q U_c/V), 
    f_(K-1)=Q-sum_(c<K-1) f_c,
    F_c=f_c/Q.                                     (15)

As in Section 2, this is a probability vector and

    TV(F,q')<= (K-1)/Q.                            (16)

A numerator equal to Q is stored in h+1 bits. This applies also to the invalid-message fallback, which can be emitted as Q,0,...,0 with denominator Q after the fixed schedule.

Combining (14) and (16),

    TV(F,p^+_(Y_M))<=5eta/16+(K-1)/Q               (17)

on every complete history. The admitted 016 bound and the pointwise triangle inequality give

    sup_(theta,mu) E TV(F,theta_(Y_M))
      <=min(1,48T+5eta/16+(K-1)/Q).                (18)

For all legal h, Q>=2M. Because M>=2, sqrt(M+1)<=2M. Thus

    (K-1)/Q <= K/(2M) <= K/sqrt(M+1) <= T,

so (18) is at most min(1,49T+5eta/16), exactly RISK. In particular the lowest legal h0 is covered directly. F is this new finite codec program, not an assertion of bitwise equality or equal true risk with either SRC-Pi or the 017 all-count output.

## 7. Sufficient accuracy, existence-based capacity, and the precise match domain

Let 0<tau<1 and take r=max(1,ceil(log2(1/tau))). Then eta<=tau. If M+1>=(128K^(5/2)/tau)^2, then T<=tau/128. Therefore

    sup risk(F) <=49tau/128+5tau/16
                 =89tau/128<tau.                  (19)

The actual algorithm is supplied only the integers K,M,h,r. The target tau chooses this public configuration; it is not a hidden source-dependent input. The exact message capacity is s_pack and satisfies (5).

By definition s_req is the least integer s for which an admissible algorithm with uniform risk at most tau exists, or infinity if none exists. In the regime of (19) the constructed program proves that the set of feasible integer capacities is nonempty, so its minimum exists by well-ordering. No risk infimum is assumed to be attained.

Now restrict to K>=12, tau<2^-16, and any integer M satisfying the sufficient sample condition. The cut model is exactly the one in admitted 017. Therefore every feasible algorithm obeys its BITS lower bound and, using the exhibited upper algorithm,

    ceil(d log2(1/(96tau))) <= s_req <= s_pack
                              <=K^3(r+7).          (20)

Here d=floor(K/4)^2 floor(floor(K/4)/2) and d>=K^3/1536. These are the exact integer statements. For t=log2(1/tau)>16, log2 96<7 and t-7>=t/2. Hence

    d log2(1/(96tau)) >= (K^3/3072)t.

Also r=ceil t<=t+1, so r+7<=t+8<=2t. Combining with (20) gives exactly CUT-MATCH,

    (K^3/3072)log2(1/tau)
       <=s_req(K,M,tau)<=2K^3 log2(1/tau).          (21)

If rounded to integer bounds, the left real quantity may be replaced by its ceiling and the right by its floor; the stronger exact bounds (20) remain available.

Independently, 017's JOINT-NEC states that any such algorithm with risk at most tau<2^-16 needs M+1>=2^-32 K^5/tau^2. Thus in this precise small-tau domain there is one algorithm simultaneously using O(K^5/tau^2) samples and O(K^3 log(1/tau)) cut bits, and each coordinate has a constant-factor necessary order. The two lower bounds have separate witnesses/quantifiers. They are not added or required to hold for one common hard source, and changing-horizon source suprema are not changed into a same-source assertion.

Equations (19)--(21) make no assertion of optimal numerical constants, optimal pre-cut working memory, behavior uniformly sharp up to tau=1, or neural resource optimality.

## 8. Sequential implementation model and integer width bounds

Use exactly the fixed-finite-tape sequential bit model declared and charged in 017: bounded-symbol cell operations, reads, writes and unit head movements, finite control, and delimited word sweeps. There is no random-access address oracle and no unit-cost arbitrary-precision multiplication/division. This section fixes arithmetic buffers sufficient for the actual program. The construction and ledger are analytic; no emitter, literal instruction ledger, or hardware run is claimed.

Let

    w=h+b+8K(r+B+8),
    P=K^3 b+s_pack+K w+w,
    u=r+B+5.

Then R+K-1<2^u. Every binomial query in (6) or the public C_tot computation has n<2^u, k<=K-1. Since binom(n,j)<=n^j, all accumulated binomial integers have fewer than Ku+1 bits. In the recurrence (9) the pre-division product is at most n^j for an active step j, hence also has at most Ku+1 bits. This is much smaller than w. Inactive steps use factor and divisor one, not an unchecked negative factor. Subtractions in (6) are between ordered nonnegative binomials; valid ranks, cumulative block counts and their partial sums never exceed C_tot. Residual S and bisection endpoints are at most R+1. Midpoint sums require just one extra bit.

For prefix arithmetic, all D and v are at most M-2, so v+K and D+1 have O(b+B+1) bits, and R(D+1) has O(b+r+B+1) bits. For the small-visit correction, a<H, k<=2, and U_c<=V=R(a+K+k). For either branch, a uniform denominator bound is

    V <= R(H+K+2).

Since H+K+2<=2^(r+B+5), V has O(r+B+1) bits (at most 2r+2B+10 suffices). Multiplying U_c by Q adds h bits. All these semantic intermediates are bounded by a constant multiple of w; in fact the displayed w has ample slack even for K=2,r=1. Row sums, residuals and guards add at most a constant or B-bit margin. Public parameters and loop/head descriptors have O(w) bits: log2 P=O(w) and log2 w<=O(w).

Reserve a fixed constant multiple, for example 4w bits, for each arithmetic workspace, with a constant number of such workspaces and a sequential K-word row buffer of O(Kw) bits. Complete products of w-bit operands use at most 2w bits, and transient doubled remainders and carry/borrow guards fit in these larger buffers. This explains why full products are retained; there is no truncation masquerading as an exact division. The coarse O(w) buffers do not mean that the front-end count updates are padded to width w: that inherited stage still uses b-bit counts and B-bit comparisons, as required for its own cost bound.

For completeness, finite tape routines have the following implementations. Addition/subtraction/comparison use full carry/borrow sweeps and rewinds in O(w) steps. Schoolbook multiplication processes every bit of one operand, shifts the other by the public bit position, and uses a full gated add into the full product buffer, with rewinds; O(w) iterations each costing O(w) give O(w^2). Binary long division scans the numerator bits from most significant to least significant and keeps the exact remainder. At each bit it doubles the remainder and adds that bit, compares with the positive divisor, subtracts if needed by a full gated sweep, and writes one quotient bit. The prefix invariant is processed_numerator=divisor*quotient+remainder, with 0<=remainder<divisor. This proves exact quotient and remainder and costs O(w^2). All bit positions are visited even if leading digits vanish or the remainder is zero. Bounds and loop ends use public delimiters, so resetting and moving heads does not hide a logarithmic per-bit random access.

Each binomial query is therefore at most K exact multiply/divide pairs of O(w^2) work each, plus O(Kw) checks/copies, for O(Kw^2). To avoid data-dependent query duration, run K rounds regardless of k; inactive rounds perform padded arithmetic with factor/divisor one. Compute the active flag j<=k<=n before selecting the nonnegative active factor; for inactive rounds select one by gated operations. If n<k select final result zero; k=0 retains result one. Fixed complete sweeps make both branches equal-duration. This proves the advertised query cost in the declared sequential model, including the sentinel n<k calls in (6).

## 9. Row processing, message access, and prevention of side channels

The prefix front end consumes the same one-hot sequence as in 017, converting the symbols and maintaining K^3 counters by sequential full-bank scans, with endpoints retained. It stops after X_M, so exactly M-2 departure counts are present. It has not read the last two symbols. This charged front-end computation is a part of the present program, not a free statistic.

For compression, scan the count bank in fixed row-major order. For each row copy its K b-bit counts into one K-word buffer and compute v by complete sweeps. Form K-1 numerators R(D_c+1), divide by v+K, and form the residual t_(K-1). Compare v with H to form a=min(v,H). Rank the composition by Section 4. Write the rank in exactly L bits, the a-field in exactly r+4 bits, and clear all row scratch before moving to the next row. The row-coordinate buffer is sequential; no arbitrary location is accessed in constant time. Public coordinate iterations simply advance its head and pay for all rewinds.

Only one row's expanded coordinates and a constant number of binomial/arithmetic words are needed at once. The algorithm never simultaneously materializes all K^2 expanded q-vectors. The complete packed message accumulates sequentially on its own tape. After the row loop, append the two endpoint labels. Clear the entire old count bank, row buffers, arithmetic registers, copied endpoints, flags, and temporary message copies. Return every head to a public origin and reset all control/loop states to the public cut state. Blank tapes still occupy physical memory, but they carry no additional history-dependent value at this cut.

Use fixed-width arithmetic and fixed public loops throughout this stage. Ranking uses a fixed number of coordinates and two binomial calls for every cumulative term, including zero terms. Each binomial call uses the padded K rounds of Section 8. Quotient/multiply routines use their full public word widths. If a subroutine would finish early, it performs the corresponding full-width inactive work instead. This ensures a common, public compression duration and cut time, not merely a reset of the eventual program counter. Clear/reset sweeps also have fixed lengths. The count-front-end scans retain their original fixed b/B stage widths; padding them to a different w-sized arithmetic budget is neither needed nor done.

After the cut read the two true new symbols. The decoder scans all K^2 message fields plus the endpoint tail in a fixed order. It checks every rank against C_tot and every a against H, and compares the two public row labels with s_* to select the needed rank and count by gated copying. It checks the endpoints' range as well. No early exit, retained search position or uncounted prefix endpoint is used. The selected rank/count and endpoints are now computations from the permitted message, not new pre-cut channels. The full scan ends at a public position.

Unrank the selected row using the padded binary search from Section 4. Invalid messages use safe rank-zero inputs during the fixed work and eventually select the fixed legal output. For valid messages compute the two indicators and label increments in (10), construct the integer U_c,V of Section 6, and carry out the full K-1 Q-grid divisions plus residual output. The row endpoint comparisons and the possible coincident increments are finite bit comparisons/additions. Choose branch outputs by gated selection after fixed safe work in both branches if required. Thus data-dependent thresholds, ranks, visits or control do not add timing, address, head-position or stopping-time information across the cut.

The message has only the fields counted in s_pack. A second material copy used while serializing is physically charged and cleared; it is not an extra surviving input. Nothing in the program reads hidden theta, mu, an ideal vector, an old raw-history copy, or future symbols.

## 10. Online work and simultaneous physical peak

We explicitly charge one-hot acquisition NK and conversion O(NKB). The accepted 017 front end processes the prefix with cost bounded by O(M K^3(b+B)); it uses b-bit ripple increments and full B-bit triple comparisons, with index sweeps, movement, copy/clear and public control already counted. The total number of updates here is only M-2, but the stated M bound is retained. The two late symbols require conversion and endpoint comparisons, not a new raw-history scan.

For one row the new codec uses at most O(K(r+B+1)) binomial queries, with O(Kw^2) cost per query. This covers either rank or unrank conservatively. Its other quantization, row-sum, comparison, coordinate-copy and residual operations cost O(Kw^2) plus the sequential row access. Hence one row costs at most

    O(K^2(r+B+1)w^2),

including arithmetic padding. Compressing all K^2 rows costs at most

    O(K^4(r+B+1)w^2).                              (22)

The decoder unpacks only one row, so its O(K^2(r+B+1)w^2) is absorbed by (22); no cost is omitted by pretending that every row is already decoded. The selected-row late update and Q divisions cost O(Kw^2).

Serialization, validating and scanning the message cost at most O(s_pack+K^2 w), including the field comparisons/copies. Clearing the count bank is O(K^3 b), and clearing row/output buffers and returned-head traversals cost O(Kw+w) plus already counted scans. Even allowing a full-width comparison/update of public loop counters per field or word is absorbed by (22). Initialization and copying of message storage are O(P). All these terms fit the claimed two main computation terms: K^3 b is absorbed by the M front-end bound, and s_pack+Kw+w=O(K^3(r+7)+Kw+w) is absorbed by (22).

Also N=M+2<=2M, so NKB<=2M K^3 B. Thus the combined online work, including real online compression and decompression, is

    O(NK+M K^3(b+B)+K^4(r+B+1)w^2).               (23)

The public C_tot/L calculation, if run online too, costs O(Kw^2) and is absorbed by (22). No row compression depending on observed counts has been moved to offline generation.

At any one streaming phase, add the simultaneous components before taking the maximum:

- the K^3 b-bit counter bank and its fixed delimiters;
- the s_pack-bit message under construction or being read, and any transient second copy (a constant multiple of s_pack);
- one expanded K-word row, accumulating output, and the two new symbols/endpoints, together O(Kw);
- a constant number of complete-product/remainder/guard scratch words, O(w);
- public parameters, loop labels, head descriptors, finite microprogram/control, and at most one input-vector buffer, O(w+K).

K<=K^3 b and all constant-factor duplicated banks are included in these sums. Consequently streaming phase-total physical peak is O(P), where

    P=K^3 b+s_pack+Kw+w.                            (24)

The prefix compression phase can have both the full counters and the whole new message alive; (24) deliberately includes both. Erasing a tape later reduces its history dependence, not its earlier physical peak. At the normalized cut all components outside the message are source-independent constants or blanks; physical O(P) and information s_pack are different assertions.

## 11. Offline representation, configuration, and optional batch input

The chosen compact program format is a fixed finite-state sequential microprogram, binary public K,M,h,r and derived widths, fixed tape-layout descriptors and delimiters, and initialized zero-filled workspace/message/output layouts. Word and bank operations are implemented by the delimited sweeps, bit arithmetic, loops and pointer movement specified above; no composition table, data-address table, or expanded list of ranks is stored.

Its full serialized length, including the initialized layouts, is O(P+w). A generator computes R,H,Q,B,b, C_tot and L by the exact integer routines. Computing C_tot requires O(Kw^2) work and O(w) arithmetic scratch. This is within O((P+1)(w+1)) because P>=Kw. Nested public layout loops can then pay as much as O(w) per emitted bit for their counters and still meet

    offline generation and all full-format writes O((P+1)(w+1)),
    offline phase-total physical peak O(P+w).       (25)

If the initial zero banks are allocated online instead of serialized, the O(P) initialization is still explicitly paid in (23); (25) is the conservative format also writing them. If the generated file/image and its live runtime copy coexist, both are included in the phase sum. An implementation choosing a fully unrolled instruction format must separately pay its expanded length and construction; that different format is not assigned the compact costs (25). This proof constructs the declared finite loop program, not a measured literal instruction ledger. No new compiler/emitter or ledger execution is asserted.

For rational tau=a0/b0 in (0,1), with positive integer numerator and denominator, public parameter selection also uses finite arithmetic. Find the smallest r>=1 with 2^r a0>=b0 by integer shifts/comparisons. Compute the minimum sufficient horizon without an irrational square root:

    W_tau=2^14 K^5 b0^2,
    M_tau=max(2,ceil(W_tau/a0^2)-1).

Exact multiply/divide with remainder computes the ceiling. h0 and the other bit lengths are obtained by integer length scans. If ell_tau is the total bit length of the rational input, this preliminary public configuration computation can be charged, conservatively, O((ell_tau+B+16)^2) work and O(ell_tau+B+16) simultaneous bits, including input/output of the public configuration; a shift/comparison search has at most ell_tau+1 rounds and word length O(ell_tau+B+16). These charges precede and are additional to the K,M,h,r codec cost (25). In particular a very redundant rational encoding with large input bit length is not free just because it represents a simple tau. Once configuration is selected, the actual data algorithm reads only K,M,h,r.

If the external input convention allocates the entire one-hot batch at the start, add its NK-bit buffer to every phase in which it remains live, giving peak O(NK+P). Its acquisition and erasure/disconnection cost O(NK), as charged in (23). Consumed prefix cells must be erased or disconnected before the cut; future last-two-symbol cells must be inaccessible until their observation times. The decoder may access exactly those two true symbols and the message. A batch implementation allowing access to future cells by the prefix encoder or readable old prefix cells after the cut has a different information interface and is not being certified by this construction.

The charges in (23)--(25) include active movement, arithmetic, metadata/control, copying, clearing, output, and actual compact-format generation/writes. Ordinary stationary tape persistence is not an implementation of neural layerwise holds. The tape model's space is not called a shared batch network width, and no SRC word constant or smaller neural depth/width is transferred to this codec. No physical injection, correction, raw-history reread or attention system is supplied for free.

## 12. Standard sufficient-configuration cost substitution and conclusion boundary

Choose the minimum sufficient horizon

    M_tau=max(2,ceil((128K^(5/2)/tau)^2)-1),
    h=h0(M_tau), r=max(1,ceil(log2(1/tau))),
    S=K^5/tau^2, Lambda=1+log2 K+log2(1/tau),

for 0<tau<1. The expression for M_tau agrees with the integer-rational construction when tau is rational. The ceiling and max give N=M_tau+2=O(S). Also b,h=O(Lambda), B=O(Lambda), r=O(1+log2(1/tau)), and hence

    w=O(K Lambda),
    s_pack=O(K^3(1+log2(1/tau))),
    P=O(K^3 Lambda).

Substitution into the full declared costs, without changing execution models, gives

    online O(S K^3 Lambda + K^6 Lambda^3),
    offline O(K^4 Lambda^2),
    streaming physical peak O(K^3 Lambda),
    optional batch peak O(S K+K^3 Lambda).           (26)

The public rational-input configuration charge, when relevant, remains separately as stated in Section 11. These are conservative upper costs, not assertions of optimal computational work. A small packed cut message does not replace the full counts or the pre-cut physical peak.

All PACK/CAP and BRIDGE/RISK assertions hold on every finite alphabet history for K>=2,M>=2, including an empty prefix count table, v=0, k=0/1/2, duplicated last-row updates, a=H, unused codewords with a legal fallback, arbitrary zero-probability histories, and all legal output precisions. There is no independent-query replacement, conditional iid row assertion, or hidden source-dependent algorithm. The stronger CUT-MATCH statement is restricted to K>=12, tau<2^-16 and horizons satisfying SUFF. Only after normal acceptance of this full proof can it be reported as a match of sample and cut-capacity orders in that domain.

This result does not constrain methods allowed to retain or reread raw history, and it does not prove optimal pre-cut memory, a single query-token width lower bound, any universal Transformer resource lower bound, or an advantage at the same exact neural budget. The full causal-batch neural allocation/strong-direct comparison, general-K fault sharpness, physical correction and novelty scope remain separate scientific work. Old admissions and their dependencies are unchanged; no earlier result acquires this obligation as a reverse premise. Standard composition enumeration, finite integer arithmetic and stability arguments are not claimed as new tools or priority results.
