#!/usr/bin/env python3
"""Harvest EZH2 (and dual EZH1/2) inhibitor literature from Europe PMC.

Organized by inhibitor (clinical-stage agents first, then tool/preclinical
compounds), plus cross-cutting buckets for CNS/BBB penetration, resistance/
mechanism, and combinations. Emphasis, per request, on preclinical + clinical
work with extractable potency, brain/BBB-penetrance, and efficacy data.
"""
import json, time, sys, urllib.parse, urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

# bucket -> list of Europe PMC query strings.
TARGETS = {
    # ---- clinical-stage EZH2 / EZH1-2 inhibitors ----
    "tazemetostat": [
        '(tazemetostat OR "EPZ-6438" OR "EPZ6438" OR "E7438") AND (EZH2 OR lymphoma OR sarcoma OR SMARCB1)',
        'TITLE:(tazemetostat OR "EPZ-6438")',
    ],
    "valemetostat": [
        '(valemetostat OR "DS-3201" OR "DS-3201b" OR ezharmia) AND (EZH1 OR EZH2 OR lymphoma OR "adult T-cell")',
        'TITLE:(valemetostat OR "DS-3201")',
    ],
    "tulmimetostat_CPI0209": [
        '(tulmimetostat OR "CPI-0209" OR "CPI0209") AND (EZH2 OR EZH1 OR tumor OR tumour)',
        '("CPI-1205" OR CPI1205 OR lirametostat) AND EZH2',
    ],
    "mevrometostat_PF06821497": [
        '("PF-06821497" OR "PF06821497" OR mevrometostat) AND (EZH2 OR prostate OR SCLC)',
    ],
    "SHR2554": [
        '("SHR2554" OR "SHR-2554") AND (EZH2 OR lymphoma)',
    ],
    "GSK126_GSK343": [
        '("GSK126" OR "GSK2816126" OR "GSK-126") AND EZH2',
        '("GSK343" OR "GSK503" OR "GSK926") AND EZH2',
    ],
    # ---- tool / early preclinical compounds ----
    "EPZ005687_EI1_EPZ011989": [
        '("EPZ005687" OR "EPZ-005687") AND EZH2',
        '("EI1" AND EZH2 AND (inhibitor OR lymphoma))',
        '("EPZ011989" OR "EPZ-011989") AND EZH2',
    ],
    "UNC1999_EED226": [
        '("UNC1999" OR "UNC2400") AND (EZH2 OR EZH1)',
        '("EED226" OR "EED-226" OR "MAK683" OR "A-395") AND (EED OR PRC2 OR EZH2)',
    ],
    "DZNep": [
        '("DZNep" OR "3-deazaneplanocin" OR deazaneplanocin) AND (EZH2 OR PRC2 OR methyltransferase)',
    ],
    # ---- cross-cutting themes ----
    "cns_bbb_glioma": [
        '(EZH2 AND (inhibitor OR tazemetostat OR EPZ-6438 OR GSK126 OR valemetostat)) AND (glioma OR glioblastoma OR DIPG OR "diffuse midline" OR H3K27M OR ATRT OR "rhabdoid" OR medulloblastoma)',
        '(EZH2 AND inhibitor) AND ("blood-brain barrier" OR "brain penetrant" OR "brain-penetrant" OR "CNS penetration" OR intracranial)',
    ],
    "resistance_mechanism_sar": [
        '(EZH2 AND inhibitor) AND (resistance OR "secondary mutation" OR Y641 OR A677 OR A687 OR "gain-of-function")',
        '(EZH2 AND (inhibitor OR "small molecule")) AND (selectivity OR "SAM-competitive" OR potency OR "structure-activity" OR crystal)',
        '(EZH2 AND (degrader OR PROTAC OR "dual inhibitor")) AND (EZH2 OR PRC2)',
    ],
    "combination_clinical": [
        '(EZH2 AND inhibitor) AND (combination OR combined OR synergy OR synergistic) AND (BRD4 OR "BET" OR PARP OR "immune checkpoint" OR PD-1 OR androgen OR enzalutamide)',
        '(tazemetostat OR valemetostat OR EZH2) AND ("phase 1" OR "phase 2" OR "phase I" OR "phase II" OR "clinical trial" OR "objective response")',
    ],
}


def epmc_search(query, page_size=90):
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


def main():
    seen = {}
    for target, queries in TARGETS.items():
        for q in queries:
            data = epmc_search(q)
            results = data.get("resultList", {}).get("result", [])
            for rec in results:
                pmid = rec.get("pmid") or rec.get("id")
                if not pmid:
                    continue
                if pmid in seen:
                    seen[pmid]["also_targets"].add(target)
                    continue
                seen[pmid] = {
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
                    "src": rec.get("source", ""),
                }
            time.sleep(0.34)
            sys.stderr.write(f"{target}: '{q[:50]}' -> {len(results)}\n")
    out = []
    for k, v in seen.items():
        v["also_targets"] = "|".join(sorted(v["also_targets"]))
        v["pubType"] = "|".join(v["pubType"]) if isinstance(v["pubType"], list) else str(v["pubType"])
        out.append(v)
    with open("/home/ubuntu/repos/lit-syn/papers/ezh2-inhibitors/raw_harvest.json", "w") as f:
        json.dump(out, f, indent=1)
    print(f"total unique records: {len(out)}")


if __name__ == "__main__":
    main()
