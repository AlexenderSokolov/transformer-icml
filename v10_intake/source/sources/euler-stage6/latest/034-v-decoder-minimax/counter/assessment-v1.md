# 034 Counter：一次互补攻击评估

结论：**GO，限于冻结的完整 DEC-MATCH / DEC-SEQUENCE / 原Pi上界费用合取。** 逐项攻击新增随机标签源、保留侧信息、实际全坐标分箱、Bayes桥和有限常数后，未发现承重缺口。本轮没有另行 submit、增加任务、重审旧Fact或重跑032枚举。

准确OID：`7e9edb773c2453ce6ca6ab0962158682e758dd98a2e5feefd614a6b6e185c6f8`。冻结文件 `outputs/034-v-decoder-minimax/lead/frozen-statement-v1.md` 为11914 bytes，SHA256 `0385830f0ad7f25dee0334213fcd8d099a6ae6b551ba06efc5ccc32c5261586e`。本轮经原生 Euler `research_state` 起止两次读取，目标均为 **DISCHARGED / VALID**；冻结文本与实时原生 exact_statement 逐字符一致。quoted候选/OPEN文字是声明中的历史措辞，不能覆盖实际网关状态。

正常接纳来自原Prover的一次提交，非本报告：Fact **`d3e63f7b5e389adf`**；Evidence **`dbadc5e7ba8291254d133f41b62bbb5acb0368631d6a7cb0b9fda79b4a5b8d3a`**，`LLM_CHECKED_PROOF / PASS / VALID`。本轮核了原始回执、解析回执、实时Evidence、Fact文件和实际提交正文的绑定。正文 `complete-proof-v1.md` 的SHA256为 `17ba6dc117edec4d1315a175f972ab541226eded4525e23652e194c656c1650f`；提交payload为 `e95bae3d226c5b1f1fe4b4d73778283b9584a63cd29263e35a58a66e4d1bcc57`；Fact文件为 `f60b0d2057aa2357a5fb424fda8cf6ec0c72b43c770dee330987838528f39a92`。payload的proof与正文逐字一致；Fact内正文仅容许文件末尾LF的格式差别，内容完全一致。

## 1. 被核范围与直接证据

保留全部整数K>=22、M>=1、h>=h_N、D>=0，完整观察X_1^(M+2)，departure仅0,...,M-1，actual目标theta_(Y_M)，TV=L1/2。每实验一个固定齐次二阶表，零边和任意初始pair律允许。不是excess、fixed suffix lower或全历史任意decoder风险。准确量词是固定共同W-only decoder A，再取source和合法共同kernel的sup，最后对A取inf。private seed和无限计算均允许，历史及其它clean统计端口均不允许。

| 直接Fact | 正常Evidence | 本轮使用 |
|---|---|---|
| SRC `fef8372728290b45` | `e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505` | 实际V逐坐标78误差、exact bits与生命周期、原后缀及完整费用；定点读取其§2、§8核端口 |
| MM5 `946d42d5bf502eb4` | `aa23c442ca1006c6ac0b12379f64a0fa500fbbd6a2e41c798b7a4de3952baa82` | identity核下每个A与clean前缀组合的全历史统计下界 |
| 032 `372cbc90282df2cd` | `1a61c7931a3b8ee13da63e8e24e758106308055d829d8e5e60195fbca96d0cf0` | 同接口上界、有限Euler字/stay圈及T<1参数界 |

这三项实时Evidence均PASS/VALID，当前Fact文件hash均与各自content_hash一致。新正文不引用032的确定标签路径律作为新随机标签律，也未用030局部CLOCK风险、005二元excess、015信息下界或033作为隐藏前提。016仅经032上界传递；没有新增直接依赖或旧Fact逆向依赖。

## 2. 新标签源与完整路径攻击

检查原Prover§2–3的全表：Euler内部pair互异，最后pair排除在较早内部赋值之外。四个互斥符号组和六个distinct marker使新增 `(e,p0)->q1`、`(e,p1)->q1`、`(p0,q1)->w^1_0` 与gate `(xi,zeta)`、`(zeta,p_s)`、`(p0,q0)`、`(p1,q1)`、`(q_s,w^s_0)` 及组内pair不冲突。所有行均按append symbol作合法shift；t_z=0或1也合法。

从任意 `(p_label,q1)` 出发，输出串为 `w^1_0,...,w^1_P,c,e,p_next,q1`，共P+5=L步，两种label分支在同一时刻回到同类B圈入口。label不改变query间距、下一query的均匀选择或再次访问gate的情况。query相位为L-2；gate departure v激活后首query恰在v+L。p0作为label不会误入stay圈，因为当前pair是 `(p0,q1)`，而非 `(p0,q0)`。

对任意余数d=M-mL，k=(L-2-d) mod L。stay gate相位L-2，首次非负gate departure为d，继为d+iL。d=0必须支付真实初始gate；d=L-1时k=L-1，初pair `(zeta,p0)` 无须支付未观察gate。初始残段完全保留，且无未知标签。首次激活在gate index m-j-1时，末query前恰有j个旧query；j=0也合法。

给定固定t、A_j、j+1个query choices和j个旧label，它们唯一决定完整观察历史；不同choices/labels在观察符号中有差别。因此完整路径质量确为

`p_j a^(-2(j+1)) product_i t_(z_i)^(ell_i)(1-t_(z_i))^(1-ell_i)`，

其中p_j=(1/m)(1-1/m)^(m-j-1)>=1/(4m)。端点t=0/1按实际选择概率解释，不需要0^0约定。对labels求和得到真正的t-independent query选择律。中间圈和初始stay段没有额外Cgrp×Dgrp query。于是条件于A_j、末query，J~Bin(j,1/a²)；给定完整无标签choice序列和t，末row的k0~Bin(J,t_z)，其它true count仅为C_p1=J-k0。最后query的departure M标签未观察、不计数。这里条件iid来自新完整路径律，没有推广到一般随机访问行。

## 3. exact side information逐项攻击

SRC实际proof§2、§8（Fact文件约195–238、587–668行）与034正文§3相符。034给A的exception逐项如下；即使将原后缀忽略的这些exact bits全交给A，也不会增加该源上的训练标签信息。

| 输入 | 见证源上的值 |
|---|---|
| K,N,h,Q、位置/type、mask、常数、固定phase/address metadata | 公开固定程序的函数 |
| query A,B、actual/external mode、若保留的declared query | actual mode固定，query为已知z=Y_M |
| actual endpoint l2_q,l1_q | 正是z，不能删掉，但已由末query确定 |
| synthetic x_q、z_q、F_q | q=N+1>=4，全为零 |
| exact endpoint intersections与selection bits | query/mode/endpoint的确定函数；非对角z使SRC endpoint intersection全部为零 |
| 若有initial-position flag副本 | z_t为公开位置bit；唯一可能非零的F_3=e_(X_2)，而初pair y_k公开确定，与未知t及训练labels无关 |

h0、f、rho虽来自flag-valued均值，仍是统计master，SRC明确不将其列入exact-bit例外。其它统计master、频率、products、guard/comparison scratch、余数、历史数组、clean V或旧sum/quotient均非此decoder输入。分配了收费存储不等于获得读取端口；也不能把全历史token冒充flag。034正文没有将这些信息漏删后再声称lower。

核可看history不改变A的可见类。增广输入 `(A_j,z_1,...,z_(j+1),J,k')` 能确定W及以上全部exact bits，因而能精确模拟真实A输入。给增广规则自由选择输出只会减小最优风险；在这个更有信息的实验中对每个规则证明lower，方向正确。未给任何训练label、隐藏k0或t。nonactivation事件只因loss非负被丢弃，不要求该事件上的模拟。

## 4. 同一个共同核与实际全坐标guard

令T=K^(5/2)/sqrt(M+1)，D0=min(D,Q/8)、eta0=D0/Q、x0=K^4 eta0。h_N>=h0、Q>=M+1和Q/8整数成立。只有T<1且x0>256T²时构造分箱核；此时M>=K^5，m>=4，不使用无效小M clock。

由 `eta0>256K/(M+1)` 可得

`D0>256K Q/(M+1)>=256K`，`A0=eta0 M>128K`，

故b=floor(A0/8)>=2且b>=A0/16，全部取整均已支付。对每条history，0<=k'=b floor(k0/b)<=k0<=J<=M；v_p0=k'、v_p1=J-k'定义合法。最终“W*正银行且距离<=D，否则V”的guard使同一个t-independent共同核在全域合法，包含见证源以外的history以及具有其它true labels的history。它没有读取隐藏theta、mu、future或decoder seed。

在见证激活历史，true C只在p0,p1有质量。W*_c=max(1,floor(Q(v_c+1)/M))满足1<=W*_c<=2Q且与对应ideal quantity误差<=1，因0<=v_c<=M。实际SRC坐标的78与本轮floor误差1必须对全部K坐标支付，得到

`||W*-V||_1 <=79K+2Q(k0-k')/M <=79K+D0/4 <D0<=D`。

这里k0-k'<b<=A0/8；D0>256K使79K<3D0/4。故源上guard逐路径总通过，不靠概率good event。全部K坐标被替换，其它K-2个W坐标成为公开M,Q的常量，有限求值误差中可能编码的其它历史信息也全部消除。只改两个理想坐标将不足以证明这个信息结论；提交正文实际支付并覆盖了全部坐标。

## 5. Bayes分箱、小J与随机读出

有限a²维product uniform prior只用于证明lower；每个参数实现仍是一个固定齐次source，同一个guarded核对全部t有效。给定A_j和完整无标签query choices，其律不依t，product prior不变。其它row的未见label求和为1，不引入末row参数的额外likelihood。

对I(r,s)=integral_0^1 u^r(1-u)^s du，有限分部积分递推给r!s!/(r+s+1)!；于是对0<=k<=J，P(k0=k|J,choices)=1/(J+1)，posterior mean为(k+1)/(J+2)。因此给定bin，k在其截取的连续整数集合中均匀。posterior mean不是算法新输入，而仅用于条件Jensen。

任意K维概率q都满足TV(q,theta_z)>=|q_p0-t_z|，允许在其它标签上放质量。固定增广输入与private seed后q_p0是一个常数；Jensen后，对s个连续整数的absolute deviation最小和是floor(s²/4)，ties由median论证覆盖。设n=J+1>=2，则总Bayes风险>=sum_i floor(s_i²/4)/[n(n+1)]。

若b>=n>=2，单bin下界至少1/16。若2<=b<n，完整bins总长度floor(n/b)b>=n/2，每个full bin贡献>=b²/8，故风险>=b/(32n)。最后短bin即使只有一个整数也仅被作为非负项舍弃，没有错误要求其有spread。由此统一>=1/32 min(1,b/n)。

**J=0单独处理不可省略。** 此时bin均值spread为0；参数仍Unif[0,1]，integral |q_p0-u| du=(q_p0²+(1-q_p0)²)/2>=1/4。原正文明确使用这条直接下界，没有把0 spread当作正数。所有论证对每个私有seed成立，再积分即可；允许随机A无漏洞。

利用b>=A0/16以及min(1,b/n)>=b/(n+b)，得到全部J>=0统一的

`Bayes TV >= A0/[512(J+1+A0)]`。

这里inf只允许看到bin，未偷换为能看hidden k、label或t的算法。给定choice序列后J确定，故上式是对可见bin及隐参数平均后的条件风险；不是逐个bin声称同一下界。

## 6. 有限调和、常数与总合取

对该源已证的J条件律用凸倒数Jensen，再用p_j>=1/(4m)：

`Bayes E TV >= A0/(2048m) sum_(j=0)^(m-1) 1/(1+A0+j/a²)`。

递减函数左端点和大于其0到m积分，m>=M/(2L)、M/m>=L，因而准确得到

`Bayes E TV >= eta0 U/2048 ln(1+M/[2U(1+eta0 M)])`。

j=0、m的floor和全余数均保留。设z0=eta0 U、b0=U/M，则x0/4096<=z0<=x0，b0<=4T²<x0/64，所以2(b0+z0)<=10x0。prefactor用z0的lower、log denominator用b0+z0的upper，比较方向均正确。

对v>=1，v ln(1+1/(10v))>=1/11。对0<v<=1，s=ln(1/v)，f(s)=ln(1+e^s/10)满足f(0)>=1/11且f'(s)>=1/11，故v f(s)>=Psi(v)/11。于是冻结候选的/16成立，常数积2048*4096*16=2^27给

`Bayes E TV >=2^-27 Psi(x0)=2^-27 Psi(K^4D/Q)`。

D>Q/8时x0=K^4/8>1，原x也>1，Psi截断恒等；大D无需非法大移动。x0<=256T²时Psi<=2sqrt(x0)<=32T，统计项覆盖；T>=1直接统计项覆盖。D=0、小网格预算、M=1也在这些数值分支，没有偷偷删域。

对每个固定A，同一核下prior平均risk<=该A的source/kernel sup，所以故障lower先成立于r(A)。另有MM5 identity核给2^-16 min(1,T)；两种source的sup lower先取max。非平凡分支得到max(2^-16 T,2^-27 Psi(x))>=2^-28(T+Psi(x))。其余分支分别用F<=1或F=min(1,T+Psi(x))<=33T。三者均足以支付冻结2^-120常数。最后才对A取inf；没有交换inf/sup或宣称同一个source同时实现统计与故障项。

原SRC suffix属于此读出类，因此R_dec,V<=R_V^Pi，032上界直接给min(1,64T+Psi(x))。由完整上下界，风险趋零强迫非负sum T+Psi(x)趋零；Psi(x)>=min(1,x)，故必要且充分为T->0和x->0。没有统一a.s.或同一source跨所有n的推论。

## 7. 原Pi费用、证据边界与保留事项

提交正文§8保留同一SRC dense/uncached实现：p=4h+4ell+64、ell=ceil(log2(M+K+4))，全部M+3位置、六头、word<=128p、depth O(Kp²)、width O(Kp)、dense参数bits O(K³p^5)、attention O((M+3)²(K+p)p²)、全部位置QKV/点运算O((M+3)K³p^6)。input/query/endpoint、mask/metadata、完整products/remainders/guards、holds/copy/clear、最终输出、offline完整格式写出均收费；总peak按同phase共存求和后最大，rolling working不代替总peak。其它sparse/cache/PURE配置未偷拼入nominal费用。

无限计算下界类不等于免费算法；核的计数扫描、selector、存储、移动、程序及任何保护器的物理实现另付。结论限于原未编码finalV端口；不限制改前缀/编码、snapshot、额外统计、历史重读或物理保护，不推出master任意decoder sharp率或所有Transformer资源下界。033中rho nominal可公开恢复的边界仍有效，与本新信息lower无混淆。

本轮只作解析数学攻击、文件读取、hash及原生证据绑定，没有运行finite path/bin枚举、compiler、literal ledger、网络batch、GPU或外部模型。Prover报告中的有限diagnostic数量不是本轮执行记录，也不是普遍证明。核查为有界人工数学复核，未声称形式化机器证明；本轮未识别需登记的新增数学障碍。GO是团队讨论结论，正常Fact来自上述既有网关Evidence。Counter未对Euler graph做typed变更，没有可合理登记的新增obstacle，也未修改图存储或制造review Evidence。

原生起止完整页中30个obligation、28个route、27个Evidence，以及relations、两个blocker、contract、acceptance、budget_policy、frontier_hash均相同；目标接纳在本轮开始前已经完成。manifest逐项记录该比较及直接依赖hash，未据此声称重新审计所有旧proof。[Non-scientific operational metadata omitted.]

031–033不重投；[Non-scientific operational metadata omitted.][Non-scientific operational metadata omitted.]本非root合取及本次GO均不代表v10母题完成。
