# C2 v2 局部输出成本修复审查

Counter，2026-10-25。有界审查仅覆盖新 §2a、v1→v2 diff 和实际 gateway 拒绝报告。
不重审 C1、既有 C2 风险论证或 C3，不改变原报告及历史记录。

| 固定输入 | SHA256 |
|---|---|
| prover/c2-proof-v2.md | b8de1c83444044357790ab8062caa443a701f260b7d631dbae35f85c308f667c |
| prover/admissions-v1/c2-v1-to-v2.diff | c33d01c2f5a02714b17080d4cbe275a4a578c2fb4d313a5e7f073864c0746bbc |
| prover/admissions-v1/c2-response.raw.json | 302eafcaf12cc877e93648096ca6a878ef334e11390cc14e1e321c0008020d8b |

**Scoped PASS：新增引理足以回答本次 gateway 的局部 output/converter 成本缺口；
没有发现必须修改的承重错误。此结论不是 C2 的 native admission 或完整 C3 接纳。**

原始响应为 accepted=false、verdict=wrong、transport_status=ok，critical_errors=[]，
仅一项 gap：未声明输出编码、位数、操作数字长和有限 bit 成本。不是 transport 故障，
也未要求改写统计/表示论证。diff 的数学新增为 §2a，其余修改是依赖及接纳状态文字。

## 局部证书核对

1. **端口。**固定公开 b,Q=2^b 时，next1 numerator j1∈[1,Q-1] 恰用 b 位，
   canonical 解码为 ((Q-j1)/Q,j1/Q)。另一 numerator 用 b+1 位 borrow-chain
   中间运算恢复，结果仍只需 b 位；16(b+1) 的 elementary 成本可保留。
   同时发两 numerator 是2b位，再发 literal denominator 是3b+1位。
   固定 radix/punctuation 是端口约定，不是免费可变长 header；其他协议另收费。

2. **字长。**ell=ceil(log2(N+1))，K=b+ell+6，故 K>=9。
   非常数分支 N>=6,Q>=4，精确 nominal counts 满足 D<=m-2，d<=m，Z<=4m。
   最近网格 dividend <16mQ<=8NQ<2^(b+ell+3)<2^K；ceiling dividends <4mQ。
   normalization 中 U=3d、V=4(C+1) 及全部乘加中间量也在此 guard 内。
   DIV 的 shifted remainder <2*divisor<=16m，仍可容纳；residual 非负，
   无 unsigned underflow。Q 本身用 b+1 位。泛用乘法的完整2K位积必须用
   两个 K 位字共同保存，后文明确的2K accumulator 已给出这一实现。

3. **库存。**两个 normalization 块10/9项，nearest6项，ceil/residual11项，
   加 controller12、routing8、loads16，总数确为72。这里甚至把两个互斥分支
   的容量相加；没有要求无效分支也执行 DIV。min/max 的 compare+select
   另按64K收费，未冒充单个 Boolean 操作。

4. **精确整数运算及时间。**school product 的80K²、DIV 的128K² elementary
   上界有足够余量覆盖列出的 ripple/shift/select 操作。DIV 的 prefix=q*d+r、
   0<=r<d 不变式给出精确 quotient/remainder；没有截断实数或 log/exp oracle。
   在文中声明的顺序 bit-read/write/Boolean 模型下，计入每 elementary operation
   的128K地址/控制余量后，32768K³/word 的保守界成立。
   72*32768=2359296，距3000000尚余640704；初始化与擦除共至多256K次写，
   最大端口写出3b+1次及可选减法16(b+1)的总额<=275K+17；即使再逐项乘
   (128K+1)收费，其总量也小于4000K³，仍远小于该余量*K³。
   因此3000000K³可保留。它不是 dense network 或其他未声明存储模型的成本界。

5. **空间。**至多128个 K位 data/scratch registers 为128K位；完整乘积、商余及
   常数可置于这些字中。K>=11时 ceil(log2(128K))<=K；K=9,10用2K地址仍足够。
   额外 addressing/control 的有限字数在256K总 live 界内。固定循环程序不是免费
   K依赖的展开指令带；公开参数的载入/储存已在局部模型中收费。

6. **全部边界。**N=3,4,5、b=1及 rows01/11走 uniform，写出 Q/2 的 b位串，
   不请求 counts、不执行除法。active 分支在零 counts 时 Z=8，仍严格为正；
   endpoints、Q=4、half-up ties、exact divisibility 和 row10 residual1
   使用同一整数 DIV，字长/循环次数不变。修复没有改变这些分支的数值语义。

无强制修补。可选文字澄清：首段“A second K-bit scratch word can hold a full
product”宜补“together with the first word”，与后文2K accumulator完全一致，
避免误读成一个 K位字独自容纳任意2K位乘积；这不改变当前已明确的实现或成本。

## 依赖和证据边界

这是 selected exact-count 输入到编码输出的**子程序成本**。完整预测器仍按既定
历史函数取 counts；§2a 明确不免费提供它们。history-to-count 获取、实际 query
绑定、观测历史工作空间、attention/masks/positions/routing/holds 仍由 C3 证明和收费。
不得把 T_convert/S_convert 当完整 predictor 的总成本；这里也没有用 C3 作前提。

本次 Euler readback 核实 C1 DISCHARGED，沿用唯一已接纳前提：Fact
`e418ec34b7dbc4a6`，Evidence
`4857f1b1b5d10ab74a979362e3d0c3068c9634016e4ce6b6a0609ed577eb2eea`。
未读取或重证其 accepted proof。C2仍OPEN；既有 failure
`b97ba0738f1848747bd400c3e74405482a403fe463232e79f62fa7068938d708`
保留，由后续正常 gateway 决定本修复是否接纳。本次未发现新障碍，不重复登记失败。

本次新 Fact IDs=[]、新 Evidence IDs=[]。无提交、调度、检索、旧诊断重跑或
图状态变更；[Non-scientific operational metadata omitted.]
[Non-scientific operational metadata omitted.]检查记录和固定清单仅是本次局部审查材料。
