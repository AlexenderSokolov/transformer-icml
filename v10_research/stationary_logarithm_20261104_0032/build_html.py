#!/usr/bin/env python3
"""Offline source-preserving proof packaging, not numerical mathematical testing."""
from pathlib import Path
from html import escape
import hashlib, json, re, shutil, subprocess
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
OLD=ROOT/'v10_research/stationary_row_tilt_20261104_0023'
OUT=HERE/'stationary_addone_sharp_log.v1.html'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
expected={
 'stationary_addone_sharp_log.candidate.v1.md':'90e949efc52cd8f3d57108ca334f9083a9858950183dd8e6f60d6664d92c6195',
 'stationary_addone_sharp_log.independent_review.v1.md':'02ef46cd71c27d218f72942e80484f36fc23253e16779ae49cb989d670335d23',
 'stationary_addone_sharp_log.redteam_review.v1.md':'05935d27057e2038dbb2033b97da78e845a7f13c966235bcbedd8cfc78d63df6',
 'stationary_sharp_output_corollaries.v1.md':'cd2379246d2ca2a3ce56ac9e32ea41c8c83b26327424f303d16d015668d587ef',
 'stationary_addone_literature_status.20261104.md':'79b16421ec826c6e0b80c4a987e1bd0a104706cc91db3341afe9553f30b995ee',
}
for p,h in expected.items(): assert sha(HERE/p)==h,p+' modified'
copies={
 'sources/fixed_alphabet_terminal_kl.v1.md':OLD/'sources/fixed_alphabet_terminal_kl.v1.md',
 'reviews/exact_real_analytical_review.v1.md':OLD/'reviews/exact_real_analytical_review.v1.md',
 'sources/precision_budget_constructive_candidate.v1.md':OLD/'sources/precision_budget_constructive_candidate.v1.md',
 'reviews/precision_analytical_review.v1.md':OLD/'reviews/precision_analytical_review.v1.md',
 'reviews/precision_adversarial_review.v1.md':OLD/'reviews/precision_adversarial_review.v1.md',
 'sources/primary_source_matching_lower_audit.v1.md':OLD/'sources/primary_source_matching_lower_audit.v1.md',
 'sources/prior_stationary_output_corollaries.v1.md':OLD/'stationary_output_corollaries.v1.md',
 'reviews/prior_stationary_output_corollaries.independent_review.v1.md':OLD/'stationary_output_corollaries.independent_review.v1.md',
 'sources/tilted_occupation_terminal_kl.candidate.v1.md':OLD/'sources/tilted_occupation_terminal_kl.candidate.v1.md',
 'reviews/tilted_occupation_independent_review.v1.md':OLD/'reviews/tilted_occupation_independent_review.v1.md',
}
for dst,src in copies.items():
    p=HERE/dst;p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists(): assert p.read_bytes()==src.read_bytes(),dst+' modified'
    else: shutil.copyfile(src,p)
sections=[
 ('corollaries','Results and network output corollaries','stationary_sharp_output_corollaries.v1.md',True),
 ('stationary-proof','Complete sharp stationary add one proof','stationary_addone_sharp_log.candidate.v1.md',True),
 ('stationary-review','First independent exact source mathematical review','stationary_addone_sharp_log.independent_review.v1.md',False),
 ('redteam-review','Second independent adversarial mathematical review','stationary_addone_sharp_log.redteam_review.v1.md',False),
 ('literature-status','Targeted literature status audit through November 2026','stationary_addone_literature_status.20261104.md',False),
 ('exact-real-proof','Complete inherited five block construction','sources/fixed_alphabet_terminal_kl.v1.md',False),
 ('exact-real-review','Independent exact real prerequisite review','reviews/exact_real_analytical_review.v1.md',False),
 ('precision-proof','Complete specified integer and dyadic evaluator','sources/precision_budget_constructive_candidate.v1.md',False),
 ('precision-review','Independent evaluator prerequisite review','reviews/precision_analytical_review.v1.md',False),
 ('precision-adversarial-review','Adversarial evaluator and guard range review','reviews/precision_adversarial_review.v1.md',False),
 ('prior-corollaries','Historical output composition with prior logarithm','sources/prior_stationary_output_corollaries.v1.md',False),
 ('prior-corollary-review','Independent historical output composition review','reviews/prior_stationary_output_corollaries.independent_review.v1.md',False),
 ('hjw-audit','Primary source HJW model and lower bound audit','sources/primary_source_matching_lower_audit.v1.md',False),
 ('all-start-proof','Preserved arbitrary start theorem','sources/tilted_occupation_terminal_kl.candidate.v1.md',False),
 ('all-start-review','Independent arbitrary start theorem review','reviews/tilted_occupation_independent_review.v1.md',False),
]
def convert(path,prefix):
    s=subprocess.check_output(['pandoc',str(path),'--from=markdown-smart-superscript-subscript+autolink_bare_uris','--to=html5','--wrap=none'],text=True)
    s=re.sub(r'\bid="([^"]+)"',lambda m:'id="'+prefix+m.group(1)+'"',s)
    return re.sub(r'href="#([^"]+)"',lambda m:'href="#'+prefix+m.group(1)+'"',s)
bindings={
 'scope':'Standalone offline research package. Source-preserving conversion and integrity checks are not numerical mathematical experiments.',
 'final_file_review':'Separate final_file_review.v1.md must bind the final HTML bytes. Original candidate labels and historical rate limitations are preserved.',
 'review_boundary':'Two independent exact-source analytical reviews pass the new mathematical proof. Substantive conclusions remain conditional on independent external review; current literature priority is not established.',
 'files':[{'section_id':sid,'title':title,'path':p,'sha256':sha(HERE/p),'bytes':(HERE/p).stat().st_size} for sid,title,p,_ in sections],
 'copied_sources':[{'stored_path':dst,'original_workspace_relative_path':str(src.relative_to(ROOT)),'sha256':sha(HERE/dst)} for dst,src in copies.items()],
 'primary_publication':{'doi':'https://doi.org/10.1109/TIT.2023.3239508','author_preprint':'https://arxiv.org/abs/2106.13947v2','published_pdf_sha256':'375c730cb4c9f6dd2eaa4439e59800764faeddbebee73f220e22d6d2cf3116a3','locations':['Theorem 1 and Remark 1, p. 3921','Theorem 22 and terminal loss, p. 3942','Theorem 24, pp. 3944-3945']},
}
ledger=HERE/'SOURCE_BINDINGS.json'
if ledger.exists() and not (HERE/'INITIAL_SOURCE_BINDINGS.v1.json').exists(): shutil.copyfile(ledger,HERE/'INITIAL_SOURCE_BINDINGS.v1.json')
ledger.write_text(json.dumps(bindings,indent=2)+'\n')
parts=[]
for sid,title,p,opened in sections:
    fragment=convert(HERE/p,sid+'-')
    if opened: parts.append(f'<section id="{sid}" class="proof-section"><!-- BEGIN {sid} -->\n{fragment}<!-- END {sid} --></section>')
    else: parts.append(f'<details id="{sid}"><summary>{escape(title)}</summary><div class="appendix"><!-- BEGIN {sid} -->\n{fragment}<!-- END {sid} --></div></details>')
nav='\n'.join(f'<li><a href="#{sid}">{escape(title)}</a></li>' for sid,title,_,_ in sections)
rows='\n'.join(f'<tr><td>{escape(e["path"])}</td><td><code>{e["sha256"]}</code></td></tr>' for e in bindings['files'])
style=(ROOT/'v10_research/fixed_alphabet_precision_upgrade_20261103_2321/style_header.v1.html').read_text()
style=style.replace('</style>', '.appendix h1{font-size:25px}.proof-section{margin-top:3em}.integrity{font-size:13px}.review-note{color:#465764}summary{padding:.5em 0}details:target{scroll-margin-top:20px}footer{margin-top:3em;color:#526271;font-size:13px}@media print{details>div{display:block!important}summary{font-size:12px}.proof-section{break-before:page}}\n</style>')
html=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Full stationary terminal KL proof with the sharp alphabet dependent logarithm, exact real and specified finite bit network corollaries, and careful HJW comparisons.">
<title>Sharp stationary rates for full history add one prediction</title>
{style}</head><body>
<header class="edition"><p>Research proof package · 4 November 2026 · Offline edition</p></header>
<h1>Sharp stationary rates for full history add one prediction</h1>
<p><strong>Main result.</strong> For a stationary second-order source on A symbols observed for n transitions, the unchanged full-history add-one predictor at the actual terminal pair satisfies</p>
<pre>Expected forward KL ≤ min&#123;log(n+A),
  14000 A³/(n+1) [1+log₊((n+1)/A³)]&#125;,    A ≥ 2, n ≥ 1.</pre>
<p>The complete proof retains terminal selection, allows zero probabilities, reducibility and periodicity, and assumes no mixing. It combines a one-count row tilt with the target stationary mass and a weighted low-count loss bound. Exact-real five-block and specified integer/dyadic outputs inherit the same stationary order through their established support floors and pathwise approximation bounds.</p>
<p><strong>Rate comparison.</strong> With N=n+2 observed symbols, this matches the HJW second-order minimax order A³/N log(N/A³) throughout their stated growing-alphabet range, after a harmless enlargement of its unspecified constant. For fixed A ≥ 2, the rate is Θ_A(log n/n). The sufficient growing-alphabet consistency condition becomes A³/n → 0.</p>
<p><strong>First-order scope.</strong> The same statistical argument gives ordinary stationary k-state add-one risk O(k²/N [1+log₊(N/k²)]). For k ≥ 3 this matches HJW Theorem 1. Conditional on independent external review, it is a potential answer to the specific question stated in their 2023 Remark 1. Current literature priority is not established. Binary first-order prediction remains exceptional: its minimax rate is Θ(log log N/N), which this argument does not attain.</p>
<p><strong>Literature status.</strong> The embedded bounded search found the question explicitly open in Han’s February 2025 slides and found no resolving unrestricted full-history add-one theorem in the later primary sources checked through 4 November 2026. The 2026 tutorial still uses suffix averaging for unrestricted achievability. This search is not exhaustive, and classical excursion and perturbation methods are acknowledged; no novelty or priority is certified.</p>
<p class="review-note"><strong>Review status.</strong> Two independent exact-source mathematical audits pass the new proof. The inherited architecture and arithmetic proofs and their reviews are reproduced below. These internal analytical reviews are not formal verification, external peer review, novelty certification or implementation testing. Substantive conclusions remain conditional on independent external review. Original candidate labels and older rate limitations are preserved in historical sources; the leading result and current corollaries state the new refinement. The separate final-file review records the exact HTML reviewed.</p>
<nav aria-label="Document contents"><p><strong>Contents</strong></p><ol>{nav}<li><a href="#integrity-ledger">Source integrity ledger</a></li></ol></nav>
<main>{chr(10).join(parts)}</main>
<section id="integrity-ledger" class="integrity"><h2>Source integrity ledger</h2>
<p>All listed proofs and reviews are embedded in full. Equations are plain text and require no equation service, script, external font or other network resource. Expand appendices to read inherited proofs and reviews. External links are citations only. Copied-source provenance and source hashes are recorded in SOURCE_BINDINGS.json. The final HTML hash is recorded separately to avoid a circular self-hash.</p>
<table><thead><tr><th>Exact source file</th><th>SHA-256</th></tr></thead><tbody>{rows}</tbody></table></section>
<footer>No mathematical numerical experiments, simulations, training or public repository mutations were performed. This preparation record predates public publication. The finite-bit theorem concerns only the stated growing-precision integer/dyadic evaluator, not generic IEEE or software execution.</footer>
</body></html>'''
OUT.write_text(html+'\n')
print(json.dumps({'path':str(OUT),'sha256':sha(OUT),'bytes':OUT.stat().st_size,'embedded_files':len(sections)},indent=2))
