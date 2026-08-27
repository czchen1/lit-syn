# 06 — Drug interactions and pharmacokinetics: what transient inflammation does to concomitant medications

**Framing.** No GD2 CAR-T study has measured a drug–drug interaction. What exists is a well-quantified
mechanistic literature showing that (a) acute inflammation suppresses cytochrome P450 activity, and
(b) blocking IL-6 *reverses* that suppression. Both directions are relevant, because CAR-T patients
receive an inflammatory insult and then, often within hours, an IL-6 blocker. Everything in this note
is therefore **[mechanistic-PK]**: a strong basis for monitoring and for anticipating dose changes, not
a measured GD2-specific interaction.

## Direction 1 — CRS suppresses CYP-mediated clearance (drug levels rise)

- Human endotoxin/inflammation studies: antipyrine clearance **−35%** (95% CI 18–48) by day 2,
  hexobarbital −20%, theophylline −20% (reviewed in PMID 36059001).
- Surgery-induced acute inflammation: metabolic ratios fell by **CYP1A2 −53%, CYP2C19 −58%, CYP3A4 −61%**
  within 1–3 days postoperatively (same review).
- Midazolam clearance fell **65.4%** as CRP rose from 10 to 300 mg/L; CRP and IL-6 were covariates on
  midazolam CL.
- COVID-19 vs HIV: darunavir CL/F 4.1 vs 10.3 mL/h and AUC 161,387 vs 75,727 ng·h/mL, with **IL-6 the
  only significant covariate** (PMID 32856282).
- Bone-marrow-transplant engraftment: cyclosporine steady-state concentration rose **3.6-fold**, peaking
  concurrently with IL-6.
- PBPK, IL-6 10 → 100 pg/mL: simvastatin AUC **×2.36**, midazolam ×2.08, omeprazole ×1.97,
  dextromethorphan ×1.37, warfarin ×1.29, caffeine ×1.07 — CYP3A4 substrates most sensitive
  (PMID 34496043, PMID 38044486, PMID 40733104).
- **The closest analogue to CRS**: modelling of *transient* IL-6 elevation after **blinatumomab** gave
  maximal suppression of CYP3A4 **28% at 48 h lasting ~7 days**, CYP1A2 9%, CYP2C9 17%, with AUC ratios
  of 1.9 (simvastatin) and 1.7 (midazolam) — i.e. for a short cytokine spike, expect **<2-fold**
  exposure changes lasting about a week, magnitude driven by *duration* of cytokine elevation
  (PMID 38044486).
- Clinical corroboration in other settings: voriconazole exposure rises with inflammation and can
  produce phenoconversion of CYP2C19 genotype (PMID 39010708, PMID 41766069, PMID 42300127);
  pediatric-specific systematic review of inflammation on CYP activity (PMID 34462878).

## Direction 2 — IL-6 blockade removes the suppression (drug levels fall)

- **Sarilumab 200 mg single dose + simvastatin** in RA: simvastatin Cmax **−46%**, **AUC∞ −45%**;
  β-hydroxy-simvastatin acid Cmax −35%, AUC −36%; CRP fell >7-fold over the same week
  (PMID 27722854).
- Tocilizumab reduces simvastatin Cmax and AUC by the same mechanism (cited in the same paper);
  sirukumab decreased midazolam AUC 30–35%, omeprazole 37–45%, S-warfarin 18–19% while *increasing*
  caffeine AUC 20–34%.
- Continuous IL-6R antagonist therapy in RA changes CYP activity measurably (PMID 37831074);
  olokizumab shows the same class effect (PMID 38984761).
- Regulatory-style assessments exist for many pro-inflammatory-pathway biologics
  (PMID 36890677, PMID 27391296, PMID 38050329 for mosunetuzumab, PMID 38383116 for cytokine–CYP
  trends).

**Net effect in a CAR-T patient**: exposure to CYP3A4/2C19/1A2 substrates can rise during CRS and then
fall abruptly when tocilizumab/siltuximab is given — a two-way, few-days-scale moving target rather
than a steady shift.

## Concomitant drugs where this plausibly matters in a GD2 CAR-T patient

Prioritised by likelihood of co-prescription in this population and narrowness of therapeutic index:

| Drug class | Concern | Practical response |
|---|---|---|
| **Antiseizure medications** (levetiracetam mostly non-CYP; but phenytoin, carbamazepine, valproate, lacosamide) | Seizure prophylaxis is standard in CNS CAR-T; CYP substrates/inducers shift with inflammation, and steroids interact with several | Prefer non-CYP agents (levetiracetam); level-monitor if using phenytoin/carbamazepine/valproate |
| **Azole antifungals** (voriconazole, posaconazole, itraconazole) | Both victims (inflammation-driven overexposure, documented phenoconversion) and perpetrators (CYP3A4 inhibition) | Therapeutic drug monitoring during and after CRS; avoid assuming genotype-based dosing holds |
| **Calcineurin/mTOR inhibitors** (tacrolimus, sirolimus, ciclosporin) | 3.6-fold ciclosporin rise documented with IL-6 peaks; used for GVHD in allogeneic GD2 products | Frequent trough monitoring, especially in ALLO_GD2-CART01-type settings with GVHD |
| **Dexamethasone / methylprednisolone** | CYP3A4 substrate and inducer; used at variable doses for TIAN/ICANS; also the drug most likely to blunt CAR efficacy | Expect variable exposure; use the minimum effective duration per the trial algorithms |
| **Dasatinib** (used as a CAR "off-switch") | CYP3A4 substrate — exposure will move with both CRS and tocilizumab | Not formally studied in this use |
| **Opioids, midazolam, other sedatives** | CYP3A4-dependent; children with brainstem disease already at risk of hypoventilation | Titrate to effect; anticipate reduced clearance during CRS |
| **Anticoagulants** (warfarin, DOACs) | CYP/coagulation double hit: warfarin S-enantiomer clearance changes plus CRS coagulopathy | INR/anti-Xa monitoring through the inflammatory window |
| **Statins** | Largest documented swing in either direction (×2.36 up with IL-6; −45% with sarilumab) | Consider holding during the acute window; the clinical consequence is usually small in this population |
| **Chemotherapy given concurrently or as bridging** | Hepatic/renal changes and cytopenias limit dosing; bridging intensity worsens haematopoietic recovery (PMID 40267180) | Sequence rather than overlap where possible |
| **Nephrotoxins** (aminoglycosides, amphotericin, contrast, NSAIDs) | AKI risk multiplies with CRS hypoperfusion | Avoid in the CRS window; dose to renal function daily, not on admission creatinine |

## Interactions specific to this therapy, not mediated by CYP

1. **Lymphodepletion dosing depends on renal function.** Fludarabine is renally eliminated;
   the first population-PK model built exclusively in CAR-T recipients found weight, **eGFR** and CAR
   construct type as significant covariates on clearance, with reduced clearance below
   eGFR 120 mL/min/1.73 m² (PMID 41471106). Fludarabine over-exposure is linked to
   treatment-related mortality in HSCT, and under-exposure to weaker lymphodepletion. So a transient
   pre-infusion creatinine rise is not a cosmetic finding — it changes the conditioning exposure.
   ICV re-dosing without lymphodepletion sidesteps this entirely.
2. **Corticosteroids and CAR T-cell activity.** Steroid exposure before or during infusion is an
   exclusion/deferral criterion in the GD2 DMG trial and CIS scoring was deferred until ≥7 days after
   steroid discontinuation (PMID 39537919). The interaction of interest is pharmacodynamic — steroids
   impair the therapy — and this is why the TIAN algorithm reaches for CSF drainage, hypertonic saline
   and IL-1/IL-6 blockade first.
3. **Hypertonic saline** for TIAN alters sodium and free-water handling, which changes the
   distribution/level of drugs sensitive to volume status and affects concurrent antiseizure agents.
4. **Anti-cytokine agents are themselves immunosuppressive** (anakinra, tocilizumab, siltuximab,
   emapalumab, ruxolitinib, etoposide for IEC-HS), stacking with lymphodepletion for infection risk
   and with cytopenias for marrow recovery.
5. **Therapeutic proteins do not have classic CYP interactions themselves** — the interaction is always
   via the cytokine milieu (PMID 36890677, PMID 27391296). Do not look for a "CAR T-cell DDI"; look for
   an inflammation-mediated one.

## What is genuinely unknown

- Whether **ICV** administration, which raises CSF cytokines but not plasma cytokines, produces any
  systemic PK effect at all. Mechanistically it should be minimal; nobody has measured it.
- The magnitude and duration of CYP suppression during CAR-T CRS specifically — the blinatumomab
  transient-IL-6 model (~28% CYP3A4 suppression for a week) is the best available proxy but CAR-T CRS
  is longer and more intense than blinatumomab's cytokine spike.
- Whether inflammation-driven changes in **renal glomerular filtration** during CRS (modelled in
  PMID 37715056) are large enough to require dose adjustment of renally cleared co-medications beyond
  routine creatinine-based dosing.
