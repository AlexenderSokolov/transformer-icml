from pathlib import Path
import hashlib,json,zipfile
from lxml import etree
from pypdf import PdfReader
R=Path(__file__).resolve().parent
project=R.parent
bindings=json.loads((R/'SOURCE_BINDINGS.json').read_text())
for item in bindings['sources']:
 p=project/item['path'];assert p.exists(),p
 assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],p
p=R/'Chinese-stage5-guide.docx'
x=etree.fromstring(zipfile.ZipFile(p).read('word/document.xml'))
ns={'m':'http://schemas.openxmlformats.org/officeDocument/2006/math','w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
assert len(x.xpath('//m:oMath',namespaces=ns))>=100
assert not x.xpath('//w:drawing',namespaces=ns)
text=''.join(x.xpath('//w:t/text() | //m:t/text()',namespaces=ns))
for bad in ['待确认','候选主域','预期给出','/workspace/','ROOT_LEDGER','[[PAGE]]']:
 assert bad not in text,bad
assert len(PdfReader(R/'Chinese-stage5-guide.pdf').pages)==6
print(json.dumps({'pass':True,'pages':6,'native_equations':len(x.xpath('//m:oMath',namespaces=ns)),'source_bindings':len(bindings['sources'])}))
