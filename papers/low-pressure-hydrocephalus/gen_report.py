#!/usr/bin/env python3
"""Assemble REPORT.md from index.tsv and notes/.

Part I (corpus statistics) and Part III (paper listings by axis) are computed
from index.tsv so they can never drift from the curated corpus. Part II is the
synthesis: notes/00–07 concatenated in order with headings demoted one level.
Regenerate after any curate.py / fetch_fulltext.py / notes/ change.
"""
import csv
import glob
import os
import re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(HERE, "index.tsv")
NOTES = os.path.join(HERE, "notes")
OUT = os.path.join(HERE, "REPORT.md")

AXIS_LABEL = {
    "core_lph": "Core entity — low-/negative-pressure hydrocephalus",
    "mechanism_biomechanics": "Mechanism — brain biomechanics, compliance, elastography, modelling",
    "treatment_techniques": "Treatment techniques — EVD titration, valves, drainage strategy",
    "etiology_settings": "Aetiological settings — trauma, craniectomy, SAH, tumour, infection",
    "adjacent_differentials": "Adjacent differentials — slit ventricle, overdrainage, intracranial hypotension",
    "historical_lph_as_nph": "Historical usage — 'low-pressure hydrocephalus' as a synonym for NPH",
}
AXIS_ORDER = list(AXIS_LABEL)
EVIDENCE_LABEL = {
    "systematic_review": "systematic review",
    "consensus_guideline": "consensus / guideline",
    "review": "narrative review",
    "case_series": "case series",
    "case_series_or_cohort": "case series / cohort",
    "case_report": "case report",
    "clinical_or_mechanistic_study": "clinical / mechanistic study",
    "imaging_physiology_study": "imaging / physiology study",
    "experimental": "experimental (animal / bench)",
    "computational_model": "computational model",
    "comment_letter": "comment / letter",
}
EVIDENCE_ORDER = list(EVIDENCE_LABEL)


def load_rows():
    rows = list(csv.DictReader(open(IDX), delimiter="\t"))
    for r in rows:
        r["_year"] = int(r["year"]) if r["year"].isdigit() else 0
    return rows


def short_author(a):
    a = a.strip()
    if not a:
        return "Anon."
    first = a.split(",")[0].strip()
    return first + (" et al." if "," in a else "")


def md_table(header, body):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(str(c) for c in row) + " |" for row in body]
    return "\n".join(out)


def part_corpus(rows):
    n = len(rows)
    years = [r["_year"] for r in rows if r["_year"]]
    ft = sum(1 for r in rows if r["local_fulltext"])
    status = Counter(r["status"] for r in rows)
    by_axis = Counter(r["axis"] for r in rows)
    lines = ["## Part I — Corpus statistics (computed from `index.tsv`)", ""]
    lines.append(
        f"{n} curated records, {min(years)}–{max(years)}; {ft} open-access full texts "
        f"mirrored under `fulltext/` (`oa_xml`), {status.get('oa_unavailable', 0)} with a PMCID "
        f"but no retrievable XML, {status.get('metadata_only', 0)} metadata-only.")
    lines.append("")
    lines.append("### Records by axis and evidence class")
    lines.append("")
    hdr = ["evidence class"] + [AXIS_LABEL[ax].split(" — ")[0] for ax in AXIS_ORDER] + ["all"]
    per_axis = {ax: Counter(r["evidence"] for r in rows if r["axis"] == ax) for ax in AXIS_ORDER}
    ctot = Counter(r["evidence"] for r in rows)
    body = [[EVIDENCE_LABEL[e]] + [per_axis[ax].get(e, 0) or "" for ax in AXIS_ORDER] + [ctot.get(e, 0)]
            for e in EVIDENCE_ORDER]
    body.append(["**all**"] + [f"**{by_axis[ax]}**" for ax in AXIS_ORDER] + [f"**{n}**"])
    lines.append(md_table(hdr, body))
    lines.append("")

    core = [r for r in rows if r["axis"] == "core_lph"]
    named = sum(1 for r in core if r["names_entity"] == "yes")
    lines.append("### Core-entity axis")
    lines.append("")
    lines.append(
        f"{len(core)} records; {named} name the entity (low-/negative-/very-low-pressure "
        f"hydrocephalus, SILPAH, ALPH) in title or abstract, {len(core) - named} describe the "
        "phenomenon without the label.")
    lines.append("")
    pop = Counter(r["population"] for r in core)
    lines.append("Population: " + ", ".join(f"{k} {v}" for k, v in pop.most_common()) + ".")
    lines.append("")
    sett = Counter()
    for r in core:
        for s in filter(None, r["settings"].split(";")):
            sett[s] += 1
    lines.append("Precipitating setting tags (multi-label, core axis):")
    lines.append("")
    lines.append(md_table(["setting", "n"], sett.most_common()))
    lines.append("")
    trt = Counter()
    for r in core:
        for s in filter(None, r["treatments"].split(";")):
            trt[s] += 1
    lines.append("Treatment tags (multi-label, core axis):")
    lines.append("")
    lines.append(md_table(["treatment", "n"], trt.most_common()))
    lines.append("")

    lines.append("### Publication years (core axis)")
    lines.append("")
    dec = Counter((r["_year"] // 5) * 5 for r in core if r["_year"])
    lines.append(md_table(["period", "n"], [(f"{k}–{k + 4}", v) for k, v in sorted(dec.items())]))
    lines.append("")
    return lines


def demote(md):
    return re.sub(r"^(#{1,5}) ", lambda m: "#" * (len(m.group(1)) + 1) + " ", md, flags=re.M)


def part_synthesis():
    lines = ["## Part II — Synthesis", "",
             "Sections below are the topical notes in `notes/` (00–07), concatenated. "
             "PMIDs cited resolve to rows of `index.tsv` except where a record is explicitly "
             "described as excluded from the corpus.", ""]
    for path in sorted(glob.glob(os.path.join(NOTES, "*.md"))):
        lines.append(demote(open(path).read().rstrip()))
        lines.append("")
        lines.append("---")
        lines.append("")
    return lines


def part_listings(rows):
    lines = ["## Part III — Paper listings by axis (computed from `index.tsv`)", "",
             "`✓FT` = open-access full text mirrored under `fulltext/`. Evidence class in "
             "brackets; `cited` = Europe PMC citation count at harvest.", ""]
    by_axis = defaultdict(list)
    for r in rows:
        by_axis[r["axis"]].append(r)
    for ax in AXIS_ORDER:
        recs = sorted(by_axis[ax], key=lambda r: (r["_year"], r["authors"]))
        lines.append(f"### {AXIS_LABEL[ax]}")
        lines.append("")
        lines.append(f"_{len(recs)} records_")
        lines.append("")
        for r in recs:
            ft = " ✓FT" if r["local_fulltext"] else ""
            pop = f" ({r['population']})" if r["population"] not in ("", "unspecified") else ""
            cited = f", cited {r['cited']}" if r["cited"] and r["cited"] != "0" else ""
            lines.append(
                f"- **{r['year'] or 'n.d.'}** {short_author(r['authors'])} — {r['title']}. "
                f"*{r['venue']}*. [{EVIDENCE_LABEL.get(r['evidence'], r['evidence'])}{pop}{cited}] "
                f"[PMID {r['pmid']}]({r['url']}){ft}")
        lines.append("")
    return lines


def main():
    rows = load_rows()
    out = ["<!-- AUTO-GENERATED by gen_report.py from index.tsv + notes/; edit those, not this file -->",
           "", "# Low-/negative-pressure hydrocephalus — literature review", "",
           f"Consolidated report over the {len(rows)}-record corpus in `index.tsv`. "
           "Part I and Part III are computed from the index; Part II is the written synthesis "
           "from `notes/`. Pipeline: `harvest.py` → `curate.py` → `fetch_fulltext.py` → "
           "`gen_report.py` → `build_pdf.py`.", ""]
    out += part_corpus(rows)
    out += part_synthesis()
    out += part_listings(rows)
    with open(OUT, "w") as f:
        f.write("\n".join(out) + "\n")
    print(f"wrote REPORT.md: {len(rows)} records, {len(AXIS_ORDER)} axes")


if __name__ == "__main__":
    main()
