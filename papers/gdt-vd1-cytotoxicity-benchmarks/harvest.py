#!/usr/bin/env python3
"""Harvest literature that reports quantitative gamma-delta T cell product metrics.

Organising question: for an expanded gamma-delta T-cell product that is ~80% Vdelta1
and largely CD4-CD8- (double negative), how do the achieved purity, subset
composition and in vitro killing at a defined effector:target ratio (10:1) compare
with published products?

Query groups target the three axes that make published numbers comparable:
product/expansion protocol, phenotype (Vd1 vs Vd2, DN/CD4-CD8-, memory subsets),
and cytotoxicity readouts reported against explicit E:T ratios.

Europe PMC REST search; records serialized to raw_harvest.json for curate.py.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
OUT = "/home/ubuntu/repos/lit-syn/papers/gdt-vd1-cytotoxicity-benchmarks/raw_harvest.json"

GDT = ('("gamma delta T" OR "gammadelta T" OR "γδ T" OR "gd T cell" OR "TCRgd" OR '
       '"TCR gamma delta" OR "Vdelta1" OR "Vd1" OR "Vδ1" OR "Vgamma9Vdelta2" OR '
       '"Vg9Vd2" OR "Vγ9Vδ2" OR "Vdelta2" OR "delta one T")')
VD1 = ('("Vdelta1" OR "Vδ1" OR "Vd1 T" OR "delta one T" OR "DOT cell" OR "DOT cells" OR '
       '"Vdelta1 T cells" OR "TCRVdelta1")')
CYTOTOX = ('("effector to target" OR "effector:target" OR "E:T ratio" OR "E/T ratio" OR '
           '"cytotoxicity assay" OR "killing assay" OR "specific lysis" OR '
           '"chromium release" OR "calcein release" OR "luciferase-based cytotoxicity" OR '
           '"xCELLigence" OR "real-time cell analysis" OR "incucyte")')

QUERIES = {
    # ---------------- Vd1-selective products ----------------
    "vd1_products": [
        f'{VD1} AND (expansion OR expanded OR "cell product" OR manufacturing OR "clinical-grade" OR GMP)',
        f'{VD1} AND {CYTOTOX}',
        f'{VD1} AND (purity OR "percentage of" OR "fold expansion" OR phenotype OR immunophenotyp*)',
        '"delta one T" OR "DOT cells" OR "DOT-CAR" OR "Delta One T cells"',
        f'{VD1} AND (leukemia OR lymphoma OR myeloma OR "solid tumor" OR "solid tumour" OR glioma OR neuroblastoma)',
        f'{VD1} AND (allogeneic OR "off-the-shelf" OR "adoptive transfer" OR "adoptive cell therapy")',
    ],
    # ---------------- expansion / manufacturing protocols ----------------
    "expansion_protocols": [
        f'{GDT} AND (zoledronate OR zoledronic OR pamidronate OR "aminobisphosphonate" OR IPP OR "isopentenyl pyrophosphate" OR "bromohydrin pyrophosphate" OR BrHPP OR "phosphoantigen")',
        f'{GDT} AND (expansion OR expanded) AND ("IL-2" OR "IL-15" OR "IL-21" OR "IL-4" OR "IL-7" OR "artificial antigen presenting" OR "feeder cell" OR "K562" OR "TransAct" OR "OKT3" OR "anti-CD3")',
        f'{GDT} AND ("clinical-grade" OR GMP OR "good manufacturing practice" OR bioreactor OR "closed system" OR "large-scale expansion" OR "cell therapy manufacturing")',
        f'{GDT} AND ("cord blood" OR "umbilical cord" OR "hematopoietic progenitor" OR "in vitro differentiation" OR "induced pluripotent")',
        f'{GDT} AND (expansion) AND (purity OR "fold expansion" OR yield OR "cell dose")',
        f'{GDT} AND ("Vdelta1 expansion" OR "Vd1 expansion" OR "selective expansion" OR "TCR-delta1 depletion" OR "Vd2 depletion" OR "alphabeta depletion" OR "αβ depletion")',
    ],
    # ---------------- phenotype: Vd1 vs Vd2, DN, memory ----------------
    "phenotype_subsets": [
        f'{GDT} AND ("CD4-CD8-" OR "CD4- CD8-" OR "double negative" OR "double-negative" OR "CD4/CD8 double negative")',
        '"double negative T cells" AND (gamma delta OR gammadelta OR "TCR gamma" OR cytotoxicity OR "adoptive")',
        f'{GDT} AND ("CD27" OR "CD45RA" OR "naive" OR "central memory" OR "effector memory" OR "TEMRA" OR "CD62L" OR differentiation) AND (subset OR phenotype OR composition)',
        f'{GDT} AND ("NKG2D" OR "DNAM-1" OR "NKp30" OR "NKp44" OR "NKp46" OR "CD16" OR "granzyme" OR perforin OR "TRAIL" OR "Fas ligand") AND (expression OR phenotype)',
        f'{GDT} AND ("Vdelta1" OR "Vdelta2") AND (frequency OR proportion OR repertoire OR "peripheral blood" OR "tissue-resident" OR "tumor-infiltrating" OR "tumour-infiltrating")',
        f'{GDT} AND (exhaustion OR "PD-1" OR TIGIT OR "TIM-3" OR LAG-3 OR senescence) AND (phenotype OR function)',
    ],
    # ---------------- cytotoxicity at defined E:T ----------------
    "cytotoxicity_et": [
        f'{GDT} AND {CYTOTOX}',
        f'{GDT} AND ("10:1" OR "5:1" OR "1:1" OR "20:1" OR "2:1") AND (cytotoxicity OR lysis OR killing)',
        f'{GDT} AND (cytotoxicity OR "specific lysis" OR killing) AND ("cell line" OR "primary blasts" OR "patient-derived" OR organoid OR spheroid)',
        f'{GDT} AND (degranulation OR "CD107a" OR "IFN-gamma" OR "interferon gamma" OR "TNF-alpha" OR "cytokine production") AND (assay OR flow cytometry)',
        f'{GDT} AND (cytotoxicity) AND ("serial killing" OR "repeat stimulation" OR "stress test" OR "long-term killing" OR persistence)',
        f'{GDT} AND ("trogocytosis" OR "immune synapse" OR "killing kinetics" OR "time-lapse")',
    ],
    # ---------------- engineered gd T (CAR / TCR / engagers) ----------------
    "engineered_gdt": [
        f'{GDT} AND ("CAR" OR "chimeric antigen receptor") AND (cytotoxicity OR efficacy OR "E:T")',
        f'"CD20 CAR" AND {VD1}',
        f'{GDT} AND ("bispecific" OR "T cell engager" OR "tribody" OR "immunoligand" OR "(HER2)2xVgamma9")',
        f'{GDT} AND ("TCR-engineered" OR "TEG" OR "T cells engineered to express a gamma delta TCR")',
        '"ADI-001" OR "ADI 001" OR "GDX012" OR "TCB008" OR "INB-100" OR "LAVA-051" OR "LAVA-1207"',
    ],
    # ---------------- clinical translation ----------------
    "clinical": [
        f'{GDT} AND ("clinical trial" OR "phase 1" OR "phase I" OR "first-in-human" OR "adoptive transfer") AND (patients OR safety OR response)',
        f'{GDT} AND ("haploidentical" OR "stem cell transplant" OR "donor lymphocyte" OR "graft" OR "immune reconstitution") AND (outcome OR relapse OR survival)',
        f'{VD1} AND (patients OR clinical OR trial)',
        f'{GDT} AND ("cell dose" OR "dose escalation" OR "product characteristics" OR "release criteria" OR "certificate of analysis")',
    ],
    # ---------------- comparators / benchmarking methodology ----------------
    "comparators_methods": [
        f'{GDT} AND ("compared with" OR versus) AND ("NK cells" OR "alphabeta T cells" OR "CAR-T" OR "CIK cells") AND (cytotoxicity OR killing)',
        '("cytotoxicity assay" OR "killing assay") AND (standardization OR standardisation OR comparison OR variability OR "assay format") AND ("NK cell" OR "T cell")',
        f'{GDT} AND (review OR "systematic review") AND (cytotoxicity OR "adoptive" OR "cell therapy")',
        f'{GDT} AND ("flow cytometry" OR "gating strategy") AND (identification OR quantification OR panel)',
    ],
}

PAGE = 100
MAX_PAGES = 6


def epmc_search(query, page_size=PAGE, max_pages=MAX_PAGES):
    out = []
    cursor = "*"
    for _ in range(max_pages):
        params = urllib.parse.urlencode({
            "query": query, "format": "json", "pageSize": page_size,
            "resultType": "core", "cursorMark": cursor,
        })
        url = f"{EPMC}?{params}"
        data = None
        for attempt in range(4):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "lit-syn/1.0"})
                with urllib.request.urlopen(req, timeout=90) as resp:
                    data = json.load(resp)
                break
            except Exception as exc:
                sys.stderr.write(f"  retry {attempt}: {exc}\n")
                time.sleep(3)
        if data is None:
            break
        results = data.get("resultList", {}).get("result", [])
        out.extend(results)
        nxt = data.get("nextCursorMark")
        if not results or not nxt or nxt == cursor:
            break
        cursor = nxt
        time.sleep(0.34)
    return out


def clean(text):
    if not text:
        return ""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text)).strip()


def main():
    seen = {}
    for domain, queries in QUERIES.items():
        for q in queries:
            results = epmc_search(q)
            for rec in results:
                key = rec.get("pmid") or rec.get("doi") or rec.get("id")
                if not key:
                    continue
                if key in seen:
                    seen[key]["also_domains"].add(domain)
                    continue
                seen[key] = {
                    "domain": domain,
                    "also_domains": set(),
                    "pmid": rec.get("pmid", ""),
                    "pmcid": rec.get("pmcid", ""),
                    "doi": rec.get("doi", ""),
                    "title": clean(rec.get("title", "")).rstrip("."),
                    "abstract": clean(rec.get("abstractText", "")),
                    "authors": rec.get("authorString", ""),
                    "venue": (rec.get("journalInfo", {}).get("journal", {}).get("title", "")
                              or rec.get("journalTitle", "")
                              or rec.get("bookOrReportDetails", {}).get("publisher", "")),
                    "year": rec.get("pubYear", ""),
                    "isOA": rec.get("isOpenAccess", "N"),
                    "inEPMC": rec.get("inEPMC", "N"),
                    "hasPDF": rec.get("hasPDF", "N"),
                    "pubType": rec.get("pubTypeList", {}).get("pubType", []),
                    "src": rec.get("source", ""),
                }
            sys.stderr.write(f"{domain}: '{q[:70]}' -> {len(results)}\n")
            time.sleep(0.34)

    out = []
    for v in seen.values():
        v["also_domains"] = "|".join(sorted(v["also_domains"]))
        v["pubType"] = "|".join(v["pubType"]) if isinstance(v["pubType"], list) else str(v["pubType"])
        out.append(v)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1)
    print(f"total unique records: {len(out)}")


if __name__ == "__main__":
    main()
