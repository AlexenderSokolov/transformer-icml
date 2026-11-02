# CB001 — A clean-safe, order-sensitive long-run veto at the critical certificate

2026-11-02. **New partial lemma; independent review pending.** This is NOT a solution of full-history unknown-budget adaptation at beta=1/M. It supplies an explicit order test with a uniform clean-risk guarantee and neutralizes the particular accepted BK001/BK002 attack supports on that curve. It does not yet bound the test under arbitrary corruption.

## 1. Statement

Use the accepted binary second-order source model: N=M+2 symbols, pair chain Y_j=(X_(j+1),X_(j+2)), j=0,...,M; an existential stationary law Pi with the certificate P^2(i,j)>=beta Pi(j) on ALL four starting states, beta>0. The actual initial distribution is arbitrary, including unsupported starts. Loss is unconditional TV at the true terminal pair. Write designated transition probabilities as

    (a,b,e,tau)=(theta00(1),theta01(1),theta10(0),theta11(0)).

For an integer 1<=L<=M, let E_00(L) be the event that the word contains a contiguous run of at least L+2 ones AND Y_M=00. Define E_11(L) by symbol exchange. Then

    E[a 1_E00(L)] <= (2/sqrt(beta))
         [1/(L+1)+2M/((L+1)(L+2))].                 (CB1)

The exchanged bound holds with tau and E_11(L). In particular, for M>=2 and L=floor(M/2), each right side is at most20/(M sqrt(beta)). If the long run is required to start at the first observed symbol, the sharper bound is

    E[a 1_{X_1...X_(L+2)=1,Y_M=00}]
       <=2/((L+1)sqrt(beta)) <=4/(M sqrt(beta)).     (CB2)

Consequently, given ANY full-word predictor A, define V_L(A) as follows:

- at terminal00, output symbol-1 probability0 when the word contains L+2 consecutive ones;
- at terminal11, output symbol-0 probability0 when the word contains L+2 consecutive zeros;
- otherwise keep A unchanged.

This is a deterministic modification of the prediction distribution, uses only the observed word and M, and is independent of k,beta and the source. For identity corruption its risk satisfies

    R_clean(V_floor(M/2)(A))
       <=R_clean(A)+min(1,40/(M sqrt(beta))).         (CB3)

Thus for every fixed c>0, at beta>=c/M it preserves an O(M^-1/2) clean guarantee with a constant allowed to depend on c. The statement is all-start, not only stationary. It makes no conditional-IID assumption.

## 2. Full support: a useful endpoint/certificate inequality

Write Pi=(y,x,x,w). Stationarity gives

    ya=xe,  w tau=xb,  y+2x+w=1.

Under full support and beta>0, a,b,e,tau are positive. The certificate entry P^2(01,10)=b tau>=beta x and stationarity imply

    b^2>=beta w.                                    (2.1)

This is NOT obtained by equating theta10(1) with b; they need not be equal. Normalization and the flows also give

    y=(1-w)e/(e+2a),
    a=tau w(e+2a)/(b(1-w)).                         (2.2)

For every horizon h>=0, stationarity and nonnegativity imply

    w P^h(11,00)<=y.

Therefore

    a P^h(11,00)<=a min(1,y/w)=min(a,tau e/b)
                         <=2 tau/sqrt(beta).        (2.3)

To prove the last inequality, if w>=1/4 then tau e/b<=tau/(sqrt(beta w))<=2tau/sqrt(beta). If w<=1/4, (2.1)-(2.2), a,e<=1 and sqrt(w)/(1-w)<=2/3 give a<=2tau/sqrt(beta). This proves (2.3) for every h, including h=0. This argument is a bound on transition probabilities, so the actual starting law need not be Pi.

## 3. A long run anywhere: charge entries, not positions

Let I_s indicate entry into a run of pair-state11 at time s: Y_s=11 and either s=0 or Y_(s-1)!=11. Restrict s to0,...,M-L. A run of L+2 observed ones contains L consecutive self-transitions at11. On E_00(L), the entry time of some such run is one of these s.

Conditional on the history through an entry s, the probability of those L self-transitions and terminal00 is

    (1-tau)^L P^(M-s-L)(11,00).

Multiply by a, use (2.3), and sum over entry times. Pathwise the number of11-run entries is at most one plus the number of11 exits. The latter has expectation tau sum_(j=0)^(M-1)P(Y_j=11)<=M tau, for every initial law. A union bound therefore gives

    E[a 1_E00(L)]
       <= (2/sqrt(beta)) tau(1+M tau)(1-tau)^L.      (3.1)

There is no factor M from summing all possible positions of the same long run, and no independence between run count and the terminal state is asserted.

Two binomial probability inequalities, valid for0<=tau<=1, are

    tau(1-tau)^L<=1/(L+1),
    tau^2(1-tau)^L<=2/((L+1)(L+2)).                 (3.2)

Indeed the corresponding expressions times L+1 and binom(L+2,2) are probabilities of exactly one and exactly two successes. Substituting (3.2) into (3.1) proves (CB1). Since L+1>=M/2 and L+2>=M/2 for L=floor(M/2), the bound is at most20/(M sqrt(beta)). For an initial long run there is only the initial entry, whose probability is at most one; omit1+M tau to obtain(CB2).

## 4. Non-full support and arbitrary unsupported starts

The accepted positive-beta support classification can also be checked directly. Stationarity gives Pi=(y,x,x,w), ya=xe and w tau=xb. If x>0, entries P^2(10,01)=ea>=beta x and P^2(01,10)=b tau>=beta x force a,b,e,tau>0 and hence y,w>0: full support. If x=0, stationary mass lies on absorbing diagonals, and both cannot have positive mass under a positive all-state certificate. Thus the only other cases are Pi=delta00 or Pi=delta11.

For Pi=delta00, a=0 and the E00 weighted loss is zero; for the exchanged E11 event, a run at00 cannot subsequently end11 because00 is absorbing. For Pi=delta11, E00 is impossible once a run at11 has occurred, and tau=0 pays the exchanged loss. This reasoning allows every actual starting pair, not just stationary support. It also covers zero transition probabilities without dividing by them.

## 5. Predictor modification and exact attack-support consequence

For binary TV loss at terminal00, replacing any estimate by0 increases its loss by at most a; analogously at11 the increase is at most tau. The two terminal events are disjoint. Their two bounds prove(CB3), also capped by the unit maximal risk increment.

**Accepted BK002 reference attack support, but advertised beta=1/M.** Every attacked input has an initial run of at least M+1-floor(M/8) ones and terminal00; both accepted reference outputs and rejected inputs preserve that whole prefix. Thus V outputs0 on EVERY attacked output, irrespective of its remaining ordering. Under the same sticky null Q_* with true terminal00 parameter r=1/(2M), the loss on each such output is exactly r. This statement concerns that legal attack support; the BK002 clean alternatives at beta=1/k^2 are not relabeled as beta=1/M sources.

**Accepted BK001 canonical attack support at beta=1/M.** BK001 uses k<=M/8 and attacked inputs x^(j)=1^(N-j)0^j with j<=M/8. Such an input has N_111=M-j. Every legal k-symbol replacement changes N_111 by at most3k. The accepted output z=Can(X) therefore has N_111(z)>=M-j-3k>=M/2; canonicalization prepends ALL these111 self-loops. Hence it begins with at least floor(M/2)+2 ones and ends00. Rejections also have a long initial run. V again outputs0 on every attacked output, with null loss r. This use of order cannot be inferred from the histogram: the veto inspects the location of the111 loops.

In either case, take A to be accepted AB003's estimator (only its clean k=0 bound is used here), and use the same sticky null with beta=1/M. Outside the attacked input set, these kernels are identity; on it V's loss is r. Thus

    R_null(V(A),this_kernel)
       <=R_clean,null(V(A))+r
       <=R_clean,null(A)+40/sqrt(M)+1/(2M).         (5.1)

This proves that these PARTICULAR ordered attack supports can be neutralized while preserving clean order. It does not prove uniform robustness of V(A) under all strict-k kernels, or any improved known-k minimax result.

## 6. Remaining constructive obstacle and next precise target

A proposed full-history candidate is AB003 plus the above veto. Its clean guarantee is proved, and the accepted counterexample supports are removed. But an arbitrary adversary can CREATE a long constant run by filling the at-most-k exceptions in a clean interval. To preserve a corruption guarantee one needs to control, for example,

    E[a 1{Y_M=00 and some interval of length floor(M/2)+2
                        contains at most k zeros}]
       <= C (M^-1/2+k/M) at beta=1/M.               (OPEN-CB)

No such bound is proved here. Even if OPEN-CB holds, it only shows that adding this veto is safe; it does not control the original AB003 estimator on all remaining corrupted words. Multiple shorter traps and localized counterfeit exits remain unhandled. A successful next estimator likely needs multiple scales or an ordering/occupation test beyond one long run. We do not advertise the candidate as an adaptive theorem.

## 7. Reading and provenance

Read accepted SC003 full proof (including its all-state support discussion), BT002 main proof and scalar completion, AB003 full proof, BK001 full proof and BK002 full proof; read each exact intake receipt. Acceptance hashes are checked separately in the diagnostic. Existing unreviewed same_beta_route_barriers and macrocycle_transport_barrier were read through their main statements/proof sections relevant to comparison. Their stationary-risk barrier and no11 MLE penalty motivated the search but are NOT premises of(CB1)-(CB3); the arbitrary-suffix, arbitrary-start long-run veto is proved above directly. No literature was consulted. Finite diagnostics and fresh LLM review are not formal or external peer review. No publication, neural/training or novelty claim is made.
