# 继承 GU 占用尾界与小字母表 IID 下界

原提供资料中已接纳证明的科学片段；本次未重新独立审查原始全篇。文字及数学保持原字节，映射与源文件哈希见 COPY_MAP.json。与本阶段无关的实现、故障、资源及历史流程内容不在本件范围。

第一节中 D 是状态总数（本题 D=K²）；n_s(m) 是前 m 次 departure 中状态 s 的访问数，G_t 是观测到 Y_t 的历史。第二节使用 N 个完整已观察符号。两节分别支撑 L1MAX 的 UC 和 MM5 在 2≤K≤11 时的下界。

## 1. Source, observation, counts and all risk conventions

Let A={0,...,K-1}, S=A², D=K². Fix theta in the full product of K-simplexes
indexed by S and mu in Delta(S). Starting with (X_1,X_2)~mu, the conditional
law of X_(j+3) given X_1,...,X_(j+2) is theta_(X_(j+1),X_(j+2)). Thus

    Y_j=(X_(j+1),X_(j+2)),
    P((a,b),(b,c))=theta_(a,b)(c),
    N>=3, M=N-2>=1, E_N=Y_M,
    n_s(M)=sum_(j=0)^(M-1) 1{Y_j=s},
    C_s,c(M)=sum_(j=0)^(M-1)1{Y_j=s,X_(j+3)=c},
    p_N^+(c|s)=(C_s,c(M)+1)/(n_s(M)+K).

All other pair transitions are zero. The last counted successor is X_N;
Y_M is not another departure and X_(N+1) is not observed. At arbitrary
pair horizon m>=0 use the same counts with m in place of M. Let
G_j=sigma(X_1,...,X_(j+2)) and H_N=G_M. The predictor receives only the
complete observed history, declared query s and public K,N,h. Actual query
is the observed endpoint E_N. theta,mu, support, closed classes, stationary
laws, future stacks and hidden source labels are not inputs. A common
randomized algorithm in a lower bound may also have an independent random
seed with the same law in all sources.


### 11.1 Suffix domination, first-v charging and the exact K^4 bound

For any fixed homogeneous pair kernel P, integer v>=1 and m>=0 define

    b_(m,v)(y)=P_y(n_(Y_m)(m)<v),
    B_(m,v)(P)=max_y b_(m,v)(y),
    beta_(K,v)(m)=sup_theta B_(m,v)(P_theta).

For m>=l>=0, full counts dominate the last l departure counts for the
same random endpoint Y_m. Given G_(m-l), the suffix is a length-l chain
with kernel P started at the known Y_(m-l). Therefore

    b_(m,v)(y)<=E_y b_(l,v)(Y_(m-l))<=B_(l,v)(P),
    B_(m,v)(P)<=B_(l,v)(P).                            (MON)

This uses no conditioning on Y_m, stationarity or reverse kernel. At m=0
the counts vanish, so B_(0,v)=beta_(K,v)(0)=1. Taking max over starting
states bounds any initial law by convexity. Individual b need not decrease:
the full K=2 table 00:(1/2,1/2),01:delta_1,10:delta_0,11:delta_1 has
b_(1,1)(00)=1/2 and b_(2,1)(00)=3/4.

For any deterministic sequence in D states, the event n_(y_t)(t)<v marks
only the first v occurrences of its current state. Hence for every T

    sum_(t=0)^T 1{n_(y_t)(t)<v}<=Dv.                   (CH)

Take expectations separately for every initial y, and then use max<=sum:

    sum_(t=0)^m B_(t,v)(P)
       <=sum_y sum_(t=0)^m b_(t,v)(y)<=D²v.

By (MON), (m+1)B_(m,v)<=D²v, and consequently

    beta_(K,v)(m)<=min(1,K^4 v/(m+1)).                 (UC)

We did not exchange sum and max. For the preceding geometric table at v=1,
B_0=B_1=1, B_2=B_3=3/4 and B_m=(3/4)2^(-(m-3)) for m>=3, giving
sum_m B_m=17/4>4=Dv. The four initial states verify these values directly:
from 00 the endpoint is new only at exit or first absorption; from 10
there is one extra initial step, from 01 first absorption is at step 1,
and 11 is absorbing. For m>=2 the 10-start probability is the 00-start
probability at m-1. This also explains the extra factor in the safe proof.



### 13.3 Any common randomized full-history predictor: iid actual lower bound

Fix N>=3,K>=2 and any such predictor. Put

    p_±=1/2±1/(8sqrt(N)), d=p_+-p_-=1/(4sqrt(N)).

Let every row of theta_± give symbol 1 probability p_±, symbol 0 probability
1-p_± and the remaining symbols zero; take mu_± as the corresponding iid
pair law. Thus the complete X_1^N consists of N iid draws. Every possible
actual endpoint has the same true next distribution, so the target is
actual prediction, not a difficult external row. For the two history laws
P_± the one-draw chi-square is

    d²/[p_-(1-p_-)]<=4/(15N),

because p_-(1-p_-)=1/4-1/(64N)>=15/64. If L is the likelihood ratio,
E_- L² multiplies over the independent draws, giving

    1+chi²(P_+||P_-)<=(1+4/(15N))^N<=exp(4/15).

Cauchy–Schwarz applied to (1/2)E_-|L-1| bounds history TV by half the
square root of chi-square. Using exp(x)<=1/(1-x) for 0<=x<1 (termwise
power-series comparison),

    TV(P_+,P_-)<=1/sqrt(11)<1/2.

For each common history x, the actual query and conditional randomized
output law are identical in the two experiments. Integrating the output
triangle inequality against min(P_+(x),P_-(x)) yields

    risk_+ + risk_- >= d sum_x min(P_+(x),P_-(x))
                    =d[1-TV(P_+,P_-)]>=d/2.

Thus at least one source has actual mean TV >=d/4=1/(16sqrt(N)). This
holds for every N and every common randomized algorithm, without I and
without a computation restriction. The witness can depend on N and the
algorithm; no single source is claimed to meet this lower bound at every N.
K>2 is a lawful zero-coordinate embedding; K=2 is strictly positive iid.

