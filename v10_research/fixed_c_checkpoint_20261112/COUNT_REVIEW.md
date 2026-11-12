# Independent mathematical review: restricted count obstruction

12 November 2026. Internal independent proof review, not formal verification, external peer review, or novelty certification.

No substantive gap found in the spectral/Fourier proof. Positivity of the two-step pair kernel gives a simple eigenvalue 1 and a uniform decaying remainder near zero. The two source parameters have the same zero mean and variance (1+h^2)/(1-h^2). Their local characteristic-function difference is bounded by C(|t|+N|t|^3)exp(-aNt^2)+Cr^N. Integrating gives O(1/N) per count/endpoint. A central interval of radius N^(2/3), plus the O(N) variance tail estimate, gives O(N^(-1/3)) total variation.

Self-loops force all unit-modulus spectral points to 0 and pi; M(t+pi)=-M(t) and b(t+pi)=b(t) correctly preserve the parity resonance. Endpoint probabilities are handled jointly throughout. The common-part risk reduction does not assume independence of count and endpoint.

Specify N>=2 and absorb the finite small horizons into C_h. The full-history estimator comparison requires N>=3. Randomized architectures must remain count-sufficient conditional on their source-independent seed; per-position random identifiers are not an allowed escape from the position-free hypothesis.

An independent floating diagnostic compared the 4x4 characteristic-function matrix formula with full enumeration in 120 finite cases (maximum discrepancy 2.23e-16), checked pi periodicity, and checked the variance coefficient numerically. These checks are not an asymptotic proof. The included check_count.py independently propagates the joint count/pair law, compares 27 cases with rational enumeration, and reports floating TV for larger lengths. Neither diagnostic establishes novelty or an unrestricted Transformer lower bound.
