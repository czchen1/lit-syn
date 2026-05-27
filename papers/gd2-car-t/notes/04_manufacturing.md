# GD2 CAR-T manufacturing: apheresis to release

## 1. Source material and selection

### 1.1 Apheresis volume and targets

- Pediatric NB trials (Bambino Gesù GD2-CART01; Heczey 2017 GD2-CAR3; Texas Children's GD2-CAR.15 NKT; Heczey 2020/2023): standard pediatric mononuclear-cell apheresis of 1.5–3 × blood volume.
- Stanford DIPG/DMG trial (Majzner 2022 PMID 35130560; Monje 2025 PMID 39537919): standard apheresis followed by CD4/CD8 immunomagnetic selection on CliniMACS Prodigy.
- TRAC-CAR programs (Cappabianca 2024 PMID 38699288; Mueller 2022 PMID 36382633): apheresis-derived or research-scale Leuko-Pak T cells used directly.

### 1.2 Selection reagents (closed system)

- **CliniMACS Prodigy CD4 / CD8 / CD62L / Pan-T reagents** (Miltenyi): clinical default for the Stanford and Hannover (Glienke) programs.
- **CD45RA depletion** (anti-CD45RA microbeads) — used in TSCM-enrichment strategies in select preclinical papers.
- **iNKT-specific magnetic microbeads** (Miltenyi) — Heczey 2020/2023 GINAKIT trial for NKT enrichment.

## 2. Activation

| Reagent | Representative papers | Notes |
| --- | --- | --- |
| Plate-bound OKT3 (mitogenic anti-CD3) + soluble anti-CD28 | Pule 2008 PMID 18978797; Quintarelli 2018 PMID 29872565 | Brenner / Bambino Gesù protocol; 1 µg/mL each; activation 48–72 h before transduction. |
| Soluble OKT3 + IL-2 (PHA in early historic protocols) | Some early NB CAR papers | Largely abandoned in favor of CD3/CD28-based reagents. |
| Anti-CD3/CD28 Dynabeads (Invitrogen/Thermo) | Long 2015 PMID 25939063; Mount 2018 PMID 29662203; Richman 2018 PMID 29180536 | Typical 3:1 bead:cell at activation; removed on day 5. |
| Anti-CD3/CD28 TransAct (Miltenyi) | Glienke 2022 PMID 35401506; Stanford Prodigy programs | Soluble bead-free reagent compatible with Prodigy automation. |
| αGalCer-pulsed irradiated PBMCs | Heczey 2014 PMID 25049283; Heczey 2020/2023 | NKT cell activation. |
| αGalCer-loaded K562 aAPCs | Tian 2025 PMID 40044579 / 39800376 | K562 with mb-cytokines used for secondary CAR-NKT expansion; associated with hyperleukocytosis at high doses. |
| Zoledronate + IL-2 | Capsomidis 2018 PMID 29310916 | Selective expansion of Vγ9Vδ2 γδ T cells. |
| Concanavalin A + IL-2/IL-4 | Capsomidis 2018 PMID 29310916 | Selective expansion of Vδ1 γδ T cells. |
| Phorbol myristate acetate (PMA)/ionomycin | only as a positive control in functional assays | Not used as a clinical activation reagent. |

## 3. Cytokine support during culture

### 3.1 IL-2 era

- Used in Pule 2008 (Methods), Heczey 2014, Heczey 2017 cohort 1, Quintarelli 2018 (one of two arms), Mount 2018, and many other 2008–2017 papers. Typical doses: 100–300 IU/mL (Mount 2018: 40 IU/mL during activation, 300 IU/mL during expansion; Quintarelli 2018: 100 U/mL).
- Documented downsides: bias toward effector-memory and terminal differentiation; risk of capillary-leak in patients if administered systemically.

### 3.2 IL-7 + IL-15 era

- Heczey 2017 (PMID 28602436) compared IL-2 (cohort 1) vs IL-7 + IL-15 (cohorts 2 & 3): "CAR T cell viability, CD4/CD8, and naive memory/effector subset composition were largely unaffected, but in vitro cytotoxicity of the GD2+ NB cell line was increased after this change."
- Quintarelli 2018 (PMID 29872565): IL-7 (10 ng/mL) + IL-15 (5 ng/mL) preserves stem-cell-memory phenotype better than IL-2.
- Glienke 2022 (PMID 35401506): IL-7 (12.5 ng/mL) + IL-15 (12.5 ng/mL) in TexMACS GMP medium throughout the Prodigy 12-day workflow.
- Majzner 2022 / Monje 2025: rhIL-7 (12.5 ng/mL) + rhIL-15 (12.5 ng/mL), Miltenyi reagents.

### 3.3 Dasatinib priming

- Majzner 2022 (PMID 35130560, Methods, lines 1206–1213) and Monje 2025 (PMID 39537919): "the addition of the tyrosine kinase inhibitor dasatinib on days 3 and 5 to improve T cell fitness." Dasatinib transiently silences LCK-proximal kinase signaling, allowing CAR T cells to be transduced and expanded while suppressing tonic exhaustion, then washed out before release.

### 3.4 IL-21 and IL-18 supplementation

- Several preclinical 2020–2025 papers add IL-21 during expansion (typically 25–50 ng/mL) to maintain stem-cell-memory and reduce terminal differentiation.
- IL-18 is used inducibly (TRUCK design) rather than added exogenously in most protocols.

## 4. Transduction

### 4.1 Retroviral

- **Spinoculation on RetroNectin-coated plates**: universal for all retroviral GD2 CAR products. Typical setup: 24-well non-tissue-culture plates pre-coated with 4–10 µg/mL recombinant human RetroNectin (Takara CH-296); 1–2 mL retroviral supernatant per well; spinoculation at 1,000–2,000 × g, 32 °C, 60–90 min; two rounds on consecutive days. Documented in Pule 2008, Heczey 2014, Heczey 2017, Quintarelli 2018, Mount 2018, Majzner 2022, Glienke 2022, Bodden 2023, Tian 2025.
- **Stable PG13 producer cell banks** (Pule 2008, Heczey 2017): clinical-grade supernatant from cGMP-validated PG13 master cell bank. Heczey 2017: "the producer cell clone was validated under Good Manufacturing Practice guidelines. The final viral supplement was stored at −80 °C and tested prior to release for clinical testing."
- **Transient 293GP/Phoenix transfection** (Long 2015, Mount 2018): suitable for preclinical or trial-startup volumes.

### 4.2 Lentiviral

- **Triple- or quadruple-plasmid transient transfection of 293T** in HEK293T or LV-MAX cells with chloroquine (Glienke 2022 PMID 35401506).
- **VSV-G pseudotyping** is universal; some clinical programs use BaEV-LV (baboon endogenous virus envelope) for primary T cells / iPSC-NK lineages.
- **Multiplicity-of-infection control**: Richman 2018 PMID 29180536 used MOI 5–7; Glienke 2022 calibrated to achieve ≤30% CAR positivity ("to avoid cells with multiple integrants") given Prodigy expansion characteristics.

### 4.3 Electroporation (mRNA or RNP)

- Singh 2014 (PMID 25104548) — IVT mRNA encoding GD2-4-1BB-CD3ζ CAR is electroporated for transient CAR expression.
- Mueller 2022 (PMID 36382633), Balke-Want 2023 (PMID 37365642), Cappabianca 2024 (PMID 38699288) — Cas9 RNP + dsDNA donor electroporated on Lonza 4D-Nucleofector at clinical scale. Yields TRAC-targeted KI with 15–34% CAR+ at small scale, scaling to >17% CAR positivity at clinical scale on the Lonza Cocoon.

## 5. Closed-system clinical-scale platforms

| Platform | Vendor | GD2 CAR programs |
| --- | --- | --- |
| CliniMACS Prodigy | Miltenyi Biotec | Stanford DIPG/DMG (Majzner 2022, Monje 2025); Hannover IL-18 TRUCK (Glienke 2022 — full 12-day workflow including CD4/CD8 selection, TransAct activation, lentiviral spinoculation, IL-7/IL-15 expansion, formulation in Maco-Pharma SSP+ bags with 3.33% HSA, cryopreservation) |
| Lonza Cocoon | Lonza | Cappabianca 2024 TRAC-CAR; some preclinical 2025–2026 programs |
| G-Rex (gas-permeable rapid expansion) | Wilson Wolf | Several Baylor/Texas Children's products; static culture vessel allowing high cell density with limited volume |
| Wave / Xuri bioreactor | Cytiva | Earlier Texas Children's programs |

### 5.1 Glienke 2022 Prodigy workflow (representative GMP example)

(Methods, lines 179–230 + Fig 1 legend.)

```
Day -1: Overnight 4 °C storage of leukapheresis bag.
Day 0:   Immunomagnetic enrichment of CD4+ and CD8+ cells. Start of T cell activation
         with CD3/CD28 TransAct beads (day 0–3). Cultivation in TexMACS basal medium
         with rh-IL-7 (12.5 ng/mL) + rh-IL-15 (12.5 ng/mL) + human AB serum until day 5.
Day 1:   Lentiviral transduction (10 mL viral supernatant added to 100 mL culture volume).
Day 3:   Culture wash; switch from static to agitation; bead deactivation.
Day 5:   Switch to AB-serum-free TexMACS for media exchanges.
Days 5–12: IL-7/IL-15-driven expansion under continuous agitation.
Day 12:  Wash and formulate in Maco-Pharma SSP+ (D2) with 3.33% HSA for cryopreservation.
```

## 6. Manufacturing timelines and yields

| Paper | Platform | Time to product | Yield | CAR+ |
| --- | --- | --- | --- | --- |
| Pule 2008 PMID 18978797 | T75 flask, retroviral | ~21 days | sufficient for cohort dose | 35%+ |
| Heczey 2017 PMID 28602436 | 24-well plates → flasks, retroviral | ~10–14 days | dose levels 1×10⁷–1.5×10⁸/m² | typically 20–40% |
| Majzner 2022 PMID 35130560 | CliniMACS Prodigy, retroviral | 7 days | 30×10⁶ or weight-based dose at DL1 | sufficient |
| Monje 2025 PMID 39537919 | CliniMACS Prodigy, retroviral | 7 days (mean) | DL1 1×10⁶/kg IV, DL2 3×10⁶/kg IV | sufficient |
| Glienke 2022 PMID 35401506 | CliniMACS Prodigy, lentiviral IL-18 TRUCK | 12 days | suitable for clinical dose | ≤30% |
| Heczey 2020 PMID 33046868 | Texas Children's CAGT cGMP, retroviral | 9–15 days | 5.6–6.9×10⁸ CAR-NKT | 20–70% |
| Mueller 2022 PMID 36382633 | Research scale, virus-free CRISPR | 9 days | research-scale | TRAC-KI 15–34% |
| Cappabianca 2024 PMID 38699288 | Lonza Cocoon, virus-free CRISPR | ~14 days | clinical-scale | ≥17% CAR+ |

## 7. Formulation, fill, and cryopreservation

- **Cryopreservation media**: 5% DMSO + autologous serum / 5% DMSO + 95% FBS (Richman 2018); CryoStor CS10 (most modern clinical programs); Maco-Pharma SSP+ + 3.33% HSA (Glienke 2022 Prodigy workflow).
- **Storage**: vapor-phase liquid nitrogen at ≤ −150 °C.
- **Final formulation volume**: 50–100 mL per dose for IV; 1–3 mL per ICV (Majzner 2022 / Monje 2025: ICV dosing via Ommaya reservoir, ~3 mL volume).
- **Patient-side thaw**: 37 °C waterbath, immediate IV infusion through 0.45 µm filter; for ICV doses, manual aspiration from Ommaya, ICV instillation.

## 8. Release testing and product characterization

Across the clinical-stage papers in this collection, GD2 CAR-T release criteria typically include:

- **Identity**: CAR expression by anti-idiotype antibody (1A7 for 14g2a; APC- or PE-labeled GD2-Fc fusion for newer constructs). Specification ≥10–20%.
- **Purity**: viability ≥ 70% (7-AAD or Trypan blue); CD3+ ≥ 80%; for NKT products, CD3+Vα24+ ≥ 60% (Heczey 2020/2023).
- **Vector copy number** (VCN, integrated proviral copies per cell) by ddPCR or qPCR, with most products specifying ≤5 copies/cell to limit insertional mutagenesis risk.
- **Endotoxin** ≤ 5 EU/kg patient weight.
- **Sterility** by USP <71> (compendial) or rapid BacT/ALERT 14-day culture; mycoplasma by PCR.
- **Potency**: in-vitro cytotoxicity vs GD2+ NB cell line (LAN-1, CHLA-255, IMR-32, SK-N-AS) at fixed E:T ratios, often paired with IFN-γ ELISA.
- **Replication-competent retrovirus/lentivirus (RCR/RCL)**: 3-week S+L− or PG13 amplification assay; required for all viral-vector products in early-phase trials.
- **Residual β2-microglobulin, residual transposase, residual Cas9** for non-viral / gene-edited products (Mueller 2022; Cappabianca 2024).

## 9. Manufacturing failures and feasibility data

- Locatelli 2025 GD2-CART01 trial (NB phase 1/2): >90% of patients successfully manufactured; one failure attributed to severe lymphopenia at apheresis.
- Majzner 2022 / Monje 2025 GD2-CAR-DMG trials: all enrolled patients manufactured successfully; mean 7-day manufacturing duration; total 20 successful products including 7 re-manufactured for repeat ICV infusions in 13 patients.
- Heczey 2020/2023 CAR-NKT: all manufacturing attempts successful in 12+ patients.
- Cappabianca 2024 / Mueller 2022 virus-free CRISPR: successful manufacturing in all attempts at clinical scale (n=3 donors each at the largest scale).
