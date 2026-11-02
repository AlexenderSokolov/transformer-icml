# Post-stage-eight robustness screen

Read on 2 November 2026. This note is later than the stage-eight scientific and artifact freezes and is not used to establish those results. This is a limited primary-source comparison, not a novelty certificate.

## Gaitonde and Mossel, 2025

Jason Gaitonde and Elchanan Mossel, *On Algorithmic Robustness of Corrupted Markov Chains*, arXiv:2507.15176v1, 21 July 2025. Primary source: https://arxiv.org/html/2507.15176v1 . Read abstract and Sections 1, 1.1 and 1.2; proof sections were not audited.

Their input is a corrupted transition matrix. Definition 1.2 controls the rowwise absolute perturbation averaged under the original stationary law. The target is the original stationary distribution. Their PageRank regularization has recovery guarantees under a spectral gap and a suitable restart distribution. This differs from a strict number of replacements in a realized word with the actual terminal next-law as target. The comparison does not exclude other relevant results in their references.

## Chen, Koehler, Moitra and Yau, 2021

Sitan Chen, Frederic Koehler, Ankur Moitra and Morris Yau, *Kalman Filtering with Adversarial Corruptions*, arXiv:2111.06395v1, 11 November 2021. Primary source: https://arxiv.org/abs/2111.06395v1 . Read metadata and abstract only, not the 57-page proof text.

This work studies linear quadratic estimation of a linear dynamical-system trajectory under corrupted measurements, with comparison to an algorithm knowing corruption locations. It is relevant background for dependent robust inference, but the inspected abstract does not establish the finite-alphabet unknown-transition actual-terminal prediction rates in this project. No claim of disjointness from every theorem in the full paper is made.

## Search boundary

Generic searches combined Markov prediction, adversarial corruption, Hamming contamination, and unknown contamination. Many results concerned corrupted dynamics, continuous physical trajectories or unrelated inverse problems. No unpublished proof or private source file was transmitted. Search results with publication dates beyond the current research date were not used. Failure to locate an identical rate in this short search is not evidence of priority.
