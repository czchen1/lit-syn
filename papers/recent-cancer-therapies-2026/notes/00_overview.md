# 00 — Overview: cancer therapy publications, 2026-03-09 → 2026-09-09

## What this collection is

A **broad, reproducible six-month sweep of the cancer-therapy literature** — clinical *and* preclinical — rather than a hand-picked bibliography. Europe PMC (MEDLINE + PMC + preprint servers) was queried across 26 therapeutic modality groups, clinical-trial vocabulary, preclinical-model vocabulary, high-impact venues, and pediatric/CNS disease areas; ~99k unique records in the window were reduced by scripted curation to the therapy-focused corpus indexed in `index.tsv`. Every count in these notes is derived from that index, so the whole thing can be regenerated with `harvest.py` → `curate.py` → `fetch_fulltext.py`.

The organising axes are:

- **modality** (`category`, 26 buckets, one primary per paper; secondary modalities appear in `topics` as `also:<bucket>`),
- **evidence level** (`evidence`: `clinical_phase3` / `clinical_phase2` / `clinical_phase1` / `clinical_other` / `evidence_synthesis` / `preclinical`),
- **venue tier** (`tier`: 1 = Nature/NEJM/Lancet/JAMA-family and the top specialty journals, 2 = strong specialty journals, 3 = everything else, including preprints).

`REPORT.md` is the consolidated cross-modality synthesis; the numbered notes below go modality by modality. Counts quoted in the notes come from the final curation run recorded in `README.md`.

## What the six months look like

Four things dominate this window:

1. **Immunotherapy is now the largest single block of clinical activity.** Checkpoint blockade alone is the biggest modality bucket, and its centre of gravity has moved from "does PD-(L)1 work in advanced disease" to (a) perioperative/neoadjuvant use, (b) fixed-duration and de-escalation questions, (c) next-generation combinations (TIGIT, LAG-3, CD40, adenosine-axis, PD-1×VEGF bispecifics), and (d) mechanistic dissection of resistance in on-treatment human samples.
2. **T-cell redirection has become routine clinical practice, not a frontier.** CAR-T and T-cell engagers together contribute a large share of the phase 1–3 reports, with the interesting questions now being earlier lines (smouldering myeloma, first-line DLBCL/FL), fixed-duration schedules, dual-antigen products, allogeneic/off-the-shelf and *in vivo*-generated CARs, and long-horizon safety (second primary malignancies, decade-long persistence).
3. **Payload and radiation chemistry keeps expanding.** ADCs (new targets: B7-H3, SEZ6, nectin-4, ADAM9, PMEL), radioligand therapy (¹⁷⁷Lu, ²²⁵Ac, ¹⁶¹Tb, BNCT), and physical/ablative approaches make up a large preclinical mass with a thin but real clinical edge.
4. **Preclinical work is overwhelmingly about combination and resistance mechanism, not new monotherapy.** Roughly half the corpus is preclinical, and the recurring structure is: identify a resistance node in a human dataset → validate in mouse/organoid/PDX → combine with an approved backbone (checkpoint blockade, chemotherapy, radiation, or a kinase inhibitor).

## Notes index

- `01_cell_therapy_and_transplant.md` — CAR-T/NK/macrophage, TIL and TCR-T, allogeneic and *in vivo* CAR, HCT conditioning and post-transplant strategies.
- `02_engagers_and_antibodies.md` — bispecific/trispecific T-cell engagers, PD-1×VEGF and other bifunctional antibodies, naked monoclonals.
- `03_antibody_drug_conjugates.md` — approved-ADC optimisation and the new-target/new-payload wave.
- `04_checkpoint_blockade_and_immunomodulation.md` — PD-(L)1/CTLA-4 practice-changing trials, next-gen checkpoints, cytokine/innate agonists, TME and metabolic immuno-modulation.
- `05_vaccines_oncolytics_microbiome.md` — neoantigen/mRNA/DC vaccines, oncolytic viruses and engineered bacteria, microbiome interventions.
- `06_targeted_small_molecules.md` — kinase inhibitors, RAS/MAPK, hematologic targeted agents, DDR, degraders, epigenetic drugs, endocrine therapy.
- `07_radiation_radiopharmaceuticals_ablation.md` — external-beam trials, protons, adaptive/MR-guided RT, radioligand therapy, ablation and energy-based therapy.
- `08_rna_gene_therapy_and_delivery.md` — mRNA/siRNA/ASO/CRISPR therapeutics and the nanomedicine delivery layer.
- `09_chemotherapy_tme_and_repurposing.md` — cytotoxic backbones, locoregional chemotherapy, ctDNA-guided escalation/de-escalation, metabolic and stromal targeting, drug repurposing.
- `10_methods_limitations_and_caveats.md` — how the corpus was built, what the classifier does well and badly, and how to use it safely.

## Conventions

- Papers are cited as *Title-fragment* with a **PMID** in parentheses; `index.tsv` holds the canonical DOI/PMID/PMCID and a resolvable URL for every row.
- Dates in the notes are the Europe PMC first-publication date (`date`), which is what the window filter uses.
- `status` is `fulltext_xml` where Europe PMC open-access XML was mirrored into `fulltext/`, otherwise `metadata_only` (index row + abstract-level synthesis, with working links).
- Preprints are retained and tagged `preprint` in `topics`; they are not peer-reviewed and are deliberately down-weighted in prioritisation.
