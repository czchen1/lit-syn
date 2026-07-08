# Preclinical efficacy, synthetic lethality, combinations & resistance

## The dependency map (why a tumor responds)
1. **EZH2 gain-of-function mutation** (Y641F/N/S/H/C, A677G, A687V) — germinal-center
   B-cell lymphomas (FL, DLBCL). Mutants over-produce H3K27me3 → addiction to PRC2.
   Basis of the FL approval; Gibaja 2016 (in-corpus) characterizes secondary
   mutants and PRC2 kinetics (PRC2^Y641N/Y661D altered SAM Km).
2. **SWI/SNF (BAF) loss → EZH2 synthetic lethality** — the strongest solid/CNS
   rationale:
   - **SMARCB1/INI1 loss:** ATRT, malignant rhabdoid tumor, epithelioid sarcoma.
   - **SMARCA4 (BRG1), ARID1A, PBRM1 loss:** e.g. Passeri 2022 (in-corpus) shows
     dramatic in vivo tazemetostat efficacy in a **PBRM1-mutant chordoma** xenograft.
   Mechanism: residual PRC2 activity is unopposed when BAF is crippled, so PRC2
   inhibition restores balance.
3. **Lineage/context dependence in CNS gliomas** — DMG/DIPG (H3K27M) and H3G34 do
   not carry EZH2 GOF; dependence is context-specific and usually needs
   **combinations** (below).

## Preclinical efficacy highlights in corpus
- **Lymphoma:** Knutson 2014 (EPZ-6438) — potent regression of EZH2-mutant NHL
  xenografts; the template for the class.
- **ATRT / rhabdoid:** tazemetostat active in INI1-negative models and pediatric
  rhabdoid tumors (Vejmelkova 2023); glutamine-metabolism targeting synergizes
  (Nakata 2020, ATRT).
- **DIPG/DMG:** EPZ-6438 + **HDACi (vorinostat)** + **ONC201/TIC10** activate the
  integrated stress response/DR5 and reduce H3K27 methylation (Zhang 2021);
  imipridone-driven EZH1/2 downregulation predicts synergy with EZH1/2i or HDACi in
  diffuse glioma (2025).
- **Glioblastoma:** EZH2 inhibition → **ferroptosis** in resistant GBM stem cells
  (2026); + **radiation** (miR-217 nanomiR, 2024); + **5-azacytidine (DNMTi)** →
  viral-mimicry immune activation in PTEN-deficient GBM (2025).
- **Medulloblastoma (Group 3, MYC):** EZH2 inhibition lowers **B7-H3**, an
  immunotherapy-combination angle (2023).
- **Solid tumors:** chordoma (PBRM1, Passeri 2022), biliary tract (Bekric 2023),
  BRAF^V600E thyroid + MAPKi (Fu 2020) — breadth of the synthetic-lethal thesis.

## Combination logic (recurring, corpus-supported)
- **EZH2i + HDACi** — cooperative chromatin de-repression (DIPG, diffuse glioma).
- **EZH2i + DNMTi (5-aza)** — reprogram the H3K27me3/DNAme onco-epigenome; viral
  mimicry / immune activation (GBM, myeloma).
- **EZH2i + ONC201/imipridones** — ISR/DR5 apoptosis in DMG.
- **EZH2i + immune checkpoint / immune modulation** — EZH2i upregulates antigen
  presentation and chemokines (e.g. tazemetostat ↑ CCL17/TARC and T-cell
  recruitment, Yuan 2021), and lowers immune-evasion targets (B7-H3), supporting
  I-O combinations.
- **EZH2i + AR-axis (enzalutamide/abiraterone)** — mCRPC (mevrometostat Ph3;
  CPI-1205 ProSTAR).
- **EZH2i + radiation / metabolism (glutamine, ferroptosis)** — CNS models.

## Resistance & next-generation chemistry (resistance/SAR bucket)
- **Acquired secondary EZH2 SET-domain mutations** reduce SAM-competitive inhibitor
  binding — the canonical on-target resistance route.
- **PRC2-independent escape** (rewiring away from EZH2 dependence).
- **Countermeasures represented in the corpus:**
  - **Allosteric EED inhibitors (EED226, A-395, MAK683):** bind the H3K27me3 pocket,
    **retain activity against catalytic-site-mutant / EZH2i-resistant cells**.
  - **Dual EZH1/2 inhibition (valemetostat, UNC1999):** removes EZH1 compensation.
  - **EZH2 degraders / PROTACs:** remove the protein (and its non-catalytic
    scaffolding functions) rather than just the enzyme activity — an active
    medicinal-chemistry direction (degrader/PROTAC papers in the resistance/SAR
    bucket, e.g. brain-metastasis-focused PROTAC work, Shi 2024).
  - **Brain-penetrant analog design** to fix the CNS-exposure "resistance by
    pharmacology" (the 2021 brain-penetrant EZH2i med-chem paper).

## Synthesis
Preclinically, EZH2 inhibitors are **broadly active where the dependency is real**
(EZH2-GOF lymphoma; SWI/SNF-loss solid/CNS tumors) and **combination-dependent in
gliomas**. The frontier is (a) **overcoming resistance** with EED-allosteric agents,
dual EZH1/2 inhibitors, and degraders, and (b) **delivering drug to brain** — the
two threads that determine whether the strong CNS-tumor biology translates into
clinical benefit for the tumors this repo studies.
