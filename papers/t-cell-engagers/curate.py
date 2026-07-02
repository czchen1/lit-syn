#!/usr/bin/env python3
"""Curate raw Europe PMC harvest into a target-organized index.tsv.

Each record is (re)assigned to a target bucket ONLY if its title matches that
target's antigen / target-specific agent. TCE-relevant records that do not name
a specific antigen (generic platform papers / cross-target reviews) go to
`foundational_platform`. Combination CAR-T x TCE papers go to
`cart_tce_combination`.

Selection priorities per target:
  1. Early / preclinical foundational work (older years kept preferentially).
  2. Geographic diversity (Europe + China guaranteed where available).
  3. Key clinical / review milestones.
"""
import json, csv
from collections import Counter

RAW = "/home/ubuntu/repos/lit-syn/papers/t-cell-engagers/raw_harvest.json"
OUT = "/home/ubuntu/repos/lit-syn/papers/t-cell-engagers/index.tsv"

d = json.load(open(RAW))

# target -> (antigen keywords, target-specific agent keywords)
TARGET_KEYS = {
    "CD19": (["cd19"], ["blinatumomab"]),
    "CD20": (["cd20"], ["glofitamab", "mosunetuzumab", "epcoritamab",
                         "odronextamab", "plamotamab"]),
    "BCMA": (["bcma", "b-cell maturation", "b cell maturation", "tnfrsf17"],
             ["teclistamab", "elranatamab", "amg 420", "amg420", "pavurutamab",
              "pf-06863135", "linvoseltamab"]),
    "GPRC5D": (["gprc5d"], ["talquetamab", "forimtamig"]),
    "CD33_FLT3_AML": (["cd33", "flt3", "cd123"],
                      ["flotetuzumab", "vibecotamab", "amg 330", "amg330",
                       "amg 673", "amg673", "pivekimab"]),
    "EpCAM": (["epcam", "epithelial cell adhesion"],
              ["catumaxomab", "solitomab", "mt110", "amg 110", "amg110"]),
    "CEA_CEACAM5": (["cea", "ceacam5", "carcinoembryonic"],
                    ["cibisatamab", "cea-tcb", "ro6958688", "medi-565",
                     "amg 211", "amg211", "tidutamab"]),
    "gp100_ImmTAC": (["gp100", "gp-100", "uveal", "immtac"],
                     ["tebentafusp", "imcgp100"]),
    "PSMA": (["psma", "prostate-specific membrane", "folh1"],
             ["pasotuxizumab", "amg 212", "amg212", "bay2010112", "hpn424",
              "ccw702", "regn5678", "acapatamab", "amg 160", "amg160"]),
    "HER2_ERBB2": (["her2", "erbb2", "her-2"],
                   ["ertumaxomab", "runimotamab", "zanidatamab"]),
    "EGFR_EGFRvIII": (["egfr", "egfrviii", "egfrv iii"], []),
    "DLL3": (["dll3", "delta-like ligand 3", "delta like ligand 3"],
             ["tarlatamab", "amg 757", "amg757", "bi 764532", "bi764532",
              "obrixtamine", "hpn328"]),
    "B7H3_CD276": (["b7-h3", "b7h3", "cd276"], ["hpn536", "vudalimab"]),
    "GD2": (["gd2", "ganglioside gd2", "disialoganglioside"], ["ng-cu"]),
    "Claudin18_2": (["claudin 18.2", "claudin-18.2", "cldn18.2", "cldn 18.2"],
                    ["givastomig", "askb589", "q-1802", "amg 910", "amg910"]),
    "Mesothelin_MUC_PSCA": (["mesothelin", "muc16", "muc1", "psca",
                             "prostate stem cell antigen"],
                            ["regn5668", "hpn536", "amg 199", "amg199"]),
    "solid_tumor_other": (["ror1", "5t4", "cd70", "fap ", " fap", "trop2",
                           "trop-2", "nectin", "steap", "cd133", "her3",
                           "erbb3", "pd-l1"], []),
}

# order in which targets appear in the index
TARGET_ORDER = [
    "foundational_platform", "CD19", "CD20", "BCMA", "GPRC5D", "CD33_FLT3_AML",
    "EpCAM", "CEA_CEACAM5", "gp100_ImmTAC", "PSMA", "HER2_ERBB2",
    "EGFR_EGFRvIII", "DLL3", "B7H3_CD276", "GD2", "Claudin18_2",
    "Mesothelin_MUC_PSCA", "solid_tumor_other", "cart_tce_combination",
]

DRUG_TERMS = [
    "blinatumomab", "catumaxomab", "solitomab", "mt110", "amg", "tarlatamab",
    "tebentafusp", "immtac", "teclistamab", "elranatamab", "talquetamab",
    "glofitamab", "mosunetuzumab", "epcoritamab", "odronextamab", "cibisatamab",
    "flotetuzumab", "vibecotamab", "pasotuxizumab", "cevostamab", "givastomig",
    "ertumaxomab", "obrixtamine", "runimotamab", "hpn", "regn", "ccw702",
    "bi 764532", "bi764532", "acapatamab", "duvortuxizumab",
]
# strong indicators of a genuine CD3-redirecting T-cell engager
TCE_TERMS = [
    "bite", "bispecific t-cell engager", "bispecific t cell engager",
    "t-cell engager", "t cell engager", "cd3 bispecific", "cd3-bispecific",
    "trifunctional", "trispecific t", "tandem diabody",
    "dual-affinity re-targeting", "immtac", "cd3xcd", "cd3 x", "x cd3",
    "×cd3", "cd3×", "immune cell engager", "stab-t",
    "anti-cd3", "/cd3", "cd3-based", "redirect t",
]
COMBO_TERMS = ["secreting", "secrete", "stab-t", "armored car", "car t cell",
               "car-t cell"]

def is_tce(rec):
    t = (rec["title"] or "").lower()
    if any(x in t for x in TCE_TERMS) or any(x in t for x in DRUG_TERMS):
        return True
    # "bispecific" only counts as a TCE when paired with T-cell/CD3 context
    if "bispecific" in t and ("cd3" in t or "t cell" in t or "t-cell" in t
                              or "t-lymphocyte" in t or "t lymphocyte" in t):
        return True
    return False

def is_combo(rec):
    """Genuine CAR-T x TCE combination: CAR cells engineered to secrete/express
    a T-cell engager, or explicit combination regimens. Excludes simple
    'BsAb vs CAR-T' comparisons and 'salvage after CAR-T failure' sequencing."""
    t = (rec["title"] or "").lower()
    has_car = ("car-t" in t or "car t" in t or "chimeric antigen" in t
               or " car " in t or "car-modified" in t or "car cell" in t)
    has_eng = (any(x in t for x in ["bite", "engager", "stab-t", "/cd3",
               "anti-cd3", "cd3 molecule", "dual-targeting antibody", "tce"])
               or "bispecific t" in t or "bispecific antibody" in t)
    combo_signal = any(x in t for x in [
        "secret", "armored", "armoured", "engineered to express",
        "engineered to secrete", "expressing a bite", "expressing bite",
        "expressing an engager", "combination", "combined with", "plus",
        "co-express", "coexpress", "deliver"])
    # exclude comparison / sequencing framing
    bad = any(x in t for x in ["versus", " vs ", " vs.", "after car", "car-t failure",
                               "car t failure", "failure", "relapsing after",
                               "comparison", "compare", "salvage", "indirect treatment",
                               "lymphodepletion", "bispecific targeted car",
                               "bispecific car"])
    if has_car and has_eng and combo_signal and not bad:
        return True
    return False

def assign_target(rec):
    """Only TCE/combination-relevant records are assigned. Non-TCE hits dropped."""
    t = (rec["title"] or "").lower()
    if is_combo(rec):
        return "cart_tce_combination"
    if not is_tce(rec):
        return None
    # specific antigen match (record already known TCE-relevant)
    for tgt in TARGET_ORDER:
        if tgt in ("foundational_platform", "cart_tce_combination"):
            continue
        antigens, drugs = TARGET_KEYS[tgt]
        if any(a in t for a in antigens) or any(dr in t for dr in drugs):
            return tgt
    return "foundational_platform"

def year_int(rec):
    y = rec["year"]
    return int(y) if y.isdigit() else 9999

def url_for(rec):
    if rec["pmcid"]:
        return f"https://pmc.ncbi.nlm.nih.gov/articles/{rec['pmcid']}/"
    if rec["doi"]:
        return f"https://doi.org/{rec['doi']}"
    if rec["pmid"]:
        return f"https://pubmed.ncbi.nlm.nih.gov/{rec['pmid']}/"
    return ""

by_t = {t: [] for t in TARGET_ORDER}
for rec in d:
    tgt = assign_target(rec)
    if tgt:
        by_t[tgt].append(rec)

CAP = {"foundational_platform": 30, "cart_tce_combination": 24,
       "CD19": 16, "BCMA": 16, "DLL3": 16, "Claudin18_2": 16}
DEFAULT_CAP = 14

def select(recs, cap):
    early = sorted([r for r in recs if year_int(r) < 2016], key=year_int)
    late = [r for r in recs if year_int(r) >= 2016]
    def late_key(r):
        geo = r["geo"]
        geo_pri = 0 if ("China" in geo or "Europe" in geo) else 1
        pt = (r["pubType"] or "").lower()
        rev = 0 if ("review" in pt) else 1
        return (geo_pri, rev, -year_int(r))
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

import re as _re
def norm_title(s):
    return _re.sub(r"[^a-z0-9]", "", (s or "").lower())

rows, counts = [], {}
global_titles = set()
for t in TARGET_ORDER:
    sel = select(by_t[t], CAP.get(t, DEFAULT_CAP))
    sel = [r for r in sel if norm_title(r["title"]) not in global_titles
           and not global_titles.add(norm_title(r["title"]))]
    counts[t] = len(sel)
    for r in sel:
        era = "preclinical_or_early" if year_int(r) < 2016 else "recent"
        topics = []
        if r["geo"]:
            topics.append("geo:" + r["geo"])
        topics.append(era)
        pt = (r["pubType"] or "").lower()
        if "review" in pt:
            topics.append("review")
        status = "OA_available" if r["isOA"] == "Y" else ("pmid_only" if r["pmid"] else "record_only")
        rows.append({
            "category": t, "authors": r["authors"], "title": r["title"],
            "venue": r["venue"], "year": r["year"], "pmid": r["pmid"],
            "doi": r["doi"], "pmcid": r["pmcid"], "url": url_for(r),
            "local_fulltext": "", "supp_pdf": "", "topics": ";".join(topics),
            "status": status,
        })

cols = ["category","authors","title","venue","year","pmid","doi","pmcid","url","local_fulltext","supp_pdf","topics","status"]
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols, delimiter="\t")
    w.writeheader()
    for row in rows:
        w.writerow(row)

print("total curated rows:", len(rows))
for t in TARGET_ORDER:
    print(f"  {t}: {counts[t]}")
geos = Counter()
for row in rows:
    for tk in row["topics"].split(";"):
        if tk.startswith("geo:"):
            for g in tk[4:].split("|"):
                geos[g]+=1
print("geo coverage:", dict(geos))
print("OA rows:", sum(1 for r in rows if r["status"]=="OA_available"))
print("early/preclinical rows:", sum(1 for r in rows if "preclinical_or_early" in r["topics"]))
