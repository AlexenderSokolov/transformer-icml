# Output-coordinate packing: targeted prior-art comparison

Checked 2026-11-02, after the stage-six scientific freeze. This note is not a novelty certification.

Primary source: Uss et al., *Predicting High-precision Depth on Low-Precision Devices Using 2D Hilbert Curves*, ICML 2025, PMLR 267:60635–60656, https://proceedings.mlr.press/v267/uss25a.html. Read the abstract and Sections 2.1–2.4 of the authors' arXiv v2, dated 18 October 2025: https://arxiv.org/html/2405.14024v2 . No claim to have audited the full experiments or appendices.

The paper represents a high-resolution scalar using two low-precision curve coordinates and reconstructs it by postprocessing. It relates curve length to additional effective bits, discusses discontinuous coarse/fine representations and self-avoidance, and uses nearest-curve decoding. Its quantization-noise reduction discussion requires stated small-noise and distributional assumptions. Thus multi-coordinate output packing and geometric reconstruction are established ideas, not a new conceptual claim of FG001 or IC001.

Our comparison is an inference from the inspected sections: FG001/IR001/IC001 instead ask an IID statistical minimax question under explicit bounded-primitive causal depth, finite evaluator, interface capacity and paid computation. The present fold-specific perturbation investigation must not be presented as refuting their separately specified Hilbert construction or empirical noise results. This limited comparison does not exclude a closer theorem elsewhere.

The standard ReLU tent iteration is already attributed in FG001 to Telgarsky (2016), Section 3.3. Earlier depth_companding_comparison.md separately distinguishes weight-precision conversion from output-summary grid precision.
