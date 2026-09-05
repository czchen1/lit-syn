#!/usr/bin/env python3
"""Append the administration-level records (categories J-N) to index.tsv and
fetch PMC open-access full text for them, matching the conventions used for
categories A-I.

Input: curated_administration.json (written by curate_administration.py).
"""
import json
import os
import re
import time
import urllib.error
import urllib.request

BASE = ("/home/ubuntu/repos/lit-syn/papers/"
        "anti-car-antibodies-solid-tumor-cart-bcell-depletion")
OA = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"

# One-line relevance note per record, written by hand.
NOTES = {
    "20350882": "nursing review: allergic (IgE) vs cytokine-release infusion reactions differ in mechanism but not presentation; risk assessment, grading, rechallenge",
    "38452439": "ESMO Open 2024 practical standard for preventing, recognising and managing infusion-related reactions to anticancer agents",
    "31447561": "review of IRR to monoclonal antibodies: premedication, rate reduction, interruption, desensitisation",
    "19220420": "60-min rituximab infusion, 105 infusions in 54 patients, no significant reactions (2nd and later doses only)",
    "17244675": "90-min rapid rituximab (20% over 30 min, 80% over 60 min) in 206 patients, no grade 3-4 IRR; basis of most rapid-infusion protocols",
    "16856919": "319 rapid rituximab infusions with and without steroids, no grade 3-4 events; rapid infusion safe without steroid premedication",
    "42530421": "retrospective cohort n=299: adding an H2 antagonist to acetaminophen + steroid + H1 did not reduce IRR incidence or severity; most IRR at 30-60 min",
    "41789935": "retrospective cohort reevaluating whether corticosteroid premedication for rituximab is necessary",
    "41572843": "2253 infusions: oral prednisolone 50 mg equivalent to IV methylprednisolone 50 mg for IRR prevention; IRR mostly mild",
    "37205922": "randomised: prednisone pretreatment cut rituximab IRR 43.2% to 15.9% in DLBCL, no difference in response or survival",
    "41989666": "randomised phase II, bepotastine vs hydroxyzine premedication; grade >=2 IRR 32% vs 52%, less drowsiness with 2nd-generation H1RA",
    "38270799": "corticosteroids inhibit ADCC; argues for steroid premedication at first dose only for ADCC-dependent mAbs - relevant to CAR-T where steroids also blunt T cells",
    "42279029": "46 desensitisation procedures in 11 patients with rituximab hypersensitivity, no anaphylaxis; allows continued dosing",
    "42073020": "1534 rituximab infusions in 391 children: 7 serum sickness, 7 anaphylaxis; anaphylaxis rechallengeable by desensitisation, serum sickness is not",
    "41937341": "EAACI task force practical approach to immediate and delayed hypersensitivity to biologicals in children",
    "32716741": "ASCO PCO 2020: test HBsAg, anti-HBc, anti-HBs before systemic therapy; past HBV + anti-CD20 = high reactivation risk, antivirals during and >=12 months after",
    "25964247": "ASCO PCO 2015: screen HBsAg and anti-HBc before anti-CD20 therapy or HCT",
    "23775967": "RCT n=80 resolved HBV: entecavir prophylaxis cut rituximab-associated reactivation 17.9% to 2.4%; undetectable baseline HBV DNA is not protective",
    "19075267": "R-CHOP in HBsAg-negative/anti-HBc-positive DLBCL: 25% HBV reactivation vs 0% with CHOP alone, one hepatic death",
    "28219691": "mechanisms, risk stratification and management of HBV reactivation with immunosuppressive and biologic therapy",
    "30646343": "cohort n=4479: 85% had no pre-rituximab immunoglobulin measurement; severe infections rose 17.2% to 21.7%; supports baseline and serial IgG",
    "23276889": "39% of patients developed low IgG after rituximab, 6.6% symptomatic needing IVIG; risk higher with maintenance dosing",
    "36706910": "review of hypogammaglobulinaemia and late-onset neutropenia after rituximab; recommends baseline and periodic IgG plus B-cell flow cytometry",
    "34757064": "hypogammaglobulinaemia after CAR-T: onset, duration, recovery and immunoglobulin replacement thresholds; children differ from adults",
    "31416717": "IgG replacement in CAR-T recipients - thresholds extrapolated from primary immunodeficiency, no CAR-T-specific evidence",
    "20827108": "late-onset neutropenia after rituximab: incidence 3-27%, median onset 77 days (range 42-153), often with infection",
    "21560117": "late-onset neutropenia in 11/209 rheumatic patients, median onset 102 days, coincided with B-cell depletion; 7 hospitalised with infection",
    "19264918": "57 rituximab-associated PML cases, median 5.5 months after last dose, 90% case-fatality",
    "21561350": "NEJM review of tumour lysis syndrome: risk stratification, hydration, urate-lowering therapy",
    "38498792": "ASCO 2024 vaccination guideline: revaccination after CAR-T or B-cell-depleting therapy, no live vaccines while depleted",
    "32727835": "VELOCE: anti-CD20 blunts tetanus, pneumococcal and neoantigen (KLH) responses - vaccinate before depletion where possible",
    "34514436": "RituxiVac: attenuated humoral (and partly cellular) mRNA vaccine response after anti-CD20; response tracks time since last dose and B-cell count",
    "33914708": "90% of CAR-T recipients off IGRT were hypogammaglobulinaemic; seroprotection lost for specific pathogens",
    "42274870": "2026 review of infection prevention after CAR-T: antiviral and PJP prophylaxis, risk-adapted antibacterial/antifungal cover, IgG replacement, vaccination timing",
    "34923107": "EBMT/EHA/JACIE 2021 best-practice recommendations covering lymphodepletion, infusion, CRS/ICANS, prophylaxis and long-term follow-up",
    "31753925": "EBMT/JACIE 2020 best-practice recommendations for CAR-T care pathway including screening labs and antibiotic prophylaxis",
    "9310469": "pivotal phase II establishing rituximab 375 mg/m2 weekly x4; infusional reactions concentrated in the first infusion, B-cell recovery from 6 months",
    "28653357": "tutorial on monoclonal antibody pharmacokinetics: target-mediated disposition, FcRn recycling, sources of variability",
    "36420256": "rituximab PK/PD across glomerulopathies: proteinuria and anti-drug antibodies raise clearance and shorten depletion; therapeutic drug monitoring options",
    "24002601": "subcutaneous rituximab 1400 mg with rHuPH20 comparable in PK and efficacy to IV, shorter administration",
    "30744432": "rHuPH20 (ENHANZE) technology underlying subcutaneous rituximab formulation",
    "29500555": "systematic review of switching reference biologics to biosimilars: no consistent immunogenicity or efficacy difference (relevant to rituximab biosimilar in NCT06973096)",
    "42340364": "anti-rituximab antibodies in 300 autoimmune patients: ADA appear as B cells reconstitute, titres and persistence differ by disease",
    "42481732": "48.5% of children with nephrotic syndrome developed anti-rituximab antibodies: lower rituximab levels, depletion 58.5 vs 163 days, more relapses",
    "40282439": "comparison of intracerebroventricular, lumbar intrathecal and cisterna magna delivery: ICV most consistent, headache/nausea/vomiting commonest procedural AEs",
    "42211720": "CD20+ CNS lymphoma arising despite peripheral B-cell depletion on rituximab - illustrates the CNS as a B-cell sanctuary",
    "40148484": "review of lymphodepletion in CAR-T: fludarabine + cyclophosphamide, dose intensity matters for expansion and persistence",
    "38191740": "argues for precision (exposure-guided) fludarabine dosing in CAR-T lymphodepletion",
    "41471106": "population PK model of fludarabine in CAR-T recipients; weight and eGFR drive clearance",
    "40609087": "clinical trial simulation: age-adjusted or TDM fludarabine dosing keeps far more children in the target AUC 13.8-25 mg*h/L",
    "30592986": "ASTCT consensus grading for CRS and ICANS - the grading language CAR-T protocols use",
    "41798119": "TIAN in 16/21 children after ICV B7-H3 CAR-T, 32% of infusions, mostly grade 1-2, median resolution <24 h; one needed CSF diversion",
    "41895715": "systematic analysis: locoregional CAR-T in high-grade glioma had 61% fewer grade >=3 AEs than IV delivery",
    "36259971": "BrainChild-03: repeated ICV B7-H3 CAR-T in DIPG feasible, CAR-T persistent in CSF",
    "38480922": "intrathecal CART-EGFR-IL13Ra2 in recurrent GBM: early neurotoxicity managed with dexamethasone and anakinra (the product used in NCT06973096)",
    "32341580": "preclinical basis for locoregional CAR-T delivery into CSF for medulloblastoma and ependymoma",
    "36629465": "ASA 2023 modular update: carbohydrate clear liquids, chewing gum, paediatric clear-liquid fasting duration",
    "28045707": "ASA 2017 preoperative fasting guideline: 2 h clear liquids, 4 h breast milk, 6 h light meal, 8 h fatty meal/solids",
    "34857683": "ESAIC 2022 paediatric guideline: clear fluids to 1 h, breast milk to 3 h, gastric ultrasound as adjunct",
    "21712716": "ESA 2011 perioperative fasting guideline for adults and children: clear fluids 2 h, solids 6 h",
}


def slug(authorstring, year, pmid):
    first = (authorstring or "").split(",")[0].strip()
    parts = first.split()
    surname = parts[0] if parts else "anon"
    surname = re.sub(r"[^a-z]", "", surname.lower()) or "anon"
    return f"{surname}_{year}_pmid{pmid}.xml"


def fetch_fulltext(pmcid, path):
    url = OA.format(pmcid=pmcid)
    req = urllib.request.Request(url, headers={"User-Agent": "lit-syn/1.0"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        body = resp.read()
    if len(body) < 2000:
        return False
    with open(path, "wb") as f:
        f.write(body)
    return True


def main():
    with open(f"{BASE}/curated_administration.json") as f:
        records = json.load(f)

    rows = []
    for r in records:
        pmid = r["pmid"]
        note = NOTES.get(pmid, "")
        if not note:
            print(f"NO NOTE for {pmid} {r['title'][:60]}")
        local = "not_open_access"
        if r.get("isOpenAccess") == "Y" and r.get("pmcid"):
            fname = slug(r["authors"], r["year"], pmid)
            path = f"{BASE}/fulltext/{fname}"
            if os.path.exists(path):
                local = f"fulltext/{fname}"
            else:
                try:
                    if fetch_fulltext(r["pmcid"], path):
                        local = f"fulltext/{fname}"
                        print(f"fetched {fname}")
                except urllib.error.HTTPError as exc:
                    print(f"no OA XML for {pmid}: {exc}")
                time.sleep(0.34)
        authors = r["authors"]
        first = authors.split(",")[0].strip() if authors else ""
        author_field = f"{first} et al." if authors.count(",") else first
        doi = r.get("doi", "")
        url = f"https://doi.org/{doi}" if doi else (
            f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/")
        rows.append("\t".join([
            r["category"], author_field, r["title"], r["journal"], r["year"],
            pmid, r.get("pmcid", ""), doi, url, local, note,
        ]))

    with open(f"{BASE}/index.tsv") as f:
        existing = f.read().rstrip("\n").split("\n")
    have = {line.split("\t")[5] for line in existing[1:] if len(line.split("\t")) > 5}
    new = [row for row in rows if row.split("\t")[5] not in have]
    with open(f"{BASE}/index.tsv", "w") as f:
        f.write("\n".join(existing + new) + "\n")
    print(f"appended {len(new)} rows, skipped {len(rows) - len(new)} duplicates")


if __name__ == "__main__":
    main()
