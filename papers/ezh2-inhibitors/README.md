# EZH2 inhibitor literature — preclinical & clinical

Curated, **compound-organized** literature on small-molecule inhibitors of
**EZH2** (and dual **EZH1/2** inhibitors, plus allosteric **EED** inhibitors that
block the same PRC2 complex). Built to answer three questions, per request:
**potency**, **BBB penetration**, and **the data** (preclinical + clinical).

Angle for this repo: EZH2/PRC2 is a central epigenetic node in the CNS tumors
tracked here (H3K27M DMG/DIPG, H3G34 glioma, SMARCB1-loss ATRT/rhabdoid), so the
notes foreground **whether each agent reaches brain at a target-engaging free
concentration**, not just enzyme potency.

## Directory structure
- `index.tsv` — curated metadata. `category` = **compound/bucket**. Columns:
  category, authors, title, venue, year, pmid, doi, pmcid, url, local_fulltext,
  supp_pdf, topics, status.
- `notes/` — the synthesis (read these):
  - `00_overview.md` — landscape table, corpus stats, five takeaways.
  - `01_potency_selectivity.md` — biochemical/cellular potency, PRC2 mechanism, EZH1/2 vs EED selectivity.
  - `02_bbb_penetration.md` — CNS exposure per agent, P-gp/BCRP efflux, intracranial efficacy.
  - `03_clinical_data.md` — approvals, trials, response rates, safety.
  - `04_preclinical_efficacy_and_combinations.md` — synthetic lethality, models, combos, resistance.
- `REPORT.md` — auto-generated paper listings grouped by compound (`✓FT` = full text mirrored).
- `fulltext/` — mirrored open-access full-text XML (Europe PMC).
- `harvest.py`, `curate.py`, `fetch_fulltext.py`, `gen_report.py` — reproducible pipeline.
- `raw_harvest.json` — unfiltered Europe PMC harvest (provenance).

## Compound buckets (12)
Tazemetostat (EPZ-6438) · Valemetostat (DS-3201, dual EZH1/2) · Tulmimetostat
(CPI-0209)/CPI-1205 · Mevrometostat (PF-06821497) · SHR2554 · GSK126/GSK343 ·
EPZ005687/EI1/EPZ011989 · UNC1999/EED226 (dual & allosteric) · DZNep ·
CNS/BBB & brain tumors · resistance/selectivity/SAR & degraders ·
combinations & clinical.

## Method & caveats
Papers were harvested from Europe PMC per compound and per theme, filtered to
genuine EZH2/PRC2-inhibitor records, and assigned to one bucket (named agent >
theme). Thin drug buckets (CPI-0209, PF-06821497) reflect how often the drug name
appears in *titles* — both are clinically important and are covered in the notes.
Potency values in the notes are canonical first-disclosure/characterization
figures (assay conditions differ; biochemical Ki/IC50 and cellular EC50 are not
directly comparable). BBB claims are flagged where **quantitative human free-brain
PK (Kp,uu) is not publicly established** — the field's key data gap.
Regenerate any artifact by re-running the scripts in order
(`harvest` → `curate` → `fetch_fulltext` → `gen_report`).
