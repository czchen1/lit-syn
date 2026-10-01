#!/usr/bin/env python3
"""Generate REPORT.md paper listings (grouped by evidence category) from index.tsv."""
import csv, os
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(BASE, "index.tsv")
OUT = os.path.join(BASE, "REPORT.md")

LABELS = {
    "mechanism_preclinical": "Mechanistic rationale (preclinical — not clinical evidence)",
    "heme_concurrent_combination": "Hematologic malignancies — ICI as part of the CAR-T regimen",
    "heme_cd30_hodgkin": "CD30 CAR-T + PD-1 blockade (Hodgkin / T-cell lymphoma)",
    "heme_pd1_maintenance": "PD-1 blockade as post-CAR-T maintenance / consolidation",
    "post_cart_checkpoint_salvage": "Checkpoint blockade as salvage after CAR-T failure",
    "ici_before_cart_sequencing": "ICI before CAR-T (bridging / prior exposure / sequencing)",
    "solid_tumor_combination": "Solid tumors — CAR-T + ICI",
    "engineered_checkpoint_resistance": "CAR-T with built-in checkpoint blockade (KO / locus-integrated / secreted)",
    "reviews_meta_analyses": "Reviews, systematic reviews and meta-analyses",
}
ORDER = list(LABELS.keys())
TIER_LABEL = {
    "prospective_trial": "trial",
    "retrospective_cohort": "retrospective",
    "case_report": "case",
    "engineered_cart": "engineered CAR-T",
    "preclinical": "preclinical",
    "review": "review",
}


def topic(r, prefix):
    for t in r["topics"].split(";"):
        if t.startswith(prefix):
            return t[len(prefix):]
    return ""


def main():
    rows = list(csv.DictReader(open(IDX), delimiter="\t"))
    by_cat = defaultdict(list)
    for r in rows:
        by_cat[r["category"]].append(r)

    lines = []
    for cat in ORDER:
        recs = sorted(by_cat[cat], key=lambda r: (r["year"] or "9999"))
        tiers = Counter(topic(r, "tier:") for r in recs)
        pinned = sum(1 for r in recs if topic(r, "selection:") == "pinned")
        yrs = [int(r["year"]) for r in recs if r["year"].isdigit()]
        lines.append(f"### {LABELS[cat]}\n")
        lines.append(
            f"_{len(recs)} papers · {min(yrs, default='-')}–{max(yrs, default='-')} · "
            f"{pinned} core (hand-curated) · "
            + ", ".join(f"{TIER_LABEL.get(k, k)} {v}" for k, v in tiers.most_common()) + "_\n")
        for r in recs:
            tier = TIER_LABEL.get(topic(r, "tier:"), "")
            star = "**★** " if topic(r, "selection:") == "pinned" else ""
            ft = "  ✓FT" if r["local_fulltext"] else ""
            auth = r["authors"].split(",")[0] + (" et al." if "," in r["authors"] else "")
            lines.append(f"- {star}**{r['year'] or 'n.d.'}** [{tier}] {auth} — "
                         f"{r['title']}. *{r['venue']}*. [link]({r['url']}){ft}")
        lines.append("")

    with open(OUT, "w") as f:
        f.write("<!-- AUTO-GENERATED listings; narrative review lives in notes/00_overview.md -->\n\n")
        f.write("# CAR-T + immune checkpoint inhibitors — paper listings by evidence category\n\n")
        f.write("`★` = core paper the review is built on (hand-curated). `[tier]` = evidence type. "
                "`✓FT` = open-access full text mirrored under `fulltext/`.\n\n")
        f.write("\n".join(lines))
    print("wrote REPORT.md:", len(rows), "papers across", len(ORDER), "categories")


if __name__ == "__main__":
    main()
