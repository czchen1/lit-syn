#!/usr/bin/env python3
"""Supplemental harvest: foundational / pre-2016 pontine-delivery literature.

The main relevance-ranked harvest skews heavily to 2017+. This pass runs
year-restricted and landmark-specific queries so the collection also contains
the founding CED/brainstem-infusion, osmotic BBB-disruption, and early
brainstem-trial literature. Results are merged into raw_harvest.json.
"""
import json
import sys
import time

from harvest import epmc_search, clean, OUT

SEED_QUERIES = {
    "convection_enhanced_delivery": [
        '"convection-enhanced delivery" AND PUB_YEAR:[1994 TO 2012]',
        '"convection-enhanced delivery" AND (brainstem OR "brain stem" OR pons) AND PUB_YEAR:[1994 TO 2016]',
        'TITLE:("convection" AND (delivery OR perfusion OR infusion)) AND brain AND PUB_YEAR:[1994 TO 2016]',
        '("high-flow microinfusion" OR "convective" AND "interstitial infusion") AND brain',
        'AUTH:"Bobo RH" OR AUTH:"Lonser RR" AND ("convection" OR infusion)',
        'AUTH:"Souweidane MM" AND (delivery OR infusion OR brainstem)',
        '"convection-enhanced delivery" AND (primate OR "non-human primate" OR canine OR porcine) AND brainstem',
    ],
    "focused_ultrasound": [
        '("focused ultrasound" AND "blood-brain barrier") AND PUB_YEAR:[2001 TO 2016]',
        'AUTH:"Hynynen K" AND ("blood-brain barrier" OR microbubble)',
    ],
    "intra_arterial": [
        '("osmotic blood-brain barrier disruption" OR "intra-arterial chemotherapy") AND brain AND PUB_YEAR:[1980 TO 2012]',
        'AUTH:"Neuwelt EA" AND ("barrier disruption" OR "intra-arterial")',
    ],
    "intrathecal_csf": [
        '("intrathecal chemotherapy" OR "intraventricular chemotherapy") AND (brain tumor OR glioma OR "CNS") AND PUB_YEAR:[1980 TO 2014]',
    ],
    "systemic_bbb_pharmacology": [
        '("blood-brain barrier" AND ("brainstem glioma" OR "pontine glioma")) AND PUB_YEAR:[1990 TO 2016]',
        'TITLE:("blood-brain barrier" OR "brain penetration") AND (chemotherapy OR drug) AND PUB_YEAR:[1990 TO 2010]',
    ],
    "surgical_access": [
        '("brainstem biopsy" OR "stereotactic biopsy of brainstem") AND PUB_YEAR:[1990 TO 2016]',
        '"safe entry zones" AND brainstem',
    ],
    "viral_vector": [
        '("oncolytic" OR "gene therapy") AND ("brainstem" OR "pontine glioma") AND PUB_YEAR:[1995 TO 2016]',
        'AAV AND ("brainstem" OR "medulla") AND (transduction OR tropism OR infusion)',
    ],
    "nanoparticle": [
        '(liposome OR nanoparticle) AND ("convection-enhanced delivery" OR brainstem) AND PUB_YEAR:[1995 TO 2016]',
    ],
    "implant_depot_device": [
        '("carmustine wafer" OR Gliadel) AND (glioma OR "brain tumor") AND PUB_YEAR:[1995 TO 2015]',
    ],
    "imaging_dosimetry_modeling": [
        '("real-time MR" OR gadolinium OR tracer) AND "convection-enhanced delivery" AND PUB_YEAR:[2000 TO 2016]',
        '("mathematical model" OR "computational") AND "convection-enhanced delivery"',
        '"diffusion tensor imaging" AND ("convection-enhanced delivery" OR "drug distribution" OR "interstitial")',
    ],
    "related_brainstem_cns_diseases": [
        '("GDNF" OR "AADC" OR putaminal) AND ("convection-enhanced delivery" OR "intraparenchymal infusion")',
        'nusinersen AND intrathecal AND (distribution OR pharmacokinetic OR CNS)',
    ],
}


def main():
    with open(OUT) as f:
        existing = json.load(f)
    seen = {(r.get("pmid") or r.get("doi") or r["title"][:60]): r for r in existing}
    added = 0
    for modality, queries in SEED_QUERIES.items():
        for q in queries:
            data = epmc_search(q)
            results = data.get("resultList", {}).get("result", [])
            for rec in results:
                key = rec.get("pmid") or rec.get("doi") or clean(rec.get("title", ""))[:60]
                if not key or key in seen:
                    continue
                seen[key] = {
                    "modality": modality,
                    "also_modalities": "",
                    "pmid": rec.get("pmid", ""),
                    "pmcid": rec.get("pmcid", ""),
                    "doi": rec.get("doi", ""),
                    "title": clean(rec.get("title", "")).rstrip("."),
                    "abstract": clean(rec.get("abstractText", "")),
                    "authors": rec.get("authorString", ""),
                    "venue": (rec.get("journalInfo", {}).get("journal", {}).get("title", "")
                              or rec.get("journalTitle", "")),
                    "year": rec.get("pubYear", ""),
                    "isOA": rec.get("isOpenAccess", "N"),
                    "inEPMC": rec.get("inEPMC", "N"),
                    "hasPDF": rec.get("hasPDF", "N"),
                    "pubType": "|".join(rec.get("pubTypeList", {}).get("pubType", [])),
                    "src": rec.get("source", ""),
                }
                added += 1
            time.sleep(0.34)
            sys.stderr.write(f"seed {modality}: '{q[:55]}' -> {len(results)}\n")

    with open(OUT, "w") as f:
        json.dump(list(seen.values()), f, indent=1)
    print(f"added {added} seed records; total {len(seen)}")


if __name__ == "__main__":
    main()
