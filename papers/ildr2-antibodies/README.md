# ILDR2 antibodies literature synthesis

Curated collection of published literature on **antibodies and antibody-derived biologics that target ILDR2** (immunoglobulin-like domain containing receptor 2; gene `ILDR2`/`C1orf32`; aliases LISCH-like, angulin-3), with an emphasis on the molecule's role as a **B7-family immune checkpoint** and the two therapeutic modalities built against it:

1. **ILDR2-Fc fusion proteins** — agonistic decoys that *engage* the inhibitory ILDR2 axis to dampen T-cell responses and induce antigen-specific tolerance (autoimmunity, transplantation).
2. **Antagonist anti-ILDR2 monoclonal antibodies** — most notably **BAY 1905254** (Bayer) — that *block* ILDR2 to relieve T-cell suppression for cancer immunotherapy.

Research/tool monoclonal antibodies raised against ILDR2 / angulin-3 (used to detect the protein in tissue) are also catalogued, along with the target-biology papers needed to understand what these antibodies bind.

## Scope

This collection is centered on ILDR2 as an **antibody target**. Papers are tagged by `relevance`:

- **`core`** — ILDR2-targeting antibodies / Fc biologics and the immune-checkpoint biology that motivates them (T-cell inhibition, B7-family context, immuno-oncology, tolerance).
- **`context`** — ILDR2 target biology required to interpret the antibodies: protein structure/domains, expression, interactome, the tricellular-tight-junction / angulin-3 function, and the original diabetes/metabolism genetics that first defined the gene.

**Excluded** (see `notes/00_overview.md` for the full list): papers about the related but distinct gene **LISCH7 / LSR** (lipolysis-stimulated lipoprotein receptor / angulin-1), and records in which `ILDR2`/`C1orf32` appears only incidentally in a gene list, GWAS table, or omics dataset without being a subject of study.

## Directory structure

- `index.tsv` — curated metadata for all 21 included papers (relevance tier, publication category, topic tags, DOI/PMID/PMCID links, local PDF path, and download status).
- `pdfs/` — open-access PDFs that downloaded cleanly (12 papers).
- `notes/` — synthesis reports (see below).
- `REPORT.md` — single-file consolidated synthesis across the whole corpus.

## Notes index

- `notes/00_overview.md` — the ILDR2 landscape, naming/aliases, corpus counts, identification strategy, and the inclusion/exclusion decisions.
- `notes/01_antibodies_and_biologics.md` — the antibody-centric core: the ILDR2-Fc agonist fusion (Compugen), the BAY 1905254 antagonist mAb (Bayer), and research/tool anti-ILDR2 / anti-angulin-3 monoclonals.
- `notes/02_target_biology.md` — what the antibodies bind: ILDR2 as a B7-like checkpoint, protein domains/paralogs, expression, interactome (GRP78/PDIA1, ZNF70), the angulin-3 / tricellular tight-junction role, and the diabetes/lipid-metabolism origin of the gene.
- `notes/03_per_paper_extractions.md` — capsule summary per included paper.

## Identification strategy

Seventeen complementary PubMed E-utils queries were combined and deduplicated, covering the gene symbol and every alias plus the antibody/checkpoint angle:

1. `ILDR2`
2. `"immunoglobulin-like domain containing receptor 2"` (and the unhyphenated variant)
3. `LISCH-like`
4. `LISCH7`
5. `C1orf32`
6. `BAY 1905254`
7. `ILDR2 checkpoint`, `ILDR2 immune`, `ILDR2 antibody`, `ILDR2-Fc`, `ILDR2 T cell`
8. `ILDR2 tumor`, `ILDR2 cancer`, `ILDR2 diabetes`, `ILDR2 tight junction`, `ILDR2 beta cell`

42 unique PubMed records were retrieved. Manual filtering on the title/abstract removed LISCH7/LSR papers (a different gene) and incidental gene-list mentions, leaving **21 ILDR2-relevant papers** (7 `core`, 14 `context`). PMC IDs and DOIs were resolved via the NCBI ID Converter and Europe PMC; open-access PDFs were retrieved from Europe PMC OA, PLOS, Nature, and MDPI (the latter via the Europe PMC render endpoint).

## Download note

12 of 21 papers downloaded cleanly as validated PDFs. The remaining 9 are either genuinely paywalled (AACR `Cancer Immunology Research`, Elsevier, Springer, Yakugaku Zasshi) or freely readable only behind a reCAPTCHA / Cloudflare challenge that blocked automated retrieval from this environment (the two 2018 `J Immunol` papers; `J Cell Sci` 2013). Those rows carry `not_available_oa …` or `free_at_publisher_pmc; blocked_recaptcha` in the `status` column with working DOI/PMID/PMC links, and their findings are captured from the abstracts (and from the two open-access B7-family reviews that summarize them) in the notes.

The BAY 1905254 paper (PMID 32312711) is the single most important "ILDR2 antibody" reference; its main text is paywalled, but its key results are recorded in `notes/01_antibodies_and_biologics.md` from the abstract and from the gastric-cancer B7-family review (PMID 34639059), which reproduces the construct and efficacy summary.
