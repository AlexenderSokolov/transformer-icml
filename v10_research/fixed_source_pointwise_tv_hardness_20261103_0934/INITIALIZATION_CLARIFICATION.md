# Initial-pair law and the all-zero history

2026-11-03. This additive clarification preserves `RESEARCH_NOTE.md` unchanged. The main source construction explicitly starts from its iid stationary pair law, which gives P(H=0^(M+2))=(1-p)^(M+2) for p=1/M² and supports the stated high-probability claim.

The transition table itself, irrespective of the initial pair law mu, has P²(u,v)=Pi(v) for all pair states u,v, with Pi=Bernoulli(p) tensor Bernoulli(p), and therefore admits the beta=1 certificate. With an arbitrary initial pair law mu, however,

  P_mu(H=0^(M+2)) = mu(00) (1-p)^M.

This need not be large and is zero when mu(00)=0. A pointwise conditional statement about that observed history under this source is meaningful only when mu(00)>0; with mu(00)=0 it is a null history, and the stationary-start occurrence guarantee cannot be imported. When mu(00)>0, the true next-symbol conditional law remains Bernoulli(p) because every transition row of the fixed table has success probability p. The construction's source-independent action maximizing q and all fixed-h rational inequalities are unchanged. No new experiment, sampling, or alteration of a retained artifact was performed for this clarification.
