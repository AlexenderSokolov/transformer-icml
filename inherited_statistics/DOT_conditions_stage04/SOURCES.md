# 科学来源与原件身份

这是新增编排索引。S014/S015 两个原版本各有九个局部证明单元，均有独立上下文 LLM 数学审查及实际接纳。审查绑定下面的完整原件，不是对本次新中文摘要或新复制件的形式认证。原身份、运行记录及私有控制元数据不在公开科学面；原始文件和历史失败保留在原工作记录中，未改写。

## 新阶段的完整原件身份

源名称只给文件名；哈希是完整原件 SHA-256，不是节选正文哈希。新增文字、准确保留源段及省略补集均由 COPY_MAP.json 单独列出。

| 原文件名 | 原全文 SHA-256 | 本包科学副本 |
|---|---|---|
| `S014_proof_v1.md` | `6d350bef16e71bf001aeb9218ba4ebf57016873613ddda78e8009f0c8f39aaf4` | `proofs/S014_complete_proof.md` |
| `S014_review_v1.md` | `f0941477f53f868f0851ecf18589f7fa759d944f0a600f6bb083b1a65e1ae641` | `reviews/S014_mathematical_review.md` |
| `S015_proof_v1.md` | `f8ad4cf098874285431be5a41087958fb89f156144da589de83b5fa1c3b00289` | `proofs/S015_complete_proof.md` |
| `S015_review_v1.md` | `126fe6c20898317f55278a7ac0f5a9b8e928fbc03db27fa941a51d0b19dab5d1` | `reviews/S015_mathematical_review.md` |

## 每个工作单元的完整依赖和新增部分

**S014。** Lemma 1 从全 pair 二步公式求平稳符号边缘 p、合法残差 Q，并用 **L1MAX 的 L1+ 原全历史实际终端上界** 得无刷新贡献。它只施于任意合法 Q，不加 Q 的 minorization。S011 Proposition 2 的 row-center 恒等式在本件再推导。MM5 和 S012 Lemmas 1,3,4 / Proposition 5 提供被明确归因的 Euler 时钟、全数据编码及有限符号检验设计；新的发射行、ending-ℓ 起点、产品初始化、固定前缀、全路径双射、改变后目标对比与精确事件权重均由 S014 Lemmas 2–4 / Propositions 5–7 重证。Corollary 8 是精确对齐序列的反例；Proposition 9 给该族 nonrefutation 的有限边界。完整九单元证明和九单元原审查推理随包保留。

**S015。** 明确归因 **MM5 §§1–9** 的符号测试设计，而不是用旧黑盒下界替代改变后的目标。Lemma 1 / Invariant 2 全新构造 period-2m 星形几何和安全零输出；Lemmas 3–5 重证每起点 membership、每余数完整历史和只限制脆弱币的事件；Proposition 6 用真实新目标的 δ 对比得下界及仅此族精确上界；Proposition 7 给确定 H_M 和有限 K⁴ 幅度；Proposition 8 用 **S011 Theorem S011** 的相同实验公共选择器上界及 **S012 Proposition 9** 的精确对数序列证书渐近，在本件再核标量桥后闭合窗口；Proposition 9 用同一族证明两项明确否定。S014 不是 S015 的前提；S012 旧族的精确 family-only upper 只作范围比较。

引用的原审查完整科学正文与有限检查事实均保留。LLM 独立审查不是形式验证、外部同行评审或文献新颖性认证。有限检查只是原作者／原审查已执行的历史结果，未在编排时重跑。

## 原样附入的早期科学闭包

`inherited/DOT_conditions_stage03_20261028.zip` 为获准的 **Stage03 历史早期审查归档**，此前未单独交付。大小 793953 字节，SHA-256 `d5c85ed930cb1711960993799a1a6fbecd84b96e041db23eae7411c2d608b2fd`。解压根目录为 `DOT_conditions_stage03/`；清单 SHA-256 `601252e8d08762c99bdd1fc7a01f41ef5901749649e049ce3041cc554c33c214`，18 个条目加清单自身共 19 文件。它没有被重新压缩或改变。

其 `inherited/DOT_conditions_stage02_20261028.zip` 是已交付的原 Stage02 ZIP，456828 字节，SHA-256 `3f6a415201271c30224c5bef8759d80dd8570168b8a20e555f500178e2ce8c50`。内层根为 `DOT_conditions_stage02/`，清单 SHA-256 `c5618c2ed29f080499ab2dd53f72d3d9e6a63ce2712c636132204892c92b8abc`；33 条目加清单共 34 文件。

**时序优先级：** Stage03 的 S010–S013 时代“对数窗口尚未匹配”的说法是历史状态。当前 S015 已证明在精确 `M=K⁴,β=ln(K)/(4K⁴)` 上公共全类 minimax 为 Θ(K⁻¹⁄⁸)。旧 PDF、原正文和审查均不事后改写；阅读当前结果以外层说明为准。S014 自身发射族的 nonrefutation 同样是局部族结论，不与不同星形族反证冲突。

### 可直接阅读的依赖入口

| 数学接口 | ZIP 内位置 |
|---|---|
| S011 公共算法上界与 row-center 恒等式 | Stage03 根下 `proofs/S011_complete_proof.md`、`reviews/S011_mathematical_review.md` |
| S012 吸收时钟、全历史检验、旧族上界与窗口证书 | Stage03 根下 `proofs/S012_complete_proof.md`、`reviews/S012_mathematical_review.md` |
| L1MAX 一般任意初始化原规则上界 | 内层 Stage02 根下 `inherited/L1MAX_statistical_proof.md`、`inherited/L1MAX_review_scientific_excerpt.md` |
| MM5 全数据时钟与有限检验方法 | 内层 Stage02 根下 `inherited/MM5_statistical_proof.md`、`inherited/MM5_review_scientific_excerpt.md` |
| GU occupation 与全数据 IID 前置接口 | 内层 Stage02 根下 `inherited/GU_UC_and_IID_interfaces.md`、`inherited/GU_review_scientific_excerpt.md` |
| S011 的初始化／原规则／近 IID 前置接口 | 内层 Stage02 根下 S003、S004、S006 的 proofs/ 和 reviews/ 对应正文 |

S011 的 S003/S004/S006 接口通过 S001/S002/S005 及 GU→L1MAX/MM5 继续闭合。全部必要正文、原审查科学推理、来源、复制映射和构建说明均在嵌套原 ZIP 内；不需私有控制材料。原归档其他文件仍作为不可变早期闭包保存，不扩展本阶段的研究范围。编排检查核对整体 ZIP、所有嵌套文件哈希及原件映射身份，**不宣称重新数学审查所有早期证明**。

### 关键继承原件身份

以下是内层 COPY_MAP.json 中的完整来源哈希，并非本次新审查。其他闭包来源见各层原 SOURCES.md 与映射。

| 原科学来源 | 原全文 SHA-256 |
|---|---|
| `S011_proof_v1.md` | `808edc31256bc1d54b7e64c220eb50e294dc50f1939616897e729c1b8234b2ec` |
| `S012_proof_v1.md` | `30cbb000d4493f18bc29f94cf46da94d719d6bc522c123204be7b0efe7cf4070` |
| `S011_review_v1.md` | `6fde32344ba59237a28f06518d8140e1eb4b3c89781b33454702a042078d08ce` |
| `S012_review_v1.md` | `c25883d56078a001c2abccaa8d841fb3749f4c58c6393030a0f1eda14eed7ac6` |
| `L1MAX-proof.md` | `96397d48a9c0b118991b14cac4b1c48b7f06613825275a5a28d3f489399287d9` |
| `MM5-proof.md` | `19d2b5e4d5a5c7c5f152f14b287bd42a5f130de4428c82f82e1a5916fe9400f3` |
| `GU-proof.md` | `cd15ce0bdd6821dbfce47784975483e93acf7834b58d218e098ba584496ca4b6` |
| `MM5-independent-report.json` | `feb0d0fcc5ca03efa229425c24afa521b3ec6226786fd4b5bccae5983555862e` |
| `L1MAX-independent-report.json` | `5850d4250f6533550229f2f2d531bcce06d58b039136fd0d15bc0b5cc8a3eebb` |
| `GU-independent-report.json` | `584b499e1888174dd468769aab1922e2b265d138e37f2cf6af642c21ccc336f2` |

## 先例和文献边界

MM5 的四字母组 Euler 时钟和有限检验、L1MAX 的原规则上界、S011/S012 的公共证书都是明确承认的直接先例。新的内容是发射／前缀统计反例、星形零输出几何、脆弱币全观察事件、精确计数、改变后目标测试和指定窗口的匹配与反证；不冒称整套检验法为新发明。

没有调用新的外部定理或另作本阶段文献搜索。原外部来源、页码／定理和适用限制继续见内层 Stage02 SOURCES.md。其 HJW 预测 KL／TV² 与本题期望 TV 的区分不变，不从错误损失方向反向开方推出下界。未附第三方论文全文；无广泛文献优先权或新颖性认证。
