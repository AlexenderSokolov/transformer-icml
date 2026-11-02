# 科学来源与嵌套依赖导航

本索引为新增编排。S016–S019 的原证明分别经独立上下文数学审查为 ACCEPTED，再由负责人完整读取并接纳；本包保留的是这些确切版本的科学正文。原作者提交时的 pending 标题不是当前状态。原接纳不等于本次复制后新的数学审查，也不代表外部同行评审或形式验证。

## 当前原始版本

以下 SHA-256 是完整原件身份；复制正文片段、删略、编辑新增与目标全文另有 COPY_MAP.json 的独立哈希。可公开文件名不带私有目录。

| 原件 | 完整原件 SHA-256 | 科学副本 |
|---|---|---|
| `S016_proof_v1.md` | `d28778b2e116a6a0717d844ff0df27c39800775e0fbd9b08c3e4d9e37d7baa0a` | `proofs/S016_complete_proof.md` |
| `S016_review_v1.md` | `50043baf9f542d246733c4d9704038a0614c743c6779f02af782c80924dbd247` | `reviews/S016_mathematical_review.md` |
| `S017_proof_v1.md` | `8c756b6448240393c71b5ccf68ec279cd13665df58628fd528cac3bb869caa27` | `proofs/S017_complete_proof.md` |
| `S017_review_v1.md` | `605a7a79c54af5382f18b895817d8ca7147b58c67a48cd0234c5a45b15e516d1` | `reviews/S017_mathematical_review.md` |
| `S018_proof_v1.md` | `0ae5c609dedec1dde7c80d3458f56fb0739ad7ab3c1e829d42dbd42e2c799838` | `proofs/S018_complete_proof.md` |
| `S018_review_v1.md` | `9e87cf57166c935ae5d3b8afe97c758708afd85f510209e93d77be9b2bf50cc1` | `reviews/S018_mathematical_review.md` |
| `S019_proof_v1.md` | `1ce16742abeab9a8c2eee94ad4d39fac0be2a14278dd7117477bca7b85f26fe6` | `proofs/S019_complete_proof.md` |
| `S019_review_v1.md` | `79c14a0518a0c0e5755e0351794e86aa49448472ac7e18dd14cb61c7145ba54f` | `reviews/S019_mathematical_review.md` |

## 当前工作单元与必要前驱

- **S016 四单位：** lem:s016-small、lem:s016-dominance、lem:s016-absorb、prop:s016-envelope。继承 S006 的完整观察 IID floor、S012 的 F/D 下界、S015 的精确星形计数／幅度及 S011 的分支上界。新的有限桥只在 T>F 时支付完整相位代价；不是新困难族或全域匹配。
- **S017 六单位：** lem:s017-round、lem:s017-lower、prop:s017-below、prop:s017-above、lem:s017-critical、prop:s017-opt。承重前驱是 S011/S012/S015，不依赖 S016。贡献是有完整 floor/ceiling 控制的固定射线推论和旧数值证书优化；其历史开放叙述由下列新风险证书在明确范围内更新。
- **S018 五单位：** lem:s018-stack、lem:s018-split、lem:s018-moment、thm:s018-geometric、thm:s018-critical。只通过准确接口继承 S004 独立行堆栈、S001 平稳占用、S011 F 下界；局部证明 MGF 联合界、含所有中点的两步全历史 split、条件仅限首次成功标签的 suffix law、整数阈值积分及全 K 临界常数。S013–S015 是被保持的障碍边界，非被静默否定。
- **S019 四单位：** lem:s019-lower、lem:s019-budget、thm:s019-strip、cor:s019-rays。前两大接口是完整 S016 下界和 S018 原规则几何上界；S017 Lemma 1 只为固定射线的受控对数转换。有限域 H 匹配及样本解释是这些接口的标准推论，没有新增统计方法、困难族或文献新颖性结论。

19 个局部完整证明单位及对应全部逐单位审查推理均保留。原审查中的数学有限检查事实保留：历史数字、精度、实际范围与“有限检查不代替符号证明”的限定均不改写。本次装配没有重跑这些检查。只删去纯身份、控制、路径、来源哈希核对项和重复框架；内部补充脚本／结果仍在原研究记录，不是必须依赖的证明前提。

## 精确继承闭包

原样附入已获准并已发送的 `inherited/DOT_conditions_stage04_20261028.zip`：1069825 字节，SHA-256 `a5f96b4987dfdaccf0c2a98d89f575b81a5ef9267ad3f7a8f9fd27254de6a1a1`。解压根为 `DOT_conditions_stage04/`，包含 14 个清单条目加清单自身共 15 文件。此处不重新压缩内部归档。

其 `inherited/DOT_conditions_stage03_20261028.zip` 为历史早期审查归档，793953 字节，SHA-256 `d5c85ed930cb1711960993799a1a6fbecd84b96e041db23eae7411c2d608b2fd`，解压根 `DOT_conditions_stage03/`，19 文件。Stage03 此前未单独交付；随 Stage04 原样继承，不误说成最新导读。

再内层 `inherited/DOT_conditions_stage02_20261028.zip` 是此前交付的 Stage02 原包，456828 字节，SHA-256 `3f6a415201271c30224c5bef8759d80dd8570168b8a20e555f500178e2ce8c50`，解压根 `DOT_conditions_stage02/`，34 文件。三层合计 68 个嵌套文件，按各层精确清单核对，非依赖私有路径。

### 按需解包定位

1. 解开外层本包的 inherited/Stage04 ZIP。S014/S015 完整科学证明与原审查在该根的 `proofs/S014_complete_proof.md`、`proofs/S015_complete_proof.md` 与同号 reviews/。
2. 在 Stage04 根解开 inherited/Stage03 ZIP。S011 全实验与分支证书、S012 吸收下界、S013 状态 TV 障碍在该根的 proofs/ 与 reviews/ 同号文件。
3. 在 Stage03 根解开 inherited/Stage02 ZIP。下列路径相对它的根：

| 接口 | Stage02 相对位置 |
|---|---|
| 平稳上下界 | `proofs/S001_stationary_upper.md`、`proofs/S002_stationary_lower.md` 及 reviews/ 同号审查 |
| η 初始化过渡 | `proofs/S003_initialization_transition.md` 及同号审查 |
| 原规则堆栈与 suffix 区别 | `proofs/S004_mixing_original_and_suffix.md` 及同号审查 |
| IID 结构与算法反例 | `proofs/S005_iid_algorithm_separation.md` 及同号审查 |
| 平稳近 IID 和 q=2 插值 | `proofs/S006_near_iid_and_two_step.md` 及同号审查 |
| 三步、正性、有限 reset | `proofs/S007_three_step_reset.md`、`proofs/S008_qualitative_positivity.md`、`proofs/S009_finite_exact_reset.md` 及同号审查 |
| 任意 μ 原规则基线 | `inherited/L1MAX_statistical_proof.md`、`inherited/L1MAX_review_scientific_excerpt.md` |
| 任意 μ 全数据下界 | `inherited/MM5_statistical_proof.md`、`inherited/MM5_review_scientific_excerpt.md` |
| 最早占用及 IID 接口 | `inherited/GU_UC_and_IID_interfaces.md`、`inherited/GU_review_scientific_excerpt.md` |

每层都有其原 SOURCES.md、复制映射、校验和及 PDF 编辑源。这里按接口继承，不声称本次装配重证或重新全文数学审查全部旧依赖；本次实际完整阅读当前四份证明／四份审查，对上述旧类读取相关精确陈述及源索引并核对身份。

## 时序与先例边界

S015 已闭合精确 γ=1/4 窗口。S017 的旧 U 临界值仍有 sqrt(log K/log log K)；它不是风险下界。S018 在精确 γ=1 序列给真实原规则新上界。S019 再在全部规定有限域给 H 匹配，并覆盖 S017 全部固定射线。S011 的其他已匹配域仍保留：δ≤a、半窗 h_floor(M/2)≤1/(M+1)，特别所有 β≥1/2 均有共同 minimax F/180 至 min(1,81F)；半窗还给原规则 81a，上述近 IID F 改善不统一赋予原规则。这些后继细化证书，不撤销旧有效数学；内层过时的开放叙述不作为当前结论。

一般率 g 与旧完整数据／最大值工具明确归属 GU、MM5、L1MAX。η 比较、有限 reset、S016/S017/S019 组合明确归为标准推论。外部先例沿用 Stage02 已完成的有限来源审读，不作新检索：Han–Jana–Wu, *Optimal Prediction of Markov Chains With and Without Spectral Gap*, IEEE TIT 69(6),3920–3959 (2023)，DOI https://doi.org/10.1109/TIT.2023.3239508。其 §V-A pp.3941–3943/Theorem 22、Lemma 6 pp.3925–3926、(104)–(107) 的 KL/suffix 平均口径，与本题原规则 E[TV] 不同；Theorem 24/(111)–(117) pp.3944–3945 和 §VI-A (135) 的 squared-TV 不能反向开方作本题下界。精确引用及未取得全文的文献核验缺口均见原 SOURCES.md，不声称没有先例、穷尽检索或优先权。本包不附第三方论文全文。
