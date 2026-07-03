#!/usr/bin/env python3
"""Harvest T-cell engager (TCE) + CAR-T/TCE-combination literature from Europe PMC.

Organized by target antigen. Emphasis on early/preclinical work and geographic
diversity (Europe + China, not only US).
"""
import json, time, sys, urllib.parse, urllib.request, re

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

# target -> list of queries. Each query is an Europe PMC query string.
TARGETS = {
    "foundational_platform": [
        'TITLE:"bispecific antibody" AND TITLE:("T cell" OR "T-cell") AND PUB_YEAR:[1980 TO 2010]',
        '("hetero-crosslinked" OR "heteroconjugate") AND "cytotoxic T" AND target',
        'TITLE:("BiTE" OR "bispecific T-cell engager" OR "T-cell engager") AND (mechanism OR platform OR review)',
        '"trifunctional antibody" AND "T cell"',
        'TITLE:"tandem diabody" AND "T cell"',
        '("DART" OR "dual-affinity re-targeting") AND "T cell" AND CD3',
        'TITLE:("T-cell engager" OR "T cell engager") AND (design OR format OR engineering OR half-life)',
    ],
    "CD19": [
        'blinatumomab AND (preclinical OR mechanism OR "phase 1" OR relapsed)',
        'TITLE:("CD19" AND ("bispecific" OR "T-cell engager" OR "BiTE"))',
    ],
    "CD20": [
        '(glofitamab OR mosunetuzumab OR epcoritamab OR odronextamab OR plamotamab) AND lymphoma',
        'TITLE:("CD20" AND ("bispecific" OR "T-cell engager"))',
    ],
    "BCMA": [
        '(teclistamab OR elranatamab OR "AMG 420" OR pavurutamab OR "PF-06863135") AND myeloma',
        'TITLE:("BCMA" AND ("bispecific" OR "T-cell engager" OR "BiTE"))',
    ],
    "GPRC5D": [
        'talquetamab AND myeloma',
        'TITLE:("GPRC5D" AND ("bispecific" OR "T-cell engager"))',
    ],
    "CD33_FLT3_AML": [
        'TITLE:("CD33" OR "FLT3" OR "CD123") AND ("T-cell engager" OR "bispecific") AND (AML OR leukemia OR leukaemia)',
        '(flotetuzumab OR vibecotamab OR "AMG 330" OR "AMG 673") AND leukemia',
    ],
    "EpCAM": [
        'catumaxomab AND (EpCAM OR ascites OR "malignant ascites")',
        'TITLE:("EpCAM" AND ("bispecific" OR "T-cell engager" OR trifunctional"))',
        '"solitomab" OR "MT110" OR "AMG 110"',
    ],
    "CEA_CEACAM5": [
        '(cibisatamab OR "CEA-TCB" OR "RO6958688") AND (CEA OR colorectal OR solid)',
        'TITLE:("CEA" OR "CEACAM5") AND ("bispecific" OR "T-cell engager")',
    ],
    "gp100_ImmTAC": [
        'tebentafusp AND (gp100 OR uveal OR melanoma)',
        'ImmTAC AND ("T cell" OR melanoma OR gp100)',
    ],
    "PSMA": [
        '(pasotuxizumab OR "AMG 212" OR "BAY2010112" OR "HPN424" OR "CCW702" OR "REGN5678") AND prostate',
        'TITLE:("PSMA" AND ("bispecific" OR "T-cell engager" OR "BiTE"))',
    ],
    "HER2_ERBB2": [
        'TITLE:("HER2" OR "ERBB2") AND ("bispecific" OR "T-cell engager" OR "BiTE")',
        '(zanidatamab OR "ertumaxomab" OR "runimotamab") AND (T cell OR bispecific)',
    ],
    "EGFR_EGFRvIII": [
        'TITLE:("EGFR" OR "EGFRvIII") AND ("bispecific" OR "T-cell engager" OR "BiTE")',
        'EGFRvIII AND "T-cell engager" AND (glioma OR glioblastoma)',
    ],
    "DLL3": [
        '(tarlatamab OR "AMG 757" OR "BI 764532" OR obrixtamine OR "HPN328") AND (DLL3 OR "small cell" OR neuroendocrine)',
        'TITLE:("DLL3" AND ("bispecific" OR "T-cell engager"))',
    ],
    "B7H3_CD276": [
        'TITLE:("B7-H3" OR "B7H3" OR "CD276") AND ("bispecific" OR "T-cell engager")',
        '("HPN536" OR "vudalimab") AND ("T cell" OR B7-H3)',
    ],
    "GD2": [
        'TITLE:("GD2") AND ("bispecific" OR "T-cell engager" OR "BiTE")',
        'GD2 AND "bispecific antibody" AND (neuroblastoma OR "T cell")',
    ],
    "Claudin18_2": [
        'TITLE:("claudin 18.2" OR "CLDN18.2" OR "claudin-18.2") AND ("bispecific" OR "T-cell engager")',
        '(givastomig OR "ASKB589" OR "Q-1802" OR "AMG 910") AND (claudin OR gastric)',
    ],
    "Mesothelin_MUC_PSCA": [
        'TITLE:("mesothelin" OR "MUC16" OR "MUC1" OR "PSCA") AND ("bispecific" OR "T-cell engager")',
        '(REGN5668 OR "HPN536" OR "AMG 199") AND (mesothelin OR MUC16)',
    ],
    "solid_tumor_other": [
        'TITLE:("FAP" OR "EGFRvIII" OR "ROR1" OR "5T4" OR "CD70") AND ("T-cell engager" OR "bispecific")',
        'TITLE:("T-cell engager" OR "BiTE") AND (glioma OR glioblastoma OR "brain tumor")',
    ],
    "cart_tce_combination": [
        '"CAR-T" AND ("secreting" OR "secrete") AND ("BiTE" OR "bispecific T-cell engager" OR "T-cell engager")',
        '("CAR T" OR "CAR-T") AND "T-cell engager" AND (combination OR combine OR armored OR "dual targeting")',
        '"STAb-T" OR ("secreting T-cell" AND bispecific)',
        'TITLE:("BiTE" OR "T-cell engager") AND ("CAR" AND ("secreting" OR combination))',
    ],
}

def epmc_search(query, page_size=60):
    params = {
        "query": query + " AND (SRC:MED OR SRC:PMC OR SRC:PPR)",
        "format": "json",
        "pageSize": str(page_size),
        "resultType": "core",
    }
    url = EPMC + "?" + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            sys.stderr.write(f"retry {attempt} for {query[:40]}: {e}\n")
            time.sleep(2)
    return {"resultList": {"result": []}}

def affil_geo(rec):
    """Best-effort geography from author affiliations / journal."""
    text = json.dumps(rec).lower()
    geos = []
    china = ["china", "chinese", "shanghai", "beijing", "guangzhou", "zhejiang",
             "sichuan", "nanjing", "wuhan", "hangzhou", "suzhou", "chengdu"]
    eu = ["germany", "münchen", "munich", "united kingdom", "england", "oxford",
          "london", "france", "paris", "italy", "spain", "madrid", "barcelona",
          "netherlands", "switzerland", "basel", "sweden", "denmark", "austria",
          "belgium", "norway", "heidelberg", "würzburg", "wurzburg"]
    us = ["usa", "united states", ", ny", ", ca", "boston", "houston",
          "bethesda", "seattle", "philadelphia", "new york", "california",
          "texas", "maryland", "massachusetts"]
    if any(k in text for k in china): geos.append("China")
    if any(k in text for k in eu): geos.append("Europe")
    if any(k in text for k in us): geos.append("US")
    return "|".join(geos) if geos else ""

def main():
    seen = {}
    for target, queries in TARGETS.items():
        for q in queries:
            data = epmc_search(q)
            results = data.get("resultList", {}).get("result", [])
            for rec in results:
                pmid = rec.get("pmid") or rec.get("id")
                key = pmid
                if not key:
                    continue
                if key in seen:
                    # keep first target assignment but note additional
                    seen[key]["also_targets"].add(target)
                    continue
                seen[key] = {
                    "target": target,
                    "also_targets": set(),
                    "pmid": rec.get("pmid", ""),
                    "pmcid": rec.get("pmcid", ""),
                    "doi": rec.get("doi", ""),
                    "title": (rec.get("title", "") or "").rstrip("."),
                    "authors": rec.get("authorString", ""),
                    "venue": (rec.get("journalInfo", {}).get("journal", {}).get("title", "")
                              or rec.get("journalTitle", "")
                              or rec.get("bookOrReportDetails", {}).get("publisher", "")),
                    "year": rec.get("pubYear", ""),
                    "isOA": rec.get("isOpenAccess", "N"),
                    "inEPMC": rec.get("inEPMC", "N"),
                    "hasPDF": rec.get("hasPDF", "N"),
                    "pubType": rec.get("pubTypeList", {}).get("pubType", []),
                    "geo": affil_geo(rec),
                    "src": rec.get("source", ""),
                }
            time.sleep(0.34)
            sys.stderr.write(f"{target}: '{q[:50]}' -> {len(results)}\n")
    # serialize
    out = []
    for k, v in seen.items():
        v["also_targets"] = "|".join(sorted(v["also_targets"]))
        v["pubType"] = "|".join(v["pubType"]) if isinstance(v["pubType"], list) else str(v["pubType"])
        out.append(v)
    with open("/home/ubuntu/repos/lit-syn/papers/t-cell-engagers/raw_harvest.json", "w") as f:
        json.dump(out, f, indent=1)
    print(f"total unique records: {len(out)}")

if __name__ == "__main__":
    main()
