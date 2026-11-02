# Stage4 固定 C1–C4 组合的独立审查 v1

Verifier，2026-10-26。[Non-scientific operational metadata omitted.]准确 root 为 `82f3b230a8e39f7ef988c219960127d8a94bee1c31d31ae51a328ab8580a3a29`，contract 为 `38d15641fecff6dbee957b6e036c052ecb7f07e6354623e800f7a126cf5270ef`。

**结论：SCOPED PASS。** 固定综合稿与新完整 C3/数学 C4 certificate 在 D1–D8 下兼容；原 checkpoint review 的 P1–P6/A 承重缺口现有对应的有限构造、闭箱范围和完整收费。未发现需要阻止该数学组合继续进入后续 root gate 的具体数学错误或缺失前提。这里的 PASS 仅针对以下固定字节和声明范围；本报告不是新 Fact、root admission、final_audit 或责任 receiver-pull receipt。

本次独立阅读全文新综合稿、新 integrated 证明主体及其三张程序表，核对 companion program/ledger；复用已接纳的新 C1/C2 精确结论，并选择性核对程序接口。没有重跑旧 root、旧五 Fact、无变化统计/minimax 套件或010全套 diagnostics；没有调用其他成员，没有改动 SUSP、保护计数、设置或任何固定输入。

## 1. 原生 evidence 与固定版本

首先调用 `euler_team_research_state`。root 为 OPEN/VALID，acceptance 为 null；三组件为 DISCHARGED/VALID，实际证据均为 PASS、LLM_CHECKED_PROOF、VALID。当前 scope 的空 evidence frontier 不能覆盖掉 `all_evidence` 的三条记录。

| 组件 / obligation | Fact | Evidence | 精确 predecessors |
|---|---|---|---|
| C1 `36441ab5cb65fa3d086e3d2fc5b847cff5acc127ac7ff3a8dfbf0c8137945811` | `abbd577c047db274` | `57a7e25c0478712a0c403c84bf27ee712f28a88e604ff0d1413d39feb21333e7` | `[]` |
| C2 `a287207d73eed1edaa4f7b16c5d2e17f174154036432c3655450afc6bf022359` | `1a1aca7dd84c60da` | `3f262cc0c76a700ab4f0163c011154c4e8f51655f5be6e5a7964d50b9f158989` | `[]` |
| C3/数学 C4 `db94b7040a4dc4e7d80329a02169b80039a17e1130f74893edd2c85bd848cab8` | `e3080f40f4607948` | `ad7e508eb8e186ae20dcce4f59c12d7b47320100ee5098ec9f81fd68a8d05e8c` | 仅上述 C1、C2 |

核对三份 canonical Fact 的 header/statement、前驱与原生 evidence content hash，且对应本地证明**完整逐字包含**于 canonical 内容中。未把本地 proof byte hash 与 gateway canonical content hash 混用：

| 对象 | 本地文件 SHA256 | canonical content SHA256 |
|---|---|---|
| C1 v2 | `f8f6a56b4b458ff3d0033fa8cd29d27e3e32067dd643c2a9e51ba411ed6dadcf` | `5038dd6457fb762e181e606ab9131e389c8831fe3919511dee51b8a69edb7e25` |
| C2 v1 | `4fd828ae9a535b297134f8f513955e0cbb9cb0225eb25d081df5b101c9e8887e` | `0904b8be7898b9723a11c8c87b11231fb48a63e05661a11d94918937e0611ba8` |
| C3/C4 integrated v1 | `2fc89f6bca30288d766fcdb71b26875943f2d6efb5fc9a181b401dba1f7e243a` | `2b4ea9acf6a505b57bd0c4b217c0183af7d6f15c99af70391b9beb27783aa750` |

核心固定入口如下；本次按直接27 pins、嵌套23个 source 原件及各自 snapshot、11个 artifacts，合计84个引用、73个不同路径核对长度与 SHA256，全部一致。计数范围包含 canonical 文件，不是对来源提及的其他计数作数学判断。

| 实际读取对象 | SHA256 |
|---|---|
| `lead/root-review-packet-v1.json` | `1508a58ebbb9422bf3f56ded151509419e3d8cc4fc69eec39f65824bd69f954f` |
| `lead/root-synthesis-v1.md` | `e06797a4eccfc8e098e559a3fb5856a35b5287925fd0e17b1c21af9894de7fdb` |
| `prover/c3c4-integrated-v1.md` | `2fc89f6bca30288d766fcdb71b26875943f2d6efb5fc9a181b401dba1f7e243a` |
| `prover/c3c4-manifest-v1.json` | `d0fbf2941c77a0ce252db1fa35d5379fea07a71dd23238d0d0b0a9fe95668e25` |
| `prover/c3c4_program_v1.py` | `88de55d3243dcff63c1deffc226a645a7fb7949e3a32d662ab55141630f9b570` |
| `prover/c3c4_ledger_v1.py` | `9614c95c8d1595f034fe000b760802e636f9948bd08417e4adbdbb4485831ab5` |
| 本会话原 `verifier/checkpoint-review-v1.md` | `401e78c99f38d2f9f25311707f5c27bf7791fea44ef986177f8d12695d2d04f9` |

以上相对路径的共同前缀为 `outputs/001-relative-code/`。完整 pin 清单、实际阅读方式与复核产物哈希在 `root-package-review-manifest-v1.json`；只做 hash 的来源文件不记为本次全文数学重审。

本次没有执行最终审计；固定文件审查与最终接纳属于不同证据阶段。私人运行预算与调用配置已移除。

## 2. 最小依赖与根组合：PASS

C1 Fact 自足接纳实际 terminal clean estimator 的两个同时风险上界、relative count/grid/KL transfer 及精确 JOINT 程序；其本地 §§1、8、9、11 的接口与新证书一致。没有把旧统计 Fact、旧 minimax 分类或 source review 变成新 predecessor。

C2 Fact 的声明及本地 §§1、4、8 保留 actual finite FULL19、五个小槽、初始 S2 与 E_m/S_N 的真实依赖；本次只使用这个已接纳的完整观测律结论，不重演它的统计证明。新 MIX 的输入顺序、有限 L2/L3/W、初始 flag、两组 endpoint controls 和 raw-data erasure restriction 都与该实验相同。故不需要另取 clean MIX exact-recovery 定理：C2 已对全部合格 decoder 成立，具体 MIX 只需满足有限定义、returned-only factorization 和成本。

新证书的 canonical 前驱恰为 C1/C2，综合稿的数学前提恰为这三项新 admission。原 checkpoint discussion、controller seed、旧 C3 和010 main/delta 仅作构造/版本/勘误来源。新证书 §§3–10、12 自足给出 primitive/program/resource 构造，既没有循环依赖，也没有用“有 envelope”代替实际实现。

这些结论仅支撑固定两个程序的完整**共同可用**预算，不能推为等实际消耗、componentwise efficiency、优化架构 lower 或任意 encoder lower。Root 仍有独立的后续 workflow gates，不因组件 admission 或本报告而完成全部 C4 工作流。

## 3. P1、P2：finite primitives、程序相同性与全闭箱：PASS

新证书 §§2–6 和 Appendix A 现已提供原提示要求的内容：

* multiplication 保留2w乘积；restoring division 在每步保留 w+1 shifted remainder，直到证明 quotient 范围后才窄化。表中最大 unsigned/signed 操作数目均被 `g(w)=1024w²` 包住，scratch 留 `32w+32`，不是 unit-cost word 操作。
* 每个 Boolean gate 有至多四层的 exact ReLU 构造；16倍允许 rails、routing、写目的地和清除，得到 `16G+32`。inactive live channels 有显式 identities，零系数也储存与求值。整数 scalar extraction 的阈值包括端点 A，不能只取 h 位。
* 两个有限 log 用 `q^(2p-1) product(2j+1)` 的整除 common denominator 生成。循环给两 log 合计 `<=32p+64` word operations；Blog/Tlog 的范围与全乘积、余数相容。生成发生在 acquisition 前。有限 recurrence 满足 `R_s<=W(S)<=6R_s`，`W(0)=R_s` 精确成立，A-scaled accumulation 不提前 floor。
* 四 causal singleton heads 在 query 分别取 m,m-1,N,N-1；历史 lag、prefix eligibility3..m、actual E_m/S_N、triple/flag features 均实际计算。P1/P2/T/U 的 finite scores/values 与 D2 完全匹配。head/value/QK/score 限额由真实构造承担。

逐项核对三张操作表；对 copied Program、MIX recovery、shared output，另做 AST 等同性核查，均与指定源程序相同。MIX 是63操作；JOINT 是15 word operations 加两个 control OR，落在18 allowance；shared output 是41操作。没有把 MIX 换成常数 decoder，也没有换 C1 的 JOINT family。

任意 independent `[0,A]^19` 输入均有 `den_i=2A-U_i in[A,2A]`；normalizer raw products `<=4A²,6A²`；D1、D2、DT 的范围分别为 `[A,4A]`、`[A,6A]`、`[A,2A]`。按实际 signed 指令推得 `H in[-8A,9A]`，故 scaled signed guard `[-16A,16A]` 足够；raw 6A² 并未被错误缩成 O(A)。clamp 后 snapping 给各 count `[0,M]`，不要求两 count 总和<=M。

shared41 对两个 counts 的全箱给 `2<=D<=2m-2`、`Z=4D`，所有 eager branches 的 divisor 均正。最近舍入 dividend `<16mQ`，ceil dividend `<8mQ`；Q2 的 unused nearest J 可以等于 Q，但最后 uniform MUX 仍给 positive output。这和 Q4 ties-up、zero count、两 count 总和2M 一起包含在证明内。输出确切写 `(Q-J,J,Q)` 对应的三个 `(b+1)` 位字段，未换成紧凑 b 位输出。

B=128p 只承担 acquisition/recovery；Q 与任意大的 b 首次进入 O 域。两个 count 的 `<=2ell+4` significant bit bridge 先窄化、再扩展，分别装入 WF-square/WO-square phase，未漏一个 WF×WO 巨型矩阵或把 b 强制等于2d。d 的 tau-bit descriptor 单独存储，未假定 d 可装入 B。

## 4. P3：实际 all-bank erasure：PASS

新 §7 已从原来的概略计划变为固定 public-bound COPY_TO_P / ERASE_ALL_OLD / external overwrite / READBACK schedule，覆盖 owned input/tail、one-hots、lags、features、crop/QKV、finite recurrence 与 numerator/denominator、clean masters/counts、控制副本、full-product/remainder、旧 port-preparation 和前一层 input/output rolling copies。P 的物理 padding 置零。控制只有真正的8个 endpoint one-hot bits。

四 rolling banks 共 `4nWF=4096nB` 个 B-bit scalar slots。逐 scalar sweep bundle 的 CONST、短 counter 更新/compare/reset 被 `512B+512<g(B)` 包住，故 `4096nB*g(B)` 支付完整物理 word 清零，而非把每个 scalar 误算作一个 logical bit。另 `1024(h+1)g(B)` 支付完整19(h+1)+8端口序列化、padding、回读和 controller cleanup。清除 scratch 由 primitive routine 自身完成，控制寄存器只含 public index；scan 顺序避免重新生成已清除的 source field。

在 Phi 时只 P 含 source-dependent predictor state。channel 内的 original-code 比较不算 predictor clean memory，也不可返回给 decoder；D3 正是将 arbitrary channel computation 留作外部、将 interface work 计费。READBACK 后旧 P、转移临时副本被清除。对各 history 和闭 returned box，后续输入因子化为

`q=D_(N,b,d)(Phi(E_(N,b,d)(history),controls),controls)`。

本项的物理结论来自上述实际有限扫描和 liveness allocation；不是由 Python alias/GC、semantic trace 的布尔值，或“变量后续未用”推出。新代码也明确区分 semantic interpreter 与该物理证书。

## 5. P4、P5：principal hybrid 与 D6 每个坐标：PASS

逐项核对新 §§4、6、8 与 D6。

| 坐标组 | 实际构造与核对理由 |
|---|---|
| input/binding/features、heads | 完整 batch 入驻；四 singleton adapters 加 MIX四统计头或 JOINT一均匀头；128 frontend 加4 phase，限额 `(8,4,8,4,2)` 满足 |
| E/T、有限评价 | `E_M=(256p+512)n²+1024n`，JOINT allowance 为 `512n²+4096nB+1024(h+1)`；实际 recurrence、value accumulations、mask scans及物理擦除都各有步骤承担，E_* 是二者之和再乘已证 g(B) |
| widths / physical words | MIX全部 named registers与 rails、extracted bits及 scratch 小于384B channels，output小于256O；WF=1024B、WO=1024O，四组 full physical banks 留足同时 copies |
| masks / metadata | 四 n-square singleton masks 加最多四 nm-square prefix masks；Z_* 的 public records 包括 crop、19 slots、endpoint/loop/word descriptors和完整 tau 字段；无源参数或 data-dependent标签 |
| 地址 / code | 在线用固定 segmented tuple fields；a_* 覆盖 layer/gate/position/channel/bit fields。code 分双域 primitive wiring与有限 loop/literal records计入 K_*，不是免费 runtime lookup。巨大 tau 记录可保留在 dormant public storage，不要求每 online gate 读取它 |
| D_* / P_bits / I_* | dense tied coefficients 每层存一次，含零和bias；先 batch 后 query 的 `I_*=132nWF+LF WF+LO WO` 与 active schedule 一致；双域桥在同域 square envelopes 中付费 |
| online work | dense full-word multiply-add 有256w²界，先前端 n slots、query recovery保守多乘 n、最后单 output bank，再加独立 T_*。额外 n 是 work overcharge，未据此把全 token history 留到 cut 后 |
| storage / online peak | U_* 含参数、code、masks和stored metadata，W_run含四 batch/四 output physical banks及working metadata；peak_run是两者之和，不是取max或只算cut capacity |

保持的是 **principal extracted-query one-shot batch hybrid dense tokenwise**。没有把 streaming widths、padded all-phase holds、globally flattened neural depth 或 unit-cost arithmetic 偷换成 D6。本报告也不从这组充足上界推断最优资源结论。

对任意 b 与 d 的说明是全域证明的必要部分：b 可使 O>B；tau 可使 a_*>B。证书没有将所有地址挤入 B，也没有声称 a_* 是整个 U_* 的 flat pointer。大文件/flat生成地址用下一项 A_gen 另付费；有限 evaluator 自己的短 scan indices 仍在 B 内，output 内的相关短字段在 O 内。

## 6. P6 与 N3–5：offline 和真实早分支：PASS

§9 的 generator 给出 log common-denominator算法、public参数处理及 lexicographic layer/row/column/bit 枚举；实际写 dense zeros、identities、mask entries、primitive/phase code、metadata 和输出字段。gate expansion iterator 的有限 arithmetic/index 操作通过 full-word schoolbook 构造计入每 emitted step 的4096 A_gen²界；输出bit数、delimiters和layer advances由 U_*+L_*+1承担。A_gen显式含 log(U_*+L_*+1)、Blog、B/O和全部公开输入长度，scratch及 **stored+scratch** peak也有有限公式。未使用 coefficient oracle 或免费 compiler。

§10 和 `build` 的公开 N<6 条件先于 parameters/frontend/cut/recovery builders；无 prefix、E_m、假 counts或第六 observation。真实读N位、初始化输出、写 Q/2,Q/2,Q 三字段并清除输入。其独立小账本 depth16、width32、physical beta=O(6,b)、code/metadata/work/generation/peaks 均明确给出。

其与 Bstar(6,b,d) 的全域比较不依赖代表点：O=32(b+11)相同；大账本 output width≥1024O、LO≥16*41*1024O²，直接覆盖小账本参数、dense work及额外 serial writes；Z_*、K_* 的 b/tau系数覆盖小账本；rolling banks和各 simultaneous peak按非负项相加覆盖。U_s<=U_*、a_s<=A_gen及公开平方项比较给出 generation work/scratch/peak。Bstar 的6只作成本 allowance。

## 7. A：三强替代的完整独立价格：PASS

§12 的三构造均改变 encoder/error placement 前计算，未被解释成冻结 FULL19 的 decoder，也未声称自动 fit Bstar：

| 替代 | 已核对的数学身份 | 计费入口 |
|---|---|---|
| gain g=M/A | 实际 finite zero-score evaluation 的 full numerator `A R_s M C` / denominator `A M R_s` 给 j=C；无 premature rational floor；C<=M<A，但不声称都锁定 | source features、eight counters、gain literal/full products/division、R=8(h+1)完整字转换及 post-decoder |
| count packing | ell_C=ceil log2(M+1)，R=8ell_C<=19kappa 时每word<2^kappa；任意 correlated admissible map 均锁定 | source counting、固定长度 serialization、全H port、读回/解包、guarded shared41 |
| output packing | pre-cut 计算 exact shared41、得到1<=J<=Q-1的 b-bit payload；b<=19kappa 时锁定 | pre-output selection+41、serialization、全H kernel、post-clamp/Q-J/literalQ及最终3(b+1)字段 |

gain/count 的 off-image decoded counts clamp 到[0,M]，output 的 off-image J clamp到[1,Q-1]，全箱均定义。gain 并没有被夸成任意 count 锁定的可靠性定理。

ten-stage kernel 的动作逐项为

`H + 2R + 16 + W + 0 + (R+8) + 3H + H + (2R+16) + H`

恰等于 `K=6H+5R+W+40`。H固定为完整 `19(h+1)+8`；step1全高位初始化，step7读全返回word，而非只读低kappa位；step4清全部source，step8、10清P/T。对锁定image完整word固定，对任意returned box后续只依赖U，不从旧source恢复。

**K只是逻辑transfer费用。** 新物理加强项 `(K+20S+1024)g(beta)`另支付每个full beta-bit scalar的初始化、pre-cut non-P purge、returned duplicates purge、最终nonoutput cleanup和retained handoffs。五组各四 S-word sweeps覆盖四 rolling banks；每组实际C=S+8的spare差额总共160 words，1024额外allowances仍覆盖它及controllers/latches。handoff至多四次，每次retained< S，属于第五组，不额外保留clean input layer。每 sweep bundle含短index更新和整word读写，成本<g(beta)。因此物理duplicate清除不是重复叙述逻辑K，也没有用host GC替代物理store。

W、S显式覆盖输入/features、counts/output/rails、P/T/U、compiler scratch与copies。G_acq、G_pre、T_transfer、G_post分别承担 acquisition、前移的output/转换、物理kernel及post输出；不能相互借“免费复用”。beta含 p,b,ell,tau,h，且证明 a<beta，address arithmetic无需未收费的大字域。完整 Z/Kcode、dense parameters、LC holds、online full-word work、stored+working peak及 A_alt/Emit/Tgen/Wgen/peakgen，均在独立alternative vector内；physical transfer另加一次work是保守双收费，不漏项。

在原比较 schedule，kappa=d、h=2d+82、ell_C=2d+73，count充分条件化为16d+584<=19d，整数阈值d>=195；b=2d<=19d也满足output packing。没有把充分条件误写为所有重编码的必要下界。h≫kappa时完整H仍进入K、W/S、physical sweeps、trace/code和generation；原 `O(R+19kappa)` 不再承担完整费用。

## 8. 原 tuple、same Phi / same t*、勘误：PASS

对每个整数d>=32，原tuple为 `N=2^(2d+74), b=2d, Q=2^(2d), u=2^(-d-16)`。`M=2^(2d+73)-2`，`Mu²=2^41-2^(-2d-31)>2^40`，`Nu=2^(d+58)`，同时位于C1、C2、D6；A/p schedule未更改。

先为tuple选C2的全域admissible Phi_*；随后针对**本具体 MIX63+41 decoder**取同一个conditional witness t_*，同源平均下界由R_av>=u R_00给出。再对JOINT在完全相同Phi_*、t_*下用C1。C2 map在整个19-word/control闭箱以逐坐标guard定义；对JOINT零padding的非零replacement被拒绝。程序没有要求两个encoder输出同code，也没有另选JOINT noise map或另一个风险witness。

完整有限代入仍为

```
U_av=(12000000*2^-74+259)eta²<260eta²,
U_av/(u/64)<260*2^(22-d)<=260/1024<1,
U_00<2^(-d-37)+2^(8-2d)+3*2^(-4d)
     <=2^-69+2^-56+3*2^-128<1/64.
```

因此同source/map下JOINT `<u/64,<1/64`，MIX `>=3u/64,>=3/64`，两gap严格`>u/32,>1/32`。比较属于两个真实程序的同一完整**可用**vector，未夸大为等消耗。

恒等式 `1800000/(1+Nu)=(1800000/2^58)eta/(1+eta/2^58)` 表明显示conditional upper总表达式为Theta(eta)，不是O(eta²)；只有noise项是O(eta²)，average expression为O(eta²)。这是upper-expression速率，未声称真实JOINT risk的matching rate。来源010原 §11 第601行的错误 both-quadratic 句及旧main漏看，均原样保留；delta第18–25行明确承认漏看并要求勘误。新综合稿与certificate没有改变tuple掩盖它。

## 9. Primary mapping、验证范围与残余不确定性

新 §13 与固定Counter primary-map的版本和位置一致：Higham1993 (1.2),(2.3)–(2.5),(3.6)仅operationwise arithmetic/cancellation背景；BHH May15,2020 manuscript Algorithm3.1、Theorem3.3/(3.6)仅给定输入normalization背景；van Erven–Harremoes arXiv v2 (6)–(7)、Theorem30/(52)–(53)为classical order2/chi-square/variational关系。没有增加第四来源或拿这些文献代证D1 risk、D3整数通道或Bstar。三PDF及文本本次只重新核字节身份，未重审无变化全文；actual数学依赖是已接纳新C1/C2及本次检查的新自足构造。

新补充 `root-package-audit-v1.py` 只做必要的package/interface转写检查：84引用/73路径hash、三canonical内的exact local body与前驱、copied AST相同性/63-15-41操作数；一个h4096/kappa6的full-H kernel，六个b4097/tau16385的N3–5早分支及small-ledger比较，以及N=2^4096、h4104/kappa6的alternative ledger检查。结果写 `root-package-checks-v1.json`，全部通过。没有调用原完整diagnostic脚本、旧统计或minimax程序。这些有限点不是全域证明，semantic erasure trace也不是physical erasure证明；全域结论来自上文逐项核对的有限算法、范围与账本推导。

残余数学不确定性是 LLM_CHECKED_PROOF 层级本身的可错性：本包没有kernel-checked形式化，也没有执行巨型N实例来实测硬件资源。固定表和有限compiler/generator上界承担构造证书，Python仅承担语义/转写核查；PASS仅限声明的exact arithmetic、one-shot hybrid与局部整数cut模型。不推论IEEE/learned/all-layer robustness、practical constants、novelty或optimized neural advantage。

**必要数学repair hints：无。** 未找到应新建 `record_obstacle` 的具体缺口，因此不以措辞偏好、历史freeze状态或gateway词法symbol扫描作数学否定，也不重记已由新证书实质补齐的原diagnostic。`a607ba0f8dab12f83e8d70e62c19311f8721c87b854b4661b23aaad40c2e70ee` 与原失败/SUSP记录均保留，不由本discussion修改。

本次新增Fact IDs=[]，新增Evidence IDs=[]，无root/route状态变更。后续仍需独立的root admission、完整reservation的native final_audit和责任会话 `[redacted routing identifier]` 真实receiver-pull科学交接。即便将来stage4 SOLVED，T1–T3母问题、优化encoder/resources、小参数域与独立learned/all-layer问题仍未由此完成。
