# Rituximab in solid-tumour CAR-T: trial-registry and not-yet-published evidence

Added after the PubMed-only round. PubMed indexes no *published* rituximab schedule for preventing
anti-CAR antibodies in solid-tumour CAR-T — but two active trials now build rituximab into the
conditioning regimen, and one of them has a public dose and timing. Results are unpublished
(one preprint, one funder board presentation).

Retrieved 2026-08-06. All quotes verbatim.

---

## 1. Stanford GD2-CAR T for H3K27M+ diffuse midline glioma — NCT04196413, Arm D

The only registry record giving an explicit rituximab dose/schedule around a solid-tumour CAR-T.

Source: https://clinicaltrials.gov/study/NCT04196413 (record last updated 2026-01-23; status recruiting)

Arm D description:

> "GD2CART will be administered in escalating doses on Day 0 in hospitalized subjects with either DIPG,
> spinal DMG, or high risk features. Intracerebroventricularly after administration of conditioning
> lymphodepletion chemotherapy regimen with rituximab, cyclophosphamide and fludarabine"

Intervention descriptions (Arm D):

> Rituximab — "First round: 750 mg/m2 per day IV for days -6 and -5. Subsequent rounds: 750 mg/m2 per day
> IV for day -5."
> Cyclophosphamide — "Cyclophosphamide 500 mg/m2 per day IV for days -4, -3, -2"
> Fludarabine — "Fludarabine 30 mg/m2 per day IV for days -4, -3, -2"

So, per cycle:

| Day | Arm D |
|---|---|
| −6 | rituximab 750 mg/m² IV (**first round only**) |
| −5 | rituximab 750 mg/m² IV (every round) |
| −4, −3, −2 | cyclophosphamide 500 mg/m² + fludarabine 30 mg/m² IV daily |
| 0 | GD2-CAR T ICV, 10–50 × 10⁶ cells |
| — | repeated with re-lymphodepletion each round |

Note the dose: **750 mg/m², i.e. 2× the conventional 375 mg/m² lymphoma/autoimmune dose**, given
5–6 days pre-infusion, and repeated with each dosing cycle rather than as a one-off induction.
Arms A–C of the same trial use no rituximab (Arm A single lymphodepletion + IV then ICV; Arm B ICV with
no lymphodepletion; Arm C sequential lymphodepletion + sequential ICV).

## 2. Why Arm D exists: anti-CAR immunity as the resistance mechanism (preprint, not peer reviewed)

Chen Y, Reynolds K, … Ramakrishna S, Mackall CL. *Anti-CAR Immunity Drives Acquired Therapeutic
Resistance to GD2-CAR T Cell Therapy in Diffuse Midline Glioma.* medRxiv, posted 2026-07-09.
PMID 42465905 · PMC13370534 · doi 10.64898/2026.06.25.26356492 ·
https://www.medrxiv.org/content/10.64898/2026.06.25.26356492v1
Local copy: `fulltext/chen_2026_medrxiv_anticar_dmg.pdf`

Abstract:

> "peripheral blood CD4+ and CD8+ T cells manifested anti-CAR immune reactivity targeting epitopes
> enriched within murine-derived and engineered junctional regions of the CAR construct. This was
> associated with appearance of circulating Human Anti-CAR Antibodies (HACAs) that bound cells expressing
> the GD2-CAR, as well as clonal expansion of CSF B cells which produced HACA which impeded the cytotoxic
> activity of GD2-CAR T cells. In several cases, appearance of circulating HACA temporally correlated with
> disease progression … levels of circulating HACA inversely correlated with circulating CAR T cell
> persistence."

Discussion — the forward-looking statement that Arm D is the test of the hypothesis:

> "We anticipate that additional evidence to confirm the role of anti-CAR responses in therapeutic
> resistance will be gleaned by comparing outcomes from patients treated on Arm A to patients currently
> being enrolled on arms delivering an intensified lymphodepletion regimen designed to reduce or eliminate
> anti-CAR immune responses."

The preprint does not itself name rituximab; the drug and schedule come from the registry record (§1)
and the funder presentation (§3).

Why solid tumours specifically (same discussion):

> "Most patients who have received investigational and commercial CAR T cells to date have been treated for
> refractory B cell and plasma cell malignancies and therefore were highly immunosuppressed at the time CAR
> T cells were administered. Further, all commercial CAR T cells today target CD19 or BCMA and thus
> eradicate B and plasma cells respectively, limiting induction of anti-CAR antibody responses."

i.e. the reason lymphoma/leukaemia/myeloma CAR-T experience is *not* transferable is that those products
are self-B-cell-depleting. This is the mechanistic justification for the scope exclusion used in this
collection.

Corroborating solid-tumour datapoint cited there: in the satri-cel (CLDN18.2) gastric/GEJ phase 2
(CT041-ST-01, Lancet 2025;405:2049–60, PMID 40460847), **95% of CAR-T recipients developed anti-CAR
antibodies**.

## 3. Interim arm-by-arm comparison, including Arm D — CIRM board presentation, January 2026

Mackall CL. *GD2-CAR T Cells for Diffuse Midline Gliomas*, CIRM Board Meeting, January 2026 (CLIN2-12595).
https://www.cirm.ca.gov/wp-content/uploads/2026/01/7b.-20290129-Closer-to-Cures-Presentation.pdf
Local copy: `fulltext/mackall_2026_cirm_board_gd2cart.pdf`

Slide table (transcribed):

| Arm | Regimen | Outcome | CAR persistence | Anti-CAR immunity |
|---|---|---|---|---|
| A (n=13) | lymphodepletion ×1, IV ×1, sequential ICV | median OS 20.6 mo, sustained benefit; dose-limiting CRS | greater persistence correlates with better outcomes | "Many patients, occur late" |
| B (n=18) | no lymphodepletion, sequential ICV | median OS 14.8 mo, transient benefit | "Very poor CAR persistence" | "All patients, occur early" |
| C (n=11) | sequential lymphodepletion, sequential ICV | median OS not reached | "Better CAR persistence" | "Preliminary data shows lower levels but still present" |
| D (now enrolling) | **sequential lymphodepletion + rituximab**, sequential ICV | too early | pending | pending |

Conclusion slide:

> "We have learned that the target product profile requires sequential intracerebral infusions and
> sequential lymphodepleting chemotherapy, likely with rituximab (mirror Arm D)."

This is the strongest statement available that a rituximab-containing regimen is the intended
solid-tumour CAR-T schedule — but note it is a funder board slide, arms are non-randomised and
sequentially enrolled, and no Arm D immunogenicity or efficacy data exist yet.

Related conference record (data overlapping the preprint): Chen Y et al., *Longitudinal single-cell atlas
of GD2-CAR T cell therapy in H3K27M-mutant diffuse midline glioma identifies humoral and cellular anti-CAR
immunity*, AACR 2026.

## 4. Penn CART-EGFR-IL13Rα2 in newly diagnosed GBM — NCT06973096, Cohort B

Source: https://clinicaltrials.gov/study/NCT06973096 (phase 1, started 2025-07-18, active not recruiting)

> Cohort B (Repeat Cycles Following Lymphodepletion): "CART-EGFR-IL13Ra2 cells will be administered via
> intracerebroventricular delivery in q6 week cycles of treatment, following lymphodepletion with
> fludarabine, cyclophosphamide, and rituximab."

Interventions:

> "Rituximab or Rituximab biosimilar — 375 mg/m2/day x 1 day"
> "Fludarabine: 30mg/m2/day x 3 days; Cyclophosphamide: 300mg/m2/day x 3 days"

Product (relevant to why ADA is expected):

> "autologous T cells transduced with a bicistronic lentiviral vector containing a murine scFv targeting
> EGFR epitope 806 and a humanized scFv targeting IL13Ra2"

So Penn's schedule is **rituximab 375 mg/m² × 1 dose per cycle**, with Flu 30 / Cy 300 mg/m² × 3 days,
before each q6-week ICV redose — half the Stanford dose, single administration, but repeated per cycle.
Cohort A (single fixed dose, no repeat) receives no lymphodepletion and no rituximab, so the rituximab is
tied specifically to the repeat-dosing cohort. The registry record does not state the rationale in words.

Predecessor trials, for contrast — no rituximab, single ICV dose, no lymphodepletion:
- NCT05168423 (recurrent GBM, phase 1; published Bagley et al., Nat Med 2025, doi 10.1038/s41591-025-03745-0;
  ASCO 2025 abstract JCO 43:16_suppl 102; ASCO 2026 OS update JCO 44:16_suppl 2013).
- NCT07209241 (phase 1b, recurrent GBM, three dosing approaches incl. repeat dosing) — registry record
  lists no rituximab as of retrieval.

## 5. What is *not* there

- **No B7-H3 CAR-T trial at the University of Pennsylvania.** Searched ClinicalTrials.gov by lead sponsor
  (53 Penn CAR-T studies, none B7-H3/CD276), by intervention (20 B7-H3 CAR-T studies: St. Jude, Stanford,
  Seattle Children's, MacroGenics, PersonGen, Zhejiang, Tiantan, Children's National, Tcelltech,
  BrainChild Bio), and by Philadelphia location. The only B7-H3 CAR-T with a Philadelphia site is
  **BrainChild Bio's BCB-276 (NCT07680439, "Illuminate")**, a phase 2 DIPG study with CHOP as a site:
  up to 15 intraventricular doses q14 days, **no lymphodepletion and no rituximab** in the record.
  Majzner's B7-H3.CD28Z.CART trials (NCT07358260, NCT07390539) are Dana-Farber/Boston Children's, Flu/Cy
  only. Seattle's BrainChild-03 (NCT04185038; PMID 39775044, 36259971) gives repeated ICV B7-H3 CAR-T
  **without** lymphodepletion and reports no rituximab.
- **No published Arm D or Cohort B results** for either rituximab-containing regimen.
- No randomised comparison of rituximab vs no rituximab in any CAR-T setting for ADA prevention.
