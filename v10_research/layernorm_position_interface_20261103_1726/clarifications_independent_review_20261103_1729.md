# 独立审查：pre-LN 输入、分数与量词澄清

两份只追加、不覆盖的澄清与指定全网证明相容，准确封闭了输入侧信道、score 接口和有限 N 网络选择的歧义；在它们明确限定的范围内未发现数学问题。

- `input_and_quantifiers_clarification_v1.html`：SHA-256 `b0e60b8b20d9224c0701f8e4f2e76b81f7d40e43c7366422d324037850e9ecbf`。
- `score_interface_clarification_v1.html`：SHA-256 `adc985442cc6c377caf0609d1ca96c5fba977507dbf226f0979ff42a9f0f089c`。
- 所补充主稿 `preln_actual_risk_obstruction_v1.html`：SHA-256 `037a0f737d8afc86ec65ebdd3321b9d324781dbf91c0c92229b7f593a6b030a7`。
- 主稿及 copy 路径独立审查 `independent_analytic_review_20261103_1728.md`：SHA-256 `314d9c9c76b5d5f16f31e0051dd1502b221dcca55b357d4eb62859490269c171`。

对等长比较，输入是固定有限 token embedding 加同一 token/源无关的位置向量和固定特殊符号标记；末位相同，较早各位因果保持相同，位置向量虽可随 N 增长仍逐坐标抵消。固定源独立的 score 偏置 B(i,j,N) 若统一有界，则只增加统一 logit 常数，且相同长度的两条历史有相同 B，故查询变化贡献与单 key O(1/N) 论证不变。禁止额外序列依赖偏置排除了绕过证明的全局 token 侧信道。澄清限定确定性推理；含 dropout 或其他随机机制另需说明。

所证量词是对每个固定网络，在同一固定源上有 liminf_N risk_N≥1/32；网络依赖常数可极大，因此这并不推出逐个有限 N 的 inf_network risk_N 有同一个正下界。不能无说明地交换 inf_network 与 liminf_N，也不能把论证用于可随 N 改权重、深度、score 范围等的网络族。对每个固定网络，最终概率输出的常数可以不同；固定源对所有这些网络相同。

方法：只读源文件、SHA-256 核对及解析证明；没有实验、枚举、仿真、科学代码执行或源覆盖。该证明属于特定模型类，不是全部 normalized Transformer 的限制。
