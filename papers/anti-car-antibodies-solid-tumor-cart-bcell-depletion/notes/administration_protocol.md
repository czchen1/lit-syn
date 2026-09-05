# Giving rituximab around CAR-T: dose, timing, premedication, monitoring, and bedside practicalities

Companion to `REPORT.md`. `REPORT.md` answers *whether* to give rituximab for anti-CAR immunity (answer:
unproven, two trials are testing it). This note answers *how the drug is actually given* once a protocol
calls for it.

**Evidence status of each block below is labelled.** Nothing here is a substitute for the treating
protocol: the two solid-tumour CAR-T regimens are investigational, and no anti-CAR-prophylaxis outcome
data exist for either.

| Label | Meaning |
|---|---|
| **[LABEL]** | US prescribing information, Rituxan IV, label effective 2025-01-06 (openFDA `drug/label`). Established. |
| **[REGISTRY]** | Verbatim from the ClinicalTrials.gov record. Investigational, no outcome data. |
| **[LIT]** | Peer-reviewed evidence, cited by PMID; strength varies and is stated. |
| **[INFERENCE]** | Our reasoning, not a sourced recommendation. |

---

## 1. Dose and timing

### 1.1 The two solid-tumour CAR-T schedules **[REGISTRY]**

|  | Stanford NCT04196413 Arm D (GD2 CAR-T, H3K27M+ DMG) | Penn NCT06973096 Cohort B (CART-EGFR-IL13Rα2, ndGBM) |
|---|---|---|
| Rituximab | **750 mg/m²/day IV on day −6 *and* day −5** for the first round; **750 mg/m²/day IV on day −5** for each subsequent round | **375 mg/m²/day IV × 1 day** (rituximab or biosimilar), before each cycle |
| Lymphodepletion | cyclophosphamide 500 + fludarabine 30 mg/m²/day, days −4, −3, −2 | cyclophosphamide 300 + fludarabine 30 mg/m²/day × 3 days |
| CAR-T | intracerebroventricular, day 0, repeated rounds | intracerebroventricular, q6-week cycles |
| Design logic | ~2× the standard single dose, split over 2 days, **1 day before lymphodepletion starts**, repeated every round | standard single dose, repeated every cycle |

Both put rituximab **immediately before lymphodepletion, i.e. 5–6 days before the CAR-T infusion**, and
repeat it with every CAR-T round rather than giving a one-off induction. Neither registry record specifies
premedication, infusion rate, or monitoring — those come from the treating protocol and the label.

### 1.2 Reference doses that anchor those numbers **[LABEL]** / **[LIT]**

- 375 mg/m² IV is the label dose for B-cell NHL (adult and paediatric ≥6 months) and the GPA/MPA induction
  dose; it comes from the pivotal 375 mg/m² weekly × 4 trial (9310469) **[LABEL]**.
- CLL uses 375 mg/m² cycle 1 then **500 mg/m² cycles 2–6**; RA and PV use **flat 1,000 mg × 2, 2 weeks
  apart** — so a >375 mg/m² dose is not itself unusual **[LABEL]**.
- Dose sets the **duration** of depletion more than the depth of blood depletion: median B-cell return
  ~2.5 / 5.0 / 6.6 months after 100 mg/m², 375 mg/m², and 2 × 375 mg/m² (see `REPORT.md` §3).
- Exposure is not fixed by BSA: clearance rises with proteinuria and with anti-rituximab antibodies
  (36420256), and anti-drug antibodies shorten depletion (58.5 vs 163 days in children, 42481732; 42340364)
  **[LIT]**.
- Subcutaneous rituximab (1,400 mg with rHuPH20) is bioequivalent-by-design in lymphoma (24002601, 30744432)
  but **is label-restricted to patients who have already tolerated a full IV dose**, and neither CAR-T
  protocol uses it **[LABEL]**.
- Biosimilars are explicitly permitted in NCT06973096; switching studies show no consistent immunogenicity
  or efficacy penalty (29500555) **[LIT]**.

### 1.3 Interaction with the CAR-T timeline **[INFERENCE]**

- Rituximab is given **before** Cy/Flu in both protocols. Cy/Flu itself depletes B cells, so the marginal
  benefit and marginal toxicity of rituximab is judged against that baseline (see `REPORT.md` §5).
- Fludarabine exposure drives CAR-T expansion and outcome, and is under-dosed in young children by fixed
  mg/m² dosing (40148484, 38191740, 41471106, 40609087) — adding rituximab does not change that, but it
  does add a day to the pre-infusion window in which the lymphodepletion schedule must not slip.
- The prophylaxis→rescue asymmetry (`REPORT.md` §4) means a **missed or delayed** pre-round rituximab dose
  cannot be made up after the CAR-T infusion.

---

## 2. Preparation and infusion **[LABEL]**

- **IV infusion only. Never IV push or bolus.** Administer only where severe infusion reactions can be
  managed.
- Dilute to **1–4 mg/mL** in 0.9% NaCl or 5% dextrose. Do not mix with other drugs. Diluted solution:
  24 h at 2–8 °C (plus a further 24 h at room temperature shown stable; refrigerate because there is no
  preservative). Inspect — should be clear and colourless.
- **First infusion (adult):** start **50 mg/h**; if no toxicity, increase by 50 mg/h every 30 min to a
  maximum of **400 mg/h**.
- **First infusion (paediatric mature B-cell NHL/B-AL):** start **0.5 mg/kg/h (max 50 mg/h)**; increase by
  0.5 mg/kg/h every 30 min to max 400 mg/h.
- **Subsequent infusions (adult):** start **100 mg/h**; increase by 100 mg/h every 30 min to max 400 mg/h.
  Paediatric: start 1 mg/kg/h (max 50 mg/h), increase by 1 mg/kg/h every 30 min.
- **90-minute rapid infusion** (20% of the dose in the first 30 min, remaining 80% over 60 min) is a label
  option **from cycle 2 onward**, only if no grade 3–4 infusion reaction in cycle 1 and only with a
  glucocorticoid-containing regimen. **Excluded:** clinically significant cardiovascular disease, or
  circulating lymphocytes ≥5,000/mm³.
- Rapid-infusion safety data: 90 min in 206 patients with no grade 3–4 reactions (17244675), 319 infusions
  with *and without* steroids with no grade 3–4 events (16856919), and 60-min infusions in 105 second-and-later
  doses (19220420) **[LIT]**.
- **[INFERENCE]** In a repeat-cycle CAR-T protocol, every rituximab dose after the first is a "subsequent
  infusion", so the faster start rate applies — but the 90-minute option assumes concurrent steroids, which
  is exactly what §3 says to think twice about here.

---

## 3. Premedication

**[LABEL]** Premedicate with **acetaminophen/paracetamol and an antihistamine before *every* infusion**.
For paediatric mature B-cell NHL/B-AL the label specifies acetaminophen + an H1 antihistamine
(diphenhydramine or equivalent) **30–60 min before** each infusion. A glucocorticoid is label-recommended
only for the autoimmune indications (methylprednisolone 100 mg IV or equivalent 30 min pre-dose for
RA/GPA/MPA/PV) and, for lymphoma, as the chemotherapy's own steroid when using the 90-minute rate.

**[LIT]** What the premedication evidence supports:

| Component | Evidence |
|---|---|
| Acetaminophen + H1 antihistamine | Standard of care; label-mandated. Most reactions occur 30–120 min into the first infusion (label; 42530421 observed most IRR at 30–60 min). |
| Second-generation H1 (e.g. bepotastine) instead of diphenhydramine/hydroxyzine | Randomised phase II: grade ≥2 IRR 32% vs 52% and less drowsiness, not significant at n=40 (41989666). Reasonable when sedation is undesirable. |
| Adding an **H2** antagonist | No benefit: IRR 38% vs 36.5%, no difference in grade 3–4 (42530421, n=299). |
| Corticosteroid premedication | Reduces IRR (prednisone pretreatment 15.9% vs 43.2% in DLBCL, 37205922); oral prednisolone 50 mg ≈ IV methylprednisolone 50 mg (41572843, 2,253 infusions). But rapid infusion is safe *without* steroids (16856919) and steroid necessity is being re-examined (41789935). |

**Corticosteroids are the one premedication decision that is CAR-T-specific.** Steroids inhibit ADCC and are
argued to belong at the first dose only for ADCC-dependent mAbs (38270799) **[LIT]**; separately, steroids
blunt CAR-T expansion and function and are the treatment for CRS/ICANS rather than a routine co-medication
(42274870, `REPORT.md` §5, where rituximab + steroids around CAR-T is linked to late cytopenias). Rituximab
here is given days **before** the CAR-T infusion, so a single pre-infusion steroid dose is
pharmacodynamically distant from the cells — but this is **[INFERENCE]**, and the decision belongs to the
CAR-T protocol, not to the infusion nurse's standing premedication order.

---

## 4. Before the first dose: screening and baseline labs **[LABEL]** + **[LIT]**

| Test | Why |
|---|---|
| **HBsAg + anti-HBc (add anti-HBs)** | Label-mandated before any rituximab dose. Anti-CD20 is a **high-risk** therapy for HBV reactivation: 25% reactivation with R-CHOP in HBsAg−/anti-HBc+ DLBCL vs 0% with CHOP, including a hepatic death (19075267). ASCO: chronic **or past** HBV + anti-CD20 → antiviral prophylaxis during and for **≥12 months after** therapy, with HBV-expert co-management (32716741, 25964247, 28219691). Entecavir prophylaxis cut reactivation 17.9%→2.4% in resolved HBV, and an undetectable baseline HBV DNA is **not** protective (23775967). Reactivation has been reported up to 24 months after therapy. |
| **CBC with differential and platelets** | Label-mandated pre-first-dose; then before each course (monotherapy) or weekly-to-monthly with chemotherapy, more often if cytopenic. Continue after the last dose until cytopenias resolve. |
| **Baseline quantitative IgG (± IgA/IgM) and B-cell flow** | 85% of a 4,479-patient cohort had **no** pre-rituximab immunoglobulin measurement, and severe infections rose 17.2%→21.7% (30646343); baseline + serial IgG and B-cell counts are the recommended monitoring (36706910). Also the only way to interpret post-CAR-T hypogammaglobulinaemia (34757064). |
| **Renal function, electrolytes, phosphate, uric acid, LDH; hepatitis C and HIV per CAR-T program** | TLS and renal toxicity are label warnings; CAR-T best-practice screening panels (34923107, 31753925). |
| **Anti-CAR ADA baseline, and confirmation of the CAR construct** | see §7. |

---

## 5. During and immediately after the infusion

**[LABEL]** Infusion-related reactions are the boxed warning: fatal reactions have occurred within 24 h,
**~80% with the first infusion**, severe reactions typically **30–120 min** into it. Manifestations include
urticaria, hypotension, angioedema, hypoxia, bronchospasm, pulmonary infiltrates, ARDS, MI, ventricular
fibrillation, cardiogenic shock, anaphylactoid events, death.

Management, per label:

1. **Interrupt or slow the infusion** for any infusion-related reaction.
2. Institute medical management as needed — **glucocorticoids, epinephrine, bronchodilators, oxygen**.
3. On symptom resolution, **resume at ≥50% rate reduction** (label also phrases this as one-half the
   previous rate).
4. **Temporarily or permanently discontinue** depending on severity and interventions required; discontinue
   for severe (grade 3–4) reactions and for serious/life-threatening arrhythmias.
5. Monitor closely, with cardiac monitoring during and after infusion, in: pre-existing cardiac or pulmonary
   disease, prior cardiopulmonary reactions, history of arrhythmia/angina, and circulating malignant cells
   ≥25,000/mm³.

**[LIT]** Practical additions:

- **Cytokine-release-type reactions and true (IgE) hypersensitivity are clinically indistinguishable at the
  bedside** but differ in mechanism and in whether rechallenge is safe (20350882, 31447561, 38452439); the
  distinction is made retrospectively, so treat by severity in the moment.
- **Anaphylaxis is rechallengeable via desensitisation; serum sickness is not.** In 1,534 paediatric
  infusions: 7 rituximab-induced serum sickness (fever + rash + arthralgia 1–30 days later, raised CRP/ESR,
  low complement) and 7 anaphylaxis; 5/7 anaphylaxis patients were successfully re-dosed under
  desensitisation, whereas RISS recurred severely (42073020). Adult desensitisation protocols: 46 procedures
  in 11 patients without anaphylaxis (42279029); paediatric workup framework in 41937341.
- **[INFERENCE]** In a repeat-cycle CAR-T protocol this matters more than usual: a reaction that closes the
  door on rituximab closes it on **every future round**, so grade the event carefully and involve
  allergy/immunology early rather than abandoning the drug.

**[LABEL]** Also mid-to-late: severe mucocutaneous reactions (including SJS/TEN, onset as early as day 1 →
discontinue permanently), TLS within **12–24 h** of the first infusion in high-burden disease (give
aggressive IV hydration + anti-hyperuricaemic therapy, correct electrolytes, monitor renal function and
fluid balance, dialyse if needed; 21561350), renal toxicity (discontinue for rising creatinine or oliguria),
and bowel obstruction/perforation with chemotherapy (evaluate abdominal pain or repeated vomiting).

---

## 6. After the dose: infection prophylaxis, immune reconstitution, vaccines

**[LABEL]**

- PJP (Pneumocystis) **and herpesvirus** prophylaxis is label-recommended in CLL during treatment and for up
  to 12 months after; PJP prophylaxis for GPA/MPA during and for ≥6 months after the last dose.
- Serious bacterial, fungal, and new or reactivated viral infection (CMV, HSV, VZV, parvovirus B19, WNV,
  HBV, HCV) can occur during and after therapy; infections have been reported with hypogammaglobulinaemia
  persisting >11 months. Withhold rituximab for serious infection; avoid in severe active infection.
- **Live viral vaccines are not recommended before or during treatment**; bring immunisations up to date
  beforehand where possible.

**[LIT]**

- Post-CAR-T infection prevention is a structured, risk-adapted programme in its own right — antiviral and
  PJP prophylaxis, selective antibacterial/antifungal cover during prolonged cytopenia, IgG replacement,
  and vaccination timed to immune recovery (42274870, 34923107, 31753925). Rituximab should be layered into
  **that** programme, not prescribed with a separate ad-hoc prophylaxis plan.
- **Hypogammaglobulinaemia:** 39% developed low IgG after rituximab and 6.6% needed IVIG for recurrent
  sinopulmonary infection, worse with maintenance dosing (23276889, 30646343). CAR-T-specific thresholds and
  duration in 34757064; IgG-replacement practice is extrapolated from primary immunodeficiency, not
  CAR-T-derived (31416717). IVIG timing must be kept away from rituximab dosing (`REPORT.md` §4).
- **Late-onset neutropenia:** grade 3–4 neutropenia weeks to months later — incidence 3–27%, median onset
  77 days (range 42–153) with infection in most (20827108); median 102 days in rheumatic disease, coinciding
  with the depletion window, 7/11 hospitalised with infection (21560117). Review 36706910. **[INFERENCE]**
  This overlaps exactly with the post-CAR-T cytopenia window, so a late neutropenia will be attributable to
  either agent; keeping counts is the only way to tell.
- **PML:** 57 rituximab-associated cases, median 5.5 months after the last dose, 90% fatal (19264918).
  New neurological signs in a CNS CAR-T patient have many likelier causes (§7), but PML belongs on the list.
- **Vaccines:** anti-CD20 blunts responses to tetanus, pneumococcal, neoantigen (KLH) and mRNA vaccines
  (32727835, 34514436); revaccinate after CAR-T or B-cell-depleting therapy per ASCO (38498792); CAR-T
  recipients lose seroprotection for specific pathogens (33914708). Vaccinate **before** depletion where the
  schedule allows.

---

## 7. CAR-T-specific cautions

- **Absolute contraindication: a CD20 or RQR8 safety/selection switch in the CAR construct.** Rituximab is
  the agent used to *delete* those cells. Confirm the construct before writing the order
  (`REPORT.md` §5, `I_confusables_do_not_confuse`).
- Anti-CAR ADA prophylaxis with rituximab has **no** outcome data in solid-tumour CAR-T; the one in-vivo
  attempt (single 7 mg/kg dose 7 days pre-infusion in macaques) failed to prevent anti-CAR IgG
  (`REPORT.md` §2).
- Rituximab does not reverse an established titre — that is plasma-cell-mediated (`REPORT.md` §4).
- B-cell depletion could in principle blunt the CAR-T response itself (type-I-IFN-dependent effects on CD8
  priming, `REPORT.md` §5); unresolved in humans.
- **New neurology after an ICV round is usually not rituximab.** TIAN (tumour inflammation-associated
  neurotoxicity) occurred in 16/21 children and 32% of infusions after intraventricular B7-H3 CAR-T, mostly
  grade 1–2, median resolution <24 h, one requiring CSF diversion (41798119); ICANS-type toxicity managed
  with dexamethasone and anakinra was seen with the intrathecal CART-EGFR-IL13Rα2 product used in
  NCT06973096 (38480922). Grade CRS/ICANS by ASTCT consensus (30592986).
- Locoregional delivery had ~61% fewer grade ≥3 adverse events than IV delivery in high-grade glioma
  (41895715); ICV-specific procedural AEs are mainly headache, nausea, vomiting (40282439).
- **[INFERENCE]** Rituximab does not meaningfully enter the CSF, and the CNS behaves as a B-cell sanctuary
  even during full peripheral depletion (42211720). A systemic dose given for systemic anti-CAR antibody
  prophylaxis should not be expected to deplete intrathecal B cells.

---

## 8. Fasting, hydration, and other bedside practicalities

- **Rituximab itself does not require fasting.** The label specifies no NPO status, no food-effect
  restriction, and no dietary requirement — it is an IV monoclonal antibody. Patients can eat and drink
  before and during the infusion **[LABEL]**. Nausea/vomiting risk around the dose comes from the
  co-administered cyclophosphamide/fludarabine, not from rituximab.
- **Fasting belongs to the procedure, not the drug.** If a round involves sedation or general anaesthesia —
  Ommaya/reservoir placement, some ICV infusions, imaging under anaesthesia — the anaesthesia service's
  fasting rule applies on that day. Published guidance for orientation only, **the institutional
  anaesthesia policy governs**: ASA 2017 (2 h clear liquids, 4 h breast milk, 6 h light meal, 8 h
  fried/fatty meal or solids; 28045707) with the 2023 modular update on carbohydrate-containing clear
  liquids, chewing gum, and paediatric clear-liquid duration (36629465); ESAIC 2022 paediatric (clear fluids
  to **1 h**, breast milk to 3 h, gastric ultrasound as an adjunct; 34857683); ESA 2011 (21712716)
  **[LIT]**. Do not translate these into a fasting order for the rituximab infusion itself **[INFERENCE]**.
- **Hydration is the opposite requirement:** the label calls for *aggressive* IV hydration plus
  anti-hyperuricaemic therapy in patients at high TLS risk — which argues against casual NPO orders on
  rituximab day **[LABEL]** **[INFERENCE]**.
- **Sedating premedication:** diphenhydramine/hydroxyzine cause drowsiness; a second-generation H1 avoids
  it (41989666). Relevant if the same day includes a neurological examination or a procedure.
- **Time budget:** a first 375 mg/m² infusion escalating from 50 mg/h takes roughly 4–6 h plus premedication
  and observation; the 90-minute schedule (cycle 2 onward, steroid-containing regimens, no prior grade 3–4
  IRR) is the label-sanctioned way to shorten it **[LABEL]** **[INFERENCE]**. Schedule accordingly on a day
  that also includes lymphodepletion or a procedure.
- **Chair/observation:** most reactions occur 30–120 min into the first infusion (label; 42530421), so the
  first dose of a course is the one requiring full monitoring capability, not the repeats.

---

## 9. Round checklist

**Before the round**
1. Confirm the CAR construct has **no CD20/RQR8 switch**.
2. HBsAg, anti-HBc, anti-HBs; start antivirals and involve hepatology if either is positive (continue ≥12
   months after the last dose).
3. CBC + differential + platelets, renal/liver panel, electrolytes, phosphate, uric acid, LDH; baseline
   quantitative IgG and B-cell flow.
4. Vaccinations up to date; no live vaccines.
5. TLS risk assessed; hydration and urate-lowering therapy ordered if high risk.
6. Baseline anti-CAR ADA sample per protocol.
7. Confirm rituximab day relative to Cy/Flu day −4 and CAR-T day 0 (day −6/−5 or day −5 per protocol),
   and that no procedure/anaesthesia conflicts with the infusion window.

**Day of infusion**
8. Acetaminophen + H1 antihistamine 30–60 min before; steroid **only** if the CAR-T protocol says so.
9. Dilute to 1–4 mg/mL in NaCl 0.9% or D5W; IV infusion only, no push/bolus.
10. First infusion 50 mg/h (paediatric 0.5 mg/kg/h, max 50 mg/h), escalate every 30 min to max 400 mg/h;
    subsequent infusions start 100 mg/h (paediatric 1 mg/kg/h).
11. No fasting for the infusion; encourage oral intake unless a procedure requires NPO.
12. For any reaction: stop or slow, treat by severity (steroid/epinephrine/bronchodilator/O₂), resume at
    ≤50% of the previous rate after resolution, discontinue for grade 3–4.

**After**
13. Serial CBC through the cytopenia window; consider late-onset neutropenia at 6 weeks–5 months.
14. Serial IgG; IVIG per protocol, timed away from rituximab.
15. PJP/antiviral prophylaxis integrated with the CAR-T program's plan, not a parallel one.
16. Monitor HBV, and keep PML on the differential for new neurology alongside TIAN/ICANS and progression.
17. Anti-CAR ADA and CAR-T persistence at each redose.

---

## 10. Sources

Label: openFDA `drug/label`, Rituxan (rituximab) IV, effective 2025-01-06 — sections 2.1 (important dosing
information, infusion rates), 2.2–2.7 (indication doses), 2.8 (premedication and prophylaxis), 2.9
(administration and storage), boxed warning, 5.1–5.11.

Registry: ClinicalTrials.gov NCT04196413 (Arm D) and NCT06973096 (Cohort B), quoted in
`notes/registry_and_unpublished_evidence.md`.

Literature: `index.tsv` categories `J_admin_premedication_infusion_reactions`,
`K_admin_screening_prophylaxis`, `L_admin_dose_route_pk`, `M_admin_cart_context`,
`N_admin_fasting_procedure`.
