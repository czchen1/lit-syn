# Recent cancer therapy publications — clinical and preclinical, 2026-03-09 → 2026-09-09

A broad, reproducible six-month sweep of the cancer-therapy literature, clinical **and** preclinical, built from Europe PMC (MEDLINE + PMC + preprint servers). The aim is coverage rather than selection: every record in the window that describes a therapeutic intervention for cancer with an identifiable evidence level is indexed, classified by modality / evidence level / venue tier, and — for the trial subset — mirrored as open-access full text. The synthesis notes then read *across* the corpus by modality.

## Scope

Included: any primary research record, meta-analysis or systematic review whose title/abstract describes a **cancer therapy** (drug, biologic, cell, gene/RNA, radiation, radioligand, physical/ablative, microbiome, transplant, or delivery system) with **clinical** (phase 1–3 trial, other human interventional/observational treatment study) or **preclinical** (cell line, organoid, PDX, GEMM, in-vivo model) evidence, first published 2026-03-09 through 2026-09-09.

Excluded by rule: errata, editorials, letters, protocols, case reports, guidelines, narrative reviews, cost-effectiveness, bibliometrics, nursing/psychosocial/quality-of-life-only studies, screening/epidemiology, prognostic-signature/bioinformatics-only papers, diagnostic imaging/radiomics, supportive-care and toxicity-management studies, surgical-technique comparisons, trial-methodology papers, veterinary and non-cancer disease contexts. See `notes/10_methods_limitations_and_caveats.md` for the full rule set and its failure modes.

## Directory structure

- `index.tsv` — one row per record, **18,424** rows: `category`, `evidence`, `tier`, `authors`, `title`, `venue`, `date`, `year`, `pmid`, `doi`, `pmcid`, `url`, `fulltext_xml`, `topics`, `status`.
- `curated.json` — same records with abstracts and the raw classification fields (`src`, `priority`, disease tags), for re-analysis.
- `fulltext/` — Europe PMC full-text XML for **648** phase 1–3 trial reports (EBI REST `fullTextXML`).
- `notes/` — modality-by-modality synthesis (`00`–`10`, index below).
- `REPORT.md` — consolidated cross-modality synthesis.
- `recent_cancer_therapies_2026_review.pdf` — REPORT + notes + grouped reference appendix (tier 1–2 rows and all trial rows).
- `harvest.py`, `curate.py`, `fetch_fulltext.py`, `build_pdf.py` — the pipeline; `harvest.log`, `curate.log`, `fetch.log` — run logs.
- `raw_harvest.json` (~220 MB, **not committed**) — the 98,991 unique harvested records; regenerate with `harvest.py`.

## Notes index

- `notes/00_overview.md` — what the collection is, the three organising axes, the four themes of the window, conventions.
- `notes/01_cell_therapy_and_transplant.md` — CAR-T/NK/macrophage, TIL and TCR-T, allogeneic and *in vivo* CAR, resistance and safety, HCT conditioning and GVHD prophylaxis.
- `notes/02_engagers_and_antibodies.md` — PD-1×VEGF and other bifunctionals, CD3 engagers in lymphoma/myeloma/solid tumours, costimulatory bispecifics, naked monoclonals.
- `notes/03_antibody_drug_conjugates.md` — deruxtecan-class optimisation and combinations, new targets (B7-H3, SEZ6, nectin-4, ADAM9, PMEL, IL1RAP), resistance, linker/payload chemistry.
- `notes/04_checkpoint_blockade_and_immunomodulation.md` — perioperative and advanced-disease PD-(L)1 trials, next-generation checkpoints, CD40/adenosine/4-1BB agonists, cytokine localisation, TME and metabolic immunomodulation, resistance biology.
- `notes/05_vaccines_oncolytics_microbiome.md` — personalised neoantigen and mutant-KRAS vaccines, pediatric vaccines, oncolytic viruses and engineered bacteria, FMT and microbial metabolites.
- `notes/06_targeted_small_molecules.md` — RAS/MAPK (pan-RAS, G12C/G12D), EGFR/ALK/ROS1/MET and other kinase inhibitors, CDK4/6, hematologic targeted agents, DDR (PARP/ATR/WEE1), degraders, epigenetic drugs, endocrine therapy.
- `notes/07_radiation_radiopharmaceuticals_ablation.md` — external-beam trials (hypofractionation, brain metastases, prostate, rectal, breast, H&N, lung, CNS, sarcoma), PSMA/SSTR/FAP radioligands and alpha emitters, ablation, electroporation, photodynamic and fluorescence-guided approaches.
- `notes/08_rna_gene_therapy_and_delivery.md` — mRNA/aptamer/CRISPR therapeutics, gene-modified cell products, liposomal and microsphere chemotherapy, extrahepatic LNP targeting, biomimetic carriers.
- `notes/09_chemotherapy_tme_and_repurposing.md` — cytotoxic regimen optimisation and ctDNA-guided (de)escalation, locoregional chemotherapy, stromal/metabolic targeting, drug repurposing.
- `notes/10_methods_limitations_and_caveats.md` — pipeline, curation rules, known weaknesses, preprint policy, safe use.

## Identification strategy

**Harvest** (`harvest.py`). Europe PMC REST `search` with `FIRST_PDATE:[2026-03-09 TO 2026-09-09] AND (SRC:MED OR SRC:PMC OR SRC:PPR)` conjoined with 67 compound queries in 24 groups: 20 modality groups (CAR-T/NK/M, TCR-T/TIL, bispecific engagers, ADCs, checkpoint blockade, cancer vaccines, oncolytic viruses, RAS/MAPK, kinase inhibitors, DDR, hematologic targeted agents, degraders, epigenetics, radiopharmaceuticals/radiotherapy, RNA/gene therapy, cytokine/innate agonists, naked antibodies, chemotherapy, endocrine therapy, nanomedicine, TME/metabolic/microbiome), plus clinical-trial vocabulary sweeps (phase 1/2/3, randomised, first-in-human, NCT identifiers), preclinical-model sweeps (xenograft, PDX, organoid, syngeneic, GEMM), 58 high-impact venues, and pediatric + CNS disease sweeps. Cursor pagination, 500 records/page, ≤16 pages/query. **98,991** unique records.

**Curation** (`curate.py`). Publication-type and title exclusions → cancer-context test → therapy-context test → evidence-level assignment (explicit phase > trial-registry/enrolment/ORR/DLT markers > observational human > meta-analysis/systematic review > preclinical model) → title-level therapy requirement for observational/synthesis rows → primary modality (26 buckets, title-weighted scoring with specificity-ordered tie-break) → disease/in-vivo/preprint tags → venue tier (curated journal list) → dedup on normalised title and on DOI. **18,424** records retained.

**Full text** (`fetch_fulltext.py`). PMCID-bearing rows ranked trials-first then by tier, capped at 700 attempts; Europe PMC `fullTextXML` mirrored where open access. **648** `fulltext_xml`, 52 unavailable, remaining rows `metadata_only` with a resolvable PMC/DOI/PubMed URL. Only the phase 1–3 subset fell inside the cap.

## Final counts

| axis | value | n |
|---|---|---|
| evidence | preclinical | 10,017 |
| | clinical_other | 5,623 |
| | clinical_phase2 | 930 |
| | clinical_phase3 | 739 |
| | clinical_phase1 | 379 |
| | evidence_synthesis | 736 |
| tier | 1 / 2 / 3 | 566 / 3,672 / 14,186 |
| source | MEDLINE / preprint | 17,137 / 1,287 |
| full text | fulltext_xml / metadata_only | 648 / 17,776 |

Modality (`category`): checkpoint 2,200 · chemo_conventional 2,075 · targeted_kinase 1,731 · tme_metabolic 1,341 · radiotherapy 1,247 · targeted_heme 955 · physical_ablative 953 · targeted_ras_mapk 793 · cytokine_innate 762 · nanomedicine_delivery 760 · rna_gene_therapy 737 · cell_therapy 734 · endocrine 491 · targeted_ddr 478 · radiopharm 457 · epigenetic 444 · adc 428 · transplant 320 · bispecific_tce 284 · repurposed 252 · antibody_other 224 · cancer_vaccine 190 · oncolytic_virus 164 · other_therapy 145 · microbiome 133 · degrader 126.

## Conventions

- `evidence` — `clinical_phase3` / `clinical_phase2` / `clinical_phase1` (explicit phase or strong trial markers), `clinical_other` (human treatment studies without a phase: cohorts, real-world, secondary analyses, single-arm without phase label), `evidence_synthesis` (meta-analysis / systematic review), `preclinical`.
- `tier` — 1: NEJM, Lancet family, JAMA family, Nature family, Cell, Science, Cancer Cell, Cancer Discovery, JCO, Annals of Oncology, Blood, Lancet Oncology/Haematology, etc.; 2: strong specialty journals (Clin Cancer Res, Cancer Res, JITC, Leukemia, Eur J Cancer, Radiother Oncol, JNCI, …); 3: all others including preprints. Venue, not quality.
- `topics` — `;`-separated disease tags (`gi`, `lung`, `breast`, `gu`, `cns`, `heme_*`, `pediatric`, …), context tags (`combination`, `resistance`, `perioperative`, `first_line`, `relapsed_refractory`, `safety`, `in_vivo`), `preprint`, and secondary modalities as `also:<bucket>`.
- `status` — `fulltext_xml` (Europe PMC XML in `fulltext/`) or `metadata_only`.
- Notes cite records by title fragment + **PMID**; every cited PMID resolves to a row in `index.tsv`.
- Preprints are retained, tagged, and down-weighted in the notes; they are not peer-reviewed.

## Regenerating

```
pip install markdown weasyprint
python3 harvest.py          # ~99k records, writes raw_harvest.json + harvest.log
python3 curate.py           # index.tsv + curated.json + curate.log
python3 fetch_fulltext.py   # optional arg: file cap (default 700)
python3 build_pdf.py
```
