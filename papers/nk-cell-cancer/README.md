# NK cells for cancer — phenotypes, engineering & manufacturing

Curated literature on what makes an NK-cell cancer therapy effective: the **cell state** infused, the
**genetic engineering** installed, and the **culture / GMP manufacturing process** used to produce it.
Manufacturing and process development are treated as primary evidence, not methodology footnotes.

**313 papers, 1993–2026** (94 from 2024–2026; 166 from 2020 onward), across 14 topic axes and 6 evidence
classes: preclinical 105, process/method 58, clinical trials 50, reviews 39, mechanistic 33, human
translational 28. Open-access full-text XML mirrored for 153 records.

## Directory structure
- `index.tsv` — curated metadata. Columns: axis, evidence, disease, manufacturing, engineered, authors,
  title, venue, year, cited, pmid, doi, pmcid, url, local_fulltext, status.
- `curated.json` — the same corpus with abstracts, for programmatic reading.
- `notes/` — narrative synthesis (read in order):
  - `00_overview.md` — corpus stats, axes, and the ten claims the literature supports
  - `01_phenotypes_and_cell_states.md` — subsets beyond CD56bright/dim, CIML, adaptive NK, dysfunction
  - `02_cell_sources.md` — peripheral blood, cord blood, iPSC, NK-92
  - `03_car_and_receptor_engineering.md` — NK-native CAR architecture, targets, gene delivery, failure modes
  - `04_engagers_and_adcc.md` — BiKE/TriKE/NKCE, AFM13, CD16 shedding, antibody combinations
  - `05_gene_editing_and_brake_removal.md` — CISH, NKG2A, TGF-β/SMAD4, CD38, ADAM17, CRISPR screens
  - `06_cytokine_support_and_armouring.md` — IL-2/IL-15/IL-21/IL-12+15+18, armoured designs
  - `07_expansion_and_gmp_manufacturing.md` — feeders, PM21, media, G-Rex, Prodigy, bioreactors
  - `08_metabolism_persistence_trafficking.md` — metabolic fitness, hypoxia, homing, solid-tumour TME
  - `09_cryopreservation_potency_and_release.md` — cryo damage, DMSO alternatives, potency assays, release
  - `10_clinical_translation_and_gaps.md` — trial-by-trial evidence, ranked efficacy levers, open gaps
- `REPORT.md` — auto-generated paper listing grouped by axis (`✓FT` = local full text). Never hand-edit.
- `nk_cell_cancer_review.pdf` — notes + report rendered as a single review document.
- `fulltext/` — mirrored open-access full-text XML (Europe PMC).
- `harvest.py`, `curate.py`, `fetch_fulltext.py`, `gen_report.py`, `build_pdf.py` — reproducible pipeline.
- `raw_harvest.json`, `harvest.log` — unfiltered harvest and per-query provenance.

## Topic axes (14)
NK phenotypes & states · cell sources · CAR-NK & receptor engineering · NK engagers · gene editing /
brake knockouts · cytokine support & armouring · expansion, feeders & GMP · cryopreservation, potency &
QC · metabolism & persistence · inhibitory receptors & checkpoints · ADCC & combinations · trafficking &
solid-tumour TME · clinical evidence · general NK therapy.

## Method & caveats
Harvested from Europe PMC across three sweeps — modern (2018–2026), recent (2024–2026) and citation-ranked
foundational (all years) — with title/abstract restriction for broad terms; 5,971 unique records deduplicated
by PMID/DOI/EuropePMC ID. Curation removes retractions, comments, editorials, case reports, abstract-less
records, prognostic-signature and bibliometric papers, incidental NK mentions, non-therapeutic ILC2/ILC3
biology and NK/T-cell lymphoma (a malignancy *of* NK lineage, not NK-cell therapy), then classifies each
record by axis and evidence class and selects per-axis quotas favouring recent work while retaining highly
cited foundational studies.

Axis assignment, evidence class, disease tag and manufacturing/engineering flags are **title/abstract-level
heuristics** — useful for navigation, not a substitute for reading the paper. Citation counts are
Europe PMC's and are time-biased against 2025–2026 records. Regenerate any artifact by re-running the
scripts in order (`harvest` → `curate` → `fetch_fulltext` → `gen_report` → `build_pdf`); `build_pdf.py`
requires `markdown` and `weasyprint`.
