# T-cell engager (TCE) & combined CAR-T × TCE literature

Curated, **target-organized** literature on CD3-redirecting T-cell engagers
(bispecific/trispecific antibodies, BiTE®, DART, tandem diabody, trifunctional
Triomab, ImmTAC/TCR-based) and genuine **CAR-T × TCE combinations** (CAR-T cells
engineered to secrete/co-deliver a T-cell engager).

Emphasis, per request: **early preclinical/foundational work is included** (back to
1986), and the collection is **not US-centric** — European and Chinese programs are
represented throughout.

## Directory structure
- `index.tsv` — curated metadata. `category` = **target antigen** (primary
  organization). Columns: category, authors, title, venue, year, pmid, doi,
  pmcid, url, local_fulltext, supp_pdf, topics, status.
- `notes/00_overview.md` — synthesis: corpus stats, geography, foundational
  thread, clinical anchors by origin, Chinese efforts, CAR-T × TCE combinations,
  and glioma relevance.
- `REPORT.md` — auto-generated paper listings grouped by target (with `[geo]`
  tags and `✓FT` for locally mirrored open-access full text).
- `fulltext/` — mirrored open-access full-text XML (Europe PMC).
- `harvest.py`, `curate.py`, `fetch_fulltext.py`, `gen_report.py` — reproducible pipeline.
- `raw_harvest.json` — unfiltered Europe PMC harvest (provenance).

## Target buckets (19)
Foundational/platform · CD19 · CD20 · BCMA · GPRC5D · CD33/FLT3/CD123 · EpCAM ·
CEA/CEACAM5 · gp100 (ImmTAC) · PSMA · HER2 · EGFR/EGFRvIII · DLL3 · B7-H3/CD276 ·
GD2 · Claudin-18.2 · Mesothelin/MUC16/MUC1/PSCA · other solid-tumor targets ·
combined CAR-T × TCE.

## Method & caveats
Papers were harvested from Europe PMC per target, filtered to genuine
CD3/T-cell-engager records (bispecific ADCs and non-CD3 bispecifics such as
PD-1×VEGF are excluded), assigned to one target bucket by antigen/agent name, and
selected to preferentially retain early/preclinical work and ensure European +
Chinese coverage. Bucket assignment and geography tags are **title/abstract-level
heuristics** — useful for navigation, not a substitute for reading. Regenerate any
artifact by re-running the scripts in order (`harvest` → `curate` →
`fetch_fulltext` → `gen_report`).
