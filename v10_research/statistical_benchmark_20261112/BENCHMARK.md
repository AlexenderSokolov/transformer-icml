# Statistical reference targets under fixed positivity/mixing

2026-11-12. Standard statistical benchmark consolidation, not a new estimator/rate claim. The existing `end-to-end-preln/REPORT.md` and `check_baselines.py` already give the spin innovation estimator and exact binomial risks; `low-rank-positional-interface/RESULT.md` already uses its root-N bound. This note adds an explicit finite-N general-row benchmark, minimax constants and a careful same-trajectory interface to the reviewed L2 obstruction.

## 1. Metric and general stationary class

Observe X_1,...,X_N in {-1,+1}, N>=3, n=N-2. For fixed known0<c<1/2, let q_(x,y)=P(X_(i+2)=+1 | X_i=x,X_(i+1)=y) belong to[c,1-c]. The source is a stationary homogeneous second-order chain. Risk is

    R(qhat,q)=E_q |qhat(X_1:N)-q_(X_(N-1),X_N)|.

This is TV error in estimating the conditional next-token law, NOT zero-one error against the realized next random token. There is no positive statistical noise floor for this metric as N grows.

For u in the four pair states define, using i=1,...,n,

    Y_i=(X_i,X_(i+1)), J_u=sum_i 1{Y_i=u},
    A_u=sum_i 1{Y_i=u,X_(i+2)=+1},
    f_u=clip_[c,1-c]((A_u+1/2)/(J_u+1)).

The row-frequency predictor is f_(X_(N-1),X_N). All counts and the selected terminal row come from the SAME path. The denominator is always positive. This is a non-neural one-pass algorithm with four pairs of O(log N)-bit integer counters and constant extra token memory. Its O(N) streaming time uses the word-RAM convention with O(log N)-bit words; it is not an O(N) bit-operation or neural-compilation claim.

## 2. Finite-N row-frequency guarantee, without conditional iid claims

Let F_j=sigma(X_1,...,X_j), pi the stationary pair law, and

    d_i=1{Y_i=u}(1{X_(i+2)=+1}-q_u).

Then d_i is F_(i+2)-measurable and E[d_i|F_(i+1)]=0. Different increments are orthogonal. Thus M_u=A_u-q_uJ_u has E M_u²<=n pi_u/4. This is a martingale calculation, not an assertion that outcomes are iid conditional on occupation or terminal state.

For the pair transition matrix P, each entry of P² is at least c²: any target pair is reached by its two prescribed symbols, each with probability at least c. Therefore pi_u>=c² and, with rho=1-4c²,

    ||P^k(u,.)-pi||TV<=rho^floor(k/2).

Stationarity gives covariance pi_u(P^k(u,u)-pi_u). Hence

    Var J_u <= n pi_u [1+2 sum_(k>=1)rho^floor(k/2)]
             = n pi_u(1/c²-1) <= n pi_u/c².

On G_u={J_u>=n pi_u/2}, clipping and Cauchy-Schwarz imply

    E[|f_u-q_u|1_Gu]
      <= 2(E|M_u|+1/2)/(n pi_u)
      <=1/sqrt(n pi_u)+1/(n pi_u).

Chebyshev gives P(G_u^c)<=4/(n pi_u c²); the error there is at most1. Consequently

    E|f_u-q_u|<=1/sqrt(n pi_u)+(1+4/c²)/(n pi_u).

Handle the data-dependent terminal selection directly:

    R= sum_u E[1{terminal=u}|f_u-q_u|]
      <=sum_u E|f_u-q_u|
      <= U_n:=4/(c sqrt(n))+4/(n c²)+16/(n c^4).

No independence between terminal and estimator is used. Constants are deliberately loose. To obtain an entirely explicit uniform benchmark, choose the constant predictor1/2 if U_n>=(1-2c)/2, and otherwise choose the row-frequency predictor. This choice uses only known n,c and gives

    sup_q R <=min(U_n,(1-2c)/2).

It is not claimed that the displayed finite-N bound is sharp, or that the data-dependent frequency predictor uniformly beats the constant predictor at small N.

## 3. Sharper reference for the stationary spin subclass

Set a=1-2c, q_xy=(1+theta xy)/2, |theta|<=a. The stationary pair law is uniform. Innovations Z_i=X_i X_(i+1) X_(i+2), i=1,...,n, are iid signs with mean theta. This follows from the bijection between the path and (X_1,X_2,Z_1,...,Z_n), whose law factors into the uniform initial pair and innovation probabilities. It does not extend to the whole four-parameter class.

Define theta_hat=clip_[−a,a](n^-1 sum_i Z_i) and

    qhat=(1+theta_hat X_(N-1)X_N)/2.

Pathwise error is |theta_hat-theta|/2, regardless of dependence between the endpoint pair and estimator. Therefore

    R_theta<=sqrt(1-theta²)/(2sqrt(n)),
    E|qhat-target|²<= (1-theta²)/(4n).

Its exact finite-sample risk is

    (1/2)sum_(k=0)^n binom(n,k)p^k(1-p)^(n-k)
       |clip_[−a,a](2k/n-1)-theta|, p=(1+theta)/2.

Choosing this estimator or constant1/2 by comparing their known uniform upper bounds gives sup_theta R<=min(a/2,1/(2sqrt(n))). Raw token counts are not innovation counts. This is the existing benchmark, explicitly recorded rather than presented as new research.

## 4. Unavoidable finite-sample minimax lower bound

Let h=min(a,1/(4sqrt(n))) and compare theta=+h,-h. They have the same stationary initial pair. The full-history KL is

    n h log((1+h)/(1-h)) <=(32/15)n h²<=2/15,

using h<=1/4 and log((1+h)/(1-h))<=2h/(1-h²). Pinsker gives TV<=1/sqrt(15). For any history, the two next-plus targets differ by exactly h; the endpoint parity only changes the sign of that difference. Integrating the pointwise two-target triangle inequality against the minimum of the two history laws yields equal-prior risk at least

    (h/2)(1-TV)>=h/3.

Thus unrestricted minimax risk over the spin subclass, and also the larger stationary class, is at least

    (1/3)min(1-2c,1/(4sqrt(N-2))).

For the spin subclass the displayed upper/lower bounds establish order min(1-2c,(N-2)^(-1/2)). For general fixed c the loose row-frequency upper and subclass lower both establish root-N order, without matching constants or optimal dependence on c. “Unavoidable” refers to finite-sample estimation uncertainty, not a constant aleatoric floor in the TV metric.

## 5. Conditional interface to the reviewed L2 theorem

Suppose the reviewed architecture theorem supplies a COMMON theta-independent template g_N(endpoint), and at theta=+h and -h respectively gives L2 errors epsilon_+,epsilon_-. Suppose also the endpoint distribution is the same under both sources, as it is for the stationary spin family. Then the template's equal-prior risk is at least h/2, and Cauchy-Schwarz plus triangle inequality gives the network's equal-prior risk at least

    h/2-(epsilon_++epsilon_-)/2.

This inference requires a genuinely common template; if it may depend on theta through the source law, the inference is invalid. No endpoint/estimator independence is needed. For fixed h and vanishing L2 errors this architectural constant floor contrasts with the unrestricted root-N reference. The remaining construction problem is legally extracting/aggregating useful order information and applying endpoint modulation under the stated architectural resource contract, not inventing a new statistical estimator.

## Diagnostics and limits

`check.py` uses exact rational enumeration for four general stationary transition tables and verifies stationary laws, occupation variances, martingale second moments, same-trajectory selected risk and per-row inequalities. It separately checks exact binomial two-point lower bounds and the spin estimator risk identity. These are finite checks, not proof of the general theorem or sharp constants. No training or neural compilation is attempted.
