# DNA vaccines for glioblastoma — literature synthesis

Curated collection of published literature on **DNA (plasmid / nucleic-acid) vaccines for glioblastoma and other gliomas**, with a focus on **vaccine antigen choice, plasmid/vector design, delivery and adjuvant strategy, and translation toward the clinic**.

## Scope

This collection is restricted to studies in which a **nucleic-acid construct (plasmid DNA, naked DNA, DNA-launched alphavirus replicon, or DNA delivered by a live bacterial vector) is administered as a vaccine/immunization to raise an antigen- or antigen-target-specific immune response against glioma/glioblastoma**. This includes:

- antigen-encoding DNA vaccines (e.g. TRP-2, gp100, SOX6, EphA2, HCMV antigens, personalized neoantigens);
- anti-angiogenic DNA vaccines that immunize against tumor-vasculature self-antigens (VEGFR2/flk-1);
- DNA vaccines combined with immune-checkpoint blockade, cytokines, or immunogenic-cell-death chemotherapy;
- live-bacterial-vectored delivery of vaccine-antigen plasmids;
- reviews and clinical reports centered on DNA/nucleic-acid vaccines for GBM.

**Explicitly excluded** (documented in `notes/04_excluded_and_adjacent.md`): non-immunizing gene therapy (cytokine/suicide-gene transgene delivery), gene-modified whole-tumor-cell vaccines, dendritic-cell vaccines transfected ex vivo with mRNA, recombinant-protein or viral-vectored (poxvirus/MVA) vaccines, tumor-lysate nanovaccines, and the large background of papers that merely use a plasmid as a laboratory tool (transfection, cloning, reporters, shRNA/siRNA, CRISPR, tumor modeling) with no vaccination intent.

## Directory structure

- `index.tsv` — curated paper metadata for all 21 in-scope papers, with topic tags, download status, and DOI/PMID/PMCID links.
- `pdfs/` — full-text PDFs of main texts (9 papers: 8 via Europe PMC OA + the Garfinkle 2026 *Nature Cancer* trial provided directly).
- `notes/` — synthesis reports organized by topic.

## Notes index

- `notes/00_overview.md` — landscape, eras, antigen/platform taxonomy, paper counts, and triage decisions.
- `notes/01_antigen_dna_vaccines.md` — antigen-encoding DNA vaccines: target antigens, plasmid/epitope design (incl. the pTOP VSV-G epitope-carrier and the UNITE/LAMP1 platform), and reported immunogenicity/efficacy.
- `notes/02_antiangiogenic_and_vectored.md` — VEGFR2/flk-1 anti-angiogenic DNA vaccines, oral attenuated-*Salmonella* and *Pseudomonas*-TTSS live-vector delivery.
- `notes/03_clinical_translation_and_delivery.md` — the GNOS-PV01 (GT-20) personalized neoantigen DNA-vaccine phase 1 trial, the SCIB1 ImmunoBody, electroporation and combination strategies, and where the field stands clinically.
- `notes/04_excluded_and_adjacent.md` — explicit record of borderline and excluded records and the rationale for each, so the scope is reproducible.

## Identification strategy

Four complementary PubMed E-utils queries were combined and deduplicated:

1. `("DNA vaccine" OR "DNA vaccination" OR "DNA-based vaccine" OR "plasmid DNA vaccine" OR "plasmid vaccine" OR "naked DNA vaccine" OR "nucleic acid vaccine" OR "gene vaccine" OR "DNA immunization" OR "DNA immunisation") AND (glioblastoma OR glioma OR GBM OR "high-grade glioma" OR "malignant glioma" OR astrocytoma)`
2. `(plasmid[tiab] AND (vaccine OR immunization OR immunisation OR vaccination)) AND (glioblastoma OR glioma)`
3. `("DNA vaccine" OR "DNA vaccination" OR "DNA immunization") AND ("brain tumor" OR "brain tumour" OR "brain cancer" OR neuro-oncology)`
4. `(EGFRvIII OR "EGFR variant III" OR survivin OR "tumor associated antigen") AND ("DNA vaccine" OR "DNA vaccination" OR "plasmid vaccine") AND (glioma OR glioblastoma OR brain)`

**80 unique candidate records** were retrieved (1991–2026). Manual abstract triage removed 59 records that use a plasmid only as a tool, are non-immunizing gene therapy, or are other vaccine modalities (see `notes/04`), leaving **21 in-scope DNA-vaccine papers**. DOIs and PMCIDs were re-extracted from each article's own `PubmedData/ArticleIdList` (the first automated pass had picked up reference-list DOIs). PDFs were retrieved from **Europe PMC OA** (`europepmc.org/articles/PMC…?pdf=render`); 8 of 21 are open access, plus the Garfinkle 2026 *Nature Cancer* trial full text (provided directly) for **9** with PDFs. The remaining 12 are paywalled or not in PMC and are marked `not_available_oa` with a resolvable DOI link.

## Status legend (`status` column)

- `oa_pdf` — open-access PDF downloaded to `pdfs/`.
- `not_available_oa` — no open-access full text located; DOI/PMID link provided for manual retrieval.
