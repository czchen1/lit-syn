#!/usr/bin/env python3
"""Render REPORT.md to REVIEW.pdf (python-markdown + WeasyPrint).

Run gen_report.py first. Requires `pip install markdown weasyprint`.
"""
import os

import markdown
from weasyprint import HTML

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "REPORT.md")
OUT = os.path.join(HERE, "REVIEW.pdf")

CSS = """
@page { size: A4; margin: 18mm 16mm 18mm 16mm;
        @bottom-center { content: counter(page) " / " counter(pages); font-size: 8pt; color: #666; } }
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 9.5pt; line-height: 1.35; color: #111; }
h1 { font-size: 20pt; margin: 0 0 8pt; }
h2 { font-size: 15pt; margin: 18pt 0 6pt; border-bottom: 1px solid #999; page-break-after: avoid; }
h3 { font-size: 12pt; margin: 14pt 0 4pt; page-break-after: avoid; }
h4 { font-size: 10.5pt; margin: 10pt 0 3pt; page-break-after: avoid; }
h5 { font-size: 10pt; margin: 8pt 0 2pt; font-style: italic; }
p, li { orphans: 3; widows: 3; }
ul, ol { padding-left: 1.3em; }
li { margin: 1.5pt 0; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.3pt; background: #f2f2f2; padding: 0 2px; }
pre { font-size: 8pt; background: #f4f4f4; padding: 6pt; white-space: pre-wrap; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt; font-size: 8.2pt; page-break-inside: auto; }
th, td { border: 1px solid #bbb; padding: 2pt 4pt; vertical-align: top; text-align: left; }
th { background: #e9e9e9; }
tr { page-break-inside: avoid; }
hr { border: 0; border-top: 1px solid #ccc; margin: 12pt 0; }
a { color: #1a4d8f; text-decoration: none; }
blockquote { border-left: 3px solid #ccc; margin: 6pt 0; padding-left: 8pt; color: #333; }
"""


def main():
    md = open(SRC, encoding="utf-8").read()
    body = markdown.markdown(md, extensions=["tables", "fenced_code", "toc", "sane_lists"])
    html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"
    HTML(string=html, base_url=HERE).write_pdf(OUT)
    print(f"wrote {os.path.basename(OUT)} ({os.path.getsize(OUT) // 1024} kB)")


if __name__ == "__main__":
    main()
