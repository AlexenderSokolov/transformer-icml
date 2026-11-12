# Independent review: two-row variable-coefficient sensitivity lemma

2026-11-12. Verdict: PASS for the complete statement supplied by the author, reproduced below. No general PreLN or average-risk theorem is certified. This review independently derives the matrix product and checks 1,050 variable-coefficient cases against exact full-prefix recurrences.

## Reviewed statement and assumptions

Fix N>=3,D>=0. Two executions use the same architecture/parameters and have row-state Euclidean differences d_i^ell. Assume explicitly, at every layer ell=0,...,D-1,

    d_i^(ell+1) <= a_ell d_i^ell+(b_ell/i) sum_(j<=i)d_j^ell,
    a_ell,b_ell>=0.

Coefficients may depend on ell and N. Initially only raw row N-1 differs, with difference <=B0; all other initial states, INCLUDING readout row N, agree. The row-N readout is not initially supplied the differing predecessor or a free endpoint pair that reveals it. Readout is a shared Lout-Lipschitz function of final row N, not of the full historical bank.

Earlier differences remain zero by nonnegativity/induction. Define

    alpha_ell=a_ell+b_ell/(N-1),
    beta_ell=a_ell+b_ell/N, gamma_ell=b_ell/N.

The last two differences are bounded by the positive matrix [[alpha,0],[gamma,beta]] acting on their previous values, from initial vector(B0,0). Therefore

    d_N^D <= B0 sum_(r=0)^(D-1) gamma_r
                    product_(ell<r) alpha_ell product_(ell>r) beta_ell.

D=0 has an empty sum and d_N^0=0. Empty products equal1. Uniform a_ell<=a,b_ell<=b gives, for D>=1,

    d_N^D <= B0 (Db/N)(a+b/(N-1))^(D-1).

If a_ell<=1 and B_D=sum_ell b_ell, then

    d_N^D <= B0 (B_D/N) exp(B_D/(N-1)).

Approximating opposite predecessor signs on both words to absolute error <=epsilon<1 implies 2(1-epsilon)<=Lout d_N^D. If epsilon stays bounded away from1 and Lout B0 has an N-independent finite upper bound, this forces B_D=Omega(N). Only when b_ell also has a fixed finite upper bound does D=Omega(N) follow. Uniform fixed a>1 and b<infinity instead gives the weaker necessary D=Omega(log N). No sufficient construction is claimed.

## Independent product derivation and useful exact identity

The actual product order is M_(D-1)...M_0. A transfer at r first evolves the N-1 row through alpha_0,...,alpha_(r-1), transfers through gamma_r, then evolves row N through beta_(r+1),...,beta_(D-1). This proves the displayed order.

There is additional structure: every matrix is a_ell I+b_ell B for the SAME fixed matrix B. Thus these particular variable-coefficient matrices commute. They are not a test of generic noncommuting triangular products. Since gamma_ell=(N-1)(alpha_ell-beta_ell), the product-difference identity gives the exact off-diagonal entry

    (N-1)[product_ell alpha_ell-product_ell beta_ell].

For constant coefficients this reduces to (N-1)[(a+b/(N-1))^D-(a+b/N)^D]. Both formulas are valid when b=0, by direct subtraction, without division by a spectral gap. The original upper bound follows by bounding each nonnegative transfer term, not by assuming a positive a or b.

## Quantifiers for the a<=1 conclusion

Each transfer term's product is at most exp(sum_(ell!=r)b_ell/(N-1)); replacing that sum by B_D and summing b_r/N proves the exponential bound. If K bounds Lout B0 and epsilon<=epsilon0<1, put eta=2(1-epsilon0)/K when K>0. Then success requires x exp(3x/2)>=eta for x=B_D/N, since N/(N-1)<=3/2. In particular

    B_D/N >=min(1,eta exp(-3/2))>0.

This establishes the claimed Omega(N), not merely failure when B_D=o(N). If K=0, success is impossible directly. Growing Lout, B0, or a shrinking target separation invalidates this fixed-gap conclusion. Without b_ell<=b_fixed, a large single b_ell can supply a linear budget in constant depth; B_D=Omega(N) alone is not a depth lower bound.

For fixed a>1,b, the comparison d_N^D<=B0 Db(a+b/(N-1))^(D-1)/N implies Omega(log N) depth for fixed gap and bounded Lout B0. If b=0 transfer is impossible rather than merely logarithmically costly. D=0 is impossible for the same distinct-target condition. At D=1 the zeroth power is the identity convention1, including zero diagonal; no 0/0 argument is used.

## Scope and risk warning

The prefix sensitivity recurrence is an extra declared pathwise hypothesis. General full-PreLN residual networks do not automatically have a_ell<=1; LN, FFN, query/key, residual and readout gains must all be accounted for. Masks or position rules may also invalidate the b_ell/i dependence. Nonlocal initialization, different parameters on the two words, a terminal free-pair bypass, or a readout with access to other rows breaks the stated reduction.

This is a deterministic worst-word bit-recovery requirement. Two selected words can be extremely rare under a statistical source. The statement does NOT establish average prediction-risk loss, and useful theta prediction need not reconstruct individual predecessor bits. No transfer to an average-risk theorem is made in this review.

## Independent diagnostic

`check.py` checks 1,050 variable-coefficient sequences for N in{3,4,8,16,64}, D=0,...,20, ten deterministic pseudo-random rational choices per pair. It compares the two-row recurrence, the transfer sum and the complete N-row prefix recurrence exactly with Fraction arithmetic. The exponential bound is additionally compared in binary64. All pass. Matrices commute by construction; the reported noncommuting count is correctly zero. Tests verify the algebraic recurrence only, not whether a particular Transformer satisfies its premise.
