# Immunotherapy resistance: mechanisms in patients, and how the TME is measured

## The mechanistic taxonomy the corpus supports

**Adaptive (IFN-γ-induced) resistance.** PD-L1 is expressed at sites of active immune
attack (PMID 12091876, PMID 22461641) and PD-1 blockade works by releasing that brake
(PMID 25428505). This is the resistance that immunotherapy already treats.

**Oncogene-driven immune evasion.** PTEN loss increases PD-L1 and confers
immunoresistance in glioma (PMID 17159987) and promotes resistance to T-cell-mediated
therapy in melanoma (PMID 26645196); EGFR activation engages the PD-1 axis in lung
tumours (PMID 24078774); β-catenin activation drives anti-PD-1 resistance in HCC
(PMID 31186238); ZEB1 promotes immune escape in melanoma (PMID 35288462); TGF-β drives
evasion in reconstituted colorectal metastasis (PMID 29443964).

**Hard genetic escape.** Acquired-resistance mutations in melanoma including B2M loss
(PMID 27433843) and JAK1/2 loss (see notes/08) — the subset least likely to be rescued by
TME modulation.

**Metabolic/epigenetic escape.** H3K18 lactylation potentiates immune escape in NSCLC
(PMID 39137401) with ACSS2 identified as a lactyl-CoA synthetase coupling KAT2A to
histone lactylation (PMID 39561764) — a mechanism that ties nutrient state directly to
chromatin-level immune evasion. Mitochondrial transfer from tumour to T cells is a newer
route (PMID 39843734).

**Host and organ context.** Gut bacterial composition drives primary resistance in RCC
(PMID 32376136); NASH-associated liver biology limits anti-tumour surveillance in
immunotherapy-treated HCC (PMID 33762733) — resistance determined outside the tumour
altogether.

**Programme-level exclusion.** T-cell exclusion is encoded as a cancer-cell programme
(PMID 30388455) and as an inferable signature of dysfunction/exclusion predicting
response (PMID 30127393); a pan-cancer T-cell atlas links a stress-response state to
resistance (PMID 37248301). The therapeutic framing — hot, altered, cold — comes from
PMID 30610226, and low-dose radiotherapy reversing immune desertification
(PMID 34479871) is the corpus's proof that "cold" is a modifiable state.

## Measurement: what makes axis selection possible

Spatial and single-cell profiling moved from atlases (breast, PMID 30982598; GBM
progression, PMID 35624211) to therapy-linked inference: spatial multi-omics of
immunotherapy efficacy in advanced NSCLC (PMID 36854570), ecosystem dynamics under
neoadjuvant chemo-immunotherapy in oesophageal cancer (PMID 36921563), an anti-PD-1-treated
NSCLC single-cell atlas (PMID 40147443), pan-cancer stromal target discovery
(PMID 38225927), conserved CAF spatial subtypes (PMID 40154487), and TIM-3 nominated
from lung adenocarcinoma precursors (PMID 40345189). Multi-omic ML predictors of therapy
response exist (PMID 34875674) but are single-cohort.

## The practical conclusion

Resistance mechanisms are heterogeneous *within* histology, and most of the reversible
ones are TME-level. That argues for assigning a TME axis per patient — myeloid-high,
stroma-excluded, metabolically suppressed, presentation-deficient — using the profiling
tools above, rather than combining agents by tumour type. No trial in this corpus
allocates therapy that way; that gap is the most consistent unmet need across all 19 axes.
