# 032 Counter：一次互补范围与承重检查

2026-10-29；准确OID `02da4576308aa8b8abc12ded4c285018a0c3ef4375f713b027fde13927e15fff`。

**结论：GO；未发现新增承重缺口，当前无需解除条件。** 已检查冻结V-MATCH、实际SRC-V银行注入、全余数完整路径、有限调和桥、序列充要性及费用保持，并对照原Prover当前470行完整正文。本报告只是一次有界互补讨论；Counter未submit、未新增Fact/Evidence、未重跑旧证明或数学枚举。

检查开始时，原生032已DISCHARGED/VALID：Fact `372cbc90282df2cd`，Evidence `1a61c7931a3b8ee13da63e8e24e758106308055d829d8e5e60195fbca96d0cf0`，LLM_CHECKED_PROOF / PASS / VALID。该接纳来自原Prover正常网关。本次另以具体数学正文检查，不把Prover交接中的“accepted”自述当独立数学依据。

## 1. 准确范围及文件绑定

对象为同一SRC-Pi、K>=22、M>=1、全部整数h>=h_N、D>=0，完整X_1^(M+2)、M次departure及同轨迹actual E[TV]。master至V生成均干净，故障只在最终V切口；W正整数、每路径L1编辑<=D，后缀从W重算sum/quotient并保留原ordered floor/residual。核是共同Markov映射，不读隐藏源/未来/私有预测器种子；不换decoder。

本次完整读取032冻结文件与Prover complete-proof-v1.md；对SRC/016/MM5只核原生Evidence、准确接口及文件身份，不重新证明。030是写作来源，其局部CLOCK/PARTIAL风险未作本项前提；031及Dot统计结果也未作前提。Prover有限preflight未由Counter执行，其数量不算本次证据。

- 冻结SHA256 `7311bf5eca3b4800d0da5a9e292ed8299c224856137f7016ffe0ebf64e15ab64`，9476 bytes，逐字节等于当前原生exact_statement；已接纳Fact的statement及Evidence exact_claim一致。
- Prover完整正文SHA256 `a993aaa8c844642fa8c99b6c569453f0de8cf747a33cb76af7b5f98fbc1d1f00`；实际提交JSON为 `fc1a1f355df3f0218ef8abcf51978bdcc70d02dc20777c571c65e60c81c43695`。载荷proof逐字等于正文。
- Fact文件SHA256 `e7295c4903277b5d403a453f429a62a60a5dc8ca6a6b04e9917646088fb39476`；Fact保留完整证明，仅末尾两个LF变为一个。冻结文字里的候选/未接纳措辞保持原样，当前接纳身份以原生Evidence为准。
- 已重算Prover submission-manifest的14项及最终manifest的23项绑定，全部实际字节数/hash匹配；这只是身份核验，不把被哈希的诊断脚本当作已执行或普遍证明。Counter来源清单见manifest-v1.json。

## 2. 高精度与上界：真实J、正银行和Psi

令A_prec=128(K+1)(M+3)^3。A_prec>=16且>=2M，故h_N>=h0；每个允许h均有Q>=A_prec、Q/8整数。更强地Q>78KM，所以epsilon_V=78KM/Q<1。无h的上限、M对齐或额外大样本前提。

SRC的实际正银行误差逐坐标78，故对于任意合法核输出，
`||W-V*||_1<=D+78K`，其中 `sum V*=Q(J+K)/M`。正向量归一化给TV<=min(1,L1误差/真实比较总和)，再付有序输出的(K-1)/Q。于是016的联合故障界取delta=gamma=0恰好适用，包含与历史/J相关的核。

Psi的积分表示 `integral_0^1 min(1,x/t)dt` 在x=0和饱和区均成立，直接给单调、次可加与Psi(x)<=2sqrt(x)。把实现项与预算项拆开，
`Psi(78K^5 M/[Q(M+1)]+K^4 M eta/(M+1))`
`<=2sqrt(39)T_K+Psi(K^4 eta)`；
加48T_K与输出项<=T_K，系数49+2sqrt(39)<63<64。真实J始终在正分母J+K中；016实阈值TRUNC允许D/Q为非整数，D=0及J=0不例外。上界较广h范围不被用来扩大032下界的精度域。

## 3. 全余数源：端点、初残段与Binomial律

非平凡分支T_K<1给整数M>=K^5。a=floor((K-6)/4)满足a>=4、4a+6<=K<=4a+9<=8a；L=a²+5<=K²，故m=floor(M/L)>=K³>=4。源仅在该分支使用；M=1及T_K>=1由恒等核/MM5覆盖，不定义非法m=0/1的门概率。

Euler字的有限存在性由平衡有向图闭路拼接给出。内部有序pair全异，最后pair未在前面的递推赋值中出现；四字母组与markers互斥，跨组/门/返回行无冲突，所有转移均合法shift、齐次且概率归一化。源一次按公开K,M选定，不随轨迹换表。

stay圈gate相位L-2，k=(L-2-d) mod L，d=M-mL，0<=d<L。因此首个观察门departure恰为d，以后未激活门在d+tL。特别：

- d=0时，初pair就是门，departure0的随机选择必须入路径概率。
- d=L-1时，k=L-1，初pair=(zeta,p0)，下一输出q0合法。初pair允许直接指定，不需支付未观察的更早stay概率。
- 门在t激活后，首个B query恰在t+L；末slot M=d+mL属于actual query或未激活门，其departure不入历史。

首次激活门index为m-j-1时，恰有j个旧query，质量
`p_j=(1/m)(1-1/m)^(m-j-1)>=1/(4m)`，0<=j<m。固定全部j+1次C×Dgrp选择后，包含首残段、各stay/activation及每个返回的完整观察路径唯一，质量 `p_j a^(-2(j+1))`。因此条件于激活j及实际末对z，旧query仍iid uniform，且
`J~Bin(j,1/a²), C_p1=J, C_c=0(c!=p1)`。

C_0=0是actual query行的后继计数，不是说整条历史没有0号符号。初始A残段和后续clock没有额外C×Dgrp pair，故其全部历史保留也不改变该计数结论。无需旧H_A下界、anchor floor好相位或030浓缩分支。这里的条件iid只由此特定源的完整路径律导出，未推广至一般Markov访问样本。

## 4. 全历史合法核与源上加满：实际78/78K均已支付

共同核仅在公开C×Dgrp actual query上改0号坐标，增量
`min(D,Q/8,2Q-V_0)`；其余坐标及其它query保持。对任意历史、任意合法V，这都是非负整数，<=D且不越2Q，W仍正。核只用公开参数、实际query及当前V，不用J、真实counts或隐藏theta。不是只在source支持上才合法的核。

在所构造源的activated query历史上，C_0=0，SRC真实误差给
`V_0/Q<=1/M+78/Q<(1+1/K)/M<=3/2`。
因此V_0+Q/8<13Q/8<2Q，源上实际增量确为d_edit=min(D,Q/8)。此处确实用真实V的78误差，没有把V换成理想Q(C+1)/M。

令S=sum V。所有K个add-one和误差给
`S<=Q(J+K)/M+78K`；高精度进一步给78KM/Q<1。真实目标p1=4a+2<=K-4<K-1且p1!=0，是非末坐标。故原程序目标输出满足
`q_p1=floor(Q V_p1/(S+d_edit))/Q<=V_p1/(S+d_edit)`。
于是
`TV(q,delta_p1)=1-q_p1>=d_edit/(S+d_edit)`
`>=eta_0 M/[J+K+78KM/Q+eta_0 M]`
`>=eta_0 M/[J+K+1+eta_0 M]`。

方向正确：目标坐标的floor增加可用的总损失下界；无需给wrong-label坐标floor后的质量作下界，也没有丢掉最后residual或全K个质量。D=0仅给零故障项，所有分母仍正。这是总risk下界，不是相对clean的excess。

## 5. Jensen、有限m及调和桥

置A_edit=eta_0 M，B_edit=K+1+A_edit。函数x↦1/(B_edit+x)在x>=0凸；条件Binomial均值为j/a²，Jensen给所需的**下界**A_edit/(B_edit+j/a²)。对实际末对均匀条件律求和后，用真实p_j>=1/(4m)，并仅丢弃非负的未激活损失，
`R_clock>=A_edit/(4m) sum_(j=0)^(m-1) 1/(B_edit+j/a²)`
`>=A_edit a²/(4m) ln(1+m/(a²B_edit))`。
递减函数的左端矩形在积分之上，j=0和有限上限均保留。

取整只用M/m>=L及m>=M/(2L)；分别降低非负前因子与单调log因子，得到冻结提议的明确式
`R_clock>=eta_0 U/4 ln(1+M/[2U(K+1+eta_0 M)])`，U=a²L。
成立范围是整个T_K<1分支及全部h>=h_N、D>=0、全余数；没有偷加对齐、浓缩或大样本条件。

## 6. 统计补集、log/饱和与不同源max

令x=K⁴eta_0、z=eta_0 U、b=U(K+1)/M。有限参数界给
`x/4096<=z<=x, b<=4T_K²`，调和式化为
`R_clock>=(z/4)ln(1+1/[2(b+z)])`。

若x<=T_K²，Psi(x)<=2T_K，恒等核/MM5足以覆盖min(1,T_K+Psi(x))，包括D=0。若x>T_K²，b+z<5x，故
`R_clock>=x/(4*4096) ln(1+1/(10x))`。
一般标量不等式
`x ln(1+1/(10x))>=Psi(x)/11>=Psi(x)/16`
成立：x>=1用ln(1+t)>=t/(1+t)；0<x<=1令v=ln(1/x)，函数ln(1+exp(v)/10)在v>=0的初值与导数均>=1/11。该一般推导支付log区与饱和，无小配置浮点风险作证。

所以该分支R>=2^-18 Psi(x)，同时同一supremum由恒等核与MM5给R>=2^-16 T_K。先取max，再比较得R>=2^-19(T_K+Psi(x))；未声称一个源实现两项之和。T_K>=1直接由MM5覆盖。所有分支均强于冻结所需2^-80常数。

D>Q/8时eta_0=min(D/Q,1/8)，K>=22保证K⁴/8>=1，故
`Psi(K⁴eta_0)=Psi(K⁴D/Q)`；一个小预算核已属于所有更大预算核类。D超过银行最大距离也不改变合法性。整数D=0、Q/8整数及预算饱和都已单独支付。

## 7. 序列、费用与精确边界

V-MATCH给任意合法公开参数序列：风险趋零当且仅当T_K趋零且K⁴D/Q趋零。充分性用Psi<=2sqrt；必要性由非负和的cap趋零，再用Psi(y)>=min(1,y)。不要求同一源见证所有n或两项必要性，不升级为统一a.s.、任意decoder或excess结论。

源与故障核是信息层实验；实际SRC程序、原六头、全M+3位置、K个输出、真实p=4h+4ell+64、ell=ceil(log2(M+K+4))均保持。完整dense/uncached点运算/QKV/attention、input/query/endpoint、mask、products/remainders/guards、holds/copy/clear、输出、offline全格式及逐phase共存总peak沿SRC收费；rolling数组不代替总peak。物理注入器/保护器、selector、数据移动、存储和程序费用另付，032不提供物理纠错或同预算优势。

|直接Fact|已核Evidence（PASS/VALID）|实际引用scope|
|---|---|---|
|SRC fef8372728290b45|e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505|实际Pi、正V切口、78银行误差、原后缀及完整费用|
|016 a53804d650803060|fef1785395851e47b5ca0b719640449061718f4c670bfcd74c24cf0aec696c88|48T、实阈值TRUNC、联合故障上界delta=gamma=0|
|MM5 946d42d5bf502eb4|aa23c442ca1006c6ac0b12379f64a0fa500fbbd6a2e41c798b7a4de3952baa82|每个固定共同全历史预测器actual下界；先固定h仍适用|

Fact frontmatter、实际提交载荷、Prover依赖清单均只有这三个直接前驱，未新增030或031；旧证明不重审，旧依赖不反向修改。

**新增数学障碍：无；解除条件：不适用。** 正常独立网关是必要接纳门槛，原Prover已通过；Counter讨论及hash复核不能替代网关。证据等级为LLM_CHECKED_PROOF，不是形式化证明或资源实测。K<22、仅h0精度、master联合K、任意decoder sharp故障率、物理纠错和真正资源比较仍在032之外。

Dot投递诊断 `ebfd7e3592f7556d4c7131eaa28e133221b39b6f79b5c9a35171cc37ed250ebf` 的完整旧记录可在Prover native-before-v1.json定位。032关闭后它不在当前active blocker视图，不能据此宣称Dot入口找到或已投递。本次不修改该失败记录，不把协作投递问题当032数学前提，不另派或替代Dot。

[Non-scientific operational metadata omitted.][Non-scientific operational metadata omitted.]本轮未执行compiler、literal ledger、batch测量、数学枚举或新模型任务，未改工具/调度/内部图存储；v10母题仍未完成。

