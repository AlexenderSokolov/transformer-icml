# C4 v2 固定组合审查

Counter，2026-10-25。**Scoped PASS：新组合、接口和科学比较未发现承重必改项；
mandatory corrections=[]。这不是独立全包审查、C4 native admission 或 root acceptance。**

本轮复用已接纳 C1–C3 与既有 scoped reviews，不重证组件，不以有限诊断充当全称证明。
已核对11个verbatim原文块、54个伴随文件、24个admissions-v2归档，哈希/长度均匹配；
C2/C3请求中的完整proof分别与固定源相同，C3包含A–K，Fact后缀与依赖也匹配。

| 本轮主要固定输入 | SHA256 |
|---|---|
| lead/fixed-package-candidate-v2.md，188206 bytes | 7da57327e4b60288358aacde288aa27a156e944247324b6e2c40da878676ce2f |
| lead/fixed-package-manifest-v2.json | 9bf3e8dcac27b349c5d079c7f55dd9f9bc6272d63f58350c27f1cce97dc18c2c |
| lead/integration-theorem-v2.md | c12b62d4b6d9d8e8977b40724d157f3835b46ec713220ec8e21ddeedf140825e |
| lead/primary-comparison-v2.md | b9d021f516a61d2d73dfe9f0c0b5279237674f44c037e65868cca3c0c302b4a5 |
| lead/c2-c3-admission-readback-v1.json | 8c25b9b3fe5e57e2b833d35b88099e6d252bfa0efc022448fa8cac306a8684c9 |

当前Euler readback确认 C1/C2/C3 DISCHARGED、C4/root OPEN、acceptance=null。
真实已接纳依赖如下，均为 VALID/PASS、LLM_CHECKED_PROOF，非形式化认证：

| Unit | Fact | Evidence | Predecessors |
|---|---|---|---|
| C1 | e418ec34b7dbc4a6 | 4857f1b1b5d10ab74a979362e3d0c3068c9634016e4ce6b6a0609ed577eb2eea | [] |
| C2 | 4f0e99ed26dfeeeb | a4152a1fc70cbd2d4ece0bea8390fb68c0ed76beb4e11a8d9dd495a8250764ee | [e418ec34b7dbc4a6] |
| C3 | a47d648004a9a607 | 3e576827ab335e24f661561d9aa89f035a36925f450dd2daf0be3b166ab3cd27 | [] |

组合检查结论：

1. **先路径、后风险。**C3恢复同一实际S_N选中的3..m精确counts，再执行C2同一
   clipping、half-up和固定coordinate1 residual；小N/Q2/常数行也一致。
   因此decoded H(x)=G(x)逐路径成立，损失先相等再取平均；在概率u>0的S_N=00上
   条件期望也相等。没有新增独立query、额外样本、mixing误差或1/u误差因子。
2. **量词及常数。**平均1/32768、条件3/32768的sum-order常数由原max下界正确推出，
   不是同源损失相加。下界仍允许完整history、独立seed及固定-u比较器知u；
   同一个上界程序不知道u,t。固定正u的收敛、triangular family与U_N>=3/16384
   没有混淆；1+Nu条件只是评价域。必要/充分容差条件也没有被写成精确可行域。
3. **端口和资源。**C2 compact b位、可选2b/3b+1，与C3 guarded3(b+1)或2(b+1)
   分别收费，只有decoded vector相同；same-bit equality仅限共享C3端口的基线。
   局部converter成本没有替代完整history/mask/hold/生成/峰值账本，各成本域未拼接。
4. **Primary及科学范围。**HJW普通可逆一阶gap定理不直接套D1；高阶符号反序不推出
   pair detailed balance，较大类lower不移入子族，一阶子曲线也不扩成整个D1。
   Paulin是path-TV/浓缩工具，Geiger–Boecherer是known-target量化直接先例，
   不是本未知law条件实验。三篇均保留原版本/hash；没有新增检索、全球新颖性、
   精确KL量化最优性、内部资源必要性或优化神经优势推论。
5. **历史与交接。**包封面和新组合正文明确覆盖当前native状态；verbatim旧headers
   只记录来源创建时状态，不作为当前pending/排队指令。真实C2 wrong及修复、
   endpoint/guard反例和source authors均保留。责任交接要求未来提供真实root/audit
   IDs，并明确stage SOLVED不结束T1→T2→T3母题；没有虚构已完成的交接接纳。

两处非阻断的措辞可更精确：Paulin简表的“1/pi factor”宜写成“N_q=1/pi(s)，
相应界可含sqrt(N_q)”；量化段的t_i>=1/M应明确限于t本身属于辅助P_M的情形，
不是一般正target的域限制。详细primary表及上下文已有这些区分，当前组合不依赖误读。

对原C4障碍 `0def94abb5dd20e9fc11024c4f656ce7f0d77ef78740e17ef61155836d95a99d`：
完整材料、真实组件接纳和直接量化primary映射已实质补齐，不能仍以“缺这些文件”
描述当前包；但独立固定全包审查及C4原生接纳尚未发生，因此不能据此清除整个障碍。
本报告不修改其历史记录或状态。

剩余门槛：独立Verifier固定组合审查 → C4以三个真实Fact为前提的native admission
→ root conjunction admission → 单独final_audit及实际责任交接。不得预设后续PASS。

本次新增Fact IDs=[]、Evidence IDs=[]；[Non-scientific operational metadata omitted.]
[Non-scientific operational metadata omitted.]旧C4 taske0845dd9未恢复；8条SUSPENDED、protection
状态、两旧根和parked routes均未由本轮改动。完整核对记录见本轮manifest/checks。
