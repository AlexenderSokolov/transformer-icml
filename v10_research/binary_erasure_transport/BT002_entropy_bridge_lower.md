# BT002 — binary corruption lower via entropy-to-bridge transport

2026-11-02. POST-STAGE7 author candidate. Independent full review pending. BT001 and frozen/accepted sources unchanged. No novelty or formal-verification claim.

## 1. Result and experiment

For M>=64, 0<=k<=M integers, beta∈[0,1], let e=max(sqrt(beta),1/M), s0=M^-1/2 and, for k>=1,

    F=(k/M)[1+ln(1+1/(e k))];   F=0 for k=0.

In SC001/SC002's full-observation corruption experiment, restricted to binary second-order sources satisfying the all-pair-state certificate P²>=beta Pi and initialized at their own hidden stationary Pi, the explicit absolute constant 2^-54 gives

    R_stat >= 2^-54 max{s0,F}.                              (BT2)

The adversary changes at most k of the first M symbols, preserves both final symbols, and has no input unknown source parameter or stationary law. Prediction sees the full corrupted word but not edit mask or attack seed, and targets the true next law at the true preserved final pair. Decoder randomness is allowed. The logarithmic lower below uses ONE explicit-in-existence source-independent kernel and ONE uniform prior for all suffix lengths. Computation of finite optimal transport tables is unrestricted. The separate IID floors may use separate witness families, as is valid for a maximum of minimax lower bounds.

Together with SC003's separately reviewed upper, this would close the fixed-binary full-history corruption frontier. This note proves the lower, subject to fresh review; it does NOT prove BT001's stronger interior constant-step transport conjecture.

## 2. Finite transportation consequence of bounded Markov coupling

Reference pair chain on A=01,B=10,C=11:

    R_p(A,B)=1-p, R_p(A,C)=p, R_p(B,A)=R_p(C,B)=1.

Observe t emitted bits from a fixed starting pair. For p∈[1/8,7/8], R_p^5(u,A)>=1/64 for every u. Indeed its A-column is (2p(1-p),(1-p)^2,p). Thus two copies with the SAME p can couple in blocks of five, meeting at the block boundary with probability at least1/64, and thereafter agreeing. Fill each block by its conditional bridge to the coupled endpoint. The expected number of emitted-bit discrepancies is <=5 sum_(r>=0)(63/64)^r=320, uniformly over initial states and horizon.

For every Hamming-1-Lipschitz real function f of the t emitted bits, reveal the transitions in order. Conditional continuation expectations after any two possible next states differ by at most321 (one current-bit discrepancy plus320 later). Use the safe constant L=326. The Doob increment conditional range is at most L, so conditional Hoeffding's lemma and iteration give

    log E_nu exp(lambda(f-E_nu f)) <= t L² lambda²/8.    (1)

Here nu=nu_(p,t) is the reference path law from A, and f is defined on the full bit cube. The conclusion also holds for functions on its support by a Hamming-Lipschitz extension.

For any mu absolutely continuous with respect to nu, the finite entropy inequality yields

    E_mu f-E_nu f <= KL(mu||nu)/lambda+t L² lambda/8.

It follows by optimization that the right side is <=L sqrt(t KL/2). Applying the finite Kantorovich–Rubinstein LP duality (Hamming metric on a finite set) gives

    W1(mu,nu) <= L sqrt(t KL(mu||nu)/2).               (2)

For completeness the entropy inequality follows by setting Q(x)=nu(x)e^(lambda f(x))/Z and using KL(mu||Q)>=0. The finite transport LP dual is max of E_mu f-E_nu f over 1-Lipschitz f for a metric cost; this also applies with zero-probability ambient words via extension.

If p,q∈[1/8,7/8], interpolate one transition kernel at a time between their t-step laws. A single changed transition differs with probability at most|p-q| and then the remaining common-q continuation costs at most320 more disagreements. The preceding segment has the same law in both compared hybrid chains. Therefore

    W1(nu_(p,t),nu_(q,t)) <= L t |p-q|.               (3)

No IID claim for suffix bits is used.

## 3. Microcanonical laws to public canonical bridges

Returns to A concatenate S=01 and Lc=101. At an exact return horizon t, counts satisfy2s+3l=t; m=s+l. Conditional on these counts, emitted words are uniform over the binomial(m,l) cycle orders; denote this p-independent law by U_(s,l).

If p_hat=l/m∈[1/8,7/8], the event consisting of these counts and return at t has probability

    binom(m,l) p_hat^l(1-p_hat)^s >=1/(m+1)>=1/(t+1).  (4)

Indeed l is a binomial(m,l/m) mode, so its mass is at least the reciprocal of the m+1 support points. This event has exactly the displayed probability because any ordering of those m cycles finishes at t; prefix-free decoding makes the correspondence one-to-one. Hence

    KL(U_(s,l)||nu_(p_hat,t)) <=ln(t+1).

Let nu^A_(q,t) denote nu_(q,t) conditional on terminal pair A. For t>=5 its conditioning probability is at least1/64, so

    KL(nu^A_(q,t)||nu_(q,t)) <=ln64.

Triangle inequality, (2), (3), and symmetry of W1 imply

 W1(U_(s,l),nu^A_(q,t))
 <= L sqrt(t/2)[sqrt(ln(t+1))+sqrt(ln64)] +Lt|p_hat-q|
 <=1024 sqrt(t ln(t+1))+326t|p_hat-q|.                (5)

The final inequality uses t>=1, ln64/ln2=6, and 326(1+sqrt6)/sqrt2<1024. Both endpoint distributions in (5) have final two bits01. The intermediate unconditioned law is used only for a metric triangle inequality, not as the eventual corrupted output.

## 4. One source-independent strict-budget kernel

Assume k>=1. For each t>=4096 define a rational grid of [1/8,7/8] by n_t=max{1,ceil(3·2^18 t/k)} equal subintervals. The spacing is at most Delta_t=k/(2^20 t), and the number of grid points is at most2+2^20t/k. For p_hat in that interval choose the closest grid point q, with deterministic tie breaking; the weaker bound |p_hat-q|<=Delta_t suffices.

Put c_E=2^-44. At horizons

    4096<=t<=c_E k²/ln(k+2),                            (6)

t<=k², so ln(t+1)<=2ln(k+2). Equation (5) is at most

    [1024 sqrt(2c_E)+326/2^20]k < k/1024.              (7)

For each eligible public count pair (s,l), choose a minimum-cost coupling from U_(s,l) to nu^A_(q,t). All probabilities are rational (q and p_hat are rational; bridge conditioning is finite), so a rational optimal coupling exists as a finite transportation LP vertex. Choose one deterministically, for example by lexicographic tie breaking over vertices. The table is a function only of public t,k,counts and q, never of the true p.

Define the kernel on every binary word of length N=M+2. If it has N-j>=2 initial zeros followed by a first1 and a suffix following the deterministic-C reference, ending in pair A, let t=j-1. Its cycle counts are uniquely readable. If (6) holds and p_hat∈[1/8,7/8], sample Y from the chosen coupling conditional on the observed cycle word X. Replace that suffix by Y only when d_H(X,Y)<=k; otherwise output the original word. In every other case output the original word. The prefix and initial1 are unchanged; both output cycle words end01, so the actual final pair is preserved. At most k editable bits are changed. This is one offline randomized history kernel on all words, valid simultaneously for all p, horizons, beta and starts. It can in fact ignore beta. Its sampled attack seed is hidden.

Conditional on an eligible microcanonical input class, (7) and Markov's inequality give truncation failure probability <=1/1024.

## 5. Uniform success mass and finite-message lower

Take ONE prior p uniform on I=[1/4,3/4]. Reference starts at A. For true p∈I, terminal A has probability at least1/16 at every t>=5, using the same R^5 A-column.

On terminal A, m∈[ceil(t/3),floor(t/2)] and its first m cycle choices are IID Bernoulli(p) before the event is imposed. For every fixed such m, Hoeffding bounds the probability l/m outside[1/8,7/8] by2exp(-m/32). A union over at most t values gives failure probability <=2t exp(-t/96). For t>=4096 this is <=1/128 and is decreasing. Therefore eligible endpoint-A input mass is at least1/16-1/128>=1/32, uniformly in p. No conditional-IID assertion after fixing t or the endpoint is needed.

For each fixed t satisfying (6), construct an auxiliary untruncated observation: on eligible count classes, use the sampled Y bridge; on all other paths use a fixed public length-t word ending01 (such a cycle word exists at every t>=2). Prepend the original public zero prefix and initial1. This auxiliary observation factors through the chosen q label, or one extra bad label, followed by a p-independent channel. Thus it has at most

    D_t=3+2^20t/k <=2^22(1+t/k)                       (8)

finite labels. This does NOT assert that its output word takes only D_t values.

A coupling between the auxiliary and actual corrupted observations agrees on eligible-and-budget-success paths. That event has probability at least1/32-1/1024>=1/64 for every p. On it, the actual preserved endpoint is A and the target Bernoulli parameter is p.

To justify independent auxiliary randomization despite truncation, first sample original counts/eligibility under their p-dependent law, then generate Y using a uniform seed U independent of p and its q-dependent bridge law; finally sample original X through the p-independent reverse disintegration of the selected microcanonical coupling. This reproduces the joint law and its budget-success event. The extra bad label uses its fixed word. The decoder's own independent randomness is fixed together with U. There are now at most D_t candidate predicted probabilities of symbol1.

Set rho=1/(512D_t). The union of radius-rho intervals around those D_t scalars has uniform-prior probability at most2D_t rho/|I|=1/128. This bound is independent of the stochastic mechanism selecting labels. Subtracting it from success mass>=1/64 gives probability>=1/128 that actual and auxiliary outputs agree at terminal A and the prediction error is at least rho. Thus

    E_prior,nu loss·1_terminalA >=1/(65536 D_t)
       >=2^-38 /(1+t/k).                             (9)

Average decoder/auxiliary seeds. Importantly, a constant failure probability was subtracted from a probability bound, not directly from a vanishing risk bound. The posterior after endpoint conditioning is never called uniform.

## 6. Stationary witness and unconditional harmonic sum

Use BT001's reviewed modified witness. For beta<=1/256 let a=1/(2M), e=max(sqrt(beta),1/M), and

    theta(1)=(a,p,1-e,e),
    Pi=x(e/a,1,1,p/(1-e)), x=(e/a+2+p/(1-e))^-1.

BT001 §3 proves stationarity, Pi_W>=1/4, and the all-state P²>=beta Pi certificate. Its reference path domination on the disjoint rare-entry events E_j is

 actual path mass >=(32M)^-1 times nu_(p,j-1) path mass

for j<=1/(4e). This source and initialization are the same for every suffix length. Conditional event probabilities may depend on p, so use pointwise domination with the SAME prior, not a false conditional-uniform prior.

Set

    J=floor min{1/(8e), c_E k²/ln(k+2)}.

For 4096<=t<=J, j=t+1<=1/(4e), since e<=1/16, and j<=M/8+1<=M/4. Thus all positions are within the observed word and every previous argument applies. Sum (9), discarding all other nonnegative losses:

    R_stat >= (2^-43/M) sum_(t=4096)^J (1+t/k)^-1,    (10)

with an empty sum interpreted as zero. This is a full-history lower with one common kernel, not an encoder-information limitation.

## 7. Floors and all-regime completion

Two separate binary IID witnesses satisfy every beta certificate because their pair chain has P²=1Pi.

**Clean floor.** Use Bernoulli parameters p±=1/2±1/(16sqrt(M+2)), stationary IID initialization, and identity corruption. Product KL is at most5/64 using Bernoulli KL<=difference²/[q(1-q)], and hence total variation is below1/4 by Pinsker. The ordinary two-point absolute-error testing bound yields risk>=1/(256sqrt M).

**Corruption floor.** Under one uniform prior p∈[1/4,3/4], apply SC001's exact uniform-one-deletion erasure to the first M IID bits with bin size b=k+1; protect the last two bits. Its complete auxiliary message has at most4(floor(M/b)+1) labels, and the output arrangement conditional on that label is p-independent. The finite-message uniform-prior absolute-error lemma gives risk>=1/[32(1+M/b)]>=k/(64M) for1<=k<=M.

The exact scalar completion is `BT002_scalar_completion.md`, (SCALAR4), with C=8, c=c_E and j0=4096. Writing T for the sum in (10) divided by M, it gives max{s0,F}<=1830 max{s0,k/M,T}. The separate three lower bounds yield R_stat>=2^-43 max{s0,k/M,T}; since1830<2048, (BT2) follows. Empty sums, bounded k and floor endpoints are included in that scalar lemma. For beta>1/256, F<=k/M+16/M<=k/M+2/sqrt M, so the floors give max{s0,F}<=576 R_stat and hence (BT2) again. For k=0 the clean floor is the statement.

## 8. Scope and remaining checks

This weaker O(sqrt(t log t)+tDelta) transport does not contradict the BT001 boundary cost Theta(t), because the canonical p_hat must stay in a fixed interior interval; nor does it prove the stronger interior neighboring-count O(1) conjecture. The t<=c_E k²/log(k+2) restriction is genuine for this route; scalar completion, not an unproved extension of transport, removes it from the final rate.

Dependencies: BT001 reviewed obstruction/witness; SC001 exact erasure and finite-message lemma. SC003 is needed only to combine this lower with its upper, not to prove this note's lower. All constructions are offline and may have enormous computation; no efficient adversarial sampler, causal attacker, public attack seed, visible mask, or edited-terminal theorem is asserted.

Dependency acceptance supplied by root: BT001 scoped receipt `intake/BT001_acceptance.json` at09:06:56 UTC (proof SHA2562671d9a079833a82b6c02d87052ae86dd16c321fae8a9fda9848cf74aead8040); SC003 upper/floors accepted09:00:43. This is provenance for dependencies, not acceptance of BT002.
