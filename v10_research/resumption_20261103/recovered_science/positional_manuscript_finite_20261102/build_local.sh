#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export TEXMFVAR="$PWD/build/texmf-var"
export TEXMFCONFIG="$PWD/build/texmf-config"
export TEXMF="{$TEXMFVAR,/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
mkdir -p "$TEXMFVAR/web2c" "$TEXMFVAR/fonts/map/pdftex"
if ! kpsewhich pdflatex.fmt >/dev/null; then
 (cd "$TEXMFVAR/web2c" && pdftex -ini -etex -interaction=nonstopmode -halt-on-error -jobname=pdflatex pdflatex.ini > format-build.txt)
fi
if ! kpsewhich pdftex.map >/dev/null; then
 for map in lm.map cm.map cmextra.map symbols.map latxfont.map; do kpsewhich "$map"; done | while IFS= read -r map; do cat "$map"; done > "$TEXMFVAR/fonts/map/pdftex/pdftex.map"
fi
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
pdftoppm -r 100 -png build/main.pdf build/page
