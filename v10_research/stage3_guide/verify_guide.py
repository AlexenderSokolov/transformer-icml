from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from docx import Document
from docx.oxml.ns import qn
from datetime import datetime
import json,re,subprocess,hashlib

root=Path(__file__).resolve().parent
base=root.parent
docx=root/'Chinese-stage3-guide.docx'
pdf=root/'Chinese-stage3-guide.pdf'
rd=root/'qa_release2'
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
freeze='2026-11-02T04:45:00+00:00'
sources=[]
for unit in ('FR001','BA001','BF001','CA001','FA001','CF001','GW001','SB001'):
    receipt=base/'intake'/f'{unit}_acceptance.json'
    r=json.loads(receipt.read_text())
    proof=base/r['proof']
    assert sha(proof)==r['sha256'],unit
    assert datetime.fromisoformat(r['time_utc'])<=datetime.fromisoformat(freeze),unit
    assert r['status']=='ROOT_ACCEPTED_AFTER_INDEPENDENT_LLM_REVIEW'
    paths=[proof,receipt]
    for rel in r.get('reviews',[r.get('review')]):
        if rel:paths.append(base/rel)
    for p in paths:
        sources.append({'path':p.relative_to(base).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
for rel in ('bounded_attention/BA001_scalar_coordinate_scope_note.md','causal_attention/CA001_boundary_branch_causality_scope_note_v1.md','prior_art/loglog_score_budget_comparison.md','prior_art/bounded_attention_family_comparison.md','reviews/FA001_review_v2.md'):
    p=base/rel
    sources.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p)})
(root/'SOURCE_BINDINGS.json').write_text(json.dumps({'science_freeze_utc':freeze,'sources':sources},ensure_ascii=False,indent=2))
with ZipFile(docx) as z:
    assert z.testzip() is None
    x=etree.fromstring(z.read('word/document.xml'))
    st=etree.fromstring(z.read('word/styles.xml'))
    text=''.join(x.xpath('//w:t/text()|//m:t/text()',namespaces=ns))
    math=x.xpath('//m:oMath',namespaces=ns)
    assert len(math)>=150
    for m in math:
        assert not re.search(r'[\u3400-\u9fff]',''.join(m.xpath('.//m:t/text()',namespaces=ns)))
    assert not x.xpath('//w:drawing|//w:pict',namespaces=ns)
    for bad in ('\\','[[PAGE]]','/workspace/','/tmp/','$','¿','�','首个完整'):
        assert bad not in text,bad
    for d in x.xpath('//m:dPr',namespaces=ns):
        assert (d.find(qn('m:begChr')).get(qn('m:val')),d.find(qn('m:endChr')).get(qn('m:val')))==('(',')')
    for table in x.xpath('//w:tbl',namespaces=ns):
        for side in ('top','left','bottom','right','insideH','insideV'):
            b=table.find('w:tblPr/w:tblBorders/w:'+side,ns)
            assert b is not None and b.get(qn('w:color'))=='D9D9D9'
        for cell in table.xpath('.//w:tc',namespaces=ns):
            for side in ('top','left','bottom','right'):
                b=cell.find('w:tcPr/w:tcBorders/w:'+side,ns)
                assert b is not None and b.get(qn('w:color'))=='D9D9D9'
    title=x.xpath('//w:p[w:pPr/w:pStyle[@w:val="Title"]]',namespaces=ns)
    assert len(title)==1 and not title[0].xpath('./w:pPr/w:pBdr',namespaces=ns)
    for sid in ('Title','Heading1','Heading2'):
        style=st.xpath('//w:style[@w:styleId="'+sid+'"]',namespaces=ns)[0]
        assert style.xpath('./w:rPr/w:color/@w:val',namespaces=ns)==['000000']
        assert not style.xpath('./w:pPr/w:pBdr',namespaces=ns)
    links=[r.get('Target') for r in etree.fromstring(z.read('word/_rels/document.xml.rels')) if r.get('TargetMode')=='External']
    assert len(links)==5
    assert all(u.startswith('https://arxiv.org/') or u.startswith('https://aclanthology.org/') or u.startswith('https://mhahn.info/') for u in links)
doc=Document(docx)
assert doc.sections[0].page_width.inches==8.5 and doc.sections[0].page_height.inches==11
info=subprocess.run(['pdfinfo',str(pdf)],check=True,capture_output=True,text=True).stdout
pages=int(re.search(r'^Pages:\s+(\d+)',info,re.M)[1])
assert pages==8
assert len(list(rd.glob('page-*.png')))==pages
assert sha(pdf)==sha(rd/pdf.name)
pt=subprocess.run(['pdftotext','-layout',str(pdf),'-'],check=True,capture_output=True,text=True).stdout
(rd/'extracted.txt').write_text(pt)
flat=''.join(pt.split())
assert flat.count('第三阶段科学冻结2026-11-0204:45UTC北京时间12:45')==8
for bad in ('¿','�','\\','03:48','11:48','首个完整'):
    assert bad not in pt,bad
for expected in ('FR001','BA001','BF001','CA001','CF001','FA001','GW001','SB001','04:45:00','声明的容量条件下','固定','分支','形式历史','填充','性能测量'):
    assert expected in flat,expected
report={'science_freeze_utc':freeze,'pages':pages,'page_size':'Letter portrait','native_OMML_equations':len(math),'raster_equations':0,'primary_source_hyperlinks':links,'structural_checks':'passed','visual_review':{'pages_inspected':[],'status':'pending final review'},'sha256':{docx.name:sha(docx),pdf.name:sha(pdf)},'source_count':len(sources)}
old_path=root/'final_verification.json'
if old_path.exists():
    old=json.loads(old_path.read_text())
    if old.get('sha256')==report['sha256']:
        report['visual_review']=old.get('visual_review',report['visual_review'])
(root/'final_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
