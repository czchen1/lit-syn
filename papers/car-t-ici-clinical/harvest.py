#!/usr/bin/env python3
"""Harvest CAR-T x immune-checkpoint-inhibitor (ICI) literature from Europe PMC.

Scope: CLINICAL evidence (trials, cohorts, case series) on CAR-T combined with,
or sequenced around, checkpoint blockade -- plus the engineered
"checkpoint-resistant CAR-T" literature and the mechanistic/review anchors
needed to interpret it.
"""
import json, os, time, urllib.parse, urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "raw_harvest.json")

QUERIES = {
    "heme_cd19_combination": [
        '("CAR-T" OR "CAR T" OR "chimeric antigen receptor") AND (pembrolizumab OR nivolumab OR atezolizumab OR durvalumab OR camrelizumab OR sintilimab OR tislelizumab) AND (lymphoma OR leukemia OR leukaemia)',
        '"chimeric antigen receptor" AND "PD-1" AND (combination OR combined) AND ("large B-cell" OR DLBCL OR "B-ALL" OR "non-Hodgkin")',
        'TITLE:("CAR" AND ("PD-1" OR "PD-L1" OR checkpoint)) AND (trial OR phase OR patients)',
    ],
    "heme_cd30_hodgkin": [
        '("CD30" AND ("CAR-T" OR "CAR T" OR "chimeric antigen receptor")) AND ("PD-1" OR nivolumab OR camrelizumab OR pembrolizumab)',
        'Hodgkin AND "chimeric antigen receptor" AND checkpoint',
    ],
    "post_cart_checkpoint_salvage": [
        '("after" OR "following" OR salvage OR relapse) AND "CAR T" AND (pembrolizumab OR nivolumab) AND (failure OR progression OR relapsed)',
        '"checkpoint inhibition after CAR-T" OR "checkpoint inhibitor after CAR T"',
    ],
    "pd1_maintenance_consolidation": [
        '"PD-1 inhibitor" AND maintenance AND "CAR-T"',
        'consolidative AND "PD-1" AND "CAR T" AND lymphoma',
    ],
    "ici_sequencing_before_cart": [
        '"prior checkpoint" AND "CAR T"',
        '(timing OR sequencing) AND ("PD-1" OR "PD-L1") AND "CAR T-cell therapy" AND lymphoma',
    ],
    "solid_tumor_combination": [
        '"chimeric antigen receptor" AND (pembrolizumab OR nivolumab OR ipilimumab OR atezolizumab) AND (mesothelioma OR glioblastoma OR "solid tumor" OR "solid tumour" OR gastric OR breast OR neuroblastoma)',
        'mesothelin AND "CAR T" AND (pembrolizumab OR "PD-1")',
        'EGFRvIII AND "CAR T" AND pembrolizumab',
        '"claudin18.2" AND "CAR T" AND "PD-1"',
    ],
    "engineered_checkpoint_resistance": [
        '("PD-1 knockout" OR "PD1 knockout" OR "PD-1 disrupted" OR "PD-1 edited" OR "dominant-negative PD-1" OR "PD-1 locus") AND ("CAR T" OR "chimeric antigen receptor" OR "T cells") AND (patients OR trial OR phase)',
        '("secreting" OR "secreted" OR nanobody OR scFv) AND "PD-1" AND "chimeric antigen receptor" AND (patients OR trial)',
        '"switch receptor" AND "chimeric antigen receptor" AND "PD-1"',
    ],
    "mechanism_preclinical": [
        '"chimeric antigen receptor" AND "PD-1" AND (exhaustion OR "PD-L1 blockade") AND (mice OR murine OR preclinical OR model)',
        'Cherkassky AND mesothelin AND "PD-1"',
    ],
    "reviews_meta_analyses": [
        '("systematic review" OR meta-analysis OR review) AND "CAR T" AND ("immune checkpoint" OR "PD-1")',
        '"combinational CAR T-cell therapy" OR "CAR-T cell therapy combined with ICIs"',
    ],
}


# Key publications the topic queries can miss (exact-title lookups). Kept
# explicit so the curated index is reproducible rather than search-rank dependent.
PINNED = {
    "heme_cd19_combination": [
        'TITLE:"tisagenlecleucel plus pembrolizumab"',
        'TITLE:"Anti-CD19 Chimeric Antigen Receptor T Cells in Combination With Nivolumab"',
        'TITLE:"Axicabtagene Ciloleucel in Combination with Atezolizumab"',
        'TITLE:"PD-1 blockade modulates chimeric antigen receptor"',
    ],
    "post_cart_checkpoint_salvage": [
        'TITLE:"Pembrolizumab for B-cell lymphomas relapsing after or refractory to CD19-directed"',
        'TITLE:"Outcomes of first therapy after CD19-CAR-T treatment failure in large B-cell lymphoma"',
    ],
    "pd1_maintenance_consolidation": [
        'TITLE:"programmed cell death 1 inhibitor maintenance"',
        'TITLE:"Efficacy of programmed cell death 1 inhibitor maintenance after chimeric antigen receptor T cells"',
    ],
    "ici_sequencing_before_cart": [
        'TITLE:"Real-world outcomes of axicabtagene ciloleucel in adult patients with primary mediastinal"',
    ],
    "engineered_checkpoint_resistance": [
        'TITLE:("PD1" AND "integrated" AND ("CAR-T" OR "CAR T"))',
        'TITLE:("non-viral" AND ("CAR-T" OR "CAR T") AND ("PD1" OR "PD-1"))',
        'TITLE:"CRISPR-edited T cells in patients with refractory non-small-cell lung cancer"',
        'TITLE:("nanobody" AND "PD-1" AND ("CAR T" OR "CAR-T"))',
        'TITLE:("PD-1" AND "knockout" AND ("CAR T" OR "CAR-T") AND (patients OR trial OR clinical))',
    ],
    "mechanism_preclinical": [
        'TITLE:"Human CAR T cells with cell-intrinsic PD-1 checkpoint blockade"',
        'TITLE:"GD2-specific CAR T cells undergo potent activation and deletion"',
    ],
}


def search(q, page_size=100, pages=2):
    out = []
    cursor = "*"
    for _ in range(pages):
        params = urllib.parse.urlencode({
            "query": q, "format": "json", "pageSize": page_size,
            "cursorMark": cursor, "resultType": "core",
        })
        req = urllib.request.Request(EPMC + "?" + params,
                                     headers={"User-Agent": "lit-syn/1.0"})
        with urllib.request.urlopen(req, timeout=90) as r:
            d = json.load(r)
        out.extend(d.get("resultList", {}).get("result", []))
        nxt = d.get("nextCursorMark")
        if not nxt or nxt == cursor:
            break
        cursor = nxt
        time.sleep(0.34)
    return out


def main():
    harvest = {}
    for cat, qs in QUERIES.items():
        qs = qs + PINNED.get(cat, [])
        recs = {}
        for q in qs:
            try:
                res = search(q)
            except Exception as e:  # network hiccup: keep going
                print(f"  ! {cat}: {e}")
                continue
            for r in res:
                key = r.get("pmid") or r.get("pmcid") or r.get("doi") or r.get("id")
                if key:
                    r["_query"] = q
                    recs.setdefault(key, r)
            time.sleep(0.34)
        harvest[cat] = list(recs.values())
        print(f"{cat}: {len(harvest[cat])}")
    with open(OUT, "w") as f:
        json.dump(harvest, f, indent=1)
    print("total", sum(len(v) for v in harvest.values()), "->", OUT)


if __name__ == "__main__":
    main()
