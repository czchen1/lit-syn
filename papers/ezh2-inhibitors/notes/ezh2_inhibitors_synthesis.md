# EZH2 inhibitors: synthesis (preclinical → clinical)

## 1. Target biology
EZH2 is the catalytic subunit of Polycomb Repressive Complex 2 (PRC2), which deposits the repressive H3K27me3 mark. EZH2 is oncogenic in two broad modes:
- **Gain-of-function point mutations** (e.g. Y641, A677, A687) that hyper-trimethylate H3K27, characteristic of germinal-center B-cell follicular lymphoma / DLBCL (`20081860`, `21190999`).
- **Overexpression / non-mutant dependency**, first described in metastatic prostate cancer (`12374981`) and driven partly by loss of miR-101 (`19008416`); reviewed in `20104248`.

A distinct axis relevant to this repository: **histone H3 tail mutations dysregulate PRC2**. H3K27M is a dominant-negative PRC2 inhibitor (`23539183`), whereas H3.3-G34 mutations (the DHG-H3G34 focus of the companion collection) have been reported to promote *aberrant* PRC2 activity — providing a rationale to test EZH2 inhibition in H3-mutant glioma. Note the important caveat that EZH2 can also act as a **context-dependent tumor suppressor in diffuse midline glioma** (`35395831`).

## 2. The drug class
- **Tazemetostat (EPZ-6438)** — first-in-class selective EZH2 inhibitor; the only FDA-approved agent. PK/pharmacology in `39642889`.
- **Valemetostat (DS-3201)**, **HH2853** — dual **EZH1/2** inhibitors; broader PRC2 blockade, active in T-cell lymphoma / solid tumors.
- **SHR2554** — selective EZH2 inhibitor in lymphoma trials.
- **Mevrometostat (PF-06821497)** — in phase III combination for prostate cancer.
- **PROTAC degraders** and dual (LSD1, BET, DOT1L, HDAC) combinations are emerging preclinically to address catalytic-inhibitor resistance and non-canonical (scaffolding) EZH2 functions.

## 3. Clinical status
- **FDA-approved indications (both via tazemetostat):**
  - **Epithelioid sarcoma** with INI1/SMARCB1 loss — pivotal phase 2 `33035459`. First EZH2-inhibitor approval; exploits synthetic lethality between SWI/SNF (SMARCB1) loss and PRC2.
  - **Relapsed/refractory follicular lymphoma** — pivotal phase 2 `33035457` (activity in both EZH2-mutant and wild-type disease).
  - Dose-finding basis: first-in-human phase 1 `29650362`.
- **Active trials / expanding indications:**
  - **Valemetostat** — first-in-human NHL phase 1 (`38315003`) and VALENTINE-PTCL-01 in relapsed/refractory peripheral T-cell lymphoma (`39486433`).
  - **SHR2554** — phase 1 mature lymphoid neoplasms (`35772429`) and PTCL (`38190117`).
  - **HH2853** — dual EZH1/2 phase 1 in solid tumors + lymphoma (`40821900`).
  - **Mevrometostat + enzalutamide** — phase III MEVPRO in metastatic prostate cancer (`42108644`).
  - Class-wide safety: systematic review/meta-analysis `39886019`.

## 4. Preclinical themes by indication
- **Lymphoma:** EZH2i is most potent in EZH2-mutant GCB lymphoma (foundational `23051747`); resistance and combinations (DOT1L) in `40009485`, `36798379`.
- **Prostate:** overcomes enzalutamide resistance (`31085587`); dual AR+EZH2 targeting (`32805266`, `38530086`); relevant to neuroendocrine/lineage-plastic disease (`39131727`).
- **Small cell lung cancer:** EZH2–SLFN11 axis governs chemoresistant relapse (`28196596`); EZH2i restores immunogenicity/3D chromatin (`41659399`); PRC2 loss + G9a/GLP vulnerability (`41723269`).
- **Pediatric CNS tumors:**
  - DMG: cholesterol-metabolism synthetic lethality (`35300150`), microglial EZH2 targeting (`34485907`), differentiation therapy (`39818258`) — balanced against tumor-suppressor caveat (`35395831`).
  - Medulloblastoma: EZH2 dependence (`22287205`) and EZH2i + PARP in MYC-high disease (`39562655`).
  - Neuroblastoma: reviewed in `37467626`.

## 5. Combination / immuno-oncology rationale
EZH2 inhibition can de-repress tumor antigens and immune genes and reshape T-cell/Treg biology: improves anti-CTLA-4 efficacy (`29905573`) and combines with 5-azacytidine to boost antitumor immunity in glioblastoma (`40514071`). This antigen-de-repression mechanism directly connects to the companion **GD2 restoration** collection (EZH2i upregulating GD2 for CAR-T/antibody targeting).

## 6. Relevance to the DHG-H3G34 / target-discovery program
- EZH2i is a plausible tool to **de-repress immunotherapy target antigens** (notably GD2) in H3-mutant glioma — see the `gd2-expression-restoration` collection.
- Any therapeutic hypothesis for EZH2i in H3G34 glioma should account for the reported context-dependent tumor-suppressor role in DMG and be validated in G34-specific models.
