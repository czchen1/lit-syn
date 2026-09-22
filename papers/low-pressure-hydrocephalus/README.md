# Low-/negative-pressure hydrocephalus (LPH / NegPH) literature

Curated collection and written review of **low-pressure, very-low-pressure and
negative-pressure hydrocephalus** — symptomatic, progressive ventriculomegaly with
normal, low (≤ 5 cm H₂O / ≤ 70 mm H₂O) or sub-atmospheric intracranial pressure,
usually in previously shunted or recently operated patients, refractory to
conventional shunt revision and responding to titrated "sub-zero" external
drainage, restoration of ventricular–subarachnoid communication (ETV) or
low-resistance CSF diversion.

Because the entity is rare (~200 published cases pooled across the systematic
reviews) the collection **deliberately keeps case reports and small series** —
they carry most of the ICP-titration and mechanistic detail — and adds five
supporting axes: brain biomechanics/compliance, drainage-and-valve technique,
aetiological settings (trauma, craniectomy, SAH, tumour, infection), adjacent
differentials (slit-ventricle syndrome, overdrainage, intracranial hypotension,
venous overdrainage), and the pre-1994 European usage of "low-pressure
hydrocephalus" as a synonym for normal-pressure hydrocephalus, which is kept
separate so it is not conflated with the modern syndrome.

## Directory structure
- `index.tsv` — curated metadata, one row per paper. Columns: `axis` (primary
  bucket, see below), `evidence` (systematic_review, consensus_guideline, review,
  case_series, case_series_or_cohort, case_report, clinical_or_mechanistic_study,
  imaging_physiology_study, experimental, computational_model, comment_letter),
  `population` (adult/pediatric/mixed/unspecified), `settings` and `treatments`
  (multi-label `;`-separated tags), `names_entity` (yes if the LPH/NegPH label
  appears in title/abstract), authors, title, venue, year, cited (Europe PMC
  citation count), pmid, doi, pmcid, url, `local_fulltext`, `status`
  (`oa_xml` mirrored / `oa_unavailable` PMCID but no XML / `metadata_only`).
- `curated.json` — same records with abstracts, keywords and MeSH.
- `notes/` — the written synthesis:
  - `00_overview.md` executive summary and ten take-home points
  - `01_history_nomenclature.md` LPH-as-NPH → Pang & Altschuler 1994 → NegPH/VLPH/SILPAH/ALPH
  - `02_pathophysiology.md` viscoelastic, poroelastic, transmantle, venous, pulsatility models
  - `03_etiologies_and_settings.md` precipitants, pooled-series frequencies, paediatric vs adult
  - `04_diagnosis.md` phenotype, ICP measurement pitfalls, imaging, differential diagnosis
  - `05_management.md` acute algorithm (sink control, adjuncts, sub-zero EVD, ETV), definitive hardware, refractory disease
  - `06_outcomes_and_evidence_gaps.md` outcomes, prognostic factors, evidence quality, research agenda
  - `07_key_papers.md` per-paper extractions for the ~35 papers that carry the field
- `REPORT.md` — **auto-generated** consolidated report: corpus statistics and
  per-axis paper listings computed from `index.tsv`, with the notes merged in
  as the synthesis section.
- `REVIEW.pdf` — `REPORT.md` rendered to PDF.
- `fulltext/` — mirrored open-access full-text XML from Europe PMC (32 papers).
- `harvest.py`, `curate.py`, `fetch_fulltext.py`, `gen_report.py`, `build_pdf.py`
  — reproducible pipeline; `raw_harvest.json` + `harvest.log` are provenance.

## Axes (primary bucket)
| axis | n | content |
|---|---|---|
| `core_lph` | 79 | the entity itself: case reports/series, systematic reviews, consensus, mechanistic papers about LPH/NegPH |
| `mechanism_biomechanics` | 50 | brain compliance, elastance, PVI, viscoelastic/poroelastic models, MR elastography, venous physiology |
| `treatment_techniques` | 30 | EVD weaning/titration, valve and anti-siphon technology, shunt-testing laboratories |
| `etiology_settings` | 14 | hydrocephalus after trauma, craniectomy/cranioplasty, SAH, posterior-fossa tumour, infection |
| `adjacent_differentials` | 30 | slit-ventricle syndrome, overdrainage, intracranial hypotension, lumbo-ventricular gradients |
| `historical_lph_as_nph` | 28 | 1969–1990s papers using "low-pressure hydrocephalus" for Adams–Hakim NPH |

## Method
1. `harvest.py` — 6 query domains, 21 compound queries, each run over all years
   and again restricted to recent years, against the Europe PMC REST search API
   (`resultType=core`, cited-count order, cursor pagination): 1,190 unique
   records. Zero-hit first pages are retried because the API
   intermittently returns empty results for valid queries.
2. `curate.py` — regex vocabulary over title + abstract + MeSH. A record enters
   the core axis if it names the entity or describes the phenomenon
   (ventriculomegaly + patent shunt/low ICP + clinical deterioration); supporting
   axes require a mechanistic, technical, aetiological or differential-diagnosis
   hook in a ventricular/CSF context. Errata, incidental mentions and unrelated
   "negative pressure" (wound therapy, ventilation) records are dropped.
   Evidence class, population and multi-label setting/treatment tags are
   assigned from the same text. Each axis is capped by a relevance score; the
   core axis is never capped. `MANUAL_AXIS` records the paper-by-paper review
   that followed the vocabulary pass: mis-bucketed core records are re-homed or
   dropped, and supporting records cited in `notes/` are pinned so a cap cannot
   remove them.
3. `fetch_fulltext.py` — Europe PMC `fullTextXML` for every row with a PMCID,
   core axis first (32 retrieved, 18 PMCIDs without OA XML).
4. `gen_report.py` → `REPORT.md`; `build_pdf.py` → `REVIEW.pdf`.

## Caveats
- Axis, evidence and tag assignment are title/abstract-level heuristics plus
  one manual pass; treat them as navigation aids.
- The evidence base itself is almost entirely case reports and small
  retrospective series; no comparative trial exists. Quantitative statements in
  the notes are taken from abstracts or from the mirrored full texts (marked
  `FT` in `07_key_papers.md`) and are cited by PMID so they can be checked.
- PMID 39760505 is discussed in `03_etiologies_and_settings.md` as an example
  of an incidental report and is intentionally **not** in the curated corpus.
- Nothing here is patient-specific advice.
