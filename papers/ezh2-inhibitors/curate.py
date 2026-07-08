#!/usr/bin/env python3
"""Curate raw Europe PMC harvest into a compound-organized index.tsv.

Each EZH2/PRC2-relevant record is assigned to ONE bucket. Priority when a paper
mentions several agents: named clinical-stage inhibitor > tool compound >
cross-cutting theme (CNS/BBB, resistance/SAR, combination/clinical). Non-EZH2
noise (papers that only mention EZH2 as a marker with no inhibitor/PRC2 context)
is dropped.

Selection priorities per bucket:
  1. Foundational / first-disclosure and preclinical potency papers.
  2. Pivotal clinical + review milestones.
  3. CNS / brain-penetrance and mechanism/resistance papers (kept preferentially).
"""
import json, csv, re
from collections import Counter

BASE = "/home/ubuntu/repos/lit-syn/papers/ezh2-inhibitors"
RAW = f"{BASE}/raw_harvest.json"
OUT = f"{BASE}/index.tsv"

d = json.load(open(RAW))

# bucket -> keyword list (matched against title, case-insensitive)
BUCKET_KEYS = {
    "tazemetostat": ["tazemetostat", "epz-6438", "epz6438", "e7438"],
    "valemetostat": ["valemetostat", "ds-3201", "ds3201", "ezharmia"],
    "tulmimetostat_CPI0209": ["tulmimetostat", "cpi-0209", "cpi0209",
                               "cpi-1205", "cpi1205", "lirametostat"],
    "mevrometostat_PF06821497": ["pf-06821497", "pf06821497", "mevrometostat"],
    "SHR2554": ["shr2554", "shr-2554"],
    "GSK126_GSK343": ["gsk126", "gsk2816126", "gsk-126", "gsk343", "gsk503",
                       "gsk926", "gsk-343"],
    "EPZ005687_EI1_EPZ011989": ["epz005687", "epz-005687", "epz011989",
                                 "epz-011989", "ei1 "],
    "UNC1999_EED226": ["unc1999", "unc2400", "eed226", "eed-226", "mak683",
                        "a-395", "eed inhibitor"],
    "DZNep": ["dznep", "deazaneplanocin", "3-deazaneplanocin"],
}

THEME_ORDER = ["cns_bbb_glioma", "resistance_mechanism_sar", "combination_clinical"]

BUCKET_ORDER = [
    "tazemetostat", "valemetostat", "tulmimetostat_CPI0209",
    "mevrometostat_PF06821497", "SHR2554", "GSK126_GSK343",
    "EPZ005687_EI1_EPZ011989", "UNC1999_EED226", "DZNep",
    "cns_bbb_glioma", "resistance_mechanism_sar", "combination_clinical",
]

# a record is EZH2-inhibitor relevant if title carries any of these
EZH2_TERMS = [
    "ezh2", "ezh1", "prc2", "polycomb", "eed", "suz12", "h3k27me3",
    "h3k27 methyl", "histone methyltransferase", "methyltransferase inhibitor",
]
INHIB_TERMS = [
    "inhibitor", "inhibition", "degrad", "protac", "small molecule",
    "small-molecule", "tazemetostat", "valemetostat", "gsk126", "epz",
    "cpi-0209", "cpi-1205", "shr2554", "dznep", "unc1999", "eed226",
    "pf-06821497", "mevrometostat", "tulmimetostat",
]
CNS_TERMS = ["glioma", "glioblastoma", "dipg", "diffuse midline", "h3k27m",
             "h3 k27m", "atrt", "rhabdoid", "medulloblastoma", "brain",
             "blood-brain", "blood brain", "cns", "intracranial",
             "brain-penetrant", "brain penetrant"]
RESIST_TERMS = ["resistance", "resistant", "secondary mutation", "y641", "a677",
                "a687", "gain-of-function", "gain of function",
                "structure-activity", "structure activity", "selectivity",
                "sam-competitive", "crystal", "co-crystal", "degrader",
                "protac", "dual ezh"]
COMBO_TERMS = ["combination", "combined", "synerg", "plus ", " plus", "phase 1",
               "phase 2", "phase i", "phase ii", "phase iii", "clinical trial",
               "objective response", "checkpoint", "enzalutamide", "androgen",
               "bet ", "brd4", "parp"]


def txt(rec):
    return (rec["title"] or "").lower()


def is_relevant(rec):
    t = txt(rec)
    has_ezh = any(x in t for x in EZH2_TERMS)
    has_inh = any(x in t for x in INHIB_TERMS)
    # a named agent alone qualifies
    named = any(x in t for kws in BUCKET_KEYS.values() for x in kws)
    return named or (has_ezh and has_inh)


def assign(rec):
    t = txt(rec)
    # 1) named agent
    for b in BUCKET_ORDER:
        if b in THEME_ORDER:
            continue
        if any(k in t for k in BUCKET_KEYS[b]):
            return b
    # 2) themes for agent-agnostic EZH2-inhibitor papers
    if any(x in t for x in CNS_TERMS):
        return "cns_bbb_glioma"
    if any(x in t for x in RESIST_TERMS):
        return "resistance_mechanism_sar"
    if any(x in t for x in COMBO_TERMS):
        return "combination_clinical"
    return "combination_clinical"


def year_int(rec):
    y = rec["year"]
    return int(y) if y and y.isdigit() else 9999


def url_for(rec):
    if rec["pmcid"]:
        return f"https://pmc.ncbi.nlm.nih.gov/articles/{rec['pmcid']}/"
    if rec["doi"]:
        return f"https://doi.org/{rec['doi']}"
    if rec["pmid"]:
        return f"https://pubmed.ncbi.nlm.nih.gov/{rec['pmid']}/"
    return ""


by_b = {b: [] for b in BUCKET_ORDER}
for rec in d:
    if not is_relevant(rec):
        continue
    by_b[assign(rec)].append(rec)

CAP = {
    "tazemetostat": 34, "valemetostat": 22, "GSK126_GSK343": 22,
    "cns_bbb_glioma": 34, "resistance_mechanism_sar": 26,
    "combination_clinical": 26, "DZNep": 18,
}
DEFAULT_CAP = 16


def select(recs, cap):
    early = sorted([r for r in recs if year_int(r) < 2016], key=year_int)

    def late_key(r):
        pt = (r["pubType"] or "").lower()
        oa = 0 if r["isOA"] == "Y" else 1
        rev = 0 if "review" in pt else 1
        return (oa, rev, -year_int(r))

    late = [r for r in recs if year_int(r) >= 2016]
    late.sort(key=late_key)
    chosen, seen = [], set()
    for r in early + late:
        k = r["pmid"] or r["title"]
        if k in seen:
            continue
        seen.add(k)
        chosen.append(r)
        if len(chosen) >= cap:
            break
    chosen.sort(key=year_int)
    return chosen


def norm_title(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


rows, counts = [], {}
global_titles = set()
for b in BUCKET_ORDER:
    sel = select(by_b[b], CAP.get(b, DEFAULT_CAP))
    sel = [r for r in sel if norm_title(r["title"]) not in global_titles
           and not global_titles.add(norm_title(r["title"]))]
    counts[b] = len(sel)
    for r in sel:
        era = "preclinical_or_early" if year_int(r) < 2016 else "recent"
        topics = [era]
        pt = (r["pubType"] or "").lower()
        if "review" in pt:
            topics.append("review")
        t = txt(r)
        if any(x in t for x in CNS_TERMS):
            topics.append("cns_bbb")
        status = "OA_available" if r["isOA"] == "Y" else ("pmid_only" if r["pmid"] else "record_only")
        rows.append({
            "category": b, "authors": r["authors"], "title": r["title"],
            "venue": r["venue"], "year": r["year"], "pmid": r["pmid"],
            "doi": r["doi"], "pmcid": r["pmcid"], "url": url_for(r),
            "local_fulltext": "", "supp_pdf": "", "topics": ";".join(topics),
            "status": status,
        })

cols = ["category", "authors", "title", "venue", "year", "pmid", "doi", "pmcid",
        "url", "local_fulltext", "supp_pdf", "topics", "status"]
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols, delimiter="\t")
    w.writeheader()
    for r in rows:
        w.writerow(r)

print("total curated:", len(rows))
for b in BUCKET_ORDER:
    print(f"  {b}: {counts[b]}")
