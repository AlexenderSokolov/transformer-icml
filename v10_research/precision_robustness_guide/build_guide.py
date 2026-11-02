from pathlib import Path
import re,subprocess,shutil,zipfile,json,datetime,io
from lxml import etree
from docx import Document
from docx.shared import Mm,Inches,Pt,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
ROOT=Path(__file__).resolve().parent
source=(ROOT/'guide_math_zh.md').read_text()
# Fixed native delimiters avoid the known LO dynamic nonround delimiter import bug.
source=source.replace(r'\left[',r'\lbrack').replace(r'\right]',r'\rbrack')
source=source.replace(r'\left\{',r'\{').replace(r'\right\}',r'\}')
(ROOT/'guide_final_math_zh.md').write_text(source)
raw=ROOT/'native_math.docx'
r=subprocess.run([shutil.which('pandoc'),'--from','markdown+tex_math_dollars','--to','docx','--output',str(raw),str(ROOT/'guide_final_math_zh.md')],capture_output=True,text=True,check=True)
assert 'Could not convert TeX math' not in r.stderr,r.stderr
if r.stderr: print(r.stderr)
doc=Document(raw)
for st in doc.styles:
    if re.fullmatch(r'Heading [1-9]',st.name):st.element.find(qn('w:name')).set(qn('w:val'),st.name.lower())
sec=doc.sections[0]
sec.page_width=Inches(8.5);sec.page_height=Inches(11)
sec.top_margin=Mm(17);sec.bottom_margin=Mm(17)
sec.left_margin=Mm(18);sec.right_margin=Mm(18)
sec.header_distance=Mm(7);sec.footer_distance=Mm(7)
FONT='Noto Serif CJK SC'
def setfont(el):
    rf=el.find(qn('w:rFonts'))
    if rf is None:rf=OxmlElement('w:rFonts');el.insert(0,rf)
    for k in ('ascii','hAnsi','eastAsia','cs'):rf.set(qn('w:'+k),FONT)
    for k in ('asciiTheme','hAnsiTheme','eastAsiaTheme','cstheme'):rf.attrib.pop(qn('w:'+k),None)
def style(name,size,bold=False):
    if name not in doc.styles:return
    st=doc.styles[name];st.font.name=FONT;st.font.size=Pt(size);st.font.bold=bold;st.font.color.rgb=RGBColor(0,0,0)
    setfont(st.element.get_or_add_rPr())
    for b in st.element.xpath('.//w:pBdr'):b.getparent().remove(b)
    return st
for name in ('Normal','Body Text','First Paragraph','Compact'):
    st=style(name,11)
    if st:
        pf=st.paragraph_format;pf.line_spacing=1.08;pf.space_after=Pt(5);pf.space_before=Pt(0);pf.widow_control=True
for name,size,bold in [('Title',18,True),('Subtitle',11,False),('Heading 1',13,True),('Heading 2',11.4,True),('Heading 3',11,True)]:
    st=style(name,size,bold);pf=st.paragraph_format;pf.space_before=Pt(5 if name=='Heading 2' else 0);pf.space_after=Pt(6);pf.keep_with_next=True;pf.line_spacing=1.05
st=style('Hyperlink',11);st.font.underline=False
mathpr=doc.settings.element.find(qn('m:mathPr'))
if mathpr is None:mathpr=OxmlElement('m:mathPr');doc.settings.element.append(mathpr)
mf=mathpr.find(qn('m:mathFont'))
if mf is None:mf=OxmlElement('m:mathFont');mathpr.insert(0,mf)
mf.set(qn('m:val'),'Latin Modern Math')
next_break=False;logical_pages=1
for p in list(doc.paragraphs):
    t=p.text.strip()
    if t=='[[PAGE]]':next_break=True;p._element.getparent().remove(p._element);continue
    if t=='马尔可夫预测的精度容量与鲁棒性':p.style='Title'
    elif t=='第七阶段研究指南 2026年11月2日':p.style='Subtitle'
    elif p.style.name=='Heading 2':p.style='Heading 1'
    elif p.style.name=='Heading 3':p.style='Heading 2'
    if next_break:p.paragraph_format.page_break_before=True;logical_pages+=1;next_break=False
    if p._element.xpath('./m:oMathPara'):
        p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.space_before=Pt(1);p.paragraph_format.space_after=Pt(5);p.paragraph_format.line_spacing=1;p.paragraph_format.keep_together=True
    for r in p.runs:
        r.font.color.rgb=RGBColor(0,0,0);r.font.name=FONT;setfont(r._element.get_or_add_rPr())
    for b in p._element.xpath('./w:pPr/w:pBdr'):b.getparent().remove(b)
# Compact tables for comparable resource and reading records; no narrative cells.
for ti,t in enumerate(doc.tables):
    t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False
    widths=[Inches(2.5),Inches(4.0)] if ti==0 else [Inches(2.3),Inches(4.2)]
    for ci,width in enumerate(widths):t.columns[ci].width=width
    tw=t._tbl.tblPr.find(qn('w:tblW'));tw.set(qn('w:type'),'dxa');tw.set(qn('w:w'),'9360')
    # Explicit light-gray grid overrides Pandoc's dark header rule.
    for old in t._tbl.tblPr.findall(qn('w:tblBorders')):t._tbl.tblPr.remove(old)
    borders=OxmlElement('w:tblBorders')
    for side in ('top','left','bottom','right','insideH','insideV'):
        border=OxmlElement('w:'+side)
        for k,v in [('val','single'),('sz','4'),('color','D9D9D9'),('space','0')]:border.set(qn('w:'+k),v)
        borders.append(border)
    t._tbl.tblPr.append(borders)
    for rowidx,row in enumerate(t.rows):
        trpr=row._tr.get_or_add_trPr()
        no=OxmlElement('w:cantSplit');trpr.append(no)
        if rowidx==0:
            repeat=OxmlElement('w:tblHeader');trpr.append(repeat)
        for ci,c in enumerate(row.cells):
            c.width=widths[ci];c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            tcpr=c._tc.get_or_add_tcPr()
            for old in tcpr.findall(qn('w:tcBorders')):tcpr.remove(old)
            cb=OxmlElement('w:tcBorders')
            for side in ('top','left','bottom','right'):
                border=OxmlElement('w:'+side)
                for k,v in [('val','single'),('sz','4'),('color','D9D9D9'),('space','0')]:border.set(qn('w:'+k),v)
                cb.append(border)
            tcpr.append(cb)
            margins=OxmlElement('w:tcMar')
            for tag,val in [('top','70'),('bottom','70'),('left','90'),('right','90')]:
                m=OxmlElement('w:'+tag);m.set(qn('w:w'),val);m.set(qn('w:type'),'dxa');margins.append(m)
            tcpr.append(margins)
            if rowidx==0:
                sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'EDEDED');tcpr.append(sh)
            for p in c.paragraphs:
                p.paragraph_format.line_spacing=1.03;p.paragraph_format.space_after=Pt(0);p.paragraph_format.space_before=Pt(0)
                for r in p.runs:r.font.size=Pt(9.5);r.font.color.rgb=RGBColor(0,0,0);r.bold=rowidx==0;setfont(r._element.get_or_add_rPr())
# Running header records scientific snapshot, not production date.
hp=sec.header.paragraphs[0];hp.alignment=WD_ALIGN_PARAGRAPH.RIGHT
r=hp.add_run('第七阶段  科学冻结 2026-11-02 08:09:06 UTC');r.font.name=FONT;r.font.size=Pt(8);r.font.color.rgb=RGBColor(0,0,0);setfont(r._element.get_or_add_rPr())
fp=sec.footer.paragraphs[0];fp.alignment=WD_ALIGN_PARAGRAPH.CENTER
field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');rr=OxmlElement('w:r');tt=OxmlElement('w:t');tt.text='1';rr.append(tt);field.append(rr);fp._p.append(field)
props=doc.core_properties;props.title='马尔可夫预测的精度容量与鲁棒性';props.subject='第七阶段研究指南';props.author='';props.last_modified_by='';props.comments='';props.created=datetime.datetime(2026,11,2,8,9,6);props.modified=props.created
# LibreOffice imports dynamic nonround delimiters inconsistently. Preserve native
# editable OMML but use fixed delimiter runs around the existing expression.
for delim in list(doc.element.xpath('//m:d')):
    pr=delim.find(qn('m:dPr'))
    if pr is None: continue
    beg=pr.find(qn('m:begChr'));end=pr.find(qn('m:endChr'))
    if beg is None or end is None: continue
    chars=(beg.get(qn('m:val')),end.get(qn('m:val')))
    if chars==('(',')'): continue
    parent=delim.getparent();idx=parent.index(delim)
    pieces=[]
    for char in [chars[0]]:
        rr=OxmlElement('m:r');tt=OxmlElement('m:t');tt.text=char;rr.append(tt);pieces.append(rr)
    for e in delim.findall(qn('m:e')): pieces.extend(list(e))
    rr=OxmlElement('m:r');tt=OxmlElement('m:t');tt.text=chars[1];rr.append(tt);pieces.append(rr)
    parent.remove(delim)
    for offset,el in enumerate(pieces):parent.insert(idx+offset,el)
out=ROOT/'Chinese-stage7-guide.docx';doc.save(out)
# Normalize package timestamps for reproducible clean builds.
buffer=io.BytesIO()
with zipfile.ZipFile(out) as old, zipfile.ZipFile(buffer,'w',zipfile.ZIP_DEFLATED) as new:
    for name in sorted(old.namelist()):
        info=zipfile.ZipInfo(name,(2026,11,2,8,9,6));info.compress_type=zipfile.ZIP_DEFLATED
        new.writestr(info,old.read(name))
out.write_bytes(buffer.getvalue())
with zipfile.ZipFile(out) as z:
    xml=etree.fromstring(z.read('word/document.xml'));ns={'m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
    eq=xml.xpath('//m:oMath',namespaces=ns)
    for m in eq:assert not re.search(r'[\u3400-\u9fff]',''.join(m.xpath('.//m:t/text()',namespaces=ns)))
    txt=''.join(xml.xpath('//*[local-name()="t"]/text()'))
    assert not any(x in txt for x in ('\\','[[PAGE]]','/workspace/','/tmp/'))
    assert not xml.xpath('//*[local-name()="drawing"]')
    for d in xml.xpath('//m:dPr',namespaces=ns):
        assert (d.find(qn('m:begChr')).get(qn('m:val')),d.find(qn('m:endChr')).get(qn('m:val')))==('(',')')
print(json.dumps({'output':str(out),'native_equations':len(eq),'logical_pages':logical_pages},ensure_ascii=False))
