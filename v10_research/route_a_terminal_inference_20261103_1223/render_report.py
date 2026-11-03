from pathlib import Path
from html import escape
p=Path(__file__).parent
src=(p/'report_source.txt').read_text()
parts=src.split('\n\n')
head='''<!doctype html><html lang="en"><meta charset="utf-8"><title>Route A finite terminal risk</title><style>body{max-width:1050px;margin:2em auto;padding:0 1.2em;font:16px/1.6 system-ui;color:#17212b}h1,h2{color:#163d5b}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:15px/1.55 ui-monospace,monospace;background:#f3f6f9;padding:.8em;border-radius:5px}p{overflow-wrap:anywhere}.warn{border-left:4px solid #b56a1c;padding:1em;background:#fff7e9}</style><body>'''
html=head
for i,part in enumerate(parts):
 if not part.strip():continue
 lines=part.splitlines()
 if i==0: html+='<h1>'+escape(lines[0])+'</h1><p class="warn">'+escape(' '.join(lines[1:]))+'</p>'
 elif lines[0][:2].strip().isdigit() and '. ' in lines[0]:
  html+='<h2>'+escape(lines[0])+'</h2><pre>'+escape('\n'.join(lines[1:]))+'</pre>'
 else:html+='<pre>'+escape(part)+'</pre>'
html+='</body></html>'
(p/'route_a_terminal_report_v1.html').write_text(html)
