# 科学正文复制与哈希核对证明

## 核对结论

每个保留的科学片段均与所列原文件字节区间完全相等；目标文件哈希、片段哈希、拼接科学正文哈希均已重新计算并一致。S 单元的原证明与原审查哈希另与其已接纳记录核对。源文件保持未改。

该核对不是数学重新审查，更不是形式证明。新增标题、导读、摘要、编排说明位于复制区间之外。原有数学编号保留；剔除的是身份、运行、控制、流程与历史提交状态，以及本阶段不使用的继承实现/资源部分。完整继承接口与省略范围见 SOURCES.md。

## 可复查方法

COPY_MAP.json 中所有字节区间使用从零开始、左闭右开的 UTF-8 字节定位。对每个 span，读取原文件 `[source_byte_start:source_byte_end]` 和目标文件 `[output_byte_start:output_byte_end]`，两者必须相等且 SHA-256 必须等于 span.sha256。源全文哈希防止定位到不同版本；目标全文哈希也覆盖新增编排文字。copied_body_sha256 是按记录顺序拼接保留片段的哈希，不包括新增文字与区间间插入空行。原文件名与全文哈希一起唯一指认来源，不需要公开内部绝对路径。source_line_start/end 是该非空字节区间触及的起止行号，从 1 起、两端包含；末行按 end−1 所在行计算。全部行号也已核对。

## 核对的原文件与目标文件

| 原文件 | 原文件 SHA-256 | 目标文件 | 目标文件 SHA-256 |
|---|---|---|---|
| S001_proof_v1.md | `6d00dc0b99ff0d6932b171bdd3e243ee923ca5d8a864cdac407c815e37f26f6d` | proofs/S001_stationary_upper.md | `7fa8b2119f84d9f382da80516aa8b3c277ebd2c4587dffd58d24bf16b11a77d4` |
| S002_proof_v1.md | `ac5e20d249704e298454f1b3633eedcf4026847801922a584a9043304cbdbdf4` | proofs/S002_stationary_lower.md | `859e02a709ed270324432762af79c1949329d80ba3c324e1a1a6a542ad88881e` |
| S003_proof_v1.md | `efa75c1ec0c1c3c8aab6956397f277bcf27dd148a480921b86186d6984f248e5` | proofs/S003_initialization_transition.md | `5ab2b390ab2d40b238932d658cd1986381bafe9514ba5fa9d25f1d3f18507759` |
| S004_proof_v1.md | `a0f4f3cb2daf8f3191281d5e0fcdbb3f645d4118f7373f5fb1b8427006a1959a` | proofs/S004_mixing_original_and_suffix.md | `e04ea48a52c5943b65d3e5472555de5c6a7ccd83b30f9509d620fb9eec426bdb` |
| S005_proof_v1.md | `389d743cebf89f7afeb4855ceb712bfec8b3b216b10ae077b23dd980b03c7eba` | proofs/S005_iid_algorithm_separation.md | `54071248416106afcc8f51734bc8ed019135ec2502e02d6e49fd09a45e6065e6` |
| S006_proof_v1.md | `88f150f0d316825bae1fd5718878e863991be64329ba92d0a3865919ca3fc4b7` | proofs/S006_near_iid_and_two_step.md | `17644d47e3b899d141c61251858aebbc1b64848306d77b0a210179b1472a2b30` |
| S007_proof_v1.md | `622e02f827feda6645641024477929066c67c68adba26bdfcd2621bab1683b24` | proofs/S007_three_step_reset.md | `aa57bda8d79f77fe5053996fdc5ffb9e1bcce599cdc76f19f2ac5eb5dbad9af9` |
| S008_proof_v1.md | `8e49cf5c7655e9db40454dba484f8bb3a9049505e52f2064e8cd59a6ff3b218d` | proofs/S008_qualitative_positivity.md | `f898ff233b9dede048fc4e26b49fb8b355c534c5c113031444c8230a4c98819e` |
| S009_proof_v1.md | `f720e3513917778a6f21fe38be600a64a5c1726a0311dd2eda4fde992e0f1fda` | proofs/S009_finite_exact_reset.md | `38bceaa3a22f9a06cf9792a2c062c471dee77418d6fb6578876b01d291e908c2` |
| S001_review_v1.md | `affe3eb2fa4c7f35f240a227758141173f5efa2af950966656c99337bc1cc1e8` | reviews/S001_mathematical_review.md | `7d850ab47469f079ae12fbb2ba0b53b954a9b087d02ad14c531e829876fef3f2` |
| S002_review_v1.md | `031d75fa365a6f9640664ddd0745729f024f5ab11c1cf57475960a1c0ccc8a67` | reviews/S002_mathematical_review.md | `61b7ef9964e68d3877f289c955fcf489611d6259d1e878212c066ba8090c4a55` |
| S003_review_v1.md | `8a6ceb06c315b49d881a710c90f9a2cb0ce41fe03c69373c6f46ea136d74d226` | reviews/S003_mathematical_review.md | `200fb9bf2e58d7ba2a3966ea8b5aa4da13c30cca82dc8d2ffb58187efe8edae3` |
| S004_review_v1.md | `9b3148ce4ac46090d9311a4f52d65dcb8f42bbfdb483e180edf830b3efa33699` | reviews/S004_mathematical_review.md | `b03d4f40f302905c287c1d5b92a24cc1de6af741075419dbdeacff296c80b22b` |
| S005_review_v1.md | `836fd40704d2d32a064f0efda7fc812d80855137c2aac4bd71ac2175f4c85bde` | reviews/S005_mathematical_review.md | `182c5899b6ec57aebe4d12f18b7b7bedf6b2761c2377c8d438ebe471f9e235b7` |
| S006_review_v1.md | `4cd7abbbfdadad9f559c4ee848dd8444cbe35d8966f8327a74df5631afdae9b1` | reviews/S006_mathematical_review.md | `c4e2400b6e78e39ab309b086c40604b058fa5316cefc2ddc45bbb9fffb3fa479` |
| S007_review_v1.md | `77b0ef21dcbd37a9ac1ba4ffb218cc7e806ad88f1c60a7c457d3586522a3e699` | reviews/S007_mathematical_review.md | `339155e75ffa32e2656c21f53716567a9262bd9f1e77925d210b1ef4b264d4e4` |
| S008_review_v1.md | `c86d149ee275d7de96a8a18b0694c6905bcbfcd7e6ab6fb90663e915dd31085f` | reviews/S008_mathematical_review.md | `fb87d39074b445b7496dd460bcac81b35181dda79f0e85b9825b1a3c3bc09e78` |
| S009_review_v1.md | `beb58f9bcc8de0910c8eae868f71eef534042d57bdc36720751340b0050d0f63` | reviews/S009_mathematical_review.md | `66f3a326ee3bc928d930c4fe2bccabe64134571212e8e4f01093c1bbad82cd3f` |
| L1MAX-proof.md | `96397d48a9c0b118991b14cac4b1c48b7f06613825275a5a28d3f489399287d9` | inherited/L1MAX_statistical_proof.md | `b430fe3d176ecefc00ac575670ea13ffc5d5799f9e232a10375333a0547f44e4` |
| MM5-proof.md | `19d2b5e4d5a5c7c5f152f14b287bd42a5f130de4428c82f82e1a5916fe9400f3` | inherited/MM5_statistical_proof.md | `4d5e865ebe00846662cef1830be02bf52cc2b839eca8a0600f8baa501ada6078` |
| GU-proof.md | `cd15ce0bdd6821dbfce47784975483e93acf7834b58d218e098ba584496ca4b6` | inherited/GU_UC_and_IID_interfaces.md | `f4abb8e565d58c5af9f6f52ca1e83fc78989dfeb70554e4d22ad1fab8308d275` |
| MM5-independent-report.json | `feb0d0fcc5ca03efa229425c24afa521b3ec6226786fd4b5bccae5983555862e` | inherited/MM5_review_scientific_excerpt.md | `4d47d00208b072a31f4004697e71358b22c39ef1d3b3c75c0615a1dca3b80a0a` |
| L1MAX-independent-report.json | `5850d4250f6533550229f2f2d531bcce06d58b039136fd0d15bc0b5cc8a3eebb` | inherited/L1MAX_review_scientific_excerpt.md | `89ab49844e640763a6ce33d3c7425b3705fcebd090c46f9dd389227d2fbcaa73` |
| GU-independent-report.json | `584b499e1888174dd468769aab1922e2b265d138e37f2cf6af642c21ccc336f2` | inherited/GU_review_scientific_excerpt.md | `73894d5e4c33438307ea7ee6f445138bcac1812d1b87eac4ba104105a010cea5` |

本轮核对 24 份科学副本、77 个原字节片段，全部通过。

## 真实性边界

原审查的 ACCEPTED 针对原证明版本。此包只忠实复用该数学与审查理由，不能称复制件或中文摘要已经另获独立数学审查。摘要经过编排核对和逐页视觉检查；那些检查不增加原定理的证据等级。
