# 10 — Methods, limitations, and caveats

## 1. Pipeline

```
harvest.py        Europe PMC REST search, FIRST_PDATE:[2026-03-09 TO 2026-09-09],
                  SRC in {MED, PMC, PPR}; 67 compound queries across 20 modality
                  groups, trial vocabulary, preclinical-model vocabulary, 58
                  high-impact venues, pediatric + CNS disease terms. Cursor pagination, 500/page,
                  up to 16 pages per query. Output: raw_harvest.json (~99k unique
                  records), harvest.log (per-query counts and overlap).
curate.py         Rule-based curation → index.tsv + curated.json.
fetch_fulltext.py Europe PMC fullTextXML for prioritised PMCID-bearing rows → fulltext/.
build_pdf.py      REPORT.md + notes/ + grouped reference appendix → PDF.
```

No API key, no manual editing of the data files. Re-running the three data scripts regenerates everything; the only drift will come from Europe PMC indexing new items into the window (typically back-filled MEDLINE records) and from journals correcting metadata.

## 2. What the curation rules do

Applied in order to each harvested record:

1. **Publication-type and title exclusions** — errata, editorials, letters, protocols, case reports, guidelines, reviews (with the exception below), cost-effectiveness, bibliometrics, nursing/psychosocial, screening/epidemiology, prognostic-signature/bioinformatics, diagnostic imaging/radiomics, supportive-care and toxicity-management studies, surgical-technique comparisons, trial-methodology papers, veterinary and non-cancer disease contexts. ~42k records removed here.
2. **Cancer context** — a cancer term in the title, or ≥3 in the abstract. ~21k removed.
3. **Therapy context** — a therapy term in the title, or ≥4 in the abstract. ~7.6k removed.
4. **Evidence level** — explicit phase in title/abstract (phase 3 checked before generic "randomised"), then strong clinical markers (trial registry ID, enrolment/ORR/DLT/RP2D language), then observational human studies (`clinical_other`), meta-analyses/systematic reviews (`evidence_synthesis`), and preclinical models. Medicinal-chemistry papers that mention comparator agents' clinical phase are forced to preclinical. Records with no evidence signal are dropped.
5. **Observational and generic-modality tightening** — `clinical_other`/`evidence_synthesis` rows must have a therapy term *in the title*; `other_therapy` (catch-all modality) rows must name a concrete agent class in the title unless preclinical.
6. **Primary modality** — 26 buckets scored on title (weighted) + abstract; ties broken by a fixed priority order that favours the more specific bucket (e.g. `bispecific_tce` over `antibody_other`, `radiopharm` over `radiotherapy`).
7. **Disease tags, in-vivo flag, preprint flag** → `topics`.
8. **Venue tier** from a curated journal list after stripping Europe PMC suffixes (": official journal of…", "(London, England)", leading "The").
9. **Deduplication** on normalised title (preferring the MEDLINE record over the preprint, and the record with a PMID) and then on DOI (keeping the earlier-dated record).

## 3. Known weaknesses

- **Recall vs precision.** The pipeline was tuned by iterative spot-checking of high-visibility strata (tier 1–2, phase 1–3, `other_therapy`). Precision in `clinical_other` and tier-3 preclinical is lower; expect residual supportive-care, prognostic, and surgical papers, especially when a title contains "treatment" or "therapy" generically. Conversely, some genuine therapy papers were removed by broad exclusions (e.g. neurocognitive-protection RCTs during cranial RT, "late effects" trials, "reconstruction"-titled studies).
- **Phase assignment is regex-based.** "Phase 3" in an abstract that *cites* a phase 3 trial can promote a secondary analysis or a real-world cohort to `clinical_phase3`. Long-term follow-ups and subgroup analyses of completed trials are therefore over-represented in the phase buckets relative to primary readouts. Use the title to confirm.
- **Single primary modality.** Combination trials (e.g. ADC + checkpoint, RT + immunotherapy, kinase inhibitor + chemotherapy) are filed under one bucket; the other appears only as `also:<bucket>` in `topics` when it is in the title. Counting by `category` therefore undercounts combinations.
- **Tier is venue, not quality.** It is a triage aid. Preprints are tier 3 by construction.
- **Date is Europe PMC `firstPublicationDate`.** Online-first and issue dates can differ by months; a small number of records first indexed in the window were published earlier in print, and some March 2026 online-first papers are missing because their first-publication date predates the window.
- **Europe PMC coverage.** MEDLINE + PMC + indexed preprint servers (bioRxiv, medRxiv, Research Square, Preprints.org, Authorea, F1000). Not covered: conference abstracts (ASCO/ESMO/AACR/ASH 2026 abstracts are absent unless published as papers), Embase-only journals, Chinese-language journals not in MEDLINE, and grey literature/press releases. This biases the corpus toward journal publication of trials rather than first disclosure.
- **Abstract-only classification.** All 18.4k records were classified from title + abstract; ~9.7k lack a PMCID at all. The 648 full-text XML files cover only the phase 1–3 trial reports with a PMCID (811 eligible, 700 attempted under the file cap, 52 not open-access at Europe PMC). Tier 1–2 preclinical rows were eligible in principle but fell below the cap; raise `MAX_FILES` in `fetch_fulltext.py` to extend coverage.
- **No manual adjudication of every row.** 18k rows were not read individually. The notes cite only records whose title and abstract were checked; the appendix in the PDF omits tier-3 preclinical and tier-3 `clinical_other` rows.

## 4. Preprints

~1.3k records (7%) are preprints (`src = PPR`, tagged `preprint`). They are kept because for preclinical and some early clinical work the preprint is the only record in the window. They are not peer-reviewed, may never be, and several already have a journal version outside the window that the title-dedup could not match. Treat them as leads.

## 5. Safe use

- For "what changed clinically in the last six months": filter `evidence in {clinical_phase3, clinical_phase2}` and `tier in {1, 2}`; ~600 rows; read titles, then the cited notes.
- For "what is the preclinical field doing in modality X": filter `category = X`, `evidence = preclinical`, and sort by `tier`; skim titles; the `in_vivo` topic separates model-based work from in-vitro-only.
- Do not use the corpus for treatment decisions; it is a literature index, not a guideline, and it contains negative trials, retracted-later preprints, and low-quality cohorts by design.
- Verify any claim in the notes against the linked record before quoting it; the notes summarise abstracts, not full results, and outcome claims are only as good as the abstract wording.
