# Independent review of PBF001

## Verdict

PASS at the explicitly stated scope. No mathematical correction is required. This closes the robustness window and an exact projected population update inside accepted PGT001's supplied-feature scalar model. It is not a new statistical mechanism, an independently established stochastic lower bound, external novelty certification, a learned-attention result, or an implementation theorem.

Reviewed candidate SHA-256: `437d945df88004758d4153385fd00699dd33ea5bee378a4e2aebbf797a9fc642`.
Reviewed source-bindings SHA-256: `4a20beb08e9624136c68672ba431c2354b9a361860448968db3e372bdb0d33e0`.

I read the complete PBF001, PGT001 and CTO001 candidate texts, the PGT/CTO acceptance records, the finite positional manuscript's experiment and factor/oracle interfaces, its complete oracle-floor lemma/proof, and its acceptance record. The six direct source hashes and byte lengths match. The independently used oracle proof source is additionally bound in this review's bindings. Accepted stochastic interfaces remain imports; this review does not reprove all occupation, half-gate or count-observation lower lemmas.

## 1. Model and target audit

There are M observed departures, with successor counts from indices 0 through M-1, observed terminal pair (X_M,X_(M+1)), and training label X_(M+2) excluded from features. B uses the observed terminal row's add-one count. Training has independent uniform row parameters and an independent uniform initial pair. This matters for the posterior; a stationary theta-dependent training start would change it. Testing instead uses a fixed homogeneous source, an all-state two-step certificate 1/M, protected terminal symbols, and source-independent legal offline kernels with per-outcome edit budgets. Loss is TV to the true source row at the actual protected terminal pair, not to the posterior B or an independent query. The same fixed predictor at each horizon serves every budget and source.

PGT's supplied G is the hard first-half gate, F is the first terminal bit, and H=GB+(1-G)F is deterministic and budget blind. The submitted formula for omega means w1 on G=1 and w0 on G=0; it does not multiply a weight by the Boolean gate. The candidate explicitly clarifies this notation. Independent prediction seeds in the source interface cannot encode theta or attack information. PBF itself only uses deterministic maps, and its pointwise inequalities hold after averaging all allowed path/attack randomness.

## 2. Imported constants and full-history floor

PGT section 3 gives a critical empirical-gate risk at most 2^17 s+2^23 k/M and a hard-Bayes-gate difference at most 16s+192k/M. Dividing by max(s,k/M) gives CH=2^17+2^23+208=8,519,888. The added 208 is 16+192, not a sigmoid approximation term. Thus D=8,519,889.

CTO's B upper is 560+192(1+log M). The candidate's inequality 1+log M <= ell+log 2 <=2ell is valid because log 2 <=ell. Using ell>=1 gives 560+384ell<=944ell. The lower cB ell uses cB=2^-30 and counts/terminal observation; B ignores the additionally available first pair. This lower is not applied directly to q or H, which use more history.

The full-history oracle lower is separately necessary. The precise manuscript proposition includes full histories, stationary starts, independent decoder randomness, and risk >=g/96 even when the budget is supplied. In fact the clean part alone gives >=1/(64 sqrt M) using stationary IID Bernoulli alternatives, identity attack, and a terminal target equal to the common IID parameter. These sources satisfy the all-state certificate since P^2(u,v)=Pi(v). For any particular full-history q, its k=0 supremum divided by s is therefore at least 1/64, hence certainly c0=1/96. This is a per-map floor, not an unjustified restricted-observation floor or an assumption of a common hardest source. A randomized full-history estimator is covered by the test argument with independent seeds.

## 3. Mixture and supremum audit

On G=0, the identity reduces to q=w0 B+(1-w0)F. On G=1, H=B, and the remainder (1-w1)(F-B) converts B into w1 B+(1-w1)F. The absolute remainder is bounded by 1-w1 <= exp(-b-K)=s exp(-b). All targets are probabilities, so Bernoulli TV is the absolute scalar difference used here.

For each individual stationary experiment e, with its own g_e, the reverse triangle inequality gives r_q(e)>=w0 r_B(e)-(1-w0)r_H(e)-exp(-b). Since r_H(e)<=CH uniformly, taking the supremum gives Gamma_stat(q)>=w0 Gamma_stat(B)-(1-w0)CH-exp(-b). The weight w0 is public and independent of e. An approximating sequence for Gamma_stat(B) suffices; attainment and common maximizing experiments are unnecessary. The upper is the usual supremum of a sum bounded by the sum of the respective suprema, using the arbitrary-start H and B bounds. Stationary experiments are a subset of arbitrary-start experiments.

For b>=0, dropping the favorable weight on CH and bounding exp(-b)<=1 yields exactly max(c0,cB x-D)<=Gamma_stat(q)<=Gamma_all(q)<=D+944x. Nonnegativity alone would not replace c0. In the small-x regime the subtracted lower may be negative, and the candidate correctly uses the independent oracle floor instead.

With T=2D/cB and c=min(c0/(1+T),cB/4), x<=T is covered by c0, and x>T gives cB x-D>=cB x/2>=cB(1+x)/4 since T>=1. D>=944 gives the displayed upper D(1+x). All constants are independent of M and b. Their very large magnitudes make this an asymptotic order statement rather than a practical threshold.

## 4. Bias-window equivalence

The uniform two-sided bound implies that a uniform robust factor is equivalent to bounded x_M. Sufficiency of the eventual upper bound b_M<=K_M-log ell_M+C follows from sigmoid(z)<=exp(z). Every omitted finite horizon has Gamma<=sqrt M regardless of the finite bias value, so finite exceptions are harmless.

Conversely, bounded positive x_M<=A and ell_M tending to infinity imply w0<=A/ell_M<=1/2 eventually. Since w0 is strictly positive for finite bias, logit inversion is legal and gives b_M-K_M<=log(2A/ell_M). No monotonic schedule is assumed. This is a necessity result only for this fixed family and does not assert that the cap with C=0 is the unique possible constant-factor constraint.

## 5. Projection, loss and quantifiers

The proof that cap=K-log ell>0 is correct: sqrt M-ell has derivative 1/(2sqrt M)-1/(M+2)>0, and at 64 it is 7-log33>0. The proposed min update is the full projection onto [0,cap] because b>=0 and -L'(b)>0 ensure the unprojected next point cannot go below zero.

PGT proves differentiability and strict negativity for every finite b using the actual clean posterior B. In either F orientation, setting d=|B-F| yields conditional derivative -(1-w)^2 d/(1-wd), strictly between -1 and 0. Finite-word averaging preserves strict negativity and continuity. Therefore every projected step before reaching the cap strictly increases b and strictly decreases clean loss, for any fixed finite positive step size. The loss is strictly decreasing throughout the interval, so its unique constrained minimizer is the cap. At the cap projection gives a fixed point.

Compactness and continuity give m_M>0 for each fixed M, so the finite-hitting proof and its conservative ceil(cap/(a m_M))+1 bound are valid. This does not require a lower bound uniform in M. For all projected iterates x<=ell/(1+ell)<1, giving Gamma_all<=CH+945. Clean excess remains nonnegative by Bayes optimality and no greater than the initial excess. The inherited entropy bound has its separate all-M estimate and explicit large-M threshold; the candidate does not misuse the large-M expression at M=64 or condition the training prior on the critical testing class.

For unconstrained descent, each fixed-M bias eventually exceeds its finite cap. PGT's limiting factor is reached by first taking iterations to infinity at that fixed M; only afterward is the family compared over horizons. No common finite iteration across all M follows. The candidate explicitly preserves this order. Projected robustness, in contrast, is simultaneous over all its iterates and horizons by its invariant interval, without any claim of a uniform hitting time.

## 6. Independent diagnostics and reproducibility

The accompanying independent script runs 26,244 exact rational pointwise mixture/absolute-loss cases, 98 exact rational conditional derivative checks, 81 finite supremum tests allowing different maximizing experiments and denominators, and nine exact factor checks including both sides of T. The artificial finite experiment arrays test algebra only and are not presented as legal statistical lower-bound witnesses.

At 120 decimal digits it checks 56 bias/horizon combinations across M=64,65,100,256,10^6,10^12,10^100,10^1000. Checks include positive cap, its exact sigmoid relation, x<1 throughout tested constrained points, the remainder estimate and the B upper simplification. Complements of extreme positive logits are evaluated as sigmoid(-z), rather than subtracting a saturated weight from one. The conditional gradient is evaluated in its stable reduced form. At M=64, cap is approximately 0.5761405436749948586 and x at the cap is approximately 0.8180662923106763063. All checks pass. These are finite diagnostics, not stochastic theorem proofs, actual population-training experiments, or finite-precision guarantees.

## 7. Scope and disposition

Accept as an exact corollary and constraint within the accepted PGT scalar model, with the candidate unchanged. B, positional G, F, K, clean prior, exact population oracle and real arithmetic are supplied. No claim about learned features, SGD/minibatches, neural advantage, practical cost, monotonic robustness, finite-bit implementation or external novelty is warranted. No author files, accepted manuscripts or external state were changed during this review.
