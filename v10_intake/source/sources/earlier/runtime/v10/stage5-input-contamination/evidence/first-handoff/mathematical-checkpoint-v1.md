# 第五阶段首个数学 checkpoint

2026-10-26。当前 root `881d17365a7019add4410343d568625dacae67d26aa17548bda2de7f9b860dbb`；contract `873515c4586d37a2bde324010bea6ae30f820927b7c25ded15b784a79eef7e45`。本文是 Lead 的具体推导核对及最小证明依赖清单，不是 Fact 或 Evidence。源 SCOPED PASS `3a35311ecb0bcb0567a1b14f2aa245ab0570986229663d71064bc46921ad64fd` 只作来源；所有承重命题仍须当前项目正常 gateway。

当前只维持两个数学方面：(I) robust upper/实际程序（C1 后 C3）；(II) full-Z common-channel lower/强基线（C2）。本地来源均在 inputs/source-stage4；没有访问旧 campaign、复审旧根或改变旧 SUSP。

## 1. 上界的完整衔接及需要重新承担的 clean 前提

记 m=floor(N/2), M=m-2, alpha=3k+1。C_sc,D_s 是真实 clean prefix 的证明变量，C'_sc,D'_s 是算法从 Z 得到的量。一次 flip 最多改变三个结束于 3..m 的 window；对每个 window，固定 triple indicator 和固定 row indicator 的变动均至多1。因此逐输入逐seed有

    |C'_sc-C_sc|<=3k, |D'_s-D_s|<=3k.

第二式独立计算 row indicator，不能从两个 count 界相加得到6k。令 v_c=(C_sc+1)/(D_s+2), v'_c=(C'_sc+alpha)/(D'_s+2alpha)，则

    C'_sc+alpha>=C_sc+1,
    D'_s+2alpha<=D_s+9k+2,
    v'_c>=gamma_s v_c, gamma_s=(D_s+2)/(D_s+9k+2).

对 f_[l,h](x)=min(h,max(l,x))，由单调性和 f(gamma*y)>=gamma*f(y) 得第一坐标比例；另一坐标用互补区间 [1-h,1-l] 得到同一比例。00 使用 [1/4,3/4]，10 对 next-zero 使用 [0,3/4]。故 dirty clipped r 与 clean clipped add-one a 的两个坐标均满足 r_sc>=gamma_s a_sc，从而路径上

    KL(p_s||r_s)<=KL(p_s||a_s)+log(1+9k/(D_s+2)).       (U1)

不需要 Z 是 Markov；通道甚至可根据实际 terminal pair 选择 edits。末pair逐seed保护，所以从 Z 选择的 row 正是真实 S_N；dirty E_m 不享有这种保护。

以下最小 clean 内容由当前 C1 自足证明承担，不可直接引用旧 Fact 状态：

1. D1 的 pi=(u,w,w,w), w=(1-u)/3, r=ut/w 满足 pi P=pi。reverse kernel

       R=[[1-t,0,t,0],[r,0,1-r,0],
          [0,1/2,0,1/2],[0,1/2,0,1/2]]

   满足 pi_i R(i,j)=pi_j P(j,i)。每个 R^3 row 在10有至少1/32共同原子，因此 TV(R^g(s,.),pi)<=d_g=(31/32)^floor(g/3)。令 g=N-m。stationary path telescoping 后，从 S_m 向过去的同一 kernel 产生整个 X_1^m，故

       TV(L(X_1^m|S_N=s),L(X_1^m))<=d_g.              (U2)

   此处没有除以 pi_s，没有改成独立 query，也没有仅比较 prefix endpoint。

2. forward 路径给 P^2(x,10)>=1/8, P^3(x,00)>=3u/32。对间隔 ell 的 visits，以 successive conditioning 得 E exp(-lambda sum I_j)<=(1-p+p exp(-lambda))^B；lambda=log2 给下尾 exp(-Bp/8)。于是

       P(D00<Mu/128)<=exp(-Mu/512), M>=6;
       P(D10<d_vis)<=exp(-M/256), M>=64,
       d_vis=floor(floor((M-1)/2)/16)>=M/128.

3. deterministic-horizon martingale Z_s=C_sc-p_sc D_s 满足 E Z_s²=p_sc(1-p_sc) M*pi_s。还需独立 row-stack 实现给固定整数 d 的事件包含

       {D>=d,C<p*d/2} subset {B_s(d)<p*d/2},

   从而概率<=exp(-p*d/8)。不得声称 C|D 是 binomial。原 clean 推导分好/坏事件并分别乘有效 KL cap，得到 K00<=50000/(1+Mu), K10<=400000/(M+1)。row10 的 successor r 可趋0，必须保留 stack 低success事件上的 logarithmic loss 处理。由(U2)、row00 cap log4、row10 cap log max(m,4)，再用 d_g<=2exp(-N/192)、M+1>=N/4，得到实际 terminal clean R_av(a)<=1000000/N。N3-5另用真实 uniform，不插入虚构 prefix。

若 k>=1 则 M>=1024，以上 visit tails 可用；good/bad 分割给

    E[1/(D00+2)]<=128/(Mu+256)+.5exp(-Mu/512)
                 <=512/(1+Mu),
    E[1/(D10+2)]<=128/(M+256)+.5exp(-M/256)
                 <=512/(M+1).

这两个函数范围为[0,1/2]，(U2) 只使各自 conditional expectation 增加至多 d_g/2。它不应用于 Z 或 seed。用真实权重 u,w、u+w<1/2、u/(1+Mu)<=1/(M+1)、d_g<=384/N，有

    sum_{s=00,10} pi_s E[1/(D_s+2)|S_N=s]
      <=8192/(3N)+96/N.

将 log(1+x)<=x 代入(U1)并平均得到

    R_av(r)<=1000000/N+25440k/N.                       (U3)

k=0 时(U1)额外项严格为0，不需要启用大 M tails。

对 Q>=4，00 nearest half-up 保持 q1 in[1/4,3/4] 且 |q1-r1|<=1/(2Q)。由 kl(p,q)<=(p-q)^2/[q(1-q)] 和 kl(p,r)>=2(p-r)^2，得

    kl(p00,q)<= (16/3)kl(p00,r)+8/(3Q²).

10 的 j_c=ceil((Q-1)z_c/Zden)，因为两个 ceiling 的未取整和为整数 Q-1，e=Q-j0-j1 in{0,1}，两个输出正且 q_c>=(1-1/Q)r_c。因此 kl(p10,q)<=kl(p10,r)+2/Q。共同乘16/3后，(U3)变成

    R_av<=16000000/(3N)+135680k/N+3/Q.

Q2 为 uniform，loss<=log2；N3-5 同样真实无prefix。zero counts 因 alpha>=1 有定义；00 的 Q4 ties 向上；10 的 Q-1 与 Zden-1 必须保留 literal1。

## 2. 完整 reverse history 到一张共同 kernel

令 H=N-2，A_j=S_(N-j), 0<=j<=H。在真实条件 S_N=00 下，stationary reverse path identity 给从 A_0=00 出发的完整 R_t 路径。每个 free symbol X_i 是 A_(N-i-1) 的第一坐标，包含 X1。两条公共 witness laws 使用 u0=k/N、t±=1/2±Delta/2、Delta=1/640000；它们不是算法输入，也不在 runtime 选择源标签。

对 R±，三步到10的路径质量分别至少 t(1-r)/2,(1-r)^2/2,(1-r)/4,(1-r)/4，均>=1/32。令 rho=31/32，D_j=rho^floor(j/3)，sum_j D_j=96。逐row TV 差 h=(Delta,(u/w)Delta,0,0)，0<=h<=Delta，pi h=2uDelta。

matched decision boundary 使用 maximal 一步 coupling，出生概率 h(s)。mismatched boundary 预先承诺三步：以1/32把两个 endpoints共同置10，其余从各自三步 residual分布抽；给定 endpoint e，链内两中间pair按

    R(a,v1)R(v1,v2)R(v2,e)/R^3(a,e)

抽取。故整段个体边缘恰为真实Markov三步段。剩余不足三步时仍抽完整段再截取prefix。内部意外相遇不改变已承诺长度。

自适应边界的证明要保留：对固定 j，按最后block起点和该起点已决定的长度分割；事件在起点可测。给定 joint past at start 后，单条block边缘是真实Markov。再只条件化这条链的block prefix，积分joint起点过去并对分割求和，得到该链 E[f(A_(j+1))|A_0..A_j]=R f(A_j)。不能对两链中间历史都条件化再断言Markov。该论证同时处理最后截断段。

一次birth后每次恢复尝试的条件失败率<=31/32，尝试次数期望<=32，末partial block过量计3。每episode charged pair positions期望<=1+3*32=97。无需episode独立。丢掉matched-boundary indicator后，birth期望<=E h(A_j^+)<=2uDelta+Delta D_j，因此

    E pair disagreements<=97(2Nu+96)Delta,
    E Hamming(X+,X-)<=97(2Nu+96)Delta
                     <=10000(1+Nu)Delta.               (L1)

这是两条真实完整条件history laws P,Q的一个coupling费用，不是skeleton/count/population费用。

取其off-diagonal flow f，divergence=P-Q=mu。逐正cycle减最小边，保divergence且不增费；所得DAG加source->x容量mu_+(x)、y->sink容量mu_-(y)，沿正path分解并按三角不等式collapse。所得Gamma marginals是未归一化mu_+,mu_-，质量tau=TV(P,Q)，cost(Gamma)<=cost(f)。不能归一化后遗漏tau，也不能把原coupling直接限于正负支持。

每个 d(x,y)<=2k 的good edge选同一显式Hamming midpoint z_xy；距两端均<=k。正row x按Gamma(x,y)/mu_+(x)，负row y按Gamma(x,y)/mu_-(y)归一化；good fraction送同一个midpoint，bad fraction留其自身；mu=0 row identity。这定义单一input-row kernel K，不根据实际源标签选择。两个源共有质量min(P,Q)经过同一个K自动线性相消：

    (P-Q)K=sum_bad Gamma(x,y)(delta_x-delta_y),
    TV(PK,QK)<=bad mass<=cost(Gamma)/(2k).             (L2)

所有概率有理；有限rows取共同分母D，用独立均匀J in{0,...,D-1}按每row固定分区实现。每input/每seed输出在硬k球内；其他terminal fiber全用identity。外部channel计算无限制，未计入predictor。对u0=k/N，(L1)费用<=10000(1+k)Delta=(1+k)/64<=k/32，故(L2)<=1/64。T只由公开N,k构造，与Q、predictor、实际label无关，并在所有其他D1源产生的输入上合法。

任何共同full-Z randomized predictor加fresh private coins不会增大TV。以q1在1/2的阈值测试，错误时|q1-t|>=Delta/2，KL>=Delta²/2（输出端点允许无穷损失）。两错误和>=63/64，因此一个同一t_*有

    R00 >=(Delta²/4)(63/64)>=Delta²/8=c,
    R_av>=Pr(S_N=00) R00=(k/N)R00>=ck/N.

这不是每源都坏，不是逐seed小TV，不是无条件TV，不推出确定性共同通道达到。C1适用于这同一T；对任一具体实现的同一source witness同时成立。

## 3. D4/D5 一一对应及新证据最小 finite 接口

以下核对的是固定D5坐标；没有以另一个更大上包络替换。当前 C3 必须自证 primitive、compiler、frontend和各字段liveness，源文中的“admitted”不构成这里的前驱。

| 固定坐标 | 具体实现与必须承担的论证 |
|---|---|
| s=ell+b+tau+p+32（small N去p），beta=128s，g=1024beta² | b任意大时整个JOINT frontend也用beta宽；整数primitive给bit gates/步骤，MUL保全2beta乘积，DIV保全numerator/quotient及beta+1 shifted remainder，再用range cast；scratch<=32beta+32。 |
| D3 closed box | 独立C0,C1 in[0,M]给D<=3m,Zden<=12m，nearest dividend<=24mQ<32mQ，ceil dividend<12mQ。Q2 discarded候选仍定义；residual0/1及所有SUB非负。 |
| JOINT17+46 / DIRECT8+46 | JOINT六MUX、exact snapping和两OR；DIRECT六MUX两OR；46表新增5项形成k,2k,3k,alpha,2alpha，仅三个平滑operand变更；CONST0/2仍付费，Q-1及Zden-1仍literal1。 |
| DIRECT G=(512n+2048)g, core=G | 先拥有全Z batch，再每eligible triple遍历八label，显式feature和increment；acquisition循环/输入/endpoint另于54项收费。神经坐标E,L,W,dense_slots,P_bits,mask_bits,I_holds全0，但packed bit内存非免费。 |
| DIRECT W_work=8N+8192beta+Z_meta | 输入和副本、八counter、54结果、完整乘积/余数、控制器、port、先前numerator与清零同时存活。 |
| JOINT frontend132, W=2048beta | 128构造层加四extraction/clear phases；四singleton bindings加一zero-score uniform head，总5、最多同时4、value8、QK<=4、score0。j=floor(A R_s C/(M R_s))，11显式零words；实际Z snapping精确。所有Boolean scalar仍各beta物理位。 |
| JOINT G=64g+256*19(h+1)+8192beta+128(b+1), L=16G+96 | 63算术项及一整primitive余量、19 words读bits、控制/初始化/复制/清零/输出；自证16G+32 Boolean-to-dense compiler，保留64层接口余量。不得凭Python int操作单价。 |
| JOINT E=512n²+16nW+256W+1024(h+b+ell+tau+1) | zero-score evaluator所有循环；全batch四bank扫描/迁移/清除；query重复和清零；端点/public/serialization。E按word bundles另乘g，非神经层数。 |
| JOINT dense_slots=(132+L)(W+1)², P_bits=dense_slots*beta | 每零系数、identity和bias均存储/求值；frontend在n位置执行，query算术在1位置执行，不能偷换成全程streaming。 |
| mask_bits=4n²+(m+1)², I_holds=132nW+LW | 全mask含零entry；所有实际live fields保留hold并付费。 |
| JOINT core=256(132n+L)(W+1)²beta²+E*g, W_work=4nWbeta+Z_meta | 完整dense MAC、四批bank、head累加、query duplicates、scratch/controller/port，加metadata working copy；先付全batch，再实际擦除source-bearing非query状态后release。 |
| small N G=(128(N+1)+512)g, core=G | 仅packed uniform，实际读N位；E,L,W,neural/dense/masks/holds全0，W_work同DIRECT，不生成prefix或虚构第六input。 |
| Z_meta=1024ns | 两份每token至多64 records*8s位，均public；dirty bits/counts/endpoints不能塞入public metadata。 |
| a=beta+bitlength(G+E+Z_meta+N+L+1)+32 | segmented runtime bank/token/channel/layer/column/bit fields；全位地址算术、fetch、dispatch均收费。 |
| K_code=4096*g*(beta+a)+4096*(s+1)*(beta+a)² | g在此为1024beta²这个数。至多24 primitive类型、每类<=g wiring records、每record<=64(beta+a)位，以及<512条SSA/phase/loop descriptors、全部literal与padding。 |
| U_stored=P_bits+mask_bits+Z_meta+K_code; T_online=4096(a+beta)²core; peak_online=U_stored+W_work | controller/地址/fetch的完整bit费用及stored+working同时峰值，不能漏先前副本。 |
| a_gen=beta+bitlength(U_stored+T_online+N+L+1)+s+32; Emit=U_stored+L+1024 | 独立flat generator地址；primitive wiring、新SSA、loops、masks、dense zeros、metadata/code padding及port全部有限枚举。 |
| T_gen=1024s²+4096Emit*a_gen²; W_gen=64a_gen+64Emit*a_gen; peak_gen=U_stored+W_gen | 每emitted bit/delimiter的有限counter运算；已生成program与working同时保留；不需实际materialize巨网表，但需要明确生成规则及计数。 |
| output=3(b+1), GPU=0 | fresh port按LSB-first写out0,out1,Q，正numerators和为Q；扫描清除除该port外全部source-bearing input/endpoints/controls/scratch/copies。 |

上表源自D5和固定012证书逐项核对，尚非新C3成本证书。待证最小finite接口为：exact arithmetic wiring+scratch；Boolean rolling-state dense compiler+holds；causal lag/triple/singleton/uniform有限frontend；物理banks的allocate/copy/erase/release；显式public code及runtime/generator地址解释器。这些可以直接内联C3，毋需导入旧风险/成本包。

## 4. 当前原生证据与下一依赖

本checkpoint时新Fact IDs=[]，新Evidence IDs=[]。当前原生proposal route `2ff059747c1b1bf8519464a584238cf32f2b97a79d5bbb9c957274cfdfebc2df`，C1义务 `b5f118d33a9d9687ac8e3d48ca7df6e5c0403aeba52c026d88087e385e813354`，C2义务 `52a14a0c60279133c7acc7067c15eb4cfbff32368f8a721e59df9bf3eecd9ff1`，C3义务 `c9d1bbb51ee633f91f029e917ded7f6e1de7f6e9e227f681761ee9ed66b81bec`。Prover首单C1，Counter首单C2；Lead收到真实gateway回包后读Fact/Evidence及正确前驱，再接C3、固定独立review和根C4。

[Non-scientific operational metadata omitted.]当前policy只GPU有限为0，其余unlimited。该记录不是已运行audit。

最终handoff必须区分实际native/cold audit和尚未发生的receiver pull。母题尚需T1/T2/T3综合，本合同既不建立JOINT统计/资源优越性，也不建立1/N、1/Q匹配下界、完整conditional分类、确定性attack、逐时sensor、IEEE/训练或发表新颖性。强DIRECT与JOINT每Z同输出，分别成本不可称同预算。CGR iid Huber、Pydi/Jog class maps/transport/submeasure保留为既有工具；dependent整段可作一个feature。
