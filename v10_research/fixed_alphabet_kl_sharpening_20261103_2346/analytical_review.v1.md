# Exact-file analytical review: logarithm-squared terminal KL

3 November 2026. **PASS for the exact note identified below.** No numerical experiments, simulations, sample enumeration, training, uploads, or public repository changes were performed.

## Reviewed source and review scope

- Source: `log_squared_terminal_kl.v1.md`.
- SHA-256: `5121f41a8cea60692de1ab845d26aeb92155416f2d981ff3dd5da2c433c92488`.
- The entire frozen source, including its finite-parameter theorem, proof, readout transfer, marginal-bound example, and scope statements, was inspected.

This review followed analytical discussion with the author, including a suggestion to use the j+1 rescaling. It independently reconstructs and checks the resulting exact-file algebra and dependence arguments; it is not a claim of blind external peer review or wholly independent invention. The theorem is an upper bound, not a claim of optimality or literature priority.

## 1. Main finding

The stated U_new and V_new are valid for every finite A>=2 and n>=1, with the distinct arbitrary-initial and stationary values of c exactly as written. For each fixed A they imply

    sup E D_KL(p_{Y_n} || B_{Y_n})
        = O_A(log^2(n+2)/(n+1)).

The proof includes zero probabilities, deterministic rows, reducibility, periodicity, arbitrary initial pairs, and the actual terminal query. It does not condition transition counts to be binomial. At n=0 the separately stated log A bound is correct.

The logarithm-squared improvement is substantive: the logarithm attached to a small true coordinate mean is averaged with a target-specific occupation bound before the row probabilities are summed. It does not incur the additional harmonic factor that arose from applying one uniform t log t bound to every count.

## 2. Target-specific occupation and reciprocal moment

For a fixed target s, the suffix argument proves that the maximum over initial states B_m^s is nonincreasing in m. It does not require monotonicity for each individual initial state. The flag Y_m=s with fewer than w earlier copies of s can occur at most w times on a deterministic trajectory. Summing separately over the D starting states and then using max<=sum gives

    P(Y_n=s,J_s<w) <= Dw/(n+1)

under arbitrary initialization. The stationary n-window flag argument gives w/(n+1). Both proofs were checked, including the integer endpoints of the preceding n-position window.

Thus r=D/(n+1) or 1/(n+1), while c=Dr. Summing over the target states recovers the corresponding actual-terminal occupation bound. The summation-by-parts identity for 1/(J+1) includes J=0 and gives exactly c[1+log(n+1)]. No minimum stationary mass, mixing assumption, or positive transition lower bound is introduced.

## 3. Confidence event and terminal selection

There are A^2 categorical row stacks, A symbol indicators per stack, and n positive deterministic prefix lengths. The two-sided Bernstein union bound is therefore 2A^3 n exp(-t). The displayed t makes this at most (n+1)^-2. The j=0 inequality is deterministic.

Each row stack is unconditionally iid at each deterministic prefix. The original homogeneous source is obtained by consuming the next unused entry at each departure. On the simultaneous event, every row/prefix estimate can be evaluated pathwise at the actual terminal row and its count. Neither count conditioning nor terminal-selection independence is needed. Correlation among categorical indicator coordinates does not invalidate a union bound.

## 4. Rescaling and scalar constants

With x_b=(j+1)p_b and a_b=k_b+1, direct expansion gives

    sum_b h(x_b,a_b)
      =(j+1)D_KL(p||q)+(A-1)
        -(j+1)log[1+(A-1)/(j+1)].

The final remainder is nonnegative by log(1+u)<=u. The inequality direction in (6) is consequently correct. This is the essential reason that the displacement is p_b-1 rather than Ap_b-1, and that t>=1 suffices for every A. No hidden t>=A hypothesis survives.

On the Bernstein event, delta^2<=4zt+8t^2/9 and |p-1|<=1 give

    (x-a)^2<=8zt+(34/9)t^2.

For z>=16t the lower bound a>=z/2 holds. The resulting coefficient is 16+17/36, strictly smaller than 17. The large-mean branch therefore has the claimed 17t upper bound.

For z<16t, the count bound gives a<=24t, including the +1 pseudocount because t>=1. The inequality

    (z+p)log_+(z+p)<=z log_+(2z)+p log_+(2p)

is valid. It also follows from convexity of f(u)=u log_+u and f(z+p)<=one-half f(2z)+one-half f(2p), with f(0)=0. Since a>=1, dropping the nonpositive terms in h proves the stated small-mean bound.

Finally, sum_b p_b log_+(2p_b)<=log 2 because each logarithmic factor is at most log 2 and the probabilities sum to one. Combining the branches yields exactly

    D_KL(p||q)
      <=(24At+log 2)/(j+1)
        +sum_b p_b log_+(2jp_b) 1{jp_b<16t}.

This argument remains valid at j=0, p_b=0, and p_b=1. The notation for zero logarithmic terms is explicitly supplied in the source.

## 5. Low-mean expectation and row dependence

For each fixed row s and symbol b, p=p_s(b) is a fixed parameter. If p=0 the term is zero. Otherwise the strict event J_s p<T is exactly represented by J_s<ceil(T/p), including when T/p is an integer. The target-specific occupation bound therefore gives

    E[1{Y_n=s} p log_+(2J_s p) 1{J_s p<T}]
       <=r(T+p)log(2T)
       <=r(T+1)log(2T).

The ceiling need not be at most n: the occupation upper bound may exceed one and still be valid. There is no division by zero, and arbitrarily small positive p causes no failure.

Only after obtaining this bound for a fixed p does the proof sum over D rows and A symbols. This gives DAr(T+1)log(2T)=cA(T+1)log(2T), with the exact displayed T=16t. In particular it does not pull the probability of the randomly selected terminal row outside an expectation.

All terms used to dominate the good-event loss are nonnegative, so dropping the good-event indicator before applying the unconditional occupation bounds is legitimate. On its complement the deterministic log(n+A) loss cap gives the stated failure contribution. This proves the entire U_new expression and its cap V_new.

For fixed A, t=O_A(log(n+2)). The rare term t log(32t) is no larger than a constant times t^2 for t>=1, while the main term is t times a harmonic logarithm. Thus the claimed O_A(log^2 n/n) order follows. The explicit bound, rather than this fixed-A asymptotic notation, must be used when A grows.

## 6. Readout transfer and unchanged computation

The exact-real five-block approximation and output floor are unchanged. Applying its previously reviewed pointwise entropy-variational inequality with the new add-one expectation gives exactly

    E D_KL(p_{Y_n}||R)
       <=2V_new+2A(44A+1)^2/L.

The deterministic log[1+(A-1)L] cap is valid. The new proof does not give the estimator a true-probability input: z=jp and the branch split are analysis-only quantities. No architecture, parameter, data port, training, or arithmetic-backend change is required by this statistical refinement.

The side statement about D contexts and A possible outcomes is a valid adaptation of the proof. For an explicit general-D formula, its confidence union factor is 2DAn rather than 2A^3n, and c is D^2/(n+1) or D/(n+1). The second-order theorem already has D=A^2, so its displayed formulas are correct without modification. This is a clarification of the generalization, not a defect in the stated order-two result.

## 7. Marginal-bound barrier and attribution

The abstract example J uniform on {1,...,n}, W=log(n/J) satisfies both displayed marginal tails. Its expectation is

    E[W/J]=(1/n)sum_{j=1}^n log(n/j)/j.

The integrand log(n/x)/x is nonnegative and decreasing on [1,n]; comparison with its integral gives one-half log^2 n with discrepancy at most log n before division by n. Hence the claimed asymptotic expansion is correct.

This example demonstrates a limitation of arguments using only those two marginal inequalities. It is correctly not presented as a Markov-source lower bound or an optimality result for full-history add-one.

The cited HJW Remark 1 was checked against the locally preserved published text. It distinguishes the usual full-history estimator from its suffix average and states an open optimality question in the paper's setting. The note appropriately avoids claiming that the 2023 question remains open throughout all later literature. The local published-PDF path and the prior-proof relative path resolve as described.

## Verdict

**PASS** for source SHA-256 `5121f41a8cea60692de1ab845d26aeb92155416f2d981ff3dd5da2c433c92488`. No mathematical correction is required for its fixed-alphabet order-two theorem. The explicit initial-law distinctions, growing-alphabet limitations, analysis-only true-mean split, and nonoptimality qualifications must be retained.
