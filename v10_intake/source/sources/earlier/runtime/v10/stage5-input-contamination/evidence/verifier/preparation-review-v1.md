# 独立 Verifier 准备单 v1：clean/finite 接口边界

2026-10-26。本单只审当前 D1–D7 与首个数学 checkpoint 的接口充分性；不是 C1/C2/C3 固定组合复审或最终接纳。本单是研究讨论，不产生 Fact/Evidence。

结论：在“列出的承重接口由当前项目自足证明承担”的解释下，未定位到必须修改定义、量词或 checkpoint 的具体遗漏。不能把这个结论解释成接口已经全部证明，尤其不能把 checkpoint 的 D5 对照表当成 C3 成本证书。

## 固定对象及来源边界

| 对象 | SHA256 | 本次作用 |
|---|---|---|
| `inputs/STAGE_DEFINITIONS.md` | `fc104078b9455bdd86586decd50902df6688400cc00f06e6b105699efefd0e02` | 当前 D1–D7，全文读取 |
| `outputs/001-input-contamination/lead/mathematical-checkpoint-v1.md` | `25499c426e891a348f3382e572b55ed4587581cf865597282c0a029220c401f7` | 当前准备单核对对象，全文读取 |
| `inputs/source-stage4/outputs/001-relative-code/prover/c1-proof-v2.md` | `f8f6a56b4b458ff3d0033fa8cd29d27e3e32067dd643c2a9e51ba411ed6dadcf` | 已 SOLVED clean 来源；只读有关推导，包括修订后的 Appendix R |
| `inputs/source-stage4/outputs/012-input-contamination/verifier/combined-review-v1.md` | `3a35311ecb0bcb0567a1b14f2aa245ab0570986229663d71064bc46921ad64fd` | 固定 source review，非新项目 admission |

另外只读本地复制的 source012 upper certificate 与 common-channel lower 的有关段落，用来定位接口，不重跑其代码或 diagnostics。没有访问复制来源以外的旧 campaign。新组件只读取 gateway/readback 和 Fact 头部以核实原生状态，没有提前复审其完整新 proof。

## clean row10：低 success 事件不能只用访问尾界

定位：checkpoint 第38–48行；D1 第3行，D3 第19行。未知参数允许 row10 next-zero 概率 `p=r=ut/w` 任意趋近0；不能将其当作 interior Bernoulli row。

checkpoint 第44–48行正确地区分了两个必要工具：确定性 horizon 的 martingale 二阶矩，和固定长度独立 row-stack 的事件包含。所需包含为

`{D>=d, C<p*d/2} ⊆ {B_s(d)<p*d/2}`，

其中 d 是确定整数、`C=B_s(D)`，右边才涉及 d 个独立 Bernoulli(p)。`C | D` 不是可以免费使用的 binomial law。

第48行明确将 logarithmic loss 留为当前 C1 的责任，未省掉该承重接口。具体必须展开的低 success 估计可定位于 source clean §6.2/Appendix R：令 `d=d_vis, y=p*d`，在 `H={D>=d,C<y/2}` 上，`q>=1/(M+2)`、`q<=p/2+1/d`，并用

`kl(p,q)<=p log_+(p/q)+4q`，

得到 `E[loss;H] <= [y log_+(256y)+2y+4] exp(-y/8)/d <=108/d`。这才在 p 趋0 时保持 `O(1/M)`；不能以单独的 `log(m)*exp(-p*d/8)` 代替。good-success、low-visits 两项分别仍需 martingale 矩和 spaced-visit 尾界。checkpoint 已要求自证 `K10<=400000/(M+1)` 及 `K00<=50000/(1+Mu)`，而非从旧 Fact 状态导入。

该段是对待证接口的具体化，不是本单新接纳的统计引理。

## whole-prefix 桥和污染上界的量词

定位：checkpoint 第27–36、48、50–66行；D1 第5行、D2 第11–15行、D6 第83行。

整个 clean prefix 的 bridge 必须由 stationary reverse path 推出，不能只比较 endpoint 后丢掉 history，也不能除以稀有质量 `pi_s`。checkpoint 的 U2 明确给出了全 prefix 版本。

新增污染项使用 bridge 的对象只为 `f_s(X_1^m)=1/(D_s+2)`，范围 `[0,1/2]`，所以 conditioning 误差至多 `d_g/2`。它不作用于 Z、T 的 seed 或 dirty count。通道可依赖全历史与 terminal pair；逐输入逐 seed 的 U1 先成立，再平均独立私有 coins，正好覆盖所有 D2 随机 batch channels。

“只作用 clean reciprocal”限定的是这一步新增污染项的 transfer。clean comparator 风险本身仍可用 U2 转移其 clean loss，但必须分别乘上第48行给出的真实 loss caps；这里没有把 TV 误当作 KL cap。

row 与 triple 指示量各自给出3k界，不能由两个 cell 相加给 row 的6k界。两坐标共同 domination 经互补 clipping 保留，包括 row10 的单侧 clipping。最后 pair 由 D2 逐 seed 保护，所以使用真实 S_N；dirty E_m 不获得保护。k=0 不调用大 M 尾界；Q=2、Q=4/ties/zero counts 和实际 N=3,4,5 uniform 分支已分别列出。未发现这里将 actual terminal query 换成独立 query。

## C2：完整 adaptive 边缘、未归一化 flow 和一张 K

定位：checkpoint 第80–114行；D2 第11、15行，D6 第83–87行。

第84–90行保留了完整三步 block 的两个 intermediate pairs、起点即承诺长度、内部相遇不提前停止、最后不足三步抽完整段再截 prefix。固定 j 按 block start/已承诺长度分割后，只条件于单链自己的 block prefix，再积分 joint start past。这是完整单链 Markov law 的论证接口；不能改成对两链的 intermediate history 同时条件化。未选中的零概率 endpoint 不需要执行 conditional-bridge 除法。符号映射 `X_i=first(A_(N-i-1))` 覆盖全部 free bits，包括 X1，费用不是 skeleton/count/population alias。

第92–98行的 episode 计费不要求 episode 独立；每 episode 期望97、birth 求和所用 mixing 必须针对刚证出的真实单链边缘。代入 `u0=k/N` 后，费用 `<=10000(1+k)Delta <=k/32`；常数不依赖 Q、预测器或实际 hidden label。

第100行要求先去 cycle、再分解并 collapse 路径，得到 marginals 为未归一化 `mu_+,mu_-`、总质量 `tau=TV(P,Q)` 的 Gamma。不能直接限制原 coupling 到正负支持，亦不能归一化后遗失 tau。这里的局部 tau 不是 D5 的 public bitlength 参数。

第102–107行要求每个实际 input row 只有一个 K。good edge 的同一 midpoint 距两端各至多 k；bad fraction 留原输入，zero-residual row identity。共同质量 min(P,Q) 在两个法律下经过同一 K 后线性相消，并不被暗中分配 identity：

`(P-Q)K = sum_bad Gamma(x,y)(delta_x-delta_y)`。

有限 rational rows 的共同分母 seed 实现使每 input/每 seed 合法，其他 terminal fiber identity。该构造只用两条公开 witness laws 编表，不在 runtime 选择源标签，也不依赖 Q 或 predictor。第109–112行用 full-Z 加 fresh predictor coins 的同一测试，先选一个条件风险 witness，再用同一源的 stationary mass k/N 得平均下界，量词正确。

## D4/D5：各坐标完整，但证明仍由 C3 承担

定位：checkpoint 第118–142行；D3 第21–23行，D4 第29–35行，D5 第39–79行。

独立 count box 的 guard 无须 `C0+C1<=M`。由各自 `C0,C1<=M` 和合法 k，`D<=2M+6k+2<=3m`，故 `Zden<=12m`。nearest dividend `<= (6Q+4)D <=8QD<=24mQ<32mQ` 对 Q>=2 成立；ceiling dividend `<Q*Zden<=12mQ`。这覆盖 eager Q=2 候选的算术定义，最终 positivity 则由 uniform MUX 保证。full 2beta product、全 quotient/numerator、beta+1 shifted remainder、非负 SUB 和 range-justified cast 均是独立 proof 责任。

下表核对的是固定公式与承担对象是否列齐；没有证明一个更大的替代 envelope。

| D5 坐标或成组字段 | checkpoint 位置 | 新 C3 需要提供的证书 |
|---|---|---|
| ell,b,tau,n,s,beta,g | 第122行及第9、80行参数 | 参数域全覆盖，b 可任意大，frontend 也使用并支付 beta 物理宽度 |
| DIRECT G,core；E,L,W,dense_slots,P_bits,mask_bits,I_holds=0 | 第125行 | owned 全 Z、八 label 的 acquisition、54项及读写/cleanup；零 neural 坐标不免除 packed memory 费用 |
| DIRECT W_work | 第126行 | 全 batch/副本、八 counters、保留结果、产品/余数/控制/port 的同时存活界 |
| JOINT W,132 frontend layers，5 heads/最多4 simultaneous，value8/QK<=4/score0 | 第127行 | causal lags、singleton masks、dirty endpoints、两AND特征、exact finite zero head、实际 count snap，不能使用 clean bypass |
| JOINT G,L | 第124、128行 | 实际 JOINT17+46 表，Boolean primitives、rolling compiler、holds 与接口阶段；不得用 Python 整数操作作硬件单价 |
| JOINT E | 第129行 | word bundles 与 neural depth 分开；n² evaluator、完整四-bank scans/迁移/清除及 serialization |
| dense_slots,P_bits | 第130行 | 所有零 coefficient、bias、identity 均存储/求值，frontend n 位置与 query 1 位置分别计费 |
| mask_bits,I_holds | 第131行 | 全 masks 含零项；实际 live fields 的保留，不隐含全程 streaming |
| JOINT core,W_work | 第132行 | dense MAC、E*g、每 Boolean channel 的 beta-bit scalar、四批 banks 和 metadata working copy；擦除前不 release |
| N=3,4,5 的 G/core/zero neural fields/W_work | 第133、140行 | 只读实际 N 位并写同一个 port，不实例化 prefix/head 或虚构 input |
| Z_meta | 第134行 | public records 双份的容量/生成；dirty bits/counts/endpoints 只能在 data banks |
| a,K_code | 第135–136行 | segmented runtime fields、有限 primitive wiring/SSA/phase/loop descriptors、literal/padding；fetch/dispatch/address 全收费 |
| U_stored,T_online,peak_online | 第137行 | instruction/coefficient/operand fetch，stored+working 同时峰值及之前副本 |
| a_gen,Emit,T_gen,W_gen,peak_gen | 第138–139行 | 独立 flat generator 地址，显式枚举 wiring/SSA/loops/masks/dense zeros/metadata/code padding/port，含已生成 program 的同时峰值 |
| output=3(b+1),GPU=0 | 第140行 | fresh LSB-first 三字段；清除除 port 外全部 source-bearing input/control/scratch/旧副本 |

D4 要求的新自足 46 项表不能只写“旧41加5”；checkpoint 第124行及 D4 第33行已明确要求该表。DIRECT8+46 之外 acquisition 另付，JOINT17+46 之外 frontend/evaluator 另付。常量0/2保留收费，Q-1/Zden-1中的1仍为 literal1。五类最小 finite 接口在第142行均已列出；下一次固定复审要检查它们的实际证明与 generator/liveness，而非只检查此表是否抄齐。

## 当前证据快照及返回 Lead 的边界

本轮先通过 `euler_team_research_state` 回读当前精确 root/scope/budget。当前 C1、C2 已 DISCHARGED，C3 与 root 仍 OPEN、acceptance 为空。这是对原生状态的回读，不是本单作出的再次接纳：

| 组件 | 当前 Fact ID | 当前 Evidence ID |
|---|---|---|
| C1 | `f9e055bd405c4b56` | `61f169db99848f6794e334ea287037fae00a592f4b5e5254d580c0b9f74a599f` |
| C2 | `df40a215d931bd32` | `3448f22a5b9e86526c831f0518a83b828eaf69eb2acf455fb0057f354dae7cd3` |

checkpoint 第146行明确写“本checkpoint时”，其空证据清单是当时快照，不能当作当前图状态，也不是数学 scope 错误。

[Non-scientific operational metadata omitted.]本单 GPU=0，不调用 audit。[Non-scientific operational metadata omitted.]

已通过 team members/messages 读取配置与公开任务。尝试 bounded `euler_team_ask(lead)` 被服务以 `only the lead may schedule team consultations` 拒绝，未启动额外咨询、代理或替代模型；这是角色权限限制，不是数学障碍，不妨碍本轮准备单。没有提交 proof、改变 obligation/route、产生新的 Fact/Evidence，亦没有为不存在的数学阻塞建图。

本单新 Fact IDs = []，新 Evidence IDs = []。当时的科学未决项是 C3 的实际全域收费证书尚待固定版本；其后仍需对 C1/C2/C3 的完整组合进行独立审查。既有来源审查和组件接纳不自动证明组合已接纳；本阶段也不完成 v10 母问题。
