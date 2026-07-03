#!/usr/bin/env python3
"""Generate REPORT.md target sections (paper listings) from index.tsv.

Narrative synthesis paragraphs are authored separately and merged in via
per-target text in SYNTH below.
"""
import csv, os
from collections import Counter, defaultdict

BASE = "/home/ubuntu/repos/lit-syn/papers/t-cell-engagers"
IDX = os.path.join(BASE, "index.tsv")
OUT = os.path.join(BASE, "REPORT.md")

LABELS = {
    "foundational_platform": "Foundational & platform (target-agnostic)",
    "CD19": "CD19",
    "CD20": "CD20",
    "BCMA": "BCMA (TNFRSF17)",
    "GPRC5D": "GPRC5D",
    "CD33_FLT3_AML": "CD33 / FLT3 / CD123 (myeloid)",
    "EpCAM": "EpCAM",
    "CEA_CEACAM5": "CEA / CEACAM5",
    "gp100_ImmTAC": "gp100 (ImmTAC / TCR-based)",
    "PSMA": "PSMA (FOLH1)",
    "HER2_ERBB2": "HER2 / ERBB2",
    "EGFR_EGFRvIII": "EGFR / EGFRvIII",
    "DLL3": "DLL3",
    "B7H3_CD276": "B7-H3 / CD276",
    "GD2": "GD2",
    "Claudin18_2": "Claudin-18.2 (CLDN18.2)",
    "Mesothelin_MUC_PSCA": "Mesothelin / MUC16 / MUC1 / PSCA",
    "solid_tumor_other": "Other solid-tumor targets (ROR1, 5T4, CD70, HER3, TROP2, FAP, PD-L1)",
    "cart_tce_combination": "Combined CAR-T x T-cell engager",
}
ORDER = list(LABELS.keys())

rows = list(csv.DictReader(open(IDX), delimiter="\t"))
by_t = defaultdict(list)
for r in rows:
    by_t[r["category"]].append(r)

def geo_of(r):
    for tk in r["topics"].split(";"):
        if tk.startswith("geo:"):
            return tk[4:]
    return ""

lines = []
for t in ORDER:
    recs = sorted(by_t[t], key=lambda r: (r["year"] or "9999"))
    lines.append(f"### {LABELS[t]}  \n")
    n = len(recs)
    early = sum(1 for r in recs if "preclinical_or_early" in r["topics"])
    geos = Counter()
    for r in recs:
        for g in geo_of(r).split("|"):
            if g:
                geos[g] += 1
    yr_lo = min((int(r["year"]) for r in recs if r["year"].isdigit()), default="-")
    yr_hi = max((int(r["year"]) for r in recs if r["year"].isdigit()), default="-")
    geo_str = ", ".join(f"{k} {v}" for k, v in geos.most_common())
    lines.append(f"_{n} papers · {yr_lo}–{yr_hi} · {early} early/preclinical · geo: {geo_str}_\n")
    lines.append("")
    for r in recs:
        yr = r["year"] or "n.d."
        g = geo_of(r)
        gtag = f" [{g}]" if g else ""
        ft = "  ✓FT" if r["local_fulltext"] else ""
        link = r["url"]
        auth = r["authors"].split(",")[0] + (" et al." if "," in r["authors"] else "")
        lines.append(f"- **{yr}**{gtag} {auth} — {r['title']}. *{r['venue']}*. [link]({link}){ft}")
    lines.append("")

with open(OUT, "w") as f:
    f.write("<!-- AUTO-GENERATED target listings; see 00_overview.md for synthesis -->\n\n")
    f.write("# T-cell engager literature — paper listings by target\n\n")
    f.write("`✓FT` = open-access full text mirrored under `fulltext/`. "
            "`[geo]` from author affiliations (best-effort).\n\n")
    f.write("\n".join(lines))
print("wrote REPORT.md with", len(rows), "papers across", len(ORDER), "targets")
