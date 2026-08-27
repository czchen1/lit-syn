# 07 — Monitoring and mitigation

Everything here is derived from what the published GD2 and locoregional CNS CAR-T protocols actually
did, plus general CAR-T guidance (ASTCT grading PMID 30592986; pediatric management PMID 30082906;
ICAHT grading PMID 38181508; IEC-HS management PMID 41779733). It is a synthesis of published practice,
not a protocol.

## Structural safeguards used in the GD2 CNS programme

- **Eligibility geography**: exclusion of bulky thalamic or cerebellar tumours (preclinical lethal
  hydrocephalus at those sites) and of clinically significant dysphagia as a marker of medullary
  dysfunction (PMID 39537919).
- **No corticosteroids at enrolment**, and CIS scoring deferred ≥7 days after steroid discontinuation.
- **Ommaya/Rickham reservoir placed before treatment** in DIPG, for ICP measurement *and* therapeutic
  CSF removal — routine plus symptom-prompted measurements. ICV trials of other targets require a CNS
  catheter as an eligibility criterion (PMID 39775044).
- **Pre-specified TIAN algorithm**: CSF removal → hypertonic saline → anti-cytokine agents →
  corticosteroids, with neurocritical-care availability.
- **iCasp9 suicide gene** in the construct, with rimiducid/AP1903 available (used in 4 children with
  grade 3 ICANS on GD2-CART01, PMID 40841488; never needed in DMG arm A).
- **Dose separation of route**: IV DL1 (1×10⁶/kg) as MTD, ICV flat doses 10–30×10⁶ without
  lymphodepletion, ≥21–28 days between infusions, requiring circulating CAR <5% and toxicity resolved
  to <grade 2 before re-dosing.

## Monitoring that the literature justifies

**Neurologic / intracranial (both routes; the priority for ICV)**

- Structured neurological examination at fixed timepoints, with a quantified improvement score so that
  *worsening* is detectable against a moving baseline.
- ICP measurement via reservoir — scheduled and on symptoms. Documented episodes: 22 mmHg and 34 mmHg
  with resolution within minutes of drainage.
- Low threshold for MRI (T2/FLAIR at the tumour site correlates with focal TIAN symptoms) and for EEG
  when encephalopathy is present (triphasic waves/diffuse slowing seen in the grade 4 ICANS case).
- Explicitly grade CRS, ICANS and TIAN **separately** at every infusion; do not collapse fever after
  ICV dosing into "CRS".

**Systemic inflammation (IV route, and any febrile ICV patient)**

- CRP, ferritin, fibrinogen, D-dimer, LDH, triglycerides; cytokine panel where available. Rising
  ferritin with falling fibrinogen and transaminitis → evaluate for IEC-HS.
- Blood counts; anticipate Cy/Flu nadir; use CAR-HEMATOTOX-type baseline risk assessment where the
  patient is heavily pretreated.
- Liver panel (ALT, AST, bilirubin, albumin, INR) through the CRS window — noting that grade 1–2
  transaminase change is expected and does not by itself require intervention, while AST>ALT with
  hypotension suggests hypoperfusion, and bilirubin rise flags CRS severity or IEC-HS.
- Creatinine/eGFR **daily during the acute window**, with electrolytes including sodium, potassium,
  phosphate, magnesium; urine output and fluid balance. Sodium and osmolality are mandatory if
  hypertonic saline is used.
- Culture-directed infection workup for every fever, since infection both mimics and precipitates CRS
  (the two grade 3 CRS events in the ICV/sDMG experience were confounded by urosepsis).

**Concomitant medications**

- Reconcile the medication list against CYP3A4/2C19/1A2 dependence at baseline (see note 06) and again
  when tocilizumab/siltuximab is given.
- Therapeutic drug monitoring during and for ~1 week after the inflammatory peak for azoles,
  calcineurin/mTOR inhibitors, and any narrow-index CYP substrate; INR/anti-Xa if anticoagulated.
- Recalculate renally cleared drug doses on the current creatinine, not the admission value; this
  includes fludarabine exposure planning before conditioning (PMID 41471106).

## Mitigation strategies with evidence behind them

| Strategy | Evidence | Note |
|---|---|---|
| **Use the ICV route for re-dosing, without lymphodepletion** | 62 ICV infusions, no DLT, no ICANS, CRS mostly grade 1, no organ-function signal (PMID 39537919); 253 ICV doses of B7-H3 with one DLT (PMID 39775044) | The single largest toxicity reduction available |
| **Cap the IV dose** | Grade 4 CRS at 3×10⁶/kg vs none at 1×10⁶/kg in DMG | MTD is route-specific |
| **Split/fractionate dosing** | No further grade ≥2 CRS after switching to 1.5×10⁷/m² split 5–7 days apart (PMID 38771986) | Cheap, no engineering needed |
| **Keep scFv affinity standard** | Fatal encephalitis with high-affinity E101K in mice (PMID 29180536) | Antigen-density discrimination is the safety mechanism |
| **Exclude high-risk tumour geography** | Preclinical hydrocephalus in thalamic/cerebellar disease | Now standard eligibility |
| **Pre-emptive IL-1 blockade (anakinra)** | Used prophylactically/early for TIAN and CRS in GD2 CNS trials; CSF-penetrant | IL-1 mechanism separates CRS from neurotoxicity (PMID 29808007, PMID 29808005) |
| **CSF drainage + hypertonic saline first for type 1 TIAN** | Minutes-scale reversal of ICP events | Preserves CAR activity vs steroids |
| **iCasp9 + rimiducid** | Reversed grade 3 ICANS in 4/54 children (PMID 40841488) | Definitive but ablates the therapy |
| **Pharmacological CAR pausing (dasatinib)** | Used in refractory grade 4 ICANS (PMID 35130560); itacitinib explored (PMID 32998963) | Reversible alternative to iCasp9; not formally trialled |
| **Engineering: logic gates, affinity tuning, microenvironment-actuated CARs** | Preclinical only (PMID 28341563, PMID 36396552, PMID 39841845, PMID 41005308) | Not yet in GD2 patients |

## Gaps worth closing

1. **No prospective organ-function dataset for ICV GD2 CAR-T.** The claim "ICV spares the liver and
   kidneys" rests on absence of reported AEs, not on published serial laboratory values.
2. **No measured DDI or CYP-probe study in any CAR-T CRS cohort**, let alone GD2 or ICV. A midazolam or
   4-drug-cocktail probe study around CRS and tocilizumab administration would settle a question
   currently answered by PBPK extrapolation.
3. **No standardised TIAN grading validated prospectively.** BrainChild-03's retrospective application
   of TIAN criteria (PMID 41798119) showed most events could not be classified as type 1 vs type 2 —
   the distinction that determines whether CSF diversion is indicated.
4. **Repeat-dosing late toxicity** (ependymal injury, CSF-flow changes, anti-CAR immunity, device
   complications) is unreported despite cohorts receiving up to 81 doses over >3 years.
5. **No circulating neuro-injury biomarker** in clinical GD2 CAR-T; NFL is used in mouse models
   (PMID 38551501) and would directly address the residual on-target off-tumour question.
6. **Attribution of intratumoural haemorrhage** — two cohorts, one grade 5 and one grade 4 event, each
   argued to be background DIPG natural history. Only a larger denominator resolves this.
