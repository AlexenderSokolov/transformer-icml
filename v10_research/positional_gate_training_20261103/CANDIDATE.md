# PGT001: exact clean population descent removes a supplied positional gate

3 November 2026. Candidate for independent review and root acceptance. Separate from the frozen 55-page manuscript. Root supplied the synthesis route. This is a deliberately specified scalar-bias model, not a novelty claim, learned-attention theorem, or general SGD result. All logarithms are natural.

## 1. Experiments, features, and finite statement

Fix an integer M>=64. Training is exactly CTO001: four independent row probabilities p_u=theta_u(1) uniformly distributed on (0,1), an independent uniformly distributed initial binary pair, M observed departures, and one next-symbol label. The observed word W=(X_0,...,X_(M+1)) has terminal pair U=(X_M,X_(M+1)); label V=X_(M+2) is excluded from all features. Its exact posterior predictive probability of 1 is

    B(w)=(H_(U,1)(w)+1)/(J_U(w)+2).

For any observed word w, J counts departures from its terminal pair over indices 0,...,M-1, and D counts them over 0,...,floor(M/2)-1. Define

    F(w)=first(U),   G(w)=1{J>0 and 512D>=J},
    B_G(w)=G(w)B(w)+(1-G(w))F(w),
    s=M^(-1/2), K=(log M)/2, phi_M(w)=(2G(w)-1)K,
    omega_b(w)=1/(1+exp(-b-phi_M(w))),
    q_b(w)=omega_b(w)B(w)+(1-omega_b(w))F(w).

Only b is trainable. B, F, G, K and phi_M are explicitly supplied fixed features and computations. In particular the first-half positional count is not learned. Neither k nor a mixing certificate is an input. Set b_0=0.

Testing is exactly CTO001's separate critical experiment: fixed homogeneous binary order-two theta, arbitrary initial law mu, stationary Pi with P^2(u,v)>=Pi(v)/M for all four states, and any source-independent offline randomized editing kernel changing at most k positions in 0,...,M-1 per outcome, protecting M,M+1. Here 0<=k<=M is integer. Test loss is expected TV to the true terminal source row theta_U, not to B. Let

    g_M(k)=max(s,k/M),
    Gamma_all(Q)=sup_(qualifying theta,mu,attack,k) R(Q)/g_M(k).

Define Gamma_stat similarly with stationary starts. Every predictor in this statement is the same fixed map across budgets and sources.

**Theorem.** Let a be any fixed finite positive real step size and use the exact clean population gradient

    L_M(b)=E[-V log q_b(W)-(1-V)log(1-q_b(W))],
    b_(t+1)=b_t-a L_M'(b_t).

Then:

1. The initialized predictor has a uniform robust guarantee

       R(q_0)<=min{1,(2^17+17)s+(2^23+192)k/M},
       Gamma_all(q_0)<=2^17+2^23+209.

2. Every iterate is finite, b_(t+1)>b_t, and b_t tends to +infinity. L_M(b_t) decreases strictly to the exact Bayes loss L_M(B). No finite b attains that infimum.

3. At each fixed M, q_(b_t) converges uniformly over all words to B, and

       |Gamma_all(q_b)-Gamma_all(B)|<=min(sqrt(M),M exp(-b)),

   with the same inequality for Gamma_stat. Consequently

       lim_(t->infinity) Gamma_all(q_(b_t))=Gamma_all(B),
       2^-30[1+log((M+2)/2)] <= Gamma_stat(B)
          <= Gamma_all(B) <= 560+192(1+log M).

   The limiting worst unknown-budget factor is therefore Theta(log M) as M grows. These are first t->infinity at fixed M, then comparisons across M. There is no uniform finite-iteration, practical-constant, or monotonic-in-t robustness claim.

The constants are intentionally loose inherited constants. Their separation becomes informative only asymptotically; these formulas do not establish a practically sized threshold for degradation.

## 2. Dependencies and antecedent check

Direct statistical inputs from the accepted finite positional manuscript are:

- For selected clean-row occupation J and every INTEGER w>=1, Pr(J<w)<=min(1,16w/(M+1)), for every homogeneous source and arbitrary start, without a certificate.
- The exact empirical first-half gate A predicts designated symbol d(u)=1-first(u) with probability C/J on acceptance J>0,512D>=J, and zero otherwise. Its general-beta risk is at most min(1,65536/sqrt(M)+65536/(M sqrt(beta))+2^23 k/M).
- An edit changes each selected-row departure count by at most six; protection of the terminal pair ensures the same selected row before and after edits.

CTO001, with its accepted hash checked in SOURCE_BINDINGS.json, supplies the posterior formula, full support of every word, clean prior experiment, critical logarithmic lower and upper bounds for B, and prior-averaged clean A risk <=131080s. The source of CTO001's lower is the accepted finite-window/count-observation lower bound. None of the imported stochastic lemmas is established by the finite diagnostics here.

Inspected CTO001, its existing Monte Carlo diagnostic, the exact finite positional source interfaces and a scoped local Markdown search for population gradient, trainable bias, sigmoid(b), one-parameter gate/bias, and gradient descent. The prior-art comparison already discusses specialized population gradient-flow results in other models; those results are not dependencies here. No matching one-bias statement was found in that scoped search. This is not an exhaustive archive or external novelty search. Existing approximate-gate and finite-bank results remain antecedents for the supplied features; this candidate does not claim their construction or learning.

## 3. Robustness of the hard Bayes gate and the initialization

On any word accepted by G, A's probability of 1 is H_(U,1)/J, regardless of the designated-symbol orientation. On rejection it is F=first(U). Thus B_G=A on rejection, including J=0, and on acceptance

    |B_G-A|=|J-2H_(U,1)|/[J(J+2)]<=1/(J+2).

For an edited word use primes for observed counts. This comparison only uses C'/J' when J'>0. In particular a rejected J'=0 word never produces an undefined empirical ratio.

We need a universal clean reciprocal bound. For t in (0,1), set x=t^(-1)-1>0. Integer J obeys {1/(J+1)>t}={J<x}={J<ceil(x)}. Here ceil(x)>=1 and ceil(x)<=x+1=t^(-1). The occupation lemma therefore gives

    Pr(1/(J+1)>t)<=min(1,16/((M+1)t)).

Integrating and using min(1,z)<=sqrt(z) proves E[1/(J+1)]<=8/sqrt(M+1). This includes J=0 and does not apply the integer lemma directly to a real threshold.

For k>=1 the clean event J>=12k implies J'>=J-6k>=J/2, so

    1/(J'+2)<=2/(J+4)<=2/(J+1).

On its complement use the unit bound for |B_G-A|. Since 12k is a positive integer, Pr(J<12k)<=min(1,192k/(M+1)), even when 12k>M. Consequently

    E|B_G(Z)-A(Z)|<=16/sqrt(M+1)+192k/(M+1)
                       <=16s+192k/M.

For k=0 no edit occurs and the accepted-branch comparison gives E|B_G-A|<=E[1/(J+2)]<=8/sqrt(M+1), hence also the displayed common bound. The attack can be randomized: these comparisons hold pathwise, and the probability event refers to the clean path.

At b=0 the two weights are 1/(1+s) on G=1 and s/(1+s) on G=0. Hence

    sup_w |q_0(w)-B_G(w)|<=s/(1+s)<=s.

Combining with the accepted critical A risk, and then the unit-loss cap, proves assertion 1. The extra 17s pays for add-one smoothing and the sigmoid approximation; there is no k-dependent initialization.

## 4. Conditional differentiation and divergence of the bias

For every word 1/(M+2)<=B<=1-1/(M+2), F is either zero or one, and 0<omega_b<1 at finite b. Thus q_b is interior. There are finitely many words and their masses do not depend on b, so termwise differentiation is valid, and L_M is continuously differentiable. Conditional clean label mean is B, giving

    d/db CE(B,q_b)=(q_b-B) q_b' /[q_b(1-q_b)],
    q_b-B=-(1-omega_b)(B-F),
    q_b'=omega_b(1-omega_b)(B-F).

Therefore the proposed derivative has the correct negative sign:

    L_M'(b)=-E[omega_b(1-omega_b)^2 (B-F)^2
                        /{q_b(1-q_b)}].

For an especially transparent bound let d=|B-F|, which is strictly between zero and one. For F=0, q_b=omega_b d; for F=1, 1-q_b=omega_b d. In both cases the conditional derivative simplifies to

    -(1-omega_b)^2 d/(1-omega_b d).

It is strictly negative. Since 1-omega_b d>=1-omega_b and d<1, its magnitude is at most (1-omega_b)d<1. Thus -1<L_M'(b)<0 for every finite b. In particular every finite-step update is finite, and 0<b_(t+1)-b_t<a. Large positive steps cannot increase the loss: L_M is strictly decreasing on the entire real line, not merely locally along a smoothness-controlled step.

If the increasing sequence b_t were bounded above it would have a finite limit b_*. Continuity would imply b_(t+1)-b_t tends to -aL_M'(b_*)>0, whereas convergence of the sequence forces those increments to zero. This contradiction proves b_t->+infinity. All finite-word q_b tend to B, and finite-word continuity of cross-entropy at the interior B proves L_M(b_t)->L_M(B). At finite b, q_b differs from B on every word, so strict properness makes its excess positive. B lies in the closure of this parameterized family, not at a finite parameter value.

## 5. Uniform convergence and continuity of the worst-case factor

For any finite b and any word, phi_M>=-K gives

    |q_b-B|=(1-omega_b)|B-F|
       <=1/(1+exp(b-K))<=min(1,exp(K-b)).

For any two deterministic maps Q,T with uniform probability difference at most epsilon, the reverse triangle inequality for Bernoulli TV gives |R(Q)-R(T)|<=epsilon on every individual qualifying test experiment, including edited words. Since g_M(k)>=s, each normalized risk differs by at most epsilon/s. Supremum over the same experiments preserves that bound in both directions. This proves the factor inequality; finiteness is automatic from R<=1 and g>=s.

Apply at b_t->infinity for fixed M, then import CTO001's factor bounds to prove assertion 3. In particular, for any fixed constant C, sufficiently large horizons have limiting factor greater than C; for each such fixed horizon, all sufficiently late iterates have factor greater than C. This does not bound those iteration indices uniformly in M, identify their practical size, or establish that factor increases at every individual step. Nor does it assert that the positional feature disappears exactly at any finite time: only its effect vanishes in the limit.

## 6. Optional clean excess of the initialized robust rule

The clean k=0 comparison above is <=8s, so E|q_0-A|<=9s. CTO001's prior-averaged risk of A is <=131080s, including its explicitly paid weak-certificate prior tail. Thus with D_0=131089,

    E_(theta,W)|theta_U(1)-q_0(W)|<=D_0 s.

No conditioning of the training prior on the critical test class is allowed. Both probabilities of q_0 are at least

    eta_M=1/[(sqrt(M)+1)(M+2)],

because omega_0>=1/(sqrt(M)+1), and both probabilities of B are at least 1/(M+2). The entropy/KL argument proved in CTO001 then gives, for every M>=64,

    0<=L_M(0)-L_M(B)<=log(1/eta_M),

and for M>=(2D_0)^2,

    L_M(0)-L_M(B)
      <=H_2(D_0s)+D_0s log((1-eta_M)/eta_M)
      =O(log M/sqrt(M)).

The large-M condition is needed for monotonicity of binary entropy on [0,1/2] after Jensen; no small-M substitution is implicit. Thus initialization can already have vanishing excess as M grows, although exact population optimization at each fixed M ultimately selects the nonadaptive limit.

## 7. Representation, computation, and interpretation exclusions

This is an explicitly fixed-feature scalar-bias learning model with a population-gradient oracle. Computing B requires terminal-row counts and division; computing G requires the paid first-half positional statistic, its comparison with J, and a J>0 test; F uses the protected terminal pair. Exact log M, sigmoid, real b, counts, comparisons, division, storage, addressing, raw input, activation/weight precision, and gradient evaluation all remain explicit unpriced operations here. The expectation can be written as a sum over 2^(M+2) words with exact prior masses, but this is not a free efficient procedure. No polynomial-time or finite-precision training guarantee is proved.

There is no stochastic minibatch gradient, general SGD convergence theorem, attention implementation, learned positional feature, generic architecture expressivity claim, neural advantage, or theorem that all clean-training algorithms must lose robustness. A classical counter can supply precisely the same features. The result is confined to the stated prior, clean population logloss, one-parameter path, initialization and exact updates. Changing the prior, initialization law, trainable features, objective, or training algorithm changes the problem. It does not prove corruption during training is necessary.

Diagnostics below are algebraic and finite checks, not evidence for the imported minimax lower bound or an empirical demonstration of worst-case degradation. No external writes, publication, or manuscript edits were performed.
