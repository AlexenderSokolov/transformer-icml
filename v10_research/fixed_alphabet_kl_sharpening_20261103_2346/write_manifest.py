#!/usr/bin/env python3
"""Seal final research files after independent exact-file review."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
html=HERE/'fixed_alphabet_sharp_terminal_kl.v1.html'
review=HERE/'final_file_review.v1.md'
assert review.is_file(), 'Independent final-file review is required before sealing.'
assert sha(html) in review.read_text(), 'Review does not bind the exact HTML hash.'
verification=json.loads((HERE/'HTML_VERIFICATION.json').read_text())
assert verification['html_sha256']==sha(html)
assert verification['all_source_hashes_match']
final={
 'artifact':html.name,'sha256':sha(html),'bytes':html.stat().st_size,
 'composition':'sharp_kl_output_corollaries.v1.md','composition_sha256':sha(HERE/'sharp_kl_output_corollaries.v1.md'),
 'statistical_source_sha256':sha(HERE/'tilted_occupation_terminal_kl.candidate.v1.md'),
 'final_review':review.name,'final_review_sha256':sha(review),
 'mathematical_scope':'Fixed-A terminal forward-KL upper and matching minimax n-order; exact-real and specialized integer/dyadic outputs kept separate; A^5 upper factor not sharp growing-A dependence.',
 'novelty_certification':False,'mathematical_numerical_work':False,'external_upload':False,'repository_mutation':False,
 'source_fidelity':'All embedded documents pass exact conversion and normalized displayed-text equality.',
 'presentation':verification['rendering']}
(HERE/'FINAL_ARTIFACT.json').write_text(json.dumps(final,indent=2)+'\n')
files=[p for p in HERE.rglob('*') if p.is_file() and p.name not in {'MANIFEST.json','MANIFEST.sha256'} and 'qa' not in p.parts and '__pycache__' not in p.parts]
entries=[{'path':str(p.relative_to(HERE)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(files)]
manifest={'edition':'2026-11-04','artifact':html.name,'artifact_sha256':sha(html),
 'scope':'Sealed research package. This ledger excludes its own two encodings and optional presentation images.', 'files':entries}
(HERE/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
(HERE/'MANIFEST.sha256').write_text(''.join(e['sha256']+'  '+e['path']+'\n' for e in entries))
print(json.dumps({'artifact_sha256':sha(html),'manifest_sha256':sha(HERE/'MANIFEST.json'),'files':len(entries)},indent=2))
