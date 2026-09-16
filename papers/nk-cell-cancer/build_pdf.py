#!/usr/bin/env python3
"""Render the collection (synthesis notes + evidence listing) to a single PDF."""
import csv
import glob
import os
from collections import Counter

import markdown
from weasyprint import HTML

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "nk_cell_cancer_review.pdf")

CSS = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm;
        @bottom-center { content: counter(page); font-size: 9pt; color: #666; } }
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 10.2pt; line-height: 1.45; color: #111; }
h1 { font-size: 19pt; margin: 0 0 6pt; page-break-before: always; }
h1.title { page-break-before: avoid; font-size: 25pt; margin-top: 40mm; text-align: center; }
p.subtitle { text-align: center; font-size: 12pt; color: #444; }
h2 { font-size: 13pt; margin-top: 16pt; border-bottom: 0.6pt solid #ccc; padding-bottom: 2pt; }
h3 { font-size: 11pt; margin-top: 12pt; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.6pt; background: #f4f4f4; padding: 0 2px; }
table { border-collapse: collapse; width: 100%; font-size: 9pt; margin: 6pt 0; }
th, td { border: 0.5pt solid #bbb; padding: 3pt 4pt; text-align: left; vertical-align: top; }
th { background: #f0f0f0; }
ul { margin: 4pt 0; padding-left: 16pt; }
li { margin-bottom: 3pt; }
a { color: #14448c; text-decoration: none; }
"""
EXT = ["tables", "fenced_code", "sane_lists"]


def md(path):
    with open(path) as fh:
        return markdown.markdown(fh.read(), extensions=EXT)


def main():
    with open(os.path.join(HERE, "index.tsv")) as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    ev = Counter(r["evidence"] for r in rows)
    manuf = sum(1 for r in rows if r["manufacturing"] == "yes")
    years = [int(r["year"]) for r in rows if r["year"].isdigit()]
    title = ("<h1 class='title'>NK cells for cancer: phenotypes, engineering and "
             "manufacturing that improve efficacy</h1>"
             "<p class='subtitle'>A literature synthesis across research and "
             "process-development evidence</p>"
             f"<p class='subtitle'>{len(rows)} curated records, {min(years)}&ndash;{max(years)} "
             f"&middot; {ev['clinical_trial']} clinical trials &middot; "
             f"{ev['process_method']} process/manufacturing methods &middot; "
             f"{ev['preclinical'] + ev['mechanistic']} preclinical/mechanistic &middot; "
             f"{ev['review'] + ev['systematic_review']} reviews &middot; "
             f"{manuf} with culture/manufacturing content</p>")
    body = [title]
    body += [md(p) for p in sorted(glob.glob(os.path.join(HERE, "notes", "*.md")))]
    body.append(md(os.path.join(HERE, "REPORT.md")))
    html = "<html><head><meta charset='utf-8'><style>%s</style></head><body>%s</body></html>" % (
        CSS, "\n".join(body))
    HTML(string=html, base_url=HERE).write_pdf(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
