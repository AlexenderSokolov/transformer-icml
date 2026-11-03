# CTO001: clean population logloss identifies a non-adaptive rule, while robust rules have vanishing excess

3 November 2026. Candidate for separate review; not accepted or merged into the consolidated manuscript. All logarithms are natural. This is an objective/identifiability corollary of accepted statistical results, not a novelty claim or a theorem about optimization dynamics or learnability of a specified architecture. The comparator uses the real number s=M^-1/2 in unrestricted statistical maps; no exact finite-arithmetic implementation or resource bound is claimed. The comparator is guaranteed to belong to the unrestricted class, not to every restricted class containing B.

## 1. Precisely separate the training and testing experiments

Fix an integer M>=64. Draw four independent parameters p_u=theta_u(1) uniformly on (0,1), u in {00,01,10,11}. Independently draw (X_0,X_1) uniformly on the four pairs. Conditional on these quantities generate the homogeneous binary order-two path X_0,...,X_(M+2). The observed training word is W=(X_0,...,X_(M+1)); the single prediction label is V=X_(M+2). Thus W contains exactly M departures, indexed i=0,...,M-1; its terminal pair is U=(X_M,X_(M+1)). Define H_(u,c)(w) by these M departures and J_u=H_(u,0)+H_(u,1). The label is not counted in H.

A prediction map F assigns a probability F(w) in [0,1] to V=1. Its population loss is L_M(F)=E[-V log F(W)-(1-V)log(1-F(W))], with the usual extended-value convention. A randomized map uses randomness independent of the entire training experiment and, in testing, independent of the source and attack randomness. Equivalently it specifies a fixed probability kernel on predictions conditional only on the observed word. The prediction class is all such maps, or any class containing the exact Bayes map below; statements about global minimizers apply only when that rule is available and the population infimum is attained.

Testing is a separate worst-case experiment: a fixed homogeneous order-two theta, arbitrary initial law mu, and a stationary Pi with P^2(u,v)>=Pi(v)/M for ALL four states u,v. A legal source-independent offline kernel changes at most k positions in {0,...,M-1} on each outcome and protects positions M,M+1. Loss is expected TV to theta_(X_M,X_(M+1)), NOT to the training posterior predictive distribution. Set g_M(k)=max(M^-1/2,k/M). Gamma_stat and Gamma_all are the supremum of risk/g over all k and qualifying test experiments, respectively with stationary and arbitrary initial laws, for the SAME map at fixed M.

Training does not condition theta on this critical test class. In fact some training sources have much weaker certificates. Its independently uniform initial pair is deliberately not theta-dependent stationary initialization. Changing either choice generally changes the posterior formula.

## 2. Finite theorem

Let s=M^-1/2, D=131081, and ell=1+log((M+2)/2).

(i) The unique population prediction kernel minimizing clean logloss is the deterministic map

    B_M(w)=(H_(U,1)(w)+1)/(J_U(w)+2).

Every minimizing randomized map equals B_M on every binary word, almost surely over its internal randomness. In particular exact global optimality gives a count-and-terminal-pair rule even when the admissible architecture has unrestricted full-history access.

(ii) For every homogeneous binary order-two source and every initial law, without any certificate assumption,

    E |B_M(W)-theta_U(1)| <= min(1,560/sqrt(M)).

Nevertheless on the critical testing class,

    2^-30 ell <= Gamma_stat(B_M) <= Gamma_all(B_M)
                 <= 560+192(1+log M).

Thus both unknown-budget factors are Theta(log M). The lower is a supremum over budgets and sources, not a logarithmic loss penalty at each budget. It is inherited by every exact population minimizer.

(iii) Let A_M be the accepted full-history first-half gate, defined explicitly below, and set Q_M=(1-2s)A_M+s in the probability-of-1 coordinate. Then it is a single budget-blind rule and

    Gamma_all(Q_M) <= 2^17+2^23+1.

Under the SAME training prior as (i), its finite clean excess satisfies

    0 <= L_M(Q_M)-L_M(B_M) <= log(1/s)                    [all M>=64],

and, if M>=(2D)^2,

    L_M(Q_M)-L_M(B_M)
      <= min{log(1/s), H_2(Ds)+Ds log((1-s)/s)}.

Here H_2(t)=-t log t-(1-t)log(1-t), including endpoint limits. In particular the excess is O(log M/sqrt(M)). Constants and the large threshold are deliberately conservative and are not practical sample recommendations.

## 3. Bayes calculation, full support, and proper-loss uniqueness

For every word w the conditional likelihood is

    Pr(W=w|theta)=1/4 product_u p_u^H_(u,1) (1-p_u)^H_(u,0).

The initial factor is 1/4, independent of theta. Each row posterior is therefore independent Beta(H_(u,1)+1,H_(u,0)+1). Although the terminal row U is selected by the word, conditional on W it is fixed. Conditional on theta,W the next label has probability theta_U(1). Taking its posterior mean proves the stated B_M formula. No claim of conditional independence of selected departures given their count or endpoint is used.

Indeed the exact marginal word probability is

    Pr(W=w)=1/4 product_u [H_(u,1)! H_(u,0)!/(J_u+1)!] > 0.

Every binary word has positive training probability, and B_M(w) is strictly between zero and one. Conditioning on W=w and the independent predictor randomness gives the standard exact identity

    L_M(F)-L_M(B_M)
      = sum_w Pr(W=w) E_rng KL(Bern(B_M(w)) || Bern(F(w))).

This identity remains valid with infinite loss on the left and nonnegative infinite terms on the right. Binary KL is nonnegative and vanishes precisely when its two probabilities agree (by strict convexity, or the log-sum inequality). A minimizer must consequently equal B_M almost surely for each word. The domain is finite, so a single probability-one event can cover all words if randomness is realized as a shared seed. Every corrupted test output is still one of these finitely many words; there are no unseen zero-training-probability words on which a global optimum can be freely changed. Equalities of the resulting prediction kernels therefore apply to every test source and legal attack.

## 4. Clean accuracy and robust nonadaptivity of B

For J>0, with C=H_(U,1),

    |(C+1)/(J+2)-C/J|=|J-2C|/[J(J+2)] <=1/(J+2).

The accepted empirical lemma gives E[1{J>0}|C/J-theta_U(1)|]<=512/sqrt(M+1). It is stated for designated symbol d(u)=1-first(u), but changing to symbol 1 complements both probabilities where necessary and leaves absolute error unchanged. The universal occupation lemma gives Pr(J=0)<=16/(M+1). Layer cake yields E[1/(J+2)]<=8/sqrt(M+1): for t in (0,1), the event J<t^-1-2 is either empty or is bounded using integer threshold ceil(t^-1-2)<=t^-1, giving probability at most min(1,16/((M+1)t)); integrate and use min(1,z)<=sqrt(z). Therefore clean risk is at most 520/sqrt(M+1)+16/(M+1)<=536/sqrt M, hence the advertised 560/sqrt M. This is a source-uniform unconditional risk bound, not conditioning on visits.

B factors through exact triple counts and terminal pair, hence through the accepted T_2 observation (counts plus first and last two symbols). The accepted finite-window theorem gives Gamma_stat(B)>=2^-30 ell. No reconstruction of the initial pair is needed; the extra observed initial pair is simply ignored. FOT003 confirms that for compatible exact word counts it is reconstructible anyway, but is not a dependency of this argument.

For completeness, the matching upper requires no certificate. Legal edits give |C'-C|,|J'-J|<=6k, with the same selected row because it is protected. Put a=C+1,b=J+2,a'=C'+1,b'=J'+2. Since 0<=a'/b'<=1,

    |a'/b'-a/b| <= (|a'-a|+|b'-b|)/b <=12k/(J+2),

and the difference is also at most one. For k>=1 the same integer-threshold occupation calculation bounds

    E min(1,12k/(J+2))
      <= integral_0^1 min(1,192k/((M+1)t)) dt
      <= 192(k/M)[1+log(M/k)].

To check the final inequality, put b=192k/M. If b>=1 the right side is at least one. If b<1, the integral is at most b(1+log(1/b)), which is at most the displayed expression. Thus edited risk is at most min(1,560s+192(k/M)[1+log(M/k)]). At k=0 use the clean bound; dividing by g and using 1<=k<=M gives the claimed factor upper.

## 5. Robust comparator and prior averaging with weak-certificate sources

On any observed word z let u be its final pair and d(u)=1-first(u). Let J', C' count all M departures from u and those with successor d(u), and let D' count departures from u among indices 0,...,floor(M/2)-1. The accepted half gate predicts designated probability a=C'/J' if J'>0 and 512D'>=J', and a=0 otherwise. Define A_M(z)=a when d(u)=1 and A_M(z)=1-a when d(u)=0. Hence A is a legal full-history probability-of-1 map, independent of k and beta.

The accepted general-beta bound is

    R(A)<=min{1,65536/sqrt M+65536/(M sqrt beta)+2^23 k/M}.

At beta=1/M this is <=2^17 s+2^23 k/M. Since |Q_M-A_M|=s|1-2A_M|<=s and 0<s<=1/8, Q_M lies in [s,1-s] and its test risk increases by at most s. This proves (iii)'s constant factor with arbitrary starts and legal randomized attacks.

For training, define m(theta)=min_u min(p_u,1-p_u). For 0<s<=1/2, independence gives Pr(m<s)=1-(1-2s)^4<=8s (the union bound alone suffices). On m>=s, every two-step pair probability is

    P^2((a,b),(c,d))=theta_(a,b)(c) theta_(b,c)(d)>=m^2.

Every finite stochastic matrix has a stationary law Pi; here strict positivity of P^2 also gives irreducibility. Since Pi(v)<=1, P^2(u,v)>=m^2 Pi(v), an all-state certificate beta=m^2. Applying the GENERAL-beta gate bound at k=0, with the independent uniform start, gives risk <=65536s+65536/(Mm)<=131072s. On m<s use the unit loss bound, including arbitrarily weak certificates. Averaging theta gives

    E_theta,W |A_M(W)-theta_U(1)| <=131080s,
    E_theta,W |Q_M(W)-theta_U(1)| <=D s.

One must not apply the critical-class bound uniformly to the training prior. These bounds explicitly pay for its weak-certificate tail. Boundary parameters m=0 have prior measure zero and would already be covered by the unit bound.

## 6. From source-TV accuracy to population excess logloss

Let p=theta_U(1), q=Q_M(W), b=B_M(W). Conditional on theta,W, the expected label logloss is H_2(p)+KL(p||q). Thus

    L_M(Q_M)-L_M(B_M)
       = E[KL(p||q)-KL(p||b)] <= E KL(p||q).

All quantities are finite: q is in [s,1-s], and b is in [1/(M+2),1-1/(M+2)]. Also, conditioning on W shows the stronger identity that this difference equals E KL(b||q). The target p is the true conditional source law, while b is its posterior mean; they are not interchangeable pointwise.

Elementary entropy bound: for any p,q in [0,1], delta=|p-q|, the Bernoulli coupling formed from a common uniform variable has disagreement indicator E with Pr(E=1)=delta. Each coupled binary variable is determined by the other and E. Therefore H(U|V)<=H(E)=H_2(delta), and conversely H(V|U)<=H_2(delta). The entropy chain rule implies |H_2(p)-H_2(q)|<=H_2(delta). If q in [eta,1-eta] and 0<eta<=1/2, direct expansion now gives

    KL(p||q)=H_2(q)-H_2(p)+(p-q)log((1-q)/q)
       <= H_2(delta)+delta log((1-eta)/eta).

Apply this at eta=s. Write delta_bar=E|p-q|<=Ds. Concavity of H_2 gives E H_2(delta)<=H_2(delta_bar). Only when Ds<=1/2 may we further use monotonicity on [0,1/2] to obtain H_2(delta_bar)<=H_2(Ds); the linear coefficient is nonnegative. This proves the large-M formula. For every M>=64, directly -p log q-(1-p)log(1-q)<=log(1/s), so KL(p||q)<=log(1/s), proving the separate finite small-M bound without an invalid Jensen/monotonicity shortcut. Finally H_2(x)<=x log(1/x)+x for x<=1/2 and log((1-s)/s)<=log(1/s), proving O(s log M) as M tends to infinity with D fixed.

## 7. Interpretation, scope, and antecedents

This shows a separation between exact optimality and a vanishing-excess criterion along growing horizons. At each fixed M, finite-word full support means that excess tending to zero controls the prediction kernel on every word; no fixed-horizon discontinuity is asserted. Exact clean population logloss singles out a rule whose worst unknown-budget TV factor grows logarithmically; a different full-history rule has a uniform factor and vanishing clean population excess. The average training objective and worst-case test supremum are different quantifiers. The source-wise clean accuracy of B rules out an explanation based merely on bad clean TV prediction.

It does NOT show that SGD finds or fails to find either rule, that arbitrary finite architectures represent B or Q, that an approximately optimal learned network is robust, or that corruption during training is mathematically necessary. It does not certify empirical nearoptimality from data, nor give a quantitative robustness conclusion for all near-minimizers. Internal randomness must not carry hidden theta or attack information. No neural statistical advantage is claimed; a classical counter can compute the gate.

The accepted finite positional manuscript supplies the occupation, empirical, general-beta half-gate, and finite-window lower interfaces. Accepted ACG001 verifies a more general approximate-statistic gate but its approximation theorem is not required here. BCJ001 already established the approximate half-gate/finite-bank mechanism; this candidate neither rediscovers it nor claims priority. A scoped local search for population logloss, cross-entropy, Beta(1,1), and clean-training terminology found no previous same objective statement in the inspected v10 research Markdown corpus; this is only a duplication check, not exhaustive historical or external novelty research. The entropy argument and posterior calculation above are proved here and require no external literature claim.

Diagnostics are finite checks, not proofs of the imported stochastic lemmas. SOURCE_BINDINGS.json pins the precise inspected sources and source gates. No external writes or consolidated manuscript edits were performed.
