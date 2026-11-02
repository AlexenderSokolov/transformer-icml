# 来源与科学依赖

## 证据与编排范围

本阶段主定理采用各单元已冻结、独立上下文 LLM 审查为 ACCEPTED 的证明版本；这不是形式证明或形式内核认证，也不声称跨模型独立性。`reviews/` 保留原审查的数学范围、逐引理理由、实际有限检查及结论，删除身份、调度和运行元数据。保留原单元的局部限定，不把早期单侧审查改写成综合审查。

`proofs/` 和 `inherited/` 的已复制数学段落保持原字节；原编号也保留，因此省略元数据处可能出现编号跳跃。`COPY_MAP.json` 列出原文件 SHA-256、原始字节区间、目标字节区间及各片段哈希。本次排版和哈希核对不等于新的独立数学审查；最终摘要是这些已接纳结果的中文综合。

## 必需的继承基线

以下均是本阶段已提供资料的科学接口，不是第三方论文全文。

1. **L1MAX 的 L1+ 统计上界。** 全部整数 K≥2、M≥1，任意齐次二阶合法 shift 源 θ、任意初始 pair 律 μ，原完整历史 add-one 在实际末行满足

       E TV(p⁺_{Y_M}, θ_{Y_M}) ≤ min{1,48 sqrt(K⁵/(M+1))}.

   本包保留原证明 §1 的统计设定、GU 的 UC 接口与 §§2–8 的完整统计推导。原证明的网络实现、精度、故障和资源部分不是此处的前提或结论。 Ψ 与 R_K⁺ 的独立阅读记号以明确标注的编排补充提供，来自已接纳 L1MAX 科学声明 §1／§2（TRUNC）；该声明完整文件 SHA-256 为 `bc24d183f5299df636e67f0b439aadbcd4d79671b69c327ed7083ddfab857c6f`，与下表可读证明文件的哈希分开。

2. **MM5 的一般初始化 minimax 下界。** 同一完整历史、同一实际末行 E[TV] 实验中，对每个允许源独立随机种子的共同算法，先取源与初始律的 supremum，再取算法 infimum，有

       R_general(K,M) ≥ 2^(-16) min{1,sqrt(K⁵/(M+1))}.

   本包保留 §§1–8 全部承重推导以及 §9 的样本必要性和边界。高 K 构造使用合法齐次四组时钟源、全部余数初始化及完整观察双射；不将其非平稳初始化误移至平稳类。唯一前驱 GU 只用于 2≤K≤11 的共同算法 IID 下界。

3. **GU 的两个精确接口。** §11.1 对任意初始化证明整数 w≥1 的实际末行占用尾界

       P(n_{Y_M}<w) ≤ min{1,K⁴w/(M+1)}.

   §13.3 对全部 N≥3、K≥2 的共同随机全历史算法给合法 IID 子类下界 1/(16sqrt(N))。这两个片段附于 `inherited/GU_UC_and_IID_interfaces.md`。本阶段仅继承其既有接纳；没有对 GU 全篇或其无关结论进行新认证。

这三项的源文件 SHA-256：

| 来源原文件 | SHA-256 |
|---|---|
| L1MAX-proof.md | `96397d48a9c0b118991b14cac4b1c48b7f06613825275a5a28d3f489399287d9` |
| L1MAX-independent-report.json | `5850d4250f6533550229f2f2d531bcce06d58b039136fd0d15bc0b5cc8a3eebb` |
| MM5-proof.md | `19d2b5e4d5a5c7c5f152f14b287bd42a5f130de4428c82f82e1a5916fe9400f3` |
| MM5-independent-report.json | `feb0d0fcc5ca03efa229425c24afa521b3ec6226786fd4b5bccae5983555862e` |
| GU-proof.md | `cd15ce0bdd6821dbfce47784975483e93acf7834b58d218e098ba584496ca4b6` |

原独立报告中的提交包哈希与以上“可读文件”的哈希不是同一个对象，不互换。原 MM5 收尾关于旧上界尚有差距的历史评语已被后来 L1MAX 的上界闭合，不作为本阶段当前结论复制。

## 本阶段依赖关系

- S001：新的平稳有限窗口计数 + 继承 L1MAX 的确定前缀 L4 最大值/二进分层分析 → 原 add-one 平稳上界。
- S002：合法双随机棋盘源族 + 条件于实际末对的完整反向历史 + 有限检验 → 平稳 minimax 下界；不依赖 MM5。
- S003：S001、S002 与 L1MAX/MM5 的精确统计接口 + 初始律正部支配及路径风险线性 → 初始化 TV 距离的匹配过渡。比较原理是标准工具，结果按紧性推论归类。
- S004：S001 的平稳占用和最大值分析 + 独立证明的 suffix 路径转移/原计数下界 + S002 缩放族 → 原算法与 suffix 的不同有限界。
- S005：本单元自足的两步 reset 结构、IID 检验与重叠碰撞计算；不依赖 S001–S004。
- S006：S001 原规则上界、S002 缩放棋盘族、S005 平稳 IID 见证 + pooled 鞅界与两步结构 → F 过渡。

## 直接先例 Han Jana Wu 的准确范围

Yanjun Han, Soham Jana, Yihong Wu. *Optimal Prediction of Markov Chains With and Without Spectral Gap*. IEEE Transactions on Information Theory 69(6), 3920–3959 (2023).

- DOI: <https://doi.org/10.1109/TIT.2023.3239508>
- 作者公开版本: <https://arxiv.org/abs/2106.13947>
- 已提供并审读的出版 PDF 哈希: `375c730cb4c9f6dd2eaa4439e59800764faeddbebee73f220e22d6d2cf3116a3`。
- 出版页码与 arXiv 页码不能混用。以下均为出版页码。

**确实覆盖的对象。** §V-A pp.3941–3943 的高阶设定与 Theorem 22 取 m=2、k=K，覆盖真正平稳的二阶符号 shift 源与实际末端预测。其上界不额外要求正边、不可约、唯一平稳律或混合。不能把任意 K² 状态一阶链的下界直接搬进合法 shift 子类。

**损失与算法的差别。** Lemma 6 pp.3925–3926 与 (104)–(107) 给的是 forward KL 风险，达到上界的预测器是多个 suffix add-one 的平均，而不是单一原完整历史 add-one。令 L=M+1、d=K²(K−1)，取全部 j=0,…,M 的 terminal-suffix add-one 平均 A_mix。由实际 pointwise redundancy 式 (106) 与 Lemma 6 只除一次 L，得

    E KL(θ_{Y_M} || A_mix)
       ≤ [d{log(1+L/d)+1}+2log K]/L =: B(K,M),
    E TV(θ_{Y_M},A_mix) ≤ min{1,sqrt(B(K,M)/2)}.

这是已知工具的直接推论，有平方根对数损失；它不证明本阶段的无对数 E[TV] 率，也不证明原完整历史 add-one 的风险。p.3942 Lemma 23 印刷显示的归一化与 (106) 的累计 redundancy 不一致，来源审读已据 (106) 和 (26) 明确只除一次，未采用重复归一化。

**下界不可逆搬运。** Theorem 22 的 KL 下界不能反向经 Pinsker 变成 TV 下界。Theorem 24 / (111)–(117), pp.3944–3945 的二元二阶构造能给 squared-TV 下界；对 Z∈[0,1]，(EZ)²≤EZ²≤EZ，因此 EZ²≥r 仅直接推出 EZ≥r，不是 EZ≥sqrt(r)。§VI-A pp.3949–3950 的“Total Variation”风险 (135) 也是 E[TV²]，不是本题 E[TV]。

**谱隙不可混用。** Theorem 3 与 Theorem 33 的相关 full-history 结论针对带谱条件的一阶链；pair-shift 链一般不可逆。不能省略这些条件而转称为无混合二阶结论。

## 有限范围近邻与未完成文献核验

- Hao, Orlitsky, Pichapati. *On Learning Markov Chains*, NeurIPS 2018. <https://arxiv.org/abs/1810.11754>。其对象区分 actual prediction、max-row 学习与独立 query；不是本阶段目标的直接替代。
- Wolfer, Kontorovich. *Minimax Learning of Ergodic Markov Chains*, ALT 2019. <https://proceedings.mlr.press/v98/wolfer19a.html>。其 max-row PAC 目标及平稳质量/伪谱隙参数不同。
- Erol, Zheng. *On Semi-supervised Estimation of Discrete Distributions under f-divergences*, ISIT 2024. <https://arxiv.org/abs/2405.09523>。IID 完整对与边缘样本不是重叠轨迹与相关末行。
- Han, Jiang, Wu. *Prediction from compression for models with infinite memory*, COLT 2024. <https://proceedings.mlr.press/v247/han24a.html>。已核部分以 KL 冗余方法为主，未提供本阶段原 add-one 无平方 TV 结论。
- Falahatgar et al., ISIT 2016. <https://doi.org/10.1109/ISIT.2016.7541787>。本次来源审读未取得完整主文本；这是明确的全文核验缺口，不能据此声称没有先例。

以上是已完成的有限来源审读范围，不是穷尽检索。标准方法和直接推论均按其身份归属；不提出首创或文献优先权主张。本包不再分发任何第三方论文全文。

## S007 的附加依赖边界

S007 的三步 reset 下界不是把 S002 已有族直接放入三步类；它重新构造三坐标零和扰动，逐项证明 P³=Π 与 P²≠Π，并重做完整条件反向历史及四个改变行的信息界。任意初始化的原规则上界只用 S004 的 ORIGINAL 版本；K=2,…,5 的下界用 S005 实际平稳、完整 N=M+2 观测的 IID 见证。S002 只提供方法背景，不冒充满足 exact-three-reset 的已知下界。

## S008 的继承范围

S008 的逐算法精确 supremum 等式由本单元的完整路径 telescope、移动目标风险连续性与两种不同正则化自足证明；只在末尾代入一般初始化的 L1MAX/MM5 与平稳 S001/S002 率。它不对这些前驱重新认证，也不把 MM5 的旧零边见证误说成原已严格正。平稳正则化针对选定平稳律的 triple flow，不声称零质量行均匀接近；任意 μ 的构造与此不同，二者不能自动插值为 TV-close 初始化的等式。

## S009 的标准推论身份

S009 只继承 S004 的 ORIGINAL 完整历史上界与 S007 的全 K、全算法三步 reset 下界；自行给出 `P^j=Π+(P−Π)^j` 的投影代数和完整的幂零核链证明，推出存在有限 reset 已蕴含 `P^(K²)=Π`。K² 是派生公共维数界，隐藏 q、π 不成为算法输入；长 horizon 用 S004，短 horizon 仅用目标率截断，下界由 E₃⊂E_fin。该项是标准有限维/统计推论，不是全 reset 核分类、最小指数或近似混合锐率。
