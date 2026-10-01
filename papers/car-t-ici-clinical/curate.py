#!/usr/bin/env python3
"""Curate the raw Europe PMC harvest into a clinical-evidence index.tsv.

Two-stage selection:

1. PINNED -- the publications the review is actually built on, matched by a
   distinctive title fragment and assigned a category + evidence tier by hand.
   Metadata still comes from the harvest, so nothing is transcribed manually.
2. AUTO -- remaining harvest records that name both a CAR-T term and a
   checkpoint term in the title AND look like patient data or a review. These
   provide breadth/navigation only; they are tagged `selection:auto`.

Evidence tiers (`tier:` topic) are what separate real patient data from
rationale:
  prospective_trial, retrospective_cohort, case_report, engineered_cart,
  preclinical, review
"""
import csv, json, os, re
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw_harvest.json")
OUT = os.path.join(BASE, "index.tsv")

CATEGORY_ORDER = [
    "mechanism_preclinical",
    "heme_concurrent_combination",
    "heme_cd30_hodgkin",
    "heme_pd1_maintenance",
    "post_cart_checkpoint_salvage",
    "ici_before_cart_sequencing",
    "solid_tumor_combination",
    "engineered_checkpoint_resistance",
    "reviews_meta_analyses",
]

# (title fragment, category, tier)
PINNED = [
    # --- mechanistic rationale (preclinical; NOT clinical evidence) ---
    ("human car t cells with cell-intrinsic pd-1 checkpoint blockade",
     "mechanism_preclinical", "preclinical"),
    ("gd2-specific car t cells undergo potent activation and deletion",
     "mechanism_preclinical", "preclinical"),
    # --- heme: ICI as a planned part of the CAR-T regimen ---
    ("tisagenlecleucel plus pembrolizumab", "heme_concurrent_combination", "prospective_trial"),
    ("axicabtagene ciloleucel in combination with atezolizumab",
     "heme_concurrent_combination", "prospective_trial"),
    ("timing of anti-pd-l1 antibody initiation", "heme_concurrent_combination", "prospective_trial"),
    ("anti-cd19 chimeric antigen receptor t cells in combination with nivolumab",
     "heme_concurrent_combination", "retrospective_cohort"),
    ("pd-1 blockade modulates chimeric antigen receptor", "heme_concurrent_combination", "case_report"),
    # --- CD30 / Hodgkin ---
    ("cd30 car-t cells in combination with anti-pd-1 camrelizumab",
     "heme_cd30_hodgkin", "prospective_trial"),
    # --- maintenance / consolidation after CAR-T ---
    ("programmed cell death 1 inhibitor maintenance therapy after combined treatment",
     "heme_pd1_maintenance", "retrospective_cohort"),
    ("programmed cell death 1 inhibitor maintenance after chimeric antigen receptor t cells",
     "heme_pd1_maintenance", "retrospective_cohort"),
    ("sequential pd-1 inhibitors as consolidative therapy", "heme_pd1_maintenance",
     "retrospective_cohort"),
    # --- ICI as salvage after CAR-T failure ---
    ("pembrolizumab for b-cell lymphomas relapsing after or refractory to cd19-directed",
     "post_cart_checkpoint_salvage", "prospective_trial"),
    ("efficacy of checkpoint inhibition after car-t failure", "post_cart_checkpoint_salvage",
     "retrospective_cohort"),
    ("outcomes of first therapy after cd19-car-t treatment failure", "post_cart_checkpoint_salvage",
     "retrospective_cohort"),
    # --- ICI before CAR-T / sequencing ---
    ("real-world outcomes of axicabtagene ciloleucel in adult patients with primary mediastinal",
     "ici_before_cart_sequencing", "retrospective_cohort"),
    # --- solid tumors ---
    ("regional mesothelin-targeted car t-cell therapy", "solid_tumor_combination",
     "prospective_trial"),
    ("repeated peripheral infusions of anti-egfrviii car t cells in combination with pembrolizumab show no efficacy",
     "solid_tumor_combination", "prospective_trial"),
    ("claudin18.2-specific car t cells in gastrointestinal cancers", "solid_tumor_combination",
     "prospective_trial"),
    ("car t cells administered in combination with lymphodepletion and pd-1 inhibition",
     "solid_tumor_combination", "prospective_trial"),
    # --- CAR-T with built-in checkpoint blockade ---
    ("anti-pd-1 nanobody-armored msln car-t", "engineered_checkpoint_resistance",
     "engineered_cart"),
    ("safety and feasibility of crispr-edited t cells in patients with refractory non-small-cell",
     "engineered_checkpoint_resistance", "engineered_cart"),
    ("pd1 locus specifically integrated", "engineered_checkpoint_resistance", "engineered_cart"),
    # --- syntheses ---
    ("combinational car t-cell therapy for solid tumors", "reviews_meta_analyses", "review"),
    ("ray of dawn", "reviews_meta_analyses", "review"),
    ("synergistic immunotherapeutic impact of engineered car-t cells with pd-1 blockade",
     "reviews_meta_analyses", "review"),
    ("combined or sequential treatment with immune checkpoint inhibitors and car-t",
     "reviews_meta_analyses", "review"),
]

PRECLIN_CAP = 40  # max auto-selected preclinical papers kept as context

CART = ("car-t", "car t", "chimeric antigen receptor", "cart cell", "cart-cell")
ICI = ("pd-1", "pd1", "pd-l1", "pdl1", "checkpoint", "ctla-4", "ctla4", "pembrolizumab",
       "nivolumab", "atezolizumab", "durvalumab", "camrelizumab", "sintilimab",
       "tislelizumab", "ipilimumab", "toripalimab", "lag-3", "tim-3")
CLINICAL = ("patient", "phase", "trial", "cohort", "case", "real-world", "first-in-human",
            "clinical")
PRECLIN = ("preclinical", "murine", " mice", "in vitro", "mouse", "xenograft",
           "organoid", "patient-derived", "cell line", "humanized model")
DRUGS = ("pembrolizumab", "nivolumab", "atezolizumab", "durvalumab", "camrelizumab",
         "sintilimab", "tislelizumab", "ipilimumab", "toripalimab", "penpulimab")
REVIEWISH = ("review", "meta-analysis", "systematic", "perspective", "prospects",
             "challenges", "landscape")
SOLID = ("solid", "mesotheli", "glioblastoma", "glioma", "gastric", "gastrointestinal",
         "breast", "neuroblastoma", "hepatocellular", "pancrea", "lung", "ovarian",
         "claudin", "egfrviii", "muc1", "gpc3", "her2", "gd2", "b7-h3", "sarcoma")
HEME = ("lymphoma", "leukemia", "leukaemia", "myeloma", "hodgkin", "dlbcl", "b-all",
        "all ", "b-cell malignanc", "nhl")


def norm(s):
    if not isinstance(s, str):
        s = ""
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    return re.sub(r"\s+", " ", s).strip()


def main():
    raw = json.load(open(RAW))
    recs = {}
    for cat, rows in raw.items():
        for r in rows:
            key = (r.get("pmid") or r.get("pmcid") or r.get("doi") or r.get("id") or "").lower()
            if not key:
                continue
            r.setdefault("_harvest_cats", [])
            if key in recs:
                recs[key]["_harvest_cats"].append(cat)
            else:
                r["_harvest_cats"] = [cat]
                recs[key] = r

    assigned = {}   # key -> (category, tier, selection)
    for frag, cat, tier in PINNED:
        hits = [(k, r) for k, r in recs.items()
                if frag in norm(r.get("title", "")).lower() and r.get("pmid")]
        if not hits:
            print(f"  ! pinned not in harvest: {frag}")
            continue
        # prefer the journal record (has a pmid) with the most complete metadata
        k, r = sorted(hits, key=lambda kr: -len(norm(kr[1].get("abstractText", ""))))[0]
        assigned[k] = (cat, tier, "pinned")

    for k, r in recs.items():
        if k in assigned:
            continue
        t = norm(r.get("title", "")).lower()
        ab = norm(r.get("abstractText", "")).lower()
        title_match = any(c in t for c in CART) and any(i in t for i in ICI)
        abstract_match = (any(c in t for c in CART) and any(d in ab for d in DRUGS)
                          and any(i in ab for i in ("combin", "after car", "following car",
                                                    "maintenance", "sequential")))
        if not (title_match or abstract_match):
            continue
        is_rev = any(w in t for w in REVIEWISH)
        has_clinical = any(w in t for w in CLINICAL)
        if is_rev:
            cat, tier = "reviews_meta_analyses", "review"
        elif (not has_clinical or any(w in t for w in PRECLIN)
              or any(w in ab[:400] for w in (" mice", "murine", "xenograft"))):
            cat, tier = "mechanism_preclinical", "preclinical"
        else:
            hcat = r["_harvest_cats"][0]
            cat = hcat if hcat in CATEGORY_ORDER else None
            if cat == "reviews_meta_analyses":
                cat = ("post_cart_checkpoint_salvage"
                       if any(w in t for w in ("after car", "failure", "failed", "relapsing after"))
                       else None)
            if cat is None or cat in ("heme_cd19_combination",):
                cat = ("solid_tumor_combination" if any(w in t for w in SOLID)
                       else "heme_concurrent_combination")
            if cat == "post_cart_checkpoint_salvage" and "after" not in t and "failure" not in t:
                cat = "heme_concurrent_combination"
            tier = ("case_report" if "case" in t else
                    "prospective_trial" if ("phase" in t or "trial" in t) else
                    "retrospective_cohort")
        assigned[k] = (cat, tier, "auto")

    # The preclinical bucket is context, not evidence: cap it so it cannot
    # dominate the collection (newest first, engineered-CAR-T designs preferred).
    preclin = [k for k, (c, t, sel) in assigned.items()
               if c == "mechanism_preclinical" and sel == "auto"]
    ENG = ("knockout", "knock-out", "secret", "switch receptor", "dominant-negative",
           "locus", "edit", "armored", "nanobody", "scfv")

    def preclin_rank(k):
        t = norm(recs[k].get("title", "")).lower()
        return (0 if any(w in t for w in ENG) else 1, -int(recs[k].get("pubYear") or 0))

    for k in sorted(preclin, key=preclin_rank)[PRECLIN_CAP:]:
        del assigned[k]

    by_cat = defaultdict(list)
    for k, (cat, tier, sel) in assigned.items():
        r = recs[k]
        topics = [f"tier:{tier}", f"selection:{sel}"]
        t = norm(r.get("title", "")).lower()
        if any(w in t for w in SOLID):
            topics.append("setting:solid_tumor")
        if any(w in t for w in HEME):
            topics.append("setting:hematologic")
        pmcid = r.get("pmcid") or ""
        oa = (r.get("isOpenAccess") == "Y") and bool(pmcid)
        url = (f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/" if pmcid else
               (f"https://doi.org/{r['doi']}" if r.get("doi") else
                f"https://europepmc.org/abstract/MED/{r.get('pmid','')}"))
        by_cat[cat].append({
            "category": cat,
            "authors": norm(r.get("authorString", "")),
            "title": norm(r.get("title", "")).rstrip("."),
            "venue": norm(r.get("journalTitle")
                              or (r.get("journalInfo", {}) or {}).get("journal", {}).get("title")
                              or ""),
            "year": r.get("pubYear", ""),
            "pmid": r.get("pmid", ""),
            "doi": r.get("doi", ""),
            "pmcid": pmcid,
            "url": url,
            "local_fulltext": "",
            "supp_pdf": "",
            "topics": ";".join(topics),
            "status": "OA_available" if oa else ("pmid_only" if r.get("pmid") else "metadata_only"),
        })

    cols = ["category", "authors", "title", "venue", "year", "pmid", "doi", "pmcid",
            "url", "local_fulltext", "supp_pdf", "topics", "status"]
    n = 0
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        for cat in CATEGORY_ORDER:
            rows = sorted(by_cat[cat], key=lambda r: (r["year"] or "9999", r["title"]))
            for r in rows:
                w.writerow(r)
                n += 1
            print(f"{cat}: {len(rows)}")
    print("wrote", n, "rows ->", OUT)


if __name__ == "__main__":
    main()
