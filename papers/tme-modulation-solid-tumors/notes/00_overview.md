# Overview: what the corpus says about modulating the solid-tumour TME

Scope of the synthesis: 261 curated papers (2002–2026) selected from a 16,224-record
Europe PMC harvest, covering 19 mechanistic/interventional axes. 120 papers explicitly
concern immunotherapy resistance, immune exclusion or cold-tumour biology.

## The organising problem

Checkpoint blockade works where a pre-existing, IFN-γ-driven T-cell response is being
restrained by an adaptive brake. The clinical literature settled that framing early —
PD-L1 is induced by IFN-γ at sites of active immune attack (PMID 22461641), and response
tracks with pre-treatment CD8 infiltration at the invasive margin (PMID 25428505). Every
axis in this corpus is therefore an answer to one of three questions:

1. **No T cells were ever primed** → antigen supply, innate sensing, DC licensing
   (`innate_agonists`, `antigen_presentation_ifn`, `radiation_chemo_priming`,
   `epigenetic_priming`).
2. **T cells exist but cannot reach or persist in the tumour** → stroma, vessels,
   chemokines, metabolism (`caf_stroma_ecm`, `vasculature_hypoxia`, `trafficking_tls`,
   `metabolic_tme`).
3. **T cells arrive and are actively switched off** → myeloid and Treg suppression,
   exhaustion programmes (`myeloid_macrophage`, `treg_suppressive_lymphoid`,
   `cytokine_engineering`).

`clinical_resistance` collects the papers that show which of these actually breaks in
patients; `spatial_profiling` collects the methods that let you tell them apart in a
given tumour.

## Cross-cutting conclusions the corpus supports

- **Resistance is usually TME-level, not antigen-level.** Hard genetic escape does occur
  — JAK1/2 loss (PMID 27903500), B2M/MHC-I loss (PMID 27433843) — but is a minority of
  cases. The larger fraction is potentially reversible suppression: myeloid programmes
  (PMID 39633050), TGF-β-driven exclusion (PMID 29443964), lactate/adenosine metabolism
  (PMID 36859386, PMID 39137401), and cell-intrinsic exclusion programmes (PMID 30388455).
- **Single-agent TME modulation has failed repeatedly at scale; the failures are
  informative.** IDO1 inhibition (ECHO-301, PMID 31221619), stromal hyaluronan depletion,
  and CSF1R monotherapy each validated the target biologically but not clinically. The
  pattern is that depleting one suppressive node is compensated by another, and that
  stromal ablation can be actively harmful (PMID 24856586).
- **Localisation, not novelty, is the dominant engineering theme of the last five years.**
  IL-12, IL-2 and STING agonists were all known to work and all limited by systemic
  toxicity; the productive work is tumour-restricted delivery — intratumoral injection,
  regulated gene therapy (PMID 31413142), immunocytokines, TME-responsive nanocarriers,
  and armoured cell products (PMID 35314843, PMID 38168996).
- **Priming modalities are the most clinically mature TME modulators.** Radiotherapy
  (PMID 30397353, PMID 34479871), chemotherapy-induced immunogenic cell death, epigenetic
  priming (PMID 26317466) and neoantigen vaccines (PMID 37165196, PMID 38246194) all have
  randomised or phase 2 support, and they act on question 1 above rather than trying to
  out-compete the suppressive network.
- **Microbiome modulation is the clearest example of reversing acquired resistance in
  humans.** Two independent FMT trials converted anti-PD-1-refractory melanoma to
  responsive (PMID 33542131, PMID 33303685), now extended to a phase 2 in NSCLC and
  melanoma (PMID 41606121).
- **Cold tumours segregate by which barrier dominates.** PDAC is a stromal/chemokine
  exclusion problem (PMID 24277834); glioblastoma is a myeloid-suppression and
  penetrance problem (PMID 35177622, PMID 32437507); MSS colorectal sits between TGF-β
  exclusion (PMID 29443964) and multi-agent combination signals (PMID 38871975).
- **Combination is now indexed to measurement.** Spatial and single-cell profiling has
  moved from descriptive atlases to trajectory-level response prediction
  (PMID 38194915, PMID 40147443), which is the mechanism by which axis selection can
  become patient-specific rather than histology-specific.

## How to read the rest of the notes

`notes/01`–`notes/13` take each axis group in turn: the mechanism, what has been shown in
patients, what failed and why, and the open question. `REPORT.md` is the auto-generated
listing of every curated paper by axis and evidence level. `index.tsv` is the machine
-readable index, including which records have full text mirrored under `fulltext/`.
