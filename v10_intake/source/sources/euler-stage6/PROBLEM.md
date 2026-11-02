# v10一般二阶概率预测：条件、统一风险与后继资源可靠性

> Linked from the existing input-contamination workspace and its reviewed general-source files. The old project, root, failures and sessions are preserved. This project has a new mathematical scope and distinct native identities.

## Exact statement

## B. 条件接口 I 与精确根声明

给定任意共同确定有限预测器族 F，合法精度为整数

    h>=h_0(M):=max(4,ceil(log2 M)+1), Q=2^h.

假定每条有限历史 x_1^N∈A^N、每个 s∈S、每个合法 h，输出均为概率向量，并满足以下**确定性程序接口**：

    TV(F_(K,N,h)(x_1^N;s),p_s^+(x_1^N))
       <=78KM/[Q(n_s(x_1^N)+K)]+(K-1)/Q.             (I)

I 包括零计数以及与某一 theta 的支持不相容的历史；不是对数据分布增加正性、混合或可访问性的假设。该条件统计命题不声称任何满足 I 的族都具有 Pi 的成本。实际 Pi 满足 I 及其完整实现成本应由独立正常来源义务证明，见 `inputs/source-v10/outputs/005-native-general-handoff/lead/source-dependencies-v1.md`。

精确数学根命题为：**对上述每个 K 和每个满足 I 的共同有限族 F，下面 G1–G6、G7 的统计转移部分及 U1/UC/U2 全部成立。** 对渐近 G1–G6（注明有限 N 部分除外）使用同一个公开序列

    h_N=ceil(log2(128(K+1)(N+1)^3)), e_N=(N+1)^(-2).

由 I，全路径、全 query 的 F 与 p^+ 的 TV 差至多 e_N。G7 中原 Pi 的实际构造存在性和完整成本不从 I 推出，明确移交 SRC-Pi 来源义务；原 G7 未变文件仍完整保留。这是用户允许的条件统计根，不是把原 G7 的成本结论暗中删除后宣称整个实际网络已被接纳。

### G1：同一观察事件上的有限 N 风险界

对每个合法 h、0<alpha<1，写自然对数

    A_alpha=K ln2+ln(2K²M/alpha),
    g(0)=1,
    g(j)=min(1,sqrt(A_alpha/(2j))+(K-1)/(j+K)
                 +78KM/[Q(j+K)]+(K-1)/Q), j>=1.

存在观察历史可测事件，概率至少 1-alpha，在其上全部 s 同时有 Z_N(s)<=g(n_s)。所以 fixed、all、actual、任意观察历史权重的期望分别由 E g(n_s)、E max_s g(n_s)、E g(n_(E_N))、E sum_s w_s g(n_s)，各加 alpha 后与 1 取小控制。对 p_N(s)>0、整数 v>=1，

    E[Z_N(E_N)|E_N=s]
      <=min(1,g(v)+(alpha+P(E_N=s,n_s<v))/p_N(s)).     (G1-C)

行栈证明只对确定栈长度使用 iid 界，再取联合事件；不能条件于随机 n_s 或 E_N 后称样本 iid。

### G2：逐源 actual 一致性及有限访问行精确极限

对每个固定 theta,mu，有限对链 a.s. 在有限时间 tau 进入一个随机闭不可约类 C_infty。所有行同时有 Z_N(s)→ell_s a.s.，其中

    ell_s=0                                  if s∈C_infty;
    ell_s=TV((C_s(infinity)+1)/(n_s(infinity)+K),theta_s)
                                             if s∉C_infty.

第二行计数 a.s. 有限。任意固定非空 S0⊆S 的最大误差 a.s./L1 趋向 max_(s∈S0)ell_s。因此在给定 theta,mu 上，该集合一致当且仅当其所有有限访问行的最终 add-one 向量 a.s. 恰等于真实行。尤其

    max_(s∈C_infty)Z_N(s)→0 a.s./L1,
    Z_N(E_N)→0 a.s., R_act→0,
    E sum_s(n_s/M)Z_N(s)→0.

随机进入的类不等于所有可能进入类的并。实际末尾一致性不要求正性、平稳初始化、全链不可约、非周期或唯一平稳分布。

### G3：actual conditional 风险的正确范围

固定 theta,mu，若常返 s 所在闭类从 mu 可达，则存在 c_s>0、M_s，使 M>=M_s 且 p_(M+2)(s)>0 时 p_(M+2)(s)>=c_s。沿所有充分大的可条件化时刻，E[Z_N(E_N)|E_N=s]→0。证明覆盖周期类的全部正质量入口余数；不只挑单一相位。暂态 s 不在此结论内：其条件风险可以失败，也可以因有限访问 add-one 恰好正确而成功。均值趋零不能自动除以趋零条件概率。

### G4：任意初始下有限 N 访问控制

令 eta_mu(b)=P(tau>b)。若每个闭类内从任意起点，在 L 个连续状态（含起点）内命中任意指定类内 s 的概率至少 a>0，则对于 0<=b<M，

    B=floor((M-b)/L), v=floor(aB/2)>=1:
    R_act<=min(1,g(v)+alpha+eta_mu(b)+K² exp(-aB/8)).  (G4-F)

固定源的一组保守参数为 D=K²、p_* 为正边最小值、L=D、a=p_*^(D-1)，eta_mu(b)<=(1-p_*^D)^floor(b/D)。它们仅用于证明，不交给算法。不可约时取 b=0，亦得全 query maximum 同类界。

闭不可约类内 Poisson 方程 (Id-P_C)f_s=1_s-pi_s^C 可解；H_s=osc(f_s)。任意类内初始 nu、m>=1，

    E_nu n_s(m)-m pi_s^C=nu f_s-nu P_C^m f_s,
    P_nu(|n_s(m)-m pi_s^C|>H_s+x)
        <=2 exp(-2x²/(m H_s²)), H_s>0,x>0.

H_s=0 用确定性情形；去掉初始 b 段后比较整段 M pi_s 另付 b 边界与 eta_mu(b)。不假设非周期或可逆。

### G5：全 K² 一致性的结构分类

对固定 theta，满足 I 并使用 h_N 的族对**所有初始 mu**都有全 K² a.s./L1 一致性，当且仅当对链不可约。对指定 mu 不作这个必要性结论。

若有至少两个闭类，每条合法历史至少有一个闭类从未访问；该真闭类存在某行一个后继概率为零，所以对每个 N，max_s Z_N(s)>=1/K-e_N。唯一全链平稳律因而是本 add-one 近似族全行一致性的必要但非充分条件；它不是 actual 风险一致性的必要条件。若只有一个真闭类，类外非均匀行可从类内初始化使之失败；若类外全均匀，可从类外沿正概率简单路径一次访问后进入闭类，仍产生错误的有限 add-one 极限。

### G6：边界证据及精确不可能性

1. K=2、从吸收 00 开始的两个源可有相同全零历史而 11 行分别 delta_0、delta_1。任意共同随机算法的两源 fixed-11 风险之和>=1；至少一固定源的 limsup>=1/2。这不否定 actual 一致性。
2. 00=(p,1-p)，01→11，11 吸收，初始 00，0<p<1；在 E_N=00 上概率 p^M，全部已见 00 后继为 0，条件风险趋 1-p。此时 actual 均值仍趋零。合法周期 00→01→11→10→00 给非周期非必要，并保留零概率条件时刻未定义。未访问行刚好均匀的正例保留。
3. 对每个 M 取 epsilon=1/(16M)，00=(1-epsilon,epsilon)，01=10=(1/2,1/2)，11=(a,1-a)，a=1/4 或 3/4；分别以 pi∝(1,2epsilon,2epsilon,epsilon/a) 初始化。两源全零历史质量各至少 5/8，故任意共同随机算法的两源最大 fixed-11 风险至少 5/32。这是每 N 的类 supremum 下界，源随 N 变化；该同族 F 的 actual 风险却至多 59/(16M)+e_N。
4. 所有其他已审暂态成功/失败、多入口周期、随机闭类反例按原 Counter 的完整表保留，不能合并不同示例的行。K 随 N 增长的例子仅为 K 无关速率的边界证据。

### G7 的统计转移与实现义务的边界

改变合法历史的概率律不改变给定历史对应的程序输出或费用。只要另行正常证明具体 Pi 全路径满足 I，上述 G 及以下 U 可直接实例化到同一个 Pi。直接 add-one 的统计证明也成立；它的有限前端和输出运算另行收费。**实际 Pi 存在、SRC-Pi 完整成本、与强 direct 基线的成本比较，均不是 I 单独的逻辑后果，不属于本条件根已经完成的内容。**

### U1/UC：统一实际末尾占用与可计算模

对整数 v>=1、m>=0，定义

    B_(m,v)(P)=max_y P_y(n_(Y_m)(m)<v),
    beta_(K,v)(m)=sup_theta B_(m,v)(P_theta).

B 随 m 非增；个别初始态的概率未必非增。确定路径的 first-v charging 与 max_y<=sum_y 给

    beta_(K,v)(m)<=min(1,K^4 v/(m+1)).               (UC)

不以错误的 sum max<=max sum 把 K^4 降成 K²。另有含退化表的紧性证明给固定 K,v 的 beta→0。对 0<epsilon<1，

    A_K(v,epsilon)=min(1,2^(K+1)K² exp(-2v epsilon²)
                                /(1-exp(-2epsilon²))),
    rho_K(M)=min(1,inf_(1<=v<=M,0<epsilon<1)
       [epsilon+(K-1)/(v+K)+A_K(v,epsilon)+beta_(K,v)(M)]).

rho_K 非增且趋零，并可计算到任意给定正有理绝对误差：分母 L 的有限转移表格最大值 b_grid 满足 b_grid<=beta<=min(1,b_grid+m(K-1)/L)，再在远离 epsilon=0 的公开紧区间作有限区间计算。这里只断言有限可计算性，不给免费或实用计算成本。对 h_N，sup_(theta,mu)R_act<=min(1,rho_K(M)+e_N)。从而对固定 K 有统一均值及统一依概率一致性，不推出统一 a.s.，不扩为 fixed/all/conditional 统一一致性。

### U2：显式粗率及同目标下界

令 J=n_(Y_M)(M)，c=K^4/(M+1)，H(c)=1（c>=1），H(c)=c(1+ln(1/c))（0<c<1）。则对全 theta,mu，

    P(J=0)<=min(1,c), E[1/(J+K)]<=H(c),
    E[1{J>=1}/sqrt(J)]<=2sqrt(2c).

置 A=K ln2+ln(2K²M(M+1))，

    S_K(M)=min(1,min(1,c)+2sqrt(Ac)+(K-1)H(c)+1/(M+1)),
    sup_(theta,mu) E TV(p^+_(Y_M),theta_(Y_M))<=S_K(M),
    U_K(M,Q)=min(1,S_K(M)+(78KM H(c)+K-1)/Q),
    sup_(theta,mu)R_act(F_h)<=U_K(M,Q).              (UQ)

h_N 下可用 min(1,S_K(M)+e_N)。最低合法 h_0 下 Q>=2M，有 min(1,S_K(M)+39K H(c)+(K-1)/(2M)) 的上界；固定 K 均为 O_K(sqrt(log(M+1)/(M+1)))。h_0 不声称与 h_N 逐位相同，也不自动继承有限访问外部行的精确极限分类。

任意 N>=3、K>=2、任意共同随机全历史预测器，某个合法 iid 源的 actual 均值风险至少 1/(16sqrt(N))。可取所有行相同的 Bernoulli 参数 1/2±1/(8sqrt(N))，初始对为 iid；K>2 时其余符号零质量。每 N 选择一个见证，不称存在同一源在全部 N 同时达到下界。

若每次最终输出在分母 R=2^b、b>=1 的 simplex 网格，另有某 iid 源逐输出 TV>=1/(2R)。这是输出格式界，不是内部精度/层数/宽度界；不能与统计下界相加并声称同一见证。前 K-1 坐标 floor、末坐标补残差的 F_R 满足 TV(F_R(q),q)<=(K-1)/R，实际模块需付完整实现成本。

**保留的数学缺口：** sqrt(log N) 是否可去、sharp K 依赖、最优资源—风险关系均未决。不能把固定 K 上下界指数相近称为已匹配的 sharp rate，不能由特殊 iid、稀有 row 或有限 code 下界推出整个 Transformer 类的最优性。



## Parameter domain

K>=2 fixed finite; N>=3,M=N-2; theta in the full product of K-simplexes, mu any pair law; h integer in the stated legal domain. The exact statement separately quantifies upper families, lower-bound algorithms and witness sources; uniform suprema may choose theta,mu per N while each trajectory remains homogeneous.

## Assumptions

- Each experiment has a fixed finite alphabet K>=2 and a time-homogeneous second-order transition table. Zeros and arbitrary initial pair distributions are allowed.
- Only the full observed history, declared query and public parameters are available; the next target and hidden source parameters are unavailable.
- The exact root is conditional on the explicitly defined all-path predicate I for a family F. I is not assumed for the concrete source Pi or for every comparator; a separate normally checked source obligation must establish each actual realization.
- Risk types, quantifier order and each implementation/cost convention remain as defined. Earlier file reviews and prior-project Facts are sources, not automatic admissions in this project.

## Definitions

## A. 共同源、观察、算法及风险定义

对每个整数 K>=2，A={0,...,K-1}，S=A²，D=K²。一个实验固定一个时间齐次二阶表 theta∈(Delta(A))^S，允许零坐标；初始对分布 mu∈Delta(S) 任意。令

    Y_j=(X_(j+1),X_(j+2)),
    P_theta((a,b),(b,c))=theta_(a,b)(c),
    N>=3, M=N-2, E_N=Y_M,
    n_s(M)=sum_(j=0)^(M-1)1{Y_j=s},
    C_s,c(M)=sum_(j=0)^(M-1)1{Y_j=s,X_(j+3)=c},
    p_s^+=(C_s+1)/(n_s+K).

每次预测完整观察 X_1^N。最后一个计数后继是 X_N；Y_M 不是额外 departure。actual query 从已观察最后两符号取得；fixed-query 任务另有明确的公开 s。X_(N+1)、theta、mu、支持、闭类、平稳律、未来行栈及隐藏源标签不可见。外部 query 是同一历史下调用的查询参数，不额外赠送干净端点或统计量。获得和复制实际端点在实现中收费。

共同算法族的程序和公开精度可以依赖 K,N,h，不能依赖未知 theta,mu 或其隐藏标签。统计根中的理想 p^+ 是分析变量；给定实现的计数、头输出等实际可见代码由来源实现义务确定，不能据理想表达式新增 readout 端口。比较中的任意全历史预测器可以用全部 X_1^N 和源独立随机种子，输出任意概率向量。具体 Pi 则遵守自己已声明的内部信息切口。

TV(p,q)=1/2 sum_c|p_c-q_c|。对给定 family F，令 Z_N(s)=TV(F_(K,N,h)(X_1^N;s),theta_s)。严格区分：

| 名称 | 定义 | 量词 |
|---|---|---|
| fixed row | E Z_N(s) | 固定公开 s |
| all contexts | E max_(s∈S) Z_N(s)；另可问其 a.s. 极限 | 全 K² 行，不改成访问行 |
| actual terminal | R_act=E Z_N(E_N) | 同一历史的末尾 query |
| conditional terminal | E[Z_N(E_N)\|E_N=s] | 仅当 p_N(s)=mu P^M(s)>0；零概率时未定义 |
| empirical weighted | E sum_s(n_s/M)Z_N(s) | 同历史频率权重 |
| other history weighted | E sum_s w_s(X_1^N)Z_N(s) | w 为观察历史可测 simplex；不自动有一致性 |

逐源极限固定 K,theta,mu 后令 N→∞。统一均值是每个 N 的 sup_(theta,mu) R_act；取 supremum 时源可随 N 改选，但一个样本路径内部的核必须齐次。固定 K 的统一结论不是 K 随 N 变化的无条件结论，也不是 changing-source 的统一几乎处处结论。输出允许零坐标，损失仅 TV，本 contract 不把它解释为 positive-output KL。


## 共同研究范围的约定

接口I是一个程序性质的定义，不能作为所有算法已经满足的全局假设。条件统计根对任意满足I的共同有限族F证明蕴含式；具体Pi满足I及其完整成本须由SRC-Pi的正常独立来源义务支持，不能在证明SRC-Pi时先假定它。原第二阶段固定证明是可查来源，旧Fact编号不是新项目前驱。

后继真实资源/可靠性命题可以在同一contract内建立独立义务，不必谎称它们是统计根的前提。数据观察及TV实验保持上述定义。每项具体实现须声明自己的内部代码、允许回读、输出格式、参数/字长、batch或streaming等执行方式；比较只在所声明的共同条件下成立。原Pi的finite-attention加pointwise batch hybrid、literal bit/ReLU模块的packed/scalar、sparse/dense选项分别核算，不将一项格式的便宜坐标拼入另一项。

完整费用包括实际head和局部绑定、输入/query/端点取得、参数/零系数、物理字、复制/跨层保持/清除、mask/position、所有活动bank与metadata、online/offline工作和同时峰值。不能免费引入计数、normalizer、译码或生成器。新算术/扰动参数由各精确义务局部量化；改变共同数据律、可见信息或风险须建立新的明确数学范围。

给定接口的条件定理、具体实现定理、训练可达性、必要资源及新颖性是不同主张。数学根只包含数学命题。行政完成程序不是数学前提；独立后续结论不改变已有定理的证明依赖。

