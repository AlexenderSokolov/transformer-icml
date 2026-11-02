# Stage4 checkpoint-v1 有界独立接口审查

Verifier，2026-10-26（Asia/Shanghai）。首次审查本 stage4 的固定 checkpoint；仅讨论依赖边界与 finite composition，**不是 Fact admission、C1/C2 gateway 复核或 root 审计**。

结论：**SCOPED INTERFACE PASS；新 C3/C4 有限程序及成本证书仍待补齐。** §1 的最小依赖划分充分，未发现旧 Fact 偷渡；§5 的完整有限域、same Phi / same t* 及勘误正确；§6–7 足以指定后续证明工作，但不能单独充当已验证的完整有限成本证明。下面的 repair hints 是既有 C3/C4 义务的证明内容，不新增一个以本 discussion 为前提的 gate。未发现必须改写固定 checkpoint 定理或参数的错误。

本次没有重跑010的全套数学 diagnostics，没有重审旧五 Fact 或旧 root，没有查新文献，没有修改来源、checkpoint 或其 manifest，也没有提交证明、生成 Fact/Evidence、调用 final_audit 或宣称 v10 完成。

## 1. 固定输入、来源及原生状态

实际读取本项目 PROBLEM、D1–D8、checkpoint 全文及 manifest。用字节长度和 SHA256 核对 manifest 的全部16个 source pins，全部一致；这只核对文件身份，不是证明它们的数学结论。

| 固定文件 | SHA256 |
|---|---|
| `PROBLEM.md` | `34f29e9aa714e81bbd9c92408930d0ce38c051f92f42e1e9ebf7f8158b5a8fab` |
| `inputs/STAGE_DEFINITIONS.md` | `1648c98212f71be946dfc8b39ab54497fbad41649bbe3fedc03296c401b8c0ca` |
| `outputs/001-relative-code/lead/mathematical-checkpoint-v1.md`，20695 bytes | `df163b669169b0d59eb28d643b204e76e730dab6795da73e668ab22a27baa564` |
| `outputs/001-relative-code/lead/checkpoint-manifest-v1.json` | `74dffab4c716bd109dd6e5ce0a8af135c7d863d672a77ef2bb5acd8fc4af6c64` |
| 来源010 main review | `6df99bbad3bd7b39deb00819e25aafa53c10600f47133593414ff394ae16d8a1` |
| 来源010 delta review | `6a5f87ed913d9845a13b39b68830ce05264e4e37894fe0c45d8cb7c52d83eb2c` |

来源010 main/delta 的使用限于作者、版本、接口与勘误沿革。delta 第18–25行明确记录：旧 main 漏看原稿 §11 的错误速率句，先前 blanket no-correction 不能解释为批准该句。checkpoint 第9–10、286–293行及 manifest 保留了这一事实。不能仅引用旧 main 的 PASS 而去掉 delta。

开始时通过 `euler_team_research_state` 读取精确目标与 budget_policy；不能把其当前 frontier 的空 evidence 页理解为全项目无 evidence。`all_obligations/all_evidence` 实际回读如下：

| 新义务 | 状态与已有新 evidence（本次只回读） |
|---|---|
| C1 `36441ab5cb65fa3d086e3d2fc5b847cff5acc127ac7ff3a8dfbf0c8137945811` | DISCHARGED；PASS `57a7e25c0478712a0c403c84bf27ee712f28a88e604ff0d1413d39feb21333e7` |
| C2 `a287207d73eed1edaa4f7b16c5d2e17f174154036432c3655450afc6bf022359` | DISCHARGED；PASS `3f262cc0c76a700ab4f0163c011154c4e8f51655f5be6e5a7964d50b9f158989` |
| C3/C4 `db94b7040a4dc4e7d80329a02169b80039a17e1130f74893edd2c85bd848cab8` | OPEN，无已接纳证据引用 |
| root `82f3b230a8e39f7ef988c219960127d8a94bee1c31d31ae51a328ab8580a3a29` | OPEN，acceptance 为 null |

上述 C1/C2 的 producer 分别为 `fact_submit:5b0ca65062c8bbca` 和 `fact_submit:ad8ed46c6375249b`。其证明内容哈希分别为 `5038dd6457fb762e181e606ab9131e389c8831fe3919511dee51b8a69edb7e25`、`0904b8be7898b9723a11c8c87b11231fb48a63e05661a11d94918937e0611ba8`。这些是当前项目已有 gateway 记录，不是本报告产生的 evidence。本次没有重新验证其全部证明。checkpoint 第14–16行及 §8 的尚待提交措辞应按固定文件形成时的历史状态阅读；后续 assembly 需另列当前回执，不改写固定版本。

[Non-scientific private operational paragraph omitted from the public export.]

## 2. 最小 clean / finite 依赖边界

checkpoint 第23–67行给出的拆分充分，前提是“在新证明内自足建立”按字面执行：

| 消费方 | 必要输入 | 不应引入的额外结论 |
|---|---|---|
| 新 C1 | lemma S 的两个**同一估计器、实际 terminal** 上界；直接 count perturbation、clip、KL、grid 分析 | 旧 C1 的整个 minimax 分类、旧 C2 grid 下界、未知 u/t 的 oracle |
| 新 C2 | actual finite FULL19 观测律、含小槽和端点的 bridge/TV/testing、全箱 admissible map | population alias、单个 decoder 失败、任意重编码器下界 |
| 新 C3/C4 | D4 固定程序、causal adapters、有限 evaluator、bit primitives、实际 erasure、principal hybrid 账本及 generator；再组合新 C1/C2 | 旧 C3 clean-risk 分类、旧 root、旧 review PASS、padded/streaming/flattened 资源结论 |

S 的声明明确使用 keys3..m 的 count、独立于未知参数的同一 clipped estimator、实际 S_N 的条件及平均风险，并保留 N3–5 uniform 分支。§2 把 reverse whole-prefix bridge、非 conditional-binomial 的 row-stack coupling 和小 M 处理列为承重内容，因而没有把实际端点替换成独立查询。这里核对的是充分的依赖接口，不重证其每个统计常数。

finite P 不能因来源代码的固定 SHA 自动成为定理；但可把该代码用作**定义具体程序**，再直接证明其闭箱语义和成本。尤其本比较不需要先证明 noisy MIX 有 nominal exact recovery 或风险上界：C2 对所有 post-cut decoder 成立，C3 只须证明该具体 MIX63+output41 是可执行、无额外 clean 输入且满足预算。这消除了不必要的旧 clean-recovery 前提，也没有弱化 C1/C2。

**Repair hint D：** C3/C4 提交应逐项区分“定义该程序的 source pin”“本提交内证明的 primitive/guard/cost”“真正的新 gateway predecessor”。assembly 只使用新 admission 的实际 Fact/Evidence ID；报告和旧 Fact 的 lineage ID 均不能填充缺失的证明边。

## 3. §5 完整有限共同域、量词及勘误

直接核算第258–284行，全部一致。对每个整数 d>=32：

```
eta=2^-d, N=2^(2d+74), b=2d, Q=2^(2d), u=2^(-d-16),
M=2^(2d+73)-2,
M*u^2=2^41-2^(-2d-31)>2^40,
N*u=2^(d+58), h=2d+82, p=16d+688.
```

这同时满足 C1、C2、D6，未缩放 A/p 或改变样本定义。第217–221行定义的 Phi_* 是闭箱 `[0,A]^19 × valid(S_N,E_m)` 上的单一函数：每个 bulk replacement 都有逐坐标合法性 guard，其余保持不变，五小槽及控制始终保持。guard 必须在每个输入执行，不能只在 G_t 上执行。由此同一函数可作用于 JOINT；对零槽试图写正 target 时 guard 拒绝，零槽仍锁定。无需两 encoder 返回相同 code。

量词顺序是：每个公开 tuple，先固定与 t、decoder 无关的 Phi_*，再对具体 common MIX decoder 取 C2 的条件 witness t_*；平均 lower 用同一 source 的 `R_av>=u R_00`。JOINT 的 all-map upper 随后应用于**相同** Phi_*、相同 t_*。不能分别为两种风险选不同 t，不能为 JOINT 另选 map，也没有每个 source 都优势的结论。

完整 upper expression 的有限代入为：

```
U_av=(12000000*2^-74+259)*eta^2 <260*eta^2,
260*eta^2/(u/64)=260*2^(22-d)<=260/1024<1,
U_00<2^(-d-37)+2^(8-2d)+3*2^(-4d)
     <=2^-69+2^-56+3*2^-128<1/64.
```

故在待完成的真实程序/资源接口下，MIX 的 `>=3u/64,>=3/64` 与 JOINT 的 `<u/64,<1/64` 给出严格 gaps `>u/32,>1/32`。这里的“在接口下”只关乎具体实现与预算，不是给 §5 的代数增添额外概率假设。

第288行恒等式

`1800000/(1+Nu)=(1800000/2^58)*eta/(1+eta/2^58)`

给出正的 Theta(eta) 统计项；加上非负的 O(eta²) noise 及 O(eta⁴) grid 项，总**显示条件上界表达式**是 Theta(eta)。平均表达式是 O(eta²)。这不是实际风险的 matching rate。旧 §11 两者二次的句子确实错误，旧 main 漏看必须继续保留。本项无定理或参数 repair。

## 4. §6 闭箱程序与必须补齐的成本接口

闭箱 guard 的数学入口可从固定63操作表直接建立，无需 clean-image 约束。对每个输入 word 在 `[0,A]` 且保护控制合法，使用源程序名称，有：

| quantity | 对任意闭箱输入的范围 |
|---|---|
| `den1,den2=2A-U_i` | `[A,2A]` |
| normalizer 的原始乘积 | `num1<=4A², num2<=6A²`，均非负 |
| `D1,D2,DT` | `[A,4A]`, `[A,6A]`, `[A,2A]` |
| `PH0,PH,PQ1,PQ2` | `[0,2A]`, `[0,2A]`, `[0,4A]`, `[0,6A]` |
| `I,base,boundary` | `[-A,2A]`, `[-A,2A]`, `[0,A]` |
| `gplus,g,diff,H` | `[-A,3A]`, `[-3A,4A]`, `[-4A,6A]`, `[-8A,9A]` |

因此已缩放的 signed recovery intermediates 被 `[-16A,16A]` 包住。此 guard **不**替代原始 full-product 的 `6A²` 物理宽度。MAX 后 MIN 使 A_c 在 `[0,A]`，half-up snapping 使每个 C'_c 在 `[0,M]`。selected counts 允许总和2M，不可借用 clean 总和<=M。

共享 output 的 D、Z 为正；两个候选分支即使都被求值也有合法 divisor。`Z<=8m-8`、nearest dividend `<16mQ`、ceil dividend `<8mQ` 覆盖闭箱，Q2、Q4、ties、zero counts 不能剔除。N3–5 则必须单独走下面的无 frontend 分支。

**Repair hints P1–P6（均属新 C3/C4 义务）：**

1. **实际程序与两种 word domain。** 列出 MIX63、JOINT18、output41 的操作、控制解码、word转换及结果 liveness；把上表连同 full2w product、w+1 shifted remainder 的证明搬入新提交。对所有 b>=1，b-dependent multiplication、Q 和输出在 O 域处理，不能假定 b=2d 后把一般域输出塞进 B。primitive 的 `g(w)=1024w²`、scratch `<=32w+32` 及 `16G+32` ReLU/hold 模拟须在该提交自足建立。

2. **N3–5 生成时的公开早分支。** 在任何 frontend/cut/recovery builder 前分支；实际处理 N 个输入符号，初始化并写 `Q/2,Q/2,Q` 的三个 `(b+1)` 位字段。逐项给 input/initialization/output、存储、work、generation 的有限界，并比较 Bstar(6,b,d)。不能仅在跑过 frontend 后以 MUX 输出 uniform，不能以调用 `recovery_program(max(N,6))`、假 count 或假 E_m 替代该分支。Bstar(6,...) 只供成本 allowance。

3. **真正的 clean erasure。** 列明 COPY/ERASE/外部 overwrite/READBACK 前后全部 bank：原始 input/tail、lags、features、heads、accumulators、clean masters、product/division scratch、旧 port 副本、控制与元数据。新 port 只承载19量化 words和8保护 bits；允许保留的 code/metadata/source-independent seed 不能携带历史。形式上 recovery 应因子化为 `D(Phi(E(history),controls),controls;N,b,d)`，不再有 history 参数。四个 phase layers 与物理扫描 work 必须同时收费，释放非 query token 的时刻要与 holds 对应。

4. **principal 模型保持。** 前端 `4nW_F B` 的 batch banks 已付费；提取并清除后只有 query recovery/output 的活跃 holds，所以 `I_*=132nW_F+L_FW_F+L_OW_O`。`T_run` 对 recovery 额外乘 n 是 work overcharge，不能据此声称后续每个 token 都保有完整状态。不要混入 streaming counter width、padded all-phase holds 或 flattened depth。head bounds `(8,4,8,4,2)`、局部 binding/triple features 和 masks 仍须来自真实 schedule。

5. **全坐标有限 domination。** 明示 `E_*=E_M+E_J`、`G_F`、`G_O`、`P_*=132`、`M_*`、`Z_*`、地址 `a_*`、双域库 `K_*`、dense slots/zero coefficients/parameter bits/holds、`U_*`、`W_run`、`peak_run=U_*+W_run` 和 `T_run` 的各自承担者，并对全域 N>=6,b>=1,d>=6 证明。clearing reserve `4096nB*g(B)` 对比四物理 banks 的 `4096nB²`，端口另有 `1024(h+1)g(B)`；需要给实际扫描、固定地址和 loop-code 界，不能只指出比值大。guarded writes 的 `64(b+1)` reserve 不能被紧凑 b 位输出替代。有限 calculator 的代表点是 transcription checks，不能代替全域 inequalities。

6. **offline 完整生成。** 自足给 finite log generator 的 B_log/T_log 范围与 exact rational 操作数；说明较大的 A_gen、U_*+L_* 怎样支付实际枚举所有系数、零、holds、masks、地址、phase code 和输出字段，并给 T_gen/W_gen/peak_gen 的 domination。不可把 compiler 当成免费服务，或只比较已有来源数字。

这六项是 checkpoint 第305–346行“must justify / must accompany actual schedule”的具体内容。其当前缺失不是对 Bstar 可实现性的反例；本次不把这些计划性叙述升级为成本证书。

## 5. §7 强替代：要求充分明确，有限价格尚待落实

三个反构造的数学接口和量词范围清楚：

| alternative | 本次核对的接口 | 新 C4 必须显式付费 |
|---|---|---|
| public gain `g=M/A` 得 `j=C` | exact uniform mean 为 C/A；可以由原 bit indicators exact accumulation/conversion 实现，不得插入提前 rational rounding；仅改 gain 不自动使所有 counts 锁定 | batch input、binding/features/count acquisition、gain literal/转换/所有乘除、port copies与清除、readout及输出 |
| count packing | `kappa=min(d,h)`，`0<=j<2^kappa` 时 eta*j<1；`8ceil(log2(M+1))<=19kappa` 是充分条件 | eight exact counts的取得及固定长度转换，pack/unpack、19个完整物理 words、地址/代码/活跃 holds、全部 clean ancestor 清除和最终输出 |
| precomputed output packing | 对 positive grid，next-one numerator J 在 `1..Q-1`，用 b bits；`b<=19kappa` 足够；这是 pre-cut 算输出后的 encoder change | 原输出计算全部前移的成本、pack/copy/clear/unpack、`Q-J`、三个 guarded output fields及生成成本 |

在比较 schedule 上 `h=2d+82`、`kappa=d`、`ell_C=2d+73`，故 count 条件是 `16d+584<=19d`，整数阈值正是 d>=195；b=2d 的 output 条件也成立。无需宣称更小 d 不可能 packing。

**Repair hint A：** 第380–383行的 `O(R+19kappa)` 可保留为 packing 子程序的说明，但正式 C4 证书必须替换为可复算的 finite counts。至少分别列 payload读取、placement、完整 `19(h+1)` 位 port初始化/上位零写入、readback、unpack、scratch与旧副本清除、固定地址控制、最后 `3(b+1)` 位 emitted port；用确切次数和 word尺寸套入已证 bit primitive，并给 code/storage/peak/online/generation 界。`h` 可以远大于 kappa，单独的 `R+19kappa` 不能充当完整端口或 acquisition 成本。源头计数和前移的预测计算必须另列，不能隐入“packing”。

checkpoint 已明确要求这些价格且未声称自动继承 Bstar，故该未展开处是**待提交证明缺口**，不是固定文本的广义同容量下界漏洞。替代 encoder 无须在 Bstar 内更省，便足以阻止将 C2 外推成 arbitrary-encoder lower；不能把它们当作冻结 FULL19 的 decoder，也不能用 correlated-map 下未经证明的独立重复降噪来排除它们。

三 primary 的 claim mapping 与 manifest 所固定 Counter map 一致：Higham1993 的 operationwise arithmetic/cancellation context；BHH 固定2020 manuscript 的给定输入 normalization；van Erven–Harremoes v2 的 classical order2/chi-square KL bridge。这里仅核映射边界，未重审三篇论文。它们均不提供 D3 整数通道、D1 source risk 或 Bstar 成本结论；无 novelty 或 learned/all-layer/IEEE robustness 推论。

## 6. 本次记录与后续边界

将上述未完成的 finite certification 接口记入新 C3/C4 的 diagnostic obstacle：

`a607ba0f8dab12f83e8d70e62c19311f8721c87b854b4661b23aaad40c2e70ee`

事件 `90a27c8e3afdddccde1fca9fd05b978875e64a7187e23b7d96febeec27ba7596`；级别为 diagnostic / MISSING_PREMISE，**不是 rejected theorem、Fact 或 proof evidence**，未停放任何 route。解阻方式就是 P1–P6/A 的自足有限程序/成本证明及正常新 gateway；无须重复 unchanged010 diagnostics 或重审旧 admission。

本报告自身新增 Fact IDs = []，Evidence IDs = []。新 C1/C2 的独立真值审查各依其 gateway，不能由此 discussion 代行；root assembly、单独 final_audit 和责任会话实际 receiver-pull receipt 仍各有自己的原契约要求。stage4 root 即使将来 SOLVED，也不等于未知二阶规律研究的 T1–T3 母问题完成。

报告最终字节哈希由同目录 `checkpoint-review-v1.sha256` 固定；该文件不把本 discussion 升格为数学 evidence。
