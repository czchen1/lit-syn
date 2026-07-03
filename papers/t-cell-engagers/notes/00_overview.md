# T-cell engagers (TCE) and combined CAR-T × TCE — literature synthesis

Scope: CD3-redirecting T-cell engagers (bispecific/trispecific antibodies, BiTE®,
DART, tandem diabody, trifunctional/Triomab, ImmTAC/TCR-based) and genuine
**CAR-T × TCE combinations** (CAR-T cells engineered to secrete or co-deliver a
T-cell engager). Organized **by target antigen**. Deliberately includes early
preclinical/foundational work (back to 1986) and is not US-centric — European and
Chinese programs are represented throughout.

## Corpus at a glance
- **264 papers** across **19 target buckets** (`index.tsv`).
- Years **1986–2026**: 36 pre-2010, 32 in 2010–2019, 196 in 2020+.
- **58** flagged `preclinical_or_early` (pre-2016).
- **132** open-access full texts mirrored locally under `fulltext/` (`✓FT` in `REPORT.md`).
- Geographic footprint (best-effort from author affiliations; papers can count in
  more than one region): **Europe 174, US 156, China 60**. Europe is the single
  largest bloc, reflecting the field's European origins.

## How it was built
`harvest.py` queries Europe PMC per target (multiple query strings each), then
`curate.py` (a) keeps only genuine CD3/T-cell-engager records — bare "bispecific
antibody" hits without T-cell/CD3 context, bispecific ADCs, and PD-1×VEGF-type
bispecifics are dropped; (b) assigns each paper to a single target bucket by
antigen/agent name, routing target-agnostic platform/reviews to
`foundational_platform` and CAR-T-that-secrete-engagers to `cart_tce_combination`;
(c) preferentially retains early/preclinical papers and guarantees European and
Chinese representation where available. `fetch_fulltext.py` mirrors OA XML.
Assignments are title/abstract-level heuristics — treat bucket edges as fuzzy.

## Foundational thread (target-agnostic)
The concept predates the CAR-T era. **Staerz & Bevan (1986)** built a hybrid
hybridoma producing a bispecific mAb that "focuses" effector T-cell activity onto
targets — the seed of the whole field. Through the 1990s, mostly **European**
(Groningen/Kroesen, Milan/Canevari–Mezzanzanica, Brussels/Demanet) and US groups
(Lum's armed activated T cells) explored anti-CD3 × anti-tumor bispecifics,
tandem diabodies (Kipriyanov 1999), and CD28 co-stimulatory retargeting
(Grosse-Hovest 1999). These established the mechanics — MHC-independent
polyclonal T-cell redirection, the importance of format/half-life, and the
cytokine-release liability — that modern engineered formats refine.

## Clinically de-risked anchors, by origin
- **CD19 — blinatumomab**: the CD19×CD3 BiTE from **Micromet (Munich, Germany)**,
  later Amgen; first-in-class approval for R/R B-ALL. The reference proof that a
  short-half-life TCE can drive deep responses.
- **EpCAM — catumaxomab**: EpCAM×CD3 **trifunctional Triomab** from **Trion Pharma
  (Germany)**; the first approved bispecific (EU, malignant ascites). Solitomab
  (MT110/AMG 110) extended EpCAM to a BiTE format.
- **gp100 — tebentafusp**: a soluble **TCR-based ImmTAC** from **Immunocore (UK)** —
  the first TCR-format TCE and the first therapy to extend survival in metastatic
  uveal melanoma. Demonstrates targeting of intracellular/HLA-presented antigens.
- **DLL3 — tarlatamab (AMG 757)**: half-life-extended BiTE; the breakout solid-tumor
  (SCLC/neuroendocrine) TCE. The DLL3 bucket is dominated by 2025–2026 real-world
  and management literature, signaling clinical maturation.
- **Heme multi-target**: CD20 (glofitamab/mosunetuzumab — **Roche, Switzerland**;
  epcoritamab — **Genmab, Denmark**), BCMA (teclistamab, elranatamab; AMG 420 as the
  early BCMA BiTE), GPRC5D (talquetamab), and myeloid CD33/FLT3/CD123
  (flotetuzumab, vibecotamab, AMG 330/673).

## Solid-tumor targets and the barriers
CEA/CEACAM5 (cibisatamab/CEA-TCB, **Roche**; a deep early diabody/pretargeting
literature from Italian and Dutch groups), PSMA (pasotuxizumab/AMG 212 from
**Bayer/Amgen**, acapatamab, HPN424), HER2 (ertumaxomab trifunctional; newer
HER2-low-selective designs), EGFR/EGFRvIII, B7-H3, GD2, mesothelin/MUC16/MUC1/PSCA,
and a broader ROR1/5T4/CD70/HER3/TROP2/FAP bucket. Recurring themes: on-target
off-tumor toxicity, poor T-cell infiltration, antigen heterogeneity/escape, and
the immunosuppressive microenvironment — motivating 4-1BB-conditional designs,
affinity tuning to widen the therapeutic window, trispecifics, and combinations.

## Chinese efforts
Concentrated but substantial, and strongest in **Claudin-18.2** (the most active
Chinese TCE target): IBI389 (**Innovent**), DR30318 (trispecific), AHT-102, Q-1802,
alongside givastomig (CLDN18.2×4-1BB) and AMG 910. Chinese groups also contribute
heavily to the CAR-T × TCE combination literature (below) and to CLDN18.2,
GPRC5D, and BCMA construct engineering. See `topics` `geo:China` tags in `index.tsv`.

## Combined CAR-T × T-cell engager
`cart_tce_combination` captures the genuine "armored/secreting" strategy — CAR-T
cells engineered to secrete a TCE so the graft continuously seeds bystander
T-cell redirection and counters antigen escape. Examples in-corpus: **B7-H3 CAR-T
secreting an EGFR TCE for glioblastoma**, GPC3 CAR-T secreting a B7-H3 BiTE (HCC),
Mesothelin CAR-T secreting anti-FAP/CD3 (pancreatic stroma) or NKG2D-BiTEs (TNBC),
CD22 CAR-T secreting a CD19 TCE (B-ALL), CD70 CAR-T secreting anti-CD33/CD3 (AML),
Muc16 CAR-T secreting a WT1 TCE (ovarian), and CD3ε-nanobody-engineered EVs that
generate TCE-secreting CAR-T in vivo. Rationale across these: dual-antigen
coverage to blunt escape, and local TCE delivery to limit systemic toxicity. The
related **STAb-T** concept (secreting-T-cell, from Álvarez-Vallina's Spanish group)
is tagged in the platform/combination material.

## Glioma relevance (ties to the DHG-H3G34 target work)
Four buckets overlap directly with the lab's CAR-T/radioligand target list for
DHG-H3G34: **EGFRvIII** (AMG 596 BiTE; Roche EGFRvIII×CD3 first-in-human GBM;
IL13Rα2×EGFRvIII trispecific), **B7-H3/CD276**, **GD2**, and **DLL3**. The
EGFRvIII and B7-H3-CAR-secreting-EGFR-TCE entries are the most CNS-relevant and
worth reading first for a glioma T-cell-engager strategy.

## Files
- `index.tsv` — curated metadata; `category` = target, `topics` carries
  `geo:*`, era, and `review` tags, `status`/`local_fulltext` track OA + mirror.
- `REPORT.md` — auto-generated paper listings grouped by target.
- `fulltext/` — mirrored OA full-text XML.
- `harvest.py` / `curate.py` / `fetch_fulltext.py` / `gen_report.py` — reproducible pipeline.
- `raw_harvest.json` — unfiltered Europe PMC harvest (provenance for re-curation).
