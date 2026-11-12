# Candidate theorem: source-average mean-field approximation with evolving keys and values

12 November 2026. Self-contained research draft, not peer-reviewed or formally verified. This result is a logarithmic-depth obstruction, not a sharp architecture/resource frontier.

## 1. Source, target, and architectural contract

Fix c in (0,1/2), a=1-2c, and theta in [-a,a]. Generate X_1,X_2 as independent fair signs and, for t>=1,

    P_theta(X_{t+2}=z | X_t=x,X_{t+1}=y)=(1+theta xyz)/2.

Every transition lies in [c,1-c]. The stationary pair law is uniform: summing the transition over its first sign gives one, so uniform pairs are preserved. The next-symbol plus probability after N>=2 observations is

    p_theta(X)= (1+theta X_{N-1}X_N)/2.

Risk throughout means expected absolute probability error, R_theta(Q)=E_theta|Q-p_theta|. It is not classification error, squared loss, or log loss.

Parameters, positional information and initial embeddings may depend on N but not on theta or the observed word. Each raw row starts from h_i^0(X_i), a function only of its own sign and public information. There are D blocks. Each attention block uses the entire self-inclusive prefix j<=i, with no selected, local, parity, or data-dependent hard mask. Keys, queries and values are recomputed from the evolving row states. The displayed theorem is single-head; multiple heads are covered by summing their projection-weighted stability and forcing constants.

At layer ell, on a declared common radius-H state ball:

* scores s_ij are in [-S_ell,S_ell]; values have norm at most V_ell;
* |s_ij(x)-s_ij(y)| <= Ls_ell(d_i+d_j), where d_j=||x_j-y_j||;
* ||v_j(x)-v_j(y)|| <= Lv_ell d_j;
* attention output projection has operator norm at most Lo_ell;
* the subsequent row-local map F_ell, applied after the attention residual, is (1+Lf_ell)-Lipschitz on the reached domain.

Thus a block is h_i'=F_ell(h_i+O_ell A_i(h)). Its true outputs stay in the H ball. The scalar final probability map is Lout-Lipschitz on the common H ball, including reference states, not merely on actual trajectories. All constants include the actual normalization maps, including positive LayerNorm epsilon, scale and shift; declaring only matrix norms is insufficient. Scores can include arbitrary public positional pair biases consistent with the bounds. The same bounds must hold on the reference-state ball, not just the realized network trajectories. The FFN domain must include residuals with any convex average of admissible values. State projections mentioned below are proof devices fixing true states, not extra real-network capabilities.

The three readout contracts are:

(A) append row n=N+1 initialized publicly and read its output;
(B) use N raw rows and read h_N;
(C) append a row initialized with the actual pair T=(X_{N-1},X_N), supplied for free, and read it. For (C), the common envelope must cover all four artificially fixed pair tags on all histories, or projected artificial executions must agree with every consistent real execution.

The model cannot insert theta directly into parameters or tag. Its computations must be the same function across the source family. H need not be N-independent if all the stated derived bounds remain uniform, but any depth/resource dependence of S,V,Ls,Lv,Lo,Lf,Lout must be retained.

## 2. Explicit conclusion

Let kappa_c=sqrt(4+8/c^2), E_0=0, and define, layer by layer,

    a_ell=(1+Lf_ell)(1+2 Lo_ell V_ell exp(2S_ell)Ls_ell),
    b_ell=(1+Lf_ell)Lo_ell exp(2S_ell)(Lv_ell+2V_ell Ls_ell),
    u_ell=2(1+Lf_ell)Lo_ell kappa_c exp(2S_ell)(1+V_ell^2),
    E_{ell+1}=(a_ell+2b_ell)E_ell+u_ell.

Pointwise-only layers have their actual local Lipschitz a_ell and b_ell=u_ell=0. Equivalently,

    E_D=sum_{ell=0}^{D-1} u_ell product_{r=ell+1}^{D-1}(a_r+2b_r).

There exist public, theta-independent templates q_N in (A), q_N(s) in (B), and q_N(tau) in (C), such that

    (A) E_theta|Q-q_N| <= delta_A=Lout E_D/sqrt(N+1),
    (B) E_theta|Q-q_N(X_N)| <= delta_B=Lout E_D/sqrt(N),
    (C) E_theta|Q-q_N(T)| <= 4 delta_A.

Consequently, uniformly over admissible theta,

    (A),(B): R_theta(Q) >= |theta|/2-delta_A or delta_B, respectively.

For (C), for each fixed h in (0,a],

    max(R_0(Q),R_h(Q)) >= h/4-4 delta_A.

In particular, if a_ell+2b_ell<=B>1 and u_ell<=U, then E_D<=U(B^D-1)/(B-1). With fixed c,B,U,Lout, fix h in (0,a]. Under (A) or (B), requiring R_h<=h/4 forces E_D>=h sqrt(n)/(4 Lout), where n=N+1 or N respectively. Under (C), requiring max(R_0,R_h)<=h/8 forces E_D>=h sqrt(N+1)/(32 Lout). Thus either specified requirement forces D >= (log N)/(2 log B)-O(1). A uniform risk requirement over the full source class implies these requirements when its threshold is small enough. No such lower bound follows from risk at theta=0 alone. This is not a statement that logarithmic depth suffices, nor a vanishing-risk lower bound above that depth. If B=1 use E_D<=UD; if B<1 use E_D<=U/(1-B). A zero Lout makes the approximation trivial and precludes nonconstant outputs.

## 3. Proof: concentration of token-local functions

Write Y_t=(X_t,X_{t+1}). For any two pairs, its two-step transition probability is at least c^2. With pi uniform on four pairs, K^2>=4c^2 pi. Let rho=1-4c^2. Doeblin decomposition contracts total variation by rho each two steps. Thus bounded, centered token-local vectors g_i(X_i), obtained from functions f_i of norm<=R by subtracting their expectations, satisfy

    |E <g_i(X_i),g_j(X_j)>| <= 4R^2 rho^{floor((j-i-1)/2)}, j>i.

To see this for vector functions, condition on the pair at i, apply the total-variation bound to the future conditional mean of f_j, and use ||g_i||<=2R. The one-step offset is deliberately conservative. This proof does not require a dimension factor. Also E||g_i||^2<=4R^2. Since sum_{h>=1}rho^{floor((h-1)/2)}=2/(1-rho)=1/(2c^2), summing diagonal and both off-diagonal terms gives at most (4+4/c^2)R^2 i; in particular

    E || i^{-1} sum_{j<=i}g_j(X_j) ||^2 <= kappa_c^2 R^2/i.       (1)

A deterministic sentinel contribution has zero fluctuation. Each raw marginal is fair, so E f_j(X_j)=(f_j(+)+f_j(-))/2, independently of theta. The f_j may vary arbitrarily with position. No conditional independence given the terminal state or count is asserted.

## 4. Proof: deterministic reference construction

Maintain two reference branches bar_h_i^ell(+),bar_h_i^ell(-) at each raw row, and one at a publicly initialized sentinel. Initialize with the actual embedding. For fixed receiving row i and fixed branch r, form reference scores and values and average the vectors

    f_ij^r(s)=(exp(s_ij^r(s))v_j(s), exp(s_ij^r(s)))

over both equally weighted source tags s. Include any sentinel as a single deterministic contribution. Divide the averaged numerator by averaged denominator, perform the actual residual and local map, and project the resulting reference state onto the H ball. The references are theta-independent by induction. The projection is nonexpansive and fixes the corresponding true next state.

This construction is a ratio of expected sketches, NOT the expected ratio. For each fixed query tag, (1) applies with R=exp(S)sqrt(1+V^2). The actual query tag can equal X_i and hence be dependent on its prefix. The valid bound is

    E||error_{X_i}|| <= E||error_+||+E||error_-||
                     <=2 kappa_c R/sqrt(i).                 (2)

It does not condition the source on the query tag. The sentinel needs only one branch; retaining two is conservative. In particular, the self row causes no independence gap.

For normalized sketches (n,d),(n',d') with d,d'>=exp(-S) and ||n'/d'||<=V,

    ||n/d-n'/d'|| <= exp(S)(||n-n'||+V|d-d'|)
                   <=exp(S)sqrt(1+V^2)||(n,d)-(n',d')||.

Combining this with (2) bounds the reference-bank empirical attention minus deterministic reference attention by

    2 kappa_c exp(2S)(1+V^2)/sqrt(i).                       (3)

## 5. Proof: actual evolving-bank stability

Compare two banks with row differences d_j. Every softmax weight is at most exp(2S)/i. Interpolating their score vectors, the derivative identity for softmax weighted averages bounds score-induced output change by 2V times the weighted absolute score change. Interpolated scores remain in [-S,S]. Separately changing values therefore gives

    ||A_i(x)-A_i(y)||
      <=2V exp(2S)Ls d_i
        +exp(2S)(Lv+2V Ls) i^{-1}sum_{j<=i}d_j.            (4)

This argument interpolates score vectors, so it does not require differentiability of scores or FFNs. It fully charges changes to receiving queries and source keys/values.

Compare the actual bank with reference states at the same realized signs, then apply (3). After the residual, output projection, local map and reference projection, e_i^ell=E||h_i^ell-bar_h_i^ell(X_i)|| satisfies

    e_i^{ell+1}<=a_ell e_i^ell+b_ell i^{-1}sum_{j<=i}e_j^ell+u_ell/sqrt(i).

Since e_i^0=0 and i^{-1}sum_{j<=i}j^{-1/2}<=2/sqrt(i), induction yields e_i^ell<=E_ell/sqrt(i). The actual states need not be token-local: only the auxiliary references are. Reading row n and applying Lout proves (A) and (B).

## 6. Proof: risk and terminal disclosure

Under (A), X_{N-1}X_N is a fair sign, so for every fixed real q,

    E_theta|q-p_theta| >= |theta|/2.

Under (B), conditional on X_N, X_{N-1} remains fair because the stationary pair is uniform. The same inequality holds for any two-valued template q(X_N). Triangle inequality and the approximation bounds give the two risk claims.

For (C), fix an artificial terminal tag tau and run the architecture on an unconditional source word with that fixed tag. The source concentration proof is unchanged; its public template q(tau) has unconditional approximation error <=delta_A. There are four tags. On the event T=tau, this artificial execution agrees with the real one. As P_theta(T=tau)=1/4,

    E_theta[|Q-q(tau)| | T=tau] <=4delta_A.

Averaging the conditional bound gives overall error <=4delta_A. Compare theta=0 and theta=h. For any tag tau, their target probabilities differ by h/2, while their template q(tau) is the same. Triangle inequality, then uniform averaging over tau, gives template risks with sum at least h/2. Subtracting both approximation errors gives R_0+R_h>=h/2-8delta_A, proving (C). No assumption of independence between endpoint and history is used.

## 7. Robust noise scope

**Exogenous randomized computation.** All conclusions remain valid if an arbitrary common random seed Z is independent of the source and theta, and conditional on Z every initial state and layer satisfies the above contract with the same constants and the identical theta-independent computational rule across the source family. This includes source-independent randomized weights, public or private random bits, and bounded additive noises already absorbed in the uniform layer/domain contract. Condition on the entire seed, apply the proof, and average. The reference may depend on Z; this is a coupling/proof device, not a claim that private randomness is publicly communicated. The risk arguments hold for each seed. In (C), pair probabilities remain 1/4 conditional on Z. Arbitrary noise correlations across rows/layers are allowed in this conditional-contract formulation.

**Perturbations with an explicit error budget.** More generally, if a comparison incurs an additional expected row error nu_i^ell>=0 after layer ell, replace the recurrence by the vector inequality

    e^{ell+1} <= (a_ell I+b_ell P)e^ell +u_ell w+nu^ell,
    P_ij=1{j<=i}/i, w_i=i^{-1/2}.

The final row error is bounded by the corresponding product expansion. In particular, if nu_i^ell<=v_ell/sqrt(i), replace u_ell by u_ell+v_ell. If nu_i^ell<=v_ell uniformly, there is an additional uniform error T_D, with T_0=0 and T_{ell+1}=(a_ell+b_ell)T_ell+v_ell. Multiply it by Lout in the final risk error; terminal disclosure pays the same factor four. An initial error is propagated by the same positive matrices. This bounded-perturbation statement does not require noise independence, but it must be established by an actual coupling to an admissible theta-independent reference model. It is not permission to hide arbitrary parameter-dependent information in noise.

**Not covered automatically.** Unbounded Gaussian noise has no pathwise H/S envelope; truncation or a separate tail/domain argument is needed. Data-dependent/adversarial noise is not exogenous and requires the explicit comparison budget. Noise that reveals theta or supplies new nonlocal observations invalidates the architecture contract unless that information is charged. Neither an exact-state information contraction nor a noise-robust finite-bit communication theorem follows from this approximation result.

## 8. Attribution, novelty, and limitations

The stationary source and independent triple innovations are known: Loic Turban, *One-dimensional Ising model with multispin interactions*, J. Phys. A 49, 355002 (2016), section 2, zero-field free-boundary m=3 model with theta=tanh K; https://arxiv.org/html/1605.05199v2 ; DOI 10.1088/1751-8113/49/35/355002.

Doeblin covariance bounds, bounded-score attention sensitivity, deterministic mean-field references and Lipschitz propagation are established methods. Hahn (2020), *Theoretical Limitations of Self-Attention in Neural Sequence Models*, provides relevant prior bounded-attention sensitivity context; https://aclanthology.org/2020.tacl-1.11/ . Exact correspondence of this source-uniform evolving-bank template theorem to prior literature has not been certified. No novelty claim is made here. The earlier parity chi-square/communication lemmas are not used in this proof; their generic weight-enumerator and rate-distortion identities have separate established precedents.

The theorem includes evolving K/V, all-row updates, arbitrary public positions within the envelope, raw-last-row readout and free terminal-pair disclosure. It excludes hard subprefix masks and uncharged global initial features. It yields only a constant-risk/logarithmic-depth barrier under uniform gain bounds. A depth-independent aggregate full-network Frobenius budget is not equivalent to the displayed per-layer budgets and must be checked separately. The finite CPU diagnostic uses untrained models and is not proof, optimization evidence, or superiority evidence.
