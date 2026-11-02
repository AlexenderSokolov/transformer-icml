# 来源身份与必要完整科学闭包

## 本阶段原件与复制关系

S 编号只指本条件统计项目。下表绑定完整原件的精确字节，不是删略科学副本哈希；副本各自哈希及精确区间见 COPY_MAP.json。没有私有目录依赖。

| 完整原件 | 字节 | SHA-256 | 本包科学副本 |
|---|---:|---|---|
| `structural_survival_diagnostic_v2.md` | 39016 | `3c3c0658bd58613a98b2212871b868ba75c6f1f9350c9ade0f10297d48cd7d3c` | `proofs/S023_complete_proof_v2.md` |
| `S023_mathematical_review_v1.md` | 36289 | `882a60c76f93ef89f9a0ee918b905299c379c0c3d8fdfddaab85818834e73484` | `reviews/S023_mathematical_review_v1_science.md` |
| `S023_mathematical_review_v2.md` | 12138 | `3009c465bae495242b68c0d88284ffd48d834090004e4489f672099f0b3e808a` | `reviews/S023_mathematical_review_v2.md` |
| `closed_class_adaptation_diagnostic_v1.md` | 27540 | `d1237df20f020e85ddf5c3e7a918736e72a5df2af05982078b953d11e42cf411` | `proofs/S024_complete_proof.md` |
| `S024_mathematical_review_v1.md` | 27179 | `68d4d4fb3e4d7a7a73c4a5adeebd8396245aa746e6ba622d0ca4e84ba08b9f2e` | `reviews/S024_mathematical_review.md` |
| `near_iid_adaptation_diagnostic_v1.md` | 28840 | `0732155622905e5f5b00d819d416f053ecf76019e0a09b29939ec5b0d17fde20` | `proofs/S025_complete_proof.md` |
| `S025_mathematical_review_v1.md` | 28290 | `e8a472a379f67d1f637802199b6e9f62303005391be097c6b4e5b42eb9b9b551` | `reviews/S025_mathematical_review.md` |

只接纳 S023 v2、S024 v1、S025 v1。S023 v1 的完整科学审查是失败历史判断和 v2 所继承的完整审查前件，不追认 v1。原 v1 证明 SHA-256 为 `7709f4a406925151ecd4f1b3fde204cc17708d97698f90fa18c239433874c760`；不附原始失败档案，但完整科学范围失败、六单元论证及有界修复均附。两主定理并未被推翻。S025 的真 NEXT 反例完整在其 §2 和审查 Unit 1，另有中文说明。

## 唯一继承归档

只继承已经交付的 S020–S022 v2 科学 ZIP，1,780,367 字节，SHA-256 `7970826c3b61295768e5ffc9cde39faa2020e0bd702479a915a7b047acb23cee`，逐字节不变。选择这一整份已有归档有实质必要：S023 直接依赖 S020、S021v2 及其范围失败／修复审查，S024/S025 直接依赖 S022；各支再经 S001/S006/S011/S012/S015/S018/S019 回连早期接口。只取其中某一新单元不能闭合这三份新结果的全部依赖。一个已交付科学归档保持已有证明、审查和复制来源链，不复制整个研究目录。

逐层解包后可读取各层 SOURCES、COPY_MAP、proofs、reviews。下表箭头表示在 ZIP 内再打开 ZIP，不是计算机目录。各层原历史状态保留，当前接纳与目标状态以本包为准。

| 归档链 | 字节 | SHA-256 | 本层文件数 |
|---|---:|---|---:|
| `inherited/DOT_conditions_next_stage_20261029_v2.zip` | 1780367 | `7970826c3b61295768e5ffc9cde39faa2020e0bd702479a915a7b047acb23cee` | 19 |
| `inherited/DOT_conditions_next_stage_20261029_v2.zip → DOT_conditions_next_stage_20261029_v2/inherited/DOT_conditions_phase_review_20261028_v2.zip` | 1460410 | `cc8b3cf77d799e65d5cafd51d4738262c76a8c58756ffcf5b968d6a65ff1a188` | 19 |
| `inherited/DOT_conditions_next_stage_20261029_v2.zip → DOT_conditions_next_stage_20261029_v2/inherited/DOT_conditions_phase_review_20261028_v2.zip → DOT_conditions_phase_review_20261028/inherited/DOT_conditions_stage04_20261028.zip` | 1069825 | `a5f96b4987dfdaccf0c2a98d89f575b81a5ef9267ad3f7a8f9fd27254de6a1a1` | 15 |
| `inherited/DOT_conditions_next_stage_20261029_v2.zip → DOT_conditions_next_stage_20261029_v2/inherited/DOT_conditions_phase_review_20261028_v2.zip → DOT_conditions_phase_review_20261028/inherited/DOT_conditions_stage04_20261028.zip → DOT_conditions_stage04/inherited/DOT_conditions_stage03_20261028.zip` | 793953 | `d5c85ed930cb1711960993799a1a6fbecd84b96e041db23eae7411c2d608b2fd` | 19 |
| `inherited/DOT_conditions_next_stage_20261029_v2.zip → DOT_conditions_next_stage_20261029_v2/inherited/DOT_conditions_phase_review_20261028_v2.zip → DOT_conditions_phase_review_20261028/inherited/DOT_conditions_stage04_20261028.zip → DOT_conditions_stage04/inherited/DOT_conditions_stage03_20261028.zip → DOT_conditions_stage03/inherited/DOT_conditions_stage02_20261028.zip` | 456828 | `3f6a415201271c30224c5bef8759d80dd8570168b8a20e555f500178e2ce8c50` | 34 |

## 直接科学依赖的可读副本身份

下表 SHA-256 是既有归档中科学副本的身份；原件全文身份由其各层 COPY_MAP 继续提供。S020/S021/S022 在唯一继承归档外层；S016/S018/S019 在其 phase-review；S015 在 stage04；S011/S012 在 stage03；S001/S003/S005/S006 及 L1MAX/GU/MM5 在 stage02。各层相应完整科学审查随层保留。原件名和副本名不同不表示版本可互换。

| 必要科学正文 | 字节 | 副本 SHA-256 |
|---|---:|---|
| `DOT_conditions_next_stage_20261029_v2/proofs/S020_complete_proof.md` | 28164 | `a478d1219c97b479f0c96d0124a6d3fff023e18a4177361a758003db4b1de8eb` |
| `DOT_conditions_next_stage_20261029_v2/proofs/S021_complete_proof_v2.md` | 25127 | `6b1eef09db3959a2e846e5e56fcf6d4d084ed51ceaaca0033ca6a9d4e4dc57b3` |
| `DOT_conditions_next_stage_20261029_v2/proofs/S022_complete_proof.md` | 20291 | `028f43ae12886781bfd3641712c66720d24c667b59ca22a74c5dbbea5b0a5774` |
| `DOT_conditions_stage02/proofs/S001_stationary_upper.md` | 16004 | `7fa8b2119f84d9f382da80516aa8b3c277ebd2c4587dffd58d24bf16b11a77d4` |
| `DOT_conditions_stage02/proofs/S003_initialization_transition.md` | 18715 | `5ab2b390ab2d40b238932d658cd1986381bafe9514ba5fa9d25f1d3f18507759` |
| `DOT_conditions_stage02/proofs/S005_iid_algorithm_separation.md` | 19549 | `54071248416106afcc8f51734bc8ed019135ec2502e02d6e49fd09a45e6065e6` |
| `DOT_conditions_stage02/proofs/S006_near_iid_and_two_step.md` | 28893 | `17644d47e3b899d141c61251858aebbc1b64848306d77b0a210179b1472a2b30` |
| `DOT_conditions_stage03/proofs/S011_complete_proof.md` | 30903 | `8286e13dabe19b4b7adc72ab11bc65a5a8594f70c507c6321bc398f46860c762` |
| `DOT_conditions_stage03/proofs/S012_complete_proof.md` | 43629 | `7021dea45b1a262cd6ff71caee4cd8a1f7a973828313100d3d6ad5acbfe09132` |
| `DOT_conditions_stage04/proofs/S015_complete_proof.md` | 48577 | `452f4274a9b47635a4d3d7995db09f222b10d024cef935b9b1f5370ebad9db69` |
| `DOT_conditions_phase_review_20261028/proofs/S016_complete_proof.md` | 23244 | `bfb6ab6e9bd403d4a8502da6474b51f8b31940189dad339cfa5dac1b5ecbf645` |
| `DOT_conditions_phase_review_20261028/proofs/S018_complete_proof.md` | 33339 | `0bd13ecdc9d33df0cd56a5367885fa6779ce6fcabf16caf59ecbf9ed8e7b4d46` |
| `DOT_conditions_phase_review_20261028/proofs/S019_complete_proof.md` | 15887 | `7cf5eb6a408109d534bc1537a7123b90201795d5b6450832b2649ccba739905b` |
| `DOT_conditions_stage02/inherited/L1MAX_statistical_proof.md` | 15130 | `b430fe3d176ecefc00ac575670ea13ffc5d5799f9e232a10375333a0547f44e4` |
| `DOT_conditions_stage02/inherited/GU_UC_and_IID_interfaces.md` | 5188 | `f4abb8e565d58c5af9f6f52ca1e83fc78989dfeb70554e4d22ad1fab8308d275` |
| `DOT_conditions_stage02/inherited/MM5_statistical_proof.md` | 21262 | `4d5e865ebe00846662cef1830be02bf52cc2b839eca8a0600f8baa501ada6078` |

## 每项新结果真正使用的接口

- **S023**：S020 的 D 状态实际终点占用、完整末对齐两步 split 和未证明 TARGET；S021v2 的固定公开模板边界与 state-dependent hazard 配方；S012/S015 的精确 K≥13 几何、初始化、完整 product law、首次失败目标与 vulnerable count；L1MAX 的任意 μ 原完整规则 48g；GU 的 first-w 占用机制；S016 仅用于既有 lower 包络与窗口背景。并未把受限模板或类别链结论推成全类上界。
- **S024**：S022 固定 g 规则的 IID 853i 与精确 disjoint-triple／边界恢复；经 S022 的 L1MAX 一般48g、S005 pooling及全数据IID lower；S001 的平稳原规则48a和整数末行占用；S011 的 h_b、B、强β及F原域；S006 的全状态共同中心与任意μ pooled鞅；S018 的保留全部中间符号的 first-success stationary suffix；S019 仅在原 M≤K⁴／β≤1/2 条带的128H。其 NEXT 不属于任何证明前提。
- **S025**：本包 S024 的确定样本 multinomial尾、IID triple恢复和同一算法的旧保证；继承 S022 的原完整 IID 二阶矩423K³/n；S006/S011 的全状态共同中心与 pooled鞅；通过 S024 继承的 S001/S011/S019 正确有限域，以及全 M+2 数据 IID lower。新的 clipped edit、真实终点刷新、CT/GT/SEL和并集取最小值在本包自行证明；不假定原依赖历史有 IID 行栈。

S003/MM5 等更早接口通过已经接纳的 lower 或边界链间接保留，不能反过来称新证明重新认证了它们。数学审查的实际源接口、有限检查与限制原文均保留；集中来源表省去私有控制与重复管理条目，不省去科学依赖。

## 接纳和证据口径

S023：完整 v1 六单元独立上下文审查 + v2 精确差异和保留前提的有界复核，最终仅接纳 v2。S024：完整六单元审查后接纳较小并集。S025：完整七单元审查后接纳反例、NI与原 Ω_closed 闭合。各原审查的有限检查是历史证据，本次装配没有重新运行这些数学枚举，公开 verifier 只检查字节。

各正文中的检查器文件名、计数和哈希是原证明／审查的历史证据标识；脚本与输出不随本科学包附送，不是读完符号证明所需的黑箱。

本阶段没有新外部论文黑箱或第三方全文。科学闭包在包内自足可读；不等于包含全部控制记录、原始日志和项目恢复资料。所有旧归档字节不变，历史 NEXT 与 B 尚未完成的语句不得当作当前状态。
