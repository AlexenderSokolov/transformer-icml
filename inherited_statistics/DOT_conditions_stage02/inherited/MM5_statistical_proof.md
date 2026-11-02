# 继承 MM5 一般初始化共同算法下界

原提供资料中已接纳证明的科学片段；本次未重新独立审查原始全篇。文字及数学保持原字节，映射与源文件哈希见 COPY_MAP.json。与本阶段无关的实现、故障、资源及历史流程内容不在本件范围。

## 1. 准确命题和算法量词

设 \(K\ge2,M\ge1,N=M+2\) 为整数，字母表 \(\mathcal A=\{0,\ldots,K-1\}\)。二阶源的一条实验内使用固定转移表 \(\theta\)，允许零概率边，初始对分布 \(\mu\) 任意。对
\[
Y_t=(X_{t+1},X_{t+2}),\quad0\le t\le M,
\]
观察全部 \(H=X_1^{M+2}\)，实际目标为 \(\theta_{Y_M}\)。预测器 \(\mathsf A\) 是同一个从完整历史到 K-simplex 的概率核；可依公开 \(K,M\) 选择，可用源独立随机种子，不能读取隐藏 \(\theta,\mu\) 或 \(X_{M+3}\)。记
\[
R_{\min}(K,M)=\inf_{\mathsf A}\sup_{\theta,\mu}
 \mathbb E_{\theta,\mu,\mathsf A}
 \operatorname{TV}(\mathsf A(H),\theta_{Y_M}),
\qquad \operatorname{TV}(p,q)=\tfrac12\sum_z|p_z-q_z|.
\]
我们将证明全部上述有限参数均满足
\[
R_{\min}(K,M)\ge 2^{-16}
       \min\{1,\sqrt{K^5/(M+1)}\}.                    \tag{MM5}
\]
这里每个下界都作用于同轨迹 actual 的 TV 第一矩。辅助计算 KL 只是测试工具，不把 KL 或 TV 平方风险当作目标。所有下界对任意一个固定共同随机算法成立，随后才取算法 infimum。

## 2. 有限 Euler clock 与完整齐次源表

先固定 \(K\ge12\)，令
\[
m=\lfloor K/4\rfloor\ge3,\quad L=m^2,\quad b=\lfloor m/2\rfloor.
\]
取四组互不相交字母
\[
\mathcal C=\{0,\ldots,m-1\},\quad
\mathcal U=\{m,\ldots,2m-1\},\quad
\mathcal V=\{2m,\ldots,3m-1\},\quad
\mathcal W=\{3m,\ldots,4m-1\},
\]
并将 W 中字母固定编号为 \(w_1,\ldots,w_m\)。当 \(4m<K\) 时，剩余字母留在原 K 字母表中，下面仍为全部 \(K^2\) 行赋值。

存在周期字 \(c_0,\ldots,c_{L-1}\)（令 \(c_{t+L}=c_t\)），使
\[
p_t=(c_t,c_{t+1}),\quad 0\le t<L
\]
恰枚举全部 \(\mathcal C^2\)，每个 pair 一次。所需有限证明如下。在顶点集 C 上放置每条有向边 \(a\to a'\)，包括自环；每点入度和出度都为 m。沿未用边走到无法继续时，终点必为起点：否则终点已用入边比出边多一，平衡度数保证仍有未用出边，矛盾。得到闭游走后，剩余图仍逐点平衡。如果还有未用边，则当前游走上有顶点具有未用出边。否则当前经过的顶点全部出边已用，由完整图性质全部顶点都已被经过，从而全部边都已用，矛盾。由这个顶点在剩余边中再走闭游走，拼入原游走。每次至少多用一条边，有限次后得到每边恰用一次的闭游走；沿其读顶点即得周期字。自环不改变平衡论证。

字中有符号 0，故可循环旋转使 \(c_5=0\)。为每个 m 固定一个这样的字。由于 \(L\ge9\)，保留的 \(p_0,p_5,\ldots,p_{L-1}\) 两两不同。此字是公开的有限构造，只依 m，不依未知参数或观测结果。

令
\[
\mathcal I=(\mathcal U\times\mathcal V)\times\{1,\ldots,b\},
\qquad \sigma\in\{-1,+1\}^{\mathcal I}.
\]
\(\sigma\) 在一条实验中固定。取公开 \(0<\alpha\le1/2\)；其具体值在 §6 选定。对 \(s=(u,v)\in\mathcal U\times\mathcal V\)，定义
\[
q_\sigma(w_{2j-1}\mid s)=\frac{1+\alpha\sigma_{s,j}}m,\qquad
q_\sigma(w_{2j}\mid s)=\frac{1-\alpha\sigma_{s,j}}m
 \quad(1\le j\le b).                                \tag{1}
\]
若 m 为奇数，余下 \(w_m\) 的质量为 \(1/m\)；W 外坐标为零。每对质量和为 \(2/m\)，加上可能的余坐标后总和为 1；W 内各概率至少 \(1/(2m)>0\)。

定义全部转移行：
\[
\begin{array}{ll}
\theta^\sigma_{p_0}=\operatorname{Unif}(\mathcal U),&\\
\theta^\sigma_{(c_1,u)}=\operatorname{Unif}(\mathcal V),&u\in\mathcal U,\\
\theta^\sigma_{(u,v)}=q_\sigma(\cdot\mid u,v),&u\in\mathcal U,\ v\in\mathcal V,\\
\theta^\sigma_{(v,w)}=\delta_0,&v\in\mathcal V,\ w\in\mathcal W,\\
\theta^\sigma_{(w,0)}=\delta_{c_6},&w\in\mathcal W,\\
\theta^\sigma_{p_t}=\delta_{c_{t+2}},&5\le t<L,\\
\theta^\sigma_s=\delta_0,&\text{其余全部行}.
\end{array}                                                       \tag{2}
\]
前六项分别属于 C² 中一行、C×U、U×V、V×W、W×C，以及 C² 中另一些不同的行，所以没有覆盖冲突；最后一项补齐所有其他行。特别，跳过的 \(p_1,\ldots,p_4\) 及含多余字母的行也已合法定义。每行都是概率向量。表内不含时刻、过去计数或随机选择，故同一实验确实齐次。每个后继符号 z 都通过 \((a,a')\mapsto(a',z)\) 产生 pair 转移，严格满足 shift。

从 \(p_0\) 开始，五步路径为
\[
p_0\to(c_1,A)\to(A,B)\to(B,Z)\to(Z,0)
 \to(0,c_6)=p_5,                                    \tag{3}
\]
其中 A 均匀于 U，B 的条件律恒均匀于 V，Z 的条件律为 \(q_\sigma(\cdot\mid A,B)\)。最后等号使用 \(c_5=0\)。之后确定地沿 \(p_5,p_6,\ldots,p_{L-1},p_0\) 运行。五步替换原 clock 的前五步，整圈长度恰为 L，不随 A、B、Z 或 \(\sigma\) 改变。

为精确说明相位，定义不交状态集合
\[
\mathcal D_0=\{p_0\},\quad
\mathcal D_1=\{c_1\}\times\mathcal U,\quad
\mathcal D_2=\mathcal U\times\mathcal V,\quad
\mathcal D_3=\mathcal V\times\mathcal W,\quad
\mathcal D_4=\mathcal W\times\{0\},\quad
\mathcal D_t=\{p_t\}\ (5\le t<L).
\]
它们不交是因为字母组不交和 clock pair 唯一。由 (2)，从 \(\mathcal D_t\) 只到 \(\mathcal D_{(t+1)\bmod L}\)。其并是闭支持，大小
\[
(L-4)+m+m^2+m^2+m=3m^2+2m-4\le K^2.
\]
从任一此类状态最终到 \(p_0\)，从 \(p_0\) 又可达其中每一状态，因此它也是一个闭不可约类。回到 \(p_0\) 的步数只能是 L 的倍数且 L 步返回必然发生，所以周期恰为 L。我们不要求全表不可约或非周期。该过程只有原 pair 状态，没有外加计时器。

## 3. 全余数初始化和所有 departure 索引

固定任意 \(M\ge1\)，写
\[
M=nL+d,\quad n=\lfloor M/L\rfloor,\quad0\le d<L,\quad
k=(2-d)\bmod L\in\{0,\ldots,L-1\}.
\]
固定公开 \(v_*\in\mathcal V,w_*\in\mathcal W\)。采用下表的 \(\mu=\mu_{K,M}\)，对所有 \(\sigma\) 相同：

| k | 对应 d | 初始对律 | 到第一次 UV 的说明 |
|---|---|---|---|
| 0 | 2 | \(\delta_{p_0}\) | 两次均匀选择产生 A、B |
| 1 | 1 | \(\delta_{c_1}\otimes\operatorname{Unif}(\mathcal U)\) | 初始 A，加一次均匀 B |
| 2 | 0 | \(\operatorname{Unif}(\mathcal U)\otimes\operatorname{Unif}(\mathcal V)\) | 初始对就是 A、B |
| 3 | \(L-1\) | \(\delta_{v_*}\otimes\delta_{w_*}\) | 先固定 \((v_*,w_*)\to(w_*,0)\to p_5\)，沿 clock 后再选 A、B |
| 4 | \(L-2\) | \(\delta_{w_*}\otimes\delta_0\) | 先固定 \((w_*,0)\to p_5\)，沿 clock 后再选 A、B |
| \(5\le k<L\) | \(L+2-k\) | \(\delta_{p_k}\) | 先走公开 clock，再选 A、B |

每一初始律支持于 \(\mathcal D_k\)，不依 \(\sigma\) 或 \(\alpha\)。初始对无需来自更早的、未观察的转移；在 \(k=3,4\) 时，\(w_*\) 来自固定初始化，不是一个未知 UV 行的标签样本。

从不交相位集合及 (2) 可知，对全部 \(0\le t\le M\)，
\[
Y_t\in\mathcal D_{(k+t)\bmod L}.
\]
故 \(Y_t\in\mathcal U\times\mathcal V\) 当且仅当 \(t\equiv d\pmod L\)。这些时刻恰为
\[
t_i=d+(i-1)L,\quad1\le i\le n+1,\qquad t_{n+1}=M.     \tag{4}
\]
观察的 departures 是 \(0,\ldots,M-1\)，因此恰有 n 次未知 UV 行 departure，索引是 \(t_1,\ldots,t_n\)；实际末行 \(Y_M\) 尚未 departure。

对 \(1\le i\le n\)，定义训练三元组
\[
D_i=(A_i,B_i,Z_i)=(X_{t_i+1},X_{t_i+2},X_{t_i+3});
\]
定义实际末对
\[
T=(A_{n+1},B_{n+1})=(X_{M+1},X_{M+2})=Y_M.           \tag{5}
\]
所有训练标签都被观察，因为 \(t_i\le M-L\) 且 \(L\ge9\)。而 \(X_{M+3}\) 没有被观察。除 \(t_i\) 外，其余已观察 departures 全使用公开的、\(\sigma\) 无关的行。

这些索引覆盖小参数：\(M=1\) 时 \(n=0,d=1,k=1\)，初始 A 与下一次生成的 B 构成实际末对；\(M=2\) 时 \(n=0,d=2,k=0\)，两步选择后停在实际末对。一般 \(n=0\) 时只有 \(t_1=M=d\)，没有未知训练 departure。\(k=2,n=0\) 会强制 \(M=0\)，不在本题域内；当 \(k=2\) 且 \(M\ge1\) 时 \(n\ge1\)，初始 pair 构成首个训练 context。

## 4. 完整历史的可逆编码和精确路径律

下面不用丢弃数据后的单向数据处理来证明下界，而证明整个观察实验的双射。

令
\[
D=(D_1,\ldots,D_n)\in(\mathcal U\times\mathcal V\times\mathcal W)^n,
\qquad T\in\mathcal U\times\mathcal V.
\]
从每个完整正概率历史 H 按固定索引 (5) 提取 \((D,T)\)。反向映射 \(G_{K,M}(D,T)\) 如下，它不使用 \(\sigma\) 或 \(\alpha\)。

首先确定初始 pair：\(k=0,3,4\) 或 \(k\ge5\) 用上表中的固定 pair；\(k=1\) 取 \((c_1,A_1)\)；\(k=2\) 取 \((A_1,B_1)\)。这里若 \(n=0\)，下标 1 的 A、B 就取自 T。然后从 t=0 至 M-1 按 (2) 的公开结构重建：phase 0 要生成 U 字母时取下一次 UV context 的 \(A_i\)，phase 1 取其 \(B_i\)，phase 2（必为某个 \(t_i\)，\(i\le n\)）取指定标签 \(Z_i\)，phase 3 写入 0，phase 4 写入 \(c_6\)，其余 phase 写入唯一 clock 后继。最后在 phase 2 停止，不生成最终标签。

上述步骤在重叠坐标上相容，因为每一步都只追加一个合法后继符号；同一 \(Z_i\) 出现在相继 pair \((B_i,Z_i),(Z_i,0)\) 中，是同一个已追加符号的确定复制。在 \(k=3,4\) 的初始残段使用固定 \(v_*,w_*\)，而不从 D 中拿一个不存在的标签。任意 \((D,T)\) 都能如此生成唯一完整历史，因为所有 U、V 的选择以及 W 的标签都有正概率。反过来，按 (5) 提取恢复原来的 D、T；从原历史提取再重建也逐符号恢复原历史。因此是公共支持上的双射，不是扔掉其他信息的压缩近似。

将完整路径概率
\[
\mu(Y_0)\prod_{t=0}^{M-1}
       \theta^\sigma_{Y_t}(X_{t+3})
\]
逐项相乘。每个 context 的 A、B 各产生一个 \(1/m\) 因子：在 \(k=1\) 时第一个 A 因子来自 \(\mu\)，在 \(k=2\) 时第一个 A、B 两因子都来自 \(\mu\)，其他均来自 uniform 转移。它们都恰计一次。每个 \(t_i\), \(i\le n\)，贡献 \(q_\sigma(Z_i\mid A_i,B_i)\)。其余所有因子为 1。得到每个完整历史的精确概率
\[
\mathbb P_\sigma(H=G_{K,M}(D,T))
 =m^{-2(n+1)}\prod_{i=1}^n q_\sigma(Z_i\mid A_i,B_i).
                                                               \tag{6}
\]
固定的初始 \(w_*\) 不带 q 因子。\(n=0\) 时乘积为空，(6) 为 \(m^{-2}\)。

由 (6)，整个观察实验精确等价于
\[
D_1,\ldots,D_n\ \hbox{iid},\quad
P_\sigma(D_i=(u,v,z))=m^{-2}q_\sigma(z\mid u,v),\quad
T\sim\operatorname{Unif}(\mathcal U\times\mathcal V)
\ \hbox{且独立于全部 D}.                              \tag{7}
\]
特别，条件于任何 \(T=s\)，D 的律仍为该 iid 产品律，每个条件事件概率均为 \(m^{-2}>0\)。完整 H 在该条件下的律是它经同一个 \(G_{K,M}(\cdot,s)\) 双射得到的律。这里 T 就是原轨迹的 actual 末对，不是添加的测试样本；(7) 也没有对一般源或随机行访问数作条件 iid 假定。

## 5. 有限 testing 与 KL–TV 的自足工具

以下只处理有限观察空间；随机算法的种子将在测试输出概率中积分，不需要有限种子空间。记
\[
D(P\Vert Q)=\sum_xP(x)\log\frac{P(x)}{Q(x)}
\]
为自然对数 KL，取通常的零质量约定。

对于有公共严格正支持的 P、Q，有 Pinsker 界
\[
\operatorname{TV}(P,Q)\le\sqrt{D(P\Vert Q)/2}.        \tag{8}
\]
短证明：取 \(E=\{x:P(x)\ge Q(x)\}\)，令 \(a=P(E),c=Q(E)\)。正负差之和相抵给 \(\operatorname{TV}(P,Q)=a-c\)。在 E 上，\(f(x)=x\log x\) 的凸性给
\(\sum_E P\log(P/Q)\ge a\log(a/c)\)；在补集上同理，故
\[
D(P\Vert Q)\ge d(a\Vert c)
 =a\log(a/c)+(1-a)\log((1-a)/(1-c)).
\]
当 \(0<c<1\) 时，关于 a 的二阶导数为 \(1/a+1/(1-a)\ge4\)，在 \(a=c\) 处函数值和一阶导数为零，积分两次得 \(d(a\Vert c)\ge2(a-c)^2\)。边界由极限或零 TV 的情形处理，证明 (8)。这里合并不等式的凸性步骤也可直接以权重 \(Q(x)/c\) 应用 Jensen，因 \(f''(x)=1/x>0\)。

若一个随机测试在给定 x 后输出“+”的概率为 \(\varphi(x)\in[0,1]\)，则
\[
P_+(\text{输出}-)+P_-(\text{输出}+)
=1-\sum_x(P_+(x)-P_-(x))\varphi(x)
\ge1-\operatorname{TV}(P_+,P_-).                    \tag{9}
\]
最后一步由正差项至多其总和、负差项不增加总和得到。它适用于任何源独立随机种子，乃至任意共同随机概率核，而不要求测试是确定函数。

## 6. 相邻源的完整观察 KL 与两个截断分支

固定一个 bit \(\beta=(s_0,j_0)\in\mathcal I\)，比较仅翻转该 bit 的 \(\sigma,\sigma'\)。单个训练三元组律只在 context \(s_0\) 的两个标签上不同，精确 KL 为
\[
D(P_\sigma(D_1)\Vert P_{\sigma'}(D_1))
=\frac1{m^2}\left[
 \frac{1+\alpha}{m}\log\frac{1+\alpha}{1-\alpha}
+\frac{1-\alpha}{m}\log\frac{1-\alpha}{1+\alpha}\right]
=\frac{2\alpha}{m^3}\log\frac{1+\alpha}{1-\alpha}.      \tag{10}
\]
无论翻转方向如何都为同一值；其余 bit 的取值不影响该计算，奇数 m 的公共余坐标贡献为零。

在 (6) 的公共双射下，完整历史 likelihood ratio 就是 n 个标签 likelihood ratio 的乘积；末对和填充因子相同。对数相加并用 (7) 取期望，故完整观察 KL **恰为**
\[
D(P_\sigma(H)\Vert P_{\sigma'}(H))
=\frac{2n\alpha}{m^3}\log\frac{1+\alpha}{1-\alpha}.     \tag{11}
\]
条件于任何 actual \(T=s\) 时，D 的律未变，且 \(G_{K,M}(\cdot,s)\) 仍为双射，所以完整条件观察律也有同一 KL。这适用于测试 \(\sigma_{s,j}\)，即使翻转的正是所条件化的末行：T 的均匀分布本来就不依 \(\sigma\)。

对 \(0<\alpha\le1/2\)，
\[
\log\frac{1+\alpha}{1-\alpha}
=\int_0^\alpha\frac{2\,dx}{1-x^2}\le4\alpha.
\]
现在取
\[
\alpha=\min\left\{\frac12,\frac18\sqrt{\frac{m^3}{n+1}}\right\}.
                                                               \tag{12}
\]
它只依公开 K、M。若平方根分支被选中，则
\[
\frac{8n\alpha^2}{m^3}=\frac{n}{8(n+1)}\le\frac18.
\]
若选中 \(1/2\) 分支，则 \(m^3\ge16(n+1)\)，因而
\[
\frac{8n\alpha^2}{m^3}=\frac{2n}{m^3}
\le\frac{n}{8(n+1)}\le\frac18.
\]
所以 (11) 对完整观察及上述每个末行条件观察都至多 \(1/8\)，由 (8) 相邻律的 TV 至多 \(1/4\)。\(n=0\) 时完整 KL 正好为零，训练数据是唯一的空元组；上述界仍有效。由 (9)，任何共同随机测试在相邻两源上的错误概率之和至少为 \(3/4\)。

## 7. 任意随机预测器的 actual 损失和同一有限先验

固定任意共同随机全历史预测器 \(\mathsf A\)，可写为 \(\mathsf A(H,R)\)，其中 R 的律不依源且独立于路径；也可直接将输出概率核视作随机化。对于 actual \(T=s\) 和每个 \(1\le j\le b\)，由输出向量 \(\widehat p=\mathsf A(G_{K,M}(D,s),R)\) 定义测试
\[
\widehat\sigma_{s,j}=+
  \quad\Longleftrightarrow\quad
  \widehat p_{w_{2j-1}}\ge\widehat p_{w_{2j}},
\]
其余情况输出“−”。ties 统一归“+”。

真坐标差是 \(2\alpha\sigma_{s,j}/m\)。测试错误时，预测差与真差方向相反或为零，故差的距离至少 \(2\alpha/m\)。三角不等式给该坐标对的 TV 贡献
\[
\frac12\left(
 |\widehat p_{w_{2j-1}}-q_\sigma(w_{2j-1}\mid s)|
+|\widehat p_{w_{2j}}-q_\sigma(w_{2j}\mid s)|
\right)\ge\frac{\alpha}{m}
       {\bf1}\{\widehat\sigma_{s,j}\ne\sigma_{s,j}\}.   \tag{13}
\]
当真符号为“−”且预测相等时，确实是错误且等式边界允许；真符号为“+”的 tie 归为正确，不影响下界。各 j 的坐标对不交，W 外预测质量只贡献额外非负损失，因此逐路径
\[
\operatorname{TV}(\widehat p,q_\sigma(\cdot\mid s))
\ge\frac{\alpha}{m}\sum_{j=1}^b
       {\bf1}\{\widehat\sigma_{s,j}\ne\sigma_{s,j}\}.   \tag{14}
\]

对固定 s、j，把算法随机性积分掉，所得
\(\varphi_{s,j}(D)=\mathbb P_R(\widehat\sigma_{s,j}=+)\)
是 D 的同一个 [0,1] 值函数，不依隐藏 \(\sigma\)。这是因为重建映射及算法都共同。对仅翻转 \((s,j)\) 的相邻符号向量，§6 与 (9) 可用于这个函数，故条件于 \(T=s\) 的两项错误率之和至少 \(3/4\)。

现令 \(\sigma\) 在整个有限超立方体 \(\{-1,+1\}^{m^2b}\) 上均匀平均，记平均为 \(\operatorname{Av}_\sigma\)。固定 s,j 及所有其他 bit，将两个可能值配成一对，上一步说明
\[
\operatorname{Av}_\sigma
 \mathbb P_{\sigma,\mathsf A}
  (\widehat\sigma_{s,j}\ne\sigma_{s,j}\mid T=s)\ge\frac38.
                                                               \tag{15}
\]
具体是 \(2^{m^2b-1}\) 个配对，每个和至少 \(3/4\)，再除以 \(2^{m^2b}\)。这一步对所有 s,j 用的是同一个有限先验。

在每一个源上真正 actual 行的权重为
\(\mathbb P_\sigma(T=s)=m^{-2}\)。把 (14) 取期望，用 (15) 得
\[
\begin{aligned}
\operatorname{Av}_\sigma
 \mathbb E_{\sigma,\mathsf A}
   \operatorname{TV}(\mathsf A(H),\theta^\sigma_{Y_M})
&\ge\frac{\alpha}{m}\frac1{m^2}
   \sum_{s\in\mathcal U\times\mathcal V}\sum_{j=1}^b\frac38\\
&=\frac{3\alpha b}{8m}\ge\frac{\alpha}{8}.
\end{aligned}                                                     \tag{16}
\]
最后一步由 \(b/m\ge1/3\) 对 \(m\ge3\) 成立：偶数 m 时为 \(1/2\)，奇数时 \((m-1)/(2m)\ge1/3\)，包含 m=3 的端点。

所有源都属于原允许类，且在此比较中采用相同、\(\sigma\) 无关的 \(\mu_{K,M}\)。对同一个 \(\mathsf A\)，全源 supremum 至少是这个有限族的最大风险，最大值至少平均值。因此 (16) 证明每个算法都有一个源达到至少 \(\alpha/8\)，随后取所有算法 infimum 得
\[
R_{\min}(K,M)\ge\frac{\alpha}{8}
=\min\left\{\frac1{16},\frac1{64}\sqrt{\frac{m^3}{n+1}}\right\}
\ge\frac1{64}\min\left\{1,\sqrt{\frac{m^3}{n+1}}\right\},
\quad K\ge12.                                      \tag{17}
\]
没有把不同源风险直接相加当作单个源的风险，也没有交换 infimum 和 supremum。这里未知源可依算法选择；不声称一个固定 \(\sigma\) 同时使所有算法失败。

## 8. 全部有限 K,M 的常数比较及唯一前驱接口

先处理 \(K\ge12\)。令
\[
z=\sqrt{\frac{K^5}{M+1}},\qquad t=\sqrt{\frac{m^3}{n+1}}.
\]
若 \(n=0\)，则 \(t=m^{3/2}>1\)，(17) 给 \(R_{\min}\ge1/64\)，直接大于所需 \(2^{-16}\min\{1,z\}\)。没有借大样本渐近式覆盖此情形。

若 \(n\ge1\)，则
\[
n+1\le2n\le\frac{2M}{m^2}.
\]
又 \(m=\lfloor K/4\rfloor\ge K/8\)：取 \(x=K/4\ge3\)，\(\lfloor x\rfloor\ge x-1\ge x/2\)。所以
\[
t^2=\frac{m^3}{n+1}
\ge\frac{m^5}{2M}
\ge\frac{K^5}{2\cdot8^5(M+1)}
=\frac{z^2}{256^2}.                                 \tag{18}
\]
由单调性及分 z≤1、z≥1 两种情况，
\(\min\{1,t\}\ge256^{-1}\min\{1,z\}\)。故 (17) 给出高 K 情形的保守余量
\[
R_{\min}(K,M)\ge2^{-14}\min\{1,z\}
\ge2^{-16}\min\{1,z\}.                              \tag{19}
\]
n=0 时同样满足 (19)。本文按冻结目标提交常数 \(2^{-16}\)，不把这点数值余量另拆义务。

对 \(2\le K\le11\)，**此处且仅此处**使用 G/U 中已接纳的以下准确接口：对任意 \(N\ge3,K\ge2\) 和任意共同随机全历史概率预测器，存在一个合法 iid 源及其 iid 初始对律，使同轨迹 actual TV 期望至少 \(1/(16\sqrt N)\)。它可用所有行相同的两个 Bernoulli 参数构成，K>2 时其他字母零质量；接口不要求预测器满足程序 I。令 \(N=M+2\)，每算法全源 supremum 至少此数，于是
\[
R_{\min}(K,M)\ge\frac1{16\sqrt{M+2}}.                \tag{20}
\]


因为 \(M+2\le4(M+1)\)、\(K^5\le11^5=161051<2^{18}\)，
\[
\frac1{16\sqrt{M+2}}\ge\frac1{32\sqrt{M+1}},
\]
而
\[
2^{-16}\min\{1,z\}
\le\frac{2^{-16}K^{5/2}}{\sqrt{M+1}}
<\frac1{128\sqrt{M+1}}.
\]
所以 (20) 蕴含所需下界，包括全部小 M 和饱和区域。结合 (19)，(MM5) 对所有 \(K\ge2,M\ge1\) 成立。

## 9. 样本必要性、适用范围和来源边界

令某个共同算法在固定 K,M 的整个源类上满足统一 actual 均值风险至多 \(\tau\)，其中 \(0<\tau<2^{-16}\)。其最坏风险不小于 \(R_{\min}(K,M)\)，故
\[
\tau\ge2^{-16}\min\{1,z\}.
\]
因为 \(\tau<2^{-16}\)，必须有 \(z<1\)，继而
\[
M+1\ge 2^{-32}K^5/\tau^2.                           \tag{21}
\]
这仅是统计样本数必要条件，不是内部 bits、深度、宽度、算术工作或整程序费用的下界。实际 Pi 和 strong direct 若作为共同全历史算法的子类，当然也受此统计必要性约束；这不需要 SRC，也不增加任何具体实现或资源结论。

本文在每个 horizon 使用与其余数对应的合法 \(\mu_{K,M}\)。这正是原每 horizon supremum 允许的初始化选择，没有宣称同一初始律对全部 M 同时实现下界。每条轨迹的 \(\theta^\sigma\) 始终齐次，未知符号固定。W 内正概率、组外零边、剩余字母不可达、周期类和六类初始化均在原域内。一般源不具有 (7) 的末对独立性，本文仅从这个合法子族的路径律中证明并使用它。

