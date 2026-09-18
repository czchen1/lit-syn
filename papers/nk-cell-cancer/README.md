# NK cells for cancer: what makes a good product

Curated literature read from a **product point of view**: which scientific and manufacturing advances change a
design decision, which failure modes destroy products, and where the evidence supports a real choice versus
only an option. Manufacturing and process development are treated as primary evidence, not methodology
footnotes.

The central claim the corpus supports: **NK therapy's unsolved problem is potency-duration, not target
recognition** — preclinical CAR-NK relapse was metabolic collapse rather than antigen escape (PMID 37494448),
and cryopreserved product loses tissue-relevant killing while passing standard release assays (PMID 33067467).

**313 papers, 1993–2026** (94 from 2024–2026; 166 from 2020 onward), across 14 topic axes and 6 evidence
classes: preclinical 105, process/method 58, clinical trials 50, reviews 39, mechanistic 33, human
translational 28. Open-access full-text XML mirrored for 153 records.

## Directory structure
- `index.tsv` — curated metadata. Columns: axis, evidence, disease, manufacturing, engineered, authors,
  title, venue, year, cited, pmid, doi, pmcid, url, local_fulltext, status.
- `curated.json` — the same corpus with abstracts, for programmatic reading.
- `notes/` — the argument (read in order):
  - `00_thesis_and_decision_frame.md` — the central claim, the five levers ranked, what not to fund
  - `01_scientific_advances.md` — advances tiered by whether they change a design decision
  - `02_manufacturing_advances.md` — process advances with yield numbers; the comparison nobody has run
  - `03_failure_modes.md` — eight failure modes ranked, with mechanism and mitigation
  - `04_design_decisions.md` — six decisions, the case for each option, and what tips it
  - `05_potency_and_release.md` — why standard release testing misses potency, and what to measure
  - `06_clinical_evidence_and_open_questions.md` — trial anchors, unresolved questions, what would change the
    argument
  - `07_case_snk01_vs_mcenk.md` — two autologous products (NKGen SNK01, ImmunityBio M-ceNK) read protocol by
    protocol: culture method, target phenotype markers, release testing, and the opposite bets they make
- `REPORT.md` — auto-generated paper listing grouped by axis (`✓FT` = local full text). Never hand-edit.
- `nk_cell_cancer_review.pdf` — notes + report rendered as a single review document.
- `fulltext/` — mirrored open-access full-text XML (Europe PMC).
- `harvest.py`, `curate.py`, `fetch_fulltext.py`, `gen_report.py`, `build_pdf.py` — reproducible pipeline.
- `raw_harvest.json`, `harvest.log` — unfiltered harvest and per-query provenance.

## Topic axes (14) — the index organisation, not the argument's structure
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
