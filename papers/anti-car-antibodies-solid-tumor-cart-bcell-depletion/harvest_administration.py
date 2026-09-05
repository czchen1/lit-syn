#!/usr/bin/env python3
"""Harvest administration-level evidence for giving rituximab around CAR-T.

Follow-up question to REPORT.md: given the two rituximab-containing solid-tumour
CAR-T regimens (NCT04196413 Arm D, NCT06973096 Cohort B), how is the drug
actually given -- premedication, infusion rate, monitoring, screening,
prophylaxis, fasting/NPO, and interaction with lymphodepletion and the CAR-T
product itself.

Europe PMC REST search, no API key. Records serialised to
raw_harvest_administration.json for manual curation into
notes/administration_protocol.md and index.tsv.
"""
import json
import time
import urllib.parse
import urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
OUT = ("/home/ubuntu/repos/lit-syn/papers/"
       "anti-car-antibodies-solid-tumor-cart-bcell-depletion/"
       "raw_harvest_administration.json")

RITUX = '("rituximab" OR "anti-CD20" OR "CD20 monoclonal antibody")'
CART = '("CAR T" OR "CAR-T" OR "chimeric antigen receptor")'

QUERIES = {
    "premedication_infusion_reactions": [
        f'{RITUX} AND ("infusion-related reaction" OR "infusion reaction") AND '
        '(premedication OR antihistamine OR acetaminophen OR paracetamol OR '
        'corticosteroid OR management)',
        f'{RITUX} AND ("infusion related reactions") AND (incidence OR risk factors OR grading)',
        f'{RITUX} AND ("rapid infusion" OR "90-minute infusion" OR "shortened infusion" OR '
        '"accelerated infusion") AND (safety OR feasibility)',
        f'{RITUX} AND ("cytokine release syndrome" OR "cytokine release") AND '
        '("first infusion" OR "infusion reaction")',
        f'{RITUX} AND "serum sickness"',
        f'{RITUX} AND (anaphylaxis OR "IgE" OR "hypersensitivity") AND (retreatment OR "repeat dosing")',
        f'{RITUX} AND ("anti-rituximab antibodies" OR "antidrug antibodies" OR "HACA")',
    ],
    "pediatric_administration": [
        f'{RITUX} AND (pediatric OR paediatric OR children) AND '
        '("infusion reaction" OR premedication OR "infusion rate" OR administration)',
        f'{RITUX} AND (pediatric OR paediatric) AND (pharmacokinetics OR clearance OR "body surface area")',
        f'{RITUX} AND (pediatric OR paediatric) AND (hypogammaglobulinemia OR '
        '"immunoglobulin replacement" OR infection)',
    ],
    "screening_and_prophylaxis": [
        f'{RITUX} AND "hepatitis B" AND (reactivation OR prophylaxis OR entecavir OR '
        'lamivudine OR tenofovir OR screening)',
        f'{RITUX} AND ("Pneumocystis" OR "PJP" OR "PCP prophylaxis" OR '
        'trimethoprim-sulfamethoxazole OR cotrimoxazole)',
        f'{RITUX} AND (hypogammaglobulinemia OR hypogammaglobulinaemia) AND '
        '("immunoglobulin replacement" OR IVIG OR "IgG trough")',
        f'{RITUX} AND (vaccination OR immunisation OR immunization) AND '
        '(timing OR response OR "live vaccine")',
        f'{RITUX} AND ("late-onset neutropenia" OR "late onset neutropenia" OR '
        '"delayed neutropenia")',
        f'{RITUX} AND ("tumor lysis syndrome" OR "tumour lysis syndrome") AND '
        '(prophylaxis OR hydration OR rasburicase OR allopurinol)',
        f'{RITUX} AND ("progressive multifocal leukoencephalopathy" OR PML) AND risk',
        f'{RITUX} AND ("hepatitis C" OR HIV OR tuberculosis) AND (screening OR reactivation)',
    ],
    "cns_and_route": [
        f'{RITUX} AND ("cerebrospinal fluid" OR "CSF concentration" OR "CNS penetration")',
        f'{RITUX} AND ("intrathecal" OR "intraventricular" OR "intra-CSF") AND (lymphoma OR CNS)',
        f'{RITUX} AND ("subcutaneous" OR "hyaluronidase") AND (pharmacokinetics OR "non-inferior")',
        f'{RITUX} AND (biosimilar OR "CT-P10" OR "GP2013" OR interchangeability)',
    ],
    "dose_depth_duration": [
        f'{RITUX} AND ("B-cell depletion" OR "B cell depletion") AND '
        '("dose" OR "dose-response") AND (duration OR repopulation OR reconstitution)',
        f'{RITUX} AND ("500 mg/m2" OR "750 mg/m2" OR "high-dose rituximab") AND '
        '(pharmacokinetics OR safety OR "dose escalation")',
        f'{RITUX} AND (pharmacokinetics OR exposure) AND ("tumor burden" OR "target-mediated")',
    ],
    "cart_context": [
        f'{CART} AND (corticosteroid OR dexamethasone OR glucocorticoid) AND '
        '(expansion OR persistence OR efficacy OR outcome)',
        f'{CART} AND ("lymphodepletion" OR "lymphodepleting") AND '
        '(fludarabine AND cyclophosphamide) AND (dose OR schedule OR administration)',
        f'{CART} AND (rituximab) AND ("late cytopenia" OR "prolonged cytopenia" OR '
        '"immune reconstitution" OR infection)',
        f'{CART} AND ("intracerebroventricular" OR "Ommaya" OR "intraventricular") AND '
        '(anesthesia OR sedation OR procedure OR administration)',
        f'{CART} AND ("infection prophylaxis" OR "antimicrobial prophylaxis" OR '
        '"immunoglobulin replacement") AND (guideline OR consensus OR recommendation)',
    ],
    "fasting_npo_sedation": [
        '("preoperative fasting" OR "fasting guidelines" OR "nil per os" OR "NPO") AND '
        '(sedation OR anesthesia OR anaesthesia) AND (children OR pediatric OR guideline)',
        '("monoclonal antibody" OR chemotherapy) AND infusion AND (fasting OR "food intake" OR NPO)',
        '(fludarabine OR cyclophosphamide) AND (antiemetic OR emesis OR "fluid intake" OR hydration) AND '
        '(guideline OR prophylaxis)',
    ],
}


def search(query, page_size=50, pages=1):
    out = []
    cursor = "*"
    for _ in range(pages):
        params = urllib.parse.urlencode({
            "query": query,
            "format": "json",
            "pageSize": page_size,
            "cursorMark": cursor,
            "resultType": "core",
            "sort": "CITED desc",
        })
        req = urllib.request.Request(f"{EPMC}?{params}",
                                     headers={"User-Agent": "lit-syn/1.0"})
        with urllib.request.urlopen(req, timeout=90) as resp:
            data = json.load(resp)
        results = data.get("resultList", {}).get("result", [])
        out.extend(results)
        cursor = data.get("nextCursorMark")
        if not cursor or len(results) < page_size:
            break
        time.sleep(0.34)
    return out


def main():
    harvest = {}
    for group, queries in QUERIES.items():
        seen = {}
        for q in queries:
            try:
                res = search(q)
            except Exception as exc:
                print(f"FAILED {group}: {q[:60]}: {exc}")
                continue
            for r in res:
                key = r.get("pmid") or r.get("id")
                if key and key not in seen:
                    seen[key] = {
                        "pmid": r.get("pmid", ""),
                        "pmcid": r.get("pmcid", ""),
                        "doi": r.get("doi", ""),
                        "title": r.get("title", ""),
                        "authorString": r.get("authorString", ""),
                        "journal": (r.get("journalInfo", {}) or {})
                                   .get("journal", {}).get("title", ""),
                        "year": r.get("pubYear", ""),
                        "isOpenAccess": r.get("isOpenAccess", ""),
                        "citedByCount": r.get("citedByCount", 0),
                        "abstract": (r.get("abstractText", "") or "")[:1200],
                        "query_group": group,
                    }
            print(f"{group}: +{len(res)} -> {len(seen)} unique")
            time.sleep(0.34)
        harvest[group] = list(seen.values())
    with open(OUT, "w") as f:
        json.dump(harvest, f, indent=1)
    print("total unique:", sum(len(v) for v in harvest.values()))


if __name__ == "__main__":
    main()
