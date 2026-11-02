# 032 Prover 正常接纳交接

准确 OID：02da4576308aa8b8abc12ded4c285018a0c3ef4375f713b027fde13927e15fff。一次完整 submit_proof 已正常接纳，原生状态 DISCHARGED / VALID；没有拆常数或删减冻结结论，没有修订后重投。

- Fact：`372cbc90282df2cd`。
- Evidence：`1a61c7931a3b8ee13da63e8e24e758106308055d829d8e5e60195fbca96d0cf0`，LLM_CHECKED_PROOF / PASS / VALID。
- Fact 文件：`fact_graph/facts/372cbc90282df2cd.md`。
- Fact SHA256：`e7295c4903277b5d403a453f429a62a60a5dc8ca6a6b04e9917646088fb39476`。
- 冻结声明 SHA256：`7311bf5eca3b4800d0da5a9e292ed8299c224856137f7016ffe0ebf64e15ab64`，原生 statement 与冻结文件逐字节一致（9476 bytes）。
- 完整证明：`complete-proof-v1.md`，470 行，SHA256 `a993aaa8c844642fa8c99b6c569453f0de8cf747a33cb76af7b5f98fbc1d1f00`。
- 实际载荷：`submit-request-v1.json`，SHA256 `fc1a1f355df3f0218ef8abcf51978bdcc70d02dc20777c571c65e60c81c43695`。
- 正常回执：`gateway-raw-receipt-v1.json`、`gateway-receipt-v1.json`；transport_status=ok，root_final_audit_required=false。

## 完整结论及承重步骤

在 K>=22、M>=1、全部整数 h>=h_N、D>=0 的原实验中，证明

    2^-80 min(1,T_K+Psi(K^4 D/Q)) <= R_V^Pi
       <= min(1,64T_K+Psi(K^4 D/Q)).

同一 Pi、同一最终 V 切口、同一有序 floor/residual 后缀；只针对总 actual 均值风险。D=0、巨大预算、M=1 和所有 horizon 余数均包含。对任意合法公开序列，同时证明风险趋零当且仅当 T_K->0 且 K^4 D/Q->0。

正文 §1 从016联合故障界取delta=gamma=0，经真实J和正银行归一化，使用Psi次可加以及49+2sqrt(39)<64支付上界。§§2–3在T_K<1推m>=4，完整构造固定齐次clock和全余数初pair；保留k=L-1的任意初始化及departure0随机门，完整路径律给p_j及条件Binomial计数，未删除历史或另加独立query。

§4为所有历史定义共同核，仅在公开C×Dgrp末对向0号坐标注入min(D,Q/8,2Q-V0)。实际SRC误差78证明容量足够；p1<K-1的目标坐标floor方向和所有K个正质量给下界。§5保留j=0和有限m，用条件Jensen及有限积分比较得到

    E_clock TV >= eta0 U/4 ln(1+M/[2U(K+1+eta0 M)]).

§6令x=K^4 eta0。x<=T_K²时由MM5覆盖，x>T_K²时由上述调和界支付log和饱和；只将不同源的sup下界取max。eta0=min(D/Q,1/8)满足Psi(K^4 eta0)=Psi(K^4 D/Q)，故大预算同样覆盖。保守估计已足以推出冻结2^-80，无另拆常数节点。§7证明序列充要性，§8保持原完整实际费用。

## 实际直接依赖

| Fact | Evidence | 实质使用 |
|---|---|---|
| SRC fef8372728290b45 | e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505 | 同一Pi、实际V误差78、原切口/后缀和完整费用 |
| 016 a53804d650803060 | fef1785395851e47b5ca0b719640449061718f4c670bfcd74c24cf0aec696c88 | 48T、实阈值TRUNC、原Pi联合故障上界 |
| MM5 946d42d5bf502eb4 | aa23c442ca1006c6ac0b12379f64a0fa500fbbd6a2e41c798b7a4de3952baa82 | 恒等核下任意共同全历史预测器actual下界 |

无其他直接Fact前驱。030仅复用全余数源的写作，相关源/路径证明已自足写入本正文；未外推030 CLOCK/PARTIAL。031和Dot成果均不是本项前提。详见`dependencies-and-reuse-v1.json`。

## 核验与原状态保护

`input-check-v1.py`核原生/冻结绑定、预算及三个Fact/Evidence。`exact-preflight-v1.py`以整数/Fraction检查1683条完整源路径、102个余数配置及180个一般正银行floor代数实例；这些只是有限诊断，不替代一般证明，也不是Pi实测、浮点风险、compiler或ledger。

`acceptance-check-v1.py`验证原生DISCHARGED/VALID、Evidence PASS/VALID、Fact content hash、完整proof和真实请求、原statement/scope、三个准确直接前驱及14项提交冻结hash。网关只规范化证明末尾LF；Fact中的证明段SHA256为`5f831b4858543644b986fce54641ebda70f691a83082f34eda452b7eb0f8c055`，不是正文中间内容变化。

24个旧Fact均按原Evidence content_hash在当前Fact目录逐项匹配，内容及旧依赖未改。历史Evidence的producer是提交标识，不能直接当成当前Fact文件名；核验脚本按真实内容hash绑定，并记录匹配路径。所有旧Evidence、旧obligation（除032本身）、routes、root acceptance、预算及旧关系保持。

原生活动blocker视图中，032关闭后不再列附在它上面的Dot投递诊断ebfd7e3592f7556d4c7131eaa28e133221b39b6f79b5c9a35171cc37ed250ebf。原始完整记录保存在`native-before-v1.json`；未调用任何failure更新，也未宣称Dot入口已找到或任务已投递。两个027诊断仍逐项不变。准确差异见`native-preservation-check-v1.json`，没有把blocker视图说成完全不变。

[Non-scientific operational metadata omitted.]Counter另项互补检查由Lead协调，不把讨论或枚举视作本项目Fact。本项接纳依据上列正常独立网关。

## 费用与剩余范围

同一SRC dense/uncached主实现，真实p=4h+4ell+64，全部M+3位置、六头、QKV/mask/input/query/endpoint、full products/remainders/guards、holds/copy/clear、输出、offline完整格式及逐phase共存总peak全部收费。故障核是信息层实验；物理注入器/保护器、selector、移动、存储和程序费用须另付。无新decoder、snapshot/count table/cache或历史回读。

未运行compiler、literal ledger、batch或profile。[Non-scientific operational metadata omitted.]最终`manifest-v1.json`绑定全部交付、冻结文件、来源和本次Fact，`manifest-check-v1.json`记录重算结果。

K<22、h0-only精度、master联合K、任意decoder sharp故障率、物理纠错及真正资源比较未由032解决。[Non-scientific operational metadata omitted.]Dot后续统计任务仍归原Dot。冻结032合取内无本次网关报告的剩余数学缺口；不宣称v10母题完成。
