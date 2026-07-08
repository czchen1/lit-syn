# Clinical data — trials, approvals, response rates, safety

## Approvals (the two anchors)
- **Tazemetostat (Tazverik, Epizyme/Ipsen) — FDA-approved 2020, two indications:**
  1. **Metastatic/locally advanced epithelioid sarcoma** (Jan 2020) — the first
     approval, on the basis of **INI1/SMARCB1 loss** synthetic lethality; ORR ≈
     **15%** in the pivotal cohort but with durable responses in a disease with few
     options.
  2. **Relapsed/refractory follicular lymphoma** (Jun 2020) — accelerated approval;
     **EZH2-mutant** cohort ORR ≈ **69%** vs ≈ **35%** in EZH2-wild-type
     (E7438-G000-101 / Study 101; multiple corpus papers analyze this trial,
     e.g. Proudman 2022, Izutsu 2021, Munakata 2021). Well-tolerated oral dosing
     (800 mg BID); this cohort is the clearest demonstration that **GOF EZH2
     mutation predicts response**.
- **Valemetostat (Ezharmia, Daiichi Sankyo) — approved in Japan:**
  - **Relapsed/refractory adult T-cell leukemia/lymphoma (ATL)** — 2022; and
  - **Relapsed/refractory peripheral T-cell lymphoma (PTCL)** — 2024.
  Dual EZH1/2 inhibition; meaningful single-agent ORRs in T-cell lymphomas where
  standard options are poor.

## Clinical-stage but not yet approved
- **Mevrometostat (PF-06821497, Pfizer)** — most advanced *solid-tumor combination*
  program: **Phase 3 in metastatic castration-resistant prostate cancer (mCRPC)**
  in combination with **enzalutamide**, built on preclinical AR-pathway/PRC2
  crosstalk rationale. Also explored in SCLC.
- **Tulmimetostat (CPI-0209, Constellation/MorphoSys)** — Phase 1/2 across solid
  tumors and lymphomas; second-generation design emphasizing **prolonged target
  residence time** for deeper PD.
- **CPI-1205 (lirametostat)** — earlier Constellation agent; Phase 1/2 (ProSTAR in
  mCRPC with abiraterone/enzalutamide), largely superseded by CPI-0209.
- **SHR2554 (Jiangsu Hengrui)** — China Phase 1/2, chiefly **relapsed/refractory
  lymphoma** (and combinations, e.g. with the PD-L1 agent SHR-1316); encouraging
  early single-agent activity in mature T/B-cell lymphomas.
- **GSK126 (GSK2816126)** — Phase 1 in lymphoma/solid tumors **terminated**:
  insufficient exposure/activity at tolerated doses (solubility/PK), an important
  cautionary datapoint that potency ≠ clinical success without PK.
- **MAK683 (EED inhibitor, Novartis)** — Phase 1/2 in DLBCL and nasopharyngeal
  carcinoma; validates the **allosteric EED** mechanism clinically.

## Pediatric / CNS-relevant clinical experience
- Tazemetostat has been studied in **pediatric INI1-negative tumors including
  ATRT** (PBTC/company pediatric programs) and **malignant rhabdoid tumors**
  (Vejmelkova 2023, in-corpus): occasional durable responses but **modest overall
  CNS activity**, consistent with the BBB/efflux limits in `02_bbb_penetration.md`.
- No EZH2 inhibitor is approved for a **CNS/brain tumor** indication; DIPG/DMG and
  glioma use remains **investigational and combination-oriented**.

## Safety themes (class + agent-specific)
- **Class:** generally **well-tolerated oral** agents; common AEs are cytopenias,
  fatigue, nausea, alopecia, dysgeusia. Because PRC2 is a broad epigenetic
  regulator, **on-target effects on normal stem/progenitor compartments** are a
  theoretical long-term concern.
- **Tazemetostat:** boxed/again-flagged risk of **secondary malignancies**
  (T-lymphoblastic lymphoma, MDS/AML) seen especially in **pediatric** patients —
  a critical consideration for treating children with brain tumors. **CYP3A**
  substrate → dose adjust with strong 3A inhibitors/inducers.
- **Valemetostat:** cytopenias, alopecia, dysgeusia; manageable in the ATL/PTCL
  programs.
- **GSK126:** exposure-limited (the practical "failure" mode was PK, not toxicity).

## What the clinical data tell us for this repo's CNS focus
The **efficacy that is proven is extracranial and biomarker-driven** (EZH2-mut FL,
SMARCB1-loss sarcoma/rhabdoid, ATL/PTCL). For **brain tumors**, the biology
(SMARCB1-loss ATRT; H3K27M/DMG context dependence; H3G34) supports the target, but
translation is gated by **CNS exposure** and points toward **combination regimens**
and **CNS-optimized/dual EZH1/2 or EED agents** with **documented free-brain PK** —
still the field's key data gap.
