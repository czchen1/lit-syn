# GD2 CAR-T toxicity — literature synthesis, with emphasis on intracerebroventricular (ICV) delivery

Curated collection of published literature on **what goes wrong when GD2-directed CAR T cells are
given to patients**, and how the toxicity profile changes when the cells are delivered into the CSF
(intracerebroventricular / intraventricular, via Ommaya or Rickham reservoir) rather than
intravenously.

The organising questions are:

1. What toxicities are actually observed with GD2 CAR-T, clinically and preclinically, and at what
   grade, timing and reversibility?
2. How does the ICV route change that profile — what it removes (systemic CRS, ICANS), what it adds
   (tumour inflammation-associated neurotoxicity, intracranial pressure, hardware), and what it
   leaves unchanged?
3. Which organ-function changes are transient (liver enzymes, creatinine, electrolytes, counts,
   coagulation) and large enough to interact with concomitant drugs and therapies?

## Scope

Included:

- **GD2 CAR-T / CAR-NKT clinical trials** — neuroblastoma, H3K27M-mutant DMG/DIPG, medulloblastoma,
  sarcoma, glioma; autologous, allogeneic, armoured (C7R, IL-15), and iCasp9-equipped products.
- **GD2 preclinical toxicity** — affinity-driven CNS toxicity, brainstem inflammation models,
  on-target/off-tumour biology.
- **Locoregional CNS CAR-T of other targets** (B7-H3, IL13Rα2, EGFR806, HER2, CARv3-TEAM-E) as the
  best available route-specific safety comparator for ICV GD2 CAR-T.
- **General CAR-T toxicity evidence** — CRS, ICANS, IEC-HS/HLH, ICAHT/cytopenias, coagulopathy,
  AKI/electrolytes, hepatic effects, cardiopulmonary events, infection — where it transfers to the
  GD2/ICV setting.
- **Anti-GD2 antibody toxicity** (dinutuximab, naxitamab, hu14.18K322A, 3F8) as the reference
  for what GD2 target engagement does to normal nerve.
- **Inflammation–pharmacokinetics literature** — IL-6/cytokine suppression of drug-metabolising
  enzymes, reversal by IL-6 blockade, critical-illness PK, renal-function effects on lymphodepletion
  dosing — restricted to work that bears on concomitant-medication management.

Excluded: routine population-PK/dosing-optimisation literature for individual antibiotics and ICU
drugs, generic hepatotoxin/nephrotoxin pharmacology, and CAR-T efficacy work with no safety content.

## Directory structure

- `index.tsv` — curated metadata for all **852** records (category, topics, PMID/DOI/PMCID, canonical URL, status).
- `fulltext/` — Europe PMC open-access full-text XML (**502** records) via the EBI REST `fullTextXML` endpoint.
- `notes/` — synthesis notes by toxicity domain (index below).
- `REPORT.md` — cross-domain synthesis: IV vs ICV comparison, evidence grading, drug-interaction implications, monitoring.
- `gd2_cart_toxicity_review.pdf` — standalone review (report + all notes + full reference list), built by `build_pdf.py`.
- `harvest.py`, `harvest_seeds.py` — Europe PMC harvest scripts (domain queries + landmark title seeds).
- `curate.py` — scoring/classification/deduplication, writes `index.tsv` and `curated.json`.
- `fetch_fulltext.py` — full-text XML retrieval, updates `index.tsv`.
- `extract.py` — prints article text, or only toxicity-relevant paragraphs/tables, from the downloaded XML.
- `raw_harvest.json` — deduplicated raw harvest (**13,060** records) before curation.

## Notes index

- `notes/00_overview.md` — why the question is route-specific; toxicity taxonomy (CRS / ICANS / TIAN / IEC-HS / ICAHT / on-target off-tumour); how to read the evidence.
- `notes/01_gd2_clinical_toxicity.md` — every GD2 CAR-T/CAR-NKT clinical dataset, with observed toxicity, grades and management.
- `notes/02_preclinical_and_on_target_off_tumor.md` — affinity/architecture-driven CNS toxicity, brainstem models, nerve GD2 expression, antibody-derived pain signal.
- `notes/03_icv_route_and_tian.md` — the ICV route: what it changes, TIAN, intracranial pressure, hydrocephalus, hardware, comparator locoregional trials.
- `notes/04_crs_ics_hlh.md` — CRS and IEC-HS/HLH: mechanism, grading, incidence in GD2 products, anti-cytokine therapy.
- `notes/05_organ_function_hepatic_renal_heme.md` — transient hepatic, renal/electrolyte, haematologic and coagulation changes: magnitude, timing, reversibility.
- `notes/06_drug_interactions_and_pk.md` — inflammation- and cytokine-blockade-mediated changes in drug metabolism and clearance; concrete concomitant-drug implications.
- `notes/07_monitoring_and_mitigation.md` — monitoring schedule, thresholds, engineering/dosing mitigations, iCasp9, and what remains unproven.
- `notes/08_microglia_myeloid_axis.md` — CSF myeloid/microglial states by route, CCL2/TNF/IL-10 correlates of TIAN, amplifier-vs-target framing.
- `notes/10_icv_without_lymphodepletion.md` — what omitting conditioning changes: compartment dosing vs expansion, measured CSF CAR detection, dose density, hardware dependence, unmeasured anti-CAR immunity.
- `notes/09_resistance_and_failure_modes.md` — efficacy ceiling, pre-infusion attrition, exhaustion/persistence, compartmental (delivery) failure, antigen density, MDSC/TME suppression, and toxicity management that defeats efficacy.

## Identification strategy

Europe PMC REST `search` (core results, cursor pagination, throttled), two passes:

1. `harvest.py` — 10 domain query groups: GD2 CAR-T clinical core; ICV/locoregional CNS delivery;
   CRS; neurotoxicity/ICANS; hepatic; renal/electrolyte; haematologic/coagulation; cardiopulmonary;
   drug interactions/PK; preclinical toxicity; toxicity mitigation and engineering.
2. `harvest_seeds.py` — landmark-title seeding (exact `TITLE:` queries) plus narrow follow-up
   queries for topics the broad passes under-retrieve (TIAN, ASTCT grading, IL-1/IL-6 CRS mechanism,
   inflammation–CYP work).

PMID-list seeding was deliberately **not** used: recalled identifiers resolved to unrelated
articles on validation, so all seeds are resolved by title search and verified against the returned
metadata.

## Curation

`curate.py` scores each record on GD2 specificity, CAR-T context, toxicity vocabulary, CNS route,
and evidence type; deduplicates on normalised title preferring the journal version over preprints
and abstracts; and assigns one primary `category` plus multiple `topics`. Pharmacology records are
held to a stricter rule (title-level drug-metabolism/interaction terminology *and* an
inflammation/immunotherapy context) because the naive query returns large volumes of unrelated ICU
population-PK work.

Primary categories: `gd2_cart_clinical`, `gd2_cart_preclinical`, `cns_locoregional_delivery`,
`neurotoxicity`, `cytokine_release_syndrome`, `hlh_mas`, `on_target_off_tumor`, `hepatic`,
`renal_electrolyte`, `hematologic_coagulopathy`, `cardiopulmonary`, `infection_immune`,
`drug_interaction_pk`, `steroids_immunomodulation`, `mitigation_engineering`, `grading_management`.

Because one paper usually spans several domains, `topics` (not `category`) is the right field to
filter on: e.g. 34 records carry `icv_intraventricular`, 104 carry `gd2_agent`, 376 carry
`organ_function`.

## Reproduce

```bash
python3 harvest.py           # writes raw_harvest.json (+ harvest.log)
python3 harvest_seeds.py     # adds landmark/narrow-topic records
python3 curate.py            # writes index.tsv, curated.json
python3 fetch_fulltext.py    # populates fulltext/, updates index.tsv
python3 extract.py --tox 39537919   # toxicity paragraphs/tables of one record
python3 build_pdf.py         # writes gd2_cart_toxicity_review.pdf
```

`build_pdf.py` needs `markdown` and `weasyprint`.

## Caveat

This is a literature synthesis for research use. Nothing here is individualised clinical advice,
and the GD2 CAR-T clinical evidence base is small (tens of patients per trial, mostly phase 1), so
absolute rates should be read as order-of-magnitude.
