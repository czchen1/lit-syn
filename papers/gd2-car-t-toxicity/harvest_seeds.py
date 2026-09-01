#!/usr/bin/env python3
"""Seed pass: guarantee landmark GD2 CAR-T / locoregional CNS cell-therapy records.

The broad harvest is recall-driven and page-capped, so the papers the synthesis is
built on are fetched by identifier and merged into raw_harvest.json. Also runs
narrow queries for material the domain queries under-retrieve (early GD2-CAR
neuroblastoma trials, TIAN, IEC-HS, ICAHT, ICV device complications, and
inflammation-driven CYP suppression).
"""
import json
import sys
import time

from harvest import clean, epmc_search

OUT = "/home/ubuntu/repos/lit-syn/papers/gd2-car-t-toxicity/raw_harvest.json"

# Landmark records, fetched by title. Titles rather than PMIDs: identifiers recalled
# from memory resolve to the wrong article often enough to poison the index, whereas a
# title query either matches the intended paper or returns nothing.
SEED_TITLES = [
    "GD2-CAR T cell therapy for H3K27M-mutated diffuse midline gliomas",
    "Intravenous and intracranial GD2-CAR T cells for H3K27M+ diffuse midline gliomas",
    "GD2-CART01 for Relapsed or Refractory High-Risk Neuroblastoma",
    "Antitumor activity and long-term fate of chimeric antigen receptor-positive T cells in patients with neuroblastoma",
    "Virus-specific T cells engineered to coexpress tumor-specific receptors",
    "Antitumour activity without on-target off-tumour toxicity of GD2-chimeric antigen receptor T cells in patients with neuroblastoma",
    "Anti-GD2 CAR-NKT cells in patients with relapsed or refractory neuroblastoma",
    "Anti-GD2 CAR-NKT cells in relapsed or refractory neuroblastoma",
    "High-Affinity GD2-Specific CAR T Cells Induce Fatal Encephalitis in a Preclinical Neuroblastoma Model",
    "Potent antitumor efficacy of anti-GD2 CAR T cells in H3-K27M+ diffuse midline gliomas",
    "Intracerebroventricular B7-H3-targeting CAR T cells for diffuse intrinsic pontine glioma",
    "Intracerebroventricular B7-H3-targeting CAR T cells for non-pontine diffuse midline glioma",
    "Locoregional infusion of HER2-specific CAR T cells in children and young adults with recurrent or refractory CNS tumors",
    "Intraventricular CARv3-TEAM-E T Cells in Recurrent Glioblastoma",
    "Intrathecal bivalent CAR T cells targeting EGFR and IL13Ra2 in recurrent glioblastoma",
    "Regression of Glioblastoma after Chimeric Antigen Receptor T-Cell Therapy",
    "Tumor inflammation-associated neurotoxicity",
    "ASTCT Consensus Grading for Cytokine Release Syndrome and Neurologic Toxicity Associated with Immune Effector Cells",
    "Chimeric antigen receptor T-cell therapy - assessment and management of toxicities",
    "Endothelial Activation and Blood-Brain Barrier Disruption in Neurotoxicity after Adoptive Immunotherapy with CD19 CAR-T Cells",
    "Monocyte-derived IL-1 and IL-6 are differentially required for cytokine-release syndrome and neurotoxicity due to CAR T cells",
    "CAR T cell-induced cytokine release syndrome is mediated by macrophages and abated by IL-1 blockade",
    "Immune Effector Cell-Associated Hemophagocytic Lymphohistiocytosis-Like Syndrome",
    "Consensus grading and management of immune effector cell-associated hematotoxicity",
    "CAR-HEMATOTOX: a model for CAR T-cell-related hematologic toxicity in relapsed/refractory large B-cell lymphoma",
    "Disease-Drug Interaction of Sarilumab and Simvastatin in Patients with Rheumatoid Arthritis",
    "Regulation of drug-metabolizing enzymes and transporters in inflammation",
    "Impact of inflammation on cytochromes P450 activity in pediatrics",
    "Effect of interleukin-6 receptor inhibition on CYP3A4 activity",
]

EXTRA_QUERIES = {
    "gd2_cart_core": [
        '"GD2" AND ("CAR T" OR "chimeric antigen receptor") AND (neuroblastoma) AND '
        '(trial OR patients) AND (toxicity OR safety OR "adverse events")',
        '"GD2" AND "CAR" AND ("osteosarcoma" OR "Ewing sarcoma" OR "melanoma" OR '
        '"small cell lung") AND (safety OR toxicity)',
        '"GD2" AND ("CAR T" OR "chimeric antigen receptor") AND ("bone marrow" OR '
        '"hematologic toxicity" OR "prolonged cytopenia")',
        '"anti-GD2" AND (pain OR neuropathy OR "capillary leak" OR hyponatremia OR '
        '"transaminase" OR hepatic) AND (children OR patients)',
    ],
    "icv_locoregional_cns": [
        '("tumor inflammation-associated neurotoxicity" OR "tumour inflammation-associated '
        'neurotoxicity" OR TIAN)',
        '("Ommaya" OR "ventricular reservoir" OR "ventricular access device") AND '
        '(infection OR complication OR catheter OR malposition OR h?emorrhage)',
        '("intraventricular" OR "intracerebroventricular") AND ("CAR T" OR "CAR-T") AND '
        '("cerebrospinal fluid" AND (cytokine OR pleocytosis OR protein))',
        '"CAR T" AND ("cerebrospinal fluid" cytokines OR "CSF cytokine") AND (neurotoxicity OR TIAN OR inflammation)',
        '("diffuse midline glioma" OR DIPG OR "H3K27M") AND ("CAR T" OR "chimeric antigen receptor") AND (toxicity OR safety OR neurologic)',
    ],
    "neurotoxicity": [
        '("intracranial pressure" OR hydrocephalus OR "cerebral edema") AND ("CAR T" OR '
        '"immune effector cell") AND (management OR monitoring OR treatment)',
        '"GD2" AND (brain OR CNS OR "central nervous system") AND expression AND (normal OR healthy OR neuron OR astrocyte)',
    ],
    "drug_interaction_pk": [
        '("interleukin-6" OR IL-6) AND ("CYP3A4" OR "cytochrome P450") AND (suppression OR downregulation OR "loss of activity")',
        '("cytokine release syndrome" OR "CAR T") AND ("tacrolimus" OR "cyclosporine" OR '
        '"voriconazole" OR "phenytoin" OR "warfarin" OR "methotrexate") AND (level OR clearance OR interaction OR toxicity)',
        '"disease-drug interaction" AND (inflammation OR cytokine OR "acute phase")',
        '("CAR T" OR "chimeric antigen receptor") AND (hepatic OR renal) AND ("dose modification" OR "dose adjustment" OR "organ dysfunction") AND (chemotherapy OR "supportive care" OR antibiotics)',
    ],
    "preclinical_toxicity": [
        '"GD2" AND CAR AND ("humanized mouse" OR "immunocompetent" OR "syngeneic") AND (toxicity OR "on-target")',
        '"GD2" AND ("ganglioside expression" OR immunohistochemistry) AND ("peripheral nerve" OR "dorsal root" OR skin OR brain)',
    ],
}


def main():
    with open(OUT) as f:
        existing = json.load(f)
    seen = {}
    for rec in existing:
        key = rec.get("pmid") or rec.get("doi") or rec.get("title")
        seen[key] = rec
    before = len(seen)

    def add(rec, domain):
        key = rec.get("pmid") or rec.get("doi") or rec.get("id")
        if not key:
            return
        if key in seen:
            return
        seen[key] = {
            "domain": domain,
            "also_domains": "",
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
            "pubType": "|".join(rec.get("pubTypeList", {}).get("pubType", [])),
            "src": rec.get("source", ""),
            "seed": True,
        }

    # landmark seeds, by title
    for t in SEED_TITLES:
        q = 'TITLE:"%s"' % t.replace('"', '')
        res = epmc_search(q, page_size=25, max_pages=1)
        if not res:
            sys.stderr.write(f"seed MISS: {t[:60]}\n")
        for rec in res:
            add(rec, "seed")
        time.sleep(0.34)

    for domain, queries in EXTRA_QUERIES.items():
        for q in queries:
            res = epmc_search(q, page_size=100, max_pages=4)
            sys.stderr.write(f"{domain}: '{q[:60]}' -> {len(res)}\n")
            for rec in res:
                add(rec, domain)
            time.sleep(0.34)

    out = list(seen.values())
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1)
    print(f"raw_harvest: {before} -> {len(out)}")


if __name__ == "__main__":
    main()
