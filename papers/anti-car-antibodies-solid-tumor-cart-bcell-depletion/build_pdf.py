"""Render the collection (report + notes + reference appendix) to one markdown file and one PDF.

The markdown file is the single source for both: the PDF is that markdown converted to HTML.
"""

import csv
import os

import markdown
from weasyprint import HTML

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_MD = os.path.join(HERE, "rituximab_anticar_cart_report.md")
OUT_PDF = os.path.join(HERE, "rituximab_anticar_cart_report.pdf")

NOTES = [
    "notes/dosing_schedules_extracted.md",
    "notes/registry_and_unpublished_evidence.md",
    "notes/administration_protocol.md",
    "notes/search_strategy.md",
]

CAVEAT = (
    "No published solid-tumour CAR-T trial has shown that rituximab prevents anti-CAR antibodies or "
    "improves CAR-T persistence. The two CAR-T-specific schedules quoted here are investigational trial "
    "protocols, not standards of care, and the administration guidance is transferred from the "
    "prescribing information and from other indications. Nothing here is a treatment recommendation for "
    "an individual patient."
)

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
h1:first-of-type { page-break-before: avoid; font-size: 26pt; margin-top: 40mm; text-align: center; }
h1:first-of-type + p, h1:first-of-type + p + p { text-align: center; font-size: 12pt; color: #444; }
h2 { font-size: 13pt; margin-top: 16pt; border-bottom: 0.6pt solid #ccc; padding-bottom: 2pt; }
h3 { font-size: 11pt; margin-top: 12pt; }
blockquote { margin: 24mm 0 0 0; font-size: 9.5pt; color: #444; border-top: 0.6pt solid #ccc;
             padding-top: 6pt; }
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


def rows():
    with open(os.path.join(HERE, "index.tsv")) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def front_matter(records):
    years = sorted(r["year"] for r in records if r["year"].isdigit())
    return "\n\n".join([
        "# Rituximab around solid-tumour CAR-T",
        "*B-cell depletion to limit anti-CAR (anti-idiotype) antibodies and permit repeat dosing: "
        "schedules, evidence class, and administration*",
        f"*Literature synthesis of {len(records)} curated records ({years[0]}–{years[-1]})*",
        f"> {CAVEAT}",
    ])


def references(records):
    by_cat = {}
    for r in records:
        by_cat.setdefault(r["category"], []).append(r)
    parts = ["# Appendix: full reference list",
             f"All {len(records)} curated records, grouped by category and ordered by year "
             "(descending). Records without a PMID are trial-registry entries, preprints, or "
             "presentations."]
    for cat in sorted(by_cat):
        recs = sorted(by_cat[cat], key=lambda r: r["year"], reverse=True)
        parts.append(f"## {CATEGORY_TITLES.get(cat, cat.replace('_', ' '))} ({len(recs)})")
        items = []
        for r in recs:
            ident = f"PMID {r['pmid']}" if r["pmid"] else (f"DOI {r['doi']}" if r["doi"] else r["url"])
            authors = (r["authors"] or "[no author listed]").rstrip(". ")
            items.append(f"- {authors}. {r['title']} *{r['venue']}* {r['year']}. {ident}.")
        parts.append("\n".join(items))
    return "\n\n".join(parts)


def main():
    records = rows()
    sections = [front_matter(records)]
    for path in ["REPORT.md"] + NOTES:
        with open(os.path.join(HERE, path)) as fh:
            sections.append(fh.read().strip())
    refs = references(records)
    with open(OUT_MD, "w") as fh:
        fh.write("\n\n---\n\n".join(sections + [refs]) + "\n")
    print(OUT_MD)

    body = [markdown.markdown(s, extensions=EXT) for s in sections]
    body.append("<div class='refs'>%s</div>" % markdown.markdown(refs, extensions=EXT))
    html = "<html><head><meta charset='utf-8'><style>%s</style></head><body>%s</body></html>" % (
        CSS, "\n".join(body))
    HTML(string=html, base_url=HERE).write_pdf(OUT_PDF)
    print(OUT_PDF)


if __name__ == "__main__":
    main()
