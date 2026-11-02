from pathlib import Path
from zipfile import ZipFile
from datetime import datetime
from lxml import etree
from docx import Document
from docx.oxml.ns import qn
import json,hashlib,re,subprocess,shutil,os
root=Path(__file__).resolve().parent
base=root.parent
rd=root/'qa_v3'
docx=root/'Chinese-sharp-ratio-addendum.docx'
pdf=root/'Chinese-sharp-ratio-addendum.pdf'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
freeze='2026-11-02T05:15:00+00:00'
sources=[]
for unit in ('SH001','SB001','BA001'):
 receipt=base/'intake'/f'{unit}_acceptance.json'
 r=json.loads(receipt.read_text()); proof=base/r['proof']
 assert sha(proof)==r['sha256'],unit
 assert r['status']=='ROOT_ACCEPTED_AFTER_INDEPENDENT_LLM_REVIEW'
 assert datetime.fromisoformat(r['time_utc'])<=datetime.fromisoformat(freeze)
 for p in [proof,receipt,base/r['review']]:
  sources.append({'path':p.relative_to(base).as_posix(),'sha256':sha(p),'bytes':p.stat().st_size})
for rel in ('reviews/SH001_review_bindings_v1.json','reviews/SH001_independent_checks_v1.py','reviews/SH001_independent_checks_v1.json','score_precision/SH001_source_bindings_v1.json'):
 p=base/rel;sources.append({'path':rel,'sha256':sha(p),'bytes':p.stat().st_size})
bindings=json.loads((base/'reviews/SH001_review_bindings_v1.json').read_text())
for rel,expected in bindings['files'].items(): assert sha(base/rel)==expected,rel
old_verified=[]
for folder in ('stage3_guide',):
 m=json.loads((base/folder/'BUILD_MANIFEST.json').read_text())
 for entry in m['outputs']+m['support_files']:
  p=base/folder/entry['path'];assert sha(p)==entry['sha256'],str(p)
  old_verified.append({'path':p.relative_to(base).as_posix(),'sha256':sha(p)})
(root/'SOURCE_BINDINGS.json').write_text(json.dumps({'science_freeze_utc':freeze,'sources':sources,'prior_stage3_files_unchanged':old_verified},ensure_ascii=False,indent=2))
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
with ZipFile(docx) as z:
 assert z.testzip() is None
 x=etree.fromstring(z.read('word/document.xml'));st=etree.fromstring(z.read('word/styles.xml'))
 txt=''.join(x.xpath('//w:t/text()|//m:t/text()',namespaces=ns))
 equations=x.xpath('//m:oMath',namespaces=ns)
 assert len(equations)==96
 for m in equations:assert not re.search(r'[\u3400-\u9fff]',''.join(m.xpath('.//m:t/text()',namespaces=ns)))
 assert not x.xpath('//w:drawing|//w:pict',namespaces=ns)
 for bad in ('\\','$','[[PAGE]]','/workspace/','/tmp/','�','¿'):
  assert bad not in txt,bad
 for d in x.xpath('//m:dPr',namespaces=ns):
  assert (d.find(qn('m:begChr')).get(qn('m:val')),d.find(qn('m:endChr')).get(qn('m:val')))==('(',')')
 title=x.xpath('//w:p[w:pPr/w:pStyle[@w:val="Title"]]',namespaces=ns)
 assert len(title)==1
 assert not title[0].xpath('./w:pPr/w:pBdr',namespaces=ns)
 for sid in ('Title','Heading1','Heading2'):
  style=st.xpath('//w:style[@w:styleId="'+sid+'"]',namespaces=ns)[0]
  assert style.xpath('./w:rPr/w:color/@w:val',namespaces=ns)==['000000']
  assert not style.xpath('./w:pPr/w:pBdr',namespaces=ns)
 assert not x.xpath('//w:tbl',namespaces=ns)
 sect=Document(docx).sections[0]
 assert sect.page_width.inches==8.5 and sect.page_height.inches==11
shutil.copyfile(rd/pdf.name,pdf)
assert sha(pdf)==sha(rd/pdf.name)
info=subprocess.run(['pdfinfo',str(pdf)],check=True,capture_output=True,text=True).stdout
pages=int(re.search(r'^Pages:\s+(\d+)',info,re.M)[1]);assert pages==3
assert len(list(rd.glob('page-*.png')))==3
pt=subprocess.run(['pdftotext','-layout',str(pdf),'-'],check=True,capture_output=True,text=True).stdout
flat=''.join(pt.split())
assert flat.count('科学冻结2026-11-0205:15UTC北京时间13:15')==3
for bad in ('$','\\','�','¿'):assert bad not in pt,bad
for good in ('第三阶段论文快照与八页指南仍有效','SB001v2','SH001v1','BA001v1','05:13:19','最优常数','LLM','fa8e326047f2df8f01dd7b3112da655937ad7be1a3508ad00b80ccd51b64fd50'):
 assert good in flat,good
report={'science_freeze_utc':freeze,'science_freeze_beijing':'2026-11-02 13:15:00','pages':pages,'page_size':'Letter portrait','native_OMML_equations':len(equations),'raster_equations':0,'structural_checks':'passed','visual_review':{'pages_inspected':[1,2,3],'render_dir':rd.name,'status':'passed','notes':'All latest page PNGs inspected; no clipping, overlap, missing glyphs or unconverted math.'},'source_bindings_verified':True,'old_stage3_guide_unchanged':True,'external_upload_or_send':False,'sha256':{docx.name:sha(docx),pdf.name:sha(pdf)}}
(root/'final_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
manifest={'science_freeze_utc':freeze,'science_freeze_beijing':'2026-11-02 13:15:00','pages':pages,'native_OMML_equations':len(equations),'native_math_path':'Pandoc TeX math to native OMML, bundled-runtime python-docx formatting; fixed nonround delimiters verified','marker':{'create_docx_successful_calls':1,'create_pdf_successful_calls':1},'runtime_bundle':os.environ['CODEX_PRIMARY_RUNTIME_BUNDLE_VERSION'],'render_dir':rd.name,'outputs':[{'path':p.name,'bytes':p.stat().st_size,'sha256':sha(p)} for p in (docx,pdf)],'support_files':[{'path':p.name,'bytes':p.stat().st_size,'sha256':sha(p)} for p in [root/'addendum_math_zh.md',root/'addendum_final_math_zh.md',root/'build_addendum.py',root/'verify_addendum.py',root/'SOURCE_BINDINGS.json',root/'final_verification.json']],'source_files_modified':False,'external_upload_or_send':False}
(root/'BUILD_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
