"""
Converte um arquivo Markdown (com frontmatter YAML simples) em PDF.
Uso: python md_to_pdf.py caminho/arquivo.md [caminho/saida.pdf]

Ferramenta de apoio para o acervo pessoal de estudos em estudos/provas e
estudos/transcricoes -- gera uma versao em PDF de cada transcricao a partir
do Markdown, para quem preferir ler/imprimir em PDF.
"""
import sys
import re
from pathlib import Path

import markdown as md
from xhtml2pdf import pisa

CSS = """
@page { size: A4; margin: 2cm; }
body { font-family: Helvetica, Arial, sans-serif; font-size: 11pt; line-height: 1.4; }
h1 { font-size: 18pt; margin-top: 0; }
h2 { font-size: 14pt; margin-top: 1em; }
table { border-collapse: collapse; width: 100%; margin-bottom: 1em; }
th, td { border: 1px solid #999; padding: 4px 8px; font-size: 9pt; text-align: left; }
code, pre { font-family: Consolas, monospace; background: #f4f4f4; }
hr { border: none; border-top: 1px solid #ccc; margin: 1.5em 0; }
.frontmatter { background: #f0f0f0; padding: 10px; font-size: 9pt; margin-bottom: 1.5em; }
.frontmatter b { display: inline-block; min-width: 140px; }
"""


def split_frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    raw_fm, body = m.group(1), m.group(2)
    fm = {}
    key = None
    for line in raw_fm.split("\n"):
        if re.match(r"^[a-zA-Z_][\w]*:", line):
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().lstrip(">").strip()
        elif key:
            fm[key] += " " + line.strip()
    return fm, body


def convert(md_path: Path, pdf_path: Path):
    text = md_path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)

    fm_html = ""
    if fm:
        rows = "".join(f"<div><b>{k}:</b> {v}</div>" for k, v in fm.items())
        fm_html = f'<div class="frontmatter">{rows}</div>'

    body_html = md.markdown(body, extensions=["tables", "fenced_code"])
    html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head>" \
           f"<body>{fm_html}{body_html}</body></html>"

    with open(pdf_path, "wb") as out:
        result = pisa.CreatePDF(html, dest=out)
    if result.err:
        raise RuntimeError(f"Falha ao gerar PDF para {md_path}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    md_path = Path(sys.argv[1]).resolve()
    if not md_path.exists():
        print(f"Arquivo nao encontrado: {md_path}")
        sys.exit(1)
    pdf_path = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else md_path.with_suffix(".pdf")
    convert(md_path, pdf_path)
    print(f"OK: {pdf_path}")


if __name__ == "__main__":
    main()
