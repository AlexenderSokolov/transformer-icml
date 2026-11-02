# BAI002 — Arbitrary-start binary upper for an absorbing source with a regular active core

2026-11-02. Author proof candidate; independent review required. BAI001 v1 is frozen and unchanged. This is a restricted-class theorem, NOT the complete arbitrary-initialization square-root-beta extension.

## 1. Source, program, and explicit result

Fix 0<eta<=1/2, M>=64, integer kappa>=1, and dyadic Q>=16. Write z=kappa Q and delta=eta³. The binary second-order source has rows

    theta00(1)=0, theta01(1)=b,
    theta10(0)=e, theta11(0)=t,
    b,t in[eta,1-eta], e in[0,1].

Initialization is ANY pair law. The predictor T is exactly accepted SB001 v2, including its complete triple bank, empty-block uniform fallback, and ordered simplex rounding. The query is the actual endpoint Y_M and loss is actual next-symbol TV.

Let Hstat be the original accepted arbitrary-start add-one statistical scale from SB001, with Hstat<=2^(5/2)/sqrt(M+1). Then

    risk(T) <= min{1,
      2^13 Hstat + Psi(32/(M+1)) + 3/Q
      + 96/(delta z) + 3 exp(-delta M/64)
      + 32/z + 16/M}.                                  (BAI2.1)

In particular, for a constant C_eta depending ONLY on eta,

    risk(T)<=min{1,C_eta [M^(-1/2)+Q^(-1)+z^(-1)]}.       (BAI2.2)

Thus this class has no logarithmic precision surcharge at any grid or score budget. The result is uniform as e decreases to zero and does not require stationarity or a beta input.

For e>0 the unique stationary pair law is delta00, and the complete all-state certificate holds exactly for

    0<=beta<= e min(t,1-b).

Indeed the four P² entries into00 are 1,(1-b)e,e,te; all other stationary target masses are zero. In particular b=t=1/2 gives beta=e/2 and includes the genuine failure of weighted square-root-beta marginal mixing from BAI001 section6. This theorem shows why that mixing failure need not cause a precision loss.

## 2. Reflection comparison uses complete paths, not conditional IID

Use active states A=01,B=10,C=11. Define the reflected kernel

    R = [[0,1-b,b], [1,0,0], [0,t,1-t]].

The true source has an absorbing state00. If it starts in an active state and its endpoint remains active, the entire observed pair path has stayed active. For every such length-M path, its probability under the true source is its R probability multiplied by

    (1-e)^(N_B),

where N_B counts departures from B. This multiplier lies in[0,1] (interpreted by the product of transition factors, including e=1). Paths starting00 never finish active. Hence any NONNEGATIVE functional F of the complete active path, including its actual terminal query and its earlier terminal-state count, satisfies

    E_true[F 1{Y_M active}] <= E_R,nu[F],                (2.1)

where nu is the initial active sub-probability law. It can be completed to a probability law for an upper bound. No posterior or conditional independence assertion is used.

## 3. Uniform fixed-block occupation in the reflected chain

The B column of R² is

    (bt,1-b,(1-t)t),

whose entries are all at least eta². From B the next state is A with probability one, and the following state is C with probability b>=eta. Therefore, conditional on the start of ANY four-step block, the probability of a visit to B at offset2, A at offset3, or C at offset4 is at least delta=eta³, separately for each target state.

Take n=floor((M-1)/4) disjoint four-step blocks. Their selected visit times all lie in{0,...,M-1}, so the selected visits for state s are a lower bound for

    J_s=sum_(j=0)^(M-1)1{Y_j=s}.

Also n>=M/8 for M>=64. Let I_k be the selected-visit indicator for one fixed state. Conditional on the history at the beginning of its block, P(I_k=1)>=delta. Iterated conditional expectation gives

    E exp(-sum I_k) <= [1-delta(1-exp(-1))]^n.

By Markov's inequality and 1-exp(-1)-1/2>=1/8,

    P(sum I_k < delta n/2) <= exp(-delta n/8).

Consequently, uniformly over the initial law and for each active s,

    P_R(J_s<delta M/16)<=exp(-delta M/64).               (3.1)

The simultaneous good event for all three states fails with probability at most3exp(-delta M/64). On that event the ACTUAL terminal count J=J_(Y_M) is at least delta M/16. Thus for every A>0,

    E_R min(1,A/(J+2))
      <=16A/(delta M)+3exp(-delta M/64).                 (3.2)

This argument does not require stationarity, a spectral estimate, or a lower bound on the true source's stationary active masses (which are zero).

## 4. Actual predictor error on active terminal paths

SB001's deterministic bound, with its add-one empirical predictor q_hat, is

    TV(T,q_hat)<=2/(J+2)+min(1,A/(J+2))+3/Q,
    A=6M/z.                                            (4.1)

The accepted statistical result bounds E TV(q_hat,theta_(Y_M)) by2^13Hstat under arbitrary initialization. The universal terminal-occupation lemma bounds E[2/(J+2)] byPsi(32/(M+1)). Both bounds can be used on the active event by nonnegativity and then extended to the complete trajectory.

For the numerical term on the active event, use the exact path domination (2.1) and (3.2). This gives

    E_true[min(1,A/(J+2)) 1_active]
      <=96/(delta z)+3exp(-delta M/64).                 (4.2)

The source row at B differs from its reflected counterpart, but this causes no problem: (4.2) concerns only a numerical occupation functional. The statistical comparison remains with the TRUE source throughout, not with R.

## 5. Absorbing terminal paths and the actual empty-block branch

When Y_M=00, the true next-symbol law is delta0, and every previously observed transition from00 has successor0. If J>0, the selected pre-floor block is therefore(r,0), with

    r=kappa J/[M+(kappa-1)J].

If floor(Qr)>=1, SB001 normalizes this pure block to delta0 and final ordered rounding preserves it EXACTLY. Hence terminal00 loss can occur only in the all-zero floor branch (including J=0).

For J>0 that branch means Qr<1, equivalently

    [kappa(Q-1)+1]J<M,

which implies J<2M/z because Q>=2. The same strict inequality includes J=0. With w=ceil(2M/z), the universal four-state terminal-occupation bound yields

    P(Y_M=00 and all floors zero)
      <=P(J<w)<=16w/(M+1)<=32/z+16/M.                  (5.1)

The loss cap one suffices. There is no ideal zero-count side channel and no change to the implemented fallback.

Adding sections4 and5 proves (BAI2.1). To obtain (BAI2.2), use Psi(x)<=2sqrt(x), 16/M<=2/sqrt(M) for M>=64, and

    3exp(-delta M/64)<=12/[sqrt(delta) sqrt(M)],

which follows by maximizing sqrt(M)exp(-delta M/64) over positive real M. All constants depend only on eta.

## 6. Scope and unchanged costs

This is a proper special class: the active-core parameters b and t remain bounded away from both0 and1. Allowing t to vanish introduces a genuine initial waiting state inside the active region; allowing b near an endpoint can introduce additional nearly deterministic cycles. Those cases are NOT covered by a uniform constant here.

The algorithm uses neither eta nor e nor beta. All SB001 complete-bank, causal decoder-cut, finite arithmetic, all-token work, and full peak-storage accounting are unchanged. This is only a sharper analysis of that exact finite program. It does not prove the general arbitrary-start binary square-root-beta cutoff, a lower bound, or any external novelty claim.

Sources read directly: SB001 v2 deterministic error and universal occupation/statistical inequalities; BU001 v2 acceptance metadata (context only); BAI001 frozen obstruction note. The new proof is the reflected-path domination plus fixed-block actual-count estimate. Independent review and diagnostic execution are separate evidence layers, not formal verification.
