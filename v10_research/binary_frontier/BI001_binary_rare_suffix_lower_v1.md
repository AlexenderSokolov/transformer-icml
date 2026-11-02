# BI001 — Binary rare-suffix lower via a uniformly mixing active chain

2026-11-02. Author candidate; independent review required. No accepted file changed.

## Claim

In exactly SH001 §1's one-block bounded-local-ratio model, **K=2** suffices for a logarithmic lower at beta=0. More generally put

    e=max(sqrt(beta),1/M), z=kappa Q.

For M>=64, 0<=beta<=1/256, z<=M/4, there is c=c(D,r)>0 independent of all other parameters and encoder tables such that

    R_stat >= (c/z) log(1+(1/8) min{z/(M e), M/z}).       (BI1)

Thus at beta=0 and Q comparable to sqrt(M), risk O(M^-1/2) requires kappa=Omega(log M); SB001's binary upper supplies kappa=O(log M). Binary K=2 is **not** an exception to the no-mixing-constraint logarithmic necessity. This proof does NOT establish SH001's exact beta-adaptive threshold for binary sources. Its cutoff uses sqrt(beta), rather than beta.

## 1. Actual binary stationary source and all-state certificate

Order pair states as W=00,A=01,B=10,C=11. Fix a=1/(2M), p in I=[1/4,3/4], e as above, and homogeneous second-order rows

    theta_W(1)=a, theta_A(1)=p,
    theta_B(1)=1-e, theta_C(1)=1/2.

Let x=1/(e/a+2+2p). The actual stationary pair law is

    Pi=(xe/a,x,x,2px).

Direct multiplication verifies stationarity. In particular Pi_W>=4/11>1/4, since e>=1/M=2a. It depends on p and is hidden. The two-step transition matrix is

    [(1-a)^2, (1-a)a,       a(1-p),       ap]
    [(1-p)e,  (1-p)(1-e),   p/2,          p/2]
    [e(1-a),  ea,           (1-e)(1-p),   (1-e)p]
    [e/2,     (1-e)/2,      1/4,          1/4].

For completeness, a<=1/128, e<=1/16, e^2>=beta and e>=4beta. For target W, Pi_W<=1 and every entry is >=beta: the smallest relevant e/4>=beta; (1-a)^2>=beta. For target A or B use x<=a/e. The exceptional entry ea>=beta a/e uses e^2>=beta; row-W entries a(1-a),a(1-p) dominate beta a/e by e>=4beta. All other entries in these columns are >=1/8 or >=3/16, hence exceed beta x. For target C use Pi_C=2px<=2pa/e. Row-W entry ap dominates beta Pi_C because e>=2beta; every other entry is >=1/8, hence exceeds beta Pi_C since Pi_C<=1. This proves P²(s,t)>=beta Pi(t) for every binary pair s,t, including all starting states. Initialize at this Pi.

## 2. Reference suffix experiment and domination, not conditional IID

Set

    J=floor(min{1/(4e),M²/(4z²)}).

Under the domain above J>=4, J<=M/4, eJ<=1/4, and z sqrt(J)/M<=1/2. For 4<=j<=J, E_j consists of histories of length n=M+2 with n-j initial zeros, followed by a first 1 and an active suffix with no pair00. The suffix pair chain starts at A and follows the reference kernel

    R = [[0,1-p,p],[1,0,0],[0,1/2,1/2]]

on A,B,C for j-1 further transitions. Denote its law by nu_pj. Under the actual source every reference path has probability density

    Pi_W (1-a)^(M-j) a (1-e)^N_B

relative to nu_pj, where N_B is the number of transitions out of B within that suffix (N_B<=j-1). This density is at least 1/(32M): Pi_W>=1/4, (1-a)^M>=1/2, (1-e)^j>=1-ej>=3/4, a=1/(2M). The E_j are disjoint. Their probabilities need not be p-independent. No conditional uniform prior or IID suffix is asserted; use the SAME uniform prior on p and pathwise domination by (32M)^-1 nu_pj.

At terminal A the actual next-symbol law is Bernoulli(p). At terminal B or C it is not informative about p; their losses will simply be discarded.

## 3. Uniform coupling lemma for arbitrary positional local sums

The reference R obeys R²(s,B)>=1/8 for every s and p. Indeed the B-column of R² is (p/2,1-p,1/4). Couple two chains in two-step blocks using their shared atom (1/8)delta_B. After coalescence use identical transitions. Conditional bridges fill intermediate steps. The expected number of differing states, counting the initial state, is at most

    2 sum_(b>=0)(7/8)^b =16.

Consequently, for any sum F of position-specific functions of trailing windows of length <=r, each bounded in [-kappa,kappa], the difference between conditional expected remaining F after two possible next states following a common prefix is at most 32 kappa r: each differing symbol affects at most r summands, each by <=2kappa. The slack bound 34 kappa r will be used below. This argument also covers windows crossing the fixed zero-prefix boundary and shortened/padded windows.

Reveal the j-1 reference transitions successively. The Doob martingale increments for F have conditional range at most 34 kappa r, so orthogonality gives

    Var_p F <= (34 kappa r)^2 j.                         (3.1)

Differentiating the finite path-probability polynomial gives the sum of j-1 single-transition insertions of R'_p. Only row A varies, with signed entries -1,+1 to B,C. For every insertion the difference of continuation expectations is bounded by the same 34 kappa r, and the distribution of the preceding common prefix has total mass one. Therefore

    |d/dp E_p F| <=34 kappa r j.                         (3.2)

This is not an independent-coin bounded-difference argument. It uses uniform geometric coupling of the finite-state active chain.

Finally R³(s,A)>=(1/8) for all s: its A-column is (p/2,1-p,1/4). Thus under nu_pj, for every j>=4,

    P_p(terminal A)>=1/8.                               (3.3)

## 4. Complete good-message tube

Freeze every boundary side value s before taking reference-chain expectations, exactly as in BA001; H=2^(2r) bounds their number. A frozen numerator and denominator are sums to which (3.1)-(3.2) apply; deterministic zero-prefix terms do not affect either estimate. Denominators are >=M. Write h_ds=E A_ds/E D_ds and choose

    T=34r sqrt(64 D H), N=ceil(2T+4)+1,
    A0=H(2+68r)N^D.

Chebyshev and union over 2DH sums imply a simultaneous event G_pj of probability >=31/32 on which deviations from expectations are <=kappa T sqrt(j). Hence

    |B_ds-h_ds|<=2kappa T sqrt(j)/M,
    |h'_ds|<=68kappa r j/M.

With parameter mesh spacing <=M/(68r z j), all complete good messages (grid bank, actual boundary side, granted j, fixed metadata) belong to a p-independent set of cardinality at most

    R_j=A0(1+zj/M).

Indeed at most (2+68r)(1+zj/M) mesh points suffice per s; the scaled random-tube radius is <=T, mesh approximation adds 1 and downward rounding adds less than 1. A box of radius T+2 contains at most N^D integer grid banks. This remains true for negative numerator values and real Q. Exact boundary-query values are counted by s, not as independent infinite-range information.

## 5. Target-specific finite-message bound

Fix any decoder seed. On terminal A associate to each good message the decoder's predicted probability of symbol1. There are at most R_j such scalars. Under the uniform prior of length ell=1/2, the union of radius ell/(64 R_j) intervals about these outputs has prior probability <=1/32. For every p, (3.3) and P(G^c)<=1/32 give

    P_p(G and terminal A)>=3/32.

After integrating over the prior, the probability of being good, terminal A, and outside those output neighborhoods is >=1/16. The actual reference terminal target on A equals p, so

    E_prior,nu [loss * 1_terminalA]>=1/(2048 R_j).

No posterior uniformity after seeing the endpoint is used. Average over decoder seeds; encoder seeds are granted and treated conditionally, with the same uniform prior and constants.

Pathwise domination from §2, and the disjoint E_j, now give

    R_stat >= 1/(65536 A0 M) sum_(j=4)^J 1/(1+zj/M).

Put u=z/M<=1/4. With j=k+4, 1+u(k+4)<=(1+4u)(1+uk)<=2(1+uk). Integrating k=0,...,J-4 over [0,J-3], and using J-3>=J/4, yields

    sum_(j=4)^J 1/(1+uj) >= log(1+uJ)/(8u).

As J>=one-half its defining real cutoff,

    uJ >= (1/8) min{z/(Me),M/z}.

This proves BI1 with c=1/(524288 A0).

## 6. What the square-root-beta loss means

The naive same-scale binary transplant genuinely fails for this topology. Its stationary Pi_A=x, but P²(B,A)=ea. Thus the certificate requires

    ea>=beta/(e/a+2+2p),
    e²+ea(2+2p)>=beta.

If e and a are both order 1/M (constant stationary waiting and active masses, order-M active runs), necessarily beta=O(M^-2). This is a rigorous obstruction to this particular witness, NOT a universal upper bound, impossibility theorem, or proof of the optimal binary beta-dependence.

For beta=0, e=1/M and BI1 matches SH001's logarithmic form. The standard SH001 §5 necessity algebra, restricted to beta=0, gives kappa=Omega(log M) when Q is in a fixed sqrt(M) band and risk <=C/sqrt(M). SB001 works for K=2 and kappa=O(log M), so the order is matched there. For positive beta the exact binary threshold remains open.

Dependencies read: original intake instructions; BA001 complete proof; SH001 complete proof; UI001 source/model and uniform-IID scope; SB001 v2 model and upper. Diagnostics, independent audit, and root acceptance are still pending. No external novelty or implementation claim.
