# AB003 — Joint-blind optimality through square-root budgets (candidate)

2026-11-02. New author candidate; fresh full independent review and root acceptance required. Accepted AB001/AB002 are unchanged.

## 1. Result and scope

Use exactly the protected-endpoint, binary, full-corrupted-history source experiment in accepted SC003/BT002. Let M>=64, beta in [0,1], and integer 0<=k<=floor(sqrt(M)). Both stationary and arbitrary initializations are allowed, including unsupported starting pairs. There is one deterministic finite-rational estimator, **independent of both k and beta**, with risk

    R <= min{1, 2^18 M^-1/2 + 2^22 F_2(M,k,beta)},     (AB3)

where F_2 is the accepted binary profile, zero at k=0 and otherwise

    F_2=(k/M)[1+log(1+1/(k max(sqrt(beta),1/M)))].

Thus one joint-blind estimator attains the known-k minimax order simultaneously in the entire range k<=sqrt(M), uniformly over beta and both initialization conventions. It is a total map for every corrupted word and can still be run for larger k; **no optimality bound beyond the stated range is claimed**. AB001's impossibility uses k much larger than sqrt(M) and is consistent with this result. Supplied-beta adaptation for all budgets remains open.

## 2. The estimator

For state u, designate d(u) to be the complement of its first bit, exactly as in SC003. Put

    B=12 ceil(sqrt(M)).

Count the corrupted triples with departures 0,...,M-1, and use the preserved terminal pair u. Let C' be its designated-successor count and J' its total row count. Output designated probability

    qhat = C'/J' if C'>B, and qhat=0 otherwise.        (2.1)

The other coordinate is 1-qhat. The active branch always has J'>B>0, so the ratio is defined. The rule reads only the corrupted word and M; it does not know the actual number of edits, the advertised maximum k, beta, the clean counts, the edit mask, or the source law. A hard threshold is essential: this is not the soft subtraction (C'-B)_+/(J'+B+2), whose threshold bias would require a different analysis.

## 3. A deterministic perturbation bound

Let q=q_u be the true designated probability at the preserved terminal row, and C,J its clean designated and total counts. These are analysis variables only. Define

    E=1{J>0}|C/J-q|,
    d=6k.

Every changed symbol affects at most three triples, each changing a histogram by l1 at most two. Hence |C'-C|<=d and |J'-J|<=d. Our budget range ensures d<=B/2.

We claim, for every admissible clean/corrupted pair,

    |qhat-q| <= 5 E +4 min(q,36k/(J+2))
                    +q 1{J<=3B/q},                 (3.1)

where the last term is defined to be zero when q=0. At k=0 the middle term is zero, without evaluating any singular expression.

### Inactive branch

If C'<=B then qhat=0 and C<=B+d<=3B/2. For J>3B/q and q>0, C/J<q/2, so q<=2E. On the complementary event, the last term in (3.1) pays q exactly. For J=0 the last term pays q; if q=0 the loss is zero. This proves the desired bound on the inactive branch.

### Active branch

If C'>B then C>C'-d>B-d>=B/2>=d, hence J>0. Write p=C/J and p'=C'/J'. Direct normalization gives

    |p'-p| <=2d/J.

Also p'<=4p: if J>=2d, then C+d<2C and J-d>=J/2, so p'<=(C+d)/(J-d)<=4p (the d=0 case is immediate); if J<2d, then p=C/J>d/J>1/2, so p'<=1<2p. Thus |p'-p|<=4p as well, and

    |p'-q| <= |p-q|+min(4p,2d/J)
             <=5|p-q|+min(4q,2d/J)
             <=5|p-q|+4 min(q,6d/(J+2)).            (3.2)

The second inequality uses that x->min(4x,c) is 4-Lipschitz on nonnegative reals. For the last, J>=1 implies J+2<=3J, and the displayed denominator bound is deliberately loose. Since 6d=36k, (3.2) implies (3.1). When d=0 it simply reads |p-q|<=5|p-q|.

## 4. The hard-threshold bias has no logarithm

The accepted universal terminal-occupation inequality on the four-state pair chain is

    P(J_(Y_M)<w)<=min(1,16w/(M+1)), integer w>=1,     (4.1)

valid for every source and every initial law, without any minorization assumption.

The row probabilities q_u are fixed source constants; they are not a single random threshold to insert into (4.1). Sum explicitly over the four states. For each u with q_u>0, put w_u=floor(3B/q_u)+1. Then

    {Y_M=u,J_u<=3B/q_u}
       subset {J_(Y_M)<w_u},

and (4.1), with its bound possibly larger than one, gives

    q_u P(Y_M=u,J_u<=3B/q_u)
       <=16 q_u w_u/(M+1)
       <=16(3B+q_u)/(M+1).

Rows with q_u=0 contribute exactly zero and need no threshold. Therefore

    E[q_(Y_M) 1{J_(Y_M)<=3B/q_(Y_M)}]
       <=64(3B+1)/(M+1)
       <=2600 M^-1/2.                              (4.2)

For the last finite-domain constant, M>=64 implies ceil(sqrt(M))<=sqrt(M)+1<=9sqrt(M)/8, hence B<=27sqrt(M)/2 and 3B+1<=325sqrt(M)/8. Dividing by M+1>=M yields 64*325/8=2600.

This is the no-log benefit of a hard count threshold. It does not assume the row observations are IID after terminal selection.

## 5. Clean comparator and weighted occupation inputs

The exact inherited clean-comparator interface recorded and proved from R011 in accepted SC003 §3 is

    E E <=(8192+1)sqrt(32)/sqrt(M+1).                 (5.1)

It concerns original clean empirical row frequencies, used only in the analysis. The estimator never observes them.

For V_A=min(q_(Y_M),A/(J+2)), use the same fixed orientations as SC003. Its accepted weighted occupation interfaces, valid for arbitrary starts, are:

1. Full stationary support and beta>=M^-2, from BIF001:

       E V_A <=4/sqrt(M)+(16672 A/M)
                       [1+log(1+1/(sqrt(beta) A))].   (5.2)

2. A singleton stationary support with beta>0, from BAI003 v2:

       E V_A <=256 max(A,1)/M+16/(M+2).              (5.3)

   The same public orientation covers either absorbing diagonal by symbol exchange. The support classification under positive all-state minorization is the one proved in SC003 §4.

3. For every source and start, (4.1) implies

       E min(1,A/(J+2))<=Psi(16A/(M+1)),             (5.4)

   where Psi(x)=x(1+log(1/x)) for 0<x<1 and Psi(x)=1 for x>=1. This is SC003's layer-cake interface and includes J=0.

For k>=1 use A=36k. In case 1, A>=k gives

    E V_A <=4s+600192 F_2.                           (5.5)

In case 2, E V_A<=9232 k/M<=9232 F_2. In the weak range beta<M^-2, put e_*=1/M. Equation (5.4) and the scalar estimate

    Psi(576k/M)<=576(k/M)[1+log(1+M/k)]

give E V_A<=576F_2. The scalar estimate follows by splitting M/k below or above 576, exactly as in SC003; no positive-support classification is needed in the weak range. Equality beta=M^-2 belongs to case 1 or case 2. Thus, uniformly for k>=1,

    E V_(36k)<=4s+600192 F_2.                        (5.6)

For k=0 the functional V_0 is identically zero and no logarithm or A=0 input is evaluated.

## 6. Assembly and minimax-order comparison

Take expectations in (3.1), use (4.2), (5.1), and (5.6). The statistical coefficient is at most

    5*8193*sqrt(32)+2600+16 <2^18,

and the corruption coefficient is 4*600192=2400768<2^22. This proves (AB3), capped by unit TV loss. At k=0 omit the weighted term and retain the same statistical bound.

The accepted BT002 lower c H_2 applies to each fixed k even if k is supplied. Restricting estimators to be joint-blind cannot improve that lower. Conversely (AB3) is at most a universal constant times H_2 because s+F_2<=2max(s,F_2) and the cap is respected. Therefore the same estimator simultaneously attains the known-k order over the stated k<=sqrt(M) range, for both initialization conventions.

## 7. Algorithmic and logical scope

B is an exactly computable integer from M, for example using integer square-root and one comparison. The active probability C'/J' is an exact rational number with O(log(M+2))-bit numerator and denominator. A direct scan has O(M log(M+2)) conservative bit complexity including counters, and O(M+log(M+2)) live bits including retained input/output. These are ordinary sequential full-history costs, not a neural-depth or training claim.

The proof uses the true k only to establish the analyst's condition d<=B/2; neither the estimate nor a data-dependent guessed budget uses k. The guarantee is uniform over every allowed corruption kernel, and therefore over pointwise actual budget k or any advertised maximum k within the range. It is not an oracle that receives the realized edit count. No supplied-beta all-budget conclusion, stationary-only restriction, fixed-histogram lower, or unseen-clean-data algorithm is hidden in the statement.

## 8. Corollary: sharp order boundary for an adaptive budget range

Let b_M be any public integer-valued function with 0<=b_M<=M. Ask for one family A_M, allowed to be designed using this public range envelope b_M but **not** supplied the actual k or beta, and one finite constant C such that

    sup_source sup_strict-k-kernel E TV(A_M(Z),theta_(Y_M))
       <= C H_2(M,k,beta)

for every M>=64, every beta in [0,1], and every integer 0<=k<=b_M. The source supremum may use stationary initialization or arbitrary initialization.

Such a family exists if and only if b_M=O(sqrt(M)), equivalently sup_(M>=64) b_M/sqrt(M)<infinity. The estimator constant may depend on the fixed range-envelope bound. This is a statement about uniform adaptation over an entire budget range including k=0, not a pointwise impossibility at a single large budget such as k=M.

### Sufficiency

If b_M<=L sqrt(M) for a fixed positive integer L, replace the threshold in (2.1) by B_L=12L ceil(sqrt(M)). The same pathwise proof works for all k<=floor(L sqrt(M)), because 6k<=B_L/2. The only altered expectation is the threshold term, now at most 2600L/sqrt(M). The clean-comparator and weighted-occupation terms are unchanged. Thus

    R <=min{1,2^18 L M^-1/2+2^22 F_2},               (8.1)

which is a finite constant multiple of H_2 throughout the required range. Choose an integer L at least max(1,sup_M b_M/sqrt(M)). The design uses the permitted public envelope, not the unknown realized budget.

### Necessity

If b_M/sqrt(M) is unbounded, there is a sequence M_n tending to infinity along which this ratio tends to infinity. Put

    k_n=min{b_(M_n), floor(M_n^(3/4))}.

Then k_n/sqrt(M_n) tends to infinity, k_n<=b_(M_n), k_n<=floor(M_n/8) eventually, and log(M_n/k_n) tends to infinity (indeed it is at least (1/4)log M_n up to harmless flooring).

The putative k=0,beta=0 guarantee gives the AB001 clean risk S_(M_n)(A)<=C/sqrt(M_n). Apply AB001's exact finite inequality to the same A_(M_n) and this k_n. The ratio of its negative term to its positive term is

    <= (8192C/9) (sqrt(M_n)/k_n)
          [ log(2 floor(M_n/8)/k_n)
            / log((floor(M_n/8)+1)/k_n) ],

which tends to zero: the bracket tends to one and sqrt(M_n)/k_n tends to zero. Consequently the null corruption risk is at least a fixed positive multiple of

    (k_n/M_n) log(M_n/k_n).

At the null's beta=1/M_n, k_n>=sqrt(M_n) eventually gives H_2<=2k_n/M_n. The ratio of actual risk to the purported C H_2 bound diverges, a contradiction. AB001's null and clean alternatives are stationary, so necessity already holds in the stationary experiment; sufficiency was valid for arbitrary starts.

This corollary combines the new small-budget construction with separately accepted AB001. It does not change AB001's proof or say that risk must be large at every individual k above sqrt(M). At k comparable to M, H_2 is already constant and a pointwise adaptation obstruction of that form would be false. The supplied-beta all-budget question is still not answered.
