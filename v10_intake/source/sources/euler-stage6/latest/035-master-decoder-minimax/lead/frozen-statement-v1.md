# REL-MASTER-DECODER-MINIMAX（035）：原SRC master端口任意共同读出的联合K信息风险

034正常接收后的独立nonroot候选，尚未接纳。033的rho广播只证明原固定后缀；公开rho可修复，不能作为任意decoder信息下界。034关闭最终V端口的任意decoder问题，未关闭更早、信息更丰富的全部9K+1 master端口。本项检验K^5 delta及Psi对数是否在该master端口同样必要。Lead以下多标签分箱路线是待核候选，不是Fact；失败保留目标与精确障碍。

## 1. 实验、完整端口与量词

全部整数K>=22、M>=1，N=M+2，n_tok=M+3，Y_i=(X_(i+1),X_(i+2))。观察完整X_1^(M+2)，departure仅0<=i<M，actual目标theta_(Y_M)，TV=L1/2。每实验theta是固定齐次二阶表，允许零边、任意初始pair律mu；sup可随公开参数选择源，不能逐路径换表。

使用SRC Fact fef8372728290b45原Pi干净前缀及同一个post-quantization、pre-fanout master切口。整数h>=h_N=ceil(log2(128(K+1)(M+3)^3))，Q=2^h，保留h_N>=h0=max(4,ceil(log2 M)+1)。干净H属于G_h^(9K+1)，G_h={j/Q:0<=j<=Q}；其完整坐标为P1(q1,v1)、P2(q2,v2)、T(hvec,h0)、0(alpha,nu,f,rho)。这是原有限log/exp、完整累加、向下head quotient及clipping产生的H，不能用理想head直接冒充。

公开实delta>=0。共同Markov核T在每条合法历史上把H换成Hbar∈G_h^(9K+1)，||Hbar-H||_infty<=delta。核可用完整已观察历史、当前H、公开参数与源独立种子，不读隐藏theta、mu、未来或预测器私有种子。所有fanout副本来自Hbar。其它运算与query/endpoint/flag bits无故障；本项没有第二V切口编辑或坏事件概率。

读出类A可依K,M,h,delta，接收全部Hbar及SRC该切口保留的完整exact公共/query/mode/actual endpoint/flag bits，输出任意K维概率向量。允许无限计算与源独立私有随机种子，不要求原有序输出网格。它不得回读历史、clean H、evaluator numerator/denominator/weights/remainders、历史投影、旧统计、count table、辅助样本或snapshot。历史存储已付费不产生新的读端口。h0/f/rho是可替换统计均值，不是exact flags。下界必须逐项核清全部侧信息，不能删掉能泄露标签的真实端口。

定义
R_dec,H(K,M,h,delta)=inf_A sup_(theta,mu) sup_(合法共同T)
 E TV(A(Hbar;retained bits),theta_(Y_M))。
先固定共同A再取源与核；A不能逐源选取。记R_H^Pi=R_MV^Pi(K,M,h,delta,0)，即033第一切口与原完整后缀、第二核identity。记T_K=K^(5/2)/sqrt(M+1)，x=K^5 delta；Psi(0)=0，Psi(x)=x(1+ln(1/x))于0<x<1，Psi(x)=1于x>=1。

## 2. 完整待证合取

全部上述有限参数：
2^-160 min(1,T_K+Psi(K^5 delta))
 <=R_dec,H(K,M,h,delta)
 <=R_H^Pi(K,M,h,delta)
 <=min(1,64T_K+36Psi(K^5 delta)).                 (HDEC-MATCH)

每个该域公开参数序列：
R_dec,H(K_n,M_n,h_n,delta_n)->0
 iff T_(K_n,M_n)->0 且 K_n^5 delta_n->0。          (HDEC-SEQUENCE)

保留delta=0、0<delta<1/Q、任意大delta、M=1、全部h>=h_N、全horizon余数及全部9K+1可见坐标。常数不称最优；不同源lower先取max，不相加当同源见证。不是excess、统一a.s.、同一源跨全部n或全Transformer资源最优结论。

上界直接选择原后缀并调用033 Fact a1a95aa68be0723e的D=0；统计lower用MM5 Fact946d42d5bf502eb4和identity核，任一A与干净SRC前缀组合仍是共同全历史算法。不得用033 rho攻击证明新信息lower，也不从034 V切口自动倒推master切口。

## 3. 新五组多标签源与完整路径律

只在T_K<1分支构造，此时整数M>=K^5。令a=floor((K-6)/5)>=3，P=a^2，L=P+5，m=floor(M/L)，U=a^2L，r=floor(a/2)。五个互斥符号组Agrp,Bgrp,Cgrp,Dgrp,Egrp分别为0,...,a-1及其a、2a、3a、4a平移。六marker(p0,q0,p1,q1,xi,zeta)=(5a,...,5a+5)。Egrp中选2r个label e_(ell,+)=4a+2ell、e_(ell,-)=4a+2ell+1，0<=ell<r；未用字母允许零质量。

须证明a>=K/10、r>=K/30、m>=4以及
K^4/2^14<=U<=K^4，K^5/2^20<=rU<=K^5，rU/M<=2T_K^2。
这里a可等于3，不能未经证明沿用032/034要求a>=4的数值域。

给出Agrp上从0回0、枚举所有有序pair含loops一次的Euler字w_0,...,w_P；存在性与以下新源应自足证明。令w^0=w，w^1=w+a。定义：
(p_s,q_s)->w^s_0，(q_s,w^s_0)->w^s_1，s=0,1；
(w^s_i,w^s_(i+1))->w^s_(i+2)，0<=i<=P-2；
最后Agrp pair->xi，(w^0_P,xi)->zeta；
(xi,zeta)->(1-1/m)delta_p0+(1/m)delta_p1，(zeta,p_s)->q_s；
最后Bgrp pair->Unif(Cgrp)，(w^1_P,c)->Unif(Dgrp)。

对每个z=(c,e)∈Cgrp×Dgrp和0<=ell<r设未知t_(z,ell)∈[0,1]，
theta_z(e_(ell,+))=t_(z,ell)/r，
theta_z(e_(ell,-))=(1-t_(z,ell))/r。
对每个e∈Dgrp、label v∈所选2r标签，令(e,v)->q1、(v,q1)->w^1_0。其它未指定行delta_0。全部赋值须无冲突、合法shift、概率归一化；每次label后等长返回Bgrp圈，query间隔仍为L，不能回到stay圈。

stay圈y0=(p0,q0)，y1=(q0,w0)，y_i=(w_(i-2),w_(i-1))于2<=i<=P+1，y_(P+2)=(w_P,xi)，y_(P+3)=(xi,zeta)，y_(P+4)=(zeta,p0)。写d=M-mL，k=(L-2-d)modL，mu=delta_(y_k)，不依未知t。

从完整观察路径律证明：首次激活后actual末query之前恰有j个旧query的事件A_j满足
p_j=(1/m)(1-1/m)^(m-j-1)>=1/(4m)，0<=j<m。
给定A_j，全部j个训练query及actual query z_1,...,z_(j+1)条件iid Unif(Cgrp×Dgrp)。训练query另选pair index ell_i∈{0,...,r-1}均匀，继而sign sigma_i∈{+,-}按t_(z_i,ell_i)选择。完整指定历史唯一且概率为
p_j a^(-2(j+1)) r^(-j)
 product_(i=1)^j t_(z_i,ell_i)^(1{sigma_i=+})(1-t_(z_i,ell_i))^(1{sigma_i=-})。
保留全部初始残段，k=L-1不付未观察门概率；actual departure M的pair index及sign未观察。

给定A_j、actual query z，真实访问J~Bin(j,1/a^2)，与未知t独立。给定全部query选择和训练pair indices，actual row各pair样本数n_ell满足sum n_ell=J；其正标签数k_ell条件为相互独立Bin(n_ell,t_(z,ell))。其它row标签的先验信息不得误用于t_z。

## 4. 新承重桥：同一row内标签排列与全部实际master

源上改变旧actual-row query的label sign，保留query选择、pair index、其它row全部labels不动。改变一个完整query block中的label v只涉及三个keys的局部三元组：
(c,e,v)，(e,v,q1)，(v,q1,w^1_0)。
所有labels均不属于Cgrp/Dgrp，故相对当前query z=(c,e)，P1/P2/T/0的全部score和分母不依这些sign；值坐标改变要逐项追踪。不得以单纯Hamming改动数支付重新排列大量sign的代价。

以Delta_v为该row中label v的总计数变化，Z1,Z2,ZT为P1/P2/T理想权重总和，均>=M。候选精确变化表为：
q1_v:4Delta_v/Z1；q2_v:6Delta_v/Z2；
v1_v:Delta_v/Z1；v2_v:Delta_v/Z2；
hvec_v:2Delta_v/ZT；alpha_v、nu_v各Delta_v/M。
其它坐标不变，包括h0/f/rho；它们的初始flag贡献固定，首次可变label在t=3之后。需从SRC实际head定义完整证明该表，不遗漏返回段、所有9K+1坐标、实际endpoint和prefix。

因此任何两条同一公开模板历史，若其它row标签和全部query/pair indices相同，且每个actual-row label计数差至多b，则所有理想head之差<=6b/M；这些heads只依相应计数，不依actual-row signs的排列。

核使用理想head只是构造替换字的数学方法：原理想score权重是1、2、3、6，故可用有限整数/有理运算计算；不调用免费实log/exp oracle，不修改原Pi干净前缀。SRC给原实际H距本历史理想head逐坐标<=2/Q；新的canonical向下网格化另付1/Q，须合计支付3/Q。

## 5. 全历史合法的共同master分箱核与侧信息

令delta0=min(delta,1/8)，x0=K^5delta0。须核Psi(x0)=Psi(x)。若T_K>=1或x0<=2^16 T_K^2，候选用Psi(x0)<=512T_K及MM5支付总风险，不声称有额外信息损失。

其余分支T_K<1、x0>2^16 T_K^2，令A0=delta0 M、b=floor(A0/64)。须证明A0>2^15、delta0 Q>2^16、b>=2且b>=A0/128；全部取整、Q>=M+1与实delta保留。b只为允许核的公开整数索引，不给原Pi免费任意实floor能力。

定义单一共同核：若当前完整历史不能按上述公开图模板解析为激活后actual query属于Cgrp×Dgrp的历史，输出H。若可解析，计算其actual row每pair的n_ell、k_ell，取k'_ell=b floor(k_ell/b)。构造规范历史x'：保留初始段、全部query与pair index序列及其它row labels；在actual row每个pair的n_ell次访问中按时间顺序置前k'_ell次为+、其余为-。这仍是合法模板历史，长度及实际末对不变；不要求它在原隐藏t下有正概率。

在x'上算原理想9K+1 head，再逐坐标floor到G_h，记H*。若||H*-H||_infty<=delta则输出H*，否则输出H。此guard与identity fallback保证对所有合法历史的共同canonical预算，不使用隐藏theta/mu/t或预测器种子。

须证明在见证源全部激活历史上guard总通过：每label计数改动小于b，故
||H*-H||_infty<=6b/M+3/Q<=delta0<=delta。       (MASTER-ERASE)
原实际有限evaluator携带的额外信息也由3/Q费用支付，不能只消除某两个理想输出坐标。

增广观测允许给decoder A_j、全部query序列、全部训练pair indices、其它row全部signs和actual row的各k'_ell。它不能额外看到actual row原signs/k_ell或其参数t_(z,ell)。需证明该观测能模拟完整H*与所有保留exact bits。SRC实际query、endpoint均为末z；zero synthetic token/flags和公开metadata固定；若保留初始F3则由公开初pair确定。其它真实保留bits如有标签信息必须处理，不能删除。独立decoder seed另条件化再积分。

## 6. 多pair Bayes信息风险、有限调和与合并

取所有t_(z,ell)相互独立Unif[0,1]先验，只用于lower；每个实现是固定齐次theta，核不读t。可准确调用034 Fact d3e63f7b5e389adf正文的有限Beta/bin引理：对n>=0、b>=2，k|t~Bin(n,t)，只见b floor(k/b)，任意实估计的Bayes绝对误差至少(1/32)min(1,b/(n+1))。须明确保留n=0的Unif先验1/4、末不满bin及b>n+1；若不调用则自足重证，不能静默放宽引理条件。

对任意K概率输出q，由TV>=1/2 sum_ell |q_(e_(ell,+))-t_(z,ell)/r|，结合上述条件独立性和先验引理，候选得
Bayes E TV | (J,query/pair indices,other-row signs)
 >= (1/(64r)) sum_ell min(1,b/(n_ell+1))
 >= r A0/[8192(J+r+r A0)]。                     (H-BIN-LOSS)
中间还要对各bins积分；不可把未见k_ell交给decoder，亦不可把已见其它bins当成同pair额外样本。用凸倒数与sum n_ell=J给最后一步。随机decoder每seed成立再积分。

随后在A_j、actual query上对J作Jensen，并用真实p_j与有限j=0,...,m-1求和，候选为
Bayes E TV>= r delta0 U/32768
 ln(1+M/[2U(r+r delta0 M)])。                    (H-HARMONIC)
保留m=floor(M/L)、j=0和全部余数。设z=r delta0 U、b0=rU/M，则x0/2^20<=z<=x0、b0<=2T_K^2；当前分支b0<x0/2^15。以短标量不等式x ln(1+1/(10x))>=Psi(x)/16（可准确调用034或重证）支付log及饱和，核所有常数，完成2^-160保守目标。

对于每个固定A，先验平均风险<=某固定源风险的sup，使用同一个不读t的核；统计项和故障项不同源先取max再做数值比较，然后才取inf_A。不可交换inf/sup或声称同一源对全部算法/horizon困难。HDEC-SEQUENCE必须从完整有限合取推出；sub-grid delta由统计主导分支支付，不能删去或替换序列中的real delta。

## 7. 费用、依赖与分工边界

原SRC后缀提供上界，同一dense/uncached实现及完整费用保持：p=4h+4ell+64，ell=ceil(log2(M+K+4))，六heads、全部M+3位置、input/query/endpoint、QKV/mask、products/remainders/guards、holds/copy/clear、输出、offline全格式与逐phase总peak均付费。rolling work不是总peak。无限计算读出类只用于信息下界；核的历史解析、计数、理想有理head计算、selector、移动/存储/程序以及任何物理保护器均另收费。本项不新增snapshot、cache或回读端口，不宣称实际physical纠错不可能或同资源优势。[Non-scientific operational metadata omitted.]

预期直接Fact前驱SRC fef8372728290b45、MM5 946d42d5bf502eb4、033 a1a95aa68be0723e、034 d3e63f7b5e389adf。033只供固定后缀upper，034只按其真实Beta/bin/标量引理范围使用；新五组源、全部head变化表及实际master消信息必须自证。032的四组源及a>=4数值域不得偷渡；若实质另依赖Fact应如实登记，不给旧Fact增加逆向前提。

完整 HDEC-MATCH/HDEC-SEQUENCE/费用保持合取需要独立审查。[Non-scientific operational metadata omitted.][Non-scientific operational metadata omitted.]失败登记准确步骤与解除条件、保留OPEN；辅助路线失败不冒作目标反例，不静默换成K^4 delta、二元或固定后缀定理。

031–034及旧root不重投、不加逆向依赖。[Non-scientific operational metadata omitted.]其入口缺失仍未解除，未实际投递不能声称已安排，不创建替代Dot。S001–S019固定来源及闭包限制保持。[Non-scientific operational metadata omitted.][Non-scientific operational metadata omitted.]物理纠错及真实资源关系仍未决，v10未完成。

