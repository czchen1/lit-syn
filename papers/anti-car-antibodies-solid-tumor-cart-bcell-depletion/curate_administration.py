#!/usr/bin/env python3
"""Fetch metadata + abstracts for the administration-level records selected by hand
from raw_harvest_administration.json and the targeted follow-up searches.

Writes curated_administration.json (metadata for index.tsv rows) and prints the
abstracts so the numbers quoted in notes/administration_protocol.md can be checked
against source.
"""
import json
import time
import urllib.parse
import urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
BASE = ("/home/ubuntu/repos/lit-syn/papers/"
        "anti-car-antibodies-solid-tumor-cart-bcell-depletion")

# category -> PMIDs. Categories extend the existing index.tsv scheme.
SELECTED = {
    "J_admin_premedication_infusion_reactions": [
        "20350882",   # infusion reactions: diagnosis, assessment, management
        "38452439",   # management of infusion-related reactions in cancer therapy
        "31447561",   # early identification of IRR to mAbs
        "19220420",   # rapid infusion of rituximab over 60 min
        "17244675",   # rapid infusion rituximab with steroid-containing chemo
        "16856919",   # rapid infusion rituximab +/- steroid, single institution
        "42530421",   # H1 vs H1/H2 antagonist premedication, rituximab IRR
        "41789935",   # reevaluating corticosteroid premedication for rituximab
        "41572843",   # oral glucocorticoid premedication, rituximab in RA
        "37205922",   # prednisone premedication protocol reduces rituximab IRR
        "41989666",   # bepotastine vs hydroxyzine for rituximab IRR
        "38270799",   # steroid premedication and mAb therapy: reconsider?
        "42279029",   # rituximab hypersensitivity desensitization protocols
        "42073020",   # severe reactions to rituximab in children (serum sickness, anaphylaxis)
        "41937341",   # EAACI task force: hypersensitivity to biologicals in children
    ],
    "K_admin_screening_prophylaxis": [
        "32716741",   # ASCO PCO 2020: HBV screening/management before cancer therapy
        "25964247",   # ASCO PCO 2015: HBV screening
        "23775967",   # RCT entecavir prophylaxis for rituximab-associated HBV reactivation
        "19075267",   # HBV reactivation in resolved HBV treated with rituximab-chemo
        "28219691",   # HBV reactivation with immunosuppressive/biologic therapy
        "30646343",   # immunoglobulin levels, infectious risk, mortality with rituximab
        "23276889",   # incidence of hypogammaglobulinaemia with rituximab, IVIG use
        "36706910",   # hypogammaglobulinaemia, late-onset neutropenia, infections after rituximab
        "34757064",   # hypogammaglobulinaemia after CAR-T: characteristics/management
        "31416717",   # IgG replacement in CAR-T recipients
        "20827108",   # late-onset neutropenia after rituximab: case series + review
        "21560117",   # late-onset neutropenia, B-cell depletion, infection
        "19264918",   # PML after rituximab in HIV-negative patients (57 cases)
        "21561350",   # tumour lysis syndrome review
        "38498792",   # ASCO guideline: vaccination of adults with cancer
        "32727835",   # VELOCE: vaccine responses on anti-CD20
        "34514436",   # humoral/cellular vaccine responses after CD20 depletion
        "33914708",   # antibodies against vaccine-preventable infections after CAR-T
        "42274870",   # infectious complications after CAR-T: prevention
        "34923107",   # EBMT/EHA/JACIE 2021 best practice recommendations, CAR-T
        "31753925",   # EBMT/JACIE 2020 best practice recommendations, CAR-T
    ],
    "L_admin_dose_route_pk": [
        "9310469",    # IDEC-C2B8 pivotal: 375 mg/m2 weekly x4
        "28653357",   # pharmacokinetics of monoclonal antibodies
        "36420256",   # rituximab PK/PD alterations in glomerulopathies (proteinuria, clearance)
        "24002601",   # subcutaneous rituximab with hyaluronidase
        "30744432",   # ENHANZE hyaluronidase SC delivery
        "29500555",   # switching reference medicines to biosimilars
        "42340364",   # prevalence of anti-rituximab antibodies
        "42481732",   # anti-rituximab antibodies and efficacy in children
        "40282439",   # intra-CSF drug delivery in CNS malignancies
        "42211720",   # CD20+ CNS lymphoma despite peripheral B-cell depletion (CSF sanctuary)
    ],
    "M_admin_cart_context": [
        "40148484",   # lymphodepletion chemotherapy in CAR-T (review)
        "38191740",   # CAR-T and fludarabine: precision dosing
        "41471106",   # population PK fludarabine model in CAR-T
        "40609087",   # age-adjusted fludarabine dosing simulation
        "30592986",   # ASTCT consensus grading CRS/ICANS
        "41798119",   # TIAN in children with DIPG receiving ICV B7-H3 CAR-T
        "41895715",   # locoregional CAR-T delivery in high-grade glioma: safety systematic analysis
        "36259971",   # intraventricular B7-H3 CAR-T for DIPG
        "38480922",   # intrathecal bivalent CART-EGFR-IL13Ra2 in recurrent GBM
        "32341580",   # locoregional CAR-T to CSF, medulloblastoma/ependymoma
    ],
    "N_admin_fasting_procedure": [
        "36629465",   # ASA 2023 preoperative fasting guidelines (carbohydrate, chewing gum, peds)
        "28045707",   # ASA 2017 practice guidelines for preoperative fasting
        "34857683",   # ESAIC 2022 pre-operative fasting in children
        "21712716",   # ESA 2011 perioperative fasting in adults and children
    ],
}


def fetch(pmid):
    params = urllib.parse.urlencode({
        "query": f"EXT_ID:{pmid}",
        "format": "json",
        "resultType": "core",
        "pageSize": 1,
    })
    req = urllib.request.Request(f"{EPMC}?{params}",
                                 headers={"User-Agent": "lit-syn/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    res = data.get("resultList", {}).get("result", [])
    return res[0] if res else None


def main():
    out = []
    for cat, pmids in SELECTED.items():
        for pmid in pmids:
            try:
                r = fetch(pmid)
            except Exception as exc:
                print(f"FAIL {pmid}: {exc}")
                continue
            if not r:
                print(f"MISSING {pmid}")
                continue
            rec = {
                "category": cat,
                "pmid": r.get("pmid", ""),
                "pmcid": r.get("pmcid", ""),
                "doi": r.get("doi", ""),
                "title": r.get("title", "").rstrip("."),
                "authors": r.get("authorString", ""),
                "journal": (r.get("journalInfo", {}) or {})
                           .get("journal", {}).get("title", ""),
                "year": r.get("pubYear", ""),
                "isOpenAccess": r.get("isOpenAccess", ""),
                "abstract": r.get("abstractText", "") or "",
            }
            out.append(rec)
            print("=" * 100)
            print(cat, rec["pmid"], rec["year"], rec["journal"])
            print(rec["title"])
            print(rec["abstract"][:2200])
            time.sleep(0.34)
    with open(f"{BASE}/curated_administration.json", "w") as f:
        json.dump(out, f, indent=1)
    print("\nrecords:", len(out))


if __name__ == "__main__":
    main()
