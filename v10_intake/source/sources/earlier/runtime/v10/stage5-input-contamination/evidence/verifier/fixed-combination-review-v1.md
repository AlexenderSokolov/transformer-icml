# 本阶段新固定完整组合：独立 FILE-SCOPED 复核 v1

Verifier，2026-10-26，保持 `[redacted model routing]`。结论：**FILE-SCOPED PASS**。

本结论针对下列固定全文中的数学证明、有限实现及原 D5 分别定价的完整资源声明。全文逐段读取并独立核对后，未发现需要阻止数学组合的承重 gap。发现一处非承重的章节引用笔误，列于末节；不修改固定源文件。此报告不产生 Fact/Evidence，不是 root admission 或 final_audit，也不确认责任会话 handoff 已发生。

## 1. 固定对象、原生读回及独立性

| 固定对象 | bytes | SHA256 |
|---|---:|---|
| `lead/fixed-full-proof-v1.md` | 163186 | `a7c4e4194e68b186cc3cd6a3bdf8e0b9bfb01c0a1981427c588e1e9a38a1b7ae` |
| `lead/fixed-combination-v1.md` | 18305 | `023534f2978bee9d8132100c1cdd4a85c9208d1afa1a99924dd510617915a553` |
| `lead/fixed-combination-manifest-v1.json` | 10356 | `0596e9f1bd16bbb9c7c132e70a959cdc2147b133580bf9aad72282a657cb288e` |
| `inputs/STAGE_DEFINITIONS.md` | 15528 | `fc104078b9455bdd86586decd50902df6688400cc00f06e6b105699efefd0e02` |

表中 `lead/` 均相对于 `outputs/001-input-contamination/`。以下行号均指固定全文，章节号特别标明所属组件。

本轮先调用 `euler_team_research_state` 读取精确 root、scope、budget 与 evidence。live frontier 为 `47764359856c626063a362ea0f080309b80ec551ea175c80134fbb6996945041`，与固定清单一致；root `881d17365a7019add4410343d568625dacae67d26aa17548bda2de7f9b860dbb` 仍 OPEN、VALID、无 root evidence，acceptance=null。三项组件状态、evidence content hash 与固定清单匹配：

| 当前组件 | Fact ID | Evidence ID | 回读 |
|---|---|---|---|
| C1 | `f9e055bd405c4b56` | `61f169db99848f6794e334ea287037fae00a592f4b5e5254d580c0b9f74a599f` | DISCHARGED / VALID / LLM_CHECKED_PROOF / PASS |
| C2 | `df40a215d931bd32` | `3448f22a5b9e86526c831f0518a83b828eaf69eb2acf455fb0057f354dae7cd3` | DISCHARGED / VALID / LLM_CHECKED_PROOF / PASS |
| C3 | `39367951834d7aa7` | `426929d6b208d95764b59cd20f658f51c91334448c86cfb5cdb9b8bf2d5e4b00` | DISCHARGED / VALID / LLM_CHECKED_PROOF / PASS |

逐字节核过固定清单的28个 artifact、三组件 authored/canonical 六个 hash，以及新 C3 manifest 的十三个 source/artifact hash：全部匹配。三个 canonical Fact 均有 `predecessors: []`，且包含各自 authored proof 的完整原字节。固定全文包含准确根、未改 D1–D7、三份 authored proof、C4 combination 和 D6 map 的原文。实际 C3 authored hash 是 `5ac089baa1a28d2f89db223e16542ba43ac153c6930e81806c6627d0e0e22827`。

这些原生接纳记录仅确定当前证明与前驱身份，不预定本轮复核结论。独立核对对象是这次新全文，不是准备单、旧012组合、affine 方法讨论或旧 root。配置通过 team members 只读确认；没有调度其他模型代替独立审阅。

## 2. C1：clean、真实末态与污染/grid 的完整组合

**PASS。** C1 自足推导位于第166–750行。

1. 第263–306行直接验证 `pi P=pi`、真实 reverse kernel 和三步共同原子。第308–342行用 stationary path telescoping 和共同 backward kernel，将 S_m 的混合界转成整个 `X_1^m` 的 TV 界；没有只控制 endpoint 后遗漏 prefix，也没有以稀有质量 pi_s 放大误差。clean loss 用真实有限 cap 乘 TV，末态权重是同一轨迹的 u,w。
2. 第346–418行分开证明 spaced-visit tails、确定 horizon 的 martingale 二阶矩和固定 row-stack 的事件包含。`C=B_s(D)` 可以使用，但没有声称 `C|D` 为 binomial。访问阈值是 proof 中的确定整数，不提供给算法。
3. 第448–500行实际承担 row10 的任意稀有 successor `p=r`。在 `H={D>=d,C<pd/2}` 上，以 `y=pd` 用 `kl(p,q)<=p log_+(p/q)+4q`，配合 `q>=1/(M+2)`、`q<=p/2+1/d` 得 `[y log_+(256y)+2y+4] exp(-y/8)/d<=108/d`。因此 p 趋0 时仍有统一 `O(1/M)`，没有留下 `log M` 的不受控乘项。good-success、low-visits 两项另用二阶矩和访问尾界。`K00<=50000/(1+Mu)`、`K10<=400000/(M+1)` 及第502–522行 clean actual-terminal `1000000/N` 的常数衔接成立。
4. 第524–569行逐输入、逐 seed 分别计算 triple indicator 与 row indicator 的3k扰动；row 界不是两个 cell 界相加。`alpha=3k+1` 使两个 raw 坐标由同一 gamma 支配 clean add-one 坐标。互补 clipping 区间保留另一坐标的相同比例，包括 row10 的单侧 clipping。对实际 S_N 应用路径上 KL 界合法，因为最后 pair 每 seed 保留；dirty E_m 没有被当作 clean。
5. 第571–627行先消去通道，再仅对 clean reciprocal `1/(D_s+2)` 使用 whole-prefix bridge，范围 `[0,1/2]` 给误差 `d_g/2`。没有把 Z、channel coins 或 dirty counts 当 Markov。k>=1 才启用 M>=1024 的 tails；k=0 由路径项严格为0处理。真实权重给 `(8192/3+96)/N`，乘9k正好为 `25440k/N`。
6. 第629–750行在独立 closed count box 中证明所有 eager candidates 有定义、非负 SUB、正 divisor、完整 dividend 与 grid positivity。Q=2 的 discarded nearest candidate 可以有零坐标，最终 uniform MUX 恢复正输出，不计算其 log。Q=4 half-up ties、单零/双零 counts、ceiling residual 0/1、N=3,4,5 实际 uniform branch 均已覆盖。

row00 grid multiplier 为16/3，row10 的两坐标比例只加2/Q；结合后的确为

`R_av <= 16000000/(3N) + 135680 k/N + 3/Q`。

这是一族未知参数的 Z,N,k,Q-only 规则，对全部合法 source/channel 成立；证明没有替换 terminal query 或为算法提供 clean side information。

## 3. C2：完整路径、一张共同 K 与同源双风险

**PASS。** C2 第813–1267行独立承担其全部前提，不依赖 C1 或历史 FULL19 下界。

第920–1002行直接验证 stationary reversal、三步共同原子、mixing 和真实 `S_N=00` 条件的完整 reverse path。`A_j=S_(N-j)` 包含每个中间 pair；第1128–1136行的 first-coordinate 映射覆盖所有 free symbols，包括 X1。

第1004–1079行的 adaptive construction 合法：matched boundary 用 rational maximal 一步 coupling；mismatched boundary 起点即承诺三步，endpoint 后按真实 conditional bridge 抽两个中间 pair，内部意外相遇不改长度。零 endpoint 概率不执行除法。余下不足三步时抽完整 block 后截 prefix。固定 j 的证明按最后 block start 与已承诺长度分割，只条件于一条链自己的 block prefix，然后积分 joint start past，得到该链完整 Markov law。没有对两链中间历史同时条件化后错误断言 Markov 性。

第1081–1144行的97计费保留末 partial block 的过量计数，不假设 episodes 独立。birth 求和使用已证出的真实单链边缘，得 full-history Hamming cost `C<=10000(1+Nu)Delta`；代入 `Nu=k` 后 `C<=(1+k)/64<=k/32`。

第813–918行的 finite residual construction 保留 Jordan 总质量 `tau=TV(P,Q)`：先去正 cycles，再 DAG path decomposition/collapse，Gamma 的 marginals 恰为未归一化 mu_+,mu_-，费用不增。没有直接限制原 coupling 到正负支持，也没有遗漏 tau 因子。

每个实际 input 只有一张固定 row K。good edge 两端送同一显式 Hamming midpoint；bad fractions 留各自输入；zero residual rows identity。共有质量 m=min(P,Q) 经相同 K 后线性相消，故

`(P-Q)K = sum_bad Gamma(x,y)(delta_x-delta_y)`，

且正负 bad residual 支持分离，`TV(PK,QK)=B<=C/(2k)`。midpoint 输出碰到其他 input 不破坏此恒等式。有限 rational rows 的共同分母 integer seed 分区，使每 input/每 seed 的输出均在硬 k 球内；其他 terminal fibers identity。此合法性不是从平均 transport cost 推出的。

第1146–1199行将 reverse coupling 仅用于离线构造 public(N,k) 表，不在 runtime 根据 actual label 选择 plus/minus 攻击。T 不依赖 Q、predictor、实际 hidden label，对所有其他 D1 源产生的输入仍合法；其计算费按 D2 在预测器外。

第1201–1237行对任意 full-Z randomized predictor 加 fresh independent coins 后做同一测试，错误和至少63/64。先选 conditional-risk witness，再在同一源用 `Pr(S_N=00)=k/N` 得平均风险。由此一个 SAME t_* 同时有 `R00>=Delta^2/8` 与 `R_av>=c k/N`。允许 unrestricted outputs/infinite KL，无需把 baseline 限制为19个内部 words。

## 4. C3：原语、literal affine renderer、完整 finite generator

**PASS。** 本次审阅的是新 C3 §§1–11 的实际证明，尤其第1497–2354行的构造链，未将旧 source 的“admitted”用语当作当前前提。

### 4.1 精确语义与有限算术

第1356–1442行完整打印 JOINT17、DIRECT8 和 common46 表，保留付费 CONST0/CONST2，五项 alpha 构造及 literal1 的 Q-1/Zden-1。DIRECT acquisition 在54项之外另计；JOINT frontend/evaluator 在63项之外另计。

第1444–1495行对独立 j∈[0,A] 证明 snap 范围，对 actual Z 的 j 证明 exact snap。独立 C0,C1∈[0,M] 给 `D<=3m`、`Zden<=12m`、nearest dividend `<32mQ`、ceiling dividend `<12mQ`；不借用可实现 count-sum 条件。大 Q 增加 beta 并支付 frontend 物理宽度，Q 的 endpoint bit 保留。实际 guarded-port 是3(b+1)位的逐位相同输出。

第1497–1608行给具体 carry/borrow、in-place-safe ADD/SUB、full 2beta product、full numerator/quotient restoring DIV 及 beta+1 shifted remainder。地址/控制收费与 logical gate 分开。迭代器的 sharp logical counts 可直接由有限 loop 逐项相加：MUL 为 `14w^2+12w+6`，DIV 为 `20w^2+49w+14`；乘至多5个 bit-data actions 并加 copy/clear 后仍在 g=1024w² 内。scratch 的实际上界低于32w+32。产品、trial remainder 和 quotient 均在静态 range guard 之前保留完整宽度，没有用 modular Python 语义替代。

### 4.2 literal 系数与 alias

第1610–1695行以两层实际 affine/ReLU 模板编译 Boolean basis，不先转 NAND 后增加未付层数。所有 coincident column terms 相加；因此 x=y 得系数2，MUX 的 y=c 得 cancellation，destination 可以 alias 任一 operand。第一层保留旧 data，第二层才写 dst 并归零 s0/s1；旧 scratch 非零不破坏计算。

每个 absent entry 实际生成/求值为零，identity rows 也生成并付 holds。augmented constant row 是付费 affine convention，由 literal1 参与 MAC，不伪装成 W 之外的未付 activation。scalar extraction 逐位保留 j=A 的高位，先用独立 remainder，再在最后写 bit0，避免 scalar/bit alias。该构造足以支持固定 G 与 L，无需未证明的 compiler oracle。

### 4.3 Z-only acquisition 和银行生存期

第1697–1857行给 frontend 的具体 slots、四个 causal singleton masks、两AND triple features、dirty terminal/prefix controls、prefix index-map 和第五个 finite zero-score head。head 分子 `A R_s C_sc(Z)`、分母 `M R_s`，精确得到 j；所有 mask entries 包括零均读写。128 construction layers 加四 phase layers、五 total heads/最多四 simultaneous、value8/QK<=4/score0 与 D5 一致。synthetic query 不是第 N+1 个观察值。

DIRECT 真实拥有 full Z，显式遍历每个 eligible triple 及全部八 labels，计数器归纳给相同 C_sc(Z)。端点只从 owned Z 来；没有 clean endpoint、预计算 triple table 或 source-dependent counter address。

第1859–2004行保留 full a-bit records，并分别证明 JOINT、DIRECT 和 SMALL 的地址界，未把 DIRECT 的 G 套入 JOINT 地址证明。query ranges、renderer scratch、P 和 port 地址分离。四个完整 nW beta-bit physical banks 先同时计费；P copy 完成后扫描清除全 source-bearing 非query state，才 release nonquery positions。最后 port 写完，再扫清包括 old buffers、controls、MAC/controller data scratch 和旧 numerator 的所有副本。public scan indices 之外没有 source-dependent pointer 或未清 data。高 physical padding bits 也被处理。

### 4.4 原 D5 每个坐标

下表定位实际证明及收费对象；第2006–2055行 R1–R4 与原 D5 公式逐一相同。

| D5 坐标 | 新 C3 中已核的承担对象 |
|---|---|
| ell,tau,n,s,beta,g | §§1,2,3：任意 legal N,k,b，exact bitlength/word widths，固定 g=1024beta² 与 scratch32beta+32 |
| DIRECT G/core；E,L,W,dense_slots,P_bits,mask_bits,I_holds=0 | §5.2：owned input、八label scan、dirty controls、8+46、metadata/port/cleanup；packed memory 未被零 neural 坐标免单 |
| DIRECT W_work=8N+8192beta+Z_meta | §§5.2,6,10：input/copies、八counts、54 SSA、完整算术scratch、地址/控制及port同时存在 |
| JOINT W,G,L | §§3–6：63项、paid scalar extraction、初始化/copy/clear、literal renderer、padding matrices/holds，W=2048beta、L=16G+96 |
| JOINT E | §§5.1,7：512n² evaluator余量、16nW batch passes、256W query passes、serialization/literal项；word bundles 乘g，非 neural depth |
| dense_slots,P_bits | §§4,8.1：132 frontend matrices 在n位置，L query matrices 在1位置；每个零/identity/bias和 redundant row均存储/求值、每 coefficient beta bits |
| mask_bits,I_holds | §§5.1,8.1：4n²+(m+1)² 全 masks；active identity holds 132nW+LW；旧buffer residence另付storage |
| JOINT core | §8.1：signed full-product/full-accumulation MAC 的256beta²界，所有 dense entries 加 E*g，不作 sparse discount |
| JOINT W_work | §§6–8：4nWbeta+Z_meta，包括 Boolean neural channel 的整 beta-bit scalar、B3 evaluator、copies/port和同时峰值 |
| a,K_code | §§6,9,10：segmented full-width records；至多24 primitive wiring types，每类至多g records；<512 descriptors；完整 padded instruction/operand/coefficient fetch与dispatch |
| Z_meta,U_stored | §9：public metadata 两份64×8s records/token；stored code/constants/dense/masks/padding；dirty data不藏入metadata |
| T_online,peak_online | §§8–10：4096(a+beta)² surcharge支付 bitwise addresses/controller/fetch；stored arrays 与 working banks 同时保留 |
| a_gen,Emit | §11.1–11.2：独立 flat generator address，不截成runtime a；public expression tree、原语/SSA/row/column/bit counter automaton及付费 transitions |
| T_gen,W_gen,peak_gen | §11.3：每 bit/record/layer delimiter 有界 track操作；恰U_stored stored bits、最多L+1024其他units；生成中的program与全部working一起保留 |
| N=3,4,5 分支 | §§1,8,10,11：不实例化prefix参数/head，仅实际N bits的packed uniform；原small G/core/work及全部zero neural坐标 |
| output,GPU | §§2,7,10：fresh3(b+1)位LSB-first port，positive numerators和为Q，清除其余source-bearing状态；GPU0 |

### 4.5 从原语到完整 generator 的实接

第2095–2145行的 library/code 记录是可展开 finite wiring，不赋予 MUL/DIV 单位硬件成本。`1536g(beta+a)` 的 library records 在固定 K_code 第一项内；其余 descriptors、literals、padding 在第二项内。a-bit runtime addresses 放 controller/code，不能塞进8s metadata fields。

第2147–2194行把 basic data work 与地址/fetch/dispatch 的完整 bit cost 分开。a<2beta 是实际证明的界，并非以a=beta替换。整条 execution 的额外费用落在原 `4096(a+beta)^2*core`；packet 按字段流读，不需另分配64(a+beta)的 live record bank。

第2196–2354行提供完整 finite counter generator，含 public cap expression 的非单位成本求值、primitive microsteps、SSA state transitions、每个 literal coefficient bit、frontend/extraction rows、masks、metadata、padding与port wiring。collision 使用项求和，非黑箱 next-coefficient。所有不直接 emit 的有界 transitions 被附到真实正长度 record/bit 或 layer delimiter；未留下 uncharged seek。per-unit counter operations 自己以 binary tracks 展开，而非循环假设大word地址免费。`Emit=U_stored+L+1024` 支付全部 stored bits 和额外 delimiter/header units，online/offline simultaneous peaks 均在原公式内。

因此本轮没有发现 C3 以新包络替代 D5、把 scalar bit 与 packed bit 混同、免费 masks/zeros/holds、提前释放银行或依赖 Python GC 的情况。这里的 PASS 是 analytic constructive proof 的复核，不是把 companion Python 当硬件实测。

## 5. C4、强 DIRECT 与 D6/D7 范围

**PASS。** 第2439–2482行先用 C3 的逐 z guarded-port identity，在同一 source/channel probability space 上得到样本逐点 KL equality，包括条件于真实 S_N=00 的风险。再将 C2 用于单一 D3 map A，所选一个 t_* 因此同时适用于 JOINT 与 DIRECT。C1 对同一 T、同一 source 的上界也成立。这不是分别为两实现选两个 witness，更不声称对所有 predictors 有一个共同 witness。

`T_(N,k)` 先于 Q/predictor 固定，witness 可依赖该 predictor 与 Q；对任意 full-Z randomized predictor 的 stronger lower 保留。污染 contribution 的 O(k/N) upper 与 full-Z Omega(k/N) risk lower 没有被升级为每个 predictor 的 attacked-minus-clean 差下界，也没有宣称匹配1/N或1/Q下界。

第2526–2540行与 D6 map 保留强 DIRECT、两种独立资源模型及所有排除项。三个 primary PDF 的实际 SHA256 与修正后的引用匹配；本轮只读本地 pinned primary text 的有关段落核对：CGR 的 iid Huber neighborhoods/TV testing/modulus，Pydi–Jog 的 class-dependent point maps、distribution attacks、transport-tail和submeasure论证。整条 dependent trajectory 可以是一个 feature；dependence本身不构成 novelty区别。有限Hamming midpoint和一张common hard-budget K由当前C2自证，未把一般OT结果的范围偷换过来。没有新增文献检索或发表新颖性判断。

[Non-scientific operational metadata omitted.]本轮 native root 仍 OPEN；此 FILE-SCOPED PASS 不 discharge D7 后三项。[Non-scientific operational metadata omitted.]新 C3 的既有接纳不被解释为恢复旧任务。v10 母问题的 T1/T2/T3 综合仍留待责任会话。

## 6. 实际 gap、非承重笔误和执行边界

- **阻断性数学/实现/成本/scope gaps：无。** 不要求修改固定 D1–D7、三项新证明或数学串联，才可给本范围内 PASS。
- **一处非承重章节引用笔误：** 固定全文第2512行（combination §5 的 DIRECT 行）写 `C3 §5.3`；新 C3 的 DIRECT paid batch scan 实为 `§5.2`，见全文第1822–1857行。实际正文与收费均已存在，故不影响证明。若未来重新出编辑版本，可改该定位；本轮不改已锁文件。
- 没有重跑旧诊断或作者的既有拼接检查。新迭代器的循环次数由上文逐项代数核对；未执行机械穷举。使用本地短脚本核验固定哈希、嵌入、header 和 scope。
- 返回前再次核对固定源字节与审查文件，未发现审阅期间源文件漂移。没有声称测试样例构成全域证明。
- 本报告本身未产生新的数学 Fact 或 Evidence，不表示后来已完成接纳。

FILE-SCOPED PASS 仅针对本次锁定文件的数学审查，不证明后续组合接纳已经完成。本次完整报告与 companion manifest 锁定所审文件和结论。
