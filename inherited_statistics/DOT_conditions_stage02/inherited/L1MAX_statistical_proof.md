# 继承 L1MAX 一般初始化 add-one 上界

原提供资料中已接纳证明的科学片段；本次未重新独立审查原始全篇。文字及数学保持原字节，映射与源文件哈希见 COPY_MAP.json。与本阶段无关的实现、故障、资源及历史流程内容不在本件范围。

## 编排补充的独立阅读记号（非原证明逐字摘录）

原 L1MAX 已接纳科学声明 §1 与 §2（TRUNC）使用以下记号。本段是为独立阅读补入的编排说明，不是新增引理，也不列入下方逐字复制片段：

    R_K⁺(M) = sup_(θ,μ) E TV(p⁺_(Y_M), θ_(Y_M)),
    Ψ(0)=0; Ψ(x)=x(1+ln(1/x))（0<x<1）; Ψ(x)=1（x≥1）.

其中 θ 为任意合法齐次二阶表，μ 为任意初始 pair 律，p⁺ 为原完整历史 add-one；ln 为自然对数。原科学声明完整文件 SHA-256 为 `bc24d183f5299df636e67f0b439aadbcd4d79671b69c327ed7083ddfab857c6f`。它与下方可读证明文件是不同来源对象，不把声明哈希冒充证明文件哈希；这里只补记号，不交付原控制封装。

## 原证明科学正文


## 1. Scope and exact predecessor use

Fix K>=2 and M>=1, both integers, and N=M+2. Let theta be any homogeneous
second-order transition table on A={0,...,K-1}, with zero entries allowed,
and mu any law on the initial pair. For this one experiment theta is fixed.
Set

    Y_i=(X_(i+1),X_(i+2)),          0<=i<=M,
    C_s,a=sum_(i=0)^(M-1)1{Y_i=s,X_(i+3)=a},
    n_s=sum_a C_s,a,     J=n_(Y_M),
    p^+_s,a=(C_s,a+1)/(n_s+K),
    T=T(K,M)=K^(5/2)/sqrt(M+1),    c=K^4/(M+1).

Exactly M departures are counted. The last counted successor is X_(M+2).
The pair Y_M is observed but its departure is not. Every risk below is
E TV(output,theta_(Y_M)) on this complete observed history, where
TV(u,v)=||u-v||_1/2. No new predictor or observation experiment is substituted.

The only predecessors used are:

1. G/U: integer UC in exactly this actual experiment,
   P(J<w)<=min{1,cw} for all integers w>=1, uniformly over theta and mu.


## 2. Finite row-stack realization of exactly the original history

Take a finite product probability space carrying an initial pair of law mu,
and, independently, symbols

    xi_s,l ~ theta_s,  s in A^2,  1<=l<=2M,

independent over all s,l. This requires no positivity. Starting at the initial
pair, for i=0,...,M-1 let s=Y_i, let j be the number of earlier departures
from s, append X_(i+3)=xi_s,j+1, and move to (X_(i+2),X_(i+3)).
The pair shift is exactly the required legal shift (a,b)->(b,d).
A row uses at most M symbols, so its 2M-stack always suffices.

Here is a finite path-law verification that also explains what is, and is
not, conditioned on. For a proposed finite prefix x_1,...,x_(i+2), the event
that the construction produces it is the initial-pair event together with,
in each row, equality constraints on exactly the consumed stack prefix
specified by that history. There are no constraints on any unused symbols.
Induction over i proves this assertion: the next prescribed symbol is
exactly the next unused coordinate of the currently prescribed row.
Independence in the product space therefore gives prefix mass

    mu(x_1,x_2) product_(r=0)^(i-1)
       theta_(x_(r+1),x_(r+2))(x_(r+3)).

This is the original homogeneous path law. Zero-probability prefixes give
zero in both constructions; no conditional assertion at a null event is
needed. This proves equality of the full observed-history distribution.

On this coupling, simultaneously for every row s, with e_a the unit vector,

    S_s,j=sum_(l=1)^j(e_(xi_s,l)-theta_s), S_s,0=0,
    (C_s,a-n_s theta_s,a)_a = S_s,n_s.                 (2.1)

The 2M samples only define a finite auxiliary analysis space. They are not
provided to the estimator. In particular, we never assert iid row samples
after conditioning on the random J, Y_M, or a selected count event.

## 3. A finite Doob L2 bound and the L1 mean

We first prove the finite maximal inequality used here. For a nonnegative
submartingale W_0,...,W_m with bounded values, set H=max_(0<=j<=m) W_j.
For lambda>0, partition {H>=lambda} by the first time j that W_j>=lambda.
Each such event is measurable at time j. The submartingale property,
iterated to time m, gives

    lambda P(H>=lambda)
       <=sum_j E[W_j 1{first hit j}]
       <=E[W_m 1{H>=lambda}].

Integrating this inequality with respect to 2 d lambda gives

    E H^2 <=2 E(W_m H)
           <=2(E W_m^2)^(1/2)(E H^2)^(1/2).

All integrations are finite because H is bounded; the equality
E H^2=integral_0^infinity 2lambda P(H>=lambda)d lambda follows
pointwise from integrating 2lambda up to H. Dividing when E H^2>0,
and separately treating zero, proves

    E H^2 <=4 E W_m^2.                                (3.1)

For a fixed row s, S_s,j is a vector martingale in its deterministic
prefix filtration. Convexity of the Euclidean norm shows that
W_j=||S_s,j||_2 is a nonnegative submartingale. For m=2v, 1<=v<=M,

    E||S_s,2v||_2^2
       =2v E||e_(xi_s,1)-theta_s||_2^2
       =2v(1-||theta_s||_2^2) <=2v.                   (3.2)

The cross terms vanish by independence and centering at deterministic
indices; the last one-step identity is obtained by expanding the square.
Define

    F_s,v=max_(0<=j<=2v)||S_s,j||_1,
    Z_v=max_(s in A^2) F_s,v.

The deterministic vector inequality ||z||_1<=sqrt(K)||z||_2,
Cauchy–Schwarz, (3.1), and (3.2) yield

    E F_s,v <=sqrt(K) E max_(j<=2v)||S_s,j||_2
              <=sqrt(8Kv).                           (3.3)

This use of sqrt(K) is solely in the mean bound. It will not multiply
the concentration deviation.

## 4. Direct L1 bounded differences and a conditional MGF proof

If one stack symbol at coordinate r<=2v is changed from a to b, S_s,j
is unchanged for j<r and is changed by e_b-e_a for j>=r. The latter
vector has L1 norm at most 2. The reverse triangle inequality and

    |max_j u_j-max_j v_j|<=max_j|u_j-v_j|

therefore imply that F_s,v changes by at most 2. This is the oscillation
of the entire L1-prefix maximum, not of one scalar summand.

We prove the needed bounded-differences estimate from conditional intervals.
For any finite random variable B in an interval of length d, define
phi(lambda)=ln E exp(lambda B). Under exponentially tilted probabilities,

    phi''(lambda)=Var_lambda(B)<=d^2/4.

The variance bound follows by measuring square distance from the midpoint
of the same interval: variance is no greater than that second moment.
Since phi(0)=0 and phi'(0)=E B, integration twice for lambda>=0 gives

    E exp(lambda(B-E B)) <= exp(lambda^2 d^2/8).        (4.1)

Constant variables give the same inequality with d=0. Thus this also
holds conditionally on any positive-probability finite past, with the
conditional interval endpoints and mean.

More generally let f depend on independent coordinates with one-coordinate
oscillations at most d_i. Expose the coordinates successively and let D_i
be differences of its conditional-expectation martingale. With the past
fixed, averaging over a common independent future shows that the possible
next conditional expectations have range of length at most d_i:
the pointwise oscillation bound remains true after averaging the future.
Subtracting the preceding conditional expectation changes only the interval's
location. Hence E[D_i|past]=0 and (4.1) gives

    E[exp(lambda D_i)|past]<=exp(lambda^2 d_i^2/8).

Iterated conditioning proves

    E exp(lambda(f-E f))<=exp(lambda^2 sum_i d_i^2/8).
                                                               (4.2)

No chosen stopping index or row is conditioned on in this argument.
Applying (4.2) directly to F_s,v with 2v coordinates and d_i=2 gives
E exp(lambda(F_s,v-E F_s,v))<=exp(v lambda^2). Markov's inequality
and lambda=t/(2v) therefore give, for every t>=0,

    P(F_s,v-E F_s,v>t)<=exp(-t^2/(4v)).                (4.3)

For t=0 the assertion is just the probability bound one. The argument
also covers deterministic rows, which may have F_s,v identically zero.

## 5. Row maximum, shifted tail integral, and the constant 25/4

Put b=sqrt(8Kv) and a=sqrt(8v ln K). From (3.3)–(4.3), a finite union
over exactly K^2 rows gives, for every t>=0,

    P(Z_v>b+a+t)
       <=K^2 exp(-(a+t)^2/(4v))
       <=exp(-t^2/(4v)).                              (5.1)

The cancellation uses a^2/(4v)=2ln K and the remaining cross term
is nonpositive in the exponent. This union bound needs no independence
between the row maxima.

Let R=(Z_v-b-a)_+, the positive part. Tail integration, with
u=t^2/(4v), yields

    E R^4
       =integral_0^infinity 4t^3 P(R>t)dt
       <=integral_0^infinity 4t^3 exp(-t^2/(4v))dt
       =32v^2 integral_0^infinity u exp(-u)du
       =32v^2.                                       (5.2)

The final integral equals one by integration by parts; it is a numerical
integral, not an extension of the random row stacks.

For completeness, the Lp inequalities used here and in the selection
step are finite-sum/integral inequalities. Young's inequality
xy<=x^p/p+y^q/q for reciprocal exponents p,q>1 follows by minimizing
x^p/p-xy+y^q/q over x>=0. Dividing two nonzero random variables by
their Lp,Lq norms and taking expectations proves Holder; zero norms
are treated separately. For p=4 it also gives Minkowski, since

    E(U+V)^4
       =E[(U+V)^3 U]+E[(U+V)^3 V]
       <=||U+V||_4^3 (||U||_4+||V||_4)

for nonnegative U,V; divide if the left norm is nonzero.
Since Z_v<=b+a+R, we conclude

    ||Z_v||_4
      <=sqrt(8Kv)+sqrt(8v ln K)+32^(1/4)sqrt(v).        (5.3)

To check the constant uniformly, the function ln x/x has derivative
(1-ln x)/x^2 and maximum 1/e for x>0. Also
e>1+1+1/2+1/6=8/3, so 1/e<3/8. For K>=2, dividing (5.3) by sqrt(Kv)
thus bounds its coefficient by

    sqrt(8)+sqrt(3)+2^(3/4) <25/4.                    (5.4)

Here is a rational verification of the strict last comparison:

    sqrt(8)<283/100,       since 283^2=80089>80000;
    sqrt(3)<1733/1000,     since 1733^2=3003289>3000000;
    2^(3/4)<1683/1000,    since
                 1683^4=8022993935121>8000000000000.

Their rational upper bounds sum to 6246/1000<6250/1000=25/4.
This proves all of L1MAX. In particular it absorbs an ADDITIVE
sqrt(log K) deviation into the sqrt(K) mean scale. It does not claim
that (5.1)'s deviation has no logarithmic row-count term, and does
not multiply that deviation by another sqrt(K).

## 6. A fully explicit numerical dyadic sum

For any real a>0 define

    D(a)=sum_(l=0)^infinity 2^(-l/2)min{1,a2^l}^(3/4).

We prove D(a)<=10sqrt(a). If a>=1, all minima equal one, and

    D(a)=1/(1-2^(-1/2))=2+sqrt(2)<7/2<=10sqrt(a).

For 0<a<1, let L be the unique integer >=0 satisfying
a2^L<=1<a2^(L+1). The two geometric parts obey

    sum_(l=0)^L a^(3/4)2^(l/4)
       <= a^(3/4)2^(L/4)/(1-2^(-1/4))
       <= sqrt(a)/(1-2^(-1/4)),
    sum_(l=L+1)^infinity 2^(-l/2)
       =2^(-(L+1)/2)/(1-2^(-1/2))
       <sqrt(a)/(1-2^(-1/2)).

These include exact dyadic a, with the equality-threshold term assigned
to the first sum. For a rational check on their combined constant,

    2^(-1/4)<27/32,

because 2*27^4=1062882>1048576=32^4. Therefore the first denominator
inverse is <32/5, and the second equals 2+sqrt(2)<7/2. Their sum
is <99/10<10. This proves

    D(a)<=10sqrt(a),  for all a>0.                    (6.1)

Only this deterministic numerical sum is infinite.

## 7. Actual selected-row error, with all correlations retained

On a path with J>=1 define only there the empirical probability row
phat_(Y_M)=(C_(Y_M),a/J)_a. For deterministic dyadic v=2^l<=M, set

    E_v={v<=J<2v}.

By (2.1), on this event

    TV(phat_(Y_M),theta_(Y_M))
       =||S_(Y_M),J||_1/(2J)
       <=Z_v/(2v).                                   (7.1)

This is a pathwise inequality: J, the actual row, and all row errors
may be dependent. The auxiliary maximum includes j<=2v<=2M, so it
exists even in the final partially filled dyadic layer.

Apply Holder unconditionally to Z_v 1_(E_v), with exponents 4 and 4/3.
Using L1MAX and UC at the INTEGER threshold w=2v gives

    E[TV(phat_(Y_M),theta_(Y_M))1_(E_v)]
       <=||Z_v||_4 P(E_v)^(3/4)/(2v)
       <=(25/8)sqrt(K) v^(-1/2) min{1,2cv}^(3/4).       (7.2)

If P(E_v)=0 the left side is zero. We have not asserted anything
about an iid law conditional on E_v, J, or Y_M. Nor have we moved
a maximum outside a sum over starting states. The actual integer UC
constant remains K^4.

The finitely many layers l=0,...,floor(log2 M) partition {1<=J<=M}.
In particular J=M is included, even when M is a power of two, in the
layer beginning at v=M. Summing (7.2) and extending only its nonnegative
NUMERICAL right side to the infinite sum in (6.1), with a=2c, yields

    E[empirical actual loss on {J>=1}]
       <=(25/8)sqrt(K) D(2c)
       <=(125sqrt(2)/4) sqrt(Kc)
       =(125sqrt(2)/4) T.                             (7.3)

No F_s,v for v>M is defined or needed. The empirical loss is not
defined by a zero denominator at J=0; it has not been used there.

## 8. Integer UC, real thresholds, smoothing, and L1+

We prove the requested truncated expectation for every real A>=0:

    E min{1,A/(J+K)} <=Psi(cA)<=2sqrt(cA).              (8.1)

For A=0 all quantities are zero. For A>0, 0<t<1, write x=A/t-K.
The event that min{1,A/(J+K)}>t is {J<x}. If x<=0 it is empty.
If x>0, since J is a nonnegative integer,

    {J<x}={J<ceil x},    1<=ceil x<=x+1<=A/t.

Apply integer UC at w=ceil x to get probability at most min{1,cA/t}.
Tail integration over t in (0,1) gives Psi(cA), splitting at t=cA
when 0<cA<1; for cA>=1 the integral equals one. Finally
min{1,cA/t}<=sqrt(cA/t), whose integral is 2sqrt(cA). This proves
(8.1) with J=0, small M, and all real threshold cases included.

If J>=1 and u is the K-uniform vector, the exact add-one identity is

    p^+_(Y_M)=[J/(J+K)]phat_(Y_M)+[K/(J+K)]u.

Its TV distance from the true row is at most the empirical TV loss
plus K/(J+K). At J=0, p^+ is uniform and its TV loss is at most one.
Thus, treating the two cases separately and then enlarging the smoothing
expectation to all paths,

    E TV(p^+_(Y_M),theta_(Y_M))
       <=P(J=0)
         +E[empirical actual loss on {J>=1}]
         +E min{1,K/(J+K)}.                            (8.2)

There is no definition of phat at zero in this formula.
UC with w=1 gives P(J=0)<=min{1,c}<=sqrt(c)<=sqrt(Kc)=T.
Equation (8.1) with A=K gives the smoothing term at most 2sqrt(Kc)=2T.
Combining with (7.3),

    E TV(p^+_(Y_M),theta_(Y_M))
       <=[125sqrt(2)/4+3]T <48T.                      (8.3)

Indeed sqrt(2)<36/25, because 2<1296/625; hence the coefficient is
strictly less than (125/4)(36/25)+3=48. Loss is also at most one,
so the non-strict asserted bound follows after taking the supremum:

    R_K^+(M)<=min{1,48T(K,M)}.                         (L1+)

Every constant is independent of theta, mu, K and M. Degenerate rows
and arbitrary initialization were included in the finite coupling,
and no recurrence, mixing, stationarity or positivity assumption
entered the argument. UC applies to its full admitted class, including
transient, reducible and periodic chains. This proves the full
finite-parameter upper bound in the original experiment.

