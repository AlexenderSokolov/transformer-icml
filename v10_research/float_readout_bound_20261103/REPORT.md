# Conditional numerical bridge from counter banks to the fixed-half pilot

3 November 2026. Deterministic mathematical analysis and rational arithmetic on existing half-mode weights; no random sampling, random initialization, training, publication, or modification of the source artifacts. This is a **conditional** error analysis, not certification of NumPy, OpenBLAS, or the actual pilot implementation. The floating counterexample remains valid: equal count banks need not give bitwise-identical pooled features. The result below bounds the potential *utility consequence* if its explicitly stated numerical premises are established.

## Model and clean mathematical problem

For M>=2 let L=floor(M/2), R=M-L, and x be the exact rational nine-vector reconstructed from (J,C1,D,E), protected terminal pair u, and M as in the four-counter note. Regard each saved binary64 parameter W, b, v, c as its exact real value, not an ideal unrounded original parameter. Let

  H_j=tanh(sum_i x_i W_ij+b_j),  r=sum_j H_j v_j+c,
  e=1/(M+2)^2, a=1-2e, q=e+a sigmoid(r),
  CE(t,q)= -t log q -(1-t) log(1-q).

Here t=(C1(clean)+1)/(J(clean)+2) is fixed from the clean word and lies in [0,1]. Interpret tanh, sigmoid and log as exact real functions, and fix a completely specified deterministic candidate evaluation protocol (including the layout, slot, batch size and backend). The endpoints are protected. Let the actual implementation's candidate score be U_float, and the above ideal bank score be U_ideal. The ideal vector is an identity over rationals; `four_counter.py:model_inputs` uses ordinary division and is not itself an exact rational utility oracle.

## A priori feature bound under an explicit reduction model

Let unit roundoff u=2^-53, gamma_n=nu/(1-nu), requiring nu<1. For n=M,L,R, suppose the pooling coefficient is correctly rounded binary64 RN(1/n), selected indicators are exactly 0 or 1, products by these indicators are exact, and each output is computed by a binary addition tree of at most n terms, each rounded to nearest, with at most n-1 additions on each summand's path. Assume no overflow, problematic underflow, flush-to-zero, extended precision store surprises, or other operations not covered by this graph. In particular binary64 coefficients and all nonzero intermediate sums are normal. These are **assumptions**, not established facts about `einsum`, its BLAS graph, or NumPy's division on the recorded backend.

If k selected indicators occur, the ideal rail is k/n. Since sums are nonnegative,

  |float rail - k/n| <= (k/n)[u+(1+u) gamma_(n-1)] <= d_n,
  d_n = u+(1+u) gamma_(n-1).

This applies to all six rails, including empty rails. Odd M uses L and R separately. Also, if 1/M is correctly rounded and normal, its error is <=u/M; the two terminal bits are exact. Thus use d=(d_M,d_M,d_L,d_L,d_R,d_R,0,0,u/M). More generally, all following formulas hold for independently proven abstract per-coordinate absolute errors d_i, regardless of the reduction method. A `gamma` bound can cover many tree and FMA orders, but cannot be attributed to a particular optimized backend merely from inspecting source or observing numerical agreement.

## Readout propagation, including arithmetic

Let V=sum_j |v_j| and S_i=sum_j |v_j||W_ij|. The exact readout is globally Lipschitz:

  |r(x_hat)-r(x)| <= sum_i S_i d_i,

because tanh is 1-Lipschitz. This inequality alone describes the mathematical readout applied exactly to perturbed input, not actual floating evaluation.

For the actual 9-by-32 affine map, additionally assume IEEE binary64 round-to-nearest and an operation graph where the usual absolute dot-product bound gamma_9 applies to each 9-term dot, followed by one rounded bias addition; similarly gamma_32 applies to the 32-term output dot followed by one rounded addition of c. Require finite values and no problematic underflow/overflow/FTZ, and no lower-precision or unmodeled operations. Define

  A_j=sum_i (1+d_i)|W_ij|,
  h_j=gamma_9 A_j + u[(1+gamma_9)A_j+|b_j|],
  T0=gamma_32 V + u[(1+gamma_32)V+|c|],
  T1=(1+gamma_32)(1+u)V.

If each implemented tanh differs by at most tau_h in absolute value from exact tanh at its actual floating input, a uniform bound on actual-vs-ideal logits is

  R = sum_i S_i d_i + sum_j |v_j| h_j + T0 + T1 tau_h.      (1)

The last coefficient includes both activation error and its effect on output-dot error. Bias, weight representation, rounded multiply/accumulate and final addition are accounted for relative to the *stored* weights under those premises. Any weight conversion, TF32, mixed precision, nonstandard reduction, underflow or larger/different error requires its own term. We have not established a global tanh accuracy bound for this platform. `bounds.json` reports (1) with tau_h=0 as a diagnostic component, not a complete actual-pilot certificate.

## Correct smoothed cross-entropy sensitivity and remaining error

For q=g(r)=e+a sigmoid(r), write s=sigmoid(r). Since g'=a s(1-s) satisfies 0<=g'<=min(g,1-g), for any t in [0,1],

  |d CE(t,g(r))/dr| = |g'[(1-t)/(1-g)-t/g]| <= 1.

This is a direct global logit-to-CE bound. The CE function itself is **not** 1-Lipschitz in its probability argument: on [e,1-e] its valid general probability Lipschitz constant is 1/e (sharper constants may be available at a fixed t). Smoothing here is an affine transform of sigmoid, not a hard clamp. Its comparison does not permit silently dropping float errors in computing e, sigmoid, q or logs.

Suppose additionally that actual q_float differs from exact g(r_float) by at most tau_q uniformly over the candidates, where 0<=tau_q<e. This single assumption includes implemented sigmoid, rounded epsilon and final affine output. Then both endpoints lie in [e-tau_q,1-e+tau_q]. Suppose the float target differs from exact t by at most beta and remains in [0,1], and the actually returned floating CE differs from exact CE(float target,q_float) by at most tau_CE, uniformly. This last term covers log, log1p, multiplication, addition and exceptional behavior; it is not assumed zero in a complete certificate. Then

  |U_float-U_ideal| <= epsilon
  epsilon = R + tau_q/(e-tau_q)
              + beta log[(1-e+tau_q)/(e-tau_q)] + tau_CE.      (2)

Under correctly rounded float64 division with exact integer numerator and denominator, beta<=u for this target when counts and their increments remain exactly representable. Prove that premise for the actual statistics reduction before using it. Equation (2) is conditional: no platform-independent tau_h, tau_q or tau_CE was established here. NaNs, infinities, accidental endpoint outputs, non-determinism, and a failure of the stated bounds are excluded. A direct bound on |U_float - CE(t,g(r_float))| can replace the last three terms and may be much tighter.

## Approximate maximization, not exact floating equivalence

For a finite fixed legal candidate set, let z_star maximize U_float under the specified evaluation protocol and let z_hat maximize U_ideal over all reachable banks, with a legal witness. Uniform (2) gives

  U_float(z_star)-U_float(z_hat) <= 2 epsilon.

If the bank optimizer returns an ideal score within eta of the ideal maximum, the corresponding guarantee is 2 epsilon+eta. This includes the ideal utility comparison error only when eta is actually established; an ordinary floating utility call does not magically provide eta=0. The constant 2 is sharp without further information (two ideal-tied candidates with float errors of opposite sign). Score differences below this uncertainty can reverse ordering, so no exact floating argmax or exact tie claim follows. If batch context changes score, define a candidate-to-slot-and-filler protocol or consistently bind each candidate to its position in a complete evaluation batch before applying the uniform bound.

## Fixed checkpoint values

`bounds.py` reads all ten saved `half_edit_{0,50,100,150,200}.npz` files in smoke and independent replay without constructing a model. It interprets each float exactly as a rational, uses exact Fraction arithmetic in (1) with tau_h=0, and rounds decimal displays upward. SHA-256 input bindings and all horizon-specific figures are in `bounds.json`. The five smoke/replay norm and bound values coincide at displayed precision; they are separately bound by hashes. At step 200, S_0+...+S_5 <=14.928373672821, V<=9.7440180599953. Conditional R excluding tau_h is:

  M=64:   <=1.2692987090343e-13
  M=128:  <=1.9670358768025e-13
  M=256:  <=3.3625329805200e-13
  M=1025: <=1.1746381927788e-12

Add at most 9.7440180599953*tau_h (the file gives upward-rounded coefficient), then the additional terms in (2). M=64 and 128 were training lengths, 256 an evaluation length; M=1025 is the float-collision horizon, not a pilot evaluation result. At M=1025 this checkpoint's conditional d_M is about 1.138e-13; the observed counterexample's single ULP is covered if the stated graph premise applies. The constructed counterexample uses a deliberately huge W=2^53 and has a radically different sensitivity. Small saved-weight sensitivity does not erase bitwise collision or prove any actual trained checkpoint has a particular maximum; nor do these results cover learned-position or random-weight pooling heads.

## Reproduction, checks, and limitations

From repository root:

  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python v10_research/float_readout_bound_20261103/bounds.py
  python v10_research/float_readout_bound_20261103/test_bounds.py

The test deterministically exhausts words at M=2..7 for all six rational rails and a reference left-to-right binary64 pool, and checks the analytical derivative inequality on a rational grid plus a sharp 2-epsilon example. The exhaustive finite test is a diagnostic, not a proof of arbitrary M, actual einsum order, tanh error, target computation, or CE/log errors. The saved files `bounds.log`, `test_bounds.log`, `bounds.json` provide outputs and source/settings records. No model invocation is needed. Input weights are existing exploratory checkpoints, not evidence about unseen models, statistical performance, or generalization.
