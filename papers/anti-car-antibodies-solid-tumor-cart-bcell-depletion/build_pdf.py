"""Render the collection (report + notes + reference appendix) to a single PDF."""

import csv
import os

import markdown
from weasyprint import HTML

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "rituximab_anticar_cart_report.pdf")

NOTES = [
    "notes/dosing_schedules_extracted.md",
    "notes/registry_and_unpublished_evidence.md",
    "notes/administration_protocol.md",
    "notes/search_strategy.md",
]

CATEGORY_TITLES = {
    "A_anticar_evidence_solid": "A — Anti-CAR antibody evidence in solid tumours",
    "B_mechanism_assays_regulatory": "B — Mechanism, ADA assays, regulatory guidance",
    "C_solid_redosing_trials": "C — Solid-tumour CAR-T trials that redose",
    "D_ritux_pharmacology_schedule": "D — Rituximab pharmacology and what sets a schedule",
    "E_prophylaxis_gene_therapy": "E — Anti-CD20 prophylaxis in gene therapy",
    "F_prophylaxis_ITI_regimens": "F — Immune tolerance induction regimens",
    "G_solid_tumour_HAMA_precedent": "G — Solid-tumour anti-murine-antibody precedent",
    "H_lymphodepletion_context": "H — Lymphodepletion and concomitant immunosuppression",
    "I_confusables_do_not_confuse": "I — Confusables (not evidence)",
    "J_admin_premedication_infusion_reactions": "J — Premedication and infusion reactions",
    "K_admin_screening_prophylaxis": "K — Screening, prophylaxis, and late effects",
    "L_admin_dose_route_pk": "L — Dose, route, and pharmacokinetics",
    "M_admin_cart_context": "M — CAR-T round context",
    "N_admin_fasting_procedure": "N — Procedural fasting guidelines",
}

CSS = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm;
        @bottom-center { content: counter(page); font-size: 9pt; color: #666; } }
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 10.2pt; line-height: 1.45; color: #111; }
h1 { font-size: 19pt; margin: 0 0 6pt; page-break-before: always; }
h1.title { page-break-before: avoid; font-size: 26pt; margin-top: 40mm; text-align: center; }
p.subtitle { text-align: center; font-size: 12pt; color: #444; }
p.caveat { margin-top: 24mm; font-size: 9.5pt; color: #444; border-top: 0.6pt solid #ccc;
           padding-top: 6pt; }
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


def rows():
    with open(os.path.join(HERE, "index.tsv")) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def references(records):
    by_cat = {}
    for r in records:
        by_cat.setdefault(r["category"], []).append(r)
    parts = ["<h1>Appendix: full reference list</h1>",
             f"<p>All {len(records)} curated records, grouped by category and ordered by year "
             "(descending). Records without a PMID are trial-registry entries, preprints, or "
             "presentations.</p>"]
    for cat in sorted(by_cat):
        recs = sorted(by_cat[cat], key=lambda r: r["year"], reverse=True)
        heading = CATEGORY_TITLES.get(cat, cat.replace("_", " "))
        parts.append(f"<h2>{heading} ({len(recs)})</h2><ul class='refs'>")
        for r in recs:
            ident = f"PMID {r['pmid']}" if r["pmid"] else (f"DOI {r['doi']}" if r["doi"] else r["url"])
            authors = (r["authors"] or "[no author listed]").rstrip(". ")
            parts.append(f"<li>{authors}. {r['title']} <i>{r['venue']}</i> {r['year']}. {ident}.</li>")
        parts.append("</ul>")
    return "\n".join(parts)


def main():
    records = rows()
    years = sorted(r["year"] for r in records if r["year"].isdigit())
    title = ("<h1 class='title'>Rituximab around solid-tumour CAR-T</h1>"
             "<p class='subtitle'>B-cell depletion to limit anti-CAR (anti-idiotype) antibodies and "
             "permit repeat dosing: schedules, evidence class, and administration</p>"
             f"<p class='subtitle'>Literature synthesis of {len(records)} curated records "
             f"({years[0]}&ndash;{years[-1]})</p>"
             "<p class='caveat'>No published solid-tumour CAR-T trial has shown that rituximab prevents "
             "anti-CAR antibodies or improves CAR-T persistence. The two CAR-T-specific schedules quoted "
             "here are investigational trial protocols, not standards of care, and the administration "
             "guidance is transferred from the prescribing information and from other indications. "
             "Nothing here is a treatment recommendation for an individual patient.</p>")
    body = [title, md(os.path.join(HERE, "REPORT.md"))]
    body += [md(os.path.join(HERE, n)) for n in NOTES]
    body.append(references(records))
    html = "<html><head><meta charset='utf-8'><style>%s</style></head><body>%s</body></html>" % (
        CSS, "\n".join(body))
    HTML(string=html, base_url=HERE).write_pdf(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
