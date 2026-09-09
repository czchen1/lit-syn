"""Render the collection (report + modality notes + reference appendix) to a single PDF.

The appendix lists every curated record grouped by modality and evidence level; the
full corpus is large, so tier-3 preclinical records are summarised as a count per
modality rather than listed individually (they remain in index.tsv).
"""

import csv
import glob
import os
from collections import Counter

import markdown
from weasyprint import HTML

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "recent_cancer_therapies_2026_review.pdf")

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
.refs { font-size: 7.6pt; }
.refs li { margin-bottom: 1.5pt; }
"""

EXT = ["tables", "fenced_code", "sane_lists"]
EV_ORDER = ["clinical_phase3", "clinical_phase2", "clinical_phase1", "clinical_other",
            "evidence_synthesis", "preclinical"]
EV_LABEL = {"clinical_phase3": "Phase 3 / randomised", "clinical_phase2": "Phase 2",
            "clinical_phase1": "Phase 1 / first-in-human", "clinical_other": "Other clinical",
            "evidence_synthesis": "Systematic reviews / meta-analyses",
            "preclinical": "Preclinical"}


def md(path):
    with open(path) as fh:
        return markdown.markdown(fh.read(), extensions=EXT)


def references():
    with open(os.path.join(HERE, "index.tsv")) as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    by_cat = {}
    for r in rows:
        by_cat.setdefault(r["category"], []).append(r)
    parts = ["<h1>Appendix: reference list</h1>",
             f"<p>{len(rows)} curated records (2026-03-09 to 2026-09-09), grouped by modality "
             "and evidence level, ordered by priority then date. Tier-3 preclinical records "
             "and tier-3 'other clinical' records are counted rather than listed; all are in "
             "<code>index.tsv</code>.</p>"]
    for cat in sorted(by_cat, key=lambda c: -len(by_cat[c])):
        recs = by_cat[cat]
        parts.append(f"<h2>{cat.replace('_', ' ')} ({len(recs)})</h2>")
        by_ev = {}
        for r in recs:
            by_ev.setdefault(r["evidence"], []).append(r)
        for ev in EV_ORDER:
            sub = by_ev.get(ev, [])
            if not sub:
                continue
            listed = [r for r in sub if not (ev in ("preclinical", "clinical_other") and r["tier"] == "3")]
            omitted = len(sub) - len(listed)
            parts.append(f"<h3>{EV_LABEL[ev]} ({len(sub)})</h3>")
            if listed:
                parts.append("<ul class='refs'>")
                for r in listed:
                    ident = f"PMID {r['pmid']}" if r["pmid"] else (f"DOI {r['doi']}" if r["doi"] else "")
                    authors = (r["authors"] or "[no author listed]").rstrip(". ")
                    if len(authors) > 120:
                        authors = authors[:117].rsplit(",", 1)[0] + ", et al"
                    parts.append(f"<li>{authors}. {r['title']}. <i>{r['venue']}</i> {r['date']}. {ident}.</li>")
                parts.append("</ul>")
            if omitted:
                parts.append(f"<p class='refs'><i>+ {omitted} tier-3 records not listed.</i></p>")
    return "\n".join(parts)


def main():
    with open(os.path.join(HERE, "index.tsv")) as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    ev = Counter(r["evidence"] for r in rows)
    n_clin = sum(v for k, v in ev.items() if k.startswith("clinical"))
    title = ("<h1 class='title'>Cancer therapies: the last six months</h1>"
             "<p class='subtitle'>Clinical and preclinical publications, 9 March &ndash; 9 September 2026, "
             "across all therapeutic modalities</p>"
             f"<p class='subtitle'>Literature synthesis of {len(rows):,} curated records "
             f"({n_clin:,} clinical, {ev['preclinical']:,} preclinical, "
             f"{ev['evidence_synthesis']:,} evidence syntheses)</p>")
    body = [title, md(os.path.join(HERE, "REPORT.md"))]
    body += [md(p) for p in sorted(glob.glob(os.path.join(HERE, "notes", "*.md")))]
    body.append(references())
    html = "<html><head><meta charset='utf-8'><style>%s</style></head><body>%s</body></html>" % (
        CSS, "\n".join(body))
    HTML(string=html, base_url=HERE).write_pdf(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
