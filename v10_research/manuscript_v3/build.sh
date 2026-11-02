#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
# Keep all generated format caches within this source directory.
export TEXMFVAR="$PWD/build/texmf-var"
export TEXMFCONFIG="$PWD/build/texmf-config"
if [[ -d /usr/share/texlive/texmf-dist ]]; then
  export TEXMF="{$TEXMFVAR,/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
fi
mkdir -p "$TEXMFVAR/web2c" "$TEXMFVAR/fonts/map/pdftex" qa
if ! kpsewhich pdflatex.fmt >/dev/null; then
  (cd "$TEXMFVAR/web2c" && pdftex -ini -etex -interaction=nonstopmode -halt-on-error -jobname=pdflatex pdflatex.ini > format-build.txt)
fi
if ! kpsewhich pdftex.map >/dev/null; then
  # Debian TeX installations without their generated system cache.
  for map in lm.map cm.map cmextra.map symbols.map latxfont.map; do
    kpsewhich "$map"
  done | while IFS= read -r map; do cat "$map"; done > "$TEXMFVAR/fonts/map/pdftex/pdftex.map"
fi
pdflatex -interaction=nonstopmode -halt-on-error finite_precision_prediction.tex > build-pass1.txt
bibtex finite_precision_prediction > build-bibtex.txt
pdflatex -interaction=nonstopmode -halt-on-error finite_precision_prediction.tex > build-pass2.txt
pdflatex -interaction=nonstopmode -halt-on-error finite_precision_prediction.tex > build-pass3.txt
if grep -E 'Overfull|undefined|LaTeX Error|Fatal error' finite_precision_prediction.log; then
  echo 'Resolve the reported layout or reference defects before delivery.' >&2
  exit 1
fi
pdfinfo finite_precision_prediction.pdf > qa/pdfinfo.txt
pdftotext -layout finite_precision_prediction.pdf qa/text.txt
if [[ "${1:-}" == "--render" ]]; then
  pdftoppm -r 110 -png finite_precision_prediction.pdf qa/page
fi
