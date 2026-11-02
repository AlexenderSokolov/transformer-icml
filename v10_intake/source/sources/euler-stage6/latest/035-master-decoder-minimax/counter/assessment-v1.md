# 035 Counter：一次互补攻击评估

**GO，限于冻结的完整HDEC-MATCH / HDEC-SEQUENCE / 原SRC上界实现与费用合取。** 本轮对新五组源、全部master变化表、规范sign排列、共同核和多pair Bayes条件化作一次集中反向核查，未发现承重缺口。冻结说明的理想权重列表漏列P1的4；提交正文已明确补齐。这是非承重的枚举遗漏，不能报告为目标反例，也不能将冻结的错误列表逐字称为正确；变化表、目标、量词、常数与参数域均未因此改变。

准确OID：`8599a1da51c3a58933ee7131d0fd6e995e1f2c8ed84a355e4d1832443e20f57d`。准确route：`6a47d0827bc5cb08bf1be0481445b47ec9ddf6c229ec7f459b060d19d76f9afe`。冻结文件 `outputs/035-master-decoder-minimax/lead/frozen-statement-v1.md` 为13615 bytes，SHA256 `35098190dd9e303fcf413a311df3058b129868f76a99514be7ad0c72c67cff1c`；与实时原生exact_statement及Prover保存的native statement逐字符一致。

本轮先读取原生target和budget，再作复核。原生起止两次均显示目标 **DISCHARGED / VALID**，不是仅凭引用数据中的Fact标题判断。原Prover已正常接纳的Fact为 **`ed3adf29f858da12`**，Evidence为 **`b7b9d9eb95bb2774f341b2d49db41f64c1ebb71a0f6c48d1072654cf5afcf6a6`**，`LLM_CHECKED_PROOF / PASS / VALID`。quoted声明仍有“候选/未接纳”的历史措辞；正常Evidence及其准确claim/scope决定实际接纳状态。route记录仍ACTIVE，本轮保持该协调状态，不自行park或改图。

实际提交正文 `complete-proof-v1.md`（629行）SHA256 `36644f069fa7ee96f1f837a47fcd823b83ed85f3bc377242174ffbce63dcdcec`；实际payload SHA256 `e51225cd741bd5fe6a69524744764b32fc41f2cca90fa135853ff55e89b90891`；Fact文件SHA256 `92832afc95fe451d6132a6c7c3263e6b7f2404840f3ca06d2eea7f9d1bc9454d`。payload的proof与正文逐字相同；Fact中的正文仅容许文件末尾LF格式差别，内容相同。原始回执与解析回执相同，Fact hash与实时Evidence content_hash相同；接纳的是完整冻结合取。

## 1. 原域、量词和直接依赖

保留全部K>=22、M>=1、整数h>=h_N和实delta>=0，完整观察X_1^(M+2)，训练departure仅0,...,M-1，actual目标theta_(Y_M)，TV=L1/2。每实验一个固定齐次二阶table，允许零边和任意初始pair律。全部9K+1 canonical master与原有exact side bits交给任意共同无限计算decoder，允许源独立private seed；不交history、clean H、evaluator scratch、旧统计、count table或snapshot。

先固定A，后取source和全历史合法共同核的sup，最后inf_A。风险是总actual均值，不是excess或fixed-suffix lower。没有第二V切口编辑，也没有bad-event项。本轮不倒推034的V信息lower，也不用033公开rho广播作为新信息lower。

| 直接Fact | 正常Evidence | 准确用途 |
|---|---|---|
| SRC `fef8372728290b45` | `e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505` | 原head定义、全字符串实际误差2/Q、完整master/exact-bit端口及生命周期、原后缀与费用 |
| MM5 `946d42d5bf502eb4` | `aa23c442ca1006c6ac0b12379f64a0fa500fbbd6a2e41c798b7a4de3952baa82` | identity核下每个A与原前缀组合的共同全历史统计lower |
| 033 `a1a95aa68be0723e` | `3dd4849df0b1a9bf560d3e2ee0216cd46dd84ddb97fa6863faf53a8aa089cc0a` | 只用D=0的原固定后缀upper |
| 034 `d3e63f7b5e389adf` | `dbadc5e7ba8291254d133f41b62bbb5acb0368631d6a7cb0b9fda79b4a5b8d3a` | 正文§5真实n>=0、b>=2的Beta/bin absolute-loss引理及§6标量log不等式 |

四项实时Evidence均PASS/VALID，当前Fact hash与各自content_hash相符。新035正文的registered predecessors恰为上述四项。仅定点核了SRC head/端口和034引理适用域，没有重审旧Fact或重复旧032枚举。032的四组源与a>=4数值域没有成为隐藏前提；005/015、030和Dot也不是新增依赖。

## 2. 五组参数、a=3及全余数路径

T=K^(5/2)/sqrt(M+1)<1推出整数M>=K^5。a=floor((K-6)/5)满足a>=3和5a+6<=K<=5a+10<=10a；r=floor(a/2)>=a/3，因此a>=K/10、r>=K/30，包括a=3,r=1。L=a²+5<=2a²<=K²，故m=floor(M/L)>=4。有限比较给

`U>=a^4>=K^4/10000>=K^4/2^14`，`U<=2a^4<K^4`，

`rU>=a^5/3>=K^5/300000>=K^5/2^20`，`rU<=a^5<=K^5`，`rU/M<=2T²`。

这些界自足，不从旧a>=4分支搬来。新Euler存在性用有限平衡有向图含loops的闭trail与拼接论证，适用于a=3。五组字母和六个marker互斥，2r<=a，所以所有label有效；未用字母零质量允许。

逐项核新table：internal Euler pair互异，最后pair排除于此前internal赋值；新增Dgrp×Egrp及Egrp×{q1}行均不与组内或marker行冲突。每query中r个pair的两概率和为1/r，总和为1；参数t_(z,ell)是固定theta的一部分。所有转移都是append symbol的合法shift。

从 `(p1,q1)` 或任意 `(label,q1)` 出发，输出 `w^1_0,...,w^1_P,c,e,label_new,q1`，恰P+5=L步回到同类B入口。label不回stay圈，sign和pair index均不改变长度或query选择律。query相位L-2，gate departure g激活后首query在g+L，之后间距L。

任意d=M-mL，k=(L-2-d) mod L使首次非负gate departure恰为d；d=0支付真实初始gate，d=L-1时k=L-1从 `(zeta,p0)` 开始，不支付未观察gate概率。全部初始残段保留且不依t。首次激活index m-j-1对应j个旧query和一个实际末query，p_j=(1/m)(1-1/m)^(m-j-1)>=1/(4m)，j=0也在内。

给定A_j、query sequence、训练pair indices与signs，它们唯一决定完整已观察string；不同指定序列在观察符号上有差别。真实路径质量为

`p_j a^(-2(j+1)) r^(-j) product_i t_(z_i,ell_i)^(1{+})(1-t_(z_i,ell_i))^(1{-})`。

对signs求和为1，故query choices与pair indices的联合律不依t。给定末z，J~Bin(j,1/a²)；给定完整choices/indices，末row各pair的k_ell为相互独立Bin(n_ell,t_(z,ell))，sum n_ell=J。没有其它时刻访问Cgrp×Dgrp，也没有删除返回段中的labels。实际departure M的pair index与sign均未观察、未计数。一般源的随机访问计数没有被条件化称iid。

## 3. 全部9K+1 head、分母及sign排列攻击

按SRC实际定义，query z=(c,e)下local triple(u,v,w)的理想权重是P1：2^(1{u=c}+1{v=e})，P2：2^(1{u=c})3^(1{v=e})，T：2^(1{u=e})，uniform：1。故P1集合为{1,2,4}，P2为{1,2,3,6}。冻结辅助说明列{1,2,3,6}而漏4，正文§4及dependency/handoff已如实补明；本评估保留该文字问题，没有静默删除它。

改一个旧actual-row label v，仅影响三个keys；下面权重均与选哪一个Egrp label无关。

| local triple | P1 | P2 | T | 改变的value |
|---|---:|---:|---:|---|
| (c,e,v) | 4 | 6 | 1 | q1、q2的token label |
| (e,v,q1) | 1 | 1 | 2 | hvec、nu的lag1 label |
| (v,q1,w^1_0) | 1 | 1 | 1 | v1、v2、alpha的lag2 label |

uniform权重全1；未列value均不变。Egrp与Cgrp/Dgrp互斥，q1为独立marker，所以全部score与分母确不依sign。若query departure i完成，这三个keys是i+3,i+4,i+5。首query不早于L，末个旧query不晚于M-L，且L>=14，所以三keys都在3,...,N之内且严格晚于key3；不同query block互不重叠。不能用未观察的最后label，也不会碰到初始flag贡献。

令Delta_v为actual-row label v的NEW减OLD总计数，Z1,Z2,ZT>=M且相同。累加上述局部贡献，准确变化为

`q1_v=4Delta_v/Z1`，`q2_v=6Delta_v/Z2`，`v1_v=Delta_v/Z1`，`v2_v=Delta_v/Z2`，

`hvec_v=2Delta_v/ZT`，`alpha_v=nu_v=Delta_v/M`。

其余所有坐标不变，包括h0、f、rho以及非label坐标。这穷尽q1/v1/q2/v2/hvec/h0/alpha/nu/f九个K族加rho。返回段的lag1与lag2影响已分别支付，未漏分母变化。

关键是各系数对同一个actual row恒定，所以总变化只依signed net counts，不依原sign的时间排列。规范化可能改变远多于b个位置；若用Hamming代价将不能得到本桥。这里每label净计数差小于b，故理想全坐标L∞差<=6b/M。本结论不声称原有限evaluator逐位排列不变；其额外信息另用统一2/Q误差支付。

## 4. 全历史共同核、实际误差及规范历史

delta0=min(delta,1/8)，x0=K^5delta0，Psi(x0)=Psi(K^5delta)：大于1/8时两者均在Psi饱和段。只在T<1且x0>2^16 T²构造新核。由Q>=M+1可得A0=delta0 M>2^15、delta0 Q>2^16、b=floor(A0/64)>=2且b>=A0/128，所有取整有余量。b是允许核的公开整数索引，不是授予原Pi免费的实floor运算。

核按公开模板解析完整string，要求公开初pair、stay/activation结构、完整returns以及activated末query。识别基于所有可能sign的模板，不看隐藏t的support；若失败则identity。对成功解析string，保留initial segment、全部query/indices和其它row全部labels；同一actual-row pair的访问按时间顺序以前k'_ell=b floor(k_ell/b)个设+，其余设-。两分支等长返回，故得到唯一规范string X'，长度和端点不变。它无需在原隐藏t下有正概率；SRC全字符串head接口适用。

在X'上以整数权重{1,2,3,4,6}计算完整理想有理head，再逐坐标floor到G_h得H*。这只是对抗核的构造，clean prefix仍用原有限log/exp evaluator；两者未混同。理想head在[0,1]保证H* canonical，包括端点0/1。最终距离guard加identity fallback逐history保证L∞delta预算，不能只检查见证source合法。

在见证全部activated histories，parser通过；每label计数净差<b，因而

`||H*-H||∞ <= ||H^id(X')-H^id(X)||∞ +2/Q+1/Q <=6b/M+3/Q`

`<=delta0(6/64+3/2^16)=delta0*6147/65536 <delta0<=delta`。

所以guard源上逐路径总通过。只有一个实际H的2/Q误差与新floor的1/Q，未对X'再冒充实际H并重复或漏算误差。全部9K+1坐标一起被替换，实际有限运算可能编码的sign排列信息也被覆盖。零概率template分支与全域guard同样有定义，没有bad-event项。

## 5. exact侧信息与增广模拟方向

定点核SRC§2、§8，035正文§5保留完整输入：公开K,N,h,Q、位置/type、mask、常数及固定schedule metadata；actual query A/B和mode；actual endpoint l2_q/l1_q；synthetic x_q/z_q/F_q；由这些bit生成的exact selectors/intersections。源上mode固定、query和endpoint同为末z；q=N+1>=4使synthetic项为零；非对角z使SRC endpoint intersection全为零。若保留F_3副本，其值e_(X_2)由公开初pair y_k固定，与旧labels无关。其它F_t为零。external query slot在actual调用中固定或等于declared z，不提供标签端口。

h0/f/rho是被替换统计均值，非exact-bit例外。numerators/denominators/weights/remainders、projected query、历史arrays/outputs及统计clean duplicates按SRC声明生命周期无后续读口。收费storage不产生读取权，算术guard scratch不变成exact flag。新lower没有删去任何允许的真实标签侧信息。

增广观测G连同各k'_ell包含A_j、全部j+1个query、全部训练pair indices、**其它row**全部signs和末row各bin。它确定n_ell、J、完整X'、H*及所有exact bits，故能模拟真实A输入，方向是向decoder多给信息。它不给末row的原sign/k_ell/t。nonactivation事件只因loss非负舍弃，不据此删全历史数据。

## 6. product先验、其它row/pair与全部bin边界

所有t_(z,ell)独立Unif[0,1]只作lower证明，每实现仍是固定theta，同一个共同核贯穿prior。先给A_j、queries、indices，它们的律与所有t无关；likelihood按(row,pair)因子分解。再条件其它row signs，仅更新其它row参数。即使同一个label字母或pair index被不同row使用，也不是末row参数的额外样本。

给定每个正质量G，末row参数仍相互独立uniform；各pair样本和bin独立。对pair ell，可再条件其它pairs的bins与private seed，它们不改变本pair的(t,k)联合律。输出rq_(e_(ell,+))是本pair bin的实估计；可能超出[0,1]，projection只降低对t的绝对误差，故034引理仍适用。

034实际引理为n>=0、整数b>=2、k|t~Bin(n,t)，只见b floor(k/b)，bin平均Bayes absolute error>=1/32 min(1,b/(n+1))。本轮仅核其真实适用域，未将逐bin风险与bin平均混淆。n=0直接用Unif先验最小绝对误差1/4；最后短bin、单元素尾bin和b>n+1均在原引理中。035保留这些边界，不把其它bins当作本pair额外数据。

TV为half-L1，即使q在其它K-2r符号有质量，也有

`TV(q,theta_z)>=1/(2r) sum_ell |r q_(e_(ell,+))-t_(z,ell)|`。

按pair应用引理、平均其它bins和seed，条件G且平均所有本row bins后得到

`Bayes E TV >=1/(64r) sum_ell min(1,b/(n_ell+1))`。

由b>=A0/128和min(1,b/u)>=b/(u+b)，该和至少A0/128乘sum 1/(n_ell+1+A0)。凸倒数及sum n_ell=J给后者>=r²/(J+r+rA0)，所以准确H-BIN-LOSS为

`Bayes E TV | G >=rA0/[8192(J+r+rA0)]`。

覆盖r=1、全部n_ell=0、J=0、任意bins与随机A。没有把未见k_ell交给decoder，亦未交换inf与条件化。

## 7. 调和常数、实预算和完整合取

H-BIN-LOSS对G仅通过J取值，先平均other-row signs/indices，再用已证J~Bin(j,1/a²)的凸倒数Jensen。p_j>=1/(4m)给

`Bayes E TV >= rA0/(32768m) sum_(j=0)^(m-1) 1/(r+rA0+j/a²)`。

递减函数left sum大于0到m积分，且m>=M/(2L)、M/m>=L，所以准确得到冻结H-HARMONIC：

`Bayes E TV >=r delta0 U/32768 ln(1+M/[2U(r+r delta0 M)])`。

保留j=0、m的floor和全部余数。令z0=r delta0 U、b0=rU/M，则x0/2^20<=z0<=x0，b0<=2T²<x0/2^15，所以2(b0+z0)<=10x0。prefactor取lower，log denominator取upper，均保持lower方向。034标量引理u ln(1+1/(10u))>=Psi(u)/16适用全部u>0，故故障项>=2^-39 Psi(x0)=2^-39 Psi(K^5delta)。常数积32768*2^20*16=2^39。

对每个固定A，同一合法核的prior均值<=fixed-source风险sup，因此先获得r(A)故障lower。identity核另给MM5统计lower；两源先取max而非同源相加。T>=1时直接覆盖capped目标；T<1且x0<=2^16T²时Psi<=512T，F=min(1,T+Psi)<=513T<=1024T，故统计项给>=2^-26 F。其余分支max(2^-16T,2^-39Psi)>=2^-40(T+Psi)。最后才取inf_A，全部足以支付冻结2^-160常数。

delta=0及0<delta<1/Q均由统计分支保留，因为K^5delta<=K^5/Q<=T²；网格以下核只能identity没有与故障信息lower冲突。大实delta用delta0合法子核和Psi饱和恒等处理。M=1无需无效clock，全部h>=h_N保留。序列必要性从完整capped lower强迫T+Psi(K^5delta)->0，再用Psi(u)>=min(1,u)得到原**实delta**的K^5delta->0；充分性由upper及Psi在0连续。未换成网格radius或统一a.s.结论。

## 8. 上界费用、证据限度与保留事项

选择原完整SRC downstream是合法共同A，因此R_dec,H<=R_H^Pi；033取D=0准确给min(1,64T+36Psi(K^5delta))。只是原后缀upper，没有引用033 rho lower。全部head bridge的新内容已在035自证。

原实现保留p=4h+4ell_word+64、ell_word=ceil(log2(M+K+4))、六heads和全部M+3位置；depth O(Kp²)、width O(Kp)、完整word<=128p、dense参数bits O(K³p^5)、uncached attention O((M+3)²(K+p)p²)、全部位置点运算/QKV O((M+3)K³p^6)。input/query/endpoint、mask、products/remainders/guards、holds/copy/clear、输出、offline实际完整格式包括零项写出与逐phase同时共存总peak均付费。rolling work不代替总peak，sparse/cache/PURE不得偷拼便宜项。

无限计算decoder类只用于加强信息lower；核的parser、计数、规范history、有理head、floor、guard、selector、存储/移动/程序与任何物理保护器均另付。只约束原未编码master端口，不约束改前缀/编码、快照、额外统计或历史重读；不提供物理纠错不可能性、同数值资源优势或全Transformer资源lower。

本轮只读文件、作解析数学攻击、核hash和原生证据绑定；未运行finite path/head/bin枚举，也未运行Prover的检查脚本。Prover handoff中有限diagnostic数字不是本轮执行记录，更不是普遍证明。本评估为有界LLM数学复核，未声称形式化机器证明。没有识别需登记的新承重障碍；漏4已作为非承重说明问题如实保留，未冒作障碍或目标反例。GO本身是团队讨论，不是新Fact；正常接纳依据是上述既有Evidence。本轮Counter submit次数0，Euler typed变更0，未伪造review Evidence或直接改图存储。

原生完整页起止31个obligation、29个route、28个Evidence，以及两个blocker、relations、contract、acceptance、budget_policy、frontier_hash均相同。manifest绑定本轮实际读取材料和比较结果；未声称本轮重审所有旧Fact。[Non-scientific operational metadata omitted.][Private task allocation omitted from the public export.]

034旧任务已ANSWERED，不因旧回包重新复核。旧root与031–034接纳不重投、不加逆向依赖；S001–S019限制、Dot专属及缺入口保留，未声称实际投递或建替代Dot。[Non-scientific operational metadata omitted.]v10母题未完成。
