from pathlib import Path
import hashlib,json,zipfile,subprocess,os
from lxml import etree
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent;WORK=ROOT.parent.parent;BASE=ROOT.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={}
def bind(p,expected=None):
 p=p.resolve();assert p.is_file(),p
 h=sha(p)
 if expected:assert h==expected,(p,h,expected)
 files[str(p.relative_to(WORK))]=h
freeze_path=BASE/'delivery_stage8/SCIENTIFIC_FREEZE.json';freeze=json.loads(freeze_path.read_text());bind(freeze_path)
assert freeze['scientific_freeze_utc']=='2026-11-02T09:22:25.495805+00:00'
assert freeze['new_units']==['SC001','SC002','SC003','BT001','BT002','EP001']
units=[]
for u in freeze['new_units']+['IU001','AU001','BIF001','BAI003']:
 p=BASE/'intake'/f'{u}_acceptance.json';bind(p,freeze['receipts'].get(str(p.relative_to(WORK))))
 r=json.loads(p.read_text());bind(BASE/r['proof'],r['sha256'])
 for key in ('review','delta_review'):
  if r.get(key):bind(BASE/r[key])
 for p,h in r.get('component_proofs',{}).items():bind(BASE/p,h)
 units.append({'unit':u,'scope':r['scope'],'acceptance':str((BASE/'intake'/f'{u}_acceptance.json').relative_to(WORK))})
for d in ('source_symbol_corruption','source_symbol_corruption_mixing','binary_source_corruption','binary_erasure_transport','terminal_symbol_corruption'):
 for p in (BASE/d).glob('*'):
  if p.is_file() and p.suffix in ('.md','.json','.py'):bind(p)
r011=json.loads((BASE/'binary_source_corruption/SC003_independent_full_review_bindings.json').read_text())
for p,h in r011['files'].items():bind(WORK/p,h)
for p in ['v10_intake/source/DOT_START_PROMPT.txt','v10_intake/source/START_HERE.md','v10_research/prior_art/source_corruption_screen.md']:bind(WORK/p)
with zipfile.ZipFile(ROOT/'Chinese-stage8-guide.docx') as z:
 x=etree.fromstring(z.read('word/document.xml'));ns={'m':'http://schemas.openxmlformats.org/officeDocument/2006/math','w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
 equations=x.xpath('//m:oMath',namespaces=ns);assert len(equations)>=90
 assert not x.xpath('//*[local-name()="drawing"]')
 assert not [p for p in z.namelist() if p.startswith('word/media/')]
 text=''.join(x.xpath('//*[local-name()="t"]/text()'));assert '[[PAGE]]' not in text and '\\' not in text
 for claim in ('BT001','BT002','SC001','SC002','SC003','EP001','隐藏','任意计算','离线随机核'):assert claim in text,claim
 styles=etree.fromstring(z.read('word/styles.xml'));assert styles.xpath('//w:style[@w:styleId="Normal"]//w:sz[@w:val="22"]',namespaces=ns)
pdf=ROOT/'Chinese-stage8-guide.pdf';reader=PdfReader(pdf);assert len(reader.pages)==9
assert len(list((ROOT/'render').glob('page-*.png')))==9
before=sha(ROOT/'Chinese-stage8-guide.docx')
subprocess.run([os.environ['CODEX_PRIMARY_RUNTIME_PYTHON'],str(ROOT/'build_guide.py')],check=True,capture_output=True)
after=sha(ROOT/'Chinese-stage8-guide.docx');assert before==after,'Non-deterministic rebuild'
manifest={'freeze_utc':freeze['scientific_freeze_utc'],'units':units,'files':dict(sorted(files.items())),'guide_source_sha256':sha(ROOT/'guide_math_zh.md'),'scope':'Six new accepted units with full component proofs/reviews/receipts, direct inherited interfaces and original mandate. Binding does not claim a fresh transitive proof audit.'}
(ROOT/'SOURCE_BINDINGS.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
report={'status':'PASS','pages':9,'native_OMML_objects':len(equations),'formula_images':0,'body_pt':11,'source_bindings':len(files),'docx_rebuild_byte_identical':True,'docx_sha256':after,'pdf_sha256':sha(pdf),'markdown_sha256':sha(ROOT/'guide_math_zh.md'),'checks':'Freeze and component hashes; complete receipts and reviews; native equations; no drawings/media; nine PDF/PNG pages; body 11 pt; deterministic clean DOCX rebuild. Visual review is separate.'}
(ROOT/'VERIFICATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
