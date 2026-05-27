# Cytokine armoring and TRUCK designs in GD2 CAR

## 1. Why arm a GD2 CAR with a cytokine?

GD2+ solid tumors (neuroblastoma, DIPG, melanoma, osteosarcoma) have an immunosuppressive microenvironment with M2-polarized TAMs, MDSCs, low effector cytokine concentrations and limited homeostatic IL-15. Across the field, the dominant rationale for arming a GD2 CAR with a cytokine cassette is:

1. **Improve in-vivo persistence** of the CAR product without systemic cytokine toxicity.
2. **Reprogram the tumor microenvironment** by recruiting / activating other immune effectors (NK, NKT, bystander αβ T).
3. **Counteract tumor-intrinsic suppression** (e.g. PD-L1 induction, T-cell anergy).

## 2. IL-15 armoring

### 2.1 GD2-CAR.15 NKT (Texas Children's, Heczey lab)

- **Construct**: SFG retroviral cassette encoding a GD2 CAR (14g2a-CD28-CD3ζ form) coupled via P2A to soluble IL-15. Detailed in Heczey 2020 (PMID 33046868 main + supplement) and Heczey 2023 (PMID 37188782 supplement).
- **Manufacturing**: iNKT-bead selection from apheresis → αGalCer-pulsed irradiated PBMC stimulation → gamma-retroviral spinoculation → expansion in IL-2 → cryopreservation. Final products: 80–97% NKT purity, 20–70% CAR+, 5–9×10⁸ CAR-NKT total.
- **Clinical effect**: documented in-vivo NKT persistence enhanced compared to CAR alone; circulating CAR-NKT detectable at 8+ weeks; objective responses in 6 of 12 patients. Best response: complete remission in heavily pretreated NB.
- **Safety considerations**: Tian 2025 (PMID 40044579 / 39800376) documented hyperleukocytosis at the highest dose level (DL5, 1×10⁸ CAR-NKT/m²), specifically when K562-based αGalCer-loaded aAPCs (rather than autologous PBMCs) were used for secondary in-vitro stimulation; this drove the recommendation to incorporate an inducible safety switch into the IL-15-armored construct in future protocols.

### 2.2 RD-IL15 superagonist in NK-92 (Bodden 2023, PMID 37686586)

- **Construct**: lentiviral pSIEW vector encodes `hu14.18.28.z_RD-IL15` — a 14.18 (humanized)-CD8α hinge-CD28 TM-CD3ζ CAR followed by P2A and RD-IL15 (an IL-15 fused via a flexible linker to a soluble IL-15Rα sushi domain, producing an autocrine super-agonist).
- **Property**: NK-92/hu14.18.28.z_RD-IL15 cells proliferate without exogenous IL-2 supplementation.
- **Cell killing**: enhanced and IL-2-independent vs CAR-only control. Co-culture with RD-IL15-secreting CAR-NK enhances proliferation of bystander immune cells.

### 2.3 Membrane-bound IL-15 (mbIL-15) co-stimulation

- Several preclinical GD2 CAR-NK papers (Chiavelli 2024 PMID 38302615; Antonucci 2022 PMID 35603195) use K562-aAPC expressing mbIL-15 + 4-1BBL for ex-vivo NK expansion before GD2 CAR transduction, providing functional benefits without inserting the IL-15 transgene into the effector itself.

### 2.4 IL-15 in T cells: less common in GD2 CARs

- Most clinical GD2 CAR-T programs rely on IL-7 + IL-15 supplementation during manufacturing (see Manufacturing note) rather than incorporating IL-15 into the construct. The exception is the Heczey/Cheung NKT lineage.

## 3. IL-18 TRUCK (Glienke 2022, PMID 35401506)

- **Construct**: "all-in-one" lentiviral vector encoding a constitutive 14g2a-CD8α hinge-CD8 TM-4-1BB-CD3ζ GD2 CAR plus an NFAT-responsive promoter driving IL-18. CAR triggering activates NFAT, which then drives IL-18 secretion only in the tumor microenvironment.
- **Manufacturing**: full 12-day CliniMACS Prodigy workflow (see Manufacturing note, §5.1) — CD4/CD8 selection, TransAct activation, lentiviral spinoculation, IL-7/IL-15 expansion, formulation in Maco-Pharma SSP+ with 3.33% HSA.
- **Rationale**: IL-18 reprograms TAMs and activates bystander NK and Th1 effectors; restricting expression to NFAT-driven release contains systemic toxicity. Called the "4th-generation" CAR.

## 4. IL-7Rα (C7R) — constitutively active IL-7 signaling

- **Construct**: a chimeric IL-7Rα fragment that signals constitutively without IL-7 ligand. Co-expressed with GD2 CARs in T cells and NKT cells to drive autocrine IL-7-pathway activation.
- **Reference papers in collection**: Heczey 2017 era and follow-up. C7R-armored GD2 CARs show enhanced TSCM enrichment ex vivo and improved in-vivo persistence in xenograft NB models.

## 5. CCR2b / CXCR2 chemokine receptor co-arming

- Several preclinical 2020–2025 papers in collection co-express **CCR2b** (CCL2 receptor) or **CXCR2** (CXCL1/8 receptor) with GD2 CAR to improve infiltration into solid tumors. Rationale: NB tumors produce high CCL2 and IL-8, but unmodified T cells lack these receptors at meaningful levels.

## 6. CCL19/IL-7 secretion (7×19 cells)

- A handful of preclinical 2022–2026 papers in collection use the Adachi 7×19 architecture (T cells secreting IL-7 + CCL19) with a GD2 CAR — IL-7 maintains T cell viability, CCL19 recruits naive T cells and dendritic cells to the tumor.

## 7. PD-1 / PD-L1 modulation

### 7.1 PD-1 knockout

- Several allogeneic GD2 CAR programs (Quintarelli 2025 PMID 39815015 supplement; recent 2025–2026 preclinical papers) use CRISPR or TALEN to knock out PDCD1 (PD-1) to render CAR-T resistant to PD-L1-mediated suppression.

### 7.2 PD-1/CD28 chimeric receptor

- Several preclinical papers in collection co-express a PD-1 extracellular / CD28 intracellular chimera that converts the inhibitory signal into a costimulatory one.

### 7.3 PD-L1 dominant-negative

- Preclinical 2024–2026 papers use a soluble PD-1-Fc decoy or a dominant-negative PD-1 lacking the ITSM motif to mop up PD-L1 without delivering an inhibitory signal.

## 8. Trade-offs noted across armored designs

| Armoring | Persistence | Activity | Toxicity risk | Notes |
| --- | --- | --- | --- | --- |
| Constitutive IL-15 (GD2-CAR.15 NKT) | ++ | ++ | Hyperleukocytosis at high doses (Tian 2025) | Add iCasp9 safety switch |
| RD-IL15 superagonist (NK-92) | ++ | ++ | Auto-proliferation in absence of IL-2 | NK-92 line is irradiated before infusion, capping self-replication |
| NFAT-IL18 (Glienke 2022) | + | +++ | Lower — IL-18 only secreted in tumor | Adds complexity to vector design |
| C7R | ++ | + | Auto-proliferation in absence of IL-7 | Constitutively active — no off switch beyond suicide gene |
| CCR2b / CXCR2 | n/c | ++ in tumor-localized contexts | Low | Useful in tumors with high chemokine gradients |
| 7×19 (IL-7 + CCL19) | ++ | ++ | Moderate (recruits bystander cells) | Original Adachi data was in CD19 CAR |
| PD-1 KO | + | ++ | Loss of physiologic checkpoint | Important for allogeneic / multi-knockout products |

## 9. Cytokine support during expansion (vs in-construct armoring)

It is worth distinguishing **product armoring** (cytokine encoded in the CAR cassette and expressed by the engineered cell) from **manufacturing-only support** (cytokine added to the culture medium but not into the construct). The latter is described in detail in `04_manufacturing.md`. Briefly:

- IL-2 (Heczey 2014, 2017 cohort 1; Quintarelli 2018) — used during expansion only.
- IL-7 + IL-15 (Heczey 2017 cohorts 2/3; Quintarelli 2018; Mount 2018; Glienke 2022; Majzner 2022; Monje 2025) — current default for both T cells and NKT cells.
- IL-21 — sometimes used during preclinical expansion to maintain stem-cell-memory.
- Dasatinib (Majzner 2022 / Monje 2025) — used to suppress tonic signaling during the transduction window, not as a cytokine per se.
