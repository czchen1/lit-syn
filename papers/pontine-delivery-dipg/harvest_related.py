#!/usr/bin/env python3
"""Fourth harvest pass: non-oncologic CNS diseases whose delivery experience is
directly transferable to the pons (MR-guided intraparenchymal AAV infusion,
intraventricular enzyme replacement, intrathecal antisense oligonucleotides,
transcranial focused-ultrasound BBB opening in neurodegeneration).

Merges into raw_harvest.json under modality keys reused by curate.py.
"""
import json
import sys
import time

from harvest import epmc_search, clean, OUT

RELATED_QUERIES = {
    "convection_enhanced_delivery": [
        '("MR-guided" OR "MRI-guided" OR "intraputaminal" OR "intraparenchymal") AND (AAV OR "gene therapy") AND (Parkinson OR AADC OR "aromatic L-amino acid decarboxylase" OR "MLD" OR Canavan)',
        '"convection-enhanced delivery" AND (Parkinson OR Gaucher OR "enzyme replacement" OR "lysosomal storage" OR epilepsy OR "Huntington")',
        '("intraputaminal infusion" OR "intrastriatal infusion") AND (GDNF OR neurturin OR CDNF OR "growth factor")',
        '"brainstem" AND ("gene therapy" OR "AAV") AND (infusion OR injection OR delivery)',
    ],
    "intrathecal_csf": [
        'nusinersen AND (intrathecal OR "CSF distribution" OR pharmacokinetic)',
        '("antisense oligonucleotide" OR ASO) AND intrathecal AND (CNS OR "spinal muscular atrophy" OR ALS OR Huntington)',
        'cerliponase AND (intraventricular OR "CLN2" OR "enzyme replacement")',
        '("intracerebroventricular enzyme replacement" OR "ICV enzyme replacement") AND (mucopolysaccharidosis OR "lysosomal")',
        'onasemnogene AND (intrathecal OR intracisternal OR "CSF")',
    ],
    "focused_ultrasound": [
        '"focused ultrasound" AND "blood-brain barrier" AND (Alzheimer OR Parkinson OR "amyotrophic lateral sclerosis" OR "essential tremor")',
        '"focused ultrasound" AND (brainstem OR pons OR "posterior fossa") AND (safety OR feasibility OR targeting OR skull)',
        '"transcranial" AND ("MR-guided focused ultrasound") AND (thalamotomy OR lesioning OR "acoustic window")',
    ],
    "systemic_bbb_pharmacology": [
        '("blood-brain barrier" OR "brain penetration") AND (nusinersen OR risdiplam OR "small molecule") AND ("CSF" OR "brain exposure") AND (pediatric OR children)',
        '("regional heterogeneity" OR "regional differences") AND "blood-brain barrier" AND (brainstem OR "posterior fossa" OR pons)',
    ],
}


def main():
    with open(OUT) as f:
        existing = json.load(f)
    seen = {(r.get("pmid") or r.get("doi") or r["title"][:60]): r for r in existing}
    added = 0
    for modality, queries in RELATED_QUERIES.items():
        for q in queries:
            data = epmc_search(q)
            results = data.get("resultList", {}).get("result", [])
            for rec in results:
                key = rec.get("pmid") or rec.get("doi") or clean(rec.get("title", ""))[:60]
                if not key or key in seen:
                    continue
                seen[key] = {
                    "modality": modality,
                    "also_modalities": "related_disease",
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
            sys.stderr.write(f"related {modality}: '{q[:55]}' -> {len(results)}\n")

    with open(OUT, "w") as f:
        json.dump(list(seen.values()), f, indent=1)
    print(f"added {added} related-disease records; total {len(seen)}")


if __name__ == "__main__":
    main()
