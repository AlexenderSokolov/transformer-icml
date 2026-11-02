# C4-integration-012：两篇原始文献的有界定理级比较，Counter v1

这是同一 root 的 review，不是新义务、旧证明重投或 Fact。原生 state 中 root 仍 OPEN。已接纳的 Fact276fa450421a1a95、Facta08ed3def2c2da35 只按原内容用于比较；文件哈希与 VALID/PASS evidence 匹配，见 existing-evidence-audit.json。[Non-scientific operational metadata omitted.]未调用 submit_proof/final_audit。[Non-scientific operational metadata omitted.]

**建议选择 (b)：目前可稳妥定位为标准统计/数值工具在一个严格接口上的专门化与实现整合；尚不足以据此确认一个有科学分量的新中心贡献。** 两文没有逐项直接给出已接纳 T123 的完整链条，但“未直接蕴含”不等于新颖。下面保留确实不相同的技术内容，也列出不能略去的已有覆盖。这是科学价值判断，不撤销任何数学接纳，不作全领域优先权判断。

## 1. 身份、版本和实际比较对象

| 原始来源 | 核定身份/版本 | 已冻结原件 |
|---|---|---|
| [Ekbote 等，What One Cannot, Two Can](https://arxiv.org/abs/2508.07208v2) | Chanakya Ekbote、Marco Bondaschi、Nived Rajaraman、Jason D. Lee、Michael Gastpar、Ashok Vardhan Makkuva、Paul Pu Liang；2508.07208v2，2025-11-14修订；原件标 NeurIPS2025 | versioned abs/HTML、74页PDF、TeX archive与解包文本 |
| [Kavian–Zaidi–Sefidgaran](https://arxiv.org/abs/2609.34731v1) | Masoud Kavian、Abdellatif Zaidi、Milad Sefidgaran；Information-Theoretic Analysis of Next-Token Prediction under Markovian Data，2609.34731v1，2026-09-28提交 | versioned abs/HTML、PDF、TeX archive与主TeX |

八次官方 GET 均返回200，URL、UTC、原始字节SHA256及30个解包可读源文件哈希保存在 sources/retrieval-receipt.json。源码只读取，未执行。Ekbote 的网页转换漏掉 boxed theorem；定理编号/正文用 PDF 与 TeX 交叉核对，不能把网页空白当作没有定理。原始 main .tex 的 PDF 页号口径与网页行号明确分开，定位见 passage-index.md。

本地 novelty-map 的这两篇题名、作者归属与日期大体相符，无需制造身份错误；本轮补充固定 Ekbote v2。该 map 的概述不能替代原文：Ekbote 的参数位精度声明和附录 C 的新核泛化 Theorem8 必须纳入；Kavian 已处理轨迹内依赖，不能受前轮 iid-sensor 直接替换障碍的误伤。map 未被编辑。

当前中心候选严格按 Facta08 理解：一份 expanded E_R + canonical floor/erasure 的有限码 A 家族；固定名义 beta；完整 aggregate/query/terminal/public/descendant 观察且 cut 后无历史重读；D1 每固定 theta 的一致性；D5 聚合替换后再 floor 的真实 TV 下/上界；强 direct correction 理想相等；同一巨大但显式增长的 cap 内，S_N=2^floor(log2 M) 的物理绝对误差恢复。它没有承诺固定总预算、效率、任意架构最优性、任意位翻转容错或新统计最优率。

为防止口径漂移，本次比较使用 Facta08 §5–6 的**替换再floor**模型：
- 共享八edge事件坏概率 <=16 exp(-M h^2/289)，真实终端条件坏概率再除 pi_s。
- 在其非空条件(19)–(20)下，rare conditional 的上下尺度为 delta/v，真实实际平均为 delta；上界常数分别24(c+1)、80(c+1)，不是旧parent的12/40。
- lower 的 actual average 对每一参数先作平稳加权再最大化，保留00和10的贡献；不是独立query替换。
- §7 floor-only lower 有另行的 phase/sample条件，不能与该任意b的物理替换 lower 混同。
- §8 的纯floor恒等式与完整码等价要匹配有效网格 b+k；固定物理绝对delta的缩放比较才有不同的误差类。S=M 仅在M为相应二次幂时成立。

这些是现有已接纳内容的定位，不在本轮重证。

## 2. Ekbote：应承认的覆盖及七维表

精确来源：[v2 §2/4/5、Appendices B/C/D/H/I](https://arxiv.org/html/2508.07208v2)，PDF Theorem3 在第7页，Theorem8 在第34页。E1–E8的原文锚点见索引。

Theorem3 的目标是 conditional k-gram：两attention层、每层一头、embedding6S+3。Remark2给参数数
9(6S+3)^2+(6S+3)(2T+2S+9)，并**明确报告**
Omega(log T+k) 每参数位数足够达到 O(1/T) 加性逼近；这里按原文的“足够”措辞记录，不改成精度必要性。Appendix B 的 clean 三MLP构造用 triadic context、ReLU/LN、residual与 kappa->infinity 的匹配；另一个两MLP版本保留 early-position contamination，并讨论其在不可约源下的消失。

主文 Theorem4/附录 Theorem7 分析受限训练；附录 **Theorem8 还声明新一阶核的归纳泛化**，显示
sup_y |f_hatθ(s_0:n)_y - pi_tilde(y|s_n)| ≲ log(n+1)/(n+1)^(c gamma)。
C.3 把该证明转引 Nichani H.4/Theorem4.5，本轮没有追读该外部证明。所读显示未明确给出这个随机新序列不等式的概率/期望量词，故不把它自行加强为逐路径或本项目条件TV定理。

| 维度 | 已核原文内容 | 对当前中心候选的直接覆盖/缺口（本次推断） |
|---|---|---|
| 对象 | 任意阶条件经验频数；C还声称新一阶核泛化 | k=2直接覆盖经验条件行这个对象；“浅层能用历史估计Markov规律”已不是可独占贡献。项目平滑参考及零count行为需另接。 |
| 信息 | 输入完整有序序列，网络形成triadic当前/过去context | 未指定项目的 erased q/r/mu 完整码cut；不允许把它的全序列权限直接授给cut后decoder。 |
| 架构 | 2 attention层/每层1头，MLP/LN/相对位置/residual | 项目不能宣称更浅或更少头；其固定score有限后端与ReLU校正需逐算子编译，不由此架构名词自动获得。 |
| 量词 | 表示构造广；训练C是一阶、特定prior/初始化/冻结参数；D另有二阶及更高阶假设 | C要求共同gamma正下界等；D的binary strict preference被D5直接违反。不能把受限训练定理视为全D1前向族，也不能忽略Theorem8。 |
| 资源 | 有参数数、显式每参数精度、H.4量化权重/activations实验 | 不是项目完整寄存器/分母/flags/擦除/后端运算cap。已读构造用kappa极限，未提供本项目固定beta的误差校正链；这不否认其有限参数逼近声明。 |
| 风险 | 经验频数表达；prior平均CE训练；Theorem8目标核误差；H实验CE/attention-Frobenius | 有实质预测重叠，绝非仅“表示存在”。但所读陈述不直接给聚合绝对误差后D5的conditional/actual TV与全部endpoint副本的下界实验。 |
| 直接蕴含缺前提 | 原文定理的权限、算子、参数/统计量词应原样保留 | 需固定score替代kappa极限、零count/平滑、完整码factorization、该cut的有限N两过程重叠、同cap/同误差位置缩放与真实风险转换。不能把这些当一行参数替换。 |

直接代入检查有两项具体失败，而非泛称“设定不同”：
1. 把一般D1二阶源抬升为一阶pair源时，从(a,b)只能到(b,y)，其K^2乘K^2矩阵有结构零。因此不能用此抬升满足 C 的全entry min pi>=gamma/S>0。改造训练实验/允许稀疏支撑的不同证明仍可能，未被排除。
2. D 的binary second-order assumption 要 pi(1|11)>pi(1|01)，而D5两者恒等1/2。其更高阶条款也另加reversibility/谱条件，不是免费的一般D1适用定理。

相反，名义统计一致性这个宽泛方向并不形成有力差异：经验条件频数的表示，再加适当有限逼近与固定正源的联合计数强律，就会产生相应统计推论。项目准确不同之处在固定score与特定被损坏观察上的可恢复性，不在“又证明能表示条件频数”。此处是方法比较推断，不宣称已完成另一篇在D3下的同预算编译。

还有一个独立的源码算术诊断，必须保留但不能夸大。B中权重
att_i=3^(i-1)/sum_(j=0)^(k-1)3^j，Z=sum_(i=1)^k att_i 3^i，
按这些显示公式得到 Z=3(3^k+1)/4；源码却声称 Z=3^(k+1)/5。k=2两者为15/2和27/5，check_review.py已作有理核查。**这只标记一个标量公式不一致，不能据此宣称Theorem3被反驳。** 它进一步说明不能直接把该源码当作已完成的逐码backend移植；阈值/边界细节若用于新编译须独立修正核查。本轮没有替作者补整篇证明，也未把此诊断登记为新研究节点。

## 3. Kavian：主定理精确定向及七维表

精确来源：[v1 §II–IV](https://arxiv.org/html/2609.34731v1)，K1–K6定位见索引。将其N记为n_tr以区别项目的单历史长度N。其独立单位是n_tr条轨迹，每条长T；轨迹内有限记忆、可有时间依赖，模型看rho-token窗口。假设有界logit B和有界参数范数C。Theorem1为

    E gen(S,W)
      <= [2B(1+2rho)+log d] sqrt(tau_min I(S;W)/(2 n_tr T)).

这里 gen=L_population(W)-L_empirical(S,W)。Lemma1另给history-state mixing的改进；不能说该论文忽略context overlap。Theorem2把I换成在**期望generalization-gap distortion**限制下的率失真函数并加epsilon。Theorem4是具体范数受限attention类的margin gap，主量级

    O((C^2 rho / theta_margin)^2
           sqrt(tau_min log(rho d n_tr T)/(n_tr T))).

这里margin gap的定义是 L_(-theta_margin/2)(W)-Lhat_(theta_margin/2)(S,W)，两侧阈值并不相同。其compression在M4=M2^T M1与M3参数上作随机投影/加噪并控制期望margin distortion，非项目q/r/mu聚合后的统一绝对delta码替换。

| 维度 | 已核原文内容 | 对当前中心候选的直接覆盖/缺口（本次推断） |
|---|---|---|
| 对象 | 学得参数的population-minus-training CE或margin gap | 与真实条件律估计误差不是同一量；泛化gap界不提供小的excess loss或TV。 |
| 信息 | n_tr条独立轨迹，轨迹内相关/窗口重叠；可n_tr=1 | 不以“只有一条依赖历史”排除它。需区分参数W、其压缩物与推断时完整聚合观察。 |
| 架构 | 一般有界logit类；IV-C三矩阵attention的特化 | 一般式可容纳合适ICL映射的学习解释，但具体压缩特化不直接等于E_R+擦除+校正+全部残差的电路。 |
| 量词 | 针对满足B,C与mixing条件的算法/模型分布给期望gap上界 | 源是stationary时可在其模型内，但不因此得到本项目每固定theta无theta参数日程、一致性和对所有cut-decoder的两过程lower。 |
| 资源 | mutual information/期望distortion、投影维度、矩阵范数 | 未直接给有限有理分母/flags/scratch权限或逐操作word cap。不能把I、参数压缩率、summary小数b、全观察bit数互换。 |
| 风险 | 独立test轨迹上的平均CE gap；IV用margin gap | 项目conditional terminal TV与stationary actual TV仍需excess/calibration和endpoint-dependence桥梁；已读定理没有替代这个风险量。 |
| 直接蕴含缺前提 | 算法依赖、temporal mixing与有界性是其真实前提 | 需额外小training/excess loss、目标/模型对应、同历史终端风险转换、特定后聚合信道与码级factorization、动态范围/编码资源核对。 |

一个完全具体的不蕴含例子：在stationary iid Bernoulli(3/4)上，将其看成合法二阶D1，固定模型输出(1/2,1/2)，logits恒0。对每条训练或test轨迹，其每token CE都等于log2，所以 gen=0且I(S;W)=0；但在每个context及实际terminal的TV恒为1/4。所有概率严格正、有界性与有限mixing成立。这与Theorem1完全相容，说明即使把gap上界做到0仍缺预测准确性的前提；不是论文反例或新接纳的根级障碍。

参数压缩与后聚合信道也不能混同：源的lossy约束是一个有符号期望gap差，项目lower要求同一观察依赖map在两种源、所有copies/编码字段和off-event分支均合法。前者不能自动提供后者的common-center原子；后者也不是源的I或rate-distortion必要性。正文/源码里ETTh2的“quantize”是数据分箱，bfloat16是实验算术；均未被提升为本文未读部分没有任何精度理论的断言。

## 4. 当前中心候选还剩什么，是否足够有价值

**能够准确保留的窄内容**：固定有限score下，把(q,r,mu)校正为概率参考；在同一实际有限码机制上实现后聚合替换再floor、保留所有残差而仍证明全码factorization；把依赖计数波动与真实末查询条件/平稳平均TV接合；在一个显式共同cap下比较literal A、direct correction及dyadic physical-range change。这些具体组合没有被本轮所读两篇定理直接给出。这个范围支持一份可审查的机制分类，而非“已知统计学没有覆盖实际末查询”的论断。

**不能担当中心新意的部分**：
- 两层条件频数、任意阶经验Markov推断、参数位精度或训练后新核泛化这个宽泛对象，都已有明确先例。
- 依赖序列浓缩、mixing/window处理、统计编码到预测的转换已存在；给一个专门minorization常数或union bound不构成新集中原理。
- 逆频率放大、共同原子/数据处理、同信息decoder的两点论证是标准工具。
- 理想A/direct-correction相等的代数式不提供架构优势。
- S^-1 Q_b(Sz)=Q_(b+k)(z) 是网格/动态范围重新分配；匹配相对误差或同比absolute并匹配有效网格时，完整码比较为单位共轭。固定物理delta时delta/S变小有实际不同的误差类，但允许范围随M增长，这本身不是“更多信息”或预算不变的精度突破。
- 共同cap极为保守且增长巨大，无法由“同cap可放进去”推得效率、必要性或对任意budget reallocation的最优性。

因此建议(b)。这不是声称两篇已直接逐项证明Facta08，也不是以源码typo否定其研究价值；判断依据是**目前剩余增量主要是严格接口上的组合与计费**，尚未展示不由标准机制解释的预算不变关系、效率提升或不可替代障碍。完整码/endpoint处理避免了真实错误，具有技术审查价值，但不能仅凭以往论文未陈述同一实现就升格为有分量的新中心。

如果Lead后续要提升科学主张，应在原母题下明确一个规范化不变的资源/风险问题，例如共同硬动态范围、总可用码预算或相对噪声约束下，稀有context的可达风险与必要性是否仍存在非平凡差距；须与强comparator允许的全部预算重分配相容。这里只指出价值判断所缺的证据，不创建节点、不声称已有新的数学不可能性，也不在本轮执行该新研究。

## 5. 已读、未读与交接边界

已读：两篇versioned身份页；E的§2、§4、§5、B整个源文件（矩阵说明阅读，不是逐矩阵形式验证）、C假设/算法/两主声明及C.3全部短证明转引、D假设和训练定理、H.3/H.4、I参数表；K的§II、III全部主定理/证明sketch、IV-A与IV-C、AppendixD开头和窗口coupling证明开头。精确source范围见passage-index.md；原始PDF/TeX/HTML和完整hashreceipt已保存。

未读/未验证：E的C.2完整梯度常数证明、D后续长证明、E/F/G所有辅助证明、H.1/H.2所有图、转引Nichani的外部证明和转引Rajaraman的精度推导；K的AppendixD全部约九百行压缩尾界/entropy代数、其余全部实验复现与全篇证明审计、所有后续引用或不同版本。没有执行训练/外部源码。不能用这些未读范围声明不存在相关定理、不能规避比较或证明全领域新颖。

不确定性特别保留：E Theorem8的显示随机量词与外部证明依赖未在本轮消解；B的Z标量公式不一致只作局部诊断。K的混合/压缩界按原定理作用域记录，不在本轮证明所有常数正确。另一个满足假设的reduction始终可能，未被排除。

本次无新Fact/evidence ID。两个既有evidence分别为
c26b740c85ac169c6d03ea64b7d544c0b36393672ca71098297042024b51d69d
和2b2d6d6fc5ffbe2458b82f116c2e88633e5b9c260b9a39f99248c755430723e0。
最终如何计入C4或是否需要新数学，交由Lead经原生证据门决定；root仍OPEN。

普通中文：两篇近邻比“只会表示、只讲训练”的概括更强。Ekbote已经谈到精度和新规律泛化；Kavian也确实处理相关历史。但它们没有直接给出我们这份完整码、真实末查询风险和指定物理误差模型的整条链。整条链没有被直接写过，并不足以说明中心结论新颖；尤其放大数值再缩回的优势来自误差单位和付费范围改变。当前最稳妥的是承认这份工作完成了严格的专门化与实现整合，保留科学增量尚未充分建立的判断。

