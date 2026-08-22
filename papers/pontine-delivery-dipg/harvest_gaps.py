#!/usr/bin/env python3
"""Third harvest pass: fill route-specific gaps found on review of the index.

Adds coverage of (i) direct fourth-ventricle / cisternal infusion, (ii) named
brainstem delivery programs and devices (Renishaw, MTX110, omburtamab, rhenium
nanoliposomes, IL13-PE), (iii) intranasal and BBB-shuttle routes, which the
broad passes under-sampled. Merges into raw_harvest.json.
"""
import json
import sys
import time

from harvest import epmc_search, clean, OUT

GAP_QUERIES = {
    "intrathecal_intraventricular": [
        '"fourth ventricle" AND (infusion OR chemotherapy OR methotrexate OR etoposide OR topotecan) AND (brain tumor OR glioma OR medulloblastoma OR delivery)',
        'AUTH:"Sandberg DI" AND (ventricle OR infusion OR delivery)',
        '("intraventricular" OR "intra-CSF" OR intrathecal) AND ("diffuse midline glioma" OR DIPG OR "brainstem glioma")',
        '"intracisternal" AND (infusion OR delivery OR chemotherapy) AND (brain OR CNS OR tumor)',
        '("intraventricular topotecan" OR "intraventricular methotrexate" OR "intrathecal topotecan")',
        '"intraventricular" AND ("omburtamab" OR "8H9" OR "radioimmunotherapy") AND (CNS OR brain OR neuroblastoma)',
    ],
    "named_programs_devices": [
        '"MTX110" OR ("soluble panobinostat" AND delivery)',
        '"Renishaw" AND (drug delivery OR catheter OR neuroinfuse)',
        'omburtamab AND (delivery OR brainstem OR intraventricular OR DIPG)',
        '("rhenium" AND nanoliposome) OR "186RNL"',
        '"IL13-PE" OR "IL13-Pseudomonas" OR "IL13RA2 immunotoxin"',
        '"PNOC" AND (trial OR consortium) AND (glioma OR DIPG OR delivery)',
        '"ONC201" AND (CSF OR "brain penetration" OR pharmacokinetic OR delivery)',
        '("drug delivery system" OR "implanted device") AND ("diffuse intrinsic pontine glioma" OR "brainstem")',
    ],
    "intranasal": [
        '"intranasal" AND (glioma OR "brain tumor") AND (mesenchymal stem cell OR nanoparticle OR chemotherapy OR immunotherapy)',
        '"nose-to-brain" AND (glioma OR "brain tumor" OR "brainstem")',
        '"intranasal" AND ("perillyl alcohol" OR NEO100 OR temozolomide OR "5-azacytidine")',
        '("FUSIN" OR ("focused ultrasound" AND intranasal))',
    ],
    "antibody_conjugate_shuttle": [
        '("transferrin receptor" OR "TfR" OR "insulin receptor") AND ("brain delivery" OR "BBB shuttle" OR transcytosis) AND (antibody OR fusion protein)',
        '("antibody-drug conjugate" OR ADC) AND ("brain tumor" OR glioma OR "CNS penetration" OR "diffuse midline glioma")',
        '"molecular Trojan horse" OR ("brain shuttle" AND antibody)',
        '("peptide-mediated" OR angiopep OR "ApoE peptide" OR "RVG peptide") AND ("brain delivery" OR "blood-brain barrier") AND (glioma OR CNS)',
    ],
    "imaging_dosimetry_modeling": [
        '("infusate distribution" OR "drug distribution mapping" OR "tissue clearance") AND (brainstem OR pons OR "convection")',
        '("patient-specific" OR "in silico") AND ("drug delivery" OR infusion) AND (brainstem OR "diffuse midline glioma" OR glioma)',
        '("gadolinium co-infusion" OR "surrogate tracer" OR "MRI-monitored infusion") AND brain',
    ],
    "brainstem_bbb_biology": [
        '("blood-brain barrier" OR "vascular" OR pericyte OR "tight junction") AND ("brainstem" OR pons OR "diffuse midline glioma") AND (integrity OR permeability OR heterogeneity)',
        '("intact blood-brain barrier" AND (DIPG OR "diffuse midline glioma"))',
        '("blood-brain barrier organoid" OR "microfluidic BBB" OR "BBB-on-a-chip") AND (glioma OR "midline glioma" OR pediatric)',
    ],
}


def main():
    with open(OUT) as f:
        existing = json.load(f)
    seen = {(r.get("pmid") or r.get("doi") or r["title"][:60]): r for r in existing}
    added = 0
    for modality, queries in GAP_QUERIES.items():
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
            sys.stderr.write(f"gap {modality}: '{q[:55]}' -> {len(results)}\n")

    with open(OUT, "w") as f:
        json.dump(list(seen.values()), f, indent=1)
    print(f"added {added} gap records; total {len(seen)}")


if __name__ == "__main__":
    main()
