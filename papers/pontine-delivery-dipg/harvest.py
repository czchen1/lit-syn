#!/usr/bin/env python3
"""Harvest literature on drug/therapeutic delivery to the pons and brainstem.

Focus: DIPG / diffuse midline glioma H3K27-altered, plus related conditions that
require getting agents into the brainstem or across the blood-brain barrier
(other pediatric high-grade gliomas, leptomeningeal disease, brainstem
cavernomas/DVAs where technique papers are informative).

Organized by delivery modality. Europe PMC REST search; records serialized to
raw_harvest.json for downstream curation.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
OUT = "/home/ubuntu/repos/lit-syn/papers/pontine-delivery-dipg/raw_harvest.json"

DISEASE = ('("diffuse intrinsic pontine glioma" OR "DIPG" OR "diffuse midline glioma" '
           'OR "brainstem glioma" OR "brain stem glioma" OR "H3K27M" OR "pontine")')

MODALITIES = {
    "convection_enhanced_delivery": [
        f'"convection-enhanced delivery" AND {DISEASE}',
        '"convection enhanced delivery" AND (brainstem OR "brain stem" OR pons OR pontine)',
        '"convection-enhanced delivery" AND (catheter OR "infusion rate" OR reflux OR "volume of distribution" OR dosimetry)',
        '"convection-enhanced delivery" AND (glioma OR glioblastoma) AND ("clinical trial" OR "phase 1" OR "phase I" OR safety)',
        '("interstitial infusion" OR "intratumoral infusion" OR "intratumoural infusion") AND (brainstem OR pons OR glioma)',
        '"convection-enhanced delivery" AND (panobinostat OR "MTX110" OR omburtamab OR "8H9" OR topotecan OR carboplatin OR IL13 OR "immunotoxin")',
    ],
    "focused_ultrasound_bbb_opening": [
        f'("focused ultrasound" OR "MR-guided focused ultrasound" OR "MRgFUS" OR "low-intensity focused ultrasound" OR LIFU) AND {DISEASE}',
        '("focused ultrasound" OR sonication) AND microbubble AND ("blood-brain barrier" OR "blood brain barrier") AND (brainstem OR pons)',
        '("focused ultrasound" AND "blood-brain barrier opening") AND (glioma OR glioblastoma OR "brain tumor" OR "brain tumour")',
        '("focused ultrasound" OR "ultrasound-mediated") AND ("drug delivery" OR "liposomal doxorubicin" OR panobinostat OR temozolomide) AND brain',
        '"histotripsy" OR ("sonodynamic therapy" AND glioma)',
    ],
    "intra_arterial_and_bbb_disruption": [
        '("intra-arterial" OR "intraarterial" OR "superselective intra-arterial cerebral infusion" OR SIACI) AND (glioma OR "brain tumor" OR DIPG OR brainstem)',
        '("osmotic blood-brain barrier disruption" OR "mannitol" AND "blood-brain barrier disruption") AND (brain tumor OR glioma OR chemotherapy)',
        '"intra-arterial" AND ("basilar artery" OR "vertebral artery" OR "posterior circulation") AND (infusion OR chemotherapy OR bevacizumab)',
        '("regadenoson" OR "NEO100" OR "RMP-7" OR "Cereport" OR bradykinin) AND "blood-brain barrier"',
    ],
    "intrathecal_intraventricular": [
        f'("intrathecal" OR "intraventricular" OR "intracerebroventricular" OR "Ommaya") AND {DISEASE}',
        '("intracerebroventricular" OR "intraventricular") AND ("CAR T" OR "CAR-T" OR "chimeric antigen receptor") AND (glioma OR "midline glioma" OR brainstem)',
        '("intrathecal" OR "intra-CSF") AND ("drug delivery" OR pharmacokinetics) AND (CSF OR "cerebrospinal fluid") AND (brain OR tumor OR tumour)',
        '"cerebrospinal fluid" AND ("glymphatic" OR "CSF flow") AND ("drug distribution" OR "drug delivery")',
    ],
    "car_t_and_cell_therapy_delivery": [
        f'("CAR T" OR "CAR-T" OR "chimeric antigen receptor") AND {DISEASE}',
        '("GD2 CAR" OR "B7-H3 CAR" OR "GD2-CAR" OR "B7H3 CAR") AND (glioma OR "midline glioma" OR DIPG OR pons)',
        '("neural stem cell" OR "mesenchymal stem cell" OR "NSC-mediated") AND ("drug delivery" OR "oncolytic" OR "tumor-tropic") AND (glioma OR brain)',
        '("locoregional" OR "loco-regional") AND ("CAR T" OR "cell therapy") AND (CNS OR brain OR glioma)',
    ],
    "viral_vectors_and_oncolytic": [
        f'("oncolytic" OR "adenovirus" OR "DNX-2401" OR "poliovirus" OR "herpes simplex virus" OR "reovirus") AND {DISEASE}',
        '("AAV" OR "adeno-associated virus") AND ("brainstem" OR pons OR "midline glioma" OR "CNS gene therapy") AND (delivery OR tropism OR intraparenchymal)',
        '("oncolytic virus" AND ("intratumoral injection" OR "intratumoural injection")) AND (brain OR glioma OR "brain stem")',
        '("gene therapy" AND ("intraparenchymal" OR "intrathecal" OR "intracisternal")) AND (brainstem OR "midline" OR CNS)',
    ],
    "nanoparticle_and_formulation": [
        f'(nanoparticle OR liposome OR "lipid nanoparticle" OR micelle OR dendrimer OR exosome) AND {DISEASE}',
        '(nanoparticle OR "lipid nanoparticle") AND ("blood-brain barrier" OR "brain delivery") AND (glioma OR "brain tumor") AND (targeting OR crossing OR transcytosis)',
        '("convection-enhanced delivery" OR "intratumoral") AND (nanoparticle OR liposome OR "nanocarrier") AND brain',
        '("brain-penetrating nanoparticle" OR "PEGylated nanoparticle" AND "brain tissue penetration")',
        '(exosome OR "extracellular vesicle") AND ("brain delivery" OR "blood-brain barrier") AND (glioma OR siRNA OR mRNA)',
    ],
    "intranasal": [
        '"intranasal" AND ("nose-to-brain" OR "brain delivery" OR "CNS delivery") AND (glioma OR "brain tumor" OR chemotherapy OR perillyl)',
        f'"intranasal" AND {DISEASE}',
        '("nose-to-brain" AND (nanoparticle OR "olfactory" OR trigeminal)) AND (drug delivery OR CNS)',
    ],
    "systemic_bbb_penetrant_pharmacology": [
        f'("blood-brain barrier" OR "brain penetration" OR "efflux" OR "P-glycoprotein" OR "ABCB1" OR "ABCG2") AND {DISEASE}',
        '(ONC201 OR dordaviprone OR panobinostat OR "ONC206" OR paxalisib OR "GDC-0084" OR selumetinib OR everolimus) AND ("brain penetration" OR pharmacokinetics OR "CSF")',
        '"unbound brain-to-plasma" OR ("Kp,uu" AND brain)',
        f'("drug delivery" OR "pharmacokinetic") AND {DISEASE} AND (barrier OR penetration OR distribution)',
        '("blood-brain barrier" AND ("intact" OR heterogeneity OR permeability)) AND ("diffuse midline glioma" OR DIPG OR "brainstem tumor")',
    ],
    "implants_depots_and_devices": [
        '("Gliadel" OR "carmustine wafer" OR "polymer implant" OR "drug-eluting implant" OR hydrogel) AND (glioma OR "brain tumor" OR intracranial) AND (delivery OR local)',
        '("implanted catheter" OR "subcutaneous port" OR "refillable" OR "chronic infusion" OR "repeated convection-enhanced delivery") AND (brain OR brainstem OR glioma)',
        '("microneedle" OR "intracranial microdevice" OR "implantable microdevice") AND (brain OR tumor)',
        '"drug delivery device" AND (brainstem OR "brain stem" OR pons)',
    ],
    "imaging_dosimetry_and_modeling": [
        '("real-time MRI" OR "gadolinium tracer" OR "co-infusion" OR "iron oxide tracer") AND "convection-enhanced delivery"',
        '("computational model" OR "finite element" OR "predictive model" OR simulation) AND ("convection-enhanced delivery" OR "interstitial fluid flow") AND brain',
        '("PET imaging" OR "SPECT" OR radiolabeled) AND ("convection-enhanced delivery" OR "intratumoral") AND (glioma OR brainstem OR dosimetry)',
        '"diffusion tensor imaging" AND ("convection-enhanced delivery" OR "drug distribution") AND brain',
    ],
    "surgical_access_and_safety": [
        '("brainstem biopsy" OR "stereotactic biopsy") AND (DIPG OR "diffuse midline glioma" OR "brainstem glioma") AND (safety OR feasibility OR yield)',
        '("transcerebellar" OR "transfrontal" OR "trajectory planning" OR "safe entry zone") AND (brainstem OR pons) AND (biopsy OR catheter OR approach)',
        '"brainstem" AND ("surgical anatomy" OR "safe entry zones") AND (lesion OR cavernoma OR "cavernous malformation")',
        '("robot-assisted" OR "frameless stereotaxy" OR "neuronavigation") AND (brainstem OR pons) AND (biopsy OR infusion OR catheter)',
    ],
    "radiation_and_combined_modality": [
        f'("re-irradiation" OR "reirradiation" OR "radiosensitizer" OR "radiotherapy") AND {DISEASE} AND (delivery OR combination OR outcome)',
        '("radiation-induced blood-brain barrier" OR "radiation and BBB permeability") AND (glioma OR brain)',
        '("boron neutron capture" OR "brachytherapy" OR "radioimmunotherapy") AND (brainstem OR pons OR "midline glioma")',
    ],
    "related_brainstem_cns_diseases": [
        '("brainstem" OR pons) AND ("drug delivery" OR "targeted delivery") AND (multiple sclerosis OR ALS OR "spinal muscular atrophy" OR "Parkinson" OR leukodystrophy)',
        '("intraparenchymal infusion" OR "convection-enhanced delivery") AND (Parkinson OR "GDNF" OR AADC OR "gene therapy") AND (brain OR putamen OR brainstem)',
        '("leptomeningeal" OR "CSF dissemination") AND ("diffuse midline glioma" OR medulloblastoma OR ependymoma) AND (delivery OR intrathecal)',
        '"ependymoma" AND (brainstem OR "posterior fossa") AND ("drug delivery" OR "convection-enhanced delivery" OR intrathecal)',
    ],
}


def epmc_search(query, page_size=100):
    params = {
        "query": query + " AND (SRC:MED OR SRC:PMC OR SRC:PPR)",
        "format": "json",
        "pageSize": str(page_size),
        "resultType": "core",
    }
    url = EPMC + "?" + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            sys.stderr.write(f"retry {attempt} for {query[:50]}: {e}\n")
            time.sleep(3)
    return {"resultList": {"result": []}}


def clean(text):
    if not text:
        return ""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text)).strip()


def main():
    seen = {}
    for modality, queries in MODALITIES.items():
        for q in queries:
            data = epmc_search(q)
            results = data.get("resultList", {}).get("result", [])
            for rec in results:
                key = rec.get("pmid") or rec.get("doi") or rec.get("id")
                if not key:
                    continue
                if key in seen:
                    seen[key]["also_modalities"].add(modality)
                    continue
                seen[key] = {
                    "modality": modality,
                    "also_modalities": set(),
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
            time.sleep(0.34)
            sys.stderr.write(f"{modality}: '{q[:60]}' -> {len(results)}\n")

    out = []
    for v in seen.values():
        v["also_modalities"] = "|".join(sorted(v["also_modalities"]))
        v["pubType"] = "|".join(v["pubType"]) if isinstance(v["pubType"], list) else str(v["pubType"])
        out.append(v)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1)
    print(f"total unique records: {len(out)}")


if __name__ == "__main__":
    main()
