# Clarification and independent exact record

The phrase “includes all statistical-scale budgets” in NOTE.md is asymptotic, not a finite-uniform claim: for a fixed C>0 and integer k≤C sqrt(M), the theorem's hypothesis k≤floor(M/1024) follows when M≥(1024 C)^2 (and M≥8). No such inclusion is claimed below that threshold.

The original diagnostic.log was not overwritten and does not contain n, individual binomial summands or exact numerator and denominator of each tail; those outputs were not retained in that run, and some float-rendered tails underflow. DIAGNOSTIC_NOTES.md discloses this. Rather than rerun or reconstruct the original outputs, check_comprehensive.py makes a separate deterministic, exact-arithmetic check on the same declared 60 cases, saving comprehensive_records.jsonl with every case's inputs, n, k, match probability, mean, threshold, included upper index, common denominator, every exact binomial-term numerator, total numerator, and comparison result. The exact check compares the tail against (1023/1024)^M, which is no greater than exp(−M/1024). This diagnostic is a finite check, not a substitute for the proof. No randomness or model initialization was used.

NOTE.md SHA-256 7ec2be2957f705b844cbae6d2a1b8325d6580bd655581b3df3daaba1fa493ea6.
