# SB001 v2 correction handoff

Root-requested scope/resource clarifications completed; fresh independent review pending.

- General Q band sufficient risk multiplier is now explicitly (K,c_-)-dependent, with value `(2^13+2)K^(5/2)+(2C_K+2K-1)/c_-`. SB2's special schedule remains K-only.
- Comparison family now has AT MOST D retained coordinates. Statistical zero-padding only embeds into BA001's exact-D experiment; actual implementation and costs retain exactly K³ coordinates. No free physical exact-D padding is claimed.
- Main rates and actual ledger unchanged. Frozen v1 plus every file in its original manifest verified byte-identical.
- No active new theorem identifier or filename uses SP001. Only historical rename notes mention the old provisional collision; unrelated accepted SP001 untouched.

Proof: `SB001_loglog_effective_score_budget_v2.md`
SHA-256: `d10086be4d358e322872daffad4dd10572588d6dcffaecbffefc409df6a217b7`

The existing exact-rational diagnostics are unchanged and continue to support the unchanged mathematical map; the v1 audit is not represented as a fresh v2 review.
