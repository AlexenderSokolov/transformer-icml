#!/usr/bin/env python3
"""Deterministic offline proof packaging. No mathematical numerical tests."""
from pathlib import Path
from html import escape
import hashlib, json, re, shutil, subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'fixed_alphabet_sharp_terminal_kl.v1.html'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
assert sha(HERE/'tilted_occupation_terminal_kl.candidate.v1.md') == 'c42b6f1d86c9c91aa6ba8257a86c613150e6fb477deb549cd70d1e7b79548281'
copies = {
 'sources/fixed_alphabet_terminal_kl.v1.md': 'v10_research/fixed_alphabet_kl_upgrade_20261103_2300/fixed_alphabet_terminal_kl.v1.md',
 'reviews/exact_real_analytical_review.v1.md': 'v10_research/fixed_alphabet_kl_upgrade_20261103_2300/independent_analytical_review.v1.md',
 'sources/precision_budget_constructive_candidate.v1.md': 'v10_research/fixed_alphabet_precision_upgrade_20261103_2321/precision_budget_constructive_candidate.v1.md',
 'reviews/precision_analytical_review.v1.md': 'v10_research/fixed_alphabet_precision_upgrade_20261103_2321/independent_analytical_review.v1.md',
 'reviews/precision_adversarial_review.v1.md': 'v10_research/fixed_alphabet_precision_upgrade_20261103_2321/independent_adversarial_review.v1.md',
 'sources/targeted_prior_art_audit.v2.md': 'v10_research/terminal_kl_sharp_rate_literature_20261103_2358/targeted_prior_art_audit.v2.md',
}
for target, source in copies.items():
    dest = HERE/target
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists(): assert dest.read_bytes() == (ROOT/source).read_bytes(), target+' changed'
    else: shutil.copyfile(ROOT/source, dest)
assert sha(HERE/'sources/fixed_alphabet_terminal_kl.v1.md') == 'ca5e4d0c0ee5d7b20c8dcd5a0a58775d0e570bf3571837c6c2750e4e964c4a58'
assert sha(HERE/'sources/precision_budget_constructive_candidate.v1.md') == 'e555323ee18b39b0003863e9d41084d6f2222a575c340b0a9bb8c87213d01a16'

sections = [
 ('synthesis', 'Main result and two distinct output corollaries', 'sharp_kl_output_corollaries.v1.md', True),
 ('statistical-proof', 'Complete row-tilted terminal KL proof', 'tilted_occupation_terminal_kl.candidate.v1.md', True),
 ('statistical-review-one', 'First exact-source analytical review', 'tilted_occupation_analytical_review.v1.md', False),
 ('statistical-review-two', 'Second independent analytical review', 'tilted_occupation_independent_review.v1.md', False),
 ('exact-real-proof', 'Complete five-block exact-real construction and proof', 'sources/fixed_alphabet_terminal_kl.v1.md', False),
 ('exact-real-review', 'Independent exact-real prerequisite review', 'reviews/exact_real_analytical_review.v1.md', False),
 ('precision-proof', 'Complete specialized integer and dyadic evaluator proof', 'sources/precision_budget_constructive_candidate.v1.md', False),
 ('precision-review-one', 'First independent specialized-evaluator review', 'reviews/precision_analytical_review.v1.md', False),
 ('precision-review-two', 'Second adversarial specialized-evaluator review', 'reviews/precision_adversarial_review.v1.md', False),
 ('prior-art', 'Bounded primary-source prior-art audit', 'sources/targeted_prior_art_audit.v2.md', False),
 ('matching-lower', 'Primary-source matching minimax lower-bound audit', 'primary_source_matching_lower_audit.v1.md', False),
 ('previous-statistical-proof', 'Preserved log-squared predecessor', 'log_squared_terminal_kl.v1.md', False),
 ('previous-statistical-review', 'Analytical review of the log-squared predecessor', 'analytical_review.v1.md', False),
]
def convert(path, prefix):
    text = subprocess.check_output(['pandoc', str(path), '--from=markdown-smart-superscript-subscript+autolink_bare_uris', '--to=html5', '--wrap=none'], text=True)
    text = re.sub(r'\bid="([^"]+)"', lambda m: 'id="'+prefix+m.group(1)+'"', text)
    return re.sub(r'href="#([^"]+)"', lambda m: 'href="#'+prefix+m.group(1)+'"', text)

bindings = {'scope':'Offline research composition; no mathematical numerical experiments, external uploads, or public repository mutations.',
 'reviewed_statistical_source_sha256':sha(HERE/'tilted_occupation_terminal_kl.candidate.v1.md'),
 'final_file_review':'A separate review must bind final HTML bytes; this builder makes no final-file-review claim.',
 'files':[{'section_id':sid,'title':title,'path':path,'sha256':sha(HERE/path),'bytes':(HERE/path).stat().st_size} for sid,title,path,_ in sections],
 'copied_sources':[{'stored_path':target,'original_workspace_relative_path':source,'sha256':sha(HERE/target)} for target,source in copies.items()]}
(HERE/'SOURCE_BINDINGS.json').write_text(json.dumps(bindings,indent=2)+'\n')
parts=[]
for sid,title,path,opened in sections:
    fragment=convert(HERE/path, sid+'-')
    if opened:
        parts.append(f'<section id="{sid}" class="proof-section"><!-- BEGIN {sid} -->\n{fragment}<!-- END {sid} --></section>')
    else:
        parts.append(f'<details id="{sid}"><summary>{escape(title)}</summary><div class="appendix"><!-- BEGIN {sid} -->\n{fragment}<!-- END {sid} --></div></details>')
nav='\n'.join(f'<li><a href="#{sid}">{escape(title)}</a></li>' for sid,title,_,_ in sections)
rows='\n'.join(f'<tr><td>{escape(e["path"])}</td><td><code>{e["sha256"]}</code></td></tr>' for e in bindings['files'])
style=(ROOT/'v10_research/fixed_alphabet_precision_upgrade_20261103_2321/style_header.v1.html').read_text()
style=style.replace('</style>', '.appendix h1{font-size:25px}.proof-section{margin-top:3em}.integrity{font-size:13px}.review-note{color:#465764}summary{padding:.5em 0}details:target{scroll-margin-top:20px}footer{margin-top:3em;color:#526271;font-size:13px}@media print{details>div{display:block!important}summary{font-size:12px}.proof-section{break-before:page}}\n</style>')
html=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Offline source-bound proof package for fixed-alphabet terminal forward KL at logarithmic rate, with distinct exact-real and specialized finite-bit corollaries.">
<title>Fixed alphabet terminal KL at logarithmic rate</title>
{style}</head><body>
<header class="edition"><p>Research proof package · 4 November 2026 · Local offline edition</p></header>
<p class="review-note"><strong>Reading status.</strong> The new statistical proof has two passing analytical reviews. The complete exact-real construction and specialized integer/dyadic evaluator have separate reviews, and a primary-source audit verifies the matching fixed-alphabet minimax lower bound. This package preserves original candidate-status paragraphs as historical source text and identifies the subsequent reviews. Analytical review is not formal verification, external peer review, or novelty certification. The companion final-file receipt identifies the precise HTML reviewed.</p>
<nav aria-label="Document contents"><p><strong>Contents</strong></p><ol>{nav}<li><a href="#integrity-ledger">Source integrity ledger</a></li></ol></nav>
<main>
{chr(10).join(parts)}
</main>
<section id="integrity-ledger" class="integrity"><h2>Source integrity ledger</h2>
<p>Every proof and review listed here is embedded in full. Text uses plain mathematical notation so that no equation service, script, font download or other network resource is required. Expand the appendices to read prerequisite proofs and reviews. External links are citations only. Source filenames retain their original versions; the JSON bindings also record copied-source provenance. The final HTML hash is recorded separately to avoid a circular self-hash.</p>
<table><thead><tr><th>Exact source file</th><th>SHA-256</th></tr></thead><tbody>{rows}</tbody></table></section>
<footer>No mathematical numerical work, model training, external upload or public repository mutation was performed for this package. The statistical theorem concerns fixed alphabets with an A^5 upper factor; its finite-bit corollary concerns only the explicitly specified arbitrary-precision evaluator.</footer>
</body></html>
'''
OUT.write_text(html)
print(json.dumps({'path':str(OUT),'sha256':sha(OUT),'bytes':OUT.stat().st_size,'embedded_files':len(sections)},indent=2))
