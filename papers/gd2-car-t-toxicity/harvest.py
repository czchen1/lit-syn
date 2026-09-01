#!/usr/bin/env python3
"""Harvest literature on GD2 CAR-T toxicity, clinical and preclinical.

Organising question: what goes wrong when GD2-directed CAR T cells are given to a
patient (or an animal), with particular attention to (a) intracerebroventricular /
locoregional CNS delivery and (b) transient organ-function changes that alter the
pharmacology of concomitant drugs.

Toxicity domains are the query groups. Europe PMC REST search; records serialized
to raw_harvest.json for downstream curation by curate.py.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
OUT = "/home/ubuntu/repos/lit-syn/papers/gd2-car-t-toxicity/raw_harvest.json"

GD2 = ('("GD2" OR "disialoganglioside" OR "GD2-CAR" OR "GD2 CAR" OR "14g2a" OR '
       '"hu14.18" OR "dinutuximab" OR "naxitamab" OR "3F8" OR "ch14.18")')
CART = ('("CAR T" OR "CAR-T" OR "CAR T-cell" OR "chimeric antigen receptor" OR '
        '"CAR NKT" OR "CAR-NK" OR "engineered T cell")')
TOX = ('(toxicity OR adverse OR safety OR "adverse events" OR complication OR '
       'tolerability OR "dose-limiting")')

QUERIES = {
    # ---------------- GD2-specific core ----------------
    "gd2_cart_core": [
        f'{GD2} AND {CART} AND {TOX}',
        f'{GD2} AND {CART} AND ("phase 1" OR "phase I" OR "phase 1/2" OR "first-in-human" OR "clinical trial")',
        f'{GD2} AND {CART} AND (neuroblastoma OR osteosarcoma OR sarcoma OR melanoma OR "diffuse midline glioma" OR DIPG OR H3K27M OR neuroblastoma)',
        f'{GD2} AND {CART} AND ("on-target off-tumor" OR "on-target, off-tumour" OR "off-tumor toxicity" OR "off-target")',
        f'"GD2-CART01" OR "GD2 CART01" OR "CARTOX" AND GD2',
    ],
    # ---------------- CNS / intraventricular delivery ----------------
    "icv_locoregional_cns": [
        f'("intracerebroventricular" OR "intraventricular" OR "intra-cerebroventricular" OR "Ommaya" OR "Rickham" OR "intrathecal" OR "locoregional") AND {CART} AND (glioma OR "midline glioma" OR DIPG OR neuroblastoma OR CNS OR brain)',
        f'"intracerebroventricular" AND {CART}',
        f'{GD2} AND {CART} AND ("intracranial pressure" OR hydrocephalus OR "external ventricular drain" OR "cerebrospinal fluid" OR ventriculoperitoneal)',
        f'{CART} AND (glioma OR "midline glioma" OR DIPG) AND ("tumor inflammation-associated neurotoxicity" OR "tumour inflammation-associated neurotoxicity" OR TIAN)',
        f'("B7-H3 CAR" OR "B7H3 CAR" OR "IL13Ralpha2 CAR" OR "IL13Rα2" OR "HER2 CAR") AND (intraventricular OR intracranial OR intratumoral OR locoregional) AND (safety OR toxicity OR "adverse events")',
        f'{CART} AND ("posterior fossa" OR brainstem OR "pontine" OR "fourth ventricle") AND (edema OR oedema OR toxicity OR "neurologic deterioration")',
    ],
    # ---------------- CRS ----------------
    "cytokine_release_syndrome": [
        f'"cytokine release syndrome" AND {GD2}',
        f'"cytokine release syndrome" AND {CART} AND (grading OR consensus OR management OR tocilizumab OR anakinra OR siltuximab)',
        f'"cytokine release syndrome" AND (IL-6 OR interleukin-6 OR ferritin OR CRP OR "C-reactive protein") AND ("organ dysfunction" OR hypotension OR "capillary leak")',
        f'"macrophage activation syndrome" OR "hemophagocytic" AND {CART}',
        f'{CART} AND ("cytokine release syndrome" OR CRS) AND (pediatric OR children OR paediatric) AND ("solid tumor" OR "solid tumour")',
    ],
    # ---------------- neurotoxicity ----------------
    "neurotoxicity": [
        f'("ICANS" OR "immune effector cell-associated neurotoxicity" OR "neurotoxicity") AND {CART} AND (grading OR management OR pathophysiology OR incidence)',
        f'"neurotoxicity" AND {GD2} AND {CART}',
        f'{CART} AND neurotoxicity AND ("cerebral edema" OR "cerebral oedema" OR seizure OR "status epilepticus" OR "EEG" OR levetiracetam)',
        f'{CART} AND ("blood-brain barrier" OR "endothelial activation" OR "angiopoietin") AND neurotoxicity',
        f'{GD2} AND ("peripheral neuropathy" OR "neuropathic pain" OR allodynia OR "pain" OR "nerve") AND (antibody OR "CAR T" OR immunotherapy) AND (toxicity OR adverse)',
    ],
    # ---------------- hepatic ----------------
    "hepatic": [
        f'{CART} AND (hepatotoxicity OR "liver injury" OR transaminitis OR "transaminase" OR "hyperbilirubinemia" OR "ALT elevation" OR "sinusoidal obstruction syndrome" OR "veno-occlusive")',
        f'{GD2} AND (hepatic OR liver) AND (toxicity OR "adverse events" OR transaminase)',
        f'("CAR T" OR "chimeric antigen receptor") AND (liver OR hepatic) AND (dysfunction OR failure OR "Child-Pugh" OR "drug metabolism")',
        f'"cytokine release syndrome" AND (liver OR hepatic) AND (injury OR dysfunction OR enzyme)',
    ],
    # ---------------- renal / electrolyte ----------------
    "renal_electrolyte": [
        f'{CART} AND ("acute kidney injury" OR "renal dysfunction" OR nephrotoxicity OR "creatinine" OR "renal impairment" OR "tumor lysis syndrome")',
        f'{CART} AND (hyponatremia OR SIADH OR hypophosphatemia OR "electrolyte" OR "fluid overload")',
        f'"chimeric antigen receptor" AND ("renal impairment" OR dialysis OR "glomerular filtration") AND (safety OR outcome OR dosing)',
    ],
    # ---------------- hematologic / coagulation ----------------
    "hematologic_coagulopathy": [
        f'{CART} AND (cytopenia OR "prolonged cytopenia" OR ICAHT OR neutropenia OR thrombocytopenia OR "aplastic" OR "hematopoietic recovery")',
        f'{CART} AND (coagulopathy OR "disseminated intravascular coagulation" OR fibrinogen OR "D-dimer" OR bleeding OR thrombosis)',
        f'{GD2} AND {CART} AND (cytopenia OR neutropenia OR thrombocytopenia OR lymphodepletion)',
        f'{CART} AND (hypogammaglobulinemia OR "B-cell aplasia" OR "immune reconstitution" OR "infection" AND (prophylaxis OR incidence))',
    ],
    # ---------------- cardiopulmonary ----------------
    "cardiopulmonary": [
        f'{CART} AND (cardiotoxicity OR "cardiac dysfunction" OR arrhythmia OR "ejection fraction" OR "QT")',
        f'{CART} AND ("respiratory failure" OR hypoxia OR "pulmonary edema" OR "pulmonary oedema" OR ARDS OR "capillary leak syndrome")',
        f'{GD2} AND (hypotension OR bronchospasm OR "capillary leak" OR "infusion reaction") AND (antibody OR "CAR T")',
    ],
    # ---------------- drug interactions / PK ----------------
    "drug_interaction_pk": [
        '("cytokine" OR "interleukin-6" OR "IL-6" OR inflammation) AND ("cytochrome P450" OR CYP3A4 OR "drug metabolism" OR "drug-drug interaction") AND (suppression OR downregulation OR clearance)',
        '(tocilizumab OR siltuximab OR "IL-6 receptor") AND ("CYP3A4" OR "drug interaction" OR "cytochrome P450" OR "simvastatin" OR clearance)',
        f'{CART} AND ("drug-drug interaction" OR "concomitant medication" OR "pharmacokinetic interaction" OR polypharmacy)',
        f'{CART} AND (corticosteroid OR dexamethasone) AND (expansion OR efficacy OR outcome) AND (toxicity OR management)',
        f'{CART} AND (anticonvulsant OR levetiracetam OR antiepileptic OR "seizure prophylaxis")',
        '("chimeric antigen receptor" OR "CAR T") AND (antifungal OR azole OR voriconazole OR posaconazole OR "vancomycin" OR aminoglycoside) AND (interaction OR dosing OR nephrotoxicity OR hepatotoxicity)',
        '"critical illness" AND ("drug clearance" OR "augmented renal clearance" OR "hepatic clearance") AND (cytokine OR inflammation OR sepsis)',
    ],
    # ---------------- preclinical toxicity ----------------
    "preclinical_toxicity": [
        f'{GD2} AND {CART} AND (mice OR murine OR "mouse model" OR rat OR "non-human primate" OR canine) AND (toxicity OR lethal OR "on-target" OR safety OR histopathology)',
        f'{GD2} AND ("affinity" OR "E101K" OR "high-affinity scFv") AND (CAR OR "chimeric antigen receptor") AND (toxicity OR "CNS toxicity" OR lethality)',
        f'{CART} AND ("syngeneic" OR "immunocompetent" OR "humanized mouse") AND ("toxicity model" OR "preclinical safety" OR "cytokine release syndrome model")',
        f'{GD2} AND (expression OR immunohistochemistry) AND ("normal tissue" OR "healthy tissue" OR "peripheral nerve" OR brain OR skin) AND (ganglioside OR GD2)',
        f'{CART} AND (neurotoxicity OR "CNS toxicity") AND ("mouse model" OR "animal model" OR "non-human primate" OR macaque)',
    ],
    # ---------------- safety engineering / mitigation ----------------
    "toxicity_mitigation": [
        f'{GD2} AND {CART} AND ("safety switch" OR iCasp9 OR "inducible caspase" OR rimiducid OR "suicide gene" OR EGFRt OR "logic gate" OR "dose escalation")',
        f'{CART} AND (dasatinib OR "kinase switch" OR "pause switch" OR "cytokine sink" OR "IL-1 receptor antagonist" OR anakinra) AND (toxicity OR CRS OR neurotoxicity)',
        f'{CART} AND ("toxicity management" OR "consensus guideline" OR "grading system" OR ASTCT) AND (CRS OR neurotoxicity OR ICANS)',
        f'{CART} AND ("solid tumor" OR "solid tumour") AND ("toxicity" OR "adverse event") AND (review OR "systematic review" OR meta-analysis)',
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
