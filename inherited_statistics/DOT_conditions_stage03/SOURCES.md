# 科学来源与精确依赖

本文为新增编排索引，不是逐字原证明。科学副本的新增文字和源片段均在 COPY_MAP.json 分开标注。四个工作单元的原件有独立上下文数学审查及接纳；原审查结论均为 ACCEPTED、无数学修复。接纳绑定下表的原版本，不是一次对新复制件的重新证明。原版本的提交时状态文字仅是历史；本包已省略其管理性部分。

## 本增补的原始科学版本

源文件名为可公开的数学文件名。SHA-256 是完整原件的身份，不是仅保留正文的哈希；副本全文、保留片段及新增文字另有映射哈希。

| 原文件名 | 原全文 SHA-256 | 本包科学副本 |
|---|---|---|
| `S010_proof_v1.md` | `355dc4a05311c7ec1d67a760cef3aaa1e1783ec32b539e8f659763a437a854c9` | `proofs/S010_complete_proof.md` |
| `S011_proof_v1.md` | `808edc31256bc1d54b7e64c220eb50e294dc50f1939616897e729c1b8234b2ec` | `proofs/S011_complete_proof.md` |
| `S012_proof_v1.md` | `30cbb000d4493f18bc29f94cf46da94d719d6bc522c123204be7b0efe7cf4070` | `proofs/S012_complete_proof.md` |
| `S013_proof_v1.md` | `60856b7946be481c818d90a0be9d1e4d61062c91e2c8f09ae53226be6750dc9c` | `proofs/S013_complete_proof.md` |
| `S010_review_v1.md` | `363736bf4ff2fae25c451e1892c3e8f38783336c0742b4d0e0827790587c4529` | `reviews/S010_mathematical_review.md` |
| `S011_review_v1.md` | `6fde32344ba59237a28f06518d8140e1eb4b3c89781b33454702a042078d08ce` | `reviews/S011_mathematical_review.md` |
| `S012_review_v1.md` | `c25883d56078a001c2abccaa8d841fb3749f4c58c6393030a0f1eda14eed7ac6` | `reviews/S012_mathematical_review.md` |
| `S013_review_v1.md` | `443d99aa8b5a793b3c8438405a3ca03431f4050c02e1f28063ddc5c2ae874bdf` | `reviews/S013_mathematical_review.md` |

## 逐工作单元依赖与贡献位置

- **S010：**原 proof 的 Result、§1–6、MM5 source-to-new-claim map。unit_001–003 明确重述并修改 MM5 四字母组 Euler clock、全部余数初始化和完整历史编码；unit_004–005 新证明平滑不变律、全起点占用及全 pair minorization；unit_006–008 对改变后的目标重新 testing 并给常数／范围。黑盒 MM5 风险只用于 β=0；L1MAX §8 L1+ 只供任意初始化原规则上界。其正源性质不可从 S012 数值优势中删除。
- **S011：**§1–6 的所有七个局部结果。S003 Theorem S003.1 只给长度 ℓ 的后缀初始化 TV 上界；S004 S004.2 与 Lemma 5/Corollary 6 供原计数原堆栈上界和合法 copy 背景；S006 Lemmas 1、5 的行中心／martingale 桥在 S011 再陈述，且 Theorem S006-B 供真实平稳子类下界。β=0 用 MM5/L1MAX；β=1 的原算法分离通过 S006 中已接纳的 S005 接口。新的公开选择、有限常数桥、精确系数和全 burn 证书算术均在本件。绝不把 S003 下界按 β 参数生搬到较小混合类。
- **S012：**§1–4 的全部九个局部结果及开头 (S012) 公式。MM5 的 clock／编码／testing 构型有署源，吸收后的全表、稀疏平稳律、完整条件实验及新目标损失重新证明。S006 Lemma 3 的实际平稳 IID 子类（保留 M+2 个符号）供小 K；S011 的 F/180 与三个上界证书供组合／窗口计算；L1MAX 给原规则上界；MM5 黑盒只供 β=0；S010 仅为保留与比较，不是吸收构造的数学前提。Proposition 8 的 δ₀ 上界仅是该族上界；Proposition 9 是指定证书渐近。
- **S013：**全部六个局部结果。唯一数学接口是本增补 S011 Lemma 1 的端点安全 h_t；证明也直接说明其剩余核收缩桥。其余为明确二元矩阵、平稳方程、归纳、有限反例参数和逐行预测等式。无 S012 或其他未接纳诊断进入推理。

本包保留了原 review 的完整逐引理科学审查、隐藏命题／假设／符号／量词审查及有限检查事实。删除的完整管理段落和内嵌身份／控制来源片段均在映射以其确切字节区间和哈希披露；没有静默改写数学句子。新标题、中文说明、时序澄清和分隔符均被列为非原文新增区间。

## 继承的 Stage02 科学闭包

`inherited/DOT_conditions_stage02_20261028.zip` 是先前已交付的原 ZIP，456828 字节，SHA-256 `3f6a415201271c30224c5bef8759d80dd8570168b8a20e555f500178e2ce8c50`，本次没有重压缩或更改。它解压为 `DOT_conditions_stage02/`。其清单 SHA-256 为 `c5618c2ed29f080499ab2dd53f72d3d9e6a63ce2712c636132204892c92b8abc`，包含 33 条文件记录，加清单自身共 34 文件。

依赖入口均在这个归档内：

| 必要接口 | 归档内位置（相对 DOT_conditions_stage02/） |
|---|---|
| S003 初始化 TV 上界 | proofs/S003_initialization_transition.md；reviews/S003_mathematical_review.md |
| S004 原算法／后缀算法及收缩 | proofs/S004_mixing_original_and_suffix.md；reviews/S004_mathematical_review.md |
| S006 全行中心、平稳下界及 IID floor | proofs/S006_near_iid_and_two_step.md；reviews/S006_mathematical_review.md |
| S001/S002 平稳上下界 | proofs/S001_stationary_upper.md；proofs/S002_stationary_lower.md；各原 review |
| S005 真 IID 子类与原规则分离 | proofs/S005_iid_algorithm_separation.md；reviews/S005_mathematical_review.md |
| L1MAX 任意初始化原规则上界 | inherited/L1MAX_statistical_proof.md；inherited/L1MAX_review_scientific_excerpt.md |
| MM5 任意初始化下界与时钟 | inherited/MM5_statistical_proof.md；inherited/MM5_review_scientific_excerpt.md |
| GU 的 UC 与全数据 IID 前置接口 | inherited/GU_UC_and_IID_interfaces.md；inherited/GU_review_scientific_excerpt.md |

旧 S003 的基线通过 GU→L1MAX/MM5 闭合；旧 S004、S006 再通过 S001/S002/S005 连接。所有这些正文、原审查科学片段、来源说明、原复制映射与校验脚本均在原 ZIP 中，不需读任何私有控制对象或取得新材料。旧包其他 S007–S009 等文件是原归档不可变的一部分，不是本阶段扩张的研究范围。旧包中的历史开放边界以其所属时期为准，S012 对旧 M=K⁴、β=K⁻⁶ 例子已有明确更新。

这是**继承既有闭包**，不宣称本次重读或重新数学审查全部旧证明。当前检查实际验证了 ZIP 整体身份、嵌套清单及全部 33 个文件哈希；这些是完整性证据，不是数学复证。

### 继承源的原始身份

以下哈希照原 ZIP 的复制映射列出，是原科学来源全文身份；不是新审查或文献证书。

| 原科学来源 | 原全文 SHA-256 |
|---|---|
| `S001_proof_v1.md` | `6d00dc0b99ff0d6932b171bdd3e243ee923ca5d8a864cdac407c815e37f26f6d` |
| `S002_proof_v1.md` | `ac5e20d249704e298454f1b3633eedcf4026847801922a584a9043304cbdbdf4` |
| `S003_proof_v1.md` | `efa75c1ec0c1c3c8aab6956397f277bcf27dd148a480921b86186d6984f248e5` |
| `S004_proof_v1.md` | `a0f4f3cb2daf8f3191281d5e0fcdbb3f645d4118f7373f5fb1b8427006a1959a` |
| `S005_proof_v1.md` | `389d743cebf89f7afeb4855ceb712bfec8b3b216b10ae077b23dd980b03c7eba` |
| `S006_proof_v1.md` | `88f150f0d316825bae1fd5718878e863991be64329ba92d0a3865919ca3fc4b7` |
| `S001_review_v1.md` | `affe3eb2fa4c7f35f240a227758141173f5efa2af950966656c99337bc1cc1e8` |
| `S002_review_v1.md` | `031d75fa365a6f9640664ddd0745729f024f5ab11c1cf57475960a1c0ccc8a67` |
| `S003_review_v1.md` | `8a6ceb06c315b49d881a710c90f9a2cb0ce41fe03c69373c6f46ea136d74d226` |
| `S004_review_v1.md` | `9b3148ce4ac46090d9311a4f52d65dcb8f42bbfdb483e180edf830b3efa33699` |
| `S005_review_v1.md` | `836fd40704d2d32a064f0efda7fc812d80855137c2aac4bd71ac2175f4c85bde` |
| `S006_review_v1.md` | `4cd7abbbfdadad9f559c4ee848dd8444cbe35d8966f8327a74df5631afdae9b1` |
| `L1MAX-proof.md` | `96397d48a9c0b118991b14cac4b1c48b7f06613825275a5a28d3f489399287d9` |
| `MM5-proof.md` | `19d2b5e4d5a5c7c5f152f14b287bd42a5f130de4428c82f82e1a5916fe9400f3` |
| `GU-proof.md` | `cd15ce0bdd6821dbfce47784975483e93acf7834b58d218e098ba584496ca4b6` |
| `MM5-independent-report.json` | `feb0d0fcc5ca03efa229425c24afa521b3ec6226786fd4b5bccae5983555862e` |
| `L1MAX-independent-report.json` | `5850d4250f6533550229f2f2d531bcce06d58b039136fd0d15bc0b5cc8a3eebb` |
| `GU-independent-report.json` | `584b499e1888174dd468769aab1922e2b265d138e37f2cf6af642c21ccc336f2` |

## 先例与证据边界

MM5 四字母组时钟与有限 testing、L1MAX 原规则上界及 S003/S004/S006 接口都是明确承认的先前材料，不冒称本阶段发明。S010 修改时钟并证明平滑平稳律／新目标 testing；S012 用允许的稀疏平稳律构造吸收时钟并量化见证族局限；S011 的直接组合／有限桥和 S013 的有限矩阵阻碍按原文注明其贡献，不主张文献广泛首创。

本阶段没有调用新的第三方定理或作新文献搜索。已有外部文献、定理／页码和其适用限制仍见归档的 SOURCES.md 及原摘要文献页；引用口径没有扩大。旧公开材料明确区分 HJW 的预测 KL／TV² 与本题 E[TV]，并披露有限文献范围；本增补不从这些损失反向开方导出新下界。第三方论文全文没有附入任何新文件或继承 ZIP。
