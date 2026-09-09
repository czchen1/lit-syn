# TME modulation in solid tumours and immunotherapy-resistant tumours

Reproducible literature collection on modulating the tumour microenvironment (TME) in
solid tumours, with emphasis on primary and acquired resistance to immunotherapy.

- **Corpus**: 16,224 unique Europe PMC records harvested; 261 curated across 19 axes.
- **Coverage**: 2002–2026; 71 clinical trials, 23 human translational, 70 reviews/evidence
  syntheses, 97 preclinical/mechanistic; 120 records explicitly about resistance,
  immune exclusion or cold-tumour biology.
- **Full text**: 112 open-access Europe PMC XML files mirrored under `fulltext/`.
- **Deliverable**: `tme_modulation_solid_tumors_review.pdf` (synthesis notes + evidence listing).

## Layout

| Path | Contents |
| --- | --- |
| `harvest.py` | Europe PMC harvest across 23 thematic query groups × 3 date sweeps |
| `check_queries.py` | Dry-run hit counts per query (query-selectivity check, no records fetched) |
| `raw_harvest.json`, `harvest.log` | Raw harvest and per-query provenance |
| `curate.py` | Filtering, deduplication, axis/evidence/disease/resistance classification |
| `curated.json`, `index.tsv` | Curated records (JSON and machine-readable TSV index) |
| `fetch_fulltext.py`, `fulltext/` | Open-access full-text XML for priority records |
| `gen_report.py`, `REPORT.md` | Auto-generated per-axis evidence listing |
| `notes/` | Narrative synthesis: `00_overview.md` plus 13 axis-group notes |
| `build_pdf.py` | Renders notes + REPORT.md to the combined review PDF |

## Search strategy

Source: Europe PMC REST (`/search`), no API key required. 23 thematic query groups —
myeloid, suppressive lymphoid, CAF/ECM, vasculature/hypoxia, metabolism, innate agonists,
engineered cytokines, trafficking/TLS, antigen presentation/IFN, clinical resistance,
epigenetic priming, radiation/chemotherapy priming, intratumoral/oncolytic, microbiome,
TME-directed delivery, cell therapy, physical modulation, spatial profiling, cold-tumour
disease contexts (PDAC/GI, CNS, other), general TME modulation, and a high-impact journal
sweep.

Every clause is field-restricted to `TITLE`/`ABSTRACT`. This matters: Europe PMC's default
field searches the *full text* of OA articles, so an unrestricted `"macrophage"` clause
returned ~82,000 records for a single query. Broad concepts are additionally
title-anchored, and compound terms (`"a & b"`) are expanded into explicit co-occurrence
(`(TITLE:a OR ABSTRACT:a) AND (TITLE:b OR ABSTRACT:b)`). Field restriction alone reduced
the overlapping modern-hit estimate from ~1.46M to ~152k.

Each query runs against three sweeps, ranked by citation count (`sort=CITED desc`):

| Sweep | Window | Pages × 100 | Rationale |
| --- | --- | --- | --- |
| `modern` | 2015-01-01 – 2026-12-31 | 3 | current mechanism and trial literature |
| `recent` | 2024-01-01 – 2026-12-31 | 2 | offsets citation lag for new work |
| `foundational` | all years | 1 | landmark papers that define each axis |

Pagination uses `cursorMark`; Europe PMC ignores the `page` parameter alongside
`sort=CITED desc` (verified — pages 1–3 returned identical records). Records are
deduplicated on PMID/DOI/Europe PMC id, and a paper matching several query groups keeps
its alternates in `also_domains`.

## Curation rules

Applied in `curate.py` (16,224 raw → 9,725 eligible pool → 261 curated):

- **Dropped**: retractions, comments, editorials, case reports, study protocols;
  prognostic-signature and bioinformatics-only papers; broad disease primers and
  disease-name-only titles; haematology-only records; records with no TME or
  immune-response vocabulary in title/abstract; abstracts under 200 characters;
  pre-1990 records.
- **Axis assignment**: title keyword hits weighted 3×, abstract hits 1×. A record with no
  title-level hit is treated as cross-cutting and routed to `general_tme_modulation`,
  which itself requires an immune/TME concept in the title. The harvest domain is kept
  when it is a credible runner-up, so a record stays with the query that found it.
- **Evidence level**: `clinical_trial`, `systematic_review`, `review`,
  `translational_human`, `preclinical`, `mechanistic`, from publication types plus
  title/abstract cues.
- **Also tagged**: solid-tumour disease context (15 tags, or `pan-solid`),
  resistance relevance (yes/no), venue tier (210 of 261 records are tier-1 venues).
- **Selection**: per-axis quotas (13 per axis; 22 cross-cutting, 18 clinical resistance)
  ranked by citation count, venue tier, evidence level and recency, so each axis has a
  comparable clinical/preclinical/review mix rather than being dominated by whichever
  axis has the largest literature.

## Caveats

- The curated set is a **priority subset**, not an exhaustive export: quotas keep axes
  balanced and the collection readable. The full eligible pool is reproducible from
  `raw_harvest.json` by relaxing `PER_AXIS` in `curate.py`.
- Ranking is citation- and venue-weighted, which favours established work; the `recent`
  sweep and a recency term in the score partly offset this, but 2025–2026 papers are
  still under-weighted relative to their eventual impact.
- Axis assignment is keyword-based. Papers are frequently relevant to several axes;
  only one primary axis is recorded in `index.tsv` (alternates survive as `also_domains`
  in `raw_harvest.json`).
- Hit counts in `harvest.log` are much larger than the number of records fetched: each
  query intentionally contributes only its most-cited slice.
- 149 curated records are metadata-only — either not open access or not in Europe PMC
  full text; `url` always resolves (PMC, then PubMed, then DOI).
- Disease tags come from title/abstract mentions, so a mechanistic paper using one model
  system may be tagged with that disease rather than as pan-solid.

## Regenerate

```bash
cd papers/tme-modulation-solid-tumors
python3 check_queries.py     # optional: per-query hit counts before harvesting
python3 harvest.py           # ~10-15 min, writes raw_harvest.json + harvest.log
python3 curate.py            # writes curated.json + index.tsv
python3 fetch_fulltext.py    # fills fulltext/ and the local_fulltext column
python3 gen_report.py        # writes REPORT.md
python3 build_pdf.py         # writes tme_modulation_solid_tumors_review.pdf
```

Requires `markdown` and `weasyprint` for the PDF step; harvesting and curation use only
the standard library.
