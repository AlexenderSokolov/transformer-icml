# S002 平稳二阶 shift minimax 下界

科学正文摘录。以下保留已接纳版本的数学文字与原有编号，不重写证明；仅省略提交身份、流程元数据和历史状态。来源与依赖见 `../SOURCES.md`，逐字节映射见 `../COPY_MAP.json`。本次编排不是新的独立数学审查。

## 0. Accurate result and scope

For integers \(K\ge2\), \(M\ge1\), observe the complete symbol history
\(H=(X_1,\ldots,X_{M+2})\) from an unknown, time-homogeneous order-two source
\(\theta_{ab}(c)\), started from a stationary pair law. Put
\(Y_i=(X_{i+1},X_{i+2})\), \(0\le i\le M\).
An estimator \(A=A(H,U)\in\Delta_K\) may use all of \(H\), the public \(K,M\), and an independent random seed \(U\), but not the hidden source. Its loss is the **actual endpoint** loss
\[
\operatorname{TV}(A(H,U),\theta_{Y_M})
=\frac12\sum_c|A_c(H,U)-\theta_{Y_M}(c)|.
\]

Let \(\mathcal S_K\) be the full stationary-initialization class in the frozen contract, including reducible and periodic sources and sources with zero transition probabilities. Then
\[
\boxed{\quad
\inf_A\sup_{(\theta,\pi)\in\mathcal S_K}
\mathbb E_{\theta,\pi}\operatorname{TV}(A,\theta_{Y_M})
\ \ge\ \frac1{180}\min\left\{1,\sqrt{\frac{K^3}{M+1}}\right\}.
\quad} \tag{S002.1}
\]

In fact the same lower bound holds on a subclass with known uniform pair law
\(\pi(a,b)=K^{-2}\), all symbol-transition probabilities in
\([0.9/K,1.1/K]\), and the uniform two-step minorization
\(P_\theta^2(s,t)\ge0.81\pi(t)\).
The estimator can even be told these subclass properties. Thus the lower bound is not a slow-mixing or nonstationary-phase phenomenon.

This is only the lower side of the stationary-rate question. It does not assert an upper bound, add-one optimality, or that fast mixing is necessary.

## 1. A legal stationary hypercube of sources

Write \(r=\lfloor K/2\rfloor\). Pair the first \(2r\) symbols into
\(B_i=\{2i,2i+1\}\), \(0\le i<r\), and define
\(\varepsilon(2i)=+1\), \(\varepsilon(2i+1)=-1\).
If \(K\) is odd, the symbol \(K-1\) is unpaired.
For each \(b\in\{0,\ldots,K-1\}\), \(0\le i,j<r\), choose a sign
\(\sigma_{bij}\in\{-1,+1\}\). The total number of signs is \(d=Kr^2\).

For \(0<\alpha\le1/2\), define
\[
\theta^\sigma_{ab}(c)=
\begin{cases}
 K^{-1}\bigl(1+\alpha\sigma_{bij}\varepsilon(a)\varepsilon(c)\bigr),
 &a\in B_i,\ c\in B_j,\\
 K^{-1},&a\text{ or }c\text{ is unpaired}.
\end{cases} \tag{S002.2}
\]
All entries belong to \([(1-\alpha)/K,(1+\alpha)/K]\).
For every fixed \(a,b\), the perturbations cancel within each column pair \(B_j\), so
\(\sum_c\theta^\sigma_{ab}(c)=1\).
For every fixed \(b,c\), they cancel within each row pair \(B_i\), so
\(\sum_a\theta^\sigma_{ab}(c)=1\).
These assertions include unpaired symbols, whose entries are unperturbed.

The legal pair-shift transition matrix is
\[
P_\sigma((a,b),(b,c))=\theta^\sigma_{ab}(c),
\]
and all non-shift transitions are zero. The uniform pair law is stationary because
\[
\sum_a\frac1{K^2}P_\sigma((a,b),(b,c))
=\frac1{K^2}\sum_a\theta^\sigma_{ab}(c)=\frac1{K^2}. \tag{S002.3}
\]
We always initialize \(Y_0\sim\pi\), with this exact stationary law; there is no horizon-dependent phase choice. In particular \(Y_M\sim\pi\) for every sign vector and every \(M\).

## 2. Full history conditional on the actual endpoint

The stationary reverse transition is
\[
Q_\sigma((b,c),(a,b))
=\frac{\pi(a,b)P_\sigma((a,b),(b,c))}{\pi(b,c)}
=\theta^\sigma_{ab}(c), \tag{S002.4}
\]
with zero probability on other reverse transitions. Column stochasticity from Section 1 makes every \(Q_\sigma\) row a probability distribution.

Fix an arbitrary actual endpoint \(s\in\{0,\ldots,K-1\}^2\), and let
\(\mathsf P^s_\sigma\) denote the conditional law of the **entire** observed symbol history given \(Y_M=s\).
The pair path \(Y_0,\ldots,Y_M\) and the symbol history \(H\) determine each other exactly. For every legal such path ending at \(s\),
\[
\mathsf P^s_\sigma(Y_0=y_0,\ldots,Y_M=s)
=\frac{K^{-2}\prod_{i=0}^{M-1}P_\sigma(y_i,y_{i+1})}{K^{-2}}
=\prod_{i=0}^{M-1}Q_\sigma(y_{i+1},y_i). \tag{S002.5}
\]
Thus \(Z_t=Y_{M-t}\), \(0\le t\le M\), under this conditional law is exactly the reverse Markov chain started deterministically at \(Z_0=s\). In particular, (S002.5) retains the observed initial pair and every intervening symbol; it does not remove side information, replace the endpoint by an independent query, or assume an independence relation between visits and endpoint.

For any reverse starting pair \(s=(u,v)\) and destination \(t=(a,b)\), there is a unique two-step reverse path through \((b,u)\). Therefore
\[
Q_\sigma^2((u,v),(a,b))
=\theta^\sigma_{bu}(v)\theta^\sigma_{ab}(u)
\le\frac{(1+\alpha)^2}{K^2}. \tag{S002.6}
\]
Consequently, for every starting state \(s\), every \(t\ge2\), and every pair \(z\),
\[
\Pr^s_\sigma(Z_t=z)
=\sum_x\Pr^s_\sigma(Z_{t-2}=x)Q_\sigma^2(x,z)
\le\frac{(1+\alpha)^2}{K^2}. \tag{S002.7}
\]

## 3. Conditional full-history information for a single bit flip

Fix a sign coordinate \(\ell=(b,i,j)\), and write \(\sigma^{\ell}\) for its flip. Put
\(a_0=2i,a_1=2i+1,c_0=2j,c_1=2j+1\).
In the reverse kernel the two sources differ **only** in the two rows
\[
D_\ell=\{(b,c_0),(b,c_1)\}. \tag{S002.8}
\]
Within either changed reverse row, only the two outgoing coordinates \(a_0,a_1\) change, exchanging probabilities \((1+\alpha)/K\) and \((1-\alpha)/K\). Hence the row relative entropy, using natural logarithms, is exactly
\[
\begin{aligned}
D\bigl(Q_\sigma(z,\cdot)\Vert Q_{\sigma^\ell}(z,\cdot)\bigr)
&=\frac{2\alpha}{K}\log\frac{1+\alpha}{1-\alpha}\\
&\le\frac{8\alpha^2}{K},\qquad z\in D_\ell. \tag{S002.9}
\end{aligned}
\]
For the inequality, integrate \(1/x\) on \([1-\alpha,1+\alpha]\) to obtain
\(\log((1+\alpha)/(1-\alpha))\le2\alpha/(1-\alpha)\le4\alpha\).
All unchanged rows have relative entropy zero.

For the \(M\) reverse transitions the departure times are \(t=0,\ldots,M-1\). Bounding the first two times by \(1\) each and applying (S002.7) thereafter gives, uniformly in \(s,\sigma,\ell\),
\[
\begin{aligned}
\mathbb E^s_\sigma\sum_{t=0}^{M-1}{\bf1}\{Z_t\in D_\ell\}
&\le \min(M,2)+(M-2)_+\frac{2(1+\alpha)^2}{K^2}\\
&\le 2+\frac{9M}{2K^2}. \tag{S002.10}
\end{aligned}
\]
This deliberately loose bound is also valid when \(M=1\) or \(M=2\).

The finite-path relative-entropy chain rule, directly obtained by expanding the logarithm of the product in (S002.5), now yields
\[
\begin{aligned}
D(\mathsf P^s_\sigma\Vert\mathsf P^s_{\sigma^\ell})
&=\sum_{t=0}^{M-1}\mathbb E^s_\sigma
D\bigl(Q_\sigma(Z_t,\cdot)\Vert Q_{\sigma^\ell}(Z_t,\cdot)\bigr)\\
&\le \frac{16\alpha^2}{K}+\frac{36\alpha^2M}{K^3}. \tag{S002.11}
\end{aligned}
\]
All legal reverse paths have positive probability under both sources, so no support issue enters this identity. Illegal pair paths have probability zero under both and are excluded from the common finite support.

Choose
\[
\beta=\min\left\{1,\sqrt{\frac{K^3}{M+1}}\right\},
\qquad \alpha=\frac{\beta}{10}. \tag{S002.12}
\]
Then \(\alpha\le1/10\), \(\alpha^2\le1/100\), and
\[
\frac{\alpha^2M}{K^3}
=\frac1{100}\min\left\{1,\frac{K^3}{M+1}\right\}\frac{M}{K^3}
\le\frac1{100}. \tag{S002.13}
\]
Using \(K\ge2\) in (S002.11) shows
\[
D(\mathsf P^s_\sigma\Vert\mathsf P^s_{\sigma^\ell})
\le\frac{44}{100}<\frac12.
\]
Pinsker's inequality therefore implies the **endpoint-uniform, complete-history** bound
\[
\operatorname{TV}(\mathsf P^s_\sigma,\mathsf P^s_{\sigma^\ell})
\le\sqrt{\frac{22}{100}}<\frac12. \tag{S002.14}
\]
An elementary proof of the version of Pinsker used here is given in Section 7.

## 4. Loss controls bit errors at the random target row

Fix an endpoint \(s=(a,b)\) with paired first coordinate \(a\in B_i\). For each \(j<r\), define a decoded sign from the estimator output by
\[
\widehat\sigma_{s,j}(H,U)=
\begin{cases}
+1,&\varepsilon(a)\bigl(A_{2j}(H,U)-A_{2j+1}(H,U)\bigr)\ge0,\\
-1,&\varepsilon(a)\bigl(A_{2j}(H,U)-A_{2j+1}(H,U)\bigr)<0.
\end{cases} \tag{S002.15}
\]
The tie rule is explicit and is independent of the hidden sign.
The true signed difference of the two target coordinates is
\[
\varepsilon(a)\bigl(\theta^\sigma_{ab}(2j)-\theta^\sigma_{ab}(2j+1)\bigr)
=\frac{2\alpha}{K}\sigma_{bij}. \tag{S002.16}
\]
If the decoded sign is incorrect, (S002.15)--(S002.16), including the possible tie, give
\[
\begin{aligned}
|A_{2j}-\theta^\sigma_{ab}(2j)|
+|A_{2j+1}-\theta^\sigma_{ab}(2j+1)|
&\ge\left|(A_{2j}-A_{2j+1})
 -(\theta^\sigma_{ab}(2j)-\theta^\sigma_{ab}(2j+1))\right|\\
&\ge\frac{2\alpha}{K}. \tag{S002.17}
\end{aligned}
\]
The coordinate pairs are disjoint. Hence, pointwise on every complete history and every seed having endpoint \(s\),
\[
\operatorname{TV}(A,\theta^\sigma_s)
\ge\frac\alpha K\sum_{j=0}^{r-1}
{\bf1}\{\widehat\sigma_{s,j}\ne\sigma_{bij}\}. \tag{S002.18}
\]
No inequality is needed for endpoints whose first symbol is unpaired; their nonnegative loss will simply be discarded.

## 5. Conditional testing and averaging

Place the uniform prior on all \(2^d\) sign vectors. Because every source has the same uniform terminal law, for each fixed endpoint \(s\) the prior conditional on \(Y_M=s\) is still uniform. In particular, conditioning on the actual terminal row does not reveal a sign through its marginal probability.

Fix a paired endpoint \(s=(a,b)\), write \(a\in B_i\), and fix \(j<r\). Pair every vector \(\sigma\) with its flip \(\sigma^\ell\), \(\ell=(b,i,j)\). Under these two conditional experiments, the true target bit has opposite signs and (S002.14) applies.
For any randomized binary test between probability laws \(P,Q\), the sum of its two error probabilities is at least \(1-\operatorname{TV}(P,Q)\). Indeed, if \(\varphi(h)\in[0,1]\) is the conditional probability of deciding the first hypothesis, that sum equals
\(1-\int\varphi\,d(P-Q)\ge1-\operatorname{TV}(P,Q)\).
The estimator's independent seed is incorporated into \(\varphi\); it need not be omitted or discretized.

Thus, for each paired sign-vector pair, the sum of conditional decoding errors is at least \(1/2\). Averaging those pairs gives
\[
2^{-d}\sum_\sigma
\Pr^s_\sigma\{\widehat\sigma_{s,j}\ne\sigma_{bij}\}
\ge\frac14. \tag{S002.19}
\]
This inequality is conditional on **the same actual endpoint** that indexes the loss; it is not an unconditional testing bound substituted for a random query.

For every estimator \(A\), its average risk over the hypercube, retaining the source-specific full-history experiment, therefore satisfies
\[
\begin{aligned}
2^{-d}\sum_\sigma
\mathbb E_{\theta^\sigma,\pi}\operatorname{TV}(A,\theta^\sigma_{Y_M})
&=\frac1{K^2}\sum_s2^{-d}\sum_\sigma
\mathbb E^s_\sigma\operatorname{TV}(A,\theta^\sigma_s)\\
&\ge\frac1{K^2}\sum_{\substack{s=(a,b)\\ a\ \mathrm{paired}}}
\frac\alpha K\sum_{j=0}^{r-1}\frac14\\
&=\frac{\alpha r^2}{2K^2}. \tag{S002.20}
\end{aligned}
\]
There are exactly \(2rK\) retained endpoints. For all \(K\ge2\),
\(r/K\ge1/3\): for even \(K\) the ratio is \(1/2\), and for odd \(K\ge3\),
\((K-1)/(2K)\ge1/3\). Combining this fact with (S002.12) and (S002.20) proves
\[
2^{-d}\sum_\sigma
\mathbb E_{\theta^\sigma,\pi}\operatorname{TV}(A,\theta^\sigma_{Y_M})
\ge\frac\alpha{18}=\frac\beta{180}. \tag{S002.21}
\]

The supremum over the stationary class is at least the average over this finite subclass for every fixed \(A\). The subclass itself does not depend on \(A\), and the argument covers every randomized estimator allowed by the contract. Taking the infimum over \(A\) establishes (S002.1).

## 6. Boundary audit and a limited mixing corollary

1. **Exact order-two shift:** only \((a,b)\to(b,c)\) transitions are used. Structural zeros of the pair matrix remain present.
2. **True stationarity:** every source is initialized with its exact uniform stationary pair law. The same law works for every sign and every horizon.
3. **All visible information:** (S002.5) is the probability of the full observed history, including the initial pair; no hidden earlier sample or removed observation is assumed.
4. **Endpoint/visit correlation:** it is handled by conditioning and reversing the stationary chain. No forward visit count is declared independent of the endpoint.
5. **Zero counts:** the proof does not condition on, divide by, or require positive empirical counts. It covers histories with an unvisited target row.
6. **Odd \(K\):** the leftover first-coordinate rows and output coordinates are unperturbed, and only their nonnegative loss is discarded. The ratio \(r/K\ge1/3\) covers the worst case \(K=3\).
7. **Small \(K,M\):** \(K=2\), \(M=1\), and \(M=2\) are covered by the displayed estimates. The two-step bound is used only at times at least two.
8. **The larger stationary class:** it permits zero edges, reducibility and periodicity. A positive irreducible subclass is sufficient for its minimax lower bound; no such extra assumption is imposed on the class whose risk is bounded below.
9. **Horizon dependence:** the amplitude \(\alpha\) may depend on the known \(K,M\), as permitted by the minimax supremum; a selected source stays fixed throughout its trajectory.
10. **Randomization:** the same independent randomization kernel operates under the two hypotheses. The randomized testing inequality explicitly preserves it.
11. **No minimax inference from a single easy source:** the lower bound averages over \(2^{Kr^2}\) unknown sources, not over sampling noise from a known uniform source.

For the stated limited mixing corollary, the unique forward two-step route from \((a,b)\) to \((c,d)\) goes through \((b,c)\), so
\[
P_\sigma^2((a,b),(c,d))
=\theta^\sigma_{ab}(c)\theta^\sigma_{bc}(d)
\ge\frac{(1-\alpha)^2}{K^2}
\ge0.81\pi(c,d). \tag{S002.22}
\]
Thus \(P_\sigma^2=0.81\Pi+0.19R_\sigma\), where every row of \(\Pi\) is \(\pi\), \(R_\sigma\) is a stochastic matrix, and \(\pi R_\sigma=\pi\). A Markov kernel does not increase total variation: this follows by applying the variational definition of TV to functions taking values in \([0,1]\). Consequently,
\[
\operatorname{TV}(\mu P_\sigma^{2t},\pi)
\le0.19^t\operatorname{TV}(\mu,\pi),\qquad t\ge0. \tag{S002.23}
\]
The bound holds uniformly across the hypercube. It shows that a uniform constant mixing guarantee alone cannot improve the \(K^3\) minimax sample exponent within this source class. It does **not** claim a matching upper bound for a general mixing class or a necessity of any mixing assumption.

## 7. Elementary finite-space Pinsker justification

For probability vectors \(p,q\) on a common finite support with \(q>0\), set
\(B=\{x:p(x)\ge q(x)\}\), \(u=p(B)\), and \(v=q(B)\).
Then \(u-v=\operatorname{TV}(p,q)\). If TV is zero the claim is immediate. Otherwise the relevant two-set partition has \(0<v<1\).
The log-sum inequality on \(B\) and its complement gives
\[
D(p\Vert q)\ge u\log\frac uv+(1-u)\log\frac{1-u}{1-v}=d(u\Vert v).
\]
For completeness, log-sum follows by applying Jensen's inequality to the convex function \(z\mapsto z\log z\) with weights proportional to the \(q(x)\)'s on each part. For fixed \(v\), the function \(f(u)=d(u\Vert v)\) has \(f(v)=f'(v)=0\) and
\(f''(u)=1/[u(1-u)]\ge4\) on \((0,1)\).
Integrating this second-derivative lower bound twice, and extending by continuity at the endpoints, gives
\(d(u\Vert v)\ge2(u-v)^2\). Hence
\[
\operatorname{TV}(p,q)\le\sqrt{D(p\Vert q)/2},
\]
which is the inequality used in (S002.14).
