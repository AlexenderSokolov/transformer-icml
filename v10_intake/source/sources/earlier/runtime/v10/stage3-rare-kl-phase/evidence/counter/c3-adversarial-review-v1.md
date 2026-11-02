# C3 首次实际对抗审查：固定 v1

Counter，2026-10-25。精确义务：
`c82d400c69019a551db29a66e99faec5bfbf281097c5c8ae57075ea5789772fb`。
这是新工作项的文件级审查，不是旧挂起任务的恢复，不是独立 Verifier 或 native admission。

**结论：声明的名义有限算术及各自成本模型内，未发现强制修补的承重错误。
给予 scoped PASS，可供后续独立固定版本审查。完整有限电路存在性来自路径恒等式、
误差推导和显式 compiler，而非诊断实例。本报告不接纳 C3/C4 或 root。**

已逐节读完主证明及嵌入附录 A–K，并读 ledger、certificate 全部四个实例、IR、
展开指令表、code audit、诊断代码/结果及 Lead review。24个指定输入 pin 均复核；
附录与单独 ledger 字节完全一致。旧 source 文件仅作 hash 核对，不执行其诊断。

| 固定输入 | SHA256 |
|---|---|
| prover/c3-proof-v1.md | 68dcb797dfe0e2103d2f35034311efa97d9ae496dedf4eafc67c600b34a8679c |
| prover/c3-resource-ledger-v1.md | c00336780dfb8e7cfcdad1ffc2542d8319508b1fdf40f278dcf1960c0105076c |
| prover/c3-resource-certificate-v1.json | 2a5aa300d24cebebc8006f2f4ced9ad4fa00f07f562e5d9eb697c534c5765125 |
| prover/c3-code-audit-v1.md | 5648f1bc74b43d44f7597ae055190e41d21413d207049ec59601210211334ee6 |
| lead/c3-review-v1.md | e8665348447fb61abac0f263d820d79c50aaf967bbef0972af392c83d50202a0 |

## 1. 因果信息链及有限误差链

| 部分 | 本次核验及适用边界 |
|---|---|
| 真实 query 与前缀 | 主证明§2：物理 query 位于 N+1；四个付费 singleton heads 在该处分别读 m,m-1,N,N-1。E_m来自前两头，S_N来自后两头。crop发生在绑定之后，buffer地址m+1不改变物理时间。 |
| 样本及许可信息 | 第二层 query 的 keys 恰为3..m；合成 query和tail均不采样。值为观测位、局部lag与公开初始flag的函数。19个统计masters、S_N/E_m的8个one-hot位及公开metadata是恢复器的全部输入；没有下一步符号、免费count表或raw-history decoder边。 |
| 四头代数 | §3：(4)识别source pair及initial flag；(5)的source/successor pair telescoping保留初始pair与E_m。两product heads的展开消去successor marginal/lag2-successor项，得(7)的选中triple frequency。对M=1、零行均成立，不用stationarity。 |
| 有限log/exp | §4：共同分母逐项整除，最后一次floor；log3保留p+1位。系数误差<2δ，score误差<=4δ。8p项recurrence完整乘积后才DIV；每次截断向后累计最多8δ，权重误差<=100pδ。 |
| masters | 非空行的分母至少key数；归一化比值误差<=200pδ，再加一次<1/Q_A floor。p>=4h+64使总误差<=2/Q_A，闭端点0、1包括在内。Singleton bit copies精确。 |
| signed恢复 | §5表逐项由triangle inequality成立；normalizer分母在[Q_A,2Q_A]。35η+6ζ=76/Q_A，不要求heads误差独立。任意闭网格输入下g∈[-3,4]、H∈[-8,9]，[-16,16] guard足够。SUB保持符号至clip，不把负值提前送入unsigned截断。 |
| grid与snap | §6从bit h开始，包括H=2^h；整数输入下ReLU差恰为bit，不是连续实数floor。76M/Q_A<=76/256<1/2给严格半计数半径，故两个counts逐路径精确恢复。非名义closed-grid输入只保证各count∈[0,M]，读出据此容许D<=2M。 |

上述推导没有 source-stage C1/count-snap Fact 前提。C3证明的是确定输出函数，
不是继承一个未接纳的统计 theorem；后续风险结论仍须保持 C1/C2 自己的 native 依赖。

## 2. 完整指令表、Boolean/ReLU compiler 和输出

恢复表确为19个共享操作加每坐标22项，共63；输出表41项。展开JSON与IR完全一致，
无重复结果名或use-before-definition。恢复的边界mux以 e0==b、e1==c 判定 E_m；
normalizer、四个product/DIV、signed差、clip及snap均与公式逐项对应。

输出表同时算两候选后mux：a选row00/10，末位b或公开small/Q2 flag强制uniform。
所有候选的除数Z、2Z都正；Q=2时一个未选nearest候选允许为0，最终输出仍为uniform。
N<6不执行M<=0恢复，而以zero counts进入合法常数读出。零counts、Q4、两端、
half-up ties和row10 residual1均未改变；canonical坐标及coordinate1 residual保持。

附录A给出的primitive不是unit-cost word oracle。对w>=2，表中最大原始多项式
不超过512w²；再给sign/scratch双倍余量仍在g(w)=1024w²内。
完整product保留2w位；DIV扫描至多2w dividend bits，保留w+1 shifted remainder，
以prefix=q*d+r、0<=r<d的不变式证明精确商余。所列scratch银行相加为
18w+10以下，受32w+32覆盖；operands/results另在named banks内保留。

AND/NOT/XOR/OR的ReLU恒等式在所有bit输入成立，四层与四个临时通道可实现；
采用factor16后还留出two-rail/boundary余量，并逐层支付其他live channels的identity。
WF=1024B、WO=1024O显著超过保留全部named words、双轨、scratch、metadata及
grid expansion的512B/512O上界，未依赖未证明的最优寄存器分配。

B=128p覆盖score、完整实际乘积、aggregation、normalizer、signed guard与snap；
输出独立采用O=32v，避免把任意b塞入固定N的frontend字长。读出largest dividend
<16mQ、完整2v product和v+1 remainder均受覆盖；旧8mQ界没有被重新使用。

**输出确有收费。**附录D明确容纳两项b+1 guarded numerator words和literal Q的
b+1位，即一种完整固定接口为3(b+1)位；只发两numerators且Q公开时为2(b+1)位。
G_O额外1024O覆盖copy/write/erase和可选两行dyadic decoding，参数/metadata也收费。
这与另行审查的C2紧凑b位端口是不同编码约定，不应混称同一emitted-bit count。
指数b的替代端口若采用自描述header，应固定协议并收费；例如gamma(b)只需
2 floor(log2 b)+1位，仍在现有O与Z0余量内。literal-Q固定接口本身已足够支撑存在性，
没有把任意未指定header或第二坐标视为免费。

## 3. 各成本域分别核验

附录E的公开loops足以支付adapter、QKV、mask扫描、每edge的8p次exp迭代和精确
aggregation；E=(256p+512)n²+1024n、T_A=E*g(B)不藏exact softmax/log/exp。
它与neural层数是不同量；不将attention内部bit steps伪装成两个Boolean层。

| 声明模型 | 对应式及本次结论 |
|---|---|
| hybrid、phase-shaped token/query dense | (A7)–(A12)：P0前段包含n个token，恢复/输出阶段允许付费query extraction。I计每个实际保留通道；D/P_D计每层矩阵全部零系数。跨宽度过渡有32层余量，不要求b相关字全程留在frontend。T_dense还过收unused rows的执行。 |
| sparse neural | (A9)–(A11)及F补充式：P_S包含arithmetic、identities、coefficients和addresses；在线式也执行I项identity。不能借shared register machine“不变寄存器不需逐步复制”的廉价列。 |
| shared addressed word program | (A13)与S_shared：读写word和其public address按长度收费；arithmetic由A展开。B/O两个primitive libraries、两条完整指令表、loop/dispatch、mask/metadata均存储。此处是明确register-memory模型，不是任意indexed access的免费神经电路。 |
| padded token batch | (A14)：所有n个token、全部phase取最大width/word，holds=L_H*n*W，mask=8n²；stored code与working、peak分别相加。保留input和unused slots，未沿用抽取后的低保持量。 |
| global dense batch | (A15)：总width=nW，matrix按整个batch vector平方收费，含block zeros和cross-token routing；不是把per-token W当全网络width。 |
| fully flattened Boolean/ReLU | (A16)–(A17)：T_F展开所有T_A、恢复、读出及输入操作；S_F保留全银行。TF*SF identities、TF*(SF+1)² dense slots、稀疏程序/地址、rolling及peak均单列。没有拿hybrid少层数与flattened无primitive混合。 |
| sequential eight-counter | (A20)、J：收费消费全部N个符号，仅3..m更新；最后以真实末pair选行。count live width是W_C，另加同一41项output phase、32 boundary layers、b相关存储与成本。 |
| one-shot eight-counter batch | (A21)、J：W_CB=W_C+2N+2ell，整份未消费history银行在count各层保留，所有holds、dense slots、stored/work/online式均替换该width。不是仅加静态2N bits后仍引用streaming width。 |

所有模型均显式加入M0或8n² masks、Z0或Z_base positions/routing/interface metadata；
rolling work与stored program相加才是online peak。Hybrid/shared的finite-evaluator code
K0可复用，但每次执行仍付T_A/相应addressed cost；flattened则复制展开全部算术。
输入history驻留、copy/erase、holds与address fields未被删掉。

附录I的共同分母生成是有限整数程序：odd-factor product、q-power、逐项精确DIV、
求和及最终R-scaled DIV可置于32p+64 word envelope。D_q的位数O(p log p)，
B_log=8p²+32覆盖全部实际full products与scaled numerator；T_log/W_log收费。
布局生成(A19)按所选完整stored bits U及depth Dlen枚举，包括全部dense zeros、
holds、masks、positions和地址；generation peak为U+W_gen。该函数在各格式独立代入，
不表示巨大布局已经物化，也不声称最优复杂度。

## 4. 强基线、保留失败及审查限度

基线的eight-counter invariant随arrival归纳；恢复器由有限路径代数与strict snap
恢复同一selected counts，之后共用41项读出。因此所有路径的最终numerators一致，
而不只是几个fixture一致。两种输入域都保留，八计数器属于合法强比较器。
输出相同只转移风险，不证明对优化baseline的逐项预算支配或神经优势。

所有原失败保留。尤其10001110的正确counts(1,0)、错误端点counts(2,0)仍不同；
closed endpoint需要h+1位；half-count tie不能把strict改成nonstrict；
N16,m8,Q4,C0=C1=6的nearest dividend280仍反驳旧8mQ=256，而受16mQ=512覆盖。
这些是指定错误扩张的反例，不是当前构造的下界或噪声可靠性保证。

本次新检查只核对24 pins、附录一致、63/41结构、Boolean gate truth tables、
primitive多项式和五个读出边界fixture，并重新求值certificate四个给定参数实例。
结果均PASS，见c3-structural-checks-v1.json。没有重跑旧diagnostic main或写入Prover文件。
有限实例不能证明全N,b；本报告的全称判断依赖上面的构造、归纳和不等式审查。

Lead固定review的旧任务号、旧排队状态及“五个义务OPEN”属于其写作时记录，不能
当作本轮操作指令或当前状态。本轮未调用ask、submit、schedule、continue或final_audit；
未恢复/编辑旧task[redacted routing identifier]、四条SUSPENDED或protection counts。

当前Euler readback：C1 DISCHARGED，既有Fact `e418ec34b7dbc4a6`、Evidence
`4857f1b1b5d10ab74a979362e3d0c3068c9634016e4ce6b6a0609ed577eb2eea`；
C2、C3、C4及root仍OPEN，acceptance=null。此C3确定性证明不以C1/C2风险定理为前提。
本次新Fact IDs=[]、新Evidence IDs=[]。未发现新障碍，不另造重复failure或改变图状态。
[Non-scientific operational metadata omitted.]LIMITED0及原显式final-audit预留保留。无新检索、原campaign访问或旧源改写。
后续独立Verifier仍须审查完整固定包；这份discussion PASS不代替正常truth gateway。
