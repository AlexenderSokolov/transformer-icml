# REL-V-BANK-JOINT-K（032）：原SRC-Pi最终银行绝对编辑预算与总actual风险

这是031正常接收后的独立nonroot机制可靠性候选，尚未接纳。031不是本项前提；已接纳的STAT/INIT/PI-STAT不重投。新的承重问题是原Pi在最终V银行故障下的联合K、M、D/Q风险，而非重复固定K=2的excess或切口信息下界。先给可核完整候选；若不成立，准确登记障碍，不静默删结论。Lead提出下述clock注入路线，尚非证明或Fact。

## 1. 完整实验、同一程序和故障量词

整数K>=22、M>=1，N=M+2，n_tok=M+3；Y_i=(X_(i+1),X_(i+2))。完整观察X_1^(M+2)，departure仅i=0,...,M-1，actual目标theta_(Y_M)，TV=L1/2。每实验theta为固定齐次二阶表，允许零边及任意初始对律mu。sup可依公开参数选择源；源不能逐路径暗换。

严格使用SRC Fact fef8372728290b45的同一Pi_(K,N,h)，不是023的anchor程序。令
h0=max(4,ceil(log2 M)+1)，h_N=ceil(log2(128(K+1)(M+3)^3))。
本项匹配仅取整数h>=h_N；须核h_N>=h0，Q=2^h。原六头、有限求值、全部位置、原decoder、V银行及有序输出逐位保持。master和其后至V生成均干净，无master故障、无坏事件概率项。

C_c是真实actual query的triple count，J=sum C_c；V为SRC实际正整数银行，V_c in {1,...,2Q}，且逐路径
|V_c-Q(C_c+1)/M|<=78。
切口在全部V_c生成之后、任何最终总和/quotient之前。核T在每条合法历史上把V换为W in {1,...,2Q}^K，||W-V||_1<=D，D>=0是公开整数。核可使用完整已观察历史、当前V、公开参数及源独立种子，不读隐藏theta、mu、未来或预测器私有种子。核是共同Markov映射，预算约束逐路径成立，不仅高概率成立。

原后缀只见W及SRC保留的准确公共/query/endpoint/flag bits；清理过的干净V、总和、quotient、evaluator scratch与历史旁路不可重读。先重算S_W=sum W，再按原有序规则对c<K-1输出floor(Q W_c/S_W)/Q，最后坐标补残差。不改用别的decoder。

定义
R_V^Pi(K,M,h,D)=sup_(theta,mu) sup_(T合法共同核) E TV(Pi^T(X;Y_M),theta_(Y_M))，
T_K=K^(5/2)/sqrt(M+1)，eta=D/Q，
Psi(0)=0，Psi(x)=x(1+ln(1/x))于0<x<1，Psi(x)=1于x>=1。
这里是固定原程序的总actual均值风险，不是故障相对clean的excess，也不是inf_decoder。

## 2. 一次完整目标

证明全部上述有限参数满足
2^-80 min(1,T_K+Psi(K^4 eta))
 <= R_V^Pi(K,M,h,D)
 <= min(1,64T_K+Psi(K^4 eta)).                    (V-MATCH)

D可大于银行最大距离；合法核类自然饱和。保留D=0、M=1、全部h>=h_N、所有horizon余数及完整K坐标。上界可按016的更广合法h范围引用，但本匹配不由此扩展到h0。不得把K<22、master扰动或031的条件源类加入此结论。

上界预期从016 Fact a53804d650803060的原Pi联合故障界取delta=gamma=0：
min(1,48T_K+(K-1)/Q+
 Psi(K^4 M(78K/Q+D/Q)/(M+1)))。
须明确由Psi次可加/单调及原合法精度界推出V-MATCH的64系数，保留真实J、正银行归一化和实阈值。实质另用Fact须登记。

下界允许取MM5 Fact946d42d5bf502eb4与恒等核，给
R_V^Pi>=2^-16 min(1,T_K)。
另用以下合法源与共同核给故障项；两个不同源的sup下界先取max，不能相加成同一源或称每条轨迹都困难。

## 3. 可核新路线：全余数clock与有限银行注入

只需在T_K<1的非平凡支段构造；其余由MM5覆盖。令a=floor((K-6)/4)，P=a^2，L=P+5，m=floor(M/L)。须证明a>=4、K/8<=a，且T_K<1保证m>=4。

使用四个互斥符号组A={0,...,a-1}、B={a,...,2a-1}、C={2a,...,3a-1}、Dgrp={3a,...,4a-1}，六marker(p0,q0,p1,q1,xi,zeta)=(4a,...,4a+5)。本节Dgrp是符号组，D仍为编辑预算。
w_0,...,w_P取从0回0、每个有序相邻pair恰出现一次的含loops Euler字；w^0=w，w^1=w+a。需给有限存在性、赋值无冲突与合法shift核：
(p_s,q_s)->w^s_0，(q_s,w^s_0)->w^s_1；
(w^s_i,w^s_(i+1))->w^s_(i+2)，0<=i<=P-2，s=0,1；
最后A pair->xi，(w^0_P,xi)->zeta；
(xi,zeta)->(1-1/m)delta_p0+(1/m)delta_p1，(zeta,p_s)->q_s；
最后B pair->Unif(C)，(w^1_P,c)->Unif(Dgrp)，(c,e)->p1，(e,p1)->q1；
其他行delta_0。

stay圈y0=(p0,q0)，y1=(q0,w0)，y_r=(w_(r-2),w_(r-1))于2<=r<=P+1，
y_(P+2)=(w_P,xi)，y_(P+3)=(xi,zeta)，y_(P+4)=(zeta,p0)。
写d=M-mL，k=(L-2-d) mod L，mu=delta_(y_k)。观察中的门保持真正随机1/m激活，初pair不付未观察的早期门概率。
必须自足证明：首次门departure=d，之后未激活门d+tL；首次激活后末尾前有j个旧query的质量
p_j=(1/m)(1-1/m)^(m-j-1)>=1/(4m)，0<=j<=m-1。
此前j个query及actual末query由完整路径律条件iid Unif(C×Dgrp)，指定完整选择序列质量p_j a^(-2(j+1))。实际末对departure M不入历史，真目标delta_p1；条件于实际末对，J~Bin(j,1/a^2)。保留首残段全部历史，不能删history或把一般源条件样本称iid。

该source-writing来自030全余数构造；030的CLOCK/PARTIAL风险只在它自己的分支内，本项不外推它到T_K<1的全部参数。上述源/路径论证须在新正文自足，若实际调用030额外定理则如实注册直接依赖。anchor共同floor相位机制不用于本SRC-V实验。

设d_edit=min(D,Q/8)，eta_0=d_edit/Q，Q/8为整数。共同核在实际query属于C×Dgrp时只改变wrong label 0：
W_0=V_0+min(d_edit,2Q-V_0)，W_c=V_c (c!=0)，其他query保持V。
核只需公开K,M,h,D、实际query及当前V，不读J、真实counts、theta或未来。须在全路径证明合法预算与正银行，而在所构造源上另证容量足够，使增量恰d_edit。不得用理想V代替实际V；逐坐标78误差、总和78K及高精度Q均支付。

p1=4a+2<K-1须核；目标质量由非末坐标的floor给出，故若确有增量d_edit，应从实际输出导出
TV(Pi^T,delta_p1)
 >= d_edit/(sum V+d_edit)
 >= eta_0 M/[J+K+78KM/Q+eta_0 M]。
这是候选计算链，需逐步检验，包括D=0时的零项，不把非负总损失当成excess。

对J的凸倒数作条件Jensen，再按真实p_j求和；取U=a^2 L，预期得到某个明确常数的有限调和下界，形如
(eta_0 U/4) ln(1+M/[2U(K+1+eta_0 M)])。
必须保留m=floor(M/L)取整、j=0、全余数及Q误差，不能把此候选式当Fact。

合并的可检验方向：K^4/4096<=U<=K^4，U(K+1)/M可由常数T_K^2控制；若K^4 eta_0<=T_K^2，Psi<=2sqrt(.)使统计下界覆盖，其他参数由调和式支付log与饱和。D>Q/8用允许小预算核包含关系。证明固定2^-80总常数，不为常数另拆节点。若该桥失败，登记准确不等式和真实范围，不默许改成大样本/对齐结论。

## 4. 可靠性意义、费用及严格边界

若V-MATCH成立，则对任意K_n>=22、M_n>=1、h_n>=h_N(M_n,K_n)、整数D_n>=0的公开序列，
R_V^Pi(K_n,M_n,h_n,D_n)->0
当且仅当T_(K_n)->0且K_n^4 D_n/Q_n->0。
由总风险下界和Psi的性质给必要性，由上界给充分性；这是固定Pi和指定V切口、最坏合法核的均值一致性，不声称同一源全参数困难、统一a.s.或任意decoder的sharp必要性。必要的两项可以由不同源见证。

该结论拟回答“联合K下最终银行需控制多少归一化总编辑”这一机制接口问题。它不提供物理纠错构造或同资源优势；015的任意decoder二元信息下界、原master切口及物理编码仍保持自己的scope。本项不更换decoder、不增加snapshot/count table/cache/历史读取。

同一SRC主实现dense/uncached，真实p=4h+4ell+64、ell=ceil(log2(M+K+4))；全部M+3位置、六heads、input/query/endpoint、QKV/mask、完整算术products/remainders/guards、holds/copy/clear、输出、offline完整格式和逐phase共存总peak沿SRC完整收费。故障核是明确的信息层扰动实验；若将其或保护器物理实现，注入器、selector、数据移动、存储与程序成本另付，不属于nominal Pi免费能力。未运行compiler、literal ledger或batch测量；[Non-scientific operational metadata omitted.]不回021/022费用定义循环。

## 5. 依赖、证据和分工

预计直接Fact前驱仅SRC fef8372728290b45、016 a53804d650803060、MM5 946d42d5bf502eb4。既有Fact不重证或添加逆向依赖。全余数source可复用写作来源，但新概率范围与actual银行/有序输出/调和桥必须自足证明。
完整 V-MATCH/序列等价/费用保持合取需要独立审查；讨论与有限检查不是已接纳的定理。失败写准确障碍，不删除或偷偷缩小目标。031不再列候选；031 Fact53aa09cd3b53aefb及Evidence81742e0b0292442a08f50836040f73605371a9329ca82e863018fd3b58cc096f保持。
[Non-scientific operational metadata omitted.]本地不另开重合研究。Dot已完成S001--S019固定来源，S018/S019只按科学需要正常吸收，不逐个造19义务。当前本地成员表无Dot投递入口，不能把本地记录冒作已向原Dot派发。
030小K/低kappa及027两方法障碍保留；一般master联合K、任意decoder sharp故障率、物理纠错和真正资源关系仍未决。[Non-scientific operational metadata omitted.][Non-scientific operational metadata omitted.]同类通道再失败保存实际错误，不机械重试。v10母题仍未完成。
