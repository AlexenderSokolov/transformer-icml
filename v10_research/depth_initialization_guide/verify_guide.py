from pathlib import Path
import json,hashlib,zipfile,re
from lxml import etree
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
units=['BC001','BAI002','BAI003','BAI004','BOD001','WM001','BIF001','GD001']
files=set();accepted=[]
for u in units:
 p=BASE/'intake'/f'{u}_acceptance.json';r=json.loads(p.read_text());files.add(p)
 proof=BASE/r['proof'];assert sha(proof)==r['sha256'],u;files.add(proof)
 for k in ('review','delta_review','revision_note'):
  if r.get(k):files.add(BASE/r[k])
 for v in r.get('reviews',[]):files.add(BASE/v)
 for v,h in r.get('component_proofs',{}).items():
  x=BASE/v;assert sha(x)==h;files.add(x)
 accepted.append({'unit':u,'proof':r['proof'],'sha256':r['sha256'],'accepted_utc':r['time_utc']})
 # Direct diagnostic and source-binding evidence; no archived/candidate directories.
 for x in proof.parent.glob('*.json'):
  if 'binding' in x.name or 'diagnostic' in x.name or 'checks' in x.name: files.add(x)
# The frozen synthesis's exact inherited proof bindings remain separately traceable.
for u in ['SB001','BU001','BS001','TR001','CA001','FA001','CF001']:
 p=BASE/'intake'/f'{u}_acceptance.json'
 if p.exists():
  files.add(p);r=json.loads(p.read_text())
  for key in ['proof','review','delta_review']:
   if isinstance(r.get(key),str) and (BASE/r[key]).exists():files.add(BASE/r[key])
manifest={'freeze_utc':'2026-11-02T06:56:00Z','freeze_beijing':'2026-11-02 14:56','accepted_units':accepted,'files':{str(p.relative_to(BASE)):sha(p) for p in sorted(files)},'guide_source_sha256':sha(ROOT/'guide_math_zh.md'),'excluded':'Postfreeze growing-depth mixing-dependent threshold research; prior stage artifacts remain unchanged.'}
(ROOT/'SOURCE_BINDINGS.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
with zipfile.ZipFile(ROOT/'Chinese-stage6-guide.docx') as z:
 x=etree.fromstring(z.read('word/document.xml'));ns={'m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
 eq=x.xpath('//m:oMath',namespaces=ns);text=''.join(x.xpath('//*[local-name()="t"]/text()'))
 assert len(eq)>150 and not x.xpath('//*[local-name()="drawing"]')
 assert not any(t in text for t in ['[[PAGE]]','/workspace/','/tmp/','\\frac','\\rm'])
 assert not any(n.startswith('word/media/') for n in z.namelist())
reader=PdfReader(ROOT/'Chinese-stage6-guide.pdf');assert len(reader.pages)==8
texts=[p.extract_text() for p in reader.pages]
assert all(len(t)>300 for t in texts)
assert '06:56' in texts[0] and '14:56' in texts[0]
assert all('\ufffd' not in t for t in texts)
report={'status':'PASS','freeze_utc':manifest['freeze_utc'],'pages':8,'native_editable_OMML_objects':len(eq),'formula_images':0,'page_text_characters':[len(t) for t in texts],'source_receipt_hash_checks':'PASS','science_review':'Independent read-only review passed after one-step/two-step virtual-completion and suffix-horizon notation clarifications.','visual_review':{'status':'PENDING','directory':'qa_release4','required_pages':list(range(1,9))},'outputs':{n:sha(ROOT/n) for n in ['Chinese-stage6-guide.docx','Chinese-stage6-guide.pdf']},'build_inputs':{n:sha(ROOT/n) for n in ['guide_math_zh.md','guide_final_math_zh.md','build_guide.py','verify_guide.py']}}
(ROOT/'QA_RECEIPT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pages':8,'native_math':len(eq),'bound_sources':len(files),'checks':'PASS'},ensure_ascii=False))
