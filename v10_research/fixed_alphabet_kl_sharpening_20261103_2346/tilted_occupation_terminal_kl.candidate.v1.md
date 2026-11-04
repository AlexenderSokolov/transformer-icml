# Candidate: terminal KL through row-tilted occupation bounds

Analytical candidate, 3 November 2026. This file must receive independent exact-file review before acceptance. It preserves all previous frozen notes. No numerical experiment, simulation, training, external upload or public repository mutation was performed. No literature-priority claim is made.

## 1. Statement

Let A>=2, n>=1, and observe X_1,...,X_{n+2} from a homogeneous second-order source on [A]. All transition rows and the initial pair distribution are arbitrary. Zero probabilities, deterministic rows, reducibility and periodicity are allowed. Define D=A^2, Y_i=(X_{i+1},X_{i+2}) for 0<=i<=n, and

    J_s=sum_{i=0}^{n-1}1{Y_i=s},
    C_{s,b}=sum_{i=0}^{n-1}1{Y_i=s,X_{i+3}=b},
    B_s(b)=(C_{s,b}+1)/(J_s+A),
    J=J_{Y_n}.

Write p_s(b) for the true row probabilities, use natural logarithms, and evaluate forward KL at the actual terminal context. Let

    K_n=1+floor(log_2 n),
    W_{A,n}=A^4/(n+1) [log A+1536 A K_n],
    V_{A,n}=min{log(n+A), W_{A,n}}.

The candidate theorem is

    E D_KL(p_{Y_n}||B_{Y_n}) <= V_{A,n}.                 (1)

Thus the actual full-history add-one predictor has O_A(log(n+2)/(n+1)) risk for each fixed A, uniformly over arbitrary initial pair distributions. The result also applies to stationary initial pairs, but it does not retain the better stationary alphabet factor of the earlier log-squared bound. For n=0 use log A.

The leading alphabet factor here is A^5, not the A^3 complexity in sharp stationary higher-order minimax results. This candidate does not assert optimal growing-alphabet dependence, a new estimator, or a solution of every parameter regime of the full-history add-one question in prior work.

## 2. A kernel-uniform, fixed-target occupation bound

For every homogeneous Markov chain on D states, every initial distribution mu, every target state s, and integer w>=1,

    P_mu(Y_n=s,J_s<w) <= D w/(n+1).                       (2)

For clarity, the bound is uniform over the transition kernel; this is crucial when it is used for an altered kernel below.

Proof: For a chain started at z define

    b_m^s(z)=P_z(Y_m=s, sum_{i=0}^{m-1}1{Y_i=s}<w),
    B_m^s=max_z b_m^s(z).

If m>=ell, fewer than w earlier copies in the full path implies fewer than w copies in its last ell departures. Conditioning at time m-ell gives B_m^s<=B_ell^s. On each deterministic path only the first w occurrences of s satisfy the flag, so sum_{m=0}^n b_m^s(z)<=w. Therefore

    (n+1)B_n^s <=sum_{m=0}^n B_m^s
                <=sum_z sum_{m=0}^n b_m^s(z)<=Dw.

Mixture over the starting state proves (2). Put r=D/(n+1). In particular, for any integer m>=1,

    P_mu(Y_n=s, m<=J_s<2m)<=2rm.                          (3)

No stationarity, irreducibility, reversibility or mixing assumption is used.

## 3. Change one row, rather than conditioning a stack

Fix s,b and p=p_s(b) in (0,1). For any q in (0,1), define an alternative homogeneous second-order source Q with the same initial pair distribution and all rows unchanged except s. In row s let

    q_s(b)=q,
    q_s(a)=p_s(a)(1-q)/(1-p), a!=b.                       (4)

Thus the alternative remains in the same D-state pair-chain class. Zero probabilities among the other symbols remain zero. The original law P and Q have the same path support. For any observed path of positive probability, put j=J_s and k=C_{s,b}. The exact path-probability ratio is

    P(path)/Q(path)
       =(p/q)^k [(1-p)/(1-q)]^(j-k).                     (5)

The initial factor cancels, all unmodified rows cancel, and each departure from s contributes one of the two displayed factors. There is no extra factor from Y_n: the probability of the observed path already includes the terminal state and all n observed transitions.

Let d(q||p) denote binary forward KL. If q>p and k/j>=q, or q<p and k/j<=q, then

    log[P(path)/Q(path)]
       =-j d(q||p)
         -(k-jq)log[q(1-p)/(p(1-q))]
       <=-j d(q||p).                                    (6)

Consequently, for E_m={Y_n=s,m<=J_s<2m},

    P(E_m, C_{s,b}/J_s>=q)
       <=2rm exp[-m d(q||p)], q>p,
    P(E_m, C_{s,b}/J_s<=q)
       <=2rm exp[-m d(q||p)], q<p.                       (7)

To obtain (7), sum (6) over the indicated paths and apply (3) under the altered law Q, not under P. The initial distribution remains the same but is not assumed stationary for Q. This use of the arbitrary-start bound is intentional.

## 4. A joint occupation-times-deviation tail

For t>=1 let

    delta=sqrt(2pt/m)+2t/(3m).

For either q=p+delta or q=p-delta lying in (0,1), the Bernstein binary-KL bound gives

    d(q||p)>=delta^2/[2(p+delta/3)]>=t/m.                 (8)

Here is a direct justification of the first inequality. For Z a centered Bernoulli(p) variable, |Z|<=1 and E Z^2<=p. Expansion of the exponential gives, for either sign and 0<=lambda<3,

    log E exp(+-lambda Z)
       <=p lambda^2/[2(1-lambda/3)].

Use the variational formula for binary KL and take lambda=delta/(p+delta/3)<3. This gives the first inequality in (8). For the second, put v=t/m and expand delta=sqrt(2pv)+2v/3; then delta^2>=2v(p+delta/3).

On m<=J_s<2m,

    J_s delta <=sqrt(4J_s p t)+4t/3.

Thus (7)-(8), with a union over the two directions, give

    P(E_m, |C_{s,b}-J_s p|>sqrt(4J_s p t)+4t/3)
       <=4rm exp(-t).                                   (9)

If p+delta>=1, the corresponding strict upper-tail event is impossible; similarly if p-delta<=0 for the lower tail. Such directions do not require an endpoint tilt. If p=0 or p=1, the row count is deterministic given J_s, so the deviation event is empty and (9) holds directly.

Equation (9) does not assert that C_{s,b} is binomial after conditioning on J_s or on the terminal state. It obtains the product factor by a change of the actual transition kernel. A different deterministic alternative kernel may be used for each threshold t; tail integration below requires separate probability bounds, not one common simultaneous alternative law.

## 5. Scalar forward-KL control

For x>=0 and a>0 set

    h(x,a)=x log(x/a)-x+a,

with 0 log 0=0. Suppose j>=0, p in [0,1], 0<=k<=j, u>=1, and

    |k-jp|<=sqrt(2jp u)+2u/3.                             (10)

Then

    h((j+1)p,k+1)<=48u(1+log u).                         (11)

Proof: Let z=jp, a=k+1, x=z+p. From sqrt(2zu)<=z/2+u,

    z<=2k+10u/3,
    (k-z)^2<=4zu+8u^2/9<=8ku+128u^2/9.

Since |p-1|<=1 and u>=1,

    (x-a)^2<=16ku+31u^2,
    x<=2a+10u/3.

The inequality h(x,a)<=(x-a)^2/a shows h<=47u when a>=u. If a<u then x<6u and a>=1, giving

    h(x,a)<=x log_+x+a<=6u log(6u)+u
             <=48u(1+log u).

This proves (11), including p=0, p=1 and j=0.

For a full A-symbol row with counts summing to j, let q_b=(k_b+1)/(j+A). The exact scaling identity is

    sum_b h((j+1)p_b,k_b+1)
       =(j+1)D_KL(p||q)+(A-1)
           -(j+1)log[1+(A-1)/(j+1)]
       >=(j+1)D_KL(p||q),                                (12)

where the last step uses log(1+v)<=v. Thus no A-dependent lower bound on u is needed.

## 6. Integrate one coordinate on one dyadic band

Fix s,b,m. Define the nonnegative random variable

    Z=h((J_s+1)p_s(b),C_{s,b}+1)/(J_s+1).

Take u=2t in (10). The threshold in (10) becomes exactly the one in (9). By (11), for t>=1 and on E_m outside that deviation event,

    Z<=96t[1+log(2t)]/(J_s+1)
       <=192t(1+log t)/m=:f_m(t).                        (13)

The second inequality uses 1+log 2<=2 and J_s+1>=m. Therefore

    P(E_m,Z>f_m(t))<=4rm exp(-t), t>=1.                  (14)

Since f_m is strictly increasing, layer-cake integration and (3) give

    E[1{E_m}Z]
       <=f_m(1)P(E_m)
            +integral_1^infty f_m'(t)P(E_m,Z>f_m(t))dt
       <=384r+768r integral_1^infty(2+log t)exp(-t)dt
       <=384r+2304r/e
       <1536r.                                          (15)

For the penultimate step use log t<=t-1, so the integral is at most integral_1^infty(1+t)e^(-t)dt=3/e. The final inequality uses e>2. No union over coordinates is used in (15); nonnegative scalar expectations are summed only after integration.

## 7. Sum bands, rows and symbols

The disjoint dyadic bands m=1,2,4,...,2^floor(log_2 n) cover J_s=1,...,n. For a selected terminal row with positive count, (12) bounds KL by the sum of the A nonnegative scalar Z terms. Summing (15) over K_n bands, D target rows and A symbols yields

    E[1{J>=1}D_KL(p_{Y_n}||B_{Y_n})]
       <=1536 D A K_n r
       =1536 D^2 A K_n/(n+1).                           (16)

On J=0 the add-one estimator is uniform, so its loss is at most log A. Equation (2) with w=1, summed over s, gives P(J=0)<=D^2/(n+1). Thus

    E[1{J=0}D_KL(p_{Y_n}||B_{Y_n})]
       <=D^2 log A/(n+1).                               (17)

Combine (16)-(17), substitute D=A^2, and use the deterministic pathwise cap log(n+A). This proves the candidate bound (1).

## 8. Transfer to the existing five-block output

The independently reviewed five-block exact-real construction is unchanged. Its pathwise approximation and support bounds, for L=n+2+A, are

    TV(R,B)<=min{1,(44A+1)/L},
    R_b>=1/[1+(A-1)L]>=1/(AL).

The existing entropy-variational transfer consequently gives

    E D_KL(p_{Y_n}||R)
       <=2V_{A,n}+2A(44A+1)^2/L.                         (18)

The deterministic cap log[1+(A-1)L] may also be applied. If (1) is accepted after independent review, this is an O_A(log n/n) statistical rate with an O_A(1/n) exact-real output-approximation penalty. No finite-precision theorem or architecture change is asserted.

## 9. Relation to the log-squared proof and prior work

The separate log-squared note correctly shows that a terminal occupation marginal and a self-normalized error marginal alone do not imply log n/n: their adverse correlation can cost a further logarithm. The present argument does not use that invalid inference. It applies the occupation bound under an explicitly altered transition kernel and obtains the joint probability bound (9).

For a general D-state ordinary chain with A=D possible next states, the proof gives O(D^3 log n/n) for fixed D. This is not the optimal D^2 dependence in the stationary minimax theorem of Han, Jana and Wu. Their Remark 1 asks about optimality of usual full-history add-one in the setting of their stated theorem; the present candidate must not be described as settling the complete growing-state question. In the stationary binary first-order case the optimal minimax rate is different, so this candidate also does not assert minimax optimality there.

For fixed A and order two, the candidate upper rate matches the order in n of the stationary minimax lower bound quoted in the existing fixed-alphabet research. Matching the rate in n does not imply optimal alphabet dependence, and no priority assertion is made. Literature status after the cited 2023 paper has not been exhaustively established here.

## Source bindings

- Prior reviewed fixed-alphabet proof and output construction: ../fixed_alphabet_kl_upgrade_20261103_2300/fixed_alphabet_terminal_kl.v1.md.
- Separately derived log-squared refinement: log_squared_terminal_kl.v1.md in this directory.
- Han, Jana and Wu, "Optimal prediction of Markov chains with and without spectral gap," IEEE Transactions on Information Theory 69(6), 2023, 3920-3959, Remark 1 and higher-order results. DOI: https://doi.org/10.1109/TIT.2023.3239508 ; author preprint: https://arxiv.org/abs/2106.13947 . Relevant published text was inspected in the locally available PDF at [preparation path omitted; see the DOI and source identity] from the workspace root.

This file is a review candidate, not an accepted theorem until its exact contents pass independent analytical scrutiny. The use of arbitrary-start occupation under the tilted kernel, rather than stationarity under that kernel, is an essential part of the argument.
