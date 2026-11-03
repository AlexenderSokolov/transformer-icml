"""Check manuscript source freeze, references, preserved proofs, and build health.
Run after build_local.sh. The PDF byte hash may vary across rebuilds because of
TeX timestamps/IDs; this checker does not promise deterministic PDF identity.
"""
from pathlib import Path
from collections import Counter
import hashlib,json,re,subprocess
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
freeze=json.loads((HERE/'verification/SCIENTIFIC_SOURCE_FREEZE.json').read_text())['files']
for path,h in freeze.items(): assert sha(HERE/path)==h,path
texts=[(HERE/'main.tex').read_text()]+[p.read_text() for p in (HERE/'sections').glob('*.tex')]
labels=Counter(v for t in texts for v in re.findall(r'\\label\{([^}]+)\}',t))
refs={v for t in texts for v in re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',t)}
assert all(n==1 for n in labels.values())
assert refs<=labels.keys(),refs-labels.keys()
cites={v.strip() for t in texts for c in re.findall(r'\\cite\w*(?:\[[^\]]*\])?\{([^}]+)\}',t) for v in c.split(',')}
bib=set(re.findall(r'@\w+\{([^,]+),',(HERE/'references.bib').read_text()))
assert cites<=bib,cites-bib
base=ROOT/'v10_research/resumption_20261103/recovered_science/positional_manuscript_finite_20261102'
for f in ['proofs_positive.tex','proofs_negative.tex','proofs_finite_horizon.tex']:
 assert sha(HERE/'sections'/f)==sha(base/'sections'/f),f
log=(HERE/'build/main.log').read_text()
assert not re.search(r'Overfull|Underfull|Warning|undefined|^!',log,re.M)
info=subprocess.check_output(['pdfinfo',str(HERE/'build/main.pdf')],text=True)
assert re.search(r'^Pages:\s+55$',info,re.M)
assert re.search(r'^Author:\s*$',info,re.M)
assert re.search(r'^JavaScript:\s+no$',info,re.M)
print(json.dumps({'status':'PASS_STRUCTURE_AND_BUILD_NOT_PROOF_REVIEW','source_files':len(freeze),'labels':len(labels),'references':len(refs),'citations':len(cites),'pdf_pages':55,'inherited_appendices_byte_identical':True},indent=2))
