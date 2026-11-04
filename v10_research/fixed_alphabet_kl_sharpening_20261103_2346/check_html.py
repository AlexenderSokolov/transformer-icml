#!/usr/bin/env python3
"""Source fidelity and presentation checks, not mathematical numerical tests."""
from pathlib import Path
from html.parser import HTMLParser
import hashlib, json, re, subprocess, sys
HERE=Path(__file__).resolve().parent
HTML=HERE/'fixed_alphabet_sharp_terminal_kl.v1.html'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def normalize(s):return ' '.join(s.split())
def convert(p,prefix):
    text=subprocess.check_output(['pandoc',str(p),'--from=markdown-smart-superscript-subscript+autolink_bare_uris','--to=html5','--wrap=none'],text=True)
    text=re.sub(r'\bid="([^"]+)"',lambda m:'id="'+prefix+m.group(1)+'"',text)
    return re.sub(r'href="#([^"]+)"',lambda m:'href="#'+prefix+m.group(1)+'"',text)
class ReadHTML(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.parts=[];self.ids=[];self.links=[];self.resources=[]
    def handle_data(self,d):self.parts.append(d)
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        if t in {'h1','h2','h3','h4','p','li','pre','br'}:self.parts.append('\n')
        if 'id'in a:self.ids.append(a['id'])
        if t=='a' and 'href'in a:self.links.append(a['href'])
        if t in {'script','iframe','img','link','embed','object','video','audio'}:self.resources.append((t,a))
    def handle_endtag(self,t):
        if t in {'h1','h2','h3','h4','p','li','pre'}:self.parts.append('\n')
def source_display(p):
    s=p.read_text()
    s=re.sub(r'(?m)^\d+\. +','',s)
    s=re.sub(r'(?m)^#{1,6} +','',s)
    s=re.sub(r'(?m)^[ ]{0,3}[-*+] +','',s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1',s)
    s=s.replace('`','').replace('**','')
    s=re.sub(r'\*([^*\n]+)\*',r'\1',s)
    return normalize(s)
text=HTML.read_text();bindings=json.loads((HERE/'SOURCE_BINDINGS.json').read_text())
checks={}
for e in bindings['files']:
    path=HERE/e['path'];sid=e['section_id']
    assert sha(path)==e['sha256'],e['path']+' source hash mismatch'
    actual=text.split('<!-- BEGIN '+sid+' -->\n',1)[1].split('<!-- END '+sid+' -->',1)[0]
    assert actual==convert(path,sid+'-'),sid+' exact conversion mismatch'
    p=ReadHTML();p.feed(actual)
    assert normalize(''.join(p.parts))==source_display(path),sid+' decoded display mismatch'
    checks[sid]={'source_sha256':e['sha256'],'exact_conversion':True,'decoded_display_equals_source':True}
assert '<sup>' not in text and '<sub>' not in text
p=ReadHTML();p.feed(text)
assert len(p.ids)==len(set(p.ids)), 'duplicate IDs'
assert all(x[1:] in p.ids for x in p.links if x.startswith('#')), 'missing anchor'
assert not p.resources, 'unexpected resource'
assert not re.search(r'url\s*\(|@import',text,re.I), 'external style resource'
report={'scope':'Exact source fidelity, offline HTML structure and presentation only; no mathematical numerical testing.',
 'html_sha256':sha(HTML),'html_bytes':HTML.stat().st_size,'source_checks':checks,
 'all_source_hashes_match':True,'source_count':len(checks),'duplicate_ids':[],
 'missing_internal_targets':[],'external_resources_required':[],
 'rendering':{'status':'not_attempted','visual_pass_claimed':False}}
if '--render' in sys.argv:
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
            page=browser.new_page(viewport={'width':1280,'height':1000})
            requested=[];page.on('request',lambda r:requested.append(r.url))
            page.goto(HTML.as_uri(),wait_until='load')
            page.locator('details').evaluate_all('(els)=>els.forEach(e=>e.open=true)')
            page.evaluate('document.fonts.ready')
            layoutjs="""()=>({width:document.documentElement.scrollWidth,viewport:innerWidth,overflow:[...document.querySelectorAll('p,pre,table,li')].filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>e.tagName+': '+e.textContent.slice(0,100))})"""
            desktop=page.evaluate(layoutjs)
            assert desktop['width']<=desktop['viewport'] and not desktop['overflow'],desktop
            qa=HERE/'qa';qa.mkdir(exist_ok=True)
            for name,selector in [('opening','header'),('corollaries','#synthesis-exact-real-five-block-corollary'),('finite-bits','#synthesis-specialized-finite-bit-corollary'),('tilt','#statistical-proof-change-one-row-rather-than-conditioning-a-stack'),('tail','#statistical-proof-integrate-one-coordinate-on-one-dyadic-band'),('architecture','#exact-real-proof'),('precision','#precision-proof'),('literature','#prior-art'),('ledger','#integrity-ledger')]:
                page.locator(selector).scroll_into_view_if_needed();page.screenshot(path=str(qa/(name+'.png')))
            page.set_viewport_size({'width':390,'height':844});page.locator('header').scroll_into_view_if_needed()
            mobile=page.evaluate(layoutjs)
            assert mobile['width']<=mobile['viewport'] and not mobile['overflow'],mobile
            page.screenshot(path=str(qa/'mobile.png'))
            assert not [x for x in requested if not x.startswith('file:')],requested
            browser.close()
            report['rendering']={'status':'layout_checks_passed','desktop':desktop,'mobile':mobile,'screenshots':'qa/','visual_pass_claimed':False,'external_requests':[],'note':'Screenshots require visual inspection; source fidelity checked separately.'}
    except Exception as e:
        reason = ('Chromium could not create its process singleton socket: Operation not permitted. No browser page was rendered.' if 'socket() failed: Operation not permitted' in str(e) else str(e)[:1000])
        report['rendering']={'status':'blocked','visual_pass_claimed':False,'reason':reason}
(HERE/'HTML_VERIFICATION.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
