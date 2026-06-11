# GD2 CAR-effector therapy: comprehensive clinical management plan

A clinician-facing synthesis of how every published GD2 CAR-effector trial manages each phase of
treatment, with a **per-section comparison table** across trials. It extends
[`08_clinical_formulation.md`](08_clinical_formulation.md) (formulation/dose focus) and is indexed
to the lab registry in [`10_trial_index_by_lab.md`](10_trial_index_by_lab.md).

## How to read this document
Each section states the **principle**, gives a **comparison table** (trials as columns/rows), and
ends with a **practical recommendation** distilled from the cross-trial experience. Cells marked
**NR** = not reported in available sources; **n/a** = not applicable to that product.

### Trial key (used in all tables)

| Short name | Trial / product | Lab | Lead refs (PMID) |
| --- | --- | --- | --- |
| **Baylor-1G** | NCT00085930, 1st-gen GD2 CAR-CTL/ATC | Baylor CAGT | 21984804; 39962287 |
| **GRAIN** | NCT01822652, iC9-GD2-CAR3 (±pembrolizumab) | Baylor CAGT | 28602436 |
| **GINAKIT2** | NCT03294954, GD2-CAR.15 **NKT** | Baylor CAGT | 33046868; 37188782; 39800376 |
| **GD2-CART01** | NCT03373097, 3rd-gen + iCasp9 | Bambino Gesù | 37018492; 40841488 |
| **ALLO-CART01** | ALLO_GD2-CART01 (allogeneic) | Bambino Gesù | 39815015 |
| **Stanford-DMG** | NCT04196413, GD2CART IV+ICV | Stanford | 35130560; 39537919 |
| **1RG-CART** | NCT02761915, 2nd-gen + RQR8 | UCL/GOSH | 33239386 |
| **4SCAR-GD2** | NCT02765243, 4th-gen lentiviral | Chang/Zhujiang | 34724115 |
| **CARPETS** | ACTRN12613000198729, GD2-iCAR-PBT | Adelaide | 38754916 |

Sources: trial PDFs and supplements in this collection, the archived ClinicalTrials.gov protocol
records in [`../protocols/clinicaltrials_gov/`](../protocols/clinicaltrials_gov/), and PubMed
abstracts for paywalled reports (Del Bufalo 2023 NEJM, Locatelli 2025, Straathof 2020).

---

## Section 1 — Patient selection & safety-relevant eligibility

**Principle.** GD2 is expressed on normal neurons/peripheral nerve, so the main *a priori* safety
concern is on-target/off-tumor neurotoxicity; CNS-tumor trials add the risk of inflammation in a
space-constrained compartment. Eligibility rules therefore encode anatomical and physiologic
guardrails.

| Item | GD2-CART01 / ALLO-CART01 | Stanford-DMG | GINAKIT2 | 1RG-CART | CARPETS |
| --- | --- | --- | --- | --- | --- |
| Age | 1–25 y (18 mo–25 y allo) | 2–60 y (NCT04196413; treated pts pediatric–young adult) | 1–21 y r/r NB | ≥1 y | adults, metastatic melanoma/solid |
| Disease | high-risk r/r NB (+ exploratory GD2+ solid) | H3K27M+ DIPG / spinal DMG | r/r NB | r/r NB | metastatic GD2+ melanoma & solid |
| Safety-driven exclusions | severe prior Cy/Flu toxicity; uncontrolled infection; steroids ≥2 mg/kg within 2 wk | **excluded bulky thalamic/cerebellar tumours** (herniation risk) | severe prior Cy/Flu toxicity; inadequate organ function | adequate organ/marrow function | adequate organ function; off steroids |
| Performance status | adequate organ/marrow function | Karnofsky/Lansky ≥60% | adequate organ/marrow function | NR | ECOG-based |
| CNS device requirement | n/a (IV) | **Ommaya/ICP-monitoring device required in DIPG** | n/a | n/a | n/a |

**Recommendation.** For CNS-delivered GD2 CAR-T, exclude bulky tumours that cannot tolerate
inflammatory swelling, mandate an ICP-monitoring/CSF-access device before infusion, and require a
steroid washout (steroids blunt CAR expansion). For systemic NB trials, the binding constraints
are organ function and prior conditioning tolerance, not GD2 biology per se.

---

## Section 2 — Bridging therapy (manufacturing window)

**Principle.** Autologous manufacture takes ~2–3 weeks; aggressive disease may need control
without compromising the apheresis product or CAR fitness.

| Trial | Manufacturing window | Bridging allowed | Notes |
| --- | --- | --- | --- |
| Stanford-DMG | ~2 wk (Prodigy, day-7 cryopreserve) | local therapy only — re-irradiation allowed (resume ≥4 wk after); **no** non-protocol systemic chemo/targeted/immuno | tightest rules; a spinal-DMG patient progressed during manufacture → treated under eIND |
| GD2-CART01 | standard autologous | per protocol; lymphocyte collection **at diagnosis** improved outcomes | Locatelli 2025: best results when apheresis taken early |
| GINAKIT2 | NKT expansion to clinical scale | per protocol | low NKT frequency historically limiting; product 94.7±3.8% pure |
| ALLO-CART01 | n/a — allogeneic, made for lymphopenic patients who **cannot** generate autologous product | donor-derived avoids window | rationale: profound lymphopenia after prior lines |
| CARPETS | autologous PBT | standard of care between apheresis and infusion | |

**Recommendation.** Collect lymphocytes **early** (ideally at diagnosis) for the fittest product;
restrict bridging to local measures (RT, cyst drainage) where possible; reserve an allogeneic
product for patients who cannot manufacture autologously.

---

## Section 3 — Lymphodepletion (LD)

**Principle.** Cy/Flu LD improves CAR expansion/persistence. Intensity is titrated against
toxicity; CNS-delivered (ICV) doses are given **without** systemic LD.

| Trial | LD regimen | Schedule | Notes |
| --- | --- | --- | --- |
| Baylor-1G | **none** | — | 1st-gen, no conditioning; relied on EBV-CTL persistence |
| GRAIN | Cy 500 mg/m²/d ×3 (d−4,−3,−2) + Flu 30 mg/m²/d ×2 (d−4,−3) (+ pembrolizumab d+1, d+21) | d−4…−2 | doses per Heczey 2017; **NCT01822652 lists the reverse (Cy ×2 / Flu ×3)**; <12 kg dosed by weight |
| GINAKIT2 | **fractionated** Cy 500 mg/m²/dose ×2 + Flu 30 mg/m²/dose ×3 | per protocol §7.2 | grade 3–4 cytopenias attributed to Cy/Flu, pre-infusion; Etanercept arm adds CRS prophylaxis |
| GD2-CART01 | Cy + Flu, conventional doses | per NEJM appendix | exact doses in NEJM protocol (not OA) |
| ALLO-CART01 | standard Cy/Flu | — | donor product |
| Stanford-DMG | Cy 500 mg/m²/d + Flu 25 mg/m²/d ×3 (published cohorts); **+ Rituximab 750 mg/m²/d d−6,−5 in a separate ctgov LD arm (ARM D)** | d−4…−2 (IV) | rituximab regimen from NCT04196413 only, not in Majzner 2022/Monje 2025 text; **no LD before ICV redoses**; first ICV (eIND) used intensified Cy 600 + Flu 30 ×4 (d−5…−2) |
| 1RG-CART | **phased escalation of LD intensity** (not cell dose) across cohorts | per cohort | unique design: dose-escalate the *conditioning*, fixed-ish cells |
| 4SCAR-GD2 | Cy 300 mg/m²/d + Flu 25 mg/m²/d ×3 | d−4…−2 | lower Cy than most |
| CARPETS | cohort 1 none; cohorts 2–3 Cy 500 + Flu 30 mg/m²/d ×3 | d−4…−2 | LD added specifically to boost expansion |

**Recommendation.** Default to **Cy 500 / Flu ~25–30 mg/m²/d × 3** for systemic products; add
**rituximab** if the construct carries a depletable B-cell epitope and redosing is planned;
**omit LD entirely for ICV administration**. Counsel that grade 3–4 cytopenias are usually LD-,
not CAR-, attributable.

---

## Section 4 — Dose, route & dose-escalation / DLT definitions

**Principle.** Most trials use 3+3 escalation with a 28-day (some 6-week) DLT window. Route is IV
for systemic disease; Stanford pioneered **IV→ICV** for CNS disease.

| Trial | Route | Dose levels (CAR+ cells) | RP2D / MTD | DLT window |
| --- | --- | --- | --- | --- |
| Baylor-1G | IV | 3 DLs: 2×10⁷, 5×10⁷, 1×10⁸ /m² (CAR-CTL + CAR-ATC co-infused) | no DLT (Louis 2011) | 15-yr safety follow-up |
| GRAIN | IV | DL1 1×10⁷ → up to 2×10⁸/m² (fresh) | no DLT | 6 wk |
| GINAKIT2 | IV | DL1 3×10⁶/m² → ~3-fold steps to DL5 3×10⁸/m² (± etanercept) | MTD not reached | 28 d |
| GD2-CART01 | IV | 3, 6, 10 ×10⁶ CAR+/kg | **RP2D/MTD 10×10⁶/kg** | 4 wk |
| ALLO-CART01 | IV | up to 10×10⁶/kg (selected 3×10⁶/kg start) | individualized | per protocol |
| Stanford-DMG | **IV then ICV** | IV DL1 1×10⁶/kg, DL2 3×10⁶/kg; ICV 10–50×10⁶ flat (redosed) | DL1 IV declared; ICV redosing program | 28 d |
| 1RG-CART | IV | 1×10⁷ → 1×10⁸/m² (with escalating LD) | clinical activity at ≥10⁸/m² | per cohort |
| 4SCAR-GD2 | IV | infused 0.13–34 ×10⁶/kg (wide) | NR | 1 yr AE capture |
| CARPETS | IV | DL1 1×10⁷/m², DL2 2×10⁷/m², DL3 1×10⁸/m² | no DLT | 42-d DLT window |

**Stanford DLT definition (representative, Monje 2025):** any grade 5; grade 4 CRS; grade 4
neurotoxicity ≥96 h; new grade 3 neurotoxicity ≥28 d; grade 4 neutropenia/thrombocytopenia >28 d;
≥grade 3 non-haematologic toxicity (with protocol exceptions). Redosing eligibility required CAR
<5% circulating, ≥21–28 d since last dose, and toxicity resolved to <grade 2.

**Recommendation.** Use a 3+3 with a 28-day window and an explicit carve-out that expected,
reversible CNS-inflammation events are managed (not automatically DLT-defining) — Stanford's
experience shows TIAN would otherwise halt an effective program. For CNS disease, plan **ICV
redosing** with predefined re-treatment thresholds.

---

## Section 5 — Cytokine release syndrome (CRS)

**Principle.** GD2 CAR-T CRS is generally **milder and less frequent** than CD19 CAR-T, but rises
with potency (3rd-gen, IL-15 armoring) and dose. Grade with ASTCT/Lee criteria; treat with
anti-IL-6 ± anti-IL-1 ± steroids; reserve the suicide switch for refractory grade 4.

| Trial | CRS incidence | Severity | First-line management | Escalation |
| --- | --- | --- | --- | --- |
| Baylor-1G | essentially none | low-grade fever only | supportive | — |
| GRAIN | 1 patient (1C) | ≤ grade 2 | none needed (spontaneous resolution) | — |
| GINAKIT2 | low | grade 2 in 1/12 (Heczey 2023) | **tocilizumab** (resolved) | anakinra (hyperleukocytosis case) |
| GD2-CART01 | **20/27 (74%)** | mild in 19/20 (95%) | anti-cytokine + steroids | **iCasp9 (rimiducid) activated in 1 patient → grade 4 CRS aborted** |
| Stanford-DMG (IV) | all patients post-IV | DL1 grade 2 in 1/3; DL2 ≥grade 2 in 6/8; **3 DLT grade 4 CRS at DL2** | tocilizumab, anakinra, steroids; vasopressors/resp support | grade 4: CPAP/intubation; iCasp9 available |
| Stanford-DMG (ICV) | 41/62 infusions no CRS (66%) | mostly grade 1 (16); rare grade 2–3 | supportive | ICV markedly less systemic CRS than IV |
| 1RG-CART | 2/6 at ≥10⁸/m² | grade 2–3 | per institutional guideline | — |
| 4SCAR-GD2 | 9/10 | grade 1–2 (transient) | supportive | capillary-leak in 4/10 |
| CARPETS | grade 1 CRS in 5/12 | grade 1 fever <48 h | supportive | no DLT |

**Recommendation.** Stratify CRS watch by potency/route: low-intensity vigilance for 1st/2nd-gen
IV NB products; **ICU-level readiness at DL2+ for 3rd-gen/IL-15 or high IV doses**. Standard ladder
= tocilizumab → anakinra → corticosteroids; **the iCasp9 suicide switch is the proven backstop for
refractory grade 4 CRS** (clinically demonstrated in GD2-CART01). ICV delivery substantially
reduces systemic CRS.

---

## Section 6 — ICANS (immune effector cell-associated neurotoxicity) vs TIAN

**Principle.** Two distinct CNS toxicities must be separated: classic **ICANS** (diffuse
encephalopathy, ICE score) and **TIAN** — *tumour inflammation-associated neurotoxicity* — local
inflammation at CNS tumour sites (Stanford-defined). They can co-exist and require different
management.

| Trial | ICANS | TIAN | Distinguishing management |
| --- | --- | --- | --- |
| Stanford-DMG | DL1 grade 2 (1/3); DL2 grade 3 (1), grade 1 (3); a grade 4 ICANS after intensified ICV | **91% after IV, 100% after first ICV**; grade typically falls with subsequent infusions; no DLT due to TIAN | ICANS → anti-cytokine/steroids; TIAN → see Section 7 algorithm |
| GD2-CART01 | **grade 3 ICANS in 4 children (Locatelli 2025)** | n/a (systemic NB) | grade 3 ICANS **rapidly controlled by iCasp9/rimiducid activation** |
| 4SCAR-GD2 | **no central neurotoxicity** | n/a | — |
| GINAKIT2 / GRAIN / Baylor-1G | none significant | n/a | — |

**Recommendation.** In CNS trials, pre-specify both ICANS and TIAN grading and **monitor ICP
routinely** (not only symptom-prompted). For systemic NB, the GD2-CART01 experience shows the
**iCasp9 switch terminates grade 3 ICANS quickly** — keep rimiducid immediately available.

---

## Section 7 — TIAN management algorithm (CNS-delivered GD2 CAR-T)

**Principle.** TIAN has two categories (Majzner 2022; Monje 2025):
1. **ICP/space-constraint TIAN** — oedema/CSF-flow obstruction → potential herniation; a
   neuro-critical-care emergency.
2. **Local-dysfunction TIAN** — transient worsening of pre-existing deficits at the tumour site;
   usually managed conservatively unless it threatens respiratory drive.

**Pre-emptive measures built into the Stanford protocol:**
- Place an **Ommaya/ICP device in all DIPG patients** before treatment.
- **Scheduled + symptom-prompted ICP measurement** and serial neuro exams; inpatient through
  toxicity resolution.
- Exclude bulky thalamic/cerebellar tumours.

**Acute TIAN ladder (escalating):**

| Step | Intervention | Trigger |
| --- | --- | --- |
| 1 | Positioning; **3% hypertonic saline** | elevated ICP |
| 2 | **CSF removal via Ommaya** | documented raised ICP / acute deterioration (e.g., ICP 22 mmHg → drain 10 mL → return to baseline in minutes) |
| 3 | **Anakinra** (IL-1R antagonist) + corticosteroids | significant neurological symptoms |
| 4 | **Tocilizumab** for concurrent CRS; siltuximab/dasatinib in select cases | systemic inflammatory component |
| 5 | External ventricular drain for refractory hydrocephalus | obstructive hydrocephalus |
| 6 | **iCasp9 (rimiducid) activation** | life-threatening, refractory toxicity |

Worked per-patient anti-inflammatory schedules (tocilizumab/dexamethasone/methylprednisolone/
anakinra/dasatinib/siltuximab by day post-infusion) are tabulated in the Majzner 2022 supplement
(`supplements/35130560_PMC8967714/41586_2022_4489_MOESM4_ESM.docx`, Supplementary Table 3).

**Recommendation.** Treat ICP-category TIAN as a neuro-emergency with immediate CSF drainage and
hypertonic saline; treat local-dysfunction TIAN conservatively. Anakinra + steroids are the CNS
anti-inflammatory backbone (steroids are acceptable here, unlike during expansion). TIAN diminishes
with successive ICV doses — it should not by itself terminate an effective program.

---

## Section 8 — On-target/off-tumor toxicity & GD2 neuropathic pain

**Principle.** Unlike the anti-GD2 antibody dinutuximab (which causes severe neuropathic pain in
most children), GD2 CAR-T has shown **little/no on-target off-tumor pain** — attributed to the
high antigen-density threshold for CAR effector function.

| Trial | On-target pain / neuropathy | Assessment | Comment |
| --- | --- | --- | --- |
| Baylor-1G | mild local pain only; no antibody-type neuropathic pain | NCI pain scale | foundational safety signal |
| Heczey 2017 (GRAIN) | no severe pain / CNS pain | CTCAE v4 | explicitly contrasts with dinutuximab |
| Stanford-DMG | **no on-target off-tumor toxicity**; no painful neuropathy | neuro exam | autopsy: differential GD2 in tumour vs normal brain |
| GINAKIT2 | no DLT from peripheral-nerve targeting | FACES/objective pain at each visit (protocol) | |
| 4SCAR-GD2 | neuropathic pain in 3/10, transient/mild | CRS+pain grading | |
| 1RG-CART | activity "without on-target off-tumor toxicity" | — | STM title emphasizes this |

**Recommendation.** Assess pain objectively at every visit (FACES for young children). Expect
GD2 CAR-T pain to be far milder than dinutuximab; persistent severe pain should prompt evaluation
for an alternative cause. Have corticosteroids/anti-T-cell antibody (e.g., alemtuzumab) or the
suicide switch available should true on-target normal-tissue toxicity emerge.

---

## Section 9 — Hyperleukocytosis / HLH-MAS (IL-15–armored NKT specific)

**Principle.** IL-15 transgene armoring boosts persistence/potency but adds a proliferative-toxicity
risk. The GINAKIT2 program documented a **lethal non-clonal hyperleukocytosis** at the highest dose
level (Tian 2025) — a critical management case report.

| Element | Detail (Tian 2025, GINAKIT2 DL5) |
| --- | --- |
| Setting | first patient on DL5 (**3×10⁸ NKT/m²**; DL4 was 1×10⁸/m²) |
| Course | CRS → tocilizumab (d7) → anakinra (d8); progressive hyperleukocytosis; ICU transfer; **leukapheresis d18**; death same day |
| Mechanism | non-clonal hyperleukocytosis, hyperinflammation; autopsy-confirmed |
| Protocol consequence | prompted **dose-level revision** of the IL-15 NKT program |

**Recommendation.** For IL-15–armored products, monitor WBC/blast counts and ferritin/HLH markers
daily during expansion; pre-specify hyperleukocytosis thresholds triggering anti-cytokine therapy
**and** leukapheresis early; cap dose escalation conservatively. Keep the suicide switch on hand.

---

## Section 10 — Safety-switch / cell-ablation strategy

**Principle.** Most modern GD2 CAR products embed an inducible kill switch; design differs by lab,
and **two mechanisms have proven clinical utility**.

| Trial | Switch | Trigger drug | Clinical activation reported? |
| --- | --- | --- | --- |
| GD2-CART01 / ALLO-CART01 | **iCasp9** | rimiducid (AP1903) | **Yes** — grade 4 CRS (Del Bufalo 2023, n=1) and grade 3 ICANS (Locatelli 2025, n=4) aborted |
| Stanford-DMG | iCasp9 | rimiducid (AP1903) | available; not required at DL1 |
| GRAIN / GINAKIT2 (partial) / CARPETS / 4SCAR-GD2 | iCasp9 | rimiducid (AP1903) | not triggered in reports |
| 1RG-CART | **RQR8** (CD20/CD34 epitope) | **rituximab** | depletion strategy; enables redosing too |
| Baylor-1G | none | — | relied on CTL contraction |

**Recommendation.** Prefer an embedded suicide switch for potent/armored or allogeneic products.
**iCasp9/rimiducid is the only mechanism with published clinical evidence of rapidly aborting
severe GD2 CAR-T toxicity** while preserving the option of clinical benefit; ensure rimiducid is
stocked on-site before the first infusion.

---

## Section 11 — Anti-cytokine, premedication & concomitant medication

| Category | Agents used across trials |
| --- | --- |
| Infusion premedication | paracetamol/acetaminophen, diphenhydramine; ± low-dose methylprednisolone |
| CRS prophylaxis (GINAKIT2 arm) | **etanercept** (anti-TNF) with NKT product |
| Anti-cytokine treatment | **tocilizumab** (IL-6R), **anakinra** (IL-1R), **siltuximab** (IL-6) |
| Corticosteroids | dexamethasone, methylprednisolone — deferred during expansion, used for CNS/severe CRS |
| Adjuncts | **dasatinib** (also a pharmacologic CAR "off-switch"/fitness aid), hypertonic saline (CNS) |
| Combination/checkpoint | **pembrolizumab** (GRAIN, CARPETS cohort 3) |
| Seizure prophylaxis | per standard supportive care in CNS trials (Stanford) |

**Recommendation.** Standardize infusion premedication; **avoid corticosteroids during the
expansion window** unless needed for severe CRS/CNS toxicity; have tocilizumab + anakinra at the
bedside; in CNS trials add seizure prophylaxis and hypertonic saline to the order set.

---

## Section 12 — Hematologic toxicity, cytopenias & infection prophylaxis

| Trial | Notable hematologic/infectious findings | Supportive care |
| --- | --- | --- |
| GINAKIT2 | grade 3–4 cytopenias = **Cy/Flu-attributable** (pre-infusion) | filgrastim, transfusion per institution |
| GD2-CART01 | cytopenias within expected LD range; no new safety signals (final) | standard |
| Stanford-DMG | grade 4 neutropenia/thrombocytopenia >28 d is DLT-defining | inpatient supportive care |
| 4SCAR-GD2 | grade 3–4 hematologic AEs most common, post-Cy/Flu | supportive |
| CARPETS | grade 1–2 LD-related GI/marrow effects | supportive |

**Recommendation.** Attribute most early cytopenias to LD, not the CAR; provide G-CSF/transfusion
support and standard antimicrobial prophylaxis for the lymphodepleted period; flag prolonged
(>28 d) grade 4 cytopenias as protocol-defined DLTs.

---

## Section 13 — ICV administration & device management (CNS programs)

| Element | Stanford-DMG practice |
| --- | --- |
| Access | Ommaya reservoir (also used for ICP monitoring/CSF drainage) |
| LD before ICV | **none** |
| ICV dose | 10–50 ×10⁶ flat (typically 30×10⁶ or weight-based DL1, whichever lower) |
| Redosing cadence | ≥21–28 d apart, when CAR <5% circulating and toxicity <grade 2 |
| Toxicity profile | far less systemic CRS than IV; TIAN still expected but attenuates over doses |

**Recommendation.** ICV delivery is a viable repeat-dosing route for CNS GD2 CAR-T: no LD, smaller
flat doses, frequent redosing, and lower systemic CRS — but it requires an indwelling device and
the full TIAN monitoring apparatus.

---

## Section 14 — Redosing / retreatment criteria

| Trial | Redosing? | Criteria |
| --- | --- | --- |
| Stanford-DMG | **yes (ICV, multiple)** | response/SD or clinical benefit; ≥21–28 d; CAR <5%; toxicity <grade 2 |
| GD2-CART01 | single infusion (phase 1/2 primary) | persistence ≥12 mo in 64% reduces redosing need |
| Baylor-1G | dual product (CTL + ATC) at one timepoint | — |
| GRAIN | ± pembrolizumab to enhance/prolong | re-evaluate at 6 wk |
| 1RG-CART | rituximab-ablatable design supports controlled redosing | — |

**Recommendation.** Build explicit redosing thresholds (response/benefit + low circulating CAR +
resolved toxicity). For CNS disease, plan **serial ICV** dosing from the outset.

---

## Section 15 — Monitoring & long-term follow-up

| Element | Practice across trials |
| --- | --- |
| Acute monitoring | inpatient through CRS/neurotoxicity resolution; routine ICP in CNS trials |
| Cellular kinetics | qPCR/flow for CAR persistence (GD2-CART01: detectable up to 30 mo, median 3 mo; persistence ≥12 mo in 64% correlated with outcome) |
| Response assessment | RECIST/Curie/INRC (NB); MRI ± clinical neuro score (DMG); +28 d radiologic checkpoint |
| Gene-therapy follow-up | **15-year** RCR/long-term follow-up (retroviral/lentiviral products); Baylor-1G now reports **up to 18 years** |

**Recommendation.** Enroll all integrating-vector recipients in 15-year LTFU; track CAR persistence
as a pharmacodynamic biomarker (greater persistence tracked with durable benefit in both the Baylor
1st-gen and GD2-CART01 cohorts).

---

## Section 16 — Master comparison matrix

| Domain | Baylor-1G | GRAIN | GINAKIT2 | GD2-CART01 | Stanford-DMG | 1RG-CART | 4SCAR-GD2 | CARPETS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Generation | 1G | 3G | 2G+IL15 (NKT) | 3G | 2G(4-1BB) | 2G(4-1BB) | 4G | 3G |
| Route | IV | IV | IV | IV | IV→ICV | IV | IV | IV |
| LD | none | Cy/Flu | frac. Cy/Flu | Cy/Flu | Cy/Flu(+RTX); none for ICV | phased Cy/Flu | Cy(300)/Flu | none→Cy/Flu |
| Safety switch | none | iCasp9 | iCasp9(partial) | iCasp9✚ | iCasp9 | RQR8/RTX | iCasp9 | iCasp9 |
| CRS | none | ≤G2 (1pt) | G2 (1/12); 1 fatal hyperleuk. | 74%, 95% mild | up to G4 (DLT) IV | G2–3 2/6 | G1–2 9/10 | G1 |
| ICANS/CNS | none | none | none | **G3 ICANS×4** | ICANS + **TIAN** | none | none | none |
| On-target pain | mild | none | none | NR | none | none | G1–2 (3/10) | NR |
| Switch fired? | — | no | no | **yes** | no(DL1) | (RTX design) | no | no |
| Efficacy snapshot | 18-yr CRs | activity | ORR 25% | ORR 63–66%, 5-yr OS 42–68% | 3/4→benefit; ICV benefit | regressions, no RECIST CR | responses | SD/responses |

---

## Section 17 — Distilled clinical-management protocol (cross-trial best practice)

1. **Select & prepare:** confirm GD2 expression; exclude space-constrained bulky CNS tumours;
   washout steroids; collect lymphocytes early; place ICP device for CNS delivery.
2. **Bridge** with local therapy only where possible.
3. **Lymphodeplete** with Cy 500 / Flu 25–30 mg/m²/d × 3 (add rituximab if a depletable epitope is
   present and redosing is planned); **no LD for ICV**.
4. **Infuse** at the RP2D (10×10⁶/kg is the best-validated systemic dose, from GD2-CART01); for CNS
   disease, IV prime then serial ICV.
5. **Monitor** inpatient with ASTCT CRS/ICANS grading; add routine ICP and TIAN grading for CNS.
6. **Treat toxicity** stepwise: tocilizumab → anakinra → corticosteroids for CRS; the TIAN ladder
   (hypertonic saline → CSF drainage → anakinra/steroids) for CNS; reserve **iCasp9/rimiducid** for
   refractory grade 4 CRS or grade 3 ICANS (clinically proven to abort both).
7. **Watch IL-15 products** for hyperleukocytosis/HLH — escalate to anti-cytokines + early
   leukapheresis.
8. **Redose** on predefined response + low-CAR + resolved-toxicity criteria (serial ICV for CNS).
9. **Follow up** for 15 years; use CAR persistence as a pharmacodynamic readout.

---

*Provenance:* every quantitative claim traces to a paper PDF/supplement in this collection, the
archived ClinicalTrials.gov records, or the cited PubMed abstract. Paywalled full texts
(NEJM/Nature/STM) are represented by their abstracts plus, where available, local supplements;
fields not recoverable from open sources are marked **NR**.
