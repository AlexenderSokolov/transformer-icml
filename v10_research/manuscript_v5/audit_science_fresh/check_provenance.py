from pathlib import Path
import re,json,hashlib,difflib
root=Path('.');out=Path(__file__).parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
m=json.loads(Path('v10_research/manuscript_v5/SOURCE_MANIFEST.json').read_text());checked=[]
for s in m['sources']:
 assert sha(s['path'])==s['sha256'],s['path'];checked.append(s['path'])
f=json.loads(Path('v10_research/delivery_stage7/SCIENTIFIC_FREEZE.json').read_text())
for p,h in f['receipts'].items():assert sha(p)==h,p
old=Path('v10_research/manuscript_v4/finite_precision_prediction.tex').read_text();new=Path('v10_research/manuscript_v5/finite_precision_prediction.tex').read_text()
a=old[old.index('\\section{Complete messages'):old.index('\\section{Finite resource')];b=new[new.index('\\section{Complete messages'):new.index('\\section{The mixing-dependent')]
# All inline and display math in inherited technical core, excluding prose.
pattern=r'\$[^$]*\$|\\\[.*?\\\]|\\begin\{(equation\*?|align\*?|gather\*?)\}.*?\\end\{\1\}'
get=lambda t:[x.group(0) for x in re.finditer(pattern,t,re.S)]
ma,mb=get(a),get(b);assert ma==mb,'inherited math changed'
(out/'v4_core_editorial.diff').write_text(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='v4 core',tofile='v5 inherited core')))
# Named equations also ensure no dropped labeled equation elsewhere in old body.
def eqs(t):
 d={}
 for x in re.finditer(r'\\begin\{(equation\*?|align\*?)\}(.*?)\\end\{\1\}',t,re.S):
  label=re.search(r'\\label\{([^}]+)\}',x.group(2))
  if label:d[label[1]]=x.group(0)
 return d
old_eq=eqs(old);new_eq=eqs(new)
for k,v in old_eq.items():assert new_eq[k]==v,k
result={'status':'PASS','manifest_sources_verified':len(checked),'frozen_receipts_verified':len(f['receipts']),'inherited_core_math_fragments_identical':len(ma),'v4_labeled_equations_identical':len(old_eq),'v4_tex_sha256':sha('v10_research/manuscript_v4/finite_precision_prediction.tex'),'v4_pdf_sha256':sha('v10_research/manuscript_v4/finite_precision_prediction.pdf')}
(out/'provenance.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
