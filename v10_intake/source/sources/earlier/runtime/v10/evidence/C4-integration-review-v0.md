# C4-integration-012 固定整包独立评审 v0

准确目标：`4f974bc0673ee0456e1ba3acbe18fd194e9f8f8fa0a29e4d2ed8c2296f52c140`，原 contract `3aa0ff5ddc4dd7295ab94404797636c9f50fa30cd6e7249cc5f98467b5f1179a`，D1–D8 和根的 C1–C4 不变。

**明确决策：限定范围内可进入完整根证明的准备及原生 gateway 环节；未发现需要另证新数学单元的阻断缺口。C1–C3 已由这 12 个既有 Fact 覆盖，旧九 Fact 版本诊断的限定缺前提现已补齐。五篇文献的保守比较满足本根的比较措辞，但不能证明出版级中心新颖性。正式根 statement 必须显式继承下文两项已有范围条件。此决定是 assessment，不是 root PASS、Fact 接纳或最终 audit。**

## 1. 现场输入、原生证据与执行范围

| 输入 | 现场 SHA256 |
|---|---|
| `lead/fixed-review-manifest-v0.json` | `f39c5261c32ee64a61170af9e18350297a8e48445c02b10aa4af812a43b05af8` |
| `lead/root-package-v0.md` | `f2b6c2cf0e7070f24e4255a089e9b5a7477397795ad889e8fade2e465a6fce00` |
| `lead/return-audit.json` | `cc730eeedd7f81ca8c9274b1feec79c013a28177bd9fc1cd538e53bf567edbea` |
| Fact26 文件 | `92d5355625fbc37cac24cecb4622bef38066f819a0762956c9b04ce324a7d286` |
| Facta08 文件 | `79696ad758a9dbb96509010f961e3ad3c1f8669d0dd3b7dec536b75ca476aa6e` |
| Fact276 文件 | `b581dbe9531e9ec1de571c5194398f44050acb7bbe6371671d57d2990a044e28` |

清单中的 51 个实际文件全部匹配。现场原生状态为 root OPEN、acceptance=null、12 条证据均 VALID/PASS，且实际 Fact 内容哈希、前驱清单和 statement 正文逐项对应原生 evidence。新 a08 的 proof/coverage、新 276 的 proof 均逐字包含在实际 Fact 中。没有把提交时的 pending 文本改成事后前驱；276 不是 a08 的前驱。详细记录见 [hash-audit.json](hash-audit.json)、[fact-audit.json](fact-audit.json)、[native-audit.json](native-audit.json)。

关键原生证据：

| Fact | 原生 evidence ID | 对本次评审的作用 |
|---|---|---|
| `26a62994567c7f02` | `4c3d2da3d5496214640575e15b0f40a1acc94df4faab9b587a1422f95228c78c` | 扩展后端 signed floor、完整规范码、原定位误差、纯 floor 相位定理 |
| `a08ed3def2c2da35` | `2b2d6d6fc5ffbe2458b82f116c2e88633e5b9c260b9a39f99248c755430723e0` | 同族 T1–T3、物理替换后 floor、共同 cap、缩放恢复和 B 伴随结论 |
| `276fa450421a1a95` | `c26b740c85ac169c6d03ea64b7d544c0b36393672ca71098297042024b51d69d` | 两篇统计/通信先例、真实末查询比较、完整观察与统计 predictor 的访问差别 |

这是固定版本的独立 LLM 科学审查，不是形式化验证；私人会话、模型路由与运行预算已从公开导出移除。

下文位置记号：P = `lead/root-package-v0.md`（141 行）；T = `outputs/T123-synthesis-011/prover/exact-proof.md`（424 行）；F26 = `fact_graph/facts/26a62994567c7f02.md`；S276 = `outputs/C4-statistical-010/counter/exact-proof.md`（276 行）。阅读边界见 [read-boundary.json](read-boundary.json)。本次核对组合与覆盖，不以重新推导替代既有接纳。

## 2. C1–C3 的逐项覆盖

| 根要求 | 精确依据及判定 |
|---|---|
| C1：A 实际因果接口与 zero counts | T §2、F26 §2–4：N+3 行、两个 singleton predecessor heads、K² conjunction、固定 nominal β 的 matched head、uniform r/全部 μ head、selector、残差、完整码和 simplex readout 均收费；P_s=(a_s+λv0)/(u_s+λ)，u_s=0 也合法。不是仅给一个 oracle 比值。覆盖。 |
| C1：单个 θ-independent schedule、每 fixed D1 的 max-context/实际末查询 | T L155–169，式 (12)–(13)：J_N=max(4,M+1)，b_N=ceil log2[64K(C0+1)MJ_N]；nominal sup_(H,s) reference error<1/J_N，包括零计数。counts 强律与 π_s>0 给 per-fixed-θ max-context a.s.；actual loss 被该最大值控制；conditional expected risk 另用 E[maxloss]/π_s。没有将不同 N 的条件事件拼成一个 a.s. 条件空间。覆盖，输出网格须保留下文条件。 |
| C1：指定 direct head 的极限、充要条件、真实随机反例 | T L171–183，式 (14)：实际 E_R 前端在 pre-cut 的 normalized qtilde 与 exact q 的误差 ζ_N→0，故极限为 (rθ+γπ_s p_s)/(1+γπ_s)，等于目标 iff p_s=rθ；全 context 相等 iff iid。β=log3、uniform binary interaction θ=1/4 给 bias=1/6。该诊断 port 已被擦除，未加给 lower decoder。覆盖。 |
| C1：B 的 actual finite-history operator 与 interaction | T §9，式 (25)–(30)：empirical μ 在分母，Walsh 矩有完整有限样本式和合法非特征向量路径；population gain=tanhβ1 tanhβ2。其独立 compiler、校准、残差和风险只用于 D4 uniform binary，未冒用 A/D5 的假设。覆盖。 |
[Non-scientific operational metadata omitted.]实际采用已收费的 singleton 替换。没有用 hard-copy limit 代替有限分数精确复制。覆盖。 |
| C2：显式有限历史上界与联合波动 | T §3，式 (9)–(11) 及 §6：同一 K³-edge event，有 π_s、ηθ、Fθ、N、β、实现参数、所有声明误差和 R 的依赖；sampling 通过 P_s 只算一次。conditional failure<=p_h/π_s，actual bad event 只付 p_h。覆盖。 |
| C2：非平凡 finite-N necessity 与同族 achievable upper | T §5–6，式 (15)–(21)：真实 D5 两过程、同一 full-code channel、all endpoint atoms、every randomized decoder lower；同一 A/C family 和 E_delta 有 matching δ/v conditional、δ actual orders。不是 population mean、输出网格或故意慢的 inverse。覆盖其明确的表示/误差模型范围。 |
| C2：allowed strong same-budget baseline | T §2/§8：C 与 A 在整个 clipped cube 上理想公式相同，C 用一个 product bank 而 A 用两个；相同信息、原误差位置和 common cap，允许预算重分配。actual interpolation error 不同且无最优性主张。这种等式/负结论符合根未预设优越性的要求。B 不被强行作跨不同 source law 的同预算优劣比较。覆盖。 |
| C3：同一机制中的 robustness/failure | T §3/§5–8：located upper 与 aggregate-only lower 保持分开；normalized E_delta 的 obstruction 和 dyadic scaling 的 positive recovery 均落在共同 growing cap。pure floor 另有自己的 phase/sample 定理。覆盖。 |
| C3：extra precision、输出 precision、单位变换与风险 | T §7–8、F26 §8–9：summary fractional b、output b_out、内部 B_arith/B_param 分开；不同最坏参数下界只取 max；付费范围与有效网格匹配后才有共轭。TV 未升级为 log-loss。覆盖。 |

这里的 C2 lower 是指定完整观察经降级后的信息损失结论。它不排除同样巨大 cap 内重分配资源、保存 unquantized counts 或原始历史的其他网络。根要求至少一个有实质内容的必要性或 separation，并允许限定范围及负比较；它没有要求 architecture-wide minimax 下界或最优采样率。不能因此把本包降回“只有 generic output quantization”，也不能把它升级为所有 Transformer 的计算下界。

## 3. 五个指定重点的核对

### 3.1 Gcap=Gdag+Gplus 确实支付了组合

T L70–113，式 (5)–(8)，保留原 pre-cut 的 Bplus 格式和 b_in,N，先由 Bbase 固定 input cap，再计算含注入的内部 bound。新 Bdag 不反馈定义旧 input cap，故没有 storage width/input cap 的循环。对所有 k<=k_max，取 h_star=b+k_max 后的 Gdag；较小 h 的**实际分母仍是 2^h**，不是改成 2^h_star，仅公开 padding 共用更大宽度。

中心 channel 的表、整数距离比较、packet/identity branch 和清码原在 Gplus 内；T L113 因保留原格式可以把它直接接在新 floor suffix 前。因此相加 Gdag+Gplus 后再用 32/64 的 stage/storage 包络，支付串行执行和清除，而不是取两个不相关 cap 的 maximum。中心常数属于 sign-independent adversarial channel 的已付费表，不是依赖未知 θ 的 predictor 参数。所有 coefficients/words/掩码仍有式 (7)–(8) 的上界。

本轮核查这一组合相容性及单调 padding，不重做 F26 所有 school-arithmetic gates。没有发现 Gcap 之外漏掉的新增 numerical bank、attention head 或历史 reread。

### 3.2 物理误差后 floor：代码与统计实验没有被偷换

F26 L68–96、T L43–55/L117–133/L199–216：先在 physical aggregate cut 写 B'，再计算 signed n=floor(2^b x)，写规范 pair `(n,2^(b+k))`，清掉旧码、物理 floored intermediates、决定标记和工作区，最后才 inverse/clip/selector/readout。负数用 `−q−1{remainder>0}`，所以不是只适用于 [0,1] 的旧 unsigned 程序。

由 `0<=x−Q_b(x)<τ`，E_delta 的新增 normalized error 是 `(δ+τ)/S`。ζ、value/score 上游误差不除以 S；late selector/selected-u 错误留在原 normalized 位置。T 的式 (9)–(11) 和 (18) 保持此顺序。

lower 的 T 先把两种源的整个 B' 都写成相同 C_s；相同完整码经过任何同一确定性 floor/后续计算仍相同。因此中心 lower 不要求 floor cell interior，也不等同于纯 floor 的下界。identity/off-event 分支原 nominal code 长度<=Bbase<b_in,N，center numerator/denominator 长度由 j0<=ellM 控制，均被实际 packet domain 接纳；floor 后的较长码是内部计算，不被错误地要求再塞进旧 external cap。

### 3.3 00/10 的 actual weighting 正确，不能移用纯 floor 常数

T L192、L218–228 给目标 gaps d00=Δ、d10=vΔ/w。每 endpoint 条件共同 atom 的质量至少 1−α。先相加两个 sign 的真实 actual risks：

`Ract_-+Ract_+ >= (1−α)[vΔ+w(vΔ/w)] = 2(1−α)vΔ`，

再取 sign 最大值得 `(1−α)vΔ`。式 (19)–(20) 中 α<1/32，代入 Δ=(c+v)δ/v 后，正是 P L72–74 的 `31(c+v)δ/32`。没有把逐 context 的不同 sign 最大值相加。

纯 floor E0 的共同 cell 只证明 query00；故 T §7/F26 §7 的 actual lower 是 `(1−α_f)(c+v)δ_f/8`，balanced constant 为 31(c+v)δ_f/256，不能额外加 10 的贡献。两套常数在 P L74、76 和 T §7 中已正确分开。

### 3.4 固定 physical error 的恢复是 per-fixed-θ、aggregate-only 结论

T L313–330：S_N=2^floor(log2 M)，M/2<S_N<=M，含 M=1；并未在 nondyadic M 上假装 S_N=M。允许的 fixed δ∈[0,1] 给 `(δ+τ_N)/S_N→0`。在同一 source-path probability-one event 上，u_s→π_s>0，最终 uI_s>=π_min/2；于是用真实 denominator 的式 (10)，加 ζ,d,Eout→0，得到 max-context、actual 和 conditional expected consistency，对所有 admissible aggregate-channel realizations 一致成立。

这没有使用不会消失的粗糙 all-history `M·δ/S_N` 上界，也没有宣称 zero-count histories 上 perturbed reference error 均趋零。所有 earlier/late errors 在该恢复比较中设为 absent；若保持非零需另看式 (9)。normalized S=1 的中心 lower 在同一个 b_N、同一个 growing cap 下仍存在，得到两固定规律风险之 max 的 liminf/至少一固定 sign 的 limsup，而非强行指定一个 sign 的 liminf。

### 3.5 same physical b 不共轭的限制已准确修复

T L332–340、F26 L391–403：确切恒等式为 `S^−1 Q_b(Sz)=Q_(b+k)(z)`，包括 signed finite rationals 和 exact ties，前提是无 saturation、规定擦除、同一 normalized canonical 编码。可比较的是 scaled `(b,k)` 与 unscaled `(b+k,0)`。

有噪码时还须把 scaled class 取为 `(a,d)→(Sa,d)` 的合法 image，留足 numerator bits；两个任意 hard-capped classes 不自动互为 image。公开 b/k/S/header 不同，则整串只由已知可逆 public-field relabeling 对应；擦除后不能再用“保留的 raw word”逆变换。相同 physical b 下，以 z=3/8、S=2、b=1 为例，unscaled 为 0、scaled normalized 为 1/4，故未匹配有效网格时没有观察或 minimax risk 的共轭结论。

需要的 numerator capacity 为 b+k+1（含 endpoint），另加 denominator/sign/framing 和 scale weights；都在共同包络内。不能把此等价式解释成总字长固定时的免费精度。

## 4. 旧诊断 9ba6 的现状

旧记录 `9ba6fedaa6b7562e4ef6bcba21553e9c7e2a2bf6e55d10d5b6f20852acc8cc64` 针对旧九 Fact 集，指出旧 backend floor 与 expanded backend located-error 之间不能只靠相同 ζ 或 common cap 拼接。它在当时成立，保留原记录是正确的。

新证据的对应修复是：

| 旧缺前提 | 新证明的实际修复 |
|---|---|
| expanded E_R 上的真正 floor 编译与全码擦除 | F26 §2–5：同一 expanded frontend，signed divider，规范 denominator/零码，before-copy cut，非循环 cap |
| 不能由 q_old/q_new 同误差推出同 floor | F26 §7：直接对 q_new 使用 joint event 和严格 cell margins，不认同旧、新 unreduced fractions |
| 同族 general-D1 upper 与 θ-independent schedule | F26 §4/§6，T §3/§4：保留原误差位置并显式加入 floor，所有 K 与 zero counts 的 nominal reference theorem |
| 物理 center-map 后接 floor 的同族风险比较 | T §2/§5–8：旧格式完整 channel、Gplus+Gdag、endpoint 因子化、同一 actual A/C upper、dyadic positive recovery |

**因此旧诊断的限定 missing premise 在这个新 12-Fact 版本中已获证据修复。**不需要删除诊断、倒改旧审查、重新证明旧 Fact 或把 root 改成另一个问题。该结论由 26/a08 的实际新证明支持；276 补充的是统计来源/访问比较，不是 a08 的事后前驱。

本轮没有对研究图状态作关闭、接纳、撤销或重开操作；旧 diagnostic 继续原样可见。本评审也不是一条新原生 Fact。

## 5. 两项应显式写入最终根 statement 的已有范围条件

这些不是新增研究义务，也不是已有 Fact 的反例；是 P 的简述在脱离所指 annex 时可能遗漏的量词。正式 root proof 不能让简述作更强声明。

1. **输出网格的一致性条件。**P L33 与 L78 的“reference <1/J_N / consistency”应补明：默认保留 exact rational simplex 输出；若启用 binary output grid，取 T L167 的 `b_out,N>=ceil log2(8J_N)`，或至少使其误差另行趋零。固定 b_out 不能包括在一般一致性结论中。精确反例是 iid binary p=1/2、b_out=0：每次 emitted probability 属于 {0,1}，TV 恒为 1/2，即使已知真概率也不能一致。最小修复是在最终主陈述/版本说明中带入既有输出 schedule；无需新引理或新 Fact。
2. **固定物理误差恢复的幅度域与位置。**P L9/L78/L136 应明确沿用 T L315 的 `δ∈[0,1]`、原 finite-input cap、aggregate-only，其他早/晚注入 absent；不能简写为任意有限 δ 或所有位置的固定故障都能被缩放消掉。若要扩大至 δ>1，需要扩展 admitted error domains/range/cap；当前根没有要求这种扩大。最小修复是保留原已证条件。

P L27 已把确切 theorem annex 指定为控制依据，因此按预期限定解释时两条件已有支撑。建议在准备根提交的下一固定版本显写，免得完整 statement 与其证明域不一致。除此以外，本轮没有找到需要新增数学桥梁的具体缺口。

## 6. C4：现有比较是否满足根措辞

**就当前保守、具体机制分类的主张，五源比较达到 C4 的有界比较要求；它不等于穷尽优先权检索或出版新颖性认证。**根要求在 object/information/architecture/quantifiers/resources/risk 上与已核验 primary 作比较，并允许 equality/negative conclusion；没有要求证明 globally first 或达到特定会议的新颖性门槛。

[Non-scientific operational metadata omitted.]D'Angelo v1 的 Definition3.1/Eq8、正确 lag swap 和实际 terminal operator；Zhou v3 §4.4/G.2.2 的 count-restoration 与 CTW。P L98–100 没有扩大这些核验的范围，没有把 limit-copy 误当固定 finite-score 实现，也没有把本地实现等同文献全部 residual/word semantics。当前包不靠这三项本来已知的构造单独声称创新。

后两篇在本轮再次打开指定 primary 版本核对，且与冻结 sources 和 admitted 276 的作用域一致：

- Han–Jana–Wu v2 的 Eq95 已经是 stationary higher-order **真实末查询**的 KL prediction risk；Lemma6 的 suffix averaging 用 stationarity 和 code redundancy，Theorem22 给其限定 alphabet/sample regime 的 KL rate。S276 式 (2) 的 U_KN 由自己的 normalized sequential code 和 chain rule 只除一次 N−1；没有依赖 rendered Lemma23 的可疑 normalization，也没有反转 Pinsker。其 actual TV upper 为 sqrt(U/2)、conditional 为 sqrt(U/(2π_s))，不是 local same-cap circuit theorem。[指定 primary](https://arxiv.org/html/2106.13947v2)
- Han–Özgür–Weissman v4 Theorem1 的 approximately regular hypotheses 和 Lemma1 的 iid transcript factorization，与 S276 的复述一致。重叠 pairs 的 `P(Y0=00,Y1=11)=0` 而 marginal product=vw>0，确实排除直接 iid 替入；并未排除把整个 trajectory 当单个 observation 后另证条件的其他 reduction。per-sensor communication k 不是本地 fractional b。[指定 primary](https://arxiv.org/html/1802.08417v4)

S276 的完整码碰撞亦使用正确范围：000100 与 001000 的 canonical observations 相同，而 suffix-average values 为 8/15 与 2/5；这只阻止逐串复现该函数。两历史的 initial pair/counts 相同，在每个 fixed θ 下 likelihood 相同、terminal true-law target 相同，故不能凭该碰撞推出更大的真实 prediction risk 或统计 baseline 的优势。P L113–115 正确保留这一限制。

五篇比较共同覆盖表示/软匹配、归一化计数恢复、真实 dependent terminal statistical prediction 以及 quantized communication 的近邻；不是只按论文标题说“问题不同”。未读的 Ekbote/Kavian 补充**不属于本 v0 证据，本轮也未读取其结果或价值判断**。本决定不预设它们支持或反对新颖性。若下一版本引用补充，需另标版本/哈希并调整相应比较；不应倒填本冻结版本。

## 7. 出版级中心新颖性的独立判断

**NOT ESTABLISHED。当前包不足以把“新的出版级中心贡献”当作已获支持的结论。**

逆频率敏感性、two-point/common-atom argument、数据处理、joint-count concentration、suffix averaging、缩放/floor 恒等式、浅层频数表示和 normalized counts 恢复，均是既有工具或明确先例。端点条件化和真正 stationary weighting 是必要的正确性工作，单独不是新统计对象。显式清除 denominator/framing bypass、signed finite compiler 和一个兼容 cap 解决了真实证明漏洞，但仅由这些细化不能推出新理论机制、最优风险或更强资源率。

仍可如实提出的技术增量是：**在一套完全指定、真正兼容的有限码 soft-summary 实现上，把 nominal recovery、指定 cut 的真实随机历史 obstruction、located-error upper 及付费 range/grid 比较连成一个可复核分类。**三篇表示论文和两篇统计/通信定理没有按本包的完整接口直接给出这条实现链。但“没有直接替换 theorem”不是“所有先例都不能推出它”；其核心风险阶数仍可能主要是标准量化估计论在特殊机制上的实例化。

因此不支持以“新的 Markov 概率预测问题”“首次处理实际末查询”“新软匹配公式”“新计数恢复”“免费 precision scaling”作为中心创新口号，也没有证据支持 depth/A/B/Transformer 的普遍优势。若以出版为目标，还需要用精确的剩余技术增量及最近来源支持其价值；本轮不把这项科学判断冒充已经完成。与此同时，根是允许负比较的 classification stage，**不能把尚未确立出版新颖性，自动变成要求训练可达性、隐状态或新过程模型的根前提**。

## 8. 尚缺的整包接纳前提及交回决定

数学方面：按第5节保留已证范围后，C1–C3 的 exact claim 与 proof/cap/风险接口已有覆盖；没有再列一个泛化“整合待完成”义务或要求新研究分支。C4 的五源比较和普通中文、真实失败与未决边界已有具体内容。本轮新的独立整包评审现已形成，但它在原 v0 manifest 中合理地是 excluded future input。

仍须完成的 truth-gateway 前提是：

1. 根的最终 self-contained exact statement/proof 使用原 C1–C4，引用这 12 个已接纳 Fact 的精确范围、五源比较和本次决策；明确带入第5节输出/误差条件，不能把全部 family indices 都说成一致。若补充 Counter 报告，标为后来版本，不冒充本 v0 证据。
2. 把实际评审文件及哈希作为随后固定版本的 review receipt；保留旧诊断和各失败版本，不覆盖原冻结包。本评审并未获得接纳根的权限。
3. 本轮评审不等于最终组合的接纳；它没有把组件结论或本次审查自动提升为整个研究问题已完成。私有流程和资源预留指令在公开导出中省略。

这不是重交或重开任何旧局部任务；没有已接纳 Fact 需要因本轮评审重投。审查范围之外仍包括：所有后端位门的第二次完整形式化复验、穷尽文献优先权、最优采样率/总字长或任意 architecture 下界、learnability、隐状态和新过程阶段。这些不得静默并入本根完成条件。

普通中文：现在新增证明真正接好了旧稿缺的桥，不再只说“两个后端都很准”就把舍入下界搬过来。物理错误、舍入、清码、后续读出和资源预算的先后关系也对得上。两个稀有情境的下界按真实频率加权，缩放恢复只针对指定位置的固定绝对误差；若最后输出格子一直很粗，仍然不能一致。数学分类已可准备根证明，五篇先例比较也没有发现虚报的优势；但这不意味着已经证明成果足够新颖或已经接纳根。本轮只交回这个有范围的评审决定。
