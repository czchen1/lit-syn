# GD2 CAR-T toxicity, with emphasis on intracerebroventricular delivery

Synthesis of **852** curated records (2003–2026, 502 with open-access full text) on GD2 CAR-T safety.
Domain detail is in `notes/`; this report states the answers, the evidence behind them, and what is
not known.

## 1. Bottom line

1. **On-target/off-tumour toxicity has not materialised clinically.** Across every published GD2
   CAR-T/CAR-NKT cohort, no patient has developed the painful neuropathy that anti-GD2 antibodies cause
   in most children, and no radiographic or clinical evidence of normal-CNS injury has been attributed
   to the CAR. Autopsy in one DIPG patient found CAR transcript and lymphocytic infiltrate confined to
   tumour, with tumour GD2 ≫ normal brain GD2 (PMID 35130560). The mechanism is antigen-density
   discrimination — and it is fragile: raising scFv affinity (14G2a E101K) caused **fatal encephalitis in
   low-GD2 cerebellar and basal brain regions** in mice (PMID 29180536).
2. **The dominant clinical toxicity is inflammation, and its location depends on the route.** IV
   infusion produces CRS (dose-limiting at 3×10⁶/kg in DMG: three grade 4 events) plus ICANS in ~45% of
   patients. ICV infusion produces almost none of either but near-universal **TIAN** on first exposure.
3. **ICV administration without lymphodepletion is markedly less toxic systemically.** In the only
   internal comparison (NCT04196413 arm A; 11 IV vs 62 ICV infusions): **no DLT in 62 ICV infusions**,
   CRS in 33.9% of ICV infusions (mostly grade 1) vs 100% of IV infusions, and **zero ICANS after ICV**
   despite higher CSF cytokines (PMID 39537919). The 253-dose ICV B7-H3 experience agrees: commonest AEs
   headache/nausea/fatigue/fever, one grade 3 hydrocephalus, no ICANS, one DLT (intratumoural
   haemorrhage) (PMID 39775044).
4. **The ICV-specific hazards are mechanical and hardware-related, not biochemical**: raised ICP
   (documented 22 and 34 mmHg episodes reversing within minutes of CSF drainage), obstructive and
   communicating hydrocephalus, reservoir/catheter dependence, and intratumoural haemorrhage of
   ambiguous attribution.
5. **Transient organ-function change is a function of systemic inflammation, and is therefore an IV
   problem.** No GD2 CAR-T trial reports attributed hepatic, renal or electrolyte toxicity; one trial
   explicitly documents normal liver enzymes, bilirubin and electrolytes acutely and long-term
   (PMID 40420236). In general CAR-T populations, hepatic dysfunction accompanies **64% of grade 3–4
   CRS** and grade 3–4 transaminase elevation occurs in **31–64%** of severe CRS, while AKI occurs in
   **~18.6%** pooled and **resolves in ~79% within a month**.
6. **Cytopenias in GD2 CAR-T trials are lymphodepletion, not CAR, toxicity** — reversible in a median 4
   days in one series, and occurring *before* cell infusion in the CAR-NKT trial. ICV re-dosing omits
   lymphodepletion and produced essentially no cytopenia (one grade 1 lymphocytopenia in 21 patients
   over 253 doses).
7. **Drug-interaction risk is real but indirect and unmeasured in this therapy.** CRS-grade
   inflammation suppresses CYP3A4/2C19/1A2 (midazolam clearance −65% as CRP rose 10→300 mg/L; PBPK
   simvastatin AUC ×2.4 at IL-6 100 pg/mL), and IL-6 blockade reverses it (sarilumab cut simvastatin
   AUC by **45%**). The best transient-cytokine analogue predicts **~28% CYP3A4 suppression for about a
   week**. Nobody has measured a DDI in a CAR-T patient. The therapy-specific interactions that *are*
   documented are different in kind: renal function governs fludarabine exposure during conditioning,
   and corticosteroids blunt the CAR itself.

## 2. IV versus ICV, quantified

Same product, same trial, same patients (PMID 39537919; first four patients in PMID 35130560):

| | IV (11 infusions) | ICV (62 infusions) |
|---|---|---|
| Lymphodepletion | Cy/Flu required | none |
| Dose | 1×10⁶/kg (MTD) or 3×10⁶/kg | 10–30×10⁶ flat |
| CRS | 100% of infusions; **grade 4 in 3/8 at DL2 → DLT** | 33.9%; 16 grade 1, 4 grade 2, 1 grade 3 (urosepsis) |
| ICANS | 5/11 patients (grade 3 in 1) | **0** |
| TIAN | 91–100% of patients; grade 3–4 in 5/11 | 71% of infusions; grade 3–4 in 8/62 |
| Cytopenias | grade 3–4 expected (Cy/Flu) | not reported |
| Hepatic/renal/electrolyte AEs | none attributed (CRS mostly ≤grade 2 at MTD) | none attributed |
| Haemorrhage | 1 grade 5 intratumoural (vascular anomaly) | — |
| DLTs | yes (CRS) | **none** |
| Blood cytokines | higher | lower |
| CSF cytokines | lower | **higher** |

The dissociation — higher CSF cytokines yet no ICANS — is the most informative safety observation in the
collection: ICANS tracks the blood/endothelial compartment, and moving the inflammatory response into
the CSF does not reproduce it. It also explains why systemic organ-function change tracks the IV route.

## 3. Toxicity domains and evidence grade

| Domain | GD2-specific evidence | Strength | Notes |
|---|---|---|---|
| CRS | 6 clinical cohorts; near-universal after IV; grade 4 at DL2 in DMG; mild in 95% of GD2-CART01 | **Direct, consistent** | Dose- and route-driven |
| TIAN | Defined in the GD2 DMG trial; 100% first ICV exposure; all reversible | **Direct** | Grading not prospectively validated |
| ICANS | 5/11 in DMG IV; grade 3 in 4/54 on GD2-CART01 (rimiducid-reversed); 0/62 ICV | **Direct** | Distinguishable from TIAN only when tumour is focal |
| On-target/off-tumour | Absent in all cohorts; fatal in high-affinity preclinical model | **Direct-negative + preclinical hazard** | Affinity/architecture dependent |
| Haematologic | Near-universal grade 3–4 with Cy/Flu; pooled anaemia 97%, neutropenia ≥3 93% | **Direct but confounded** | Conditioning, not CAR |
| Hepatic | No attributed events; explicit normal labs in one trial | **Indirect** [CART-general] | Expect grade 1–2 ALT/AST if CRS ≥3 |
| Renal/electrolyte | No attributed events; sodium moved deliberately for TIAN | **Indirect** [CART-general] | AKI ~18.6% pooled after systemic CAR-T |
| Coagulopathy | Not reported in GD2 cohorts | **Indirect** | Matters before neurosurgical procedures |
| Cardiopulmonary | Grade 4 CRS: pressors, pulmonary oedema, intubation; capillary leak 4/10 in one trial | **Direct** | CRS-mediated |
| IEC-HS/HLH | None reported; high ferritin without HLH | **Indirect**; ~3.5% after CAR-T generally | The scenario where hepatic dysfunction becomes clinical |
| Infection | Fungal and bacterial cases; urosepsis confounded 2 CRS events | **Direct** | Stacked immunosuppression |
| Drug interactions | **None measured** | **Mechanistic only** | See §5 |
| Device/hardware | Reservoir required; 1 grade 3 hydrocephalus in ICV B7-H3; haemorrhage DLT | **Direct, ICV-specific** | Under-reported as a category |
| Myeloid/microglial amplification | CSF scRNA-seq myeloid states differ by route; grade ≥2 TIAN correlates with CSF MCP-1/CCL2, TNF-α, IL-10 | **Direct but correlative** | Mechanism untested; see `notes/08` |

### 3a. The myeloid axis behind TIAN

TIAN correlates with myeloid, not T-cell, readouts: grade ≥2 TIAN tracks CSF **MCP-1/CCL2**, TNF-α and
IL-10, and grade ≥2 CRS tracks plasma MCP-1/CCL2. CSF single-cell RNA-seq shows route-dependent myeloid
states — an interferon-responsive population at peak inflammation after ICV, versus phagocytic,
lipid-metabolic, immune-suppressive DAM/MDSC-like states after IV and at late timepoints. Autopsy in
the first DMG patient showed dense Iba1⁺/CD163⁺ myeloid infiltration **within tumour** and resting,
non-reactive microglia in unaffected cortex. Microglia are therefore best read as **amplifiers**
downstream of tumour-restricted CAR engagement, not as GD2 targets; the causal claim remains untested.
Detail in `notes/08`.

## 4. Transient organ-function changes that could affect other therapies

Magnitude, timing and reversibility are tabulated in `notes/05`. The decision-relevant summary:

- **Liver**: laboratory transaminase elevation is common and under-reported as an AE (58% laboratory vs
  8% reported in one 148-patient trial); grade ≥3 is uncommon (0–8%) unless CRS is grade 3–4, where
  hepatic dysfunction reaches 64%; AST>ALT pattern suggests hypoperfusion; bilirubin usually spared
  outside IEC-HS. Resolves with CRS.
- **Kidney**: AKI ~18.6% pooled, onset day +1 to +28 (mode day +7), mostly mild, **79% recovered within
  a month**; predictors are CRS, ICANS grade ≥3, pre-existing CKD; associated with worse survival even
  when reversible.
- **Electrolytes/fluid**: hyponatraemia from resuscitation/SIADH; **iatrogenic sodium shifts from
  hypertonic saline given for TIAN**; hypophosphataemia and hypokalaemia with inflammation; tumour lysis
  with high burden.
- **Marrow and haemostasis**: near-universal transient cytopenias with Cy/Flu, prolonged in a minority
  (ICAHT, predictable by CAR-HEMATOTOX); CRS coagulopathy common with low absolute bleeding rates but
  relevant to reservoir/EVD procedures during the inflammatory window.
- **Consequences for concomitant therapy**: nephrotoxins and contrast should be avoided in the CRS
  window and renally cleared drugs dosed on the current creatinine; myelosuppressive bridging or
  concurrent chemotherapy compounds ICAHT and should be sequenced rather than overlapped; neurosurgical
  procedures should be planned around coagulation parameters; steroid-sparing is preferred both for
  efficacy and to avoid steroid-mediated interactions.
- **After ICV dosing without lymphodepletion, none of this applies to a measurable degree** — the main
  systemic constraint on co-administered therapy is removed.

## 5. Drug-interaction assessment (explicitly graded)

**What is established** [mechanistic-PK]: acute inflammation suppresses CYP-mediated clearance in a
CRP/IL-6-dependent way (midazolam CL −65% over CRP 10→300 mg/L; postoperative CYP3A4 −61%, CYP1A2 −53%,
CYP2C19 −58%; ciclosporin Css ×3.6 at IL-6 peak; darunavir CL/F halved in COVID-19 with IL-6 the sole
covariate). IL-6 blockade reverses it (sarilumab: simvastatin AUC −45%, Cmax −46%; sirukumab: midazolam
AUC −30–35%). For a **transient** cytokine spike the modelled effect is **<2-fold, ~28% CYP3A4
suppression, lasting ~1 week** (blinatumomab analogue).

**What is not established**: any measured interaction in a CAR-T, GD2 CAR-T, or ICV CAR-T patient. No
CYP-probe study exists in CRS. The magnitude in CAR-T CRS is likely to exceed the blinatumomab model
(higher, longer cytokine elevation) but this is inference.

**Therefore**: treat CRS as a transient, bidirectional perturbation of CYP3A4-dominant clearance —
levels up during CRS, down after IL-6 blockade — and manage it with therapeutic drug monitoring for
narrow-index substrates (azoles, calcineurin/mTOR inhibitors, anticonvulsants, anticoagulants) rather
than with pre-emptive dose changes. Do not claim a GD2-specific interaction.

**Therapy-specific interactions that are documented**, and matter more in practice:

- **Renal function → fludarabine exposure** (eGFR a significant covariate on clearance in the first
  CAR-T-specific population-PK model, PMID 41471106): a transient creatinine rise before conditioning
  changes lymphodepletion intensity, which changes both efficacy and toxicity.
- **Corticosteroids → CAR activity**: a pharmacodynamic interaction the trials manage explicitly
  (steroid-free at enrolment; response scoring deferred ≥7 days after steroids).
- **Anti-cytokine agents → infection and marrow recovery**: anakinra, tocilizumab, siltuximab, and, for
  IEC-HS, etoposide/ruxolitinib/emapalumab stack with lymphodepletion.
- **Hypertonic saline** for TIAN as a deliberate electrolyte intervention interacting with volume- and
  sodium-sensitive drugs.

## 6. What would change these conclusions

1. Serial laboratory and cytokine data published for an **ICV-only** cohort (arms B/C of NCT04196413) —
   would convert "no reported organ toxicity" into a measured claim.
2. A **CYP-probe or population-PK study around CRS and tocilizumab** in CAR-T recipients.
3. Prospective **TIAN grading** with the type 1/type 2 distinction operationalised, since BrainChild-03
   could not classify most events retrospectively (PMID 41798119).
4. A larger ICV denominator for **intratumoural haemorrhage** attribution.
5. A circulating **neuro-injury biomarker** (e.g. NFL) in GD2 CAR-T patients, to test the
   on-target/off-tumour null result with something more sensitive than examination.
6. Any clinical use of a **higher-affinity or armoured GD2 CAR** — the preclinical hazard is specific to
   affinity/architecture and the current safety record should not be assumed to transfer.

## 7. Practical distillation

- The ICV route is the main safety lever: it converts a systemic-inflammatory toxicity problem into an
  intracranial-pressure and hardware problem, and removes the lymphodepletion-driven organ and marrow
  toxicity that otherwise constrains concomitant treatment.
- Every ICV programme needs a reservoir, ICP measurement, an osmotic-therapy and CSF-drainage pathway,
  and staff who will access the reservoir within minutes — not a pharmacological algorithm alone.
- Grade CRS, ICANS and TIAN separately at every infusion; fever after ICV dosing is expected.
- Assume liver enzymes and creatinine will move transiently whenever CRS reaches grade 3, monitor them
  daily in the acute window, and use those values (not admission values) for co-medication dosing.
- Handle drug interactions as monitoring problems in a moving inflammatory window, and say plainly that
  the GD2-specific interaction data do not exist.
