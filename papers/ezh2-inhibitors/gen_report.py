#!/usr/bin/env python3
"""Generate REPORT.md (paper listings by inhibitor/bucket) from index.tsv.

Narrative synthesis (potency, BBB penetration, clinical data) lives in
notes/; this file is auto-generated navigation.
"""
import csv, os
from collections import Counter, defaultdict

BASE = "/home/ubuntu/repos/lit-syn/papers/ezh2-inhibitors"
IDX = os.path.join(BASE, "index.tsv")
OUT = os.path.join(BASE, "REPORT.md")

LABELS = {
    "tazemetostat": "Tazemetostat (EPZ-6438 / E7438) — approved",
    "valemetostat": "Valemetostat (DS-3201) — dual EZH1/2, approved (Japan)",
    "tulmimetostat_CPI0209": "Tulmimetostat (CPI-0209) / CPI-1205 — Constellation/MorphoSys",
    "mevrometostat_PF06821497": "Mevrometostat (PF-06821497) — Pfizer",
    "SHR2554": "SHR2554 — Hengrui",
    "GSK126_GSK343": "GSK126 / GSK343 / GSK503 — GSK tool + clinical",
    "EPZ005687_EI1_EPZ011989": "EPZ005687 / EI1 / EPZ011989 — first-generation tool compounds",
    "UNC1999_EED226": "UNC1999 (EZH1/2) / EED226, MAK683, A-395 (EED allosteric)",
    "DZNep": "DZNep (3-deazaneplanocin A) — indirect PRC2 depletor",
    "cns_bbb_glioma": "CNS / BBB penetration & brain tumors (glioma, DIPG/H3K27M, ATRT)",
    "resistance_mechanism_sar": "Resistance, selectivity, SAR & degraders",
    "combination_clinical": "Combinations & clinical / translational",
}
ORDER = list(LABELS.keys())

rows = list(csv.DictReader(open(IDX), delimiter="\t"))
by_b = defaultdict(list)
for r in rows:
    by_b[r["category"]].append(r)

lines = []
for b in ORDER:
    recs = sorted(by_b[b], key=lambda r: (r["year"] or "9999"))
    if not recs:
        continue
    lines.append(f"### {LABELS[b]}  \n")
    n = len(recs)
    early = sum(1 for r in recs if "preclinical_or_early" in r["topics"])
    cns = sum(1 for r in recs if "cns_bbb" in r["topics"])
    ft = sum(1 for r in recs if r["local_fulltext"])
    yr_lo = min((int(r["year"]) for r in recs if r["year"].isdigit()), default="-")
    yr_hi = max((int(r["year"]) for r in recs if r["year"].isdigit()), default="-")
    lines.append(f"_{n} papers · {yr_lo}–{yr_hi} · {early} early/preclinical · "
                 f"{cns} CNS/BBB-tagged · {ft} full texts mirrored_\n")
    lines.append("")
    for r in recs:
        yr = r["year"] or "n.d."
        ftm = "  ✓FT" if r["local_fulltext"] else ""
        auth = r["authors"].split(",")[0] + (" et al." if "," in r["authors"] else "")
        lines.append(f"- **{yr}** {auth} — {r['title']}. *{r['venue']}*. [link]({r['url']}){ftm}")
    lines.append("")

with open(OUT, "w") as f:
    f.write("<!-- AUTO-GENERATED listings; see notes/00_overview.md for synthesis -->\n\n")
    f.write("# EZH2 inhibitor literature — paper listings by compound\n\n")
    f.write("`✓FT` = open-access full text mirrored under `fulltext/`.\n\n")
    f.write("\n".join(lines))
print("wrote REPORT.md with", len(rows), "papers across", len(by_b), "buckets")
