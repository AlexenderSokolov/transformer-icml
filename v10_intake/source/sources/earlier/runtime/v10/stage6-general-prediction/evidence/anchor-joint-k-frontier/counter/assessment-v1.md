# 027 一次有界互补预检：共享anchor、joint-K上界与clock下界

Counter，2026-10-29。仅针对 diagnostic OID c9d2f2d07e036688ffb481878486cdd40330e4564e75b1339e654a4c072dd3a8。本文是未接纳的数学核查报告，不是Fact；本轮不submit。

本次判断：AGG及全域UPPER成立，直接统计前驱必须明确包含016。两阶段pair-clock已有可检查的合法实现，不再只是UC sharp的猜想；其完整观察律和实际共同floor可在严格子域给出Psi(K^4/lambda)量化下界。全域匹配仍NO-GO；现有方法缺口不是目标反例。另可从该子域推导出：任何统一上界若保持O(T)统计项，不能把量化项中的K^4整体换成K^p、p<4。这仍不证明全参数域的匹配下界。

## 1. 本轮来源、原生状态和依赖

首先读取Lead文件 outputs/027-anchor-joint-k-frontier/lead/bounded-frontier-question-v1.md，SHA256 8a198af293ad5ba4db5de2d05c761a23c4a9aa1df59018030fa1f85f13085223。原生Euler状态显示027为OPEN、evidence_refs为空，路线 [redacted orchestration identifier] 为ACTIVE。

随后通读Prover的461行 joint-k-frontier-diagnostic-v1.md，SHA256 8a1ba3557d4d94340e2637d07f400eb71bdd863cafd83cd313603e6cf9e7d092，并独立核查其全域上界、完整源、占用、相位、实际head、两次clip和有限求和。Prover的有限checker只是辅助，未把小配置结果当全参数证明。

实际使用的既有Fact为：

|用途|Fact|原生Evidence（均PASS/VALID）|
|---|---|---|
|准确F、有限weight、全路径合法性与完整费用|023 c5ca8f2e82eafcfc|4bdb115ae34079859922c01c137d03a50853cedb43cefa6736969773bc852fa4|
|actual add-one 48T及TRUNC|016 a53804d650803060|fef1785395851e47b5ca0b719640449061718f4c670bfcd74c24cf0aec696c88|

本地Fact的hash分别为92c451b503e6a288fa1b2a6f7eec3efd4e02cb737ae0caaad88d86b991105538和bc24d183f5299df636e67f0b439aadbcd4d79671b69c327ed7083ddfab857c6f，均与原生content_hash一致。016是本轮直接依赖，不隐藏在023的既有依赖内。MM5、UC的sharp性、026的固定K结论均未用于制造量化下界；026按要求不再审查。

已读取Prover登记的MISSING_PREMISE记录 f557ceba3e8d54defd029041857c535baf2130460e4013afb265d2d296affa72：其内容是全域尚缺的随机相位/参数域条件，不是证明Psi(K^4/lambda)不可能。Counter进一步给出第8节的准确空事件见证，对该扩域障碍作实质加强；其Euler诊断ID见manifest，不另开研究路线。

## 2. AGG：一个head内的共同分母确实消去多余K倍

固定任意完整历史及query，在q的一头内写d=D_int/R、s_c=A_int,c/R、R=2^u。M个历史key各贡献一个one-hot label，synthetic anchor只有anchor value且weight准确R，因此

    d=1+sum_c s_c，0<=s_c，d<=D_*=4M+1.

每个head分别有此恒等式，四头的d不必相等。令x=G/d>=8、Z=floor(x)、Y_c=floor(x s_c)、f=x-Z、e_c=x s_c-Y_c。则Z>=7x/8>0、Z_safe=Z，且准确有

    Y_c/Z-s_c=(s_c f-e_c)/Z，0<=f,e_c<1.

同一f必须保留。直接求和给

    sum_c|Y_c/Z-s_c|
      <=(sum_c s_c+K)/Z
      <=(8/7)d(d+K)/G.

这里没有把同一anchor误差作为K个任意相关扰动另行放大。即使K远大于M，不出现的label也有s_c=Y_c=e_c=0，所用K项只是保守估计，仍合法。

设S_c为理想整数weight分子。每个key的有限weight误差只进入一个label，所以

    sum_c|s_c-S_c|<=sum_(M keys)|finite_weight/R-ideal_weight|
                  <=100M u2^-u.

没有额外K倍。half-up到整数的误差每坐标至多1/2，含ties。因为S_c∈[0,4M]，第一clip是相对真实比较点的收缩：

    |clip_[0,4M](z)-S_c|<=|z-S_c|.

因此单头的L1误差不超过(8/7)d(d+K)/G+K/2+100M u2^-u。理想四头容斥给真实C_c∈[0,M]；四头三角界后再用

    |clip_[0,M](z)-C_c|<=|z-C_c|

得到

    ||C'-C||_1
      <=(32/7)D_*²/G+(32/7)D_*K/G+2K+400M u2^-u.

两次投影均按包含比较点的方向使用，未提前删除clip，也未声称非q anchor正。

原DOMAIN给D_*/G<=1/8。实际u的023界200G u2^-u<=1/G又给400M u2^-u<=2M/G²<=1<=K/2。故K项最多为(4/7+2+1/2)K=(43/14)K<4K，而32/7<8。因此AGG的完整有限式

    ||C'-C||_1<=8D_*²/G+4K

成立于全部合法K>=2、M>=1、h、g；不需要高lambda、K<=M或任何源正性。M=1时D_*=5、G>=40（合法G实际至少64），同一推导逐项有效。K>>M时所得风险界可能饱和，但程序及证明均未越域。

## 3. 归一化、最终floor和UPPER的直接统计前驱

令V=C+1、V'=C'+1，真实总量A=J+K，计算总量A'>0。加减V'/A给

    ||V'/A'-V/A||_1
      <=(||V'-V||_1+|A'-A|)/A
      <=2||V'-V||_1/(J+K).

取TV后因子2消失。原ordered输出的前K-1项各floor损失<1/Q，最后残差接收其总和，TV误差至多(K-1)/Q。因此

    TV(F,p^+)<=min(1,(8D_*²/G+4K)/(J+K))+(K-1)/Q.

这里使用真实J+K，不假定计算总量A'等于它，也未把非q的sum C'<=KM误写成<=M。

直接调用016的TRUNC与actual 48T。TRUNC包括实A>=0：在0<t<1，若x=A/t-K>0，则{J<x}={J<ceil x}且ceil x<=x+1<=A/t；x<=0为空事件。整数UC提供的上界经layer-cake积分给Psi(cA)，c=K^4/(M+1)，没有条件iid或反向UC推理。

Psi(x)=integral_0^1 min(1,x/t)dt自足给单调、次可加、Psi(cx)<=cPsi(x)（c>=1）及Psi(x)<=2sqrt(x)，包括零和饱和端点。逐项有

    D_*²/(M+1)<=16M （差值16M(M+1)-D_*²=8M-1>=0），
    c(8D_*²/G)<=128K^4/lambda，
    c(4K)=4T²，Psi(4T²)<=4T，
    (K-1)/Q<=K/(2M)<=T.

于是全原DOMAIN有

    R_K<=min(1,53T+Psi(128K^4/lambda))
       <=min(1,64T+128Psi(K^4/lambda)).

支持Lead UPPER的原常数。其统计来源是016，确定性有限程序来源是023；本次核查不产生新的已接纳上界Fact，也不是运行方式或资源收费的改变。

## 4. 两阶段clock的完整合法机制及首个占用引理

以下核查Prover已经写出的具体源，范围K>=22。取a=floor((K-6)/4)>=4，四个不交组A、B、C、D各a个符号，加六个互异marker p0,q0,p1,q1,eta,zeta，总4a+6<=K。令w_0,...,w_(a²)为A上的pair枚举Euler字，首末均为0；其a²个相邻有序pair各出现一次。B上取平移复制。字的有限存在性来自平衡完全有向图的unused-edge闭路拼接，循环规则只用于源规范，不是F的新程序。

设L=a²+5、m>=2、M=(m+1)L-2、epsilon=1/m、mu=delta_(p0,q0)。两个stage在各自(p_s,q_s)后依次输出该组的a²+1个clock符号；边界行(p_s,q_s)、(q_s,w_0)和所有内部pair按字顺序赋值。最后内部pair分别改为以下出口，不重复赋值：

    A block: w^A_0,...,w^A_(a²), eta,zeta,p0,q0 （概率1-epsilon）
             或同一前缀后p1,q1                    （概率epsilon）；
    B block: w^B_0,...,w^B_(a²), c,d,p1,q1，
             c∼Unif(C)、d∼Unif(D)，每圈重新抽取。

等价逐row规范：A最后pair->eta，(w^A_(a²),eta)->zeta，(eta,zeta)->p0/p1，(zeta,p0/p1)->q0/q1；B最后pair->Unif(C)，(w^B_(a²),c)->Unif(D)，(c,d)->p1，(d,p1)->q1。其他row为delta0。所指定row总数3a²+2a+8；不同marker/字母类型互不冲突，两个内部pair集合也不交。每次转移都为(x,y)->(y,z)，各block严格L步，激活后不可返回。

在phase L-2，A为gate pair(eta,zeta)，B为query pair(c,d)。在M=mL+(L-2)时，如先前激活，实际末对就是当前新抽取query；其自己的departure恰为M，未计入观察的0,...,M-1，真实目标为delta_(p1)。

设已完成B圈数为n∈{0,...,m-1}。激活概率

    p_n=(1/m)(1-1/m)^(m-n-1)>=1/(4m).

对任意给定的n及先前n个query和当前query序列，完整历史唯一，路径概率准确分解为p_n a^(-2(n+1))。这是完整观察律，不是丢掉可能泄露信息的clock后才假设iid。于是给定当前query，先前相同行、列和交叉计数R_i、C_j、J分别具有Bin(n,1/a)、Bin(n,1/a)、Bin(n,1/a²)边缘律，三者可相关。每次该query departure都输出p1，所以J是原actual计数。

若n<=a²v/2，Markov给P(J<v|n,current query)>=1/2。计入这些n及p_n可得

    P(Y_M∈C×D,J<v)>=(1/16)min(1,a²v/m)
                   >=(1/16)min(1,a^4v/(M+2))
                   >=2^-16 min(1,K^4v/(M+2)).

最后使用a>=K/8。故该clock确实实现K^4占用尺度于这些horizon；没有从UC上界反推sharp，没有将MM5的统计下界作为量化下界。仅本引理仍不足以证明F必然输出错误。

## 5. 实际joint四头：从占用到错误质量的关键核查

在给定末query(c_i,d_j)的完整历史上，只有先前C×D query departures能匹配第一或第二query符号；它们的label都为p1。所有其他label都是wrong，其每头分子严格为R H_c（H_c是该label的普通departure计数）。理想分母为

    (M+1,M+1+R_i,M+1+C_j,M+1+R_i+C_j+J).

实际分母为

    R(M+1)，
    R(M+1)+(E1-R)R_i，
    R(M+1)+(E1-R)C_j，
    R(M+1)+(E1-R)(R_i+C_j-2J)+(E2-R)J，

E1=W(L2)、E2=W(2L2)分别来自完整score递推。这些是共同可达恒等式；不存在人为独立HEAD噪声。

Prover的部分量化结论严格保留

    kappa=lambda/a^4>=2^48，M>=2^80 K lambda²，
    K>=22，M=(m+1)L-2，m>=2.                     (SUBDOMAIN)

设w=lambda n/(a²M)、1<=w<sqrt(kappa)/1000，r={lambda-aw}、z={lambda-(2a+1)w}、H=z-2r。每单位w周期内，r∈[0,1/4]的a个分支对固定r覆盖全部模a余数；非整数lambda造成分支索引改变时，这个余数集合仍完整。因此可用

    (1/a)sum_(j=0)^(a-1){x+j/a}=(a-1)/(2a)+{ax}/a

求和，不需要把各分支索引固定到整个r区间。积分得到该band上的integral H>=(a-2)/(16a)>=1/32。H<=1给{H>=1/16}长度>=1/60；删除r、z距整数<rho=1/1000的点后长度>=19/1500>1/100。相位跳跃至多3a+1个，每段条件仿射，好集合至多4a区间。

真实n格点步长Delta=lambda/(a²M)，每周期好n至少1/(100Delta)-8a>=1/(200Delta)。SUBDOMAIN支付端点损失，并保证这些n<m/2，因此至少一半历史圈仍是A圈；A label总量H_A=(m-n)(a²+1)>=M/8。

设beta=10^-6，E_n要求R_i、C_j、J各自距均值至多beta M/lambda。各边缘二项方差<=n/a，用Chebyshev与union而不要求三者独立，得到

    P(E_n^c|n,current query)
      <=3a w lambda/(beta²M)
      <=3/(beta²2^80)<1/2.

在E_n上理想anchor相对lambda-aw或lambda-(2a+1)w的误差由计数波动、倒数展开和实际有限weight共同支付：

    3beta + lambda/M + 16a²w²/lambda + 1/lambda
      <21*10^-6<delta=1/10000<rho.

所以同一历史同时产生

    Z10=Z01=floor(lambda-aw)，
    Z11=floor(lambda-(2a+1)w)，
    Z00=floor(G/(M+1)).

00整数边界不近似。所有Z>=lambda/2>=2。写b_ab=(GR/D_int,ab)/Z_ab，则1<=b_ab<1+2/lambda，且真实phase符号给

    Gamma=b11-b10-b01+b00
      >=[H-3delta-4(aw+1)/lambda]/lambda
      >=1/(32lambda).

至此才获得正错误质量机制；占用引理本身从未被用来免费保证共同floor符号。

## 6. 子域下界：两次clip、全部K质量与有限求和

对每个A label c，实际Y_ab,c=floor(H_c GR/D_int,ab)。raw half-up相对H_cb_ab误差<=1；非负且<2M，所以第一clip在这些wrong labels上不动作。第二clip仍保留正确方向：

    C'_c>=H_c Gamma-4>=H_c/(32lambda)-4.

比较下界允许为负且始终<=M，因此投影不破坏该方向。把a个A label求和，以H_A>=M/8及M/lambda>=2048a支付舍入，得到sum_(c∈A)C'_c>=M/(512lambda)。

其他label不需要预设clip不动作；用已核AGG控制全bank即可：

    Bsum<=J+8D_*²/G+5K
         <=(w+206)M/lambda<=256(w+1)M/lambda.

这里J<=(w+beta)M/lambda、D_*<=5M、K<=M/lambda，故K个add-one全计入。归一化后A质量>=1/[2^17(w+1)]。所有A坐标属于前K-1项，最后有向floor总扣减<=a/Q<=K/(2M)；SUBDOMAIN保证M>=2^17K(w+1)，所以

    sum_(c∈A)F_c>=1/[2^18(w+1)].

真实目标delta_(p1)在A外，actual TV至少这一质量。每个好n激活概率>=1/(4m)，E_n概率>=1/2；每周期好n数>=a²M/(200lambda)。有限调和求和因此给

    E TV>= [a^4/(1600*2^18 lambda)] sum_(k=1)^(Jper-1)1/(k+2)
         >=[1/(6400*2^18)] ln(kappa)/kappa
         >=2^-40 ln(kappa)/kappa
         >=2^-53 Psi(K^4/lambda).

Jper=floor(sqrt(kappa)/1000)，使用kappa^(1/4)>=4096>3000支付求和首尾；a>=K/8及Psi缩放支付最后比较。此为SUBDOMAIN内的actual无故障量化下界，不是自由误差或统计lower。

同域内T<=2^-40 K²/lambda<=2^-40 Psi(K^4/lambda)，所以UPPER再给R_K<=129Psi(K^4/lambda)。该域非空：选择任意对齐M>=2^178 K a^8，h=h0、g=ceil(log2(M a^4 2^48))，即有a^4 2^48<=lambda<2a^4 2^48及全部原DOMAIN条件，并满足SUBDOMAIN的大样本条件。其source只按公开K、M选取，每次实验内仍齐次。

## 7. 可检验的新推论：全域upper不能将K指数统一降到4以下

这不是全域lower，而是上述非空子域对“更好upper”的限制。令K->infinity，每K选择上一节的对齐M>=2^178 K a^8及合法g，则

    2^48<=kappa<2^49，
    T<=2^-89 K²/a^4->0，
    R_K>=2^-40 ln(kappa)/kappa>2^-90.

对任意固定p<4及有限绝对常数C3，K^p/lambda<=2^-48 K^p/a^4->0。于是Psi(C3K^p/lambda)->0。故不存在同时覆盖这些合法参数的统一upper

    R_K<=C1 T+C2 Psi(C3 K^p/lambda)，p<4，

其中C1、C2、C3均为参数无关有限常数。这排除了这种特定形状的降K指数上界；未排除带不同统计项、不同参数限制或不同函数的其它更精细上界。它也没有补齐低kappa、非对齐M或截断饱和区的源级下界。该推论连同本报告仍为未接纳讨论，不能登记为新Fact。

## 8. 全域冻结决定、精确方法缺口和解除条件

全域联合K匹配目前NO-GO；不是因为clock无法嵌入。完整有限字母、合法shift、等长连接、公开终端相位、完整观察律和joint head identities均已有有效机制。当前真正限制来自把实际随机计数替为均值以稳定三个floor，其支付式准确为

    3a w lambda/(beta²M)，beta=10^-6.

离开浓缩条件，该上界可超过1；这时证明没有给出同时stable floors的正概率，不能继续沿用Gamma>0。此为方法证书失效，不是实际floor一定失败或目标反例。

Counter找到更强的准确方法见证：取K=22、a=4、L=21、n=17，

    M=1152921504741064714，m=54901024035288795，
    h=h0=62，b=61，g=122，G=2^122.

这里M=(m+1)L-2，h,g满足全部原DOMAIN，kappa>=2^48；w=lambda n/(a²M)满足4<w<5<sqrt(kappa)/1000。对同一真实格点，令D0=19547470530800013320611715034351497，则准确相位为

    r=1221717167454045059705295640276353/D0，
    z=15882320162268127830723320058401607/D0，
    H=13438885827360037711312728777848901/D0.

直接有理比较给rho<=r<=1/4、rho<=z<=1-rho、H>=1/16，所以这是好相位格点，不是删掉的端点或不合法历史。可是R_i与C_j为整数，其比较均值为n/a=17/4，距最近整数1/4；均值浓缩容差为

    beta M/lambda
      =332306999023600226450399155583975449
         /1329227995784915872903807060280344576000000
      <1/4.

因此P(E_n|n,current query)=0准确成立，对所有terminal query均如此。该配置在SUBDOMAIN的大样本条件之外，并不反驳Prover保留条件的PARTIAL-LOWER；它证明“仅好相位+原DOMAIN+高kappa便沿用同一E_n正概率”是错误扩域。也没有据此断言实际Gamma总是非正或真实风险低于候选。修复须限制参数域，或直接分析实际整数计数的联合phase；仅在此处继续用均值替代无法成立。

甚至只对这一浓缩步骤，整个w窗口的一个更直接充分条件是

    M>=6a Wmax lambda/beta²
      =6 lambda^(3/2)/(1000 beta² a)，

保证失败概率<=1/2。这比2^80 K lambda²宽松，但只是单项支付；尚未把端点、rounding、K质量、horizon和饱和区全部重新组合成扩域定理，本报告不声称完成该扩域。

解除全域障碍需明确保留terminal选择的相关行/列/交叉计数phase论证，或覆盖所缺区域的另一个合法源；还需任意horizon的精确初始相位/同长连接、小K及低kappa/饱和范围的有限证明。UC上界、MM5统计下界和任意HEAD误差模型都不能替代这些责任。

若下一轮获授权，已有依据冻结“全域AGG/UPPER + 明确SUBDOMAIN真实源lower”的完整部分定理并走正常网关；没有依据把它扩大为全域min(1,T+Psi(K^4/lambda))匹配。该决定与既有failure f557ceba3e8d54defd029041857c535baf2130460e4013afb265d2d296affa72一致；本轮只对新增的好格点空事件反例登记精确方法诊断，不重复登记其它既有缺口。

## 9. 核验、证据不确定性与执行边界

Counter额外作了六条小型完整clock历史的精确结构检查（a=4、5，m=5，n=0、1、3），核对所有transition支持、M+2个观察符号、末query、实际J、A质量，以及三种完整score weight的符号系数。未给weights赋自由误差，也未把这些小M历史当SUBDOMAIN风险见证。另以有理数复算6项常数裕量均为正。它们只核bookkeeping；全参数结论依赖上面的有限推导，不依赖枚举外推、浮点风险或连续模拟。

本次为有界人工数学核查，不是形式化证明系统；Prover诊断、源构造与本报告都没有接纳Evidence。现有PASS/VALID仅指本报告明确列出的023与016前驱。027保持OPEN，未submit、新Fact/Evidence均0。既有方法缺口为诊断记录，不是LLM_CHECKED_PROOF。

同一023程序、实际u及主dense/uncached费用保持：全n位置、六heads、QKV、mask、input/query/endpoint、完整products/remainders、guards、holds/copy/clear、输出、offline全格式和逐phase总peak均收费。clock是数据源规律；聚合计数是分析对象，不是新decoder输入、免费cache或历史重读。[Non-scientific operational metadata omitted.]

[Non-scientific operational metadata omitted.]单个子域进展不宣告v10母目标解决。

