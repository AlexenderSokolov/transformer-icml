# BAI004 — Full-support initial-delay reductions (intermediate lemmas)

2026-11-02. New research candidate; independent review pending. These are intermediate occupation results, NOT a complete arbitrary-start precision theorem. Accepted BAI003 is untouched.

Use binary states W=00,A=01,B=10,C=11 and positive row parameters a=thetaW(1), b=thetaA(1), e=thetaB(0), t=thetaC(0), all in(0,1). Let q=(a,b,e,t), J_s=sum_(j=0)^(M-1)1{Y_j=s}, and V_s=1{Y_M=s}min(q_s,A0/(J_s+2)), A0>0.

## 1. General initial-equals-target reciprocal lemma

For any d-state homogeneous chain, any target s, and n>=1,

    E_s[1{Y_n=s}/J_s]<=d/n.                            (1.1)

On the event in question J_s>=1. Let F_s(z) be the pgf of the first positive return to s, allowing a defective law. Schur complementation of I-zP gives

    1-F_s(z)=det(I-zP)/det(I-zP_(-s)).

All calculations are formal power series near zero. Therefore

 [z^n](-log(1-F_s(z)))
   =[tr(P^n)-tr(P_(-s)^n)]/n<=d/n.

The same coefficient equals sum_(k>=1)P_s(tau_k=n)/k. On the kth positive return J_s=k exactly, since the initial visit is included among earlier visits. This proves (1.1). Nonnegativity follows from the return expansion; irreducibility and aperiodicity are unnecessary.

## 2. An explicit diagonal-to-successor-crossing cutoff

For M>=8 put x=aM and G=1+ln(1+b/(e A0)). Then

 E_W V_A
 <=8A0/M +(5A0/M)x(1+x)exp(-x/4)G
 <=63 A0 G/M.                                         (2.1)

The symbol-swapped analogue is

    E_C V_B <=63 A0[1+ln(1+e/(b A0))]/M.               (2.2)

### Proof

The first hitting time T of A from W is geometric(a), and no A visit occurs before T. Let f(n) be E_A V_A at horizon n, with the same A0. For T<=M/2, the remaining horizon n=M-T is at least M/2. Equation(1.1) and min(b,A0/(J+2))<=A0/J on an A endpoint give f(n)<=4A0/n<=8A0/M.

For T>M/2, its point probability is bounded by a exp(-aM/4), since T-1>=M/2-1>=M/4. It remains to control the sum of f(n) up to M.

Between an entrance to A from W and the next visit to W, the number N of A visits is geometric(e): every A-to-B phase eventually reaches B (t>0), and at B absorption into W occurs independently with probability e. Thus P(N>j)=(1-e)^j. Resetting counts at each such excursion only increases the reciprocal functional. The expected complete-excursion cost is

    C0=sum_(j>=0)(1-e)^j min(b,A0/(j+2)).

A direct harmonic/exponential split gives

    C0<=5A0[1+ln(1+b/(e A0))]=5A0G.                    (2.3)

For detail take L=ceil(max(1,A0/b)). The j<L sum is at most2A0: if A0>=b use bL<=A0+b<=2A0, and otherwise L=1 and the first term is at most A0/2. For j>=L, use(1-e)^j<=exp(-ej) and1/(j+2)<=1/(j+1); comparison with the decreasing integral gives a bound A0 times a universal constant plus A0 log_+(1/(eL)). Since L>=A0/b, this is covered by the displayed factor5.

Over a length-M path starting A, there is one initial active excursion and at most aM further excursions in expectation, because a departure W→A has conditional probability a at each time. Strong Markov at excursion entrances and nonnegative complete-excursion costs imply

    sum_(n=0)^M f(n)<=(1+aM)C0.                       (2.4)

This comparison is pathwise before taking expectations: the true cumulative A count is at least the count within its current excursion. Truncating a final excursion only lowers its cost.

Multiply (2.4) by the late-hit density a exp(-aM/4), and add the early-hit bound. Finally x(1+x)exp(-x/4)<=11: separately maximize x exp(-x/4)<=4/Euler_e and x² exp(-x/4)<=64/Euler_e². This proves (2.1), and symbol symmetry proves (2.2).

This is an e cutoff for the W→A contribution, NOT yet a square-root-beta bound. The retained x-dependent factor may be important: it exponentially suppresses a genuinely late initial departure when aM is large.

## 3. Crossing starts reduce to diagonal starts, up to statistical-scale error

Let h=b+e-be. Starting A or B, until the first diagonal hit the chain alternates A,B. In each two-step block it hits a diagonal with probability h, regardless of which crossing state begins the block.

If h<=M^(-1/2), then for either crossing initial state

    E q_(Y_M)<=2(b+e)<=4/sqrt(M),                      (3.1)

so E sum_s V_s is bounded by the same quantity, independently of A0.

Indeed crossing endpoint contributions are at most b+e. For W endpoints, sum over the last B→W entrance: P(Y_M=W) is at most e sum_(j>=0)(1-a)^j=e/a, hence aP(Y_M=W)<=e. There is no initial W mass. Similarly tP(Y_M=C)<=b. Finally b+e<=2h.

If h>M^(-1/2), put u=floor(M/2) and let T_diag be the first diagonal hit. Then

    P(T_diag>u)<=(1-h)^floor(u/2)
                  <=exp(-sqrt(M)/8), M>=8.            (3.2)

On T_diag<=u, the post-hit suffix has length n=M-T_diag>=ceil(M/2), begins at a diagonal, and has the same actual terminal query. Its terminal prior count is at most the full-path count. By the strong Markov property,

 E_cross sum_s V_s
 <=exp(-sqrt(M)/8)
   + sup_{i in{W,C}, ceil(M/2)<=n<=M}
        E_i[sum_s 1{Y_n=s}min(q_s,A0/(J_s(n)+2))].     (3.3)

The first term is O(M^-1/2) with an absolute constant, by maximizing sqrt(M)exp(-sqrt(M)/8). This is an exact suffix/count reduction, not a marginal mixing statement.

## 4. Remaining obstruction

Equations(2.1)-(2.2) handle initial waiting on one diagonal and terminal query at its immediate successor crossing. Initial-equals-target cases are already controlled by(1.1). Section3 removes initially alternating crossing states once a uniform diagonal-start bound is established.

The unresolved terms include an initial diagonal followed by the opposite diagonal as terminal query, and the opposite crossing query. Their first-hit laws can include both geometric waiting phases and repeated active attempts. The all-state certificate may convert the explicit e/b cutoff of(2.1)-(2.2) to square-root-beta after accounting for the other diagonal's holding rate and the numerical/statistical floor, but this conversion has NOT been proved here.

No full-support risk theorem, beta-adaptive rate, stationary-law domination, improved global gap, or initialization separation is claimed.
