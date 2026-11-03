# Noisy supplemental messages: common-overlap minimax reduction

Date: 2026-11-03. Status: independently derived proposition; awaiting separate review. This note uses no Markov-specific lemma and makes no claim that the v10 sharp reliability threshold has been established.

## Main findings

1. With unrestricted randomized estimators, nonnegative loss, and a fixed post-attack BSC with crossover probability eta, Gamma_eta >= 2 eta Gamma_0. This holds for arbitrary joint processing of the base observation and noisy bit, not just decode-then-estimate procedures.
2. For loss in [0,1], Gamma_exact <= Gamma_eta <= min{Gamma_0, Gamma_exact + eta/g_min}, with the additive bound useful only if g_min = inf_k g_k > 0.
3. For R independent transmissions of the same bit, the stronger common-overlap lower bound uses lambda_R = sum_y min(P_0(y),P_1(y)). For fixed 0 < eta < 1/2,
   lambda_R = Theta_eta(R^(-1/2) rho^R), rho=2 sqrt(eta(1-eta)).
4. If Gamma_0 >= c log M, a bounded noisy competitive ratio requires R = Omega_eta(log log M). A generic sufficient construction using error O(M^(-1/2)) takes R=O_eta(log M). These bounds leave a genuine gap and do not identify a sharp threshold.

## 1. Experiment, estimator class, and quantifiers

Let k range over a nonempty budget set K. For each k let I_k be a nonempty set of admissible data-law/attack-kernel pairs. Write i in I_k for the entire instance. Under i, sample a state S including the target, any complete path, and any pre-channel randomness; perform the admissible attack; and obtain base observation Z and a bit b=b(S) (or b determined by the extended pre-channel state). Loss is ell_i(S,a)>=0 and normalizer g_k>0. The bit's particular path definition is irrelevant to the reduction.

A single estimator A is a Markov kernel from its observations to actions. It cannot take the unknown k or i as an extra input unless those variables are already explicitly part of the observation model. Estimator-private randomness independent of the experiment is permitted. The admissible estimator class is closed under ignoring an observation, independent random simulation, and composition with a known channel. Define

Gamma_0 = inf_A sup_{k in K} sup_{i in I_k} E_i[ell_i(S,A(Z))]/g_k,
Gamma_Q = inf_A sup_{k in K} sup_{i in I_k} E_{i,Q}[ell_i(S,A(Z,Y))]/g_k,
Gamma_exact = inf_A sup_{k in K} sup_{i in I_k} E_i[ell_i(S,A(Z,b))]/g_k.

Here Y is drawn from a fixed known channel Q(.|b), independently of the complete pre-channel experiment conditional on b. Crucially the instance sets I_k are identical in the three comparisons. The suprema remain outside the risk and inside the estimator infimum; neither an instance-dependent estimator nor a budget-specific estimator is introduced.

The arguments allow extended nonnegative risks. Statements involving an additive upper bound are understood in the extended sense; products 0 times infinity are avoided by treating zero overlap separately.

## 2. General finite-input, finite-output common-overlap theorem

More generally let the hidden message X take values in a finite alphabet H and let Y take values in a finite alphabet O. Define

m(y)=min_{x in H} Q(y|x),  lambda=sum_y m(y),  0<=lambda<=1.

Then, for lambda>0,

                       Gamma_Q >= lambda Gamma_0.

For lambda=0 the corresponding assertion is simply Gamma_Q>=0. For lambda=1, Q has identical rows and Gamma_Q=Gamma_0.

### Proof preserving all quantifiers

Fix any joint noisy-observation estimator A. If lambda>0, define a *single* baseline estimator A^m: on Z=z, independently sample V from m/lambda and run A(z,V), including its ordinary private randomness. This construction depends on Q and A only, not on k, i, S, or b.

For every k and i, conditional on the entire pre-channel state (including Z and X), Q(y|X)>=m(y). Nonnegative loss therefore gives

R_i,Q(A) >= sum_y m(y) E_i[ell_i(S,A(Z,y))]
          = lambda R_i(A^m).

Dividing by the same g_k and taking the two suprema yields

sup_{k,i} R_i,Q(A)/g_k >= lambda sup_{k,i} R_i(A^m)/g_k
                              >= lambda Gamma_0.

This holds for every A, so taking inf_A proves the assertion. There is **no interchange of infimum and supremum** and no assumption that A decodes X first. It covers arbitrary optimal joint decoding/estimation and arbitrary use of the correlation between Z and X.

Equivalent latent-mixture interpretation: Q(.|x)=lambda (m/lambda)+(1-lambda)Q_res(.|x). A Bernoulli mixture indicator can be sampled independently of all pre-channel variables. On the common component, Y contains no new information beyond Z. The estimator need not know that component occurred.

For a general input alphabet the same argument works when the pointwise infimum is measurable and defines a common subprobability measure. Pairwise overlap alone is not generally a universal common component when there are three or more possible messages. For two rows, lambda=1-TV(Q(.|0),Q(.|1)).

### Sharpness as a universal multiplicative constant

Consider no base observation, a parameter b in {0,1}, zero-one estimation loss, g=1, and BSC_eta. Randomized baseline minimax risk is 1/2, noisy minimax risk eta, and exact risk zero. Thus Gamma_eta/Gamma_0=2 eta. No universally larger BSC multiplicative factor is possible. For the symmetric repeated-BSC experiment below the same example gives Gamma_R/Gamma_0=lambda_R.

## 3. One BSC transmission and bounded-loss upper bound

For 0<=eta<=1/2,

Q_eta = 2 eta U + (1-2 eta) I,

where U outputs an independent uniform bit and I copies the hidden bit. The common mass is exactly lambda=2 eta. Consequently Gamma_eta>=2 eta Gamma_0 for eta>0, with the trivial nonnegative statement at eta=0.

Ignoring Y gives Gamma_eta<=Gamma_0. Simulating Q from the exact bit gives Gamma_exact<=Gamma_eta. For the remaining upper bound assume 0<=ell<=1 and take an epsilon-optimal exact estimator A. Couple B=b xor N with N~Bernoulli(eta) independent of the entire experiment and estimator randomness, and apply A(Z,B). When N=0 its action and loss agree with A(Z,b); when N=1 the loss increases by at most 1. Hence for every i,

R_i,eta(A applied to B) <= R_i,exact(A)+eta.

If g_min=inf_k g_k>0, the unified estimator has worst normalized risk at most Gamma_exact+epsilon+eta/g_min. Let epsilon decrease to zero. No minimizer is assumed to exist. If Gamma_exact is infinite the stated upper bound is vacuous. If g_min=0, the uniform additive expression is infinite; the per-instance inequality still holds but does not by itself control the competitive ratio.

Without bounded loss the additive eta/g_min bound is false: multiply zero-one loss by an arbitrarily large constant in the binary example. Without randomized baselines the overlap proof does not establish the asserted Gamma_0 bound: A^m may be randomized. For example a single fair uninformative channel output lets a deterministic-only estimator randomize a binary guess, reducing worst-case risk from 1 to 1/2, even though lambda=1. Thus randomization closure is essential or must be replaced by a problem-specific derandomization argument.

## 4. R independent transmissions of the same bit

For integer R>=0 observe Y=(b xor N_1,...,b xor N_R), with iid Bernoulli(eta) noise independent of the entire pre-channel experiment. These are repetitions of one fixed hidden bit, not R different path queries or adaptive message choices. For an output string y of Hamming weight j,

P_0(y)=eta^j(1-eta)^(R-j),
P_1(y)=eta^(R-j)(1-eta)^j.

Thus

lambda_R = sum_{j=0}^R binom(R,j) min{eta^j(1-eta)^(R-j), eta^(R-j)(1-eta)^j}.

For 0<eta<1/2, if T~Binomial(R,eta), symmetry gives the exact form

lambda_R = 2 P(T>R/2) + P(T=R/2).

The equality event is empty for odd R. With fair independent tie-breaking, majority decoding has the same conditional error for either bit,

e_R = P(T>R/2)+(1/2)P(T=R/2)=lambda_R/2.

This is also the equal-prior binary-testing Bayes error. Symmetry makes it a minimax decoder for this channel alone. None of these decoding-optimality facts are needed for the joint-estimator lower bound:

Gamma_R >= lambda_R Gamma_0.

For bounded loss and g_min>0, decode by majority and apply an epsilon-optimal exact estimator to obtain

Gamma_exact <= Gamma_R <= min{Gamma_0, Gamma_exact+e_R/g_min}.

Optimal joint processing can be better than this construction, but cannot evade the common-overlap lower bound.

## 5. Exponential estimates and reliability implications

Fix eta strictly between 0 and 1/2. Put rho=2 sqrt(eta(1-eta)) in (0,1) and D=-log rho=D_KL(Bernoulli(1/2)||Bernoulli(eta)). All logs here are natural.

The elementary Bhattacharyya bound gives

lambda_R <= sum_y sqrt(P_0(y)P_1(y)) = rho^R.

A useful weaker lower bound follows immediately by retaining the all-common components in the one-bit mixture:

lambda_R >= (2 eta)^R.

A sharper two-sided estimate, with positive constants depending only on eta, is

c_eta rho^R/sqrt(R+1) <= lambda_R <= C_eta rho^R/sqrt(R+1),  R>=1.

Proof: take j_0=ceil(R/2). The first upper-tail point mass is
p_{j_0}=binom(R,j_0) [eta(1-eta)]^(R/2) times 1 if R even, or sqrt(eta/(1-eta)) if R odd.
The central-binomial estimate binom(R,ceil(R/2))=Theta(2^R/sqrt(R+1)), obtained directly from Stirling's formula, proves the claimed order for p_{j_0}. Above j_0 successive point masses have ratio

p_{j+1}/p_j = ((R-j)/(j+1)) eta/(1-eta) <= eta/(1-eta)<1.

Therefore the relevant tail is between its first term and that term divided by 1-eta/(1-eta). For odd R, lambda_R is twice this tail. For even R, lambda_R is p_{R/2} plus twice the strictly larger-index tail, so it lies between p_{R/2} and a fixed eta-dependent multiple thereof. This proves both sides, with parity incorporated into the constants. These constants are not claimed uniform as eta tends to 0 or 1/2.

### Necessary repetition count

Suppose a family of problems indexed by M has Gamma_0(M)>=c log M, and demand Gamma_R(M)<=C with constants c,C>0 independent of M. For fixed eta in (0,1/2), the coarse lower bound already implies

(2 eta)^R c log M <= C,
R >= [log log M + log(c/C)]/log(1/(2 eta)) = Omega_eta(log log M).

The sharper bound implies

R D + (1/2)log(R+1) >= log log M - O_eta,c,C(1).

In particular the necessary count is at least (log log M -(1/2)log log log M-O(1))/D: if R exceeds (log log M)/D this is automatic; otherwise bound log(R+1) by log log log M+O_eta(1). This is only a necessary condition furnished by this reduction, not a matching lower bound on achievable reliability complexity.

### Generic sufficient repetition count, with explicit extra assumptions

If Gamma_exact(M)<=C_0 and g_min(M)>=c_g M^(-1/2), majority plus the exact estimator has Gamma_R<=C_0+rho^R M^(1/2)/(2c_g). Taking

R >= (log M)/(2D)+O_eta,c_g(1)

makes the excess ratio O(1), so R=O_eta(log M) suffices under these assumptions. More generally e_R=O(g_min) suffices, giving R=O_eta(log(1/g_min)) when g_min tends to zero. An error target M^(-1/2) by itself costs O_eta(log M) transmissions, but its relevance to competitive risk depends on the normalizer and exact estimator bound. Neither condition is proved here for v10.

**Unresolved gap:** Omega(log log M) necessity versus O(log M) generic sufficiency. Do not report either bound as a sharp reliability threshold. Joint estimation may exploit Z and outperform the generic decoding upper bound; this note does not settle whether it does for the concrete experiment.

## 6. Attack/noise ordering and information conditions

The precise sufficient condition is P(Y=y | complete pre-channel state)=Q(y|b). The attack may know the data, b, eta, R, and estimator; it may be randomized and correlate Z strongly with b. Merely knowing the noise distribution or eventual decoding rule does not break the theorem. Conditional on b, actual channel coins must still be fresh and independent of the state and attack that produced Z and the loss target.

“Attack occurs first” is not by itself enough if an attacker is given future channel coins, channel outputs, or correlated side information before acting. Noise-aware adaptation can destroy the fixed-channel conditional law and the common-component simulation proof. An attack performed after the transmissions can also fall outside the theorem if it uses the observed outputs to change Z or the evaluated state. If the actual attacker families differ across baseline/exact/noisy experiments, the same-family comparison needs a separate inclusion argument and cannot simply be assumed.

If the noise coins are revealed to the estimator, BSC can be inverted: Y together with N reveals b exactly. The relevant observed channel is then the augmented channel (Y,N), whose two input rows have disjoint supports and overlap zero. Thus one cannot apply the 2 eta lower bound while silently exposing noise randomness.

The theorem does not require the attacker to be ignorant of the hidden bit. It requires ignorance of fresh realized channel randomness in the specific conditional-independence sense above. If the state includes attacker's private randomness, that randomness also precedes and is independent of the channel coins.

## 7. Boundary and failed-extension ledger

- eta=0: one transmission reveals b; lambda_R=0 for R>=1, e_R=0, Gamma_R=Gamma_exact. The positive-noise Omega(log log M) conclusion does not apply.
- eta=1/2: all transmissions are independent of b; lambda_R=1, e_R=1/2, Gamma_R=Gamma_0 for every finite R, and no finite repetition count recovers information. rho=1, D=0; the fixed-interior asymptotic formula and repetition bounds do not apply.
- R=0: the output alphabet contains just the empty string, lambda_0=1, e_0=1/2 (a private fair guess), Gamma_R=Gamma_0 regardless of eta. This avoids ambiguous 0^0 terms in the expanded mass formula.
- R=1: lambda_1=2 eta, e_1=eta, reproducing Section 3.
- R=2: lambda_2=2 eta, because fair ties mean the second repetition does not reduce the minimax bit error. Repetition improvement is not strictly monotone at every integer.
- Unbounded loss: the additive error upper bound fails without an integrable uniform loss-difference bound.
- g_min=0: no finite uniform eta/g_min or e_R/g_min upper bound follows.
- Deterministic-only baseline: common-output simulation may leave the estimator class; the randomized baseline qualification is essential.
- Instance-specific/channel-specific choice of an estimator inside the adversarial supremum is invalid; the proof instead fixes A and constructs one A^m valid for every instance.
- Replacing lambda_R by 2 eta independently of R is false: for fixed eta<1/2, lambda_R tends to zero and the binary testing example attains the ratio lambda_R.
- Replacing the all-row overlap by a minimum pairwise overlap for a general multi-message channel is unjustified: pairwise common portions need not coincide. The theorem uses one common submeasure dominated by every row.
- Sharpness for the concrete v10 risk/normalizers is not established by the binary example, which only proves sharpness of the universal channel factor.

No repository publication or external state change was performed in this derivation.

## 8. Any R-bit encoded supplemental message through independent BSC noise

Let C in {0,1}^R be an arbitrary pre-channel encoded message. It may depend on the full path, Z, the instance, and private encoder randomness; include all such randomness in the pre-channel state. Corruption, encoding, and the base observation must be fixed before the fresh independent noise is sampled. The estimator observes noiseless Z and Y=C xor N, where N has independent Bernoulli(eta) coordinates, 0<=eta<=1/2.

For every c and y, Q(y|c)>=eta^R. Consequently a common submeasure is m(y)=eta^R, with total mass (2 eta)^R, and

Gamma_encoded,R >= (2 eta)^R Gamma_0,  0<eta<=1/2.

This statement applies to *every* encoder and joint estimator, and hence also to an infimum over an allowed family of encoders: each composite procedure induces one baseline simulator drawing an independent uniform R-bit Y. Encoder dependence on Z or a hidden state does not change this uniform common component. A randomized encoder is handled by conditioning on its private coins and then averaging. If the family of feasible baseline instances itself depends on the selected encoder, however, a fixed-family minimax comparison needs separate justification.

For all 2^R possible clean strings this common mass is exact: each output y has a complementary input c with Q(y|c)=eta^R. A restricted codebook may have a larger common mass; repeating a single bit is precisely such a restriction and admits the sharper lambda_R above. Do not apply that repetition-specific lambda_R to an arbitrary R-bit code.

Thus a bounded competitive ratio C requires

R >= log(Gamma_0/C)/log(1/(2 eta))

whenever 0<eta<1/2 and Gamma_0>C. In particular Gamma_0>=c log M entails Omega_eta(log log M) necessary noisy message length even for arbitrary encoding, not only repetition. For each fixed R and eta>0, Gamma_encoded,R is bounded below by a positive constant times Gamma_0; combined with ignoring the supplemental message, its optimum is Theta_eta,R(Gamma_0). At eta=1/2 every such noisy message is independent uniform and gives exactly Gamma_0. At eta=0, R>=1, the nontrivial lower bound vanishes; R=0 always gives Gamma_0.

This does not assert that an R-bit *whole-message* decoding error is small, does not allow correlated or adversarial noise, and does not apply if the base observation is also replaced by a noisy observation. The sufficiency claim remains the separate construction that repeats the already-proved single exact gate and applies the bounded-loss error-transfer argument.

### Explicit failure of noise-aware corruption

Let the target theta range over {0,1}, take hidden bit b=theta, and take a fair fresh noise bit N. If an attacker who sees N is allowed to set Z=N and Y=theta xor N, then Z alone is uniform and has randomized minimax zero-one risk 1/2, while (Z,Y) determines theta and has risk zero. The purported eta=1/2 factor-one lower bound would fail. The example violates the required conditional law Y|complete pre-channel tuple=BSC_(1/2)(b): once Z=N is included, the channel noise is no longer fresh. It demonstrates why temporal/conditional-independence qualifications are substantive, rather than cosmetic.
