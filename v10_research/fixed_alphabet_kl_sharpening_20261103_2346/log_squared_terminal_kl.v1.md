# Full-history terminal KL: removing the extra log-log factor

Analytical note, 3 November 2026. This is a separate refinement of the fixed-alphabet terminal KL proof. It does not modify the previously frozen proof or its deliverable. No numerical experiment, simulation, training, external upload, or public repository mutation was performed. Independent review is separate from this derivation.

## Result and scope

Let A>=2 and n>=1. Observe a homogeneous second-order source X_1,...,X_{n+2} on [A], with arbitrary transition probabilities and arbitrary initial pair distribution. Deterministic rows, zero probabilities, reducibility and periodicity are allowed. Put D=A^2 and Y_i=(X_{i+1},X_{i+2}), 0<=i<=n. For every context s define

    J_s=sum_{i=0}^{n-1}1{Y_i=s},
    C_{s,b}=sum_{i=0}^{n-1}1{Y_i=s,X_{i+3}=b},
    B_s(b)=(C_{s,b}+1)/(J_s+A),
    J=J_{Y_n}.

Write p_s(b) for the true row probabilities. The loss is the forward KL divergence D_KL(p_{Y_n}||B_{Y_n}) at the actual terminal context, with natural logarithms. No independent query or suffix-averaged substitute is used.

Define

    t=max{1, log[2 A^3 n(n+1)^2]},
    c=A^4/(n+1) for arbitrary initial pairs,
    c=A^2/(n+1) for stationary initial pairs,
    U_new=c{(24At+log 2)[1+log(n+1)]
                 + A(16t+1)log(32t)}
                 + log(n+A)/(n+1)^2,
    V_new=min{log(n+A), U_new}.

Then

    E D_KL(p_{Y_n}||B_{Y_n}) <= V_new.                    (1)

In particular, for each fixed A the risk is O_A(log^2(n+2)/(n+1)), uniformly over all sources and initial pair distributions stated above. This removes the extra log-log factor from the previously reviewed O_A(log^2 n loglog n/n) bound. It does not establish O_A(log n/n), optimal alphabet dependence, or a matching lower bound for this estimator. At n=0 the elementary bound log A applies.

The same argument applies to a finite-state homogeneous chain with D contexts and A possible emitted outcomes per context, provided the outcome and next-state mechanism admits the standard independent row-stack representation. For an ordinary D-state chain, take A=D. The present second-order source has D=A^2.

## 1. Fixed-target terminal occupation

Fix a target state s and integer w>=1. For a chain started at z let

    b_m^s(z)=P_z(Y_m=s, sum_{i=0}^{m-1}1{Y_i=s}<w),
    B_m^s=max_z b_m^s(z).

For m>=ell, having fewer than w full-history copies of s implies having fewer than w copies in the last ell departures. Conditioning on Y_{m-ell} and using homogeneity yields B_m^s<=B_ell^s. On a deterministic path only the first w occurrences of s can satisfy this flag, so sum_{m=0}^n b_m^s(z)<=w for every z. Consequently

    (n+1)B_n^s <= sum_{m=0}^n B_m^s
                <= sum_z sum_{m=0}^n b_m^s(z) <= Dw.

Taking any mixture over the initial state proves

    P(Y_n=s,J_s<w) <= r w,
    r=D/(n+1).                                           (2)

Under stationary initialization one instead has r=1/(n+1). Indeed, among r'=n,...,2n at most w times can satisfy Y_{r'}=s and have fewer than w copies of s in their preceding n positions: if w+1 were marked, the last marked time has all w earlier marks inside that window. Stationarity makes each marked event have the probability on the left of (2). This proves the improved bound.

In both cases c=Dr. Summing (2) over target states gives P(J<w)<=cw. Summation by parts then gives

    E[1/(J+1)]
      =1/(n+1)+sum_{k=0}^{n-1}P(J<=k)/[(k+1)(k+2)]
      <=1/(n+1)+c sum_{k=0}^{n-1}1/(k+2)
      <=c[1+log(n+1)].                                    (3)

The per-target form (2), rather than only its sum, is essential below because the true row probabilities vary with the terminal state.

## 2. One simultaneous deterministic-prefix event

Generate n independent categorical entries for each of the A^2 rows, independently across rows and independently of the initial pair. At a departure from s consume its next unused entry. The resulting source has exactly the required transition law. Let K_{s,b,j} count symbol b in the first j entries of row s. Then C_{s,b}=K_{s,b,J_s} pathwise.

Bernstein's inequality and a union bound over A^2 rows, A symbols and n deterministic prefix lengths give an event G with

    |K_{s,b,j}-jp_s(b)| <= sqrt(2jp_s(b)t)+2t/3             (4)

for all those prefixes, and

    P(G^c)<=2A^3 n exp(-t)<=(n+1)^(-2).                    (5)

At j=0 inequality (4) is deterministic. No binomial or independence assertion is made after conditioning on J_s, on Y_n, or on the observed path. Evaluation at the selected row and selected prefix uses only simultaneous pathwise validity.

## 3. A scale choice that removes smoothing dependence from t

Fix any row and deterministic prefix, and abbreviate j>=0, p_b=p_s(b), k_b=K_{s,b,j}, q_b=(k_b+1)/(j+A). Set

    h(x,a)=x log(x/a)-x+a,
    x_b=(j+1)p_b, a_b=k_b+1, z_b=jp_b.

Use 0 log 0=0. Since sum_b x_b=j+1 and sum_b a_b=j+A,

    sum_b h(x_b,a_b)
       =(j+1)D_KL(p||q)+(A-1)
                    -(j+1)log[1+(A-1)/(j+1)]
       >=(j+1)D_KL(p||q),                                 (6)

by log(1+u)<=u. Thus this rescaling, unlike x_b=(j+A)p_b, gives only the displacement p_b-1, whose absolute value is at most one. It needs t>=1, not t>=A.

## 4. Split by the true coordinate mean

For one coordinate suppress b. Under (4), write delta=k-z. Then

    delta^2<=4zt+8t^2/9,
    (x-a)^2<=2delta^2+2<=8zt+(34/9)t^2.                  (7)

Here x=z+p, a=k+1, and t>=1. The elementary inequality h(x,a)<=(x-a)^2/a holds for x>=0,a>0, including x=0 by continuity.

If z>=16t, then

    a>=z-sqrt(2zt)-2t/3 >=z/2,

because sqrt(2t/z)+2t/(3z)<=1/sqrt(8)+1/24<1/2. Hence

    h(x,a)<=2[8+34/144]t<17t.                             (8)

If z<16t, then

    a<=16t+sqrt(32)t+2t/3+1<=24t.

Since a>=1, h(x,a)<=x log_+x+a. The binary entropy inequality gives

    (z+p)log_+(z+p)<=z log_+(2z)+p log_+(2p),             (9)

with zero terms interpreted as zero. For z+p>1 this follows from
(z+p)log(z+p)<=z log(2z)+p log(2p), and replacing negative logarithms by zero only increases the right side. For z+p<=1 it is immediate. Thus

    h(x,a)<=24t+z log_+(2z)+p log_+(2p).                  (10)

Combine (8) and (10), sum the coordinates, and use

    sum_b p_b log_+(2p_b)<=log 2.

Equations (6)-(10) yield the pointwise inequality

    D_KL(p||q)
      <=(24At+log 2)/(j+1)
        +sum_b p_b log_+(2jp_b)1{jp_b<16t}.               (11)

The factor jp_b/(j+1) from (6) was upper bounded by p_b. The argument also covers j=0, p_b=0 and p_b=1.

Unlike a uniform bound of order t log t/(j+A), (11) charges the log t factor only where that particular true coordinate mean is small.

## 5. Integrate the small-mean term before summing the rows

Fix s,b and put p=p_s(b), T=16t. If p=0 the corresponding term is zero. If p>0, the log is bounded above by log(2T) on {J_s p<T}. With w=ceil(T/p), this event implies J_s<w, including the case T/p is an integer. Equation (2) therefore gives

    E[1{Y_n=s}p log_+(2J_s p)1{J_s p<T}]
      <=p log(2T) P(Y_n=s,J_s<T/p)
      <=p log(2T) r ceil(T/p)
      <=r(T+p)log(2T)
      <=r(T+1)log(2T).                                   (12)

The use of (2) remains valid when the ceiling exceeds n, because its upper bound need not be below one. Summing (12) over the D rows and A symbols gives at most

    c A(16t+1)log(32t).                                  (13)

This sum does not extract a random terminal-row probability from an expectation. Each p in (12) is fixed first; only then are rows summed.

On G, apply (11) to the selected terminal row and count. Use (3), (12)-(13) without conditioning on G. On every path, q_b>=1/(j+A), so D_KL(p||q)<=log(j+A)<=log(n+A). The complement G^c therefore costs at most log(n+A)/(n+1)^2. This proves (1).

## 6. Transfer to the reviewed five-block output

The five-block exact-real output construction in the prior fixed-alphabet note is unchanged. Its proved pathwise bounds, with L=n+2+A, are

    TV(R,B)<=min{1,(44A+1)/L},
    R_b>=1/[1+(A-1)L]>=1/(AL).

Its entropy-variational KL transfer consequently gives

    E D_KL(p_{Y_n}||R)
       <=2V_new+2A(44A+1)^2/L.                            (14)

The deterministic cap log[1+(A-1)L] may also be taken. Thus the same output has O_A(log^2 n/n) statistical risk and an O_A(1/n) implementation penalty. No additional architecture, training, finite-precision, or computational claim is made here.

## 7. What this does not establish

The remaining harmonic occupation factor and the logarithmic confidence level give log^2 n/n. Merely replacing the confidence event by an exponential-tail self-normalized bound and separately using the occupation envelope does not justify log n/n. A simple abstract counterexample to that inference is J uniform on {1,...,n} and W=log(n/J):

    P(J<w)<=w/n,
    P(W>u)<=exp(-u), u>=0,
    E[W/J]=(1/n)sum_{j=1}^n log(n/j)/j
           =(log n)^2/(2n)+O(log n/n).

This is a barrier for arguments using only those two marginal bounds. It is not a Markov-source lower bound and does not show the present log^2 rate is optimal. Achieving O_A(log n/n) would require additional control of how the row-estimation error and terminal occupation depend on each other, or a different argument.

Han, Jana and Wu, "Optimal prediction of Markov chains with and without spectral gap," IEEE Transactions on Information Theory 69(6), 2023, 3920-3959, Remark 1, explicitly distinguish suffix-averaged add-one from full-history add-one and leave the latter's optimality open in their stated setting. The present O_A(log^2 n/n) result does not resolve that question, and does not transfer their stationary minimax theorem to arbitrary initialization. It also does not claim that their 2023 question remains unresolved in all later literature. Primary publication: https://doi.org/10.1109/TIT.2023.3239508 ; author preprint: https://arxiv.org/abs/2106.13947 . The relevant text was checked in the locally available published PDF.

## Sources and provenance

- Prior fixed-alphabet proof: ../fixed_alphabet_kl_upgrade_20261103_2300/fixed_alphabet_terminal_kl.v1.md, particularly Sections 2-4 and 8. The prior frozen files are not overwritten.
- Published HJW PDF inspected locally: [preparation path omitted; see the DOI and source identity] from this note's directory, or [preparation path omitted; see the DOI and source identity] from the workspace root.
- The fixed-target occupation bound is the target-specific version of the prior shift-and-charge argument. The improvement arises by splitting true means before occupation averaging. The j+1 rescaling was suggested during independent analytical discussion and must be included in review of this exact file.

No numerical work supplies any step of this proof. This note is an estimator-specific upper-bound refinement, not a claim of literature priority or formal verification.
