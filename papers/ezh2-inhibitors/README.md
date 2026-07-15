# EZH2 inhibitors: preclinical and clinical literature

Curated papers on EZH2 (and dual EZH1/2) inhibition in cancer, spanning foundational PRC2/EZH2 biology, preclinical mechanism/combination studies, and clinical trials (including the FDA-approved indications). Emphasis on histone-mutant pediatric glioma and other CNS tumors given the broader repository focus on H3-mutant diffuse hemispheric/midline glioma.

## Directory structure

- `index.tsv` — curated paper metadata, topic categories, and download status.
- `notes/ezh2_inhibitors_synthesis.md` — synthesis of the drug class, clinical status, and biology relevant to H3-mutant glioma.
- `pdfs/` — downloaded open-access PDFs (see download note below).

## `index.tsv` columns

`category`, `authors`, `title`, `venue`, `year`, `doi`, `url`, `local_pdf`, `notes`.

## Category tags

- `foundational_biology` — EZH2/PRC2 biology, oncogenic mutations, H3K27me3.
- `preclinical_mechanism` — mechanistic proof-of-concept for EZH2 inhibition.
- `clinical_trial` / `clinical_trial_approval` — human trials; `_approval` marks the pivotal studies underpinning FDA approvals.
- `preclinical_prostate`, `preclinical_sclc`, `preclinical_glioma`, `preclinical_medulloblastoma` — indication-specific preclinical work.
- `immuno_combination` — EZH2i + immunotherapy.
- `resistance` — resistance mechanisms and combination strategies to overcome them.
- `review` — reviews / meta-analyses.

## Scope & selection notes

Selected from PubMed relevance searches (Jul 2026) across queries for tazemetostat, valemetostat, SHR2554, HH2853, mevrometostat, and mechanism/resistance/combination terms. The pool was large (hundreds of hits); this is a curated, not exhaustive, set biased toward (1) landmark biology, (2) registration-enabling clinical trials, and (3) CNS/pediatric-glioma relevance.

**Caveat on EZH2 in glioma:** EZH2 is oncogenic in most contexts (basis for inhibitor development), but at least one study reports a context-dependent *tumor-suppressor* role in diffuse midline glioma (see `35395831`). Interpret EZH2i rationale in H3-mutant glioma with this nuance.

## Download note

Metadata is verified against PubMed (PMIDs in the `url` column). Open-access PDF retrieval was attempted; rows without a committed PDF are marked `no_open_pdf_added` or `download_blocked; see URL`. Access full text via the DOI/PubMed link.
