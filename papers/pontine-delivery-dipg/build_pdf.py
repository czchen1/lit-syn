"""Render the collection (report + modality notes + reference appendix) to a single PDF."""

import csv
import glob
import os

import markdown
from weasyprint import HTML

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "pontine_delivery_review.pdf")

CSS = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm;
        @bottom-center { content: counter(page); font-size: 9pt; color: #666; } }
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 10.2pt; line-height: 1.45; color: #111; }
h1 { font-size: 19pt; margin: 0 0 6pt; page-break-before: always; }
h1.title { page-break-before: avoid; font-size: 26pt; margin-top: 40mm; text-align: center; }
p.subtitle { text-align: center; font-size: 12pt; color: #444; }
h2 { font-size: 13pt; margin-top: 16pt; border-bottom: 0.6pt solid #ccc; padding-bottom: 2pt; }
h3 { font-size: 11pt; margin-top: 12pt; }
table { border-collapse: collapse; width: 100%; font-size: 8.4pt; margin: 8pt 0; }
th, td { border: 0.4pt solid #bbb; padding: 3pt 4pt; text-align: left; vertical-align: top; }
th { background: #f0f0f0; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.6pt; background: #f4f4f4; padding: 0 2px; }
pre { background: #f6f6f6; padding: 6pt; font-size: 8.4pt; white-space: pre-wrap; }
ul { margin: 4pt 0 4pt 0; padding-left: 16pt; }
li { margin-bottom: 3pt; }
.refs { font-size: 8pt; }
.refs li { margin-bottom: 2pt; }
"""

EXT = ["tables", "fenced_code", "sane_lists"]


def md(path):
    with open(path) as fh:
        return markdown.markdown(fh.read(), extensions=EXT)


def references():
    with open(os.path.join(HERE, "index.tsv")) as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    by_cat = {}
    for r in rows:
        by_cat.setdefault(r["category"], []).append(r)
    parts = ["<h1>Appendix: full reference list</h1>",
             f"<p>All {len(rows)} curated records, grouped by primary modality and ordered by "
             "year (descending). Records without a PMID are conference abstracts.</p>"]
    for cat in sorted(by_cat, key=lambda c: -len(by_cat[c])):
        recs = sorted(by_cat[cat], key=lambda r: r["year"], reverse=True)
        parts.append(f"<h2>{cat.replace('_', ' ')} ({len(recs)})</h2><ul class='refs'>")
        for r in recs:
            ident = f"PMID {r['pmid']}" if r["pmid"] else (f"DOI {r['doi']}" if r["doi"] else "abstract")
            authors = (r["authors"] or "[no author listed]").rstrip(". ")
            parts.append(f"<li>{authors}. {r['title']} <i>{r['venue']}</i> {r['year']}. {ident}.</li>")
        parts.append("</ul>")
    return "\n".join(parts)


def main():
    title = ("<h1 class='title'>Methods of delivery to the pons</h1>"
             "<p class='subtitle'>Diffuse intrinsic pontine glioma, H3K27-altered diffuse midline "
             "glioma, and related CNS diseases</p>"
             "<p class='subtitle'>Literature synthesis of 1,066 curated records (1989&ndash;2026)</p>")
    body = [title, md(os.path.join(HERE, "REPORT.md"))]
    body += [md(p) for p in sorted(glob.glob(os.path.join(HERE, "notes", "*.md")))]
    body.append(references())
    html = "<html><head><meta charset='utf-8'><style>%s</style></head><body>%s</body></html>" % (
        CSS, "\n".join(body))
    HTML(string=html, base_url=HERE).write_pdf(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
