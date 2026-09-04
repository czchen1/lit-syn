#!/usr/bin/env python3
"""Harvest literature for evaluating the ANKTIVA (N-803) intravesical formulation vs IV.

Organising question: ANKTIVA (nogapendekin alfa inbakicept-pmln, N-803/ALT-803) is a
92-kDa IL-15N72D:IL-15RaSu/IgG1-Fc complex supplied as 400 mcg/0.4 mL and diluted into
50 mL of saline containing BCG for a 2-hour bladder dwell. What does the literature
support about (a) that formulation and its dilution step, (b) the systemic IV/SC route
for the same molecule, and (c) intravesical pharmaceutics generally - urine dilution,
dwell time, urothelial permeability to macromolecules, and instillation optimisation?

Query groups follow the axes on which the two routes differ: molecule identity and
route-specific clinical data, systemic PK/toxicity of IL-15 agonists, intravesical
pharmacokinetics and the dilution/dwell variables, macromolecule delivery across the
urothelium, and formulation/device strategies that alter intravesical residence.

Europe PMC REST search; records serialized to raw_harvest.json for curate.py.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
OUT = ("/home/ubuntu/repos/lit-syn/papers/anktiva-formulation-intravesical-vs-iv/"
       "raw_harvest.json")

N803 = ('("N-803" OR "ALT-803" OR "ALT803" OR nogapendekin OR inbakicept OR ANKTIVA OR '
        '"IL-15 superagonist" OR "IL15 superagonist" OR "IL-15 super-agonist" OR '
        '"IL-15N72D" OR "IL15N72D" OR "IL-15Ralpha sushi" OR "IL-15Ra sushi" OR '
        '"IL-15/IL-15Ralpha" OR "interleukin-15 superagonist")')
IL15 = ('("interleukin-15" OR "interleukin 15" OR "IL-15" OR "IL15" OR "rhIL-15" OR '
        '"heterodimeric IL-15" OR "hetIL-15" OR "IL-15 agonist" OR "RLI" OR "SO-C101" OR '
        '"NIZ985" OR "XmAb24306" OR "NKTR-255" OR "efbalropendekin")')
IVES = ('(intravesical OR intravesically OR "bladder instillation" OR "intravesical '
        'instillation" OR "bladder infusion" OR "intravesical therapy" OR '
        '"intravesical administration" OR "instilled into the bladder")')
ROUTE = ('("intravenous" OR "intravenously" OR "subcutaneous" OR "subcutaneously" OR '
         '"systemic administration" OR "route of administration" OR "systemic exposure")')

QUERIES = {
    # ---------------- the molecule itself, either route ----------------
    "n803_molecule": [
        N803,
        f'{N803} AND {IVES}',
        f'{N803} AND {ROUTE}',
        f'{N803} AND (pharmacokinetic* OR "serum concentration" OR "plasma concentration" '
        f'OR clearance OR "half-life" OR bioavailability OR "AUC" OR "Cmax")',
        f'{N803} AND ("cytokine release" OR "capillary leak" OR hypotension OR fever OR '
        f'"adverse event*" OR toxicity OR "dose-limiting")',
        f'{N803} AND (BCG OR "bacillus Calmette" OR NMIBC OR "non-muscle invasive" OR '
        f'"carcinoma in situ" OR QUILT)',
    ],
    # ---------------- IL-15 agonists systemically ----------------
    "il15_systemic": [
        f'{IL15} AND ("first-in-human" OR "phase 1" OR "phase I" OR "dose escalation") AND '
        f'({ROUTE})',
        f'{IL15} AND ("continuous infusion" OR "bolus infusion" OR "intravenous bolus") AND '
        f'(pharmacokinetic* OR toxicity OR "adverse event*")',
        f'{IL15} AND ("cytokine release syndrome" OR "capillary leak syndrome" OR '
        f'"IL-6" OR "interferon gamma" OR "sink" OR "receptor-mediated clearance" OR '
        f'"target-mediated drug disposition")',
        f'{IL15} AND (Fc OR "Fc fusion" OR "albumin fusion" OR PEGylat* OR "half-life '
        f'extension") AND (pharmacokinetic* OR exposure OR "half-life")',
        f'{IL15} AND (bladder OR urothelial OR NMIBC) AND (agonist OR superagonist OR '
        f'therapy)',
    ],
    # ---------------- intravesical pharmacokinetics, dilution, dwell ----------------
    "intravesical_pk_dilution": [
        f'{IVES} AND (pharmacokinetic* OR "drug concentration" OR "urine concentration" OR '
        f'"plasma level*" OR absorption OR "systemic absorption" OR "systemic uptake")',
        f'{IVES} AND (dilution OR "urine volume" OR "residual urine" OR "urine output" OR '
        f'hydration OR dehydration OR "fluid restriction" OR "urine production")',
        f'{IVES} AND ("dwell time" OR "retention time" OR "instillation time" OR '
        f'"contact time" OR "exposure time" OR "2 hours" OR "1 hour")',
        f'{IVES} AND (mitomycin) AND (optimiz* OR optimis* OR concentration OR dilution OR '
        f'"urinary pH" OR alkaliniz* OR pharmacokinetic*)',
        f'{IVES} AND ("urinary pH" OR "urine pH" OR alkaliniz* OR "sodium bicarbonate" OR '
        f'"ionic strength" OR osmolality) AND (stability OR activity OR absorption OR '
        f'concentration)',
        f'{IVES} AND (dose OR "dose-response" OR "concentration-response") AND '
        f'(recurrence OR efficacy OR response) AND (bladder cancer OR NMIBC)',
    ],
    # ---------------- macromolecules and biologics across the urothelium ----------------
    "urothelial_permeability_macromolecules": [
        f'{IVES} AND (antibody OR "monoclonal antibody" OR protein OR peptide OR cytokine '
        f'OR interferon OR interleukin OR "fusion protein") AND (delivery OR permeation OR '
        f'absorption OR penetration)',
        '("urothelial permeability" OR "bladder permeability" OR "urothelium barrier" OR '
        '"glycosaminoglycan layer" OR "GAG layer" OR "umbrella cells" OR '
        '"bladder permeability barrier") AND (drug OR macromolecule OR protein OR '
        'permeation OR transport)',
        f'{IVES} AND ("molecular weight" OR "molecular size" OR kDa OR "size dependence") '
        f'AND (permeation OR absorption OR penetration OR delivery)',
        f'{IVES} AND (interferon OR "IL-2" OR "interleukin-2" OR "IL-12" OR "IL-15" OR '
        f'"TNF" OR "GM-CSF") AND (bladder cancer OR NMIBC OR "carcinoma in situ")',
        f'{IVES} AND ("checkpoint inhibitor" OR pembrolizumab OR atezolizumab OR '
        f'durvalumab OR nivolumab OR "PD-1" OR "PD-L1") AND (bladder OR NMIBC)',
    ],
    # ---------------- formulation and device strategies ----------------
    "formulation_devices": [
        f'{IVES} AND (hydrogel OR "in situ gel" OR mucoadhesive OR liposom* OR nanoparticle '
        f'OR "sustained release" OR "controlled release" OR "drug delivery system")',
        '("TAR-200" OR "TAR-210" OR "pretzel device" OR "intravesical delivery system" OR '
        '"UGN-101" OR "UGN-102" OR "Jelmyto" OR "reverse thermal gel" OR '
        '"chemoablation") AND (bladder OR urothelial OR ureter*)',
        f'{IVES} AND (BCG OR "bacillus Calmette") AND (admixture OR "co-administration" OR '
        f'combination OR compatibility OR viability OR "colony forming")',
        f'{IVES} AND (stability OR compatibility OR "in-use stability" OR adsorption OR '
        f'aggregation OR "protein adsorption" OR catheter OR syringe OR "container '
        f'closure") AND (protein OR biologic* OR drug OR formulation)',
        '(BCG OR "bacillus Calmette-Guerin") AND (saline OR diluent OR "reconstitution" OR '
        '"viability" OR "colony forming units") AND (instillation OR intravesical OR '
        'stability)',
        f'{IVES} AND (electromotive OR EMDA OR hyperthermia OR "chemohyperthermia" OR '
        f'"radiofrequency" OR "device-assisted") AND (bladder cancer OR NMIBC)',
    ],
    # ---------------- route comparison as a design question ----------------
    "route_comparison": [
        f'{IVES} AND {ROUTE} AND (compar* OR versus OR "vs.") AND (bladder OR urothelial)',
        '("local delivery" OR "locoregional" OR "compartmental delivery" OR '
        '"intracavitary") AND (immunotherapy OR cytokine OR "immune agonist") AND '
        '(systemic OR intravenous) AND (compar* OR versus OR advantage OR toxicity)',
        f'{IVES} AND ("systemic toxicity" OR "systemic side effects" OR "systemic immune '
        f'activation" OR "abscopal" OR "systemic immunity") AND (cytokine OR immunotherapy '
        f'OR bladder)',
        '("intratumoral" OR "intratumoural" OR "intravesical" OR "intraperitoneal") AND '
        '(cytokine OR "IL-15" OR "IL-2" OR "IL-12") AND (systemic exposure OR "therapeutic '
        'index" OR "reduced toxicity")',
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
