# Vδ1 γδ T-cell purity, double-negative phenotype, and E:T 10:1 cytotoxicity benchmarks

Fresh literature search (Europe PMC, not derived from the existing lit-syn γδ collection) assembled to benchmark a specific in-house result — a ~80% Vδ1 γδ T-cell product with a CD4−CD8− double-negative population, assayed for cytotoxicity at an E:T ratio of 10:1 — against published γδ T-cell product composition and killing data.

## Read this first

`notes/gdt_vd1_benchmark_report.md` — the comparison itself: Vδ1 purity benchmarks, why the double-negative fraction is expected rather than distinguishing, published % killing at E:T 10:1, the confounders that make 10:1 numbers non-comparable across papers, and the specific values still needed to close the comparison.

## Directory structure

- `harvest.py` → `raw_harvest.json` — Europe PMC search across 7 query groups (Vδ1/DOT products, expansion protocols, phenotype/subsets, cytotoxicity with explicit E:T ratios, engineered γδ, clinical translation, comparator/assay methodology). 6,878 unique records.
- `curate.py` → `index.tsv`, `curated.json` — regex scoring for γδ identity, Vδ1/DOT specificity, CD4−CD8− DN signal, quantitative anchors (percentages, `n:1` ratios, fold expansion, EC50/IC50) and oncology/product context; off-topic infectious/inflammatory γδ biology is filtered out. 288 records kept.
- `fetch_fulltext.py` → `fulltext/` — Europe PMC open-access full-text XML (153 downloaded, 46 indexed records had no OA full text).
- `extract_benchmarks.py` → `benchmarks.tsv` — 762 candidate quantitative sentences from 113 papers, classified `et` (E:T-linked killing), `purity` (product composition), `dn` (double-negative phenotype), pulled from paragraphs, figure captions, and tables.

`raw_harvest.json`, `harvest.log`, and `fulltext/` are gitignored (~35 MB); regenerate with `python3 harvest.py && python3 curate.py && python3 fetch_fulltext.py && python3 extract_benchmarks.py`.

## Scope notes

Records span 1992–2026, weighted to 2020+ (102 records) and 2025+ (67). Curation deliberately separates categories that are frequently conflated when benchmarking:

- Vδ1-specific products vs Vγ9Vδ2 products vs bulk/polyclonal γδ.
- Expanded/manufactured products vs freshly isolated or tissue-derived cells.
- Vδ1 purity vs total TCRγδ+ purity.
- CD4−CD8− γδ cells vs CD3+CD4−CD8− "DNT cell" therapy products (which contain αβ T cells).
- Direct % lysis/killing at a stated E:T ratio vs qualitative or figure-only cytotoxicity claims.
- Tumor-target assay results vs non-cancer disease-state observations.
