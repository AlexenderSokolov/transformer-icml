> Public-export notice: this is a privacy-screened derivative of the dated analytical preparation. Its historical no-upload/no-mutation statements describe preparation, not this later publication. Mathematical claims and original scientific hashes are preserved. See [public export](../../provenance/arbitrary_initial_kl_lower_20261104/PUBLIC_EXPORT.md) and [public source map](../../provenance/arbitrary_initial_kl_lower_20261104/PUBLIC_SOURCE_MAP.json) for current public identities.

# v10 阶段综合修正附录：任意初始化的 A⁵ 下界

日期：2026-11-04 01:22 UTC。原始分析综合的公开导出。此附录只新增，不覆盖或修改 v10_verified_stage_synthesis.zh.v1.md、既有证明或封存报告。数学结论依两份已完成的独立内部分析审阅；它们不是外部同行评审、形式化验证或新颖性认证。本轮没有数学数值测试、训练、软件求值器执行或外部上传。

## 1. 修正哪一句

原综合 §3 仅以 HJW 平稳子类的 A³ 下界比较任意初始化 A⁵ 上界，遗漏了项目已有 MM5 下界。这使“字母表差距仍未关闭”的说法不完整并可能误导，应由以下结论取代：

**任意初始化下，已有 MM5 的实际末端 TV 下界，经 Pinsker 与 Jensen 严格推出 forward-KL minimax 下界 2⁻³¹ min{1,A⁵/(n+1)}。它与已审阅的普通全历史 add-one 上界 O(A⁵ log(n+2)/(n+1)) 在低风险区的 A⁵ 多项式字母表因子上匹配，剩余一般增长字母表下的精细对数、饱和行为及完整联合 (A,n) minimax 速率尚未确定。**

不能再把 A⁵ 相对于平稳 A³ 的差别单纯描述为尚无下界支持的证明损失。平稳与任意初始化是两个不同的源类。

## 2. 精确下界、观察实验与量词

A≥2、n≥1 为整数。观察齐次二阶 A 符号源的完整历史 H=X₁,…,Xₙ₊₂，共 n 次已观察转移；预测同轨迹真实末端 pair Y_n=(Xₙ₊₁,Xₙ₊₂) 的下一符号行。核 θ 在一次实验中固定，初始 pair 分布 μ 任意，允许零概率、可约性和周期性。

预测器 Q 是同一个完整历史到 A-simplex 的概率核，可依公开 A,n，允许源独立随机化，不能读取隐藏 θ、μ 或未观察下一符号。定义

    R_KL^all(A,n)=inf_Q sup_(θ,μ) E D_KL(θ_{Y_n}‖Q(H))，

并用同一实验和算法类定义 R_TV^all，TV 为半 L₁ 距离，KL 用自然对数。MM5 的原符号是 K=A、M=n；其辅助训练块数 floor(n/m²) 不能误作全局转移数 n。

原 MM5 给出全部上述有限参数的下界

    R_TV^all(A,n)≥2⁻¹⁶ min{1,√(A⁵/(n+1))}。

逐源逐算法应用 Pinsker、Jensen，再依原次序取 sup 和 inf，得到

    R_KL^all(A,n)≥2[R_TV^all(A,n)]²
                 ≥2⁻³¹ min{1,A⁵/(n+1)}。

第二处也是“≥”，不能写成等号。若预测在真实正概率坐标上输出零，KL 为无穷，不妨碍此下界。这里没有交换 inf 与 sup，也不要求极值被某个源或算法取得。

这是对所有核与初始分布取上确界的下界，不是对每个预先指定初始分布、每个固定确定初始 pair 或每个固定源的下界。困难源可依公开 horizon 和算法选择，不宣称一个源同时使所有算法、所有 horizon 失败。其初始律依 A,n，但在同一困难族中对所有隐藏符号参数相同。

## 3. 下界为何确实是同轨迹末端问题

MM5 用原字母表内四组符号和 Euler pair 周期，在合法二阶齐次转移表中构造稀疏出现的未知行；没有外加隐藏时钟。所有余数的初始化都明确给出，让实际末端落在未知 U×V 行。

完整历史与已观察训练三元组加真实末端 pair 之间有不依隐藏参数的双射。困难族中末端 pair 的均匀性和与训练数据的独立性由完整路径律证明，不是把问题改成独立测试样本，也不是给一般随机行计数假设条件 iid。

m 为奇数时未知行有 floor(m/2) 对扰动坐标，剩余坐标质量为 1/m；原证明已正确使用 floor(m/2)/m≥1/3。小字母表接口已在新审阅中直接核对，另一审阅另给自足 iid 两点推导。全部 A≥2、n≥1 的常数和边界已包含，不限于大样本、整除周期或偶数分组。

## 4. 与现有上界合成后的准确阶段

原综合中的任意初始化 add-one 上界不变。令 K_n=1+floor(log₂ n)，则

    sup_(θ,μ) E D_KL(θ_{Y_n}‖B_{Y_n})≤V(A,n)，
    V(A,n)=min{log(n+A),
      A⁴[log A+1536 A K_n]/(n+1)}。

因为 log A≤A 且 K_n≥1，其第二分支≤1537 A⁵ K_n/(n+1)，不需要额外假设 A≤O(log n)。因此

    2⁻³¹ min{1,A⁵/(n+1)}
      ≤R_KL^all(A,n)
      ≤sup_(θ,μ) E D_KL(θ_{Y_n}‖B_{Y_n})
      ≤V(A,n)。

minimax 风险还可用始终均匀预测获得 log A 上界，故 R_KL^all≤min{log A,V(A,n)}。这个 log A cap 是两个预测器择优后的 minimax 上界，不能写成普通 add-one 自身已证明的 cap。

据此可准确说：

- A⁵ 多项式障碍对任意初始化源类是必要的，低风险区与现有上界至多差对数因子。
- 当 n→∞、A=A_n 时，minimax KL 一致性的必要条件为 A_n⁵/(n+1)→0；现有 add-one 上界给出的充分条件为 A_n⁵ log(n+2)/(n+1)→0。它们尚未合并为精确阈值。
- 对 ε<2⁻³¹ 的统一最坏 KL 误差目标，必要 n+1≥2⁻³¹ A⁵/ε。这是统计样本数必要条件，不是内部位数、深度、宽度、计算工作量或精度最优性下界。
- 下界在高 A⁵/n 区只饱和到普适正数；KL 可随 A 增大，不能据此宣称完整饱和区是 Θ(1)，或写全局 Θ(min{1,A⁵ log n/n})。
- MM5 是所有共同预测器的 minimax 下界，符合相同观察和算法量词的五块网络 R、专门求值器 Q 也受它约束。这不同于二元一阶补充中仅针对普通 add-one 的下界；后者不可自动转给网络。

## 5. 平稳下界仍保留，不能删掉全部对数

在 HJW 二阶定理域 2≤A≤(n+2)^(1/3)/C₂，平稳源类另有

    R_KL^all(A,n)≥A³/[C₂(n+2)]·log((n+2)/A³)，

因为平稳类是任意初始化类的子集。在该域可将它与 MM5-KL 下界取最大值。固定 A 的 Ω_A(log n/n) 下界因此仍成立；结合已知上界，固定 A 的 Θ_A(log n/n) 结论不变。MM5 自身并没有给出 A⁵ log n/n 下界，也不能用它暗示所有对数都能删除。

平稳新上界 A³/n·[1+log₊(n/A³)] 与任意初始化 A⁵ 障碍并不矛盾。MM5 初始相位把终点集中在信息行，不能直接用于平稳初始化。沿 n=A⁵、A→∞，任意初始化 KL 下界保持正的普适量级，而平稳可达上界趋零，说明两类在联合参数上可以真实分离。

## 6. 来源身份与审阅边界

- 当前可读 MM5 原证明：MM5-proof.md（原始准备定位符略；公开科学副本见下列不变链接），SHA-256 19d2b5e4d5a5c7c5f152f14b287bd42a5f130de4428c82f82e1a5916fe9400f3。
- 旧 MM5-independent-report.json 引用另一 proof hash 5fef432092c4d7394021f1651dbcd086b660028b2a62c1297342340892dd6d24。历史身份差异尚未解释，不能说旧报告是对当前原件逐字节审阅；本次两份审阅均直接分析当前 19d2… 原件。
- 已公开的 1721 trace 明示该差异并直接核验可读原件；1732 odd-m 修正只纠正后续审阅中“m/2 对”的措辞，未改变原证明、定理或常数。原件、科学删节副本和隐私处理后的公开副本不可混为同一哈希。
- 此前公开不变快照 0d678eefb558d5108dd5ef893b033c6f58077d81 中的科学证明：https://github.com/AlexenderSokolov/transformer-icml/blob/0d678eefb558d5108dd5ef893b033c6f58077d81/inherited_statistics/DOT_conditions_stage02/inherited/MM5_statistical_proof.md 。这是历史已存在来源，不是本附录新上传结果。
- 本次量词/溯源审阅：[量词/溯源审阅](arbitrary_initial_kl_lower_audit_20261104.md)，SHA-256 bcd14491c92dfe88f58df180baa855a0993f827058c1a70063b71fc312ef54c6。
- 本次独立 KL 转移审阅：[独立 KL 转移审阅](kl_lower_transfer_audit_20261104.md)，SHA-256 5b63af72865fe3a3bc72ad785f3f71e72374668110841bdca0fccbe8327e8f05。

MM5 TV 下界是继承的已有项目数学；KL 推论使用标准 Pinsker 与 Jensen。本附录不宣称首创、论文录用或穷尽文献检索，也没有用哈希核验代替数学证明。

## 7. 公开导出及保留缺口

原综合及本附录的操作状态陈述仅描述各自准备时点，不作为实时发布状态。公开副本省略与数学无关的准备定位符及操作记录；原始/公开身份和逐行变更见 ../../provenance/arbitrary_initial_kl_lower_20261104/PUBLIC_SOURCE_MAP.json。

20:35 微型试验原始结果丢失、未恢复的边界不变。本次公开没有恢复训练记录、运行新训练或数学数值实验。
