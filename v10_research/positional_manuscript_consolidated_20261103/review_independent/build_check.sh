#!/usr/bin/env bash
# Independent build in a disposable directory. Author sources remain read-only.
set -euo pipefail
review="$(cd "$(dirname "$0")" && pwd)"
paper="$(dirname "$review")"
work="$(mktemp -d /tmp/positional-review-build.XXXXXX)"
cp "$paper/main.tex" "$paper/references.bib" "$work/"
cp -r "$paper/sections" "$work/sections"
cd "$work"
export TEXMFVAR="$work/texmf-var"
export TEXMFCONFIG="$work/texmf-config"
export TEXMF="{$TEXMFVAR,/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
mkdir -p "$TEXMFVAR/web2c" "$TEXMFVAR/fonts/map/pdftex" build
if ! kpsewhich pdflatex.fmt >/dev/null; then
 (cd "$TEXMFVAR/web2c" && pdftex -ini -etex -interaction=nonstopmode -halt-on-error -jobname=pdflatex pdflatex.ini > format-build.txt)
fi
if ! kpsewhich pdftex.map >/dev/null; then
 for map in lm.map cm.map cmextra.map symbols.map latxfont.map; do kpsewhich "$map"; done | while IFS= read -r map; do cat "$map"; done > "$TEXMFVAR/fonts/map/pdftex/pdftex.map"
fi
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex > "$review/build_check_transcript.txt" 2>&1
python - "$review" "$work" <<'PY'
from pathlib import Path
from hashlib import sha256
import sys,json,re
r,w=map(Path,sys.argv[1:]);text=(w/'build/main.log').read_text()
(r/'build_check_final.log').write_text(text.replace(str(w),'<temporary-build>'))
transcript=r/'build_check_transcript.txt'
transcript.write_text(transcript.read_text().replace(str(w),'<temporary-build>'))
bad=[line for line in text.splitlines() if re.search(r'Warning|Overfull|Underfull|undefined references|undefined citations',line)]
assert not bad,bad
pages=int(re.search(r'Output written on .+?\((\d+) pages,',text).group(1))
assert pages==55,pages
sources={str(p.relative_to(w)):sha256(p.read_bytes()).hexdigest() for p in [w/'main.tex',w/'references.bib',*sorted((w/'sections').glob('*.tex'))]}
(r/'build_check.json').write_text(json.dumps({'status':'PASS','pages':pages,'warnings':bad,'sources':sources,'scope':'Independent clean-directory TeX build only. Visual PDF inspection is separately performed by the author.'},indent=2)+'\n')
print(json.dumps({'status':'PASS','pages':pages,'warning_count':len(bad)}))
PY
