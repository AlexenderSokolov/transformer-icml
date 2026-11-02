# C4/C2 量词综合：固定审查附录 v1

Counter，2026-10-25。有界文件审查；不重复原 C1/C2 证明或旧诊断，不提交 Fact。

| 本次输入 | SHA256 |
|---|---|
| lead/joint-accuracy-corollary-v1.md | 37c3f17f3e427787baa8892e216a5c9b68508f538f24e3a95cdc31c646012c92 |
| lead/primary-synthesis-checkpoint-v1.md | b12f56a4e7458c7886370c595d62aad2966b266ed943c7d6614738a7a77dd7f1 |
| 原 pinned counter/sources/primary-map-v1.md | f5b2fdcfd9b96ce74ebc8141b9dd0dde7c33caa10952aca6dacf90229a9d6f45 |

**结论：两份新稿未见承重数学错误。四项必要条件和四项充分条件均成立，但不是
同一组可行性的充要条件。只建议收窄一处“exact”的措辞；无需改变算法或常数。**

## 1. 有限精度条件和共同程序

对任意 q，A(q)>=M_N,Q，B_u(q)>=C_N,Q(u)，即使后者的 lower comparator
允许知 u。因此 pending C1/C2 的下界确实分别推出

    N+6 >= 3/(16384 epsilon_A),   Q >= 1/(3 epsilon_A),
    1+(N-2)u >= 3/(16384 epsilon_C),   Q >= 1/sqrt(2 epsilon_C).

它们逐项限制同一个 q 的两种 worst-case risk；未相加不同源上的 lower witnesses。
共同 C2 程序的两条上界则由新稿的四个充分式各分配 epsilon/2 直接推出。
这用的是一个已指定、独立于 u,t 的程序，不是把两个 minimax 的不同最优器拼接。

必要 Q 条件的取 log2、整数 ceiling 及 b>=1 域正确；充分 b 的双重约束也正确。
清分母后 doubling 可有限生成 b。单独的平均要求是
b=log2(1/epsilon_A)+O(1)，单独固定 u 的条件要求是
b=(1/2)log2(1/epsilon_C)+O(1)，均以相应历史条件满足为前提。
联合要求取两阈值的较大者；同容差时平均项更强或与域 b>=1 并列。
这些是输出位数，不是 internal h_A、总储存、运算、深度或架构的必要界。

**具体文字修复：**把“the exact dyadic output lower condition”改成
“the preceding necessary Q inequalities have the equivalent integer-bit form”。
这里使用 delta_Q>=1/Q 已经放松了必要条件，不能把“exact”理解成精确可行域。
例如 N=100,u=1/8,Q=2,epsilon_A=epsilon_C=1/5 满足四项所列必要式，
但平均格式下界 delta_2/3=log2/3>1/5 仍排除该目标。
若要更紧的有限必要式，可保留 delta_Q/3<=epsilon_A，等价于
Q>=1/(1-exp(-3epsilon_A))；这仍不是 joint feasibility 的充分条件。

## 2. 固定 u、同时保证及全域条件 minimax

共同程序实际提供的量词是：对每个公开 N,Q，存在同一个不知 u 的 q_N,Q，
其平均界在全 D1 成立，条件界对每个 u 分别成立。
条件目标 epsilon_C 的充分式1+Nu>=2000000/epsilon_C只描述评价时的 law 区域；
不是算法可检验的停止规则，也不是额外给定了 u 的正下界。
该区域在某些公开 N 下可能为空；新稿没有因此许诺全 u 的条件保证。

U_N 的推导顺序也正确：对每个固定 q、每个正 u，先有

    sup_t R_N,00(u,t;q) >= 3/[16384(1+(N-2)u)]。

固定 N 后对 u 取 supremum，右侧随 u↓0 趋3/16384；最后才对 q 取 inf。
因此 U_N>=3/16384，包含随机化比较器且不限输出格式。没有交换 inf/sup，
没有引入 u=0 的 law，也不要求同一个 t 或同一个 law 实现所有下界。
所以 epsilon_C<3/16384 的全 u 保证不可能由有限 N,Q 达到；不能将固定-u
可达性升级为全域条件一致性。该结论与每个固定正 u 下、N,Q→∞的期望KL收敛兼容，
不表示 fixed-law inconsistency 或几乎必然结论。内部精度变化不能消除这一统计下界。

## 3. Primary 综合与精确反例

新 primary checkpoint 与原 pinned map 一致：HJW 的普通可逆一阶定理不能因
symbolic reversal 套到 pair 链；全 stationary 二阶 lower 不能搬入 D1；Paulin
的 path-TV 工具不是现成预测风险定理；Geiger–Böcherer 是已知 target 的同方向
KL/M-type 量化直接先例，式10不是本历史条件实验。没有新的 novelty 或资源必然性推论。
其辅助可行集 t_i>=1/M 的限定也保留了，没有把 target-dependent 阈值扩成统一阈值。

精确 KL 反例核算成立：对 t=37/100,Q=4，欧氏最近 next1=1/4，而

    kl(t,1/4)-kl(t,1/2) = log2-(63/100)log3
                        = log(2^100/3^63)/100 > 0。

本次重新作整数运算，2^100 和3^63与新稿所列整数完全一致，差为
123089326797391906610753508949>0。故无需浮点误差判断。
这只排除“逐 target 精确 KL 最优”的扩张，不反驳 C2 的量级分类。
普通中文的“00 内部远离概率边界，所以舍入损失平方下降；常见10的稀少后继
趋零，所以正输出网格造成一阶损失”与原风险映射一致。

## 4. 待接纳依赖与本次状态

C1 `1dd6b3b9191952ba424db347dab176cd3336d5399831f867f595a13a40e5ce25`
和 C2 `8b179af3ef2fe36eca7503ff37e9baca6ba118d546cf884db6ad7e4da0d0b6f8`
仍是待接纳 native premises；C2 必须使用接纳后真实 C1 Fact 作为 predecessor。
C3 `c82d400c69019a551db29a66e99faec5bfbf281097c5c8ae57075ea5789772fb`
的完整证书另由 Prover 处理，本附录不审查或接纳它。排队审查不是已返回的证据。

本次 Euler readback 为上述义务 OPEN、all_evidence=[]、acceptance=null。
既有 C4 诊断缺口 `0def94abb5dd20e9fc11024c4f656ce7f0d77ef78740e17ef61155836d95a99d`
仍待完整证据包修复；本次未发现新的承重障碍，未新增重复失败、义务或路线。
Fact IDs=[]；Evidence IDs=[]；未 ask、submit_proof、final_audit 或改变图状态。
[Non-scientific operational metadata omitted.]完整 C4、root接纳与 final_audit
均未由这份附录完成；阶段完成也仍不等于 v10 母问题/T1→T2→T3 完成。
